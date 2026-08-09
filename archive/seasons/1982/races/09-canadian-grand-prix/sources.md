# Canadian Grand Prix — source ledger

To kanoniczny rejestr źródeł folderu rundy. Dokumenty treści cytują
`source_id` i `claim_id`; nie prowadzą konkurencyjnych list źródeł. Cutoff
rejestru obejmuje `pre-weekend.md`, `pre-race.md`, `post-race.md` i
`standings-after.md` (granica post-race: natychmiastowa procedura po
Grand Prix Kanady 1982, 13 VI — flaga, klasyfikacja, podium).

## Source entry

```yaml
source_id: "ARCHIVE-R08-STAND"
title: "Klasyfikacja po Grand Prix Detroit"
author_or_organisation: "F1 Time Capsule archive (standings-after.md R08)"
publication_date: "not-applicable"
event_date: "1982-06-06"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/08-detroit-grand-prix/standings-after.md"
access_date: "2026-08-09"
supports:
  - claim_id: "R09-PW-STD-01"
    scope: "Prowizoryczna kolejność i punkty po Detroit: Watson 26, Pironi 19, Prost 18, Rosberg 17, Patrese 13, Lauda 12, Cheever/Alboreto 10, Mansell/de Angelis 7, Reutemann/Villeneuve 6; McLaren 38, Williams 26, Ferrari 25, Renault 22, Brabham 15, Lotus 14, Talbot-Ligier 11, Tyrrell 10, Alfa 4, Osella 3, ATS 2, Fittipaldi 1; otwarte apelacje LB; skala prowizoryczna; konflikt Pironi 19 vs 20."
  - claim_id: "R09-PO-STD-01"
    scope: "Baza arytmetyki mistrzostw po Kanadzie = stany po Detroit + punkty R09; Pironi pozostaje 19 (nie Wiki 20)."
disagreement_notes: "Konflikt Pironi 19 vs UPI-base 20 (UNC-R07-PO-PIR-PTS / UNC-R09-PO-PIR-PTS); brak oficjalnego biuletynu FIA."
notes: "Baza przed Montrealem i baza post-race; nie kopiować pełnych tabel do narracji."
```

```yaml
source_id: "ARCHIVE-R08-PW"
title: "Grand Prix Detroit — przed weekendem (obsada przyjazdu)"
author_or_organisation: "F1 Time Capsule archive (pre-weekend.md R08)"
publication_date: "not-applicable"
event_date: "1982-06-04/1982-06-06"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/08-detroit-grand-prix/pre-weekend.md"
access_date: "2026-08-09"
supports:
  - claim_id: "R09-PW-ENT-BASE"
    scope: "Baza obsady Detroit: Pironi-only Ferrari; Toleman DNA w Detroit; Lammers Theodore; pary głównych zespołów; Ligier JS17; Ferrari pull-rod 126C2."
  - claim_id: "R09-PW-TEC-580"
    scope: "Reguła minimum 580 kg bez dolewania płynów przed ważeniem — carry-forward z Detroit PW."
  - claim_id: "R09-PW-EXP-WINNERS"
    scope: "Narracja pięciu różnych zwycięzców w punktowanych rundach — carry-forward z Detroit PW."
disagreement_notes: null
notes: "Carry-forward personalny i regulaminowy; weryfikować obsadę względem MS/RSC Montreal."
```

```yaml
source_id: "ARCHIVE-R08-PR"
title: "Grand Prix Detroit — przed startem (kontuzja Lammersa)"
author_or_organisation: "F1 Time Capsule archive (pre-race.md R08)"
publication_date: "not-applicable"
event_date: "1982-06-04/1982-06-06"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/08-detroit-grand-prix/pre-race.md"
access_date: "2026-08-09"
supports:
  - claim_id: "R09-PW-ENT-THEO-01"
    scope: "Lammers złamał kciuk w piątkowym treningu Detroit; bez czasu kwalifikacyjnego — kontekst zastępstwa w Montrealu."
disagreement_notes: null
notes: "Używane tylko jako fakt sprzed weekendu montrealskiego."
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
  - claim_id: "R09-PW-DATE-02"
    scope: "Canadian GP Montreal 12/13 June 1982 — konflikt tabeli (sobota 12) vs prozy (13 czerwca); przesunięcie Kanady na czerwiec."
disagreement_notes: "1982-CAL-02; operacyjna data rundy 13 VI z MS-JUL1982-CAN."
notes: "publication_date dnia unknown; content-based availability. Już w season/calendar.md."
```

