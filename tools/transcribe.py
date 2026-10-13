#!/usr/bin/env python3
"""Transcribe any video/audio in a case's Drive 01_assets/ that has no paired transcript.

Writes <basename>.srt next to each file (same folder, same basename). Skips files that already
have a .srt or .vtt. Engine: mlx-whisper on Apple Silicon (recommended) or whisperx.

Usage:
  python3 tools/transcribe.py C001              # transcribe what's missing
  python3 tools/transcribe.py C001 --list       # only list what's missing
  python3 tools/transcribe.py C001 --engine whisperx
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from common import case_media_dir, config, die


def srt_time(t: float) -> str:
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def write_srt(segments: list[dict], out: Path) -> None:
    lines = []
    n = 0
    for seg in segments:
        text = (seg.get("text") or "").strip()
        if not text:
            continue
        n += 1
        lines += [str(n), f"{srt_time(seg['start'])} --> {srt_time(seg['end'])}", text, ""]
    tmp = out.with_suffix(".srt.part")
    tmp.write_text("\n".join(lines))
    tmp.rename(out)  # atomic-ish so a half-written file never looks finished


def pick_engine(requested: str) -> str:
    def has(mod: str) -> bool:
        try:
            __import__(mod)
            return True
        except ImportError:
            return False

    if requested == "mlx":
        return "mlx" if has("mlx_whisper") else die("mlx-whisper not installed: pip install mlx-whisper")
    if requested == "whisperx":
        return "whisperx" if has("whisperx") else die("whisperx not installed: pip install whisperx")
    if has("mlx_whisper"):
        return "mlx"
    if has("whisperx"):
        return "whisperx"
    die("no transcription engine found. On Apple Silicon: pip install mlx-whisper")


def transcribe(path: Path, engine: str, tcfg: dict) -> list[dict]:
    lang = tcfg.get("language") or None
    if engine == "mlx":
        import mlx_whisper
        res = mlx_whisper.transcribe(str(path), path_or_hf_repo=tcfg.get("mlx_model"), language=lang)
        return res.get("segments", [])
    import whisperx
    model = whisperx.load_model(tcfg.get("whisperx_model", "large-v3"), "cpu", compute_type="int8", language=lang)
    audio = whisperx.load_audio(str(path))
    return model.transcribe(audio).get("segments", [])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("case_id")
    ap.add_argument("--engine", default=None, choices=["auto", "mlx", "whisperx"])
    ap.add_argument("--list", action="store_true", help="list missing transcripts and exit")
    a = ap.parse_args()

    tcfg = config().get("transcription", {})
    exts = {e.lower() for e in tcfg.get("video_ext", []) + tcfg.get("audio_ext", [])}
    assets = case_media_dir(a.case_id) / "01_assets"
    if not assets.exists():
        die(f"missing {assets}")

    files = sorted(p for p in assets.rglob("*") if p.is_file() and p.suffix.lower() in exts)
    missing = [p for p in files if not (p.with_suffix(".srt").exists() or p.with_suffix(".vtt").exists())]

    print(f"{len(files)} media files, {len(files) - len(missing)} already transcribed, {len(missing)} missing")
    for p in missing:
        print(f"  missing: {p.relative_to(assets)}")
    if a.list or not missing:
        return

    if not shutil.which("ffmpeg"):
        die("ffmpeg not found: brew install ffmpeg")
    engine = pick_engine(a.engine or tcfg.get("engine", "auto"))
    print(f"engine: {engine}")

    failed = []
    for i, p in enumerate(missing, 1):
        print(f"[{i}/{len(missing)}] {p.relative_to(assets)} …", flush=True)
        try:
            write_srt(transcribe(p, engine, tcfg), p.with_suffix(".srt"))
        except Exception as e:  # keep going; report at the end
            failed.append((p, e))
            print(f"    failed: {e}")
    print(f"done: {len(missing) - len(failed)} written, {len(failed)} failed")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
