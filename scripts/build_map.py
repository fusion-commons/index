#!/usr/bin/env python3
# Copyright 2026 The Fusion Commons contributors
# SPDX-License-Identifier: Apache-2.0
"""Generate site/map.svg — the open fusion software map.

Usage:
    python scripts/build_map.py
"""

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site" / "map.svg"

W, H = 1680, 1070
INK, MUTED, LINE, PANEL, BG = "#20242c", "#5c6470", "#d9d5cb", "#ffffff", "#f7f6f3"
ARROW = "#8a8f98"
PILL = {
    "o": ("#e2f2e8", "#1e6f42"),  # open
    "r": ("#faeed3", "#8a6414"),  # registration
    "x": ("#f9e3e1", "#a03730"),  # restricted
    "n": ("#eef1f6", "#44506a"),  # neutral
}

CARDS = [
    dict(x=60, y=150, w=400, h=185, title="1 · Plant & systems design",
         role="Choose the machine — size, fields, cost, operating point",
         pills=[("PROCESS", "o"), ("Bluemira", "o"), ("FUSE", "o"), ("cfspopcon", "o"), ("MITIM", "o")]),
    dict(x=505, y=150, w=400, h=185, title="2 · Equilibrium & shaping",
         role="Hold the plasma — magnetic equilibrium and 3D shape",
         pills=[("DESC", "o"), ("FreeGS", "o"), ("VMEC++", "o"), ("SIMSOPT", "o"), ("SPEC", "o"), ("GSFit", "o"), ("EFIT", "r")]),
    dict(x=950, y=150, w=400, h=185, title="3 · Turbulence & transport",
         role="Predict confinement — turbulence, profiles, performance",
         pills=[("TORAX", "o"), ("CGYRO", "o"), ("QuaLiKiz", "o"), ("stella", "o"), ("GyroSwin", "o"), ("GENE", "r"), ("XGC", "r")]),
    dict(x=60, y=415, w=400, h=185, title="4 · Edge & exhaust",
         role="Tame the exhaust — edge plasma, divertor, heat loads",
         pills=[("UEDGE", "o"), ("Hermes-3", "o"), ("BOUT++", "o"), ("HEAT", "o"), ("SOLPS-ITER", "r"), ("EIRENE", "r")]),
    dict(x=505, y=415, w=400, h=185, title="5 · Materials & tritium",
         role="Survive & refuel — hydrogen in materials, damage, safety",
         pills=[("FESTIM", "o"), ("TMAP8", "o"), ("LAMMPS", "o"), ("MOOSE", "o"), ("SRIM", "r")]),
    dict(x=950, y=415, w=400, h=185, title="6 · Neutronics & breeding",
         role="Breed & shield — neutron transport, activation, blankets",
         pills=[("OpenMC", "o"), ("DAGMC", "o"), ("Paramak", "o"), ("Geant4", "o"), ("ALARA", "o"), ("FISPACT-II", "r"), ("MCNP", "x")]),
    dict(x=60, y=680, w=490, h=185, title="7 · Control & machine learning",
         role="Steer it — control, disruption prediction, surrogates",
         pills=[("KODEX", "o"), ("fusion_tcv", "o"), ("disruption-py", "o"), ("fusion_surrogates", "o"), ("TearingAvoidance", "o")]),
    dict(x=595, y=680, w=430, h=185, title="8 · Diagnostics",
         role="See it — synthetic diagnostics and inversion",
         pills=[("Cherab", "o"), ("Raysect", "o"), ("ToFu", "o"), ("FIDASIM", "o"), ("SOFT2", "o")]),
    dict(x=1070, y=680, w=550, h=185, title="9 · Experimental data",
         role="Learn from experiment — open shots, benchmarks, archives",
         pills=[("FAIR MAST", "o"), ("TokaMark", "o"), ("MDSplus", "o"), ("SPARCPublic", "o"), ("ConStellaration", "o"), ("OpenSTEP", "o")]),
    dict(x=1400, y=150, w=220, h=380, title="Nuclear & atomic data",
         role="Cross-sections & rates",
         pills=[("FENDL", "o"), ("ENDF/B", "o"), ("JEFF", "o"), ("TENDL", "o"), ("OPEN-ADAS", "o"), ("NIST ASD", "o"), ("IAEA AMDIS", "o")],
         footnote="The evaluated libraries every neutronics and spectroscopy code consumes."),
    dict(x=60, y=915, w=1560, h=80, title="SHARED LANGUAGE — STANDARDS & FRAMEWORKS", role=None,
         pills=[("IMAS Data Dictionary", "n"), ("IMAS-Python", "n"), ("OMAS", "n"), ("G-EQDSK / FreeQDSK", "n"),
                ("MDSplus", "n"), ("OMFIT", "n"), ("PlasmaPy", "n")]),
]

