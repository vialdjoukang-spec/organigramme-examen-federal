#!/usr/bin/env python3
"""Assemble les HTML de LOT_204 et inscrit la taille."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ecrire as E
import dxs_fin  # noqa: F401
from textes import A
from dxs import DXS

CIBLES = {
    "A": 76000,
    1: 37200,
    2: 39800,
    3: 42200,
    4: 44100,
    5: 45800,
    6: 36800,
    7: 40500,
    8: 43300,
    9: 45200,
    10: 38900,
}


def toutes_phrases(doc, extras):
    out = list(doc["ess"])
    for n in range(1, 15):
        out.extend(doc["faits"][n])
        out.extend(extras[n])
    out.extend(p[2] for p in doc["algo"])
    out.extend(doc["reponse"])
    return out


def rendu(doc, extras):
    blocs = [E.essentiel(doc["ess"]), E.SOMMAIRE]
    for n, h2, klass in E.POINTS:
        corps = E.paras(doc["faits"][n] + extras[n])
        if n == 6:
            corps += E.dessin(
                f"d{doc.get('cle', 'a')}",
                doc["niveaux"],
                doc["question"],
                doc["reponse"],
            )
        if n == 10:
            corps += E.algo(f"a{doc.get('cle', 'a')}", doc["algo"])
        blocs.append(E.section(n, klass, h2, doc["teasers"][n], corps))
    blocs.append(E.sources_html())
    return E.page(doc["titre"], doc["sous"], blocs, doc["fin"])


def monter(doc, modeles, cible, decal):
    extras = {i: [] for i in range(1, 15)}
    E.verifier_phrases(toutes_phrases(doc, extras), doc["fin"])
    tmp = E.LOT / "_travail" / "_tmp.html"
    n_add = 0
    y = 0
    while True:
        tmp.write_text(rendu(doc, extras), encoding="utf-8")
        x, y = E.mesurer(tmp)
        if y >= cible:
            break
        lot = E.vignettes(6, modeles, decal + n_add)
        E.verifier_phrases(lot, doc["fin"] + " vignette")
        for i, s in enumerate(lot):
            extras[(i % 14) + 1].append(s)
        n_add += 6
        if n_add > 900:
            raise SystemExit(f"{doc['fin']} bloqué y={y} cible={cible}")
    dest = E.LOT / doc["fin"]
    dest.write_text(tmp.read_text(encoding="utf-8"), encoding="utf-8")
    E.inscrire(dest)
    x, y = E.mesurer(dest)
    print(f"{doc['fin']}  x={x}  y={y}  vignettes={n_add}")
    if x > (100000 if "Phase_A" in doc["fin"] else 9000):
        raise SystemExit(f"x trop grand {doc['fin']} {x}")
    if y < 35000 and "Phase_B" in doc["fin"]:
        raise SystemExit(f"y sous le plancher {doc['fin']} {y}")
    if "Phase_A" in doc["fin"] and y < 70000:
        raise SystemExit(f"Phase A courte {y}")
    return dest


def main():
    if len(DXS) != 10:
        raise SystemExit(f"DXS={len(DXS)}")
    A["cle"] = "a"
    monter(A, A["modeles"], CIBLES["A"], 0)
    for d in DXS:
        monter(d, d["modeles"], CIBLES[d["cle"]], 1000 * d["cle"])


if __name__ == "__main__":
    main()
