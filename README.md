# SillyTavern Skills

This repository contains Codex skills for SillyTavern workflows.

## Skills

1. `character-card-v3-generator`
- Purpose: Generate, refine, and validate Character Card V3 cards and lorebooks.
- Path: `skills/character-card-v3-generator`
- Main file: `skills/character-card-v3-generator/SKILL.md`

2. `sillytavern-extension-builder`
- Purpose: Scaffold and ship high-quality third-party SillyTavern extensions.
- Path: `skills/sillytavern-extension-builder`
- Main file: `skills/sillytavern-extension-builder/SKILL.md`

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
skills/sillytavern-extension-builder/scripts/scaffold_extension.sh /path/to/SillyTavern/public/scripts/extensions/third-party my-ext "My Ext" "you" "https://github.com/you/my-ext"
```

Slash-command-first template:

```bash
skills/sillytavern-extension-builder/scripts/scaffold_extension.sh --template slash /path/to/SillyTavern/public/scripts/extensions/third-party my-ext "My Ext" "you" "https://github.com/you/my-ext"
```

## Choosing A Template

Use `default` when:
- The extension is mainly UI-driven (settings panel, event handlers, DOM behavior).
- You need generation/chat lifecycle hooks as the core behavior.
- Slash commands are optional or secondary.

Use `slash` when:
- The extension's primary interface is one or more slash commands.
- You need argument parsing/validation and command help text from the start.
- UI is minimal and mostly for toggles/debug options.

Quick rule:
- If users mostly click UI controls, start with `default`.
- If users mostly type `/your-command ...`, start with `slash`.

You can still mix both patterns later; these templates optimize the initial structure.

## Validation

Validate skill structure:

```bash
python3 "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" skills/character-card-v3-generator
python3 "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" skills/sillytavern-extension-builder
```
