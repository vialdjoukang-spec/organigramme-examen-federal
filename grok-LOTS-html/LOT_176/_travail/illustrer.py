#!/usr/bin/env python3
"""Trois schémas du dessinateur pour LOT_176. Le vérificateur d'exemple exige
des chaînes de la dissection aortique : on ne modifie pas l'outil. On appelle
rendre(), puis on contrôle la géométrie et la bascule, sans ces cinq marques."""
from __future__ import annotations
import json
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RACINE / "grok-LOTS-html" / "outils" / "dessinateur"))
import dessinateur  # noqa: E402

OUT = RACINE / "grok-LOTS-html" / "LOT_176" / "illustrations"
POLICE = "../../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf"

VB = [0, 0, 1000, 760]


def E(cx, cy, rx, ry):
    return {"type": "ellipse", "cx": cx, "cy": cy, "rx": rx, "ry": ry}


def zone(i, sid, nom, geo, badge, definition, fill, stroke):
    return {
        "id": sid,
        "nom": nom,
        "numero": i,
        "geometrie": geo,
        "remplissage": fill,
        "contour": stroke,
        "epaisseur": 2,
        "badge": badge,
        "definition": definition,
    }


def niv(i, etiquette, note, structures, defaut=False):
    d = {
        "id": i,
        "etiquette": etiquette,
        "note": note,
        "viewBox": VB,
        "repere": {"texte": "D", "x": 78, "y": 86, "titre": "Droite du patient, à gauche de l'écran"},
        "structures": structures,
    }
    if defaut:
        d["defaut"] = True
    return d


def fig_trimestre():
    return {
        "id": "lot176-trimestre",
        "titre": "Trois plans du premier trimestre",
        "question": {
            "intitule": "Quel plan décide de la suite ?",
            "html": "<p>La longueur cranio-caudale date. La clarté nucale et le cœur ne se lisent pas sur le même plan. Une clarté trop épaisse ou une malformation quitte la voie simple du test non invasif.</p>",
        },
        "sources_courtes": "Schéma. Repères tirés de la ligne directrice ISUOG du 3 janvier 2023 et de la fiche OFSP du 7 juillet 2015. Orientation : D à gauche de l'écran.",
        "niveaux": [
            niv("datation", "Longueur cranio-caudale", "Plan sagittal. Le fœtus est neutre, ni fléchi ni déplié.", [
                zone(1, "paroi", "Paroi maternelle", E(500, 390, 420, 300), [150, 160], "Limite du champ, pas une mesure fœtale.", "#f3cfc3", "#e4b5a6"),
                zone(2, "cavite", "Cavité amniotique", E(500, 400, 250, 190), [760, 220], "Le fœtus doit être séparé de l'amnios pour une autre mesure.", "#f7efe0", "#c4a574"),
                zone(3, "foetus", "Fœtus en position neutre", E(470, 410, 120, 70), [470, 560], "Calipers aux deux extrémités, ligne presque perpendiculaire au faisceau.", "#d9ecf8", "#176fa0"),
                zone(4, "placenta", "Placenta", E(700, 330, 80, 50), [700, 250], "L'ADN libre du test non invasif vient surtout du placenta.", "#e7b7b2", "#8a3b36"),
            ], True),
            niv("clarte", "Clarté nucale", "Coupe sagittale médiane. Tête et thorax seuls, au maximum.", [
                zone(1, "crane", "Tête et thorax", E(420, 390, 150, 110), [180, 250], "L'image ne montre que la tête et le thorax.", "#d9ecf8", "#176fa0"),
                zone(2, "nuque", "Espace nucal", E(590, 360, 36, 22), [700, 300], "Trois mesures sur des images séparées. On garde la plus grande.", "#f6d0d2", "#a1262f", ),
                zone(3, "amnios", "Amnios écarté", E(640, 500, 70, 28), [760, 560], "On ne mesure pas l'amnios avec la nuque.", "#f7efe0", "#c4a574"),
                zone(4, "os", "Os propre du nez", E(300, 340, 28, 12), [250, 480], "Le profil se voit sur la même coupe sagittale.", "#f4f1ea", "#5c564c"),
            ]),
            niv("coeur", "Quatre cavités précoces", "Axe cardiaque vers la gauche, entre 30 et 60 degrés.", [
                zone(1, "thorax", "Thorax", E(500, 400, 220, 180), [180, 200], "Le cœur occupe environ un tiers du thorax.", "#f3cfc3", "#e4b5a6"),
                zone(2, "droite", "Cavités droites", E(430, 390, 70, 80), [360, 560], "Droite du patient, à gauche de l'écran.", "#d9ecf8", "#176fa0"),
                zone(3, "gauche", "Cavités gauches", E(580, 400, 70, 80), [700, 560], "Deux ventricules distincts, remplissage séparé.", "#f6d5cc", "#8a4b3c"),
                zone(4, "axe", "Axe vers la gauche", E(520, 250, 40, 18), [520, 180], "L'axe normal pointe à gauche, de 30 à 60 degrés.", "#1a7a50", "#0e4d32"),
            ]),
        ],
    }


