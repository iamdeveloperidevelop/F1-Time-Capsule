# Source policy

Research must make every important factual claim traceable while protecting the
document's temporal boundary.

## Source hierarchy

Prefer, in order appropriate to the claim:

1. official contemporary regulations and bulletins;
2. official entry lists and results documents;
3. contemporary newspapers and motorsport magazines;
4. team, driver, and manufacturer announcements;
5. contemporary television and radio material;
6. reputable historical archives;
7. specialist databases for structured facts;
8. later secondary analysis, only when necessary.

Do not depend on unsourced fan pages, content farms, AI-generated pages, or
social-media summaries without primary evidence. Wikipedia may help locate
sources but must not be the only support for a disputed claim. A modern
retrospective is not evidence of what people expected at the time.

Structured databases often expose full-season outcomes. Extract only facts
allowed by the current cutoff, and do not let surrounding records influence the
narrative.

## Source record

Where the source permits it, record:

```yaml
source_id: "[SOURCE ID]"
title: "[SOURCE TITLE]"
author_or_organisation: "[AUTHOR, PUBLISHER, CREATOR, OR ORGANISATION]"
publication_date: "[DATE OR unknown]"
event_date: "[DATE, INTERVAL, OR not-applicable]"
source_type: "[BULLETIN | RESULT | PRESS | ANNOUNCEMENT | BROADCAST | ARCHIVE | DATABASE | SECONDARY]"
contemporary: "[true | false]"
spoiler_risk: "[none | contains-later-material | unknown]"
locator: "[URL, ARCHIVAL REFERENCE, ISSUE/PAGE, OR TIMECODE]"
access_date: "[YYYY-MM-DD OR not-applicable]"
supports:
  - claim_id: "[CLAIM ID]"
    scope: "[EXACTLY WHAT THIS SOURCE SUPPORTS]"
disagreement_notes: "[CONFLICTS OR UNCERTAINTY, OR null]"
notes: "[LIMITATIONS, TRANSLATION, OR null]"
```

Do not invent a precise calendar `publication_date` when the source does not
give one; leave the field `unknown` rather than guessing “15 January” or similar.
`publication_date`, `event_date`, and the content document's `knowledge_cutoff`
are distinct. Record page, section, or timecode where practical. A citation
supports only the claim expressed in `scope`, not every nearby statement.

### Content-based availability

An unknown exact publication day does **not**, by itself, quarantine otherwise
suitable contemporary material. Agents may judge whether a source was usable at
the document cutoff from the combination of:

1. issue or cover dating (for example a monthly magazine dated January 1982);
2. the cited content itself (preseason preview language, no session or race
   results beyond the cutoff, no post-event framing); and
3. any stronger dated evidence when available.

Record that judgment briefly in `notes` or a footnote. Prefer using such a
source as a provisional, attributed contemporary report over emptying the
reader-facing field. If the same issue mixes pre-cutoff and post-cutoff
material, use only the separable pre-cutoff claims and mark
`spoiler_risk: contains-later-material`.

Do **not** block an entire preseason preview, entry survey, or expectations
piece solely because a monthly magazine's day-of-month is unknown, when the
cited passage is clearly pre-cutoff in substance.

Set `contemporary` according to the source, not the desired evidence profile.
Set `spoiler_risk: contains-later-material` whenever any surrounding source
material crosses the document cutoff, even if the cited fact is safely
separable. Use `unknown` until the surrounding material has been checked.

`templates/shared/source-entry.template.yaml` is the reusable copy of this
schema. Race ledgers in `sources.md` use repeated entries in this exact shape;
they must not invent a second citation format.

## Claim categories

- **Confirmed fact:** supported by suitable evidence and publicly knowable by
  the cutoff.
- **Contemporary expectation:** a prediction or opinion attributed to a press,
  team, driver, or paddock source available by the cutoff.
- **Author interpretation:** a cautious inference from confirmed information,
  labelled as analysis and no more certain than its premises.
- **Unresolved disagreement:** incompatible credible accounts that available
  evidence cannot settle.

Do not convert expectations into retrospective facts. Avoid “clearly destined
to,” “obviously the strongest,” “inevitably,” or “proved that” unless the
relevant proof itself existed before the cutoff.

## Disagreement and uncertainty

When credible sources disagree:

1. record the disagreement and each material version in research notes,
   footnotes, or the source ledger;
2. compare proximity, authority, date, independence, and specificity;
3. explain which version is better supported, if one is;
4. preserve uncertainty if the evidence remains inconclusive; and
5. never guess or silently merge incompatible accounts.

Absence of evidence is not proof that an event did not occur. Keep confidence
proportional to the evidence. Make translations, reconstructed dates, and
unresolved conflicts visible in footnotes or source apparatus, not as repeated
interruptions in the main narrative.

## Reader-facing presentation

Reader-facing prose presents the best-supported account in natural language.
Do not place claim IDs, source IDs, open-item ledger links, audit statuses, or
research meta-commentary in the running text.

When the reader needs a caveat (provisional reconstruction, undated source,
unresolved conflict, attributed expectation that must not be mistaken for
fact), mark the relevant sentence with a footnote marker and put the caveat
under `## Przypisy`. Detailed citation records belong under `## Uwagi źródłowe`
or in `sources.md`. Use `templates/shared/uncertainty-note.template.md` for
research-grade uncertainty records when a fuller note is needed outside the
narrative.

## Unresolved evidence without workflow blockage

An unavailable, incomplete, or day-undated source must not be overstated as a
hard-dated official fact. Under content-based availability, a contemporary
press or magazine piece whose substance is clearly pre-cutoff may still support
reader-facing orientation as a provisional, source-attributed report: keep the
main sentence readable, attach at most a brief footnote for the dating
limitation, and do not increase the claim's certainty, prominence, or scope
from later knowledge. Exact day-of-month gaps for non-outcome material are not,
by themselves, a reason to omit the claim, stop an otherwise safe workflow
transition, or require the user to perform verification.

Record the gap in the season's `things-to-resolve-after-season.md` ledger with:

- the affected document and claim or question;
- the boundary at which it remained unresolved;
- the exact evidence needed to resolve it; and
- a status such as `open`.

Reader-facing text may rely only on uncertainty already supportable at its
boundary. Footnotes may note that an identified source could not be dated or
fully verified. The document must not reveal a later answer, use the gap to
select later-known participants or details, or retrospectively alter an earlier
document. A later authorized stage may resolve the item only with evidence
public by that later stage's cutoff.

## Copyright and quotations

Paraphrase factual material. Do not reproduce long copyrighted passages. Use a
short direct quotation only when its exact wording has meaningful historical
value, and identify its speaker, context, source, and date.
