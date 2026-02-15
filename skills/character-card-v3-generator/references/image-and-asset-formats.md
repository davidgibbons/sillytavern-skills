# Image and Asset Format Guide (CCv3)

This file documents practical image/asset format handling for Character Card V3.

Source of truth:
- https://github.com/kwaroran/character-card-spec-v3

## Card Container Formats

CCv3 cards are commonly transported as:

1. PNG/APNG
- Card data is embedded in a PNG/APNG `tEXt` chunk named `ccv3`.
- The chunk value is the CCv3 JSON string encoded as UTF-8 then base64.
- If both `chara` (v2) and `ccv3` exist, clients should prefer `ccv3`.

2. JSON
- File is directly the CharacterCardV3 JSON object.

3. CHARX (`.charx`)
- Zip container with `card.json` at root.
- Embedded assets are referenced by `embeded://path/to/file.ext` (spec spelling is `embeded://`).

## `data.assets` Basics

Each asset object should include:
- `type` (string): for example `icon`, `background`, `user_icon`, `emotion`
- `uri` (string): `https://...`, data URL, `embeded://...`, or `ccdefault:`
- `name` (string): identifier, often `main` for primary asset
- `ext` (string): lowercase extension without dot, e.g. `png`, `webp`, `jpeg`

Compatibility rules:
- If `assets` is missing, client may behave as if a default icon exists.
- If multiple `icon` entries exist, include exactly one with `name: "main"`.
- For `background`, at most one `name: "main"` is recommended.

## Recommended Image Formats

For broad compatibility, prefer:
- `png` for transparent icons
- `jpeg`/`jpg` for photo-like backgrounds
- `webp` for smaller size with good quality

Spec-level note:
- Clients should support at least png, jpeg, and webp where possible.

## URI Strategy

Use this order by portability:
1. `ccdefault:` for baseline fallback
2. `embeded://...` for self-contained CHARX distributions
3. `https://...` for externally hosted assets
4. data URLs only for small assets (can increase card size quickly)

Security/portability notes:
- Some clients may ignore insecure `http://` URIs.
- Some clients may not fetch external URIs in restricted environments.
- Keep cards usable even when external assets fail.

## Example `assets` Array

```json
"assets": [
  {
    "type": "icon",
    "uri": "ccdefault:",
    "name": "main",
    "ext": "png"
  },
  {
    "type": "background",
    "uri": "https://example.com/harbor.webp",
    "name": "main",
    "ext": "webp"
  },
  {
    "type": "emotion",
    "uri": "embeded://assets/emotion/images/angry.png",
    "name": "angry",
    "ext": "png"
  }
]
```

## Authoring Checklist

- Keep one `icon` named `main`.
- Ensure `ext` matches actual resource format.
- Provide fallback behavior (`ccdefault:`) where possible.
- Avoid huge inline data URLs for large images.
- Test card in at least one target frontend before publishing.
