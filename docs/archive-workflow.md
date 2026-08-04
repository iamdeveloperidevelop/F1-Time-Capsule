# Archive workflow and state transitions

This document defines how the archive advances. It does not authorize historical
content. Every historical task still needs an explicit target, content contract,
and exact knowledge cutoff.

The manually invoked interfaces for these transitions are listed in
[`commands.md`](commands.md). Each command stops at its declared boundary and
never runs the next stage automatically.

There is no global workflow pointer. Progress is the existence and metadata of
canonical documents under `archive/seasons/[YYYY]/`. Parallel agent sessions
are allowed when they write to disjoint paths and each command's on-disk
prerequisites are already satisfied.

## Authority for progression

Document metadata (the sibling `.meta.yaml`) is authoritative for that
document's temporal boundary.
Sources establish what was publicly knowable by that boundary.
Do not invent a repository-wide “current position”; suggest the next sensible
command in the agent reply only.

Before any transition:

1. read the target document metadata and selected contract;
2. verify the proposed cutoff from cutoff-safe sources, or record the narrowest
   supported descriptive boundary and its uncertainty;
3. confirm that the transition was explicitly requested;
4. confirm on-disk prerequisites for that command (see stage gates below);
5. preserve all earlier-boundary documents unchanged.

Reject a command only when the target cutoff is wrong, required files or
metadata are missing, or a spoiler/source audit would fail—not because another
season or round is in progress elsewhere.

An unresolved source, calendar, or historical-detail question does not itself
block progression: omit the unsupported reader-facing claim, state only
cutoff-safe uncertainty where useful, and add the gap to the season's
`things-to-resolve-after-season.md` ledger. Do not ask the user to verify it.

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
Infer the season's practical stage from which documents exist and are ready,
not from a global lock file.

## Stage gates (prerequisites on disk)

- **Initialize / prepare season:** no prior season package required; create
  `archive/seasons/[SEASON]/` from templates when absent.
- **Preseason package:** verified preseason cutoff recorded in season
  `metadata.yaml` before research; race scaffolds only for rounds known on the
  announced calendar at that cutoff.
- **`/pre-weekend` for round `01`:** season preseason package complete enough
  that calendar and season cutoffs are recorded.
- **`/pre-weekend` for round `N` > `01`:** previous round's
  `standings-after.md` exists (canonical standings snapshot after that event).
- **`/pre-race` for a round:** that round's `pre-weekend.md` exists and is
  past placeholder.
- **`/post-race` for a round:** that round's `pre-race.md` exists and is past
  placeholder; post-race cutoff and immediate official process defined in race
  `metadata.yaml`.

Within one round the order is always
`pre-weekend` → `pre-race` → `post-race`. Do not skip stages for the same
round. Parallel work on different seasons, or on different rounds whose
prerequisites are already on disk, does not conflict.

## Initialize a season

1. Select either structure-only initialization or explicitly authorized
   historical-content initialization.
2. Create `archive/seasons/[SEASON]/` from `templates/season/` using the
   template-to-destination map in
   `.cursor/skills/init-season/SKILL.md`.
3. For structure-only initialization, keep all placeholders, leave document
   statuses at `planned`, `unstarted`, and `not-run`, and stop without research.
4. For explicitly authorized historical-content initialization, establish the
   exact preseason cutoff before research.
5. Fill `metadata.yaml` with identifiers and boundary definitions.
6. Research and write the season reference documents under their contracts.
7. Verify the announced calendar as it stood at the cutoff.
8. Create race directories only for rounds publicly known at that cutoff.
9. Add later calendar changes only in a later explicitly authorized transition,
   when those changes have become historically knowable.
10. Complete at `season-prelude`; do not skip directly to a race stage.

If a source, schedule detail, entry, or regulation cannot be verified, record
it in `things-to-resolve-after-season.md`. A season package may progress with
`source_status: partial` when all reader-facing statements are safe at their
declared boundary and no spoiler-audit issue remains.

Structure-only initialization does not establish a verified historical cutoff,
even if placeholders describe where that cutoff will later be recorded.

## Before a race weekend

1. Confirm the canonical standings snapshot after the previous completed event
   (for round `01`, use the season package / preseason standings context).
2. Establish the cutoff immediately before the first official session.
3. Research only information publicly available by that boundary.
4. Create or update `pre-weekend.md`; do not alter an earlier event file.
5. Verify its claims and source entries.
6. Run the spoiler audit.
7. Stop at the `pre-weekend` boundary for the requested `[ROUND]` only.

Unresolved facts are recorded in the season ledger, not treated as a request for
the user to supply evidence. Omit them from the brief or label only the
cutoff-safe uncertainty they create.

## Before watching the race

1. Establish the exact instant immediately before the scheduled race start.
2. Research practice, qualifying, grid, and confirmed pre-start decisions only.
3. Create `pre-race.md` and keep it concise.
4. Link season references instead of repeating biographies, histories, or
   technical explanations.
5. Run source verification and the spoiler audit.
6. Stop at the `pre-race` boundary.
7. Do not create or research `post-race.md` unless explicitly requested.

## After watching the race

1. Define the exact post-race cutoff and the immediate official process included
   by that cutoff in race `metadata.yaml`.
2. Create `post-race.md` from evidence available by that cutoff.
3. Create or update the canonical `standings-after.md`.
4. Record only immediate consequences already public by the cutoff.
5. Update `sources.md`, complete audits, then stop at the `post-race` boundary.
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

## Completing a transition

After the documents for the requested transition exist and their exact cutoffs
are recorded:

- leave progress encoded only in those files and their metadata;
- in the agent reply, suggest one explicit, non-automatic next command when
  useful (for example `/pre-race 1982 04`);
- never write a global “where we are” file.

Never infer a next round, expand the calendar, or advance a cutoff merely
because later information is available. The next action requires a user task.
