# Multi-Character and World/Scenario Card Design

Use this guide when the card is a world, scenario, or ensemble cast instead of a single protagonist.

## Card Type Decision

Single-character card:
- One primary persona drives voice and behavior.
- Side characters are mostly contextual.

World/scenario card:
- The "system" is the product (setting, rules, factions, event logic).
- Multiple NPCs appear over time with role-based behavior.

Use a world/scenario card when user interaction is expected to rotate across many entities or locations.

## Where To Put Information

Put in `description`/`scenario` (always-on):
- World premise and tone.
- Core simulation rules that should always apply.
- 1-3 anchor factions and their stable goals.
- Hard constraints (power limits, magic rules, economy logic).

Put in lorebook (conditional):
- Detailed character rosters.
- Location-specific facts.
- Event branches and consequence tables.
- Rare/occasional NPC profiles.
- Time/phase-specific behaviors.

Rule of thumb:
- If information must always influence output, keep it in always-on fields.
- If information should appear only when relevant, move it to lorebook entries.

## Handling Character Lists

In always-on fields:
- Keep only a compact cast index (name + role + one-line intent) for key recurring actors.

In lorebook:
- Store full character details and trigger by keys (name, title, aliases).
- Split each NPC into one entry per high-value behavior domain (motivation, relationships, red lines) instead of one huge blob.

Occasional characters:
- Put entirely in lorebook.
- Use narrow keys and optional secondary keys.
- Avoid injecting occasional NPC detail into base scenario text.

## Structured World Events and Logic

Represent world logic as small, composable entries:
- Trigger conditions (what activates).
- State update (what changes).
- Consequence text (what the model must reflect).

Prefer event families over monoliths:
- Politics events
- Travel/logistics events
- Combat/escalation events
- Social reputation events

Use insertion ordering and priority to keep deterministic behavior under token pressure.

## Graceful Multi-Character Behavior

- Define a response arbitration rule in always-on fields (for example: "Only one NPC leads each turn unless scene explicitly requires multiple speakers").
- Require explicit speaker labeling in dialogue-heavy scenarios.
- Keep NPC voices distinct with one concrete speech cue each.
- Prevent omniscient leakage: NPCs should only act on information they could plausibly know.

## Anti-Patterns

- Giant always-on cast biographies.
- Scenario text that hardcodes temporary scene state forever.
- One lorebook entry containing the entire world bible.
- Multiple NPCs speaking every turn without scene need.
- Event systems without clear trigger boundaries.

## Review Checks (World/Scenario Cards)

- Does the card still behave sensibly if lorebook is mostly inactive?
- Do occasional NPCs stay dormant unless triggered?
- Are event outcomes consistent across repeated similar prompts?
- Can the model keep speaker identity stable in 3+ NPC scenes?
- Does token pressure remove low-priority lore before core rules?
