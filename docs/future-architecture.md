# Archive architecture

The repository now contains only the generic roots and reusable templates. A
real season directory is created only by an explicit initialization task.
Scaffolding does not authorize historical research or content, and this layout
remains a default that may be revised from evidence gained in later phases.

## Current scaffold

```text
archive/
  seasons/
    README.md

templates/
  season/
  race/
  shared/
```

## Intended season structure

```text
archive/
  seasons/
    [SEASON]/
      README.md
      metadata.yaml

      season/
        prelude.md
        context.md
        regulations.md
        technology.md
        teams.md
        drivers.md
        people-and-organisations.md
        calendar.md
        glossary.md

      races/
        01-[grand-prix-slug]/
          metadata.yaml
          pre-weekend.md
          pre-race.md
          post-race.md
          standings-after.md
          sources.md

        02-[grand-prix-slug]/
          ...
```

The short filenames are storage names, not new content contracts.
`pre-weekend.md` implements the race-prelude contract, `pre-race.md` implements
the pre-start-weekend-brief contract, `post-race.md` implements the
post-race-report contract, and `standings-after.md` implements the
standings-snapshot contract. `sources.md` is the canonical event source ledger.

One season owns shared reference material and ordered race folders. Each race
keeps separate files for separate knowledge boundaries; a later file never
widens or replaces an earlier one. `standings-after.md` is the only full
standings table for its event cutoff.

## Templates and authority

`templates/season/` and `templates/race/` define document shape.
`templates/shared/` provides the canonical reusable metadata, source-entry,
standings, uncertainty, and spoiler-audit shapes. Templates summarize their
contract but do not reproduce complete policy.

When instructions conflict, the order in `AGENTS.md` applies. In particular,
the knowledge cutoff and canonical policy always override a template.

## State and review

`archive-state.yaml` points to the active workflow stage. It does not establish
historical truth, prove a cutoff, or replace per-document metadata and sources.
If state conflicts with a document, use the document's verified metadata for
its boundary and correct state before progressing.

Metadata records `research_status`, `source_status`, `spoiler_audit_status`, and
`last_verified`. Do not encode review state by copying a document into
“generated” and “reviewed” folders. A single document, its metadata, and version
control prevent drift.

A source whose surrounding material crosses the cutoff uses
`spoiler_risk: contains-later-material` and is quarantined from the permitted
evidence set. Its existence is recordkeeping, not permission to import later
knowledge.

## Navigation goals

- Season indexes support sequential reading in historical order.
- Season references support selective reading by subject.
- Race documents link backward to established context and forward only after a
  reader explicitly chooses to advance.
- Stable identifiers connect claims, source entries, snapshots, and documents
  without repeating full text.

## Open decisions

- Whether a season retrospective becomes a standard file after real usage.
- Whether research evidence needs a separate repository root in addition to
  race-local source ledgers.
- Whether season-local references later gain spoiler-aware cross-season indexes.
- How reader-facing links warn before crossing a knowledge boundary.
- How corrections preserve the state of knowledge at a historical cutoff.
- Whether publication builds ever require generated artifacts.

These decisions remain deferred until an explicit later task has evidence to
resolve them.
