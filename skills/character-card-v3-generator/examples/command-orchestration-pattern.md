# Command-Orchestration Pattern (Generic)

This example shows how to build command-like behavior using lorebook entries.

## Goal

Enable optional user actions (for example `!explore`, `!tryto`, `!talkto`) with controlled, variable outcomes.

## Pattern

1. Command trigger entry
- Key: `!tryto`
- Purpose: detect action attempt and instruct this-turn resolution.
- Placement/depth: near end of prompt build for high recency.
- Persistence: one-turn/ephemeral when supported.

Example content idea:

```text
This turn only: user attempted an action command.
Resolve the action with one of: pass, fail, twist.
Narrate attempt first, then consequence.
If uncertain moment fits the scene, briefly delay the reveal before final outcome.
```

2. Outcome modules (reusable)

```text
action_success_state
- Describe why success is plausible under world rules.
- Apply state update.

action_failure_state
- Failure is caused by world circumstances or constraints, not arbitrary refusal.
- Apply state update.

action_twist_state
- Outcome appears to go one way, then reveals a logical complication.
- Apply state update.
```

3. Weighted selection

A common ST-style pattern is repeated-value selection:

```text
{{success::success::failure::twist}}
```

Interpretation: more repeated labels mean higher selection chance.

## Design Rules

- Keep command logic short and deterministic.
- Keep world consistency stronger than randomness.
- Always write explicit state deltas, not just flavor.
- Remove stale command injections after the active turn when possible.

## Test Protocol

1. Run 10+ command invocations.
2. Inspect prompt assembly for entry order and cleanup.
3. Confirm branch frequencies roughly match intent.
4. Verify no stale command text remains in later turns.
