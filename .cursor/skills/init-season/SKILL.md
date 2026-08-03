---
name: init-season
description: Initialize an empty Formula 1 season from the repository's canonical templates.
disable-model-invocation: true
---

# Initialize season

This is a manually invoked, structure-only workflow. Do not research, browse for,
or draft historical content.

## Invocation

Treat the complete text following `/init-season` as the argument payload. After
trimming surrounding whitespace, require exactly one argument matching
`^[0-9]{4}$`. Do not infer a season from repository files or state.

If validation fails, make no changes and respond with exactly:

```text
Usage: /init-season [YYYY]
Example: /init-season 1981
```

Use the validated argument as `[SEASON]`.

## Required preparation

Before modifying any file:

1. Read `AGENTS.md`, all relevant `.cursor/rules/`,
   `docs/content-contracts.md`, `docs/archive-workflow.md`,
   `docs/temporal-scope.md`, and `docs/source-policy.md`.
2. Read `archive-state.yaml` and every canonical template needed from
   `templates/season/`.
3. Treat the current canonical rules, documents, templates, metadata schema,
   and archive-state workflow as authoritative over this skill.
4. Confirm that every required canonical input exists. If an input or template
   is missing, stop without modifying files and report the missing canonical
   input. Never synthesize a replacement.

The required destination scaffold is:

```text
archive/seasons/[SEASON]/
├── README.md
├── metadata.yaml
├── things-to-resolve-after-season.md
└── season/
    ├── prelude.md
    ├── context.md
    ├── regulations.md
    ├── technology.md
    ├── teams.md
    ├── drivers.md
    ├── people-and-organisations.md
    ├── calendar.md
    └── glossary.md
```

Use this canonical template-to-destination map:

| Template | Destination under `archive/seasons/[SEASON]/` |
| --- | --- |
| `README.template.md` | `README.md` |
| `metadata.template.yaml` | `metadata.yaml` |
| `things-to-resolve-after-season.template.md` | `things-to-resolve-after-season.md` |
| `prelude.template.md` | `season/prelude.md` |
| `context.template.md` | `season/context.md` |
| `regulations.template.md` | `season/regulations.md` |
| `technology.template.md` | `season/technology.md` |
| `teams.template.md` | `season/teams.md` |
| `drivers.template.md` | `season/drivers.md` |
| `people-and-organisations.template.md` | `season/people-and-organisations.md` |
| `calendar.template.md` | `season/calendar.md` |
| `glossary.template.md` | `season/glossary.md` |

## Preflight protection

Before creating or changing anything:

1. Check whether `archive/seasons/[SEASON]/` exists.
2. If it exists, do not overwrite, reset, recreate, or repair anything. Report
   that the season is already initialized and list any missing files from the
   expected scaffold. Repair only in response to a separate explicit request.
3. Inspect `archive-state.yaml` using its exact current schema and workflow.
   If it records a different active season, stop without modifying files and
   explain the conflict. Never silently replace another active season.
4. Determine whether the canonical schema permits the requested state
   transition. Do not invent fields or enum values.
5. Record the pre-existing paths so validation can prove that nothing was
   overwritten.

## Initialize the scaffold

Instantiate every required file from its canonical template. Copy template
structure and content; do not independently author equivalent files.

Replace only safe structural placeholders authorized by the canonical
templates and schemas:

- replace `[SEASON]` with the validated four-digit season;
- set the canonical future-content language field or placeholder to `pl`, as
  required by the canonical metadata schema.

Leave every historical field unresearched, unresolved, `null`, or at its
canonical placeholder. In particular, do not infer or invent a preseason
knowledge cutoff. Do not replace any other placeholder merely because a likely
value seems obvious.

Create no files or directories beyond the expected season scaffold and any
parent directories required to contain it. Do not create race directories.

## Archive state

After the scaffold is successfully instantiated, update `archive-state.yaml`
only when the canonical schema and workflow permit it. Edit the existing
document in place, preserving its structure and unrelated fields; never replace
it with an example or reconstructed state.

Use the exact existing field names and enum values to express:

```yaml
active_season: [SEASON]
active_round: null
current_stage: season-prelude
knowledge_cutoff: null
last_completed_document: null
next_allowed_action: generate-season-prelude
```

If the canonical schema does not permit this update, leave
`archive-state.yaml` unchanged and report that fact. A different active season
is a blocking conflict and must have stopped the workflow during preflight.

## Strict exclusions

Do not:

- research the season or browse for historical information;
- insert driver, team, race, or circuit names;
- insert dates other than the season identifier;
- insert regulations, technical facts, results, standings, or summaries;
- assume an announced or final calendar;
- generate source entries;
- create race directories or any race structure.

This workflow initializes structure only.

## Validation

Before reporting completion, verify all of the following:

- the validated season argument was used everywhere `[SEASON]` was safely
  replaced;
- every scaffold file is traceable to its canonical template and differs only
  by authorized structural substitutions;
- all generated YAML metadata parses correctly and conforms to the canonical
  metadata schema;
- every required scaffold file exists;
- no race directory or extra structure was created;
- no historical fact or non-season date was introduced;
- no pre-existing file was overwritten;
- `archive-state.yaml` is valid and changed only as the canonical workflow
  permits.

If validation fails, report the failure accurately; do not claim successful
initialization.

## Completion response

After successful validation, respond concisely with only:

1. initialized season;
2. created files;
3. archive-state change;
4. validation result;
5. confirmation that no historical research or race structure was generated.
