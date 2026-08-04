---
name: historical-f1-research
description: Use when planning or conducting Formula 1 historical research for a document with a fixed knowledge cutoff.
---

# Historical F1 research

Read `docs/temporal-scope.md`, `docs/source-policy.md`, and the selected contract
in `docs/content-contracts.md`.

## Inputs

- Document type and event, if any
- Event time, latest-used public-knowledge time, and hard knowledge cutoff
- Questions or claims to investigate
- Existing source records and known constraints

## Workflow

1. Validate the metadata boundary before searching.
2. Break the task into claims, uncertainties, and expected source types.
3. Search the source hierarchy, favouring contemporary primary material.
4. Record dates, source type, the most exact practical locator, any locator
   limitation, spoiler risk, and supported claim. Leave exact
   `publication_date` as `unknown` when needed; apply content-based
   availability from `docs/source-policy.md` instead of quarantining a whole
   preseason source for a missing day-of-month.
5. Separate confirmed facts, contemporary expectations, interpretations, and
   disagreements.
6. Compare conflicting evidence without forcing a resolution.
7. Produce an evidence pack for drafting; mark gaps explicitly. Prefer a usable
   attributed field over an empty one when contemporary previews exist.

## Prohibited behaviour

- Searching later outcomes to decide what matters
- Treating retrospectives as contemporary expectations
- Copying full-season database context into a bounded evidence set
- Inventing missing details, quotations, or fake exact calendar dates
- Emptying preseason coverage because only a monthly issue date is known
- Writing polished narrative unless the task explicitly includes drafting

## Expected output

A cutoff statement, research questions, claim-to-source map, conflict log,
spoiler-risk notes, unsupported gaps, and a drafting-ready evidence summary.
If the task includes drafting, put uncertainty and citation apparatus in
footnotes / source notes per `docs/methodology.md` and `docs/source-policy.md`;
do not turn the reader-facing draft into a research log.

## Self-check

- [ ] Every retained fact was knowable by the cutoff, including via
      content-based availability where exact day is unknown.
- [ ] Publication, event, and public-knowledge dates are distinguished.
- [ ] Important claims have exact support and the best practical locator.
- [ ] Expectations and interpretations are labelled.
- [ ] Conflicts and gaps remain visible without gutting readable coverage.
- [ ] Later-source contamination has been checked.
