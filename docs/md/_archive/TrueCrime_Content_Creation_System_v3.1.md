<p class="kicker">Radley · Content Creation System · v3.1 · October 20, 2026</p>

# True Crime Channel: Content Creation System v3.1

**An evidence-driven investigative thriller, built from primary sources, with clearly labeled cinematic recreations and investigative graphics.**

The production starts with what the records establish and the authentic moments that best communicate it. The team builds a linked story, tests the opening five minutes, then develops the full cut. Narration supplies context, attribution and transitions; recordings carry decisive moments whenever the available material supports them. The person whose life was lost remains present throughout.

**Runtime:** 15–30 minutes. The evidence earns the length.

**Document scope:** This revision replaces v3 and the v2.4 specification. It incorporates *DARKHORSE — Moriah Wilson Episode: Consolidated format and editorial recommendations*. It specifies production practices and proposed tool changes; revising this document does not update existing scripts, commands, templates, media or case records. Case examples are editorial plans, not independently verified findings. Original records must support the finished episode.

## 1. What changes in v3.1

| Area | v3 | v3.1 |
|---|---|---|
| Name | Production Workflow | **Content Creation System** |
| Runtime | 20–40 minutes, 25–30 normal | **15–30 minutes** |
| Maps | Samples after source and privacy review; final builds in Mapbox Studio or Google Earth Studio | Every approved key location in `04_locations.csv` and `people.csv` is pulled from Mapbox with the project key as a black and white dark map at 2K, saved to the case `_Production/MAPS/` folder (see §8) |
| Temp VO | Generated with the script in Stage 6 | Generated through **ElevenLabs via MCP** only after the script is approved (Stage 6b) |

All other v3 rules carry forward unchanged. The v2.4 to v3 changes are listed below.

| v2.4 approach | v3 approach |
|---|---|
| VO-first; lock narration before testing the film | Evidence-led; select authentic moments, draft beats, test the opening, then develop the full script and cut |
| 40–50-minute default | 15–30-minute range (v3.1) |
| Cold open up to 2:30 | Approximately 90 seconds for DARKHORSE; establish the conflict and investigative question immediately |
| Mandatory exhibit chapters | Incident → investigation → breakthrough → pursuit → resolution; chapter count follows the case |
| Persistent Knowledge Ledger | Occasional “What police knew / What the audience has been shown” panel, dated and sourced |
| Interview baseline and behavioral interpretation | Compare statements with records; demeanor, silence and requests to leave are not proof of guilt |
| Narration covers 65–70% | No fixed narration percentage; determine the balance in the pilot assembly |
| Tense signals reconstruction | Visible labels and a distinct treatment identify reconstructions; tense serves clarity |
| Person-specific lenses and recreation quota | Purpose-specific visual treatments; generate only shots the cut needs |
| Visual duration comes from VO | Duration comes from the combined edit: recordings, narration, overlaps and intentional holds |
| Late rights gate | Acquisition, permitted use, verification and editorial restrictions tracked from intake through final review |

The local text repository, shared Drive media, transcript pairing, permanent IDs, temporary VO, human final narration and production checkpoints remain useful. The system supports an evidence-led edit.

## 2. Source policy and the four storytelling categories

### Permitted source collection

Build from police bodycam, police interviews and interrogations, court documents and exhibits, discovery, 911 calls, recorded statements and other relevant records obtained through applicable public-records processes.

**Do not use personal or family photographs, news clips, or outside archival imagery in the episode, thumbnail or promotional cutdowns.** A personal photograph remains excluded even when it appears in a court exhibit. Previously collected excluded material may remain in the archive, flagged as unavailable for production use.

Surveillance, courtroom recordings, booking images and evidence photographs are candidates only when they belong to the permitted source collection and are approved for production use. Acquisition and approval are separate fields: possession of a file does not establish permission to publish it. Record the clearance basis and any restrictions rather than automatically clearing material marked “Public Record.”

Family words documented in court records may support accurately attributed text cards or authentic courtroom audio. No new family interview or personal photograph is needed.

| Category | What it contains | What it does |
|---|---|---|
| Authentic footage | Permitted bodycam, interviews, surveillance and courtroom recordings | Lets real discoveries, exchanges and decisions carry tension |
| Authentic audio | 911, recorded interviews, witness statements and courtroom audio | Carries testimony or emotion when corresponding picture is unavailable |
| Cinematic recreations | Labeled environments, spatial reconstructions and restrained first-person views | Explains documented geography, movement and context |
| Investigative graphics | Maps, timelines, relationship charts, source excerpts, communications and comparisons | Makes evidence and its connections understandable |

