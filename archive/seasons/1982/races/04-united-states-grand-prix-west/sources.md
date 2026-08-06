# United States Grand Prix West — source ledger

To kanoniczny rejestr źródeł folderu rundy. Dokumenty treści cytują
`source_id` i `claim_id`; nie prowadzą konkurencyjnych list źródeł.

## Source entry

```yaml
source_id: "ARCHIVE-R03-STAND"
title: "Klasyfikacja po Grand Prix Brazylii"
author_or_organisation: "F1 Time Capsule archive (standings-after.md R03)"
publication_date: "not-applicable"
event_date: "1982-03-21"
source_type: "ARCHIVE"
contemporary: true
spoiler_risk: "none"
locator: "archive/seasons/1982/races/03-brazilian-grand-prix/standings-after.md"
access_date: "2026-08-06"
supports:
  - claim_id: "R04-PW-STD-01"
    scope: "Prowizoryczna kolejność i punkty po Rio (po odrzuceniu protestu przez stewardów imprezy): Prost 13, Piquet 9, Rosberg 8, Reutemann 6, Arnoux 4 / Watson 4, Lauda 3, Mansell 2, Alboreto 1; Renault 17, Williams 14, Brabham 9, McLaren 7, Lotus 2, Tyrrell 1."
  - claim_id: "R04-PO-STD-01"
    scope: "Stan przed Long Beach = prowizoryczna tabela po Rio (jak wyżej); baza arytmetyki standings-after R04."
disagreement_notes: "Skala punktowa prowizoryczna; brak oficjalnego biuletynu FIA w pakiecie R03; ścieżka ASN otwarta."
notes: "Wskaźnik do kanonicznej migawki; nie kopiować pełnych tabel do narracji."
```

```yaml
source_id: "AS-1982-BRA"
title: "Grand Prix Gold: 1982 Brazilian GP (Autosport contemporary report reprint)"
author_or_organisation: "Autosport / Nigel Roebuck (Grand Prix Gold reprint)"
publication_date: "unknown"
event_date: "1982-03-21"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.autosport.com/f1/news/grand-prix-gold-1982-brazilian-gp-5099000/5099000/ — korpus współczesny o proteście Ferrari/Renault, odrzuceniu przez stewardów imprezy i skierowaniu do brazylijskiego ASN; kwarantanna kursywy/edytorskich dopisków o późniejszym DSQ"
access_date: "2026-08-05"
supports:
  - claim_id: "R04-PW-POL-01"
    scope: "Protest Ferrari/Renault przeciw dwóm pierwszym w Rio; stewardzi imprezy odrzucili; sprawa dalej ASN / przypuszczalnie Paryż — bez zmiany wyniku na mecie przy granicy po Rio."
disagreement_notes: "Reprint 2012 może zawierać późniejsze dopiski; izolować od werdyktu FISA z kwietnia."
notes: "Użyte dla otwartego statusu protestu przed Long Beach; nie jako dowód późniejszego wykluczenia."
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
locator: "https://www.motorsportmagazine.com/archive/article/april-1982/70/brazilian-grand-prix-10/ — April 1982; kontekst zbiorników wody / minimum 580 kg i sporu o masę"
access_date: "2026-08-05"
supports:
  - claim_id: "R04-PW-TEC-02"
    scope: "Współczesny opis praktyki zbiorników wody / sporu o minimum 580 kg wokół weekendu w Rio — otwarty wątek regulaminowy przed Long Beach."
disagreement_notes: "Publication_date dnia unknown; nie używać relacji wyścigu Rio poza kontekstem sporu o masę."
notes: "Content-based availability dla kontekstu protestu; bez foreshadowingu DSQ."
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
  - claim_id: "R04-PW-TEC-01"
    scope: "Ogłoszenie, że Brabham BT50–BMW nie pojawi się przed San Marino na Imoli 25 kwietnia."
  - claim_id: "R04-PW-POL-03"
    scope: "Tło po Kyalami: GPDA→PRDA, kary, anulowana Argentyna; kalendarzowa kruchość płatnych rund."
  - claim_id: "R04-PW-EXP-01"
    scope: "Jenkinson: przy dalszym chaosie Chris Pook mógłby teoretycznie rozważyć IndyCar zamiast F1 w Long Beach."
disagreement_notes: "Publication_date dnia unknown."
notes: "Content-based availability; spekulacje o Long Beach / Indy-car tylko jako atrybuowana opinia."
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
  - claim_id: "R04-PW-POL-03"
    scope: "Kary trybunału po Kyalami (29 kierowców; zawieszenia odroczone) jako tło polityczne sezonu."
disagreement_notes: null
notes: "Content-based availability; publication_date dnia unknown."
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
  - claim_id: "R04-PW-ENT-02"
    scope: "Przypisany przegląd obsady/ekip widocznych na Kyalami jako ciągłość peletonu — nie zamknięta lista zgłoszeń na Long Beach."
disagreement_notes: "Nie dowodzi niezmienionej listy poza Andretti↔Reutemann."
notes: "Użyte tylko jako szkielet ciągłości; delta entry z MS-MAY1982-USW."
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
  - claim_id: "R04-PW-CAL-01"
    scope: "Przedsezonowa reprodukcja kalendarza FIA: United States Grand Prix West — Long Beach, 4 April 1982 jako runda 04."
disagreement_notes: null
notes: "Ten sam materiał co sezonowe CAL-01; publication_date dnia unknown; content-based availability."
```

