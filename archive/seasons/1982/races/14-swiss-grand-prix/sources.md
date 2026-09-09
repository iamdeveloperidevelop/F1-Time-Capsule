# Swiss Grand Prix — source ledger

To kanoniczny rejestr źródeł folderu rundy. Dokumenty treści cytują
`source_id` i `claim_id`; nie prowadzą konkurencyjnych list źródeł. Cutoff
rejestru przy post-race obejmuje `pre-weekend.md`, `pre-race.md`,
`post-race.md` i `standings-after.md` (granica: koniec natychmiastowej
procedury po wyścigu Dijon-Prenois, niedziela 29 VIII 1982 CEST).

## Source entry

```yaml
source_id: "ARCHIVE-R13-STAND"
title: "Klasyfikacja po Grand Prix Austrii"
author_or_organisation: "F1 Time Capsule archive (standings-after.md R13)"
publication_date: "not-applicable"
event_date: "1982-08-15"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/13-austrian-grand-prix/standings-after.md"
access_date: "2026-09-09"
supports:
  - claim_id: "R14-PW-STD-01"
    scope: "Prowizoryczna kolejność i punkty po Österreichring: Pironi 38; Rosberg 33; Watson 30; Lauda 26; Prost 25; de Angelis 22; Arnoux/Patrese/Tambay 19; Piquet 17; Ferrari 63; McLaren 56; Williams 46; Renault 44; otwarte apelacje LB; skala prowizoryczna; konflikt Pironi 38 vs 39 / Ferrari 63 vs 64."
disagreement_notes: "Konflikt Pironi/Ferrari z liniami Wiki (UNC-R14-PW-PIR-PTS)."
notes: "Baza przed Dijon; nie kopiować pełnych tabel do narracji PW/PR."
```

```yaml
source_id: "ARCHIVE-R13-POST"
title: "Grand Prix Austrii — po wyścigu"
author_or_organisation: "F1 Time Capsule archive (post-race.md R13)"
publication_date: "not-applicable"
event_date: "1982-08-15"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/13-austrian-grand-prix/post-race.md"
access_date: "2026-09-09"
supports:
  - claim_id: "R14-PW-DEV-AT"
    scope: "de Angelis 1, Rosberg 2 (+0.050), Laffite 3; Tambay 4; Lauda 5; Baldi 6; Rosberg 2. w mistrzostwach; Ferrari sole Tambay; Brabham pit stop; Patrząc stąd dalej → Swiss GP Dijon 29 VIII."
disagreement_notes: null
notes: "Carry-forward faktów z Austrii; nie importować foreshadowingu Swiss GP weekend."
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
  - claim_id: "R14-PW-EVT-01"
    scope: "Swiss GP Dijon-Prenois 29 August 1982 na ogłoszonej liście FIA; Italian GP Monza 12 September jako następna ogłoszona runda."
disagreement_notes: null
notes: "publication_date dnia unknown; content-based availability. Już w season/calendar.md."
```

```yaml
source_id: "MS-1982-10-CH"
title: "The Swiss Grand Prix — Another first"
author_or_organisation: "Motor Sport (J.H. / Jenkinson)"
publication_date: "1982-10"
event_date: "1982-08-27/1982-08-29"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/october-1982/42/the-swiss-grand-prix-2/"
access_date: "2026-09-09"
supports:
  - claim_id: "R14-PW-ORG-01"
    scope: "Swiss GP we Francji; ACS zakaz w CH; umowa z Dijon; «drugie GP Francji»; format Friday–Saturday testing/qualifying."
  - claim_id: "R14-PR-Q"
    scope: "Renault dominate; Arnoux crash Friday/Saturday testing → T-car; Arnoux→Ferrari 1983 hush; Lauda skips Saturday; Tambay back/nerve, misses Saturday, withdraws Sunday; BMW reliable / chassis imbalance; Surer A5; Mansell–Henton row."
  - claim_id: "R14-PO-RACE"
    scope: "Prost lead; Rosberg late charge; skirt/tyres Prost; Arnoux injection; pass lap 79; flag lap 81 after near-stop lap 78; Rosberg first GP win; only three cars full distance; Piquet pit / Patrese non-stop."
disagreement_notes: "Tekst miesza preview i wynik; izolować pasaże wg cutoff dokumentu."
notes: "publication_date dnia unknown; content-based availability. PW: tylko org/format/Ferrari decimated framing ostrożnie. PR: Qualifying. PO: Race. Kwarantanna retrospectives spoza cutoff."
```

