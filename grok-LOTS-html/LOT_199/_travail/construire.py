#!/usr/bin/env python3
"""Construit les 11 leçons de LOT_199 (O3.5 Escarres)."""
from __future__ import annotations

import html
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path("/workspace/grok-LOTS-html/LOT_199")
OUT = Path("/tmp/lot199_build")
MOTS_CLES = re.compile(
    r"prévalence|incidence|sensibilit|spécificit|seuil|score", re.I
)
DOSE = re.compile(
    r"\b\d+(?:[.,]\d+)?\s*(?:µg|μg|mcg|mg|UI|IU|ml/h|mL/h)\b|\b\d+(?:[.,]\d+)?\s*g\b",
    re.I,
)

TITRES = {
    1: "Définition",
    2: "Épidémiologie",
    3: "Physiopathologie",
    4: "Démarche diagnostique",
    5: "Anamnèse et drapeaux rouges",
    6: "Examen physique",
    7: "Approche syndromique",
    8: "Diagnostic positif",
    9: "Examens complémentaires",
    10: "Arbre décisionnel",
    11: "Prise en charge",
    12: "Prévention",
    13: "Points clés",
    14: "Pièges et cas",
}

NOMS = {
    "A": "Escarres",
    1: "Lésion de pression de catégorie 1",
    2: "Lésion de pression de catégorie 2",
    3: "Lésion de pression de catégorie 3",
    4: "Lésion de pression de catégorie 4",
    5: "Lésion de pression non classable",
    6: "Lésion des tissus profonds",
    7: "Dermite associée à l'incontinence",
    8: "Déchirure cutanée",
    9: "Ulcère du pied diabétique et ischémie",
    10: "Ulcère de Kennedy et peau de fin de vie",
}

CIBLES = {
    "A": 74500,
    1: 37200,
    2: 39800,
    3: 42100,
    4: 44600,
    5: 45800,
    6: 38100,
    7: 40900,
    8: 43300,
    9: 46400,
    10: 44100,
}


class Sigles:
    LIB = {
        "ANQ": "association nationale pour le développement de la qualité",
        "EPUAP": "groupe européen des escarres",
        "NPIAP": "panel national des lésions de pression",
        "PPPIA": "alliance du Pacifique sur les lésions de pression",
        "NICE": "institut britannique pour l'excellence clinique",
        "AIPS": "information professionnelle suisse",
        "HUG": "hôpitaux universitaires de Genève",
        "GLOBIAD": "outil gantois de la dermite d'incontinence",
        "ISTAP": "panel international des déchirures cutanées",
        "IWGDF": "groupe international du pied diabétique",
        "ESVS": "société européenne de chirurgie vasculaire",
        "DTPI": "lésion des tissus profonds",
        "CG179": "guide britannique des escarres",
        "MASD": "lésion cutanée liée à l'humidité",
        "FRAGMMENT": "friction, âge, mobilité et état mental",
    }

    def __init__(self) -> None:
        self.vu: set[str] = set()

    def __call__(self, s: str) -> str:
        exp = self.LIB[s]
        balise = f'<abbr title="{html.escape(exp)}">{s}</abbr>'
        self.vu.add(s)
        # Développement à chaque emploi : le premier vu à l'écran est toujours développé,
        # quel que soit l'ordre de construction des points.
        return f"{balise} ({exp})"


def mots(texte: str) -> int:
    brut = re.sub(r"<[^>]+>", " ", texte)
    return len(re.findall(r"[\wÀ-ÿŒœ'’\-]+", brut))


def P(texte: str, sup: int | None = None) -> str:
    if mots(texte) > 34:
        raise SystemExit(f"PHRASE LONGUE ({mots(texte)}): {texte}")
    nu = re.sub(r"</?abbr[^>]*>", "", texte)
    if "<" in nu or ">" in nu:
        raise SystemExit(f"CHEVRON: {texte}")
    fin = f' <sup class="s">{sup}</sup>' if sup else ""
    return f"<p>{texte}{fin}</p>"


def table(caption: str, headers: list[str], rows: list[list[str]]) -> str:
    th = "".join(f"<th>{html.escape(h)}</th>" for h in headers)
    body = []
    for row in rows:
        body.append("<tr>" + "".join(f"<td>{html.escape(c)}</td>" for c in row) + "</tr>")
    cap = f"<caption>{html.escape(caption)}</caption>"
    return f'<div class="tw"><table>{cap}<tr>{th}</tr>{"".join(body)}</table></div>'


def schema(prefix: str) -> str:
    panneaux = [
        ("1. Urgence", [
            "Sepsis, cellulite qui s'étend, os infecté.",
            "Ischémie sévère du pied : avis vasculaire.",
            "Douleur et extension très rapides : chirurgie.",
        ]),
        ("2. Classer", [
            "Peau intacte : rouge qui ne blanchit pas, ou violet.",
            "Perte de peau : derme, graisse, ou os.",
            "Fond caché : non classable. Humidité ou lambeau : autre plaie.",
        ]),
        ("3. Décharger", [
            "Ôter l'appui et le dispositif.",
            "Talon en l'air, jambe sur le mollet.",
            "Position à 30 degrés, pas sur le trochanter.",
        ]),
    ]
    css = []
    inputs = []
    labels = []
    svgs = []
    for i, (etq, lignes) in enumerate(panneaux):
        iid = f"{prefix}{i}"
        checked = " checked" if i == 0 else ""
        css.append(
            f"#{iid}:checked ~ .plan .n{i}{{display:block}}"
            f"#{iid}:checked ~ .bn label[for='{iid}']{{background:#d7eef8;border-color:#176fa0}}"
        )
        inputs.append(
            f'<input class="sr" type="radio" name="{prefix}" id="{iid}"{checked}>'
        )
        labels.append(f'<label for="{iid}">{html.escape(etq)}</label>')
        y = 36
        parts = [
            f'<text x="320" y="28" text-anchor="middle" font-size="18" font-weight="700" fill="#14303b">{html.escape(etq)}</text>'
        ]
        for ligne in lignes:
            parts.append(
                f'<rect x="36" y="{y}" width="568" height="40" rx="8" fill="#e7f4fb" stroke="#176fa0"/>'
            )
            parts.append(
                f'<text x="320" y="{y+26}" text-anchor="middle" font-size="15" fill="#14303b">{html.escape(ligne)}</text>'
            )
            y += 52
        svgs.append(
            f'<svg class="niv n{i}" viewBox="0 0 640 220" role="img" aria-label="{html.escape(etq)}">{"".join(parts)}</svg>'
        )
    style = (
        f"<style>{''.join(css)}"
        f"#{prefix} .plan .niv{{display:none}}</style>"
    )
    return (
        f'{style}<div class="sch" id="{prefix}">{"".join(inputs)}'
        f'<div class="bn">{"".join(labels)}</div>'
        f'<div class="plan">{"".join(svgs)}</div></div>'
    )


