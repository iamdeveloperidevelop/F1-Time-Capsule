# Future content contracts

These contracts describe future documents; they do not instantiate content.
Every document must use the metadata in `temporal-scope.md`, including an
explicit `knowledge_cutoff` and categorical `spoiler_scope`. It must follow
`source-policy.md` and `methodology.md`.

Length ranges are editorial targets, not quotas. Tables and source records do
not count toward prose length. Every final audit checks direct spoilers,
indirect spoilers, hindsight, dramatic foreshadowing, later-informed emphasis,
source dates, and whether the cutoff matches the document type.

## Shared contract requirements

- **Allowed knowledge:** only facts publicly knowable at or before the declared
  cutoff, further limited by the selected contract.
- **Forbidden knowledge:** all later facts and interpretations, even if a source
  used for an earlier claim contains them.
- **Sources:** every major factual claim is mapped to suitable evidence; major
  expectations are attributed; disagreements remain visible.
- **Metadata:** all fields from the canonical metadata contract are required.
  Use `event: null` only when the document is genuinely season-wide.
- **Duplication:** link to a fact's primary home and include only the context
  this document needs.
- **Audit:** the document cannot advance to `verified` status until
  `spoiler_audit_status: passed` and `source_status: audited`. A later workflow
  transition may still use a safe document with `source_status: partial` when
  its reader-facing claims are cutoff-safe, its limitations are explicit, and
  each unresolved item is recorded in
  `things-to-resolve-after-season.md`. `issues-found` never permits progression
  until the reader-facing issue is removed or rewritten as cutoff-safe
  uncertainty.

## Season prelude

- **Purpose:** orient the reader at the last moment before official season
  running begins.
- **Allowed knowledge:** previous-season context, confirmed participants,
  announced rules and calendar, preseason activity, known technology, and
  attributed contemporary expectations available before the opening session.
- **Forbidden knowledge:** any in-season session, result, development, change,
  or hindsight.
- **Expected sections:** boundary note; inherited context; confirmed field;
  regulations and technology overview; calendar outline; preseason evidence;
  contemporary questions; source notes.
- **Sources:** broad contemporary coverage plus official entries, regulations,
  announcements, and calendar material.
- **Length:** approximately 1,800–3,500 Polish words.
- **Duplication boundary:** summarise and link specialised season references;
  do not absorb their complete detail.
- **Metadata and audit:** season-prelude type; `event: null`; cutoff immediately
  before the first official session; confirm zero in-season knowledge.

## Season context

- **Purpose:** explain the inherited sporting, organisational, economic, and
  political situation at a stated season boundary.
- **Allowed knowledge:** context established by its cutoff, normally the season
  prelude boundary unless a version explicitly states another earlier cutoff.
- **Forbidden knowledge:** in-season consequences and retrospective judgments.
- **Expected sections:** boundary; previous context; governance; paddock and
  commercial setting; live questions; uncertainties; sources.
- **Sources:** contemporary reporting and official organisational records, with
  later synthesis used only for separable earlier facts.
- **Length:** approximately 1,200–2,500 words.
- **Duplication boundary:** owns broad context, not full team histories,
  biographies, regulations, or technical explanations.
- **Metadata and audit:** season-context type; explicit boundary; audit causal
  language for hindsight.

## Season regulations

- **Purpose:** explain rules and announced changes as understood at the cutoff.
- **Allowed knowledge:** official text, bulletins, and contemporary explanations
  public by the cutoff.
- **Forbidden knowledge:** later interpretations, enforcement, protests,
  loopholes, rulings, and effects.
- **Expected sections:** scope and authority; sporting rules; technical rules;
  changes; unresolved interpretations; plain-language implications; sources.
- **Sources:** official regulations and bulletins lead; contemporary specialist
  explanation may clarify but not override them.
- **Length:** approximately 1,200–3,000 words.
- **Duplication boundary:** owns detailed rule explanations; event documents
  quote only the operative point.
- **Metadata and audit:** season-regulations type; record regulation version and
  cutoff; audit every claimed implication against then-available text.

## Season technology

- **Purpose:** introduce cars, systems, design trends, and technical questions
  knowable at the boundary.
- **Allowed knowledge:** disclosed or credibly observed technology and
  contemporary analysis available by the cutoff.
- **Forbidden knowledge:** later performance, reliability, development paths,
  rulings, and retrospective labels.
- **Expected sections:** boundary; regulatory setting; concepts; known designs;
  trade-offs; open questions; glossary links; sources.
- **Sources:** regulations, team or manufacturer material, contemporary
  technical press, and clearly labelled observations.
- **Length:** approximately 1,800–4,000 words.
- **Duplication boundary:** primary home for detailed technical explanations;
  avoid team histories and outcome narratives.
- **Metadata and audit:** season-technology type; audit adjectives and emphasis
  for outcome-derived judgment.

