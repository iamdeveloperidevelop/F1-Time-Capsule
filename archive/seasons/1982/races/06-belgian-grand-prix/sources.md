# Belgian Grand Prix — source ledger

To kanoniczny rejestr źródeł folderu rundy. Dokumenty treści cytują
`source_id` i `claim_id`; nie prowadzą konkurencyjnych list źródeł. Cutoff
rejestru obejmuje `pre-weekend.md`, `pre-race.md`, `post-race.md` oraz
`standings-after.md` (natychmiastowa procedura post-race 9 V 1982, w tym
ważenie i DSQ Laudy).

## Source entry

```yaml
source_id: "ARCHIVE-R05-STAND"
title: "Klasyfikacja po Grand Prix San Marino"
author_or_organisation: "F1 Time Capsule archive (standings-after.md R05)"
publication_date: "not-applicable"
event_date: "1982-04-25/1982-04-26"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/05-san-marino-grand-prix/standings-after.md"
access_date: "2026-08-06"
supports:
  - claim_id: "R06-PW-STD-01"
    scope: "Prowizoryczna kolejność i punkty po Imoli z DSQ Winkelhocka (26 IV): Prost 18, Lauda 12, Alboreto 10, Pironi 9, Rosberg/Watson 8, Reutemann/Villeneuve 6, Arnoux/Patrese/Mansell 4, Jarier 3, Salazar/de Angelis 2; Renault 22, McLaren 20, Ferrari 15, Williams 14, Tyrrell 10, Lotus 6, Brabham 4, Osella 3, ATS 2; otwarte apelacje LB; Fabi NC."
disagreement_notes: "Skala punktowa prowizoryczna; brak oficjalnego biuletynu FIA w pakiecie R05."
notes: "Baza przed Zolderem; nie kopiować pełnych tabel do narracji."
```

```yaml
source_id: "ARCHIVE-R04-STAND"
title: "Klasyfikacja po Grand Prix Stanów Zjednoczonych Zachód"
author_or_organisation: "F1 Time Capsule archive (standings-after.md R04)"
publication_date: "not-applicable"
event_date: "1982-04-04/1982-04-05"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/04-united-states-grand-prix-west/standings-after.md"
access_date: "2026-08-06"
supports:
  - claim_id: "R06-PW-LB-APP-01"
    scope: "Status otwartych apelacji po Long Beach (DSQ Villeneuve twin-wing; protest Ferrari; grzywna de Angelisa) przeniesiony bez nowych rozstrzygnięć przed Zolderem."
disagreement_notes: null
notes: "Carry-forward; brak nowej depeszy ≤ cutoff R06-PW."
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
access_date: "2026-08-06"
supports:
  - claim_id: "R06-PW-CAL-01"
    scope: "Belgian Grand Prix — Zolder — 9 May 1982 na liście kalendarza FIA."
disagreement_notes: null
notes: "publication_date dnia unknown; content-based availability jako przedsezonowa reprodukcja. Już w season/calendar.md."
```

```yaml
source_id: "UPI-1982-04-22-SM"
title: "The controversy-plagued San Marino Formula One Grand Prix race..."
author_or_organisation: "UPI"
publication_date: "1982-04-22"
event_date: "1982-04-22"
source_type: "PRESS"
contemporary: true
spoiler_risk: "none"
locator: "https://www.upi.com/Archives/1982/04/22/The-controversy-plagued-San-Marino-Formula-One-Grand-Prix-race/6164388299600/"
access_date: "2026-08-06"
supports:
  - claim_id: "R06-PW-WT-01"
    scope: "Trybunał FISA unieważniający 1. Piqueta i 2. Rosberga w Rio (580 kg); oświadczenie bojkotu FOCA wobec Imoli jako tło powrotu peletonu do Belgii."
disagreement_notes: null
notes: "Tło polityczne; powrót FOCA do Zolderu potwierdzają MS June, nie ta depesza."
```

```yaml
source_id: "MS-MAY1982-SCENE"
title: "The Formula One Scene"
author_or_organisation: "D.S.J., Motor Sport"
publication_date: "1982-05"
event_date: "not-applicable"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/may-1982/45/formula-one-scene/"
access_date: "2026-08-06"
supports:
  - claim_id: "R06-PW-WT-01"
    scope: "Po Paryżu: dolewanie nielegalne; samochody muszą jeździć ≥580 kg; DSQ Piqueta/Rosberga w Brazylii; Cosworthe z balastem."
disagreement_notes: null
notes: "Dzień miesiąca unknown. Content-based: materiał o trybunale/wadze, nie o sesjach Zolderu."
```

