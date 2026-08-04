# Brazilian Grand Prix — source ledger

To kanoniczny rejestr źródeł folderu rundy. Dokumenty treści cytują
`source_id` i `claim_id`; nie prowadzą konkurencyjnych list źródeł.

## Source entry

```yaml
source_id: "ARCHIVE-R01-STAND"
title: "Klasyfikacja po Grand Prix RPA"
author_or_organisation: "F1 Time Capsule archive (standings-after.md R01 / R02)"
publication_date: "not-applicable"
event_date: "1982-01-23"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/01-south-african-grand-prix/standings-after.md; mirror after empty Argentina: archive/seasons/1982/races/02-argentine-grand-prix/standings-after.md"
access_date: "2026-08-05"
supports:
  - claim_id: "R03-STD-01"
    scope: "Prowizoryczna kolejność i punkty po Kyalami (bez zmian po pustej Argentynie): Prost 9, Reutemann 6, Arnoux 4, Lauda 3, Rosberg 2, Watson 1; Renault 13, Williams 8, McLaren 4."
disagreement_notes: "Skala punktowa prowizoryczna; brak oficjalnego biuletynu FIA w pakiecie R01."
notes: "Wskaźnik do kanonicznej migawki; nie kopiować pełnych tabel do narracji pre-weekend."
```

```yaml
source_id: "NYT-AP-1982-02-10"
title: "Argentine Grand Prix Removed From Agenda"
author_or_organisation: "Associated Press via The New York Times"
publication_date: "1982-02-10"
event_date: "1982-02-09/10"
source_type: "PRESS"
contemporary: true
spoiler_risk: "none"
locator: "https://www.nytimes.com/1982/02/10/sports/argentine-grand-prix-removed-from-agenda.html — dateline AP Feb. 10, 1982; anulowanie Argentyny; Brazylia 21 marca jako kolejna runda"
access_date: "2026-08-05"
supports:
  - claim_id: "R03-CAL-01"
    scope: "Kolejną rundą Formuły 1 miała być Grand Prix Brazylii 21 marca."
  - claim_id: "R03-DEV-01"
    scope: "Federacja wycofała Grand Prix Argentyny; kryzys łączony ze sporem licencyjnym / strajkiem na Kyalami."
disagreement_notes: "Pełny tekst AP niedostępny w sesji (403); twierdzenia oparte na datowanym leadzie i snippecie Times."
notes: "Współczesna depesza; nie używać późniejszych narracji o Falklandach."
```

```yaml
source_id: "MS-MAR1982-SCENE"
title: "The Formula One Scene"
author_or_organisation: "D.S.J., Motor Sport"
publication_date: "1982-03"
event_date: "not-applicable"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/march-1982/32/formula-one-scene/ — March 1982, p. 32"
access_date: "2026-08-05"
supports:
  - claim_id: "R03-POL-01"
    scope: "Po karach z Kyalami kierowcy w Paryżu rozwiązali GPDA i powołali PRDA; wielu odmawiało zapłaty kar i sankcji."
  - claim_id: "R03-EXP-01"
    scope: "Jenkinson: Grand Prix Brazylii „looks distinctly shaky” — oczekiwanie, nie fakt."
  - claim_id: "R03-EXP-02"
    scope: "Przypisany komentarz o koszcie sporów dla kalendarza i ryzyku utraty płatnych rund."
  - claim_id: "R03-TEC-01"
    scope: "Ogłoszenie, że Brabham BT50–BMW nie pojawi się przed San Marino na Imoli 25 kwietnia; uzasadnienie PR o mocy silnika względem podwozia."
  - claim_id: "R03-POL-02"
    scope: "Po uregulowaniu zaległości wobec FOCA Grand Prix Hiszpanii przywrócono z datą w czerwcu; Holandia jako pierwsza rezerwa."
disagreement_notes: "Publication_date dnia unknown. Spekulacje o Long Beach / Indy-car — nie używane jako fakty."
notes: "Content-based availability: komentarz po anulowaniu Argentyny i przed wynikami Brazylii; izolować od chrome WWW."
```