## Season teams

- **Purpose:** provide cutoff-safe reference entries for participating teams.
- **Allowed knowledge:** identity, organisation, personnel, equipment, and
  contemporary expectations confirmed by the cutoff.
- **Forbidden knowledge:** later form, disputes, personnel changes, and fate.
- **Expected sections:** field overview; consistent team entries; organisation;
  drivers and equipment links; stated aims; uncertainties; sources.
- **Sources:** official entries and announcements, team material, and
  contemporary independent reporting.
- **Length:** approximately 200–500 words per team plus a short overview.
- **Duplication boundary:** owns team reference facts, not full biographies,
  engineering treatises, or repeated event previews.
- **Metadata and audit:** season-teams type; audit each entry against the same
  cutoff and avoid unequal later-informed prominence.

## Season drivers

- **Purpose:** provide cutoff-safe reference entries for confirmed drivers.
- **Allowed knowledge:** careers and status up to the cutoff, confirmed roles,
  and attributed current expectations.
- **Forbidden knowledge:** later results, incidents, replacements, injuries,
  career endings, and legacy.
- **Expected sections:** field overview; consistent driver entries; prior record;
  current role; relevant style or experience; expectations; sources.
- **Sources:** official entries, driver or team statements, contemporary records,
  and reputable archives limited to pre-cutoff facts.
- **Length:** approximately 180–450 words per driver plus a short overview.
- **Duplication boundary:** owns biographical orientation; event documents use
  only immediately relevant details.
- **Metadata and audit:** season-drivers type; audit career language for hidden
  “final,” “future,” or legacy spoilers.

## Season people and organisations

- **Purpose:** explain other relevant participants and governing, commercial,
  entrant, supplier, or representative bodies.
- **Allowed knowledge:** roles, authority, relationships, and live issues
  publicly known at the cutoff.
- **Forbidden knowledge:** later decisions, conflicts, reorganisations, and
  historical significance.
- **Expected sections:** scope; people; organisations; relationships and
  authority; current issues; unresolved points; sources.
- **Sources:** official records, announcements, and contemporary reporting.
- **Length:** approximately 800–2,000 words, scaled to relevance at the cutoff.
- **Duplication boundary:** primary home for non-driver personnel and
  institutional explanation; link from event or team documents.
- **Metadata and audit:** people-and-organisations type; audit selection and
  emphasis for knowledge derived from later importance.

## Season calendar

- **Purpose:** record the announced schedule as it stood at a specific cutoff.
- **Allowed knowledge:** dates, venues, status, and changes already public.
- **Forbidden knowledge:** later postponements, cancellations, replacements,
  results, and schedule hindsight.
- **Expected sections:** boundary; canonical schedule; status notes; announced
  changes already effective; source notes.
- **Sources:** governing-body calendars, official bulletins, promoters, and
  corroborating contemporary reports.
- **Length:** approximately 300–900 words plus one canonical schedule table.
- **Duplication boundary:** owns schedule representation; other documents link
  rather than reproduce it.
- **Metadata and audit:** season-calendar type; record calendar version and
  cutoff; audit against accidental final-season schedule data.

## Season glossary

- **Purpose:** define period-relevant sporting, technical, and organisational
  terms without importing later meanings.
- **Allowed knowledge:** concise definitions accurate and knowable at the
  glossary's stated cutoff.
- **Forbidden knowledge:** outcome examples, later rule evolution, and
  retrospective significance.
- **Expected sections:** scope; alphabetical terms; cross-references; source
  notes for disputed or period-specific meanings.
- **Sources:** regulations, period technical references, and authoritative
  language sources.
- **Length:** usually 30–120 words per entry.
- **Duplication boundary:** definitions only; detailed concepts belong in
  regulations, technology, or contextual references.
- **Metadata and audit:** season-glossary type; audit examples for hidden
  outcomes and keep one canonical definition per term.

## Race prelude

- **Purpose:** establish the event state immediately before the weekend begins.
- **Allowed knowledge:** completed earlier events, current standings, confirmed
  entries and changes, venue context, public developments, forecasts, live
  storylines, and questions available before the first official session.
- **Forbidden knowledge:** any practice, qualifying, grid, race, or later
  weekend information.
- **Expected sections:** boundary; arrival state; standings links; entries;
  circuit context; technical and political storylines; weather expectations;
  questions; sources.
- **Sources:** official event documents and standings, contemporary previews,
  announcements, and dated forecasts.
- **Length:** approximately 1,200–2,400 words.
- **Duplication boundary:** advances from the previous report; links season
  references and avoids full biographies or technical recaps.
- **Metadata and audit:** race-prelude type; identify `[GRAND PRIX]`; cutoff
  before its first official session; search explicitly for same-weekend data.

## Pre-start weekend brief

- **Purpose:** update the reader after all pre-race sessions and stop at the
  instant before the race starts.
