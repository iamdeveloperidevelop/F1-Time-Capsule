---
name: spoiler-scope-audit
description: Use when adversarially checking a historical draft for direct spoilers, hindsight, foreshadowing, or knowledge beyond its declared cutoff.
---

# Spoiler scope audit

Read `docs/temporal-scope.md` and the document's contract in
`docs/content-contracts.md`.

## Inputs

- Complete draft and metadata
- Selected content contract
- Claim/source map when available
- Audit mode: report-only or authorised correction

## Workflow

1. Verify that metadata defines a precise cutoff and spoiler categories.
2. Build a list of facts permitted at that boundary.
3. Review every claim for direct future information.
4. Review wording for hindsight, retrospective certainty, dramatic
   foreshadowing, and outcome-shaped emphasis or omission.
5. Check predictions remain attributed contemporary expectations.
6. Check later sources have not influenced framing.
7. Report each violation with severity and a cutoff-safe remedy; edit only in
   correction mode.

## Prohibited behaviour

- Widening the cutoff to save a sentence
- Assuming vague wording is safe
- Revealing the forbidden fact while proposing replacement prose
- Introducing new factual claims during correction
- Treating factual truth as sufficient when the fact was not yet knowable

## Expected output

Audit result (`pass`, `pass-with-corrections`, or `fail`), issue list by
category, affected wording, reason, safe remediation, and unresolved questions.

## Self-check

- [ ] Direct spoiler categories were checked.
- [ ] Indirect spoilers and “final/future/decisive” framing were checked.
- [ ] Decisions were judged only with contemporary knowledge.
- [ ] Emphasis and viewing cues were checked for later influence.
- [ ] Corrections preserve meaning and uncertainty.
- [ ] The report itself avoids disclosing unnecessary spoilers.
