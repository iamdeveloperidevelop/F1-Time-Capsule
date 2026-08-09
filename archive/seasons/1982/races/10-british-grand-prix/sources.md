# British Grand Prix — source ledger

To kanoniczny rejestr źródeł folderu rundy. Dokumenty treści cytują
`source_id` i `claim_id`; nie prowadzą konkurencyjnych list źródeł. Cutoff
rejestru przy post-race obejmuje `pre-weekend.md`, `pre-race.md`,
`post-race.md` i `standings-after.md` (granica: koniec natychmiastowej
procedury oficjalnej po wyścigu Brands Hatch, niedziela 18 VII 1982 BST).

## Source entry

```yaml
source_id: "ARCHIVE-R09-STAND"
title: "Klasyfikacja po Grand Prix Kanady"
author_or_organisation: "F1 Time Capsule archive (standings-after.md R09)"
publication_date: "not-applicable"
event_date: "1982-06-13"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/09-canadian-grand-prix/standings-after.md"
access_date: "2026-08-10"
supports:
  - claim_id: "R10-PW-STD-CAN"
    scope: "Prowizoryczna kolejność i punkty po Kanadzie: Watson 30; Pironi/Patrese 19; Prost 18; Rosberg 17; Lauda 12; Piquet 11; McLaren 42; Brabham 30; Williams 26; Ferrari 25; Renault 22; otwarte apelacje LB; skala prowizoryczna; konflikt Pironi 19 vs 20."
disagreement_notes: "Konflikt Pironi 19 vs Wiki/UPI-base 20 (UNC-R09-PO-PIR-PTS)."
notes: "Baza przed Holandią i Brands Hatch; nie kopiować pełnych tabel do narracji."
```

```yaml
source_id: "ARCHIVE-R09-PO"
title: "Grand Prix Kanady — po wyścigu (kontuzja Mansella / Paletti / Osella)"
author_or_organisation: "F1 Time Capsule archive (post-race.md R09)"
publication_date: "not-applicable"
event_date: "1982-06-13"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/09-canadian-grand-prix/post-race.md"
access_date: "2026-08-10"
supports:
  - claim_id: "R10-PW-DEV-MAN"
    scope: "Mansell kontuzja lewego ramienia/nadgarstka w kolizji z Giacomellim w Montrealu — kontekst nieobecności w Holandii i powrotu na Brands Hatch."
  - claim_id: "R10-PW-DEV-PAL"
    scope: "Śmierć Palettiego; Osella wycofuje Jariera z restartu — kontekst jednego samochodu Oselli w kolejnych rundach."
disagreement_notes: null
notes: "Carry-forward faktów z Kanady; nie importować foreshadowingu Brands."
```

```yaml
source_id: "ARCHIVE-R09-PW"
title: "Grand Prix Kanady — przed weekendem (Toleman DNA)"
author_or_organisation: "F1 Time Capsule archive (pre-weekend.md R09)"
publication_date: "not-applicable"
event_date: "1982-06-11/1982-06-13"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/09-canadian-grand-prix/pre-weekend.md"
access_date: "2026-08-10"
supports:
  - claim_id: "R10-PW-DEV-TOL"
    scope: "Toleman nie dojechał do Montrealu mimo zapowiedzi w Detroit — carry-forward nieobecności NA przed powrotem w Holandii."
disagreement_notes: null
notes: "Carry-forward z R09 PW; Detroit DNA w tym samym łańcuchu archiwum."
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
  - claim_id: "R10-PW-EVT-01"
    scope: "British GP Brands Hatch 18 July 1982 na ogłoszonej liście FIA; Holandia/Zandvoort nieobecna na tej liście (nieuregulowane płatności)."
disagreement_notes: "Holandia wróciła 3 VII 1982 — patrz UPI-1982-06-18-NL / WP-1982-NL-R."
notes: "publication_date dnia unknown; content-based availability. Już w season/calendar.md."
```

```yaml
source_id: "UPI-1982-06-18-NL"
title: "A financial agreement with the Formula One Constructors Association..."
author_or_organisation: "UPI Archives"
publication_date: "1982-06-18"
event_date: "1982-06-18"
source_type: "PRESS"
contemporary: true
spoiler_risk: "none"
locator: "https://www.upi.com/Archives/1982/06/18/A-financial-agreement-with-the-Formula-One-Constructors-Association/2671393220800/"
access_date: "2026-08-10"
supports:
  - claim_id: "R10-PW-DEV-NL-01"
    scope: "Umowa FOCA–Zandvoort: FOCA bierze zyski z GP Holandii 3 VII, kasuje dług 1,1 mln guldenów; joint venture do 1987; Ecclestone podpisuje; Vermeulen «said Friday»."
disagreement_notes: null
notes: "Silne współczesne źródło pierwotne dla przywrócenia Holandii."
```

