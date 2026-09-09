# Austrian Grand Prix — source ledger

To kanoniczny rejestr źródeł folderu rundy. Dokumenty treści cytują
`source_id` i `claim_id`; nie prowadzą konkurencyjnych list źródeł. Cutoff
rejestru przy post-race obejmuje `pre-weekend.md`, `pre-race.md`,
`post-race.md` i `standings-after.md` (granica: koniec natychmiastowej
procedury po wyścigu Österreichring, niedziela 15 VIII 1982 CEST).

## Source entry

```yaml
source_id: "ARCHIVE-R12-STAND"
title: "Klasyfikacja po Grand Prix Niemiec"
author_or_organisation: "F1 Time Capsule archive (standings-after.md R12)"
publication_date: "not-applicable"
event_date: "1982-08-08"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/12-german-grand-prix/standings-after.md"
access_date: "2026-09-09"
supports:
  - claim_id: "R13-PW-STD-01"
    scope: "Prowizoryczna kolejność i punkty po Hockenheim: Pironi 38; Watson 30; Rosberg 27; Prost 25; Lauda 24; Arnoux/Patrese 19; Piquet 17; Tambay 16; Alboreto 14; de Angelis 13; Ferrari 60; McLaren 54; Renault 44; Williams 40; otwarte apelacje LB; skala prowizoryczna; konflikt Pironi 38 vs 39 / Ferrari 60 vs 61."
disagreement_notes: "Konflikt Pironi/Ferrari z liniami Wiki (UNC-R13-PW-PIR-PTS)."
notes: "Baza przed Österreichring; nie kopiować pełnych tabel do narracji PW/PR."
```

```yaml
source_id: "ARCHIVE-R12-POST"
title: "Grand Prix Niemiec — po wyścigu"
author_or_organisation: "F1 Time Capsule archive (post-race.md R12)"
publication_date: "not-applicable"
event_date: "1982-08-08"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/12-german-grand-prix/post-race.md"
access_date: "2026-09-09"
supports:
  - claim_id: "R13-PW-DEV-DE"
    scope: "Tambay 1, Arnoux 2, Rosberg 3; Pironi sobota Heidelberg; Lauda wycofany z myślą o Austrii; Piquet–Salazar; Ferrari prowadzi konstruktorów; Patrząc stąd dalej → Österreichring 15 VIII."
disagreement_notes: null
notes: "Carry-forward faktów z Hockenheim; nie importować foreshadowingu Austrian GP weekend."
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
  - claim_id: "R13-PW-EVT-01"
    scope: "Austrian GP Österreichring 15 August 1982 na ogłoszonej liście FIA; Swiss GP Dijon 29 August jako następna ogłoszona runda."
disagreement_notes: null
notes: "publication_date dnia unknown; content-based availability. Już w season/calendar.md."
```

```yaml
source_id: "MS-1982-09-AT-REF"
title: "Reflections on the Austro-German activities"
author_or_organisation: "Motor Sport (Denis Jenkinson)"
publication_date: "1982-09"
event_date: "1982-08-06/1982-08-15"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/september-1982/47/reflections-on-the-austro-german-activities/"
access_date: "2026-09-09"
supports:
  - claim_id: "R13-PW-CAL-DENSE"
    scope: "Cztery wyścigi w pięciu tygodniach; piątek–sobota testy/kwalifikacje przed niedzielą."
  - claim_id: "R13-PW-PIR-STATUS"
    scope: "Pironi po Hockenheim: wygląda na to, że wyzdrowieje; nie będzie jeździł w tym roku; przyszły rok nieznany (używać ostrożnie w PW jako stan po DE; nie domykać kariery)."
  - claim_id: "R13-PW-CIR-JOY"
    scope: "Kierowcy chwalą Österreichring; ~150 mph; kontrast z Monaco/Zolder/Detroit."
  - claim_id: "R13-PO-PIT-DETAIL"
    scope: "Opis postoju Brabhama; Patrese 13.8 s work / 15.6 s stationary; trzy air-jacks."
  - claim_id: "R13-PO-RELIAB"
    scope: "Austria: tylko 7 aut na mecie z 26 na starcie."
  - claim_id: "R13-PR-LOTUS-REN"
    scope: "Renault dostarczy Lotusowi V6 turbo na dwa sezony; 1983 de Angelis i Mansell."
disagreement_notes: "Tekst miesza DE i AT; izolować pasaże wg cutoff dokumentu."
notes: "publication_date dnia unknown; content-based availability. PW: tylko Pironi/kalendarz/tor. PR: Lotus–Renault. PO: pit-stop + reliability. Kwarantanna retrospectives spoza cutoff."
```