```yaml
source_id: "MS-MAR1982-TRANSVAAL"
title: "Reflections in the Transvaal"
author_or_organisation: "D.S.J., Motor Sport"
publication_date: "1982-03"
event_date: "1982-01"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/march-1982/40/reflections-transvaal/ — March 1982, p. 40"
access_date: "2026-08-05"
supports:
  - claim_id: "R03-POL-03"
    scope: "Tydzień po Kyalami trybunał ukarał 29 kierowców po 5000 USD (dodatkowe 5000 dla uczestników Zolder); zawieszenia startów odroczone na dwa lata z warunkiem utraty startów przy kolejnym naruszeniu."
disagreement_notes: null
notes: "Content-based availability; publication_date dnia unknown. Użyte dla rozwoju po R01, nie dla wyniku Kyalami."
```

```yaml
source_id: "MS-MAR1982-NOTES"
title: "Notes on the cars and teams at Kyalami"
author_or_organisation: "D.S.J., Motor Sport"
publication_date: "1982-03"
event_date: "1982-01"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/march-1982/39/notes-cars-and-teams-kyalami/ — March 1982, p. 39"
access_date: "2026-08-05"
supports:
  - claim_id: "R03-ENT-01"
    scope: "Przypisany przegląd obsady i ekip widocznych na Kyalami (pary kierowców i mniejsze zespoły), użyteczny jako ciągłość peletonu po R01 — nie zamknięta lista zgłoszeń na Rio."
  - claim_id: "R03-ENT-02"
    scope: "Lotus: de Angelis #11 i Mansell #12 potwierdzeni na Kyalami."
  - claim_id: "R03-TEC-02"
    scope: "Na Kyalami Williams i część innych ekip: zbiornik wody z pompą hamulcową opisywany jako chłodzenie tarcz i „disposable ballast” względem minimum 580 kg."
  - claim_id: "R03-TEC-03"
    scope: "Alfa Romeo: nowy monokok z włókna węglowego ukryty w garażu na Kyalami; na tor 179; turbo V8 / nowe podwozie jeszcze nie raceworthy."
disagreement_notes: "Nie dowodzi niezmienionej listy zgłoszeń na Brazylia. R03-TEC-02 zachowane w ledgerze, ale po audycie spoilera nie użyte w reader-facing pre-weekend (unikanie outcome-shaped emphasis wobec Rio)."
notes: "Content-based availability dla post-Kyalami / pre-Brazil. Nie importować wyniku protestu z Rio."
```

```yaml
source_id: "MS-JAN1982-CAL"
title: "The 1982 International Racing Season"
author_or_organisation: "Motor Sport"
publication_date: "unknown"
event_date: "not-applicable"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/january-1982/35/the-1982-international-racing-season/ — January 1982, p. 35"
access_date: "2026-08-05"
supports:
  - claim_id: "R03-CAL-02"
    scope: "Przedsezonowa reprodukcja kalendarza FIA: Brazilian Grand Prix — Rio de Janeiro, 21 March 1982 jako runda 03."
disagreement_notes: null
notes: "Ten sam materiał co sezonowe CAL-01; publication_date dnia unknown; content-based availability."
```

```yaml
source_id: "UPI-CALENDAR-1981-10-09"
title: "There will be 16 Formula One Grand Prix races..."
author_or_organisation: "United Press International"
publication_date: "1981-10-09"
event_date: "1981-10-09"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.upi.com/Archives/1981/10/09/There-will-be-16-Formula-One-Grand-Prix-races/3902371448000/ — pozycja Rio de Janeiro, Brazil, March 21"
access_date: "2026-08-05"
supports:
  - claim_id: "R03-CAL-02"
    scope: "Wczesne ogłoszenie FISA z datą Rio 21 marca."
disagreement_notes: "Ten sam wire zawiera rozbieżną datę Kyalami; nie używać UPI do daty RPA."
notes: "Wspiera obecność Rio 21 marca we wczesnym harmonogramie."
```

