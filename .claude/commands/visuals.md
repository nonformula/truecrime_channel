---
description: "Stage 6: visual plan and shot specs"
argument-hint: <CASE_ID> [notes]
---

Case: **$ARGUMENTS** (first token is the case ID, e.g. C001; anything after is extra instruction).

Before starting: read `CLAUDE.md` and `STATUS.md`. Resolve the case folder as `cases/<CASE_ID>_*` (repo) and `media:/Cases/<same folder name>/` (the local media copy in `_media/`). Run `python3 tools/media.py pull <CASE_ID>` first so the local copy has Drive's latest transcripts, research and outputs (no video). If the repo case folder is missing, or the pull fails, stop and say so.

For every row in `07_visuals/visual_index.csv`:

- **Maps:** start from `04_locations.csv` and the approved samples. Write a spec (area, points, labels, routes, zoom, style from `_channel/map_styles.yaml`, animation notes for Google Earth Studio). Apply the location privacy rules.
- **Graphics / exhibit cards / ledger states:** spec the content and the template from `_channel/gfx_templates/README.md`.
- **Recreations:** create `07_visuals/recreations/R###/shot.yaml` from `_channel/templates/shot.yaml` with lens, exact duration from `vo_timing.csv` + handles, script lines, location, grounding source, reference images, HUD values (only sourced values), and a completed rules_check. Write `prompt.md` with the still and i2v prompts built from the lens fragment + `_channel/prompt_library/`. Create `takes_log.csv` from the template. **Do not spec any recreation without a grounding source and a reference image.**

Set status `Visuals`.

When done: Run `python3 tools/media.py push <CASE_ID>` so every new or changed media file (transcripts, maps, VO, stills, takes, PDFs) is on Drive, then `python3 tools/media.py status <CASE_ID>` and report anything still not pushed. Update `_channel/master_case_index.csv` (status, last_updated) and add a handoff note to `STATUS.md`. **This is an approval gate.** Summarize what needs review in 3–6 bullets, then stop and wait. After approval, suggest the commit message `<CASE_ID> visual plan approved`.
