# Character Card V3 Skill

This repository contains a Codex skill for generating and reviewing Character Card V3 cards, including lorebooks, format strategy, regex-scoped transforms, and quality review workflows.

## Skill Location

- Skill folder: `/Users/dgibbons/git/character-card-skill/skills/character-card-v3-generator`
- Main instructions: `/Users/dgibbons/git/character-card-skill/skills/character-card-v3-generator/SKILL.md`

## What The Skill Covers

- CCv3 field mapping and structure guidance.
- Character writing quality guidelines.
- Lorebook design and trigger strategy.
- Multi-character and world/scenario card patterns.
- Card-scoped regex usage (SillyTavern-specific).
- Image/asset packaging formats (PNG/APNG, JSON, CHARX).
- Format options (Prose, Attributes, AliChat, JED/JED+, Plaintext, W++).
- Quality review rubric and release readiness checks.

## How To Use In Codex

Mention the skill by name in your prompt:

```text
Use $character-card-v3-generator to create a CCv3 card for ...
```

Example requests:

```text
Use $character-card-v3-generator to generate a standard CCv3 card for a mystery-school scenario.
```

```text
Use $character-card-v3-generator to convert this existing card to CCv3 and improve lorebook trigger quality.
```

```text
Use $character-card-v3-generator to review this card and score it with the built-in quality rubric.
```

## Key Files

- Skill workflow: `/Users/dgibbons/git/character-card-skill/skills/character-card-v3-generator/SKILL.md`
- References: `/Users/dgibbons/git/character-card-skill/skills/character-card-v3-generator/references/`
- Examples: `/Users/dgibbons/git/character-card-skill/skills/character-card-v3-generator/examples/`
- Templates: `/Users/dgibbons/git/character-card-skill/skills/character-card-v3-generator/assets/templates/`
- Validator: `/Users/dgibbons/git/character-card-skill/skills/character-card-v3-generator/scripts/validate_card.py`

## Validation

Run skill structure validation:

```bash
python3 /Users/dgibbons/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/dgibbons/git/character-card-skill/skills/character-card-v3-generator
```

Validate a generated card JSON:

```bash
python3 /Users/dgibbons/git/character-card-skill/skills/character-card-v3-generator/scripts/validate_card.py /path/to/card.json
```
