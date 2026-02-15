# `st-extension-example` Walkthrough

Source baseline: [`city-unit/st-extension-example`](https://github.com/city-unit/st-extension-example)

## 1. What the Template Demonstrates

- Manifest-driven extension loading.
- Simple settings object with defaults.
- DOM insertion into extension settings UI.
- Event hooks for app lifecycle and generation lifecycle.
- Optional module worker class export.

## 2. Manifest Pattern

The example `manifest.json` demonstrates the standard key set:

- Human metadata: `display_name`, `author`, `version`, `homePage`
- Loading controls: `loading_order`
- Dependency signaling: `requires`
- Runtime entrypoints: `js`, `css`

Reuse this as a baseline; only add keys that are actually used.

## 3. Entrypoint Pattern (`index.js`)

Template patterns worth reusing:

- `extension_settings[extensionName]` object with stable defaults
- `loadExtensionSettings(extensionName)` before usage
- `saveSettingsDebounced()` after changes
- `jQuery(async () => { ... })` startup wrapper
- `eventSource.on(event_types.APP_READY, ...)` lifecycle handling
- Generation event handler (`GENERATION_AFTER_COMMANDS`) for post-command logic

## 4. Settings UI Pattern

The example appends controls into extension settings UI using template rendering utilities.

Reuse approach:

1. Render extension HTML template (`settings.html`) with `renderExtensionTemplateAsync`.
2. Attach event handlers by stable DOM IDs/classes.
3. Sync UI state from `extension_settings`.
4. Save changes through debounced settings persistence.

## 5. Module Worker Pattern

The example includes a minimal worker class:

- `static init(moduleId)` for one-time module initialization
- `static update()` for periodic refresh

Use worker mode only when polling/update cadence is needed and safe.

## 6. Adaptation Checklist

- Replace example extension name with your slug in all constants.
- Replace sample UI/handlers with domain behavior.
- Remove unused hooks and imports.
- Keep event handlers small and testable.
- Verify no debug logs or placeholders remain before release.
