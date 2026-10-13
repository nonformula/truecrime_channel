#!/usr/bin/env python3
"""On-demand Google Drive access with rclone. Nothing syncs in the background.

Drive is the source of truth. A case's media is pulled into the repo's git-ignored _media/
folder only when you ask, and new outputs are pushed back when you ask.

SAFETY: this tool only ever ADDS or UPDATES files on Drive (rclone copy). It never deletes,
moves or syncs anything on Drive. `clear` only deletes your local copy.

Usage:
  python3 tools/media.py check                      # rclone installed + Drive reachable?
  python3 tools/media.py pull C001                  # transcripts, research, images, maps, VO, takes (no video)
  python3 tools/media.py pull C001 --for-transcribe # + only the video/audio that has no transcript yet
  python3 tools/media.py pull C001 --video          # + all video/audio (big)
  python3 tools/media.py pull C001 --only 01_assets/bodycam/bodycam_01.mp4
  python3 tools/media.py push C001                  # copy new/changed local files up to Drive
  python3 tools/media.py push C001 --dry-run
  python3 tools/media.py status C001                # what's local but not yet on Drive
  python3 tools/media.py clear C001 --video-only    # free space: remove local video/audio (if pushed)
  python3 tools/media.py clear C001                 # remove the whole local copy (if pushed)
  python3 tools/media.py ls C001 [01_assets]        # list files on Drive (nothing downloaded)
  python3 tools/media.py mkdirs C001                # create the case's folder tree on Drive
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from common import case_dir, config, die, media_root

# Only these rclone subcommands are ever run. No sync, move, delete, purge, rmdir.
ALLOWED = {"copy", "lsf", "mkdir", "check", "listremotes", "version"}  # lsf: listing only


def mcfg() -> dict:
    m = config().get("media", {})
    if m.get("mode", "rclone") != "rclone":
        die("media.mode is not 'rclone' in _channel/config.yaml; this tool isn't needed in mount mode.")
    return m


def rclone(args: list[str], capture: bool = False, check: bool = True) -> subprocess.CompletedProcess:
    if args[0] not in ALLOWED:
        die(f"refusing to run rclone {args[0]} (not on the safe list)")
    if not shutil.which("rclone"):
        die("rclone not installed: brew install rclone, then: rclone config  (see README)")
    cmd = ["rclone", *args]
    r = subprocess.run(cmd, text=True, capture_output=capture)
    if check and r.returncode not in (0,):
        if capture:
            sys.stderr.write(r.stderr)
        die(f"rclone {args[0]} failed (exit {r.returncode})")
    return r


def media_exts() -> set[str]:
    t = config().get("transcription", {})
    return {e.lower() for e in t.get("video_ext", []) + t.get("audio_ext", [])}


def remote_case(case_id: str) -> str:
    m = mcfg()
    return f"{m['rclone_remote']}:{m.get('remote_root', '').strip('/')}/{config().get('cases_dir_media', 'Cases')}/{case_dir(case_id).name}"


def local_case(case_id: str) -> Path:
    d = media_root(required=False) / config().get("cases_dir_media", "Cases") / case_dir(case_id).name
    d.mkdir(parents=True, exist_ok=True)
    return d


def exclude_media_flags() -> list[str]:
    flags = []
    for e in sorted(media_exts()):
        flags += ["--exclude", f"*{e}", "--exclude", f"*{e.upper()}"]
    return flags


COMMON = ["--exclude", "*.part", "--exclude", ".DS_Store", "--exclude", "*.srt.part"]


def cmd_check(_a) -> None:
    m = mcfg()
    print(rclone(["version"], capture=True).stdout.splitlines()[0])
    remotes = rclone(["listremotes"], capture=True).stdout.split()
    name = f"{m['rclone_remote']}:"
    if name not in remotes:
        die(f"rclone remote '{m['rclone_remote']}' not configured. Run: rclone config  (name it {m['rclone_remote']})")
    root = f"{name}{m.get('remote_root', '').strip('/')}"
    r = rclone(["lsf", root, "--max-depth", "1", "--dirs-only"], capture=True, check=False)
    if r.returncode != 0:
        die(f"can't read {root}. Check remote_root in _channel/config.yaml.\n{r.stderr.strip()}")
    print(f"Drive OK: {root}")
    print("  " + (", ".join(r.stdout.split()) or "(empty)"))
    print(f"local cache: {media_root(required=False)}")


def cmd_pull(a) -> None:
    src, dst = remote_case(a.case_id), local_case(a.case_id)
    if a.only:
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
            f.write("\n".join(a.only) + "\n")
        rclone(["copy", src, str(dst), "--files-from", f.name, "--progress"])
        print(f"pulled {len(a.only)} file(s) -> {dst}")
        return
    print(f"pulling text, images and outputs (no video/audio) from {src}\n(never overwrites a local file that is newer than Drive)")
    rclone(["copy", src, str(dst), *COMMON, *exclude_media_flags(), "--update", "--create-empty-src-dirs", "--progress"])
    if a.video:
        print("pulling all video/audio (this can be large)")
        rclone(["copy", src + "/01_assets", str(dst / "01_assets"), *COMMON, "--update", "--progress"])
    elif a.for_transcribe:
        listing = rclone(["lsf", src + "/01_assets", "-R", "--files-only"], capture=True).stdout.split("\n")
        files = {p for p in listing if p}
        exts = media_exts()
        need = [p for p in sorted(files) if Path(p).suffix.lower() in exts
                and str(Path(p).with_suffix(".srt")) not in files and str(Path(p).with_suffix(".vtt")) not in files]
        if not need:
            print("every video/audio file already has a transcript on Drive")
        else:
            print(f"pulling {len(need)} file(s) that need transcripts")
            with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
                f.write("\n".join(need) + "\n")
            rclone(["copy", src + "/01_assets", str(dst / "01_assets"), "--files-from", f.name, "--progress"])
    print(f"local copy: {dst}")


def unpushed(case_id: str) -> list[str]:
    src, dst = local_case(case_id), remote_case(case_id)
    r = rclone(["check", str(src), dst, "--one-way", "--size-only", *COMMON,
                "--missing-on-dst", "-", "--differ", "-"], capture=True, check=False)
    return sorted({ln.strip() for ln in r.stdout.splitlines() if ln.strip()})


def cmd_push(a) -> None:
    src, dst = local_case(a.case_id), remote_case(a.case_id)
    args = ["copy", str(src), dst, *COMMON, "--update", "--create-empty-src-dirs", "--progress"]
    if a.dry_run:
        args.append("--dry-run")
    print(f"pushing new/changed files to {dst} (never deletes on Drive; skips files newer on Drive)")
    rclone(args)
    if not a.dry_run:
        left = unpushed(a.case_id)
        print("all local files are on Drive" if not left else
              f"{len(left)} file(s) still differ: Drive has a newer version (a teammate's edit?). "
              f"Run pull to get it, or resolve by hand:")
        for p in left[:30]:
            print(f"  {p}")


def cmd_status(a) -> None:
    left = unpushed(a.case_id)
    if not left:
        print("nothing to push: every local file is on Drive")
        return
    print(f"{len(left)} local file(s) not on Drive or different from Drive (run: python3 tools/media.py push {a.case_id}):")
    for p in left:
        print(f"  {p}")


def cmd_clear(a) -> None:
    d = local_case(a.case_id)
    root = media_root(required=False).resolve()
    if root not in d.resolve().parents:
        die(f"refusing to delete outside the local cache: {d}")
    left = unpushed(a.case_id)
    exts = media_exts()
    if a.video_only:
        left = [p for p in left if Path(p).suffix.lower() in exts]
    if left and not a.force:
        die(f"{len(left)} local file(s) are missing from Drive or differ from it. Push (or pull) first, "
            f"or use --force to discard the local copies:\n  "
            + "\n  ".join(left[:20]))
    if a.video_only:
        n = 0
        for p in d.rglob("*"):
            if p.is_file() and p.suffix.lower() in exts:
                p.unlink()
                n += 1
        print(f"removed {n} local video/audio file(s); transcripts and everything else kept")
    else:
        shutil.rmtree(d)
        print(f"removed local copy {d} (Drive untouched)")


def cmd_ls(a) -> None:
    base = remote_case(a.case_id) + (f"/{a.sub.strip('/')}" if a.sub else "")
    out = rclone(["lsf", base, "-R", "--files-only", "--format", "sp", "--separator", "\t"], capture=True).stdout
    for ln in out.splitlines():
        size, path = ln.split("\t", 1)
        print(f"{int(size) / 1e6:10.1f} MB  {path}")


def cmd_mkdirs(a) -> None:
    from new_case import MEDIA_LAYOUT
    base = remote_case(a.case_id)
    for sub in MEDIA_LAYOUT:
        rclone(["mkdir", f"{base}/{sub}"])
    print(f"created folder tree on Drive: {base}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    p = sub.add_parser("pull"); p.add_argument("case_id")
    g = p.add_mutually_exclusive_group()
    g.add_argument("--video", action="store_true")
    g.add_argument("--for-transcribe", action="store_true")
    g.add_argument("--only", nargs="+", metavar="PATH", help="paths relative to the case folder")
    p = sub.add_parser("push"); p.add_argument("case_id"); p.add_argument("--dry-run", action="store_true")
    p = sub.add_parser("status"); p.add_argument("case_id")
    p = sub.add_parser("clear"); p.add_argument("case_id")
    p.add_argument("--video-only", action="store_true"); p.add_argument("--force", action="store_true")
    p = sub.add_parser("ls"); p.add_argument("case_id"); p.add_argument("sub", nargs="?")
    p = sub.add_parser("mkdirs"); p.add_argument("case_id")
    a = ap.parse_args()
    {"check": cmd_check, "pull": cmd_pull, "push": cmd_push, "status": cmd_status,
     "clear": cmd_clear, "ls": cmd_ls, "mkdirs": cmd_mkdirs}[a.cmd](a)


if __name__ == "__main__":
    main()
