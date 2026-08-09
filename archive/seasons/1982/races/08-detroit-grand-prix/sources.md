# Detroit Grand Prix — source ledger

To kanoniczny rejestr źródeł folderu rundy. Dokumenty treści cytują
`source_id` i `claim_id`; nie prowadzą konkurencyjnych list źródeł. Cutoff
rejestru obejmuje `pre-weekend.md`, `pre-race.md`, `post-race.md` oraz
`standings-after.md` (granica: koniec natychmiastowej procedury oficjalnej
po Grand Prix Detroit 6 VI 1982).

## Source entry

```yaml
source_id: "ARCHIVE-R07-STAND"
title: "Klasyfikacja po Grand Prix Monako"
author_or_organisation: "F1 Time Capsule archive (standings-after.md R07)"
publication_date: "not-applicable"
event_date: "1982-05-23"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/07-monaco-grand-prix/standings-after.md"
access_date: "2026-08-09"
supports:
  - claim_id: "R08-PW-STD-01"
    scope: "Prowizoryczna kolejność i punkty po Monako: Prost 18, Watson 17, Pironi 15 (UPI 16 odnotowane), Rosberg 14, Patrese 13, Lauda 12, Alboreto 10, Mansell/de Angelis 7, Reutemann/Villeneuve 6; McLaren 29, Renault 22, Williams/Ferrari 21, Brabham 15, Lotus 14, Tyrrell 10, Talbot-Ligier/Alfa 4, Osella 3, ATS 2, Fittipaldi 1; otwarte apelacje LB; skala prowizoryczna."
  - claim_id: "R08-PO-STD-BASE"
    scope: "Baza arytmetyki standings-after.md po Detroit (Pironi 15; McLaren 29; Williams/Ferrari 21)."
disagreement_notes: "Konflikt Pironi 15 vs UPI 16 (UNC-R07-PO-PIR-PTS); brak oficjalnego biuletynu FIA."
notes: "Baza przed Detroit; nie kopiować pełnych tabel do narracji."
```

```yaml
source_id: "ARCHIVE-R07-PW"
title: "Grand Prix Monako — przed weekendem (obsada przyjazdu Monte Carlo)"
author_or_organisation: "F1 Time Capsule archive (pre-weekend.md R07)"
publication_date: "not-applicable"
event_date: "1982-05-20/1982-05-23"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/07-monaco-grand-prix/pre-weekend.md"
access_date: "2026-08-09"
supports:
  - claim_id: "R08-PW-ENT-01"
    scope: "Kontynuacja obsady vs Monako jako baza: pary głównych zespołów; Pironi-only Ferrari w Monako; Lammers Theodore; de Villota March."
disagreement_notes: null
notes: "Carry-forward personalny; weryfikować względem RSC Detroit entry."
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
access_date: "2026-08-09"
supports:
  - claim_id: "R08-PW-CAL-01"
    scope: "Detroit Grand Prix — Detroit — 6 June 1982 na liście; Canadian GP 12/13 June disputed w season calendar."
disagreement_notes: "1982-CAL-02 spór daty Kanady."
notes: "publication_date dnia unknown; content-based availability. Już w season/calendar.md. Looking-ahead post-race: tylko fakt kolejnego terminu w kalendarzu — bez researchu Montreal."
```

```yaml
source_id: "UPI-1982-05-23-DET"
title: "Auto racing: Detroit's Grand Prix Copies Monte Carlo"
author_or_organisation: "UPI"
publication_date: "1982-05-23"
event_date: "1982-06-06"
source_type: "PRESS"
contemporary: true
spoiler_risk: "none"
locator: "https://www.upi.com/Archives/1982/05/23/Auto-racing-Detroits-Grand-Prix-Copies-Monte-Carlo/1377390974400/"
access_date: "2026-08-09"
supports:
  - claim_id: "R08-PW-ORG-01"
    scope: "Pierwsze GP w Detroit 6 VI; Detroit Renaissance Grand Prix / McCabe; Renaissance Center w centrum ~2-mile course; ~20 turns; ~175 miles; 26 cars; Belle Isle odrzucone; resurfacing ~$800k; bilety $15–$65; economic impact >$4m; Stewart Economic Club quote; ABC / ~1000 journalists."
disagreement_notes: "Długość/dystans w języku zapowiedzi — konflikt z późniejszymi pomiarami (UNC-R08-PW-LEN)."
notes: "Współczesna zapowiedź z dnia Monako; nie używać do wyników Detroit."
```