```yaml
source_id: "AS-ROEBUCK-CH1982"
title: "Grand Prix Gold: 1982 Swiss GP (Autosport / Nigel Roebuck reprint — Entry & Practice)"
author_or_organisation: "Autosport (Nigel Roebuck); reprint autosport.com 2012"
publication_date: "1982-09"
event_date: "1982-08-27/1982-08-29"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.autosport.com/f1/news/grand-prix-gold-1982-swiss-gp-5098972/5098972/ — sections Entry and Practice / warm-up before The race"
access_date: "2026-09-09"
supports:
  - claim_id: "R14-PW-ENT"
    scope: "Tambay pinched nerve since Wednesday after Austria; sole Ferrari; Surer A5 tested Donington; Alboreto new 011; Ligier new sidepods; circuit character Dijon."
  - claim_id: "R14-PR-SES"
    scope: "Rain Thu night; Prost 1:01.380 / Arnoux 1:01.740 Friday; Arnoux Pouas puncture crash Saturday morning; Renault withdraw from Saturday qualifiers; Patrese 1:02.710; Lauda 1:02.984 skips Saturday; Tambay 1:03.896 / straps / Sunday DNS; DNQ Serra/Byrne/Baldi; Mansell–Henton Bretelle; Arnoux→Ferrari / Prost re-sign; warm-up ≈10:00 Prost 1:05.854; start ≈13:00; Guerrero engine change → pit-lane; Brabham Piquet stop / Patrese non-stop; tyre choices."
disagreement_notes: "Reprint 2012 — używać tylko passaży contemporary; hard stop przed race narrative w PR."
notes: "Oryginalny numer AS — luka 1982-R14-AS-01. PW: Entry przed practice times. PR: przez warm-up."
```

```yaml
source_id: "AS-ROEBUCK-CH1982-R"
title: "Grand Prix Gold: 1982 Swiss GP (Autosport / Nigel Roebuck reprint — Race)"
author_or_organisation: "Autosport (Nigel Roebuck); reprint autosport.com 2012"
publication_date: "1982-09"
event_date: "1982-08-29"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.autosport.com/f1/news/grand-prix-gold-1982-swiss-gp-5098972/5098972/ — section The race"
access_date: "2026-09-09"
supports:
  - claim_id: "R14-PO-CLS-01"
    scope: "Rosberg win; Prost 2; Lauda 3; narrative phases; FL Prost 1:07.477 lap 2; de Cesaris blocking; Arnoux injection; pass Bretelle lap 79; flag errors laps 78/80/81; quotes Rosberg; retirements causes."
  - claim_id: "R14-PO-PTS-01"
    scope: "Points places 1–6; Rosberg leads championship 42 (with archive Pironi base adjustment in standings doc)."
disagreement_notes: "UNC-R14-PO-GAP gap vs F1.com; UNC-R14-PO-DNF cause granularity; Wiki Pironi 39 vs archive 38."
notes: "Isolować narrację wyścigu; kwarantanna «looks like 1982 world champion» jako domknięcie tytułu — tylko atrybucja same-day."
```

```yaml
source_id: "F1COM-1982-CH-RES"
title: "Formula1.com — 1982 Swiss Grand Prix race result"
author_or_organisation: "Formula One Management / formula1.com"
publication_date: "unknown"
event_date: "1982-08-29"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.formula1.com/en/results/1982/races/450/switzerland/race-result"
access_date: "2026-09-09"
supports:
  - claim_id: "R14-PO-CLS-01"
    scope: "Classification: Rosberg 1:32:41.087; Prost +4.440; Lauda +60.340; Piquet/Patrese/de Angelis +1 lap; points 9–6–4–3–2–1; retirement list."
disagreement_notes: "UNC-R14-PO-GAP; Arnoux listed classified DNF P16; Brabham engine label OK on result page."
notes: "Wtórne; krzyżować z AS/MS."
```

