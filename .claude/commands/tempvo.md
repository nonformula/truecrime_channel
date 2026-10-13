---
description: "Stage 5: temp AI VO and real durations"
argument-hint: <CASE_ID> [notes]
---

Case: **$ARGUMENTS** (first token is the case ID, e.g. C001; anything after is extra instruction).

Before starting: read `CLAUDE.md` and `STATUS.md`. Resolve the case folder as `cases/<CASE_ID>_*` (repo) and `media:/Cases/<same folder name>/` (Drive, via `media_root` in `_channel/config.local.yaml` or `_channel/config.yaml`). If either is missing, stop and say so.

If `tools/vo_temp.py` is built, run it, then `tools/shotlist.py`. Otherwise do it by hand:

1. Parse `05_script/script_v1.md` into lines. Produce `media:/…/08_vo/temp_vo_lines.txt` (one `VO_### | text` per line) so temp VO can be generated in ElevenLabs and saved as `TEMP_VO_###.wav` in `media:/…/08_vo/temp/`.
2. Once the files exist, measure durations (ffprobe) and write `08_vo/vo_timing.csv` (line_id, start_s, end_s, duration_s, type, file), honoring `[BEAT n]` and the gap in `_channel/tts/voice_config.yaml`.
3. Write each visual's `duration_s` into `visual_index.csv` from the lines it plays under.
4. Report total runtime vs target, and which chapters run long or short.

Set status `Temp VO`. Temp VO is never published.

When done: update `_channel/master_case_index.csv` (status, last_updated) and add a handoff note to `STATUS.md`. Suggest the commit message `<CASE_ID> temp VO`.