```yaml
source_id: "MS-JUN1982-BEL"
title: "Grote Prijs van België / 1982 Belgian Grand Prix — An air of foreboding"
author_or_organisation: "D.S.J., Motor Sport"
publication_date: "1982-06"
event_date: "1982-05-07/1982-05-09"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/june-1982/46/grote-prijs-van-belgie-3/"
access_date: "2026-08-06"
supports:
  - claim_id: "R06-PW-FOCA-01"
    scope: "Powrót „strajkujących” z Imoli; belgijskie zgłoszenie przepełnione."
  - claim_id: "R06-PW-FOCA-02"
    scope: "Zapowiedź FOCA „disruptive methods” / protestów; paddock patrzy przez ramię w piątkowy poranek przed sesją."
  - claim_id: "R06-PW-CUT-01"
    scope: "Pierwsza oficjalna jazda: piątkowy poranny test/trening; potem popołudniowe kwalifikacje; sortowanie Concorde."
  - claim_id: "R06-PW-ENT-01"
    scope: "32 kierowców w linii; cel 26 starterów; zespoły z punktami w mistrzostwie konstruktorów poprzedniego sezonu mają zapewniony pełny trening (Concorde), pozostali — poranne sortowanie."
  - claim_id: "R06-PW-CIR-01"
    scope: "Całkowita przebudowa pitów/paddocku po śmierci mechanika Oselli 1981; ukończona na czas."
  - claim_id: "R06-PW-DRV-01"
    scope: "Daly debiut Williams #2; Reutemann emerytura; Andretti nie zrywa kontraktu US; Rosberg #1."
  - claim_id: "R06-PW-DRV-02"
    scope: "Surer z powrotem w Arrows po wypadku w testach Kyalami w styczniu."
  - claim_id: "R06-PW-DRV-03"
    scope: "Henton nadal Tyrrell #2; „negotiated” Borgudda."
  - claim_id: "R06-PW-DRV-04"
    scope: "Lammers w Theodore."
  - claim_id: "R06-PW-DRV-05"
    scope: "de Villota finansuje trzeciego Marcha."
  - claim_id: "R06-PW-TEC-02"
    scope: "Brabham trio BT50–BMW obecne."
  - claim_id: "R06-PW-EXP-02"
    scope: "Oczekiwanie zakłóceń/protestów FOCA."
  - claim_id: "R06-PW-TEC-07"
    scope: "Jenkinson: Ecclestone nie będzie protestował turbosprężarek jako turbin."
  - claim_id: "R06-PR-FMT-01"
    scope: "Piątek: poranny test/sort + popołudniowa 1 h Q; sobota: testing + finałowa 1 h; niedziela: ~½ h warm-up południe; start due 15:30; pit lane 20 min wcześniej."
  - claim_id: "R06-PR-FMT-04"
    scope: "Opóźnienie piątku 21 min (brak lekarzy; Watkins); popołudnie też 21 min później."
  - claim_id: "R06-PR-PQ-01"
    scope: "Sortowanie: Boesel, Jarier, Paletti, Warwick, Fabi, de Villota; odpadli Paletti i de Villota."
  - claim_id: "R06-PR-FRI-01"
    scope: "Narracja piątku: pogoda chłodno/szaro/sucho; Rosberg FW08/3; Daly nowy; BMW pick-up; Prost overheating; Alfa 182B odstawiona; Pironi tow; deszcz potem schnięcie."
  - claim_id: "R06-PR-FRI-Q-01"
    scope: "Piątek Q: Arnoux 1:15.903, Prost 1:15.962, Piquet 1:17.124; Alboreto 4.; ważenie Arnoux 581 / Prost 592 / Guerrero 594 / Henton 577 → DSQ czasów Hentona; dwa komplety Q."
  - claim_id: "R06-PR-SAT-01"
    scope: "Sobota rano: wilgotne place, zimno; lapy Rosberg 33 / Prost 32 / Arnoux 31 / Mansell 30; Winkelhock 4; Giacomelli back; Patrese spare; hamulce/ducts."
  - claim_id: "R06-PR-SAT-Q-01"
    scope: "Finał Q: Prost/Arnoux szybciej niż piątek; Rosberg 1:15.847 jedyny Cosworth <1:16 obok Renault; Daly T-car po wybuchu; Henton odzyskuje start; Brabham troubled; traffic; 2 Q sets."
  - claim_id: "R06-PR-ACC-01"
    scope: "Wypadek Villeneuve ~ostatnie 8 min; Mass clip LF/RR; launch ~140 mph; stop; Louvain life support; śmierć ogłoszona wieczorem; restart bez poprawy czasów."
  - claim_id: "R06-PR-WD-01"
    scope: "Ferrari wycofuje drugi samochód i wraca do Włoch; niedziela puste miejsce transportera; pole zamyka o 2; Mass i Baldi na tył; Guerrero i Lammers poza; niedziela warm sunny."
  - claim_id: "R06-PR-WU-01"
    scope: "Warm-up: Rosberg misfire → wymiana silnika; Prost turbo failure → wymiana turbo; Cheever spin sand bez szkód."
  - claim_id: "R06-PO-RACE-01"
    scope: "Narracja wyścigu: start Arnoux; Rosberg lead okr. 5; awarie Renault; Watson wyprzedza Laudę okr. 47; Daly spin; Watson lead okr. 69; FL okr. 67."
  - claim_id: "R06-PO-CLS-01"
    scope: "Ważenie pierwszych 7: Watson 581, Rosberg 591, Lauda 578, Cheever 612, de Angelis 585, Piquet 587, Serra 600; DSQ Laudy; peleton w górę."
  - claim_id: "R06-PO-PTS-01"
    scope: "Klasyfikacja po DSQ: Watson–Rosberg–Cheever–de Angelis–Piquet–Serra; punkty 9–6–4–3–2–1."
disagreement_notes: "AS „Monday” pre-qual vs MS Friday (UNC-R06-PR-PQ-DAY). AS ordinals mix with/without Ferraris (UNC-R06-PR-GRID-ORD). MS OCR „16 starters” ≈26. UPI wire lag vs immediate DSQ (UNC-R06-PO-DSQ-WIRE)."
notes: "Pełny weekend w zakresie post-race. Pre-race dokumenty nie używają claimów Race. Quarantine: Monaco / later rounds / foreshadowing."
```

