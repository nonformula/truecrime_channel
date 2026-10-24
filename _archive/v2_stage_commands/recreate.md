---
description: "Stage 7: generate recreations (stills, then motion)"
argument-hint: <CASE_ID> [notes]
---

Case: **$ARGUMENTS** (first token is the case ID, e.g. C001; anything after is extra instruction).

Before starting: read `CLAUDE.md` and `STATUS.md`. Resolve the case folder as `cases/<CASE_ID>_*` (repo) and `media:/Cases/<same folder name>/` (the local media copy in `_media/`). Run `python3 tools/media.py pull <CASE_ID>` first so the local copy has Drive's latest transcripts, research and outputs (no video). If the repo case folder is missing, or the pull fails, stop and say so.

For the shots named in the arguments (or all with status Planned):

- **Pass A, stills:** if `tools/gen_batch.py` is built, queue stills. Otherwise list, per shot, the exact still prompt and the reference images to attach, for manual generation in Nano Banana Pro. Stills save to `media:/…/recreations/R###/stills/C###_R###_S##.png`.
- After stills are approved (`approved_still` in shot.yaml): **Pass B, motion.** Same approach for Kling / Veo / Runway at spec duration + handles. Takes save as `C###_R###_T##.mp4` in `takes/` and every take is logged in `takes_log.csv`.
- Remind the motion team: grade per lens, and the HUD + RECONSTRUCTION tag are applied in After Effects from the template, never generated.
- Update each shot's status and `visual_index.csv`.

When done: Run `python3 tools/media.py push <CASE_ID>` so every new or changed media file (transcripts, maps, VO, stills, takes, PDFs) is on Drive, then `python3 tools/media.py status <CASE_ID>` and report anything still not pushed. Update `_channel/master_case_index.csv` (status, last_updated) and add a handoff note to `STATUS.md`. **This is an approval gate.** Summarize what needs review in 3–6 bullets, then stop and wait. After approval, suggest the commit message `<CASE_ID> recreations approved`.
