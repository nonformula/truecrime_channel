#!/usr/bin/env python3
"""Scaffold a new case: repo folder (text) + matching Google Drive folder (media), plus a master index row.

Usage:
  python3 tools/new_case.py C001 Wilson Darkhorse --title "DARKHORSE"
  python3 tools/new_case.py C002 Doe TrafficStop --no-media     # repo only (Drive not available)
"""
from __future__ import annotations

import argparse
import re

from common import (CASE_ID_RE, CASES, CHANNEL, TEMPLATES, config, die, media_root,
                    read_csv, today, write_csv)

REPO_LAYOUT = {
    "": ["case.yaml", "00_case_brief.md", "02_research_notes.md", "03_rights.md",
         "04_timeline.md", "04_locations.csv", "06_asset_index.csv"],
    "05_script": ["script_v1.md"],
    "07_visuals": ["visual_index.csv", "ledger.csv"],
    "07_visuals/recreations": [],
    "08_vo": ["vo_timing.csv"],
    "09_edit": [],
    "10_publish": [],
}

MEDIA_LAYOUT = [
    "01_assets/bodycam", "01_assets/interrogation", "01_assets/news",
    "01_assets/surveillance", "01_assets/audio_911",
    "02_research/reference_images", "03_rights",
    "07_visuals/maps/samples", "07_visuals/maps/final", "07_visuals/graphics",
    "07_visuals/recreations", "08_vo/temp", "08_vo/final", "09_edit",
]

PART_RE = re.compile(r"^[A-Za-z0-9]+$")


def fill(text: str, values: dict) -> str:
    for k, v in values.items():
        text = text.replace("{" + k + "}", v)
    return text


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("case_id", help="C### (e.g. C001)")
    ap.add_argument("surname", help="key surname, letters/numbers only (e.g. Wilson)")
    ap.add_argument("keyword", help="short keyword, letters/numbers only (e.g. Darkhorse)")
    ap.add_argument("--title", default=None, help="working title (default: keyword)")
    ap.add_argument("--priority", default="2", choices=["1", "2", "3"])
    ap.add_argument("--no-media", action="store_true", help="skip creating the Google Drive folder")
    a = ap.parse_args()

    if not CASE_ID_RE.match(a.case_id):
        die("case id must look like C001")
    for part in (a.surname, a.keyword):
        if not PART_RE.match(part):
            die(f"{part!r}: use letters and numbers only (no spaces or underscores)")
    if list(CASES.glob(f"{a.case_id}_*")):
        die(f"{a.case_id} already exists")

    folder = f"{a.case_id}_{a.surname}_{a.keyword}"
    title = a.title or a.keyword
    values = {"CASE_ID": a.case_id, "CASE_FOLDER": folder, "TITLE": title}

    # Drive first, so a missing Drive path fails before anything is written.
    mdir = None
    if not a.no_media:
        root = media_root(required=True)
        mdir = root / config().get("cases_dir_media", "Cases") / folder
        if mdir.exists():
            die(f"Drive folder already exists: {mdir}")

    cdir = CASES / folder
    for sub, files in REPO_LAYOUT.items():
        d = cdir / sub
        d.mkdir(parents=True, exist_ok=True)
        if not files:
            (d / ".gitkeep").touch()
        for name in files:
            src = TEMPLATES / name
            (d / name).write_text(fill(src.read_text(), values))

    if mdir is not None:
        for sub in MEDIA_LAYOUT:
            (mdir / sub).mkdir(parents=True, exist_ok=True)

    idx = CHANNEL / "master_case_index.csv"
    fields, rows = read_csv(idx)
    rows.append({
        "case_id": a.case_id, "case_folder": folder, "working_title": title,
        "status": "Backlog", "priority": a.priority, "transcripts_done": "N",
        "final_vo": "Not booked", "last_updated": today(),
    })
    write_csv(idx, fields, rows)

    print(f"created repo case:  {cdir.relative_to(CASES.parent)}")
    print(f"created Drive case: {mdir}" if mdir else "Drive folder skipped (--no-media)")
    print("next: pull media from Ci into the Drive 01_assets/ folders, mark the Drive case folder")
    print(f"      'Available offline', then run /ingest {a.case_id} in Claude Code.")


if __name__ == "__main__":
    main()
