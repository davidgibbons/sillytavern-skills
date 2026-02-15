# Lorebook Guidelines

## Goal

Use lorebook entries as targeted context injection, not a static encyclopedia.

## Entry Design

- Keep one concept per entry.
- Write short, explicit `content` that changes model behavior.
- Use strong `keys` likely to appear in user/model phrasing.
- Add synonyms only when they increase recall without noise.
- Keep entries around 20-100 words when possible; split longer concepts into multiple entries.

## Activation Strategy

- Use `scan_depth` to limit false positives from distant context.
- Use `insertion_order` for deterministic ordering.
- Use `priority` only when frontend honors it.
- Use `token_budget` to prevent lorebook bloat from crowding chat history.
- For broad world facts, use broader keys and lower activation frequency.
- For niche facts, use narrow keys and higher specificity.

## Regex and Selective Matching

- Enable `use_regex` only for truly variable patterns.
- Keep regex simple and safe to avoid accidental over-triggering.
- Use `selective` + `secondary_keys` when one key is too broad.

## Decorator Usage

- Prefer plain fields first.
- Add decorators only for behavior you cannot express with base fields.
- Keep decorator stack shallow to preserve cross-client portability.

## Community-Derived Practices

From linked community discussions and guides:
- Treat lorebooks as active scene-control tools when needed.
- Favor concise imperative instructions for event/result entries.
- Use grouped, probabilistic event entries to reduce repetitive outcomes.
- Iterate from real chat failures: add/adjust entries only where behavior drifts.
- Avoid giant catch-all entries; split by trigger domain (social, combat, travel, etc.).
- Keep lorebook trigger words out of normal prose when using random-roll groups to avoid repeated accidental re-triggers.
- Use sticky/temporary persistence features carefully so an injected rule affects several turns but does not become permanent drift.
- Use comments/metadata fields for maintenance notes and keep prompt-facing `content` clean.
- Test entries in representative chat contexts and tune keys before adding more volume.

## Lightweight Workflow

1. Start with 5-15 high-impact entries only.
2. Run short chats and record failure points.
3. Add or refine entries for repeated failures.
4. Re-test with the same scenarios before growing the lorebook further.

## Validation Checklist

- Every entry has clear trigger intent.
- Entry text is useful even if injected once.
- Trigger collisions are minimized.
- High-value entries survive token pressure.
- Lorebook improves outcomes in at least 3 real test conversations.
