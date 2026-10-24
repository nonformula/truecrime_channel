# STATUS

Last updated: 2026-10-23

## In flight

| Case | Stage | Next action | Blocked on |
|---|---|---|---|
| C001 DARKHORSE (Moriah Wilson) | Cold open in edit (local `cases/MO_WILSON/edit/`, v7) | Record case stage in the plugin's Drive Case Record | — |

## Repo housekeeping

- [x] Repo on private GitHub
- [x] Claude plugin rebuilt for v3.2 (11 skills); Codex plugin 3.2.1
- [x] v2 stage commands retired to `_archive/v2_stage_commands/`
- [ ] Install the v3.2.0 `.plugin` and disable the installed v3.0.0
- [ ] Update `_channel/channel_bible.md`, `format_chain_of_custody.md` and `narrator_voice_guide.md` to v3.2 (§12 migration table)
- [ ] Decide whether `_channel/templates/`, `_channel/lenses/` and `new_case.py` still have a role now that case records live in Drive
- [ ] Update `maps_pull.py` and `map_styles.yaml` to the v3.2 map spec (B&W dark, 2048 × 1152, `_production/MAPS/`)
- [ ] Move the Mapbox token out of `cases/MO_WILSON/maps/*.sh|.command` into `.env`, then commit them
- [ ] `_channel/master_case_index.csv` is empty; fill it or retire it in favour of the Drive Case Records

## Handoff notes

- 2026-10-23: Plugin rebuilt to v3.2; repo cleanup (junk files, duplicate v2.4 doc, `vo_temp.py` stub replaced by ElevenLabs MCP, v2 commands archived); CLAUDE.md and README refreshed for the plugin-based workflow.
