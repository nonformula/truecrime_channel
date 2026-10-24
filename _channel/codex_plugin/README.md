# True Crime Channel for Codex — 3.2.1

Codex adaptation of the supplied `true-crime-channel.plugin` v3.2.0. Preserves all 11 skills, the v3.2 editorial workflow, evidence contracts, native Drive outputs, producer approvals, pre-script and separate temp-VO stages. The original Claude package is unchanged.

## Install

This directory is a local Codex marketplace. From the repository root, run:

```sh
codex plugin marketplace add ./_channel/codex_plugin
codex plugin add true-crime-channel@radley-true-crime-codex
```

Restart the client or open a new conversation to load the installed skills. In supported desktop clients, select the Radley marketplace in the Plugins directory and install True Crime Channel. Disable another installed version of this workflow before using the new one to avoid duplicate skill selection.

To move it to another machine, extract `true-crime-channel-codex.zip` into a folder, keeping the hidden `.agents` and `.codex-plugin` directories. Register the extracted folder with `codex plugin marketplace add /absolute/path/to/extracted-folder`, then run the same plugin-add command. The ZIP is a distribution of a marketplace, not a promise that a client accepts direct ZIP upload.

Google Drive must be connected separately, with access to the case and creation/edit permissions for native Docs and Sheets. Codex CLI needs a suitable configured MCP connection if connected app tools are unavailable. ElevenLabs MCP plus the channel's stock voice is required for temp VO; an authorized Mapbox execution path is required for maps. Credentials, connectors and media engines are not bundled. Missing capabilities produce explicit pending work, never fabricated completion.

## Use

Natural language selects matching skills. Explicit examples:

- `$case-ingest Ingest this case: [Drive folder link].`
- `$case-process Resume C001 from its saved Case Record.`
- `$case-verify Verify the timeline and prepare selects for C001.`
- `$case-prescript Write the pre-script for C001.`
- `$case-script Expand the approved pre-script into the full script.`
- `$case-tempvo Generate temp narration for the approved script.`

Also included: case-brief, case-spine, case-opening-test, case-production and true-crime-format. A client may display plugin-qualified skill names. Existing Drive IDs, approvals and case state remain authoritative across platforms.

## Maintain and validate

Edit `src/skills/*/SKILL.md`, `src/shared/*.md` and manifests under `src/`, then run:

```sh
python3 _channel/codex_plugin/build.py
```

The build validates manifests, all 11 skills, local reference and sibling routing paths, marketplace resolution and ZIP contents. It generates `true-crime-channel/` and the distributable ZIP. Each installed skill includes all shared references so it remains self-contained. `provenance.json` records the exact original archive hash. Build and validation do not touch live case files or the user's installed configuration.

Packaging follows [official OpenAI plugin documentation](https://developers.openai.com/plugins/build/plugins): a portable root manifest, supported Codex compatibility overlay and local marketplace. Installation is tested with the local Codex CLI in an isolated temporary configuration; live Drive and paid media operations require their configured services and have not been executed by this conversion.
