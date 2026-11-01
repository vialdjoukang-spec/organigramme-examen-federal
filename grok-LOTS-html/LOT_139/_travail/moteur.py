#!/usr/bin/env python3
"""Assemble les leçons V8 du LOT_139. Zéro réseau. Les schémas viennent du dessinateur."""
from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_139"
STYLE_SRC = RACINE / "grok-LOTS-html" / "LOT_162" / "LOT_162_Phase_A_V0.html"
DESSIN = RACINE / "grok-LOTS-html" / "outils" / "dessinateur" / "dessinateur.py"

DX = [
    (1, "Hypoxémie pulmonaire aiguë"),
    (2, "Embolie pulmonaire"),
    (3, "Œdème aigu du poumon"),
    (4, "Exacerbation de bronchopneumopathie chronique obstructive"),
    (5, "Obstruction des voies aériennes et hypoventilation"),
    (6, "Cardiopathie cyanogène à shunt droit-gauche"),
    (7, "Méthémoglobinémie"),
    (8, "Cyanose périphérique et choc"),
    (9, "Shunt intrapulmonaire"),
    (10, "Pseudocyanose et sulfhémoglobinémie"),
]


def style() -> str:
    t = STYLE_SRC.read_text(encoding="utf-8")
    i, j = t.find("<style>"), t.find("</style>")
    return t[i : j + len("</style>")]


def schema(nom_json: str) -> str:
    spec = importlib.util.spec_from_file_location("dessinateur_lot139", DESSIN)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    desc = json.loads((LOT / "figures" / nom_json).read_text(encoding="utf-8"))
    frag = mod.rendre(desc, "grok-LOTS-html/outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf")
    frag = re.sub(r"<script\b[^>]*>.*?</script>", "", frag, flags=re.I | re.S)
    if "<script" in frag.lower():
        raise SystemExit("script restant dans le schéma")
    return frag


def s(n: int, html: str) -> str:
    return f"{html}<sup class=\"s\">{n}</sup>"


def fen(fid: str, titre: str, corps: str) -> str:
    return (
        f'<div id="{fid}" popover class="fenetre"><div class="barre"><span>{titre}</span>'
        f'<button type="button" popovertarget="{fid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">{corps}</div></div>'
    )


def boutons(pairs: list[tuple[str, str]]) -> str:
    return " ".join(
        f'<button type="button" class="terme" popovertarget="{i}">{label}</button>' for i, label in pairs
    )


def paras(lignes: list[str]) -> str:
    return "".join(f"<p>{x}</p>" for x in lignes)


def table(caption: str, headers: list[str], rows: list[list[str]]) -> str:
    th = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tw"><table><caption>{caption}</caption><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def page(nom_fichier: str, h1: str, sous: str, essentiel: str, sections: list[str], sources: list[str]) -> str:
    src = "".join(f"<li>{x}</li>" for x in sources)
    html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{h1}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&amp;display=swap" rel="stylesheet">
{style()}
</head>
<body>
<main>
<h1 id="titre">{h1}</h1>
<p class="taille" id="taille">Taille : en cours</p>
<p class="sous">{sous}</p>
<section class="ilot c essentiel" aria-labelledby="ess">
<h2 id="ess">L'essentiel</h2>
<p>{essentiel}</p>
</section>
<nav class="ilot v" aria-labelledby="som">
<h2 id="som">Sommaire</h2>
<ol class="som">
<li><a href="#p1">Définition</a></li><li><a href="#p2">Épidémiologie</a></li><li><a href="#p3">Physiopathologie</a></li><li><a href="#p4">Démarche diagnostique</a></li><li><a href="#p5">Anamnèse et drapeaux rouges</a></li><li><a href="#p6">Examen physique</a></li><li><a href="#p7">Approche syndromique</a></li><li><a href="#p8">Diagnostic positif</a></li><li><a href="#p9">Examens complémentaires</a></li><li><a href="#p10">Arbre décisionnel</a></li><li><a href="#p11">Prise en charge</a></li><li><a href="#p12">Prévention</a></li><li><a href="#p13">Points clés</a></li><li><a href="#p14">Pièges et cas</a></li>
</ol>
<p class="sous">Les mots soulignés ouvrent une fenêtre. Les sources sont en bas.</p>
</nav>
{''.join(sections)}
<section class="ilot c sources" aria-labelledby="sources">
<h2 id="sources">Sources</h2>
<ol class="sources">
{src}
</ol>
<p>Les fenêtres portent le même numérotage. Le détail des extraits est dans le dossier evidence.</p>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</section>
</main>
</body>
</html>
<!-- FIN_FICHIER {nom_fichier} -->
"""
    chemin = LOT / nom_fichier
    chemin.write_text(html, encoding="utf-8")
    # inscrire la taille
    sys.path.insert(0, str(RACINE / "harnais"))
    import taille_xy
    taille_xy.main([str(chemin), "--inscrire"])
    m = taille_xy.mesurer(chemin.read_text(encoding="utf-8"))
    print(f"{nom_fichier} x={m.x[1]} y={m.y[1]} fen={m.fen}")
    return str(chemin)


SOURCES = [
    "Elsasser S. Cyanose. Forum Médical Suisse, 7 mai 2003.",
    "Rosset-Zufferey S, Ramlawi M. Revue Médicale Suisse 482, 12 août 2015.",
    "Coste F et collaborateurs. Revue Médicale Suisse 804, 16 novembre 2022.",
    "Cuénoud A et collaborateurs. Revue Médicale Suisse 940, 19 novembre 2025.",
    "O'Driscoll BR et collaborateurs. Thorax, 2017, oxygénothérapie de la British Thoracic Society.",
    "Konstantinides SV et collaborateurs. European Heart Journal, 31 août 2019, recommandations ESC avec l'ERS.",
    "Chlorure de méthylthioninium Proveblue, information professionnelle, numéro 67440.",
    "Lasix solution injectable, information professionnelle, numéro 30630.",
    "Ventolin, information professionnelle, numéro 37397.",
]