```yaml
source_id: "MS-MAY1982-USW"
title: "United States Grand Prix West"
author_or_organisation: "D.S.J., Motor Sport"
publication_date: "1982-05"
event_date: "1982-04-02/04"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/may-1982/46/united-stateswest-grand-prix/ — May 1982, p. 46; pre-weekend/pre-race jak wcześniej; post-race: sekcja Race (green light→meta), kolejność na drodze Lauda–Rosberg–Villeneuve–Patrese–Alboreto, protest Tyrrella o twin-wing (bez jawnego werdyktu DSQ w zamknięciu tekstu)"
access_date: "2026-08-06"
supports:
  - claim_id: "R04-PW-CAL-02"
    scope: "Jeden wolny weekend między Brazylią a Long Beach; zespoły przyjechały do Kalifornii prosto z Brazylii."
  - claim_id: "R04-PW-DEV-01"
    scope: "Przy przyjeździe: Reutemann „once more retired, this time for good”."
  - claim_id: "R04-PW-ENT-01"
    scope: "Frank Williams podpisał Mario Andrettiego na ten jeden wyścig; zobowiązania IndyCar uniemożliwiały sezonowy kontrakt."
  - claim_id: "R04-PW-ENT-03"
    scope: "Jedyna poważna zmiana entry vs Brazylia: Andretti zamiast Reutemanna."
  - claim_id: "R04-PW-CIR-01"
    scope: "Przebudowa toru 1982 (Pook / LBGPA): nowa sekcja zamiast hairpina Shoreline, wydłużenie Linden, chicane na Shoreline (plan pitów 1983); tor nieco dłuższy."
  - claim_id: "R04-PW-CIR-02"
    scope: "Charakter toru ulicznego: betonowe ściany, nierówności, porównanie do Monaco."
  - claim_id: "R04-PW-CUT-01"
    scope: "Brak pre-practice na torze; poranna oficjalna sesja testowa rozpoczęta o 10:00 lokalnie w piątek — marker pierwszej sesji (z raportu majowego)."
  - claim_id: "R04-PW-ENT-04"
    scope: "Plan: zgłoszenie ~31; pięciu prekwalifikantów (Boesel, Paletti, Jarier, Warwick, Fabi) z limitu Concorde 30/26."
  - claim_id: "R04-PW-EXP-02"
    scope: "Przypisana spekulacja paddocku, że poziom morza i kręty tor mogą utrudnić turbom — oczekiwanie."
  - claim_id: "R04-PR-CUT-01"
    scope: "Planowany start ok. 13:05 lokalnie w niedzielę („at 1.05 p.m. on Sunday…”) — prowizoryczny marker z relacji, nie oficjalny program."
  - claim_id: "R04-PR-SESS-01"
    scope: "Format: piątek 10:00 test 1½ h + prekwali; piątkowa godzina kwali; sobotni test; sobota 13:00 kwali; niedziela ½ h rozgrzewka."
  - claim_id: "R04-PR-DIST-01"
    scope: "Dystans 75½ okrążeń; start i meta w różnych punktach toru."
  - claim_id: "R04-PR-PQ-01"
    scope: "Warwick DNPQ — misfire Hart cured too late."
  - claim_id: "R04-PR-Q-01"
    scope: "Pole de Cesaris 1:27.316; Lauda 1:27.436; narracja piątek–sobota (Patrese BT49C, Michelin/Prost, Arnoux pożar, Rosberg sprzęgło, Piquet Linden, twin-wing Ferrari, Michelin vs Goodyear)."
  - claim_id: "R04-PR-DNQ-01"
    scope: "DNQ: Fabi (≈0,16 s za Salazarem), Paletti, Serra, Baldi."
  - claim_id: "R04-PR-TYRE-01"
    scope: "Limit dwóch kompletów opon kwali; przewaga Michelin w sobotę; rozgrzewka McLaren: Lauda twarde / Watson miękkie."
  - claim_id: "R04-PR-WU-01"
    scope: "Niedzielna rozgrzewka ½ h; 26 starterów bez poważnych incydentów; bez pełnych czasów."
  - claim_id: "R04-PR-COND-01"
    scope: "Sesje pod clear blue skies; niedziela przed startem: cloudless sky, cool breeze, conditions perfect."
  - claim_id: "R04-PR-POL-01"
    scope: "Woda/580 kg; podane ważenia Williams/McLaren/Renault/Ferrari; Brabham nie zważony."
  - claim_id: "R04-PR-AERO-01"
    scope: "Ferrari twin rear aerofoil zamontowane w sobotę (Pironi, potem Villeneuve)."
  - claim_id: "R04-PO-RACE-01"
    scope: "Narracja Race: start de Cesaris/Arnoux, kolizja Giacomelli–Arnoux, Pironi/Prost, Lauda lead okr. 15, Andretti, Watson pit, de Cesaris mur ≈34, Cheever skrzynia, meta Lauda≈14 s przed Rosbergiem, Villeneuve 3. na drodze."
  - claim_id: "R04-PO-TOP-ROAD-01"
    scope: "Na drodze: Lauda, Rosberg, Villeneuve, Patrese, Alboreto; Lotus 91 6. i 8. z Watsonem między nimi."
  - claim_id: "R04-PO-PROT-TYR-01"
    scope: "Po mecie Ken Tyrrell protestuje twin-wing Villeneuve’a jako mis-interpretation of the rules (tekst nie podaje werdyktu DSQ)."
  - claim_id: "R04-PO-RXN-01"
    scope: "Reakcje: Dennis/Barnard; Lauda o marginesie ≈3 cale; Jenkinson o precyzji vs ścianach."
disagreement_notes: "Publication_date dnia unknown. Tekst miesza przyjazd, sesje i wyścig. Zamknięcie MS kończy się na proteście Tyrrella bez jawnego DSQ — werdykt z UPI/AS. FW07C w MS vs FW07D w niektórych bazach."
notes: "Content-based availability. Pre-weekend/pre-race: izolować od Race. Post-race: Race + protest Tyrrella; DSQ koroborować UPI/AS."
```

