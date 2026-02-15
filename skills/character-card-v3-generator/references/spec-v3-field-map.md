# Character Card V3 Field Map

Source of truth: Character Card V3 spec at https://github.com/kwaroran/character-card-spec-v3

## Top-Level Object

Required:
- `spec`: must be `"chara_card_v3"`
- `spec_version`: must be `"3.0"`
- `data`: object

## `data` Core Fields

Expected core fields (CCv3 interface includes CCv2 set plus additions):
- `name`: string
- `description`: string
- `personality`: string
- `scenario`: string
- `first_mes`: string
- `mes_example`: string
- `creator_notes`: string
- `system_prompt`: string
- `post_history_instructions`: string
- `alternate_greetings`: string[]
- `group_only_greetings`: string[] (required in v3, may be empty)
- `tags`: string[]
- `creator`: string
- `character_version`: string
- `extensions`: object

Optional additions:
- `character_book`: lorebook object
- `assets`: asset[]
- `nickname`: string
- `creator_notes_multilingual`: object keyed by ISO 639-1 language code
- `source`: string[]
- `creation_date`: unix timestamp seconds
- `modification_date`: unix timestamp seconds

## Prompt Control Fields (High Impact)

These two fields are major quality levers and should be authored deliberately.

### `system_prompt` (foundational contract)

Purpose:
- Define always-on operating rules for character/world behavior.
- Establish stable constraints that should persist across the entire session.

Use for:
- Role boundaries and non-negotiable behavior rules.
- Narrative stance (for example, in-character continuity expectations).
- Safety/consistency constraints and world-logic invariants.

Avoid:
- Temporary scene state that should expire quickly.
- Repeating large lore blocks already covered by other fields.
- Overly verbose style directives that crowd context.

### `post_history_instructions` (final-turn steering)

Purpose:
- Provide additional instructions conditioned on conversation context.
- Shape how the next response is generated after message history is assembled.

Use for:
- Response formatting requirements and output structure.
- Turn-level pacing/length controls.
- Prompt-adherence checks and rule reinforcement.
- Runtime guardrails for known failure modes (repetition, drift, perspective errors).

Priority behavior:
- In many frontends, these instructions are applied after user/history context and may receive higher effective priority than base prompt fields.
- Treat this field as high-authority final steering for the current response.
- Because implementations vary across clients/models, validate behavior in target runtime.

ST-specific note:
- If per-character prompt overrides are enabled in client settings, character-level prompt fields can replace default global prompt blocks.
- Some clients support `{{original}}` to include the default global prompt content inside overrides.

### Authoring Rule

- Put durable identity/world contract in `system_prompt`.
- Put response-time steering and enforcement in `post_history_instructions`.
- Keep them complementary, not contradictory.

### Failure Pattern To Avoid

- Using `post_history_instructions` to silently fight `system_prompt` creates unstable behavior and unpredictable adherence.
- Prefer explicit hierarchy: permanent contract first, final-turn steering second.

## Non-Standard But Common Extension Fields

CCv3 recommends app-specific data live in `data.extensions`.

SillyTavern commonly stores character-local extras in this object, for example:
- `data.extensions.regex_scripts`: card-scoped regex scripts (SillyTavern extension feature)

Treat these as frontend-specific; keep them namespaced in `extensions` and do not promote them to new top-level spec fields.

## `assets` Entry

Each asset object must include:
- `type`: string
- `uri`: string (`https://`, data URL, `embeded://...`, or `ccdefault:`)
- `name`: string
- `ext`: string (lowercase extension without dot, or `unknown`)

Notes:
- If `assets` is absent, app should behave as if it contains default icon entry.
- If multiple `icon` assets exist, exactly one should be `name: "main"`.

## `character_book` (Lorebook)

Lorebook object fields:
- `extensions`: object
- `entries`: array

Common optional book-level fields:
- `name`, `description`, `scan_depth`, `token_budget`, `recursive_scanning`

Each lore entry should include:
- `keys`: string[]
- `content`: string
- `extensions`: object
- `enabled`: boolean
- `insertion_order`: number
- `use_regex`: boolean

Common optional entry fields:
- `constant`, `case_sensitive`, `selective`, `secondary_keys`, `position`
- `name`, `id`, `comment`, `priority`

## CBS and Decorators

Common curly-brace macros:
- `{{char}}`, `{{user}}`, `{{random:...}}`, `{{pick:...}}`

Lore decorators begin with `@@` at top of entry content. Useful examples:
- `@@depth N`
- `@@scan_depth N`
- `@@position before_desc|after_desc|personality|scenario`
- `@@activate_only_after N`
- `@@activate_only_every N`

Use decorators sparingly; prefer clear fields first.