```yaml
source_id: "WP-1982-NL-R"
title: "1982 Dutch Grand Prix"
author_or_organisation: "Wikipedia (compilation; isolate race facts)"
publication_date: "unknown"
event_date: "1982-07-03"
source_type: "SECONDARY"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://en.wikipedia.org/wiki/1982_Dutch_Grand_Prix — Results / Race details"
access_date: "2026-08-10"
supports:
  - claim_id: "R10-PW-DEV-NL-02"
    scope: "Zandvoort 3 July 1982; Pironi 1, Piquet 2, Rosberg 3, Lauda 4, Daly 5, Baldi 6; Tambay Ferrari #27 8.; Warwick FL; Mansell absent / Moreno; Toleman present."
  - claim_id: "R10-PW-STD-NL"
    scope: "Punkty rundy holenderskiej 9–6–4–3–2–1 dla podium+top6; wtórna tabela mistrzostw Watson 30 / Pironi 29 (konflikt z archiwum)."
disagreement_notes: "Pironi 29 vs archiwum 28; foreshadowing kariery / Hockenheim na stronach fansite — kwarantanna."
notes: "Używać tylko faktów publicznych po 3 VII i przed Brands; weryfikować z SPORTS-1982-NL."
```

```yaml
source_id: "SPORTS-1982-NL"
title: "Formula 1 - World Championship 1982 - Dutch Grand Prix classification"
author_or_organisation: "the-sports.org"
publication_date: "unknown"
event_date: "1982-07-03"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.the-sports.org/formula-1-1982-world-championship-epr17355.html — Dutch Grand Prix 1982-07-03"
access_date: "2026-08-10"
supports:
  - claim_id: "R10-PW-DEV-NL-03"
    scope: "Potwierdzenie kolejności i czasów top 6 Holandii (Pironi–Piquet–Rosberg–Lauda–Daly–Baldi)."
disagreement_notes: null
notes: "Wtórna baza wyników; bez narracji foreshadowing."
```