```yaml
source_id: "RSC-1982-R04-GRID"
title: "Long Beach 1982 Formula 1 qualifying results"
author_or_organisation: "Racing Sports Cars"
publication_date: "unknown"
event_date: "1982-04-04"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.racingsportscars.com/f1/results/qualifying/Long_Beach-1982-04-04.html — pełna tabela Q 1–31 z czasami"
access_date: "2026-08-05"
supports:
  - claim_id: "R04-PR-GRID-01"
    scope: "26-wierszowe pole z czasami od de Cesaris 1:27.316 do Salazar 1:31.825; DNQ Fabi/Paletti/Serra/Baldi; Warwick bez czasu (DNPQ)."
disagreement_notes: "Oznaczenia podwozi (FW07D vs MS FW07C); nie oficjalny biuletyn FIA."
notes: "Nie współczesna baza; wyłącznie tabela kwalifikacji/pola, izolowana od wyniku wyścigu."
```

```yaml
source_id: "SILH-1982-USW"
title: "1982 Grand Prix USA-West — Long Beach archive page"
author_or_organisation: "silhouet.com motorsport archive"
publication_date: "unknown"
event_date: "1982-04-04"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.silhouet.com/motorsport/archive/f1/1982/82usaw.html — dystans; grid; results po DSQ; FL Lauda 1:30.831; leaders de Cesaris→Lauda"
access_date: "2026-08-06"
supports:
  - claim_id: "R04-PR-DIST-01"
    scope: "Długość okrążenia 3,428 km; dystans wyścigu 258,814 km przy 75,5 okrążeniach."
  - claim_id: "R04-PR-GRID-01"
    scope: "Kolejność pola i straty do pole; DNPQ Warwick; DNQ Fabi–Baldi — koroboracja RSC."
  - claim_id: "R04-PO-CLS-01"
    scope: "Klasyfikacja po DSQ: Lauda 1:58:25.318, Rosberg +14.660, Patrese +1:18.143, Alboreto +1:20.947, de Angelis −1 okr., Watson −1 okr.; Villeneuve DSQ; FL Lauda 1:30.831 okr. 12."
disagreement_notes: "Nie oficjalny biuletyn; numery okrążeń DNF częściowo konfliktują z RSC/AS (np. Cheever)."
notes: "Pre-race: dystans/grid. Post-race: czasy i kolejność po DSQ; koroboracja z UPI/AS/RSC."
```