Narration is a separate production audio layer. Authentic audio can play over a graphic or a labeled recreation; track both layers without counting their overlapping durations twice. Authentic material may retain its raw appearance. Graphics and cinematic images must never obscure which material is a recording and which is constructed.

## 3. The narrative engine

The repeatable structure is **cold open → incident → investigation → breakthrough → pursuit → resolution**. These are story functions, not compulsory chapter titles. Combine, expand or omit a function when the verified case requires it. Evidence cards are optional tools, not a requirement to turn every chapter into an exhibit.

For DARKHORSE, establish Kaitlin Armstrong early. Suspense comes from how investigators connected her to the evidence, why she was released, how she disappeared and how the pursuit reached her. Distinguish suspicion at the time from the later verdict.

### Each beat must earn its place

Every beat identifies a story question, what the audience learns, its supporting evidence, its most effective sound and picture, and what changes because of it. A useful progression is **setup → primary-source moment → necessary interpretation → next question**. Omit interpretation when the recording already communicates the point.

Look for a meaningful change in understanding every 30–60 seconds: a discovery, contradiction, consequence or sharper question. This is a pacing diagnostic, not a quota. Let exceptional recordings and emotional pauses breathe. An eight-minute exchange may supply only 45 essential seconds; possessing footage is not a reason to use all of it.

Avoid stating the same point in narration, a clip and a graphic. Each layer should add something. Later returns to cold-open material must supply new context or evidence.

### Keep the person present

Introduce the victim's name, relevant life context and reason for being in the story early. Distribute further biography where it gives a discovery human meaning, then return to the person in the ending. Avoid both a long early biography detour and a portrait confined to the final memorial.

### Knowledge panel

Use two explicitly defined columns:

- **What police knew — as of [verified date/time]:** knowledge supported by a record of when investigators learned it.
- **What the audience has been shown:** sourced material already revealed in this edit, including clearly identified retrospective information.

Appear only when the difference matters. Do not imply that an event's occurrence proves police knew about it then. If acquisition time is unknown, mark it unresolved internally and omit unsupported timing claims from the graphic. At capture, the panel may converge on location or identity; it must not imply the entire case was proved or every question answered.

### Narration

Use a clear, informed voice that distinguishes observation, allegation, inference and adjudicated finding. Establish whose account is being quoted. Do not interpret body language as a lie detector or present silence, refusal to answer or a request to leave as incriminating behavior. Direct attention to relevant evidence, not speculative gestures.

Use tense to keep chronology understandable. Label reconstructions visually even when the narration uses past tense. Use verbatim, checked quotations and preserve their context. Do not splice separate interview moments into an apparently continuous exchange. There is no fixed VO percentage.

## 4. Storage, naming and source integrity

| Location | Contents |
|---|---|
| Local git repository and private remote | System files, case notes, indexes, linked datasets, scripts, prompts, shot specifications, timing and review reports |
| Google Drive | Source media, paired transcripts, research records, clearance documentation, reference material, generated assets, VO, edit projects and exports |
| Ci | Original archive of record; source material is copied into the case collection |

Use a repository outside cloud-synced folders for active production. This document does not move the existing workspace. Pull only the media a stage needs into a git-ignored `_media/` cache; push new outputs after the stage. Treat `media:/Cases/C001_Wilson_Darkhorse/…` as a logical Drive path, not a local filesystem path.

The intended `media.py` behavior is copy-only: no remote deletion or moves, no silent overwrite of a teammate's changed file, and no cache clearing while local outputs remain unpushed. Surface conflicts for resolution; newer timestamps alone do not settle competing edits. Verify these behaviors in the implementation before relying on them. Mount mode may remain an optional team configuration; on-demand copying is the default.

Pair every video and audio recording with a same-basename `.srt` or `.vtt` in the same Drive folder. Preserve originals. Automated transcription is a draft: a human checks selected quotations, speaker attribution, names and timecodes against the recording. Log transcript revisions and reopen downstream claims or edits affected by a correction.

Use the same `C###_Surname_Keyword` folder in both locations. Never rename indexed source files silently. Stable IDs survive reordering: events `EVT_###`, evidence `EVD_###`, people `PER_###`, beats `B_###`, source assets `A###`, visuals `G###`/`R###`, segments `SEG_###` and narration `VO_###`. New IDs do not recycle deleted ones; retain existing VO IDs and use suffixes where needed. Recreation takes retain `[CASE]_[SHOT]_[TAKE].mp4`, for example `C001_R014_T03.mp4`.

