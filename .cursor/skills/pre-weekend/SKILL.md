---
name: pre-weekend
description: Prepare one race-weekend brief at the boundary before its first official session.
disable-model-invocation: true
---

# Prepare a race weekend

This manually invoked workflow authorizes historical work only through the
selected event's pre-weekend cutoff. Do not read or write any global workflow
state file.

## Invocation

Treat the complete text following `/pre-weekend` as the argument payload. After
trimming surrounding whitespace, require exactly two whitespace-separated
arguments:

- `[YYYY]` matching `^[0-9]{4}$`;
- `[ROUND]` matching `^[0-9]{1,2}$` and representing an integer from 1 through
  99.

Normalize `[ROUND]` to two digits before resolving paths. If validation fails,
make no changes and respond with exactly:

```text
Usage: /pre-weekend [YYYY] [ROUND]
Example: /pre-weekend 1981 01
```

## Canonical preparation and preconditions

Before browsing, researching, or modifying files:

1. Read `AGENTS.md`, the relevant `.cursor/rules/`,
   `docs/temporal-scope.md`, `docs/source-policy.md`,
   `docs/content-contracts.md`, `docs/methodology.md`, and
   `docs/archive-workflow.md`.
2. Read season metadata, `season/calendar.md`, every race folder candidate for
   the normalized round, and the canonical race templates.
3. Verify that the season exists and its preseason package has a declared
   cutoff (or the narrowest supported descriptive boundary) in season
   metadata. A `source_status: partial` season package is sufficient when its
   reader-facing content has no unresolved spoiler-audit issue and its gaps are
   recorded in `things-to-resolve-after-season.md`.
4. For rounds after 01, require the previous completed race's canonical
   `standings-after.md` on disk. Inspect its metadata status and unresolved
   classification issues. Do not reconstruct prior standings from later
   sources. If that snapshot is missing, stop and name
   `/post-race [SEASON] [PREV_ROUND]` (or the missing prerequisite) as the
   expected previous action.
5. Reject only when on-disk prerequisites or the target cutoff are wrong—not
   because another season or round is in progress elsewhere. Do not proceed out
   of sequence for this round without an explicit instruction that names the
   intended exceptional transition and cutoff.

If the race folder is absent because the event became publicly knowable only
after the preseason cutoff, first verify when the calendar change became
knowable. Initialize exactly one race folder from `templates/race/`, preserving
its then-current status and avoiding duplicates by round and metadata identity.
Do not import later calendar knowledge or populate any later-stage document.

Do not overwrite a verified, reviewed, complete, or manually populated
`pre-weekend.md`. Resume partial work only when its metadata and cutoff are
compatible; otherwise stop and report the conflict.

## Knowledge boundary and research

Establish the historically precise cutoff immediately before the selected
weekend's first official session. Determine the actual period-appropriate
weekend format and local time where reliable evidence permits it. If exact time
cannot be verified, use a precise descriptive boundary and record uncertainty;
never guess.

Only information publicly knowable by that cutoff is allowed, including:

- standings after the previous completed event;
- developments public since that event;
- confirmed entries, withdrawals, and replacements;
- circuit briefing;
- weather expectations available before the weekend;
- known technical updates;
- sporting, political, and organisational context;
- attributed contemporary expectations and open questions.

Exclude all information from the first official session onward, including
practice, qualifying, grid, race, later rulings, and later-event knowledge.

Write a readable race prelude in a contemporary motorsport-journalist voice, not
a skeletal bulletin and not a reminder of the anti-spoiler rule. Cover the field
and paddock expectations through natural attribution (“W paddocku spodziewano
się…”); never label claims as “only an expectation / not the outcome.” Do not
narrow the weekend to the few drivers with hard-dated wire announcements if a
broader preseason survey exists (content-based availability). Omit hollow
sections that only cross-link season references without adding weekend context.

Do not require the user to find missing archival evidence. If an exact time,
entry, forecast, circuit detail, or other fact cannot be verified, use only the
narrowest supportable wording with a footnote, or omit it, then add a concrete open item to
the season's `things-to-resolve-after-season.md` ledger.

Use the `researcher` or `historical-f1-research` workflow for evidence
collection, the `source-auditor` or `source-verification` workflow for exact
claim support, the `spoiler-auditor` or `spoiler-scope-audit` workflow in
adversarial mode, and the `editor` or `historical-content-editor` workflow for
Polish and deduplication after factual review.

## Output

Populate only:

```text
archive/seasons/[SEASON]/races/[ROUND]-[slug]/pre-weekend.md
```

plus the existing race `metadata.yaml` cutoff field and deduplicated entries in
the canonical race `sources.md` ledger needed to support this document. Use the
canonical template and contract. Preserve all other race documents unchanged;
do not generate `pre-race.md`, `post-race.md`, or standings.

Run metadata, source, spoiler, contradiction, Polish-language, and repetition
audits. Link to canonical season references and the previous standings snapshot
instead of copying full biographies, histories, technical explanations, or
tables. Advance statuses only when the actual audits permit it. A partial source
audit does not block this transition if all reader-facing claims are
cutoff-safe and the ledger records the missing evidence; a spoiler-audit issue
does block it until remediated.

Leave progress encoded only in these files and their metadata. Do not write any
global workflow pointer. Suggest `/pre-race [SEASON] [ROUND]` in the reply.

Do not generate or research the next stage. Never commit or push historical
content automatically.

## Completion response

Report the event and cutoff, files created or updated, files skipped and
reasons, unresolved evidence or calendar issues, source/spoiler/repetition audit
results, and `/pre-race [SEASON] [ROUND]` as the suggested next command.