```yaml
source_id: "MS-JAN1982-CAL"
title: "The 1982 International Racing Season (alias CAL-01)"
author_or_organisation: "Motor Sport"
publication_date: "1982-01"
event_date: "not-applicable"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/january-1982/35/the-1982-international-racing-season/"
access_date: "2026-08-09"
supports:
  - claim_id: "R09-PW-MOVE-01"
    scope: "Kanada próbowała czerwca zamiast jesieni ze względu na pogodę."
disagreement_notes: null
notes: "Alias/cross-ref do CAL-01 dla claimów organizacyjnych."
```

```yaml
source_id: "MTL-TOPO-CGV"
title: "circuit Gilles-Villeneuve — toponymie Ville de Montréal"
author_or_organisation: "Ville de Montréal (Répertoire historique / toponymy)"
publication_date: "1995"
event_date: "1982-05-14"
source_type: "ARCHIVE"
contemporary: false
spoiler_risk: "none"
locator: "https://montreal.ca/toponymie/toponymes/circuit-gilles-villeneuve — Date de désignation: 14 mai 1982"
access_date: "2026-08-09"
supports:
  - claim_id: "R09-PW-NAME-01"
    scope: "Oficjalna desygnacja nazwy circuit Gilles-Villeneuve / Circuit Gilles Villeneuve: 14 maja 1982 — przed weekendem GP Kanady."
disagreement_notes: null
notes: "Źródło wtórne/katalogowe względem daty desygnacji; treść biograficzna Villeneuve’a nie używana poza faktem nazwy. Zmiana generycznego «piste»→«circuit» w 1991 poza zakresem."
```

```yaml
source_id: "UPI-1982-05-09-VIL"
title: "Seville Villeneuve decided to stop answering the telephone Sunday..."
author_or_organisation: "UPI"
publication_date: "1982-05-09"
event_date: "1982-05-08/1982-05-09"
source_type: "PRESS"
contemporary: true
spoiler_risk: "none"
locator: "https://www.upi.com/Archives/1982/05/09/Seville-Villeneuve-decided-to-stop-answering-the-telephone-Sunday/2077389764800/"
access_date: "2026-08-09"
supports:
  - claim_id: "R09-PW-NAME-02"
    scope: "Petycja montrealskiej stacji FR o zmianę nazwy Île Notre-Dame; Houston Group omawiała upamiętnienie przy czerwcowym GP; Jacques Villeneuve kontynuuje karierę (nie jako starter F1 Montreal 1982)."
disagreement_notes: "Petycja = wyspa; oficjalna nazwa toru osobno (MTL-TOPO-CGV)."
notes: "Kontekst majowy; bez weekendu montrealskiego."
```

```yaml
source_id: "MS-1981-CAN"
title: "1981 Canadian Grand Prix — circuit briefing / database"
author_or_organisation: "Motor Sport"
publication_date: "1981-09/unknown"
event_date: "1981-09-27"
source_type: "PRESS"
contemporary: true
spoiler_risk: "none"
locator: "https://www.motorsportmagazine.com/database/races/1981-canadian-grand-prix/ — circuit description; length 2.74 miles"
access_date: "2026-08-09"
supports:
  - claim_id: "R09-PW-CIR-01"
    scope: "Charakter układu Île Notre-Dame: drogi serwisowe terenów wystawowych, płaski, dwa hairpiny, esy/chikany, wydłużona esa przez niewidoczny garb za boksami; Labatt; francuskojęzyczny Montreal."
  - claim_id: "R09-PW-CIR-02"
    scope: "Historyczna długość układu ~2.74 miles."
disagreement_notes: null
notes: "Prior-year briefing; ignorować rekord 1986 i inne późniejsze pola bazy. publication_date dnia unknown dla numeru MS."
```