### Working folder specification

```text
truecrime-channel/
  CLAUDE.md / agent instructions       Standing production conventions
  STATUS.md                           Cases, owners, next actions and blockers
  _channel/
    channel_bible.md
    format_chain_of_custody.md         Revised evidence-led format
    narrator_voice_guide.md
    master_case_index.csv
    config.yaml · map_styles.yaml
    lenses/ · prompt_library/ · gfx_templates/ · tts/
    publishing_checklist.md
  tools/                              Existing tools plus v3 changes in §12
  cases/C001_Wilson_Darkhorse/
    case.yaml                         Runtime, source policy, approved treatments
    00_case_brief.md
    02_research_notes.md
    03_rights.md
    04_timeline.md                     Readable view of events and conflicts
    04_data/                          events.csv · evidence.csv · people.csv
    04_locations.csv
    05_script/                        beats.csv · outline_v1.md · script_v1.md
    06_asset_index.csv
    07_visuals/                       visual_index.csv · ledger.csv
      recreations/R014/               shot.yaml · prompt.md · takes_log.csv
    08_vo/                            vo_timing.csv
    _Production/MAPS/                 Local cache of the Drive MAPS folder (git-ignored)
    09_edit/                          selects.csv · sequence_timing.csv
                                      shotlist.csv · review_notes.md · edit interchange
    10_publish/                       metadata.md · factcheck_report.md
                                      rights_report.md · release_checklist.md
```

Drive mirrors the case ID and applicable numbered folders. Under `01_assets/`, use `bodycam/`, `interrogation/`, `surveillance/`, `courtroom/` and `audio_911/`; add another permitted source type as needed. Remove `news/` from the production template. Keep research originals in `02_research/`, permissions in `03_rights/`, graphics/recreations in `07_visuals/`, generated maps in `_Production/MAPS/`, temp/final audio in `08_vo/`, and projects/exports in `09_edit/`. Excluded legacy assets stay flagged, never automatically promoted into selects.

## 5. Five connected datasets

CSV files are sufficient for the pilot. Stable IDs connect the records; a database interface can come later. Each factual claim must resolve through evidence IDs to a precise original page or recording timecode, not just another summary.

| Dataset | Required information |
|---|---|
| Events | `event_id`, event date/time or interval, precision, time zone, original clock value and any verified correction, location IDs, participants, description, supporting evidence IDs, investigator knowledge date/time and its source, unresolved conflicts |
| Evidence | `evidence_id`, source asset ID, original filename/Drive path, agency or proceeding, document page or recording in/out, transcript path and version, claim supported, attribution, verification status, acquisition status, use status, restriction and clearance reference |
| People | `person_id`, name, role at the relevant time, relationships, attributed statements, linked events and evidence |
| Narrative beats | `beat_id`, act, story question, audience learns, new development, evidence IDs, selected clips, picture/audio treatment, estimated duration, audience reveal position, outstanding checks |
| Visual assets | `visual_id`, category, linked beats/segments, source clip in/out if applicable, graphic/recreation brief, grounding evidence, references, labels, planned and measured duration, approval/use status, production status |

**Three different clocks:** event time is when something happened; knowledge time is when investigators learned it; audience time is where it is revealed in the finished episode. Never substitute one for another. Keep unknowns unknown. Check camera offsets and distinguish discovery time from time of death.

Supporting indexes serve distinct jobs:

- `06_asset_index.csv`: one row per source file, with asset ID, filename/path, origin, source type, transcript, duration, usable moments, acquisition/use status and restrictions. Evidence rows may cite different passages within the same asset.
- `09_edit/selects.csv`: select ID, asset/evidence IDs, source in/out, verified transcript excerpt, context, unique story purpose and linked beats. Preserve discontinuities between excerpts.
- `07_visuals/ledger.csv`: state ID, beat/segment ID, display in/out, column, text, relevant investigation date, supporting evidence IDs and prior state. Panel updates need not sit under narration.
- `08_vo/vo_timing.csv`: VO ID, take, measured duration and version. This measures narration only.
- `09_edit/sequence_timing.csv`: segment ID, beat ID, record in/out, picture source, audio layers, source in/out, VO ID if any and overlap/hold notes. This determines episode runtime.

