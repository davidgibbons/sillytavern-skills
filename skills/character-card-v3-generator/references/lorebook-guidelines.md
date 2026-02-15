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

## Macro-Driven Lorebook Patterns (Generic)

Use macros and lightweight markers to turn lorebooks into reusable runtime control layers.

When useful:
- You need consistent structured outputs without overloading permanent prompt text.
- You need event/state progression that should react to recent turns.
- You need modular rules that can be recombined across scenarios.

Practical patterns:
- Use stable trigger tokens/phrases as an \"event bus\" for lore entries.
- Use compact structured output targets (for example XML-like blocks) and optional regex post-processing for display normalization.
- Use hidden/internal markers sparingly to track unspoken state progression across turns.
- Keep state markers short, deterministic, and easy to test.

Design rule:
- Separate semantics from presentation.
- Lorebook entries should decide behavior/state.
- Post-processing (regex/macros/format transforms) should decide rendering.

## Command-Triggered Orchestration Pattern

This pattern treats lorebook entries like lightweight runtime commands.

Use when:
- You want controlled \"action attempts\" (`!explore`, `!talkto`, `!tryto`, etc.).
- You want outcome variability without rewriting core prompt text.
- You want command logic to be active only for the current turn.

How:
1. Define a stable trigger token for one action family.
2. Inject a short instruction block that explains how this turn should resolve.
3. Force that instruction to be near the end of prompt assembly (high recency).
4. Make it ephemeral so command instructions do not linger in later turns.

Authoring tips:
- Keep command entries imperative and specific: \"this turn, resolve X, then narrate Y\".
- Include failure modes caused by world logic, not just user error.
- For uncertain outcomes, instruct pacing (brief uncertainty before final result) if desired.

## Weighted Outcome Macros

For random/weighted branching, many setups use variants of macro syntax such as:

```text
{{pass::pass::pass::fail}}
```

This gives repeated values higher effective probability.

Guidance:
- Use small outcome sets first (2-4 branches).
- Keep branch text behavior-oriented, not verbose.
- Prefer explicit branch labels (pass/fail/twist/partial) to simplify debugging.
- Macro syntax and weighted forms can vary by frontend/extensions; verify against your runtime docs.

## Composable \"Entry Packs\" (Nested Logic, Generic)

Instead of one giant command entry, split reusable outcome logic into modular state packs:
- `action_success_state`
- `action_failure_state`
- `action_twist_state`

Then have the command entry select among those modules.

Benefits:
- Reuse consistent narrative logic across many commands.
- Tune probabilities and behavior in one place.
- Reduce duplication and drift in long scenario systems.

Note:
- Direct \"entry inside entry\" expansion is usually frontend/extension-dependent.
- Keep a fallback version that works without nesting support.

## Layered/Composable Lorebook Design

\"Lorebooks into lorebooks\" is best implemented as layered entry families, not giant nested monoliths.

Suggested layers:
1. Core world invariants (always relevant triggers).
2. Domain modules (politics, combat, travel, social).
3. Scene/event modules (temporary, high-specificity triggers).
4. Character modules (NPC-specific behavior packets).

How to compose safely:
- Keep each layer independently meaningful.
- Use narrow keys for upper layers to avoid accidental cascade activation.
- Use `recursive_scanning` only when the extra chaining is intentional and tested.
- Add explicit stop conditions (or low-priority fallbacks) to prevent runaway injection.
- Ensure command-layer entries are ephemeral or low-persistence unless explicitly intended to remain active.

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

## Delayed Secrets and Progressive Reveal

For mystery-heavy or long-form RP, separate what is hinted now from what is revealed later.

Pattern:
- Early entries: behavioral directives and surface-level clues.
- Delayed entries: specific facts gated by message-count delay or concrete trigger conditions.

Directive-first examples:
- Better early hint: `Be evasive about what happened in the barn.`
- Delay exact fact until reveal conditions are met.

Why this works:
- Preserves uncertainty and theory-building.
- Avoids exposing core secrets too early.
- Keeps characters acting suspicious without forcing explicit spoilers.

## Secret/Public Split Model

For long chats, maintain at least two layers per major NPC:

1. Public layer
- Known traits, social behavior, visible history.

2. Secret layer
- Hidden motives, real past events, private fears/trauma triggers.

Use cadence controls (when available in frontend/extensions):
- `Delay`: gate when an entry can appear by chat progression.
- `Sticky`: keep an activated state for a bounded period.
- `Cooldown`: prevent immediate repeated reactivation.

Practical use:
- Rare secret reactions should not fire every repeated trigger.
- Use cooldown to make major reactions feel occasional and meaningful.

## Belief vs Fact Architecture

Model each mystery with two entry families:

1. Belief entries
- What characters think is true (possibly wrong/incomplete).

2. Fact entries
- What is actually true, released only by strict conditions.

This supports:
- False theories and character misunderstandings.
- Gradual correction and high-impact reveal moments.
- Cleaner narrative control in ensemble scenes.

Maintenance rule:
- After major revelations, update or demote stale belief entries so characters stop acting on disproven assumptions.

## Lightweight Workflow

1. Start with 5-15 high-impact entries only.
2. Run short chats and record failure points.
3. Add or refine entries for repeated failures.
4. Re-test with the same scenarios before growing the lorebook further.

## Debugging and Verification

- Keep a prompt-view/debug panel open while testing.
- Confirm command entries appear when expected and disappear after their intended turn.
- Verify weighted branches are being selected over repeated trials.
- Check that stale command instructions are not consuming context in later turns.
- If behavior is wrong, inspect assembled prompt order before editing card text.

## Validation Checklist

- Every entry has clear trigger intent.
- Entry text is useful even if injected once.
- Trigger collisions are minimized.
- High-value entries survive token pressure.
- Lorebook improves outcomes in at least 3 real test conversations.
