# Codex runtime

Use the installed sibling skills and bundled references as the workflow authority. Invoke with natural language or `$case-process`, `$case-prescript`, `$case-script`, etc.; plugin-qualified skill names may be shown by the client. Do not rely on Claude slash commands, Claude-specific tools, or repository-local paths on another machine.

## Connected tools
Discover the available Google Drive plugin tools and read applicable Google Drive, Docs and Sheets skills when present. Where tools are deferred, use the host tool-discovery facility (for example `ALL_TOOLS` in a functions runtime); inspect actual schemas before calling. A Codex CLI installation may instead expose Drive through a configured MCP server. Do not invent connector IDs, MCP URLs, credentials or tool names. This plugin bundles instructions, not a Drive connection.

Confirm read and write capabilities against the requested case. Follow `drive-workspace.md` for scope, pagination, native outputs and read-back. A local shell or repository checkout does not imply Google Drive access. If connection or permissions are missing, report the exact missing capability and prepare useful drafts with unsaved status; do not claim synchronization.

## Media and execution
Discover ElevenLabs MCP tools for temp VO and inspect the configured stock voice before authorized generation. Use an available, authorized Mapbox execution path for maps. An installed skill is not an installed media tool. Preserve source-verification requirements and producer review gates.

Use the current Codex sandbox, network and approval rules. Keep keys in configured secret storage or environment variables; never put values in documents, prompts or the plugin. Do not install services or alter user configuration merely to complete a stage. Respect prior authorization for ordinary case-output writes.

Persist progress in the Drive Case Record and report actual completed versus pending work. A session ending does not leave an unattended worker running. Do not use agent spawning as a substitute for missing tools or human review.
