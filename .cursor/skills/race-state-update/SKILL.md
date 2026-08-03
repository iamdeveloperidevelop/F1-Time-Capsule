---
name: race-state-update
description: Use in a later phase when advancing the archive from one historical race cutoff to the next without importing future event knowledge.
---

# Race state update

Definition only for Phase 0; do not execute this skill until a later task
explicitly authorises historical content. Read `docs/temporal-scope.md`,
`docs/source-policy.md`, `docs/archive-workflow.md`, and the target contracts in
`docs/content-contracts.md`. Start target files from `templates/season/` or
`templates/race/`; do not infer a transition from `archive-state.yaml`.

## Inputs

- Verified state at the previous cutoff
- Exact next cutoff and historical weekend format
- Newly available official results, decisions, and contemporary evidence
- Applicable scoring, eligibility, and tie-breaking rules
- Existing claim, source, and disagreement records

## Workflow

1. Freeze the previous state and define the next permitted interval.
2. Inventory only information that became public within that interval.
3. Verify classifications, decisions, and points against official evidence.
4. Recalculate standings independently and reconcile differences visibly.
5. Apply confirmed entries, penalties, status changes, and unresolved matters
   only when they became knowable.
6. Produce separately contracted event documents or snapshots; never overwrite
   an earlier boundary with later knowledge.
7. Run source, arithmetic, spoiler, metadata, and redundancy audits.

## Prohibited behaviour

- Executing during Phase 0
- Reading ahead to resolve a then-open issue
- Copying final-season standings into an intermediate state
- Backdating later corrections, causes, rulings, or replacements
- Guessing classification, points, eligibility, or tie-break outcomes
- Mutating an earlier snapshot to represent a later boundary

## Expected output

A change ledger from old to new cutoff, verified calculations, newly knowable
claim/source records, unresolved issues, proposed document updates, and audit
results.

## Self-check

- [ ] Every change became public after the old and by the new cutoff.
- [ ] Official status and provisional status are distinguished.
- [ ] Points and tie-breaks were independently checked.
- [ ] Later corrections and events were excluded.
- [ ] Earlier boundary documents remain intact.
- [ ] All target documents retain explicit cutoff metadata.