```yaml
source_id: "UPI-1982-04-22-IMOLA"
title: "The controversy-plagued San Marino Formula One Grand Prix race..."
author_or_organisation: "United Press International"
publication_date: "1982-04-22"
event_date: "1982-04-19/22"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.upi.com/Archives/1982/04/22/The-controversy-plagued-San-Marino-Formula-One-Grand-Prix-race/6164388299600/ — FISA Monday ruling annulling Brazil 1–2 (Piquet/Rosberg); FOCA Imola boycott talk"
access_date: "2026-08-05"
supports:
  - claim_id: "R04-PW-QUAR-01"
    scope: "Dowód, że publiczny werdykt FISA unieważniający 1–2 z Rio datuje się na poniedziałek ≈19–20 kwietnia 1982 — PO Long Beach — i dlatego jest zakazany jako fakt przy cutoff post-race Long Beach."
  - claim_id: "R04-PO-QUAR-FISA-01"
    scope: "Negatywny dowód chronologii: FISA Brazil DSQ po Long Beach — poza reader-facing post-race LB."
disagreement_notes: null
notes: "Źródło kwarantanny / negatywnego dowodu chronologii; nie cytować w reader-facing prose jako stanu przy cutoff LB."
```

```yaml
source_id: "UPI-1982-04-06-LB"
title: "Canadian Gilles Villeneuve has been disqualified from Sunday's Long..."
author_or_organisation: "United Press International"
publication_date: "1982-04-06"
event_date: "1982-04-04/05"
source_type: "PRESS"
contemporary: true
spoiler_risk: "none"
locator: "https://www.upi.com/Archives/1982/04/06/Canadian-Gilles-Villeneuve-has-been-disqualified-from-Sundays-Long/2854386917200/ — DSQ Villeneuve; Monday private session; Pook announcement ~12 h later; Ferrari protest vs McLaren disallowed; de Angelis fine $2000; appeals open"
access_date: "2026-08-06"
supports:
  - claim_id: "R04-PO-DSQ-01"
    scope: "Villeneuve wykluczony z 3. miejsca za illegal rear wing; pozostali przesunięci o jedno miejsce; Watson zyskuje punkt w mistrzostwach."
  - claim_id: "R04-PO-STEW-01"
    scope: "Decyzja early Monday private session; Chris Pook ogłosił po prawie 12 godzinach."
  - claim_id: "R04-PO-PROT-FER-01"
    scope: "Ferrari protestowało McLaren/Laudę (procedure of scrutineering) — oddalone."
  - claim_id: "R04-PO-FINE-01"
    scope: "Grzywna 2000 USD dla de Angelisa i Lotusa za nieprawidłowe ustawienie na polu."
  - claim_id: "R04-PO-APP-01"
    scope: "Oba protesty i grzywna zaskarżone; decyzja apelacji może potrwać kilka miesięcy."
disagreement_notes: "AS-1982-USW opisuje protest Ferrari jako water tank vs McLaren i Williams — inna formuła niż UPI; zachować obie wersje w aparacie."
notes: "Kluczowe źródło datowane dla granicy post-race (poniedziałkowa decyzja + ogłoszenie)."
```

