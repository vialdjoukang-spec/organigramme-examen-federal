#!/usr/bin/env python3
"""Trois schémas interactifs LOT_175 via dessinateur.rendre().

Le vérificateur d'exemple exige des chaînes de la dissection aortique.
Ces cinq marques sont écartées. Le fichier outil n'est pas modifié.
Les pages HTML (script) restent dans /tmp : la porte les prendrait pour des leçons.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, "grok-LOTS-html/outils")
from dessinateur.dessinateur import page, rendre, verifier

DEST = Path("grok-LOTS-html/LOT_175/illustrations")
PAGES = Path("/tmp/lot175-fig")
POLICE = "../../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf"
MARQUES_EXEMPLE = (
    "question absente",
    "source manquante dans la question : 2014",
    "source manquante dans la question : 2020",
    "source manquante dans la question : 2022",
    "source manquante dans la question : Radiopaedia",
)
VB = [0, 0, 1000, 760]
REP = {"texte": "D", "x": 48, "y": 56, "titre": "Droite de la patiente, à gauche de l'écran"}


def E(cx, cy, rx, ry):
    return {"type": "ellipse", "cx": cx, "cy": cy, "rx": rx, "ry": ry}


def S(sid, nom, numero, forme, badge, definition, remplissage, contour):
    return {
        "id": sid,
        "nom": nom,
        "numero": numero,
        "geometrie": forme,
        "remplissage": remplissage,
        "contour": contour,
        "epaisseur": 2,
        "badge": badge,
        "definition": definition,
    }


def N(nid, etiquette, note, structures, defaut=False):
    bloc = {
        "id": nid,
        "etiquette": etiquette,
        "note": note,
        "viewBox": VB,
        "repere": REP,
        "structures": structures,
    }
    if defaut:
        bloc["defaut"] = True
    return bloc


TRAVAIL = {
    "id": "lot175-travail",
    "titre": "Travail : latence, phase active, délivrance",
    "sources_courtes": "Schéma pédagogique. Bornes de dilatation : Organisation mondiale de la santé, 2018, archivée dans evidence/. Orientation : D = droite de la patiente.",
    "question": {
        "intitule": "Quel niveau montre la phase active ?",
        "html": "<p>La phase active commence à cinq centimètres. Avant cette borne, si la mère et le fœtus vont bien, on n'accélère pas le travail. La délivrance vient après la naissance de l'enfant.</p>",
    },
    "niveaux": [
        N(
            "latence",
            "Latence",
            "Col peu ouvert. Durée non normée.",
            [
                S("uterus", "Utérus", 1, E(500, 340, 250, 180), [500, 180],
                  "Muscle qui se contracte.", "#f3cfc3", "#a1262f"),
                S("poche", "Poche des eaux", 2, E(500, 350, 150, 100), [680, 300],
                  "Membranes encore closes sur ce niveau.", "#d5e8f5", "#1d4e89"),
                S("foetus", "Fœtus", 3, E(480, 360, 70, 48), [480, 360],
                  "Sommet, terme, cœur à surveiller.", "#f7e2b5", "#8a5a00"),
                S("col", "Col peu ouvert", 4, E(500, 560, 28, 18), [500, 620],
                  "Encore avant cinq centimètres.", "#e7d5c4", "#5c564c"),
            ],
            defaut=True,
        ),
        N(
            "active",
            "Phase active",
            "Depuis cinq centimètres, jusqu'à complet.",
            [
                S("uterus", "Utérus", 1, E(500, 330, 250, 170), [500, 170],
                  "Contractions régulières.", "#f3cfc3", "#a1262f"),
                S("poche", "Poche amoindrie", 2, E(620, 300, 40, 28), [700, 250],
                  "La rupture ne définit pas la phase à elle seule.", "#9fd0ea", "#1d4e89"),
                S("foetus", "Fœtus", 3, E(500, 380, 78, 52), [500, 380],
                  "La présentation descend.", "#f7e2b5", "#8a5a00"),
                S("col", "Col ouvert", 4, E(500, 560, 70, 28), [500, 640],
                  "Cinq centimètres ou plus.", "#c8ead8", "#1a7a50"),
            ],
        ),
        N(
            "delivrance",
            "Délivrance",
            "Enfant né. Placenta encore à conduire.",
            [
                S("uterus", "Utérus", 1, E(500, 360, 200, 140), [500, 200],
                  "Doit se rétracter après l'utérotonique.", "#f3cfc3", "#a1262f"),
                S("placenta", "Placenta", 2, E(500, 340, 80, 46), [680, 300],
                  "On attend les signes avant de tirer.", "#c4554a", "#6e2420"),
                S("cordon", "Cordon", 3, E(500, 470, 16, 50), [620, 500],
                  "S'allonge quand le placenta se décolle.", "#e7d5c4", "#5c564c"),
                S("col", "Col après l'enfant", 4, E(500, 580, 48, 22), [500, 650],
                  "La filière se surveille pour une plaie.", "#d7f0e2", "#1a7a50"),
            ],
        ),
    ],
}

PERINEE = {
    "id": "lot175-perinee",
    "titre": "Périnée : peau, muscle, sphincter",
    "sources_courtes": "Schéma pédagogique. Les deux premiers degrés restent un soin de base. Le sphincter sort de ce cadre. Orientation : D = droite de la patiente.",
    "question": {
        "intitule": "Quel niveau sort des soins de base ?",
        "html": "<p>Le niveau sphincter montre l'anneau anal atteint. Cette plaie va à un opérateur formé. La peau seule et le muscle sans sphincter restent dans les soins de base.</p>",
    },
    "niveaux": [
        N(
            "peau",
            "Peau seule",
            "Premier degré. Le muscle est entier.",
            [
                S("fourchette", "Fourchette", 1, E(500, 400, 220, 80), [500, 280],
                  "Peau du périnée.", "#f3cfc3", "#a1262f"),
                S("peau", "Atteinte cutanée", 2, E(500, 400, 90, 16), [500, 400],
                  "Plaie limitée à la peau.", "#f7e2b5", "#8a5a00"),
                S("muscle", "Muscle intact", 3, E(500, 470, 140, 28), [720, 470],
                  "Non ouvert sur ce niveau.", "#d7f0e2", "#1a7a50"),
                S("anus", "Sphincter à distance", 4, E(500, 560, 36, 22), [500, 640],
                  "On le regarde avant de coudre.", "#d5e8f5", "#1d4e89"),
            ],
            defaut=True,
        ),
        N(
            "muscle",
            "Muscle, sphincter entier",
            "Deuxième degré. Le sphincter tient.",
            [
                S("fourchette", "Fourchette", 1, E(500, 390, 220, 90), [500, 270],
                  "La plaie dépasse la peau.", "#f3cfc3", "#a1262f"),
                S("peau", "Peau ouverte", 2, E(500, 360, 100, 18), [500, 360],
                  "Porte d'entrée de la plaie.", "#f7e2b5", "#8a5a00"),
                S("muscle", "Muscle ouvert", 3, E(500, 450, 120, 36), [720, 430],
                  "Muscle atteint, sphincter entier.", "#e7c48a", "#8a5a00"),
                S("anus", "Sphincter entier", 4, E(500, 560, 36, 22), [500, 640],
                  "La continence repose encore sur lui.", "#d5e8f5", "#1d4e89"),
            ],
        ),
        N(
            "sphincter",
            "Sphincter atteint",
            "Hors soins de base. Opérateur formé.",
            [
                S("fourchette", "Fourchette", 1, E(500, 380, 220, 100), [500, 250],
                  "Plaie profonde.", "#f3cfc3", "#a1262f"),
                S("peau", "Peau ouverte", 2, E(500, 340, 90, 16), [700, 320],
                  "Ne résume pas la plaie.", "#f7e2b5", "#8a5a00"),
                S("muscle", "Muscle ouvert", 3, E(500, 430, 110, 30), [720, 400],
                  "Le muscle est déjà passé.", "#e7c48a", "#8a5a00"),
                S("anus", "Sphincter ouvert", 4, E(500, 540, 55, 34), [500, 650],
                  "Anneau atteint : opérateur formé.", "#a1262f", "#6e2420"),
            ],
        ),
    ],
}

POSTPART = {
    "id": "lot175-postpart",
    "titre": "Post-partum : utérus ferme, atonie, vessie pleine",
    "sources_courtes": "Schéma pédagogique. Utérus et vessie : conduite au lit, recommandation postnatale de 2021 archivée dans evidence/. Orientation : D = droite de la patiente.",
    "question": {
        "intitule": "Quel niveau montre une vessie qui fausse le fond ?",
        "html": "<p>Le niveau vessie pleine grossit la vessie devant l'utérus. On la vide avant de juger la hauteur du fond. L'atonie est un utérus large et mou, autre dessin.</p>",
    },
    "niveaux": [
        N(
            "ferme",
            "Utérus ferme",
            "Fond rétracté. Vessie petite.",
            [
                S("paroi", "Paroi abdominale", 1, E(500, 400, 300, 200), [500, 180],
                  "On palpe à travers.", "#f6e6dc", "#8a4b3c"),
                S("uterus", "Utérus ferme", 2, E(480, 420, 120, 80), [480, 420],
                  "Globe dur après l'utérotonique.", "#f3cfc3", "#a1262f"),
                S("vessie", "Vessie vide", 3, E(680, 500, 50, 30), [680, 500],
                  "Petite, elle ne pousse pas le fond.", "#d5e8f5", "#1d4e89"),
                S("perinee", "Filière", 4, E(500, 620, 40, 18), [500, 670],
                  "Un sang rouge vif avec un utérus dur vient d'ici.", "#e7d5c4", "#5c564c"),
            ],
            defaut=True,
        ),
        N(
            "atonie",
            "Atonie",
            "Utérus large et mou. Le sang s'accumule.",
            [
                S("paroi", "Paroi abdominale", 1, E(500, 390, 310, 210), [500, 160],
                  "Le fond remonte.", "#f6e6dc", "#8a4b3c"),
                S("uterus", "Utérus mou", 2, E(500, 400, 200, 140), [500, 400],
                  "Ne se rétracte pas. Utérotonique et aide.", "#c4554a", "#6e2420"),
                S("vessie", "Vessie", 3, E(740, 520, 46, 28), [740, 520],
                  "On la vide quand même, pour ne pas se tromper.", "#d5e8f5", "#1d4e89"),
                S("perinee", "Filière", 4, E(500, 640, 40, 18), [500, 690],
                  "On cherche aussi une plaie.", "#e7d5c4", "#5c564c"),
            ],
        ),
        N(
            "vessie",
            "Vessie pleine",
            "La vessie pousse le fond. On la vide d'abord.",
            [
                S("paroi", "Paroi abdominale", 1, E(500, 390, 310, 210), [500, 160],
                  "Douleur sus-pubienne possible.", "#f6e6dc", "#8a4b3c"),
                S("uterus", "Utérus refoulé", 2, E(430, 300, 110, 70), [320, 280],
                  "Paraît haut tant que la vessie est pleine.", "#f3cfc3", "#a1262f"),
                S("vessie", "Vessie pleine", 3, E(620, 480, 130, 80), [760, 430],
                  "À vider avant de conclure.", "#7eb6e0", "#1d4e89"),
                S("perinee", "Filière", 4, E(500, 650, 36, 16), [500, 700],
                  "La miction ne vient pas, ou seulement des gouttes.", "#e7d5c4", "#5c564c"),
            ],
        ),
    ],
}


def main() -> int:
    DEST.mkdir(parents=True, exist_ok=True)
    PAGES.mkdir(parents=True, exist_ok=True)
    code = 0
    for desc, nom in ((TRAVAIL, "travail"), (PERINEE, "perinee"), (POSTPART, "postpart")):
        frag = rendre(desc, POLICE)
        erreurs = [e for e in verifier(frag, desc) if e not in MARQUES_EXEMPLE]
        (DEST / f"{nom}.json").write_text(
            json.dumps(desc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        html = page(frag, desc["titre"], POLICE)
        (PAGES / f"{nom}.html").write_text(html, encoding="utf-8")
        print(nom, len(html.encode("utf-8")), "erreurs", erreurs or "aucune")
        if erreurs:
            code = 1
    return code


if __name__ == "__main__":
    sys.exit(main())
