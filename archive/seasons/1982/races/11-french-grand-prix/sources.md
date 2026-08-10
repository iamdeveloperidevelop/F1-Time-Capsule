# French Grand Prix — source ledger

To kanoniczny rejestr źródeł folderu rundy. Dokumenty treści cytują
`source_id` i `claim_id`; nie prowadzą konkurencyjnych list źródeł. Cutoff
rejestru przy post-race obejmuje `pre-weekend.md`, `pre-race.md`,
`post-race.md` i `standings-after.md` (granica: koniec natychmiastowej
procedury oficjalnej po wyścigu Paul Ricard, niedziela 25 VII 1982 CEST).

## Source entry

```yaml
source_id: "ARCHIVE-R10-STAND"
title: "Klasyfikacja po Grand Prix Wielkiej Brytanii"
author_or_organisation: "F1 Time Capsule archive (standings-after.md R10)"
publication_date: "not-applicable"
event_date: "1982-07-18"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/10-british-grand-prix/standings-after.md"
access_date: "2026-08-10"
supports:
  - claim_id: "R11-PW-STD-01"
    scope: "Prowizoryczna kolejność i punkty po Brands Hatch: Pironi 34; Watson 30; Lauda 24; Rosberg 21; Patrese/Prost 19; Piquet 17; McLaren 54; Ferrari 44; Brabham 36; Williams 34; Renault 23; otwarte apelacje LB; skala prowizoryczna; konflikt Pironi 34 vs 35 / Ferrari 44 vs 45."
  - claim_id: "R11-PO-PTS-01"
    scope: "Baza arytmetyki post-race: sumy po Brands + punkty Paul Ricard (linia archiwum Pironi 34→38 / Ferrari 44→51)."
disagreement_notes: "Konflikt Pironi/Ferrari z liniami Wiki (UNC-R11-PW-PIR-PTS / UNC-R11-PO-PIR-PTS)."
notes: "Baza przed Paul Ricard; nie kopiować pełnych tabel do narracji."
```

```yaml
source_id: "ARCHIVE-R10-PO"
title: "Grand Prix Wielkiej Brytanii — po wyścigu"
author_or_organisation: "F1 Time Capsule archive (post-race.md R10)"
publication_date: "not-applicable"
event_date: "1982-07-18"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/10-british-grand-prix/post-race.md"
access_date: "2026-08-10"
supports:
  - claim_id: "R11-PW-DEV-GB"
    scope: "Lauda 1, Pironi 2, Tambay 3, de Angelis 4, Daly 5, Prost 6; próba postoju Brabhama / Piquet out wtrysk; Warwick chwilowo 2.; Mansell DNF kontuzja ręki."
disagreement_notes: null
notes: "Carry-forward faktów z Brands Hatch; nie importować foreshadowingu French GP."
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
  - claim_id: "R11-PW-EVT-01"
    scope: "French GP Paul Ricard 25 July 1982 na ogłoszonej liście FIA."
disagreement_notes: null
notes: "publication_date dnia unknown; content-based availability. Już w season/calendar.md."
```

```yaml
source_id: "MS-1982-09-FR"
title: "French Grand Prix — Renault at home"
author_or_organisation: "Motor Sport (Denis Jenkinson)"
publication_date: "1982-09"
event_date: "1982-07-23/1982-07-25"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/september-1982/107/french-grand-prix-17/"
access_date: "2026-08-10"
supports:
  - claim_id: "R11-PW-CUT-01"
    scope: "Cztery pełne dni po Brands Hatch; ~1000 mil transportu; gotowość na start ≈10:00 piątek rano na Paul Ricard."
  - claim_id: "R11-PW-ENT-01"
    scope: "Lees za Mansella (Lotus 91); poza tym bezpieczny transfer; Ligier tylko JS19 (3 auta); Renault starsze podwozie Arnouxa (Monte Carlo); nerwowa atmosfera / plotka o wstrzymaniu development money; Fittipaldi F9 first string + F8D spare; ATS/Tyrrell smoother bodywork na Mistral."
  - claim_id: "R11-PW-TEC-01"
    scope: "Na torze z długą prostą moc silnika (turbo Renault/Ferrari/BMW) przeważa nad samym chassis/aero wobec Cosworth/Alfa/Matra."
disagreement_notes: "Jenkinson RE38B vs standardowe oznaczenie RE30B — używać opisu «starsze podwozie / Monte Carlo», nie forsować numeru."
notes: "publication_date dnia unknown; content-based availability. Używać TYLKO otwarcia i pasażu przed nagłówkiem Qualifying; kwarantanna qualifying/race/Mass-Baldi/wyniku. Korekta 52→54 okr. w sekcji Race — poza cutoff PW."
```