```yaml
source_id: "MS-1982-09-MOM"
title: "MATTERS OF MOMENT — A Very Good Grand Prix"
author_or_organisation: "Motor Sport"
publication_date: "1982-09"
event_date: "1982-08-15"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/september-1982/35/matters-of-moment-september-1982/"
access_date: "2026-09-09"
supports:
  - claim_id: "R13-PO-CLS-01"
    scope: "Austria 15 VIII jako jeden z najciekawszych wyścigów; bliski finisz; Cosworth Lotus vs turbo; postój Brabhama ~14 s według pierwszych doniesień; Brabhamy nie ukończyły."
disagreement_notes: "«Brabham-BRM» OCR/slip — czytać jako Brabham–BMW."
notes: "Wspomina «D.S.J.’s report … included in this issue» — osobny pełny raport AT nie znaleziony w TOC jako osobny URL; Reflections + MOM + AS Gold jako główne współczesne."
```

```yaml
source_id: "MS-1982-09-DE-R"
title: "1982 German Grand Prix — A popular win"
author_or_organisation: "Motor Sport (Denis Jenkinson)"
publication_date: "1982-09"
event_date: "1982-08-06/1982-08-08"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/september-1982/41/german-grand-prix-16/"
access_date: "2026-09-09"
supports:
  - claim_id: "R13-PW-LAUDA-RETURN"
    scope: "Lauda wycofany z Hockenheim, by być fit na własne GP tydzień później."
  - claim_id: "R13-PW-ENT-CARRY"
    scope: "Byrne za Lammersa; Keegan po Massie — carry do Austrii."
disagreement_notes: null
notes: "Używać tylko carry-forward obsady/Laudy; nie importować wyniku DE ponownie poza ARCHIVE-R12-POST."
```

```yaml
source_id: "AS-ROEBUCK-AT1982"
title: "Grand Prix Gold: 1982 Austrian GP (entry / practice / pre-race)"
author_or_organisation: "Autosport / Nigel Roebuck (reprint)"
publication_date: "unknown"
event_date: "1982-08-13/1982-08-15"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.autosport.com/f1/news/grand-prix-gold-1982-austrian-gp-5098977/5098977/ — Entry and practice + warm-up / pre-green only"
access_date: "2026-09-09"
supports:
  - claim_id: "R13-PW-ENT-FER"
    scope: "Sole Ferrari Tambay (Entry framing; hard stop przed practice times dla PW)."
  - claim_id: "R13-PR-FRI"
    scope: "Piquet 1:27.612 / 151.725 mph; Patrese 2.; Tambay; Arnoux bez czasu; Daly koło; Alboreto; burza wieczorem."
  - claim_id: "R13-PR-SAT"
    scope: "Brabham front row secured; Prost 1:28.864; Tambay engine; Arnoux mechanical injection 5.; Rosberg 1:30.300; Alboreto spare; McLaren off pace; Lotus–Renault confirmation; DNQ Boesel/Jarier/Salazar; Byrne 26."
  - claim_id: "R13-PR-WU"
    scope: "Warm-up: Brabhamy; oba auta zatrzymają się ~25 okr.; Renault oil leak / 4th gear; Tambay 4th WU; Surer Hella-Licht → spare / pit-lane start attributed; hot/dry; huge crowd."
disagreement_notes: "Surer pit-lane vs statutory lap — UNC-R13-PR-SURER."
notes: "Reprint; publication_date oryginału unknown; content-based availability. STRICT hard stop przed start-line chaos / race narrative. Intro hindsight («last time Chapman watched…») — kwarantanna."
```

