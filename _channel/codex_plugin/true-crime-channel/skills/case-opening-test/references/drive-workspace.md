# Drive workspace and reliable updates

## Authority and capability check
Use the connected Drive/Docs/Sheets tools actually available in this host. Inspect their schemas and applicable host instructions; do not assume tool names, query syntax, Markdown-to-Doc conversion or content editing capabilities. Check once per session: list/search with pagination, source reading/export, folder creation, native Doc/Sheet creation, content/range editing, parent placement and read-back. Reuse existing authorizations; the user's requested stage authorizes its normal case-output writes. Installation never grants library access by itself.

If essential writes are unavailable, prepare clearly labeled local/chat drafts and report exactly what remains unsaved. Never claim files exist in Drive without successful writes and read-back. Do not silently substitute local files for requested native Docs/Sheets. The producer does not need a terminal or repository.

## Locate and scope
Resolve a supplied Drive folder ID/link or a name against folder metadata. Confirm the chosen path in the progress update; ask only if matches remain ambiguous. Read only task-relevant material. Recursively enumerate children with pagination, excluding `_production` and its descendants. Keep all original source IDs/names unchanged. Do not move, rename, delete or trash source files.

Create/find the case production folder and `_archive` inside it. Match `_production` case-insensitively (the system document writes `_Production`); use the existing folder and never create a second differently-cased one. New cases use `_production`. Maps live in its `MAPS/` subfolder. Write case outputs only within `_production`; the user may explicitly authorize a separate shared register. No broad automatic Drive searches for unrelated case records.

## Current outputs
Maintain one current Case Record containing the exact Drive file IDs, links, revisions and tab names of current outputs. Discover existing records before creating duplicates. Preserve legacy C### IDs and existing source/evidence IDs. New cases: use an available shared case register; if none, propose an unused C### among the visible library cases, check before saving, and record the folder ID as the durable identity. With simultaneous runs, use one writer per case and a shared allocator or producer-assigned number; do not promise a Drive search is an atomic allocation.

Permanent source IDs map to Drive file IDs, never list order. Re-ingest is incremental by default: retain previous IDs, append new records, log modified/deleted/inaccessible sources and flag dependent claims for recheck. Do not infer deletion from an incomplete or failed scan. Preserve human corrections, decisions and approvals unless new evidence specifically invalidates them.

## Write procedure
1. Read current output and Case Record revisions; record the intended changes.
2. Recheck for changes immediately before writing; if another editor changed it, merge compatible updates or stop only the conflicting write. Avoid competing writers to the same case.
3. Prefer updating current Docs and precise Sheet ranges, preserving unrelated cells, formulas and tabs. Use native version history plus a Change Log. For structural/destructive changes, preserve a snapshot first using supported tools.
4. If content editing is unavailable, create a new complete revision. Verify its content, type, parent and link before repointing the Case Record. Then archive the prior plugin-owned revision if supported; otherwise mark it superseded and keep its link. Never delete it. Do not archive sources or producer-owned unrelated files.
5. Read back representative content plus row counts/IDs for Sheets and beginning/end content for Docs. Verify links and full intended writes. Update the Case Record last. A partial write remains incomplete and must be recoverable on retry.

Use file IDs to locate current outputs; version suffixes alone do not determine which version is approved. Stage approval records identify the exact artifact revision(s). Material changes mark those approvals stale and reopen affected downstream checks.

## Reading and verification
Pair same-folder recordings with same-basename .srt/.vtt/.txt or legacy `_TS.txt`; ambiguous pairings remain unresolved. Keep library clip IDs separately. HH:MM:SS:FF is frame-based: retain original timecode and frame rate if known, never reinterpret frames as decimal seconds. Last transcript time is an estimated transcript extent, not verified recording duration. Do not equate SPK_0 with an identified person without support.

Read transcripts/documents in manageable batches and checkpoint processed file IDs, source revisions and unread ranges. For truncated output, paginate or fetch subsequent ranges where supported. Log exactly what was not read and keep coverage partial; do not label the source fully reviewed. Resume from the checkpoint without reassigning IDs or duplicating rows.

Default to metadata, transcripts and documents. Do not bulk-download media or sync the library. Selected media may be accessed for explicitly requested verification/editing when tools support it; otherwise request an editor's source check. Missing transcripts go to a transcription queue. This package does not include a transcription engine or cloud worker.
