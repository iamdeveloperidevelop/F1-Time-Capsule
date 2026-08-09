# French Grand Prix — source ledger

To kanoniczny rejestr źródeł folderu rundy. Dokumenty treści cytują
`source_id` i `claim_id`; nie prowadzą konkurencyjnych list źródeł. Cutoff
rejestru przy pre-weekend obejmuje wyłącznie `pre-weekend.md` (granica:
natychmiast przed pierwszą oficjalną sesją Paul Ricard, piątek 23 VII 1982
≈10:00 CEST).

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
disagreement_notes: "Konflikt Pironi/Ferrari z liniami Wiki (UNC-R11-PW-PIR-PTS)."
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
notes: "Reprint; publication_date oryginału unknown; content-based availability dla pasażów Entry & Practice przed pierwszą sesją. STRICT quarantine: wszystkie czasy, qualifying order, grid, race, Mass accident, Arnoux/Prost controversy."
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
disagreement_notes: "Serra listed as F8D; MS mówi F9 first string + F8D spare — zachować MS dla intencji sprzętowej."
notes: "Używać tylko entry/dystans; kwarantanna qualifying/grid/race/weather-as-result."
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

## Conflict and uncertainty index

| Uncertainty ID | Claim IDs | Source IDs | Status at cutoff | Note |
| --- | --- | --- | --- | --- |
| UNC-R11-PW-PIR-PTS | R11-PW-STD-01 | ARCHIVE-R10-STAND, WP-1982-FR-R | open | Pironi 34 vs 35 / Ferrari 44 vs 45 — kontynuacja konfliktu bazowego |
| UNC-R11-PW-CUT | R11-PW-CUT-01 | MS-1982-09-FR, AS-ROEBUCK-FR1982 | open | ≈10:00 piątek z MS; brak niezależnego programu wydarzenia |
| UNC-R11-PW-LEN | R11-PW-CIR-01 | WP-1982-FR-R, PROSTFAN-1982-FR-ENT, MS-DB-1982-FR | open | 5.809 vs 5.810 km; brak oficjalnego pomiaru programu |
| UNC-R11-PW-ENT | R11-PW-ENT-02 | PROSTFAN-1982-FR-ENT, RSC-1982-R11-ENT, MS-1982-09-FR | open | Brak oficjalnego telexu FOCA/FISA; F9 vs F8D listing |
| UNC-R11-PW-REN-CHASSIS | R11-PW-ENT-01 | MS-1982-09-FR, RSC-1982-R11-ENT | open | MS RE38B vs RSC/Wiki RE30B dla zapasowego Arnouxa — w PW tylko «starsze podwozie / Monte Carlo» |
| UNC-R11-PW-WX | — | — | open | Brak datowanej prognozy pogody ≤ cutoff |
| UNC-R11-PW-LAPS | — | MS-1982-09-FR | deferred | Korekta 52→54 znana z tekstu race-morning — nie w PW |
