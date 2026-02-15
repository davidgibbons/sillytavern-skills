# Secret Reveal Pattern (Generic)

Use this for mystery arcs and long-term chats.

## Structure

1. Public entry
- Visible behavior and known history.

2. Directive hint entry (early)
- Instruct behavior without exposing facts.
- Example: "Be evasive about the incident at the old mill."

3. Delayed fact entry (late)
- Exact truth gated by delay and/or concrete trigger conditions.

4. Belief entries
- Character assumptions and false theories.

5. Fact entries
- Ground truth revealed only by strict conditions.

## Cadence Controls

When supported by frontend/extensions:
- Delay: hide entry until chat reaches progression threshold.
- Sticky: keep activated effect for limited turns.
- Cooldown: prevent repetitive re-triggering.

## Example Workflow

1. Early phase
- Characters act suspicious but vague.

2. Mid phase
- Belief entries generate conflicting theories.

3. Reveal phase
- Fact entry activates on specific trigger.
- Belief entries are updated/downgraded so NPC behavior remains coherent.

## QA Checklist

- Secrets do not leak in early turns.
- Suspicion feels consistent before reveal.
- Reveal conditions are concrete and testable.
- Post-reveal behavior reflects updated knowledge.
