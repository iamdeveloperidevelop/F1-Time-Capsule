---
name: season-status
description: Report one season's archive progress and consistency without browsing or changing files.
disable-model-invocation: true
---

# Report season status

This workflow is strictly read-only. Do not browse the web, create files, edit
metadata, repair files, stage changes, commit, or push. Do not read or write
any global workflow state file.

## Invocation

Treat the complete text following `/season-status` as the argument payload.
After trimming surrounding whitespace, require exactly one argument matching
`^[0-9]{4}$`. Do not infer a season from repository files outside this season.

If validation fails, make no changes and respond with exactly:

```text
Usage: /season-status [YYYY]
Example: /season-status 1981
```

Use the validated argument as `[SEASON]`.

## Inspection

Read only:

- `AGENTS.md`, `docs/temporal-scope.md`, `docs/content-contracts.md`, and
  `docs/archive-workflow.md`;
- `archive/seasons/[SEASON]/metadata.yaml`, if present;
- `archive/seasons/[SEASON]/things-to-resolve-after-season.md`, if present;
- all season-document sibling `.meta.yaml` files;
- race `metadata.yaml` and race-document sibling `.meta.yaml` files;
- source-ledger conflict and uncertainty indexes needed to report status;
- existence of stage documents (`pre-weekend.md`, `pre-race.md`,
  `post-race.md`, `standings-after.md`) under each race folder.

Do not follow external links or inspect web sources. Do not quote or summarize
historical narrative beyond what is necessary to identify repository progress.
Never reveal a historical fact beyond the latest verified cutoff already
declared in this season's documents.

Treat document metadata as authoritative for each document's boundary. Infer
practical stage and the next sensible command from on-disk files and metadata
under `archive/seasons/[SEASON]/` only (for example: missing previous
`standings-after.md` blocks the next `pre-weekend`; within a round the order is
`pre-weekend` → `pre-race` → `post-race`). A placeholder is not a verified
cutoff or completed document.

## Report

Report concisely:

1. whether `archive/seasons/[SEASON]/` exists;
2. season metadata and initialization status;
3. the declared preseason cutoff and whether it is placeholder, partial, or
   verified;
4. completed season documents;
5. incomplete, placeholder, unaudited, or otherwise unverified documents;
6. initialized race folders, including duplicate-round or metadata conflicts;
7. inferred furthest stage per race from on-disk documents and statuses;
8. last completed document path(s) and suggested next command for this season;
9. unresolved source, cutoff, calendar, or classification issues recorded in
   canonical files, including the after-season ledger;
10. internal metadata conflicts within this season (conflicting cutoffs or
    statuses across related documents).

Use only canonical status values found in the repository. Distinguish missing,
planned, drafted, and verified rather than treating file existence as
completion. If the season does not exist, report that fact and stop.