```yaml
source_id: "MS-JUN1982-NOTES"
title: "Notes on the cars at Zolder"
author_or_organisation: "D.S.J., Motor Sport"
publication_date: "1982-06"
event_date: "1982-05-07/1982-05-09"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/june-1982/49/notes-on-the-cars-at-zolder-3/"
access_date: "2026-08-06"
supports:
  - claim_id: "R06-PW-BMW-01"
    scope: "Ultimatum BMW wobec Ecclestone’a: jeździć BMW w Zolderze albo szukać innej ekipy."
  - claim_id: "R06-PW-TEST-01"
    scope: "Test Silverstone: Piquet BT50 ~156 mph; Palmer FW08 ~151 mph."
  - claim_id: "R06-PW-TEC-01"
    scope: "Trzy FW08; Rosberg 3 / zapas 1 / Daly nowy 4; pushrod; ~550 kg + woda do 580."
  - claim_id: "R06-PW-TEC-02"
    scope: "Trzy BT50 BMW podobnej specyfikacji; układ turbo po lewej."
  - claim_id: "R06-PW-TEC-03"
    scope: "Alfa 182B: sidepody 10 cm węższe z każdej strony; poprawiony wydech; obecne w Zolderze."
  - claim_id: "R06-PW-TEC-04"
    scope: "Ligier tłumaczył Imolę opóźnieniem JS19; w Belgii trio starych JS17."
  - claim_id: "R06-PW-TEC-05"
    scope: "ATS umowa Michelin po zawiedzeniu Avon/IRTS."
  - claim_id: "R06-PW-TEC-06"
    scope: "Ferrari 126C2 bez istotnych zmian vs Imola; Villeneuve 058, Pironi 059, T-car 057."
  - claim_id: "R06-PR-TEC-01"
    scope: "Sesje: Rosberg/Daly zamiany FW08; Patrese turbo/exhaust swap; Alfa 182B abandoned; woda w zbiornikach Williamsa trzymana pełna."
disagreement_notes: "Szerokość Alfy: MS 10 cm/strona vs AS ~12 cm (UNC-R06-PW-ALFA)."
notes: "Pre-weekend: przyjazd/ultimatum/Silverstone/FW08 design. Pre-race: zamiany sesyjne. Quarantine: wybory wyścigowe (np. Daly „returned to FW08/4 on race day” jako narracja po starcie)."
```

