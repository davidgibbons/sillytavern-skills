# Reviewing Character Cards For Quality

Use this checklist to review a card before sharing or deploying.

## 1) Spec Compliance

- `spec` is `"chara_card_v3"`.
- `spec_version` is `"3.0"`.
- Required fields exist and have correct types.
- Non-standard data is inside `data.extensions`.
- `group_only_greetings` exists (can be empty).
- `assets` entries have valid `type`, `uri`, `name`, `ext`.

Pass criteria:
- Card passes structural validation and imports cleanly in target frontend.

## 1b) Prompt-Field Governance (Critical)

- `system_prompt` defines durable behavioral contract, not temporary scene trivia.
- `post_history_instructions` is used for final-turn steering and structure enforcement.
- The two fields do not issue conflicting directives.
- If `post_history_instructions` intentionally tightens rules, the override is explicit and justified.

Pass criteria:
- In test chats, these fields improve adherence and response quality without causing role drift or contradiction loops.

## 2) Character Consistency

- Identity is clear in 1-2 sentences.
- Goals, boundaries, and tone do not conflict.
- Character does not drift into generic assistant behavior after several turns.
- `first_mes` matches intended voice and pacing.
- `first_mes` gives `{{user}}` an immediate actionable hook (decision, response, or tension).

Pass criteria:
- In test chats, behavior remains recognizable and stable over 20+ turns.

## 3) Dialogue Quality

- Replies are in-character and context-aware.
- Style is not repetitive across consecutive turns.
- Response length matches intended cadence.
- `mes_example` demonstrates the actual desired output style.

Pass criteria:
- At least 3 test scenarios show consistent voice and low repetition.

## 4) Lorebook Effectiveness

- Entries are concise and single-purpose.
- Keys are specific enough to avoid accidental activation.
- Trigger coverage matches intended scenarios.
- Token budget and insertion order are tuned.
- Delayed-reveal entries are gated correctly and do not leak core secrets early.
- Rare secret reactions use cadence controls (delay/sticky/cooldown or equivalent) to avoid repetitive firing.
- Belief entries and fact entries are separated, and post-reveal cleanup is planned.

Pass criteria:
- Lore entries fire when expected and stay quiet when irrelevant.

## 5) Token Efficiency

- Permanent fields avoid redundant text.
- No large duplicate instructions across sections.
- Rich formatting is done with examples or scoped transforms rather than repeated prose.
- Behavior signal is distributed across fields (do not overload only `description` while leaving key fields empty).
- Critical behavior rules are not stored only in optional/example blocks that may be dropped under context pressure.

Pass criteria:
- Permanent token load is proportionate to card complexity.

## 6) Safety and Leakage Checks

- Hidden/state-tracking patterns do not leak into visible output unexpectedly.
- Regex transforms do not alter critical meaning.
- Card does not force control of `{{user}}` actions unless intentionally designed.
- `post_history_instructions` does not introduce coercive or contradictory control patterns that break core role logic.

Pass criteria:
- No critical leaks or semantic corruption across test chats.

## 7) Portability

- Card remains usable if frontend-specific features are ignored.
- External assets fail gracefully.
- Regex/lore decorators degrade safely on clients with partial support.

Pass criteria:
- Core behavior survives in at least one alternate client/model setup.

## 8) Multi-Character / World Scenario Quality

- Core world rules are in always-on fields, not buried in conditional entries.
- Detailed NPC profiles are in lorebook and activate only when relevant.
- Occasional characters do not appear unless triggered by context.
- Multi-speaker turns remain readable with stable speaker identity.
- Event logic is modular (trigger -> state update -> consequence), not monolithic.

Pass criteria:
- In 3+ NPC test scenes, turn ownership and hidden knowledge boundaries remain coherent.

## Scoring Rubric (Quick)

Score each category 0-2:
- `0` = failing
- `1` = acceptable with issues
- `2` = strong

Categories:
- Spec compliance
- Consistency
- Dialogue quality
- Lorebook quality
- Token efficiency
- Safety/leak resilience
- Portability
- Multi-character/world handling

Interpretation:
- `12-14`: publish-ready
- `9-11`: usable, improve weak areas
- `0-8`: revise before release

## Recommended Review Flow

1. Run structural validation.
2. Run 3 scripted chat tests (neutral, conflict, edge-case).
3. Log failures by category.
4. Patch only highest-impact issues first.
5. Re-test same prompts to confirm improvement.
