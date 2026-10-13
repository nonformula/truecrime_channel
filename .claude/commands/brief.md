---
description: "Stage 2: case brief with recreation candidates and key locations"
argument-hint: <CASE_ID> [notes]
---

Case: **$ARGUMENTS** (first token is the case ID, e.g. C001; anything after is extra instruction).

Before starting: read `CLAUDE.md` and `STATUS.md`. Resolve the case folder as `cases/<CASE_ID>_*` (repo) and `media:/Cases/<same folder name>/` (the local media copy in `_media/`). Run `python3 tools/media.py pull <CASE_ID>` first so the local copy has Drive's latest transcripts, research and outputs (no video). If the repo case folder is missing, or the pull fails, stop and say so.

Write `00_case_brief.md` (follow `_channel/templates/00_case_brief.md`), one to two pages:

1. Logline (2–3 sentences).
2. Cold-open candidate: asset + timestamp and the dramatic-irony line it enables.
3. Principals and roles.
4. The narrative question.
5. 5–6 exhibit candidates: evidence objects that can each open a chapter, each with its source.
6. Baseline candidate, if interview footage allows.
7. Lens assignments: which principal(s) get a POV lens from `_channel/lenses/` and why, based on who they were.
8. Knowledge Ledger seeds (police column vs viewer column).
9. **Recreation candidates: suggest 3–5**, using the slots in `_channel/format_chain_of_custody.md`. For each: the moment, the exhibit it serves, lens, grounding source (transcript @ timestamp or research ref), whether reference images exist in `media:/…/02_research/reference_images/`, and a pass/fail against the recreation rules in `CLAUDE.md` (documented action, faceless, no crime or victim's final moments, not presented as real footage). Rank by story value. Drop any that fail and say why.
10. **Key locations (4–8)** from `04_locations.csv`: which exhibit each supports, links to its sample maps in `media:/…/07_visuals/maps/samples/`, privacy level.
11. Footage strength and rights risk, one line each.

Write principals, lenses, the recreation candidates and key_locations into `case.yaml` marked as proposed. Set status `Briefed`.

When done: Run `python3 tools/media.py push <CASE_ID>` so every new or changed media file (transcripts, maps, VO, stills, takes, PDFs) is on Drive, then `python3 tools/media.py status <CASE_ID>` and report anything still not pushed. Update `_channel/master_case_index.csv` (status, last_updated) and add a handoff note to `STATUS.md`. **This is an approval gate.** Summarize what needs review in 3–6 bullets, then stop and wait. After approval, suggest the commit message `<CASE_ID> brief approved`.
