# Las Vegas Grand Prix — source ledger

To kanoniczny rejestr źródeł folderu rundy. Dokumenty treści cytują
`source_id` i `claim_id`; nie prowadzą konkurencyjnych list źródeł. Cutoff
rejestru przy post-race obejmuje `pre-weekend.md`, `pre-race.md`,
`post-race.md` i `standings-after.md` (granica: koniec natychmiastowej
procedury po wyścigu Caesars Palace, sobota 25 IX 1982 PDT).

## Source entry

```yaml
source_id: "ARCHIVE-R15-STAND"
title: "Klasyfikacja po Grand Prix Włoch"
author_or_organisation: "F1 Time Capsule archive (standings-after.md R15)"
publication_date: "not-applicable"
event_date: "1982-09-12"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/15-italian-grand-prix/standings-after.md"
access_date: "2026-09-09"
supports:
  - claim_id: "R16-PW-STD-01"
    scope: "Prowizoryczna kolejność i punkty po Monzy: Rosberg 42; Pironi 38; Watson 33; Prost 31; Lauda 30; Arnoux 28; Tambay 25; Ferrari 73; McLaren 63; Renault 59; Williams 55; otwarte apelacje LB; skala prowizoryczna; konflikt Pironi 38 vs 39 / Ferrari 73 vs 74."
disagreement_notes: "Konflikt Pironi/Ferrari z liniami Wiki (UNC-R16-PW-PIR-PTS / UNC-R16-PO-PIR-PTS)."
notes: "Baza przed Vegas; nie kopiować pełnych tabel do narracji PW/PR."
```

```yaml
source_id: "ARCHIVE-R15-POST"
title: "Grand Prix Włoch — po wyścigu"
author_or_organisation: "F1 Time Capsule archive (post-race.md R15)"
publication_date: "not-applicable"
event_date: "1982-09-12"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/15-italian-grand-prix/post-race.md"
access_date: "2026-09-09"
supports:
  - claim_id: "R16-PW-DEV-01"
    scope: "Arnoux 1, Tambay 2, Andretti 3, Watson 4; Rosberg 8 / 0 pkt; Watson maths must win last round if Rosberg scores 0; Prost/Lauda out of drivers' maths; calendar pointer Las Vegas."
  - claim_id: "R16-PW-TITLE-01"
    scope: "Watson mathematical title chance after Monza; constructors Ferrari nearly locked but arithmetic remains."
disagreement_notes: null
notes: "Carry-forward faktów z Monzy; nie importować foreshadowingu wyniku Vegas."
```

```yaml
source_id: "CAL-01"
title: "The 1982 International Racing Season"
author_or_organisation: "Motor Sport (FIA calendar reproduction)"
publication_date: "1982-01"
event_date: "not-applicable"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/january-1982/35/the-1982-international-racing-season/ — p.35"
access_date: "2026-09-09"
supports:
  - claim_id: "R16-PW-DATE-01"
    scope: "Styczniowa lista FIA: Las Vegas GP 16 October 1982 jako runda 16 — stan przed późniejszym przesunięciem na 25 September."
disagreement_notes: "Faktyczna data wydarzenia 25 IX 1982 (AS/MS/F1.com); CAL-01 = stan przedsezonowy."
notes: "publication_date dnia unknown; content-based availability. Już w season/calendar.md."
```

