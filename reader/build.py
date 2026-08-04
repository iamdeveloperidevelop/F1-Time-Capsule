#!/usr/bin/env python3
"""Build a static, spoiler-safe reader from archive/."""

from __future__ import annotations

import argparse
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin
from xml.sax.saxutils import escape

import markdown as md_lib
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
ARCHIVE_ROOT = REPO_ROOT / "archive"
STATE_PATH = REPO_ROOT / "archive-state.yaml"
OUT_DIR = Path(__file__).resolve().parent / "dist"

PLACEHOLDER_RE = re.compile(
    r"\[(?:CONCISE|ONLY|CUTOFF|CONFIRMED|POSITION|DRIVER|TEAM|POINTS|TOTAL|NOTE|RULES|PROVISIONAL|SOURCE|yes \| no)",
    re.I,
)
BRACKET_TOKEN_RE = re.compile(r"\[[A-Z][A-Z0-9 /|_'’.\\-]{2,}\]")

SEASON_DOC_ORDER = [
    ("prelude.md", "season-prelude", "Preludium sezonu"),
    ("context.md", "season-reference", "Kontekst"),
    ("regulations.md", "season-reference", "Regulamin"),
    ("technology.md", "season-reference", "Technika"),
    ("teams.md", "season-reference", "Zespoły"),
    ("drivers.md", "season-reference", "Kierowcy"),
    ("people-and-organisations.md", "season-reference", "Ludzie i organizacje"),
    ("calendar.md", "season-reference", "Kalendarz"),
    ("glossary.md", "season-reference", "Słownik"),
]

RACE_DOC_ORDER = [
    ("pre-weekend.md", "pre-weekend", "Przed weekendem"),
    ("pre-race.md", "pre-race", "Przed startem"),
    ("post-race.md", "post-race", "Po wyścigu"),
    ("standings-after.md", "standings-after", "Klasyfikacja"),
]


@dataclass
class Doc:
    season: str
    kind: str
    title: str
    label: str
    rel_path: str
    href: str
    file_path: Path
    ready: bool
    unlocked: bool = False
    round: str | None = None
    event_slug: str | None = None
    event_name: str | None = None


@dataclass
class Race:
    season: str
    round: str
    directory: str
    event_name: str
    docs: list[Doc] = field(default_factory=list)


@dataclass
class Season:
    season: str
    season_docs: list[Doc]
    races: list[Race]
    reading_order: list[Doc]


def posix(path: Path) -> str:
    return path.as_posix()


def title_from_md(text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, re.M)
    return match.group(1).strip() if match else fallback


def is_ready(text: str) -> bool:
    if not text.strip() or len(text.strip()) < 80:
        return False
    if PLACEHOLDER_RE.search(text) or BRACKET_TOKEN_RE.search(text):
        return False
    return True


def load_state() -> dict:
    return yaml.safe_load(STATE_PATH.read_text(encoding="utf-8"))


def race_event_name(race_dir: Path, fallback: str) -> str:
    meta = race_dir / "metadata.yaml"
    if not meta.exists():
        return fallback
    data = yaml.safe_load(meta.read_text(encoding="utf-8")) or {}
    return data.get("event") or fallback


