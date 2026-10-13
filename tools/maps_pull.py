#!/usr/bin/env python3
"""Geocode a case's locations and pull sample maps from Mapbox with your token.

Reads   cases/<case>/04_locations.csv   (rows written by Claude during /ingest)
Writes  lat, lon, geocode_confidence back into that CSV
Saves   media:/Cases/<case>/07_visuals/maps/samples/
          C001_L03_city.png, C001_L03_neighborhood.png, C001_L03_street.png (public only)
          C001_route_L01-L02.png   (for each pair in case.yaml `routes:` or --route)
          C001_overview.png        (every plotted location)

Privacy rules (from the workflow):
  public             → city, neighborhood, street samples
  private_residence  → city + neighborhood only, never street level
  uninvolved_party   → not geocoded, not plotted

Usage:
  python3 tools/maps_pull.py C001
  python3 tools/maps_pull.py C001 --route L01>L02 --route L02>L03 --driving
  python3 tools/maps_pull.py C001 --dry-run          # show what would happen, no API calls
  python3 tools/maps_pull.py C001 --force            # re-pull existing samples
Requires MAPBOX_TOKEN in .env. Mapbox/OpenStreetMap attribution is kept on every image.
"""
from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path
from urllib.parse import quote

import requests

from common import CHANNEL, REPO, case_dir, case_media_dir, config, die, load_yaml, read_csv, write_csv

API = "https://api.mapbox.com"
SKIP = "uninvolved_party"
PRIVATE = "private_residence"


def redact(url: str) -> str:
    return url.split("access_token=")[0] + "access_token=***" if "access_token=" in url else url


