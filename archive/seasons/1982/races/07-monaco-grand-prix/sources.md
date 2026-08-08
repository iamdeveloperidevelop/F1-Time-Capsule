# Monaco Grand Prix — source ledger

To kanoniczny rejestr źródeł folderu rundy. Dokumenty treści cytują
`source_id` i `claim_id`; nie prowadzą konkurencyjnych list źródeł. Cutoff
rejestru obejmuje `pre-weekend.md`, `pre-race.md`, `post-race.md` oraz
`standings-after.md` (natychmiastowa procedura post-race 23 V 1982: flaga,
klasyfikacja, brak protestu wobec restartu Patrese’a).

## Source entry

```yaml
source_id: "ARCHIVE-R06-STAND"
title: "Klasyfikacja po Grand Prix Belgii"
author_or_organisation: "F1 Time Capsule archive (standings-after.md R06)"
publication_date: "not-applicable"
event_date: "1982-05-09"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/06-belgian-grand-prix/standings-after.md"
access_date: "2026-08-06"
supports:
  - claim_id: "R07-PW-STD-01"
    scope: "Prowizoryczna kolejność i punkty po Zolderze z DSQ Laudy: Prost 18, Watson 17, Rosberg 14, Lauda 12, Alboreto 10, Pironi 9, Reutemann/Villeneuve 6, de Angelis 5, Arnoux/Patrese/Mansell/Cheever 4; McLaren 29, Renault 22, Williams 20, Ferrari 15, Tyrrell 10, Lotus 9, Brabham 6, Talbot-Ligier 4, Osella 3, ATS 2, Fittipaldi 1; otwarte apelacje LB; skala prowizoryczna."
  - claim_id: "R07-PO-PTS-01"
    scope: "Baza arytmetyki mistrzostw przed Monako (ta sama migawka R06); punkty monakijskie dodawane osobno z klasyfikacji R07."
  - claim_id: "R07-PO-STD-01"
    scope: "Wejście do standings-after R07: sumy po Zolderze przed dodaniem punktów Monako."
disagreement_notes: "Skala punktowa prowizoryczna; brak oficjalnego biuletynu FIA w pakiecie R06; status provisional."
notes: "Baza przed Monako; nie kopiować pełnych tabel do narracji."
```

```yaml
source_id: "ARCHIVE-R06-PW"
title: "Grand Prix Belgii — przed weekendem (obsada przyjazdu Zolder)"
author_or_organisation: "F1 Time Capsule archive (pre-weekend.md R06)"
publication_date: "not-applicable"
event_date: "1982-05-07/1982-05-09"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/06-belgian-grand-prix/pre-weekend.md"
access_date: "2026-08-06"
supports:
  - claim_id: "R07-PW-ENT-01"
    scope: "Kontynuacja obsady vs Zolder jako baza porównawcza: Daly Williams #2; Surer Arrows; Henton Tyrrell #2; Lammers Theodore; de Villota March; pary głównych zespołów."
disagreement_notes: null
notes: "Carry-forward personalny; weryfikować względem RSC Monaco entry."
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
  - claim_id: "R07-PW-CAL-01"
    scope: "Monaco Grand Prix — Monte Carlo — 23 May 1982 na liście kalendarza FIA."
disagreement_notes: null
notes: "publication_date dnia unknown; content-based availability jako przedsezonowa reprodukcja. Już w season/calendar.md."
```

```yaml
source_id: "UPI-1982-05-09-GV"
title: "The death of Canadian Gilles Villeneuve overshadowed the Belgian..."
author_or_organisation: "UPI"
publication_date: "1982-05-09"
event_date: "1982-05-08/1982-05-09"
source_type: "PRESS"
contemporary: true
spoiler_risk: "none"
locator: "https://www.upi.com/Archives/1982/05/09/The-death-of-Canadian-Gilles-Villeneuve-overshadowed-the-Belgian/1821389764800/"
access_date: "2026-08-06"
supports:
  - claim_id: "R07-PW-GV-01"
    scope: "Śmierć Villeneuve’a sobotnia noc Louvain/St Raphael po wypadku w treningu Zolder; wycofanie Ferrari przed niedzielą; plan transportu ciała do Berthierville; Pironi/GPDA o spódnicach i frakcjach; Lauda „racing accident”; Balestre nadzwyczajny komitet FISA; dochodzenie Ongaro."
disagreement_notes: null
notes: "Współczesna depesza; nie używać do wyników Monako."
```

