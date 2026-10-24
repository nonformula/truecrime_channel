---
name: case-process
description: "Start or resume a case through requested v3.2 stages in Google Drive. Use for process this case, continue the case, or run through a named deliverable; coordinates existing stage skills."
---

# Process or resume a case — Content Creation System v3.2

Read `references/codex-runtime.md` for Codex tool discovery and execution boundaries.

Read `references/rules.md`, `references/drive-workspace.md`, `references/data-contract.md` and `references/gates.md` before working on a case. These references are bundled with this skill. 
Resolve the case and requested endpoint from the user's language. “Process this case” defaults to ingest and verification preparation, then propose a brief; “through script” permits all intervening development drafts. “All stages” means advance through available production capabilities and review points, not fabricate completion. Do not ask the user to choose internal plumbing.

Read current Case Record and output revisions before acting. Resume incomplete work. Route to the relevant bundled skill by reading its SKILL.md at the sibling path shown; do not assume another skill was auto-loaded. If a referenced skill is unavailable in the installed package, report the incomplete installation rather than invent its behavior.

| Stage | Skill path from this folder | Outcome |
|---|---|---|
| 1 Ingest | ../case-ingest/SKILL.md | Five Drive research files |
| 2 Verify/select | ../case-verify/SKILL.md | Checked chronology/selects or explicit verification queue |
| 3 Brief | ../case-brief/SKILL.md | Reviewed investigative premise |
| 4 Spine | ../case-spine/SKILL.md | Linked beat sheet and act timing |
| 5 Opening test | ../case-opening-test/SKILL.md | Paper edit, then actual assembly when possible |
| 5b Pre-script | ../case-prescript/SKILL.md | Beat-organized story document with VO intent, sound bites, visual cues |
| 6a Full script | ../case-script/SKILL.md | Source-linked script with SEG/VO IDs |
| 6b Temp VO | ../case-tempvo/SKILL.md | ElevenLabs temp takes and provisional sequence timing |
| 7–12 Production/release | ../case-production/SKILL.md | Stage-specific outputs and explicit external handoffs |

Respect approvals already given for unchanged revisions. Save provisional outputs when useful, but never label a human gate approved without a recorded decision. Reuse existing artifacts and IDs; do not restart the case because the conversation or platform changed.

During long reads, checkpoint source coverage and give concise progress updates. End with current-output links, stage/status, blockers and the next concrete action. This is an in-session workflow, not a persistent unattended service.
