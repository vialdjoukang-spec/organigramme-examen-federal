# -*- coding: utf-8 -*-
"""Assemble les leçons du LOT_232 et mesure x / y."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "harnais"))

from habillage import bouton, fenetre, page  # noqa: E402
from cours import SITUATIONS, TABLEAU_DX, extras  # noqa: E402
from allonge import supplements  # noqa: E402
from oral import N_ORAL, oral  # noqa: E402
from rediger import COMMUN, P, SOURCES, s  # noqa: E402
from schemas import arbre, chaine, page_schema, urgence_refus  # noqa: E402
from dedoublonner import dedoublonner  # noqa: E402
import taille_xy  # noqa: E402

RACINE = Path(__file__).resolve().parents[1]
CIBLES = {
    "A": (72000, 79000),
    1: (36500, 39000),
    2: (40000, 43000),
    3: (44500, 46000),
    4: (38000, 41000),
    5: (42000, 45000),
    6: (36000, 38500),
    7: (41000, 44000),
    8: (39000, 42000),
    9: (43000, 45500),
    10: (37000, 40000),
}


def carte(resume, wid, lib):
    return f"<p>{resume} {bouton(wid, lib)}</p>"


def bloc_commun(n):
    return P(*COMMUN[n])


def assembler(h1, sous, essentiel, extra, cartes, svgs, fin, titre):
    sections = []
    for n in range(1, 15):
        wid = f"w-p{n}"
        corps = bloc_commun(n) + extra.get(n, "")
        if n in svgs:
            corps += svgs[n]
        if n == 7:
            corps += TABLEAU_DX
        sections.append((n, carte(cartes[n], wid, "ouvrir le développement"), [fenetre(wid, f"Point {n}", corps)]))
    return dedoublonner(page(fin, titre, h1, sous, essentiel, sections, SOURCES, fin))


ESSENTIEL = (
    "<p>Un geste sur le corps n'est licite que s'il est couvert par un consentement valable "
    "ou par un autre fait justificatif. Trois conditions se cumulent : information adéquate, "
    "capacité de discernement et liberté. Le refus d'une personne capable s'impose. "
    "L'incapacité ouvre les directives anticipées, puis le représentant. "
    "L'urgence, chez une personne incapable, autorise seulement les soins indispensables.</p>"
)
SOUS = (
    "Situation de départ O7.10, demande de consentement éclairé pour une intervention. "
    "Droit suisse lu le 1er novembre 2026 : code civil, directives de 2019, guide de juin 2026, "
    "loi de 2011 sur la recherche."
)


def mesurer(html):
    m = taille_xy.mesurer(html)
    return m.x[1], m.y[1], m.fen, m.dep


def ecrire(nom, html):
    chemin = RACINE / nom
    chemin.write_text(html, encoding="utf-8")
    x, y, fen, dep = mesurer(html)
    print(f"{nom}: x={x/1000:.1f} Ko y={y/1000:.1f} Ko fen={fen} dep={dep} octets={chemin.stat().st_size}")
    return x, y


def pages_schemas():
    d = RACINE / "schemas"
    d.mkdir(exist_ok=True)
    (d / "arbre.htm").write_text(page_schema("Arbre capacité et représentation", arbre(), "capa"), encoding="utf-8")
    (d / "chaine.htm").write_text(page_schema("Chaîne de l'information", chaine(), "c5"), encoding="utf-8")
    (d / "urgence.htm").write_text(page_schema("Parcours urgence et refus", urgence_refus(), "u2"), encoding="utf-8")


def _svg(n):
    if n in (1, 3, 6, 8):
        return {10: arbre()}
    if n in (2, 9):
        return {10: chaine()}
    return {10: urgence_refus()}


def construire_dx(d):
    extra, cartes = extras(d)
    extra[14] += oral(d, N_ORAL[d["n"]])
    extra.setdefault(3, "")
    pool = supplements(d) + [c + s(7, 8) for c in d.get("complements", [])]
    ymin, ymax = CIBLES[d["n"]]
    fin = f"LOT_232_Phase_B_V0_DX.{d['n']}.html"
    k = 0
    html = assembler(d["nom"], SOUS, ESSENTIEL, extra, cartes, _svg(d["n"]), fin, d["nom"])
    y = mesurer(html)[1]
    while y < ymin and k < len(pool):
        extra[3] += P(pool[k])
        k += 1
        html = assembler(d["nom"], SOUS, ESSENTIEL, extra, cartes, _svg(d["n"]), fin, d["nom"])
        y = mesurer(html)[1]
        if y > ymax and k:
            # retirer le dernier ajout
            # on reconstruit sans le dernier
            extra[3] = extra[3].rsplit("<p>", 1)[0]
            html = assembler(d["nom"], SOUS, ESSENTIEL, extra, cartes, _svg(d["n"]), fin, d["nom"])
            break
    return html


def construire_phase_a():
    extra = {n: "" for n in range(1, 15)}
    for d in SITUATIONS:
        # Une vignette par situation, répartie sur les points, pas le texte entier des DX.
        extra[1] += P(
            f"<b>{d['nom']}.</b> {d['qui']}. Geste : {d['geste']}. {d['recit']}{s(9)}"
        )
        extra[4] += P(f"Pour {d['nom'].lower()} : {d['juste']}{s(8)}")
        extra[8] += P(f"Critère de « {d['nom']} » : {d['manque']} Trace : {d['dossier']}{s(9)}")
        extra[11] += P(f"Conduite de « {d['nom']} » : {d['juste']} Phrase dite : {d['dit']}{s(8)}")
        extra[14] += P(f"Piège de « {d['nom']} » : {d['piege']}{s(7)}")
    # Cartes de la phase A : courtes, transversales.
    cartes = {
        1: "Le consentement est l'autorisation qui rend licite une atteinte à l'intégrité. Trois conditions se cumulent.",
        2: "En 2022, 24 pour cent des adultes interrogés ont rédigé des directives. La synthèse de 2018 en trouve 16 pour cent déposées.",
        3: "Le raisonnement est normatif : atteinte, puis fait justificatif. Le défaut d'une condition rend l'acte illicite.",
        4: "On commence par l'urgence vitale, puis la capacité, puis les directives et le représentant.",
        5: "L'entretien vérifie ce qui a été compris, la pression d'un tiers, et l'existence de directives.",
        6: "Les quatre capacités de 2019 se jugent pour une décision et un moment. Un test cognitif bref ne tranche pas.",
        7: "Dix situations se séparent par un fait dominant. Le tableau comparatif est dans la fenêtre.",
        8: "Le diagnostic de situation s'écrit : information, capacité, liberté, et la trace.",
        9: "Les pièces sont la trace, la carte d'assuré, les directives, le représentant ou l'interprète.",
        10: "Trois schémas : capacité et représentation, chaîne de l'information, urgence et refus.",
        11: "En Suisse, on informe, on respecte le refus capable, on suit les articles 377 à 381 si la personne est incapable.",
        12: "On sépare l'entretien de la signature d'accueil. On confirme avant toute sédation.",
        13: "Un geste non consenti reste illicite, même bien fait. La recherche obéit à une autre loi.",
        14: "Les pièges classiques : la signature, le risque grave tu, l'incapacité collée au refus, le proche traducteur.",
    }
    svgs = {10: arbre() + chaine() + urgence_refus()}
    fin = "LOT_232_Phase_A_V0.html"
    titre = "Demande de consentement éclairé pour une intervention"
    pool = []
    for d in SITUATIONS:
        for i, para in enumerate(supplements(d)):
            # Le titre de la situation une seule fois : pas de <h3> répété (porte, phrase_double).
            pool.append((f"<h3>Développements : {d['nom'].lower()}</h3>\n" if i == 0 else "") + P(para))
    ymin, ymax = CIBLES["A"]
    html = assembler(titre, SOUS, ESSENTIEL, extra, cartes, svgs, fin, titre)
    y = mesurer(html)[1]
    k = 0
    while y < ymin and k < len(pool):
        extra[11] += pool[k]
        k += 1
        html = assembler(titre, SOUS, ESSENTIEL, extra, cartes, svgs, fin, titre)
        y = mesurer(html)[1]
        if y > ymax:
            extra[11] = extra[11][: len(extra[11]) - len(pool[k - 1])]
            html = assembler(titre, SOUS, ESSENTIEL, extra, cartes, svgs, fin, titre)
            break
    return html


def main():
    pages_schemas()
    ecrire("LOT_232_Phase_A_V0.html", construire_phase_a())
    for d in SITUATIONS:
        ecrire(f"LOT_232_Phase_B_V0_DX.{d['n']}.html", construire_dx(d))


if __name__ == "__main__":
    main()