# (path, label, label_x, label_y)
ARROWS = [
    ("M 460 242 L 499 242", None, 0, 0),
    ("M 905 242 L 944 242", None, 0, 0),
    ("M 1150 144 C 1040 92 380 92 264 144", "iterate the design point", 710, 102),
    ("M 560 335 L 560 375 L 260 375 L 260 409", "equilibrium feeds the edge", 415, 368),
    ("M 850 335 L 850 375 L 1150 375 L 1150 409", "CAD & geometry", 1005, 368),
    ("M 1400 505 L 1356 505", None, 0, 0),
    ("M 950 507 L 911 507", "damage & activation", 928, 495),
    ("M 1070 772 L 1031 772", "real shots", 1050, 760),
    ("M 595 772 L 556 772", "synthetic ↔ measured", 575, 760),
]


def esc(s: str) -> str:
    return html.escape(s)


def pill_svg(text: str, kind: str, px: float, py: float) -> tuple[str, float]:
    w = 18 + len(text) * 7.3
    bg, ink = PILL[kind]
    return (
        f'<rect x="{px:.0f}" y="{py:.0f}" width="{w:.0f}" height="25" rx="12.5" fill="{bg}"/>'
        f'<text x="{px + w / 2:.0f}" y="{py + 17:.0f}" font-size="13" font-weight="500" fill="{ink}" text-anchor="middle">{esc(text)}</text>',
        w,
    )


def card_svg(c: dict) -> str:
    parts = [f'<rect x="{c["x"]}" y="{c["y"]}" width="{c["w"]}" height="{c["h"]}" rx="14" fill="{PANEL}" stroke="{LINE}"/>']
    if c["role"] is None:  # spine
        parts.append(f'<text x="{c["x"] + 20}" y="{c["y"] + 30}" font-size="12.5" font-weight="600" letter-spacing="1.2" fill="{MUTED}">{esc(c["title"])}</text>')
        px, py = c["x"] + 20, c["y"] + 42
    else:
        parts.append(f'<text x="{c["x"] + 18}" y="{c["y"] + 30}" font-size="17" font-weight="700" fill="{INK}">{esc(c["title"])}</text>')
        parts.append(f'<text x="{c["x"] + 18}" y="{c["y"] + 50}" font-size="12.5" font-style="italic" fill="{MUTED}">{esc(c["role"])}</text>')
        px, py = c["x"] + 18, c["y"] + 64
    x0 = px
    for text, kind in c["pills"]:
        svg, w = pill_svg(text, kind, px, py)
        if px + w > c["x"] + c["w"] - 16:
            px, py = x0, py + 33
            svg, w = pill_svg(text, kind, px, py)
        parts.append(svg)
        px += w + 8
    if py + 25 > c["y"] + c["h"] - 6:
        print(f"WARNING: pills overflow card '{c['title']}' (bottom {py + 25} > {c['y'] + c['h'] - 6})")
    if c.get("footnote"):
        words, lines, cur = c["footnote"].split(), [], ""
        for wd in words:
            if len(cur) + len(wd) + 1 > int((c["w"] - 36) / 6.3):
                lines.append(cur)
                cur = wd
            else:
                cur = f"{cur} {wd}".strip()
        lines.append(cur)
        fy = c["y"] + c["h"] - 14 - 16 * (len(lines) - 1)
        for ln in lines:
            parts.append(f'<text x="{c["x"] + 18}" y="{fy}" font-size="11.5" font-style="italic" fill="{MUTED}">{esc(ln)}</text>')
            fy += 16
    return "".join(parts)


def main() -> None:
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'font-family="Inter, -apple-system, \'Segoe UI\', Roboto, sans-serif">',
        f'<rect width="{W}" height="{H}" fill="{BG}"/>',
        '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{ARROW}"/></marker></defs>',
        # Title + legend
        f'<text x="60" y="64" font-size="34" font-weight="800" fill="{INK}" letter-spacing="-0.5">The Open Fusion Software Map</text>',
        f'<text x="60" y="92" font-size="15" fill="{MUTED}">How the ecosystem fits together — every name here lives in The Fusion Commons index, with links and access status.</text>',
        f'<circle cx="1258" cy="59" r="5.5" fill="#3ba55d"/><text x="1270" y="64" font-size="13" fill="{MUTED}">open — clone &amp; run</text>',
        f'<circle cx="1420" cy="59" r="5.5" fill="#d9a62b"/><text x="1432" y="64" font-size="13" fill="{MUTED}">registration</text>',
        f'<circle cx="1537" cy="59" r="5.5" fill="#c4453c"/><text x="1549" y="64" font-size="13" fill="{MUTED}">restricted</text>',
    ]
    for path, label, lx, ly in ARROWS:
        svg.append(f'<path d="{path}" fill="none" stroke="{ARROW}" stroke-width="2" marker-end="url(#ah)"/>')
        if label:
            svg.append(f'<text x="{lx}" y="{ly}" font-size="12" font-style="italic" fill="{MUTED}" text-anchor="middle">{esc(label)}</text>')
    for c in CARDS:
        svg.append(card_svg(c))
    svg.append(
        f'<text x="60" y="1040" font-size="13" fill="{MUTED}">The Fusion Commons · github.com/fusion-commons/index · '
        'content CC BY 4.0 · founded and maintained by Kronos Fusion Energy</text>'
    )
    svg.append("</svg>")
    OUT.write_text("\n".join(svg))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
