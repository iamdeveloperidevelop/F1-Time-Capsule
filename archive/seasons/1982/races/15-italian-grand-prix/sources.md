# Italian Grand Prix — source ledger

To kanoniczny rejestr źródeł folderu rundy. Dokumenty treści cytują
`source_id` i `claim_id`; nie prowadzą konkurencyjnych list źródeł. Cutoff
rejestru przy post-race obejmuje `pre-weekend.md`, `pre-race.md`,
`post-race.md` i `standings-after.md` (granica: koniec natychmiastowej
procedury po wyścigu Monza, niedziela 12 IX 1982 CEST).

## Source entry

```yaml
source_id: "ARCHIVE-R14-STAND"
title: "Klasyfikacja po Grand Prix Szwajcarii"
author_or_organisation: "F1 Time Capsule archive (standings-after.md R14)"
publication_date: "not-applicable"
event_date: "1982-08-29"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/14-swiss-grand-prix/standings-after.md"
access_date: "2026-09-09"
supports:
  - claim_id: "R15-PW-STD-01"
    scope: "Prowizoryczna kolejność i punkty po Dijon: Rosberg 42; Pironi 38; Prost 31; Watson/Lauda 30; de Angelis 23; Patrese 21; Piquet 20; Arnoux/Tambay 19; Ferrari 63; McLaren 60; Williams 55; Renault 50; otwarte apelacje LB; skala prowizoryczna; konflikt Pironi 38 vs 39 / Ferrari 63 vs 64."
disagreement_notes: "Konflikt Pironi/Ferrari z liniami Wiki (UNC-R15-PW-PIR-PTS)."
notes: "Baza przed Monzą; nie kopiować pełnych tabel do narracji PW/PR."
```

```yaml
source_id: "ARCHIVE-R14-POST"
title: "Grand Prix Szwajcarii — po wyścigu"
author_or_organisation: "F1 Time Capsule archive (post-race.md R14)"
publication_date: "not-applicable"
event_date: "1982-08-29"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/14-swiss-grand-prix/post-race.md"
access_date: "2026-09-09"
supports:
  - claim_id: "R15-PW-DEV-CH"
    scope: "Rosberg 1, Prost 2, Lauda 3; Tambay DNS; Rosberg lider 42; Ferrari bez punktów CH; Patrząc stąd dalej → Italian GP Monza 12 IX."
disagreement_notes: null
notes: "Carry-forward faktów z Dijon; nie importować foreshadowingu Monza weekend."
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
  - claim_id: "R15-PW-EVT-01"
    scope: "Italian GP Monza 12 September 1982 na ogłoszonej liście FIA; Las Vegas GP 16 October jako następna ogłoszona runda."
disagreement_notes: null
notes: "publication_date dnia unknown; content-based availability. Już w season/calendar.md."
```

```yaml
source_id: "MS-1982-10-IT"
title: "The Italian Grand Prix — Renault v Ferrari"
author_or_organisation: "Motor Sport (D.S.J. / Jenkinson)"
publication_date: "1982-10"
event_date: "1982-09-10/1982-09-12"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/october-1982/46/italian-grand-prix-6/"
access_date: "2026-09-09"
supports:
  - claim_id: "R15-PW-ORG-01"
    scope: "Atmosfera Monzy / tifosi Ferrari; Andretti return / Fiorano / Tambay testing; ~80% fitness; improved engines; Alfa turbo show; Toleman TG183; format Friday–Saturday; start ~15:30 / warm-up ~12:30."
  - claim_id: "R15-PR-Q"
    scope: "Qualifying narrative; Andretti pole 1:28.473; Piquet/Tambay; Laffite 574 kg; DNQ March/ATS/Theodore; speeds; Renault race setup priority."
  - claim_id: "R15-PO-RACE"
    scope: "Race narrative; Arnoux win; Tambay 2 Andretti 3; Brabham clutches; first-lap chicane pile-up; Prost injection; Rosberg wing; Pertini; Italian press Ferrari-1983 framing."
disagreement_notes: "Tekst miesza preview i wynik; izolować pasaże wg cutoff dokumentu."
notes: "publication_date dnia unknown; content-based availability. PW: tylko org/entry/przedsesyjne. PR: Qualifying + warm-up. PO: Race. Kwarantanna retrospectives spoza cutoff."
```

