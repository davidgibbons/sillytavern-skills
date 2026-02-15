# Template Selection Guide

Use this guide when choosing scaffold mode in `scripts/scaffold_extension.sh`.

## `default` Template

Best for:
- UI-first extensions with settings-heavy workflows.
- Event-driven features tied to app/generation/chat lifecycle.
- Extensions where commands are optional extras, not the main entrypoint.

What you get:
- Baseline settings UI wiring.
- Event hook pattern (`APP_READY`, `GENERATION_AFTER_COMMANDS`).
- Minimal extension shell for DOM and context-based behaviors.

## `slash` Template

Best for:
- Command-first extensions where users interact through `/commands`.
- Features requiring argument parsing, validation, and command help text.
- Automation/utility actions with little or no custom UI.

What you get:
- Slash command parser registration pattern.
- Typed argument and named-argument example.
- Minimal settings toggles for command enable/debug behavior.

## Decision Checklist

Pick `default` if most answers are yes:
- Does the feature rely on rendered controls/panels?
- Does behavior depend heavily on lifecycle events?
- Will non-command users still use this feature often?

Pick `slash` if most answers are yes:
- Is command invocation the primary user journey?
- Do you need predictable argument contracts and feedback?
- Is a lightweight settings panel enough?

## Migration Notes

- `default` -> `slash`: keep settings/event shell, add slash command registration.
- `slash` -> `default`: keep commands, add richer UI and event-driven behavior.
- Mixed mode is normal for mature extensions; the template only picks your starting bias.