```yaml
source_id: "UPI-1982-05-11-GV"
title: "More than 1,000 fans and friends, many grieving in..."
author_or_organisation: "UPI"
publication_date: "1982-05-11"
event_date: "1982-05-11"
source_type: "PRESS"
contemporary: true
spoiler_risk: "none"
locator: "https://www.upi.com/Archives/1982/05/11/More-than-1000-fans-and-friends-many-grieving-in/8677389937600/"
access_date: "2026-08-06"
supports:
  - claim_id: "R07-PW-GV-02"
    scope: "Publiczne pożegnanie we wtorek 11 maja w Berthierville; zapowiedź pogrzebu środa 15:00 EDT Ste. Geneviève; kremacja Montreal."
disagreement_notes: null
notes: "Przed cutoffem Monako."
```

```yaml
source_id: "UPI-1982-05-12-GV"
title: "Gilles Villeneuve, the little driver who dreamed of retiring..."
author_or_organisation: "UPI"
publication_date: "1982-05-12"
event_date: "1982-05-12"
source_type: "PRESS"
contemporary: true
spoiler_risk: "none"
locator: "https://www.upi.com/Archives/1982/05/12/Gilles-Villeneuve-the-little-driver-who-dreamed-of-retiring/2801390024000/"
access_date: "2026-08-06"
supports:
  - claim_id: "R07-PW-GV-03"
    scope: "Pogrzeb 12 maja Berthierville: Trudeau, Lévesque, Scheckter, Stewart, wieńce Ferrari, kondukt do krematorium Montreal; Joan zamierza zabrać prochy do Monako."
disagreement_notes: "UPI podaje wiek 30 — konflikt z urodzeniem 18 I 1950 (UNC-R07-PW-AGE)."
notes: "Wiek w reader-facing pominięty."
```

