---
description: "Stage 4: VO-first script"
argument-hint: <CASE_ID> [notes]
---

Case: **$ARGUMENTS** (first token is the case ID, e.g. C001; anything after is extra instruction).

Before starting: read `CLAUDE.md` and `STATUS.md`. Resolve the case folder as `cases/<CASE_ID>_*` (repo) and `media:/Cases/<same folder name>/` (the local media copy in `_media/`). Run `python3 tools/media.py pull <CASE_ID>` first so the local copy has Drive's latest transcripts, research and outputs (no video). If the repo case folder is missing, or the pull fails, stop and say so.

Write `05_script/script_v1.md` from the approved outline, in the block format of `_channel/templates/script_v1.md` and the voice in `_channel/narrator_voice_guide.md`.

- One `### VO_###` block per line: `tense`, `text`, `picture`, `source`, optional `ledger`, optional `note`. `text: (none)` for picture-only beats. `[BEAT n]` for silence.
- Present tense over recreations, past tense over archival.
- Every factual line has a `source`. Quotes verbatim from transcripts. Anything unsourced is marked `[UNVERIFIED]`.
- Every `[RECREATION: R###]` gets a row in `07_visuals/visual_index.csv` (status Planned, disclosure Yes). Every `[GRAPHIC: G###]`, `[MAP: M###]` and `[EXHIBIT: E###]` gets a row too.
- Every ledger entry goes into `07_visuals/ledger.csv`.
- Report: line count, estimated runtime at ~150 wpm, `[UNVERIFIED]` count.

On approval, the line IDs are locked. Set status `Scripted`.

When done: Run `python3 tools/media.py push <CASE_ID>` so every new or changed media file (transcripts, maps, VO, stills, takes, PDFs) is on Drive, then `python3 tools/media.py status <CASE_ID>` and report anything still not pushed. Update `_channel/master_case_index.csv` (status, last_updated) and add a handoff note to `STATUS.md`. **This is an approval gate.** Summarize what needs review in 3–6 bullets, then stop and wait. After approval, suggest the commit message `<CASE_ID> script locked`.
