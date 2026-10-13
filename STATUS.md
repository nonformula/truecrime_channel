# STATUS

Last updated: 2026-10-12

## In flight

| Case | Stage | Next action | Blocked on |
|---|---|---|---|
| C001 DARKHORSE | Not started | Run `new_case.py`, copy media from Ci to the Drive case folder, `/ingest C001` | rclone `gdrive` remote + Mapbox token |

## Repo setup checklist

- [ ] Repo moved to a non-iCloud folder and pushed to private GitHub
- [ ] `brew install rclone`, `rclone config` (remote named `gdrive`), `python3 tools/media.py check` passes
- [ ] `.env` with `MAPBOX_TOKEN` (ElevenLabs key later, for Stage 5)
- [ ] `_channel/map_styles.yaml` filled with your Mapbox Studio style IDs
- [ ] Transcription engine installed and tested on one clip

## Handoff notes

(Add a short note here at the end of each session: what was done, what's next.)