```yaml
source_id: "MS-JUL1982-MON"
title: "A process of elimination — Monaco Grand Prix"
author_or_organisation: "Denis Jenkinson / Motor Sport"
publication_date: "1982-07"
event_date: "1982-05-20/1982-05-23"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/july-1982/62/monaco-grand-prix-14/"
access_date: "2026-08-06"
supports:
  - claim_id: "R07-PW-CUT-01"
    scope: "Pierwsza oficjalna sesja: czwartek 20 maja 1982, 8 a.m., eliminacja zespołów bez punktów konstruktorów 1981."
  - claim_id: "R07-PW-FMT-01"
    scope: "31 kierowców F1; limit 20 na wyścig; format Thu pre-qual → morning test + afternoon Q; Fri rest; Sat practice + Q; Sun 76 laps; 40th Monaco GP."
  - claim_id: "R07-PW-FMT-02"
    scope: "Lista ośmiu do prekwalifikacji: Mass, Boesel, Villota (March); Serra (Fittipaldi); Jarier, Paletti (Osella); Warwick, Fabi (Toleman)."
  - claim_id: "R07-PW-TYR-MS"
    scope: "Avon wycofuje się po niesmaku po Imoli; Ensign/Theodore bez opon (kontekst przyjazdu — nie wyniki sesji)."
  - claim_id: "R07-PR-CUT-01"
    scope: "Start was due at 3.30 p.m. Sunday; cars leave paddock for assembly grid after that marker."
  - claim_id: "R07-PR-PQ-01"
    scope: "Pre-qual: Mass, Warwick, Jarier advanced (MS order); Mass car-change / weighing accusations; five failed to reach practice."
  - claim_id: "R07-PR-TYR-01"
    scope: "Thursday: Guerrero few laps on secondhand tyres; Theodore bare wheels on jacks; Avon exit after Imola (MS framing)."
  - claim_id: "R07-PR-THU-01"
    scope: "Thursday morning/afternoon narrative: Piquet BMW struggle; Patrese Cosworth; Ligier skirts dispute; Renault injection; Watson engine; Henton prangs; Arnoux/de Cesaris/Patrese pace; weighing sample."
  - claim_id: "R07-PR-FRI-01"
    scope: "Friday rest day for F1 teams."
  - claim_id: "R07-PR-SAT-01"
    scope: "Saturday cool/hazy dry; RE34B for Prost; FW08/2 spare Daly; Piquet injection failure; Alfa misfires; Theodore acquires Goodyears; Mansell new 91/9."
  - claim_id: "R07-PR-SAT-Q-01"
    scope: "Final Q 13:00–14:00; Patrese 1:23.791; Arnoux late 1:23.281 pole (~0.5 s / ~2.5 s vs 1981 best); DNQ Baldi, Lammers, Mass, Warwick, Jarier, Guerrero."
  - claim_id: "R07-PR-PEN-01"
    scope: "Surer Arrows: 5.6 kg loose lead in cockpit after Q weighing; £300 fine; car over minimum without ballast."
  - claim_id: "R07-PR-WU-01"
    scope: "Sunday sunny morning; 30 min warm-up full race trim; Daly FW08/4; Prost RE34B; Brabham iron brakes; Pironi Ferrari 059; Cheever JS19 driveshaft bearing; Patrese/Arnoux/Rosberg confidence quotes; midday mountain gloom + cool breeze; engine mix on grid."
  - claim_id: "R07-PO-RACE-01"
    scope: "Race narrative: Arnoux lead; Giacomelli driveshaft ~5; Arnoux spin swimming pool stall; Prost lead; traffic/de Angelis; mid retirements (Salazar extinguisher, Cheever oil, Laffite, Winkelhock, Watson ignition, Lauda engine, Piquet gearbox); rain; Rosberg chicane; Alboreto suspension; Daly Tabac; Prost crash lap 74; Patrese Loews spin, marshal push, bump-start; Pironi/de Cesaris out of petrol; Patrese only car to complete 76; five mobile at finish."
  - claim_id: "R07-PO-WX-01"
    scope: "Late spots of rain → ice-rink circuit; CoC insisted on full 76 laps; not a visible downpour on pavements."
disagreement_notes: "Avon timing vs Autosport (po Belgii) — UNC-R07-PW-AVON. Pre-qual order vs AS — UNC-R07-PR-PQ-ORD. Lap-1 Prost/Patrese order vs AS — UNC-R07-PO-LAP1. Pironi fuel vs RSC electrics — UNC-R07-PO-PIR-CAUSE."
notes: "publication_date dnia unknown; content-based availability. Izolować pasaże race; nie używać retrospectives."
```

