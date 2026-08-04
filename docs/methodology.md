# Historical content methodology

This workflow applies when a later phase authorizes historical research or
content. The temporal model is canonical in `temporal-scope.md`; evidence rules
are canonical in `source-policy.md`.

## Workflow

1. Select the content contract and write its metadata before research.
2. Fix the event time, public-knowledge time, and hard knowledge cutoff.
3. List needed claims and source types without searching for later outcomes.
4. Build claim-to-source records and preserve conflicts.
5. Draft only from the scoped evidence set.
6. Audit direct spoilers, hindsight, foreshadowing, and later-informed emphasis.
7. Audit claims against citations and dates.
8. Edit language and structure without widening factual scope.
9. Run a redundancy audit and update workflow statuses.

The applicable skills in `.cursor/skills/` provide operational checklists.

## Language and style

Historical content defaults to natural Polish unless a task explicitly requests
another language. Filenames, directory names, metadata keys, rule and skill
names, and technical repository documentation remain English. Use UTF-8.
Preserve names, accents, and diacritics accurately; retain original-language
names for people, teams, organisations, cars, races, and technical concepts
when appropriate.

Write clear, precise, informative prose that is engaging without manufactured
drama. Be technically accurate, understandable to a non-engineer, respectful of
historical participants, explicit about uncertainty, and free from hindsight
and unnecessary repetition.

Avoid clickbait, exaggerated narration, fake quotations, empty phrases,
repetitive summaries, literary foreshadowing, certainty unsupported by evidence,
present-day moral certainty without historical context, and excessive lists
where prose is clearer. Explain a technical concept at its first meaningful
appearance and refer to it concisely later. Use period units when useful and add
a metric clarification where needed.

## Deduplication and navigation

Each fact has one primary home:

- detailed technology explanations in technology reference material;
- full biographies in driver reference material;
- full organisational histories in team reference material;
- event documents linking to or briefly summarising those references;
- concise glossary definitions;
- post-race reports advancing the story instead of restating the full prelude;
- full driver and constructor standings tables only in the event's
  `standings-after.md`; reports give brief context and link to that snapshot.

A document may repeat a key fact needed for comprehension, but must summarise
rather than reproduce the original explanation. Before completion, search
related documents for repeated background, tables, quotations, and technical
explanations; choose a primary home and replace secondary copies with concise
context and links.

Future content must support two reading modes:

1. sequentially, from the season opening through each event boundary; and
2. selectively, through event, team, driver, technology, or reference material.

This requires self-contained orientation without turning every document into a
complete recap. Links and short contextual summaries bridge the two modes.