```yaml
source_id: "AS-ROEBUCK-FR1982"
title: "Grand Prix Gold: 1982 French GP (Entry & Practice excerpts)"
author_or_organisation: "Autosport / Nigel Roebuck (reprint)"
publication_date: "unknown"
event_date: "1982-07-23/1982-07-25"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.autosport.com/f1/news/grand-prix-gold-1982-french-gp-5098981/5098981/ — Entry & Practice"
access_date: "2026-08-10"
supports:
  - claim_id: "R11-PW-DEV-CAL"
    scope: "Back-to-back po Brands; mechanicy due Wednesday/Thursday; first qualifying Friday; kalendarz wiązany z World Cup TV; GP Francji ~3 tygodnie później niż zwykle, w sezonie urlopowym."
  - claim_id: "R11-PW-EXP-01"
    scope: "Presja na Renault u siebie (wiele poles, mało wyników); charakter Mistral / kompromis skrzydło vs prosta — pasaż Entry & Practice przed qualifyingiem."
  - claim_id: "R11-PW-ENT-LEE"
    scope: "Geoff Lees stands in for Nigel Mansell at Lotus (decyzja po problemach z ręką na Brands)."
  - claim_id: "R11-PW-LIG-01"
    scope: "Ligier: tylko JS19 na żądanie Guy Ligier; testy new sidepods Dijon earlier in the week przed przyjazdem."
disagreement_notes: null
notes: "Reprint; publication_date oryginału unknown; content-based availability. Dla pre-weekend: tylko Entry & Practice przed pierwszą sesją. Dla pre-race: Entry & Practice + warm-up / niedzielny poranek przed zielonym. STRICT quarantine: wynik wyścigu, Mass–Baldi Signes, Arnoux/Prost team-orders outcome."
```

```yaml
source_id: "AS-ROEBUCK-FR1982-PR"
title: "Grand Prix Gold: 1982 French GP (Entry & Practice + pre-green Sunday)"
author_or_organisation: "Autosport / Nigel Roebuck (reprint)"
publication_date: "unknown"
event_date: "1982-07-23/1982-07-25"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.autosport.com/f1/news/grand-prix-gold-1982-french-gp-5098981/5098981/ — Entry & Practice; Race open through warm-up / 1.30 green note"
access_date: "2026-08-10"
supports:
  - claim_id: "R11-PR-POLE-01"
    scope: "Arnoux pole 1:34.406 (Sat, dwa flying); Prost 1:34.688; nikt inny w sekundzie; cytaty Arnoux/Prost/Rosberg/Lauda/Pironi/Warwick."
  - claim_id: "R11-PR-PRAC-01"
    scope: "Narracja treningów: Renault hydraulika/karbon; Ferrari spin/wtrysk wody; Brabham awarie i plan postoju; Toleman pożar/wypadek; Alfa late setup; Cosworth midfield; DNQ causes."
  - claim_id: "R11-PR-WU-01"
    scope: "Niedziela: upał, dym pożarów, frekwencja ~70k; warm-up Brabhamy najszybsze, potem Renault/Pironi/McLaren/Tambay/Fabi; pomarańczowe pasy Brabhama."
  - claim_id: "R11-PR-START-01"
    scope: "Autosport: «At 1.30 the green light flashed» — kotwica zegara startu (izolować od narracji wyścigu)."
disagreement_notes: "Reprint OCR «Prost 1m 38.88s» vs konsensus 1:34.688 (UNC-R11-PR-PROST-Q). Start 13:30 vs prostfan 14:00 (UNC-R11-PR-START)."
notes: "Alias claim-map dla pre-race; ten sam tekst co AS-ROEBUCK-FR1982. Kwarantanna od zielonego światła włącznie z wynikiem."
```

