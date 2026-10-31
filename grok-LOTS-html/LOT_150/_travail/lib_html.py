#!/usr/bin/env python3
"""Briques V8 du LOT_150. Ne produit pas de dose hors des extraits AIPS."""
from __future__ import annotations

import html
import re
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
EV = RACINE / "grok-LOTS-html" / "LOT_150" / "evidence"
MODELE = RACINE / "harnais" / "modele_lecon" / "MODELE_DD_V8.html"


def style_et_liens() -> str:
    m = MODELE.read_text(encoding="utf-8")
    liens = re.search(r"<link rel=\"preconnect\".*", m).group(0)
    style = re.search(r"<style>.*?</style>", m, re.S).group(0)
    return liens + "\n" + style


def e(s: str) -> str:
    return html.escape(s, quote=False)


def A(sigle: str, titre: str) -> str:
    return f'<abbr title="{html.escape(titre, quote=True)}">{e(sigle)}</abbr>'


def S(*nums: int) -> str:
    return '<sup class="s">' + ",".join(str(n) for n in nums) + "</sup>"


def b(pid: str, mot: str) -> str:
    return f'<button type="button" class="terme" popovertarget="{pid}">{mot}</button>'


def fen(pid: str, titre: str, inner: str, sous: bool = False) -> str:
    cls = "fenetre sousf" if sous else "fenetre"
    return (
        f'<div id="{pid}" popover class="{cls}"><div class="barre"><span>{titre}</span>'
        f'<button type="button" popovertarget="{pid}" popovertargetaction="hide" aria-label="Fermer">✕</button>'
        f'</div><div class="corps">{inner}</div></div>'
    )


def P(*parts: str) -> str:
    return "<p>" + " ".join(parts) + "</p>"


def table(caption: str, headers: list[str], rows: list[list[str]]) -> str:
    th = "".join(f"<th>{h}</th>" for h in headers)
    body = "\n".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return (
        f'<div class="tw"><table><caption>{caption}</caption><thead><tr>{th}</tr></thead>'
        f"<tbody>\n{body}\n</tbody></table></div>"
    )


def _motif(s: str) -> str:
    return r"\s+".join(re.escape(p) for p in s.split())


def cite(fn: str, ancre: str, fin: str | None = None) -> str:
    t = (EV / fn).read_text(encoding="utf-8")
    m = re.search(_motif(ancre), t)
    if not m:
        raise SystemExit(f"ancre absente dans {fn} : {ancre[:80]}")
    if fin is None:
        frag = m.group(0)
    else:
        m2 = re.search(_motif(fin), t[m.end():])
        if not m2:
            raise SystemExit(f"fin absente dans {fn} : {fin[:60]}")
        frag = t[m.start(): m.end() + m2.start()]
    frag = " ".join(frag.split())
    if "«" in frag or "»" in frag:
        raise SystemExit(f"guillemet interne : {frag[:80]}")
    if not (40 <= len(frag) <= 380):
        raise SystemExit(f"citation {len(frag)} car. : {frag[:80]}")
    return "«" + e(frag) + "»"


def ilot(cid: str, cls: str, titre: str, inner: str) -> str:
    return f'<section class="ilot {cls}"><h2 id="{cid}">{titre}</h2>\n{inner}\n</section>\n'


def page(nom_fichier: str, titre: str, sous: str, blocs: list[str], h2_dx: str | None = None) -> str:
    dx = f"<h2>{h2_dx}</h2>\n" if h2_dx else ""
    corps = "\n".join(blocs)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titre)}</title>
{style_et_liens()}
</head>
<body>
<main>
<h1 id="titre">{titre}</h1>
{dx}<p class="taille" id="taille">Taille : en cours de mesure</p>
<p class="sous">{sous}</p>
{corps}
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- FIN_FICHIER {nom_fichier} -->
"""