```yaml
source_id: "MS-MAR1978-BRA"
title: "The Brazilian Grand Prix Goes to Rio"
author_or_organisation: "A.H., Motor Sport"
publication_date: "1978-03"
event_date: "1978-01-29"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/march-1978/76/the-brazilian-grand-prix-goes-to-rio/"
access_date: "2026-08-05"
supports:
  - claim_id: "R03-VEN-01"
    scope: "Lokalizacja: Circuit Internacional do Rio de Janeiro, twisting autodromo ~20 mil na południe od Rio near Jacarepagua."
  - claim_id: "R03-CIR-01"
    scope: "Charakter układu: ciasne, następujące po sobie zakręty; porównanie do płaskiej Jaramy; długa prosta tylna."
  - claim_id: "R03-WX-01"
    scope: "Klimat: „insufferably hot”; jedyny ówczesny tor F1 w tropiku właściwym (Rio nieco na północ od Zwrotnika Koziorożca)."
disagreement_notes: null
notes: "Użyte wyłącznie jako cutoff-safe kontekst toru/klimatu z 1978. Wyniki i czasy treningu 1978 — poza zakresem."
```

```yaml
source_id: "MS-MAY1981-BRA"
title: "Brazilian Grand Prix"
author_or_organisation: "A.H., Motor Sport"
publication_date: "1981-05"
event_date: "1981-03-29"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/may-1981/64/brazilian-grand-prix-7/"
access_date: "2026-08-05"
supports:
  - claim_id: "R03-VEN-02"
    scope: "Nazwa Autodromo Riocentro; powrót GP Brazylii do Rio po Interlagos 1979–1980."
  - claim_id: "R03-CIR-02"
    scope: "Długość okrążenia podana jako 5,031 km (stan relacji 1981)."
  - claim_id: "R03-CIR-03"
    scope: "Ecclestone: Rio Autodromo „signed up” na kolejne dwa lata (oczekiwanie lokalizacji 1982 przy granicy 1981)."
  - claim_id: "R03-CIR-04"
    scope: "Uwagi o zakrętach o stałym promieniu i dwóch długich prostych (kontekst 1981)."
  - claim_id: "R03-WX-02"
    scope: "Weekend 1981 obejmował deszcz (zmienność klimatu z wcześniejszej wizyty; nie prognoza 1982)."
disagreement_notes: "Długość i umowa FOCA ze stanu 1981 nie są oficjalnym biuletynem 1982."
notes: "Wyniki, kwalifikacje i polityka Lotus 88 z 1981 — poza zakresem narracji R03 pre-weekend."
```