```yaml
source_id: "MS-JUL1982-DET"
title: "The Grand Prix of Detroit"
author_or_organisation: "Denis Jenkinson / Motor Sport"
publication_date: "1982-07"
event_date: "1982-06-03/1982-06-06"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/july-1982/43/the-grand-prix-of-detroit/"
access_date: "2026-08-09"
supports:
  - claim_id: "R08-PW-CUT-01"
    scope: "Planowany czwartkowy nieoficjalny test; odwołanie po inspekcji FISA (escape roads/barriers); planowany piątkowy trening 10:00–11:30 i kwalifikacje 13:00–14:00 jako oryginalny rozkład."
  - claim_id: "R08-PW-CIR-01"
    scope: "Opis układu: rzeka, Renaissance Center, kąty proste, tunel, anty-clockwise, wyboje/studzienki, prowizoryczne boksy; Detroit Renaissance Grand Prix Inc.; akt zamykający ulice."
  - claim_id: "R08-PW-TOL-01"
    scope: "Toleman wycofany — transporter spóźniony z Monako; Warwick i Fabi nie przyjechali."
  - claim_id: "R08-PW-FER-01"
    scope: "Ferrari samotny wpis Pironi; dwa 126C2 w dyspozycji (w tym egzemplarz z nowym przednim zawieszeniem pull-rod)."
  - claim_id: "R08-PW-TEC-01"
    scope: "Brabham: dwa BMW Piquet / dwa Cosworth Patrese + karbon hamulce Patrese; Ligier JS17 + JS19 T-car; Ensign Michelin między Monako a Detroit; Theodore drugi TY02 Goodyear; Williams trójka FW08; McLaren przestawienie podwozi; elastyczność ustawień przy braku wiedzy o torze."
  - claim_id: "R08-PR-FRI-01"
    scope: "Piątek: scrub 10:00–11:30 i 13:00–14:00; tylko 16:00–17:00; spins/walls; Jarier rocker + quotes; Arnoux wall / Prost electrics→spare; Lammers thumb / hospital; end 17:25; Lauda get-stuck-in paraphrase."
  - claim_id: "R08-PR-SAT-01"
    scope: "Sobota: dwie godziny Q z 4 h przerwą; ~1 h delay; grey/gloomy; Q1 Prost pace / Piquet bottom / Watson–Serra stop / Rosberg 3rd carbon + oil/water ballast / Winkelhock 5th; rain in break; wet Q2 few runners Lauda ~18 s slower; de Cesaris tunnel crash; DNQ narrative Piquet + de Villota; grid 26."
  - claim_id: "R08-PR-WU-01"
    scope: "Niedziela: clear warm morning; WU 11:20–11:50; Prost ELF camera; Pironi modified Ferrari; no carbon brakes Williams/Brabham pits; Piquet media / BMW low profile; Jarier fuel-line fire + powder; Paletti lost wheel last ess; Jarier takes spare; Paletti repairs unfinished."
  - claim_id: "R08-PR-ASSY-01"
    scope: "Pre-lights assembly: 25 leave pits (Paletti out); Jarier wall (claimed puncture); Winkelhock steering arm break/repair; Paletti too late DNS; Jarier #31 on Paletti car at pit exit; breeze + grey clouds before start."
  - claim_id: "R08-PR-CUT-01"
    scope: "Warm-up 11:20–11:50 local; R5 before F1 start prep; exact F1 green-light clock not stated."
  - claim_id: "R08-PO-NAR-01"
    scope: "Race narrative: Prost lead; Baldi/Boesel/Alboreto/Salazar early; de Cesaris driveshaft; Jarier engine; Winkelhock steering crash; Guerrero–de Angelis–Patrese; red flag; >1 h delay with repairs; 18-car restart aggregate; Prost fuel-injection fade; Rosberg lead; Watson rhythm overtakes incl. Lauda/Cheever/Pironi one lap; Watson lead on road ~37 / aggregate ~44; Lauda crash vs Rosberg; Laffite–Pironi contact; Alboreto/Mansell retirements; Prost FL 1:50.438; 62 laps / 2 h; scrutineering weight OK + aerofoil warnings."
  - claim_id: "R08-PO-CLS-01"
    scope: "RESULTS table: Watson 1:58:41.043; Cheever 1:58:56.769; Pironi 1:59:09.120; Rosberg 1:59:53.019; Daly 2:00:04.800; Laffite +1; Mass/Surer +1; Henton +2; Arnoux/Serra +3; Prost listed 12th +8 laps; DNF/DNS rows; 6+56 laps; 4.011 km; FL Prost; 25 starters / 12 finishers; NB early stop note."
  - claim_id: "R08-PO-SCR-01"
    scope: "Post-race weigh-in first six + Mass; all passed weight; March and one Talbot aerofoil height/width warning only."
  - claim_id: "R08-PO-PTS-01"
    scope: "Points inference 9–6–4–3–2–1 for top six finishers (scale provisional archive-wide)."
disagreement_notes: "Artykuł zawiera pełny weekend — dla wcześniejszych dokumentów izolować; dla post-race używać Race+RESULTS. Konflikt: Prost 12th vs RSC/Wiki NC; Giacomelli DNF lap 41 vs ~30 narrative/RSC; niektóre DNF laps off-by-one vs Wiki/RSC. Kwarantanna foreshadowing Montreal / season retrospectives (artykuł ich nie rozwija w RESULTS)."
notes: "publication_date dnia unknown; content-based availability. Primary contemporary race narrative for R08-PO."
```

