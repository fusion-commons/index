#!/usr/bin/env python3
# Copyright 2026 The Fusion Commons contributors
# SPDX-License-Identifier: Apache-2.0
"""Build the static Fusion Commons website into _site/ from data/*.yml.

Usage:
    python scripts/build_site.py
"""

import datetime
import html
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_site"

HOSTS = [
    ("gitlab", "GitLab"),
    ("bitbucket.org", "Bitbucket"),
    ("huggingface.co", "Hugging Face"),
    ("github.com", "GitHub"),
]


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def host_of(url: str) -> tuple[str, str]:
    for needle, label in HOSTS:
        if needle in url:
            return needle.split(".")[0], label
    return "web", "Web"


def status_rank(e: dict) -> int:
    return {"open": 0, "registration": 1, "restricted": 2}.get(e.get("status"), 0)


def md_links(s: str) -> str:
    s = esc(s)
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)


def health_key(url: str) -> str | None:
    m = re.match(r"https?://(github\.com|gitlab\.[^/]+|gitlab\.com|bitbucket\.org)/([^/]+/[^/#?]+)", url)
    if not m:
        return None
    return f"{m.group(1)}/{m.group(2).removesuffix('.git')}"


def fmt_health(h: dict | None) -> str:
    if not h:
        return ""
    bits = []
    if h.get("stars") is not None:
        bits.append(f"★ {h['stars']:,}")
    if h.get("updated"):
        bits.append(f"updated {h['updated'][:7]}")
    if not bits:
        return ""
    return f'<span class="health">{" · ".join(bits)}</span>'


def render_entry(e: dict, section_slug: str, health: dict, cat_title: str = "") -> str:
    status = e.get("status")
    dot = f'<span class="dot {status}" title="{status}"></span>' if status else '<span class="dot none"></span>'
    hkey, hlabel = host_of(e["url"])
    hostpill = f'<span class="pill host">{hlabel}</span>' if hkey not in ("github", "web") else ""
    meta = []
    if e.get("lang"):
        meta.append(f'<span class="pill">{esc(e["lang"])}</span>')
    if e.get("install"):
        meta.append(f'<span class="pill">{esc(e["install"])}</span>')
    if e.get("mirror"):
        meta.append(f'<a class="mirror" href="{esc(e["mirror"]["url"])}">{esc(e["mirror"]["label"])} ↗</a>')
    hh = fmt_health(health.get(health_key(e["url"]) or "", None))
    if hh:
        meta.append(hh)
    metahtml = f'<div class="meta">{"".join(meta)}</div>' if meta else ""
    search = " ".join(
        str(x).lower()
        for x in [e["name"], e["desc"], e.get("lang", ""), e.get("install", ""), cat_title]
    )
    return (
        f'<div class="entry" data-s="{esc(search)}" data-status="{status or "resource"}"'
        f' data-host="{hkey}" data-install="{e.get("install", "")}" data-section="{section_slug}">'
        f"{dot}<div class='entry-main'><div class='entry-head'>"
        f'<a class="name" href="{esc(e["url"])}">{esc(e["name"])}</a>{hostpill}</div>'
        f'<p class="desc">{md_links(e["desc"])}</p>{metahtml}</div></div>'
    )


def render_cell(cell: str) -> str:
    cls = ""
    for mark, c in (("🟩", "ok"), ("🟨", "mid"), ("🟥", "bad"), ("🟢", "ok"), ("🟡", "mid"), ("🔴", "bad")):
        if cell.startswith(mark):
            cls, cell = c, cell[len(mark):].strip()
            break
    if cell in ("—", ""):
        return '<td><span class="cellmuted">—</span></td>'
    inner = md_links(cell)
    if cls:
        return f'<td><span class="cellpill {cls}">{inner}</span></td>'
    return f"<td>{inner}</td>"


def render_scorecard(card: dict) -> str:
    head = "".join(f"<th>{esc(c)}</th>" for c in card["columns"])
    rows = "".join(
        "<tr>" + f"<td class='rowname'>{md_links(row[0])}</td>" + "".join(render_cell(c) for c in row[1:]) + "</tr>"
        for row in card["rows"]
    )
    note = f'<p class="cardnote">{esc(card["note"])}</p>' if card.get("note") else ""
    return (
        f'<div class="scorecard"><h4>{esc(card["title"])}</h4>{note}'
        f'<div class="tablewrap"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div></div>'
    )


def build() -> None:
    data = yaml.safe_load((ROOT / "data" / "entries.yml").read_text())
    cards = yaml.safe_load((ROOT / "data" / "scorecards.yml").read_text())
    cards_by_cat = {c["category"]: c for c in cards.get("scorecards", [])}
    health_path = ROOT / "data" / "health.json"
    health = json.loads(health_path.read_text()) if health_path.exists() else {}

    body, catoptions, total = [], [], 0
    gated = []
    for section in data["sections"]:
        slug = re.sub(r"[^a-z0-9]+", "-", section["title"].lower()).strip("-")
        body.append(f'<section class="topsection" data-section="{slug}"><h2>{esc(section["title"])}</h2>')
        for cat in section["categories"]:
            body.append(f'<div class="category" id="{cat["id"]}"><h3>{esc(cat["title"])}</h3>')
            catoptions.append(f'<option value="{cat["id"]}">{esc(cat["title"])}</option>')
            for e in sorted(cat["entries"], key=lambda e: (status_rank(e), e["name"].lower())):
                body.append(render_entry(e, slug, health, cat["title"]))
                total += 1
                if e.get("access"):
                    gated.append(e)
            for note in cat.get("notes", []):
                body.append(f'<p class="note">{md_links(note)}</p>')
            if cat["id"] in cards_by_cat:
                body.append(render_scorecard(cards_by_cat[cat["id"]]))
            body.append("</div>")
        body.append("</section>")

    gated.sort(key=lambda e: (e["status"] != "registration", e["name"].lower()))
    access_rows = "".join(
        f'<tr><td class="rowname"><span class="dot {e["status"]}"></span> '
        f'<a href="{esc(e["url"])}">{esc(e["name"])}</a></td><td>{esc(e["access"])}</td></tr>'
        for e in gated
    )
    body.append(
        '<section class="topsection" id="access"><h2>Getting access to licensed codes</h2>'
        "<p>Many of the field's most important codes are free for research but require a signed "
        "agreement. This is normal, and turnaround is usually days to weeks. The front doors:</p>"
        f'<div class="scorecard"><div class="tablewrap"><table><thead><tr><th>Code</th><th>How to get it</th></tr></thead>'
        f"<tbody>{access_rows}</tbody></table></div></div></section>"
    )

    template = (ROOT / "site" / "template.html").read_text()
    out = (
        template.replace("__BODY__", "\n".join(body))
        .replace("__CATOPTIONS__", "".join(catoptions))
        .replace("__TOTAL__", str(total))
        .replace("__DATE__", datetime.date.today().isoformat())
    )
    OUT.mkdir(exist_ok=True)
    (OUT / "index.html").write_text(out)
    (OUT / ".nojekyll").write_text("")
    print(f"Wrote {OUT / 'index.html'} — {total} entries")


if __name__ == "__main__":
    build()
