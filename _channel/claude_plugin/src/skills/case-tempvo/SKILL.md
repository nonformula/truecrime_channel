---
name: case-tempvo
description: "Generate temporary narration for an approved script through ElevenLabs via MCP and measure provisional sequence timing. Use for temp VO, scratch narration, TTS timing pass, or v3.2 stage 6b."
---

# Temporary VO — stage 6b

Read `references/rules.md`, `references/drive-workspace.md`, `references/data-contract.md` and `references/gates.md` before working on a case. These references are bundled with this skill. Read `references/segment-format.md`.

Precondition: the full script (stage 6a) is approved for its exact current revision. If it is not, stop and report that gate; do not generate audio from a draft unless the user explicitly consolidates the gates and that decision is recorded.

1. Check capability: an ElevenLabs MCP connection is available in this session and the channel's stock production voice is configured. Inspect the tool schemas; do not assume tool names. Generation spends credits, so it must be within the user's authorized scope. If either is missing, deliver a temp-VO queue (VO ID, exact text revision, pronunciation notes) and state generation pending.
2. Generate one file per approved VO line, narration only. Never generate quoted source audio, participant speech or any case-participant-like voice. Name files `TEMP_[CASE]_[VO_ID]_r[n]` with the tool's audio extension and save to the case `08_vo/temp/` folder on Drive; never drop the `TEMP_` prefix.
3. Measure each take's actual duration. Record VO rows: vo_id, text_revision, take_link, temporary, tts voice/model, measured_duration, status. A word-count estimate is not a measurement.
4. Update the Sequence tab: a clip with VO over it occupies one interval; give document holds, audio-only statements and silent pauses explicit timing. Calculate the provisional runtime from the combined sequence, not the narration track alone.
5. Read back, record the stage in the Case Record and flag segments whose timing changed materially.

Ready when every approved VO line has a measured temp take and the provisional runtime is reported against the 15–30 minute range. Return links, measured versus estimated totals, lines that ran long or short, and the next action (stage 7 visual plan via `case-production`). Temp VO is never published.