def build_season(season: str, last_completed: str | None) -> Season:
    season_root = ARCHIVE_ROOT / "seasons" / season
    season_docs: list[Doc] = []

    for filename, kind, label in SEASON_DOC_ORDER:
        path = season_root / "season" / filename
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        stem = path.stem
        season_docs.append(
            Doc(
                season=season,
                kind=kind,
                title=title_from_md(text, label),
                label=label,
                rel_path=posix(path.relative_to(REPO_ROOT)),
                href=f"/seasons/{season}/season/{stem}/",
                file_path=path,
                ready=is_ready(text),
            )
        )

    races: list[Race] = []
    races_dir = season_root / "races"
    race_dirs = sorted(
        d for d in races_dir.iterdir() if d.is_dir() and re.match(r"^\d{2}-", d.name)
    ) if races_dir.exists() else []

    for race_dir in race_dirs:
        match = re.match(r"^(\d{2})-(.+)$", race_dir.name)
        if not match:
            continue
        round_no, _slug = match.groups()
        event_name = race_event_name(race_dir, race_dir.name)
        race = Race(
            season=season,
            round=round_no,
            directory=race_dir.name,
            event_name=event_name,
        )
        for filename, kind, label in RACE_DOC_ORDER:
            path = race_dir / filename
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8")
            stem = path.stem
            race.docs.append(
                Doc(
                    season=season,
                    kind=kind,
                    title=title_from_md(text, f"{event_name} — {label}"),
                    label=label,
                    rel_path=posix(path.relative_to(REPO_ROOT)),
                    href=f"/seasons/{season}/races/{race_dir.name}/{stem}/",
                    file_path=path,
                    ready=is_ready(text),
                    round=round_no,
                    event_slug=race_dir.name,
                    event_name=event_name,
                )
            )
        races.append(race)

    reading_order: list[Doc] = []
    prelude = next((d for d in season_docs if d.kind == "season-prelude"), None)
    if prelude:
        reading_order.append(prelude)
    for race in races:
        reading_order.extend(race.docs)

    last_idx = next(
        (i for i, d in enumerate(reading_order) if d.rel_path == last_completed),
        -1,
    )

    all_docs = [*season_docs, *[d for r in races for d in r.docs]]
    for doc in all_docs:
        if not doc.ready:
            doc.unlocked = False
            continue
        if doc.kind == "season-reference":
            doc.unlocked = True
            continue
        try:
            idx = reading_order.index(doc)
        except ValueError:
            doc.unlocked = False
            continue
        doc.unlocked = last_idx >= 0 and idx <= last_idx

    return Season(season=season, season_docs=season_docs, races=races, reading_order=reading_order)


def list_seasons() -> list[str]:
    seasons_dir = ARCHIVE_ROOT / "seasons"
    return sorted(
        d.name
        for d in seasons_dir.iterdir()
        if d.is_dir() and re.match(r"^\d{4}$", d.name)
    )


def with_base(href: str, base: str) -> str:
    if href.startswith("http"):
        return href
    base_n = base if base.endswith("/") else base + "/"
    path = href.lstrip("/")
    return urljoin(base_n, path)


def neighbors(season: Season, doc: Doc) -> tuple[Doc | None, Doc | None]:
    unlocked = [d for d in season.reading_order if d.unlocked]
    try:
        idx = unlocked.index(doc)
    except ValueError:
        return None, None
    prev_doc = unlocked[idx - 1] if idx > 0 else None
    next_doc = unlocked[idx + 1] if idx + 1 < len(unlocked) else None
    return prev_doc, next_doc


class ArchiveLinkPreprocessor(md_lib.preprocessors.Preprocessor):
    """Rewrite relative archive .md links into reader routes."""

    def __init__(self, md, *, season: str, current_dir: str, base: str):
        super().__init__(md)
        self.season = season
        self.current_dir = current_dir
        self.base = base

    def run(self, lines: list[str]) -> list[str]:
        pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

        def repl(match: re.Match[str]) -> str:
            text, href = match.group(1), match.group(2)
            if href.startswith(("http://", "https://", "mailto:", "#")):
                return match.group(0)
            path_part, _, hash_part = href.partition("#")
            resolved = resolve_link(self.current_dir, path_part, self.season)
            reader = archive_to_reader(resolved, self.season)
            if not reader:
                return match.group(0)
            full = with_base(reader, self.base)
            if hash_part:
                full = f"{full}#{hash_part}"
            return f"[{text}]({full})"

        return [pattern.sub(repl, line) for line in lines]


def resolve_link(current_dir: str, rel: str, season: str) -> str:
    stack = current_dir.replace("\\", "/").split("/")
    for part in rel.replace("\\", "/").split("/"):
        if part in ("", "."):
            continue
        if part == "..":
            if stack:
                stack.pop()
            continue
        stack.append(part)
    candidate = "/".join(stack)
    if (REPO_ROOT / candidate).exists():
        return candidate
    # Common off-by-one in race docs: ../../../season/... from races/NN-...
    # lands on archive/seasons/season/... instead of archive/seasons/YYYY/season/...
    marker = "archive/seasons/season/"
    if candidate.startswith(marker):
        fixed = f"archive/seasons/{season}/season/{candidate[len(marker):]}"
        if (REPO_ROOT / fixed).exists():
            return fixed
    return candidate


def archive_to_reader(archive_path: str, season: str) -> str | None:
    prefix = f"archive/seasons/{season}/"
    if not archive_path.startswith(prefix) or not archive_path.endswith(".md"):
        return None
    rest = archive_path[len(prefix) : -3]
    if rest.startswith("season/") or rest.startswith("races/"):
        return f"/seasons/{season}/{rest}/"
    return None


