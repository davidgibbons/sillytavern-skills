# Writing Extensions Reference

Source baseline: SillyTavern contributor docs (`for-contributors/writing-extensions.md`).

## 1. Extension Types

- UI Extensions: add panels, controls, UX affordances, and chat-facing interactions.
- Message Summarization Extensions: generate summary messages in chat.
- Prompt Interceptor Extensions: mutate prompt pipeline content before generation.
- Slash Command Extensions: expose reusable command primitives.
- Module Worker Extensions: update module state on interval (even without direct UI input).

## 2. Minimum File Anatomy

A third-party extension directory should contain:

- `manifest.json` (required)
- `index.js` (or another JS file referenced by `manifest.json`)
- Optional runtime files like `style.css`, settings templates, and helper modules

`manifest.json` commonly includes:

- `display_name`
- `loading_order`
- `requires` (hard dependencies)
- `optional` (optional integrations)
- `js` (entry file)
- `css` (optional stylesheet)
- `author`
- `version`
- `homePage`

## 3. Core JS Import Surfaces

Typical imports from an extension entrypoint:

- `../../../extensions.js`
  - `extension_settings`
  - `loadExtensionSettings`
  - `renderExtensionTemplateAsync`
  - `getContext`
- `../../../../script.js`
  - `eventSource`
  - `event_types`
  - `saveSettingsDebounced`
- Slash command APIs from `../../slash-commands/` packages when command support is needed.

Use the current upstream docs for exact import members and path changes.

## 4. Lifecycle and Event Patterns

- Register startup logic in `jQuery(async () => { ... })`.
- Load settings before using them.
- Subscribe with `eventSource.on(event_types.SOME_EVENT, handler)`.
- Use debounced settings save for user-configurable state changes.

Common event use cases:

- App readiness
- Generation lifecycle stages
- Character/user message events
- Chat/context changes

## 5. Slash Command Guidelines

- Define command name, aliases, help text, and argument schemas.
- Validate arguments with typed parsers/enums where possible.
- Return deterministic command outputs and failure messages.
- Avoid hidden side effects; make state mutation explicit.

## 6. Module Worker Guidelines

- Export a worker class with static lifecycle methods as documented.
- `init` should be idempotent and safe on repeated calls.
- `update` should short-circuit when chat/module context is not ready.
- Keep interval work lightweight and avoid uncontrolled growth in memory or DOM state.

## 7. Packaging and Distribution

- Keep repo layout stable and manifest metadata accurate.
- Include only required runtime assets.
- Publish with a clear version and compatible install path expectations.
- If distributing as zip, preserve extension root structure.

## 8. Practical Reliability Checks

- Verify `manifest.json` file names map to existing files.
- Verify every import path from `index.js` resolves from extension location.
- Verify settings keys migrate safely if renamed.
- Verify command names do not collide with existing built-in commands.
- Verify behavior when no chat is open and when required modules are unavailable.
