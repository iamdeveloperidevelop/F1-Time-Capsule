# Provisional future architecture

This is a design proposal, not an existing content tree. Creating any part of it
requires an explicit later-phase task. Names and boundaries remain reversible.

```text
archive/
  [SEASON]/
    references/
      [SEASON-LEVEL DOCUMENTS]
    events/
      [ORDER]-[EVENT-SLUG]/
        [RACE PRELUDE]
        [PRE-START WEEKEND BRIEF]
        [POST-RACE REPORT]
        [STANDINGS SNAPSHOT]
    retrospective/
      [SEASON RETROSPECTIVE]
research/
  [SEASON]/
    source-records/
    claim-maps/
```

The proposed `archive/` root separates reader-facing content from evidence in
`research/`. One season owns shared reference material, ordered event folders,
and its retrospective. Each event keeps distinct documents for distinct
knowledge boundaries rather than mutating one article as the weekend advances.
Standings snapshots are tied to precise event cutoffs.

## State and review

Metadata records `research_status`, `source_status`, and `last_verified`.
Workflow state should not be encoded by duplicating a document into “generated”
and “reviewed” folders: copies drift and weaken the canonical-home rule. A
single canonical document plus version control and explicit review metadata is
the current preference. If later publication tooling needs immutable generated
artifacts, its output location must remain separate from authored source.

Research records may contain links or excerpts whose surrounding material
spoils later events. Reader-facing content must never inherit those permissions.
Access controls or tooling may eventually help, but the declared cutoff and
human-readable evidence map remain authoritative.

## Navigation goals

- Season indexes will support sequential reading in historical order.
- Reference indexes will support selective reading by team, driver, technology,
  organisation, term, or event.
- Event documents will link backward to established context and forward only
  when a reader explicitly chooses to advance.
- Stable identifiers will connect claims, sources, snapshots, and documents
  without repeating full text.

## Open decisions

- Exact filenames, index format, and source-record serialization.
- Whether team, driver, and technology references remain season-local or gain
  spoiler-aware cross-season indexes.
- How links warn readers before crossing a knowledge boundary.
- How corrections preserve the state of knowledge at a historical cutoff.
- Whether publication builds need generated artifacts and how review status is
  represented beyond metadata.

These decisions should be made from real Phase 1 usage, not fixed prematurely.
