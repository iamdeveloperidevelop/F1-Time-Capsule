# Archive workflow and state transitions

This document defines how the archive advances. It does not authorize historical
content. Every historical task still needs an explicit target, content contract,
and exact knowledge cutoff.

The manually invoked interfaces for these transitions are listed in
[`commands.md`](commands.md). Each command stops at its declared boundary and
never runs the next stage automatically.

## Two kinds of state

Document front matter is authoritative for that document's temporal boundary.
Sources establish what was publicly knowable by that boundary.
`archive-state.yaml` only tells an agent where the repository workflow currently
stands. It is not evidence and must never be used to resolve a historical claim.

Before any transition:

1. read the target document metadata and selected contract;
2. verify the proposed cutoff from cutoff-safe sources;
3. confirm that the transition was explicitly requested;
4. preserve all earlier-boundary documents unchanged.

If `archive-state.yaml` conflicts with verified document metadata, stop
progression, correct the workflow pointer, and do not widen any document.

## Allowed stages

| Stage | Meaning | Normal next stage |
| --- | --- | --- |
| `uninitialized` | No real season directory exists. | `season-prelude` |
| `season-prelude` | The season is initialized; prelude and reference work is next or active. | `pre-weekend` |
| `pre-weekend` | Work stops before the first official session of `[ROUND]`. | `pre-race` |
| `pre-race` | Work stops immediately before the scheduled race start. | `post-race` |
| `post-race` | Race, immediate defined official process, and standings snapshot may be known. | `pre-weekend` for an explicitly requested next round, or `season-complete` |
| `season-complete` | The explicitly defined season-end scope is complete. | None without a new explicit task |

A stage name is not proof that its documents passed review. Check
`research_status`, `source_status`, and `spoiler_audit_status` in each file.

## Initialize a season

1. Select either structure-only initialization or explicitly authorized
   historical-content initialization.
2. Create `archive/seasons/[SEASON]/` from `templates/season/` using the
   template-to-destination map in
   `.cursor/skills/init-season/SKILL.md`.
3. For structure-only initialization, keep all placeholders, leave document
   statuses at `planned`, `unstarted`, and `not-run`, update state as described
   below, and stop without research.
4. For explicitly authorized historical-content initialization, establish the
   exact preseason cutoff before research.
5. Fill `metadata.yaml` with identifiers and boundary definitions.
6. Research and write the season reference documents under their contracts.
7. Verify the announced calendar as it stood at the cutoff.
8. Create race directories only for rounds publicly known at that cutoff.
9. Add later calendar changes only in a later explicitly authorized transition,
   when those changes have become historically knowable.
10. Move state from `uninitialized` to `season-prelude`; do not skip directly to
    a race stage.

Structure-only initialization does not establish a verified historical cutoff,
even if placeholders describe where that cutoff will later be recorded.

## Before a race weekend

1. Confirm the canonical standings snapshot after the previous completed event.
2. Establish the cutoff immediately before the first official session.
3. Research only information publicly available by that boundary.
4. Create or update `pre-weekend.md`; do not alter an earlier event file.
5. Verify its claims and source entries.
6. Run the spoiler audit.
7. Set state to `pre-weekend` only for the requested `[ROUND]`.

## Before watching the race

1. Establish the exact instant immediately before the scheduled race start.
2. Research practice, qualifying, grid, and confirmed pre-start decisions only.
3. Create `pre-race.md` and keep it concise.
4. Link season references instead of repeating biographies, histories, or
   technical explanations.
5. Run source verification and the spoiler audit.
6. Set state to `pre-race`.
7. Do not create or research `post-race.md` unless explicitly requested.

## After watching the race

1. Define the exact post-race cutoff and the immediate official process included
   by that cutoff in race `metadata.yaml`.
2. Create `post-race.md` from evidence available by that cutoff.
3. Create or update the canonical `standings-after.md`.
4. Record only immediate consequences already public by the cutoff.
5. Update `sources.md`, complete audits, then set state to `post-race`.
6. Do not research the next race automatically.
7. Do not create the next `pre-weekend.md` unless explicitly requested.

## Updating standings

`standings-after.md` is the sole full driver and constructor standings snapshot
for its event boundary. It also owns points gained at the event, applicable
counting-result rules, ties, and unresolved classification issues.
`post-race.md` may summarize the championship effect and link to the snapshot,
but must not copy its full tables.

Verify arithmetic, eligibility, counting-result rules, tie-breaking, and
provisional status independently. A later ruling creates a later state; it must
not be backdated into an earlier snapshot.

## State update contract

Update `archive-state.yaml` only after the documents for the requested
transition exist and their exact cutoffs are recorded. Set:

- `active_season` and `active_round` to the initialized placeholders or values;
- `current_stage` to one allowed stage;
- `knowledge_cutoff` to the latest verified repository boundary;
- `last_completed_document` to the path that completed the transition;
- `next_allowed_action` to one explicit, non-automatic action.

Never infer a next round, expand the calendar, or advance a cutoff merely
because later information is available. The next action requires a user task.
