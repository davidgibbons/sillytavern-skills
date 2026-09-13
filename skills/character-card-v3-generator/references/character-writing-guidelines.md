# Character Writing Guidelines

## Goal

Make the model produce stable, vivid, and controllable behavior over long chats.

## Core Principles

- Define identity as behavior, not adjectives.
- Separate hard constraints from style flavor.
- Prefer specific examples over abstract descriptions.
- Keep each field focused on one job.
- Use external reference material (wiki/tropes/archetype sources) as draft input, then manually prune to only behavior-relevant facts.

## Causal Construction (Build an Engine, Not a Hairball)

A trait list ("loyal, sarcastic, secretly insecure") gives the model nothing to reason from. A trait with a cause gives it a chain to follow and extend.

- Chain every trait to a cause and an effect: `trait -> why -> observable behavior`. Example: speech impediment -> fell off a cliff as a child -> repeats himself when startled.
- Cross-link traits instead of listing them in isolation. Traits sharing a cause (a betrayal, a loss, a rule broken) should reference that cause from more than one field, so the model can pull the connection from whichever angle the conversation approaches it.
- Anchor one specific, unresolved memory instead of narrating a whole backstory. A concrete sensory detail or line of dialogue carries more weight than a paragraph of exposition and gives the model something to reuse verbatim.
- Leave real tension unresolved. A character torn between two loyalties, or holding a belief they haven't fully tested, produces more varied dialogue than one whose arc is already settled — resolving everything removes the friction that makes responses vary turn to turn.
- Repeat the load-bearing cause across fields (`personality`, `scenario`, `mes_example`) rather than stating it once. Under context pressure, not every field survives; an anchor stated only once can be dropped entirely.

## Field-by-Field Guidance

- `description`
  - State role, context, and baseline competence.
  - Avoid dense backstory dumps unless they affect behavior.

- `personality`
  - List persistent drives, speech style, and boundaries.
  - Include conflict-handling style and fail-state behavior.

- `scenario`
  - Anchor initial world state and current stakes.
  - Define what is true now, not the whole universe history.
  - Treat `description` + `personality` + `scenario` as high-cost permanent context in many runtimes; keep them dense and intentional.

- `first_mes`
  - Show voice and pacing immediately.
  - Include one concrete hook for user response.
  - In many clients, this strongly anchors future response length/style.

- `mes_example`
  - Demonstrate desired format and tone.
  - Keep examples representative of normal chat behavior.
  - Prefer multiple examples covering different emotional states and message lengths.
  - Assume examples may be dropped under context pressure; each block should be independently useful.

- `system_prompt` / `post_history_instructions`
  - Use for strict behavioral constraints and output rules.
  - Avoid repeating content already enforced in other fields.

## ST Runtime Notes (Important)

- Permanent token pressure is usually dominated by always-on fields (`description`, `personality`, `scenario`).
- `first_mes` is typically sent once at chat start.
- Example dialogue blocks are often included opportunistically and can be pushed out as context fills.
- Keep core behavior in always-on fields and use examples for style reinforcement, not sole rule storage.

## Quality Checklist

- Character can be summarized in 3-5 stable behavioral traits.
- Traits are testable in dialogue.
- Values and boundaries remain consistent across turns.
- Message style matches intended chat cadence.
- No contradictory instructions across fields.
- Appearance/personality tags are concrete enough for the model to act on without guesswork.
- Every trait traces back to a stated cause, not just an adjective.
- At least one real tension or contradiction remains unresolved — the arc isn't fully settled.

## Anti-Patterns

- Overlong prose that adds no behavioral signal.
- Duplicate constraints repeated in many sections.
- Purely aesthetic traits without actionable behavior.
- Contradictions between tone, goals, and scenario stakes.
- Trait lists with no causal chain — arbitrary adjectives nothing else in the card references.
- A fully resolved backstory or arc that leaves no friction for dialogue to explore.

## Practical Additions From Community Threads

- Add explicit sections for: backstory, likes/dislikes, goals/fears, quirks, skills, worldview, and speech mannerisms.
- Prefer tiered preferences when useful (for example, strongly likes vs mildly likes) to avoid binary behavior.
- Use example dialogue to anchor voice and formatting, especially for group-chat differentiation.
- Avoid one giant paragraph card structure when precision and stability matter.

## Optional Technique: Hidden XML Comment State

Pattern:

```xml
<!-- HIDDEN: brief note -->
```

Potential uses:
- Foreshadowing cues.
- Unperceived environment details.
- Ongoing hidden state transitions.
- NPC off-screen actions and motives (must remain in-character).

Guidelines:
- Keep notes brief, factual, and behavior-relevant.
- Never store real secrets or sensitive data.
- Ensure hidden notes do not contradict visible narrative.
- Prefer one short note per turn over dense hidden logs.

Caveats:
- \"Hidden\" means hidden from normal rendered view, not guaranteed hidden from logs/tools.
- Some frontends or transforms may strip comments.
- Models may still leak hidden notes into visible text unless constrained and tested.
