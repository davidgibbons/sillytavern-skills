# Source Notes (One-Time Harvest)

These notes capture guidance harvested once from linked community pages. Use as heuristics, not hard spec rules.

## Character quality themes

- Build cards with explicit structure (identity, motivations, boundaries, speaking style, examples).
- Use multiple example messages to anchor tone and response format.
- Keep descriptions behavior-focused; remove decorative text that does not influence output.
- Popular cards often succeed through strong first-turn hooks, clear archetypes, and highly scannable section structure.

## Lorebook quality themes

- Keep entries short and focused; split long entries.
- Use specific triggers, then broaden only when recall is too low.
- Tune activation depth and budget before adding entry volume.
- Treat lorebooks as dynamic guidance for scenario state, not just static encyclopedia entries.
- Prefer iterative improvement from observed chat failures.
- For world cards, deep setting context is better in conditional lorebook entries than in always-on base fields.

## Additional official best-practice notes

- Lorebook entry `content` must be self-contained because keywords/titles are not injected into prompt text.
- Use optional filters and inclusion groups to improve trigger precision before adding many new keys.
- Keep permanent card fields concise (`description`, `personality`, `scenario`) to preserve context window for chat history.
- Keep app-specific features in `data.extensions` for compatibility across CCv3 frontends.
- For regex transforms, scope narrowly by placement/depth and test on representative samples.
- Structured-output plus regex decoration can improve consistency while reducing repeated formatting instructions in prompts.
- XML comments (for example, `<!-- HIDDEN: ... -->`) can track hidden state, but require leak testing and frontend compatibility checks.
- Format choice matters: prose/attributes/alichat each trade off style richness vs. control vs. token cost.
- Card packaging and assets matter: PNG/APNG embedding, CHARX `card.json`, and URI strategy directly affect portability.
- Formal review rubrics improve iteration speed by separating structural, behavioral, and portability failures.
- ST character design notes reinforce token economics: always-on fields consume persistent context, while first-message/examples are less persistent.
- Macro-style trigger markers and layered lore modules can improve consistency for complex scenario logic when kept modular and testable.

## Links

- https://www.reddit.com/r/SillyTavernAI/comments/1j5fes0/model_tips_tricks_character_card_creation/
- https://www.reddit.com/r/SillyTavernAI/comments/1nbmep3/need_help_making_a_lorebook/
- https://www.reddit.com/r/NovelAi/comments/17o7rco/how_do_you_write_a_lorebook_entry/
- https://www.reddit.com/r/NovelAi/comments/18l4ni1/tips_for_text_adventure_lorebook_stuff/
- https://www.reddit.com/r/SillyTavernAI/comments/1lcmte5/how_can_i_utilize_lorebook_to_it_full_potential/
- https://huggingface.co/sphiratrioth666/Lorebooks_as_ACTIVE_scenario_and_character_guidance_tool
- https://docs.sillytavern.app/usage/core-concepts/worldinfo/
- https://docs.sillytavern.app/usage/core-concepts/characterdesign/
- https://docs.sillytavern.app/extensions/regex/
- https://docs.sillytavern.app/usage/core-concepts/macros/
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions#advanced_searching_with_flags
- https://docs.sillytavern.app/usage/api-connections/novelai/
- https://docs.sillytavern.app/usage/core-concepts/characterdesign/
- https://jannyai.com/characters/2856e071-a071-4b28-a2e2-8fbbccd79be5_character-bot-maker
- https://github.com/kwaroran/character-card-spec-v3/tree/main
