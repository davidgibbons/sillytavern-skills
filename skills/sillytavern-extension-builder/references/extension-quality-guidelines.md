# Extension Quality Guidelines

This guide combines official SillyTavern contributor docs, official template repos, and extension listing requirements.

## 1. Design for Compatibility First

- Prefer documented extension APIs over internal/private globals.
- Use the modern slash command parser API (`SlashCommandParser.addCommandObject`) rather than deprecated `registerSlashCommand`.
- Keep settings keys stable and perform migrations when renaming keys.
- Fail gracefully if optional dependencies/modules are unavailable.

## 2. Lifecycle and Event Hygiene

- Register handlers inside startup (`jQuery(async () => { ... })`) after settings load.
- Keep event handlers short, idempotent, and side-effect scoped.
- Treat event payloads as inconsistent unless documented; validate event data before use.
- Unsubscribe/guard long-running logic to prevent duplicate behavior after reloads.

## 3. Command UX Quality

- Provide clear `helpString`, argument descriptions, and defaults.
- Validate argument types and return deterministic error text for invalid input.
- Avoid command name collisions with built-in commands; namespace via extension slug when possible.
- Keep command callbacks fast and non-blocking.

## 4. Security and Privacy

- Never execute untrusted user input as code.
- Minimize external requests and clearly expose when network calls occur.
- Follow SillyTavern extension security guidance for input validation and safe DOM updates.
- Avoid storing sensitive tokens in plaintext settings unless explicitly required and documented.

## 5. Performance and Reliability

- Debounce saves (`saveSettingsDebounced`) and avoid repeated heavy writes.
- Avoid expensive logic in high-frequency events (generation/token events).
- Gate background/module-worker loops by chat/module readiness.
- If using bundled frameworks (React/Webpack templates), keep build output small and dependency set minimal.

## 6. Release Readiness Checklist

- `manifest.json` references only existing runtime files.
- Install path works as a direct git clone into `public/scripts/extensions/third-party`.
- Extension starts without console errors in clean profile.
- Commands/events/settings work when no chat is open and when chat switches.
- README/docs explain what it does, required modules, and command usage.

## 7. Distribution Recommendations

- Version semantically and document breaking changes.
- Keep runtime repo clean (remove test stubs, debug-only logs, dead imports).
- Prefer open-source and maintainability if you intend to submit to extension listings.
- Ensure extension stays independent of server-plugin requirements for broader compatibility, unless explicitly targeting plugin users.

## Sources

- SillyTavern docs: writing extensions
  - https://docs.sillytavern.app/for-contributors/writing-extensions/
- SillyTavern docs: making requests and performance/security sections
  - https://docs.sillytavern.app/for-contributors/writing-extensions/making-requests/
- Official extension examples/templates
  - https://github.com/city-unit/st-extension-example
  - https://github.com/SillyTavern/Extension-ReactTemplate
  - https://github.com/SillyTavern/Extension-WebpackTemplate
- Content listing requirements and recommendations
  - https://github.com/SillyTavern/content