```yaml
source_id: "AS-1982-USW"
title: "Grand Prix Gold: 1982 US West GP (Autosport contemporary report reprint)"
author_or_organisation: "Autosport / Nigel Roebuck (Grand Prix Gold reprint)"
publication_date: "unknown"
event_date: "1982-04-04"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.autosport.com/f1/news/grand-prix-gold-1982-us-west-gp-5098995/5098995/ — korpus współczesny o wyścigu, kolejności po DSQ, protestach; kwarantanna kursywy/edytorskich dopisków reprintu"
access_date: "2026-08-06"
supports:
  - claim_id: "R04-PO-RACE-01"
    scope: "Szczegółowa narracja: Watson charge, Giacomelli–Arnoux, Lauda lead 15, Villeneuve spin vs Rosberg, Piquet/de Cesaris, Patrese vs Alboreto okr. 59, Cheever skrzynia."
  - claim_id: "R04-PO-CLS-01"
    scope: "Po blue-pencil Villeneuve: 3–6 Patrese, Alboreto, de Angelis, Watson; Rosberg prowadzi mistrzostwa przed Prostem."
  - claim_id: "R04-PO-PROT-TYR-01"
    scope: "Tyrrell protestuje twin-wing successfully."
  - claim_id: "R04-PO-PROT-FER-01"
    scope: "Piccinini protestuje dwa pierwsze auta (McLaren i Williams) na water tank — thrown out by organisers."
  - claim_id: "R04-PO-RXN-01"
    scope: "Ramka o hymnie austriackim / klasie Laudy; cytaty Villeneuve/Andretti z weekendu użyte ostrożnie."
disagreement_notes: "Reprint 2012 może zawierać późniejsze dopiski (np. kursywa o later DSQ); izolować. Konflikt z UPI co do opisu protestu Ferrari."
notes: "Content-based availability korpusu współczesnego; nie używać foreshadowingu sezonu ani FISA Brazil."
```

```yaml
source_id: "RSC-1982-R04-RES"
title: "Long Beach 1982 Formula 1 race results"
author_or_organisation: "Racing Sports Cars"
publication_date: "unknown"
event_date: "1982-04-04"
source_type: "DATABASE"
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.racingsportscars.com/f1/results/Long_Beach-1982-04-04.html — tabela wyników po DSQ; DNF z przyczynami; Villeneuve DSQ illegal rear wing"
access_date: "2026-08-06"
supports:
  - claim_id: "R04-PO-CLS-01"
    scope: "Koroboracja kolejności 1–10 po DSQ i statusu Villeneuve DSQ."
  - claim_id: "R04-PO-DNF-01"
    scope: "Lista DNF z przypisanymi przyczynami (częściowo konflikt numerów okrążeń vs SILH/AS)."
disagreement_notes: "Nie biuletyn FIA; oznaczenia podwozi FW07D vs MS FW07C."
notes: "Użyte do koroboracji klasyfikacji po DSQ; narrację okrążeń brać z MS/AS przy konflikcie."
```

## Conflict and uncertainty index