- **Allowed knowledge:** completed preceding sessions, qualifying, grid,
  publicly known setup issues, confirmed penalties, current conditions, quotes,
  paddock developments, and cutoff-safe viewing cues.
- **Forbidden knowledge:** the start, race events, result, post-race action, and
  implications learned afterward.
- **Expected sections:** boundary and weekend format; practice; qualifying;
  grid; penalties and changes; conditions; what to watch; sources.
- **Sources:** official timing, classifications, decisions, bulletins, weather
  records, and contemporary reporting or broadcasts.
- **Length:** approximately 1,000–2,000 words.
- **Duplication boundary:** adds weekend evidence without restating the entire
  race prelude; grid appears once canonically.
- **Metadata and audit:** pre-start-weekend-brief type; cutoff immediately
  before race start; adversarially remove outcome-shaped viewing cues.

## Post-race report

- **Purpose:** narrate and explain the race using only the immediate post-race
  state.
- **Allowed knowledge:** race events, classification, retirements and then-known
  causes, points, updated standings, immediate procedures, consequences already
  public, and contemporary reactions.
- **Forbidden knowledge:** next-event information, later appeals or rulings,
  later diagnoses, future consequences, and season hindsight.
- **Expected sections:** boundary; race narrative; decisive factors knowable by
  cutoff; classification; retirements; official action; brief standings
  context linked to the snapshot; reactions; unresolved issues; sources.
- **Sources:** official timing, classification and decisions; contemporary
  reports, broadcasts, and attributed participant reactions.
- **Length:** approximately 1,800–3,500 words plus the canonical race
  classification.
- **Duplication boundary:** does not replay the full prelude; owns the event's
  narrative and classification, but does not duplicate the full championship
  tables from `standings-after.md`.
- **Metadata and audit:** post-race-report type; state the exact procedural
  cutoff; label unresolved matters and exclude their later resolution.

## Standings snapshot

- **Purpose:** preserve the championship state at one precise official boundary.
- **Allowed knowledge:** points and classifications valid at the cutoff,
  including only decisions already official then.
- **Forbidden knowledge:** later corrections, appeals, disqualifications,
  dropped-score effects not yet applicable, and future rounds.
- **Expected sections:** boundary; driver table; constructor table where
  applicable; scoring notes; ties; provisional or disputed items; sources.
- **Sources:** official classifications and regulations, independently
  recalculated where useful.
- **Length:** tables plus approximately 150–500 explanatory words.
- **Duplication boundary:** canonical snapshot linked by reports; do not maintain
  competing copies for the same boundary. It is the primary home for driver and
  constructor standings tables and points gained at the event.
- **Metadata and audit:** standings-snapshot type; event identifies the boundary;
  verify arithmetic, tie-breaking, eligibility, and status as of the cutoff.

## Race source ledger

- **Purpose:** keep one claim-linked source record for all documents in a race
  folder.
- **Allowed knowledge:** source metadata, support scope, and uncertainty needed
  by race documents at or before the ledger's declared cutoff.
- **Forbidden knowledge:** later source content in claims or narrative. A later
  source may be recorded only with its spoiler risk and strict isolation.
- **Expected sections:** boundary; repeated canonical source entries; conflict
  and uncertainty index.
- **Sources:** each entry follows `docs/source-policy.md` and
  `templates/shared/source-entry.template.yaml`.
- **Length:** no prose target; store only metadata and notes needed for
  traceability.
- **Duplication boundary:** `sources.md` is the sole race-folder ledger;
  documents cite source and claim identifiers rather than copying source lists.
- **Metadata and audit:** race-source-ledger type; advance its cutoff only when
  it begins supporting a later race document and recheck spoiler risk.

## Season retrospective

- **Purpose:** interpret the complete season from the moment it concludes.
- **Allowed knowledge:** events and consequences knowable through the declared
  season-end cutoff.
- **Forbidden knowledge:** later careers, later seasons, later deaths or
  injuries, modern reputation, and historical hindsight unless a separately
  labelled future task explicitly widens scope.
- **Expected sections:** boundary; season arc; sporting and technical themes;
  teams and drivers; governance; standings as of cutoff; unresolved season-end
  issues; contemporary assessments; sources.
- **Sources:** full season official record, contemporary season-end coverage,
  and earlier archive documents; later sources only under the strict isolation
  rule.
- **Length:** approximately 3,000–6,000 words.
- **Duplication boundary:** synthesises rather than concatenates race reports or
  reference documents.
- **Metadata and audit:** season-retrospective type; cutoff at season conclusion;
  audit every legacy claim and exclude post-season resolutions beyond it.

## Generic body example

```text
[CANONICAL METADATA FROM docs/temporal-scope.md]

# [TITLE]

[CONTRACT-SPECIFIC SECTIONS]
```
