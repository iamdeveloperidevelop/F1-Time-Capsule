---
name: audit-document
description: Audit one archive document for temporal, source, metadata, repetition, and language issues in report-only mode.
disable-model-invocation: true
---

# Audit an archive document

This workflow is read-only by default. It reports findings and recommended
corrections but never edits the audited file or related records. A later,
explicit request is required to apply fixes.

## Invocation and path safety

Treat the complete text following `/audit-document` as one trimmed
repository-relative path. Reject an empty payload, an absolute path, a path
containing a `..` segment, a path that does not identify an existing regular
file, or any path whose fully resolved target is outside the repository root.
Also reject symlinks that resolve outside the repository.

If validation fails, make no changes and respond with exactly:

```text
Usage: /audit-document [PATH]
Example: /audit-document archive/seasons/1981/season/technology.md
```

## Canonical preparation

Read `AGENTS.md`, the relevant `.cursor/rules/`,
`docs/temporal-scope.md`, `docs/source-policy.md`,
`docs/content-contracts.md`, `docs/methodology.md`, and the target document.
Identify its canonical contract from front matter and inspect only the related
metadata, source ledgers, standings snapshots, and primary-home documents needed
for the audit.

Do not browse for new historical evidence by default. Existing local citations
may be inspected only when necessary to evaluate support and without importing
facts beyond the declared cutoff. If exact support cannot be checked from
available repository evidence, report it as unverified rather than guessing.

Use the `spoiler-auditor` or `spoiler-scope-audit` workflow in report-only mode,
the `source-auditor` or `source-verification` workflow in report-only mode, and
the editorial checks from `historical-content-editor` without authorizing
edits. Apply the primary-home and deduplication rules in
`docs/methodology.md`. Do not duplicate their full instructions here.

## Audit checks

Report:

1. the document type and declared knowledge cutoff, including missing,
   placeholder, inconsistent, or imprecise metadata;
2. direct spoiler risks;
3. indirect spoiler risks and outcome-shaped selection or emphasis;
4. hindsight contamination and retrospective certainty;
5. dramatic foreshadowing;
6. unsupported or over-precise factual claims and quotations;
7. citations that do not support the exact wording, certainty, or date;
8. conflicting sources and uncertainty that was hidden or silently resolved;
9. metadata or status problems under the canonical schema;
10. repetition against related canonical documents and misplaced primary-home
    detail;
11. Polish language, clarity, structure, terminology, and accessibility issues;
12. inline raw IDs, audit mechanics, repeated verification caveats, or excessive
    note markers contrary to the reader-facing presentation in
    `docs/methodology.md`;
13. prioritized recommended corrections that preserve the current cutoff.

Keep the report itself spoiler-safe: identify later-knowledge leakage without
unnecessarily revealing the future fact. Distinguish confirmed defects from
items that cannot be verified with available evidence. Do not update audit
status or create an audit file.

## Completion response

Return a concise report with an overall result, cutoff and contract, findings
grouped by severity and category, unresolved verification gaps, and recommended
corrections. End by stating that no files were modified.
