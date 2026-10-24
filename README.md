# truecrime-channel

Radley's true crime channel. Production standard: `system/md/TrueCrime_Content_Creation_System_v3.2.md`. Rules for Claude: `CLAUDE.md`.

Case work runs through the **true-crime-channel plugin** (Claude or Codex) and lives in Google Drive. This repo maintains the system document, the plugins, channel config, tools and the styleguide.

## Setup (each machine)

1. Keep this repo **outside iCloud-synced folders**.
2. Install the plugin: `_channel/claude_plugin/true-crime-channel.plugin` for Claude, or see `_channel/codex_plugin/README.md` for Codex. Connect Google Drive/Docs/Sheets. Temp VO needs the ElevenLabs MCP connection.
3. Optional local tools (media pulls, transcription, maps):
   ```
   brew install rclone ffmpeg
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   pip install mlx-whisper        # Apple Silicon transcription (or: pip install whisperx)
   rclone config                  # new remote named gdrive, storage: drive
   python3 tools/media.py check
   ```
4. Copy `.env.example` to `.env` and add your keys. `.env` is git-ignored. Never put it on Drive or in a script.

## Work a case

Ask in natural language, for example: “Ingest this case: [Drive folder link]”, “Write the pre-script for C001”, “Resume C001”. Stages and gates are listed in `CLAUDE.md`.

## Media commands

| Command | What it does |
|---|---|
| `python3 tools/media.py pull C001` | Get transcripts, research, images and outputs (no video) |
| `python3 tools/media.py pull C001 --for-transcribe` | Plus only the video that still needs a transcript |
| `python3 tools/media.py pull C001 --only <path>` | One specific file |
| `python3 tools/media.py push C001` | Send new/changed files to Drive (never deletes on Drive) |
| `python3 tools/media.py status C001` | What's local but not on Drive yet |
| `python3 tools/media.py clear C001 --video-only` | Free space; refuses if anything isn't pushed |
| `python3 tools/media.py ls C001 01_assets` | List what's on Drive without downloading |

## Rebuild the plugins

```
python3 _channel/claude_plugin/build.py
python3 _channel/codex_plugin/build.py
```

## Layout

```
CLAUDE.md  STATUS.md  .env.example  requirements.txt
system/md/          production system document (+ _archive/ of earlier versions)
_channel/           plugins, channel config, voice/format guides, prompts, templates, decks
tools/              local automation
styleguide/         Radley 2030 styleguide
cases/              local editing working copies (media git-ignored)
_archive/           retired v2 stage commands
_media/             local media pulled from Drive (git-ignored)
```
