#!/usr/bin/env python3
"""Build a static, spoiler-safe reader from archive/."""

from __future__ import annotations

import argparse
import json
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


def race_event_name(race_dir: Path, fallback: str) -> str:
    meta = race_dir / "metadata.yaml"
    if not meta.exists():
        return fallback
    data = yaml.safe_load(meta.read_text(encoding="utf-8")) or {}
    return data.get("event") or fallback


def build_season(season: str) -> Season:
    season_root = ARCHIVE_ROOT / "seasons" / season
    season_docs: list[Doc] = []

    for filename, kind, label in SEASON_DOC_ORDER:
        path = season_root / "season" / filename
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        stem = path.stem
        ready = is_ready(text)
        season_docs.append(
            Doc(
                season=season,
                kind=kind,
                title=title_from_md(text, label),
                label=label,
                rel_path=posix(path.relative_to(REPO_ROOT)),
                href=f"/seasons/{season}/season/{stem}/",
                file_path=path,
                ready=ready,
                unlocked=ready,
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
            ready = is_ready(text)
            race.docs.append(
                Doc(
                    season=season,
                    kind=kind,
                    title=title_from_md(text, f"{event_name} — {label}"),
                    label=label,
                    rel_path=posix(path.relative_to(REPO_ROOT)),
                    href=f"/seasons/{season}/races/{race_dir.name}/{stem}/",
                    file_path=path,
                    ready=ready,
                    unlocked=ready,
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


READER_JS = r"""
(function () {
  var STORAGE_KEY = "f1tc-reading-progress-v1";

  function withBase(href, base) {
    var b = base || "/";
    if (!b.endsWith("/")) b += "/";
    return b + String(href || "").replace(/^\//, "");
  }

  function loadProgress() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY) || "null");
    } catch (e) {
      return null;
    }
  }

  function saveProgress(href) {
    if (!href) return;
    try {
      localStorage.setItem(
        STORAGE_KEY,
        JSON.stringify({ lastHref: href, updatedAt: new Date().toISOString() })
      );
    } catch (e) {}
  }

  function readingOrder() {
    var el = document.getElementById("reading-order");
    if (!el) return [];
    try {
      var data = JSON.parse(el.textContent || "{}");
      return Array.isArray(data.order) ? data.order : [];
    } catch (e) {
      return [];
    }
  }

  function siteBase() {
    var el = document.getElementById("reading-order");
    if (!el) return document.body.getAttribute("data-base") || "/";
    try {
      return JSON.parse(el.textContent || "{}").base || "/";
    } catch (e) {
      return "/";
    }
  }

  function findContinueTarget(order, lastHref) {
    if (!order.length) return null;
    if (!lastHref) {
      return { doc: order[0], mode: "start" };
    }
    var idx = -1;
    for (var i = 0; i < order.length; i++) {
      if (order[i].href === lastHref) {
        idx = i;
        break;
      }
    }
    if (idx < 0) return { doc: order[0], mode: "start" };
    if (idx + 1 < order.length) {
      return { doc: order[idx + 1], mode: "next", previous: order[idx] };
    }
    return { doc: order[idx], mode: "caught-up", previous: order[idx] };
  }

  function labelFor(target) {
    if (!target || !target.doc) return "Czytaj";
    var name = target.doc.label || target.doc.title || "dokument";
    if (target.mode === "start") return "Zacznij czytanie · " + name;
    if (target.mode === "next") return "Czytaj dalej · " + name;
    return "Jesteś na bieżąco · " + name;
  }

  var tracked = document.body.getAttribute("data-track-href");
  if (tracked) saveProgress(tracked);

  var order = readingOrder();
  var base = siteBase();
  var progress = loadProgress();
  var lastHref = progress && progress.lastHref ? progress.lastHref : null;
  var target = findContinueTarget(order, lastHref);

  document.querySelectorAll("[data-continue-reading]").forEach(function (btn) {
    if (!target) {
      btn.hidden = true;
      return;
    }
    btn.hidden = false;
    btn.setAttribute("href", withBase(target.doc.href, base));
    btn.textContent = labelFor(target);
  });

  var note = document.querySelector("[data-reading-note]");
  if (note) {
    if (!lastHref) {
      note.textContent = "Nie masz jeszcze zapisanego postępu — start od pierwszego dokumentu.";
    } else if (target && target.mode === "next") {
      note.textContent = "Ostatnio: " + (target.previous.title || target.previous.label) + ".";
    } else if (target && target.mode === "caught-up") {
      note.textContent = "Przeczytałeś wszystkie obecnie dostępne dokumenty.";
    } else {
      note.textContent = "";
    }
  }
})();
"""


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
html{scroll-behavior:smooth;color-scheme:only light;background-color:var(--paper)}
body{
  margin:0;min-height:100vh;font-family:var(--sans);color:var(--ink);line-height:1.55;
  background-color:var(--paper);
  background-image:
    radial-gradient(1200px 600px at 10% -10%, rgba(180,35,24,.08), transparent 55%),
    radial-gradient(900px 500px at 100% 0%, rgba(31,107,74,.07), transparent 50%),
    linear-gradient(180deg,#f7f5f0 0%,var(--paper) 40%,#ebe7de 100%);
}
a{color:var(--accent);text-decoration-thickness:1px;text-underline-offset:.18em}
a:hover{color:var(--accent-soft)}
.site-shell{display:grid;grid-template-columns:var(--rail) minmax(0,1fr);min-height:100vh}
.rail{
  position:sticky;top:0;align-self:start;height:100vh;padding:1.5rem 1.1rem 2rem;
  border-right:1px solid var(--rule);background:rgba(243,241,235,.92);
  backdrop-filter:blur(10px);overflow:auto
}
.brand{display:block;font-family:var(--serif);font-weight:600;font-size:1.35rem;line-height:1.15;color:var(--ink);text-decoration:none;letter-spacing:-.02em;margin-bottom:.35rem}
.brand:hover{color:var(--accent)}
.brand-sub{font-size:.78rem;color:var(--ink-soft);margin-bottom:1.5rem}
.nav-toggle{position:absolute;opacity:0;pointer-events:none;width:0;height:0}
.nav-toggle-label{
  display:none;align-items:center;justify-content:space-between;gap:.75rem;
  width:100%;margin:0 0 .75rem;padding:.65rem .85rem;border:1px solid var(--rule);
  border-radius:.55rem;background:rgba(255,255,255,.65);color:var(--ink);
  font:inherit;font-weight:600;font-size:.92rem;cursor:pointer
}
.nav-toggle-label::after{content:"Spis";font-size:.78rem;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-soft)}
.nav-toggle:focus-visible + .nav-toggle-label{outline:2px solid var(--accent);outline-offset:2px}
.nav-toggle:checked + .nav-toggle-label::after{content:"Zamknij"}
.rail-body{min-width:0}
.rail-label{font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-soft);margin:1.25rem 0 .5rem}
.rail nav a,.rail nav .locked{
  display:block;padding:.28rem .4rem;margin:0 -.4rem;border-radius:.35rem;color:var(--ink);text-decoration:none;font-size:.92rem
}
.rail nav a:hover,.rail nav a[aria-current="page"]{background:var(--paper-deep);color:var(--accent)}
.rail nav .locked{color:var(--lock)}
.rail .round{margin-top:.85rem;font-size:.78rem;font-weight:600;color:var(--ink-soft)}
.main{padding:2rem clamp(1.25rem,4vw,3.5rem) 4rem;min-width:0;color:var(--ink)}
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
.btn[hidden]{display:none !important}
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
@media (max-width:900px){
  .site-shell{grid-template-columns:1fr}
  .rail{
    position:sticky;top:0;z-index:20;height:auto;max-height:none;overflow:visible;
    border-right:0;border-bottom:1px solid var(--rule);padding:0.85rem 1rem
  }
  .brand{font-size:1.15rem;margin-bottom:.15rem}
  .brand-sub{margin-bottom:.65rem}
  .nav-toggle-label{display:flex}
  .rail-body{
    display:none;margin:0 0 .35rem;padding:.35rem 0 .5rem;
    max-height:min(70vh,32rem);overflow:auto;-webkit-overflow-scrolling:touch
  }
  .nav-toggle:checked ~ .rail-body{display:block}
  .main{padding:1.25rem 1.1rem 3rem}
  .hero{padding:1rem 0 1.25rem}
  .hero h1{font-size:clamp(1.9rem,8vw,2.8rem)}
  .article{font-size:1.05rem}
}
"""


def page_shell(
    *,
    title: str,
    body: str,
    base: str,
    season: Season | None = None,
    current_href: str | None = None,
    track_href: str | None = None,
    reading_manifest: dict | None = None,
) -> str:
    header = [
        '<a class="brand" href="' + with_base("/", base) + '">F1 Time Capsule</a>',
        '<div class="brand-sub">Archiwum bez spoilerów</div>',
    ]
    nav_parts: list[str] = []

    if season:
        nav_parts.append(f'<div class="rail-label">Sezon {escape(season.season)}</div><nav>')
        for doc in season.season_docs:
            if doc.kind != "season-prelude" and not doc.unlocked:
                continue
            if doc.unlocked:
                cur = ' aria-current="page"' if doc.href == current_href else ""
                nav_parts.append(
                    f'<a href="{escape(with_base(doc.href, base))}"{cur}>{escape(doc.label)}</a>'
                )
            else:
                nav_parts.append(f'<span class="locked">{escape(doc.label)} · wkrótce</span>')
        nav_parts.append("</nav>")
        nav_parts.append('<div class="rail-label">Rundy</div><nav>')
        remaining_locked = 0
        for race in season.races:
            unlocked_docs = [doc for doc in race.docs if doc.unlocked]
            if not unlocked_docs:
                remaining_locked += 1
                continue
            nav_parts.append(
                f'<div class="round">{escape(race.round)} · {escape(race.event_name)}</div>'
            )
            for doc in unlocked_docs:
                cur = ' aria-current="page"' if doc.href == current_href else ""
                nav_parts.append(
                    f'<a href="{escape(with_base(doc.href, base))}"{cur}>{escape(doc.label)}</a>'
                )
            locked_here = sum(1 for doc in race.docs if not doc.unlocked)
            if locked_here:
                nav_parts.append(
                    f'<span class="locked">+{locked_here} · wkrótce</span>'
                )
        if remaining_locked:
            nav_parts.append(
                f'<span class="locked">Dalsze rundy · {remaining_locked} · wkrótce</span>'
            )
        nav_parts.append("</nav>")
    else:
        season_ids = list_seasons()
        links = "".join(
            f'<a href="{escape(with_base(f"/seasons/{sid}/", base))}">Sezon {escape(sid)}</a>'
            for sid in season_ids
        )
        nav_parts.append(f'<div class="rail-label">Sezony</div><nav>{links}</nav>')

    rail = "".join(header) + (
        '<input type="checkbox" id="nav-toggle" class="nav-toggle" />'
        '<label class="nav-toggle-label" for="nav-toggle">'
        '<span>Menu sezonu</span>'
        "</label>"
        f'<div class="rail-body">{"".join(nav_parts)}</div>'
    )

    css_href = with_base("/assets/styles.css", base)
    js_href = with_base("/assets/reader.js", base)
    fonts = (
        "https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,600;0,9..40,700;1,9..40,400"
        "&family=Fraunces:opsz,wght@9..144,500;9..144,650&family=IBM+Plex+Mono:wght@400;500&display=swap"
    )
    manifest = reading_manifest or {"base": base, "order": []}
    manifest_json = json.dumps(manifest, ensure_ascii=False).replace("<", "\\u003c")
    track_attr = f' data-track-href="{escape(track_href)}"' if track_href else ""
    body_attrs = f'data-base="{escape(base)}"{track_attr}'

    return f"""<!doctype html>
<html lang="pl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="color-scheme" content="light only" />
  <meta name="description" content="Spoiler-safe archive Formuły 1 — czytanie sezonu bez wiedzy z przyszłości." />
  <title>{escape(title)}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="{fonts}" rel="stylesheet" />
  <link rel="stylesheet" href="{escape(css_href)}" />
</head>
<body {body_attrs}>
  <script type="application/json" id="reading-order">{manifest_json}</script>
  <div class="site-shell">
    <aside class="rail">{rail}</aside>
    <main class="main" id="tresc">{body}</main>
  </div>
  <script src="{escape(js_href)}" defer></script>
</body>
</html>
"""


def reading_manifest_for(season: Season, base: str) -> dict:
    return {
        "base": base if base.endswith("/") else base + "/",
        "order": [
            {"href": d.href, "title": d.title, "label": d.label}
            for d in season.reading_order
            if d.unlocked
        ],
    }


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


def preferred_home_season(seasons: list[Season]) -> Season | None:
    """Pick a season for the home CTA: most unlocked docs, then latest year."""
    if not seasons:
        return None
    return max(
        seasons,
        key=lambda s: (
            sum(1 for d in s.reading_order if d.unlocked),
            s.season,
        ),
    )


def render_home(seasons: list[Season], base: str) -> str:
    season = preferred_home_season(seasons)
    season_links = "".join(
        f'<a class="btn secondary" href="{escape(with_base(f"/seasons/{s.season}/", base))}">'
        f"Sezon {escape(s.season)}</a>"
        for s in seasons
    )
    if season is None:
        body = f"""
<section class="hero">
  <h1>F1 Time Capsule</h1>
  <p>Czytaj Formułę 1 rundę po rundzie — tylko to, co dało się wiedzieć w danym momencie.</p>
  <p class="muted">Brak sezonów w archiwum.</p>
</section>
"""
        return page_shell(title="F1 Time Capsule", body=body, base=base)

    first = next((d for d in season.reading_order if d.unlocked), None)
    fallback_href = with_base(first.href, base) if first else with_base(f"/seasons/{season.season}/", base)
    fallback_label = f"Zacznij czytanie · {first.label}" if first else f"Spis sezonu {season.season}"
    body = f"""
<section class="hero">
  <h1>F1 Time Capsule</h1>
  <p>Czytaj Formułę 1 rundę po rundzie — tylko to, co dało się wiedzieć w danym momencie. Bez wyników z przyszłości, bez retrospektywnego „wiadomo było”.</p>
  <div class="cta-row">
    <a class="btn" data-continue-reading href="{escape(fallback_href)}">{escape(fallback_label)}</a>
    {season_links}
  </div>
  <div class="state-card">
    <strong>Twój postęp czytania</strong>
    <div data-reading-note>Ładowanie postępu…</div>
    <div class="muted" style="margin-top:.55rem;font-size:.92rem">Zapisywane lokalnie w tej przeglądarce (localStorage). Odblokowanie w czytelniku = dokumenty gotowe (nie-placeholder); pozycję trzyma przeglądarka.</div>
  </div>
</section>
"""
    return page_shell(
        title="F1 Time Capsule",
        body=body,
        base=base,
        reading_manifest=reading_manifest_for(season, base),
    )


def render_season_index(season: Season, base: str) -> str:
    first = next((d for d in season.reading_order if d.unlocked), None)
    cta = ""
    if first:
        cta = (
            f'<div class="cta-row">'
            f'<a class="btn" data-continue-reading href="{escape(with_base(first.href, base))}">'
            f"Zacznij czytanie · {escape(first.label)}</a></div>"
        )

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
        first_open = next((d for d in race.docs if d.unlocked), None)
        open_count = sum(1 for d in race.docs if d.unlocked)
        if first_open:
            race_cards.append(
                f'<a class="card" href="{escape(with_base(first_open.href, base))}"><div class="meta">Runda {escape(race.round)}</div><h3>{escape(race.event_name)}</h3><p>{open_count} dostępne</p><span class="badge">czytaj</span></a>'
            )
        else:
            race_cards.append(
                f'<div class="card" style="opacity:.65"><div class="meta">Runda {escape(race.round)}</div><h3>{escape(race.event_name)}</h3><p>Dokumenty jeszcze niegotowe (placeholder lub brak treści).</p><span class="badge locked">niedostępne</span></div>'
            )

    body = f"""
<section class="hero" style="padding-top:.5rem">
  <h1>Sezon {escape(season.season)}</h1>
  <p>Czytaj w kolejności historycznej. „Czytaj dalej” pamięta ostatni dokument w tej przeglądarce.</p>
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
        reading_manifest=reading_manifest_for(season, base),
    )


def render_doc(season: Season, doc: Doc, *, kicker: str, base: str) -> str:
    manifest = reading_manifest_for(season, base)
    if not doc.unlocked:
        body = f"""
<div class="locked-panel">
  <h1>{escape(doc.title)}</h1>
  <p>Dokument zablokowany: szkic szablonowy lub treść jeszcze niegotowa.</p>
  <p><a href="{escape(with_base(f"/seasons/{season.season}/", base))}">Wróć do spisu sezonu</a></p>
</div>
"""
        return page_shell(
            title=f"{doc.title} · F1 Time Capsule",
            body=body,
            base=base,
            season=season,
            current_href=doc.href,
            reading_manifest=manifest,
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
        track_href=doc.href,
        reading_manifest=manifest,
    )


def build(base: str = "/") -> None:
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True)
    write(OUT_DIR / "assets" / "styles.css", CSS)
    write(OUT_DIR / "assets" / "reader.js", READER_JS)

    seasons = [build_season(season_id) for season_id in list_seasons()]
    write(out_path_for_href("/"), render_home(seasons, base))

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
