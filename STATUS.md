# STATUS

Last updated: 2026-10-12

## In flight

| Case | Stage | Next action | Blocked on |
|---|---|---|---|
| C001 DARKHORSE | Not started | Run `new_case.py`, pull media from Ci to Drive, `/ingest C001` | Drive path + Mapbox token in local config |

## Repo setup checklist

- [ ] Repo moved to a non-iCloud folder and pushed to private GitHub
- [ ] `_channel/config.local.yaml` with `media_root`
- [ ] `.env` with `MAPBOX_TOKEN` (ElevenLabs key later, for Stage 5)
- [ ] `_channel/map_styles.yaml` filled with your Mapbox Studio style IDs
- [ ] Transcription engine installed and tested on one clip

## Handoff notes

(Add a short note here at the end of each session: what was done, what's next.)
