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
access_date: "2026-08-05"
supports:
  - claim_id: "R04-PW-STD-01"
    scope: "Prowizoryczna kolejność i punkty po Rio (po odrzuceniu protestu przez stewardów imprezy): Prost 13, Piquet 9, Rosberg 8, Reutemann 6, Arnoux 4 / Watson 4, Lauda 3, Mansell 2, Alboreto 1; Renault 17, Williams 14, Brabham 9, McLaren 7, Lotus 2, Tyrrell 1."
disagreement_notes: "Skala punktowa prowizoryczna; brak oficjalnego biuletynu FIA w pakiecie R03; ścieżka ASN otwarta."
notes: "Wskaźnik do kanonicznej migawki; nie kopiować pełnych tabel do narracji pre-weekend."
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
locator: "https://www.motorsportmagazine.com/archive/article/may-1982/46/united-stateswest-grand-prix/ — May 1982, p. 46; pre-weekend: przyjazd, Reutemann/Andretti, przebudowa, 10:00 test, procedura prekwali; pre-race: Qualifying + warm-up/warunki przed startem + dystans 75½; QUARANTINE: narracja Race od zielonego światła, podium, protest Tyrrella o skrzydło"
access_date: "2026-08-05"
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
disagreement_notes: "Publication_date dnia unknown. Cały tekst miesza przyjazd, sesje i wyścig — izolować. FW07C w MS vs FW07D w niektórych bazach."
notes: "Content-based availability. Pre-weekend: tylko pasaże przed-sesyjne. Pre-race: Qualifying + warm-up/pre-start; nie używać Race od green light, podium ani końcowego protestu Tyrrella."
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
locator: "https://www.silhouet.com/motorsport/archive/f1/1982/82usaw.html — dystans 258.814 km (3.428 km × 75.5); grid gaps; DNPQ/DNQ"
access_date: "2026-08-05"
supports:
  - claim_id: "R04-PR-DIST-01"
    scope: "Długość okrążenia 3,428 km; dystans wyścigu 258,814 km przy 75,5 okrążeniach."
  - claim_id: "R04-PR-GRID-01"
    scope: "Kolejność pola i straty do pole; DNPQ Warwick; DNQ Fabi–Baldi — koroboracja RSC."
disagreement_notes: "Strona zawiera wynik wyścigu i DSQ Villeneuve — kwarantanna."
notes: "Użyte wyłącznie dla dystansu km i koroboracji kolejności pola; nie cytować wyników."
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
    scope: "Dowód, że publiczny werdykt FISA unieważniający 1–2 z Rio datuje się na poniedziałek ≈19–20 kwietnia 1982 — PO Long Beach — i dlatego jest zakazany jako fakt przedweekendowy."
disagreement_notes: null
notes: "Źródło kwarantanny / negatywnego dowodu chronologii; nie cytować w reader-facing prose jako stanu przed Long Beach."
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
| UNC-R04-PR-QUAR-RACE | — | MS-MAY1982-USW, SILH-1982-USW | quarantined | Cała narracja Race / wyniki / DSQ skrzydła. |

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