```yaml
source_id: "MS-1982-09-FR-PR"
title: "French Grand Prix — Renault at home (Qualifying + Race morning)"
author_or_organisation: "Motor Sport (Denis Jenkinson)"
publication_date: "1982-09"
event_date: "1982-07-23/1982-07-25"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/september-1982/107/french-grand-prix-17/ — Qualifying; Race through abort-start / parade (pre-green)"
access_date: "2026-08-10"
supports:
  - claim_id: "R11-PR-CUT-01"
    scope: "Format dwóch dni morning testing + afternoon qualifying (2 sets); niedziela supporting + final thirty minutes testing."
  - claim_id: "R11-PR-TURBO-01"
    scope: "Po kwalifikacjach: dwa Renault, Ferrari+BMW, Ferrari+BMW, dwie Alfy, dwa Cosworthy — geometria pola."
  - claim_id: "R11-PR-PRAC-MS"
    scope: "Upał+wiatr; Renault względnie bezawaryjne; Brabham Castrol/awarie; Ferrari Pironi spin/wastegate; Tambay water-injection; Warwick late flying 14th; Fabi 21st."
  - claim_id: "R11-PR-DIST-01"
    scope: "Poprawka 52→54 okr.; procedura abortu startu (−1 okr. przy każdym abort); ~5.810 km / 313.74 km."
  - claim_id: "R11-PR-WU-MS"
    scope: "Niedziela rano: boost knobs Renault; Brabham refuel kit; Ligier overnight fail; eksperymentalne Ferrari i spare Renault nieużywane; wybór opon."
disagreement_notes: "Podpis zdjęcia «Fabi 24th» błędny (Fabi 21.; Lees 24.) — nie używać. Arnoux chassis RE38B vs AS «new» (UNC-R11-PW-REN-CHASSIS)."
notes: "publication_date dnia unknown; content-based availability. Kwarantanna od zielonego światła / wyniku / Mass–Baldi / team orders."
```

```yaml
source_id: "WP-1982-FR-Q"
title: "1982 French Grand Prix — qualifying table"
author_or_organisation: "Wikipedia (compilation; isolate Q times)"
publication_date: "unknown"
event_date: "1982-07-23/1982-07-24"
source_type: "SECONDARY"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://en.wikipedia.org/wiki/1982_French_Grand_Prix — Qualifying"
access_date: "2026-08-10"
supports:
  - claim_id: "R11-PR-GRID-01"
    scope: "Best qualifying times P1–P26 + DNQ Lammers/Guerrero/Serra/Boesel z czasami."
disagreement_notes: null
notes: "Krzyżowy check z RSC/prostfan/STATS F1; nie oficjalny biuletyn FIA. Kwarantanna race/championship-after."
```

```yaml
source_id: "RSC-1982-R11-GRID"
title: "GP France 1982 — starting grid"
author_or_organisation: "Racing Sports Cars"
publication_date: "unknown"
event_date: "1982-07-25"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "http://www.racingsportscars.com/f1/grid/Paul_Ricard-1982-07-25.html"
access_date: "2026-08-10"
supports:
  - claim_id: "R11-PR-GRID-01"
    scope: "Grid positions and Q times Arnoux 1:34.406 … Mass 1:41.579 (cross-check)."
disagreement_notes: null
notes: "Wtórna baza; używać z Wiki/prostfan."
```

