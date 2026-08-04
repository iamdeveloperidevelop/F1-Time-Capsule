# Agent task recipes

These natural-language contracts are starting points. Replace bracketed tokens,
keep the requested cutoff explicit, and do not combine sequential stages unless
the task says so.

## Initialize a season

```text
Initialize season [SEASON] using the repository templates.
Do not research or generate historical content yet.
Create only the directory structure, metadata, and empty document files.
Leave archive document statuses at planned, unstarted, and not-run.
Do not create race folders beyond rounds explicitly supplied in this task.
Do not claim an unverified knowledge cutoff. Suggest one explicit next command
in the reply rather than writing any global workflow state.
```

## Generate a season prelude

```text
Generate the season prelude for [SEASON].
Use the season-prelude contract and set the exact cutoff to [KNOWLEDGE CUTOFF].
Research only information publicly knowable by that boundary.
Run source verification and a spoiler audit; preserve unresolved conflicts.
Do not require the user to find missing historical evidence. Omit unsupported
claims or state only supportable uncertainty, then add each concrete gap to
things-to-resolve-after-season.md.
Do not use any in-season knowledge.
```

## Initialize one race folder

```text
Initialize round [ROUND], [GRAND PRIX], under season [SEASON].
Use templates/race/ and create metadata plus empty race documents only.
Do not research, draft, or infer any weekend information.
Do not initialize another round.
```

## Generate a pre-weekend brief

```text
Generate pre-weekend.md for [SEASON], round [ROUND], [GRAND PRIX].
The cutoff is immediately before the first official session: [KNOWLEDGE CUTOFF].
Use standings-after.md from the previous completed event as the standings source.
Research only information knowable by the cutoff, verify sources, and run a
spoiler audit. Exclude all session information from this weekend. Record missing
archival evidence in things-to-resolve-after-season.md; do not block the
transition solely because source status is partial.
```

## Generate a pre-race brief after qualifying

```text
Generate concise pre-race.md for [SEASON], round [ROUND], [GRAND PRIX].
The cutoff is immediately before the scheduled race start: [KNOWLEDGE CUTOFF].
Include only completed pre-race sessions, the grid, and decisions or conditions
publicly known by the cutoff. Link season references instead of repeating them.
Run source verification and a spoiler audit. Record unresolved evidence in
things-to-resolve-after-season.md rather than asking the user to verify it. Do
not research or reveal the race.
```

## Generate a post-race report

```text
Generate post-race.md for [SEASON], round [ROUND], [GRAND PRIX].
The cutoff is [KNOWLEDGE CUTOFF], after the race and only the immediate official
process defined in metadata.yaml.
Use only evidence public by that boundary. Keep full standings in
standings-after.md, preserve unresolved matters, and run spoiler, source, and
repetition audits. Do not research the next event.
```

## Update standings

```text
Update standings-after.md for [SEASON], round [ROUND], [GRAND PRIX], as of
[KNOWLEDGE CUTOFF].
Verify classifications, points, eligibility, counting-result rules, ties, and
provisional issues independently against cutoff-safe sources.
Do not import later corrections. Do not duplicate the full tables elsewhere.
```

## Audit a document for spoilers

```text
Audit [DOCUMENT PATH] in report-only mode using its declared cutoff and content
contract.
Check direct and indirect spoilers, hindsight, dramatic foreshadowing, later
terminology, later-race or later-season knowledge, and final-outcome influence.
Do not widen the cutoff or disclose unnecessary future facts in the report.
```

## Audit a document for sources

```text
Audit [DOCUMENT PATH] and its source ledger against docs/source-policy.md.
Verify exact claim support, source identity, publication and event dates,
locators, contemporaneity, access dates, spoiler risk, and disagreements.
Return gaps and a source-status recommendation without adding new claims.
```

## Reduce duplication

```text
Review [DOCUMENT PATHS] for repeated background, tables, quotations, and
technical explanations.
Keep each detailed fact in its canonical primary home, replace secondary copies
with concise context and links, and preserve every document's cutoff.
Do not add, remove, or strengthen factual claims.
```