```yaml
source_id: "AS-GOLD-1982-MON"
title: "Grand Prix Gold: 1982 Monaco GP"
author_or_organisation: "Autosport (reprint; original contemporary report ~May/June 1982)"
publication_date: "unknown"
event_date: "1982-05-20/1982-05-23"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.autosport.com/f1/news/grand-prix-gold-1982-monaco-gp-5098992/5098992/"
access_date: "2026-08-06"
supports:
  - claim_id: "R07-PW-ENT-02"
    scope: "Ligier/Talbot przedstawia nowe JS19 na Monako po stosunkowo niewielkich testach (intencja debiutu przy przyjeździe)."
  - claim_id: "R07-PW-ENT-03"
    scope: "Brabham: Piquet przypisany BT50-BMW, Patrese BT49D Cosworth na Monte Carlo."
  - claim_id: "R07-PW-TEC-02"
    scope: "Renault elektroniczny wtrysk na Monaco po testach: lepsza odpowiedź przepustnicy, moment, zużycie, hamowanie silnikiem."
  - claim_id: "R07-PW-TYR-01"
    scope: "Avon/IRTS wycofanie po Belgii; Ensign/Theodore bez dostawcy; Goodyear odmawia; March kupuje zapas Avon po teście Croix-en-Ternois 14 maja (oświadczenie IRTS)."
  - claim_id: "R07-PW-EXP-01"
    scope: "Historyczny kontekst turbo w Monako (trudności Renault wcześniej; zwycięstwo Villeneuve’a 1981 jako dowód, że turbo może działać)."
  - claim_id: "R07-PR-PQ-02"
    scope: "Pre-qual order Jarier–Mass–Warwick; Toleman protest Mass weighing car; DNPQ Fabi, Paletti, Boesel, Serra, de Villota."
  - claim_id: "R07-PR-TYR-02"
    scope: "Session tyre drama: Thursday Theodore no tyres; Guerrero old Long Beach Avons; Saturday Lammers Goodyears; Michelin declines Ensign."
  - claim_id: "R07-PR-JS19-01"
    scope: "JS19 skirts beyond rear axle ruled illegal; cut to axle line; Ligier anger; Laffite downforce/balance/porpoising comments; Cheever Thursday rear suspension then JS17 use noted in practice narrative."
  - claim_id: "R07-PR-THU-02"
    scope: "Thursday Q: Arnoux 1:24.54 fastest; quote on clear lap; Prost electrical/engine → T-car sixth; de Cesaris quick; Pironi understeer comments."
  - claim_id: "R07-PR-SAT-Q-02"
    scope: "Saturday: Arnoux 1:23.28 pole (12th career); Patrese ~1:23.77 morning / denied pole afternoon; Giacomelli third sub-24; Prost RE34B fourth; Pironi 13th→5th; Rosberg sixth first Monaco F1 race; de Cesaris 182B seventh no improve; DNQ list matches MS."
  - claim_id: "R07-PR-EXP-01"
    scope: "Rosberg pre-start quote: Renault slow with full tanks; hope Patrese does not beat Arnoux to first corner; put money on me."
  - claim_id: "R07-PR-WX-01"
    scope: "Sunday morning deep blue then clouds; muggy overcast afternoon; would it rain?; Gilles banner at swimming pool; crowd notes."
  - claim_id: "R07-PR-PEN-02"
    scope: "End-of-qualifying cynical weight-limit remark (context only); Surer grid 19th after practice."
  - claim_id: "R07-PO-RACE-02"
    scope: "Race: Arnoux early lead; Giacomelli stub axle ~5; Arnoux spin lap 15; Prost/Patrese duel; Pironi nose ~32 / FL interim; de Cesaris valve spring; Rosberg vs Alfa; Watson ignition ~36; rain ~61; Rosberg lap 65; Alboreto 70; Daly Tabac; Prost crash lap 74; Patrese Loews; Pironi quote No fuel; de Cesaris dry; Patrese win quote; Mansell past de Angelis."
  - claim_id: "R07-PO-QTE-01"
    scope: "Attributed quotes: Patrese surprise after spin; Pironi electrical-then-fuel; Rosberg Tabac plan; Daly Tabac impact; Prost Ste Devote contact not cause of crash."
disagreement_notes: "Avon timing vs Motor Sport (po Imoli) — UNC-R07-PW-AVON. Pre-qual order vs MS — UNC-R07-PR-PQ-ORD. Lap-1 order vs MS — UNC-R07-PO-LAP1. Arnoux lap 15 vs UPI/RSC 14 — UNC-R07-PO-ARN-LAP. Reprint 2012-08-16; data oryginalnego numeru unknown (1982-R07-PW-AS-01)."
notes: "Izolować pasaże race. Kwarantanna: foreshadow Detroit/Montreal z pasaży o Piquecie jako preview następnej rundy."
```

```yaml
source_id: "RSC-1982-R07-Q"
title: "GP Monaco 1982 — Qualifying Results"
author_or_organisation: "Racing Sports Cars (database reconstruction)"
publication_date: "unknown"
event_date: "1982-05-20/1982-05-23"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.racingsportscars.com/f1/results/qualifying/Monaco-1982-05-23.html"
access_date: "2026-08-08"
supports:
  - claim_id: "R07-PR-GRID-01"
    scope: "Provisional Q times P1–P26: Arnoux 1:23.281 … Salazar 1:27.022 on grid; DNQ Baldi–Guerrero with times; Prost listed on 15T RE30B."
disagreement_notes: "Not an official FIA bulletin; cross-check P1/P2 with MS/AS."
notes: "Use for structured grid only; quarantine race results pages."
```

