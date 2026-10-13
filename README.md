# truecrime-channel

Radley's true crime channel production repo. Workflow: `docs/TrueCrime_Workflow_v2.md`. Rules for Claude: `CLAUDE.md`.

## First-time setup (each machine)

Nothing syncs to your Mac. Media stays on Google Drive and is pulled per case when you need it.

1. Keep this repo **outside iCloud-synced folders**. Suggested: `~/Dev/truecrime-channel`.
2. Install tools:
   ```
   brew install rclone ffmpeg
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   pip install mlx-whisper        # Apple Silicon transcription (or: pip install whisperx)
   ```
3. Connect rclone to Google Drive (one time, opens a browser sign-in):
   ```
   rclone config
   ```
   `n` (new remote) → name: `gdrive` → storage: `drive` → leave client_id/secret blank → scope: `1` (full access) → defaults for the rest → `y` to sign in via browser → if the channel folder is on a **shared drive**, answer `y` to "Configure this as a Shared Drive" and pick it.
4. Check `_channel/config.yaml` → `media.remote_root` matches the folder's path in Drive (default `True Crime Channel`, at the top of My Drive or the shared drive). Then:
   ```
   python3 tools/media.py check
   ```
5. Copy `.env.example` to `.env` and add your Mapbox token. `.env` is git-ignored. Never put it on Drive.
6. Open the folder in VS Code with the Claude Code extension. Stage commands appear as `/ingest`, `/brief`, etc.

## Start a case

```
python3 tools/new_case.py C001 Wilson Darkhorse --title "DARKHORSE"
```

Creates `cases/C001_Wilson_Darkhorse/` here and the matching folder tree on Drive, and adds a row to the master index. Copy the case media from Ci into the Drive case folder's `01_assets/` subfolders, then run `/ingest C001` in Claude Code.

## Daily media commands

| Command | What it does |
|---|---|
| `python3 tools/media.py pull C001` | Get transcripts, research, images and outputs (no video) |
| `python3 tools/media.py pull C001 --for-transcribe` | Plus only the video that still needs a transcript |
| `python3 tools/media.py pull C001 --only 01_assets/bodycam/bodycam_01.mp4` | One specific file |
| `python3 tools/media.py push C001` | Send new/changed files to Drive (never deletes on Drive) |
| `python3 tools/media.py status C001` | What's local but not on Drive yet |
| `python3 tools/media.py clear C001 --video-only` | Free space; refuses if anything isn't pushed |
| `python3 tools/media.py ls C001 01_assets` | List what's on Drive without downloading |

Every stage command pulls at the start and pushes at the end, so day to day you rarely type these.

**If you'd rather use Google Drive for Desktop:** set `media.mode: mount` and `media_root` in `_channel/config.local.yaml`. `media.py` isn't needed in that mode.

## Layout

```
CLAUDE.md  STATUS.md  .env.example  requirements.txt
_media/             local media copy pulled from Drive (git-ignored)
.claude/commands/   one command per stage
_channel/           channel-wide config, format, voice, lenses, prompts, templates
tools/              automation
cases/              one folder per case (text only)
docs/               workflow document
```
