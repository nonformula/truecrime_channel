# True Crime Channel: standing context for Claude

Read this at the start of every session. The full workflow lives in `docs/TrueCrime_Workflow_v2.md`.

## What this repo is

The working files for Radley's true crime YouTube channel. One folder per case under `cases/`. Episodes follow the **Chain of Custody** format (`_channel/format_chain_of_custody.md`) and are **VO-first**: the narration script leads, the edit follows.

## Where things live

- **This repo (git):** text only. Briefs, timelines, scripts, indexes (CSV), shot specs, prompts, timing files, tools.
- **Google Drive (`media:/`):** all media AND all transcripts. Footage, `.srt` transcripts, research PDFs, reference images, recreation stills/takes, temp + final VO, edit exports.
- **Ci:** the archive of record. Media is pulled from Ci into Drive per case.
- `media:/` resolves to `MEDIA_ROOT` (see `_channel/config.yaml`, overridable in `_channel/config.local.yaml` or the `MEDIA_ROOT` env var). Case media is at `media:/Cases/<CASE_FOLDER>/`.
- Never copy media or transcripts into this repo. Never commit `.env`.

## Stages (slash commands)

`/ingest` → `/brief` ◆ → `/spine` ◆ → `/script` ◆ → `/tempvo` → `/visuals` ◆ → `/recreate` ◆ → `/animatic` ◆ → `/finalvo` → `/publish-check` ◆

◆ = human approval gate. Stop at a gate and wait for approval. After approval, suggest a commit message like `C001 brief approved`.

## Non-negotiable rules

1. **Source everything.** Every factual claim traces to a transcript timestamp or a research file. Unsourced = `[UNVERIFIED]`. Never invent times, events, quotes or dialogue.
2. **Quotes are verbatim** from transcripts.
3. **Recreation rules** (full list in `docs/` §9): grounded in a source + real reference image, disclosed, faceless by default, POV never imitates police footage, documented actions only, **no depiction of the crime or a victim's final moments**, never imply the person recorded it.
4. **Location rules:** private residences at neighborhood level only, no uninvolved parties plotted, geocodes are verified by a person.
5. **Temp AI VO is never published.** Files prefixed `TEMP_`.
6. **Line IDs are permanent** once a script is locked (`VO_041`, new lines `VO_041a`).
7. Never rename source files after indexing.
8. End on the victim, never the perpetrator.

## Naming

- Case folder: `C###_Surname_Keyword` (e.g. `C001_Wilson_Darkhorse`)
- Recreation take: `C###_R###_T##.mp4`
- Sample map: `C###_L##_<zoom>.png`
- Visual IDs: `R###` recreation, `G###` graphic, `M###` map, `E###` exhibit card
- Asset IDs: `A###`

## Tools (`tools/`, run with `python3 tools/<name>.py`)

| Tool | Status |
|---|---|
| `new_case.py` | ready |
| `transcribe.py` | ready (needs `mlx-whisper` or `whisperx` + ffmpeg) |
| `maps_pull.py` | ready (needs `MAPBOX_TOKEN` in `.env`) |
| `vo_temp.py`, `shotlist.py` | stub: build after the first locked script |
| `validate.py` | stub: build before the first Stage 10 |
| `gen_batch.py` | stub: build after the pilot |

If a stub is needed before it's built, do that stage's work by hand following the stage command, and keep the same file names and formats.

## Session habits

- One stage per session. Read `STATUS.md` first; update it last.
- Update `_channel/master_case_index.csv` whenever a case changes status.
- Writing style for anything a viewer hears or reads: calm, precise, non-sensational. Follow `_channel/narrator_voice_guide.md`.
