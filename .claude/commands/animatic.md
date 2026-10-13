---
description: "Stage 8: animatic edit list"
argument-hint: <CASE_ID> [notes]
---

Case: **$ARGUMENTS** (first token is the case ID, e.g. C001; anything after is extra instruction).

Before starting: read `CLAUDE.md` and `STATUS.md`. Resolve the case folder as `cases/<CASE_ID>_*` (repo) and `media:/Cases/<same folder name>/` (Drive, via `media_root` in `_channel/config.local.yaml` or `_channel/config.yaml`). If either is missing, stop and say so.

If `tools/shotlist.py --edl` is built, run it. Otherwise write `09_edit/shotlist.csv` by hand: one row per VO line or picture beat in script order, with start/end from `vo_timing.csv`, the VO file, the picture source (footage in/out, approved take or still, graphic placeholder), and on-screen text (ledger, exhibit, HUD citation).

Then list what's missing for a complete animatic. Editor notes go back as line IDs or visual IDs, not timeline positions.

When done: update `_channel/master_case_index.csv` (status, last_updated) and add a handoff note to `STATUS.md`. **This is an approval gate.** Summarize what needs review in 3–6 bullets, then stop and wait. After approval, suggest the commit message `<CASE_ID> animatic reviewed`.