```yaml
source_id: "RSC-1982-R08-ENT"
title: "Detroit 1982 — entry / qualifying reconstruction"
author_or_organisation: "Racing Sports Cars (database reconstruction)"
publication_date: "unknown"
event_date: "1982-06-06"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.racingsportscars.com/f1/results/qualifying/Detroit-1982-06-06.html"
access_date: "2026-08-09"
supports:
  - claim_id: "R08-PW-ENT-02"
    scope: "Rekonstrukcja listy kierowców/zespołów obecnych lub zgłoszonych (bez czasów kwalifikacji i bez DNQ jako wyniku sesji)."
  - claim_id: "R08-PR-GRID-01"
    scope: "Provisional Q times P1–P26 Prost 1:48.537 … Serra 1:55.848; DNQ de Villota 1:56.589, Piquet 1:57.779; Lammers listed among other present without Q time; Toleman DNA."
disagreement_notes: "Not an official FIA bulletin; Lammers placement vs Wiki Q row 29 — compatible as injured non-qualifier."
notes: "Wtórne; oficjalna lista FOCA/FISA — luka 1982-R08-PW-ENT-01. Dla pre-race używać też jako RSC-1982-R08-Q (ta sama strona)."
```

```yaml
source_id: "RSC-1982-R08-Q"
title: "Detroit 1982 — Qualifying Results (structured times)"
author_or_organisation: "Racing Sports Cars (database reconstruction)"
publication_date: "unknown"
event_date: "1982-06-06"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.racingsportscars.com/f1/results/qualifying/Detroit-1982-06-06.html"
access_date: "2026-08-09"
supports:
  - claim_id: "R08-PR-GRID-01"
    scope: "Same structured grid as RSC-1982-R08-ENT supports block; primary locator for pre-race table."
disagreement_notes: "Alias of qualifying page already used for entry identity; kept for claim-map clarity."
notes: "Use for structured grid only."
```

```yaml
source_id: "RSC-1982-R08-RES"
title: "Detroit 1982 — Race Results (structured classification)"
author_or_organisation: "Racing Sports Cars (database reconstruction)"
publication_date: "unknown"
event_date: "1982-06-06"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.racingsportscars.com/f1/results/Detroit-1982-06-06.html"
access_date: "2026-08-09"
supports:
  - claim_id: "R08-PO-CLS-01"
    scope: "Structured race order P1–P11 times/laps; Prost NC 54 laps; DNF rows with laps/causes; Paletti DNS; DNQ de Villota/Piquet; start time 14:20 listed (not independently verified as official programme)."
  - claim_id: "R08-PO-PTS-01"
    scope: "Cross-check top-six order for provisional points."
disagreement_notes: "Not official FIA; Prost NC vs MS finisher; DNF lap numbers often one lower than MS table."
notes: "Secondary reconstruction; prefer MS narrative for story; use for classification cross-check."
```