Use verification statuses such as `unreviewed / verified / disputed / unsupported`; acquisition statuses `needed / requested / received`; use statuses `pending / approved / restricted / excluded`. “Verified” means the proposed claim accurately reflects the cited record, not that an allegation in that record has been independently proved.

The master case index records case ID, working title, priority, hook, owner, stage, source strength, use/rights issues, target and measured runtime, recreation count, final-VO status, blocker and update date. Suggested stages: Backlog → Indexed → Verified → Briefed → Spined → Opening Tested → Scripted → Planned → Assembled → Final VO → Cleared → Published. Published requires an actual publication record, not a passed checklist.

## 6. The twelve production stages

**◆ marks a human editorial or production checkpoint.** These are gates for producing episodes under this system, not approval requests to revise this document. Stage commands below are an interface specification; confirm or update their implementation before use. A failed gate returns the affected work to its owning stage.

### 1. Ingest and audit — `/ingest CASE`

Inventory the permitted case collection and outstanding requests. Transcribe recordings that lack paired transcripts. Index original paths and source provenance; separate acquisition from use approval and flag excluded imagery. Extract events, people and locations, preserving uncertainty. Log promising moments without treating machine transcripts as final evidence.

**Deliver:** asset index, draft evidence/events/people tables, paired transcripts, location list and source-gap list.

**Ready when:** received sources are traceable and missing or prohibited material is visible rather than assumed available.

### 2. Verify chronology and select authentic moments ◆ — `/verify CASE` *(new)*

Reconcile event times, interview dates, camera clocks, lock records, phone events, sale and travel chronology where relevant. Record when police learned each fact. Check selected quotations against recordings and log precise in/out points with context and a reason to retain them. Conflicts that affect a central claim block that claim; they need not stop unrelated work.

**Deliver:** verified working chronology, evidence status, selects and unresolved-check list.

**Gate:** the proposed hook and central connections have adequate support, or the brief explicitly narrows them to what can be supported.

### 3. Case brief ◆ — `/brief CASE`

Write a concise brief: logline, investigative question, known-suspect or discovery structure, victim's early introduction and later human context, strongest authentic moments, source gaps, key geography and runtime target. Propose only useful panel states and possible graphics/recreations. State what each recreation would explain and what evidence and reference material would support it; do not require 3–5 shots or assign every principal a POV lens.

**Deliver:** `00_case_brief.md` and updated `case.yaml`.

**Gate:** the team agrees on the question, source boundaries, human focus and feasible scope.

### 4. Linked beat sheet and story spine ◆ — `/spine CASE`

Build the narrative beats table and outline. Give every beat a new development, evidence links, best authentic sound/picture, duration estimate and remaining checks. Separate event chronology from reveal order. Distribute biography and place emotional pauses intentionally. Mark where the cold open returns with additional meaning.

**Deliver:** `beats.csv`, outline and estimated act durations.

**Gate:** the whole story is understandable; no chapter exists solely to use available footage or fill runtime.

### 5. Opening-five-minutes test ◆ — `/opening-test CASE` *(new)*

Assemble the approximately 90-second DARKHORSE hook plus the return to discovery, Mo and the evening timeline. Use selected original media, scratch or temporary narration, and simple graphics/stills. Prototype the panel, timeline, source labels, vehicle comparison and reconstruction label. Avoid costly full motion generation at this point.

Assess whether the opening makes the central question clear, establishes Mo as a person, preserves chronology and sustains momentum after the title. Try less narration where authentic sound already works. If the opening fails, revise the brief, selects or spine before expanding it.

**Deliver:** five-minute pilot assembly, measured timing, narration approach and review notes.

**Gate:** approve the narrative approach and visual language, not just an attractive teaser.

### 6a. Full source-linked script ◆ — `/script CASE`

Expand the approved spine using the tested balance of recordings and narration. Script footage-led and audio-led segments as explicitly as VO. Cite factual narration, on-screen claims, quotations and panel states. Assign stable segment and VO IDs. Never write or synthesize case-participant speech.

**Deliver:** sourced script with segment and VO IDs.

**Gate:** the full script is sourced, coherent and approved. Freeze IDs for production; wording and structure remain revisable through tracked changes. Temp VO does not start until this gate passes.

### 6b. Temporary VO — `/tempvo CASE`

Runs only on an approved script. Generate one temporary narration file per VO line through ElevenLabs via MCP, using the channel's stock production voice. Save files with the `TEMP_` prefix to `08_vo/temp/`. Narration only; never case-participant voices.