```yaml
source_id: "AS-ROEBUCK-GB1982"
title: "Grand Prix Gold: 1982 British GP (Autosport / Nigel Roebuck reprint)"
author_or_organisation: "Autosport (Roebuck); republished autosport.com 2012"
publication_date: "unknown"
event_date: "1982-07-16/1982-07-18"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.autosport.com/f1/news/grand-prix-gold-1982-british-gp-5098982/5098982/ — Entry & Practice; Race morning warm-up / pre-parade; Race (post-green)"
access_date: "2026-08-10"
supports:
  - claim_id: "R10-PW-EXP-01"
    scope: "Po dziewięciu rundach turbo vs Cosworth 5:4; Brands jako nadzieja Cosworth przed sierpniowymi torami turbo; testy Rosberg najszybszy przed de Angelisem."
  - claim_id: "R10-PW-EXP-02"
    scope: "Cytat/parafruza Franka Dernie o FW08 i braku prostych na Brands; nadzieja Rosberga na pierwsze zwycięstwo."
  - claim_id: "R10-PW-TEC-BRA"
    scope: "Historie o tajemniczych testach Brabhama na Donington / planowanym postoju — jako plotka/przygotowanie przedsesyjne; bez walidacji wyścigowej."
  - claim_id: "R10-PW-ENT-02"
    scope: "Fittipaldi F9 testowane na Donington w tygodniu; Boesel wypadek Snetterton; de Villota wycofany."
  - claim_id: "R10-PW-POL-01"
    scope: "Kontekst zwrotów biletów po Villeneuve / obawy organizatorów (pasaż race-morning — użyty ostrożnie jako tło sprzed sesji)."
  - claim_id: "R10-PW-EVT-02"
    scope: "Format weekendu: piątkowy poranek pierwszej aktywności, timed sessions, sobota, niedziela — bez zegara programu."
  - claim_id: "R10-PR-SES-01"
    scope: "Narracja piątek/sobota: de Angelis AM; Rosberg pole 1:09.540; Arnoux–Rosberg Druids; sobota ride-height; Brabham assault Patrese/Piquet; Pironi gearbox cars; Lauda/Arnoux/Prost/Daly/Tambay/Giacomelli/Toleman/Mansell/Henton/Serra/Cheever."
  - claim_id: "R10-PR-TEC-BRA-01"
    scope: "Plan postoju Brabhama: air-jacks, filtry, Blash 35–40 s / pół baku; Stappert intention; Rosberg «Murray hoax»."
  - claim_id: "R10-PR-WU-01"
    scope: "Rozgrzewka: Rosberg wyskok biegu / ~11300 rpm → wymiana silnika; Warwick szybki (bez czasu); pogoda sobota gorgeous / niedziela słońce."
  - claim_id: "R10-PR-PRE-01"
    scope: "Parada: parowanie paliwa Rosberga, push-start, start z końca pola; sprzęt paliwowy Brabhama, Goodyear «A», Blash half-distance."
  - claim_id: "R10-PR-QTE-01"
    scope: "Cytaty przedstartowe: Blash, Stappert, Rosberg, Lauda, Sage, Prost, Pironi, Daly, Tambay, Mansell, Giacomelli."
  - claim_id: "R10-PO-START-02"
    scope: "Patrese stall (first gear jumped out); Arnoux hit; Fabi on wheel; Pironi jink; no red flag."
  - claim_id: "R10-PO-LEAD-01"
    scope: "Piquet leads laps 1–9 (~10 s); injection pump belt; Brabham refuel cancelled."
  - claim_id: "R10-PO-WAR-01"
    scope: "Warwick charge 16→2; CV joint ~lap 40; crowd reaction; quotes Pironi/Warwick."
  - claim_id: "R10-PO-WAT-01"
    scope: "Serra–Jarier Hawthorns; Watson spin/stall; Guerrero oil line then engine."
  - claim_id: "R10-PO-LATE-01"
    scope: "Second-half problems; Tambay passes de Angelis last lap; Daly–Prost; Henton FL lap 63; Rosberg fuel pressure ~51."
  - claim_id: "R10-PO-Q-LAU-01"
    scope: "Lauda post-race quotes (no problem after Piquet out; car/engine/tyres; Porsche wish)."
disagreement_notes: "Reprint 2012 miesza preview z pełnym raportem praktyki/wyścigu — izolować Entry & Practice + warm-up/pre-parade + Race; kwarantanna site chrome / linki do French GP Gold / późniejsze wyjaśnienia Warwick half-tank. Intro «engine blow» vs body «jumped out of gear» (UNC-R10-PR-ROE-ENGINE). Narracyjne «40 s» / «15 s» vs oficjalne +25.7 s (UNC-R10-PO-GAP)."
notes: "publication_date oryginalnego numeru Autosport unknown; content-based availability dla pasażów weekendu Brands Hatch do natychmiastowej procedury po wyścigu. Kwarantanna: późniejsze wywiady Warwicka o pół baku; treść French GP; retrospectives."
```

```yaml
source_id: "RSC-1982-R10-ENT"
title: "GP Great Britain 1982 — Entry List"
author_or_organisation: "Racing Sports Cars"
publication_date: "unknown"
event_date: "1982-07-18"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.racingsportscars.com/f1/entry/Brands_Hatch-1982-07-18.html"
access_date: "2026-08-10"
supports:
  - claim_id: "R10-PW-ENT-01"
    scope: "Zgłoszenia Brands Hatch: pary zespołów, Tambay #27 / Pironi #28, Mansell Lotus, Toleman Warwick/Fabi, Lammers Theodore, Jarier Osella, Ligier JS19/JS17, Fittipaldi F8/F9, Brabham BT50-BMW obu kierowców."
disagreement_notes: "Brak de Villoty na liście — spójne z AS-ROEBUCK wycofaniem; oficjalny telex FOCA nieobecny."
notes: "Rekonstrukcja entry; nie używać kolumn wyników."
```