```yaml
source_id: "AS-GOLD-1982-BEL"
title: "Grand Prix Gold: 1982 Belgian GP"
author_or_organisation: "Autosport / Nigel Roebuck (reprint)"
publication_date: "unknown"
event_date: "1982-05-07/1982-05-09"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.autosport.com/f1/news/grand-prix-gold-1982-belgian-gp-5098993/5098993/"
access_date: "2026-08-06"
supports:
  - claim_id: "R06-PW-BMW-01"
    scope: "Publiczne niezadowolenie BMW ~10 dni przed Zolderem; jeździć turbo albo koniec współpracy."
  - claim_id: "R06-PW-EXP-04"
    scope: "Napięcie w boksie Ferrari po Imoli; brak komunikacji Villeneuve–Pironi już przy przyjeździe / przed pierwszymi sesjami."
  - claim_id: "R06-PW-DRV-02"
    scope: "Powrót Surera; AS: wciąż daleki od pełnej sprawności (konflikt z MS)."
  - claim_id: "R06-PW-TEC-03"
    scope: "Alfa 182B: sidepody węższe o ok. 12 cm łącznie (konflikt z MS 10 cm/strona)."
  - claim_id: "R06-PR-SAT-Q-02"
    scope: "Pole Prost; Arnoux 2.; Rosberg 1:15.847; Lauda 1 set Q Michelin; Alboreto 1:16.308; Pironi ~0,1 s przed Villeneuve przed wypadkiem; Watson ~1 s za Laudą; Stappert „complete disaster”; Daly T-car."
  - claim_id: "R06-PR-ACC-02"
    scope: "Wypadek 13:52; ~8 min do końca; Mass przesuwa w prawo / Villeneuve też w prawo; śmierć sobotni wieczór ~7 h później; Mass bez obrażeń."
  - claim_id: "R06-PR-TYR-01"
    scope: "Villeneuve: Goodyear A undriveable, B lepsze; komentarz o sterowaniu w left-right over the hill."
  - claim_id: "R06-PR-WU-02"
    scope: "Warm-up 11:45; de Cesaris najszybszy, Lauda, Watson; Prost turbo out; Rosberg spare/misfire; niedziela cieplejsza niż Q."
  - claim_id: "R06-PR-FMT-03"
    scope: "Start „At 3.30 they were on their way”."
  - claim_id: "R06-PO-RACE-02"
    scope: "Narracja AS: soft/hard Michelin McLaren; cytaty Watson (Daly vs Rosberg) i Rosberg (flat / left rear / brakes); lead okr. 69; DSQ „three pounds”."
  - claim_id: "R06-PO-CLS-01"
    scope: "Lauda 3. na drodze → DSQ post-race scrutineering; Cheever dziedziczy 3."
disagreement_notes: "Forma Surera MS vs AS; szerokość Alfy MS vs AS; AS „Monday” pre-qual vs MS Friday; AS ordinals with/without Ferraris; waga −2 kg (MS) vs „three pounds” (AS)."
notes: "Reprint 2012. Pełny The Grand Prix w zakresie post-race. Quarantine: „he will win soon” jako proroctwo; Monaco nav; career retrospectives poza faktami do cutoff."
```

```yaml
source_id: "MS-1978-BEL"
title: "1978 Belgian Grand Prix report (circuit length)"
author_or_organisation: "Motor Sport"
publication_date: "unknown"
event_date: "1978-05-21"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/database/races/1978-belgian-grand-prix/"
access_date: "2026-08-06"
supports:
  - claim_id: "R06-PW-CIR-02"
    scope: "Długość toru Zolder podana jako 4,262 km we współczesnym materiale MS."
disagreement_notes: null
notes: "Wymiar obiektu z wcześniejszego sezonu; nie program 1982."
```

