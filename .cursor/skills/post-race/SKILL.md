---
name: post-race
description: Cross one race spoiler boundary and prepare its immediate post-race report and standings.
disable-model-invocation: true
---

# Complete a race

Explicit invocation of this workflow is the user's authorization to cross the
selected race's start boundary. Availability of a result online is never
authorization. The workflow does not authorize knowledge from the next event.

## Invocation

Treat the complete text following `/post-race` as the argument payload. After
trimming surrounding whitespace, require exactly two whitespace-separated
arguments:

- `[YYYY]` matching `^[0-9]{4}$`;
- `[ROUND]` matching `^[0-9]{1,2}$` and representing an integer from 1 through
  99.

Normalize `[ROUND]` to two digits. If validation fails, make no changes and
respond with exactly:

```text
Usage: /post-race [YYYY] [ROUND]
Example: /post-race 1981 01
```

## Canonical preparation and preconditions

Before browsing, researching, or modifying files:

1. Read `AGENTS.md`, the relevant `.cursor/rules/`,
   `docs/temporal-scope.md`, `docs/source-policy.md`,
   `docs/content-contracts.md`, `docs/methodology.md`, and
   `docs/archive-workflow.md`.
2. Read `archive-state.yaml`, season and race metadata, the selected race's
   completed `pre-weekend.md`, `pre-race.md`, existing `sources.md`, the
   previous standings snapshot where applicable, and every needed canonical
   race/shared template.
3. Require `pre-race.md` to be completed or reviewed under canonical statuses,
   with no unresolved reader-facing spoiler-audit issue. A partial source audit
   is sufficient when the cutoff-safe limitations are recorded in
   `things-to-resolve-after-season.md`.
4. Verify state permits `/post-race` for this exact season and round. If not,
   stop and name the expected previous action. If state conflicts with verified
   metadata, report the conflict and do not advance.

Do not overwrite verified, reviewed, complete, or manually populated target
documents. Resume partial work only when all target cutoffs, classifications,
and source records are compatible. Report every skipped file and reason.

## Immediate post-race boundary

Define a clear immediate post-race cutoff in race metadata before drafting.
State exactly which official procedures are included and when the boundary
ends. It may include:

- race completion and the initial classification;
- immediate official steward decisions public by the cutoff;
- podium proceedings and immediate interviews;
- points provisionally or officially awarded by the cutoff;
- contemporary reactions available within the declared boundary.

Exclude the next race weekend, later appeals or rulings not yet public, later
driver replacements, later calendar changes, end-of-season conclusions, later
accidents or conflicts, and retrospective statements such as “this proved
decisive for the championship.” Label classifications and points provisional
whenever that is their status at the cutoff.

Do not require the user to provide missing archival evidence. Omit unsupported
claims or label only supportable uncertainty, then record the concrete evidence
gap in `things-to-resolve-after-season.md`. A later authorized boundary may
resolve it, but must not backfill the earlier document.

Use the `researcher` or `historical-f1-research` workflow for cutoff-safe
evidence, the `source-auditor` or `source-verification` workflow for claim
support, the `spoiler-auditor` or `spoiler-scope-audit` workflow against the
next historical boundary, and the `editor` or `historical-content-editor`
workflow for Polish and repetition after facts are fixed. Use
`race-state-update` for the bounded classification and standings transition.

## Outputs

Populate only the selected race's:

```text
post-race.md
standings-after.md
sources.md
```

and the corresponding post-race fields in `metadata.yaml`. Use canonical
templates and contracts. Preserve all earlier-boundary documents unchanged.

`post-race.md` must provide a concise result summary, selective race narrative,
key phases, classified results or a compact reference to their canonical
section, retirements and then-known causes, team and driver analysis, technical
observations, immediate sporting and political consequences, attributed
contemporary reactions, and unresolved issues. It may summarize major
championship changes but must not duplicate complete standings tables.
Apply the reader-facing presentation in `docs/methodology.md`: keep raw IDs,
ledger links, limitations, and audit status in sparse notes or the final
`Uwagi do źródeł` section, not in the narrative.

`standings-after.md` is the sole canonical location for complete driver and
constructor standings at this boundary. Calculate points using the historically
correct scoring, eligibility, counting-result, and tie-breaking rules. Verify
the classification status and calculations independently against cutoff-safe
official evidence. Never backdate a later correction.

Update the existing race `sources.md` ledger without duplicate entries. Advance
its cutoff only to the declared post-race boundary and quarantine later-bearing
sources as required by `docs/source-policy.md`.

Run:

- exact claim-level source audit;
- adversarial spoiler audit against the next historical cutoff;
- cross-document repetition audit;
- independent standings, arithmetic, eligibility, counting-result, tie-break,
  and provisional-status verification;
- metadata, contradiction, and Polish-language checks.

Advance statuses only when actual results allow it.
Partial source status does not block progression when all reader-facing claims
remain cutoff-safe and the season ledger records the outstanding evidence.

## State transition

After successful completion, update `archive-state.yaml` in place using only
its canonical schema:

- mark this event through `current_stage: post-race`, the active season/round,
  verified cutoff, and `last_completed_document`;
- if a next round was already historically known by this cutoff, set
  `active_round` to it and `next_allowed_action` to
  `/pre-weekend [SEASON] [NEXT_ROUND]`;
- do not research, scaffold, or generate that next brief unless a calendar
  change newly knowable at this boundary requires only canonical empty
  scaffolding;
- if no next round was known, use only the state permitted by the current
  schema and report the blocked or season-end condition.

Do not infer the user has watched another race. For the final scheduled or
actually completed round, do not generate a season retrospective or mark
`season-complete` unless a separate explicit task defines and authorizes that
boundary. Never commit or push historical content automatically.

## Completion response

Report the event and post-race cutoff, classification status, files created or
updated, skipped files and reasons, unresolved source/classification issues,
source/spoiler/repetition/standings audit results, state change, and the next
permitted command if one is historically known.
