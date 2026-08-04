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

Unknown dates must remain `unknown`, not inferred. `publication_date`,
`event_date`, and the content document's `knowledge_cutoff` are distinct.
Record page, section, or timecode where practical. A citation supports only the
claim expressed in `scope`, not every nearby statement.

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

1. state the disagreement and each material version;
2. compare proximity, authority, date, independence, and specificity;
3. explain which version is better supported, if one is;
4. preserve uncertainty if the evidence remains inconclusive; and
5. never guess or silently merge incompatible accounts.

Absence of evidence is not proof that an event did not occur. Keep confidence
proportional to the evidence and make translations or reconstructed dates
visible under the reader-facing presentation policy in `methodology.md`.

## Unresolved evidence without workflow blockage

An unavailable, incomplete, or insufficiently dated source must not be stated
as a confirmed reader-facing fact. It may be retained as an explicitly
provisional, source-attributed report when that is useful for orientation:
preserve the uncertainty, record the source limitation in a sparse endnote or
source section, and do not increase the claim's certainty, prominence, or scope
from later knowledge. Repeating verification caveats in the narrative is not
required. The gap is not, by itself, a reason to stop an otherwise safe
workflow transition or require the user to perform verification.

Record the gap in the season's `things-to-resolve-after-season.md` ledger with:

- the affected document and claim or question;
- the boundary at which it remained unresolved;
- the exact evidence needed to resolve it; and
- a status such as `open`.

Reader-facing text may state only the uncertainty already supportable at its
boundary. Attribute a provisional report in prose and place dating,
verification, source-ID, and locator detail in an endnote or source section as
defined in `methodology.md`. Material competing versions still belong
concisely in prose. The text must not reveal a later answer, use the gap to
select later-known participants or details, or retrospectively alter an earlier
document. A later authorized stage may resolve the item only with evidence
public by that later stage's cutoff.

## Copyright and quotations

Paraphrase factual material. Do not reproduce long copyrighted passages. Use a
short direct quotation only when its exact wording has meaningful historical
value, and identify its speaker, context, source, and date.