```yaml
source_id: "MS-APR1982-BRA"
title: "Brazilian Grand Prix"
author_or_organisation: "A.H., Motor Sport"
publication_date: "1982-04"
event_date: "1982-03-21"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/april-1982/70/brazilian-grand-prix-10/ — pełna relacja April 1982: przedstart, Race, wynik na mecie Piquet–Rosberg–Prost, podium/upadek; wstęp o disposable ballast; brak narracji DSQ w tekście A.H."
access_date: "2026-08-05"
supports:
  - claim_id: "R03-PR-SES-01"
    scope: "Trening w dusznej, wilgotnej atmosferze; wyboisty tor; podpory szyi i przewody tlenowe; limit dwóch kompletów opon kwalifikacyjnych."
  - claim_id: "R03-PR-Q-01"
    scope: "Pole Prost 1:28.808; Villeneuve 1:29.173; Rosberg 1:29.358; Arnoux 1:30.121; Piquet 1:30.281; kolejność czołówki: Prost, Villeneuve, Rosberg, Arnoux, Lauda, Reutemann, Piquet, Pironi, Patrese."
  - claim_id: "R03-PR-CAR-01"
    scope: "Brabham odłożył BT50–BMW; nowe BT49D–Cosworth z hamulcami z włókna węglowego dla Piqueta i Patrese."
  - claim_id: "R03-PR-CAR-02"
    scope: "Debiuty / nowe auta widoczne w kwalifikacjach: Ferrari 126C2, Alfa Romeo 182, Lotus 91 (Mansell czasowo na zapasowym 87)."
  - claim_id: "R03-PR-ENT-01"
    scope: "Baldi zakwalifikował Arrowsa; Henton nie; Laffite/Cheever na końcu pola; cytat Laffite’a o wadze JS17 vs butelki wody."
  - claim_id: "R03-PR-TYR-01"
    scope: "Villeneuve świadomy twardszych opon niż Williams/Brabham na pełnych bakach; limit dwóch kompletów kwalifikacyjnych."
  - claim_id: "R03-PR-POL-01"
    scope: "Od początku treningów Ferrari i Renault zapowiadały formalny protest przy zwycięstwie FOCA „featherweight”; zbiorniki wody opisywane jako chłodzenie hamulców / dojście do 580 kg."
  - claim_id: "R03-PR-DIST-01"
    scope: "Dystans imprezy 63 okrążenia (wprowadzenie relacji)."
  - claim_id: "R03-PO-TOP6-01"
    scope: "Kolejność na mecie 1–6: Piquet, Rosberg, Prost, Watson, Mansell, Alboreto."
  - claim_id: "R03-PO-POD-01"
    scope: "Piquet zwycięzca na mecie; upadek na podium; Rosberg cytat o will power; strata Rosberga „just under 12 sec”."
  - claim_id: "R03-PO-RACE-01"
    scope: "Narracja: Villeneuve start/prowadzenie; walka Piquet–Rosberg; wypadek Villeneuve’a na hairpinie; Patrese wyczerpanie; procesja do mety."
  - claim_id: "R03-PO-BALLAST-01"
    scope: "Kontekst disposable ballast / topping-up do 580 kg; FOCA vs Ferrari/Renault."
disagreement_notes: "OCR/model: tekst mówi „Renault RE36B” (prawdopodobnie RE30B); Williams „FW07C” vs inne bazy „FW07D”; ATS „D6” vs Autosport „D5”. Strata Rosberga „<12 s” vs bazy ~9 s — zachować MS jako przypisane."
notes: "Dla post-race: wynik na mecie i narracja użyteczne. Tekst A.H. nie opisuje DSQ — zgodne z cutoff (stewardzi odrzucili protest)."
```

