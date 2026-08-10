# German Grand Prix — source ledger

To kanoniczny rejestr źródeł folderu rundy. Dokumenty treści cytują
`source_id` i `claim_id`; nie prowadzą konkurencyjnych list źródeł. Cutoff
rejestru przy pre-weekend obejmuje wyłącznie `pre-weekend.md` (granica:
natychmiast przed pierwszą oficjalną sesją Hockenheim, piątek 6 VIII 1982
CEST).

## Source entry

```yaml
source_id: "ARCHIVE-R11-STAND"
title: "Klasyfikacja po Grand Prix Francji"
author_or_organisation: "F1 Time Capsule archive (standings-after.md R11)"
publication_date: "not-applicable"
event_date: "1982-07-25"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/11-french-grand-prix/standings-after.md"
access_date: "2026-08-10"
supports:
  - claim_id: "R12-PW-STD-01"
    scope: "Prowizoryczna kolejność i punkty po Paul Ricard: Pironi 38; Watson 30; Prost 25; Lauda 24; Rosberg 23; Patrese 19; Piquet 17; Arnoux/de Angelis 13; Alboreto 11; McLaren 54; Ferrari 51; Renault 38; Williams/Brabham 36; otwarte apelacje LB; skala prowizoryczna; konflikt Pironi 38 vs 39 / Ferrari 51 vs 52."
disagreement_notes: "Konflikt Pironi/Ferrari z liniami Wiki (UNC-R12-PW-PIR-PTS)."
notes: "Baza przed Hockenheim; nie kopiować pełnych tabel do narracji."
```

```yaml
source_id: "ARCHIVE-R11-POST"
title: "Grand Prix Francji — po wyścigu"
author_or_organisation: "F1 Time Capsule archive (post-race.md R11)"
publication_date: "not-applicable"
event_date: "1982-07-25"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/11-french-grand-prix/post-race.md"
access_date: "2026-08-10"
supports:
  - claim_id: "R12-PW-DEV-FR"
    scope: "Arnoux 1, Prost 2, Pironi 3, Tambay 4, Rosberg 5, Alboreto 6; team orders Arnoux/Prost; Mass–Baldi Signes (lekkie oparzenie barku Massa); Brabham postój anulowany; protest fartuchów bez potwierdzonego wyniku tego dnia; Patrząc stąd dalej → Hockenheim 8 VIII."
disagreement_notes: null
notes: "Carry-forward faktów z Paul Ricard; nie importować foreshadowingu German GP weekend."
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
access_date: "2026-08-10"
supports:
  - claim_id: "R12-PW-EVT-01"
    scope: "German GP Hockenheim 8 August 1982 na ogłoszonej liście FIA."
disagreement_notes: null
notes: "publication_date dnia unknown; content-based availability. Już w season/calendar.md."
```

```yaml
source_id: "MS-1982-09-DE-R"
title: "1982 German Grand Prix — A popular win (arrival / paddock prelude)"
author_or_organisation: "Motor Sport (Denis Jenkinson)"
publication_date: "1982-09"
event_date: "1982-08-06/1982-08-08"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/september-1982/41/german-grand-prix-16/"
access_date: "2026-08-10"
supports:
  - claim_id: "R12-PW-CIR-01"
    scope: "Opis Hockenheim (stadion betonowy, proste, dawna Ostkurve); nowa szykana przed Ostkurve; mglista atrybucja Scheckter."
  - claim_id: "R12-PW-ARR-01"
    scope: "Klimat przyjazdu: deszcz / sceptycyzm co do suchego weekendu; peleton w porządku po Brands+Francja; Mansell wraca do Lotusa; Byrne za Lammersa w Theodore; Keegan w Marchu czekający na Massa (Mass nadal cierpi po Ricard)."
  - claim_id: "R12-PW-ENT-CAR"
    scope: "Inventarz przyjazdu: Williams FW08/6 Daly; Renault RE30B/10 Prost; Ferrari experimental longitudinal T-car; Lotus pull-rod/rocker T-cars; Brabham lightweight carbon-brake T-car."
  - claim_id: "R12-PW-CUT-DAY"
    scope: "Pierwsza aktywność practice w piątek rano (dzień; nie używać suchego piątku jako przeżytej pogody sesji w race-prelude)."
  - claim_id: "R12-PW-LEN-01"
    scope: "RESULTS box: 6.797 km × 45 laps = 305.865 km (scheduled figures; conflict with Wiki 6.802)."
disagreement_notes: "Keegan→March (MS) vs grandprix.com Arrows (UNC-R12-PW-KEEGAN). Mass fitness: arrival uncertainty vs later session withdrawal (UNC-R12-PW-MASS-FIT)."
notes: "publication_date dnia unknown; content-based availability. STRICT hard stop: po akapicie inventarza paddocku; PRZED «Prost started the morning session…». Kwarantanna: cała praktyka/kwalifikacje, wypadek Pironiego, grid, wyścig, RESULTS poza izolowaną długością."
```

