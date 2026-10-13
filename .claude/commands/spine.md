---
description: "Stage 3: Chain of Custody outline"
argument-hint: <CASE_ID> [notes]
---

Case: **$ARGUMENTS** (first token is the case ID, e.g. C001; anything after is extra instruction).

Before starting: read `CLAUDE.md` and `STATUS.md`. Resolve the case folder as `cases/<CASE_ID>_*` (repo) and `media:/Cases/<same folder name>/` (the local media copy in `_media/`). Run `python3 tools/media.py pull <CASE_ID>` first so the local copy has Drive's latest transcripts, research and outputs (no video). If the repo case folder is missing, or the pull fails, stop and say so.

Draft `05_script/outline_v1.md` from the approved brief, on `_channel/format_chain_of_custody.md`, for the runtime in `case.yaml`.

For every beat: narration purpose, retention reason, the open question it carries out of the chapter (chapter ends), and what carries the picture: `[FOOTAGE: A### @ mm:ss–mm:ss]`, `[GRAPHIC]`, `[MAP: L##]`, `[EXHIBIT]`, or `[RECREATION: candidate + lens]`. Mark every `[LEDGER]` update. Mark beats with no footage. Strongest real footage inside the first 90 seconds. End on the victim. Estimate minutes per chapter and total.

Set status `Spined`.

When done: Run `python3 tools/media.py push <CASE_ID>` so every new or changed media file (transcripts, maps, VO, stills, takes, PDFs) is on Drive, then `python3 tools/media.py status <CASE_ID>` and report anything still not pushed. Update `_channel/master_case_index.csv` (status, last_updated) and add a handoff note to `STATUS.md`. **This is an approval gate.** Summarize what needs review in 3–6 bullets, then stop and wait. After approval, suggest the commit message `<CASE_ID> spine approved`.