```yaml
source_id: "PROSTFAN-1982-FR-ENT"
title: "1982 French GP — entry list and race details"
author_or_organisation: "prostfan.com (compilation)"
publication_date: "unknown"
event_date: "1982-07-25"
source_type: "SECONDARY"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.prostfan.com/racedet/82fra.htm — Entry List / Race details"
access_date: "2026-08-10"
supports:
  - claim_id: "R11-PW-ENT-02"
    scope: "30 zgłoszeń kierowców nr 1–36 (z lukami numeracji); Lees #12 Lotus; oficjalna nazwa LXVIII Grand Prix de France; 5810 m × 54 laps = 313.740 km."
  - claim_id: "R11-PR-START-01"
    scope: "Local Start Time 14:00 h (wtórna kotwica vs AS ~13:30)."
  - claim_id: "R11-PR-DIST-01"
    scope: "5810 m × 54 laps = 313.740 km (krzyżowy check z MS)."
disagreement_notes: "Serra listed as F8D; MS mówi F9 first string + F8D spare — zachować MS dla intencji sprzętowej. Start 14:00 vs AS 13:30."
notes: "Pre-weekend: entry/dystans. Pre-race: także 14:00 i dystans. Kwarantanna wyniku wyścigu."
```

```yaml
source_id: "RSC-1982-R11-ENT"
title: "GP France 1982 — car data / practiced field"
author_or_organisation: "Racing Sports Cars"
publication_date: "unknown"
event_date: "1982-07-25"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "http://www.racingsportscars.com/f1/entry/data/Paul_Ricard-1982-07-25.html ; http://www.racingsportscars.com/f1/race/Paul_Ricard-1982-07-25.html"
access_date: "2026-08-10"
supports:
  - claim_id: "R11-PW-ENT-03"
    scope: "Zestaw podwozi/silników przy Paul Ricard 1982 (Brabham BT50-BMW, Tyrrell 011, Williams FW08, McLaren MP4/1, Lotus 91, Renault RE30, Ferrari 126, Ligier JS19, Toleman TG181-Hart itd.); Practiced 30."
disagreement_notes: "Track length «unknown» w nagłówku RSC vs 5.81 km w innych źródłach."
notes: "Wtórna baza; nie używać wyników/grida. Oficjalny telex entry — luka."
```

```yaml
source_id: "WP-1982-FR-R"
title: "1982 French Grand Prix"
author_or_organisation: "Wikipedia (compilation; isolate venue facts)"
publication_date: "unknown"
event_date: "1982-07-25"
source_type: "SECONDARY"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://en.wikipedia.org/wiki/1982_French_Grand_Prix — Race details"
access_date: "2026-08-10"
supports:
  - claim_id: "R11-PW-CIR-01"
    scope: "25 July 1982; 68ème Grand Prix de France; Circuit Paul Ricard, Le Castellet, Var; course length 5.809 km; 54 laps / 313.686 km."
disagreement_notes: "Minor length variance vs 5.810 km / 313.74 km elsewhere."
notes: "STRICT quarantine: qualifying, race, championship-after, Pironi «last finish», Mass retirement foreshadowing, Arnoux team-orders narrative."
```

```yaml
source_id: "MS-DB-1982-FR"
title: "1982 French Grand Prix — Motorsport Magazine database"
author_or_organisation: "Motor Sport Magazine database"
publication_date: "unknown"
event_date: "1982-07-25"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/database/races/1982-french-grand-prix/"
access_date: "2026-08-10"
supports:
  - claim_id: "R11-PW-CIR-02"
    scope: "Sunday 25 July 1982; Grand Prix de France; Paul Ricard permanent road course; ~3.61 miles."
disagreement_notes: null
notes: "Używać date/venue/length; kwarantanna wyników."
```

