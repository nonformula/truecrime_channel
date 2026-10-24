# True Crime Channel — v3.2.0

A Drive-based production workflow for Radley's trusted team, aligned with `TrueCrime_Content_Creation_System_v3.2.md` and the decision to keep current case documents in Drive. The private repo maintains this plugin; producers work in their case's `_production` folder. No full-library desktop download is required.

## Start
Install the package using your host's supported plugin installation flow. Connect Google Drive/Docs/Sheets with access to the case and permission to create/edit its production outputs. Stage 6b needs an ElevenLabs MCP connection with the channel's stock voice; stage 7 maps need a Mapbox execution path with the project key. This package does not supply credentials or connectors. If a host only offers read access, the workflow reports unsaved drafts instead of claiming Drive writes. Installation availability depends on your host/account; this archive has not been live-install tested.

Try:
- “Ingest this case: [Drive folder link].”
- “Verify the timeline and prepare the strongest selects for C001.”
- “Write the brief for C001.”
- “Build the story spine and opening-five-minutes paper edit.”
- “Write the pre-script for C001.”
- “Expand the approved pre-script into the full script.”
- “Generate temp VO for the approved C001 script.”
- “Resume C001 from its saved case record.”

Ingest creates five native Drive files: Case Record; Source & Evidence Index; Chronology; People & Locations; Research & Ingest Report. Later skills add selects, brief, spine, opening test, pre-script, script and production plan. Existing IDs/approvals survive incremental updates. Current file links live in the Case Record.

## What changed in v3.2
- **Stage 5b pre-script** (`case-prescript`): a beat-organized Doc with visuals, VO intent, verbatim sound bites and function per beat, approved before the full script.
- **Storytelling devices**: analysis, audience question, foreshadowing, emphasis, connect the dots and the spoken knowledge ledger, used in combination.
- **Stage 6 split**: 6a full script (`case-script`) expands the approved pre-script; 6b temp VO (`case-tempvo`) runs through ElevenLabs via MCP only after script approval.
- **Runtime** 15–30 minutes (from v3.1).
- **Maps** (from v3.1): Mapbox, single black and white dark style, 2048 × 1152, saved to the production `MAPS/` folder, skipped locations logged.
- New `Pre-Scripted` case stage value and `C###_08B_PRE_SCRIPT` document.

## Scope
Stage procedures cover all twelve stages plus 5b/6a/6b. Later media stages run only when their tools, inputs and approvals exist; otherwise the plugin delivers an explicit handoff. It includes no transcription/generation/editing engine, cloud worker or unattended service. Actual source verification, assembled-film review, human final VO and clearance decisions are never fabricated. Original case records, not pilot examples, establish facts.

## Maintaining
Source lives in `_channel/claude_plugin/src/`. Edit `src/shared/` references and `src/skills/*/SKILL.md`, then run `python3 _channel/claude_plugin/build.py`. The build copies every shared reference into each skill's `references/` so each skill installs self-contained, validates manifest, frontmatter and reference links, and writes `_channel/claude_plugin/true-crime-channel.plugin`. Do not edit the generated archive by hand. Previous archives are kept in `_channel/claude_plugin/_archive/` for rollback; disable the old installed version to avoid conflicting rules. Building never touches live Drive files.
