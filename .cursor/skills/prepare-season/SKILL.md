---
name: prepare-season
description: Prepare a complete cutoff-safe preseason Formula 1 archive package and initialize its race scaffolds.
disable-model-invocation: true
---

# Prepare season

This manually invoked workflow authorizes historical work only for the requested
season and only through its verified preseason boundary. It does not authorize
any in-season knowledge. Do not read or write any global workflow state file.

## Invocation

Treat the complete text following `/prepare-season` as the argument payload.
After trimming surrounding whitespace, require exactly one argument matching
`^[0-9]{4}$`. Do not infer a season from repository files.

If validation fails, make no changes and respond with exactly:

```text
Usage: /prepare-season [YYYY]
Example: /prepare-season 1981
```

Use the validated argument as `[SEASON]`.

## Canonical preparation and preflight

Before browsing, researching, or modifying files:

1. Read `AGENTS.md`, the relevant `.cursor/rules/`, `docs/methodology.md`,
   `docs/temporal-scope.md`, `docs/source-policy.md`,
   `docs/content-contracts.md`, `docs/archive-workflow.md`, and
   `docs/agent-task-recipes.md`.
2. Read `.cursor/skills/init-season/SKILL.md`, every canonical season and race
   template needed, and all existing files under `archive/seasons/[SEASON]/`.
3. Confirm that all canonical inputs exist. Stop without changes and report any
   missing input; never synthesize a replacement.
4. Record existing paths and file contents or hashes before editing. Inspect
   season metadata and every document status. If cutoffs or statuses conflict
   within this season package, stop and report the conflict.
5. Other seasons or rounds in progress elsewhere are not a conflict. Work only
   under `archive/seasons/[SEASON]/`.

If the season directory is absent, perform the canonical structure-only
initialization in `.cursor/skills/init-season/SKILL.md` as the first part of
this workflow, using `templates/season/`. The user need not invoke
`/init-season` separately. If initialization cannot complete safely, stop
before research.

If the directory exists, never recreate it. Preserve manually written text and
continue only placeholder or incomplete work. Do not overwrite any document
whose canonical metadata marks it verified, or any equivalent reviewed or
complete status supported by the current schema. Report unsupported statuses,
conflicting cutoffs, and non-placeholder content that cannot be resumed safely.

## Establish the preseason boundary

Establish and record the precise knowledge cutoff:

> Immediately before the first official session of the opening championship
> event as it was understood at that historical moment.

Verify the opening event, the period-appropriate weekend schedule, the first
official session, its start, and local time when reliable evidence supports it.
Distinguish event time, publication time, and public-knowledge time. If an exact
time cannot be verified, use the narrowest precise descriptive boundary the
evidence supports, record the uncertainty, and do not guess.

Write the same compatible cutoff into season metadata and all season documents,
using each canonical field and contract. Never reset an already verified cutoff
without an explicit correction request and supporting evidence.

## Research and drafting

Research only facts publicly knowable by the preseason cutoff. Follow the
canonical source hierarchy and document contracts. Use:

- the `researcher` subagent or `historical-f1-research` skill to establish the
  cutoff, collect claim-mapped evidence, separate contemporary from
  retrospective material, and preserve disagreements;
- the `source-auditor` subagent or `source-verification` skill to verify exact
  support, dates, locators, and claim certainty;
- the `spoiler-auditor` subagent or `spoiler-scope-audit` skill to find direct
  and indirect spoilers, hindsight, foreshadowing, and outcome-shaped emphasis;
- the `editor` subagent or `historical-content-editor` skill only after factual
  review, to improve Polish and reduce repetition without adding facts.

Populate the complete canonical season package:

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

Use the matching template and contract for each file. Cover the complete
preseason scope assigned by those contracts, including inherited sporting
context, defending champions, governance and politics, regulations, scoring
and eligibility, entries, teams, drivers and confirmed transfers, technology,
engines, tyres, relevant people and organisations, the announced calendar,
circuit orientation, glossary terms, and attributed contemporary expectations.
Place details in their canonical primary homes and link rather than duplicate.