def render_markdown(text: str, *, season: str, current_dir: str, base: str) -> str:
    converter = md_lib.Markdown(extensions=["tables", "fenced_code", "sane_lists"])
    converter.preprocessors.register(
        ArchiveLinkPreprocessor(converter, season=season, current_dir=current_dir, base=base),
        "archive_links",
        25,
    )
    return converter.convert(text)


CSS = r"""
:root {
  --ink: #1a2332;
  --ink-soft: #3d4a5c;
  --paper: #f3f1eb;
  --paper-deep: #e8e4da;
  --rule: #c9c2b4;
  --accent: #b42318;
  --accent-soft: #d4533a;
  --lock: #8a8490;
  --ok: #1f6b4a;
  --shadow: 0 18px 50px rgba(26, 35, 50, 0.08);
  --serif: "Fraunces", "Iowan Old Style", "Palatino Linotype", Palatino, serif;
  --sans: "DM Sans", "Segoe UI", sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, monospace;
  --measure: 42rem;
  --rail: 16rem;
}
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0;min-height:100vh;font-family:var(--sans);color:var(--ink);line-height:1.55;
  background:
    radial-gradient(1200px 600px at 10% -10%, rgba(180,35,24,.08), transparent 55%),
    radial-gradient(900px 500px at 100% 0%, rgba(31,107,74,.07), transparent 50%),
    linear-gradient(180deg,#f7f5f0 0%,var(--paper) 40%,#ebe7de 100%);
}
a{color:var(--accent);text-decoration-thickness:1px;text-underline-offset:.18em}
a:hover{color:var(--accent-soft)}
.site-shell{display:grid;grid-template-columns:var(--rail) minmax(0,1fr);min-height:100vh}
.rail{
  position:sticky;top:0;align-self:start;height:100vh;padding:1.5rem 1.1rem 2rem;
  border-right:1px solid var(--rule);background:rgba(243,241,235,.82);
  backdrop-filter:blur(10px);overflow:auto
}
.brand{display:block;font-family:var(--serif);font-weight:600;font-size:1.35rem;line-height:1.15;color:var(--ink);text-decoration:none;letter-spacing:-.02em;margin-bottom:.35rem}
.brand:hover{color:var(--accent)}
.brand-sub{font-size:.78rem;color:var(--ink-soft);margin-bottom:1.5rem}
.rail-label{font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-soft);margin:1.25rem 0 .5rem}
.rail nav a,.rail nav .locked{
  display:block;padding:.28rem .4rem;margin:0 -.4rem;border-radius:.35rem;color:var(--ink);text-decoration:none;font-size:.92rem
}
.rail nav a:hover,.rail nav a[aria-current="page"]{background:var(--paper-deep);color:var(--accent)}
.rail nav .locked{color:var(--lock)}
.rail .round{margin-top:.85rem;font-size:.78rem;font-weight:600;color:var(--ink-soft)}
.main{padding:2rem clamp(1.25rem,4vw,3.5rem) 4rem}
.hero{max-width:48rem;padding:2.5rem 0 2rem}
.hero h1{font-family:var(--serif);font-size:clamp(2.4rem,5vw,3.8rem);line-height:1.05;letter-spacing:-.03em;margin:0 0 .75rem}
.hero p{font-size:1.1rem;color:var(--ink-soft);max-width:34rem;margin:0 0 1.5rem}
.cta-row{display:flex;flex-wrap:wrap;gap:.75rem}
.btn{
  display:inline-flex;align-items:center;gap:.4rem;padding:.7rem 1.1rem;border-radius:999px;
  border:1px solid var(--ink);background:var(--ink);color:var(--paper);text-decoration:none;font-weight:600;font-size:.95rem
}
.btn:hover{background:#101722;color:var(--paper)}
.btn.secondary{background:transparent;color:var(--ink)}
.btn.secondary:hover{background:var(--paper-deep);color:var(--ink)}
.state-card{margin-top:2rem;padding:1.1rem 1.25rem;border:1px solid var(--rule);border-radius:.85rem;background:rgba(255,255,255,.45);box-shadow:var(--shadow);max-width:36rem}
.state-card strong{display:block;font-size:.75rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ok);margin-bottom:.35rem}
.article-wrap{max-width:calc(var(--measure) + 2rem)}
.doc-kicker{font-size:.78rem;letter-spacing:.11em;text-transform:uppercase;color:var(--ink-soft);margin-bottom:.5rem}
.article{font-family:var(--serif);font-size:1.125rem;line-height:1.7}
.article h1{font-size:clamp(1.9rem,3.5vw,2.6rem);line-height:1.15;letter-spacing:-.02em;margin:0 0 1.25rem}
.article h2{font-family:var(--sans);font-size:1.05rem;margin:2.2rem 0 .75rem;padding-top:.4rem;border-top:1px solid var(--rule)}
.article h3{font-family:var(--sans);font-size:1rem;margin:1.5rem 0 .5rem}
.article p,.article li{margin:0 0 1rem}
.article ul,.article ol{padding-left:1.25rem}
.article table{width:100%;border-collapse:collapse;font-family:var(--sans);font-size:.92rem;margin:1.25rem 0 1.75rem;display:block;overflow-x:auto}
.article th,.article td{border-bottom:1px solid var(--rule);padding:.55rem .65rem;text-align:left;vertical-align:top}
.article th{font-weight:650;color:var(--ink-soft)}
.article blockquote{margin:1.25rem 0;padding:.2rem 0 .2rem 1rem;border-left:3px solid var(--accent);color:var(--ink-soft)}
.article code{font-family:var(--mono);font-size:.86em;background:var(--paper-deep);padding:.1em .35em;border-radius:.25rem}
.pager{display:flex;justify-content:space-between;gap:1rem;margin-top:2.5rem;padding-top:1.25rem;border-top:1px solid var(--rule);font-family:var(--sans)}
.pager a{max-width:45%;text-decoration:none;color:var(--ink)}
.pager a span{display:block;font-size:.75rem;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-soft);margin-bottom:.2rem}
.pager a:hover strong{color:var(--accent)}
.locked-panel{max-width:var(--measure);padding:2rem;border:1px dashed var(--rule);border-radius:1rem;background:rgba(255,255,255,.4)}
.locked-panel h1{font-family:var(--serif);margin-top:0}
.card-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(16rem,1fr));gap:.9rem;margin-top:1.5rem}
.card{display:block;padding:1rem 1.1rem;border:1px solid var(--rule);border-radius:.85rem;background:rgba(255,255,255,.5);text-decoration:none;color:var(--ink)}
.card:hover{border-color:var(--accent);color:var(--ink)}
.card .meta{font-size:.75rem;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-soft);margin-bottom:.35rem}
.card h3{font-family:var(--serif);font-size:1.2rem;margin:0 0 .35rem}
.card p{margin:0;font-size:.9rem;color:var(--ink-soft)}
.badge{display:inline-block;font-size:.7rem;letter-spacing:.06em;text-transform:uppercase;padding:.15rem .45rem;border-radius:999px;background:#d9efe4;color:var(--ok);margin-top:.65rem}
.badge.locked{background:#ece8ef;color:var(--lock)}
.section-title{font-family:var(--serif);font-size:1.8rem;margin:2.5rem 0 .4rem}
.muted{color:var(--ink-soft)}
@media (max-width:900px){.site-shell{grid-template-columns:1fr}.rail{position:relative;height:auto;border-right:0;border-bottom:1px solid var(--rule)}}
"""