```yaml
source_id: "F1COM-1982-CH-GRID"
title: "Formula1.com — 1982 Swiss Grand Prix starting grid"
author_or_organisation: "Formula One Management / formula1.com"
publication_date: "unknown"
event_date: "1982-08-29"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.formula1.com/en/results/1982/races/450/switzerland/starting-grid"
access_date: "2026-09-09"
supports:
  - claim_id: "R14-PR-GRID"
    scope: "26-car grid times Prost 1:01.380 through Mansell 1:06.211."
disagreement_notes: "Błędna etykieta «Brabham Ford» — UNC-R14-PR-BRA-ENG; silnik BMW z AS/MS/race result."
notes: "Cross-check z RSC / Wiki Q."
```

```yaml
source_id: "RSC-1982-CH-Q"
title: "RacingSportsCars — 1982 Dijon F1 qualifying / entry"
author_or_organisation: "RacingSportsCars"
publication_date: "unknown"
event_date: "1982-08-29"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "http://www.racingsportscars.com/f1/results/qualifying/Dijon-1982-08-29.html ; entry list sibling"
access_date: "2026-09-09"
supports:
  - claim_id: "R14-PR-GRID"
    scope: "Czasy kwalifikacji; event title 1er Grand Prix de Suisse; organiser ACS; Brabham BMW labels."
disagreement_notes: null
notes: "Wtórne; kwarantanna wyniku wyścigu na powiązanych stronach."
```

```yaml
source_id: "WP-1982-CH"
title: "Wikipedia — 1982 Swiss Grand Prix"
author_or_organisation: "Wikipedia contributors"
publication_date: "unknown"
event_date: "1982-08-29"
source_type: "SECONDARY"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://en.wikipedia.org/wiki/1982_Swiss_Grand_Prix"
access_date: "2026-09-09"
supports:
  - claim_id: "R14-PW-EVT-01"
    scope: "Data 29 August 1982; Dijon-Prenois; length ~3.801 km; 80 laps — tylko cross-check; Q1/Q2 table cross-check."
disagreement_notes: "UNC-R14-PW-LEN; standings Wiki Pironi 39 / Ferrari 64."
notes: "STRICT quarantine: wyniki w PW; standings Wiki; «career-ending» Pironi; «last Swiss GP» retrospectives; «only win of champion season». Tylko data/venue/length/Q izolowane."
```

## Conflict and uncertainty index

| Uncertainty ID | Claim IDs | Source IDs | Status at cutoff | Note |
| --- | --- | --- | --- | --- |
| UNC-R14-PW-PIR-PTS | R14-PW-STD-01 | ARCHIVE-R13-STAND, WP-1982-CH | open | Pironi 38 vs 39 / Ferrari 63 vs 64 — linia archiwum |
| UNC-R14-PW-LEN | R14-PW-EVT-01 | WP-1982-CH, F1COM-1982-CH-RES | open-nonblocking | ~3,80 km; nie pedantyzować metrów w prose |
| UNC-R14-PR-BRA-ENG | R14-PR-GRID | F1COM-1982-CH-GRID | resolved-in-prose | Narracja: BMW; F1.com grid „Ford” błędne |
| UNC-R14-PO-GAP | R14-PO-CLS-01 | F1COM-1982-CH-RES, AS-ROEBUCK-CH1982-R, WP-1982-CH | open-nonblocking | +4.440 vs ~4 s / +4.442 — przyjęto F1.com |
| UNC-R14-PO-DNF | R14-PO-CLS-01 | AS-ROEBUCK-CH1982-R, F1COM-1982-CH-RES | open | Różna granularność przyczyn DNF / klasyfikacja Arnouxa |
| UNC-R14-PO-PIR-PTS | R14-PO-PTS-01 | ARCHIVE-R13-STAND, WP-1982-CH | open | Kontynuacja konfliktu po punktach CH |
