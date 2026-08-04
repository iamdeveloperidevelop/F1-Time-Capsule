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
contemporary: false
spoiler_risk: "contains-later-material"
locator: "https://www.motorsportmagazine.com/archive/article/april-1982/70/brazilian-grand-prix-10/"
access_date: "2026-08-05"
supports: []
disagreement_notes: null
notes: "QUARANTINE dla pre-weekend: zawiera trening, kwalifikacje, wyścig, protest o wodę/balast, debiuty samochodów. Nie wspiera twierdzeń tego dokumentu."
```

## Conflict and uncertainty index

| Uncertainty ID | Claim IDs | Source IDs | Status at cutoff | Note |
| --- | --- | --- | --- | --- |
| UNC-R03-CUT | R03-CUT-01 | — | unresolved | Brak oficjalnego programu 1982 z dniem/godziną pierwszej sesji |
| UNC-R03-GO | R03-EXP-01, R03-CAL-01 | MS-MAR1982-SCENE, NYT-AP-1982-02-10 | open | „Shaky” vs zaplanowana następna runda; brak depeszy potwierdzającej 8–19 Mar |
| UNC-R03-ENT | R03-ENT-01 | MS-MAR1982-NOTES | open | Przegląd po Kyalami ≠ zamknięta lista zgłoszeń Rio |
| UNC-R03-NAME | R03-VEN-01, R03-VEN-02 | MS-MAR1978-BRA, MS-MAY1981-BRA | noted | Aliasy Jacarepaguá / Riocentro / Circuit Internacional — ten sam kompleks |
| UNC-R03-WATER | R03-TEC-02 | MS-MAR1982-NOTES | unused-in-PW | Fakt Kyalami zachowany w ledgerze; nie użyty w prose pre-weekend po audycie spoilera |

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