def page_shell(
    *,
    title: str,
    body: str,
    base: str,
    season: Season | None = None,
    current_href: str | None = None,
) -> str:
    rail = ['<a class="brand" href="' + with_base("/", base) + '">F1 Time Capsule</a>',
            '<div class="brand-sub">Archiwum bez spoilerów</div>']

    if season:
        rail.append(f'<div class="rail-label">Sezon {escape(season.season)}</div><nav>')
        for doc in season.season_docs:
            if doc.kind != "season-prelude" and not doc.unlocked:
                continue
            if doc.unlocked:
                cur = ' aria-current="page"' if doc.href == current_href else ""
                rail.append(
                    f'<a href="{escape(with_base(doc.href, base))}"{cur}>{escape(doc.label)}</a>'
                )
            else:
                rail.append(f'<span class="locked">{escape(doc.label)} · wkrótce</span>')
        rail.append("</nav>")
        rail.append('<div class="rail-label">Rundy</div><nav>')
        for race in season.races:
            rail.append(f'<div class="round">{escape(race.round)} · {escape(race.event_name)}</div>')
            shown = False
            for doc in race.docs:
                if doc.unlocked:
                    cur = ' aria-current="page"' if doc.href == current_href else ""
                    rail.append(
                        f'<a href="{escape(with_base(doc.href, base))}"{cur}>{escape(doc.label)}</a>'
                    )
                    shown = True
                elif doc.ready:
                    rail.append(f'<span class="locked">{escape(doc.label)} · zablokowane</span>')
                    shown = True
            if not shown:
                rail.append('<span class="locked">jeszcze niepisane</span>')
        rail.append("</nav>")
    else:
        rail.append(
            '<div class="rail-label">Start</div><nav>'
            f'<a href="{escape(with_base("/seasons/1982/", base))}">Sezon 1982</a></nav>'
        )

    css_href = with_base("/assets/styles.css", base)
    fonts = (
        "https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,600;0,9..40,700;1,9..40,400"
        "&family=Fraunces:opsz,wght@9..144,500;9..144,650&family=IBM+Plex+Mono:wght@400;500&display=swap"
    )
    return f"""<!doctype html>
<html lang="pl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="description" content="Spoiler-safe archive Formuły 1 — czytanie sezonu bez wiedzy z przyszłości." />
  <title>{escape(title)}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="{fonts}" rel="stylesheet" />
  <link rel="stylesheet" href="{escape(css_href)}" />
</head>
<body>
  <div class="site-shell">
    <aside class="rail">{"".join(rail)}</aside>
    <main class="main">{body}</main>
  </div>
</body>
</html>
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def out_path_for_href(href: str) -> Path:
    clean = href.strip("/")
    if not clean:
        return OUT_DIR / "index.html"
    return OUT_DIR / clean / "index.html"


def pager_html(prev: Doc | None, nxt: Doc | None, base: str) -> str:
    if not prev and not nxt:
        return ""
    left = (
        f'<a href="{escape(with_base(prev.href, base))}"><span>Poprzedni</span><strong>{escape(prev.title)}</strong></a>'
        if prev
        else "<span></span>"
    )
    right = (
        f'<a href="{escape(with_base(nxt.href, base))}" style="text-align:right"><span>Następny</span><strong>{escape(nxt.title)}</strong></a>'
        if nxt
        else "<span></span>"
    )
    return f'<nav class="pager" aria-label="Nawigacja sekwencyjna">{left}{right}</nav>'


def render_home(state: dict, season: Season, base: str) -> str:
    continue_doc = next(
        (d for d in season.reading_order if d.rel_path == state.get("last_completed_document")),
        None,
    ) or next((d for d in season.reading_order if d.unlocked), None)
    ctas = []
    if continue_doc:
        ctas.append(
            f'<a class="btn" href="{escape(with_base(continue_doc.href, base))}">Czytaj dalej · {escape(continue_doc.label)}</a>'
        )
    ctas.append(
        f'<a class="btn secondary" href="{escape(with_base(f"/seasons/{season.season}/", base))}">Spis sezonu {escape(season.season)}</a>'
    )
    body = f"""
