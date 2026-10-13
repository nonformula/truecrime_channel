---
description: "Stage 10: metadata and rights gate"
argument-hint: <CASE_ID> [notes]
---

Case: **$ARGUMENTS** (first token is the case ID, e.g. C001; anything after is extra instruction).

Before starting: read `CLAUDE.md` and `STATUS.md`. Resolve the case folder as `cases/<CASE_ID>_*` (repo) and `media:/Cases/<same folder name>/` (Drive, via `media_root` in `_channel/config.local.yaml` or `_channel/config.yaml`). If either is missing, stop and say so.

1. Write `10_publish/metadata.md`: 5 titles (search-aware, nothing the video can't pay off), thumbnail concept + 3–4 words of text, a 150-word description with the hook up top and the disclosure line from `_channel/publishing_checklist.md`, 15–20 tags, chapters from exhibit breaks.
2. If `tools/validate.py` is built, run it. Otherwise check by hand and write `10_publish/rights_report.md` with:
   1. footage cues whose rights_status isn't Public Record or Licensed
   2. unsourced or `[UNVERIFIED]` lines
   3. recreations missing reference, grounding source, disclosure, or an approved take
   4. any `TEMP_` VO still referenced
   5. any recreation depicting a disputed act or a victim's final moments
   6. any map missing Mapbox/OpenStreetMap attribution or showing a private residence at street level
3. Output **GO / NO-GO** with the specific items to resolve. Walk through `_channel/publishing_checklist.md`.

When done: update `_channel/master_case_index.csv` (status, last_updated) and add a handoff note to `STATUS.md`. **This is an approval gate.** Summarize what needs review in 3–6 bullets, then stop and wait. After approval, suggest the commit message `<CASE_ID> cleared`.