```yaml
source_id: "MS-JUL1982-CAN"
title: "Canadian Grand Prix — Triumph and Tragedy"
author_or_organisation: "Motor Sport"
publication_date: "1982-07"
event_date: "1982-06-13"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/july-1982/48/canadian-grand-prix-14/"
access_date: "2026-08-09"
supports:
  - claim_id: "R09-PW-DATE-01"
    scope: "Dateline Montreal, June 13th — operacyjna data wyścigu niedziela 13 VI 1982."
  - claim_id: "R09-PW-CUT-01"
    scope: "Pierwsza oficjalna jazda: practise due on Friday morning; transportery 580 mil Detroit→Montreal; ekipy w dobrej formie po naprawach."
  - claim_id: "R09-PW-MOVE-01"
    scope: "Kanada przeniesiona na czerwiec i ustawiona po Detroit; piąty rok GP Kanady na wyspie."
  - claim_id: "R09-PW-WX-01"
    scope: "Trzy dni fali upałów w Montrealu przed piątkowym treningiem."
  - claim_id: "R09-PW-ENT-FER-01"
    scope: "Ferrari: Pironi; sprzęt 126C2 z nowym zawieszeniem przednim przy przyjeździe; Pironi not bothering with older type."
  - claim_id: "R09-PW-ENT-TOL-01"
    scope: "Toleman never did appear, in spite of all the promises in Detroit."
  - claim_id: "R09-PW-ENT-THEO-01"
    scope: "Lammers w Montrealu z kciukiem w gipsie; Geoff Lees sprowadzony; Theodore bedding-in new car po Detroit."
  - claim_id: "R09-PW-ENT-ATS-01"
    scope: "ATS overnight rebuild monocoque dla Winkelhocka przed Montrealem."
  - claim_id: "R09-PW-ENT-BRAB-01"
    scope: "Brabham brand new BT49D dla Patrese po Detroit; kontynuacja BMW BT50."
  - claim_id: "R09-PW-ENT-MCL-01"
    scope: "McLaren: Watson ten sam samochód; Lauda przejmuje T-car z Detroit (MP4/6)."
  - claim_id: "R09-PW-ENT-LIG-01"
    scope: "Talbot/Ligier abandoned JS19; Laffite/Cheever in the old cars — model JS17 via DET carry-forward, not named in CAN text."
  - claim_id: "R09-PW-FMT-01"
    scope: "Format: piątkowy poranek practice; późniejsza qualifying hour (plan); sobota; niedziela — bez wyników."
  - claim_id: "R09-PR-CUT-01"
    scope: "Warm-up 1.15 p.m.; race due 4.15 p.m. (TV); Sunday grey/cold west wind before start."
  - claim_id: "R09-PR-FRI-01"
    scope: "Friday rain; Arnoux–Winkelhock collision; wet Q; Rosberg/de Cesaris pace; Winkelhock no Friday Q."
  - claim_id: "R09-PR-SAT-01"
    scope: "Hot Saturday; Williams engine failures; Rosberg T-car Q; de Cesaris crashed tyre/kerb; Pironi 1:27.509 / 1:27.805; Arnoux 1:27.895; order Ferrari–Renault–Renault–BMW–Alfa–Cosworths."
  - claim_id: "R09-PR-POLE-01"
    scope: "Pironi pole 1:27.509 never beaten; consecutive 1:27.805."
  - claim_id: "R09-PR-DNQ-01"
    scope: "DNQ Winkelhock (car mid Saturday Q), Villota, Serra (car died early Sat); Toleman DNA."
  - claim_id: "R09-PR-WX-01"
    scope: "Sunday greyness/cold wind; Metro strike; organisers ~100 buses free transport — pre-start."
  - claim_id: "R09-PR-WU-01"
    scope: "Warm-up troubles: Giacomelli electrical; Henton gearbox; Guerrero driveshaft; Rosberg races T-car."
  - claim_id: "R09-PO-CUT-01"
    scope: "Post-race clocks: start due 4.15; restart ready after 6.15; finish few minutes after 8 p.m.; 70 laps / 4.41 km / 308.7 km."
  - claim_id: "R09-PO-START-01"
    scope: "First start: long light; Pironi clutch drag/stall; ~5.5 s red-to-green; field dodges; Boesel/Salazar/Lees melee."
  - claim_id: "R09-PO-PAL-01"
    scope: "Paletti Osella hits Ferrari rear ~100 mph; fatal injuries; helicopter; death same day (on-spot vs after hospital wording)."
  - claim_id: "R09-PO-RF-01"
    scope: "Red flag; ~2 h delay; 23-car restart; Osella/Theodore withdraw; Boesel spare; Salazar Winkelhock car; Pironi 059."
  - claim_id: "R09-PO-RACE-01"
    scope: "Restart race phases: Arnoux lead; Piquet lap 9; Brabham 1–2; Renault outs; fuel drama; FL Pironi lap 66."
  - claim_id: "R09-PO-DIST-01"
    scope: "70 laps, 4.41 km/lap, 308.7 km; winner time 1:46:39.577 / 173.7 km/h."
  - claim_id: "R09-PO-POD-01"
    scope: "Podium Piquet–Patrese–Watson; Seville Villeneuve holds winners trophy (MS caption)."
  - claim_id: "R09-PO-CLS-01"
    scope: "RESULTS order P1–P12/MS finishers + retirements/DNS list; times top 3."
  - claim_id: "R09-PO-FL-01"
    scope: "Fastest lap Pironi 1:28.323 lap 66."
  - claim_id: "R09-PO-PTS-01"
    scope: "Round points order supports 9-6-4-3-2-1 to Piquet–Patrese–Watson–de Angelis–Surer–de Cesaris."
  - claim_id: "R09-PO-RET-01"
    scope: "Then-known retirement causes and lap numbers in MS RESULTS/narrative."
disagreement_notes: "For pre-weekend/pre-race: isolate arrival/sessions/grid/WU; for post-race: use Race + RESULTS; quarantine later-issue contamination and season retrospectives. Henton P12 vs Wiki/RSC NC (UNC-R09-PO-HENTON). Lap-count MS vs Wiki (UNC-R09-PO-LAPN)."
notes: "CBA: pasaże przyjazdu (PW); sesje/pole/WU (PR); Race+RESULTS (PO). publication_date dnia unknown."
```

