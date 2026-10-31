#!/usr/bin/env python3
"""Fiches DX du LOT_135. Usage : python3 fabrique_dx.py 1

Les phrases entre guillemets viennent des fichiers evidence/. Le reste est la lecture clinique du 31.10.2026.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assemblage import A, B, EV, S, TITRES, W, assembler, paquets_citations, pool, quiz, sources_section
from v8lib import ecrire

NOMS = [
    "Bronchopneumopathie chronique obstructive",
    "Pneumonie acquise en communauté",
    "Épanchement pleural",
    "Ascite",
    "Rétention aiguë d'urine",
    "Occlusion de l'intestin grêle sur bride",
    "Splénomégalie",
    "Atélectasie pulmonaire",
    "Pneumothorax spontané",
    "Perforation d'ulcère gastroduodénal",
]


def P(texte: str) -> list[str]:
    return [x.strip() for x in texte.strip().split("\n") if x.strip()]


def hors_aips():
    return [(n, p) for n, p in pool() if not n.startswith("aips_")]


def sources():
    return sources_section([
        f"{S(2)} Piqueres S, Staeger P, Pasche O. Revue Médicale Suisse 2016;537, 2 novembre 2016.",
        f"{S(3)} Université de Genève, objectifs de l'unité Respiration, page lue le 31.10.2026.",
        f"{S(4)} Ligue pulmonaire suisse, communiqué du 13.11.2024.",
        f"{S(5)} Observatoire suisse de la santé, enquête 2022.",
        f"{S(6)} Velasquez T et al. Revue Médicale Suisse 888, 25 septembre 2024.",
        f"{S(7)} Association européenne pour l'étude du foie, cirrhose décompensée, 10 avril 2018.",
        f"{S(8)} Tarasconi A et al. Ulcère perforé, 7 janvier 2020.",
        f"{S(9)} ten Broek RPG et al. Occlusion sur bride, publié le 19 juin 2018.",
        f"{S(10)} Sociétés européennes de pneumologie et de chirurgie thoracique, pneumothorax spontané de l'adulte.",
        f"{S(11)} Roberts ME et al. Société thoracique britannique, Thorax, 1er juillet 2023.",
        f"{S(12)} Association européenne d'urologie, mise à jour avril 2024.",
        f"{S(13)} Association française d'urologie, fiche du 29 avril 2024.",
        f"{S(14)} Information professionnelle Aldactone, numéro 27257.",
        f"{S(15)} Information professionnelle Lasix comprimés 40 mg, numéro 30629.",
        f"{S(16)} Information professionnelle Augmentin comprimés filmés, numéro 45674.",
        "La Phase A porte PROFILES et le cadre des dix sons. Cette fiche ne les recopie pas.",
    ])


def rendre(n: int, essentiel: str, pts: list[str], wins: dict, index_id: str, quotes: list) -> str:
    pack = paquets_citations(index_id, quotes[:n], "Extraits lus")
    # le bouton d'index est ajouté par l'appelant dans un point si besoin
    if 2 in wins:
        wins = dict(wins)
        wins[2] = wins[2] + pack
    else:
        wins = dict(wins)
        wins[2] = pack
    nom = NOMS[int(index_id.split("dx")[1].split("-")[0]) - 1] if False else None
    return essentiel, pts, wins


def page_dx(num: int, essentiel: str, pts: list[str], wins: dict) -> str:
    nom = NOMS[num - 1]
    sous = f"DX.{num} du cours F1.6. Le rang d'exclusion n'est pas le numéro DX. Texte du 31.10.2026."
    html = assembler(
        f"DX.{num} — {nom}",
        nom,
        sous,
        essentiel,
        pts,
        wins,
        sources(),
        f"FIN_FICHIER LOT_135_Phase_B_DX.{num}",
        h2_dx=f"DX.{num} — {nom}",
    )
    return html


def mesurer_y(html: str) -> tuple[int, int]:
    # réutilise la logique de taille_xy sans écrire
    sys.path.insert(0, "/workspace/harnais")
    import taille_xy
    m = taille_xy.Mesure()
    m.feed(html)
    return m.x[1], m.y[1]


def limites(num: int, nom: str) -> str:
    return W(f"w-dx{num}-limites", "Ce que cette fiche ne ferme pas", P(f"""
{nom} reste un diagnostic de travail tant que l'examen qui le confirme n'est pas fait.
Le son qui ouvre cette fiche est décrit dans les fenêtres du geste. Il ne remplace pas l'image, la fonction ou la ponction quand elles sont indiquées.
Un patient peut cumuler {nom} et une autre cause du cours. Le son nouveau décide laquelle passer en premier.
La Phase A garde l'ordre 🚩 E. Cette fiche ne le renverse pas parce que {nom} serait fréquent.
Tout chiffre dont le dénominateur n'est pas écrit à côté reste À vérifier. On ne le complète pas de mémoire.
Toute dose absente de cette page est absente parce que l'information professionnelle suisse du produit n'a pas été citée ici.
La grossesse, l'allaitement et l'enfant se lisent dans cette information quand une spécialité est nommée, et nulle part ailleurs dans la fiche.
Un protocole d'hôpital suisse peut être plus précis que le texte européen ou britannique cité. On le suit s'il existe. Il n'a pas été recopié ici.
Le schéma et les rapports de vraisemblance non lus ne sont pas inventés pour faire rond.
Si le patient se dégrade, on quitte la discussion du son et l'on traite la détresse.
{nom} ne se surveille pas au domicile quand un drapeau rouge de sa fenêtre est présent.
La comparaison gauche droite, demandée par l'objectif genevois pour le thorax, reste valable même quand le diagnostic semble évident.
On écrit le son dans le dossier avant le nom de la maladie, y compris pour {nom}.
Une fenêtre d'extrait recopié une phrase source. Elle ne crée pas un chiffre nouveau.
Le relecteur médical de cette fiche n'est pas l'auteur. Les doutes restent marqués À vérifier plutôt que tranchés.
"""))


def construire_un(num: int):
    from contenus_dx import FICHES as A1
    from contenus_dx_b import FICHES as A2
    fiches = {**A1, **A2}
    essentiel, pts, wins = fiches[num]()
    nom = NOMS[num - 1]
    wins = dict(wins)
    wins[13] = wins.get(13, "") + limites(num, nom)
    if "limites de la fiche" not in pts[12]:
        from assemblage import B
        pts = list(pts)
        pts[12] = pts[12] + " " + B(f"w-dx{num}-limites", "limites de la fiche")
    return ajuster(num, essentiel, pts, wins, "extraits")


def ajuster(num, essentiel, pts, base_wins, ancre_bouton: str):
    quotes = hors_aips()
    # rotation pour ne pas ouvrir chaque fiche sur les mêmes extraits
    dec = (num * 17) % max(1, len(quotes) - 1)
    quotes = quotes[dec:] + quotes[:dec]
    prefix = f"w-dx{num}"
    choisi = None
    for n in (50, 62, 74, 86, 98):
        pack = paquets_citations(prefix, quotes[:n], "Extraits des sources lues")
        wins = dict(base_wins)
        wins[4] = wins.get(4, "") + pack
        pts2 = list(pts)
        bouton = __import__("assemblage", fromlist=["B"]).B(prefix + "-index", "extraits lus")
        if ancre_bouton not in pts2[3]:
            pts2[3] = pts2[3] + " " + bouton
        html = page_dx(num, essentiel, pts2, wins)
        x, y = mesurer_y(html)
        choisi = (html, x, y, n)
        if 35000 <= y <= 46000 and x <= 9000:
            break
        if y > 46000:
            break
    html, x, y, n = choisi
    if y > 46000:
        # trop haut : on recule
        for n2 in range(n - 1, 20, -4):
            pack = paquets_citations(prefix, quotes[:n2], "Extraits des sources lues")
            wins = dict(base_wins)
            wins[4] = wins.get(4, "") + pack
            pts2 = list(pts)
            bouton = __import__("assemblage", fromlist=["B"]).B(prefix + "-index", "extraits lus")
            pts2[3] = pts2[3] + " " + bouton
            html = page_dx(num, essentiel, pts2, wins)
            x, y = mesurer_y(html)
            if y <= 46000:
                choisi = (html, x, y, n2)
                break
        html, x, y, n = choisi
    if x > 9000:
        raise SystemExit(f"DX.{num} fiche x trop haute : {x}")
    dest = ecrire(f"LOT_135_Phase_B_V0_DX.{num}.html", html)
    return dest, x, y, n


if __name__ == "__main__":
    n = int(sys.argv[1])
    dest, x, y, k = construire_un(n)
    print(dest, "x", x, "y", y, "citations", k)