```yaml
source_id: "MS-1982-09-FR-R"
title: "French Grand Prix — Renault at home (Race + RESULTS)"
author_or_organisation: "Motor Sport (Denis Jenkinson)"
publication_date: "1982-09"
event_date: "1982-07-25"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/september-1982/107/french-grand-prix-17/ — Race through RESULTS"
access_date: "2026-08-10"
supports:
  - claim_id: "R11-PO-CLS-01"
    scope: "Klasyfikacja 1–16 + DNF z czasami absolutnymi top 6; 54 okr.; 5.810 km; 313.74 km; Very Warm; 26 starters / 16 finishers."
  - claim_id: "R11-PO-POD-01"
    scope: "Podium Arnoux–Prost–Pironi."
  - claim_id: "R11-PO-FL-01"
    scope: "FL Patrese 1:40.075 okr. 4 (209.003 km/h)."
  - claim_id: "R11-PO-ABORT-01"
    scope: "Procedura abortu uzgodniona; faktyczny start bez abortu; Jarier półoś na starcie."
  - claim_id: "R11-PO-NAR-01"
    scope: "Start Renault 1–2; Brabhamy lead; Patrese pożar; Piquet out; Renault 1–2; Signes Mass–Baldi; team orders zignorowane; protest fartuchów (Tyrrell→Williams)."
  - claim_id: "R11-PO-PIQ-01"
    scope: "Piquet out silnik BMW; RESULTS lap 24 (narracja MS «lap 14» — konflikt)."
  - claim_id: "R11-PO-TEC-01"
    scope: "Plan postoju Brabhama niedokończony; turbo vs Cosworth; fartuch/prowadzenie Prosta."
  - claim_id: "R11-PO-PROT-01"
    scope: "Po mecie protest o fartuchy Renault (Tyrrell skłania Williamsa); wynik tego dnia niepodany jako formalne rozstrzygnięcie."
disagreement_notes: "Oznaczenia podwozi RE38B/RE36B OCR vs konsensus RE30B; narracja Piquet «lap 14» vs RESULTS lap 24 (UNC-R11-PO-PIQ-LAP); Fabi oil pressure vs AS electrical; DNF lap N vs Wiki completed (UNC-R11-PO-LAPN)."
notes: "publication_date dnia unknown; content-based availability. Dla post-race: Race + RESULTS. Kwarantanna foreshadowingu Hockenheim / karier."
```

```yaml
source_id: "AS-ROEBUCK-FR1982-R"
title: "Grand Prix Gold: 1982 French GP (Race)"
author_or_organisation: "Autosport / Nigel Roebuck (reprint)"
publication_date: "unknown"
event_date: "1982-07-25"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.autosport.com/f1/news/grand-prix-gold-1982-french-gp-5098981/5098981/ — Race"
access_date: "2026-08-10"
supports:
  - claim_id: "R11-PO-START-01"
    scope: "Zielone ~13:30; Arnoux–Prost–Pironi; Jarier driveshaft; Fabi electrical; Salazar spin."
  - claim_id: "R11-PO-PAT-01"
    scope: "Patrese lead / FL; pożar silnika ~okr. 8; Piquet lead; wybuch ~okr. 24 (~22 s przewagi)."
  - claim_id: "R11-PO-MASS-01"
    scope: "Mass–Baldi Signes ~okr. 11; March w strefie widzów; Mass lekkie oparzenie barku; Baldi OK; ~12 widzów rannych, nikt krytycznie."
  - claim_id: "R11-PO-ORD-01"
    scope: "Sygnały team orders; Arnoux odmawia."
  - claim_id: "R11-PO-Q-PRO-01"
    scope: "Cytat Prost: przed wyścigiem uzgodniono, że przy 1–2 to on wygrywa."
  - claim_id: "R11-PO-Q-ARN-01"
    scope: "Cytat Arnoux: 5–10 s przepuściłby; miał ~23 s; rytm; Pironi; własne nadzieje."
  - claim_id: "R11-PO-Q-PIR-01"
    scope: "Cytat Pironi: cztery punkty; zbyt konserwatywne opony."
  - claim_id: "R11-PO-Q-TAM-01"
    scope: "Cytat Tambay: A/AA jak jazda po lodzie."
  - claim_id: "R11-PO-Q-ROS-01"
    scope: "Cytat Rosberg: blister lewej tylnej; Alboreto w ciasnych; Williams szybszy na prostej."
  - claim_id: "R11-PO-MID-01"
    scope: "Watson electrical; Lauda pit delay; Daly puncture; Warwick clutch; Prost damaged skirt."
  - claim_id: "R11-PO-LATE-01"
    scope: "Druga połowa: Renault control; Ferrari opony; Rosberg–Alboreto Class B."
  - claim_id: "R11-PO-PIQ-01"
    scope: "Piquet engine ~okr. 24 (~22 s lead)."
  - claim_id: "R11-PO-TEC-01"
    scope: "Brabham pit plan; turbo domination; Prost skirt."
disagreement_notes: "Fabi electrical vs MS oil (UNC-R11-PO-FABI). Site chrome «Previous: German GP» i kazanie safety — kwarantanna foreshadowingu."
notes: "Reprint; publication_date oryginału unknown; content-based availability. Izolować Race; nie używać nav/safety sermon jako foreshadowing wyniku przyszłych rund."
```