```yaml
source_id: "AS-ROEBUCK-IT1982"
title: "Grand Prix Gold: 1982 Italian GP (Autosport / Nigel Roebuck reprint — Entry & Practice)"
author_or_organisation: "Autosport (Nigel Roebuck); reprint autosport.com 2012"
publication_date: "1982-09"
event_date: "1982-09-10/1982-09-12"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.autosport.com/f1/news/grand-prix-gold-1982-italian-gp-5098971/5098971/ — sections Entry and practice / warm-up before The Grand Prix"
access_date: "2026-09-09"
supports:
  - claim_id: "R15-PW-ENT"
    scope: "Andretti return / ticket sales; Tambay pain ~80%; Arnoux→Ferrari day before practice; Baldi A5 / Surer A4; Tyrrell Denim; March Michelin Mass/Keegan; Toleman TG183; circuit/atmosphere."
  - claim_id: "R15-PR-SES"
    scope: "Practice/qualifying detail; Andretti 1:28.473 pole; grid story; Cheever→Renault 1983; Laffite underweight; warm-up Piquet spare / Tambay engine; Brabham pit plan; Gilles messages; start ~15:28–15:30; tyre notes."
disagreement_notes: "Reprint 2012 — używać tylko passaży contemporary; hard stop przed race narrative w PR. Intro Gold ma hindsight Vegas/title — kwarantanna dla PW/PR."
notes: "Oryginalny numer AS — luka 1982-R15-AS-01. PW: Entry przed practice times. PR: przez warm-up."
```

```yaml
source_id: "AS-ROEBUCK-IT1982-R"
title: "Grand Prix Gold: 1982 Italian GP (Autosport / Nigel Roebuck reprint — Race)"
author_or_organisation: "Autosport (Nigel Roebuck); reprint autosport.com 2012"
publication_date: "1982-09"
event_date: "1982-09-12"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.autosport.com/f1/news/grand-prix-gold-1982-italian-gp-5098971/5098971/ — section The Grand Prix"
access_date: "2026-09-09"
supports:
  - claim_id: "R15-PO-CLS-01"
    scope: "Arnoux win; Tambay 2; Andretti 3; Watson 4; narrative phases; sticky throttle; Brabham clutches; Prost injection; Rosberg wing; quotes Arnoux/Andretti/Rosberg; Watson maths vs Rosberg; constructors «virtually»."
  - claim_id: "R15-PO-PTS-01"
    scope: "Points places 1–6; championship arithmetic after Monza (with archive Pironi base adjustment in standings doc)."
disagreement_notes: "UNC-R15-PO-GAP gaps vs F1.com; UNC-R15-PO-DNF cause granularity; Wiki Pironi 39 vs archive 38."
notes: "Isolować narrację wyścigu; kwarantanna «destiny… Las Vegas finale» / «final» Andretti career jako domknięcie — tylko atrybucja same-day maths Watson/Rosberg i calendar pointer."
```

```yaml
source_id: "F1COM-1982-IT-RES"
title: "Formula1.com — 1982 Italian Grand Prix race result"
author_or_organisation: "Formula One Management / formula1.com"
publication_date: "unknown"
event_date: "1982-09-12"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.formula1.com/en/results/1982/races/451/italy/race-result"
access_date: "2026-09-09"
supports:
  - claim_id: "R15-PO-CLS-01"
    scope: "Classification: Arnoux 1:22:25.734; Tambay +14.060; Andretti +48.450; Watson +87.850; Alboreto/Cheever +1 lap; points 9–6–4–3–2–1; retirement list."
disagreement_notes: "UNC-R15-PO-GAP vs Wiki hundredths; DNF labels NC vs classified."
notes: "Wtórne; krzyżować z AS/MS."
```

