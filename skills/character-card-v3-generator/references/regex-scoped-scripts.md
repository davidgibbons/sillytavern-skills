# Card-Scoped Regex Scripts (SillyTavern)

This file documents SillyTavern-specific card-scoped regex scripts.

Important:
- This is not a CCv3 core field.
- Store these scripts under `data.extensions.regex_scripts`.
- Keep scripts portable by making the card still usable when a client ignores regex extensions.

## Where Scripts Are Stored

- Global scripts: app settings
- Scoped scripts: active character card data

In SillyTavern, scoped scripts are stored as:

```json
{
  "data": {
    "extensions": {
      "regex_scripts": []
    }
  }
}
```

## Script Object Shape

Each script object typically includes:

- `id` (string UUID)
- `scriptName` (string)
- `findRegex` (string)
- `replaceString` (string)
- `trimStrings` (string[])
- `placement` (number[])
- `disabled` (boolean)
- `markdownOnly` (boolean)
- `promptOnly` (boolean)
- `runOnEdit` (boolean)
- `substituteRegex` (number)
- `minDepth` (number or null)
- `maxDepth` (number or null)

`placement` values (SillyTavern):
- `1` user input
- `2` AI response
- `3` slash commands
- `5` world info injections
- `6` reasoning blocks

`substituteRegex` values (SillyTavern):
- `0` no macro substitution
- `1` raw substitution
- `2` escaped substitution

## Example: Cleanup Narrative Marker

```json
{
  "id": "4f6d9668-e5f2-4bf3-9ffd-e7f47d7c5f64",
  "scriptName": "Strip Narrator Prefix",
  "findRegex": "/^Narrator:\\s*/gm",
  "replaceString": "",
  "trimStrings": [],
  "placement": [2],
  "disabled": false,
  "markdownOnly": false,
  "promptOnly": false,
  "runOnEdit": true,
  "substituteRegex": 0,
  "minDepth": null,
  "maxDepth": null
}
```

## Example: Emphasize Action Verb in AI Output

```json
{
  "id": "cd82917e-4669-4c30-8b08-c7c31fbe8f0f",
  "scriptName": "Bold Action Verbs",
  "findRegex": "/\\b(draws|lunges|dodges|parries)\\b/gi",
  "replaceString": "**$1**",
  "trimStrings": [],
  "placement": [2],
  "disabled": false,
  "markdownOnly": true,
  "promptOnly": false,
  "runOnEdit": false,
  "substituteRegex": 0,
  "minDepth": 0,
  "maxDepth": 4
}
```

## Best Practices

- Prefer simple patterns and explicit flags (`i`, `g`, `m`, `s`, `u`) over complex nested expressions.
- Restrict `placement` to only the text sources that need transformation.
- Start with `AI response` placement only, then expand carefully.
- Use depth limits to avoid mutating deep history unexpectedly.
- Test with representative chat snippets before distribution.
- Avoid regex transforms that alter meaning-critical facts.
- Keep script names descriptive because slash commands target `scriptName`.

## Why Scoped Regex Is Useful For Character Cards

- Enforce consistent output formatting without repeatedly encoding formatting instructions in every card field.
- Normalize model drift (for example, clean repeated prefixes, spacing noise, or inconsistent section markers).
- Apply display-only decoration after generation, which can reduce prompt/card verbosity and keep structure deterministic.
- Keep formatting behavior tied to a specific character card instead of global app settings.

## Token-Efficiency Pattern: Generate Compact XML, Decorate After

Use the card/system prompt to request compact XML-like structure, then use scoped regex to convert it to richer display formatting.

Why this can help:
- The model emits a short, regular schema.
- Decoration rules live in regex scripts instead of repeated prompt text.
- Formatting remains consistent across turns.

Example model output target:

```xml
<scene>Rain taps on broken glass.</scene>
<thought>Need to stall for time.</thought>
<speech>"You're late."</speech>
```

Example regex idea:
- Match `<speech>...</speech>` and wrap it in a preferred style.
- Match `<thought>...</thought>` and render as italics or muted text.
- Strip container tags that are not needed in final display.

Use caution:
- Regex runs client-side; it does not change tokens already spent in completion.
- Net savings come from simpler persistent prompts and reduced instruction repetition, not from post-processing alone.
- Keep transforms reversible enough for debugging.

## References

- SillyTavern Regex docs:
  - https://docs.sillytavern.app/extensions/regex/
- SillyTavern regex engine and storage behavior:
  - https://github.com/SillyTavern/SillyTavern/blob/release/public/scripts/extensions/regex/engine.js
  - https://github.com/SillyTavern/SillyTavern/blob/release/public/scripts/char-data.js
- Regex flags reference:
  - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions#advanced_searching_with_flags