```yaml
source_id: "AS-ROEBUCK-CAN1982"
title: "Grand Prix Gold: 1982 Canadian GP (Nigel Roebuck contemporary report reprint)"
author_or_organisation: "Autosport / Nigel Roebuck"
publication_date: "unknown (event-week contemporary; web reprint 2012-08-16)"
event_date: "1982-06-11/1982-06-13"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.autosport.com/f1/news/grand-prix-gold-1982-canadian-gp-5098985/5098985/"
access_date: "2026-08-09"
supports:
  - claim_id: "R09-PR-CUT-01"
    scope: "Warm-up morning; race due 4.15 (TV); Sunday grey/misty/chilly before start."
  - claim_id: "R09-PR-FRI-01"
    scope: "Friday untimed then timed Q in rain; Arnoux–Winkelhock damage; de Cesaris/Rosberg wet pace; Mansell tyre-window quote."
  - claim_id: "R09-PR-SAT-01"
    scope: "Hot Saturday; Rosberg morning 1:28.22 then T-car; Daly engine change; de Cesaris monocoque write-off; Pironi pole quotes/dedication; Arnoux porpoising; speed traps; Cheever pit-exit near-miss."
  - claim_id: "R09-PR-TYRE-01"
    scope: "Goodyear C vs E; Michelin soft Friday; Pirelli narrower race tyre faster than Q tyres for most; Rosberg E-compound quote."
  - claim_id: "R09-PR-WX-01"
    scope: "Saturday evening forecast cloudy/showers; Metro strike known pre-start; organisers commandeering coaches."
  - claim_id: "R09-PR-WU-01"
    scope: "Warm-up: Brabhams quickest; Henton pinion/crownwheel; Jarier engine; Guerrero driveshaft; Surer exhaust; Giacomelli fuel starvation; cool wind favours turbos (paddock observation)."
  - claim_id: "R09-PR-WATCH-01"
    scope: "Attributed paddock interest: Pironi favourite; turbo front; Watson balance quote; turbo-grid Sunday question."
  - claim_id: "R09-PO-START-01"
    scope: "First start texture: Pironi arm up; Daly/Mansell dodge quotes; Boesel clips Ferrari; Paletti impact >100 mph."
  - claim_id: "R09-PO-PAL-01"
    scope: "Fire ~45 s after impact; extrication ~28 min; helicopter; died ~2 h later of massive internal injuries (AS wording)."
  - claim_id: "R09-PO-RF-01"
    scope: "Restart 6.15; Enzo Osella withdraws Jarier; Theodore no spare; Pironi spare courage note (author)."
  - claim_id: "R09-PO-RACE-01"
    scope: "Race phases, Patrese climb, fuel outs Cheever/de Cesaris/Daly, Surer seven cylinders."
  - claim_id: "R09-PO-QTE-01"
    scope: "Attributed quotes: Daly start; Mansell Giacomelli/arm; Piquet boost/mixture; Watson third-bonus; fuel reactions."
  - claim_id: "R09-PO-MAN-01"
    scope: "Mansell left-arm injury; track hospital; possible lengthy absence (contemporary speculation)."
  - claim_id: "R09-PO-RET-01"
    scope: "Retirement causes per AS (Laffite handling; Alboreto engine+gearbox; Guerrero clutch)."
disagreement_notes: "Quarantine 2012 packaging, Previous/Next Gold nav (Dutch etc.), «only win of season» framing if present in wrappers. publication_date of original Autosport issue unknown. Laffite/Alboreto cause conflicts vs MS."
notes: "CBA: Entry/Practice/WU (PR); The Grand Prix body (PO). Prefer with MS for times/RESULTS."
```
```yaml
source_id: "WP-1982-CAN-Q"
title: "1982 Canadian Grand Prix — Qualifying table"
author_or_organisation: "Wikipedia (secondary compilation)"
publication_date: "unknown"
event_date: "1982-06-11/1982-06-12"
source_type: "SECONDARY"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://en.wikipedia.org/wiki/1982_Canadian_Grand_Prix — Classification/Qualifying"
access_date: "2026-08-09"
supports:
  - claim_id: "R09-PR-GRID-01"
    scope: "Structured Q1/Q2 best times P1–P26 and DNQ rows (Winkelhock/de Villota/Serra)."
  - claim_id: "R09-PR-POLE-01"
    scope: "Cross-check Pironi 1:27.509 pole."
disagreement_notes: "Living page; Round numbering as Race 8 vs archive round 09. Quarantine Race / Death of Paletti / standings-after-race sections. Boesel 1:31.759 preferred over RSC 1:31.901 conflict (UNC-R09-PR-BOESEL)."
notes: "Secondary cross-check for structured grid only; prefer MS/AS narrative for session story."
```

