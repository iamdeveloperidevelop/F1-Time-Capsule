---
name: init-season
description: Initialize an empty Formula 1 season from the repository's canonical templates.
disable-model-invocation: true
---

# Initialize season

This is a manually invoked, structure-only workflow. Do not research, browse for,
or draft historical content. Do not read or write any global workflow state file.

## Invocation

Treat the complete text following `/init-season` as the argument payload. After
trimming surrounding whitespace, require exactly one argument matching
`^[0-9]{4}$`. Do not infer a season from repository files.

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
2. Read every canonical template needed from `templates/season/`.
3. Treat the current canonical rules, documents, templates, and metadata schema
   as authoritative over this skill.
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
    ├── prelude.meta.yaml
    ├── context.md
    ├── context.meta.yaml
    ├── regulations.md
    ├── regulations.meta.yaml
    ├── technology.md
    ├── technology.meta.yaml
    ├── teams.md
    ├── teams.meta.yaml
    ├── drivers.md
    ├── drivers.meta.yaml
    ├── people-and-organisations.md
    ├── people-and-organisations.meta.yaml
    ├── calendar.md
    ├── calendar.meta.yaml
    ├── glossary.md
    └── glossary.meta.yaml
```

Use this canonical template-to-destination map:

| Template | Destination under `archive/seasons/[SEASON]/` |
| --- | --- |
| `README.template.md` | `README.md` |
| `metadata.template.yaml` | `metadata.yaml` |
| `things-to-resolve-after-season.template.md` | `things-to-resolve-after-season.md` |
| `prelude.template.md` | `season/prelude.md` |
| `prelude.template.meta.yaml` | `season/prelude.meta.yaml` |
| `context.template.md` | `season/context.md` |
| `context.template.meta.yaml` | `season/context.meta.yaml` |
| `regulations.template.md` | `season/regulations.md` |
| `regulations.template.meta.yaml` | `season/regulations.meta.yaml` |
| `technology.template.md` | `season/technology.md` |
| `technology.template.meta.yaml` | `season/technology.meta.yaml` |
| `teams.template.md` | `season/teams.md` |
| `teams.template.meta.yaml` | `season/teams.meta.yaml` |
| `drivers.template.md` | `season/drivers.md` |
| `drivers.template.meta.yaml` | `season/drivers.meta.yaml` |
| `people-and-organisations.template.md` | `season/people-and-organisations.md` |
| `people-and-organisations.template.meta.yaml` | `season/people-and-organisations.meta.yaml` |
| `calendar.template.md` | `season/calendar.md` |
| `calendar.template.meta.yaml` | `season/calendar.meta.yaml` |
| `glossary.template.md` | `season/glossary.md` |
| `glossary.template.meta.yaml` | `season/glossary.meta.yaml` |

When copying Markdown templates, strip any HTML comment that only points at the
sibling metadata template; archive Markdown starts at the document title.
Instantiate each content `.md` together with its sibling `.meta.yaml`.

## Preflight protection

Before creating or changing anything:

1. Check whether `archive/seasons/[SEASON]/` exists.
2. If it exists, do not overwrite, reset, recreate, or repair anything. Report
   that the season is already initialized and list any missing files from the
   expected scaffold. Repair only in response to a separate explicit request.
3. Other seasons or in-progress rounds elsewhere are not a conflict. Proceed
   when this season path is free.
4. Record the pre-existing paths so validation can prove that nothing was
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
parent directories required to contain it. Do not create race folders.

## Progress

Do not write any global workflow pointer. Progress is the created season
scaffold under `archive/seasons/[SEASON]/`. In the completion reply, suggest
`/prepare-season [SEASON]` as the next sensible command when useful.

## Strict exclusions

Do not:

- research the season or browse for historical information;
- insert driver, team, race, or circuit names;
- insert dates other than the season identifier;
- insert regulations, technical facts, results, standings, or summaries;
- assume an announced or final calendar;
- generate source entries;
- create race directories or any race structure;
- read or update a global archive-state file.

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
- no pre-existing file was overwritten.

If validation fails, report the failure accurately; do not claim successful
initialization.

## Completion response

After successful validation, respond concisely with only:

1. initialized season;
2. created files;
3. validation result;
4. confirmation that no historical research or race structure was generated;
5. suggested next command: `/prepare-season [SEASON]`.