```yaml
source_id: "AS-1982-BRA"
title: "Grand Prix Gold: 1982 Brazilian GP (Autosport contemporary report reprint)"
author_or_organisation: "Autosport / Nigel Roebuck (reprint page)"
publication_date: "unknown"
event_date: "1982-03-21"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.autosport.com/f1/news/grand-prix-gold-1982-brazilian-gp-5099000/5099000/ — współczesny korpus Roebucka (Entry/practice + The Grand Prix) do zamknięcia z protestem/stewardami; QUARANTINE: kursywa redakcyjna 2012 „*Piquet and Rosberg would later be disqualified…”; podpis „walking away from F1” przy Reutemannie"
access_date: "2026-08-05"
supports:
  - claim_id: "R03-PR-CUT-01"
    scope: "Kierowcy na polu czekali na 13:00 lokalnie — prowizoryczny raport współczesny; brak oficjalnego programu w pakiecie."
  - claim_id: "R03-PR-WU-01"
    scope: "Poranna rozgrzewka: najszybszy Piquet, potem de Cesaris i Lauda; bez pełnej tabeli czasów."
  - claim_id: "R03-PR-COND-01"
    scope: "Niedziela przed startem: bardzo gorąco ze słońcem po dusznych, pochmurnych dniach kwalifikacji."
  - claim_id: "R03-PR-ENT-02"
    scope: "DNPQ Paletti (wypadek piątkowy poranek); DNQ Warwick i Fabi (Toleman), Guerrero (Ensign); Henton (misfire); Cheever ostatni w polu wypychając Fabiego."
  - claim_id: "R03-PR-TYR-02"
    scope: "Ferrari na mieszankach B Goodyear; Williams i Brabham na C — informacja przedstartowa."
  - claim_id: "R03-PO-TOP6-01"
    scope: "Kolejność na mecie 1–6: Piquet, Rosberg, Prost, Watson, Mansell, Alboreto."
  - claim_id: "R03-PO-RACE-01"
    scope: "Szczegółowa narracja okrążeń, kolizji, Villeneuve lap 30, Patrese exhaustion, Alboreto past Winkelhock."
  - claim_id: "R03-PO-PROT-01"
    scope: "Piccinini i Sage protestują dwa pierwsze auta; cytat Sage’a o zbiornikach wody."
  - claim_id: "R03-PO-STEW-01"
    scope: "Stewardzi imprezy odrzucają protest; sprawa idzie do brazylijskiego ASN, „presumably to Paris”."
  - claim_id: "R03-PO-RXN-01"
    scope: "Reakcje: crowd, Villeneuve quote, Rosberg straight-line, Blash/Patrese, anonymous gladiator quote."
disagreement_notes: "Strona WWW datowana 2012 jako reprint; treść korpusu to współczesny raport weekendowy. Kursywa DSQ i podpis o Reutemannie — materiał późniejszy."
notes: "Content-based availability: korpus wyścigu + protest/stewardzi IN cutoff; editorial DSQ OUT."
```

```yaml
source_id: "ARCHIVE-R02-STAND"
title: "Klasyfikacja po terminie Grand Prix Argentyny (mirror po Kyalami)"
author_or_organisation: "F1 Time Capsule archive"
publication_date: "not-applicable"
event_date: "1982-03-07"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/02-argentine-grand-prix/standings-after.md"
access_date: "2026-08-05"
supports:
  - claim_id: "R03-PO-STD-01"
    scope: "Stan przed Rio = po pustej Argentynie: Prost 9, Reutemann 6, Arnoux 4, Lauda 3, Rosberg 2, Watson 1; Renault 13, Williams 8, McLaren 4."
disagreement_notes: "Skala punktowa prowizoryczna (1982-R01-PTS-01)."
notes: "Baza arytmetyki standings-after R03."
```

```yaml
source_id: "GPR-1982-R03"
title: "1982 Brazilian Grand Prix — archival result reconstruction"
author_or_organisation: "GP Racing Stats"
publication_date: "unknown"
event_date: "1982-03-21"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://gpracingstats.com/seasons/1982-world-championship/1982-brazilian-grand-prix/ — wiersze DQ z czasami Piquet/Rosberg; QUARANTINE: championship tables i punkty po DSQ; winner=Prost framing"
access_date: "2026-08-05"
supports:
  - claim_id: "R03-PO-TIME-DB"
    scope: "Prowizoryczne absoluty: Piquet 1:43:56.760; Rosberg 1:44:05.737 — tylko aparat, nie tabela reader-facing jako oficjalny wynik."
disagreement_notes: "Baza pokazuje DSQ i reklasyfikację; nie używać tabel mistrzostw ani Prost-as-winner przy cutoff R03-PO."
notes: "Izolowane czasy on-road; konflikt z MS gap Rosberga."
```

```yaml
source_id: "F1-1982-R03-GRID"
title: "Formula 1 starting grid archive: Brazil 1982"
author_or_organisation: "Formula 1"
publication_date: "unknown"
event_date: "1982-03-21"
source_type: "RESULT"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.formula1.com/en/results/1982/races/438/brazil/starting-grid"
access_date: "2026-08-05"
supports:
  - claim_id: "R03-PR-GRID-01"
    scope: "26-wierszowe pole z czasami od Prost 1:28.808 do Cheever 1:35.288; data wydarzenia 21 Mar 1982."
disagreement_notes: "Archiwum nie jest oficjalnym biuletynem FIA z 1982; czasy czołówki zgodne z MS-APR1982-BRA."
notes: "Nie współczesne archiwum; użyte wyłącznie jako prowizoryczna tabela pola, izolowana od wyniku wyścigu."
```

