#!/usr/bin/env python3
# Copyright 2026 The Fusion Commons contributors
# SPDX-License-Identifier: Apache-2.0
"""Fetch repository health (stars, last activity) for indexed repos.

Writes data/health.json, keyed by "<host>/<owner>/<repo>". Uses the public
GitHub/GitLab/Bitbucket APIs; set GITHUB_TOKEN to raise the GitHub rate limit
(the nightly workflow does). Repos that cannot be fetched are simply skipped —
the site renders fine without them.

Usage:
    python scripts/fetch_health.py [--limit N]
"""

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def get_json(url: str, headers: dict) -> dict | None:
    req = urllib.request.Request(url, headers={"User-Agent": "fusion-commons-health", **headers})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.load(r)
    except Exception as e:  # noqa: BLE001 — any failure just skips the repo
        print(f"  skip {url}: {e}", file=sys.stderr)
        return None


def repo_targets() -> list[tuple[str, str, str]]:
    data = yaml.safe_load((ROOT / "data" / "entries.yml").read_text())
    seen, out = set(), []
    for section in data["sections"]:
        for cat in section["categories"]:
            for e in cat["entries"]:
                m = re.match(
                    r"https?://(github\.com|gitlab\.[^/]+|bitbucket\.org)/([^/]+)/([^/#?]+)",
                    e["url"],
                )
                if not m:
                    continue
                host, owner, repo = m.group(1), m.group(2), m.group(3).removesuffix(".git")
                key = f"{host}/{owner}/{repo}"
                if key in seen or repo in ("tree", "blob"):
                    continue
                seen.add(key)
                out.append((host, owner, repo))
    return out


def main() -> int:
    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])
    gh_headers = {}
    if os.environ.get("GITHUB_TOKEN"):
        gh_headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"

    health, fetched = {}, 0
    for host, owner, repo in repo_targets():
        if limit is not None and fetched >= limit:
            break
        key = f"{host}/{owner}/{repo}"
        if host == "github.com":
            d = get_json(f"https://api.github.com/repos/{owner}/{repo}", gh_headers)
            if d and "stargazers_count" in d:
                health[key] = {"stars": d["stargazers_count"], "updated": d.get("pushed_at", "")[:10]}
        elif host.startswith("gitlab"):
            path = urllib.parse.quote(f"{owner}/{repo}", safe="")
            d = get_json(f"https://{host}/api/v4/projects/{path}", {})
            if d and "star_count" in d:
                health[key] = {"stars": d["star_count"], "updated": d.get("last_activity_at", "")[:10]}
        elif host == "bitbucket.org":
            d = get_json(f"https://api.bitbucket.org/2.0/repositories/{owner}/{repo}", {})
            if d and "updated_on" in d:
                health[key] = {"stars": None, "updated": d["updated_on"][:10]}
        fetched += 1
        time.sleep(0.2)

    out = ROOT / "data" / "health.json"
    out.write_text(json.dumps(health, indent=1, sort_keys=True) + "\n")
    print(f"Wrote {out}: {len(health)} repos ({fetched} attempted)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