```yaml
source_id: "AS-ROEBUCK-LV1982"
title: "Grand Prix Gold: 1982 Las Vegas GP (Autosport / Nigel Roebuck reprint — Entry & Practice / warm-up)"
author_or_organisation: "Autosport (Nigel Roebuck); reprint autosport.com 2012"
publication_date: "1982-09"
event_date: "1982-09-23/1982-09-25"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.autosport.com/f1/news/grand-prix-gold-1982-las-vegas-gp-5098970/5098970/ — sections Entry and practice / warm-up before The Grand Prix"
access_date: "2026-09-09"
supports:
  - claim_id: "R16-PW-ENT-01"
    scope: "Weak tickets; FISA ban CART twin-bill; heat vs mid-October 1981; anti-clockwise neck; Murray absent; Andretti CART permission; Arnoux last Renault; title maths Rosberg/Watson quotes; Mansell survival talk."
  - claim_id: "R16-PW-CIR-01"
    scope: "Caesars Palace car-park circuit context; earlier date three weeks vs 1981."
  - claim_id: "R16-PW-FMT-01"
    scope: "Thursday–Friday practice/qualifying; Saturday race."
  - claim_id: "R16-PR-SES-01"
    scope: "Practice/qualifying narrative; Prost pole 1:16.356; Arnoux 2; Alboreto/Cheever; Rosberg 6 Watson 9; Tambay pain; Jarier crash; DNQ Fabi/Salazar/Serra; Byrne reserve; tyre/setup quotes."
  - claim_id: "R16-PR-WU-01"
    scope: "Warm-up ~10:00; start ~13:00 / 13:11; Tambay DNS; Guerrero hose/engine DNS; weather humidity/rain chance; Watson 2nd in warm-up."
  - claim_id: "R16-PR-START-01"
    scope: "Scheduled one o'clock start; warm-up 10."
  - claim_id: "R16-PR-GRID-01"
    scope: "Grid order and qualifying story aligned with F1.com times."
disagreement_notes: "Reprint 2012 — używać tylko passaży contemporary; hard stop przed race narrative w PR. Intro Gold ma hindsight title — kwarantanna dla PW."
notes: "Oryginalny numer AS — luka 1982-R16-AS-01. PW: Entry przed practice times. PR: przez warm-up."
```

```yaml
source_id: "AS-ROEBUCK-LV1982-R"
title: "Grand Prix Gold: 1982 Las Vegas GP (Autosport / Nigel Roebuck reprint — Race)"
author_or_organisation: "Autosport (Nigel Roebuck); reprint autosport.com 2012"
publication_date: "1982-09"
event_date: "1982-09-25"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.autosport.com/f1/news/grand-prix-gold-1982-las-vegas-gp-5098970/5098970/ — section The Grand Prix"
access_date: "2026-09-09"
supports:
  - claim_id: "R16-PO-CLS-01"
    scope: "Alboreto win; Watson 2; Cheever 3; Prost 4; Rosberg 5; Daly 6; narrative phases; quotes Rosberg/Watson/Alboreto."
  - claim_id: "R16-PO-RACE-01"
    scope: "Race narrative: Renault duel; Alboreto pace; Watson charge; Arnoux V5; Andretti suspension; Lauda overheat; tyre vibration; constructors clinch arithmetic when Lauda out."
  - claim_id: "R16-PO-PTS-01"
    scope: "Points places 1–6; Rosberg title with 2 points / 5th; Watson 39 championship."
  - claim_id: "R16-PO-CON-01"
    scope: "Ferrari constructors secured when only Watson among McLarens could still score after Lauda retirement."
disagreement_notes: "UNC-R16-PO-PAT-DNF vs MS clutch; UNC-R16-PO-PIR-PTS Wiki; intro hindsight «only» championship — OK as same-day result framing in PO."
notes: "Isolować narrację wyścigu; nie pisać retrospektywy sezonu ani foreshadowingu Andretti career end."
```

```yaml
source_id: "MS-1982-11-LV"
title: "The Las Vegas Grand Prix — Another first time win"
author_or_organisation: "Motor Sport (J.H. on behalf of D.S.J. & A.H.)"
publication_date: "1982-11"
event_date: "1982-09-23/1982-09-25"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/november-1982/43/las-vegas-grand-prix/"
access_date: "2026-09-09"
supports:
  - claim_id: "R16-PW-ORG-01"
    scope: "Las Vegas 25 September; car-park finale framing; Murray absent Brabham; Tambay withdraw race morning; Jarier crash opens Byrne; end-of-season announced moves atmosphere."
  - claim_id: "R16-PR-WU-01"
    scope: "Tambay warm-up withdrawal; Guerrero engine; blank grid slots."
  - claim_id: "R16-PO-RACE-01"
    scope: "Alboreto win; Watson charge from 9th; Rosberg 5th title; Ferrari constructors; Patrese clutch note; Piquet plug; announced 1983 moves."
disagreement_notes: "Patrese clutch vs AS engine (UNC-R16-PO-PAT-DNF). Tekst miesza wynik i komentarz sezonu — w PO nie budować osobnej retrospektywy; w PW tylko org/entry izolowane."
notes: "publication_date dnia unknown; content-based availability. PW: tylko przedsesyjne. PR: warm-up/DNS. PO: race + same-day moves."
```

