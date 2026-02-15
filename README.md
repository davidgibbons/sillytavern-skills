# SillyTavern Skills

This repository contains Codex skills for SillyTavern workflows.

## Skills

1. `character-card-v3-generator`
- Purpose: Generate, refine, and validate Character Card V3 cards and lorebooks.
- Path: `/Users/dgibbons/git/sillytavern-skills/skills/character-card-v3-generator`
- Main file: `/Users/dgibbons/git/sillytavern-skills/skills/character-card-v3-generator/SKILL.md`

2. `sillytavern-extension-builder`
- Purpose: Scaffold and ship high-quality third-party SillyTavern extensions.
- Path: `/Users/dgibbons/git/sillytavern-skills/skills/sillytavern-extension-builder`
- Main file: `/Users/dgibbons/git/sillytavern-skills/skills/sillytavern-extension-builder/SKILL.md`

## Usage In Codex

Mention a skill in your prompt:

```text
Use $character-card-v3-generator to generate a standard CCv3 card for this concept.
```

```text
Use $sillytavern-extension-builder to scaffold a slash-command-first extension called my-tools.
```

## Extension Scaffold Examples

Default template:

```bash
/Users/dgibbons/git/sillytavern-skills/skills/sillytavern-extension-builder/scripts/scaffold_extension.sh /path/to/SillyTavern/public/scripts/extensions/third-party my-ext "My Ext" "you" "https://github.com/you/my-ext"
```

Slash-command-first template:

```bash
/Users/dgibbons/git/sillytavern-skills/skills/sillytavern-extension-builder/scripts/scaffold_extension.sh --template slash /path/to/SillyTavern/public/scripts/extensions/third-party my-ext "My Ext" "you" "https://github.com/you/my-ext"
```

## Validation

Validate skill structure:

```bash
python3 /Users/dgibbons/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/dgibbons/git/sillytavern-skills/skills/character-card-v3-generator
python3 /Users/dgibbons/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/dgibbons/git/sillytavern-skills/skills/sillytavern-extension-builder
```
