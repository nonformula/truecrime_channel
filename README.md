# truecrime-channel

Radley's true crime channel production repo. Workflow: `docs/TrueCrime_Workflow_v2.md`. Rules for Claude: `CLAUDE.md`.

## First-time setup (each machine)

1. Keep this repo **outside iCloud-synced folders** (not Desktop or Documents if iCloud Drive syncs them). Suggested: `~/Dev/truecrime-channel`.
2. Install Google Drive for Desktop and sign in. Find the channel folder path, usually:
   `~/Library/CloudStorage/GoogleDrive-<account>/My Drive/True Crime Channel`
   (or `.../Shared drives/True Crime Channel`).
3. Copy `_channel/config.local.example.yaml` to `_channel/config.local.yaml` and set `media_root` to that path.
4. Copy `.env.example` to `.env` and fill in your keys. `.env` is git-ignored. Never put it on Drive.
5. Python 3.11+:
   ```
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   pip install mlx-whisper        # Apple Silicon transcription (or: pip install whisperx)
   brew install ffmpeg
   ```
6. Open the folder in VS Code with the Claude Code extension. Stage commands appear as `/ingest`, `/brief`, etc.

## Start a case

```
python3 tools/new_case.py C001 Wilson Darkhorse --title "DARKHORSE"
```

Creates `cases/C001_Wilson_Darkhorse/` here and `Cases/C001_Wilson_Darkhorse/` on Drive, and adds a row to the master index. Then pull media from Ci into the Drive `01_assets/` folders, mark the Drive case folder **Available offline**, and run `/ingest C001` in Claude Code.

## Layout

```
CLAUDE.md  STATUS.md  .env.example  requirements.txt
.claude/commands/   one command per stage
_channel/           channel-wide config, format, voice, lenses, prompts, templates
tools/              automation
cases/              one folder per case (text only)
docs/               workflow document
```