```yaml
source_id: "WP-1982-FR-R-PO"
title: "1982 French Grand Prix — race classification"
author_or_organisation: "Wikipedia (compilation; isolate race table)"
publication_date: "unknown"
event_date: "1982-07-25"
source_type: "SECONDARY"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://en.wikipedia.org/wiki/1982_French_Grand_Prix — Race classification; Championship standings after the race (cross-check only)"
access_date: "2026-08-10"
supports:
  - claim_id: "R11-PO-CLS-01"
    scope: "Pozycje, okrążenia ukończone, statusy DNF, punkty 9–6–4–3–2–1; FL Patrese."
  - claim_id: "R11-PO-PTS-01"
    scope: "Punkty rundy; tabele mistrzostw Wiki (Pironi 39 / Ferrari 52) jako linia konfliktu vs archiwum."
disagreement_notes: "Lead/notes: last Pironi finish, Mass retirement, Arnoux left Renault — STRICT quarantine. Pironi 39 vs archiwum 38 (UNC-R11-PO-PIR-PTS)."
notes: "Krzyżowy check z MS/F1.com; nie oficjalny biuletyn FIA."
```

```yaml
source_id: "F1COM-1982-FR-RES"
title: "1982 French Grand Prix — race result"
author_or_organisation: "formula1.com"
publication_date: "unknown"
event_date: "1982-07-25"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.formula1.com/en/results/1982/races/447/france/race-result"
access_date: "2026-08-10"
supports:
  - claim_id: "R11-PO-TIME-01"
    scope: "Czas zwycięzcy 1:33:33.217; straty zaokrąglone (+17.310 / +42.130 / +76.240 / +90.990 / +92.340)."
  - claim_id: "R11-PO-CLS-01"
    scope: "Kolejność i okrążenia 1–16 + NC/DNF jako krzyżowy check."
disagreement_notes: "Zaokrąglenie gap vs MS absolutne (UNC-R11-PO-GAP); przyczyny DNF blank na stronie."
notes: "Wtórna baza timingowa; preferować MS absolutne czasy w narracji z footnote rounding."
```

```yaml
source_id: "RSC-1982-R11-RES"
title: "GP France 1982 — race results"
author_or_organisation: "Racing Sports Cars"
publication_date: "unknown"
event_date: "1982-07-25"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "http://www.racingsportscars.com/race/Paul_Ricard-1982-07-25.html"
access_date: "2026-08-10"
supports:
  - claim_id: "R11-PO-FL-01"
    scope: "FL Patrese; frekwencja ~70k; 16 finisherów (krzyżowy check)."
disagreement_notes: null
notes: "Wtórna baza; używać z MS/Wiki/F1.com."
```

## Conflict and uncertainty index

