<p class="kicker">Radley · Production Workflow · v2.4 · For Review · October 12, 2026</p>

# True Crime Channel: Episode Production Workflow v2

A repeatable system for turning the Ci archive into published episodes at speed. v2 changes three things from v1: the channel's working files run out of a **local git repo** while **all media and transcripts stay on Google Drive**, episodes are **VO-first** (the script leads and the edit follows), and **AI recreations and temp AI VO** are built into the pipeline as tracked, reproducible steps instead of one-off tasks.

The two v1 rules still hold: every video is transcribed, and each transcript sits next to its video.

## 1. How the system works (the loop)

Each case moves through ten stages. Claude reads and drafts; scripts in `tools/` do the mechanical work; a human signs off at each gate (◆).

| # | Stage | Output | Gate |
|---|---|---|---|
| 1 | Ingest | transcripts, asset index, timeline, locations + sample maps | |
| 2 | Case Brief | hook, lenses, 3–5 recreation picks, key locations, ledger seeds | ◆ |
| 3 | Story Spine | exhibits + ledger beats | ◆ |
| 4 | VO Script | line-ID'd narration with cues | ◆ |
| 5 | Temp VO | AI TTS per line, real durations | |
| 6 | Visual Plan | maps, HUDs, shot specs at real durations | ◆ |
| 7 | Recreations | stills → video takes, graded + overlaid | ◆ |
| 8 | Animatic | temp VO + footage + recreations rough cut | ◆ |
| 9 | Final VO | human narrator, drop-in by line ID | |
| 10 | Metadata + Rights Gate | titles, chapters, disclosure, go / no-go | ◆ |

**What changed from v1 and why:**

- **The script moves ahead of the visual plan.** The narrator carries the channel, so the VO is written and locked first. The visuals are then planned against it.
- **Temp VO sits between script and visuals.** Generating an AI read of every line gives each beat its real duration before any recreation is generated. Recreations get made at the length they'll actually play, which cuts wasted generation credits and re-timing work.
- **An animatic replaces the rough cut guesswork.** Temp VO, real footage and recreation stills are assembled into a watchable cut before the human narrator records, so structure problems show up early.
- **Final human VO drops in by line ID.** The narrator records from the same line-ID'd script, so each file replaces its temp twin without re-editing.

Three cue types appear in the script, same as v1: **[FOOTAGE]**, **[GRAPHIC]**, **[RECREATION]**. v2 adds two channel devices that are also cued: **[LEDGER]** (Knowledge Ledger updates) and **[EXHIBIT]** (chapter evidence cards).

## 2. Storage: repo + Google Drive

The system is split across three places, each doing one job:

| Where | What lives there | Why |
|---|---|---|
| **Local git repo** (+ private GitHub) | Scripts, indexes, prompts, shot specs, timing files, case notes, tools | Small text files that Claude edits constantly. Git gives version history and gate checkpoints. |
| **Google Drive** | **All media and all transcripts**: footage, `.srt` transcripts, research source files, reference images, recreation takes, temp + final VO, edit exports | Shared with the team, backed up, one source for everything heavy or source-of-truth. |
| **Ci** | The original archive | Archive of record. Media is pulled from Ci into Drive per case. |

**How they connect: on demand, nothing syncs.** Google Drive is never installed or mounted on the Mac. `tools/media.py` uses **rclone** to pull a case from Drive into a git-ignored `_media/` folder inside the repo only when a stage needs it, and to push new outputs back when the stage ends. In this doc, any path written `media:/…` means that case's folder on Drive (and its local copy in `_media/` while you work).

