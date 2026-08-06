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

### Published voice

Write as a motorsport journalist living in that historical moment—Autosport,
*Motor Sport*, or *Grand Prix International*, not an AI explaining a spoiler
policy. Always write naturally from the historical point of view. Never explain
that you are writing from that point of view.

The anti-spoiler cutoff is an **internal generation rule**. It must never appear
in published prose as commentary about spoilers, future knowledge, “what readers
did not yet know,” “only an expectation,” “not the outcome,” “provisional for
the archive,” or similar meta framing. Omit forbidden future information
completely; do not announce the omission.

**Show, don't explain.** Prefer attributed contemporary narration:

- “The paddock expected…” / „W paddocku spodziewano się…”
- “Teams believed…” / „Zespoły uważały…”
- “Engineers were concerned…” / „Inżynierowie obawiali się…”
- “Rumours suggested…” / „Plotki głosiły…”
- “Many observers thought…” / „Wielu obserwatorów sądziło…”

instead of explaining why something is uncertain (“this was only an
expectation,” “this remained provisional as a knowledge limit,” “this is not
the result”). Let the reader infer uncertainty from natural attribution and
from factual status language that a contemporary reporter would use (“the
protest remained under appeal,” “the classification was still provisional”).

Do not open reader-facing documents with a “knowledge boundary,” “Granica
wiedzy,” or similar meta section that restates the sibling `.meta.yaml`.
`knowledge_cutoff`, `event_time`, `public_knowledge_time`, and `spoiler_scope`
already live there. Spoiler-audit results belong in `spoiler_audit_status`
(and, when needed, a separate audit record using
`templates/shared/spoiler-audit.template.md`), not as a closing reader section.
Do not put “Granica wiedzy,” cutoff restatements, or spoiler-policy notes in
`## Uwagi źródłowe` either—keep those fields in YAML and internal ledgers.

### Prose quality

Write clear, precise, informative prose that is engaging without manufactured
drama. Be technically accurate, understandable to a non-engineer, respectful of
historical participants, and free from hindsight and unnecessary repetition.
The main text should read as continuous narrative or reference prose, not as a
research log.

Keep uncertainty, source limits, claim identifiers, and ledger links out of the
running text. When a caveat is needed, mark the sentence with a short footnote
marker (`*¹`, `*²`, …) and explain it once under a closing `## Przypisy`
section—as a source or status note a careful journalist might give, not as a
lecture on temporal scope. Put claim/source maps, status lines, and detailed
citation records in `## Uwagi źródłowe`, `sources.md`, or the season open-items
ledger — not inside paragraphs the reader is meant to follow.

State the best-supported account cleanly. Prefer one brief footnote over
repeated hedging such as “nie potwierdza”, “luka dowodowa”,
“separowalna informacja”, “brak daty dziennej blokuje użycie”, “oczekiwanie,
nie fakt”, “nie wynik”, or “według późniejszej relacji” in every sentence.
Factual provisionality of a classification or appeal may be stated once in
natural sporting language. An unknown exact publication day for clearly
pre-cutoff contemporary material belongs in at most one short source note, not
as a reason to strip the field or expectations section down to a single team.
If nothing usable can be said without inventing certainty, omit the point from
the main text rather than narrating the absence of evidence. Preserve conflicts
and open gaps in footnotes and ledgers; never resolve them silently.

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