```yaml
source_id: "MS-JUN1981-BEL"
title: "1981 Belgian Grand Prix race report"
author_or_organisation: "D.S.J., Motor Sport"
publication_date: "1981-06"
event_date: "1981-05-17"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/june-1981/46/grote-prijs-van-belgie-6/"
access_date: "2026-08-06"
supports:
  - claim_id: "R06-PW-CIR-03"
    scope: "GP Belgii 1981 na Zolderze jako wyścig 70 okrążeń."
disagreement_notes: null
notes: "Poprzedni sezon; nie dowodzi dystansu 1982."
```

```yaml
source_id: "SEC-CASABLANCA-LEAD"
title: "Secondary leads on Casablanca FISA congress / FOCA return"
author_or_organisation: "STATS F1 / Grandprix.com / retrospectives"
publication_date: "unknown"
event_date: "1982-04/1982-05"
source_type: "SECONDARY"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "Secondary research leads only; not used as hard fact"
access_date: "2026-08-06"
supports:
  - claim_id: "R06-PW-CAS-01"
    scope: "LEAD ONLY: kongres ~tydzień po Imoli; wtórne twierdzenia o kompromisie i powrocie FOCA."
disagreement_notes: "Brak datowanej depeszy pierwotnej w pakiecie; MS nie nazywa Casablanki."
notes: "Nie traktować jako potwierdzonego dowodu. Luka badawcza."
```

```yaml
source_id: "UPI-1982-05-09-GV"
title: "The death of Canadian Gilles Villeneuve overshadowed the Belgian..."
author_or_organisation: "UPI"
publication_date: "1982-05-09"
event_date: "1982-05-08/1982-05-09"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.upi.com/Archives/1982/05/09/The-death-of-Canadian-Gilles-Villeneuve-overshadowed-the-Belgian/1821389764800/"
access_date: "2026-08-06"
supports:
  - claim_id: "R06-PR-ACC-03"
    scope: "Villeneuve zmarł sobotnią nocą w Louvain / St Raphael z obrażeń głowy i szyi po wypadku w końcówce treningu/praktyki; Ferrari wycofało się ~2 h przed oficjalnym potwierdzeniem śmierci."
disagreement_notes: "Sekwencja wycofania vs potwierdzenie śmierci (UNC-R06-PR-FERRARI-ORDER)."
notes: "Dateline niedziela — używać wyłącznie faktów o sobotniej śmierci i wycofaniu Ferrari znanych przed startem. Quarantine: wynik wyścigu, cytaty o bezpieczeństwie zależne od przebiegu niedzieli, pogrzeb/transport ciała jako kolor poza briefem przedstartowym jeśli niepotrzebne."
```

```yaml
source_id: "RSC-1982-R06-Q"
title: "GP Belgium 1982 — Qualifying Results (reconstruction)"
author_or_organisation: "Racing Sports Cars"
publication_date: "unknown"
event_date: "1982-05-07/1982-05-09"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.racingsportscars.com/f1/results/qualifying/Zolder-1982-05-09.html"
access_date: "2026-08-06"
supports:
  - claim_id: "R06-PR-GRID-01"
    scope: "Rekonstrukcja czasów Q i kolejności: Prost 1:15.701, Arnoux 1:15.730, Rosberg 1:15.847, Lauda 1:16.049, Alboreto 1:16.308, Pironi 1:16.501, de Cesaris 1:16.575, Villeneuve 1:16.616, dalej przez Mass 1:19.777 / Baldi 1:19.815; Guerrero/Lammers poza 26; Paletti/de Villota wśród other present / DNPQ."
disagreement_notes: "Nie oficjalny biuletyn FIA; numery pozycji RSC mieszają Ferraris jako DNS z kolejnością Q."
notes: "Używać jako rekonstrukcja czasów + tabela niedzielnego pola po zamknięciu (MS). Quarantine wyników wyścigu z innych stron RSC — wyniki Race używane w post-race przez RSC-1982-R06-RES."
```