Measure the combined sequence, not the narration track alone. An authentic clip with VO over it occupies one interval. A document hold, audio-only statement or silent pause also needs explicit timing.

**Deliver:** per-line temp audio, VO timing and provisional sequence timing.

**Ready when:** every approved VO line has a measured temp take and the provisional runtime is reported against the 15–30 minute range.

### 7. Visual plan ◆ — `/visuals CASE`

Choose the clearest available treatment for each approved beat. Specify maps, timeline states, document highlights, relationships, comparisons and any needed recreations. Link each asset to its actual segment duration and grounding evidence. Separate documented reconstruction from illustrative tribute. Record references, geographic uncertainty, labels, sound treatment and planned handles.

**Deliver:** visual index, graphics briefs and recreation shot specifications.

**Gate:** each requested asset contributes information or necessary emotional context and satisfies the source policy.

### 8. Produce graphics and selected recreations ◆ — `/recreate CASE [R###…]`

Build graphics from checked records. For each approved recreation, generate and review stills first, then create motion from approved stills. Log tool/model version, prompt, settings, seed where available, source references and each take. Review continuity and whether the image introduces unsupported details. Choose an approved take.

Add labels and source references in post-production, not inside generated imagery. Generation tools and APIs are production choices to test, not fixed dependencies of the format. A manual submission/logging path is acceptable until reliable automation exists.

**Deliver:** approved graphics/takes, logs and completed labels.

**Gate:** no invented action, misleading source treatment or unsupported detail has entered the film through an image or sound effect.

### 9. Full assembly and density review ◆ — `/animatic CASE`

Assemble authentic picture/audio, temporary narration, graphics and approved recreations; clearly mark any remaining placeholders. Review the entire film against the 15–30 minute range. Diagnose developments per minute, repeated explanations, confusing jumps, unsupported implications, excessive biography blocks and recreations that merely fill time. Preserve meaningful silence and exceptional authentic exchanges.

The editor can solve problems in the cut; reconcile accepted changes back into the script, beat sheet, timing and shot specifications before approval. Retire removed IDs instead of renumbering them.

**Deliver:** full rough cut, measured act/runtime report and reconciled notes.

**Gate:** structure and pacing work. Running toward the 30-minute ceiling needs identifiable story value. Remove repetition before removing substantive evidence.

### 10. Human final VO and finishing — `/finalvo CASE` *(new interface)*

Prepare a recording script with line IDs, pronunciation, attribution and context. Record the human narrator and replace temporary reads by ID. Recalculate timing; review any affected cuts, graphics and recreations. Handles help, but do not guarantee that timing changes can be absorbed without editing.

Complete graphics, labels, color, sound and the final mix. Keep designed atmosphere distinct from authentic audio. Do not replace intelligible evidentiary words with synthetic speech.

**Deliver:** finished review export, final audio, updated sequence timing and project media inventory.

**Ready when:** there are no placeholders or temporary VO in the review export.

### 11. Factual, editorial and use review ◆ — `/publish-check CASE`

Review the actual finished export alongside the current script and source inventory. Confirm every factual statement, displayed quote, date, clock correction, evidence comparison, attributed allegation and retrospective reveal. Confirm source-use approvals, required credits, recreation/tribute labels and privacy treatments. Review portrayals of named people separately from asset clearance, with the production's designated legal reviewer where needed.

Check all picture and audio tracks, nested sequences and exported media for temp VO, excluded images, missing labels or unapproved substitutions. Automated checks catch missing data; a human checks meaning and context.

**Deliver:** fact-check report, rights/use report and an explicit go/no-go list with owners for unresolved items.

**Gate:** all release blockers are resolved. A passed script validator alone is insufficient.

### 12. Release package and archive ◆ — `/package CASE` *(new)*

Prepare title options, an evidence-based thumbnail concept, concise description, source credits, reconstruction disclosure and chapters drawn from final timings. Check promotional claims and imagery under the same policy as the episode. Review the platform's current synthetic-content disclosure controls at upload and record the choices made.

Save the approved master, captions, project, source versions, clearance records and review reports. Checkpoint the text repository and confirm shared outputs were pushed. Record publication only after the authorized release occurs. Capture lessons from the pilot for the channel templates.

**Deliver:** release-ready package and archive manifest; publication record after release.

**Gate:** the approved export and packaging match. Later substantive edits reopen the affected review gates.

## 7. Script and timing specification

v3 must represent an authentic-audio scene even when it has no narrator. Use segment blocks with optional VO IDs. The following is a schema illustration, not a factual script or executable parser guarantee; bracketed values must be replaced before production.