```yaml
source_id: "AS-ROEBUCK-AT1982-R"
title: "Grand Prix Gold: 1982 Austrian GP (race section)"
author_or_organisation: "Autosport / Nigel Roebuck (reprint)"
publication_date: "unknown"
event_date: "1982-08-15"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.autosport.com/f1/news/grand-prix-gold-1982-austrian-gp-5098977/5098977/ — The Grand Prix"
access_date: "2026-09-09"
supports:
  - claim_id: "R13-PO-CLS-01"
    scope: "Przebieg: start crash; Tambay puncture; Patrese lead + pit; Piquet early stop; Patrese/Piquet DNF; Prost lead then injection; de Angelis beats Rosberg; Laffite 3; Tambay 4; Lauda 5; Baldi 6; Serra 7."
  - claim_id: "R13-PO-PTS-01"
    scope: "Punkty 9–6–4–3–2–1 za 1–6; Rosberg second in championship narrative (verify vs archive arithmetic)."
  - claim_id: "R13-PO-QUOTES"
    scope: "Cytaty de Angelis, Prost/Sage, Tambay; Chapman weigh-in incident same-day."
disagreement_notes: "AS «by a tenth» vs F1.com +0.050 — UNC-R13-PO-GAP."
notes: "Isolować narrację wyścigu; kwarantanna lead «nobody knew… last time Chapman», DFV 150th/last, Dijon rhetorical question beyond calendar date, «defenceless Pironi» career framing."
```

```yaml
source_id: "F1COM-1982-AT-RES"
title: "Formula1.com — 1982 Austrian Grand Prix race result"
author_or_organisation: "Formula One Management / formula1.com"
publication_date: "unknown"
event_date: "1982-08-15"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.formula1.com/en/results/1982/races/449/austria/race-result"
access_date: "2026-09-09"
supports:
  - claim_id: "R13-PO-CLS-01"
    scope: "Klasyfikacja: de Angelis 1:25:02.212; Rosberg +0.050; Laffite +1; Tambay +1; Lauda +1; Baldi +1; Serra +2; Prost DNF 48; pozostałe DNF/NC."
  - claim_id: "R13-PO-PTS-01"
    scope: "Punkty 9–6–4–3–2–1."
  - claim_id: "R13-PO-FL-01"
    scope: "Fastest lap page cross-check: Piquet 1:33.699 lap 5 (via F1.com fastest laps)."
disagreement_notes: "Etykiety silników / przyczyny DNF często generyczne."
notes: "Wtórne; używać do tabeli i punktów; preferować AS/MS dla przyczyn i narracji."
```

```yaml
source_id: "F1COM-1982-AT-GRID"
title: "Formula1.com — 1982 Austrian Grand Prix starting grid"
author_or_organisation: "Formula One Management / formula1.com"
publication_date: "unknown"
event_date: "1982-08-15"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.formula1.com/en/results/1982/races/449/austria/starting-grid"
access_date: "2026-09-09"
supports:
  - claim_id: "R13-PR-GRID"
    scope: "26-car grid times Piquet 1:27.612 through Byrne 1:34.985."
disagreement_notes: "Błędna etykieta «Brabham Ford» — UNC-R13-PR-BRA-ENG; silnik BMW z AS/MS/race result."
notes: "Cross-check z RSC qualifying."
```

```yaml
source_id: "RSC-1982-AT-Q"
title: "RacingSportsCars — 1982 Österreichring F1 qualifying"
author_or_organisation: "RacingSportsCars"
publication_date: "unknown"
event_date: "1982-08-15"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.racingsportscars.com/f1/results/qualifying/Zeltweg-1982-08-15-14269.html"
access_date: "2026-09-09"
supports:
  - claim_id: "R13-PR-GRID"
    scope: "Czasy kwalifikacji; Ferrari sole Tambay; DNQ poza top 26."
disagreement_notes: null
notes: "Wtórne; kwarantanna wyniku wyścigu na powiązanych stronach."
```

```yaml
source_id: "RSC-1982-AT-RES"
title: "RacingSportsCars / secondary DNF cause cross-check"
author_or_organisation: "RacingSportsCars / GrandPrix.com-style secondary"
publication_date: "unknown"
event_date: "1982-08-15"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "secondary DNF cause lists cross-checked against AS-ROEBUCK-AT1982-R"
access_date: "2026-09-09"
supports:
  - claim_id: "R13-PO-DNF"
    scope: "Szczegółowe przyczyny DNF gdzie AS/F1.com są generyczne (np. camshaft drive Piquet)."
disagreement_notes: "UNC-R13-PO-DNF — różna granularność."
notes: "Nie używać do foreshadowingu."
```

