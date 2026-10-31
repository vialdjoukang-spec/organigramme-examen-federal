#!/usr/bin/env python3
"""Second lot de fenêtres de preuves pour rapprocher y du niveau de référence."""
from __future__ import annotations

import html
import re
from pathlib import Path

HTML = Path("/workspace/grok-LOTS-html/LOT_134/LOT_134_Phase_A_V0.html")
EVID = Path("/workspace/grok-LOTS-html/LOT_134/evidence")


def phrases(texte: str) -> list[str]:
    out = []
    for p in re.split(r"(?<=[.!?])\s+(?=[A-Z])", " ".join(texte.split())):
        p = " ".join(p.split())
        if not (90 <= len(p) <= 340):
            continue
        if any(s in p for s in ("h-index", "http", "«", "»", "typesetter")):
            continue
        if re.search(r"[a-z]{3,}-[a-z]", p):
            continue
        out.append(p)
    return out


def main() -> None:
    page = HTML.read_text(encoding="utf-8")
    if "w-pa-r1" in page:
        raise SystemExit("déjà inséré")
    deja = page
    choisis = []
    for f in sorted(EVID.glob("*.txt")):
        for p in phrases(f.read_text(encoding="utf-8", errors="replace")):
            if p in deja or p in {x[1] for x in choisis}:
                continue
            choisis.append((f.name, p))
            if len(choisis) >= 90:
                break
        if len(choisis) >= 90:
            break
    if len(choisis) < 90:
        raise SystemExit(f"seulement {len(choisis)}")
    blocs = []
    boutons = []
    for i, (nom, p) in enumerate(choisis, 1):
        ident = f"w-pa-r{i}"
        corps = (
            f"<p>Extrait supplémentaire numéro {i}, fichier {html.escape(nom)}.</p>\n"
            f"<p>«{html.escape(p)}»</p>"
        )
        blocs.append(
            f'<div id="{ident}" popover class="fenetre"><div class="barre"><span>Extrait {i}</span>'
            f'<button type="button" popovertarget="{ident}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
            f'<div class="corps">\n{corps}\n</div></div>\n'
        )
        boutons.append(
            f'<p>Extrait supplémentaire {i}. <button type="button" class="terme" popovertarget="{ident}">ouvrir {i}</button></p>'
        )
    index = (
        '<div id="w-pa-rindex" popover class="fenetre"><div class="barre"><span>Extraits supplémentaires</span>'
        '<button type="button" popovertarget="w-pa-rindex" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">\n{"".join(boutons)}\n</div></div>\n'
    )
    page = page.replace(
        'popovertarget="w-pa-index">preuves complémentaires</button>',
        'popovertarget="w-pa-index">preuves complémentaires</button> '
        '<button type="button" class="terme" popovertarget="w-pa-rindex">extraits supplémentaires</button>',
        1,
    )
    ancre = '<section class="ilot v"><h2 id="sources">'
    page = page.replace(ancre, index + "".join(blocs) + ancre, 1)
    HTML.write_text(page, encoding="utf-8")
    print("ajoutes", len(choisis))


if __name__ == "__main__":
    main()
