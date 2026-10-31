#!/usr/bin/env python3
"""Assemblage V8 du LOT_135 : fenêtres, citations retrouvées dans evidence/, taille y."""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from v8lib import abbr, bouton, ecrire, fenetre, ilot, page, sup  # noqa: E402

LOT = Path("/workspace/grok-LOTS-html/LOT_135")
EV = LOT / "evidence"
S = sup
B = bouton
A = abbr


def phrases_fichier(texte: str) -> list[str]:
    out = []
    for p in re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-Ý])", " ".join(texte.split())):
        p = " ".join(p.split())
        if not (90 <= len(p) <= 340):
            continue
        if any(s in p for s in ("http", "«", "»", "@", "h-index", "<", ">")):
            continue
        out.append(p)
    return out


def pool() -> list[tuple[str, str]]:
    vus, out = set(), []
    for f in sorted(EV.glob("*.txt")):
        for p in phrases_fichier(f.read_text(encoding="utf-8", errors="replace")):
            if p in vus:
                continue
            vus.add(p)
            out.append((f.name, p))
    return out


def W(ident: str, titre: str, paragraphes: list[str], sous: bool = False) -> str:
    corps = "\n".join(f"<p>{p}</p>" for p in paragraphes if p)
    return fenetre(ident, titre, corps, sous=sous)


def quiz(ident: str, paires: list[tuple[str, str]]) -> str:
    items = "\n".join(
        f'<details class="quiz"><summary>{html.escape(q)}</summary><p>{r}</p></details>'
        for q, r in paires
    )
    return fenetre(ident, "Pièges d'examen", "<p>Répondez, puis ouvrez la réponse.</p>\n" + items)


def paquets_citations(prefix: str, items: list[tuple[str, str]], titre: str) -> str:
    """Index cliquable + une fenêtre par phrase réellement présente dans evidence/."""
    blocs, boutons = [], []
    for i, (nom, p) in enumerate(items, 1):
        ident = f"{prefix}-q{i}"
        safe = html.escape(p)
        corps = (
            f"<p>Extrait {i}, copié depuis {html.escape(nom)}, fichier lu le 31.10.2026.</p>\n"
            f"<p>«{safe}»</p>"
        )
        blocs.append(fenetre(ident, f"Extrait {i}", corps))
        boutons.append(
            f"<p>Extrait {i}. {B(ident, 'ouvrir ' + str(i))}</p>"
        )
    index = fenetre(prefix + "-index", titre, "\n".join(boutons))
    return index + "".join(blocs)


def sources_section(lignes: list[str]) -> str:
    ol = "\n".join(f"<li>{l}</li>" for l in lignes)
    return f'''<section class="ilot v"><h2 id="sources">Sources</h2>
<details class="quiz sources"><summary>Sources lues le 31.10.2026</summary>
<ol class="sources">
{ol}
</ol>
</details></section>'''


def sommaire() -> str:
    items = [
        "Définition", "Épidémiologie", "Physiopathologie", "Démarche diagnostique",
        "Anamnèse et drapeaux rouges", "Examen physique", "Approche syndromique",
        "Diagnostic positif", "Examens complémentaires", "Arbre décisionnel",
        "Prise en charge en Suisse", "Prévention", "Points clés", "Pièges d'examen",
    ]
    lis = "\n".join(f'<li><a href="#p{i}">{i}. {t}</a></li>' for i, t in enumerate(items, 1))
    return f'''<nav class="ilot v" aria-labelledby="som">
<h2 id="som">Sommaire</h2>
<ol class="som">
{lis}
</ol>
<p class="sous">Les mots soulignés ouvrent une fenêtre. Les sources sont à la fin.</p>
</nav>'''


TITRES = [
    "Définition", "Épidémiologie", "Physiopathologie", "Démarche diagnostique",
    "Anamnèse et drapeaux rouges", "Examen physique", "Approche syndromique",
    "Diagnostic positif", "Examens complémentaires", "Arbre décisionnel",
    "Prise en charge en Suisse", "Prévention", "Points clés", "Pièges d'examen",
]


def assembler(titre_doc, h1, sous, essentiel, pts, wins, sources, fin, h2_dx=None):
    blocs = []
    if h2_dx:
        blocs.append(f"<h2>{h2_dx}</h2>")
    blocs.append(ilot(None, "", essentiel, essentiel=True))
    blocs.append(sommaire())
    for i, (titre, texte) in enumerate(zip(TITRES, pts), 1):
        blocs.append(ilot(i, titre, texte, wins.get(i, "")))
    blocs.append(sources)
    return page(titre_doc, h1, sous, blocs, fin)