| Uncertainty ID | Claim IDs | Source IDs | Status at cutoff | Note |
| --- | --- | --- | --- | --- |
| UNC-R04-PW-CUT-01 | R04-PW-CUT-01 | MS-MAY1982-USW | open | Zegar 10:00 z raportu majowego; brak niezależnego programu. |
| UNC-R04-PW-REU-01 | R04-PW-DEV-01 | MS-MAY1982-USW | open | Brak datowanego wire’u z dniem emerytury; wtórne „5 dni po Rio”. |
| UNC-R04-PW-ASN-01 | R04-PW-POL-01 | AS-1982-BRA, UPI-1982-04-22-IMOLA | resolved-for-cutoff | Ścieżka ASN otwarta przed LB; FISA DSQ po LB — poza zakresem. |
| UNC-R04-PW-CIR-01 | R04-PW-CIR-01 | MS-MAY1982-USW | open | Brak oficjalnej długości km w pakiecie; MS: „slightly longer”. |
| UNC-R04-PW-WX-01 | — | — | open | Brak datowanej prognozy sprzed pierwszej sesji. |
| UNC-R04-PW-JONES-01 | — | — | open | Podejście do Jonesa nie potwierdzone źródłem współczesnym w pakiecie — pominięte w prose. |
| UNC-R04-PW-ENT-01 | R04-PW-ENT-02 | MS-MAR1982-NOTES, MS-MAY1982-USW | open | Brak oficjalnej listy FOCA sprzed piątku. |
| UNC-R04-PR-CUT-01 | R04-PR-CUT-01 | MS-MAY1982-USW | open | 13:05 z MS; brak oficjalnego programu. |
| UNC-R04-PR-GRID-01 | R04-PR-GRID-01 | RSC-1982-R04-GRID, SILH-1982-USW, MS-MAY1982-USW | open | Brak biuletynu FIA; rekonstrukcje + MS dla czołówki. |
| UNC-R04-PR-WU-01 | R04-PR-WU-01 | MS-MAY1982-USW | open | Rozgrzewka bez pełnych czasów. |
| UNC-R04-PR-PEN-01 | R04-PR-PEN-01 | — | open | Brak biuletynu kar przed startem w pakiecie. |
| UNC-R04-PR-MODEL-01 | R04-PR-GRID-01 | MS-MAY1982-USW, RSC-1982-R04-GRID | noted | FW07C (MS) vs FW07D (RSC). |
| UNC-R04-PR-DIST-01 | R04-PR-DIST-01 | MS-MAY1982-USW, SILH-1982-USW | open | 75½ z MS; km z bazy, nie biuletyn. |
| UNC-R04-PR-QUAR-RACE | — | — | resolved-for-cutoff | Narracja Race użyta przy post-race; wcześniej kwarantanna pre-race. |
| UNC-R04-PO-RES-01 | R04-PO-CLS-01 | UPI-1982-04-06-LB, MS-MAY1982-USW, AS-1982-USW, SILH-1982-USW, RSC-1982-R04-RES | open | Brak biuletynu FIA; czasy z baz. |
| UNC-R04-PO-PROT-01 | R04-PO-PROT-FER-01 | UPI-1982-04-06-LB, AS-1982-USW | open | Konflikt opisu protestu Ferrari: UPI scrutineering vs McLaren/Lauda; AS water tank vs McLaren+Williams. |
| UNC-R04-PO-LAPS-01 | R04-PO-RACE-01, R04-PO-DNF-01 | MS-MAY1982-USW, AS-1982-USW, SILH-1982-USW, RSC-1982-R04-RES | open | Rozbieżne numery okrążeń DNF (np. Cheever, de Cesaris 34/35). |
| UNC-R04-PO-APP-01 | R04-PO-APP-01 | UPI-1982-04-06-LB | open-deferred | Apelacje po LB — poza natychmiastowym cutoff do osobnej granicy. |
| UNC-R04-PO-FISA-01 | R04-PO-QUAR-FISA-01 | UPI-1982-04-22-IMOLA | quarantined | FISA Brazil DSQ ≈19–20 IV — poza cutoff LB. |

## Pre-weekend claim map (R04-PW)

| claim_id | Scope | Source IDs |
| --- | --- | --- |
| `R04-PW-STD-01` | Prowizoryczne punkty po Rio | `ARCHIVE-R03-STAND` |
| `R04-PW-POL-01` | Protest / ASN otwarta | `AS-1982-BRA` |
| `R04-PW-TEC-02` | Woda / 580 kg kontekst | `MS-APR1982-BRA` |
| `R04-PW-CAL-01` | Kalendarz LB 4 IV | `MS-JAN1982-CAL` |
| `R04-PW-CAL-02` | Przyjazd prosto z Brazylii | `MS-MAY1982-USW` |
| `R04-PW-DEV-01` | Emerytura Reutemanna | `MS-MAY1982-USW` |
| `R04-PW-ENT-01` | Andretti jeden wyścig | `MS-MAY1982-USW` |
| `R04-PW-ENT-03` | Delta entry Andretti | `MS-MAY1982-USW` |
| `R04-PW-ENT-04` | Procedura prekwali | `MS-MAY1982-USW` |
| `R04-PW-CIR-01` | Przebudowa toru | `MS-MAY1982-USW` |
| `R04-PW-CIR-02` | Charakter uliczny | `MS-MAY1982-USW` |
| `R04-PW-CUT-01` | Marker 10:00 piątek | `MS-MAY1982-USW` |
| `R04-PW-QUAR-01` | FISA Brazil po LB | `UPI-1982-04-22-IMOLA` |