```yaml
source_id: "RSC-1982-R09-GRID"
title: "Labatt Canadian Grand Prix 1982 — grid reconstruction"
author_or_organisation: "Racing Sports Cars / database"
publication_date: "unknown"
event_date: "1982-06-13"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.racingsportscars.com/f1/photo/Montreal-1982-06-13.html?sort=Grid"
access_date: "2026-08-09"
supports:
  - claim_id: "R09-PR-GRID-01"
    scope: "Secondary grid times/chassis/tyre columns; strip Result fields."
disagreement_notes: "Boesel time conflict vs WP-1982-CAN-Q (UNC-R09-PR-BOESEL)."
notes: "Alias/extension of RSC-1982-R09-ENT page; use only for structured pre-start identity, not race."
```

```yaml
source_id: "MS-JUL1982-DET"
title: "The Grand Prix of Detroit"
author_or_organisation: "Motor Sport"
publication_date: "1982-07"
event_date: "1982-06-06"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/july-1982/43/the-grand-prix-of-detroit/"
access_date: "2026-08-09"
supports:
  - claim_id: "R09-PW-ENT-TOL-CTX"
    scope: "Kontekst DNA Tolemana w Detroit (transporter) — tło «promises in Detroit»."
  - claim_id: "R09-PW-ENT-THEO-01"
    scope: "Kontuzja/wypadek Lammersa w Detroit jako tło zastępstwa."
  - claim_id: "R09-PW-ENT-FER-PULL"
    scope: "Ferrari 126C2 z nowym przednim zawieszeniem pull-rod w dyspozycji przy Detroit — carry-forward identyfikacji pull-rod do Montrealu."
  - claim_id: "R09-PW-ENT-LIG-01"
    scope: "Ligier/Talbot na JS17 jako autach wyścigowych (JS19 zapas) przy Detroit — carry-forward modelu «old cars» z CAN."
disagreement_notes: null
notes: "Używane tylko jako kontekst przed Montrealem; nie importować wyników Detroit poza ARCHIVE-R08-STAND."
```