```yaml
source_id: "MS-DB-1982-DE"
title: "1982 German Grand Prix — Motor Sport Database"
author_or_organisation: "Motor Sport Magazine database"
publication_date: "unknown"
event_date: "1982-08-08"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/database/races/1982-german-grand-prix/"
access_date: "2026-08-10"
supports:
  - claim_id: "R12-PW-EVT-02"
    scope: "Data niedziela 8 sierpnia 1982; Hockenheimring; nazwa Grosser Preis von Deutschland."
disagreement_notes: null
notes: "Używać tylko daty/miejsca; kwarantanna wyników i sesji. Embeduje raport MS."
```

```yaml
source_id: "WP-1982-DE"
title: "1982 German Grand Prix"
author_or_organisation: "Wikipedia"
publication_date: "unknown"
event_date: "1982-08-08"
source_type: "SECONDARY"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://en.wikipedia.org/wiki/1982_German_Grand_Prix"
access_date: "2026-08-10"
supports:
  - claim_id: "R12-PW-EVT-03"
    scope: "Data 8 August 1982; round 12; Hockenheimring; oficjalna nazwa XLIV Großer Preis von Deutschland; layout note (zacieśniona pierwsza szykana + nowa przed Ostkurve); długość 6.802 km / 45 laps jako linia wtórna."
  - claim_id: "R12-PW-CIR-FIRST"
    scope: "Pierwsza szykana zacieśniona względem poprzedniego roku (layout note)."
disagreement_notes: "Długość 6.802 vs MS 6.797 (UNC-R12-PW-LEN)."
notes: "STRICT quarantine: pole, qualifying, Pironi accident, race, standings after Germany."
```

```yaml
source_id: "PROSTFAN-1982-DE-ENT"
title: "prostfan.com — 1982 German GP race details / entry list"
author_or_organisation: "prostfan.com"
publication_date: "unknown"
event_date: "1982-08-08"
source_type: "SECONDARY"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.prostfan.com/racedet/82ger.htm"
access_date: "2026-08-10"
supports:
  - claim_id: "R12-PW-ENT-LIST"
    scope: "Kompilacja entry (numery/pary): Mansell Lotus 12; Byrne Theodore; standardowe pary poza stanem Massa na przyjeździe; dystans 6797 m × 45."
disagreement_notes: "Publikowana lista może pokazywać Keegana zamiast Massa — stan przyjazdu Mass/Keegan-wait: preferować MS-1982-09-DE-R."
notes: "Wtórne; nie zastępuje oficjalnego telexu (1982-R12-PW-ENT-01). Kwarantanna wyników/kwalifikacji. Nie używać do ostatecznego statusu Massa."
```

```yaml
source_id: "GPCOM-1982-DE"
title: "grandprix.com — German GP 1982"
author_or_organisation: "grandprix.com"
publication_date: "unknown"
event_date: "1982-08-08"
source_type: "SECONDARY"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.grandprix.com/races/german-gp-1982.html"
access_date: "2026-08-10"
supports:
  - claim_id: "R12-PW-GAP-01"
    scope: "Potwierdzenie dwutygodniowej przerwy Ricard→Hockenheim; Mansell wraca; Byrne za Lammersa (cross-check)."
disagreement_notes: "Błędnie umieszcza Keegana w Arrows zamiast March (UNC-R12-PW-KEEGAN) — nie używać tej linii."
notes: "Używać tylko po cross-checku z MS; kwarantanna wyników i sesji."
```

## Conflict and uncertainty index

| Uncertainty ID | Claim IDs | Source IDs | Status at cutoff | Note |
| --- | --- | --- | --- | --- |
| UNC-R12-PW-PIR-PTS | R12-PW-STD-01 | ARCHIVE-R11-STAND, WP-1982-DE | open | Pironi 38 (archiwum) vs 39 (Wiki); Ferrari 51 vs 52 |
| UNC-R12-PW-LEN | R12-PW-LEN-01, R12-PW-EVT-03 | MS-1982-09-DE-R, WP-1982-DE, PROSTFAN-1982-DE-ENT | open | 6.797 vs 6.802 km |
| UNC-R12-PW-KEEGAN | R12-PW-ARR-01 | MS-1982-09-DE-R, GPCOM-1982-DE | resolved-for-draft | Prefer MS March; quarantine GP.com Arrows |
| UNC-R12-PW-MASS-FIT | R12-PW-ARR-01 | MS-1982-09-DE-R | open-at-arrival | Mass still suffering / Keegan waiting; do not settle session withdrawal in race-prelude |
| UNC-R12-PW-CUT-CLOCK | R12-PW-CUT-DAY | MS-1982-09-DE-R | open | Friday morning known; exact clock unverified |
| UNC-R12-PW-WX-FORECAST | R12-PW-ARR-01 | MS-1982-09-DE-R | open | Arrival gloom only; no dated meteo forecast |