```yaml
source_id: "F1COM-1982-IT-GRID"
title: "Formula1.com — 1982 Italian Grand Prix starting grid"
author_or_organisation: "Formula One Management / formula1.com"
publication_date: "unknown"
event_date: "1982-09-12"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.formula1.com/en/results/1982/races/451/italy/starting-grid"
access_date: "2026-09-09"
supports:
  - claim_id: "R15-PR-GRID"
    scope: "26-car starting grid times Andretti 1:28.473 through Serra 1:35.230."
disagreement_notes: "UNC-R15-PR-Q minor Q1/Q2 Wiki variances."
notes: "Wtórne; krzyżować z AS/MS/Wiki Q."
```

```yaml
source_id: "WP-1982-IT"
title: "Wikipedia — 1982 Italian Grand Prix"
author_or_organisation: "Wikipedia contributors"
publication_date: "unknown"
event_date: "1982-09-12"
source_type: "SECONDARY"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://en.wikipedia.org/wiki/1982_Italian_Grand_Prix"
access_date: "2026-09-09"
supports:
  - claim_id: "R15-PW-CIR"
    scope: "Date 12 Sep 1982; Monza; course ~5.800 km; 52 laps; official name LIII Gran Premio d'Italia (cross-check only)."
  - claim_id: "R15-PR-Q"
    scope: "Qualifying table cross-check."
  - claim_id: "R15-PO-FL"
    scope: "Fastest lap Arnoux 1:33.619 lap 25 (cross-check)."
  - claim_id: "R15-PO-CHAMP-NOTE"
    scope: "Secondary note Prost/Lauda mathematically eliminated; top-5 standings lines (Pironi 39 / Ferrari 74 — conflict with archive)."
disagreement_notes: "Contains career retrospectives («final» Andretti); quarantine. Pironi 39 / Ferrari 74 vs archive line."
notes: "Tylko cross-check; nie primary narrative. Kwarantanna foreshadowing."
```

## Conflict and uncertainty index

| Uncertainty ID | Claim IDs | Source IDs | Status at cutoff | Note |
| --- | --- | --- | --- | --- |
| UNC-R15-PW-PIR-PTS | R15-PW-STD-01 | ARCHIVE-R14-STAND, WP-1982-IT | open | Pironi 38 vs 39 / Ferrari base 63 vs 64 carry-forward |
| UNC-R15-PW-LEN | R15-PW-CIR | F1COM-1982-IT-RES, WP-1982-IT, MS-1982-10-IT | open-nonblocking | ~5.800 km adopted; trivial mile/km variance ledger-only |
| UNC-R15-PR-Q | R15-PR-GRID, R15-PR-Q | F1COM-1982-IT-GRID, AS-ROEBUCK-IT1982, WP-1982-IT | open-nonblocking | Minor Q1/Q2 table variances; best times adopted |
| UNC-R15-PO-GAP | R15-PO-CLS-01 | F1COM-1982-IT-RES, WP-1982-IT | open-nonblocking | Hundredths gaps; F1.com adopted |
| UNC-R15-PO-DNF | R15-PO-CLS-01 | AS-ROEBUCK-IT1982-R, F1COM-1982-IT-RES, MS-1982-10-IT | open | DNF cause granularity / NC labelling |
| UNC-R15-PO-PIR-PTS | R15-PO-PTS-01 | ARCHIVE-R14-STAND, WP-1982-IT | open | After IT: archive Ferrari 73 vs Wiki 74; Pironi 38 vs 39 |
| UNC-R15-PO-FL | R15-PO-FL | WP-1982-IT, AS-ROEBUCK-IT1982-R | open-nonblocking | FL time from secondary; narrative pace in AS/MS |