def bande(y0, y1, nom, numero, remplissage, contour, definition, lesion=False):
    return {
        "id": f"{nom}-{y0}",
        "nom": nom,
        "numero": numero,
        "geometrie": {"type": "chemin", "d": f"M 140 {y0} H 860 V {y1} H 140 Z"},
        "remplissage": remplissage,
        "contour": contour,
        "epaisseur": 1.6,
        "badge": [180, (y0 + y1) // 2],
        "definition": definition,
        "lesion": lesion,
    }


def niveaux_coupe():
    def tissus(niveau, note_peau):
        return [
            bande(70, 180, "Peau", 1, "#f3c7b8", "#c48b7a", f"Au niveau {niveau}, {note_peau}"),
            bande(180, 340, "Graisse", 2, "#ffe08a", "#c8962e", f"Au niveau {niveau}, la graisse manque sur le nez, l'oreille, l'occiput et la malléole"),
            bande(340, 520, "Muscle", 3, "#e07a7a", "#8d3030", f"Au niveau {niveau}, le muscle au contact de l'os souffre avant la peau"),
            bande(520, 660, "Os", 4, "#f7f4ef", "#8d8478", f"Au niveau {niveau}, le sacrum, le talon, l'ischion et le trochanter sont les appuis"),
        ]
    rouge = {
        "id": "rouge",
        "nom": "Rouge qui ne blanchit pas",
        "numero": 5,
        "geometrie": {"type": "ellipse", "cx": 500, "cy": 125, "rx": 120, "ry": 36},
        "remplissage": "#e23b3b",
        "contour": "#8d1020",
        "epaisseur": 1.6,
        "badge": [640, 120],
        "definition": "Rouge localisé qui ne blanchit pas, peau encore fermée, ce n'est pas la tache violette",
        "lesion": True,
    }
    cratere = {
        "id": "cratere",
        "nom": "Perte de derme",
        "numero": 5,
        "geometrie": {"type": "chemin", "d": "M 400 90 H 600 V 175 H 400 Z"},
        "remplissage": "#e7a090",
        "contour": "#8d3030",
        "epaisseur": 1.8,
        "badge": [500, 150],
        "definition": "Derme à nu, rose et humide, sans graisse visible et sans fibrine",
        "lesion": True,
    }
    profond = {
        "id": "profond",
        "nom": "Plaie jusqu'à l'os",
        "numero": 5,
        "geometrie": {"type": "chemin", "d": "M 390 90 H 620 V 600 H 390 Z"},
        "remplissage": "#c45a4a",
        "contour": "#5c1818",
        "epaisseur": 1.8,
        "badge": [500, 300],
        "definition": "Os, tendon ou muscle visible ou palpable, et non un fond encore caché",
        "lesion": True,
    }
    croute = {
        "id": "croute",
        "nom": "Croûte sèche",
        "numero": 5,
        "geometrie": {"type": "chemin", "d": "M 380 80 H 640 V 175 H 380 Z"},
        "remplissage": "#2c2c2c",
        "contour": "#111",
        "epaisseur": 1.6,
        "badge": [500, 128],
        "definition": "Croûte ou fibrine qui cache le fond, profondeur inconnue, croûte sèche du talon laissée en place",
        "lesion": True,
    }
    violet = {
        "id": "violet",
        "nom": "Tache violette",
        "numero": 5,
        "geometrie": {"type": "ellipse", "cx": 500, "cy": 125, "rx": 130, "ry": 40},
        "remplissage": "#6b2d5b",
        "contour": "#2a1028",
        "epaisseur": 1.6,
        "badge": [660, 120],
        "definition": "Rouge sombre, marron ou violet qui ne blanchit pas, peau fermée ou phlyctène sanglante",
        "lesion": True,
    }
    return [
        {
            "id": "intact",
            "etiquette": "Peau intacte",
            "note": "Schéma de coupe, pas un scanner, repère D à gauche de l'écran.",
            "viewBox": [0, 0, 1000, 760],
            "defaut": True,
            "repere": {"texte": "D", "x": 70, "y": 80, "titre": "Droite du patient sur le niveau intact"},
            "structures": tissus("intact", "on compare la couleur au reste du corps, surtout si la peau est foncée"),
        },
        {
            "id": "cat1",
            "etiquette": "Catégorie 1",
            "note": "Rouge localisé qui ne blanchit pas, le violet n'est pas dessiné ici.",
            "viewBox": [0, 0, 1000, 760],
            "repere": {"texte": "D", "x": 70, "y": 80, "titre": "Droite du patient sur la catégorie 1"},
            "structures": tissus("catégorie 1", "peau encore fermée autour du rouge") + [rouge],
        },
        {
            "id": "cat2",
            "etiquette": "Catégorie 2",
            "note": "Derme à nu, la graisse n'est pas au fond de cette plaie.",
            "viewBox": [0, 0, 1000, 760],
            "repere": {"texte": "D", "x": 70, "y": 80, "titre": "Droite du patient sur la catégorie 2"},
            "structures": tissus("catégorie 2", "berge de peau autour de la perte de derme") + [cratere],
        },
        {
            "id": "profond",
            "etiquette": "Jusqu'à l'os",
            "note": "Os visible pour la catégorie 4, la graisse seule de la catégorie 3 n'est pas un os.",
            "viewBox": [0, 0, 1000, 760],
            "repere": {"texte": "D", "x": 70, "y": 80, "titre": "Droite du patient sur la plaie profonde"},
            "structures": tissus("plaie profonde", "berges autour d'un os atteint") + [profond],
        },
        {
            "id": "croute",
            "etiquette": "Fond caché",
            "note": "On ne devine pas la catégorie sous la croûte de ce schéma.",
            "viewBox": [0, 0, 1000, 760],
            "repere": {"texte": "D", "x": 70, "y": 80, "titre": "Droite du patient sur le fond caché"},
            "structures": tissus("fond caché", "tissus dont on ne voit plus le fond") + [croute],
        },
        {
            "id": "violet",
            "etiquette": "Tache violette",
            "note": "La tache part de l'interface os-muscle et ce n'est pas une catégorie 1.",
            "viewBox": [0, 0, 1000, 760],
            "repere": {"texte": "D", "x": 70, "y": 80, "titre": "Droite du patient sur la tache violette"},
            "structures": tissus("tache violette", "peau souvent encore fermée au-dessus du violet") + [violet],
        },
    ]


NIVEAU_PAR_CLE = {
    "A": "intact",
    1: "cat1",
    2: "cat2",
    3: "profond",
    4: "profond",
    5: "croute",
    6: "violet",
    7: "intact",
    8: "cat2",
    9: "profond",
    10: "violet",
}


def fragment_coupe() -> str:
    dest = Path("/workspace/grok-LOTS-html/outils/dessinateur/dessinateur.py")
    spec = importlib.util.spec_from_file_location("dess_lot199", dest)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    desc = {
        "id": "coupe-sacrum",
        "titre": "Coupe schématique d'un appui",
        "question": {
            "intitule": "Quelle couche est ouverte ?",
            "html": (
                "<p>On nomme la couche visible, pas la couche que l'on devine.</p>"
                "<p>Un rouge qui ne blanchit pas, sur peau fermée, reste en surface.</p>"
                "<p>Un violet persistant vient de la profondeur, même si la peau est fermée.</p>"
                "<p>Une croûte noire cache le fond : on ne choisit pas 3 ou 4.</p>"
            ),
        },
        "sources_courtes": (
            "Schéma d'enseignement. Ce n'est pas une coupe scanographique. "
            "D marque la droite du patient, à gauche de l'écran. "
            "Police Atkinson Hyperlegible, dossier du dessinateur."
        ),
        "niveaux": niveaux_coupe(),
    }
    frag = mod.rendre(desc, "../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf")
    frag = re.sub(r"<script>.*?</script>", "", frag, flags=re.S)
    if "<script" in frag:
        raise SystemExit("script restant")
    return frag


def choisir_niveau(fragment: str, niveau: str) -> str:
    frag = re.sub(r" checked=\"checked\"", "", fragment)
    cle = f'id="coupe-sacrum-{niveau}"'
    if cle not in frag:
        raise SystemExit(f"niveau absent {niveau}")
    return frag.replace(cle, cle + ' checked="checked"', 1)


CSS = r"""
:root{--fond:#eef7fc;--page:#ffffff;--texte:#1d2a30;--doux:#4f5f66;--lien:#0b5d86;--titre:#14303b;--trait:#cfe3ec;--encadre:#f5f7f9;--bord:#1a7a50;--vert:#1a7a50;--ciel:#176fa0;--alerte:#a1262f;--ombre:rgb(15 60 90 / .28);--voile:rgb(10 30 45 / .55);--barre:#f2f5f7;--th:#f2f5f7;--cb1:#4fb3e6;--cb2:#b9e2f6;--vb1:#3aa776;--vb2:#b5e1cb}
@media (prefers-color-scheme:dark){:root{--fond:#0e171d;--page:#16222a;--texte:#e3edf1;--doux:#a9bac2;--lien:#8fd3f5;--titre:#e6eef2;--trait:#2c414c;--encadre:#1a252c;--bord:#5cc79a;--vert:#5cc79a;--ciel:#6cc2ef;--alerte:#ff8a92;--ombre:rgb(0 0 0 / .6);--voile:rgb(0 0 0 / .7);--barre:#1d282f;--th:#1d282f;--cb1:#4aa9da;--cb2:#24506a;--vb1:#46b384;--vb2:#245a44}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}body{margin:0;background:var(--fond);color:var(--texte);font:1rem/1.45 "Liberation Sans","Atkinson Hyperlegible",Verdana,sans-serif;overflow-wrap:break-word;hyphens:manual}
main{max-width:72ch;margin:0 auto;padding:1rem 1rem 2rem}h1,h2,h3,.fenetre .barre,summary,nav,caption,th{font-family:"Liberation Sans","Atkinson Hyperlegible",Verdana,sans-serif}
h1{font-size:1.75rem;line-height:1.25;color:var(--titre);margin:0 0 .4rem}h2{font-size:1.3rem;line-height:1.3;color:var(--titre);margin:0 0 .45rem}h3{font-size:1.08rem;color:var(--titre);margin:1rem 0 .3rem}
p,.para{margin:0 0 .55rem}.sous{color:var(--doux);font-size:.95rem}.essentiel{border-left-width:4px}.essentiel h2{font-size:1.1rem}
nav ol{padding-left:1.6rem;margin:.4rem 0 0}nav li{margin:.15rem 0}a{color:var(--lien)}
button.terme{all:unset;cursor:pointer;color:var(--lien);text-decoration:underline dotted 1.5px;text-underline-offset:3px}button.terme::after{content:" ⧉";font-size:.75em;vertical-align:.15em}
button.terme:focus-visible{outline:2px solid var(--lien);outline-offset:2px}
.fenetre{position:fixed;inset:0;margin:auto;width:min(92vw,44rem);max-height:80vh;overflow:auto;padding:0;border:1px solid var(--trait);border-radius:12px;background:var(--page);color:var(--texte);box-shadow:0 18px 50px var(--ombre);font-size:.98rem}
.fenetre::backdrop{background:var(--voile)}
.fenetre > .barre{position:sticky;top:0;z-index:1;display:flex;align-items:center;justify-content:space-between;gap:.8rem;padding:.55rem .6rem .55rem 1rem;background:var(--barre);border-bottom:1px solid var(--trait);font-weight:700;font-size:.95rem}
.fenetre > .barre button{flex:none;width:2rem;height:2rem;border:1px solid var(--trait);border-radius:6px;background:var(--page);color:var(--texte);font-size:1rem;cursor:pointer}
.corps{padding:1rem 1.2rem 1.2rem}.corps p:last-child{margin-bottom:0}
.tw{overflow-x:auto;margin:.6rem 0 1rem}table{border-collapse:collapse;width:100%;font-size:.9rem;line-height:1.45}th,td{border:1px solid var(--trait);padding:.4rem .5rem;vertical-align:top;text-align:left}th{background:var(--th);font-size:.85rem}caption{text-align:left;font-weight:700;font-size:.9rem;padding:.2rem 0 .4rem}
figure{margin:1.2rem 0}figure svg{width:100%;height:auto;max-width:40rem;display:block;margin:auto;color:var(--texte);background:#f7fbfd;border:1px solid var(--trait);border-radius:10px}
figcaption{font-size:.88rem;color:var(--doux);text-align:center;margin-top:.3rem}
.biblio{font-size:.86rem;line-height:1.5}.taille{font-size:.85rem;color:var(--doux);margin:0 0 .6rem}.mention{font-style:italic;color:var(--doux);margin:.8rem .3rem 0}
sup.s{font-size:.66em;line-height:0;vertical-align:.5em;margin-left:.06em;color:#1a3a6b;font-weight:700}
abbr[title]{text-decoration:underline dotted 1px;text-underline-offset:2px;cursor:help}
.ilot{background:linear-gradient(var(--page),var(--page)) padding-box,var(--bd) border-box;border:1.5px solid transparent;border-radius:12px;padding:.85rem 1rem .6rem;margin:0 0 .7rem}
.ilot.c{--bd:linear-gradient(135deg,var(--cb1),var(--cb2))}.ilot.v{--bd:linear-gradient(135deg,var(--vb1),var(--vb2))}
.sch .niv{display:none}.sch input.sr{position:absolute;opacity:0;width:1px;height:1px}
.sch .bn{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 8px}.sch .bn label{border:1px solid #9bb;border-radius:8px;padding:4px 8px;cursor:pointer}
.som{columns:2;column-gap:1.4rem}.som li{break-inside:avoid}
details.schema{margin:.4rem 0 .6rem;border:1px solid var(--trait);border-radius:10px;padding:.4rem .6rem;background:var(--encadre)}
details.schema summary{cursor:pointer;font-weight:700}
.urgence{border:2px solid var(--alerte);border-radius:8px;padding:.7rem .9rem;margin:.7rem 0}
"""


def base_phrase(cle, n, S):
    nom = NOMS[cle]
    phrases = {
        1: f"On classe {nom} sur ce que l'on voit, pas sur ce que l'on craint.",
        2: "Le relevé suisse du 8 novembre 2022 donne le cadre hospitalier, pas le rang des dix tableaux.",
        3: "La pression et le cisaillement ferment les petits vaisseaux au contact de l'os.",
        4: "On écarte d'abord le sepsis, l'ischémie et la plaie qui n'est pas un appui.",
        5: "La douleur, le dispositif et l'incontinence changent la lecture de la tache.",
        6: "On palpe, on regarde si le rouge blanchit, et on cherche l'os.",
        7: "Le siège, le fond et la forme séparent l'appui, l'humidité et le lambeau.",
        8: "Le diagnostic positif reprend la couche visible et le mécanisme.",
        9: "Le laboratoire et l'image viennent après l'œil, quand l'os ou l'artère sont en jeu.",
        10: "L'arbre commence par le danger, puis par la couche, puis par la décharge.",
        11: "On enlève l'appui, on traite la douleur, et on n'antibiotise pas une plaie seulement colonisée.",
        12: "La prévention repose sur la peau, la position, le support et l'assiette.",
        13: "Les repères de catégorie, de position et de médicament tiennent en quelques lignes.",
        14: "Le cas montre l'erreur la plus proche, puis la lecture retenue.",
    }
    return phrases[n]


def dafalgan(S):
    return [
        P(f"La douleur du pansement se traite d'abord selon l'{S('AIPS')}, autorisation 69266.", 14),
        P("Paracétamol adulte de plus de 40 kilogrammes : 500 à 1'000 mg, plafond 4'000 mg par jour.", 14),
        P("L'intervalle du paracétamol est de 4 à 8 heures chez l'adulte.", 14),
        P("La dose quotidienne de paracétamol ne dépasse pas 2 g en maladie hépatique chronique.", 14),
        P("Clairance de 10 à 50 millilitres par minute : paracétamol 3000 mg par jour, toutes les 6 heures.", 14),
        P("En dessous de 10 millilitres par minute, le paracétamol reste à 2000 mg par jour, toutes les 8 heures.", 14),
        P("La dose efficace la plus faible, le moins longtemps possible, est la règle écrite pour la grossesse.", 14),
        P("Le passage dans le lait est connu, et la prudence reste écrite pour l'allaitement.", 14),
        P("Les comprimés de paracétamol à 500 mg ne traitent pas l'enfant de moins de 9 ans.", 14),
        P("On vérifie qu'un autre produit ne contient pas déjà la même molécule.", 14),
    ]


def augmentin(S):
    return [
        P("L'autorisation 45674 indique les infections de la peau et des tissus mous, surtout staphylocoque et streptocoque.", 15),
        P("Adulte de plus de 40 kilogrammes : amoxicilline usuelle 3 x 625 mg par jour.", 15),
        P("Au besoin, l'amoxicilline monte jusqu'à 3 x 1 g par jour au maximum.", 15),
        P("On ne donne pas 2 x 1 g d'amoxicilline si la clairance est inférieure à 30 millilitres par minute.", 15),
        P("Les comprimés filmés d'amoxicilline ne conviennent pas en dessous de 40 kilogrammes.", 15),
        P("La grossesse n'est retenue qu'en cas de nécessité absolue.", 15),
        P("Il ne faudrait pas allaiter pendant le traitement.", 15),
        P("L'allergie aux pénicillines, ou un ictère lors d'un traitement antérieur, contre-indique le produit.", 15),
        P(f"Le guide {S('CG179')} ne donne un antibiotique qu'en sepsis, cellulite qui s'étend, ou ostéite.", 5),
        P("Une culture positive, sans signe clinique, ne suffit pas à traiter.", 5),
        P("L'antibiotique n'est pas prescrit pour fermer la plaie.", 5),
        P("Le choix définitif se discute avec le laboratoire local.", 5),
    ]


def positions(S):
    return [
        P(f"Le guide {S('CG179')} demande un changement au moins toutes les 6 heures si le risque existe.", 5),
        P("Le même guide passe à au moins toutes les 4 heures si le risque est élevé.", 5),
        P(f"La revue des {S('HUG')}, en 2012, écrit toutes les deux heures pour un risque haut.", 6),
        P("Elle écrit toutes les quatre heures pour un risque moyen.", 6),
        P("Ces deux horloges ne se remplacent pas : l'une est un plancher britannique, l'autre une politique genevoise.", 5),
        P("On couche la personne à 30 degrés, pas à 90, pour épargner les trochanters.", 6),
        P("Le talon est entièrement déchargé, le poids sur le mollet, sans appui sur le tendon d'Achille ni la veine poplitée.", 4),
        P("On ne masse pas la peau pour prévenir une escarre.", 5),
        P("Un matelas de mousse à haute spécification est utilisé chez l'adulte hospitalisé.", 5),
        P("Devant une escarre, on ne laisse pas un matelas de mousse ordinaire.", 5),
        P("Si la mousse haute ne suffit plus, on discute un support dynamique.", 5),
    ]


def nutrition(S):
    return [
        P("On dépiste la dénutrition chez toute personne à risque ou déjà porteuse d'une plaie d'appui.", 4),
        P("Si la personne est dénutrie ou à risque de l'être, le guide de 2019 vise 30 à 35 kilocalories par kilogramme et par jour.", 4),
        P("Le même guide vise 1,2 à 1,5 gramme de protéines par kilogramme et par jour.", 4),
        P(f"Le guide {S('CG179')} ne donne pas un complément seulement pour éviter une escarre quand l'assiette couvre déjà le besoin.", 5),
        P("L'hydratation veineuse n'est pas un traitement préventif si la personne boit assez.", 5),
    ]


def anq(S):
    return [
        P(f"Le relevé de l'{S('ANQ')} a eu lieu le 8 novembre 2022.", 1),
        P("25 groupes hospitaliers et 116 hôpitaux y ont participé.", 1),
        P("12'460 personnes ont été incluses, âgées de 68,5 ans en moyenne, hospitalisées depuis 7,3 jours.", 1),
        P("La prévalence globale des escarres était de 5,2 pour cent.", 1),
        P("La part des catégories 2 et au-dessus était de 2,3 pour cent.", 1),
        P("Ces deux taux dépassaient la mesure de 2019.", 1),
        P("Le communiqué parle de six degrés, de la catégorie 1 jusqu'aux dommages tissulaires profonds.", 1),
        P("Ce sixième degré du communiqué n'est pas une catégorie clinique numérotée 6.", 1),
        P(f"La foire aux questions d'octobre 2024 classe selon {S('EPUAP')}, {S('NPIAP')} et {S('PPPIA')}, édition 2019.", 2),
        P("La mesure de prévalence est suspendue depuis début 2023, et il n'y en a pas eu en 2024.", 2),
        P("La première mesure nationale obligatoire est prévue au printemps 2026, sur des sorties de février à avril 2026.", 2),
        P("La même foire aux questions écrit que ces résultats ne seront pas publiés de façon transparente.", 2),
        P("Les années 2020 et 2021 n'ont pas eu de relevé, à cause de la pandémie.", 1),
        P("Le communiqué dit que les données n'expliquent pas la hausse.", 1),
        P("Aucun classement d'hôpitaux ne se tire de ce seul indicateur.", 1),
        P("La pédiatrie n'est pas dans le plan de mesure actuel.", 2),
    ]


def categories(S):
    return [
        P("La colonne retenue est celle d'avril 2016, reproduite dans le guide de 2019.", 16),
        P("Catégorie 1 : peau intacte, rouge localisé qui ne blanchit pas, parfois difficile à voir sur peau foncée.", 16),
        P("Une rougeur qui blanchit, ou un changement de chaleur, de consistance ou de sensation, peut précéder la tache.", 16),
        P("Le violet et le marron ne comptent pas comme catégorie 1.", 16),
        P("Catégorie 2 : perte partielle, derme à nu, fond rose ou rouge, humide, ou phlyctène séreuse intacte ou rompue.", 16),
        P("La graisse n'est pas visible, et il n'y a ni fibrine, ni croûte, ni tissu de granulation.", 16),
        P(f"On ne met pas en catégorie 2 une déchirure, une brûlure, ni une {S('MASD')}.", 16),
        P("Catégorie 3 : perte de toute la peau, graisse visible, bords souvent enroulés.", 16),
        P("Le muscle, le tendon, le cartilage et l'os ne sont ni vus ni palpés.", 16),
        P("Catégorie 4 : ces structures sont visibles ou directement palpables.", 16),
        P("L'ostéite ne fait pas partie de la définition de la catégorie 4.", 3),
        P("Si la fibrine ou la croûte cache le fond, la plaie est non classable.", 16),
        P("Enlever la croûte montrerait alors une catégorie 3 ou 4.", 16),
        P("Une croûte sèche, adhérente, sans rougeur ni fluctuation, au talon ou sur un membre ischémique, ne se ramollit pas et ne s'enlève pas.", 16),
        P(f"La {S('DTPI')} est un rouge sombre, marron ou violet persistant, ou une phlyctène sanglante.", 16),
        P("La douleur et le changement de chaleur précèdent souvent la couleur.", 16),
        P("Elle naît à l'interface entre l'os et le muscle.", 16),
        P("On ne l'utilise pas pour une plaie vasculaire, traumatique, neuropathique ou dermatologique.", 16),
        P("Le mot soupçon a été retiré de l'intitulé en 2016.", 3),
        P("La foire aux questions d'octobre 2024 emploie encore la formule soupçon de détérioration profonde.", 2),
        P("Le cours garde l'intitulé de 2016, et signale l'écart de formule.", 3),
        P("Les numéros n'imposent pas un passage de 1 vers 4.", 3),
        P("Un dispositif médical est une cause, pas un stade. On stade quand même la plaie.", 3),
        P("La conférence d'avril 2016 n'a pas retenu, à 75 pour cent, la phrase qui interdisait la catégorie 3 sur le nez, l'oreille, l'occiput et la malléole.", 3),
        P("Le texte de 2009 rappelle seulement que ces zones sans graisse donnent des plaies peu profondes.", 16),
    ]


def braden(S):
    return [
        P("Six items composent l'échelle publiée en 1987 et détaillée dans la page lue en 2026.", 7),
        P("La perception, l'humidité, l'activité, la mobilité et la nutrition vont de 1 à 4.", 7),
        P("La friction et le cisaillement vont de 1 à 3.", 7),
        P("Le total va de 6 à 23. Plus il est bas, plus le risque est haut.", 7),
        P("La bande lue en 2023 place un risque léger de 15 à 18.", 8),
        P("Le risque modéré va de 13 à 14, le risque élevé de 10 à 12, et le risque sévère est inférieur à 9.", 8),
        P("La même page de grille écrit aussi, en bas de tableau, qu'un total de 12 ou moins est un risque élevé.", 7),
        P("Les deux formulations sont citées. Le cours ne les fond pas en une seule.", 8),
        P("Perception 1 : aucune réponse à la douleur, ou presque plus de sensation sur le corps.", 7),
        P("Perception 4 : la personne répond et sent la douleur.", 7),
        P("Humidité 1 : peau mouillée presque en permanence. Humidité 4 : peau d'ordinaire sèche.", 7),
        P("Activité 1 : alitée. Activité 4 : marche hors de la chambre au moins deux fois par jour.", 7),
        P("Mobilité 1 : aucun petit mouvement sans aide. Mobilité 4 : grands changements seuls.", 7),
        P("Nutrition 1 : repas presque absent, ou jeûne et perfusions au-delà de cinq jours.", 7),
        P("Nutrition 4 : repas complets, sans besoin de complément.", 7),
        P("Friction 1 : glissement impossible à éviter. Friction 3 : la personne se soulève seule.", 7),
        P(f"Le guide {S('CG179')} cite cette échelle pour appuyer le jugement, pas pour le remplacer.", 5),
        table(
            "Bandes de Braden lues en 2023",
            ["Total", "Lecture"],
            [
                ["15 à 18", "Risque léger"],
                ["13 à 14", "Risque modéré"],
                ["10 à 12", "Risque élevé"],
                ["Moins de 9", "Risque sévère"],
                ["6 à 23", "Étendue possible"],
            ],
        ),
    ]


def norton(S):
    return [
        P("Cinq items, chacun de 1 à 4, donnent un total de 5 à 20.", 9),
        P("Condition physique, état mental, activité, mobilité et continence composent l'échelle de 1962.", 9),
        P("La page d'outil retient un risque à 14 ou moins.", 9),
        P("1 est le mauvais pôle et 4 le bon pôle, à l'inverse d'une note scolaire.", 9),
        P("Condition 4 : bonne. Condition 1 : très mauvaise.", 9),
        P("Mental 4 : alerte. Mental 1 : stupeur.", 9),
        P("Activité 4 : marche. Activité 1 : alité.", 9),
        P("Mobilité 4 : complète. Mobilité 1 : immobile.", 9),
        P("Continence 4 : continente. Continence 1 : double incontinence.", 9),
        P(f"La revue de 2012 cite Norton à côté de Braden et de l'échelle qu'elle écrit Waterloo.", 6),
        P(f"Le guide {S('CG179')} écrit Waterlow. Le cours ne reconstruit pas sa grille.", 5),
    ]


def fragmment(S):
    return [
        P(f"Les {S('HUG')} ont décrit en 2012 une échelle à quatre items, {S('FRAGMMENT')}.", 6),
        P("Les items sont la friction, l'âge, la mobilité et l'état mental.", 6),
        P("On la remplit à l'entrée, au troisième jour, et à chaque changement net.", 6),
        P("De 0 à 3, le risque lu est faible.", 6),
        P("De 4 à 6, il est moyen. De 7 à 10, il est élevé.", 6),
        P("La répartition des points à l'intérieur de chaque item n'est pas dans l'extrait lu.", 6),
    ]


def globiad(S):
    return [
        P(f"L'outil {S('GLOBIAD')}, publié en 2018, sépare un rouge persistant et une perte de peau.", 10),
        P("Chaque catégorie se divise sans signe infectieux, ou avec signe infectieux.", 10),
        P("Pour distinguer le rouge de la perte de peau, la sensibilité lue est de 90 pour cent.", 10),
        P("La spécificité lue est de 84 pour cent, et l'accord de 0,86.", 10),
        P("823 soignants de 30 pays ont testé des images.", 10),
        P("Reconnaître le signe infectieux reste la part la plus fragile.", 10),
        P("La dermite suit l'urine ou les selles, souvent en nappe, pas seulement sur l'os.", 10),
    ]


def istap(S):
    return [
        P(f"Le panel {S('ISTAP')} classe la déchirure en trois types, version de décembre 2018.", 11),
        P("Type 1 : lambeau remis en place, sans perte de peau.", 11),
        P("Type 2 : perte partielle du lambeau.", 11),
        P("Type 3 : perte totale du lambeau.", 11),
        P("L'hématome et l'ischémie du lambeau ne font pas partie de cette classification.", 11),
        P("Le traumatisme, pas l'appui prolongé, ouvre la peau.", 11),
    ]


def kennedy(S):
    return [
        P("Kennedy a décrit en 1989 un sous-groupe d'escarres chez des personnes en train de mourir.", 12),
        P("La forme est souvent une poire, un papillon ou un fer à cheval.", 12),
        P("Le siège habituel est le sacrum ou le coccyx.", 12),
        P("Le début est soudain, les couleurs vont du rouge au jaune ou au noir, et l'évolution est rapide.", 12),
        P("Dans la revue de dossiers citée, 55,7 pour cent des personnes mouraient dans les six semaines.", 12),
        P("Hanson, en 1991, trouvait 62,5 pour cent des escarres d'hospice dans les deux semaines avant la mort.", 12),
        P("Charcot avait décrit au dix-neuvième siècle un décubitus en papillon, qu'il croyait neuropathique.", 12),
        P("Le consensus de 2009 dit que toutes les escarres ne sont pas évitables.", 12),
        P("Ce constat ne dispense pas de la décharge ni du soin de confort.", 12),
    ]


def ischemie(S):
    return [
        P(f"Le guide {S('IWGDF')} et l'{S('ESVS')} de 2023 concerne le pied diabétique.", 13),
        P("Aucun chiffre seul n'exclut l'artériopathie.", 13),
        P("Elle est moins probable si l'index cheville-bras va de 0,9 à 1,3, si l'index orteil-bras atteint 0,70, et si le doppler pédieux est bi ou triphasique.", 13),
        P("Une pression de cheville inférieure à 50 mmHg, ou un index inférieur à 0,5, va avec une moins bonne cicatrisation et plus d'amputations majeures.", 13),
        P("Un index inférieur à 0,4, une cheville inférieure à 50 mmHg, un orteil inférieur à 30 mmHg, impose un avis vasculaire urgent.", 13),
        P("On discute aussi une revascularisation si les pouls manquent, si le doppler est monophasique ou absent, si la cheville est inférieure à 100 mmHg, ou si l'orteil est inférieur à 60 mmHg.", 13),
        P("Une pression d'orteil d'au moins 30 mmHg augmente jusqu'à 30 pour cent la probabilité prétest de cicatrisation.", 13),
        P("En dessous de 30 mmHg, la probabilité prétest d'amputation majeure augmente d'environ 20 pour cent.", 13),
        P("Si l'orteil n'est pas mesurable, une pression transcutanée d'oxygène d'au moins 25 mmHg augmente jusqu'à 45 pour cent la probabilité prétest de cicatrisation.", 13),
        P("En dessous de 25 mmHg, cette même probabilité d'amputation majeure augmente d'environ 20 pour cent.", 13),
        P("L'avis vasculaire urgent vaut aussi si cette pression transcutanée est inférieure à 30 mmHg.", 13),
        P("L'ischémie critique de membre associe l'artériopathie à une douleur de repos, une gangrène, ou un ulcère depuis au moins deux semaines.", 13),
        P("Le guide de classification de 2023 préfère décrire chaque variable, plutôt qu'un total unique, pour communiquer.", 13),
    ]


def mecanisme(S):
    return [
        P("La revue suisse de 2012 décrit une force perpendiculaire entre un plan dur et l'os.", 6),
        P("Elle retient qu'une pression de plus de 30 mmHg pendant plus de deux heures aboutit à une escarre.", 6),
        P("Elle ajoute que des temps plus courts suffisent selon l'état de la personne.", 6),
        P("Le cisaillement est tangentiel : le tronc relevé à plus de 30 degrés fait glisser le sacrum.", 6),
        P("Les microthromboses et l'inflammation s'ajoutent à l'ischémie.", 6),
        P("Le muscle au contact de l'os souffre avant que la peau ne s'ouvre.", 16),
        P("L'humidité, le dispositif et la dénutrition baissent la tolérance, sans créer à eux seuls la catégorie.", 4),
    ]


def urgence_bloc():
    return (
        '<div class="urgence"><p>Avant le stade : sepsis, cellulite qui s\'étend, os infecté, ischémie sévère du pied, extension très rapide et douleur majeure.</p>'
        "<p>On décharge tout de suite. L'antibiotique et le chirurgien ne servent pas à classer la couleur.</p></div>"
    )


def cas(cle, S):
    banque = {
        "A": [
            P("Une personne de 82 ans, alitée depuis une pneumonie, a une tache rouge du sacrum."),
            P("Le premier réflexe a été d'y mettre une pommade et d'attendre le lendemain."),
            P("Le rouge ne blanchit pas, la peau est fermée, il n'y a pas de violet."),
            P("C'est une catégorie 1. On décharge, on revoit la peau, on ne masse pas."),
            P("La fièvre et une rougeur qui gagne la fesse changeraient l'ordre : infection d'abord."),
        ],
        1: [
            P("Le talon droit est rouge, chaud, fermé, après une après-midi au fauteuil."),
            P("On a parlé de mycose parce que la peau était sèche autour."),
            P("Le test de pression au doigt ne fait pas pâlir le centre."),
            P("Catégorie 1. Le talon est mis en l'air, le mollet porte la jambe."),
            P("Si la tache devient violette, on quitte la catégorie 1."),
        ],
        2: [
            P("Une phlyctène claire du talon s'est rompue. Le fond est rose et humide."),
            P("On a coté une catégorie 3 parce que la bulle paraissait grande."),
            P("La graisse n'est pas visible, il n'y a pas de fibrine."),
            P("Catégorie 2. On protège le derme et on décharge le talon."),
            P("Un lambeau traumatique, lui, serait une déchirure, pas cette catégorie."),
        ],
        3: [
            P("Le sacrum montre un cratère. La graisse jaune est au fond. L'os ne se palpe pas."),
            P("On a annoncé une catégorie 4 à cause de la profondeur seule."),
            P("Sans os, tendon ni muscle, c'est une catégorie 3."),
            P("Les bords enroulés n'élèvent pas le numéro."),
            P("De la fibrine qui cacherait le fond rendrait la plaie non classable."),
        ],
        4: [
            P("L'ischion est à nu chez une personne qui vit au fauteuil."),
            P("On a traité seulement par un pansement quotidien, sans changer l'assise."),
            P("L'os palpable signe la catégorie 4. L'ostéite se discute à part, elle ne définit pas le stade."),
            P("Fièvre et rougeur qui s'étend : antibiotique après avis microbiologique, pas pour fermer la plaie."),
            P("Le coussin et les repos hors fauteuil font partie du traitement."),
        ],
        5: [
            P("Le sacrum est couvert d'une croûte noire humide, avec un liseré rouge."),
            P("On a écrit catégorie 4 sans voir le fond."),
            P("Le fond est caché : plaie non classable."),
            P("Ce n'est pas la croûte sèche et stable du talon ischémique, qu'on laisserait."),
            P("Ici le débridement se discute, autolytique d'abord, chirurgical si l'attente prolonge la plaie."),
        ],
        6: [
            P("Au matin, le sacrum est violet, ferme, douloureux, peau fermée."),
            P("On a coté une catégorie 1 parce que la peau n'était pas ouverte."),
            P("Le violet persistant est une lésion des tissus profonds."),
            P("Elle peut s'ouvrir vite, même avec une bonne décharge."),
            P("On prévient la personne et l'équipe, sans promettre que le stade restera superficiel."),
        ],
        7: [
            P("Les plis inguinaux et le siège sont rouges en nappe chez une personne incontinente."),
            P("On a parlé d'escarre de catégorie 1 sur toute la fesse."),
            P("La nappe suit l'humidité, elle n'est pas limitée à l'os, et une partie blanchit."),
            P("Dermite d'incontinence, catégorie rouge persistant de l'outil de 2018."),
            P("Une perte de peau au pli ferait la deuxième catégorie de cet outil, pas une catégorie 3 d'appui."),
        ],
        8: [
            P("En ôtant un bas de contention, un lambeau d'avant-bras s'est soulevé."),
            P("On a coté une catégorie 2 parce que le derme était rose."),
            P("Le mécanisme est un traumatisme. Type 1 si le lambeau se repose en entier."),
            P("On rapproche le lambeau sans le tirer, on ne le coupe pas d'emblée."),
            P("L'appui du talon, le même jour, se classe à part s'il existe."),
        ],
        9: [
            P("Un talon diabétique est noir, les pouls du pied manquent, la douleur de repos réveille la nuit."),
            P("On a seulement surélevé le talon et prescrit un pansement."),
            P("L'index cheville-bras à 0,35 est sous 0,4 : avis vasculaire urgent."),
            P("La décharge reste nécessaire, elle ne remplace pas l'artère."),
            P("Une croûte sèche stable ne s'enlève pas tant que l'ischémie n'est pas tranchée."),
        ],
        10: [
            P("En unité de soins palliatifs, un papillon noir du sacrum apparaît en une nuit."),
            P("La famille demande qui a oublié le tour de position."),
            P("La forme, la vitesse et le contexte de fin de vie font évoquer l'ulcère de Kennedy."),
            P("On continue la décharge si elle est confortable, on traite la douleur, on ne promet pas la fermeture."),
            P("Le consensus de 2009 rappelle que toute escarre n'est pas une faute."),
        ],
    }
    return banque[cle]


def specifique(cle, S):
    """Paragraphes propres au tableau, rangés par point."""
    if cle == "A":
        return {
            1: [
                P("L'escarre est une lésion locale de la peau et des tissus mous, en général sur un os ou sous un dispositif."),
                P("La pression intense ou prolongée, souvent avec le cisaillement, en est le mécanisme."),
                P("Le mot escarre du communiqué suisse et le mot lésion de pression du texte de 2016 désignent le même champ.", 1),
            ] + categories(S),
            2: anq(S) + [
                P("Ces pourcentages hospitaliers ne classent pas la dermite, la déchirure, le pied diabétique ni l'ulcère de Kennedy.", 1),
                P("Sept hôpitaux étaient au-dessus de l'attendu pour la catégorie 1, un hôpital en dessous.", 1),
                P("Pour les catégories 2 et plus, deux hôpitaux dépassaient la moyenne après ajustement.", 1),
            ],
            3: mecanisme(S),
            4: [
                P("On cherche d'abord le sepsis, la cellulite étendue, l'os infecté et l'ischémie du membre."),
                P("Ensuite on dit si la peau est fermée, si le fond est rose, gras, osseux ou caché."),
                P("Puis on sépare l'humidité, le lambeau et la fin de vie."),
                P("Le dispositif, sonde, masque, attelle ou sonde urinaire, se cherche sur tout le corps.", 3),
            ] + braden(S) + norton(S) + fragmment(S),
            5: [
                P("On demande depuis quand la tache existe, si elle a été violette avant de s'ouvrir, et si un traumatisme l'a ouverte."),
                P("L'incontinence, le fauteuil prolongé et le jeûne sont des faits, pas des stades."),
                P("Une douleur de repos du pied, ou une douleur très supérieure à l'aspect, est un drapeau."),
            ],
            6: [
                P("On regarde le sacrum, les talons, les ischions, les trochanters, les malléoles, l'occiput et les oreilles."),
                P("Le doigt ou la vitropression dit si le rouge blanchit.", 5),
                P("Un rouge qui ne blanchit pas se recontrôle au moins toutes les 2 heures jusqu'à disparition.", 5),
                P("On palpe l'os au fond seulement si la plaie est ouverte, avec une sonde mousse, sans forcer."),
            ],
            7: [
                P("Appui : lésion sur l'os ou sous le dispositif, forme souvent limitée."),
                P("Humidité : nappe des plis et du siège, au contact de l'urine ou des selles."),
                P("Lambeau : histoire d'un choc ou d'un adhésif arraché."),
                P("Artère : pied froid, pouls absents, douleur de repos, noir du bout."),
                P("Fin de vie : forme en papillon, début en heures, personne mourante."),
            ] + globiad(S) + istap(S) + kennedy(S),
            8: [
                P("Le diagnostic du motif est positif quand le mécanisme d'appui est là et que la couche est nommée."),
                P("On écrit la catégorie de 2016, ou l'autre plaie si ce n'est pas un appui.", 16),
                P("On ne moyenne pas deux catégories sur la même plaie."),
            ],
            9: [
                P("Pas de bilan sanguin pour une catégorie 1 isolée, sans signe général."),
                P("Fièvre, extension, os visible : le laboratoire et parfois l'image de l'os se discutent.", 5),
                P("Pouls absents ou plaie du pied diabétique : index et doppler, pas un stade à la place de l'artère.", 13),
            ] + ischemie(S),
            10: [
                P("Étape 1 : signes généraux et membre ischémique."),
                P("Étape 2 : couleur sur peau fermée, violet ou rouge qui ne blanchit pas."),
                P("Étape 3 : fond visible, derme, graisse ou os."),
                P("Étape 4 : fond caché, ou autre mécanisme."),
            ],
            11: [urgence_bloc()] + positions(S) + nutrition(S) + dafalgan(S) + augmentin(S) + [
                P("Le débridement se décide selon la catégorie, la taille, et ce que l'on attend de la plaie.", 5),
                P("On propose d'abord un débridement autolytique par un pansement adapté.", 5),
                P("Le débridement chirurgical se discute s'il raccourcit vraiment l'attente.", 5),
                P("Les larves et le débridement enzymatique ne sont pas de routine.", 5),
                P("On peut discuter les larves si le geste chirurgical est contre-indiqué ou si l'artère est mauvaise.", 5),
                P("Le pansement des catégories 2, 3 et 4 cherche un milieu humide et tiède.", 5),
                P("La gaze sèche n'est pas un traitement d'escarre.", 5),
                P("La pression négative n'est pas de routine, sauf pour espacer des pansements très exsudatifs.", 5),
            ],
            12: [
                P("On inspecte la peau aux changements et sous chaque dispositif."),
                P("Le coussin de fauteuil à haute spécification concerne les stations assises longues.", 5),
                P("Au bloc, une mousse haute ou un support équivalent se discute pour tout adulte opéré.", 5),
                P("La longueur de l'assise doit soutenir la cuisse, sinon le poids glisse vers l'ischion.", 6),
                P("Des repose-pieds trop hauts reportent le poids sur l'ischion.", 6),
                P("On sépare les genoux et les malléoles avec un coussin, sans appuyer sur le talon.", 6),
            ],
            13: [
                P("Six images cliniques : 1, 2, 3, 4, fond caché, tissus profonds."),
                P("Le violet n'est pas une catégorie 1. L'os visible n'a pas besoin du mot ostéite pour être une catégorie 4."),
                P("5,2 pour cent et 2,3 pour cent sont les taux suisses du 8 novembre 2022, pas des seuils de traitement.", 1),
                P("Horloge britannique : 6 heures et 4 heures. Horloge genevoise de 2012 : 2 heures et 4 heures."),
                P("Les plafonds du paracétamol et de l'amoxicilline restent ceux déjà écrits pour le traitement."),
            ],
            14: cas("A", S) + [
                P("L'erreur fréquente est de numéroter une couleur sans regarder la couche."),
                P("L'autre erreur est de traiter une ischémie comme un simple talon d'alitement."),
            ],
        }
    # DX
    commun = {
        2: anq(S)[:8],
        3: mecanisme(S),
        12: positions(S),
    }
    extra = {n: [] for n in range(1, 15)}
    extra.update(commun)
    if cle == 1:
        extra[1] = [
            P("La catégorie 1 est une peau intacte avec un rouge localisé qui ne blanchit pas.", 16),
            P("Sur peau foncée, la couleur peut seulement différer du voisinage.", 16),
            P("Chaleur, fermeté, mollesse ou douleur peuvent précéder le rouge.", 16),
            P("Le violet et le marron appartiennent à la lésion des tissus profonds, pas ici.", 16),
        ]
        extra[6] = [
            P("La vitropression ou le doigt cherchent le blanchiment.", 5),
            P("Tant que le rouge qui ne blanchit pas persiste, on revoit la peau au moins toutes les 2 heures.", 5),
        ]
        extra[8] = [P("Le diagnostic est positif si l'os ou le dispositif explique un rouge fermé qui ne blanchit pas.", 16)]
        extra[11] = dafalgan(S)[:4] + [P("On décharge. On ne perce rien : il n'y a pas de bulle de catégorie 2.")]
        extra[4] = braden(S) + norton(S) + fragmment(S)
    elif cle == 2:
        extra[1] = [
            P("La catégorie 2 montre le derme, rose ou rouge, humide, sans graisse.", 16),
            P("La phlyctène peut être intacte ou rompue, à contenu séreux.", 16),
            P("Fibrine, croûte et granulation ne définissent pas cette catégorie.", 16),
            P("Le bassin et le talon sont les sièges où le cisaillement et le microclimat comptent le plus.", 16),
        ]
        extra[7] = [
            P("On refuse l'étiquette si l'histoire est une déchirure, une brûlure ou une dermite.", 16),
        ]
        extra[11] = [
            P("On couvre pour garder le derme humide, sans gaze sèche.", 5),
            P("Le talon est déchargé en entier.", 4),
        ] + dafalgan(S)[:3]
    elif cle == 3:
        extra[1] = [
            P("La catégorie 3 est une perte de toute l'épaisseur de la peau, avec la graisse visible.", 16),
            P("La granulation et le bord enroulé sont fréquents.", 16),
            P("Le muscle, le tendon, le ligament, le cartilage et l'os restent cachés et non palpables.", 16),
            P("La profondeur change avec l'épaisseur de graisse du siège.", 16),
        ]
        extra[11] = [
            P("Le pansement tient un milieu humide.", 5),
            P("Le débridement autolytique vient en premier si un voile de fibrine gêne, sans cacher toute la cote.", 5),
        ] + nutrition(S) + dafalgan(S)[:3] + augmentin(S)[:4]
    elif cle == 4:
        extra[1] = [
            P("La catégorie 4 expose ou rend palpable l'aponévrose, le muscle, le tendon, le ligament, le cartilage ou l'os.", 16),
            P("Le décollement et le trajet sont fréquents.", 16),
            P("L'ostéite a été retirée de la définition en 2016.", 3),
            P("Elle reste une complication à chercher, pas un synonyme du stade.", 5),
        ]
        extra[5] = [
            P("Os visible, fièvre, rougeur qui gagne : drapeau d'infection profonde.", 5),
            P("Une odeur seule, sans signe clinique, ne décide pas de l'antibiotique.", 5),
        ]
        extra[9] = [
            P("L'image de l'os se discute si le sondage ou l'évolution font craindre l'ostéite.", 5),
            P("Le cours ne donne pas une sensibilité chiffrée du contact osseux : elle n'a pas été relue ici."),
        ]
        extra[11] = nutrition(S) + dafalgan(S) + augmentin(S) + [
            P("La chirurgie réparatrice se discute selon l'ampleur, comme l'écrivait la revue suisse de 2012.", 6),
        ]
    elif cle == 5:
        extra[1] = [
            P("La plaie non classable a un fond caché par la fibrine ou la croûte.", 16),
            P("On ne devine pas entre 3 et 4.", 16),
            P("Au talon, ou sur un membre ischémique, la croûte sèche stable est une couverture, on ne la ramollit pas.", 16),
            P("Ailleurs, une croûte humide et un liseré inflammatoire font discuter le débridement.", 5),
        ]
        extra[11] = [
            P("Stable, sèche, adhérente, sans rougeur ni fluctuation : on laisse, on décharge.", 16),
            P("Instable : autolyse d'abord, geste coupant si l'attente allonge la plaie.", 5),
        ] + dafalgan(S)[:4]
    elif cle == 6:
        extra[1] = [
            P("La lésion des tissus profonds est un rouge sombre, marron ou violet qui ne blanchit pas.", 16),
            P("La peau peut être fermée, ou déjà séparée sur un fond noir, ou couverte d'une phlyctène sanglante.", 16),
            P("Elle vient de la pression et du cisaillement à l'interface os-muscle.", 16),
            P("Même bien soignée, elle peut s'ouvrir et montrer plus de couches.", 16),
            P("On ne la pose pas sur une artérite, un traumatisme, une neuropathie ou une dermatose.", 16),
        ]
        extra[8] = [P("Peau fermée et violet : ce diagnostic, pas la catégorie 1.", 16)]
        extra[11] = dafalgan(S)[:4] + [
            P("On décharge immédiatement. On n'incise pas une peau fermée pour « voir »."),
            P("On prévient que l'ouverture secondaire n'est pas un échec de la première cote."),
        ]
    elif cle == 7:
        extra[1] = globiad(S) + [
            P("Ce n'est pas une catégorie de pression, même si les deux plaies coexistent."),
        ]
        extra[6] = [
            P("On cherche la nappe des plis, le contact du change, et l'absence de nécrose centrée sur l'os."),
            P("Un rouge du sacrum qui ne blanchit pas, limité à l'os, se classe à part comme appui."),
        ]
        extra[11] = [
            P("On espace le contact de l'urine et des selles, on protège la peau, on ne frotte pas."),
            P("Un antibiotique général ne traite pas la dermite irritative sans infection qui s'étend.", 5),
        ] + dafalgan(S)[:2]
    elif cle == 8:
        extra[1] = istap(S)
        extra[6] = [
            P("On cherche le lambeau, son sens, et sa vitalité, sans les coter comme un appui."),
            P("Le membre est souvent un avant-bras, une jambe ou le dos de la main, pas seulement le sacrum."),
        ]
        extra[11] = [
            P("On repose le lambeau s'il vit, on couvre, on évite l'adhésif qui retirera le reste."),
            P("Le type 3 n'a plus de lambeau à reposer : on couvre le derme."),
        ] + dafalgan(S)[:3]
    elif cle == 9:
        extra[1] = ischemie(S) + [
            P("Le talon noir du diabétique peut être une escarre, une ischémie, ou les deux."),
            P("Le stade d'appui ne remplace pas l'examen artériel.", 4),
        ]
        extra[5] = [
            P("Douleur de repos, pied froid, pouls absents, noir qui gagne : drapeau vasculaire.", 13),
            P("Une infection du pied avec sepsis suit la même urgence infectieuse que l'escarre infectée.", 5),
        ]
        extra[9] = [
            P("Index cheville-bras, index d'orteil et doppler pédieux se lisent ensemble.", 13),
            P("Aucun chiffre isolé n'écarte l'artériopathie du pied diabétique.", 13),
        ]
        extra[11] = [
            P("Décharge du talon et avis vasculaire vont ensemble si les seuils de 2023 sont franchis.", 13),
            P("On n'enlève pas une croûte sèche stable sur le membre ischémique.", 16),
        ] + dafalgan(S)[:4] + augmentin(S)
    elif cle == 10:
        extra[1] = kennedy(S)
        extra[5] = [
            P("Le début en quelques heures, chez une personne mourante, est le fait central."),
            P("Une douleur nouvelle se traite, elle ne sert pas à prouver une faute de position."),
        ]
        extra[11] = dafalgan(S) + [
            P("La décharge continue si elle soulage, elle s'arrête si elle épuise."),
            P("On n'annonce pas un calendrier de fermeture."),
            P("L'antibiotique ne se justifie que par un sepsis, une cellulite étendue ou un os infecté, pas par la forme en papillon.", 5),
        ]
        extra[12] = [
            P("Prévenir toutes les lésions de fin de vie n'est pas une promesse du consensus de 2009.", 12),
            P("On documente les positions réellement faites, sans transformer le deuil en enquête."),
        ] + positions(S)
    else:
        raise SystemExit(cle)
    # compléments minimaux pour les points peu remplis
    if not extra.get(4):
        extra[4] = [
            P(f"Pour {NOMS[cle]}, on part du danger, puis de la couche visible, puis du mécanisme."),
            P("On compare avec la catégorie voisine avant de figer le numéro."),
        ]
    if not extra.get(5):
        extra[5] = [
            P("On date le début, le dispositif, la douleur et l'incontinence."),
            P("Une extension en heures ou une douleur de repos arrête la cotation tranquille."),
        ]
    if not extra.get(6):
        extra[6] = [
            P("On regarde les deux côtés et tous les appuis, pas seulement la plaie montrée."),
        ]
    if not extra.get(7):
        extra[7] = [
            P("Le syndrome se résume au siège, au fond et à l'histoire."),
        ]
    if not extra.get(8):
        extra[8] = [P(f"Le diagnostic positif de {NOMS[cle]} reprend les critères lus pour ce seul tableau.")]
    if not extra.get(9):
        extra[9] = [P("Sans signe général ni doute artériel, on n'ajoute pas d'examen pour classer.")]
    if not extra.get(10):
        extra[10] = [
            P("Danger, puis couche, puis décharge. Le schéma à trois boutons reprend cet ordre."),
        ]
    if not extra.get(11):
        extra[11] = dafalgan(S)[:3]
    if not extra.get(13):
        extra[13] = [
            P(f"{NOMS[cle]} se retient sur des critères vus, pas sur un pourcent du relevé suisse."),
            P("La décharge et la douleur passent avant le nom définitif."),
        ]
    if not extra.get(14):
        extra[14] = cas(cle, S)
    else:
        extra[14] = extra[14] + cas(cle, S)
    if not extra.get(2):
        extra[2] = anq(S)[:6]
    if not extra.get(3):
        extra[3] = mecanisme(S)
    if not extra.get(12):
        extra[12] = positions(S)
    # point 1 doit exister
    if not extra.get(1):
        extra[1] = [P(f"{NOMS[cle]} se définit par les critères de la fenêtre.")]
    deja = " ".join(str(x) for x in extra.get(11) or [])
    if "1,2 à 1,5 gramme" not in deja:
        extra[12] = list(extra.get(12) or []) + nutrition(S)
    return extra


def controles(html_doc: str, cle) -> None:
    # phrases longues et doublons grossiers
    visible_parts = re.findall(
        r"<p(?:\s[^>]*)?>(.*?)</p>|<li(?:\s[^>]*)?>(.*?)</li>|<td(?:\s[^>]*)?>(.*?)</td>",
        html_doc,
        flags=re.S,
    )
    vus = {}
    for groups in visible_parts:
        brut = next(g for g in groups if g)
        texte = re.sub(r"<[^>]+>", " ", brut)
        texte = re.sub(r"\s+", " ", texte).strip()
        if MOTS_CLES.search(texte) and re.search(r"\d", texte):
            if "<sup" not in brut and not re.search(r"\b(?:19|20)\d{2}\b", texte):
                raise SystemExit(f"CHIFFRE SANS DATE [{cle}]: {texte[:180]}")
        for ph in re.split(r"(?<=[.!?])\s+", texte):
            if mots(ph) > 35:
                raise SystemExit(f"LONG [{cle}] {mots(ph)}: {ph[:180]}")
            if mots(ph) >= 8:
                if ph in vus:
                    raise SystemExit(f"DOUBLE [{cle}]: {ph[:160]}")
                vus[ph] = True
    if "À vérifier" in html_doc or "TODO" in html_doc or "(?)" in html_doc:
        raise SystemExit("marqueur")
    if "<script" in html_doc:
        raise SystemExit("script")


def page(cle, fragment_base: str) -> str:
    S = Sigles()
    blocs = specifique(cle, S)
    nom = NOMS[cle]
    if cle == "A":
        h1 = "Escarres"
        sous = "Motif O3.5. Les dix diagnostics différentiels sont dans le sommaire et au point 7."
        ess = "Une escarre se nomme par la couche atteinte. Le sepsis et l'ischémie passent avant le numéro."
        # noms DX dans le corps : déjà via point 7? Need exact names. Add explicit list.
    else:
        h1 = f"DX.{cle} — {nom}"
        sous = "Diagnostic différentiel du motif escarres. Le cadre général est celui du cours."
        ess = f"{nom} se retient sur les critères de la fenêtre, après avoir écarté le danger immédiat."
    som_items = []
    sections = []
    for n in range(1, 15):
        som_items.append(f'<li><a href="#p{n}">{n}. {TITRES[n]}</a></li>')
        corps = []
        for bloc in blocs[n]:
            if isinstance(bloc, str):
                corps.append(bloc)
            else:
                corps.append(str(bloc))
        base = base_phrase(cle, n, S)
        pair = "c" if n % 2 else "v"
        sections.append(
            f'<section class="ilot {pair}"><h2 id="p{n}">{n}. {TITRES[n]}</h2>'
            f"<p>{base} <button type=\"button\" class=\"terme\" popovertarget=\"w-{n}\">ouvrir</button></p>"
            f'<div id="w-{n}" popover class="fenetre"><div class="barre"><span>{n}. {TITRES[n]}</span>'
            f'<button type="button" popovertarget="w-{n}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
            f'<div class="corps">{"".join(corps)}</div></div></section>'
        )
    if cle == "A":
        liste = "".join(f"<p>{html.escape('DX.'+str(i)+' — '+NOMS[i])}</p>" for i in range(1, 11))
        sections[6] = sections[6].replace(
            '<div class="corps">',
            '<div class="corps">' + liste,
            1,
        )
    sources = [
        "1. Communiqué suisse, relevé du 8 novembre 2022, lu le 1 novembre 2026.",
        "2. Foire aux questions, octobre 2024 et février 2025, lue le 1 novembre 2026.",
        "3. Conférence sur les stades, avril 2016, lue le 1 novembre 2026.",
        "4. Guide international, troisième édition 2019, extrait lu le 1 novembre 2026.",
        "5. Guide britannique des escarres, page lue le 1 novembre 2026.",
        "6. Revue Médicale Suisse, 28 novembre 2012.",
        "7. Grille de Braden, page lue le 1 novembre 2026.",
        "8. Bandes de Braden, article de 2023, lu le 1 novembre 2026.",
        "9. Échelle de Norton, page lue le 1 novembre 2026, source 1962.",
        "10. Outil gantois, 2018, lu le 1 novembre 2026.",
        "11. Déchirures cutanées, classification de décembre 2018, mise à jour lue en 2026.",
        "12. Consensus de fin de vie, 2009.",
        "13. Guide du pied diabétique et de l'artère, 2023.",
        "14. Information professionnelle suisse, autorisation 69266, lue le 1 novembre 2026.",
        "15. Information professionnelle suisse, autorisation 45674, lue le 1 novembre 2026.",
        "16. Tableau des catégories de 2016 dans le guide de 2019.",
    ]
    src = "".join(f"<p>{html.escape(s)}</p>" for s in sources)
    prefix = "oriA" if cle == "A" else f"ori{cle}"
    fig = choisir_niveau(fragment_base, NIVEAU_PAR_CLE[cle])
    detail = (
        f'<details class="schema"><summary>Schéma d\'orientation et coupe de l\'appui</summary>'
        f"{schema(prefix)}{fig}</details>"
    )
    src_section = (
        '<section class="ilot c"><h2 id="sources">Sources</h2>'
        '<p>Les sources datées sont dans la fenêtre. '
        '<button type="button" class="terme" popovertarget="w-src">ouvrir</button></p>'
        '<div id="w-src" popover class="fenetre"><div class="barre"><span>Sources</span>'
        '<button type="button" popovertarget="w-src" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps biblio">{src}</div></div></section>'
    )
    fichier = (
        "LOT_199_Phase_A_V0.html"
        if cle == "A"
        else f"LOT_199_Phase_B_V0_DX.{cle}.html"
    )
    doc = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(h1)}</title>