<section class="hero">
  <h1>F1 Time Capsule</h1>
  <p>Czytaj Formułę 1 rundę po rundzie — tylko to, co dało się wiedzieć w danym momencie. Bez wyników z przyszłości, bez retrospektywnego „wiadomo było”.</p>
  <div class="cta-row">{"".join(ctas)}</div>
  <div class="state-card">
    <strong>Aktualny punkt archiwum</strong>
    Sezon {escape(str(state.get("active_season")))}, runda {escape(str(state.get("active_round")))}, etap <code>{escape(str(state.get("current_stage")))}</code>.
    <div class="muted" style="margin-top:.55rem;font-size:.92rem">Ostatni ukończony dokument: {escape(str(state.get("last_completed_document")))}</div>
  </div>
</section>
"""
    return page_shell(title="F1 Time Capsule", body=body, base=base)


def render_season_index(season: Season, base: str) -> str:
    prelude = next((d for d in season.season_docs if d.kind == "season-prelude"), None)
    cta = ""
    if prelude and prelude.unlocked:
        cta = f'<div class="cta-row"><a class="btn" href="{escape(with_base(prelude.href, base))}">Zacznij od preludium</a></div>'

    season_cards = []
    for doc in season.season_docs:
        if doc.unlocked:
            season_cards.append(
                f'<a class="card" href="{escape(with_base(doc.href, base))}"><div class="meta">{escape(doc.label)}</div><h3>{escape(doc.title)}</h3><span class="badge">dostępne</span></a>'
            )
        else:
            badge = "zablokowane" if doc.ready else "szkic"
            season_cards.append(
                f'<div class="card" style="opacity:.65"><div class="meta">{escape(doc.label)}</div><h3>{escape(doc.title)}</h3><span class="badge locked">{badge}</span></div>'
            )

    race_cards = []
    for race in season.races:
        first = next((d for d in race.docs if d.unlocked), None)
        open_count = sum(1 for d in race.docs if d.unlocked)
        if first:
            race_cards.append(
                f'<a class="card" href="{escape(with_base(first.href, base))}"><div class="meta">Runda {escape(race.round)}</div><h3>{escape(race.event_name)}</h3><p>{open_count} dostępne</p><span class="badge">czytaj</span></a>'
            )
        else:
            race_cards.append(
                f'<div class="card" style="opacity:.65"><div class="meta">Runda {escape(race.round)}</div><h3>{escape(race.event_name)}</h3><p>Poza aktualnym punktem archiwum lub jeszcze niepisane.</p><span class="badge locked">niedostępne</span></div>'
            )

    body = f"""
