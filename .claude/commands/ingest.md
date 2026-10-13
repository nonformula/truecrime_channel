---
description: "Stage 1: ingest, index, timeline, locations and sample maps"
argument-hint: <CASE_ID> [notes]
---

Case: **$ARGUMENTS** (first token is the case ID, e.g. C001; anything after is extra instruction).

Before starting: read `CLAUDE.md` and `STATUS.md`. Resolve the case folder as `cases/<CASE_ID>_*` (repo) and `media:/Cases/<same folder name>/` (Drive, via `media_root` in `_channel/config.local.yaml` or `_channel/config.yaml`). If either is missing, stop and say so.

1. Run `python3 tools/transcribe.py <CASE_ID>` to transcribe any video/audio in `media:/…/01_assets/` that has no paired `.srt`/`.vtt`. If the engine isn't installed, report which files lack transcripts and continue with the ones that have them.
2. Read every transcript (on Drive) and research file. For each asset, add a row to `06_asset_index.csv` (asset_id A###, filename, source_type from its subfolder, transcript_file, duration, 3–6 key_moments as `mm:ss description` drawn only from the transcript, rights_status `Needs Clearance` unless proven otherwise, source_origin, notes).
3. Build `04_timeline.md`: one chronological account, every event tagged with `A### @ mm:ss` or a research ref, plus its location_id. List contradictions between sources in their own section. Never invent times or events.
4. **Locations:** extract every location the transcripts and research name (addresses, businesses, venues, roads, airports, cities) into `04_locations.csv`. Assign `L01…`, set type, events, sources (no source = don't list it), and privacy (`public` / `private_residence` / `uninvolved_party`). Leave lat/lon blank.
5. Add the location pairs the timeline connects (movement between places) to `routes:` in `case.yaml`, then run `python3 tools/maps_pull.py <CASE_ID> --driving` to geocode and pull sample maps (use no `--driving` for flights or non-road moves). Report locations flagged low-confidence and any skipped for privacy.
6. Set case status to `Indexed`.

When done: update `_channel/master_case_index.csv` (status, last_updated) and add a handoff note to `STATUS.md`. Suggest the commit message `<CASE_ID> ingested`.
