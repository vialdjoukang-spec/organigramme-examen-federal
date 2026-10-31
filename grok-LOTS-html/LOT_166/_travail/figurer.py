#!/usr/bin/env python3
"""Figures LOT_166. Appelle dessinateur.rendre sans le contrôle codé pour l'exemple aortique."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "grok-LOTS-html/outils/dessinateur"))
import dessinateur  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "figures"
POLICE = "../../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf"
VB = [0, 0, 1000, 720]


def E(cx, cy, rx, ry):
    return {"type": "ellipse", "cx": cx, "cy": cy, "rx": rx, "ry": ry}


def T(d):
    return {"type": "trait", "d": d}


def C(d):
    return {"type": "chemin", "d": d}


def S(sid, nom, num, geom, remplissage, contour, badge, definition, lesion=False, trait=False, ep=2):
    st = {
        "id": sid,
        "nom": nom,
        "numero": num,
        "geometrie": geom,
        "remplissage": remplissage,
        "contour": contour,
        "epaisseur": ep,
        "badge": badge,
        "definition": definition,
    }
    if lesion:
        st["lesion"] = True
    if trait:
        st["trait"] = True
    return st


def niveau(nid, etiquette, note, structures, cliche=None, defaut=False):
    n = {
        "id": nid,
        "etiquette": etiquette,
        "note": note,
        "viewBox": VB,
        "repere": {"texte": "D", "x": 78, "y": 64, "titre": "Repère D : côté droit du patient, à gauche de l'écran"},
        "structures": structures,
    }
    if cliche:
        n["cliche"] = cliche
    if defaut:
        n["defaut"] = True
    return n


Q_MORISON = {
    "intitule": "Pourquoi une bande noire entre le foie et le rein n'est pas toujours du sang ?",
    "html": (
        "<p>L'espace de Morison est le récessus hépato-rénal. Vide, il ne sépare pas le foie du rein par une bande anéchogène. "
        "Une bande noire, déclive, qui s'ouvre quand le patient est en décubitus, est un liquide libre.</p>"
        "<p>Le sang frais est souvent anéchogène au début : l'image ne dit pas s'il s'agit d'ascite, de bile, d'urine ou de sang. "
        "Le contexte (trauma, cirrhose, hypotension) et la ponction tranchent. Les cloisons et le plancton orientent vers un liquide riche, pas vers un transsudat simple.</p>"
        "<p>Le cliché source (James Heilman, 2014 sur Wikimedia) montre un fin liseré au pôle supérieur du rein droit. "
        "Le schéma n'est pas un calque de ces pixels : la superposition sert seulement à comparer l'emplacement.</p>"
    ),
}

Q_PLEURAL = {
    "intitule": "Où s'arrête la colonne quand il n'y a pas de liquide ?",
    "html": (
        "<p>Sans épanchement, l'air du poumon arrête les ultrasons au diaphragme : la colonne thoracique ne se voit pas au-dessus du diaphragme. "
        "Avec un liquide, le faisceau traverse l'épanchement et la colonne continue au-dessus du diaphragme. C'est le signe de la colonne, ou spine sign.</p>"
        "<p>Une étude prospective de trauma (European Journal of Trauma and Emergency Surgery, 2021) a mesuré l'extension de ce signe pour l'hémothorax, "
        "contre le scanner : sensibilité 78,7 %, spécificité 92,6 %.<sup class=\"s\">7</sup> Le signe affirme surtout l'absence de liquide quand il manque (valeur prédictive négative 97,8 % dans cette série).</p>"
        "<p>Le volume approximatif de Balik, chez le ventilé, est vingt fois la séparation maximale en millimètres. "
        "Ce n'est pas une mesure au millilitre près : l'erreur moyenne publiée avoisine 158 ml, et l'hémothorax comme l'empyème étaient exclus de la dérivation.</p>"
    ),
}

Q_PERI = {
    "intitule": "Un liseré noir autour du cœur est-il une tamponnade ?",
    "html": (
        "<p>Non. L'épanchement est le liquide. La tamponnade est la compression des cavités, un diagnostic clinique aidé par l'échographie. "
        "L'ESC 2015 classe la lame en fin de diastole : inférieure à 10 mm, de 10 à 20 mm, ou supérieure à 20 mm. L'ESC 2025 garde le seuil de 20 mm pour la lame large.</p>"
        "<p>Les signes de compression sont le collapsus auriculaire droit, le collapsus diastolique du ventricule droit, "
        "une veine cave inférieure dilatée qui se collabe peu, et une variation respiratoire des flux. Aucun de ces signes, seul, ne remplace la pression artérielle et les jugulaires.</p>"
        "<p>Le cliché source est un secteur 2D d'épanchement (AMC Echolab, CardioNetworks, CC BY-SA 3.0). "
        "Ce n'est pas le calque de la coupe sous-xiphoïdienne dessinée.</p>"
    ),
}


def morison():
    paroi = lambda: S("paroi", "Paroi abdominale", 1, E(500, 370, 430, 280), "#f3d2c4", "#e0b5a4", [150, 150],
                      "Coupe longitudinale de l'hypocondre droit. Le bord supérieur est la peau.")
    foie = lambda: S("foie", "Foie", 2, E(360, 390, 200, 160), "#c45b4a", "#8d2f28", [300, 340],
                      "Parenchyme hépatique homogène, en avant du rein.")
    rein = lambda: S("rein", "Rein droit", 3, E(680, 500, 130, 90), "#d7b08a", "#8a5a32", [700, 480],
                      "Sinus hyperéchogène au centre, cortex autour. Pôle supérieur vers le foie.")
    dia = S("diaphragme", "Diaphragme", 4, T("M180,250 C360,210 620,210 840,260"), "#f4f7f8", "#f7f1dc", [500, 200],
            "Ligne hyperéchogène courbe. Au-dessus, le thorax.", trait=True, ep=8)
    vide = S("morison", "Espace de Morison", 5, E(530, 430, 36, 14), "#c47a62", "#6e2c24", [530, 400],
             "Récessus hépato-rénal virtuel : pas de bande anéchogène entre le foie et le rein.")
    fin = S("liquide", "Liseré liquidien", 5, E(530, 440, 70, 18), "#0b1c24", "#9fd4e8", [530, 400],
            "Bande anéchogène déclive entre le foie et le rein. Liquide libre, nature non précisée par l'image.", lesion=True)
    large = S("liquide", "Épanchement abondant", 5, E(540, 450, 120, 48), "#071820", "#b7e6f5", [540, 400],
              "Large collection anéchogène de l'espace de Morison. Le rein flotte à distance du foie.", lesion=True)
    return {
        "id": "f-morison",
        "titre": "Hypocondre droit : espace de Morison",
        "question": Q_MORISON,
        "sources_courtes": (
            "Schéma pédagogique. Cliché source : James Heilman, MD, "
            "<a href=\"https://commons.wikimedia.org/wiki/File:FluidMorisonsPouchEctop.PNG\">FluidMorisonsPouchEctop</a>, "
            "Wikimedia Commons, CC BY-SA 3.0, consulté le 31 octobre 2026. "
            "Le niveau « liseré » peut superposer ce cliché ; ce n'est pas une segmentation. "
            "Repère D à gauche de l'écran. Police Atkinson Hyperlegible, SIL OFL."
        ),
        "niveaux": [
            niveau("vide", "Morison vide", "Pas de bande noire entre le foie et le rein.",
                   [paroi(), foie(), rein(), dia, vide], defaut=True),
            niveau("fin", "Liseré", "Fin liseré anéchogène. Le cliché source montre ce type de liseré.",
                   [paroi(), foie(), rein(), dia, fin], cliche="cliche-morison.png"),
            niveau("large", "Épanchement", "Collection large. L'image ne distingue pas le sang de l'ascite.",
                   [paroi(), foie(), rein(), dia, large]),
        ],
    }


def pleural():
    paroi = S("paroi", "Paroi thoracique", 1, E(500, 360, 430, 290), "#f3d2c4", "#e0b5a4", [160, 140],
              "Coupe de la base, ligne axillaire postérieure. La peau est en haut du schéma.")
    poumon = lambda y=250: S("poumon", "Poumon", 2, E(520, y, 180, 90), "#b7e3d8", "#0f6e62", [560, y - 20],
                              "Air : artefacts, glissement. Il masque la colonne quand il descend jusqu'au diaphragme.")
    foie = S("foie", "Foie sous le diaphragme", 3, E(480, 560, 220, 90), "#c45b4a", "#8d2f28", [400, 580],
             "Sous le diaphragme, à droite. Sert de fenêtre acoustique.")
    dia = S("diaphragme", "Diaphragme", 4, T("M200,470 C400,430 640,430 820,480"), "#f4f7f8", "#f4edd4", [700, 430],
            "Coupole hyperéchogène. Repère entre le thorax et l'abdomen.", trait=True, ep=8)
    spine_court = S("colonne", "Colonne arrêtée", 5, T("M250,700 L250,500"), "#f4f7f8", "#f7f7f2", [230, 600],
                    "La ligne vertébrale s'arrête au diaphragme : pas de liquide pour la prolonger.", trait=True, ep=10)
    spine_long = S("colonne", "Signe de la colonne", 5, T("M250,700 L250,300"), "#f4f7f8", "#fff6c2", [220, 340],
                   "La colonne se voit au-dessus du diaphragme parce que le liquide conduit les ultrasons.", lesion=True, trait=True, ep=10)
    liquide = S("liquide", "Épanchement pleural", 6, E(430, 400, 150, 55), "#071820", "#9fd4e8", [480, 380],
                "Zone anéchogène au-dessus du diaphragme, déclive. C'est l'épanchement.", lesion=True)
    cloison = S("cloison", "Cloisons", 6, T("M340,360 L520,430 M400,340 L560,450"), "#f4f7f8", "#f3e27a", [520, 360],
                "Septa fibrinoux. Ils évoquent un exsudat, un hémothorax ou un empyème, pas un transsudat libre.", lesion=True, trait=True, ep=4)
    plancton = S("plancton", "Signe du plancton", 7, E(400, 410, 40, 16), "#d9e27a", "#8a8a20", [360, 450],
                 "Particules échogènes mobiles dans le liquide. Le résumé consulté de 2018 ne donne pas de sensibilité.", lesion=True)
    return {
        "id": "f-pleural",
        "titre": "Base pulmonaire : signe de la colonne",
        "question": Q_PLEURAL,
        "sources_courtes": (
            "Schéma pédagogique. Cliché source : "
            "<a href=\"https://commons.wikimedia.org/wiki/File:Pleural_effusion_2.jpg\">Pleural effusion 2</a>, "
            "Wikimedia Commons, CC BY-SA 4.0, consulté le 31 octobre 2026. "
            "L'en-tête nominatif du fichier d'origine a été recadré avant dépôt. "
            "La superposition n'est pas un calque. Repère D à gauche de l'écran."
        ),
        "niveaux": [
            niveau("sec", "Sans liquide", "La colonne s'arrête au diaphragme.",
                   [paroi, poumon(300), foie, dia, spine_court], defaut=True),
            niveau("epanchement", "Spine sign", "Liquide anéchogène et colonne prolongée au-dessus du diaphragme.",
                   [paroi, poumon(240), foie, dia, spine_long, liquide], cliche="cliche-pleural.jpg"),
            niveau("cloisonne", "Cloisons", "Septa et particules. Le pus et le sang peuvent donner cette image.",
                   [paroi, poumon(230), foie, dia, spine_long, cloison, plancton]),
        ],
    }


def peri():
    foie = S("foie", "Foie", 1, E(500, 180, 280, 80), "#c45b4a", "#8d2f28", [280, 150],
             "En coupe sous-xiphoïdienne, le foie est la fenêtre proche de la sonde.")
    vd = S("vd", "Ventricule droit", 2, E(430, 400, 90, 70), "#8d3b3b", "#4a1515", [400, 370],
           "Cavité antérieure. Elle se collabe en diastole quand la pression péricardique monte.")
    vg = S("vg", "Ventricule gauche", 3, E(590, 420, 100, 75), "#a34a4a", "#4a1515", [620, 400],
           "Cavité postérieure et gauche sur cette orientation schématique.")
    od = S("od", "Oreillette droite", 4, E(400, 520, 70, 48), "#b86a6a", "#4a1515", [360, 530],
           "Paroi fine. Le collapsus systolique de l'oreillette droite est un signe de compression.")
    og = S("og", "Oreillette gauche", 5, E(600, 530, 68, 46), "#b86a6a", "#4a1515", [640, 540],
           "Oreillette gauche, en arrière.")
    sec = S("peri", "Péricarde virtuel", 6, E(510, 450, 210, 160), "#5c2a2a", "#e8d3c4", [760, 300],
            "Sac normal : quelques millilitres, pas de liseré noir circulant.")
    lame = S("lame", "Épanchement péricardique", 6, C("M300,360 C300,250 720,250 720,400 C720,560 300,580 300,450 Z M380,400 C390,330 650,330 650,430 C650,520 400,530 380,450 Z"),
             "#071820", "#9fd4e8", [250, 420],
             "Liseré anéchogène autour du cœur, mesuré en fin de diastole. Ce n'est pas encore une tamponnade.", lesion=True)
    collapse = S("collapsus", "Collapsus de l'oreillette droite", 7, E(390, 500, 28, 16), "#f6e27a", "#8a6a10", [300, 520],
                 "Paroi auriculaire droite qui s'affaisse. Signe échographique de compression, à lire avec la clinique.", lesion=True)
    return {
        "id": "f-peri",
        "titre": "Coupe sous-xiphoïdienne du péricarde",
        "question": Q_PERI,
        "sources_courtes": (
            "Schéma pédagogique d'une coupe sous-xiphoïdienne. Cliché source : AMC Echolab, CardioNetworks, "
            "<a href=\"https://commons.wikimedia.org/wiki/File:Pericardial_effusion_E00676_(CardioNetworks_ECHOpedia).jpg\">E00676</a>, "
            "Wikimedia Commons, CC BY-SA 3.0, consulté le 31 octobre 2026. "
            "Le secteur 2D a été extrait du fichier ; ce n'est pas le calque du schéma. Repère D à gauche de l'écran."
        ),
        "niveaux": [
            niveau("sec", "Sans lame", "Quatre cavités, pas de liseré circulant.",
                   [foie, vd, vg, od, og, sec], defaut=True),
            niveau("lame", "Épanchement", "Liseré anéchogène. La taille ne décide pas seule de la ponction.",
                   [foie, vd, vg, od, og, lame], cliche="cliche-peri.jpg"),
            niveau("tampon", "Compression", "Le collapsus auriculaire droit s'ajoute à la lame.",
                   [foie, vd, vg, od, og, lame, collapse]),
        ],
    }


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for desc in (morison(), pleural(), peri()):
        frag = dessinateur.rendre(desc, POLICE)
        html = dessinateur.page(frag, desc["titre"], POLICE)
        path = OUT / f"{desc['id']}.htm"
        path.write_text(html, encoding="utf-8")
        print(path.name, len(html.encode()))


if __name__ == "__main__":
    main()
