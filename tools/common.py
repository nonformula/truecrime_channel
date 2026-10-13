"""Shared helpers: repo paths, config, media root, case lookup."""
from __future__ import annotations

import csv
import os
import re
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CHANNEL = REPO / "_channel"
CASES = REPO / "cases"
TEMPLATES = CHANNEL / "templates"
CASE_ID_RE = re.compile(r"^C\d{3}$")

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("Missing dependency: pip install -r requirements.txt")

try:
    from dotenv import load_dotenv
    load_dotenv(REPO / ".env")
except ImportError:  # pragma: no cover
    pass


def die(msg: str, code: int = 1) -> None:
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


def load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path) as f:
        return yaml.safe_load(f) or {}


def config() -> dict:
    cfg = load_yaml(CHANNEL / "config.yaml")
    cfg.update({k: v for k, v in load_yaml(CHANNEL / "config.local.yaml").items() if v is not None})
    if os.environ.get("MEDIA_ROOT"):
        cfg["media_root"] = os.environ["MEDIA_ROOT"]
    return cfg


def media_root(required: bool = True) -> Path | None:
    root = config().get("media_root")
    if not root:
        if required:
            die("media_root not set. Copy _channel/config.local.example.yaml to "
                "_channel/config.local.yaml and set your Google Drive path (or set MEDIA_ROOT).")
        return None
    p = Path(os.path.expanduser(str(root)))
    if required and not p.exists():
        die(f"media_root does not exist: {p}\nIs Google Drive for Desktop running and signed in?")
    return p


def case_dir(case_id: str) -> Path:
    if not CASE_ID_RE.match(case_id):
        die(f"case id must look like C001, got {case_id!r}")
    hits = sorted(CASES.glob(f"{case_id}_*"))
    if not hits:
        die(f"no case folder for {case_id} in {CASES}. Run tools/new_case.py first.")
    if len(hits) > 1:
        die(f"more than one folder for {case_id}: {[h.name for h in hits]}")
    return hits[0]


def case_media_dir(case_id: str, required: bool = True) -> Path | None:
    root = media_root(required)
    if root is None:
        return None
    d = root / config().get("cases_dir_media", "Cases") / case_dir(case_id).name
    if required and not d.exists():
        die(f"Drive case folder missing: {d}")
    return d


def read_csv(path: Path) -> tuple[list[str], list[dict]]:
    with open(path, newline="") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)


def write_csv(path: Path, fields: list[str], rows: list[dict]) -> None:
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def today() -> str:
    return date.today().isoformat()