class Mapbox:
    def __init__(self, token: str | None, dry: bool):
        self.token, self.dry = token, dry
        self.s = requests.Session()

    def get(self, url: str) -> requests.Response | None:
        full = f"{url}{'&' if '?' in url else '?'}access_token={self.token or ''}"
        if self.dry:
            print(f"    GET {redact(full)}")
            return None
        for attempt in range(3):
            r = self.s.get(full, timeout=30)
            if r.status_code == 429:  # rate limited
                time.sleep(2 ** attempt)
                continue
            return r
        return r

    def geocode(self, query: str, country: str | None) -> tuple[float, float, str] | None:
        url = f"{API}/search/geocode/v6/forward?q={quote(query)}&limit=1"
        if country:
            url += f"&country={country}"
        r = self.get(url)
        if r is None:
            return None
        if r.status_code != 200:
            print(f"    geocode failed ({r.status_code}): {r.text[:120]}")
            return None
        feats = r.json().get("features", [])
        if not feats:
            return None
        lon, lat = feats[0]["geometry"]["coordinates"]
        conf = (feats[0].get("properties", {}).get("match_code") or {}).get("confidence", "unrated")
        return lat, lon, conf

    def driving_polyline(self, a: tuple[float, float], b: tuple[float, float]) -> str | None:
        url = (f"{API}/directions/v5/mapbox/driving/{a[1]},{a[0]};{b[1]},{b[0]}"
               f"?geometries=polyline&overview=simplified")
        r = self.get(url)
        if r is None or r.status_code != 200:
            return None
        routes = r.json().get("routes", [])
        return routes[0]["geometry"] if routes else None

    def static(self, style: str, overlay: str, view: str, size: str, out: Path) -> bool:
        st = load_yaml(CHANNEL / "map_styles.yaml")
        q = f"attribution={str(st.get('attribution', True)).lower()}&logo={str(st.get('logo', True)).lower()}"
        url = f"{API}/styles/v1/{style}/static/{overlay}/{view}/{size}?{q}"
        r = self.get(url)
        if r is None:
            return True
        if r.status_code != 200 or not r.headers.get("content-type", "").startswith("image"):
            print(f"    static map failed ({r.status_code}): {r.text[:160]}")
            return False
        out.write_bytes(r.content)
        return True


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("case_id")
    ap.add_argument("--route", action="append", default=[], help="pair like L01>L02 (repeatable)")
    ap.add_argument("--driving", action="store_true", help="draw routes along roads (Directions API)")
    ap.add_argument("--style", default=None, help="style key from map_styles.yaml")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-geocode", action="store_true", help="only pull maps for rows that have lat/lon")
    a = ap.parse_args()

    token = os.environ.get("MAPBOX_TOKEN")
    if not token and not a.dry_run:
        die("MAPBOX_TOKEN missing. Add it to .env (see .env.example).")

    cdir = case_dir(a.case_id)
    case = load_yaml(cdir / "case.yaml")
    st = load_yaml(CHANNEL / "map_styles.yaml")
    style_key = a.style or st.get("default_style", "dark")
    style = f"{st.get('username', 'mapbox')}/{st['styles'][style_key]}"
    w, h = st.get("size", {}).get("width", 1280), st.get("size", {}).get("height", 720)
    size = f"{min(w,1280)}x{min(h,1280)}{'@2x' if st.get('size', {}).get('retina', True) else ''}"
    zooms = st.get("zooms", {"city": 11, "neighborhood": 14.5, "street": 17})
    mk, rt = st.get("marker", {}), st.get("route", {})
    pin = lambda lat, lon: f"pin-{mk.get('size','l')}+{mk.get('color','e0262b')}({lon:.6f},{lat:.6f})"

    out_dir = (case_media_dir(a.case_id, required=not a.dry_run) or Path("/dev/null")) / "07_visuals/maps/samples"
    if not a.dry_run:
        out_dir.mkdir(parents=True, exist_ok=True)

    loc_csv = cdir / "04_locations.csv"
    fields, rows = read_csv(loc_csv)
    if not rows:
        die(f"{loc_csv.relative_to(REPO)} has no locations yet. Run /ingest first.")
    mb = Mapbox(token, a.dry_run)
    country = case.get("geocode_country") or config().get("maps", {}).get("geocode_country")
    low = set(config().get("maps", {}).get("low_confidence", ["low", "medium"]))

    flagged, pulled, skipped = [], 0, []
    plotted: dict[str, tuple[float, float]] = {}
    for row in rows:
        lid, privacy = row["location_id"], (row.get("privacy") or "").strip()
        if privacy == SKIP:
            skipped.append(lid)
            continue
        if not (row.get("lat") and row.get("lon")) and not a.no_geocode:
            query = row.get("address_or_place") or row.get("name")
            print(f"{lid} geocode: {query}")
            g = mb.geocode(query, country)
            if g:
                row["lat"], row["lon"], row["geocode_confidence"] = f"{g[0]:.6f}", f"{g[1]:.6f}", g[2]
            elif not a.dry_run:
                row["geocode_confidence"] = "not_found"
        if not (row.get("lat") and row.get("lon")):
            if not a.dry_run:
                flagged.append(f"{lid} not found")
            continue
        lat, lon = float(row["lat"]), float(row["lon"])
        plotted[lid] = (lat, lon)
        if row.get("geocode_confidence") in low | {"unrated"}:
            flagged.append(f"{lid} confidence={row['geocode_confidence']}")

        levels = ["city", "neighborhood"] + ([] if privacy == PRIVATE else ["street"])
        for lvl in levels:
            out = out_dir / f"{a.case_id}_{lid}_{lvl}.png"
            if out.exists() and not a.force:
                continue
            print(f"{lid} sample: {lvl}")
            if mb.static(style, pin(lat, lon), f"{lon:.6f},{lat:.6f},{zooms[lvl]},0", size, out):
                pulled += 1

    if not a.dry_run:
        write_csv(loc_csv, fields, rows)

    # routes
    pairs = [tuple(p) for p in case.get("routes", []) or []]
    pairs += [tuple(r.split(">")) for r in a.route]
    for src, dst in pairs:
        if src not in plotted or dst not in plotted:
            print(f"route {src}>{dst}: skipped (location missing or not plotted)")
            continue
        out = out_dir / f"{a.case_id}_route_{src}-{dst}.png"
        if out.exists() and not a.force:
            continue
        A, B = plotted[src], plotted[dst]
        poly = mb.driving_polyline(A, B) if a.driving else None
        if poly:
            path = f"path-{rt.get('width',4)}+{rt.get('color','e0262b')}-{rt.get('opacity',0.9)}({quote(poly, safe='')})"
        else:
            line = {"type": "Feature", "properties": {"stroke": f"#{rt.get('color','e0262b')}",
                    "stroke-width": rt.get("width", 4), "stroke-opacity": rt.get("opacity", 0.9)},
                    "geometry": {"type": "LineString", "coordinates": [[A[1], A[0]], [B[1], B[0]]]}}
            path = f"geojson({quote(json.dumps(line, separators=(',', ':')), safe='')})"
        print(f"route {src}>{dst}{' (driving)' if poly else ' (straight line)'}")
        if mb.static(style, f"{path},{pin(*A)},{pin(*B)}", "auto", size, out):
            pulled += 1

    # overview
    if plotted:
        out = out_dir / f"{a.case_id}_overview.png"
        if a.force or not out.exists():
            print("overview")
            if mb.static(style, ",".join(pin(*ll) for ll in plotted.values()), "auto", size, out):
                pulled += 1

    print(f"\n{'(dry run) ' if a.dry_run else ''}samples pulled: {pulled}  ->  {out_dir}")
    if skipped:
        print(f"not plotted (uninvolved_party): {', '.join(skipped)}")
    if flagged:
        print("needs human check before use:")
        for f in flagged:
            print(f"  {f}")
    print("reminder: set verified=Y in 04_locations.csv only after checking each key location against research.")


if __name__ == "__main__":
    main()