```yaml
segment_id: SEG_012
beat_id: B_004
purpose: Establish what this record adds to the investigation
picture:
  category: authentic_footage
  asset_id: A017
  source_in: '[verified source timecode]'
  source_out: '[verified source timecode]'
audio:
  mode: source_audio
  asset_id: A017
  transcript: '[checked verbatim excerpt]'
vo: null
evidence_ids: [EVD_023]
attribution: '[speaker and statement context]'
event_time: '[verified value, interval or unknown]'
police_knowledge_as_of: '[verified value or unknown]'
record_in: '[assembly time]'
record_out: '[assembly time]'
knowledge_state: null
checks: []
```

A narrated segment adds `vo.line_id`, `vo.text` and measured VO duration. A source-audio segment over a map links both the authentic audio asset and the graphic ID. A recreation adds its visual ID, grounding evidence and visible label. All factual picture text also needs evidence references. A silent hold has an explicit duration and purpose.

Legacy `[FOOTAGE]`, `[GRAPHIC]`, `[RECREATION]`, `[LEDGER]` and optional `[EXHIBIT]` cues may remain as readable shorthand. Add `[AUDIO]` and explicit segment timing to the parser. `[BEAT n]` means an intentional hold in the sequence; do not automatically add it again when it already lies within a playing clip.

The finished runtime is the length of the assembled sequence, including overlap decisions and transitions. Visual durations come from that sequence, with planned durations clearly distinguished from measured ones. Temporary VO is a timing aid, never a published track. Keep `TEMP_` prefixes; validate against the project inventory and the export, not filenames alone. A narrator voice clone requires written consent; case-participant voice cloning is excluded.

## 8. Maps and cinematic recreations

### Maps

Extract locations during intake. `04_locations.csv` records location ID, name, source wording, type, event/evidence links, coordinates, geocode confidence, human verification, privacy classification and permitted display precision.

Geocoding proposes a location; it does not prove it. Check key points against the records. Connect points with a literal traveled route only when evidence supports that route. Otherwise use a clearly labeled schematic connection or describe the route as unknown. Do not turn map software's suggested route into case evidence.

**Generation (v3.1).** After source, relevance and privacy review, pull every available key location from `04_locations.csv`, along with any location tied to a person in `04_data/people.csv`, from Mapbox using the project key. Generate each map in a black and white dark style at 2K resolution (2048 × 1152, 16:9) and save it to the case `_Production/MAPS/` folder on Drive (`media:/Cases/C001_Wilson_Darkhorse/_Production/MAPS/`). A location that fails review, or lacks usable coordinates, is listed in a skipped-locations log with the reason rather than silently dropped. File names follow `[CASE]_[LOCATION]_[ZOOM].png`, for example `C001_L03_neighborhood.png`.

Prepare wide and neighborhood context, then close views only for approved public locations. Show private residences at neighborhood level or as restrained stylized pins without readable house numbers or street-level views. Omit uninvolved-party locations unless their inclusion is documented, necessary and approved. Review location data before sending it to a mapping service.

Use the single approved black and white dark style recorded in `map_styles.yaml` and required provider attribution; verify current commercial-use terms before release. Store tokens in ignored local configuration. Provider map bases are production graphics inputs, not evidence of case movement or permission to use outside archival imagery.

### Recreations

1. **Give every shot a purpose.** Explain documented space, movement or context. No fixed recreation share and no minimum shot count.
2. **Ground literal claims.** Link the depicted event to evidence and the environment to approved references. A reference establishes appearance, not proof of an action. If adequate references are unavailable, use an abstract graphic or omit the shot.
3. **Distinguish illustration.** An evocative ride can be labeled “ILLUSTRATIVE TRIBUTE”; it must not assert an exact recorded route, moment or viewpoint. Support the biographical context and record that the specific scene is illustrative.
4. **Label visibly.** Use “RECONSTRUCTION” or the appropriate illustrative label throughout the shot; identify recreated screens/ads as “GRAPHIC RECREATION.” A description disclosure supplements on-screen labels.
5. **Use restrained perspectives.** Environments, objects, hands or faceless figures can explain space. Do not imply access to private thoughts, an actual personal camera, or nonexistent police footage. Avoid surveillance/bodycam styling that could be mistaken for an original recording.
6. **Invent no evidentiary behavior.** No synthetic dialogue, case-participant voice clones, invented conversations or exact gestures. Do not fill a gap in surveillance with a reconstruction that appears to prove what happened there.
7. **Do not depict the killing or the victim's final moments.** Do not show Mo's body. Earlier documented activity may be visualized without inventing the attack or an intimate last perspective.
8. **Do not fabricate documents.** No invented readable passport, boarding pass or evidence screen. Recreated communications or ads use sourced wording and clear labels; otherwise summarize with an attributed graphic.
9. **Separate sound sources.** Log authentic audio and designed atmosphere independently. Added sound must not imply an evidentiary recording of an undocumented event.
10. **Review the completed shot.** A compliant prompt does not guarantee a compliant output. Check visuals, sound, labels and the meaning created by adjacent cuts.