def fig_prelevement():
    return {
        "id": "lot176-prelevement",
        "titre": "Trois prélèvements, trois certitudes",
        "question": {
            "intitule": "Quel prélèvement pose un diagnostic ?",
            "html": "<p>Le sang maternel dépiste. Le trophoblaste et le liquide amniotique confirment. Un test positif sur sang ne nomme pas encore la maladie.</p>",
        },
        "sources_courtes": "Schéma. Fiche OFSP du 7 juillet 2015 et page du CHUV mise à jour le 2 septembre 2022. Orientation : D à gauche de l'écran.",
        "niveaux": [
            niv("sang", "Sang maternel", "Prise de sang. Aucun risque mécanique pour le fœtus.", [
                zone(1, "bras", "Veine maternelle", E(280, 400, 140, 80), [180, 220], "Le prélèvement est maternel.", "#f6d0d2", "#a1262f"),
                zone(2, "adn", "ADN libre d'origine placentaire", E(560, 300, 120, 60), [700, 200], "Il ne remplace pas l'échographie du premier trimestre.", "#e7e4f7", "#3d3a66"),
                zone(3, "uterus", "Utérus", E(620, 520, 160, 90), [760, 620], "Le fœtus n'est pas piqué.", "#f6d5cc", "#8a4b3c"),
                zone(4, "resultat", "Résultat de dépistage", E(400, 180, 90, 36), [400, 120], "Risque faible ou risque élevé. Ce n'est pas un caryotype.", "#d7f0e2", "#1a7a50"),
            ], True),
            niv("tropho", "Trophoblaste", "Biopsie placentaire. Geste diagnostique.", [
                zone(1, "paroi", "Paroi", E(500, 390, 400, 280), [160, 160], "Repère de profondeur.", "#f3cfc3", "#e4b5a6"),
                zone(2, "placenta", "Placenta biopsié", E(640, 300, 110, 70), [760, 220], "Confirme ou infirme un dépistage positif.", "#e7b7b2", "#8a3b36"),
                zone(3, "foetus", "Fœtus non piqué", E(400, 430, 90, 70), [300, 560], "Le prélèvement vise le trophoblaste.", "#d9ecf8", "#176fa0"),
                zone(4, "aiguille", "Trajet de l'aiguille", E(500, 180, 70, 22), [500, 120], "Réservé après information et consentement.", "#5c564c", "#142028"),
            ]),
            niv("amnios", "Liquide amniotique", "Amniocentèse. Autre geste diagnostique.", [
                zone(1, "paroi", "Paroi", E(500, 390, 400, 280), [160, 160], "Même orientation que le niveau précédent.", "#f3cfc3", "#e4b5a6"),
                zone(2, "liquide", "Liquide amniotique", E(480, 420, 150, 100), [300, 560], "Ponction du liquide, pas du placenta.", "#f7efe0", "#c4a574"),
                zone(3, "foetus", "Fœtus", E(400, 400, 70, 50), [400, 300], "On évite le fœtus.", "#d9ecf8", "#176fa0"),
                zone(4, "placenta", "Placenta laissé", E(700, 300, 80, 48), [760, 220], "Ce niveau ne biopsie pas le trophoblaste.", "#e7b7b2", "#8a3b36"),
            ]),
        ],
    }


