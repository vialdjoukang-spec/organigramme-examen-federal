#!/usr/bin/env python3
"""Trois schémas interactifs LOT_174 via dessinateur.rendre().

Le vérificateur d'exemple exige les chaînes « faux chenal », 2014, 2020,
2022 et Radiopaedia, propres au dessin aortique de LOT_150. On contrôle
la géométrie et la structure, puis on écarte seulement ces cinq marques.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, "grok-LOTS-html/outils")
from dessinateur.dessinateur import page, rendre, verifier

DEST = Path("grok-LOTS-html/LOT_174/illustrations")
POLICE = "../../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf"
MARQUES_EXEMPLE = (
    "question absente",
    "source manquante dans la question : 2014",
    "source manquante dans la question : 2020",
    "source manquante dans la question : 2022",
    "source manquante dans la question : Radiopaedia",
)
VB = [0, 0, 1000, 760]
REP = {"texte": "D", "x": 48, "y": 56, "titre": "Droite du patient, à gauche de l'écran"}


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


UTERUS = {
    "id": "lot174-uterus",
    "titre": "Utérus gravide : poche fermée, membranes rompues, petit fœtus",
    "sources_courtes": "Schéma pédagogique. Rupture avant 37 semaines : OMS, glossaire 2022, et fiche prématurité du 10 mai 2023, archivées dans evidence/. Orientation : D = droite du patient.",
    "question": {
        "intitule": "Quel niveau montre une poche des eaux ouverte ?",
        "html": "<p>Le niveau membranes rompues retire le contour fermé de la poche. Une rupture avant 37 semaines et 0 jour est une rupture prématurée des membranes avant terme. Le liquide se teste, il ne se devine pas.</p>",
    },
    "niveaux": [
        N(
            "intact",
            "Membranes intactes",
            "Poche fermée. Le poids et la semaine se lisent ensemble.",
            [
                S("paroi", "Paroi utérine", 1, E(500, 390, 250, 180), [500, 230],
                  "Muscle utérin autour de la cavité.", "#f3cfc3", "#a1262f"),
                S("poche", "Poche des eaux", 2, E(500, 390, 160, 110), [620, 340],
                  "Liquide limité par les membranes.", "#d5e8f5", "#1d4e89"),
                S("foetus", "Fœtus", 3, E(470, 400, 70, 48), [470, 400],
                  "Le poids seul ne donne pas la semaine.", "#f7e2b5", "#8a5a00"),
                S("col", "Col", 4, E(500, 600, 36, 22), [500, 600],
                  "Un col fermé ne prouve pas que le terme est sûr.", "#e7d5c4", "#5c564c"),
            ],
            defaut=True,
        ),
        N(
            "rompu",
            "Membranes rompues",
            "Brèche amniotique. Écoulement à tester.",
            [
                S("paroi", "Paroi utérine", 1, E(500, 390, 250, 180), [500, 230],
                  "La paroi reste quand le liquide part.", "#f3cfc3", "#a1262f"),
                S("breche", "Brèche amniotique", 2, E(640, 300, 34, 22), [640, 300],
                  "Écoulement clair : le tester.", "#9fd0ea", "#1d4e89"),
                S("foetus", "Fœtus", 3, E(470, 410, 70, 48), [470, 410],
                  "Moins de liquide, moins de protection.", "#f7e2b5", "#8a5a00"),
                S("col", "Col", 4, E(500, 610, 40, 24), [500, 610],
                  "Col ouvert et liquide : accouchement à évaluer.", "#e7d5c4", "#5c564c"),
            ],
        ),
        N(
            "petit",
            "Petit fœtus",
            "Cavité large autour d'un petit fœtus. Le Doppler tranche.",
            [
                S("paroi", "Paroi utérine", 1, E(500, 390, 250, 180), [500, 230],
                  "La cavité peut paraître grande.", "#f3cfc3", "#a1262f"),
                S("poche", "Poche des eaux", 2, E(500, 380, 170, 120), [630, 330],
                  "Liquide conservé ou diminué selon la cause.", "#d5e8f5", "#1d4e89"),
                S("foetus", "Petit fœtus", 3, E(440, 420, 40, 28), [440, 420],
                  "Petit pour l'âge ou petit constitutionnel.", "#f7e2b5", "#8a5a00"),
                S("placenta", "Placenta", 4, E(680, 450, 48, 32), [680, 450],
                  "Placenta petit ou mal perfusé : penser au retard.", "#c9b6d6", "#5b3a73"),
            ],
        ),
    ],
}

DOPPLER = {
    "id": "lot174-doppler",
    "titre": "Trois territoires Doppler du retard de croissance",
    "sources_courtes": "Schéma pédagogique. Consensus de Gordijn 2016 sur le retard de croissance, archivé dans evidence/. Orientation : D = droite du patient.",
    "question": {
        "intitule": "Quel vaisseau se lit en premier devant un petit fœtus ?",
        "html": "<p>L'artère ombilicale se lit avec la biométrie. Avant 32 semaines, un flux télédiastolique absent est un critère solitaire de retard de croissance dans le consensus de Gordijn 2016. Le ductus veineux dessiné ici est un repère de gravité ; son seuil chiffré n'est pas dans ce consensus relu.</p>",
    },
    "niveaux": [
        N(
            "normal",
            "Flux présents",
            "Trois flux dessinés, diastole ombilicale présente.",
            [
                S("omb", "Artère ombilicale", 1, E(280, 400, 78, 48), [280, 400],
                  "Flux présent en diastole.", "#f6b7b7", "#a1262f"),
                S("acm", "Artère cérébrale", 2, E(520, 250, 64, 40), [520, 250],
                  "Flux cérébral sans redistribution.", "#f7e2b5", "#8a5a00"),
                S("dv", "Ductus veineux", 3, E(680, 470, 52, 34), [680, 470],
                  "Onde veineuse présente.", "#b7e3d8", "#0f6e62"),
            ],
            defaut=True,
        ),
        N(
            "absent",
            "Diastole absente",
            "Flux télédiastolique ombilical absent : critère solitaire précoce, Gordijn 2016.",
            [
                S("omb", "Artère ombilicale", 1, E(280, 400, 78, 48), [280, 400],
                  "Flux télédiastolique absent, critère solitaire avant 32 semaines.", "#a1262f", "#5c1020"),
                S("acm", "Artère cérébrale", 2, E(520, 250, 64, 40), [520, 250],
                  "Peut augmenter si le cerveau est privilégié.", "#f7e2b5", "#8a5a00"),
                S("dv", "Ductus veineux", 3, E(680, 470, 52, 34), [680, 470],
                  "À relire si l'ombilicale est pathologique.", "#b7e3d8", "#0f6e62"),
            ],
        ),
        N(
            "veine",
            "Onde veineuse anormale",
            "Repère veineux. Le seuil du ductus n'est pas dans le consensus relu.",
            [
                S("omb", "Artère ombilicale", 1, E(280, 400, 78, 48), [280, 400],
                  "Souvent déjà anormale à ce stade.", "#a1262f", "#5c1020"),
                S("acm", "Artère cérébrale", 2, E(520, 250, 64, 40), [520, 250],
                  "Redistribution possible, non suffisante seule.", "#f7e2b5", "#8a5a00"),
                S("dv", "Ductus veineux", 3, E(680, 470, 52, 34), [680, 470],
                  "Repère veineux, seuil non repris du consensus relu.", "#0f6e62", "#083830"),
            ],
        ),
    ],
}

POUMON = {
    "id": "lot174-poumon",
    "titre": "Poumon du prématuré : alvéole ouverte ou fermée",
    "sources_courtes": "Schéma pédagogique. Poractant alfa, information professionnelle suisse 51886, archivée dans evidence/. Dose initiale lue : 100 à 200 mg/kg dans la trachée.",
    "question": {
        "intitule": "Quelle alvéole reçoit le surfactant exogène ?",
        "html": "<p>L'alvéole fermée par manque de surfactant. Le poractant alfa se donne dans la trachée. La dose initiale lue est 100 à 200 mg par kilogramme. La dose maximale lue est 300 à 400 mg par kilogramme.</p>",
    },
    "niveaux": [
        N(
            "ouvert",
            "Alvéole ouverte",
            "Air en place, surfactant présent.",
            [
                S("cage", "Cage thoracique", 1, E(500, 400, 280, 190), [320, 300],
                  "Paroi du thorax du nouveau-né.", "#f3cfc3", "#a1262f"),
                S("bronche", "Bronche", 2, E(500, 250, 90, 26), [500, 250],
                  "Voie de l'air et du surfactant.", "#d5e8f5", "#1d4e89"),
                S("alveole", "Alvéole ouverte", 3, E(400, 440, 78, 56), [400, 440],
                  "Paroi fine, air en place.", "#b7e3d8", "#0f6e62"),
                S("capillaire", "Capillaire", 4, E(640, 470, 48, 28), [640, 470],
                  "Échange gazeux si l'alvéole est ouverte.", "#f6b7b7", "#a1262f"),
            ],
            defaut=True,
        ),
        N(
            "ferme",
            "Alvéole fermée",
            "Manque de surfactant : atélectasie et détresse.",
            [
                S("cage", "Cage thoracique", 1, E(500, 400, 280, 190), [320, 300],
                  "Tirage et geignement si les alvéoles se ferment.", "#f3cfc3", "#a1262f"),
                S("bronche", "Bronche", 2, E(500, 250, 90, 26), [500, 250],
                  "Porte d'entrée du surfactant.", "#d5e8f5", "#1d4e89"),
                S("alveole", "Alvéole fermée", 3, E(400, 460, 34, 22), [400, 460],
                  "Collapsus par manque de surfactant.", "#8a5a00", "#3d2800"),
                S("capillaire", "Capillaire", 4, E(640, 470, 48, 28), [640, 470],
                  "Moins d'échange tant que l'alvéole est collabée.", "#f6b7b7", "#a1262f"),
            ],
        ),
        N(
            "traitement",
            "Après surfactant",
            "Réouverture après poractant alfa, 100 à 200 mg/kg.",
            [
                S("cage", "Cage thoracique", 1, E(500, 400, 280, 190), [320, 300],
                  "La paroi ne change pas.", "#f3cfc3", "#a1262f"),
                S("bronche", "Bronche", 2, E(500, 250, 90, 26), [500, 250],
                  "Instillation trachéale.", "#d5e8f5", "#1d4e89"),
                S("alveole", "Alvéole rouverte", 3, E(400, 440, 68, 48), [400, 440],
                  "Réouverture après 100 à 200 mg/kg.", "#b7e3d8", "#0f6e62"),
                S("capillaire", "Capillaire", 4, E(640, 470, 48, 28), [640, 470],
                  "L'échange reprend si la ventilation suit.", "#f6b7b7", "#a1262f"),
            ],
        ),
    ],
}


def main() -> int:
    DEST.mkdir(parents=True, exist_ok=True)
    code = 0
    for desc, nom in ((UTERUS, "uterus"), (DOPPLER, "doppler"), (POUMON, "poumon")):
        frag = rendre(desc, POLICE)
        erreurs = [e for e in verifier(frag, desc) if e not in MARQUES_EXEMPLE]
        (DEST / f"{nom}.json").write_text(json.dumps(desc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        html = page(frag, desc["titre"], POLICE)
        (DEST / f"{nom}.html").write_text(html, encoding="utf-8")
        print(nom, len(html.encode("utf-8")), "erreurs", erreurs or "aucune")
        if erreurs:
            code = 1
    return code


if __name__ == "__main__":
    sys.exit(main())