```yaml
source_id: "RSC-1982-R09-ENT"
title: "Labatt Canadian Grand Prix 1982 — entry reconstruction"
author_or_organisation: "Racing Sports Cars / database"
publication_date: "unknown"
event_date: "1982-06-13"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.racingsportscars.com/f1/photo/Montreal-1982-06-13.html?sort=Grid"
access_date: "2026-08-09"
supports:
  - claim_id: "R09-PW-ENT-FIELD-01"
    scope: "Rekonstrukcja nazwisk obsady / DNA Toleman 35–36 / Lees–Theodore; izolować od kolumn Grid/Results."
disagreement_notes: "Nieoficjalna baza; stripować Q/race."
notes: "Tylko lista przyjazdu/zgłoszeń; spoiler_risk wysoki na stronie."
```

```yaml
source_id: "WP-1982-CAN-R"
title: "1982 Canadian Grand Prix — Race classification"
author_or_organisation: "Wikipedia (secondary compilation)"
publication_date: "unknown"
event_date: "1982-06-13"
source_type: "SECONDARY"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://en.wikipedia.org/wiki/1982_Canadian_Grand_Prix — Classification/Race"
access_date: "2026-08-09"
supports:
  - claim_id: "R09-PO-CLS-01"
    scope: "Structured race table P1–P11, NC Henton 59 laps, retirements/DNS rows, points column."
  - claim_id: "R09-PO-FL-01"
    scope: "Cross-check FL Pironi 1:28.323 lap 66."
  - claim_id: "R09-PO-DIST-01"
    scope: "Cross-check 70 laps / 4.410 km / 308.700 km."
  - claim_id: "R09-PO-PTS-01"
    scope: "Points 9-6-4-3-2-1 column for top six."
disagreement_notes: "Living page; Round as Race 8 vs archive 09. Quarantine Death of Paletti retrospectives (later fatalities, autopsy detail, mother/birthday unless same-day wire added). Quarantine championship tables Pironi 20 / Brabham-Ford split (UNC-R09-PO-PIR-PTS, UNC-R09-PO-BRAB-WIKI). Henton NC vs MS P12."
notes: "Secondary cross-check only; prefer MS times and AS narrative."
```

```yaml
source_id: "RSC-1982-R09-RES"
title: "Labatt Canadian Grand Prix 1982 — results reconstruction"
author_or_organisation: "Racing Sports Cars / database"
publication_date: "unknown"
event_date: "1982-06-13"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.racingsportscars.com/f1/photo/Montreal-1982-06-13.html?sort=Results"
access_date: "2026-08-09"
supports:
  - claim_id: "R09-PO-CLS-01"
    scope: "Structured results; Classified 11 (Henton NC); retirement cause fields as secondary."
disagreement_notes: "Cause strings sometimes disagree with MS/AS (Guerrero engine; Laffite engine). Classified 11 vs MS 12 finishers."
notes: "Use for classification structure only; prefer MS/AS for narrative causes."
```

## Conflict and uncertainty index