```yaml
source_id: "WP-1982-AT"
title: "Wikipedia — 1982 Austrian Grand Prix"
author_or_organisation: "Wikipedia contributors"
publication_date: "unknown"
event_date: "1982-08-15"
source_type: "SECONDARY"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://en.wikipedia.org/wiki/1982_Austrian_Grand_Prix"
access_date: "2026-09-09"
supports:
  - claim_id: "R13-PW-EVT-01"
    scope: "Data 15 August 1982; Österreichring; oficjalna nazwa XX Holiday Großer Preis von Österreich; length 5.942 km; 53 laps — tylko cross-check."
disagreement_notes: "UNC-R13-PW-LEN — drobne różnice metrów vs inne bazy."
notes: "STRICT quarantine: wyniki, standings Wiki (Pironi 39), Chapman death, retrospectives. Tylko data/venue/length izolowane."
```

```yaml
source_id: "MS-DB-1982-AT"
title: "Motor Sport Database — 1982 Austrian Grand Prix"
author_or_organisation: "Motor Sport Magazine"
publication_date: "unknown"
event_date: "1982-08-15"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/database/races/1982-austrian-grand-prix/"
access_date: "2026-09-09"
supports:
  - claim_id: "R13-PW-EVT-01"
    scope: "Sunday 15 August 1982; Grosser Preis von Osterreich; circuit length 3.692 miles (~5.94 km)."
disagreement_notes: null
notes: "Cross-check daty/długości; kwarantanna later lap records (1987)."
```

```yaml
source_id: "MS-1981-09-AT-RES"
title: "1981 Austrian Grand Prix RESULTS box (distance precedent)"
author_or_organisation: "Motor Sport"
publication_date: "1981-09"
event_date: "1981-08"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/september-1981/38/austrian-grand-prix-8/ — RESULTS: 53 laps — 5.9424 km"
access_date: "2026-09-09"
supports:
  - claim_id: "R13-PW-LEN-01"
    scope: "Współczesny wzorzec dystansu Österreichring 53×~5.94 km (precedens 1981; 1982 potwierdzony wtórnie)."
disagreement_notes: "UNC-R13-PW-LEN"
notes: "Nie importować wyniku 1981 do narracji 1982."
```

## Conflict and uncertainty index

| Uncertainty ID | Claim IDs | Source IDs | Status at cutoff | Note |
| --- | --- | --- | --- | --- |
| UNC-R13-PW-PIR-PTS | R13-PW-STD-01 | ARCHIVE-R12-STAND, WP-1982-AT | unresolved | Pironi 38 vs Wiki 39; Ferrari 60 vs 61 before AT / 63 vs 64 after |
| UNC-R13-PW-LEN | R13-PW-LEN-01 | MS-1981-09-AT-RES, WP-1982-AT, MS-DB-1982-AT | logged-trivia | ~5.94 km adopted; metre-level variance ledger-only |
| UNC-R13-PR-BRA-ENG | R13-PR-GRID | F1COM-1982-AT-GRID | resolved-in-prose | F1.com mislabels Brabham Ford; prose uses BMW |
| UNC-R13-PR-SURER | R13-PR-WU | AS-ROEBUCK-AT1982 | unresolved | Pit-lane start attributed; no separate steward bulletin |
| UNC-R13-PO-GAP | R13-PO-CLS-01 | F1COM-1982-AT-RES, AS-ROEBUCK-AT1982-R | prefer-0.050 | AS once says «tenth»; official/databases 0.050 |
| UNC-R13-PO-DNF | R13-PO-DNF | AS-ROEBUCK-AT1982-R, F1COM-1982-AT-RES, RSC-1982-AT-RES | unresolved | Cause granularity varies |
| UNC-R13-PO-PIR-PTS | R13-PO-PTS-01 | ARCHIVE-R12-STAND, WP-1982-AT | unresolved | Continuity of 38 vs 39 base |
