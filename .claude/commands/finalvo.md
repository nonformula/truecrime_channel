---
description: "Stage 9: narrator record script and final VO drop-in"
argument-hint: <CASE_ID> [notes]
---

Case: **$ARGUMENTS** (first token is the case ID, e.g. C001; anything after is extra instruction).

Before starting: read `CLAUDE.md` and `STATUS.md`. Resolve the case folder as `cases/<CASE_ID>_*` (repo) and `media:/Cases/<same folder name>/` (Drive, via `media_root` in `_channel/config.local.yaml` or `_channel/config.yaml`). If either is missing, stop and say so.

1. Produce `media:/…/09_edit/record_script.pdf` (or a markdown version if PDF tooling is unavailable): every VO line with its ID, tense mark, pronunciation notes for names and places, and chapter breaks.
2. After recording, check `media:/…/08_vo/final/` has a `VO_###.wav` for every line. List missing or extra files.
3. Re-measure durations into `vo_timing.csv`. Flag any visual whose lines changed by more than its handles.

When done: update `_channel/master_case_index.csv` (status, last_updated) and add a handoff note to `STATUS.md`. Suggest the commit message `<CASE_ID> final VO in`.
