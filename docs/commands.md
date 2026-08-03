# Archive workflow commands

These project-level Cursor Agent Skills are manually invoked. Each command
validates its arguments and preserves the archive's current knowledge boundary.
No command automatically advances into the next spoiler stage.

## `/init-season [YYYY]`

Creates empty season scaffolding from canonical templates and updates the
workflow pointer when permitted. It performs no historical research and creates
no race folders.

## `/prepare-season [YYYY]`

Initializes the season when necessary, then researches, writes, and audits the
complete preseason package at the verified boundary before the opening event's
first official session. It also creates empty race scaffolds only for events
known on the announced calendar at that cutoff.

## `/pre-weekend [YYYY] [ROUND]`

Creates one race-weekend brief using only information public immediately before
that event's first official session. It does not include any session result or
create the pre-race brief.

## `/pre-race [YYYY] [ROUND]`

Creates a concise watch-ready brief using the historically appropriate weekend
format and stops immediately before the scheduled race start. It does not reveal
or generate the race result.

## `/post-race [YYYY] [ROUND]`

Explicitly authorizes revealing the selected race through a declared immediate
post-race boundary, including its report and verified standings snapshot. It
does not research or generate the next event.

## `/season-status [YYYY]`

Reads local metadata and workflow state to report season progress, incomplete
work, unresolved issues, and conflicts. It does not browse or modify files.

## `/audit-document [PATH]`

Audits one repository document for spoiler leakage, source support, metadata,
repetition, and language issues. It is report-only unless the user later
explicitly requests fixes.

## Normal sequence

```text
/prepare-season 1981
/pre-weekend 1981 01
/pre-race 1981 01
/post-race 1981 01
```

Use `/season-status 1981` at any point to inspect the safe next action. Use
`/audit-document archive/seasons/1981/season/technology.md` for a read-only
review. `/init-season` remains available as a low-level structure-only command,
but normal archive operation starts with `/prepare-season`.