```yaml
source_id: "RSC-1982-R03-GRID"
title: "Jacarepagua 1982 Formula 1 grid"
author_or_organisation: "Racing Sports Cars"
publication_date: "unknown"
event_date: "1982-03-21"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.racingsportscars.com/f1/grid/Jacarepagua-1982-03-21-14258.html"
access_date: "2026-08-05"
supports:
  - claim_id: "R03-PR-GRID-01"
    scope: "Prowizoryczna rekonstrukcja pola z czasami kwalifikacyjnymi zgodnymi z F1.com dla czołówki (Prost 1:28.808 itd.)."
disagreement_notes: "Oznaczenia podwozi (np. FW07D) mogą różnić się od Motor Sport (FW07C)."
notes: "Nie współczesna baza; wyłącznie tabela pola."
```

```yaml
source_id: "STATS-1982-R03"
title: "Brazil 1982 — result / non-qualifiers"
author_or_organisation: "STATS F1"
publication_date: "unknown"
event_date: "1982-03-21"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.statsf1.com/en/1982/bresil/classement.aspx — pozycje nq/npq: Fabi, Guerrero, Henton, Warwick, Paletti"
access_date: "2026-08-05"
supports:
  - claim_id: "R03-PR-ENT-02"
    scope: "Lista DNQ: Fabi, Guerrero, Henton, Warwick; DNPQ: Paletti."
disagreement_notes: "Baza zawiera wynik wyścigu — używać wyłącznie wierszy nq/npq."
notes: "Nie współczesna baza; wynik i DSQ poza zakresem pre-race."
```

## Conflict and uncertainty index

| Uncertainty ID | Claim IDs | Source IDs | Status at cutoff | Note |
| --- | --- | --- | --- | --- |
| UNC-R03-CUT | R03-CUT-01 | — | unresolved | Brak oficjalnego programu 1982 z dniem/godziną pierwszej sesji |
| UNC-R03-GO | R03-EXP-01, R03-CAL-01 | MS-MAR1982-SCENE, NYT-AP-1982-02-10 | open | „Shaky” vs zaplanowana następna runda; brak depeszy potwierdzającej 8–19 Mar |
| UNC-R03-ENT | R03-ENT-01 | MS-MAR1982-NOTES | open | Przegląd po Kyalami ≠ zamknięta lista zgłoszeń Rio |
| UNC-R03-NAME | R03-VEN-01, R03-VEN-02 | MS-MAR1978-BRA, MS-MAY1981-BRA | noted | Aliasy Jacarepaguá / Riocentro / Circuit Internacional — ten sam kompleks |
| UNC-R03-WATER | R03-TEC-02 | MS-MAR1982-NOTES | unused-in-PW | Fakt Kyalami zachowany w ledgerze; nie użyty w prose pre-weekend po audycie spoilera |
| UNC-R03-PR-CUT | R03-PR-CUT-01 | AS-1982-BRA | open | 13:00 lokalnie z Autosportu; brak oficjalnego programu |
| UNC-R03-PR-GRID | R03-PR-GRID-01 | F1-1982-R03-GRID, RSC-1982-R03-GRID, MS-APR1982-BRA | open | Brak oficjalnego biuletynu FIA; rekonstrukcje archiwalne |
| UNC-R03-PR-WU | R03-PR-WU-01 | AS-1982-BRA | open | Kolejność rozgrzewki bez pełnych czasów |
| UNC-R03-PR-PEN | R03-PR-PEN-01 | — | open | Brak biuletynu kar przed startem w pakiecie |
| UNC-R03-PR-MODEL | R03-PR-CAR-02 | MS-APR1982-BRA, RSC-1982-R03-GRID, AS-1982-BRA | noted | Rozbieżne oznaczenia podwozi (RE36B/RE30B, FW07C/D, ATS D5/D6) |
| UNC-R03-PO-GAP | R03-PO-POD-01, R03-PO-TIME-DB | MS-APR1982-BRA, GPR-1982-R03 | open | MS „just under 12 s” vs baza ~9 s dla Rosberga |
| UNC-R03-PO-RES | R03-PO-TOP6-01 | MS-APR1982-BRA, AS-1982-BRA | open | Brak oficjalnego biuletynu FIA; pełna klasyfikacja poza top 6 niepełna w MS/AS |
| UNC-R03-PO-STEW | R03-PO-STEW-01 | AS-1982-BRA | open | Godzina decyzji stewardów unknown; treść tylko z relacji Autosportu |
| UNC-R03-PO-DSQ | — | AS-1982-BRA editorial; bazy | quarantined | Późniejsze wykluczenie Piquet/Rosberg poza cutoff |