- **Pull** skips video by default: transcripts, research, reference images, maps and VO come down fast. Video comes down only for a step that needs it (`--for-transcribe`, `--only <file>`).
- **Push** only adds or updates files on Drive. It never deletes or moves anything there, and it skips any file that is newer on Drive (a teammate's edit).
- **Clear** removes the local copy to free space, and refuses if anything hasn't been pushed.
- Every stage command pulls at the start and pushes at the end.

### Repo (local, text only)

Keep it outside any iCloud-synced folder (Desktop and Documents are often synced on a Mac, and iCloud can corrupt a `.git` folder). Suggested: `~/Dev/truecrime-channel`.

```
truecrime-channel/                        ← git repo (private GitHub under nonformula)
│
├── CLAUDE.md                             ← standing context: rules, conventions, pull/push
├── STATUS.md                             ← what's in flight across all cases
├── .gitignore                            ← _media/, .env, media + *.srt safety net
├── _media/                               ← local copy of pulled cases (git-ignored)
├── .claude/commands/                     ← one slash command per stage (/ingest C001 …)
│
├── _channel/                             ← applies to every episode
│   ├── config.yaml                       ← media (rclone) and tool settings
│   ├── map_styles.yaml                   ← Mapbox Studio style IDs, zoom + size presets
│   ├── channel_bible.md                  ← lane, format rules, do/don't
│   ├── format_chain_of_custody.md        ← episode structure template (see §5)
│   ├── narrator_voice_guide.md           ← tone, tense rules, recurring phrases
│   ├── master_case_index.csv             ← every case + status (can mirror to a Sheet)
│   ├── lenses/                           ← POV_ACTIONCAM · POV_GLASSES · POV_DASH · WIDE_RECON
│   ├── prompt_library/                   ← base prompts per model (stills, i2v, negatives)
│   ├── tts/voice_config.yaml             ← temp VO voice, speed, pause rules
│   ├── gfx_templates/                    ← AE/Premiere template refs: ledger, exhibit card, HUD
│   └── publishing_checklist.md
│
├── tools/                                ← automation (Python); media.py moves files to/from Drive
│   ├── media.py                          ← rclone pull / push / status / clear (copy-only)
│   ├── new_case.py                       ← scaffold repo case folder + matching Drive folder
│   ├── transcribe.py                     ← WhisperX → .srt saved next to each video on Drive
│   ├── maps_pull.py                      ← geocode locations + pull sample maps from Mapbox
│   ├── vo_temp.py                        ← script → per-line TTS to Drive + vo_timing.csv in repo
│   ├── shotlist.py                       ← timing + cues → shot durations, edit CSV / EDL
│   ├── gen_batch.py                      ← submit recreation specs to model APIs, log takes
│   └── validate.py                       ← pre-publish checks (see Stage 10)
│
└── cases/
    └── C001_Wilson_Darkhorse/
        ├── case.yaml                     ← principals, lens assignments, runtime, status
        ├── 00_case_brief.md
        ├── 02_research_notes.md          ← Claude's notes + citations into media:/02_research
        ├── 03_rights.md                  ← clearance status per asset (proof docs on Drive)
        ├── 04_timeline.md
        ├── 04_locations.csv              ← every case location, geocoded + sourced
        ├── 05_script/  outline_v1.md · script_v1.md (§6)
        ├── 06_asset_index.csv
        ├── 07_visuals/
        │   ├── visual_index.csv · ledger.csv
        │   └── recreations/R014/  shot.yaml · prompt.md · takes_log.csv
        ├── 08_vo/vo_timing.csv
        ├── 09_edit/  shotlist.csv · EDL/XML
        └── 10_publish/  metadata.md · rights_report.md · validate log
```

### Google Drive (media + transcripts)

Same case IDs and folder numbers as the repo, so every path lines up.

```
True Crime Channel/                       ← Drive (rclone remote gdrive:)
│
├── _channel/                             ← shared AE templates, fonts, LUTs, HUD elements
│
└── Cases/
    └── C001_Wilson_Darkhorse/
        ├── 01_assets/
        │   ├── bodycam/        bodycam_01.mp4 + bodycam_01.srt
        │   ├── interrogation/
        │   ├── news/
        │   ├── surveillance/
        │   └── audio_911/
        ├── 02_research/                  ← articles, court docs, PDFs
        │   └── reference_images/         ← source truth for maps + recreations
        ├── 03_rights/                    ← licenses, FOIA letters, source proof
        ├── 07_visuals/
        │   ├── maps/
        │   │   ├── samples/              ← auto-pulled Mapbox samples per location
        │   │   └── final/                ← delivered map graphics
        │   ├── graphics/
        │   └── recreations/R014/
        │       ├── stills/               ← approved keyframes
        │       └── takes/                ← C001_R014_T03.mp4 …
        ├── 08_vo/
        │   ├── temp/                     ← TEMP_VO_012.wav …
        │   └── final/                    ← VO_012.wav …
        └── 09_edit/                      ← project files, animatic + final exports
            └── record_script.pdf
```

### Media handling that matters

- **One-time rclone setup per machine:** `brew install rclone`, then `rclone config` to add a remote named `gdrive` (browser sign-in once; choose the shared drive if the channel folder lives on one). `python3 tools/media.py check` confirms it works.
- **Transcripts are versioned by Drive, not git.** Drive keeps version history on each `.srt`. If a transcript is corrected after indexing, re-run `/ingest` for that asset so the index and timeline pick up the change.
- **Free space after heavy steps.** `media.py clear C001 --video-only` removes local video once transcripts are pushed.
- **Prefer Drive for Desktop?** Set `media.mode: mount` and `media_root` in `_channel/config.local.yaml`; everything else works the same.

### Why this split

- **Claude Code works natively on a local folder.** Stages become slash commands, tools run directly, and several cases can be processed at once.
- **Git gives you history and rollback** on everything Claude writes. Commit at each gate as a checkpoint.
- **Drive gives the team one shared home for media** without git, LFS or large-file pain.
- **Nothing heavy lives on the Mac** unless a step needs it, and nothing runs in the background.
- **`CLAUDE.md` holds the rules once,** including the pull/push habit.

**Trade-offs to plan for:** team members who don't use git need either light onboarding or a read-only Drive folder of exported scripts and briefs. Every machine running the tools needs rclone connected to the same Drive or shared drive. The one habit to keep is pushing: the stage commands do it automatically, and `media.py status` shows anything left behind.

### Rules that make this work

**Transcript pairing.** Same basename, same Drive folder, different extension: `bodycam_01.mp4` → `bodycam_01.srt`. `.srt`/`.vtt` preferred because timecodes turn a script into an edit-ready shot list. `transcribe.py` produces these automatically.

**Mirrored structure.** The repo case folder and the Drive case folder share the same `C###_Surname_Keyword` name and numbered subfolders. `new_case.py` creates both at once.

**Case naming:** `C###_Surname_Keyword`. The `C###` is used everywhere: index, filenames, cues.

**Take naming:** `[CASE]_[SHOT]_[TAKE].mp4`, e.g. `C001_R014_T03.mp4`. Same lean convention the team already uses for Runway assets.

**Line IDs are permanent.** Once a script is locked, `VO_###` IDs never get renumbered. New lines get suffixes (`VO_012a`). Temp VO, final VO, ledger, and timing all key off these IDs.

**Never rename source files after indexing.** The indexes reference them by name.

**Reference images are source truth for anything synthetic.** A recreation with no real reference behind it is a fabrication risk.

## 3. Master Case Index (`_channel/master_case_index.csv`)

Same columns as v1, plus four production columns. Claude updates it at every stage.

| Column | Purpose |
|---|---|
| Case ID · Working Title · Priority · Hook | as v1 |
| Status | Backlog / Indexed / Briefed / Spined / Scripted / Temp VO / Visuals / Animatic / Final VO / Cleared / Published |
| Footage Strength · Rights Risk · Est. Runtime · Assigned To | as v1 |
| **Recreation Load** | Low / Med / High: how much of the story has no footage |
| **Recreations Approved** | e.g. 14 / 22 |
| **Final VO** | Not booked / Booked / Recorded / Dropped in |
| **Blocked On** | the one thing holding the case up |
| Last Updated | date |

## 4. Indexes

**06_asset_index.csv** (as v1): `asset_id, filename, source_type, transcript_file, duration, key_moments, rights_status, source_origin, notes`

**07_visuals/visual_index.csv** (expanded): `visual_id, type, lens, script_lines, duration_s, reference_source, grounding_source, gen_prompt_file, model, approved_take, disclosure, status`

- **type**: map / timeline / chart / evidence_still / exhibit_card / ledger / recreation
- **lens**: POV_ACTIONCAM / POV_GLASSES / POV_DASH / WIDE_RECON (recreations only)
- **script_lines**: the VO line IDs this visual plays under, e.g. `VO_041–VO_044`
- **duration_s**: filled from `vo_timing.csv`, never guessed
- **grounding_source**: the transcript/research file that proves the moment happened. Blank = cannot be produced.
- **disclosure**: Yes by default for every recreation

**07_visuals/ledger.csv**: `line_id, column (police | viewer), text, source`. Drives the Knowledge Ledger graphic template.

## 5. Channel format: Chain of Custody

Standard episode template stored in `_channel/format_chain_of_custody.md`. Stage 3 builds every outline on it.

- **Cold open (0:00–2:30):** the strongest dramatic-irony moment in real footage. Narrator states what the viewer knows that the people on screen don't.
- **Exhibits 01–05/06:** each chapter opens on one evidence object shown as an exhibit card. Every chapter ends on an open question the next exhibit answers. Re-hook every 5–8 minutes.
- **Knowledge Ledger:** persistent graphic comparing what police know vs. what the viewer knows. Updated from narration via `[LEDGER]` cues.
- **Baseline beat:** where interview footage allows, one person is established as the baseline and the suspect is read against it (adapted from the JCS format).
- **Close:** verdict and aftermath. End on the victim, never the perpetrator.
- **Runtime target:** 40–50 min single film. Recreation-led moments get cut down separately for Shorts.

### Narrator rules (in `narrator_voice_guide.md`)

- Omniscient host who knows the ending and uses that knowledge for tension.
- **Present tense over recreations, past tense over archival.** This is the audible signal for "this is a reconstruction."
- Directs the viewer's eye ("Watch her hands"). Set up, footage pays off, narrator interprets.
- VO covers ~65–70% of runtime. Peaks get silence.
- No invented dialogue. Quotes are verbatim from transcripts.

## 6. VO-first script format

Scripts are structured markdown so `vo_temp.py`, `shotlist.py` and `validate.py` can parse them. One block per VO line:

```
## EXHIBIT 04 · The Receipt

### VO_041
tense: present
text: She pulls into the lot just after noon.
picture: [RECREATION: R014]
source: media:/02_research/carmax_sale_record.pdf
ledger: viewer + "The Jeep is gone"

### VO_042
tense: past
text: Police wouldn't learn about the sale for days.
picture: [GRAPHIC: G009]
source: 04_timeline.md#may-13

[BEAT 2.0]

### VO_043
text: (none)
picture: [FOOTAGE: A017 @ 04:12–04:31]
note: no VO, let the footage play
```

- `[BEAT n]` inserts n seconds of silence into the temp VO and the timing file.
- A line with `text: (none)` is a picture-only beat. `shotlist.py` takes its duration from the footage in/out.
- `source:` is required on every factual line. Missing = `[UNVERIFIED]` and `validate.py` fails the build.

## 7. The ten stages

Each stage is a slash command in `.claude/commands/`, run from the repo root, e.g. `/brief C001`. Prompts below are the command bodies. Stages marked ⚙ are mostly tool-driven.

**Stage 1 · Ingest & Index ⚙** `/ingest {{CASE_ID}}`

> Run `tools/transcribe.py` on any video in `media:/Cases/{{CASE_ID}}/01_assets/` missing a paired `.srt` (saved next to the video on Drive). Then read every transcript from Drive and produce `06_asset_index.csv` rows with source_type, duration, and 3–6 key_moment timestamps drawn only from the transcript. Build `04_timeline.md`: one chronological account, each event tagged with asset_id + timestamp or research file. Flag contradictions between sources. Do not invent times or events. **Then extract every location** the transcripts and research name (addresses, businesses, venues, airports, cities) into `04_locations.csv`, each tagged with the events and sources it comes from, and run `tools/maps_pull.py` to geocode them and pull sample maps (see §8b). Update the master index and STATUS.md.

**Stage 2 · Case Brief ◆** `/brief {{CASE_ID}}`

> Write `00_case_brief.md`: (1) logline, (2) cold-open candidate with asset + timestamp and the dramatic-irony line it enables, (3) principals and roles, (4) the narrative question, (5) 5–6 exhibit candidates (evidence objects that can each open a chapter), (6) baseline candidate if interview footage allows, (7) **lens assignments**: which principal, if any, gets a POV lens and which preset, justified by who they were, (8) seed entries for the Knowledge Ledger, (9) **recreation candidates: suggest 3–5 recreations** for moments with no footage that the Chain of Custody structure needs. For each give: the moment, which exhibit/chapter it serves, the lens preset, the grounding source (transcript or research file), whether reference images exist, and a pass/fail check against the §9 rules (documented action, faceless, no crime or victim's final moments, not presented as real footage). Rank them by story value and drop any that fail. (10) **key locations**: the 4–8 locations that matter most, with links to their sample maps in `media:/…/07_visuals/maps/samples/`, and which exhibit each supports, (11) footage strength + rights risk. Keep it to one to two pages. Write lens assignments and approved recreation candidates into `case.yaml`.

**Stage 3 · Story Spine ◆** `/spine {{CASE_ID}}`

> Draft `05_script/outline_v1.md` on `_channel/format_chain_of_custody.md` for a {{RUNTIME}}-minute episode. For each beat: narration purpose, retention reason, open question carried out of the chapter, and what carries the picture (footage asset + timestamp, graphic, or recreation with lens). Mark ledger updates. Mark every beat with no footage.

**Stage 4 · VO Script ◆** `/script {{CASE_ID}}`

> Write `05_script/script_v1.md` from the approved outline in the §6 block format and the voice in `narrator_voice_guide.md`. Present tense over recreations, past tense over archival. Every factual line has a `source:`. Quotes verbatim from transcripts. Every `[RECREATION]` cue gets a provisional visual_id and a row in `visual_index.csv` (status: Planned). Every `[LEDGER]` cue gets a row in `ledger.csv`. Mark anything unsourced `[UNVERIFIED]`. On approval, lock line IDs and commit.

**Stage 5 · Temp VO ⚙** `/tempvo {{CASE_ID}}`

> Run `tools/vo_temp.py`: parse `script_v1.md`, generate one TTS file per VO line (`media:/…/08_vo/temp/TEMP_VO_###.wav`) using `_channel/tts/voice_config.yaml`, honor `[BEAT]` pauses, and write `08_vo/vo_timing.csv` (line_id, duration, running in/out). Stitch `temp_vo_full.wav` on Drive. Then run `tools/shotlist.py` to write each visual's `duration_s` into `visual_index.csv` and output `09_edit/shotlist.csv`. Report the total runtime vs. target and which chapters run long.

**Stage 6 · Visual Plan ◆** `/visuals {{CASE_ID}}`

> For every row in `visual_index.csv`: **Maps** (start from `04_locations.csv` and the approved samples; spec area, points, route, style from `map_styles.yaml`; final builds in Mapbox Studio / Google Earth Studio). **Graphics** (timelines, relationship charts, exhibit cards, ledger states). **Recreations**: write `recreations/R###/shot.yaml` with lens preset, exact duration + 1s handles, the VO lines it plays under, reference images from `media:/…/02_research/reference_images/`, the grounding source, and a draft prompt built from the lens preset + `prompt_library/`. Do not spec any recreation that has no grounding source. Apply the recreation rules in §9.

**Stage 7 · Recreations ◆** `/recreate {{CASE_ID}} [R###…]`

> Run in two passes. **Pass A, stills:** generate keyframes from reference images (Nano Banana Pro) for every shot. Human approves look and continuity. **Pass B, motion:** image-to-video from approved stills (Kling / Veo / Runway Gen-4.5, routed per `prompt_library/` notes) at the spec'd duration. `gen_batch.py` saves every take to `media:/…/07_visuals/recreations/R###/takes/` named `C###_R###_T##`, and logs model, prompt, seed and settings to `takes_log.csv` in the repo. Human picks the take; record `approved_take` in the index.

Post, per shot (motion team): lens grade + grain from preset, then the **HUD / RECONSTRUCTION overlay applied in After Effects from the template, never generated.** AI models garble on-screen text, and the overlay must carry the real source citation from the shot spec.

**Stage 8 · Animatic ◆** `/animatic {{CASE_ID}}`

> Run `tools/shotlist.py --edl` to produce an edit list that lays temp VO, footage in/outs, approved recreation takes (or stills where motion isn't done), and graphic placeholders on a timeline for import into Premiere/Resolve. Editor assembles and watches the full episode. Notes go back to the script (line IDs) or the shot specs, not into the edit.

**Stage 9 · Final VO**

> Generate `media:/…/09_edit/record_script.pdf` (line IDs, tense marks, pronunciation notes). Narrator records with slated line IDs. Files saved to `media:/…/08_vo/final/VO_###.wav` drop in over their temp twins. Re-run `shotlist.py` so any timing change flags the affected shots.

**Stage 10 · Metadata + Rights Gate ◆** `/publish-check {{CASE_ID}}`

> Produce `10_publish/metadata.md`: 5 titles, thumbnail concept + 3–4 words, 150-word description with hook up top and the standard recreation disclosure line, 15–20 tags, chapters from exhibit breaks. Then run `tools/validate.py` and produce `rights_report.md`: (1) footage cues whose rights_status isn't Public Record or Licensed, (2) unsourced or `[UNVERIFIED]` lines, (3) recreations missing reference, grounding, disclosure, or an approved take, (4) **any TEMP_ VO file still in the timeline**, (5) any recreation depicting a disputed act or a victim's final moments, (6) any map missing Mapbox/OpenStreetMap attribution or showing a private residence at street level that the location rules don't allow. Output go / no-go with the items to resolve.

## 8. Temp AI VO: how it's used

- **Purpose:** timing and animatic only. It locks durations so recreations are generated once, at the right length.
- **Engine:** an API TTS with per-line generation (ElevenLabs is the obvious fit). Use a stock voice that roughly matches the narrator's pace and register.
- **Never published.** Every temp file is prefixed `TEMP_`. `validate.py` fails the build if one is still in the timeline.
- **No voice cloning of the narrator without written consent.** If you later want a cloned temp voice of your human narrator for faster animatics, get that in their contract.
- Temp reads usually run a little faster or slower than a human. Expect a ±5–10% timing shift at Stage 9. Handles on every recreation absorb it.

## 8b. Map locations pipeline

Maps start in Stage 1, not Stage 6. Every location the case mentions is pulled out early, so the brief can show what the geography looks like before the story is locked.

**Step 1: Extract.** During `/ingest`, Claude lists every location named in the transcripts and research into `04_locations.csv`:

`location_id, name, address_or_place, type, lat, lon, geocode_confidence, events, sources, privacy, notes`

- **type**: residence / business / venue / road / airport / city / region
- **events**: the timeline events that happen there
- **sources**: the transcript timestamps or research files that name it. No source = not listed.
- **privacy**: public / private_residence / uninvolved_party (see rules below)

**Step 2: Geocode.** `maps_pull.py` sends each location to the **Mapbox Geocoding API** with your token and writes back lat/lon plus a confidence score. Low-confidence matches get flagged for a human to confirm before anything is built on them.

**Step 3: Pull samples.** For each location, `maps_pull.py` calls the **Mapbox Static Images API** using your styles from `map_styles.yaml` and saves samples to `media:/…/07_visuals/maps/samples/`:

- `C001_L03_city.png` (wide context), `C001_L03_neighborhood.png` (mid), `C001_L03_street.png` (close, public locations only)
- One **route sample** per pair of locations the timeline connects (e.g. pool → restaurant → apartment), drawn as a path overlay
- A **case overview** with every location plotted

File names follow `[CASE]_[LOCATION]_[ZOOM].png`, e.g. `C001_L03_neighborhood.png`.

**Step 4: Review.** The brief links the 4–8 key locations and their samples. Stage 6 turns the approved samples into final map specs, built in Mapbox Studio or animated in Google Earth Studio.

**Access and setup**

- Your Mapbox token goes in an untracked local file (`.env` at the repo root, git-ignored; template in `.env.example`) or a macOS environment variable. **It is never committed to the repo.**
- Style IDs from your Mapbox Studio account live in `map_styles.yaml` so every case uses the same channel look.
- Mapbox and OpenStreetMap attribution stays on every published map, per Mapbox's terms. Confirm the terms for using static images in monetized video before the pilot publishes.

**Location rules**

- **Private residences** (victim, suspect or witness homes) are shown at neighborhood level or as a pin on a stylized map, never with a readable house number or a street-level image.
- **Uninvolved parties** (neighbors, friends who weren't part of the case) aren't plotted at all unless a court record makes the location public and the story needs it.
- **Geocoding is a starting point, not proof.** Every key location gets checked by a person against the research before it appears in a final map.

## 9. Recreation rules (the gate that protects the channel)

1. **Ground it.** Every recreation needs a reference image and a grounding source. No grounding = no shot.
2. **Disclose it.** On-screen RECONSTRUCTION tag, a description line, and YouTube's altered/synthetic content setting at upload.
3. **Faceless by default.** Real faces only come from real footage. Recreations use POV, hands, silhouettes, objects and places.
4. **Lenses are per-person and per-case.** Assigned in the brief, stored in `case.yaml`. Each lens has a fixed prompt fragment, grade and HUD. The viewer should know whose world they're in from the frame alone.
5. **POV never looks like police footage.** Police bodycam is only ever the real Axon/archival footage.
6. **Documented actions only.** POV of a suspect shows what the evidence proves they did. No inner monologue, no invented dialogue.
7. **No depiction of the crime or a victim's final moments.** From either perspective. Describe in narration and cut away.
8. **Don't imply a device existed.** Present POV as a reconstructed view, never as the person's own footage.
9. **Budget:** POV recreations ~20–25% of runtime. Real footage stays the backbone.
10. **Named individuals get a legal look before publish** (likeness, defamation), separate from footage clearance.

## 10. Scaling to many episodes

- **Build once, reuse forever:** lens presets, prompt library, graphics templates (ledger, exhibit card, HUD), voice config and the format template are channel-level. Per case you only write the brief, spine, script and shot specs.
- **Run cases in parallel.** Stages 1–3 need no media work and can run across several cases in one sitting. The gates are where people spend their time.
- **Batch generation overnight.** `gen_batch.py` queues every approved shot spec for a case. Humans review takes in the morning.
- **Commit at every gate.** `git commit -m "C001 script locked"` is the checkpoint. STATUS.md says what's next.
- **Tune from the pilot.** Run the full loop on C001 (DARKHORSE), then update the Channel Bible, voice guide, lens presets and prompt library from what worked before starting C002.

## 11. How to start (pilot)

1. Create the repo in a non-iCloud folder (e.g. `~/Dev/truecrime-channel`) with `CLAUDE.md`, `_channel/` and `tools/`. Add the `.gitignore` first and push to a private GitHub repo.
2. Install rclone and connect it to Drive (`rclone config`, then `media.py check`). Scaffold `C001_Wilson_Darkhorse` with `new_case.py` (creates the repo folder and the Drive folder tree). Copy its media from Ci into the Drive `01_assets/` subfolders.
3. Run `/ingest C001`. Everything downstream flows from a clean index.
4. Build the tools just before the stage that needs them: `media.py` + `new_case.py` + `transcribe.py` + `maps_pull.py` (Stage 1) → `vo_temp.py` + `shotlist.py` (after the first script) → `validate.py` (before Stage 10) → `gen_batch.py` (after the pilot).

**Open items / not yet verified:**

- Which recreation models expose a usable API for batch submission varies and changes often. `gen_batch.py` may need to be partly manual until that's confirmed per model.
- TTS engine, WhisperX setup and NLE import format (EDL vs. XML for Premiere/Resolve) need a quick test on the pilot before being standardized.
- DARKHORSE case facts used in examples (dates, sale record, timeline anchors) are placeholders until checked against the archive.
