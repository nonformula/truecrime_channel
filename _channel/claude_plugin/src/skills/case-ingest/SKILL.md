---
name: case-ingest
description: "Index or incrementally update a true-crime case in Google Drive and create the v3 research package. Use for ingest, start a case, or add new case material."
---

# Case ingest — stage 1

Read `references/rules.md`, `references/drive-workspace.md`, `references/data-contract.md` and `references/gates.md` before working on a case. These references are bundled with this skill. 
## Execute
1. Resolve the case folder, check available read/write tools and inspect the current Case Record. Existing case: resume or incrementally update by default. Ask only for ambiguous case identity or conflicting scope.
2. Enumerate all source files recursively with pagination. Exclude `_production`. Log every file in Assets, including untranscribed recordings and excluded imagery. Preserve file-to-ID mappings. Report concise inventory counts before a long read.
3. Pair transcripts, record source versions and queue missing/ambiguous transcripts. Read in batches with coverage checkpoints. Extract prospective moments with source timestamps; label duration estimates and unverified speaker attribution. Do not claim a visual discovery from text alone.
4. Read research originals with precise page/range citations. Create Evidence entries, Events, People and Locations. Preserve conflicts, date precision, clock uncertainty, allegation attribution and unknown police-knowledge time. Keep excluded sources as leads or inventory only.
5. Create/update the five initial Drive outputs in the data contract. The chronology is a Sheet, not a competing narrative Doc. Add the readable narrative summary to the Research & Ingest Report. Include strongest prospective authentic moments and the most consequential missing checks.
6. Read back outputs, update the Case Record last, and record complete versus partial coverage accurately. An unread central source means ingest may be draft_complete with a coverage blocker; verification is not approved.

## Return
Link the five current outputs, summarize important coverage/source flags, and state that stage 2 verifies chronology and selects. Never launch media downloads, transcription or maps without an available, authorized execution path. No case facts from general knowledge.