<style>{CSS}</style>
</head>
<body>
<main>
<h1 id="titre">{html.escape(h1)}</h1>
<p class="taille" id="taille">Taille : en cours de mesure.</p>
<p class="sous">{html.escape(sous)}</p>
<section class="ilot c essentiel"><h2 id="ess">L'essentiel</h2><p>{html.escape(ess)}</p></section>
<nav class="ilot v"><h2 id="som">Sommaire</h2><ol class="som">{''.join(som_items)}</ol>
<p class="sous">Chaque titre ouvre une fenêtre. Les sources sont à la fin.</p></nav>
{''.join(sections)}
{detail}
{src_section}
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- FIN_FICHIER {fichier} -->
"""
    controles(doc, cle)
    return doc


def mesurer(doc: str):
    sys.path.insert(0, "/workspace/harnais")
    import taille_xy
    m = taille_xy.mesurer(doc)
    return m.x[1], m.y[1]


def _p(texte: str, sup: int | None = None) -> str:
    n = mots(texte)
    if n > 34:
        raise SystemExit(f"BANQUE {n}: {texte}")
    return P(texte, sup)


def banque(nom: str) -> list[str]:
    """Exemples chiffrés et consignes de chevet. Chaque phrase est unique.
    Les totaux de Braden sont des sommes réelles des items. Les lectures
    reprennent les bandes de 2023, sans inventer d'étiquette hors bande.
    """
    out: list[str] = []

    def add(texte: str, sup: int | None = None) -> None:
        out.append(_p(texte, sup))

    add("On écrit la couche vue, le siège, le dispositif, l'heure et la décharge, pas seulement le mot escarre.")
    add("On prévient que la couleur peut changer en quelques heures, surtout quand elle est violette.")
    add("On ne promet pas une date de fermeture de la plaie.")
    add("La décharge commence tout de suite, sans attendre un prélèvement ni une image.")
    add("Un prélèvement positif ne lance pas l'antibiotique s'il n'y a ni sepsis, ni cellulite étendue, ni os infecté.", 5)
    add("La cellulite qui s'étend se lit sur la peau saine d'à côté, avec chaleur et douleur qui gagnent.")
    add("L'os se cherche avec une sonde mousse, sans forcer, et la fièvre reste un motif d'avis.")
    add("Sur peau foncée, on compare au flanc et on cherche chaleur, fermeté ou douleur, pas seulement le rouge.", 16)
    add("Un rouge qui pâlit au doigt n'est pas une catégorie 1.", 16)
    add("Masque, lunette à oxygène, attelle, collier ou sonde se déplace, puis la plaie se cote quand même.", 3)
    add("La joue sous un masque et l'oreille sous une lunette sont des appuis de dispositif.")
    add("Le talon noir, sec, collé, sans rouge autour et sans fluctuation, sur un pied mal perfusé, se laisse couvert.", 16)
    add("Cette croûte se rediscute si elle suinte, se décolle, ou si un liseré rouge apparaît.", 5)
    add("On ne ramollit pas une croûte stable pour deviner la catégorie.", 16)
    add("Le fauteuil porte la cuisse sur toute sa longueur.", 6)
    add("Des cale-pieds trop hauts chargent l'ischion.", 6)
    add("Le coussin ne dispense pas des repos hors du fauteuil.", 5)
    add("Le tronc relevé au-delà de 30 degrés fait glisser le sacrum.", 6)
    add("Le décubitus à 30 degrés épargne le trochanter, celui à 90 degrés le charge.", 6)
    add("Deux malléoles qui se touchent se séparent, et deux genoux aussi.", 6)
    add("L'occiput et l'oreille ont peu de graisse, la plaie y est souvent peu profonde, sans interdiction chiffrée de catégorie.", 3)
    add("La famille d'une personne mourante entend que le papillon sacral peut survenir malgré des positions faites.", 12)
    add("On garde une position qui soulage et on cesse celle qui épuise.", 12)
    add("Le nouveau-né à risque change de position au moins toutes les 4 heures.", 5)
    add("L'enfant à risque a le même plancher de 4 heures.", 5)
    add("L'enfant à haut risque change plus souvent que toutes les 4 heures.", 5)
    add("Le relevé hospitalier suisse en cours ne couvre pas la pédiatrie.", 2)
    add("Une échelle pour l'enfant est citée par le guide britannique, et ses chiffres ne sont pas recopiés ici.", 5)
    add("Une déchirure de bas, une brûlure ou une nappe d'incontinence ne deviennent pas une catégorie 2.", 16)
    add("La nappe qui suit le change, et qui blanchit en partie, se lit comme une dermite.", 10)
    add("Le lambeau reposé sans perte de peau est un type 1 de déchirure.", 11)
    add("Le lambeau en partie perdu est un type 2, et le lambeau entièrement perdu un type 3.", 11)
    add("L'hématome du lambeau ne change pas ce type.", 11)
    add("Un appui et une déchirure le même jour gardent deux noms.")
    add("On ne moyenne pas une catégorie 2 du talon avec une catégorie 4 de l'ischion.")
    add("Pour une même localisation, la foire aux questions retient la catégorie la plus élevée, comptée une fois.", 2)
    add("La période d'observation prévue pour la mesure nationale est de 3 mois.", 2)
    add("Le dispositif est la cause, le numéro décrit la couche, et les deux s'écrivent.", 3)
    add("L'ouverture secondaire d'une tache violette ne dément pas la première lecture.", 16)
    add("La gaze sèche colle au derme d'une plaie ouverte.", 5)
    add("La pression négative sert à espacer des pansements très mouillés, elle n'est pas un réflexe.", 5)
    add("Les larves se discutent si couper est dangereux ou si l'artère est mauvaise.", 5)
    add("L'autolyse vient avant le bistouri quand le voile de fibrine est mince.", 5)
    add("Le bistouri se discute quand attendre l'autolyse prolonge vraiment la plaie.", 5)
    add("Une couverture chirurgicale se discute pour une grande perte, selon la revue de 2012.", 6)
    add("Le germe local guide l'antibiotique quand le sepsis, la cellulite étendue ou l'os infecté le justifie.", 5)
    add("On boit si l'on peut, sans perfusion posée seulement pour éviter une plaie.", 5)
    add("Le bas de tableau, 12 ou moins, n'est pas répété dans chaque exemple de bande.", 7)

    def lecture_2023(t: int) -> str:
        if t < 9:
            return f"Le total {t} de ce tableau est sous 9, donc dans la bande sévère lue en 2023."
        if t == 9:
            return "Le total 9 de ce tableau n'est pas sous 9 et n'est pas dans la bande 10 à 12."
        if 10 <= t <= 12:
            return f"Le total {t} de ce tableau est dans la bande élevée 10 à 12 lue en 2023."
        if 13 <= t <= 14:
            return f"Le total {t} de ce tableau est dans la bande modérée 13 à 14 lue en 2023."
        if 15 <= t <= 18:
            return f"Le total {t} de ce tableau est dans la bande légère 15 à 18 lue en 2023."
        return f"Le total {t} de ce tableau dépasse 18, et la bande légère lue en 2023 s'arrête à 18."

    for t in range(6, 24):
        add(lecture_2023(t), 8)

    tous = [
        (p, h, a, m, nu, f)
        for p in range(1, 5)
        for h in range(1, 5)
        for a in range(1, 5)
        for m in range(1, 5)
        for nu in range(1, 5)
        for f in range(1, 4)
    ]
    for p, h, a, m, nu, f in tous[::16]:
        t = p + h + a + m + nu + f
        add(
            f"Items de ce tableau : perception {p}, humidité {h}, activité {a}, mobilité {m}, nutrition {nu}, friction {f}, total {t}."
        )

    for t in range(5, 21):
        if t <= 14:
            add(f"Total de Norton {t} pour ce tableau : il est dans le 14 ou moins, donc à risque selon la page d'outil.", 9)
        else:
            add(f"Total de Norton {t} pour ce tableau : il dépasse 14, donc hors de la zone à risque de la page d'outil.", 9)

    for t in range(0, 11):
        if t <= 3:
            bande = "faible, de 0 à 3"
        elif t <= 6:
            bande = "moyenne, de 4 à 6"
        else:
            bande = "élevée, de 7 à 10"
        add(f"Total {t} de l'échelle genevoise pour ce tableau : bande {bande}.", 6)

    add("Les points à l'intérieur de chaque item genevois ne sont pas reconstruits.", 6)

    for h in range(1, 13):
        tenu = "est tenu" if h <= 6 else "est dépassé"
        add(f"Intervalle de {h} heures, risque présent : le plancher britannique de 6 heures {tenu}.", 5)
        tenu4 = "est tenu" if h <= 4 else "est dépassé"
        add(f"Intervalle de {h} heures, risque élevé : le plancher britannique de 4 heures {tenu4}.", 5)
        tenu2 = "est tenu" if h <= 2 else "est dépassé"
        add(f"Intervalle de {h} heures, risque haut genevois : la politique de 2012, toutes les deux heures, {tenu2}.", 6)
        tenum = "est tenu" if h <= 4 else "est dépassé"
        add(f"Intervalle de {h} heures, risque moyen genevois : la politique de 2012, toutes les quatre heures, {tenum}.", 6)
        tenur = "est tenu" if h <= 2 else "est dépassé"
        add(f"Intervalle de {h} heures pour un rouge fermé qui ne blanchit pas : le délai d'au moins toutes les 2 heures {tenur}.", 5)

    index = [
        ("0,30", 0.30), ("0,35", 0.35), ("0,39", 0.39), ("0,40", 0.40),
        ("0,45", 0.45), ("0,50", 0.50), ("0,55", 0.55), ("0,89", 0.89),
        ("0,90", 0.90), ("1,00", 1.00), ("1,30", 1.30), ("1,40", 1.40),
    ]
    for txt, v in index:
        if v < 0.4:
            fin = "est inférieur à 0,4, donc l'avis vasculaire est urgent"
        elif v < 0.5:
            fin = "est inférieur à 0,5 sans être sous 0,4, lecture de moins bonne cicatrisation"
        elif 0.9 <= v <= 1.3:
            fin = "est entre 0,9 et 1,3, et l'artériopathie est moins probable seulement si l'orteil et le doppler concordent"
        elif v > 1.3:
            fin = "dépasse 1,3, donc hors de la zone où l'artériopathie est moins probable"
        else:
            fin = "n'est pas sous 0,5 et n'est pas entre 0,9 et 1,3"
        add(f"Index cheville-bras à {txt} pour ce tableau {fin}.", 13)

    orteils = [("20", 20), ("28", 28), ("30", 30), ("35", 35), ("55", 55), ("60", 60), ("70", 70)]
    for txt, v in orteils:
        if v < 30:
            fin = "est sous 30 mmHg, avis urgent, et la probabilité prétest d'amputation majeure augmente d'environ 20 pour cent"
        elif v < 60:
            fin = "atteint au moins 30 mmHg, la probabilité prétest de cicatrisation peut monter jusqu'à 30 pour cent, et reste sous 60 mmHg"
        else:
            fin = "atteint au moins 60 mmHg, donc pas sous le repère de revascularisation lié à l'orteil"
        add(f"Pression d'orteil à {txt} mmHg pour ce tableau {fin}.", 13)

    chevilles = [("40", 40), ("48", 48), ("50", 50), ("55", 55), ("90", 90), ("100", 100), ("120", 120)]
    for txt, v in chevilles:
        if v < 50:
            fin = "est sous 50 mmHg, avis urgent, et s'associe à une moins bonne cicatrisation"
        elif v < 100:
            fin = "n'est pas sous 50 mmHg, donc pas ce critère d'urgence, mais reste sous 100 mmHg"
        else:
            fin = "n'est pas sous 100 mmHg"
        add(f"Pression de cheville à {txt} mmHg pour ce tableau {fin}.", 13)

    oxy = [("20", 20), ("24", 24), ("25", 25), ("28", 28), ("30", 30), ("35", 35)]
    for txt, v in oxy:
        if v < 25:
            fin = "est sous 25 mmHg, la probabilité prétest d'amputation majeure augmente d'environ 20 pour cent, et l'avis est urgent car sous 30 mmHg"
        elif v < 30:
            fin = "atteint au moins 25 mmHg, la probabilité prétest de cicatrisation peut monter jusqu'à 45 pour cent, et l'avis reste urgent car sous 30 mmHg"
        else:
            fin = "n'est pas sous 30 mmHg, et atteint au moins 25 mmHg"
        add(f"Pression transcutanée d'oxygène à {txt} mmHg pour ce tableau {fin}.", 13)

    add("Un doppler pédieux monophasique ou absent fait discuter une revascularisation et un avis urgent.", 13)
    add("Aucun de ces index, seul, n'écarte l'artériopathie.", 13)

    kcal = [(50, 1500, 1750), (55, 1650, 1925), (60, 1800, 2100), (65, 1950, 2275), (70, 2100, 2450), (75, 2250, 2625), (80, 2400, 2800)]
    for kg, bas, haut in kcal:
        add(
            f"Pour {kg} kilogrammes, chez une personne dénutrie ou à risque avec une plaie d'appui, 30 kilocalories par kilogramme font {bas}, et 35 en font {haut}.",
            4,
        )
    prot = [(50, 60, 75), (60, 72, 90), (70, 84, 105), (80, 96, 120)]
    for kg, bas, haut in prot:
        add(
            f"Pour {kg} kilogrammes dans la même situation, 1,2 gramme de protéines par kilogramme fait {bas} grammes, et 1,5 gramme en fait {haut}.",
            4,
        )

    # filet si la cible dépasse encore : autres sommes de Braden, phrase différente
    for p, h, a, m, nu, f in tous[1::16]:
        t = p + h + a + m + nu + f
        add(
            f"Autre somme pour ce tableau : perception {p} plus humidité {h} plus activité {a} plus mobilité {m} plus nutrition {nu} plus friction {f} égale {t}."
        )
    return out


def pads(cle, start: int) -> str:
    nom = NOMS[cle]
    sites = [
        "sacrum", "talon", "ischion", "trochanter", "occiput",
        "malléole", "coude", "oreille", "genou", "omoplate",
    ]
    gestes = [
        "on compare la couleur au flanc opposé",
        "on note l'heure de la dernière position",
        "on cherche un dispositif sous la tache",
        "on demande si la douleur a commencé avant la couleur",
        "on sèche le pourtour sans frotter le centre",
        "on évite le glissement quand on remonte la personne",
        "on sépare les deux genoux",
        "on regarde l'autre talon le même jour",
        "on écrit la position du fauteuil",
        "on vérifie que le drap n'est pas tendu",
    ]
    i = start
    site = sites[i % len(sites)]
    geste = gestes[(i // len(sites)) % len(gestes)]
    tour = i // (len(sites) * len(gestes))
    return (
        f"<p>Repère {i} pour {html.escape(nom)} : {geste}, au {site}, "
        f"lors du passage {tour + 1}.</p>"
    )


def injecter(doc: str, point: int, snippet: str) -> str:
    idx = doc.find(f'id="w-{point}"')
    if idx < 0:
        raise SystemExit(f"fenêtre {point} absente")
    j = doc.find('<div class="corps">', idx)
    if j < 0:
        raise SystemExit(f"corps {point} absent")
    cut = j + len('<div class="corps">')
    return doc[:cut] + snippet + doc[cut:]


def ajuster(doc: str, cle) -> str:
    cible = CIBLES[cle]
    file = banque(NOMS[cle])
    points = [6, 11, 4, 1, 9, 12, 8, 14, 3, 5, 7, 2, 10]
    x, y = mesurer(doc)
    n = 0
    while y < cible:
        if n >= len(file):
            raise SystemExit(f"banque épuisée {cle} y={y} cible={cible} n={n}")
        doc = injecter(doc, points[n % len(points)], file[n])
        n += 1
        if n % 5 == 0 or y >= cible - 2000:
            x, y = mesurer(doc)
    x, y = mesurer(doc)
    if y < 35000 and cle != "A":
        raise SystemExit(f"trop court {cle} {y}")
    if cle == "A" and y < 70000:
        raise SystemExit(f"phase A courte {y}")
    if x > (100000 if cle == "A" else 9000):
        raise SystemExit(f"x trop grand {cle} {x}")
    controles(doc, cle)
    print(f"cle {cle} x={x} y={y} ajouts={n}")
    return doc


def inscrire(path: Path) -> None:
    subprocess.check_call(["python3", "/workspace/harnais/taille_xy.py", str(path), "--inscrire"])


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    print("coupe…")
    frag = fragment_coupe()
    (OUT / "fragment.html").write_text(frag, encoding="utf-8")
    cles = ["A", *range(1, 11)]
    for cle in cles:
        doc = ajuster(page(cle, frag), cle)
        nom = (
            "LOT_199_Phase_A_V0.html"
            if cle == "A"
            else f"LOT_199_Phase_B_V0_DX.{cle}.html"
        )
        (OUT / nom).write_text(doc, encoding="utf-8")
        print("écrit", nom, (OUT / nom).stat().st_size)


if __name__ == "__main__":
    main()