```yaml
source_id: "RSC-1982-R07-RACE"
title: "GP Monaco 1982 — Race page (start time / distance metadata)"
author_or_organisation: "Racing Sports Cars (database reconstruction)"
publication_date: "unknown"
event_date: "1982-05-23"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.racingsportscars.com/f1/race/Monaco-1982-05-23.html"
access_date: "2026-08-08"
supports:
  - claim_id: "R07-PR-CUT-02"
    scope: "Start time listed 15:30; distance 76 laps; warm-up 30 minutes noted in pre-race sessions summary."
  - claim_id: "R07-PO-FL-01"
    scope: "Rekonstrukcja FL: Patrese 1:26.354 (nie użyte w prose bez biuletynu — luka 1982-R07-PO-FL-01)."
disagreement_notes: null
notes: "Start-time metadata for pre-race; FL reconstruction quarantined from reader-facing claim pending official bulletin."
```

```yaml
source_id: "RSC-1982-R07-RES"
title: "GP Monaco 1982 — Race Results (reconstruction)"
author_or_organisation: "Racing Sports Cars (database reconstruction)"
publication_date: "unknown"
event_date: "1982-05-23"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.racingsportscars.com/f1/results/Monaco-1982-05-23.html"
access_date: "2026-08-08"
supports:
  - claim_id: "R07-PO-CLS-01"
    scope: "Rekonstrukcja: 1 Patrese 76; 2 Pironi 75 Electrics; 3 de Cesaris 75 Out of fuel; 4 Mansell 75; 5 de Angelis 75; 6 Daly 74 gearbox; 7 Prost 73 Accident; 8 Henton 72; 9 Surer 70; 10 Alboreto 69; DNF list with laps."
disagreement_notes: "Pironi Electrics vs AS/UPI/MS fuel (UNC-R07-PO-PIR-CAUSE). Watson oil/battery vs MS/AS ignition. Arnoux lap 14 vs AS 15."
notes: "Rekonstrukcja pomocnicza; preferować UPI/MS/AS dla narracji przyczyn; struktura klasyfikacji cross-check."
```

```yaml
source_id: "UPI-1982-05-23-MON"
title: "Italian Riccardo Patrese was the beneficiary of a wild..."
author_or_organisation: "UPI"
publication_date: "1982-05-23"
event_date: "1982-05-23"
source_type: "PRESS"
contemporary: true
spoiler_risk: "none"
locator: "https://www.upi.com/Archives/1982/05/23/Italian-Riccardo-Patrese-was-the-beneficiary-of-a-wild/7848390974400/"
access_date: "2026-08-08"
supports:
  - claim_id: "R07-PO-CLS-01"
    scope: "Patrese wins first GP in 71 starts; only leading car left; Pironi 2nd and de Cesaris 3rd both one lap behind despite not completing; Mansell 4th, de Angelis 5th, Daly 6th; Prost classified 7th; Arnoux spun lap 14."
  - claim_id: "R07-PO-PROC-01"
    scope: "No objections to Patrese push-start; no technical rows; no disqualifications; victory lap with Pironi on car."
  - claim_id: "R07-PO-STD-01"
    scope: "Same-day championship wire: Prost 18, Watson 17, Pironi third (implies 16), Rosberg 14, Patrese 13, Lauda 12."
  - claim_id: "R07-PO-QTE-02"
    scope: "Patrese: I cannot believe what has just happened."
disagreement_notes: "Pironi championship total 16 vs archive 15 (UNC-R07-PO-PIR-PTS). Rosberg touch with de Cesaris vs MS/AS solo kerb (UNC-R07-PO-ROS). Arnoux lap 14 vs AS 15."
notes: "Same-day primary wire for classification top and process."
```

```yaml
source_id: "RSC-1982-R07-ENT"
title: "GP Monaco 1982 — Entry List"
author_or_organisation: "Racing Sports Cars (database reconstruction)"
publication_date: "unknown"
event_date: "1982-05-23"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "unknown"
locator: "https://www.racingsportscars.com/f1/entry/Monaco-1982-05-23.html"
access_date: "2026-08-06"
supports:
  - claim_id: "R07-PW-FER-02"
    scope: "Rekonstrukcja: #28 Pironi Ferrari 126C2; #27 Ferrari chassis listed jako did not arrive / bez kierowcy; Piquet BT50 BMW; Patrese BT49D Ford; Laffite/Cheever JS19."
disagreement_notes: "Nie jest oficjalną listą FOCA/FISA; round numbering w nagłówku bazy może być niespójny z archiwum."
notes: "Tylko obraz zgłoszeń; nie używać do wyników. Luka oficjalnego entry list: 1982-R07-PW-ENT-01."
```