## Pre-race claim map (R04-PR)

| claim_id | Scope | Source IDs |
| --- | --- | --- |
| `R04-PR-CUT-01` | Start ≈13:05 lokalnie | `MS-MAY1982-USW` |
| `R04-PR-SESS-01` | Format sesji Fri–Sun | `MS-MAY1982-USW` |
| `R04-PR-DIST-01` | 75½ okr.; km z bazy | `MS-MAY1982-USW`, `SILH-1982-USW` |
| `R04-PR-PQ-01` | Warwick DNPQ | `MS-MAY1982-USW` |
| `R04-PR-Q-01` | Narracja kwali / pole czasy czołówki | `MS-MAY1982-USW` |
| `R04-PR-GRID-01` | Pełne pole 1–26 z czasami | `RSC-1982-R04-GRID`, `SILH-1982-USW` |
| `R04-PR-DNQ-01` | Fabi, Paletti, Serra, Baldi | `MS-MAY1982-USW`, `RSC-1982-R04-GRID` |
| `R04-PR-TYRE-01` | Michelin / split McLaren | `MS-MAY1982-USW` |
| `R04-PR-WU-01` | Rozgrzewka bez pełnych czasów | `MS-MAY1982-USW` |
| `R04-PR-COND-01` | Warunki przed startem | `MS-MAY1982-USW` |
| `R04-PR-POL-01` | Ważenia / woda | `MS-MAY1982-USW` |
| `R04-PR-AERO-01` | Twin-wing Ferrari | `MS-MAY1982-USW` |
| `R04-PR-PEN-01` | Brak biuletynu kar | — |
| `R04-PR-STD-01` | Punkty przed startem = po Rio | `ARCHIVE-R03-STAND` |

## Post-race claim map (R04-PO)

| claim_id | Scope | Source IDs |
| --- | --- | --- |
| `R04-PO-RACE-01` | Narracja wyścigu, kluczowe fazy, wycofania | `MS-MAY1982-USW`, `AS-1982-USW` |
| `R04-PO-TOP-ROAD-01` | Kolejność na drodze Lauda–Rosberg–Villeneuve–… | `MS-MAY1982-USW`, `AS-1982-USW` |
| `R04-PO-CLS-01` | Klasyfikacja po DSQ 1–6 + Villeneuve DSQ; czasy | `UPI-1982-04-06-LB`, `AS-1982-USW`, `SILH-1982-USW`, `RSC-1982-R04-RES` |
| `R04-PO-DSQ-01` | Werdykt DSQ Villeneuve twin-wing | `UPI-1982-04-06-LB`, `AS-1982-USW` |
| `R04-PO-STEW-01` | Poniedziałkowe posiedzenie; ogłoszenie Pook ≈12 h | `UPI-1982-04-06-LB` |
| `R04-PO-PROT-TYR-01` | Protest Tyrrella o twin-wing | `MS-MAY1982-USW`, `AS-1982-USW`, `UPI-1982-04-06-LB` |
| `R04-PO-PROT-FER-01` | Protest Ferrari vs McLaren (opis konfliktowy) | `UPI-1982-04-06-LB`, `AS-1982-USW` |
| `R04-PO-FINE-01` | Grzywna de Angelis/Lotus 2000 USD | `UPI-1982-04-06-LB` |
| `R04-PO-APP-01` | Apelacje otwarte | `UPI-1982-04-06-LB` |
| `R04-PO-DNF-01` | Lista DNF / przyczyny | `MS-MAY1982-USW`, `AS-1982-USW`, `RSC-1982-R04-RES` |
| `R04-PO-RXN-01` | Reakcje paddocku | `MS-MAY1982-USW`, `AS-1982-USW` |
| `R04-PO-PTS-01` | Punkty LB 9–6–4–3–2–1 po DSQ; sumy standings | `UPI-1982-04-06-LB`, `ARCHIVE-R03-STAND`, `SILH-1982-USW` |
| `R04-PO-STD-01` | Stan przed LB = po Rio | `ARCHIVE-R03-STAND` |
| `R04-PO-QUAR-FISA-01` | FISA Brazil po LB — kwarantanna | `UPI-1982-04-22-IMOLA` |

