#!/usr/bin/env python3
"""Capture Playwright partagée. Jamais si l'API a déjà livré l'image."""
import subprocess
from pathlib import Path

ICI = Path(__file__).resolve().parent
MJS = ICI / "capture.mjs"


def capturer(url, dest, selecteur="canvas, img, svg"):
    """Pipeline B (visionneuse) ou figure sans fichier direct."""
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not url:
        return False, "URL de capture absente"
    r = subprocess.run(
        ["node", str(MJS), url, str(dest), selecteur],
        cwd="/tmp/fedmed-pw",
        capture_output=True, text=True, timeout=40,
    )
    if r.returncode != 0 or not dest.is_file():
        return False, (r.stderr or r.stdout or "capture échouée")[:180]
    return True, "capture"


def rendu_trace(svg, dest):
    """Pipeline D : un tracé déjà dessiné en SVG, photographié, pas recréé depuis un signal brut ici."""
    html = f"<html><body style='margin:0;background:#fff'>{svg}</body></html>"
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    page = dest.with_suffix(".html")
    page.write_text(html, encoding="utf-8")
    return capturer(page.as_uri(), dest, "svg")