## Pre-weekend claim map (R03-PW)

| claim_id | Scope | Source IDs |
| --- | --- | --- |
| `R03-STD-01` | Punkty bez zmian po pustej Argentynie = migawka po Kyalami | `ARCHIVE-R01-STAND` |
| `R03-CAL-01` | Następna runda: Brazylia 21 marca | `NYT-AP-1982-02-10` |
| `R03-CAL-02` | Rio de Janeiro 21 marca w kalendarzu przedsezonowym | `MS-JAN1982-CAL`, `UPI-CALENDAR-1981-10-09` |
| `R03-DEV-01` | Anulowanie Argentyny / kontekst sporu | `NYT-AP-1982-02-10` |
| `R03-POL-01` | GPDA→PRDA, odmowa kar | `MS-MAR1982-SCENE` |
| `R03-POL-02` | Hiszpania czerwiec; Holandia rezerwa | `MS-MAR1982-SCENE` |
| `R03-POL-03` | Kary trybunału po Kyalami | `MS-MAR1982-TRANSVAAL` |
| `R03-EXP-01` | Brazylia „distinctly shaky” | `MS-MAR1982-SCENE` |
| `R03-EXP-02` | Ryzyko utraty płatnych rund | `MS-MAR1982-SCENE` |
| `R03-ENT-01` | Przegląd obsady po Kyalami | `MS-MAR1982-NOTES` |
| `R03-ENT-02` | Lotus de Angelis/Mansell na Kyalami | `MS-MAR1982-NOTES` |
| `R03-VEN-01` | Lokalizacja Jacarepaguá / Circuit Internacional | `MS-MAR1978-BRA` |
| `R03-VEN-02` | Autódromo Riocentro; powrót do Rio | `MS-MAY1981-BRA` |
| `R03-CIR-01` | Charakter układu (ciasne zakręty, Jarama) | `MS-MAR1978-BRA` |
| `R03-CIR-02` | Długość 5,031 km (1981) | `MS-MAY1981-BRA` |
| `R03-CIR-03` | Umowa FOCA na Rio (oczekiwanie 1982) | `MS-MAY1981-BRA` |
| `R03-CIR-04` | Zakręty o stałym promieniu / proste (1981) | `MS-MAY1981-BRA` |
| `R03-WX-01` | Upał tropikalny (1978) | `MS-MAR1978-BRA` |
| `R03-WX-02` | Deszcz możliwy (1981) | `MS-MAY1981-BRA` |
| `R03-TEC-01` | BT50–BMW odłożone do Imoli (bez wniosków o silniku na Rio) | `MS-MAR1982-SCENE` |
| `R03-TEC-03` | Alfa: nowy monokok niejeżdżony na Kyalami | `MS-MAR1982-NOTES` |

## Pre-race claim map (R03-PR)