```yaml
source_id: "WP-1982-GB-R"
title: "1982 British Grand Prix"
author_or_organisation: "Wikipedia (compilation; isolate pre-session facts)"
publication_date: "unknown"
event_date: "1982-07-18"
source_type: "SECONDARY"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://en.wikipedia.org/wiki/1982_British_Grand_Prix — Race details; Classification / Race; Championship standings after (cross-check only)"
access_date: "2026-08-10"
supports:
  - claim_id: "R10-PW-CIR-01"
    scope: "XXXV Marlboro British Grand Prix; Brands Hatch; 18 July 1982; course ~4.207 km / 2.614 mi; 76 laps / ~319.7 km."
  - claim_id: "R10-PO-CLS-01"
    scope: "Pełna tabela wyniku P1–P10 + DNF z okrążeniami i punktami; FL Henton 1:13.028 okr. 63; Lauda 1:35:33.812; Pironi +25.726."
  - claim_id: "R10-PO-PTS-01"
    scope: "Punkty rundy 9–6–4–3–2–1; top-5 mistrzostw Wiki (Pironi 35 — konflikt z archiwum)."
disagreement_notes: "Warwick «subsequently revealed» half-tank — kwarantanna (UNC-R10-PO-WAR-FUEL). Pironi 35 vs archiwum 34 (UNC-R10-PO-PIR-PTS)."
notes: "Izolować metadane wydarzenia/toru + klasyfikację Race; kwarantanna later Warwick note i foreshadowing."
```

```yaml
source_id: "MS-DB-1982-GB"
title: "1982 British Grand Prix — Motor Sport database"
author_or_organisation: "Motor Sport Magazine database"
publication_date: "unknown"
event_date: "1982-07-18"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/database/races/1982-british-grand-prix/"
access_date: "2026-08-10"
supports:
  - claim_id: "R10-PW-CIR-02"
    scope: "Potwierdzenie daty 18 July 1982, Brands Hatch / Fawkham Kent, nazwa Marlboro British Grand Prix, długość ~2.6136 mi."
disagreement_notes: "Lap record na stronie z 1986 — kwarantanna."
notes: "Używać tylko identyfikacji wydarzenia i długości układu."
```

```yaml
source_id: "GPCOM-1982-GB"
title: "British GP 1982 — grandprix.com race notes"
author_or_organisation: "grandprix.com"
publication_date: "unknown"
event_date: "1982-07-18"
source_type: "SECONDARY"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.grandprix.com/races/british-gp-1982.html"
access_date: "2026-08-10"
supports:
  - claim_id: "R10-PW-ENT-MAN"
    scope: "Mansell z powrotem w Lotusie po Holandii; Watson lider o punkt przed Pironim (linia wtórna); nowe podwozie Fittipaldi."
disagreement_notes: "Strona miesza preview z kwalifikacjami — izolować wyłącznie zdania przedsesyjne. Błędna kolejność Piquet/Patrese i atrybucja wypadku skrzydła de Cesarisowi vs Giacomelli (UNC-R10-PR-GRID-GPCOM, UNC-R10-PR-WING)."
notes: "Wsparcie wtórne; priorytet RSC + AS-ROEBUCK; nie używać kolejności grida z tej strony."
```

```yaml
source_id: "WP-1982-GB-Q"
title: "1982 British Grand Prix — Qualifying table"
author_or_organisation: "Wikipedia (compilation; isolate qualifying only)"
publication_date: "unknown"
event_date: "1982-07-16/1982-07-17"
source_type: "SECONDARY"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://en.wikipedia.org/wiki/1982_British_Grand_Prix — Classification / Qualifying"
access_date: "2026-08-10"
supports:
  - claim_id: "R10-PR-GRID-01"
    scope: "Pełna tabela najlepszych czasów P1–P26 + DNQ P27–P30 z Q1/Q2; litery opon G/M/P/A."
  - claim_id: "R10-PR-POLE-01"
    scope: "Pole Rosberg 1:09.540 (Q1); Patrese 1:09.627 (Q2); Piquet 1:10.060; Pironi 1:10.066."
disagreement_notes: "Guerrero 1:12.668 vs RSC 1:12.688 (UNC-R10-PR-GUE-TIME). Nie używać Race / Championship after."
notes: "Wtórna tabela; krzyżowy check z F1-GRID-1982 i narracją AS-ROEBUCK."
```

```yaml
source_id: "F1-GRID-1982"
title: "1982 British Grand Prix — Starting grid"
author_or_organisation: "formula1.com"
publication_date: "unknown"
event_date: "1982-07-18"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.formula1.com/en/results/1982/races/446/great-britain/starting-grid"
access_date: "2026-08-10"
supports:
  - claim_id: "R10-PR-GRID-02"
    scope: "Krzyżowy check kolejności i czasów P1–P26 (Rosberg–Baldi)."
disagreement_notes: "Etykiety silnika Brabham «Ford» błędne — ignorować string silnika; czasy zgodne z Wiki."
notes: "Używać tylko kolumn pozycji/czasu; nie importować wyniku."
```