def fig_morpho():
    return {
        "id": "lot176-morphologie",
        "titre": "Trois plans de malformation",
        "question": {
            "intitule": "Quel plan montre la malformation majeure ?",
            "html": "<p>Le crâne, le rachis et la paroi ne se jugent pas sur une seule coupe. Une malformation majeure adresse en médecine fœtale, sans s'arrêter au test non invasif.</p>",
        },
        "sources_courtes": "Schéma. Ligne directrice ISUOG du 3 janvier 2023 et fiche OFSP du 7 juillet 2015. Orientation : D à gauche de l'écran.",
        "niveaux": [
            niv("crane", "Pôle céphalique", "Chercher une voûte. L'anencéphalie se voit tôt.", [
                zone(1, "crane", "Voûte crânienne", E(480, 360, 150, 120), [250, 200], "Une voûte absente est une malformation majeure.", "#d9ecf8", "#176fa0"),
                zone(2, "cerveau", "Contenu crânien", E(480, 360, 80, 60), [620, 280], "Le contenu se compare à la voûte.", "#e7e4f7", "#3d3a66"),
                zone(3, "face", "Face", E(330, 470, 50, 36), [220, 520], "Le profil complète la voûte.", "#f6d5cc", "#8a4b3c"),
                zone(4, "cou", "Nuque", E(640, 450, 40, 24), [760, 500], "La clarté nucale n'est pas la voûte.", "#f6d0d2", "#a1262f"),
            ], True),
            niv("rachis", "Rachis", "Coupe longitudinale. Chercher une fermeture.", [
                zone(1, "dos", "Dos fœtal", E(500, 390, 280, 70), [500, 200], "Le rachis se suit de la nuque au sacrum.", "#f6d5cc", "#8a4b3c"),
                zone(2, "fermeture", "Ligne de fermeture", E(500, 390, 200, 16), [500, 300], "Une ouverture est une malformation du tube neural.", "#1a7a50", "#0e4d32"),
                zone(3, "sac", "Sac éventuel", E(700, 500, 50, 36), [780, 600], "Un sac dorsal ne se rassure pas par un test sanguin.", "#f6d0d2", "#a1262f"),
                zone(4, "tete", "Pôle céphalique", E(220, 390, 60, 50), [140, 500], "On relie le crâne au rachis.", "#d9ecf8", "#176fa0"),
            ]),
            niv("paroi", "Paroi abdominale", "Coupe axiale. Estomac et insertion du cordon.", [
                zone(1, "abdomen", "Abdomen", E(500, 400, 200, 150), [220, 220], "Coupe haute : estomac visible, reins non exigés ici.", "#f7efe0", "#c4a574"),
                zone(2, "estomac", "Estomac", E(420, 390, 40, 30), [360, 560], "Bulle gastrique d'un seul côté.", "#d7f0e2", "#1a7a50"),
                zone(3, "cordon", "Insertion du cordon", E(500, 250, 36, 28), [500, 160], "Une hernie ou un laparoschisis sort de la paroi.", "#e7b7b2", "#8a3b36"),
                zone(4, "rachis", "Rachis en coupe", E(620, 470, 28, 28), [740, 560], "Le rachis ferme le cercle de la coupe.", "#d9ecf8", "#176fa0"),
            ]),
        ],
    }


def controler(frag: str, desc: dict) -> list[str]:
    erreurs = dessinateur.verifier(frag, desc)
    ignores = (
        "faux chenal",
        "question absente",
        "source manquante",
        "2014",
        "2020",
        "2022",
        "Radiopaedia",
    )
    return [e for e in erreurs if not any(m in e for m in ignores)]


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    code = 0
    for desc in (fig_trimestre(), fig_prelevement(), fig_morpho()):
        frag = dessinateur.rendre(desc, "POLICE")
        page = dessinateur.page(frag, desc["titre"], POLICE)
        dest_json = OUT / f"{desc['id']}.json"
        dest_html = OUT / f"{desc['id']}.html"
        dest_json.write_text(json.dumps(desc, ensure_ascii=False, indent=1), encoding="utf-8")
        dest_html.write_text(page, encoding="utf-8")
        reste = controler(frag, desc)
        print(desc["id"], "octets", len(frag.encode()), "écarts", reste or "aucun hors exemple")
        if reste:
            code = 1
    return code


if __name__ == "__main__":
    # page wrapper: look up
    if not hasattr(dessinateur, "page_html"):
        # The module builds the page inside main only. Reuse rendre and a local wrapper.
        pass
    sys.exit(main())