| Uncertainty ID | Claim IDs | Source IDs | Status at cutoff | Note |
| --- | --- | --- | --- | --- |
| UNC-R09-DATE | R09-PW-DATE-01, R09-PW-DATE-02 | CAL-01, MS-JUL1982-CAN | open | Przedsezon 12 vs 13 VI; operacyjnie 13 VI |
| UNC-R09-CLOCK | R09-PW-CUT-01, R09-PW-FMT-01 | MS-JUL1982-CAN | open | „Friday morning” bez zegara programu |
| UNC-R09-TAMBAY | R09-PW-ENT-FER-01 | MS-JUL1982-CAN, ARCHIVE-R08-PW | open | Pironi-only potwierdzony; data komunikatu Tambay nieprzyjęta |
| UNC-R09-PIRONI-PTS | R09-PW-STD-01, R09-PO-STD-01 | ARCHIVE-R08-STAND, WP-1982-CAN-R | open | Carry-forward 19 vs 20; Wiki post-race 20 |
| UNC-R09-LEN | R09-PW-CIR-02 | MS-1981-CAN, MS-JUL1982-CAN | open | Długość z prior-year / nagłówka MS; brak programu 1982 |
| UNC-R09-WX-FCST | R09-PW-WX-01 | MS-JUL1982-CAN | open | Upał przed piątkiem OK; brak datowanej prognozy weekendu |
| UNC-R09-ENT-OFF | R09-PW-ENT-FIELD-01 | RSC-1982-R09-ENT | open | Brak oficjalnego telexu FOCA/FISA |
| UNC-R09-PR-CLOCK | R09-PR-CUT-01 | MS-JUL1982-CAN, AS-ROEBUCK-CAN1982 | open | 16:15 / 13:15 z prasy TV, nie z oficjalnego programu |
| UNC-R09-PR-GRID-OFF | R09-PR-GRID-01 | WP-1982-CAN-Q, RSC-1982-R09-GRID, MS-JUL1982-CAN | open | Brak biuletynu FIA timing; Wiki/RSC wtórne |
| UNC-R09-PR-BOESEL | R09-PR-GRID-01 | WP-1982-CAN-Q, RSC-1982-R09-GRID | open | Boesel 1:31.759 (Wiki) vs 1:31.901 (RSC=Paletti); przyjęto Wiki |
| UNC-R09-PR-GIAC-WU | R09-PR-WU-01 | MS-JUL1982-CAN, AS-ROEBUCK-CAN1982 | open | MS electrical vs Autosport fuel starvation |
| UNC-R09-PR-HENTON-WU | R09-PR-WU-01 | MS-JUL1982-CAN, AS-ROEBUCK-CAN1982 | open | MS gearbox vs AS pinion/crownwheel — zgodne mechanicznie |
| UNC-R09-PO-HENTON | R09-PO-CLS-01 | MS-JUL1982-CAN, WP-1982-CAN-R, RSC-1982-R09-RES | open | MS P12 / 12 finishers vs Wiki+RSC NC 59 laps |
| UNC-R09-PO-LAPN | R09-PO-RET-01 | MS-JUL1982-CAN, WP-1982-CAN-R | open | MS „on lap N” vs Wiki completed N−1 |
| UNC-R09-PO-ALB-CAUSE | R09-PO-RET-01 | MS-JUL1982-CAN, AS-ROEBUCK-CAN1982, WP-1982-CAN-R | open | gearbox vs engine vs both |
| UNC-R09-PO-LAF-CAUSE | R09-PO-RET-01 | MS-JUL1982-CAN, AS-ROEBUCK-CAN1982, RSC-1982-R09-RES | open | fuel pump vs handling vs engine |
| UNC-R09-PO-GUE-CAUSE | R09-PO-RET-01 | MS-JUL1982-CAN, AS-ROEBUCK-CAN1982, RSC-1982-R09-RES | open | clutch vs engine |
| UNC-R09-PO-PAL-TIME | R09-PO-PAL-01 | MS-JUL1982-CAN, AS-ROEBUCK-CAN1982 | open | on-spot vs ~2 h later / after hospital |
| UNC-R09-PO-PIR-PTS | R09-PO-STD-01 | ARCHIVE-R08-STAND, WP-1982-CAN-R | open | archive 19 vs Wiki 20 |
| UNC-R09-PO-BRAB-WIKI | R09-PO-STD-01 | WP-1982-CAN-R | open | Wiki splits Brabham-Ford; archive single Brabham 30 |
| UNC-R09-PO-SCRUT | R09-PO-CLS-01 | MS-JUL1982-CAN, AS-ROEBUCK-CAN1982 | open | brak same-day weight check w dostępnych relacjach CAN |

## Claim map (pre-weekend)

| Claim ID | Short label | Primary sources |
| --- | --- | --- |
| `R09-PW-STD-01` | Standings after Detroit | `ARCHIVE-R08-STAND` |
| `R09-PW-DATE-01` | Operative race date 13 VI | `MS-JUL1982-CAN` |
| `R09-PW-DATE-02` | Calendar 12/13 conflict | `CAL-01` |
| `R09-PW-CUT-01` | Friday morning first session | `MS-JUL1982-CAN` |
| `R09-PW-MOVE-01` | June move / after Detroit | `MS-JUL1982-CAN`, `MS-JAN1982-CAL` |
| `R09-PW-WX-01` | Pre-Friday heatwave | `MS-JUL1982-CAN` |
| `R09-PW-NAME-01` | Circuit name 14 V | `MTL-TOPO-CGV` |
| `R09-PW-NAME-02` | Island petition / memorial talk | `UPI-1982-05-09-VIL` |
| `R09-PW-ENT-FER-01` | Pironi-only Ferrari arrival | `MS-JUL1982-CAN` |
| `R09-PW-ENT-TOL-01` | Toleman DNA | `MS-JUL1982-CAN` |
| `R09-PW-ENT-THEO-01` | Lees for Lammers | `MS-JUL1982-CAN`, `ARCHIVE-R08-PR` |
| `R09-PW-ENT-FIELD-01` | Entry reconstruction | `RSC-1982-R09-ENT` |
| `R09-PW-CIR-01` | Circuit character | `MS-1981-CAN` |
| `R09-PW-FMT-01` | Weekend format plan | `MS-JUL1982-CAN` |