| Uncertainty ID | Claim IDs | Source IDs | Status at cutoff | Note |
| --- | --- | --- | --- | --- |
| UNC-R11-PW-PIR-PTS | R11-PW-STD-01 | ARCHIVE-R10-STAND, WP-1982-FR-R | open | Pironi 34 vs 35 / Ferrari 44 vs 45 — kontynuacja konfliktu bazowego |
| UNC-R11-PW-CUT | R11-PW-CUT-01 | MS-1982-09-FR, AS-ROEBUCK-FR1982 | open | ≈10:00 piątek z MS; brak niezależnego programu wydarzenia |
| UNC-R11-PW-LEN | R11-PW-CIR-01 | WP-1982-FR-R, PROSTFAN-1982-FR-ENT, MS-DB-1982-FR | open | 5.809 vs 5.810 km; brak oficjalnego pomiaru programu |
| UNC-R11-PW-ENT | R11-PW-ENT-02 | PROSTFAN-1982-FR-ENT, RSC-1982-R11-ENT, MS-1982-09-FR | open | Brak oficjalnego telexu FOCA/FISA; F9 vs F8D listing |
| UNC-R11-PW-REN-CHASSIS | R11-PW-ENT-01 | MS-1982-09-FR, RSC-1982-R11-ENT | open | MS RE38B vs RSC/Wiki RE30B dla zapasowego Arnouxa — w PW tylko «starsze podwozie / Monte Carlo» |
| UNC-R11-PW-WX | — | — | open | Brak datowanej prognozy pogody ≤ cutoff |
| UNC-R11-PW-LAPS | — | MS-1982-09-FR | resolved-for-PR | Korekta 52→54 użyta w pre-race z MS Race morning; nadal otwarta względem cutoff PW |
| UNC-R11-PR-START | R11-PR-START-01 | AS-ROEBUCK-FR1982-PR, PROSTFAN-1982-FR-ENT | open | AS ~13:30 green vs prostfan 14:00 scheduled |
| UNC-R11-PR-PROST-Q | R11-PR-POLE-01 | AS-ROEBUCK-FR1982-PR, WP-1982-FR-Q | open | AS reprint OCR «1m 38.88s» vs konsensus 1:34.688 |
| UNC-R11-PR-WU-TIMES | R11-PR-WU-01 | AS-ROEBUCK-FR1982-PR, MS-1982-09-FR-PR | open | Brak numerycznych czasów rozgrzewki w użytych źródłach |
| UNC-R11-PR-PEN | R11-PR-PEN-01 | AS-ROEBUCK-FR1982-PR, MS-1982-09-FR-PR | open | Brak oficjalnego biuletynu kar — negatywne znalezienie z prasy |
| UNC-R11-PO-PIR-PTS | R11-PO-PTS-01 | ARCHIVE-R10-STAND, WP-1982-FR-R-PO | open | Pironi 38 vs Wiki 39; Ferrari 51 vs 52 |
| UNC-R11-PO-GAP | R11-PO-TIME-01 | MS-1982-09-FR-R vs F1COM-1982-FR-RES | open | MS absolutne vs F1.com rounding (+17.308 vs +17.310 itd.) |
| UNC-R11-PO-LAPN | R11-PO-CLS-01 | MS vs WP/F1COM | open | MS «retired on lap N» vs completed laps |
| UNC-R11-PO-FABI | R11-PO-START-01 | MS vs AS/WP/F1COM | open | oil pressure vs electrical |
| UNC-R11-PO-PIQ-LAP | R11-PO-PIQ-01 | MS-1982-09-FR-R | open | Narracja MS lap 14 vs RESULTS/AS/Wiki ~24 |
| UNC-R11-PO-PROTEST | R11-PO-PROT-01 | MS-1982-09-FR-R | open | Złożenie protestu fartuchów; brak potwierdzonego wyniku tego dnia |
| UNC-R11-PO-MASS-INJ | R11-PO-MASS-01 | AS vs WP | open | AS bark vs Wiki hands — preferować AS; brak biuletynu medycznego |