For DARKHORSE, possible treatments include documented evening geography, spatial context leading explicitly into original surveillance, airport environments and route graphics, verified search/capture geography, and a labeled Vermont riding tribute. These remain candidates until evidence, references and the edit justify them.

## 9. DARKHORSE pilot: the audience's beat-by-beat journey

This is the episode-specific starting cut from the recommendations. Source-outline beat references below are carried over from that document; they are not new evidence citations. All case dates, quotes, availability and timing remain subject to original-record checks.

### The 90-second cold open

| Episode time | Beat | What it establishes |
|---|---|---|
| 0:00–0:15 | Vehicle question in Kaitlin's interview | Police have a specific evidentiary question; use a short, contextualized authentic exchange |
| 0:15–0:35 | Return timeline and vehicle appearance | Original lock/camera records create the central temporal connection; check clock offsets |
| 0:35–0:55 | Release | Show the relevant exchange and explain the warrant issue only as supported by the records |
| 0:55–1:15 | Sale and departure | Verified sale/travel evidence turns the story toward pursuit |
| 1:15–1:30 | Central question and title | How did investigators connect the woman they released to Mo's killing—and find her after she disappeared? |

These are creative allocations, not measured source excerpts. Adjust surrounding narration when an authentic exchange needs more room. Do not compress separate interview moments into a false continuous conversation. Avoid “the night before” or “the following day” until the relevant chronology is verified. The proposed 8:36/8:37 clock relationship is a verification task, not an approved narration line.

### The full episode

| Episode time | Section | Story progression | Recommendation's source-outline references |
|---|---|---|---|
| 0:00–1:30 | Cold open | Vehicle connection → release → disappearance → question | 6, 13–16, 23–25 |
| 1:30–5:30 | 1. The Final Evening | Return to discovery; establish Mo and Austin; reconstruct the relevant evening; identify what the camera and scene establish | 1–5, 9, 13–17 |
| 5:30–9:30 | 2. The Relationships | Explain the relationships, communications and attributed accounts needed to understand the investigation | 10–12, 19, 24 |
| 9:30–14:30 | 3. The Evidence | Connect vehicle, weapon evidence, phone records and interview without overstating what each proves | 18, 20–22, 26 |
| 14:30–18:30 | 4. The Disappearance | Develop sale, travel and identity evidence beyond the opening tease | 23, 25, 27, relevant 28 |
| 18:30–22:30 | 5. The Hunt | Explain the Costa Rica search, verified recruitment-ad operation and capture | 28–30 |
| 22:30–25:30 | 6. The Reckoning | Brief later escape attempt only if useful; verdict and sentence; family words and return to Mo's life | 31–34, with 7–8 |

**Starting total: 25:30.** “The Final Evening” avoids asserting a literal final 60-minute interval before verification. “The Relationships” names the chapter's function without defining Mo solely through a romantic relationship.

Within the opening test, use approximately 1:30–2:15 for discovery/response, 2:15–3:00 for Mo and Austin, 3:00–4:00 for the evening route, and 4:00–5:00 for camera/scene evidence and unresolved questions. The remaining first-act time bridges into the relationships. These allocations can move after the selects are measured.

Remove the personal-photo treatments identified in source-outline beats 3, 7 and 34. Establish Mo's name, age, cycling career and reason for visiting early, using checked records, narration, text and maps. Add short relevant passages later. End with verdict → documented family words → labeled Vermont riding tribute, Mo's name or a restrained text card. Do not substitute another prohibited photograph.

## 10. Release checklist

A release is ready only when the following are true:

- Factual narration, source excerpts, screen text, comparisons and panel states resolve to checked records; attributed allegations remain attributed.
- Quotes preserve context; edited chronology, camera offsets and retrospective reveals are clear.
- All used assets have approved use status and comply with the production source policy, including thumbnails and cutdowns.
- Reconstructions have grounding, approved references/takes and visible labels; illustrative tributes are explicitly distinguished from documented events.
- No body imagery, depiction of the killing, invented dialogue, synthetic case-participant voice, fabricated document or misleading POV is present.
- Maps use verified geography, supported route claims, approved privacy treatment and required attribution.
- The final export contains human final narration, checked captions, final graphics and no placeholders or temporary VO.
- The person at the center of the case remains present, the ending returns to that person, and the cut earns its runtime.
- Editorial, factual and use reviewers have resolved blockers; packaging and current platform disclosures match the approved export.
- The archive manifest identifies the exact approved export, source/transcript versions, permissions and production files.

## 11. Scaling without losing the evidence trail

Reuse channel styles, map templates, source labels, knowledge-panel states, transcript conventions and the linked-data schema. Reuse the process, not a predetermined number of chapters, a narration percentage or a recreation quota.

Keep one owner and one next action per case. Review source gaps early so production does not spend time generating images for claims it cannot support. Batch only approved shot specifications. Team members can work on different cases, but source changes and review decisions must flow back into the shared records.

Checkpoint text files at approved gates and keep accessible script/brief exports on Drive for collaborators who do not use git. After DARKHORSE, update the channel bible, narrator guide, timing rules and visual templates from the actual pilot results.

## 12. Migration from v2.4 and pilot start

This document is the v3.1 specification. Existing tools and commands must be checked against it; their filenames do not establish compatibility.

| Component | Required v3 change |
|---|---|
| Channel bible and format template | 15–30 minute runtime range, flexible acts, early human context, source boundaries and occasional knowledge panel |
| Narrator guide | Remove fixed VO share, reconstruction-by-tense rule and behavioral baseline analysis |
| Case templates | Add five linked datasets, source-use/acquisition separation, selects, segment IDs and knowledge-time provenance |
| Ingest/transcription | Cover audio recordings, preserve original/transcript versions, flag excluded assets and affected downstream claims |
| `maps_pull.py` | Apply source/privacy review before generation; read `04_locations.csv` and `people.csv`; output black and white dark maps at 2K to `_Production/MAPS/`; log skipped locations; distinguish documented routes from schematic connections |
| `vo_temp.py` | Replaced by ElevenLabs MCP calls run after script approval; preserve stable VO IDs, `TEMP_` prefixes and timing output |
| `shotlist.py` | Account for authentic audio, overlaps, holds and transitions; calculate runtime from the sequence and flag affected shots after changes |
| `validate.py` | Validate evidence links, status fields, screen claims, source policy, labels and final media inventory; report checks requiring human review |
| `gen_batch.py` | Submit only approved specs, record provenance and support a documented manual fallback |
| Stage commands | Add verification, opening test, final-VO and package interfaces; split `/script` and `/tempvo` into 6a and 6b; update existing commands to the twelve-stage order |
| Status/index files | Record the new stages, target/measured runtime, owners and unresolved blockers |

**Pilot sequence:**

1. Audit the existing C001 source collection and implementation. Preserve v2.4 and existing IDs; identify what needs migration instead of creating a duplicate case.
2. Flag the prohibited photo treatments and any excluded legacy media. Confirm which interview, 911, bodycam, surveillance, sale and courtroom records actually exist.
3. Build the linked chronology and selects. Resolve the opening's vehicle, interview, release, sale and departure claims before recording final narration.
4. Draft the brief and beat sheet, then assemble the opening five minutes with simple visual prototypes.
5. Use the tested opening to settle narration balance. Expand the full script and timing model before commissioning final recreations.
6. Complete visual production, full assembly, human VO, factual/use review and the release package in that order.

**Implementation checks still required:** parser compatibility with the segment schema; the NLE interchange format and handling of multiple audio layers; media copy/conflict behavior; the selected transcription/TTS/generation tools; map terms and export attribution; whether the Mapbox key and a black and white custom style exist and the ElevenLabs MCP connection and voice are configured; and the exact platform disclosure controls at release. These are implementation tasks, not claims that the tools have already been changed or tested.

---

**Revision basis:** [TrueCrime_Workflow_v3.md](TrueCrime_Workflow_v3.md), [TrueCrime_Workflow_v2.4.md](TrueCrime_Workflow_v2.4.md) and [DARKHORSE_Moriah_Wilson_Editorial_Recommendations.md](DARKHORSE_Moriah_Wilson_Editorial_Recommendations.md). No new case investigation or external source verification was performed for this revision.