## Conflict and uncertainty index

| Uncertainty ID | Claim IDs | Source IDs | Status at cutoff | Note |
| --- | --- | --- | --- | --- |
| UNC-R07-PW-AVON | R07-PW-TYR-01, R07-PW-TYR-MS | AS-GOLD-1982-MON, MS-JUL1982-MON | unresolved | AS: Avon po Belgii; MS: po Imoli; zakup Marcha 14 V zgodny z AS |
| UNC-R07-PW-AGE | R07-PW-GV-03 | UPI-1982-05-12-GV | unresolved | UPI „age of 30” vs urodzenie 18 I 1950; wiek pominięty w prose |
| UNC-R07-PW-ZONE | R07-PW-CUT-01, R07-PR-CUT-01 | MS-JUL1982-MON | open | 08:00 / 15:30 local; CEST założone, nie z programu |
| UNC-R07-PW-FER-ENTRY | R07-PW-FER-02 | RSC-1982-R07-ENT | open | Brak datowanego komunikatu Ferrari o jednym aucie |
| UNC-R07-PW-CIR-LEN | R07-PW-FMT-01 | MS-JUL1982-MON | open | 76 okrążeń z MS; długość km nie z programu 1982 |
| UNC-R07-PW-LB | R07-PW-STD-01 | ARCHIVE-R06-STAND | open | Brak aktualizacji apelacji LB 10–19 V |
| UNC-R07-PW-AS-MIX | multiple | AS-GOLD-1982-MON | mitigated | Cały tekst miesza preview/sesje/wyścig — tylko izolowane pasaże |
| UNC-R07-PR-PQ-ORD | R07-PR-PQ-01, R07-PR-PQ-02 | MS-JUL1982-MON, AS-GOLD-1982-MON | open | MS: Mass–Warwick–Jarier; AS: Jarier–Mass–Warwick; prose records both |
| UNC-R07-PR-GRID-OFF | R07-PR-GRID-01 | RSC-1982-R07-Q | open | RSC reconstruction vs missing official FIA timing bulletin |
| UNC-R07-PR-WX-SUN | R07-PR-WX-01 | MS-JUL1982-MON, AS-GOLD-1982-MON | open | Contemporary gloom/muggy; independent meteo bulletin lacking |
| UNC-R07-PO-LAP1 | R07-PO-RACE-01, R07-PO-RACE-02 | MS-JUL1982-MON, AS-GOLD-1982-MON | open | MS: Prost 3rd / Patrese 4th after Giacomelli; AS: Patrese 3rd / Prost 4th |
| UNC-R07-PO-ARN-LAP | R07-PO-RACE-01, R07-PO-RACE-02 | AS-GOLD-1982-MON, UPI-1982-05-23-MON, RSC-1982-R07-RES | open | AS lap 15; UPI/RSC lap 14 |
| UNC-R07-PO-PIR-CAUSE | R07-PO-CLS-01 | AS-GOLD-1982-MON, UPI-1982-05-23-MON, MS-JUL1982-MON, RSC-1982-R07-RES | open | Contemporary fuel (Pironi quote); RSC Electrics |
| UNC-R07-PO-ROS | R07-PO-RACE-01 | MS-JUL1982-MON, AS-GOLD-1982-MON, UPI-1982-05-23-MON | open | MS/AS: kerb/chicane alone; UPI: touch with de Cesaris |
| UNC-R07-PO-WAT | R07-PO-RACE-01 | MS-JUL1982-MON, AS-GOLD-1982-MON, RSC-1982-R07-RES | open | MS/AS ignition; RSC oil leak/battery |
| UNC-R07-PO-PIR-PTS | R07-PO-STD-01 | UPI-1982-05-23-MON, ARCHIVE-R06-STAND | open | Archive Pironi 15 (9+6); UPI implies 16 |
| UNC-R07-PO-FL | R07-PO-FL-01 | RSC-1982-R07-RACE, AS-GOLD-1982-MON | open | Official FL not in MS/UPI body; RSC Patrese 1:26.354 reconstruction |
| UNC-R07-PO-TIME | R07-PO-CLS-01 | secondary DBs only | open | Winner time 1:54:11.259 not in MS/UPI body — omitted from prose |