<section class="hero" style="padding-top:.5rem">
  <h1>Sezon {escape(season.season)}</h1>
  <p>Czytaj w kolejności historycznej albo skacz po dokumentach już odblokowanych względem stanu archiwum.</p>
  {cta}
</section>
<h2 class="section-title">Dokumenty sezonu</h2>
<div class="card-grid">{"".join(season_cards)}</div>
<h2 class="section-title">Rundy</h2>
<div class="card-grid">{"".join(race_cards)}</div>
"""
    return page_shell(
        title=f"Sezon {season.season} · F1 Time Capsule",
        body=body,
        base=base,
        season=season,
    )


def render_doc(season: Season, doc: Doc, *, kicker: str, base: str) -> str:
    if not doc.unlocked:
        body = f"""
<div class="locked-panel">
  <h1>{escape(doc.title)}</h1>
  <p>Dokument zablokowany spoiler-safe: szkic szablonowy albo poza aktualnym cutoffem archiwum.</p>
  <p><a href="{escape(with_base(f"/seasons/{season.season}/", base))}">Wróć do spisu sezonu</a></p>
</div>
"""
        return page_shell(
            title=f"{doc.title} · F1 Time Capsule",
            body=body,
            base=base,
            season=season,
            current_href=doc.href,
        )

    text = doc.file_path.read_text(encoding="utf-8")
    current_dir = posix(doc.file_path.parent.relative_to(REPO_ROOT))
    html = render_markdown(text, season=season.season, current_dir=current_dir, base=base)
    prev, nxt = neighbors(season, doc)
    body = f"""
<article class="article-wrap">
  <div class="doc-kicker">{escape(kicker)}</div>
  <div class="article">{html}</div>
  {pager_html(prev, nxt, base)}
</article>
"""
    return page_shell(
        title=f"{doc.title} · F1 Time Capsule",
        body=body,
        base=base,
        season=season,
        current_href=doc.href,
    )


def build(base: str = "/") -> None:
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True)
    write(OUT_DIR / "assets" / "styles.css", CSS)

    state = load_state()
    seasons = []
    for season_id in list_seasons():
        last = (
            state.get("last_completed_document")
            if str(state.get("active_season")) == season_id
            else None
        )
        seasons.append(build_season(season_id, last))

    active = next(s for s in seasons if s.season == str(state.get("active_season")))
    write(out_path_for_href("/"), render_home(state, active, base))

    for season in seasons:
        write(out_path_for_href(f"/seasons/{season.season}/"), render_season_index(season, base))
        for doc in season.season_docs:
            write(
                out_path_for_href(doc.href),
                render_doc(
                    season,
                    doc,
                    kicker=f"Sezon {season.season} · {doc.label}",
                    base=base,
                ),
            )
        for race in season.races:
            for doc in race.docs:
                write(
                    out_path_for_href(doc.href),
                    render_doc(
                        season,
                        doc,
                        kicker=f"Runda {race.round} · {race.event_name} · {doc.label}",
                        base=base,
                    ),
                )

    unlocked = sum(1 for s in seasons for d in s.reading_order if d.unlocked)
    print(f"Built reader -> {OUT_DIR} ({unlocked} unlocked narrative docs, base={base!r})")


def main(argv: Iterable[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build F1 Time Capsule reader")
    parser.add_argument(
        "--base",
        default="/",
        help="Site base path, e.g. /F1-Time-Capsule/ for GitHub Pages",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)
    build(base=args.base)


if __name__ == "__main__":
    main()
