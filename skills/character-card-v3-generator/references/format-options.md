# Character Format Options

This file summarizes commonly used character-writing formats and when to use them.

Important:
- CCv3 does not require one authoring format inside text fields.
- These are authoring styles for `description`, `personality`, `scenario`, and examples.
- Choose format based on target model behavior, token budget, and maintainability.

## Quick Comparison

| Format | How it looks | Best for | Risks |
|---|---|---|---|
| Prose | Natural paragraphs | Rich style, nuanced characterization | Can bloat tokens if verbose |
| Attributes | Labeled fields (`Name:`, `Traits:`, etc.) | Precision, editability, predictable behavior | Can feel rigid or list-like |
| AliChat | Dialogue/example-heavy card style | Strong voice anchoring and response-style imitation | Requires good examples; weaker if examples are noisy |
| JED / JED+ | Compact "just enough" structured definition (community style) | Low-token cards, fast iteration, clarity | No canonical spec; variants differ by community |
| Plaintext | Minimal direct statements | Very low token cost, baseline robustness | Less expressive style control |
| W++ | Bracket/quote-heavy symbolic formatting | Legacy compatibility only | Often token-inefficient and less natural for many models |

## Prose

How to use:
- Write natural, concrete paragraphs describing behavior, motivations, voice, and constraints.
- Keep each paragraph focused (identity, behavior, scenario, speaking style).
- Pair with high-quality `mes_example` snippets.

Best for:
- Character-driven chats with nuanced tone and voice.
- Models that follow natural-language instructions well.

## Attributes

How to use:
- Use labeled sections with concise values.
- Keep labels stable and meaningful (for example: role, goals, boundaries, tone, style).
- Avoid over-fragmentation into too many micro-fields.

Best for:
- Cards that need easy maintenance and explicit control.
- Collaborative editing where consistency matters.

## AliChat

How to use:
- Encode key character details through representative dialogue/exchanges.
- Use varied examples (neutral, conflict, emotional, planning).
- Keep examples close to your intended runtime output style.

Best for:
- Voice fidelity and conversational rhythm.
- Situations where output form matters as much as facts.

## JED / JED+

How to use:
- Keep a concise, high-signal definition with only behavior-relevant facts.
- Include clear constraints, motivations, and speaking cues.
- Pair with one strong first message and a few examples.

Best for:
- Token-sensitive cards.
- Rapid prototyping and iteration.

Note:
- JED/JED+ is a community convention, not a formal spec. Field shape varies by guide.

## Plaintext

How to use:
- Write direct statements with minimal formatting overhead.
- Keep sections short and unambiguous.

Best for:
- Low-context or low-token environments.
- Baseline cards where reliability is more important than rich style.

## W++

How to use:
- Only when required for compatibility with older workflows.

Best for:
- Legacy cards that already rely on this format.

Caution:
- Commonly criticized as token-heavy and less aligned with natural training text.

## Practical Selection Strategy

1. Start with `Attributes` or `JED` for control and compactness.
2. Add `Prose` where style nuance is missing.
3. Use `AliChat` examples when voice consistency is weak.
4. Add scoped regex post-processing only if formatting drift remains.

## Sources

- SillyTavern NovelAI docs (format fit notes, prose/attributes examples, AliChat/W++ comments):
  - https://docs.sillytavern.app/usage/api-connections/novelai/
- Community summary mentioning JED and plaintext as recommended templates:
  - https://jannyai.com/characters/2856e071-a071-4b28-a2e2-8fbbccd79be5_character-bot-maker
