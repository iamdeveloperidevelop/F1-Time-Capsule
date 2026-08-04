---
name: historical-content-editor
description: Use when editing Polish historical content for clarity, structure, precision, and reduced repetition without changing facts or temporal scope.
---

# Historical content editor

Read `docs/methodology.md` and `docs/temporal-scope.md`. Editing follows, rather
than replaces, factual and spoiler review.

## Inputs

- Draft with metadata and selected contract
- Verified claim/source map
- Known uncertainties and required terminology
- Related documents for redundancy checks

## Workflow

1. Freeze the factual claim set and knowledge cutoff.
2. Improve natural Polish, clarity, flow, and structure so the main text reads
   as continuous narrative or clean reference prose.
3. Move uncertainty, source limits, claim/source IDs, and ledger links out of
   running paragraphs into `## Przypisy` (short numbered notes) and
   `## Uwagi źródłowe` (citation apparatus). Mark needed caveats with `*¹`,
   `*²`, and so on.
4. Preserve factual meaning, attribution, confidence, names, and diacritics;
   do not resolve uncertainty by wording alone.
5. Explain technical terms at first meaningful use for a non-engineer.
6. Remove clickbait, empty phrasing, artificial drama, repeated summaries, and
   research-process narration (“nie potwierdza”, “luka dowodowa”, “źródła nie
   dają”, “brak daty dziennej blokuje użycie”) from the main text unless a
   single brief footnote is the right place for it. Prefer readable coverage of
   the contemporary field over a skeleton that mentions only hard-dated scraps.
7. Replace duplicated detail with concise context and links to its primary home.
8. Re-audit changed wording for accidental hindsight or spoilers.

## Prohibited behaviour

- Adding, deleting, or strengthening factual claims to improve the story
- Inventing quotations or transitions that imply facts
- Resolving uncertainty stylistically
- Leaving claim IDs, source IDs, or open-item links inside reader-facing
  paragraphs
- Introducing foreshadowing or outcome-informed emphasis
- Flattening original names or diacritics without a documented reason

## Expected output

An edited draft plus a short change note listing structural changes, removed
duplication, how uncertainties were moved to footnotes, and any factual issues
returned for research rather than silently edited.

## Self-check

- [ ] No new factual claim was introduced.
- [ ] Polish is natural, precise, and readable in the main text.
- [ ] Attribution and uncertainty are preserved in footnotes/apparatus.
- [ ] Main text is free of claim/source ID clutter and constant hedging.
- [ ] Technical explanations remain accurate and proportionate.
- [ ] Repetition has a justified primary home.
- [ ] Changed prose passes a spoiler-scope check.