```yaml
source_id: "MS-JUN1982-KANAL"
title: "Reflections in the Kanal"
author_or_organisation: "D.S.J., Motor Sport"
publication_date: "1982-06"
event_date: "1982-05-09"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/june-1982/50/reflections-in-the-kanal/"
access_date: "2026-08-06"
supports:
  - claim_id: "R06-PO-CLS-01"
    scope: "Lauda −2 kg; brak tolerancji wagi; Watson 581 kg; porównanie do DSQ Winkelhocka Imola; Piquet 587 / Cheever 612 w refleksji."
disagreement_notes: null
notes: "Content-based availability dla komentarza wagowego. Quarantine: spekulacje kadrowe poza cutoff (Jones/Andretti/Reutemann jako tło smutku — nie rozwijać foreshadowing)."
```

```yaml
source_id: "UPI-1982-05-09-RES"
title: "Auto Racing Results Belgian Grand Prix At Zolder, Belgium, May 9"
author_or_organisation: "UPI"
publication_date: "1982-05-09"
event_date: "1982-05-09"
source_type: "PRESS"
contemporary: true
spoiler_risk: "none"
locator: "https://www.upi.com/Archives/1982/05/09/Auto-Racing-Results-Belgian-Grand-Prix-At-Zolder-Belgium-May-9/1053389764800/"
access_date: "2026-08-06"
supports:
  - claim_id: "R06-PO-TIME-01"
    scope: "Czasy na drodze: Watson 1:35:41.99; Rosberg 1:35:49.26; Lauda 1:36:50.13; Cheever one lap behind."
disagreement_notes: "Lista nadal ma Laudę 3. — bez DSQ (UNC-R06-PO-DSQ-WIRE). Kolumna „laps” przy DNF wygląda na laps remaining, nie completed."
notes: "Używać do czasów top; nie do okrążeń DNF ani klasyfikacji po DSQ."
```

```yaml
source_id: "UPI-1982-05-09-SAFE"
title: "The horrifying crash that snapped the life from race..."
author_or_organisation: "UPI"
publication_date: "1982-05-09"
event_date: "1982-05-08/1982-05-09"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.upi.com/Archives/1982/05/09/The-horrifying-crash-that-snapped-the-life-from-race/4136389764800/"
access_date: "2026-08-06"
supports:
  - claim_id: "R06-PO-SAFE-01"
    scope: "Balestre: extraordinary FISA executive committee on safety; Ongaro inquiry; cytaty Pironi (180→250–260 km/h), Lauda racing accident, Prost shock, Laffite sordid game."
disagreement_notes: "UPI nadal nazywa Laudę trzecim w wyścigu."
notes: "Same-day. Quarantine: szczegółowa logistyka pogrzebu / lot ciała poza krótkim kontekstem; nie UPI 11 V Mass."
```

```yaml
source_id: "RSC-1982-R06-RES"
title: "GP Belgium 1982 — Race Results (reconstruction)"
author_or_organisation: "Racing Sports Cars"
publication_date: "unknown"
event_date: "1982-05-09"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.racingsportscars.com/f1/results/Zolder-1982-05-09.html"
access_date: "2026-08-06"
supports:
  - claim_id: "R06-PO-CLS-01"
    scope: "Rekonstrukcja: 1 Watson … 9 Laffite; DSQ Lauda underweight; DNF laps/causes; Baldi NC 51; DNS Ferrari."
  - claim_id: "R06-PO-FL-01"
    scope: "Wsparcie FL Watsona / klasyfikacji (cross-check z AS/MS)."
disagreement_notes: "Nie oficjalny biuletyn FIA; Warwick 29 vs AS ~19; Mansell clutch vs MS gearbox."
notes: "Rekonstrukcja pomocnicza; preferować MS/AS dla narracji przyczyn."
```

```yaml
source_id: "ARCHIVE-R05-STAND-PO"
title: "Klasyfikacja po Grand Prix San Marino (baza arytmetyki R06-PO)"
author_or_organisation: "F1 Time Capsule archive (standings-after.md R05)"
publication_date: "not-applicable"
event_date: "1982-04-25/1982-04-26"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/05-san-marino-grand-prix/standings-after.md"
access_date: "2026-08-06"
supports:
  - claim_id: "R06-PO-STD-01"
    scope: "Baza przed Zolderem: Prost 18, Lauda 12, Alboreto 10, Pironi 9, Rosberg/Watson 8, …; Renault 22, McLaren 20, Ferrari 15, Williams 14, …"
disagreement_notes: null
notes: "Wejście arytmetyczne do standings-after R06; tożsamość z ARCHIVE-R05-STAND w pre-weekend."
```

