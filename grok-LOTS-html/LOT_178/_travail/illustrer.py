#!/usr/bin/env python3
"""Schémas interactifs LOT_178. Les pages HTML restent hors dépôt (script)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, "grok-LOTS-html/outils")
from dessinateur.dessinateur import page, rendre, verifier

DEST = Path("grok-LOTS-html/LOT_178/illustrations")
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


def Q(intitule, html):
    return {"intitule": intitule, "html": html}


PORTES = {
    "id": "lot178-portes",
    "titre": "Quatre portes d'un problème d'accouchement",
    "sources_courtes": "Schéma pédagogique. Tracé : consensus 2015. Sang : ligne d'août 2022. Dilatation : recommandations 2018. Épaules : ligne de mars 2012.",
    "question": Q(
        "Quelle porte passe avant les autres ?",
        "<p>Celle du danger immédiat. Un tracé pathologique ou un saignement ne attend pas la fin d'un protocole lent. On mesure le sang. On ne pousse pas sur le fond utérin.</p>",
    ),
    "niveaux": [
        N("sang", "Saignement", "Mesurer, puis utérotonique, quatre causes ensemble.", [
            S("uterus", "Utérus", 1, E(500, 390, 230, 160), [340, 280],
              "Le tonus se palpe. Mou : atonie possible.", "#f3cfc3", "#a1262f"),
            S("placenta", "Placenta", 2, E(620, 360, 70, 46), [760, 300],
              "Incomplet : cause tissulaire.", "#c9b6d6", "#5b3a73"),
            S("perinee", "Périnée", 3, E(500, 590, 80, 36), [500, 640],
              "Déchirure possible même si l'utérus est mou.", "#f7e2b5", "#8a5a00"),
            S("sang", "Sang mesuré", 4, E(280, 480, 60, 40), [180, 480],
              "Le regard sous-estime. On pèse.", "#f6b7b7", "#a1262f"),
        ], defaut=True),
        N("trace", "Tracé", "Trois classes. On ne dit pas normal s'il manque un critère.", [
            S("normal", "Classe normale", 1, E(280, 360, 90, 60), [280, 280],
              "110 à 160, bande 5 à 25, pas de décélérations répétitives.", "#b7e3d8", "#0f6e62"),
            S("suspect", "Classe suspecte", 2, E(520, 360, 90, 60), [520, 280],
              "Un critère normal manque, sans critère pathologique.", "#f7e2b5", "#8a5a00"),
            S("patho", "Classe pathologique", 3, E(760, 360, 90, 60), [760, 280],
              "Agir. Faire naître si cela ne cède pas.", "#a1262f", "#5c1020"),
        ]),
        N("mecanique", "Blocage", "Épaule, cordon ou siège : le geste change.", [
            S("symphyse", "Symphyse", 1, E(500, 250, 120, 36), [500, 180],
              "L'épaule antérieure peut y buter.", "#e7d5c4", "#5c564c"),
            S("epaule", "Épaule", 2, E(420, 400, 70, 48), [300, 400],
              "Tête née, traction douce échouée : hanches fléchies d'abord.", "#f7e2b5", "#8a5a00"),
            S("cordon", "Cordon", 3, E(640, 460, 50, 30), [760, 460],
              "Devant la présentation : relever, ne pas repousser.", "#d5e8f5", "#1d4e89"),
        ]),
    ],
}

PERINEE = {
    "id": "lot178-perinee",
    "titre": "Degrés d'une déchirure périnéale",
    "sources_courtes": "Schéma pédagogique. Classification lue dans la ligne de juin 2015. En cas de doute, classer plus haut.",
    "question": Q(
        "Quel degré atteint le sphincter ?",
        "<p>Le degré 3. Le 3a déchire moins de la moitié de l'épaisseur du sphincter externe, le 3b plus de la moitié, le 3c ajoute le sphincter interne. Le degré 4 ajoute la muqueuse anorectale. Ligne de juin 2015.</p>",
    ),
    "niveaux": [
        N("degre2", "Degré 2", "Muscle atteint. Sphincter entier.", [
            S("peau", "Peau", 1, E(500, 300, 200, 40), [500, 220],
              "Degré 1 si seule la peau ou la muqueuse vaginale est atteinte.", "#f3cfc3", "#a1262f"),
            S("muscle", "Muscle", 2, E(500, 400, 180, 50), [300, 400],
              "Degré 2 : muscles, pas le sphincter.", "#f7e2b5", "#8a5a00"),
            S("sphincter", "Sphincter entier", 3, E(500, 510, 120, 36), [700, 510],
              "Encore fermé. Le toucher rectal le vérifie.", "#b7e3d8", "#0f6e62"),
            S("muqueuse", "Muqueuse", 4, E(500, 600, 70, 24), [500, 660],
              "Fermée. Un degré 4 l'ouvrirait.", "#e7d5c4", "#5c564c"),
        ], defaut=True),
        N("degre3", "Degré 3", "Le complexe sphinctérien est atteint.", [
            S("peau", "Peau", 1, E(500, 280, 200, 36), [500, 200],
              "Ouverte avec le muscle.", "#f3cfc3", "#a1262f"),
            S("muscle", "Muscle", 2, E(500, 380, 170, 46), [300, 380],
              "Dépassé. On ne s'arrête pas au degré 2.", "#f7e2b5", "#8a5a00"),
            S("sphincter", "Sphincter atteint", 3, E(500, 500, 130, 40), [720, 500],
              "3a, 3b ou 3c. Le doute classe plus haut.", "#a1262f", "#5c1020"),
            S("muqueuse", "Muqueuse fermée", 4, E(500, 610, 70, 22), [500, 670],
              "Encore fermée : ce n'est pas un degré 4.", "#e7d5c4", "#5c564c"),
        ]),
        N("degre4", "Degré 4", "Sphincters et muqueuse anorectale.", [
            S("peau", "Peau", 1, E(500, 270, 200, 34), [500, 190],
              "Large ouverture.", "#f3cfc3", "#a1262f"),
            S("muscle", "Muscle", 2, E(500, 370, 160, 42), [300, 370],
              "Réparé après le sphincter, au bloc.", "#f7e2b5", "#8a5a00"),
            S("sphincter", "Deux sphincters", 3, E(500, 490, 140, 42), [730, 480],
              "Externe et interne. Pas de point en huit.", "#a1262f", "#5c1020"),
            S("muqueuse", "Muqueuse ouverte", 4, E(500, 610, 80, 28), [500, 680],
              "Degré 4. Nouveau toucher rectal après le fil.", "#5c1020", "#2a0810"),
        ]),
    ],
}

EPAULES = {
    "id": "lot178-epaules",
    "titre": "Dystocie des épaules : trois gestes, fond interdit",
    "sources_courtes": "Schéma pédagogique. Définition et manœuvres : ligne de mars 2012. Ordre et bras postérieur : mise à jour de 2026.",
    "question": Q(
        "Quel geste est interdit ?",
        "<p>La pression sur le fond utérin. On fléchit d'abord les hanches, cuisses sur l'abdomen, puis la pression sus-pubienne du côté du dos, vers le bas et le côté. Le bras postérieur vient si l'extérieur échoue.</p>",
    ),
    "niveaux": [
        N("hanches", "Hanches fléchies", "Premier geste. Cuisses sur l'abdomen.", [
            S("symphyse", "Symphyse", 1, E(500, 250, 140, 36), [500, 170],
              "L'épaule antérieure y est bloquée.", "#e7d5c4", "#5c564c"),
            S("epaule", "Épaule antérieure", 2, E(460, 360, 70, 46), [300, 360],
              "Elle doit glisser sous la symphyse.", "#f7e2b5", "#8a5a00"),
            S("cuisses", "Cuisses fléchies", 3, E(500, 560, 180, 50), [760, 560],
              "Hanches fléchies, cuisses sur l'abdomen.", "#b7e3d8", "#0f6e62"),
        ], defaut=True),
        N("pubis", "Pression sus-pubienne", "Côté du dos fœtal, vers le bas et le côté.", [
            S("symphyse", "Symphyse", 1, E(500, 250, 140, 36), [500, 170],
              "La pression est au-dessus, pas sur le fond.", "#e7d5c4", "#5c564c"),
            S("dos", "Dos fœtal", 2, E(400, 400, 80, 50), [260, 400],
              "La pression part de ce côté.", "#f7e2b5", "#8a5a00"),
            S("pression", "Pression", 3, E(560, 300, 46, 30), [700, 300],
              "Vers le bas et le côté. Jamais le fond.", "#a1262f", "#5c1020"),
        ]),
        N("bras", "Bras postérieur", "Si les gestes externes échouent.", [
            S("symphyse", "Symphyse", 1, E(500, 240, 130, 32), [500, 160],
              "On ne reste pas sur un geste déjà inutile.", "#e7d5c4", "#5c564c"),
            S("bras", "Bras postérieur", 2, E(620, 430, 70, 40), [780, 430],
              "La main entre. Sinon seulement, on coupe.", "#d5e8f5", "#1d4e89"),
            S("fond", "Fond interdit", 3, E(500, 600, 90, 36), [500, 680],
              "Aucune pression sur le fond.", "#a1262f", "#5c1020"),
        ]),
    ],
}

CORDON = {
    "id": "lot178-cordon",
    "titre": "Procidence du cordon : relever, ne pas repousser",
    "sources_courtes": "Schéma pédagogique. Décélération prolongée : consensus 2015. Arrêt de l'oxytocine : information 22114. Pas de volume vésical archivé.",
    "question": Q(
        "Que fait la main ?",
        "<p>Elle relève la présentation. Elle ne repousse pas le cordon. La posture, genu-pectorale ou Trendelenburg, ne remplace pas la naissance. Aucun volume vésical n'est écrit.</p>",
    ),
    "niveaux": [
        N("devant", "Cordon devant", "Le cordon est devant la présentation.", [
            S("tete", "Présentation", 1, E(500, 420, 90, 70), [320, 420],
              "Elle comprime le cordon si elle descend.", "#f7e2b5", "#8a5a00"),
            S("cordon", "Cordon", 2, E(500, 560, 36, 70), [680, 560],
              "Devant, ou dans le vagin. On ne le repousse pas.", "#d5e8f5", "#1d4e89"),
            S("col", "Col", 3, E(500, 650, 70, 28), [500, 710],
              "La main reste pour relever.", "#e7d5c4", "#5c564c"),
        ], defaut=True),
        N("relever", "Main qui relève", "Les doigts restent jusqu'à la naissance.", [
            S("tete", "Présentation relevée", 1, E(500, 340, 90, 64), [300, 340],
              "On la soulève, on ne l'enfonce pas.", "#f7e2b5", "#8a5a00"),
            S("main", "Main", 2, E(500, 500, 70, 40), [720, 500],
              "Elle ne part pas écrire un bilan.", "#f3cfc3", "#a1262f"),
            S("cordon", "Cordon libre", 3, E(640, 430, 40, 24), [800, 400],
              "Moins comprimé. La naissance se prépare.", "#d5e8f5", "#1d4e89"),
        ]),
        N("naissance", "Naissance préparée", "Oxytocine arrêtée. Voie la plus rapide.", [
            S("tete", "Présentation", 1, E(500, 360, 86, 60), [320, 360],
              "La main qui relève est encore là.", "#f7e2b5", "#8a5a00"),
            S("arret", "Oxytocine arrêtée", 2, E(280, 520, 90, 40), [280, 600],
              "Arrêt dès la souffrance, information 22114.", "#a1262f", "#5c1020"),
            S("voie", "Naissance", 3, E(720, 520, 90, 40), [720, 600],
              "La posture ne suffit pas.", "#b7e3d8", "#0f6e62"),
        ]),
    ],
}


def main() -> int:
    DEST.mkdir(parents=True, exist_ok=True)
    code = 0
    for desc in (PORTES, PERINEE, EPAULES, CORDON):
        nom = desc["id"].split("-", 1)[1]
        frag = rendre(desc, POLICE)
        erreurs = [e for e in verifier(frag, desc) if e not in MARQUES_EXEMPLE]
        (DEST / f"{nom}.json").write_text(
            json.dumps(desc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        html = page(frag, desc["titre"], POLICE)
        tmp = Path("/tmp/lot178-dessins")
        tmp.mkdir(parents=True, exist_ok=True)
        (tmp / f"{nom}.html").write_text(html, encoding="utf-8")
        print(nom, "erreurs", erreurs or "aucune")
        if erreurs:
            code = 1
    return code


if __name__ == "__main__":
    sys.exit(main())