```yaml
source_id: "RSC-1982-R10-RACE"
title: "GP Great Britain 1982 — race page (schedule / sessions)"
author_or_organisation: "Racing Sports Cars"
publication_date: "unknown"
event_date: "1982-07-18"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.racingsportscars.com/f1/race/Brands_Hatch-1982-07-18.html — Start time; Pre-race sessions"
access_date: "2026-08-10"
supports:
  - claim_id: "R10-PR-EVT-03"
    scope: "Start time 15:00 (wtórne); 2 non-Q practice 180 min; 2 Q 120 min; 30 min warm-up."
disagreement_notes: "Brak współczesnego potwierdzenia zegara programu (UNC-R10-PR-CLOCK)."
notes: "Izolować metadane sesji/zegara; kwarantanna wyniku i FL."
```

```yaml
source_id: "MSS-1982-GB-INFO"
title: "1982 British Grand Prix — schedule info"
author_or_organisation: "Motorsport Stats (secondary)"
publication_date: "unknown"
event_date: "1982-07-18"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "Motorsport Stats / related schedule fields citing 15:00 Brands Hatch 18 July 1982"
access_date: "2026-08-10"
supports:
  - claim_id: "R10-PR-EVT-03b"
    scope: "Wtórne potwierdzenie planowanego startu ok. 15:00."
disagreement_notes: "Jak RSC — nie zastępuje oficjalnego programu."
notes: "Kotwica zegara tylko wtórna; ledger gap 1982-R10-PR-CUT-01."
```

```yaml
source_id: "F1COM-1982-GB-RES"
title: "1982 British Grand Prix — Race result"
author_or_organisation: "formula1.com"
publication_date: "unknown"
event_date: "1982-07-18"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "none"
locator: "https://www.formula1.com/en/results/1982/races/446/great-britain/race-result"
access_date: "2026-08-10"
supports:
  - claim_id: "R10-PO-TIME-01"
    scope: "Lauda 1:35:33.812; kolejność P1–P10; punkty 9–6–4–3–2–1."
  - claim_id: "R10-PO-GAP-01"
    scope: "Pironi +25.730 s (0.004 vs Wiki 25.726 — UNC-R10-PO-GAP)."
disagreement_notes: "Zaokrąglenie gap vs Wiki; Alboreto DNC vs Ret Engine."
notes: "Krzyżowy check czasów; nie importować późniejszych rund z nawigacji."
```

```yaml
source_id: "RSC-1982-R10-RES"
title: "GP Great Britain 1982 — Race Results"
author_or_organisation: "Racing Sports Cars"
publication_date: "unknown"
event_date: "1982-07-18"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "none"
locator: "https://www.racingsportscars.com/f1/results/Brands_Hatch-1982-07-18.html"
access_date: "2026-08-10"
supports:
  - claim_id: "R10-PO-CLS-01"
    scope: "Kolejność finiszerów P1–P10; DNF z przyczynami (CV joint Warwick; metering unit pulley Piquet; fuel pressure Rosberg; electrics de Cesaris)."
  - claim_id: "R10-PO-BRAB-02"
    scope: "Piquet 9 okr. metering unit pulley; Patrese start accident hit by Arnoux."
disagreement_notes: "Okrążenia DNF często +1 vs Wiki (UNC-R10-PO-LAPN); Alboreto NC blank; Arnoux reason text duplicate typo on page."
notes: "Przyczyny DNF; nie używać jako jedynego źródła czasów (brak gap)."
```

```yaml
source_id: "ARCHIVE-R10-PW-STD"
title: "Klasyfikacja po Holandii — arytmetyka pre-weekend Brands Hatch"
author_or_organisation: "F1 Time Capsule archive (pre-weekend.md R10)"
publication_date: "not-applicable"
event_date: "1982-07-03"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/10-british-grand-prix/pre-weekend.md — Aktualna pozycja w mistrzostwach / przypis 3"
access_date: "2026-08-10"
supports:
  - claim_id: "R10-PO-STD-BASE"
    scope: "Baza po NL: Watson 30; Pironi 28; Rosberg 21; Patrese 19; Prost 18; Piquet 17; Lauda 15; McLaren 45; Brabham 36; Williams 32; Ferrari 34; Renault 22."
disagreement_notes: "Pironi 28 vs Wiki 29 (UNC-R10-PW-PIR-PTS)."
notes: "Baza standings-after po Brands; brak osobnego folderu NL."
```

