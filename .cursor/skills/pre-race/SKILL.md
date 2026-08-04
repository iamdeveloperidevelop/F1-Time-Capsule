---
name: pre-race
description: Prepare a concise race-start brief using only information known before the scheduled start.
disable-model-invocation: true
---

# Prepare for the race start

This manually invoked workflow authorizes historical work only through the
instant immediately before the selected race's scheduled start.

## Invocation

Treat the complete text following `/pre-race` as the argument payload. After
trimming surrounding whitespace, require exactly two whitespace-separated
arguments:

- `[YYYY]` matching `^[0-9]{4}$`;
- `[ROUND]` matching `^[0-9]{1,2}$` and representing an integer from 1 through
  99.

Normalize `[ROUND]` to two digits. If validation fails, make no changes and
respond with exactly:

```text
Usage: /pre-race [YYYY] [ROUND]
Example: /pre-race 1981 01
```

## Canonical preparation and preconditions

Before browsing, researching, or modifying files:

1. Read `AGENTS.md`, the relevant `.cursor/rules/`,
   `docs/temporal-scope.md`, `docs/source-policy.md`,
   `docs/content-contracts.md`, `docs/methodology.md`, and
   `docs/archive-workflow.md`.
2. Read `archive-state.yaml`, season and race metadata, the selected race's
   `pre-weekend.md` and `sources.md`, related canonical season references, and
   the canonical `templates/race/pre-race.template.md`.
3. Require `pre-weekend.md` to be completed or reviewed under canonical
   statuses, with no unresolved reader-facing spoiler-audit issue. A partial
   source audit is sufficient when the document's cutoff-safe limitations are
   recorded in `things-to-resolve-after-season.md`.
4. Verify that state permits `/pre-race` for this exact season and round. If it
   does not, stop and name the expected previous action. If state conflicts
   with verified metadata, report the conflict rather than widening scope.

Do not overwrite a verified, reviewed, complete, or manually populated
`pre-race.md`. Resume partial work only when its declared cutoff and evidence
records are compatible; report every skipped file and reason.

## Knowledge boundary

Determine the historically appropriate weekend format; never impose modern
session names or ordering. Establish and record the exact boundary immediately
before the scheduled race start, including local time and zone when reliably
available. If precision cannot be verified, record the narrowest supported
descriptive boundary and uncertainty. Do not guess.

Depending on the period and what was public by the cutoff, allowed material can
include:

- free practice, timed practice, pre-qualifying, qualifying, and warm-up;
- the starting grid and officially confirmed grid penalties;
- officially confirmed withdrawals;
- known setup and reliability concerns;
- tyre choices publicly known before the start;
- track and weather conditions;
- contemporary quotations;
- championship context before the start.

Exclude race-start incidents, formation-lap developments occurring after the
declared cutoff, race results, retirements, post-race penalties, later appeals,
future significance, and any viewing cue shaped by knowledge of the result.

Do not require the user to provide missing archival evidence. Omit an
unsupported claim or record only the supportable uncertainty, then add the
specific evidence gap to `things-to-resolve-after-season.md`.

Use the existing researcher, source-auditor, spoiler-auditor, and editor roles
or their corresponding helper skills. Keep the verified claim set fixed during
language editing.

## Output and state

Populate only the selected race's:

```text
pre-race.md
```

plus the compatible `pre_race` field in race `metadata.yaml` and deduplicated
source entries in its canonical `sources.md`. Preserve `pre-weekend.md` and all
later-stage documents unchanged. Do not generate the race result.

Use `templates/race/pre-race.template.md` and its canonical content contract.
Keep the brief concise and ready for a reader about to watch the race. Do not
repeat full biographies, team histories, technology explanations, the entire
`pre-weekend.md`, or full championship tables stored elsewhere.

End the main narrative with the Polish heading:

```text
CO MUSZĘ WIEDZIEĆ PRZED STARTEM
```

and no more than 12 short points.

Then add the final `Uwagi do źródeł` section required by the template. Apply
the reader-facing presentation in `docs/methodology.md`: use sparse notes and
keep raw IDs, ledger links, limitations, and audit status out of the narrative.

Run metadata, source, spoiler, contradiction, Polish-language, and repetition
audits. Advance statuses only when the actual results support them. Partial
source status is compatible with progression when reader-facing claims are
cutoff-safe and the season ledger records what remains unresolved.

After successful completion, update `archive-state.yaml` in place using only
its canonical schema:

- active season and round identify this event;
- `current_stage` is `pre-race`;
- `knowledge_cutoff` is this document's verified pre-start cutoff or narrowest
  supported descriptive boundary;
- `last_completed_document` is this `pre-race.md`;
- `next_allowed_action` is `/post-race [SEASON] [ROUND]`.

Do not generate or research `post-race.md`. Never commit or push historical
content automatically.

## Completion response

Report the event and cutoff, files created or updated, files skipped and
reasons, unresolved issues, source/spoiler/repetition audit results, state
change, and `/post-race [SEASON] [ROUND]` as the next command.
