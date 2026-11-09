#!/usr/bin/env python3
"""Texte français du LOT_130. Chaque chiffre est cité vers preuves.jsonl."""
from __future__ import annotations
import html
from fabriquer import p, fen, table, cite, DX

_n = 0

def W(prefix: str, label: str, pid: str) -> tuple[str, str]:
    global _n
    _n += 1
    return fen(prefix, f"{prefix}-f{_n}", label, pid)

def h4(titre: str) -> str:
    return f'<h4 class="struct">{html.escape(titre)}</h4>\n'

def cell(texte: str, ids: list[str]) -> str:
    return texte + cite(ids)

def pack(morceaux: list[str], fenetres: list[str]) -> str:
    return "".join(morceaux) + "".join(fenetres)

def urgence(prefix: str, lignes: list[tuple[str, list[str]]]) -> str:
    fid = f"{prefix}-p11-urgence"
    corps = "".join(p(t, ids) for t, ids in lignes)
    return (
        f'<p>La <button type="button" class="fen" popovertarget="{fid}">conduite chronologique</button> '
        f'suit l’atteinte, sans attendre un bilan exhaustif.</p>\n'
        f'<div id="{fid}" popover class="fenetre">\n'
        f'<button type="button" popovertarget="{fid}" popovertargetaction="hide">Fermer</button>\n'
        f'<p class="urg">Urgence, conduite chronologique.</p>\n{corps}</div>\n'
    )

def rendre(prefix: str, spec: list[list]) -> list[str]:
    """Chaque point est une liste de chaînes HTML ou de tuples (texte, ids, etiquette, preuve)."""
    out = []
    for bloc in spec:
        morceaux, fenetres = [], []
        for item in bloc:
            if isinstance(item, str):
                morceaux.append(item if item.endswith("\n") else item + "\n")
                continue
            texte, ids, etiq, pid = item
            if texte.startswith("Posologie"):
                texte = "La " + texte[0].lower() + texte[1:].replace(" : À vérifier (AIPS).", " demeure à vérifier dans l'information professionnelle suisse.")
            if etiq and pid:
                bouton, div = W(prefix, etiq, pid)
                morceaux.append(p(texte + " " + bouton, ids))
                fenetres.append(div)
            else:
                morceaux.append(p(texte, ids))
        out.append(pack(morceaux, fenetres))
    if len(out) != 14:
        raise SystemExit(f"{prefix}: {len(out)} points")
    return out
