---
name: season-status
description: Report one season's archive progress and consistency without browsing or changing files.
disable-model-invocation: true
---

# Report season status

This workflow is strictly read-only. Do not browse the web, create files, edit
metadata, repair state, stage changes, commit, or push.

## Invocation

Treat the complete text following `/season-status` as the argument payload.
After trimming surrounding whitespace, require exactly one argument matching
`^[0-9]{4}$`. Do not infer a season from repository state.

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
- `archive-state.yaml`;
- `archive/seasons/[SEASON]/metadata.yaml`, if present;
- `archive/seasons/[SEASON]/things-to-resolve-after-season.md`, if present;
- all season-document front matter;
- race metadata and race-document front matter;
- source-ledger conflict and uncertainty indexes needed to report status.

Do not follow external links or inspect web sources. Do not quote or summarize
historical narrative beyond what is necessary to identify repository state.
Never reveal a historical fact beyond the latest verified cutoff already
declared in the archive.

Treat document metadata as authoritative for each document's boundary and
`archive-state.yaml` only as a workflow pointer. Compare them without silently
resolving discrepancies. A placeholder is not a verified cutoff or completed
document.

## Report

Report concisely:

1. whether `archive/seasons/[SEASON]/` exists;
2. season metadata and initialization status;
3. the declared preseason cutoff and whether it is placeholder, partial, or
   verified;
4. completed season documents;
5. incomplete, placeholder, unaudited, or otherwise unverified documents;
6. initialized race folders, including duplicate-round or metadata conflicts;
7. current active round and stage;
8. last completed document and next allowed action;
9. unresolved source, cutoff, calendar, or classification issues recorded in
   canonical files, including the after-season ledger;
10. files whose metadata conflicts with `archive-state.yaml`.

Use only canonical status values found in the repository. Distinguish missing,
planned, drafted, and verified rather than treating file existence as
completion. If the season does not exist, report that fact and stop.