```yaml
source_id: "F1COM-1982-LV-RES"
title: "Formula1.com — 1982 Caesar's Palace Grand Prix race result"
author_or_organisation: "Formula One Management / formula1.com"
publication_date: "unknown"
event_date: "1982-09-25"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.formula1.com/en/results/1982/races/452/las-vegas/race-result"
access_date: "2026-09-09"
supports:
  - claim_id: "R16-PO-CLS-01"
    scope: "Classification: Alboreto 1:41:56.888; Watson +27.290; Cheever +56.450; Prost +68.650; Rosberg +71.380; Daly +1 lap; points 9–6–4–3–2–1; retirement list."
disagreement_notes: "DNS Tambay/Guerrero omitted from some tables; DNF label granularity vs AS/MS."
notes: "Wtórne; krzyżować z AS/MS."
```

```yaml
source_id: "F1COM-1982-LV-GRID"
title: "Formula1.com — 1982 Caesar's Palace Grand Prix starting grid"
author_or_organisation: "Formula One Management / formula1.com"
publication_date: "unknown"
event_date: "1982-09-25"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.formula1.com/en/results/1982/races/452/las-vegas/starting-grid"
access_date: "2026-09-09"
supports:
  - claim_id: "R16-PR-GRID-01"
    scope: "Grid positions and qualifying times Prost 1:16.356 through Byrne 1:21.555."
disagreement_notes: "F1.com labels Brabham as Ford — incorrect; BMW per AS/MS (UNC-R16-PR-BRA-ENG)."
notes: "Wtórne; czasy krzyżować z AS."
```

```yaml
source_id: "WP-1982-LV"
title: "Wikipedia — 1982 Caesars Palace Grand Prix"
author_or_organisation: "Wikipedia contributors"
publication_date: "unknown"
event_date: "1982-09-25"
source_type: "SECONDARY"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://en.wikipedia.org/wiki/1982_Caesars_Palace_Grand_Prix"
access_date: "2026-09-09"
supports:
  - claim_id: "R16-PW-DATE-01"
    scope: "Date move from 16 October to 25 September; FISA/Balestre rationale; CART conflict (secondary — cross-check AS)."
  - claim_id: "UNC-R16-PO-FL"
    scope: "Fastest lap Alboreto 1:19.639 lap 59 — secondary timing claim."
disagreement_notes: "Pironi 39 / Ferrari 74 vs archive 38/73; secondary synthesis — not primary for narrative."
notes: "Używać tylko do krzyżowania daty/FL; nie jako jedyne źródło narracji."
```

## Conflict and uncertainty index

| Uncertainty ID | Claim IDs | Source IDs | Status at cutoff | Note |
| --- | --- | --- | --- | --- |
| UNC-R16-PW-PIR-PTS | R16-PW-STD-01 | ARCHIVE-R15-STAND, WP-1982-LV | open | Pironi 38 vs Wiki 39; Ferrari 73 vs 74 |
| UNC-R16-PW-LEN | R16-PW-CIR-01 | F1COM-1982-LV-RES, AS-ROEBUCK-LV1982 | open-nonblocking | Circuit length ~3.650 km; trivial metre variance not in prose |
| UNC-R16-PR-BRA-ENG | R16-PR-GRID-01 | F1COM-1982-LV-GRID, AS-ROEBUCK-LV1982 | resolved-in-prose | F1.com Ford label wrong; prose uses BMW |
| UNC-R16-PO-PIR-PTS | R16-PO-PTS-01 | ARCHIVE-R15-STAND, WP-1982-LV | open | Same Pironi/Ferrari base conflict after LV |
| UNC-R16-PO-PAT-DNF | R16-PO-RACE-01 | AS-ROEBUCK-LV1982-R, MS-1982-11-LV | open | Patrese engine vs clutch |
| UNC-R16-PO-FL | R16-PO-CLS-01 | WP-1982-LV, AS-ROEBUCK-LV1982-R | open-nonblocking | FL lap/time secondary; AS confirms Alboreto FL |

## Quarantined / hard-stop notes

- AS Gold intro hindsight („what would prove to be only world championship”) — quarantine for PW/PR; PO may state title result without career-closure framing.
- MS end-of-season paragraph on Daly sacked without knowing / Alfa may pull out — attribute lightly or omit; do not centre post-race on unconfirmed personnel gossip.
- Do not mark season package complete; no season retrospective document from this ledger.
- No `/pre-weekend 1983` authorized by this race transition.
