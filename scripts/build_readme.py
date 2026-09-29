#!/usr/bin/env python3
# Copyright 2026 The Fusion Commons contributors
# SPDX-License-Identifier: Apache-2.0
"""Generate README.md from data/entries.yml and data/scorecards.yml.

Usage:
    python scripts/build_readme.py          # rewrite README.md
    python scripts/build_readme.py --check  # exit 1 if README.md is stale
"""

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
STATUS_MARK = {"open": "🟢", "registration": "🟡", "restricted": "🔴"}
HOST_TAGS = {
    "gitlab": "GitLab",
    "bitbucket.org": "Bitbucket",
    "huggingface.co": "Hugging Face",
}
FOOTER_TOC = [
    "Getting access to licensed codes",
    "Roadmap",
    "Contributing",
    "Support",
    "License",
]


def slug(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^a-z0-9 \-]", "", s)
    return s.replace(" ", "-")


def host_tag(url: str) -> str | None:
    for needle, tag in HOST_TAGS.items():
        if needle in url:
            return tag
    return None


def status_rank(e: dict) -> int:
    return {"open": 0, "registration": 1, "restricted": 2}.get(e.get("status"), 0)


def render_entry(e: dict) -> str:
    mark = STATUS_MARK.get(e.get("status"))
    desc = e["desc"].rstrip()
    prefix = f"- {mark} " if mark else "- "
    line = f"{prefix}[{e['name']}]({e['url']}) — {desc}"
    if e.get("mirror"):
        m = e["mirror"]
        line = line.rstrip(".") + f" ([{m['label']}]({m['url']}))."
    meta = [x for x in (e.get("lang"), e.get("install"), host_tag(e["url"])) if x]
    if meta:
        line += f" `{' · '.join(meta)}`"
    return line


def render_scorecard(card: dict) -> list[str]:
    out = [f"#### {card['title']}", ""]
    if card.get("note"):
        out += [f"*{card['note']}*", ""]
    out.append("| " + " | ".join(card["columns"]) + " |")
    out.append("|" + "---|" * len(card["columns"]))
    for row in card["rows"]:
        out.append("| " + " | ".join(row) + " |")
    out.append("")
    return out


def build() -> str:
    data = yaml.safe_load((ROOT / "data" / "entries.yml").read_text())
    cards = yaml.safe_load((ROOT / "data" / "scorecards.yml").read_text())
    cards_by_cat = {c["category"]: c for c in cards.get("scorecards", [])}
    header = (ROOT / "templates" / "header.md").read_text()
    footer = (ROOT / "templates" / "footer.md").read_text()

    toc, body = ["## Contents", ""], []
    for section in data["sections"]:
        toc.append(f"- [{section['title']}](#{slug(section['title'])})")
        body += [f"## {section['title']}", ""]
        for cat in section["categories"]:
            toc.append(f"  - [{cat['title']}](#{slug(cat['title'])})")
            body += [f"### {cat['title']}", ""]
            for e in sorted(cat["entries"], key=lambda e: (status_rank(e), e["name"].lower())):
                body.append(render_entry(e))
            body.append("")
            for note in cat.get("notes", []):
                body += [f"*{note}*", ""]
            if cat["id"] in cards_by_cat:
                body += render_scorecard(cards_by_cat[cat["id"]])
    for title in FOOTER_TOC:
        toc.append(f"- [{title}](#{slug(title)})")
    toc.append("")

    # Access table, generated from entries that carry an access note.
    gated = []
    for section in data["sections"]:
        for cat in section["categories"]:
            for e in cat["entries"]:
                if e.get("access"):
                    gated.append(e)
    gated.sort(key=lambda e: (e["status"] != "registration", e["name"].lower()))
    access = [
        "## Getting access to licensed codes",
        "",
        "Many of the field's most important codes are free for research but require"
        " a signed agreement. This is normal, and turnaround is usually days to"
        " weeks. The front doors:",
        "",
        "| Code | How to get it |",
        "|------|---------------|",
    ]
    for e in gated:
        access.append(
            f"| {STATUS_MARK[e['status']]} [{e['name']}]({e['url']}) | {e['access']} |"
        )
    access.append("")

    parts = [header, "\n".join(toc), "---", "", "\n".join(body), "\n".join(access), footer]
    return "\n".join(parts)


def main() -> int:
    text = build()
    readme = ROOT / "README.md"
    if "--check" in sys.argv:
        if readme.read_text() != text:
            print("README.md is out of date — run: python scripts/build_readme.py")
            return 1
        print("README.md is up to date.")
        return 0
    readme.write_text(text)
    print(f"Wrote {readme}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
