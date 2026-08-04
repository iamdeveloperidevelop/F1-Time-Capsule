---
name: source-verification
description: Use when verifying that historical claims are exactly supported by suitable, correctly dated, cutoff-safe sources.
---

# Source verification

Read `docs/source-policy.md` and `docs/temporal-scope.md`. Use
`templates/shared/source-entry.template.yaml` for source records.

## Inputs

- Draft or claim inventory
- Source records and accessible source material
- Knowledge cutoff
- Existing conflict log

## Workflow

1. Extract every material factual claim, quotation, number, and attributed
   expectation.
2. Match each item to its cited source and the most exact practical locator;
   record limitations when the source does not permit one.
3. Verify source identity, publication date, event date, and contemporaneity.
4. Check that support entails the claim's exact wording and certainty.
5. Rate source suitability using the canonical hierarchy.
6. Identify unsupported claims, weak dependencies, spoiler-bearing sources, and
   citation gaps.
7. Compare conflicts and record the best-supported account without erasing
   uncertainty.
8. Check reader-facing presentation against `docs/methodology.md`: traceability
   remains in sparse notes and ledgers, while IDs, audit mechanics, and repeated
   source caveats stay out of narrative.

## Prohibited behaviour

- Treating a nearby citation as support without checking it
- Upgrading an inference or expectation into fact
- Using an inaccessible or fabricated citation as verified
- Guessing missing dates or silently resolving disagreement
- Importing later facts discovered during verification

## Expected output

A claim-level verification matrix, unsupported/partially supported list,
source-quality flags, date and cutoff issues, conflict findings, and overall
source-status recommendation. Keep this audit output separate from narrative;
reader-facing documents receive only the canonical notes and source section.

## Self-check

- [ ] Every major claim and quotation was inventoried.
- [ ] Locators and dates were checked to the precision available.
- [ ] Each citation supports the wording and certainty used.
- [ ] Contemporary and later sources are distinguished.
- [ ] Disagreement and inaccessible evidence are explicit.
- [ ] The recommendation matches the actual evidence coverage.
