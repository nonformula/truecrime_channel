# Script and edit timing

The full script (stage 6a) expands the approved pre-script: carry its VO lines and sound bites forward, then add exact footage references and visual element IDs. Represent one sequence segment per block. The script can live in a Google Doc with readable field labels; do not assume a local parser exists. Use the IDs and production-plan tables from the data contract.

Required fields:
- Segment ID / beat ID / act / purpose.
- Picture: category, source asset or visual ID, exact original in/out if a clip, label if recreated.
- Audio: original source and in/out; checked quotation or description; designed sound separately.
- VO: optional permanent VO_### and text. No narrator is needed for a self-explanatory recording.
- Evidence: exact EVD IDs for each factual VO claim, quoted audio and factual screen text. Retain attribution/context.
- Event time; police-knowledge date where relevant; knowledge state if useful.
- Duration: estimate or measured; record in/out when assembled; overlaps, transitions and intentional holds.
- Open checks and verification/use status.

Use explicit (no VO) for authentic moments. Quoted source audio is not a request for TTS. Keep discontinuous interview excerpts as separate segments. Do not rewrite quotes to fit time. Label scripts with open facts DEVELOPMENT DRAFT; no unresolved placeholder may silently become a factual line.

Legacy [FOOTAGE], [AUDIO], [GRAPHIC], [RECREATION], [LEDGER] and optional [EXHIBIT] cues may aid reading. A [BEAT n] is an intentional sequence hold, not extra seconds automatically added to a running clip.

Total duration is the final sequence endpoint after overlaps/transitions. Do not add source audio + VO + picture lengths when they play simultaneously. Separate estimate from measurement; never fabricate timing from a word count. Word counts may yield explicitly labeled VO estimates pending a read.

Preserve SEG/VO IDs when reordered. Append new IDs or VO suffixes; retire removed IDs. Temp files have TEMP_ prefixes, VO ID in the filename and revision metadata, e.g. `TEMP_C001_VO_041_r2.mp3`. Final human takes link to matching VO IDs. Changed take duration flags affected segments and visuals for review; handles are not a guarantee.
