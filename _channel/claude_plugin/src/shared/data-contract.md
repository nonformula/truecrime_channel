# Case documents and schemas

Use native Google Docs and Sheets in the case's `_production` folder. On first creation use the names below; preserve existing document IDs during later updates. Adapt existing legacy outputs without destructive restructuring. C### is the case ID; system version is 3.2.0, independent of document revision.

## Initial ingest outputs: five files
1. `C###_00_CASE_RECORD` — Doc.
2. `C###_01_SOURCE_EVIDENCE_INDEX` — Sheet with Assets, Evidence, Coverage, Change Log tabs.
3. `C###_02_CHRONOLOGY` — Sheet with Events and Conflicts tabs.
4. `C###_03_PEOPLE_LOCATIONS` — Sheet with People and Locations tabs.
5. `C###_04_RESEARCH_INGEST_REPORT` — Doc.

The next stages add `C###_05_SELECTS` (Sheet), `C###_06_CASE_BRIEF` (Doc), `C###_07_STORY_SPINE` (Sheet: Beats, Knowledge States, Act Timing), `C###_08_OPENING_TEST` (Doc), `C###_08B_PRE_SCRIPT` (Doc, stage 5b), `C###_09_SCRIPT` (Doc) and `C###_10_PRODUCTION_PLAN` (Sheet: Visuals, Sequence, VO, Reviews). Create later files only when that stage needs them. Media and exports are linked in the Case Record rather than embedded in these sheets. Generated maps go to the `MAPS/` subfolder of the case production folder; temp narration goes to a `08_vo/temp/` subfolder. The legacy CASE_BRIEF filename number need not change.

## Case Record
Include case ID and source-folder ID/link; title; workflow version; owner/current editor; last updated; requested scope; target/measured runtime; current stage; status; exact current artifact IDs/links/revisions; source coverage; unresolved blockers/owners; next action; approved editorial exceptions; and checkpoint (processed sources and pending work).

Stage history: stage | status | output revision(s) | date | by | decision | reopened dependencies. Status values: not_started, in_progress, draft_complete, awaiting_review, approved, blocked, needs_recheck. Case stage values: Backlog → Indexed → Verified → Briefed → Spined → Opening Tested → Pre-Scripted → Scripted → Planned → Assembled → Final VO → Cleared → Published. Use the signed-in actor only if known; otherwise record approval received from current user, identity unspecified. Never invent reviewer identity. An approved brief is not a cleared episode. Release/publication requires a real record.

## Tables (minimum fields)
- Assets: asset_id (A###), drive_file_id, original_name/path/link, source_revision, source_type, library_id, paired_transcript_id/revision, duration_value, duration_basis, source_origin, acquisition_status, use_status, clearance_basis/link, restrictions, notes. Include every inventoried file, even untranscribed or excluded material; research files can have A IDs too.
- Evidence: evidence_id (EVD_###), asset_id, page_or_source_in/out, original_timecode/frame_rate, checked_excerpt/summary, claim_supported, speaker/attribution, transcript_revision, verification_status, verification_method/by/date, acquisition_status, use_status, outstanding_checks. Use status separately from truth/verification. Legacy R## references map to exact source passages without deleting old refs.
- Coverage: source_id/revision, read_status, read_ranges, pending_ranges, pairing_status, errors, last_checkpoint.
- Events: event_id (EVT_###), event_time_or_interval, precision, timezone, original_clock, verified_offset_and_source, location_ids, person_ids, description, evidence_ids, police_knowledge_time, knowledge_evidence_ids, conflicts, verification_status. Unknown values remain explicit.
- Conflicts: conflict_id, event/claim, competing_evidence, consequence, resolution/status, owner.
- People: person_id (PER_###), name, role_at_time, relationships, attributed_statements, event_ids, evidence_ids, uncertainties.
- Locations: location_id (L###), source_wording, name/type, event_ids, evidence_ids, privacy, coordinates_if_verified, coordinate_source, verification, permitted_display_precision, map_status, map_files, skip_reason. No inferred literal route.
- Selects: select_id (SEL_###), asset_id, evidence_ids, source_in/out, verified_excerpt, source_context, discontinuities, picture_observation, unique_purpose, linked_beats, verification/use_status. Separate transcript-proposed selects from checked audiovisual selects.
- Beats: beat_id (B_###), act, story_question, audience_learns, new_development, evidence_ids, select_ids, picture/audio, estimated_duration_s, reveal_order, human_context, devices, ledger_moment, outstanding_checks.
- Knowledge States: state_id (K_###), beat/segment_ids, police_as_of, police_statement, knowledge_evidence_ids, audience_shown_statement, audience_evidence_ids, show_reason, display_interval.
- Act Timing: act_id, purpose, estimated_s, measured_s, density/repetition_notes.
- Visuals: visual_id (G###/R###), category, beat/segment_ids, purpose, grounding_evidence_ids, reference_ids, brief, labels, planned/measured_s, handles, source_in/out, use/production_status, approved_take, review_revision.
- Sequence: segment_id (SEG_###), beat_id, record_in/out, picture_id/source_in/out, audio_layers/source_in/out, vo_id, overlap/hold/transition, evidence_ids, timing_basis.
- VO: vo_id (VO_###), text_revision, take_link, temporary_or_final, tts_voice/model (temp only), measured_duration, pronunciation, status.
- Reviews: review_id, stage, artifact_revision, issue, owner, severity/blocking, decision, reviewed_by/date.

Acquisition: needed / requested / received. Use: pending / approved / restricted / excluded. Verification: unreviewed / verified / disputed / unsupported. IDs are permanent; new IDs append, removed IDs are retired. Version corrections never silently change what an old ID denotes.

Five linked narrative datasets are Events, Evidence, People, Beats and Visuals. Other tabs support their provenance and operation. Do not create a second unsynchronized copy of these records inside a local repo.

## Pre-script (stage 5b)
One readable Doc organized by episode beat, in reveal order. Header: case ID, source spine and opening-test revisions, DEVELOPMENT DRAFT label while checks remain. Each beat block:
- **Beat** — beat ID, act and a short title.
- **Visuals** — what the audience sees: asset, select or visual ID where one exists; plain description where not yet.
- **Voice over** — narration intent and, where already clear, the draft line. Name the device when it is not obvious. Write `(no VO — authentic sound)` where the beat carries itself.
- **Sound bites** — verbatim checked excerpts with speaker, source asset/EVD and in/out.
- **Function** — story question, what changes, what it hands to the next beat.
- **Checks** — any line whose support is open, written as a check, not as copy.

Mark knowledge-ledger moments as their own block with known / supported / unresolved lines and EVD links. Do not spec camera treatment, transitions or durations beyond what reading the beat needs.

## Ingest report
Summarize coverage and limits; research findings with citations; strongest prospective authentic moments; missing transcripts/records; contradictions; unread/truncated files; rights/use exclusions; locations needing review; and prioritized next checks. Distinguish promising material from verified findings. End with the next useful production action, not a claim that ingest completed fact-checking.