```yaml
source_id: "WP-1982-DET-Q"
title: "1982 Detroit Grand Prix — Qualifying table"
author_or_organisation: "Wikipedia (secondary compilation)"
publication_date: "unknown"
event_date: "1982-06-06"
source_type: "SECONDARY"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://en.wikipedia.org/wiki/1982_Detroit_Grand_Prix — Qualifying classification"
access_date: "2026-08-09"
supports:
  - claim_id: "R08-PR-GRID-02"
    scope: "Cross-check Q1/Q2 times P1–P26; Q2 wet times; Lammers no time row; narrative summary of Friday scrub / Saturday dual Q / Piquet DNQ (secondary)."
disagreement_notes: "Living page; Round numbering as Race 7 vs archive round 08."
notes: "Secondary cross-check only; prefer MS narrative + RSC times for claims."
```

```yaml
source_id: "WP-1982-DET-R"
title: "1982 Detroit Grand Prix — Race summary and classification"
author_or_organisation: "Wikipedia (secondary compilation)"
publication_date: "unknown"
event_date: "1982-06-06"
source_type: "SECONDARY"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://en.wikipedia.org/wiki/1982_Detroit_Grand_Prix — Race / Classification"
access_date: "2026-08-09"
supports:
  - claim_id: "R08-PO-CLS-01"
    scope: "Cross-check classification, gaps for top five, Prost NC, DNF laps; secondary narrative of red flag and Watson charge."
  - claim_id: "R08-PO-NAR-01"
    scope: "Secondary cross-check of major race phases only; do not import championship table (Pironi 20 / Ferrari 26) into archive arithmetic."
disagreement_notes: "Living page; standings snippet uses UPI-base Pironi 16→20 — quarantined vs ARCHIVE-R07-STAND line. Circuit length 4.168 vs MS 4.011. Quarantine any later-season framing."
notes: "Secondary only; never primary for standings sums."
```

## Conflict and uncertainty index

| Uncertainty ID | Claim IDs | Source IDs | Status at cutoff | Note |
| --- | --- | --- | --- | --- |
| UNC-R08-PW-LEN | R08-PW-ORG-01, R08-PW-CIR-01 | UPI-1982-05-23-DET, MS-JUL1982-DET | open | UPI ~2 mi / 175 mi vs MS 4.011 km / 62 okr.; Wiki 4.168 km |
| UNC-R08-PW-ZONE | R08-PW-CUT-01, R08-PR-CUT-01 | MS-JUL1982-DET | open | EDT założone; brak niezależnego potwierdzenia etykiety strefy w programie |
| UNC-R08-PW-TAMBAY | R08-PW-FER-01 | MS-JUL1982-DET | open | Samotny Pironi potwierdzony; data/publiczny komunikat Tambay poza zakresem PO jeśli po cutoff |
| UNC-R07-PO-PIR-PTS | R08-PW-STD-01, R08-PO-STD-BASE, R08-PO-PTS-01 | ARCHIVE-R07-STAND, WP-1982-DET-R | open | Carry-forward: Pironi 15→19 vs UPI-base 16→20 |
| UNC-R08-PR-START | R08-PR-CUT-01 | MS-JUL1982-DET, RSC-1982-R08-RES | open | Warm-up 11:20–11:50 solid; RSC lists 14:20 start — not verified as official programme |
| UNC-R08-PR-GRID-OFF | R08-PR-GRID-01 | RSC-1982-R08-Q, WP-1982-DET-Q | open | RSC/Wiki reconstruction vs missing official FIA timing bulletin |
| UNC-R08-PR-CHASSIS | R08-PW-TEC-01 | MS-JUL1982-DET, RSC-1982-R08-Q | open | DSJ McLaren MP4/5–4–6 vs database MP4/1B; prose avoids chassis numbers where conflicting |
| UNC-R08-PR-ASSY | R08-PR-ASSY-01 | MS-JUL1982-DET | open | Assembly/parade sequence before green; detailed pit-exit order not in official bulletin |
| UNC-R08-PO-PROST-CLS | R08-PO-CLS-01 | MS-JUL1982-DET, RSC-1982-R08-RES, WP-1982-DET-R | open | MS lists Prost 12th finisher; RSC/Wiki NC (54 laps) |
| UNC-R08-PO-GIA-LAP | R08-PO-NAR-01 | MS-JUL1982-DET, RSC-1982-R08-RES | open | MS RESULTS lap 41 vs narrative/~30 RSC/Wiki |
| UNC-R08-PO-DNF-LAPS | R08-PO-CLS-01 | MS-JUL1982-DET, RSC-1982-R08-RES, WP-1982-DET-R | open | Systematic off-by-one on several DNF lap counts |
| UNC-R08-PO-2H | R08-PO-NAR-01 | MS-JUL1982-DET | open | DSJ NB: race stopped one lap short despite 2-hour rule |
| UNC-R08-PO-JAR | R08-PO-NAR-01 | MS-JUL1982-DET, RSC-1982-R08-RES | open | Jarier DNF: MS flat engine vs RSC electrics |

