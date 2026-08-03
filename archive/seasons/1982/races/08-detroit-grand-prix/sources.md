---
season: "1982"
document_type: "race-source-ledger"
event: "Detroit Grand Prix"
event_time: "[EVENT INTERVAL COVERED BY THIS LEDGER]"
public_knowledge_time: "[WHEN THE LATEST RETAINED SOURCE INFORMATION BECAME PUBLIC]"
knowledge_cutoff: "[LATEST DOCUMENT CUTOFF THIS LEDGER CURRENTLY SUPPORTS]"
spoiler_scope:
  allowed:
    - "[SOURCE METADATA AND CLAIM SUPPORT WITHIN THE SUPPORTED CUTOFF]"
  forbidden:
    - "[LATER SOURCE CONTENT EXCEPT QUARANTINED RISK METADATA]"
content_language: "pl"
research_status: "planned"
source_status: "unstarted"
spoiler_audit_status: "not-run"
last_verified: null
---

# Detroit Grand Prix — source ledger

This is the canonical source ledger for the race folder. Content documents cite
`source_id` and `claim_id`; they do not maintain competing source lists. Update
this ledger's cutoff whenever it begins supporting a later race document.

## Source entry

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

Repeat only the source-entry block from
`templates/shared/source-entry.template.yaml`. Unknown dates remain `unknown`;
do not infer them.

## Conflict and uncertainty index

| Uncertainty ID | Claim IDs | Source IDs | Status at cutoff | Note |
| --- | --- | --- | --- | --- |
| [UNCERTAINTY ID] | [CLAIM IDS] | [SOURCE IDS] | [STATUS] | [NOTE] |