```yaml
source_id: "MS-AUG1982-GB"
title: "British Grand Prix report — Motor Sport August 1982"
author_or_organisation: "Motor Sport (DSJ / race report)"
publication_date: "1982-08"
event_date: "1982-07-18"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/issues/august-1982/ — British GP article (full text not retrieved this session)"
access_date: "2026-08-10"
supports: []
disagreement_notes: null
notes: "Potwierdzone istnienie numeru sierpniowego; pełny tekst / RESULTS nie zmapowane — gap 1982-R10-PO-MS-01. Nie używać do claimów narracyjnych do czasu audytu."
```

## Conflict and uncertainty index

| Uncertainty ID | Claim IDs | Source IDs | Status at cutoff | Note |
| --- | --- | --- | --- | --- |
| UNC-R10-PW-PIR-PTS | R10-PW-STD-NL | ARCHIVE-R09-STAND, WP-1982-NL-R | open | Pironi 28 (archiwum 19+9) vs 29 (Wiki); Ferrari 34 vs 35 |
| UNC-R10-PW-CLOCK | R10-PW-EVT-02 | AS-ROEBUCK-GB1982 | open | Piątkowy poranek bez oficjalnego zegara programu |
| UNC-R10-PW-REFUEL | R10-PW-TEC-BRA | AS-ROEBUCK-GB1982 | open | Kiedy plan postoju Brabhama stał się w pełni publiczny vs dopiero przy sprzęcie w boksach |
| UNC-R10-PW-NL-FOLDER | R10-PW-DEV-NL-02 | CAL-01, UPI-1982-06-18-NL | open | Brak folderu rundy holenderskiej w archiwum sezonu |
| UNC-R10-PR-CLOCK | R10-PR-EVT-03 | RSC-1982-R10-RACE, MSS-1982-GB-INFO | open | Start 15:00 tylko wtórnie |
| UNC-R10-PR-GRID-GPCOM | R10-PR-GRID-01 | GPCOM-1982-GB vs AS-ROEBUCK / WP-1982-GB-Q | open | GP.com: Piquet przed Patrese — odrzucone |
| UNC-R10-PR-WING | R10-PR-SES-01 | GPCOM-1982-GB vs AS-ROEBUCK-GB1982 | open | GP.com: skrzydło de Cesaris; Roebuck: Giacomelli |
| UNC-R10-PR-GUE-TIME | R10-PR-GRID-01 | WP-1982-GB-Q / F1-GRID-1982 vs RSC | open | Guerrero 1:12.668 vs 1:12.688 |
| UNC-R10-PR-WU-TIME | R10-PR-WU-01 | AS-ROEBUCK-GB1982 | open | Brak pełnej tabeli czasów rozgrzewki |
| UNC-R10-PR-ROE-ENGINE | R10-PR-WU-01 | AS-ROEBUCK-GB1982 | open | Intro «blow» vs body wyskok biegu / 11300 — traktować jako jedną awarię |
| UNC-R10-PO-PIR-PTS | R10-PO-PTS-01 | ARCHIVE-R10-PW-STD, WP-1982-GB-R | open | Pironi 34 vs Wiki 35; Ferrari 44 vs 45 |
| UNC-R10-PO-GAP | R10-PO-GAP-01 | WP-1982-GB-R vs F1COM-1982-GB-RES vs AS | open | +25.726 vs +25.730; AS narracyjne 40s/15s |
| UNC-R10-PO-LAPN | R10-PO-CLS-01 | WP vs RSC/AS | open | Okrążenia DNF off-by-one |
| UNC-R10-PO-PIQ | R10-PO-BRAB-02 | AS vs RSC vs WP | open | pump belt vs metering pulley vs fuel system |
| UNC-R10-PO-ALB | R10-PO-CLS-01 | WP Engine vs RSC NC vs AS skirt | open | Przyczyna Alboreta |
| UNC-R10-PO-WAR-FUEL | R10-PO-WAR-01 | WP later note | quarantined | Later half-tank revelation — excluded |
| UNC-R10-PO-MS-GAP | — | MS-AUG1982-GB | open | Full MS Aug report not retrieved |
