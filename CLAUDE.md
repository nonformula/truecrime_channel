# True Crime Channel: standing context for Claude

Read this at the start of every session. The production standard is `system/md/TrueCrime_Content_Creation_System_v3.2.md`. Older versions in `system/md/_archive/` are history only; never follow them.

## What this repo is

The maintenance home for Radley's true crime channel: the production system document, the Claude and Codex plugins that run it, channel config, tools and the styleguide. Episodes are **evidence-led** (not VO-first): verify sources and select authentic moments, brief, spine, test the opening, pre-script, then script.

## Where things live

- **Google Drive:** current case documents (native Docs/Sheets in each case's `_production` folder, created by the plugin), plus all media and transcripts. Drive is the record for case work; do not create a second unsynchronized copy of case records in this repo.
- **This repo (git):** text only. System docs, plugin source, channel config, tools, styleguide, presentation decks.
- **Ci:** the archive of record. Media is copied from Ci into Drive per case.
- **`cases/MO_WILSON/`** is a local editing working copy (footage, AFX, edit exports, gfx). Everything in it except text is git-ignored. It predates the `C###_Surname_Keyword` convention.
- `tools/media.py` (rclone) pulls a case from Drive into `_media/` and pushes outputs back. It only adds or updates files on Drive. Never run rclone yourself with sync, move, delete or purge.
- Never commit media, transcripts, `.env` or API tokens. `.gitignore` covers media by extension (upper and lower case); check `git status` before committing.

## Running stages

Stages run through the **true-crime-channel plugin** skills, not repo slash commands (the v2 commands are in `_archive/v2_stage_commands/`).

| Stage | Skill |
|---|---|
| 1 Ingest | `case-ingest` |
| 2 Verify + selects ◆ | `case-verify` |
| 3 Brief ◆ | `case-brief` |
| 4 Spine ◆ | `case-spine` |
| 5 Opening test ◆ | `case-opening-test` |
| 5b Pre-script ◆ | `case-prescript` |
| 6a Full script ◆ | `case-script` |
| 6b Temp VO (ElevenLabs MCP) | `case-tempvo` |
| 7–12 Visuals → release ◆ | `case-production` |
| Any / resume | `case-process`; format questions: `true-crime-format` |

◆ = human approval gate. Stop at a gate and wait for approval.

## Editing the plugins

- Claude plugin: edit `_channel/claude_plugin/src/` (shared references in `src/shared/`, one `SKILL.md` per skill), then `python3 _channel/claude_plugin/build.py`. It writes `true-crime-channel.plugin`; never hand-edit the archive. Old builds go in `_channel/claude_plugin/_archive/`.
- Codex plugin: `_channel/codex_plugin/src/`, then `python3 _channel/codex_plugin/build.py` (generates `true-crime-channel/` and the zip).
- Keep both plugins in step when the system document changes. Bump the version in each manifest.

## Non-negotiable rules (from v3.2)

1. **Source everything.** Every factual claim resolves to an exact page or recording timecode. Unsourced stays `[UNVERIFIED]`. Never invent times, events, quotes, motives or dialogue.
2. **Quotes are verbatim** and checked against the recording, with context preserved. Never splice separate moments into one exchange.
3. **Source policy:** no personal/family photographs, news clips or outside archival imagery in the episode, thumbnail or cutdowns. Acquisition is not permission to use.
4. **Recreations:** grounded in evidence plus real references, visibly labeled, faceless by default, never styled like police/surveillance footage, no depiction of the killing or victim's final moments, no fabricated documents.
5. **Locations:** private residences at neighborhood level only, no uninvolved parties, geocodes verified by a person. Maps: Mapbox, black and white dark style, 2048 × 1152.
6. **Temp AI VO is never published.** Files prefixed `TEMP_`. Final narration is human. Never clone a case participant's voice.
7. **IDs are permanent:** append new ones (`VO_041a`), retire removed ones, never renumber. Never rename indexed source files.
8. Runtime 15–30 minutes. Keep the victim present throughout and end on them, never the perpetrator.

## Tools (`tools/`, run with `python3 tools/<name>.py`)

| Tool | Status |
|---|---|
| `media.py` | ready (rclone + a `gdrive` remote) |
| `new_case.py` | ready, but builds the v2 local case tree from `_channel/templates/` |
| `transcribe.py` | ready (`mlx-whisper` or `whisperx` + ffmpeg) |
| `maps_pull.py` | ready (`MAPBOX_TOKEN` in `.env`); output size/style not yet updated to the v3.2 map spec |
| `shotlist.py`, `validate.py`, `gen_batch.py` | stubs; do the stage by hand via the plugin skill |

## Writing style

Anything a viewer hears or reads: calm, precise, non-sensational. Use the v3.2 storytelling devices (analysis, audience question, foreshadowing, emphasis, connect the dots, knowledge ledger) in combination. Reserve vivid words for moments the evidence supports. `_channel/narrator_voice_guide.md` and `_channel/channel_bible.md` are still v2 and need updating to v3.2; where they conflict, v3.2 wins.

## Session habits

- Read `STATUS.md` first; update it last.
- After a gate is approved, suggest a commit message like `C001 brief approved`.
