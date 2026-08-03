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

`event_time` records when described events occurred.
`public_knowledge_time` records when the newest used information became
knowable. `knowledge_cutoff` is the hard ceiling on permitted knowledge. These
values must not be treated as interchangeable with a source's publication date.
For a document spanning multiple events, use an interval and record more precise
dates with individual claims or sources.

`spoiler_scope` must name allowed and forbidden categories, not merely say
“spoiler-free.” A document may tighten its contract but may not silently widen
it. `content_language` records the actual output language; `pl` is the default,
not a forced value when another language is explicitly requested. Status values
describe workflow state, not evidentiary confidence.

## Absolute spoiler policy

Never reveal information beyond `knowledge_cutoff`, directly or indirectly.

Direct spoilers include future winners, poles, standings, champions, accidents,
deaths, injuries, retirements, penalties, disqualifications, protests,
replacements, calendar changes, technical rulings, team conflicts, and driver
conflicts.

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
validated by later events. Remove dramatic foreshadowing even when it is vague.

## Using later sources

A later-published source may support a clearly separable fact about an earlier
moment only if:

1. contemporary evidence or explicit dated provenance within the later source
   establishes that the fact was publicly knowable by the cutoff;
2. its support can be isolated from later interpretation;
3. no later outcome changes the wording, emphasis, or certainty; and
4. the source record warns that the source contains material beyond the cutoff.

If these conditions cannot be met, omit the claim or find a contemporary source.