## Claim map (pre-race)

| Claim ID | Short label | Primary sources |
| --- | --- | --- |
| `R09-PR-CUT-01` | Start / warm-up clock | `MS-JUL1982-CAN`, `AS-ROEBUCK-CAN1982` |
| `R09-PR-FRI-01` | Friday practice/Q wet | `MS-JUL1982-CAN`, `AS-ROEBUCK-CAN1982` |
| `R09-PR-SAT-01` | Saturday sessions / pole story | `MS-JUL1982-CAN`, `AS-ROEBUCK-CAN1982` |
| `R09-PR-POLE-01` | Pironi 1:27.509 | `MS-JUL1982-CAN`, `WP-1982-CAN-Q` |
| `R09-PR-GRID-01` | Grid P1–P26 + DNQ times | `WP-1982-CAN-Q`, `MS-JUL1982-CAN`, `RSC-1982-R09-GRID` |
| `R09-PR-DNQ-01` | DNQ / Toleman DNA | `MS-JUL1982-CAN` |
| `R09-PR-TYRE-01` | Compounds / Pirelli note | `AS-ROEBUCK-CAN1982` |
| `R09-PR-WX-01` | Sunday pre-start weather / metro | `MS-JUL1982-CAN`, `AS-ROEBUCK-CAN1982` |
| `R09-PR-WU-01` | Sunday warm-up | `MS-JUL1982-CAN`, `AS-ROEBUCK-CAN1982` |
| `R09-PR-WATCH-01` | Attributed pre-start interest | `AS-ROEBUCK-CAN1982`, `MS-JUL1982-CAN` |
| `R09-PR-STD-01` | Standings carry-forward | `ARCHIVE-R08-STAND` |

## Claim map (post-race)

| Claim ID | Short label | Primary sources |
| --- | --- | --- |
| `R09-PO-CUT-01` | Post-race cutoff / clocks | `MS-JUL1982-CAN`, `AS-ROEBUCK-CAN1982` |
| `R09-PO-START-01` | First start / Pironi stall | `MS-JUL1982-CAN`, `AS-ROEBUCK-CAN1982` |
| `R09-PO-PAL-01` | Paletti fatal accident same day | `MS-JUL1982-CAN`, `AS-ROEBUCK-CAN1982` |
| `R09-PO-RF-01` | Red flag / restart field | `MS-JUL1982-CAN`, `AS-ROEBUCK-CAN1982` |
| `R09-PO-RACE-01` | Race phases after restart | `MS-JUL1982-CAN`, `AS-ROEBUCK-CAN1982` |
| `R09-PO-DIST-01` | 70 laps / 308.7 km | `MS-JUL1982-CAN`, `WP-1982-CAN-R` |
| `R09-PO-POD-01` | Podium / Seville trophy | `MS-JUL1982-CAN` |
| `R09-PO-CLS-01` | Classification | `MS-JUL1982-CAN`, `WP-1982-CAN-R`, `RSC-1982-R09-RES` |
| `R09-PO-FL-01` | Fastest lap Pironi | `MS-JUL1982-CAN`, `WP-1982-CAN-R` |
| `R09-PO-PTS-01` | Round points 9–6–4–3–2–1 | `MS-JUL1982-CAN`, `WP-1982-CAN-R` |
| `R09-PO-STD-01` | Standings after Canada | `ARCHIVE-R08-STAND` + `R09-PO-PTS-01` |
| `R09-PO-RET-01` | Retirement causes | `MS-JUL1982-CAN`, `AS-ROEBUCK-CAN1982` |
| `R09-PO-QTE-01` | Attributed quotes | `AS-ROEBUCK-CAN1982` |
| `R09-PO-MAN-01` | Mansell arm injury same-day | `AS-ROEBUCK-CAN1982` |
