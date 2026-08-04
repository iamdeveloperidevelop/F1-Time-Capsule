# Temporal scope and spoiler safety

Time is part of content correctness. A statement can be historically true and
still be incorrect for a document if it was not publicly knowable within that
document's boundary.

## Knowledge boundaries

### Season prelude

The boundary is immediately before the season's first official session. It may
use previous-season context, defending champions, confirmed entries and
drivers, announced regulations and calendar, preseason tests, contemporary
expectations, and technology then known. It may not use anything learned during
the season.

### Race prelude

The boundary is immediately before the weekend's first official session. It may
use standings after the previous completed race, publicly known developments,
confirmed entries and replacements, circuit context, then-known weather
expectations, current technical or political storylines, and open questions. It
may not use any session information from that weekend.

### Pre-start weekend brief

The boundary is the race start. It may use preceding practice and qualifying,
the grid, setup problems made public, confirmed pre-start penalties, current
weather and track conditions, relevant quotes and paddock developments, and
what a viewer should watch. It may not reveal anything after the race begins.
The actual historical weekend format determines which preceding sessions exist.

### Post-race report

The boundary follows the race and immediate official post-race procedures. It
may use the complete race, classification, retirements and then-known causes,
points, updated standings, then-known consequences, and contemporary reactions.
It may not use the next weekend or any later development.

### Season retrospective

The task must select an exact season-end boundary at or after the final scheduled
event's immediate official procedures—for example, publication of the
classification valid at that moment. It may use knowledge through that timestamp.
Standings remain “as of cutoff” if unresolved matters exist. Later historical
hindsight is forbidden unless a future task explicitly requests it and the
document labels it as a separate scope.

## Required metadata contract

Every future content document must provide:

```yaml
season: "[SEASON]"
document_type: "[DOCUMENT TYPE]"
event: "[EVENT OR null]"
event_time: "[DATE, INTERVAL, OR HISTORICAL MOMENT DESCRIBED]"
public_knowledge_time: "[WHEN THE LATEST USED INFORMATION BECAME PUBLIC]"
knowledge_cutoff: "[LATEST PERMITTED KNOWLEDGE MOMENT, WITH TIME ZONE IF KNOWN]"
spoiler_scope:
  allowed: ["[PERMITTED CATEGORY]"]
  forbidden: ["[FORBIDDEN CATEGORY]"]
content_language: "[BCP 47 LANGUAGE TAG; pl BY DEFAULT]"
research_status: "[planned | researching | drafted | verified]"
source_status: "[unstarted | partial | claim-mapped | audited]"
spoiler_audit_status: "[not-run | issues-found | corrected | passed]"
last_verified: "[YYYY-MM-DD OR null]"
```

Archive Markdown does **not** embed this schema as YAML front matter. Each
reader-facing `.md` file has a sibling `.meta.yaml` with the same basename
(for example `people-and-organisations.md` ↔ `people-and-organisations.meta.yaml`).
The Markdown file starts at its title so it can be read without a machine
prefix. The reusable schema copy is
`templates/shared/document-metadata.template.yaml`; it mirrors this contract and
must not define competing keys or status values. When a task names a content
document, agents must also read its sibling `.meta.yaml` for cutoff and status.

`event_time` records when described events occurred.
`public_knowledge_time` records when the newest used information became
knowable. `knowledge_cutoff` is the hard ceiling on permitted knowledge. These
values must not be treated as interchangeable with a source's publication date.
`public_knowledge_time` must not exceed `knowledge_cutoff`.
For a document spanning multiple events, use an interval and record more precise
dates with individual claims or sources.

`spoiler_scope` must name allowed and forbidden categories, not merely say
“spoiler-free.” A document may tighten its contract but may not silently widen
it. `content_language` records the actual output language; `pl` is the default,
not a forced value when another language is explicitly requested. Status values
describe workflow state, not evidentiary confidence.

Initial template status is `research_status: planned`,
`source_status: unstarted`, and `spoiler_audit_status: not-run`. Do not introduce
synonyms such as `not-started` or `not-verified`.

The race filenames map to existing contract types as follows:

- `pre-weekend.md` uses `document_type: race-prelude`;
- `pre-race.md` uses `document_type: pre-start-weekend-brief`;
- `post-race.md` uses `document_type: post-race-report`;
- `standings-after.md` uses `document_type: standings-snapshot`;
- `sources.md` is a supporting `race-source-ledger`, bounded by the latest
  document cutoff it supports and using the canonical source-entry schema.

## Absolute spoiler policy

Never reveal information beyond `knowledge_cutoff`, directly or indirectly.

### What counts as a spoiler

Direct spoilers are outcome and status leaks: future winners, poles, standings,
champions, accidents, deaths, injuries, retirements, penalties,
disqualifications, protests, replacements, calendar changes, technical rulings,
and team or driver conflicts that were not yet public.

Indirect spoilers include phrases such as “as would later become clear,” “this
would prove decisive,” “the future champion,” “his final season,” “the last
months of his career,” “a tragic weekend,” “a car that would disappoint,” “the
beginning of the end,” or “an apparently minor decision with enormous
consequences.” They also include prominence given to a person or detail only
because later events made it important.

Hindsight contamination judges an earlier choice with unavailable knowledge.
Do not write that a team made the wrong design choice based on later outcomes.
State what contemporary evidence supported: for example, that reports
questioned cooling and reliability while the team expected better straight-line
performance.

Predictions must remain attributed contemporary expectations, never facts
validated by later events. Remove dramatic foreshadowing that signals a later
outcome, even when the wording is vague.

### Calibration: do not over-police dating trivia

Spoiler safety protects the reader's experience of the weekend and season, not
archival pedantry. Treat the following as **not** automatic spoilers and **not**
reasons to empty otherwise useful prose:

- an unknown exact publication day for a clearly pre-cutoff preview, entry list
  survey, or contemporary expectation piece (see content-based availability in
  `docs/source-policy.md`);
- minor differences between successive pre-cutoff forecasts or paddock notes
  that the reader will see resolved in later allowed documents (for example
  weather outlook revisions), when none of them disclose a forbidden outcome;
- incomplete clock-time precision for a session when the calendar day and
  sequence are known and no later result is implied.

Prefer a readable, attributed contemporary account with a short footnote over a
skeleton document that mentions only the one source with a fully known
day-of-month. Do not let source-dating caution collapse the field to defending
champions or eventual winners.

## Using later sources

A later-published source may support a clearly separable fact about an earlier
moment only if:

1. contemporary evidence, explicit dated provenance within the later source, or
   a documented content-based availability judgment establishes that the fact
   was publicly knowable by the cutoff;
2. its support can be isolated from later interpretation;
3. no later outcome changes the wording, emphasis, or certainty; and
4. the source record warns that the source contains material beyond the cutoff.

If these conditions cannot be met, omit the claim or find a contemporary source.