## Conflict and uncertainty index

| Uncertainty ID | Claim IDs | Source IDs | Status at cutoff | Note |
| --- | --- | --- | --- | --- |
| UNC-R06-PW-SURER | R06-PW-DRV-02 | MS-JUN1982-BEL, AS-GOLD-1982-BEL | open | MS: fully recovered; AS: still far from completely fit |
| UNC-R06-PW-ALFA | R06-PW-TEC-03 | MS-JUN1982-NOTES, AS-GOLD-1982-BEL | open | MS: 10 cm narrower each side; AS: ~12 cm across pods |
| UNC-R06-PW-CAS | R06-PW-CAS-01 | SEC-CASABLANCA-LEAD | unsupported-as-fact | Brak pierwotnego datowanego wire; nie w narracji jako fakt |
| UNC-R06-PW-LB | R06-PW-LB-APP-01 | ARCHIVE-R04-STAND, ARCHIVE-R05-STAND | open | Brak aktualizacji apelacji LB między 26 IV a piątkiem Zolder |
| UNC-R06-PR-PQ-DAY | R06-PR-PQ-01 | MS-JUN1982-BEL, AS-GOLD-1982-BEL | resolved-prefer-MS | AS „Monday” pre-qual vs MS Friday morning |
| UNC-R06-PR-GRID-ORD | R06-PR-GRID-01 | AS-GOLD-1982-BEL, MS-JUN1982-BEL, RSC-1982-R06-Q | open | AS miesza pozycje z/bez Ferrari; prefer MS close-up + RSC times |
| UNC-R06-PR-WX-SUN | R06-PR-WD-01 | MS-JUN1982-BEL, AS-GOLD-1982-BEL | open | MS/AS warm sunny Sunday; secondary meteo „cold/13 °C” nie użyte |
| UNC-R06-PR-DEATH-CLOCK | R06-PR-ACC-01 | MS-JUN1982-BEL, AS-GOLD-1982-BEL, UPI-1982-05-09-GV | open | Contemporary: evening / Saturday night / ~7 h; exact 21:12 secondary |
| UNC-R06-PR-FERRARI-ORDER | R06-PR-ACC-03 | UPI-1982-05-09-GV, MS-JUN1982-BEL | open | UPI: withdrawal ~2 h before death confirmed |
| UNC-R06-PR-MOTIVE | R06-PR-ACC-01 | MS-JUN1982-BEL, AS-GOLD-1982-BEL | open | MS: last bid to improve grid; AS: Pironi just ~0.1 s quicker; later Forghieri theories quarantined |
| UNC-R06-PO-DSQ-WIRE | R06-PO-CLS-01 | MS-JUN1982-BEL, UPI-1982-05-09-RES, UPI-1982-05-09-SAFE | open | MS: immediate weigh/DSQ; UPI 9 V still lists Lauda 3rd |
| UNC-R06-PO-WEIGHT-UNIT | R06-PO-CLS-01 | MS-JUN1982-BEL, MS-JUN1982-KANAL, AS-GOLD-1982-BEL | resolved-prefer-MS | MS 578 kg (−2); AS „three pounds” |
| UNC-R06-PO-MANSELL | R06-PO-RACE-01 | MS-JUN1982-BEL, AS-GOLD-1982-BEL | open | MS gearbox lap 10; AS/RSC clutch lap 9 |
| UNC-R06-PO-WARWICK-LAP | R06-PO-RACE-01 | AS-GOLD-1982-BEL, RSC-1982-R06-RES | open | AS ~19; RSC 29 |
| UNC-R06-PO-BALDI | R06-PO-RACE-01 | RSC-1982-R06-RES, MS-JUN1982-BEL | open | RSC NC 51; cause thin in MS |
| UNC-R06-PO-DALY-LAP | R06-PO-RACE-01 | MS-JUN1982-BEL, RSC-1982-R06-RES | open | MS start lap 61; RSC 60 |
| UNC-R06-PO-PROST-PASS | R06-PO-RACE-01 | MS-JUN1982-BEL, AS-GOLD-1982-BEL | open | AS: Lauda + de Cesaris past Prost; MS: Lauda + de Angelis |