| claim_id | Scope | Source IDs |
| --- | --- | --- |
| `R03-PR-SES-01` | Warunki treningu, wyboje, podpory szyi/tlen, 2 komplety opon | `MS-APR1982-BRA` |
| `R03-PR-Q-01` | Czasy i kolejność czołówki kwalifikacji | `MS-APR1982-BRA`, `F1-1982-R03-GRID` |
| `R03-PR-GRID-01` | Pełne 26-wierszowe pole z czasami | `F1-1982-R03-GRID`, `RSC-1982-R03-GRID` |
| `R03-PR-CAR-01` | Brabham BT49D–Cosworth zamiast BT50–BMW | `MS-APR1982-BRA` |
| `R03-PR-CAR-02` | Nowe auta: 126C2, Alfa 182, Lotus 91 / zapas 87 | `MS-APR1982-BRA` |
| `R03-PR-ENT-01` | Baldi vs Henton; Laffite/Cheever i cytat o wadze | `MS-APR1982-BRA` |
| `R03-PR-ENT-02` | DNQ Warwick/Fabi/Guerrero/Henton; DNPQ Paletti | `AS-1982-BRA`, `STATS-1982-R03`, `MS-APR1982-BRA` |
| `R03-PR-TYR-01` | Limit opon kwali; Villeneuve o twardszych oponach | `MS-APR1982-BRA` |
| `R03-PR-TYR-02` | Ferrari B vs Williams/Brabham C | `AS-1982-BRA` |
| `R03-PR-POL-01` | Zapowiedź protestu Ferrari/Renault / woda–balast | `MS-APR1982-BRA` |
| `R03-PR-DIST-01` | 63 okrążenia | `MS-APR1982-BRA`, `AS-1982-BRA` |
| `R03-PR-CUT-01` | Oczekiwanie na 13:00 lokalnie | `AS-1982-BRA` |
| `R03-PR-WU-01` | Rozgrzewka: Piquet, de Cesaris, Lauda | `AS-1982-BRA` |
| `R03-PR-COND-01` | Niedziela: upał ze słońcem | `AS-1982-BRA` |
| `R03-PR-PEN-01` | Brak biuletynu kar w pakiecie | — |

## Post-race claim map (R03-PO)

| claim_id | Scope | Source IDs |
| --- | --- | --- |
| `R03-PO-TOP6-01` | Na mecie 1–6: Piquet, Rosberg, Prost, Watson, Mansell, Alboreto | `MS-APR1982-BRA`, `AS-1982-BRA` |
| `R03-PO-POD-01` | Podium; upadek Piqueta; cytat Rosberga; strata ≈&lt;12 s (MS) | `MS-APR1982-BRA`, `AS-1982-BRA` |
| `R03-PO-RACE-01` | Narracja wyścigu, kluczowe fazy, wycofania | `MS-APR1982-BRA`, `AS-1982-BRA` |
| `R03-PO-PROT-01` | Protest Piccinini/Sage vs auta 1–2; cytat Sage’a | `AS-1982-BRA` |
| `R03-PO-STEW-01` | Stewardzi imprezy odrzucają; ASN / presumably Paris | `AS-1982-BRA` |
| `R03-PO-BALLAST-01` | Kontekst disposable ballast / 580 kg | `MS-APR1982-BRA` |
| `R03-PO-RXN-01` | Reakcje współczesne (crowd, Villeneuve, Blash, gladiator) | `AS-1982-BRA`, `MS-APR1982-BRA` |
| `R03-PO-STD-01` | Stan przed Rio = mirror po Argentynie/Kyalami | `ARCHIVE-R02-STAND` |
| `R03-PO-PTS-01` | Punkty Rio: 9–6–4–3–2–1 dla top 6 na mecie; sumy standings-after | `MS-APR1982-BRA`, `AS-1982-BRA`, `ARCHIVE-R02-STAND` |
| `R03-PO-TIME-DB` | Absoluty czasów tylko aparat (prowizoryczne) | `GPR-1982-R03` |
