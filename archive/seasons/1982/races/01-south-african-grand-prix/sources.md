---
season: "1982"
document_type: "race-source-ledger"
event: "South African Grand Prix"
event_time: "Okres przedweekendowy do granicy wiedzy bezpośrednio przed planowanym rozpoczęciem pierwszej oficjalnej sesji Grand Prix RPA na Kyalami"
public_knowledge_time: "Najnowsza wykorzystana, potwierdzona publiczna informacja: depesza UPI z 18 grudnia 1981"
knowledge_cutoff: "Immediately before the planned start of the first official session of the South African Grand Prix at Kyalami on Thursday, 21 January 1982; exact time unknown"
spoiler_scope:
  allowed:
    - "Metadane źródeł i wsparcie twierdzeń mieszczące się w obsługiwanej granicy wiedzy"
  forbidden:
    - "Treść źródeł po granicy wiedzy, poza skwantyfikowaną metadanym informacją o ryzyku spoilera"
content_language: "pl"
research_status: "drafted"
source_status: "partial"
spoiler_audit_status: "passed"
last_verified: null
---

# South African Grand Prix — source ledger

To kanoniczny rejestr źródeł folderu rundy. Dokumenty treści cytują
`source_id` i `claim_id`; nie prowadzą konkurencyjnych list źródeł.

## Source entry

```yaml
source_id: "UPI-CALENDAR-1981-10-09"
title: "There will be 16 Formula One Grand Prix races..."
author_or_organisation: "United Press International"
publication_date: "1981-10-09"
event_date: "1981-10-09"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.upi.com/Archives/1981/10/09/There-will-be-16-Formula-One-Grand-Prix-races/3902371448000/ — akapit kalendarzowy"
access_date: "2026-08-03"
supports:
  - claim_id: "R01-EVT-01"
    scope: "Ogłoszenie FISA o kalendarzu Formuły 1, umieszczającym Kyalami w Republice Południowej Afryki w ogłoszonym harmonogramie."
disagreement_notes: "Akapit kalendarzowy zawiera nierozstrzygniętą rozbieżność daty; nie stanowi podstawy do ustalenia daty ani formatu wydarzenia."
notes: "Wykorzystano wyłącznie jako kontekst ogłoszonego kalendarza i miejsca; otoczenie archiwum zawiera późniejszy materiał."
```

```yaml
source_id: "UPI-KYALAMI-1981-02-06"
title: "Nelson Piquet of Brazil, driving a Brabham BT49, splattered..."
author_or_organisation: "United Press International"
publication_date: "1981-02-06"
event_date: "1981-02-06"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.upi.com/Archives/1981/02/06/Nelson-Piquet-of-Brazil-driving-a-Brabham-BT49-splattered/4162350283600/ — trzeci akapit"
access_date: "2026-08-03"
supports:
  - claim_id: "R01-CIR-01"
    scope: "Opis Kyalami jako toru o długości 2,55 mili w lutym 1981 roku."
  - claim_id: "R01-CTX-01"
    scope: "Kontekst FISA–FOCA i uznania ówczesnej imprezy za niezaliczaną do mistrzostw."
disagreement_notes: "Opis długości z 1981 roku nie potwierdza niezmienionego układu, kierunku jazdy, liczby zakrętów ani liczby okrążeń w 1982 roku."
notes: "Wykorzystano jako ograniczony kontekst toru i odziedziczony kontekst zarządzania sportem; nie służy do wnioskowania o wpływie na weekend 1982."
```

```yaml
source_id: "UPI-LAUDA-1981-11-12"
title: "Austrian driver Niki Lauda, a two-time Grand Prix champion..."
author_or_organisation: "United Press International"
publication_date: "1981-11-12"
event_date: "1981-11-12"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.upi.com/Archives/1981/11/12/Austrian-driver-Niki-Lauda-a-two-time-Grand-Prix-champion/2164374389200/ — akapit otwierający, akapity o składzie McLarena i akapit z wypowiedzią Laudy"
access_date: "2026-08-03"
supports:
  - claim_id: "R01-ENT-01"
    scope: "Publiczne ogłoszenie powrotu Nikiego Laudy do McLarena u boku Johna Watsona."
  - claim_id: "R01-EXP-01"
    scope: "Wypowiedź Laudy, że nie oczekuje natychmiastowego zwycięstwa w Grand Prix RPA."
disagreement_notes: null
notes: "Wypowiedź Laudy jest współczesnym oczekiwaniem, nie potwierdzeniem przyszłego wyniku; otoczenie archiwum zawiera późniejszy materiał."
```

```yaml
source_id: "UPI-WILLIAMS-1981-12-18"
title: "Carlos Reutemann of Argentina, runner-up in the 1981 World..."
author_or_organisation: "United Press International"
publication_date: "1981-12-18"
event_date: "1981-12-18"
source_type: "PRESS"
contemporary: true
spoiler_risk: "contains-later-material"
locator: "https://www.upi.com/Archives/1981/12/18/Carlos-Reutemann-of-Argentina-runner-up-in-the-1981-World/9118377499600/ — pierwsze cztery akapity i akapit z wypowiedzią Franka Williamsa"
access_date: "2026-08-03"
supports:
  - claim_id: "R01-ENT-02"
    scope: "Ogłoszenie przez Williamsa pary Carlos Reutemann–Keke Rosberg."
  - claim_id: "R01-EXP-02"
    scope: "Przypisane Frankowi Williamsowi oczekiwanie, że Keke Rosberg wkrótce stanie się regularnym zwycięzcą ze względu na swoje nastawienie i szybkość."
disagreement_notes: null
notes: "Wypowiedź Franka Williamsa jest współczesnym oczekiwaniem, nie prognozą wyniku; otoczenie archiwum zawiera późniejszy materiał."
```

## Conflict and uncertainty index

| Uncertainty ID | Claim IDs | Source IDs | Status at cutoff | Note |
| --- | --- | --- | --- | --- |
| `1982-CUT-01` | Granica wszystkich twierdzeń rundy 01 | — | open | Dokładna godzina planowanego rozpoczęcia pierwszej oficjalnej sesji na Kyalami pozostaje nieznana. |
| `1982-R01-CUT-02` | — | `UPI-CALENDAR-1981-10-09` | open | Kalendarz UPI podaje 23 lutego, a obecne metadane sezonu używają 21 stycznia; żadnej wersji nie uznano za poprawną. Potrzebny jest datowany oficjalny program lub biuletyn, aby rozstrzygnąć datę i format. |
| `1982-R01-EVT-01` | `R01-EVT-01` | `UPI-CALENDAR-1981-10-09` | open | Kalendarz wspiera wyłącznie umieszczenie Kyalami w ogłoszonym harmonogramie; rozbieżność daty i formatu opisuje `1982-R01-CUT-02`. |
| `1982-R01-CIR-01` | `R01-CIR-01` | `UPI-KYALAMI-1981-02-06` | open | Długość z opisu z 1981 roku nie ustala parametrów toru na 1982 rok. |
| `1982-R01-WEA-01` | — | — | open | Nie zachowano datowanej prognozy pogody dostępnej najpóźniej 20 stycznia 1982 roku. |
| `1982-R01-POL-01` | — | — | open | Nie zachowano datowanego źródła dotyczącego konkretnie wydarzenia dla politycznego kontekstu gospodarza. |
