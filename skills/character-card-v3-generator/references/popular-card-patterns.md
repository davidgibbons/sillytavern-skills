# Applied Quality Patterns (Generalized)

Based on review of these cards in this repo:
- `/Users/dgibbons/git/character-card-skill/Sasha, your new innocent warden.png`
- `/Users/dgibbons/git/character-card-skill/Super Falls Academy .png`
- `/Users/dgibbons/git/character-card-skill/Delinquent classmate.png`

## What Performs Well (Keep)

1. Strong opening hook in `first_mes`
- All three cards immediately place `{{user}}` into a concrete scene with stakes.
- Practical rule: ensure turn 1 creates a clear response decision.

2. Clear archetype + readable structure
- Popular cards use obvious archetypes and sectioned writing (traits, likes/dislikes, goals, relationships).
- Practical rule: preserve scannable structure even in complex cards.

3. Creator-facing guidance
- Creator notes often explain role assumptions and intended interaction style.
- Practical rule: include brief operator notes for expected play style and boundaries.

4. Discoverability metadata
- Tags are dense and specific.
- Practical rule: use tags as retrieval/routing hints, not just marketing labels.

5. World cards use lorebooks as content volume container
- The world card keeps rich setting details in lorebook entries rather than only base fields.
- Practical rule: put deep optional context in lorebook, keep base fields high-signal.

## Quality Risks Seen In Popular Cards (Fix in Our Skill)

1. Overloaded entry content
- World entries can be very large; this increases injection cost and unpredictability.
- Improvement: split into smaller entries by trigger domain and scene relevance.

2. Broad or noisy keys
- Some entries include broad keys and even empty keys.
- Improvement: avoid empty keys; tighten keys + secondary conditions.

3. Field imbalance
- Some cards leave `personality`/`mes_example` empty and over-rely on `description`.
- Improvement: distribute behavior signal across dedicated fields.

4. Platform metadata spillover
- Imported worldbooks may include platform-specific non-core fields.
- Improvement: normalize imports and keep non-standard data under `extensions`.

## Normalization Pass For Any Uneven Card

1. Preserve behavior, reorganize structure
- Move permanent behavior rules into `description`/`personality`/`scenario`.
- Move conditional detail into lorebook entries.

2. Remove trigger hazards
- Delete empty keys.
- Replace broad keys with targeted variants.

3. Split giant lore entries
- Target one concept per entry.
- Keep event logic modular (`trigger -> state change -> consequence`).

4. Keep first-message strength
- Do not dilute the opening scenario hook while refactoring.

## World/Scenario Specific Takeaways

- Keep a compact cast index always-on (name, role, one-line intent).
- Put full NPC sheets in lorebook.
- Put occasional/rare NPCs only in lorebook with narrow triggers.
- Use explicit turn arbitration rules when multiple NPCs are active.