Keep reader-facing historical prose in Polish and readable. Do not use any race
or season outcome to select, evaluate, or emphasize preseason information. Use
content-based availability for day-undated contemporary preseason sources; do
not collapse the field or expectations to defending champions because a monthly
magazine lacks a day-of-month. Preserve uncertainty and source disagreements in
footnotes and source apparatus, not as constant interruptions in the main text
(`docs/methodology.md`).

## Calendar and race scaffolds

Verify the calendar version publicly known at the preseason cutoff. Do not
substitute the final season calendar for the announced calendar.

For each event officially scheduled or sufficiently confirmed at that cutoff,
create exactly one ordered directory using the canonical naming convention:

```text
archive/seasons/[SEASON]/races/[ROUND]-[grand-prix-slug]/
```

Normalize `[ROUND]` to two digits and derive a stable lowercase ASCII slug from
the historically supported event name. Preserve provisional, reserve, or other
then-known status in canonical metadata.

Instantiate only these files from `templates/race/`:

```text
metadata.yaml
pre-weekend.md
pre-weekend.meta.yaml
pre-race.md
pre-race.meta.yaml
post-race.md
post-race.meta.yaml
standings-after.md
standings-after.meta.yaml
sources.md
sources.meta.yaml
```

Strip HTML comments that only point at sibling metadata templates so archive
Markdown starts at the document title. Instantiate each content `.md` together
with its sibling `.meta.yaml`.

Apply only template-authorized substitutions for season, round, event, slug,
paths, language, and then-known calendar status. Leave all race-stage content,
cutoffs not yet established, results, standings, and source entries at their
canonical placeholders. Do not populate race briefs or research practice,
qualifying, race results, or later calendar changes.

Before creating a race folder, detect existing folders by normalized round and
metadata identity, not slug alone. Never create a duplicate or silently rename
an existing folder. Report conflicts.

## Audits and completion

For every changed season document:

1. verify metadata and contract compliance;
2. run claim-level source verification;
3. run an adversarial spoiler audit against the preseason cutoff;
4. run a cross-document repetition audit;
5. perform the Polish language edit without changing the verified claim set;
6. re-run source and spoiler checks after substantive edits.

Advance canonical document statuses only when their actual audit results allow
it. Do not invent status values or duplicate source entries. A document may
remain `source_status: partial` without blocking preparation or the next
explicitly requested stage when every reader-facing claim is cutoff-safe and
the unresolved evidence is recorded in `things-to-resolve-after-season.md`.
`spoiler_audit_status: issues-found` still requires remediation: remove the
unsafe claim or rewrite it as supported uncertainty before progression.

After the entire season package has no unresolved reader-facing spoiler issue,
leave progress encoded only in those documents and their metadata. Do not write
any global workflow pointer. Suggest
`/pre-weekend [SEASON] [FIRST_ROUND]` in the reply.

Do not require the user to locate missing historical evidence. When an exact
time, calendar detail, entry, rule, or other claim cannot be verified, use the
narrowest supported uncertainty in the relevant document, omit unsupported
facts, and record a concrete follow-up item in
`things-to-resolve-after-season.md`.

Document metadata statuses carry completion and review state. Do not generate
the first pre-weekend brief.

## Safe resumption and validation

On rerun, inspect every target before editing. Skip verified work, preserve
manual prose, resume partial documents only when their cutoff and claim records
are compatible, and report every skipped file and reason. Never commit, push,
or advance into an in-season stage automatically.

Before completion verify:

- every season document exists, uses its canonical contract, and has the same
  compatible preseason boundary;
- every reader-facing claim is cutoff-safe and exactly supported, or omitted;
- source, spoiler, metadata, contradiction, language, and repetition checks
  passed, or unresolved source questions are explicitly recorded in
  `things-to-resolve-after-season.md`;
- race folders match only the calendar known at the cutoff and canonical
  templates, with no populated race-stage content;
- no existing verified or manually written content was overwritten;
- YAML metadata parses.

## Completion response

Report concisely:

1. season prepared and cutoff used;
2. season documents created, updated, and skipped with reasons;
3. number of race folders initialized;
4. unresolved source disagreements;
5. spoiler and source audit results;
6. next recommended command, `/pre-weekend [SEASON] [FIRST_ROUND]`.