## Claim map (pre-weekend)

| Claim ID | Short label | Primary sources |
| --- | --- | --- |
| `R08-PW-STD-01` | Standings after Monaco | `ARCHIVE-R07-STAND` |
| `R08-PW-ORG-01` | Civic/org preview | `UPI-1982-05-23-DET` |
| `R08-PW-CAL-01` | Calendar date | `CAL-01` |
| `R08-PW-CUT-01` | First-session marker / Thu cancel | `MS-JUL1982-DET` |
| `R08-PW-CIR-01` | Circuit character | `MS-JUL1982-DET`, `UPI-1982-05-23-DET` |
| `R08-PW-TOL-01` | Toleman withdrawal | `MS-JUL1982-DET` |
| `R08-PW-FER-01` | Ferrari lone entry | `MS-JUL1982-DET`, `ARCHIVE-R07-PW` |
| `R08-PW-ENT-01` | Field continuity | `ARCHIVE-R07-PW` |
| `R08-PW-ENT-02` | Entry reconstruction | `RSC-1982-R08-ENT` |
| `R08-PW-TEC-01` | Arrival technical notes | `MS-JUL1982-DET` |

## Claim map (pre-race)

| Claim ID | Short label | Primary sources |
| --- | --- | --- |
| `R08-PR-CUT-01` | Start / warm-up clock | `MS-JUL1982-DET` |
| `R08-PR-FRI-01` | Friday scrubbed sessions | `MS-JUL1982-DET` |
| `R08-PR-SAT-01` | Saturday dual Q narrative | `MS-JUL1982-DET` |
| `R08-PR-GRID-01` | Grid P1–P26 + DNQ times | `RSC-1982-R08-Q`, `MS-JUL1982-DET` |
| `R08-PR-GRID-02` | Q1/Q2 cross-check | `WP-1982-DET-Q` |
| `R08-PR-WU-01` | Sunday warm-up | `MS-JUL1982-DET` |
| `R08-PR-ASSY-01` | Pre-lights assembly changes | `MS-JUL1982-DET` |

## Claim map (post-race)

| Claim ID | Short label | Primary sources |
| --- | --- | --- |
| `R08-PO-NAR-01` | Race narrative / phases | `MS-JUL1982-DET`, `WP-1982-DET-R` |
| `R08-PO-CLS-01` | Classification / times | `MS-JUL1982-DET`, `RSC-1982-R08-RES`, `WP-1982-DET-R` |
| `R08-PO-PTS-01` | Round points 9–6–4–3–2–1 | `MS-JUL1982-DET`, `RSC-1982-R08-RES` |
| `R08-PO-SCR-01` | Post-race scrutineering | `MS-JUL1982-DET` |
| `R08-PO-STD-BASE` | Championship arithmetic base | `ARCHIVE-R07-STAND` |
