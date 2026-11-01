#!/usr/bin/env python3
"""Construit les HTML V8 de LOT_197. Ne lance pas le routage."""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_197"
sys.path.insert(0, str(RACINE / "harnais"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import taille_xy  # noqa: E402
import grilles  # noqa: E402

MOTS = re.compile(r"seuil|score|prévalence|sensibilit|spécificit|incidence", re.I)
AN = re.compile(r"\b(?:19|20)\d{2}\b")


def n1(x: float) -> str:
    return f"{x:.1f}".replace(".", ",")


def n2(x: float) -> str:
    return f"{x:.2f}".replace(".", ",")


class Sig:
    def __init__(self) -> None:
        self.vu: set[str] = set()

    def __call__(self, code: str, titre: str, expl: str) -> str:
        coeur = f'<abbr title="{titre}">{code}</abbr>'
        if code not in self.vu:
            self.vu.add(code)
            return f"{coeur} ({expl})"
        return coeur


def mots(s: str) -> int:
    return len(re.sub(r"<[^>]+>", " ", s).split())


class Sac:
    def __init__(self) -> None:
        self.p: list[str] = []
        self.vus: set[str] = set()

    def a(self, phrase: str, src: int | None = None) -> None:
        brut = phrase.strip()
        if not brut.endswith("."):
            brut += "."
        if mots(brut) > 34:
            raise SystemExit(f"PHRASE LONGUE ({mots(brut)}): {brut}")
        if brut in self.vus:
            raise SystemExit(f"DOUBLE: {brut}")
        self.vus.add(brut)
        if src:
            brut += f' <sup class="s">{src}</sup>'
        self.p.append(f"<p>{brut}</p>")

    def table(self, titre: str, lignes: list[tuple[str, str]], src: int) -> None:
        self.a(titre, src)
        rows = ["<tr><th>Repère</th><th>Lecture retenue</th></tr>"]
        for a, b in lignes:
            if mots(a) > 34 or mots(b) > 34:
                raise SystemExit(f"CELLULE LONGUE: {a} | {b}")
            rows.append(f"<tr><td>{a}</td><td>{b}</td></tr>")
        self.p.append('<div class="tw"><table>\n' + "\n".join(rows) + "\n</table></div>")

    def html(self) -> str:
        return "\n".join(self.p)


def verifier_dates(html: str) -> None:
    for m in re.finditer(r"<p[^>]*>(.*?)</p>|<li[^>]*>(.*?)</li>", html, re.S):
        bloc = m.group(1) or m.group(2) or ""
        vis = re.sub(r"<[^>]+>", " ", bloc)
        if MOTS.search(vis) and re.search(r"\d", vis):
            sup = re.findall(r"<sup[^>]*>\s*(\d+)", bloc)
            if sup or AN.search(vis):
                continue
            raise SystemExit("SANS DATE: " + vis[:180])


def schema(fid: str, etapes: list[tuple[str, str, list[str]]]) -> str:
    """Trois niveaux radio, sans script. etapes: (etiquette, titre, lignes courtes)."""
    if len(etapes) != 3:
        raise SystemExit("schéma à trois niveaux")
    inputs = []
    labels = []
    plans = []
    css = []
    for i, (etiq, titre, lignes) in enumerate(etapes):
        iid = f"{fid}{i}"
        inputs.append(
            f'<input class="sr" type="radio" name="{fid}" id="{iid}"{" checked" if i == 0 else ""}>'
        )
        labels.append(f'<label for="{iid}">{etiq}</label>')
        y = 78
        textes = [f'<text x="320" y="42" text-anchor="middle" font-size="18" font-weight="700" fill="#14303b">{titre}. </text>']
        for ligne in lignes:
            if len(ligne) > 60:
                raise SystemExit("LIGNE SVG: " + ligne)
            textes.append(
                f'<rect x="40" y="{y}" width="560" height="36" rx="8" fill="#e7f4fb" stroke="#176fa0"/>'
            )
            textes.append(
                f'<text x="320" y="{y + 24}" text-anchor="middle" font-size="15" fill="#14303b">{ligne}. </text>'
            )
            y += 48
        plans.append(
            f'<svg class="niv n{i}" viewBox="0 0 640 340" role="img" aria-label="{titre}">'
            + "".join(textes)
            + "</svg>"
        )
        css.append(
            f"#{iid}:checked ~ .plan .n{i}{{display:block}}"
            f"#{iid}:checked ~ .bn label[for='{iid}']{{background:#d7eef8;border-color:#176fa0}}"
        )
    return (
        f'<details class="schema"><summary>Schéma interactif</summary><figure>'
        f"<style>{''.join(css)}.plan .niv{{display:none}}</style>"
        f'<div class="sch" id="{fid}">{"".join(inputs)}<div class="bn">{"".join(labels)}</div>'
        f'<div class="plan">{"".join(plans)}</div></div>'
        f"<figcaption>Schéma d'orientation, pas une radiographie. Le bouton change le niveau.</figcaption>"
        f"</figure></details>"
    )


def cuisse(prefix: str, rayon: tuple[int, int, int]) -> str:
    spec = importlib.util.spec_from_file_location(
        "dessinateur", RACINE / "grok-LOTS-html/outils/dessinateur/dessinateur.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    def niv(i: int, etiq: str, note: str, rq: int, rg: int, gras: int) -> dict:
        return {
            "id": f"n{i}",
            "etiquette": etiq,
            "note": note,
            "viewBox": [0, 0, 1000, 760],
            "defaut": i == 0,
            "repere": {"texte": "D", "x": 80, "y": 90, "titre": "Droite du patient, à gauche du schéma"},
            "structures": [
                {
                    "id": f"peau{i}",
                    "nom": "Peau",
                    "numero": 1,
                    "geometrie": {"type": "ellipse", "cx": 500, "cy": 390, "rx": 420, "ry": 300},
                    "remplissage": "#f3cfc3",
                    "contour": "#c48b7a",
                    "epaisseur": 1.2,
                    "badge": [150, 140],
                    "definition": "Enveloppe cutanée du schéma de cuisse. Ce n'est pas une coupe scanographique.",
                },
                {
                    "id": f"gras{i}",
                    "nom": "Graisse",
                    "numero": 2,
                    "geometrie": {"type": "ellipse", "cx": 500, "cy": 390, "rx": gras, "ry": int(gras * 0.72)},
                    "remplissage": "#ffe08a",
                    "contour": "#c8962e",
                    "epaisseur": 1.2,
                    "badge": [230, 210],
                    "definition": "Graisse sous-cutanée en jaune. Elle peut être épaisse alors que le muscle fond.",
                },
                {
                    "id": f"quad{i}",
                    "nom": "Quadriceps",
                    "numero": 3,
                    "geometrie": {"type": "ellipse", "cx": 420, "cy": 340, "rx": rq, "ry": int(rq * 0.72)},
                    "remplissage": "#e07a7a",
                    "contour": "#8d2f2f",
                    "epaisseur": 1.4,
                    "badge": [390, 280],
                    "definition": "Loge antérieure. Le rayon diminue quand la masse musculaire baisse.",
                },
                {
                    "id": f"post{i}",
                    "nom": "Loge postérieure",
                    "numero": 4,
                    "geometrie": {"type": "ellipse", "cx": 580, "cy": 480, "rx": rg, "ry": int(rg * 0.7)},
                    "remplissage": "#d35b5b",
                    "contour": "#6e2424",
                    "epaisseur": 1.4,
                    "badge": [680, 520],
                    "definition": "Ischio-jambiers schématiques, du même côté que la fonte.",
                },
                {
                    "id": f"os{i}",
                    "nom": "Fémur",
                    "numero": 5,
                    "geometrie": {"type": "ellipse", "cx": 500, "cy": 400, "rx": 42, "ry": 42},
                    "remplissage": "#f7f1e4",
                    "contour": "#8a8172",
                    "epaisseur": 1.4,
                    "badge": [500, 400],
                    "definition": "Repère osseux au centre. L'os ne mesure pas la sarcopénie.",
                },
            ],
        }

    desc = {
        "id": prefix,
        "titre": "Schéma de cuisse",
        "question": {
            "intitule": "Où est le muscle ?",
            "html": "<p>Le muscle est en rouge, la graisse en jaune, l'os au centre. Le niveau change avec les boutons.</p>",
        },
        "sources_courtes": "Schéma pédagogique. Orientation avec le repère D. Pas un cliché.",
        "niveaux": [
            niv(0, "Cuisse conservée", "Schéma. Loge musculaire large et graisse fine.", rayon[0], rayon[0] - 20, 300),
            niv(1, "Fonte musculaire", "Schéma. Les deux loges rétrécissent, l'os reste.", rayon[1], max(60, rayon[1] - 16), 300),
            niv(2, "Graisse épaisse", "Schéma. La graisse augmente et le muscle reste petit.", rayon[2], max(60, rayon[2] - 16), 390),
        ],
    }
    frag = mod.rendre(desc, "../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf")
    frag = re.sub(r"(?is)<script\b[^>]*>.*?</script>", "", frag)
    if "<script" in frag.lower():
        raise SystemExit("script restant")
    return frag


def style_page() -> str:
    src = (RACINE / "grok-LOTS-html/LOT_195/LOT_195_Phase_A_V0.html").read_text(encoding="utf-8")
    m = re.search(r"<style>.*?</style>", src, re.S)
    if not m:
        raise SystemExit("style absent")
    return m.group(0)


STYLE = style_page()

DXS = [
    "Sarcopénie primaire",
    "Dénutrition par carence d'apport",
    "Dénutrition inflammatoire chronique",
    "Cachexie cancéreuse",
    "Dysphagie oropharyngée",
    "Anorexie de la dépression",
    "Troubles alimentaires de la démence",
    "Syndrome de réalimentation",
    "Malabsorption du sujet âgé",
    "Fonte musculaire endocrinienne",
]


def page(titre: str, sous: str, essentiel: str, ilots: list[tuple[str, str, str]], fin: str, sources: str) -> str:
    som = []
    corps = []
    for i, (h2, ile, fen) in enumerate(ilots, 1):
        som.append(f'<li><a href="#p{i}">{i}. {h2.split(". ", 1)[-1]}</a></li>')
        corps.append(
            f'<section class="ilot {"c" if i % 2 else "v"}"><h2 id="p{i}">{h2}</h2>'
            f"<p>{ile} <button type=\"button\" class=\"terme\" popovertarget=\"w-{i}\">ouvrir</button></p>"
            f'<div id="w-{i}" popover class="fenetre"><div class="barre"><span>{h2}</span>'
            f'<button type="button" popovertarget="w-{i}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
            f'<div class="corps">{fen}</div></div></section>'
        )
    html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre}</title>
{STYLE}
</head>
<body>
<main>
<h1 id="titre">{titre}</h1>
<p class="taille" id="taille">Taille : mesurée par le script du dépôt.</p>
<p class="sous">{sous}</p>
<section class="ilot c essentiel"><h2 id="ess">L'essentiel</h2><p>{essentiel}</p></section>
<nav class="ilot v"><h2 id="som">Sommaire</h2><ol class="som">{''.join(som)}</ol>
<p class="sous">Chaque titre ouvre une fenêtre. Les sources sont à la fin.</p></nav>
{''.join(corps)}
<section class="ilot c"><h2 id="sources">Sources</h2>
<p>Les preuves datées sont dans la fenêtre et dans le dossier du cours. <button type="button" class="terme" popovertarget="w-src">ouvrir</button></p>
<div id="w-src" popover class="fenetre"><div class="barre"><span>Sources</span><button type="button" popovertarget="w-src" popovertargetaction="hide" aria-label="Fermer">✕</button></div><div class="corps">{sources}</div></div></section>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- {fin} -->
"""
    verifier_dates(html)
    return html


def sources_html() -> str:
    lignes = [
        "1. Consensus mondial de dénutrition, 2019, lu le 1 novembre 2026.",
        "2. Consensus européen révisé sur la sarcopénie, texte en ligne le 24 septembre 2018, revue 2019.",
        "3. Recommandation gériatrique européenne de nutrition et d'hydratation, 2022.",
        "4. Revue Médicale Suisse, 2021, dépistage de la sarcopénie au cabinet.",
        "5. Mains Libres, article reçu en mars 2020, fascicule 2020.",
        "6. Ligne britannique de soutien nutritionnel, publiée le 22 février 2006, mise à jour le 4 août 2017.",
        "7. Guide du formulaire nutritionnel court, fichier d'octobre 2021.",
        "8. Validation du formulaire court révisé, journal de 2009, page lue le 1 novembre 2026.",
        "9. Formulaire court original, 2001, sensibilité et spécificité lues pour l'ancien seuil.",
        "10. Outil hospitalier de 2003, grades lus dans l'annexe du rapport de 2019.",
        "11. Information professionnelle suisse, autorisation 10989, thiamine, lue le 1 novembre 2026.",
        "12. Information professionnelle suisse, autorisation 33481, vitamine D3 buvable, lue le 1 novembre 2026.",
    ]
    return "\n".join(f"<p>{x}</p>" for x in lignes)


# --- critères communs, phrases courtes ---

def criteres(S: Sig) -> dict[str, Sac]:
    d = {k: Sac() for k in "def epi phy dem ana exa syn dia lab arb pec pre cle pie".split()}
    G = lambda: S("GLIM", "Global Leadership Initiative on Malnutrition", "consensus de dénutrition de 2019")
    E = lambda: S("ESPEN", "European Society for Clinical Nutrition and Metabolism", "société européenne de nutrition clinique")
    W = lambda: S("EWGSOP2", "European Working Group on Sarcopenia in Older People, révision 2", "groupe européen sarcopénie, révision de 2019")
    M = lambda: S("MNA", "Mini Nutritional Assessment", "formulaire nutritionnel de la personne âgée")
    N = lambda: S("NRS", "Nutritional Risk Screening", "dépistage du risque nutritionnel à l'hôpital")
    Q = lambda: S("SARC", "Strength, assistance, rise, climb, falls", "cinq questions de dépistage musculaire")
    A = lambda: S("AIPS", "information professionnelle suisse", "information professionnelle suisse")

    d["def"].a(f"La dénutrition du consensus {G()} n'est pas un simple poids bas.", 1)
    d["def"].a("Il faut au moins un critère phénotypique et un critère étiologique.", 1)
    d["def"].a("Le phénotype regarde la perte de poids, l'indice et la masse musculaire.", 1)
    d["def"].a("L'étiologie regarde l'apport, l'assimilation, ou le fardeau inflammatoire.", 1)
    d["def"].a(f"La sarcopénie du {W()} est une maladie du muscle, pas un synonyme de maigreur.", 2)
    d["def"].a("Elle associe une force basse, puis une masse basse, puis une performance basse si elle est sévère.", 2)
    d["def"].a("La revue suisse de 2021 sépare sarcopénie, dénutrition, fragilité et cachexie.", 4)
    d["def"].a("Dans la dénutrition, la masse grasse et la masse maigre peuvent baisser ensemble.", 4)
    d["def"].a("La cachexie vient d'une maladie chronique inflammatoire et emporte souvent une sarcopénie.", 4)
    d["def"].a("L'inverse n'est pas constant : une sarcopénie peut exister sans cachexie.", 4)
    d["def"].a("La fragilité ajoute une perte d'endurance et d'autres fonctions, dont le muscle n'est qu'une part.", 4)
    d["def"].table(
        "Phénotype diagnostique lu en 2019",
        [
            ("Perte de poids", "Plus de 5 pour cent en six mois, ou plus de 10 pour cent au-delà"),
            ("Indice avant 70 ans", "Inférieur à 20 kilogrammes par mètre carré"),
            ("Indice après 70 ans", "Inférieur à 22 dans le tableau diagnostique, formulation supérieur à 70 ans"),
            ("Masse musculaire", "Basse selon une méthode validée, ou à défaut un périmètre"),
            ("Apport", "Au plus la moitié des besoins pendant plus d'une semaine"),
            ("Autre apport", "Toute baisse pendant plus de deux semaines"),
            ("Assimilation", "Maladie digestive chronique qui gêne l'absorption"),
            ("Inflammation", "Maladie aiguë grave ou maladie chronique inflammatoire"),
        ],
        1,
    )
    d["def"].table(
        "Gravité phénotypique, stades lus en 2019",
        [
            ("Stade modéré, poids", "5 à 10 pour cent en six mois, ou 10 à 20 pour cent au-delà"),
            ("Stade sévère, poids", "Plus de 10 pour cent en six mois, ou plus de 20 pour cent au-delà"),
            ("Stade modéré, indice", "Moins de 20 avant 70 ans, ou moins de 22 à partir de 70 ans"),
            ("Stade sévère, indice", "Moins de 18,5 avant 70 ans, ou moins de 20 à partir de 70 ans"),
            ("Muscle modéré", "Déficit léger à modéré selon la méthode validée"),
            ("Muscle sévère", "Déficit sévère selon la méthode validée"),
            ("Rôle de l'étiologie", "Elle guide le traitement, elle ne grade pas la sévérité"),
        ],
        1,
    )
    d["def"].a("Quatre classes étiologiques sont nommées dans le même rapport de 2019.", 1)
    d["def"].a("Maladie chronique avec inflammation.", 1)
    d["def"].a("Maladie chronique avec inflammation minime ou non perçue.", 1)
    d["def"].a("Maladie aiguë ou blessure avec inflammation sévère.", 1)
    d["def"].a("Jeûne, y compris la faim liée à un manque social ou d'environnement.", 1)
    d["def"].a("La cachexie entre dans la classe inflammatoire chronique, sans effacer son nom propre.", 1)
    d["def"].a("Le tableau diagnostique de 2019 écrit un indice inférieur à 22 seulement si l'âge est supérieur à 70 ans.", 1)
    d["def"].a("Le tableau de gravité du même rapport écrit ce repère à partir de 70 ans, signe supérieur ou égal.", 1)
    d["def"].a("À 70 ans pile, le tableau diagnostique ne formule donc pas la borne, et le cours ne l'invente pas.", 1)
    d["def"].a("Pour l'Asie, le même tableau diagnostique écrit un indice inférieur à 18,5 avant 70 ans, ou inférieur à 20 au-delà de 70 ans.", 1)
    d["def"].a("Ce repère asiatique n'est pas le repère utilisé pour une personne suivie en Suisse.", 1)
    d["def"].a(f"Le {W()} place la force avant la masse, parce que la force prédit mieux le devenir.", 2)
    d["def"].a("Sarcopénie probable : force basse seule.", 2)
    d["def"].a("Sarcopénie confirmée : force basse et quantité ou qualité musculaire basse.", 2)
    d["def"].a("Sarcopénie sévère : le tableau confirmé plus une performance physique basse.", 2)
    d["def"].a("Le chemin clinique se lit trouver, mesurer, confirmer, grader.", 2)

    d["epi"].a(f"La recommandation {E()} de 2022 vise en général les personnes de 65 ans ou plus.", 3)
    d["epi"].a("La prévalence de la dénutrition y est en général inférieure à 10 pour cent chez qui vit seul.", 3)
    d["epi"].a("Elle monte jusqu'à deux tiers des personnes âgées hospitalisées, dans la même synthèse.", 3)
    d["epi"].a("Ces deux chiffres ne décrivent pas la sarcopénie.", 3)
    d["epi"].a("Mains Libres, texte de 2020, situe la sarcopénie entre 6 et 22 pour cent après 65 ans.", 5)
    d["epi"].a("La revue suisse de 2021 donne 9,9 à 40,4 pour cent dans des populations à risque, selon la définition.", 4)
    d["epi"].a("En Suisse, la même revue estime 26,3 pour cent des femmes et 28 pour cent des hommes.", 4)
    d["epi"].a("Cette estimation suisse repose sur la force, dans un groupe d'âge moyen de 84 ans.", 4)
    d["epi"].a("On ne moyenne pas ces fourchettes : les populations et les définitions diffèrent.", 4)
    d["epi"].a("Aucune des sources lues ne donne la part suisse de chacun des dix tableaux du cours.", 4)
    d["epi"].a("Le dépistage concerne aussi les personnes en surpoids ou obèses.", 3)
    d["epi"].a("Une obésité n'écarte ni la dénutrition ni la sarcopénie.", 4)

    d["phy"].a("Avec l'âge, la dépense de repos baisse surtout parce que la masse maigre baisse.", 3)
    d["phy"].a("L'anorexie liée à l'âge réduit l'apport avant même une maladie aiguë.", 3)
    d["phy"].a("L'inflammation coupe l'appétit et augmente la dépense et la fonte musculaire.", 1)
    d["phy"].a("La synthèse des protéines musculaires ne suit plus l'apport si l'énergie manque.", 3)
    d["phy"].a("Le muscle perd aussi de la qualité, pas seulement du volume.", 2)
    d["phy"].a("La force baisse peut précéder la baisse de masse visible.", 2)
    d["phy"].a("Une inflammation passagère et légère ne suffit pas au critère étiologique de 2019.", 1)
    d["phy"].a("L'infection grave, la brûlure, le trauma et le traumatisme crânien portent une inflammation aiguë forte.", 1)
    d["phy"].a("Cancer, bronchopneumopathie, insuffisance cardiaque et maladie rénale portent une inflammation chronique.", 1)
    d["phy"].a("La dysphagie, les nausées, la diarrhée et la douleur abdominale gênent l'apport ou l'assimilation.", 1)
    d["phy"].a("La revue de 2021 rappelle le rôle de l'immobilité et de la maladie chronique sur le muscle.", 4)

    d["dem"].a("Le premier temps est un dépistage valide, pas un diagnostic.", 1)
    d["dem"].a(f"À l'hôpital, l'outil de 2003, reproduit dans l'annexe du rapport de 2019, commence par quatre questions.", 1)
    d["dem"].a("Indice inférieur à 20,5, perte de poids en trois mois, apport réduit dans la semaine, maladie sévère.", 1)
    d["dem"].a("Une seule réponse oui ouvre le tableau complet.", 1)
    d["dem"].a("Le total additionne l'état nutritionnel, la gravité de la maladie, et un point à partir de 70 ans.", 1)
    d["dem"].a("Un total d'au moins 3 déclenche un plan nutritionnel.", 1)
    d["dem"].a("Un total inférieur à 3 conduit à répéter le dépistage chaque semaine.", 1)
    d["dem"].a("Une cirrhose en soins intensifs prend le grade 3 de maladie, pas le grade 1.", 1)
    d["dem"].table(
        "État nutritionnel du tableau de 2003",
        [
            ("Grade 0", "État nutritionnel habituel"),
            ("Grade 1", "Perte de plus de 5 pour cent en trois mois, ou apport de 50 à 75 pour cent"),
            ("Grade 2", "Perte de plus de 5 pour cent en deux mois, ou indice 18,5 à 20,5 avec état général altéré"),
            ("Grade 2, apport", "Apport de 25 à 60 pour cent de l'habituel dans la semaine précédente"),
            ("Grade 3", "Perte de plus de 5 pour cent en un mois, ou plus de 15 pour cent en trois mois"),
            ("Grade 3, indice", "Indice inférieur à 18,5 avec état général altéré"),
            ("Grade 3, apport", "Apport de 0 à 25 pour cent dans la semaine précédente"),
        ],
        1,
    )
    d["dem"].table(
        "Gravité de maladie du tableau de 2003, lue dans l'annexe de 2019",
        [
            ("Grade 1", "Fracture de hanche, complication d'une maladie chronique, dialyse, diabète, cancer"),
            ("Grade 2", "Chirurgie abdominale majeure, accident vasculaire, pneumonie sévère, hémopathie"),
            ("Grade 3", "Traumatisme crânien, greffe de moelle, soins intensifs avec gravité supérieure à 10"),
        ],
        1,
    )
    d["dem"].a(f"Chez la personne âgée, le formulaire {M()} court est le dépistage le plus cité en 2022.", 3)
    d["dem"].a("Le guide d'octobre 2021 classe 12 à 14 comme normal, 8 à 11 comme risque, 0 à 7 comme dénutrition.", 7)
    d["dem"].a("La validation révisée donne les mêmes trois classes, lues sur la page de Kaiser et collaborateurs.", 8)
    d["dem"].a("Pour la version avec indice, le seuil haut de 11 a une sensibilité de 89,3 pour cent et une spécificité de 81,8 pour cent, article de 2009.", 8)
    d["dem"].a("Le seuil bas de 8 y a une sensibilité de 85,2 pour cent et une spécificité de 94,3 pour cent.", 8)
    d["dem"].a("Avec le mollet à la place de l'indice, les chiffres de 2009 deviennent 90,2 et 76,2 pour cent au seuil de 11.", 8)
    d["dem"].a("Au seuil de 8, cette version au mollet a une sensibilité de 88,3 pour cent et une spécificité de 87,1 pour cent.", 8)
    d["dem"].a("L'article de juin 2001 classe normal à partir de 11, avec une sensibilité de 97,9 pour cent contre le formulaire long.", 9)
    d["dem"].a("La spécificité lue pour cet ancien seuil est de 100 pour cent, et la justesse diagnostique est de 98,7 pour cent.", 9)
    d["dem"].a("On ne mélange pas la sensibilité de 2001 et celle de la validation à trois classes.", 8)
    d["dem"].a(f"Pour le muscle, le {Q()}-F cherche les cas, il ne confirme pas.", 2)
    d["dem"].a("Mains Libres fixe le seuil de détection à 4 points sur 10.", 5)
    d["dem"].a("La revue de 2021 retient une spécificité supérieure à 81,4 pour cent et une valeur prédictive négative supérieure à 92,3 pour cent.", 4)
    d["dem"].a("La valeur prédictive positive y est inférieure à 50 pour cent : un total haut n'est pas un diagnostic.", 4)
    d["dem"].a("Le texte de 2020 donne une valeur prédictive positive de 29 pour cent et une valeur prédictive négative de 93 pour cent.", 5)
    d["dem"].a("Le même texte de 2020 dit qu'une version francophone validée n'existe pas.", 5)
    d["dem"].a("La revue de 2021 dit au contraire que le formulaire est validé en français.", 4)
    d["dem"].a("Les deux phrases restent, parce que les sources ne disent pas la même chose.", 4)

    d["ana"].a("On demande le poids habituel, la date de la perte, et si la perte est voulue.", 1)
    d["ana"].a("Une perte voulue chez une personne obèse peut quand même cacher une dénutrition.", 7)
    d["ana"].a("Le guide de 2021 demande de garder la question de poids même en surpoids, sinon l'outil perd en sensibilité.", 7)
    d["ana"].a("On demande l'appétit sur trois mois, la mastication, la déglutition et les troubles digestifs.", 7)
    d["ana"].a("On demande qui fait les courses, qui cuit, et si les repas sont sautés.", 3)
    d["ana"].a("On demande une chute dans l'année, une lenteur, et la peine à quitter une chaise.", 4)
    d["ana"].a("On demande l'humeur, une tristesse longue, et un diagnostic de démence.", 7)
    d["ana"].a("On demande l'alcool, l'insuline, une chimiothérapie, les antiacides et les diurétiques.", 6)
    d["ana"].a("Ces médicaments entrent dans le deuxième volet du risque de réalimentation.", 6)
    d["ana"].a("On demande depuis combien de jours l'apport est presque nul.", 6)
    d["ana"].a("On demande les dents, la bouche sèche, et les régimes encore imposés.", 3)
    d["ana"].a("Un régime sans sel, sans cholestérol ou de diabète peut réduire l'apport chez la personne âgée.", 3)

    d["exa"].a("On pèse sans chaussures et sans manteau lourd, sur une balance contrôlée.", 7)
    d["exa"].a("On mesure la taille debout, ou la taille de genou, la demi-envergure ou l'envergure si la station est impossible.", 7)
    d["exa"].a("Les œdèmes et l'ascite font monter le poids sans restaurer le muscle.", 1)
    d["exa"].a("On regarde les tempes, les clavicules, les cuisses et les mollets.", 2)
    d["exa"].a("Une personne obèse peut avoir des loges musculaires pauvres : c'est l'obésité sarcopénique.", 4)
    d["exa"].a(f"La force de poigne du {W()} est basse sous 27 kilogrammes chez l'homme.", 2)
    d["exa"].a("Elle est basse sous 16 kilogrammes chez la femme.", 2)
    d["exa"].a("Le lever de chaise est bas si cinq levers dépassent 15 secondes.", 2)
    d["exa"].a("Quinze secondes pile ne dépassent pas ce seuil strict.", 2)
    d["exa"].a("La marche habituelle sur 4 mètres est sévère à une vitesse inférieure ou égale à 0,8 mètre par seconde.", 2)
    d["exa"].a("La revue suisse de 2021 illustre ce repère par plus de 5 secondes pour 4 mètres.", 4)
    d["exa"].a("Quatre mètres en exactement 5 secondes valent 0,8 mètre par seconde, donc le seuil européen est atteint.", 2)
    d["exa"].a("La batterie courte est basse à un total inférieur ou égal à 8 points sur 12.", 2)
    d["exa"].a("Le lever, la marche et le demi-tour sont bas à partir de 20 secondes.", 2)
    d["exa"].a("Le test de 400 mètres est bas s'il n'est pas fini ou s'il dure au moins 6 minutes.", 2)
    d["exa"].a("La masse appendiculaire est basse sous 20 kilogrammes chez l'homme et sous 15 kilogrammes chez la femme.", 2)
    d["exa"].a("Rapportée à la taille au carré, elle est basse sous 7,0 chez l'homme et sous 5,5 chez la femme.", 2)
    d["exa"].a("Le tableau comparatif de 2019 attribue à la cachexie 7,26 et 5,45 : ce n'est pas le même seuil.", 1)
    d["exa"].a("Le tour de mollet inférieur à 31 centimètres peut dépanner là où aucune mesure de masse n'existe.", 2)
    d["exa"].a("Dans la question du formulaire long, guide d'octobre 2021, un mollet inférieur à 31 centimètres cote 0, et 31 ou plus cote 1.", 7)
    d["exa"].a("Quand le mollet remplace l'indice dans le formulaire court, la validation de 2009 passe ce poids de un à trois points, pour garder un total de 14.", 8)
    d["exa"].a("Si le mollet remplace l'indice dans le formulaire court, on ne complète pas le formulaire long.", 7)
    d["exa"].a("Sinon le mollet serait compté deux fois.", 7)
    d["exa"].p.append(cuisse("cuisseA", (150, 90, 95)))

    d["syn"].a("On classe d'abord le danger du jour, puis le mécanisme.", 6)
    d["syn"].a("Le syndrome de réalimentation se cherche avant d'augmenter les calories.", 6)
    d["syn"].a("La fausse route se cherche avant de pousser l'alimentation orale.", 1)
    d["syn"].a("La cachexie cancéreuse se cherche si la perte est rapide et l'inflammation présente.", 1)
    d["syn"].a("La maladie chronique inflammatoire explique une fonte malgré un apport qui semble tenu.", 1)
    d["syn"].a("La démence et la dépression coupent l'apport sans être, à elles seules, le critère inflammatoire.", 1)
    d["syn"].a("La malabsorption se reconnaît à la stéatorrhée, à la diarrhée chronique ou au pancréas.", 1)
    d["syn"].a("L'hyperthyroïdie fait fondre le muscle sans être listée parmi les inflammations types de 2019.", 1)
    d["syn"].a("La carence d'apport pure n'a pas besoin d'une maladie d'organe.", 1)
    d["syn"].a("La sarcopénie primaire reste quand la force et la masse baissent sans ces mécanismes.", 2)
    d["syn"].table(
        "Ordre d'exclusion du motif",
        [
            ("E1", "Syndrome de réalimentation"),
            ("E2", "Dysphagie oropharyngée"),
            ("E3", "Cachexie cancéreuse"),
            ("E4", "Dénutrition inflammatoire chronique"),
            ("E5", "Troubles alimentaires de la démence"),
            ("E6", "Anorexie de la dépression"),
            ("E7", "Malabsorption du sujet âgé"),
            ("E8", "Fonte musculaire endocrinienne"),
            ("E9", "Dénutrition par carence d'apport"),
            ("E10", "Sarcopénie primaire"),
        ],
        1,
    )

    d["dia"].a("Le diagnostic de dénutrition de 2019 est positif seulement si les deux familles de critères sont là.", 1)
    d["dia"].a("Une masse basse sans baisse d'apport et sans maladie ne porte pas seule ce diagnostic.", 1)
    d["dia"].a("Un indice bas sans mécanisme ne le porte pas non plus.", 1)
    d["dia"].a("La gravité se lit sur le phénotype le plus altéré, pas sur l'étiologie.", 1)
    d["dia"].a("Le diagnostic de sarcopénie probable autorise déjà l'exercice et la revue de l'apport.", 2)
    d["dia"].a("La confirmation par absorptiométrie ou impédance ne doit pas retarder ces deux mesures.", 5)
    d["dia"].a("Mains Libres écrit que la mesure de masse confirme quand elle existe, sans être obligatoire pour traiter.", 5)
    d["dia"].a("Le formulaire long, sur la page de validation, classe 24 à 30 comme bien nourri.", 8)
    d["dia"].a("Il classe 17 à 23,5 comme à risque, et 0 à 16,5 comme dénutri.", 8)
    d["dia"].a("Le formulaire court ne remplace pas ce diagnostic étiologique.", 1)
    for nom in DXS:
        d["dia"].a(f"Le tableau nommé {nom} est développé à part, avec ses propres seuils.")

    d["lab"].a("L'albumine n'est pas un critère diagnostique du consensus de 2019.", 1)
    d["lab"].a("Elle baisse dans l'inflammation et ne mesure pas à elle seule les réserves.", 1)
    d["lab"].a("Avant une reprise alimentaire à risque, on lit le potassium, le phosphate et le magnésium.", 6)
    d["lab"].a("La ligne de 2006 ne demande pas de corriger ces valeurs avant de commencer, si l'on supplémente en même temps.", 6)
    d["lab"].a("La protéine C réactive aide à voir l'inflammation, elle ne pose pas le diagnostic nutritionnel.", 1)
    d["lab"].a("La thyrotropine se demande si la fonte semble endocrine et l'apport tenu.", 4)
    d["lab"].a("Une stéatorrhée oriente vers une malabsorption, puis vers le pancréas ou le grêle.", 1)
    d["lab"].a("La vitamine D ne se dose pas pour poser la sarcopénie.", 2)
    d["lab"].a("Elle se discute si une carence osseuse ou une malabsorption est déjà suspectée.", 12)
    d["lab"].a("L'absorptiométrie biphotonique mesure la masse appendiculaire quand le doute musculaire persiste.", 2)
    d["lab"].a("Le scanner ou l'imagerie par résonance ne sont pas un bilan de première ligne au cabinet.", 4)

    d["arb"].a("On écarte d'abord la réalimentation dangereuse, puis la fausse route, puis le cancer rapide.", 6)
    d["arb"].a("Ensuite viennent la maladie inflammatoire, la démence, la dépression, la malabsorption et l'endocrine.", 1)
    d["arb"].a("La carence d'apport et la sarcopénie primaire restent quand ces voies sont négatives.", 2)
    d["arb"].p.append(schema(
        "ori197",
        [
            ("1. Danger", "Avant d'augmenter l'apport", [
                "Réalimentation : indice, jeûne, électrolytes",
                "Fausse route : toux, voix, repas",
                "Perte rapide : chercher un cancer",
            ]),
            ("2. Mécanisme", "Deux familles de critères", [
                "Phénotype : poids, indice, muscle",
                "Étiologie : apport ou inflammation",
                "Force basse : sarcopénie probable",
            ]),
            ("3. Suite", "Traiter sans attendre la masse", [
                "Exercice contre résistance",
                "Énergie et protéines ajustées",
                "Revoir à un mois le poids et la force",
            ]),
        ],
    ))

    d["pec"].a(f"Le repère d'énergie de {E()} en 2022 est de 30 kilocalories par kilogramme et par jour.", 3)
    d["pec"].a("Ce repère s'ajuste à l'état nutritionnel, à l'activité, à la maladie et à la tolérance.", 3)
    d["pec"].a("Il ne s'applique pas tel quel au premier jour d'une personne à haut risque de réalimentation.", 6)
    d["pec"].a("Le haut risque de 2006 tient en un critère majeur ou en deux critères mineurs.", 6)
    d["pec"].table(
        "Haut risque de réalimentation, texte de 2006 mis à jour en 2017",
        [
            ("Un seul suffit, indice", "Indice inférieur à 16"),
            ("Un seul suffit, poids", "Perte non voulue de plus de 15 pour cent en trois à six mois"),
            ("Un seul suffit, jeûne", "Apport presque nul depuis plus de dix jours"),
            ("Un seul suffit, ions", "Potassium, phosphate ou magnésium déjà bas"),
            ("Deux requis, indice", "Indice inférieur à 18,5"),
            ("Deux requis, poids", "Perte de plus de 10 pour cent en trois à six mois"),
            ("Deux requis, jeûne", "Apport presque nul depuis plus de cinq jours"),
            ("Deux requis, contexte", "Alcool, insuline, chimiothérapie, antiacides ou diurétiques"),
            ("Départ usuel du haut risque", "Au plus 10 kilocalories par kilogramme et par jour"),
            ("Cas extrême", "5 kilocalories si indice inférieur à 14, ou jeûne négligeable au-delà de quinze jours"),
            ("Montée", "Vers le besoin complet en quatre à sept jours"),
        ],
        6,
    )
    d["pec"].a("Dans le cas extrême, le rythme cardiaque se surveille en continu.", 6)
    d["pec"].a(f"La thiamine orale de l'autorisation 10989, lue dans l'{A()}, va de 200 à 300 mg par jour si les symptômes d'hypovitaminose sont graves.", 11)
    d["pec"].a("La même information prévoit 100 mg tous les deux jours pour des symptômes légers, et 100 mg par jour pour des symptômes modérés.", 11)
    d["pec"].a("Par voie parentérale, les doses quotidiennes peuvent atteindre 200 mg, très lentement si la voie est intraveineuse.", 11)
    d["pec"].a("La ligne de 2006 propose la même fourchette orale de 200 à 300 mg juste avant la reprise et pendant les dix premiers jours.", 6)
    d["pec"].a("Cette prophylaxie n'est pas la phrase d'indication de l'information professionnelle, qui vise l'hypovitaminose.", 11)
    d["pec"].a("Les comprimés à 100 mg contiennent lactose et saccharose : intolérance au galactose ou au fructose, déficit en lactase, malabsorption du glucose et du galactose, déficit en sucrase-isomaltase.", 11)
    d["pec"].a("L'usage chez l'enfant et l'adolescent n'a pas été étudié de façon systématique.", 11)
    d["pec"].a("Pendant la grossesse et l'allaitement, le médicament ne s'utilise qu'en nécessité absolue.", 11)
    d["pec"].a("La recommandation de 2022 est d'au moins un gramme de protéine par kilogramme et par jour, puis un ajustement.", 3)
    d["pec"].a("Le commentaire cite une proposition de 1,0 à 1,2 gramme chez la personne âgée en bonne santé.", 3)
    d["pec"].a("Il cite 1,2 à 1,5 gramme en maladie aiguë ou chronique, sans en faire la phrase graduée.", 3)
    d["pec"].a("Il cite jusqu'à 2,0 grammes par kilogramme en maladie sévère, blessure ou dénutrition.", 3)
    d["pec"].a("Ces grammes supposent que l'énergie suit, sinon les protéines sont brûlées.", 3)
    d["pec"].a("L'exercice contre résistance est le traitement musculaire le mieux appuyé dans les textes de 2020 et de 2021.", 5)
    d["pec"].a("La revue de 2021 écrit que des médicaments sont à l'étude, sans dose à recopier.", 4)
    d["pec"].a(f"Si une carence en vitamine D est avérée, on ouvre l'{A()} de l'autorisation 33481, pas un schéma de sarcopénie.", 12)
    d["pec"].a("Chez l'adulte d'au moins 60 ans, la prophylaxie lue est de 0,2 ml par jour, soit 800 unités internationales.", 12)
    d["pec"].a("Un millilitre de cette solution contient 4000 unités internationales, et 0,1 ml correspond à 400 unités internationales.", 12)
    d["pec"].a("En prophylaxie chez la femme enceinte, 600 unités internationales par jour ne doivent pas être dépassées.", 12)
    d["pec"].a("Pour une carence déjà manifeste, la grossesse autorise jusqu'à 2000 unités internationales par jour, avec surveillance du calcium et du phosphate.", 12)
    d["pec"].a("Un traitement continu au-dessus de 1000 unités internationales par jour exige d'expliquer les signes de surdosage.", 12)
    d["pec"].a("Les boissons recommandées via l'autorité alimentaire européenne, reprises en 2022, sont d'environ 1,6 litre chez la femme et 2,0 litres chez l'homme.", 3)
    d["pec"].a("Le total eau, aliments compris, est de 2,0 litres chez la femme et de 2,5 litres chez l'homme.", 3)
    d["pec"].a("On lève les restrictions alimentaires qui n'ont plus de bénéfice clair.", 3)
    d["pec"].a("La nutrition entérale vient si la bouche ne suffit pas et si le pronostic d'ensemble reste favorable.", 3)
    d["pec"].a("La voie parentérale vient si l'entérale est impossible ou insuffisante, avec la même réserve de pronostic.", 3)

    d["pre"].a("Toute personne âgée est dépistée, y compris en surpoids, avec un outil valide.", 3)
    d["pre"].a("En établissement stable, le rythme lu en 2022 est d'environ tous les trois mois.", 3)
    d["pre"].a("Au cabinet, le rythme lu est d'au moins une fois par an.", 3)
    d["pre"].a("Le guide de 2021 ajoute un passage à chaque changement clinique.", 7)
    d["pre"].a("On profite d'une chute, d'une hospitalisation ou d'une plainte de faiblesse.", 4)
    d["pre"].a("Un dépistage systématique de la seule sarcopénie n'est pas réclamé par le texte de 2020.", 5)
    d["pre"].a("Le dépistage ciblé, lui, est recommandé après 65 ans en cas de chute ou de peine à marcher, se lever ou monter.", 5)
    d["pre"].a("L'activité contre résistance et un apport suffisant sont la prévention lue, pas un médicament.", 4)
    d["pre"].a("Les soignants et les proches reçoivent une information nutritionnelle simple.", 3)

    d["cle"].a("Deux familles de critères pour la dénutrition, force d'abord pour la sarcopénie.", 1)
    d["cle"].a("Un formulaire positif n'est pas un diagnostic.", 7)
    d["cle"].a("On traite la force basse avant le résultat de masse.", 5)
    d["cle"].a("On ne démarre pas à 30 kilocalories par kilogramme si le haut risque de réalimentation est là.", 6)
    d["cle"].a("La thiamine suit l'information 10989, et la ligne de 2006 en précise le moment.", 11)
    d["cle"].a("L'albumine ne pose pas le diagnostic.", 1)
    d["cle"].a("Les fourchettes de prévalence ne se moyennent pas.", 4)
    d["cle"].a("Les seuils 7,0 et 5,5 ne sont pas les seuils 7,26 et 5,45.", 2)

    d["pie"].a("Piège : appeler sarcopénie toute perte de poids.", 2)
    d["pie"].a("Piège : attendre l'imagerie pour prescrire l'exercice et revoir l'assiette.", 5)
    d["pie"].a("Piège : rassurer parce que l'indice est au-dessus de 25.", 4)
    d["pie"].a("Piège : utiliser l'albumine comme seuil de dénutrition.", 1)
    d["pie"].a("Piège : copier 30 kilocalories par kilogramme le premier jour d'un jeûne long.", 6)
    d["pie"].a("Piège : citer une dose de vitamine D qui n'est pas dans l'autorisation 33481.", 12)
    d["pie"].a("Piège : prendre la sensibilité de 2001 pour les trois classes actuelles.", 9)
    d["pie"].a("Piège : croire qu'un total de questions inférieur à 4 exclut une force basse dans tous les textes.", 5)
    d["pie"].a("Le texte de 2020 dit qu'un total inférieur à 4 rend la sarcopénie très peu probable, sans être une preuve de force normale.", 5)
    d["pie"].a("Cas corrigé. Une femme de 84 ans a un indice à 27 et une force à 14 kilogrammes.", 2)
    d["pie"].a("La première idée, une nutrition rassurante parce que l'indice est confortable, est fausse.", 4)
    d["pie"].a("La force est sous 16 kilogrammes, le lever dépasse 15 secondes, la marche de 4 mètres dépasse 5 secondes.", 2)
    d["pie"].a("Si la masse est basse, la sarcopénie est confirmée et sévère.", 2)
    d["pie"].a("Sans baisse d'apport et sans maladie, le consensus de dénutrition de 2019 n'est pas rempli.", 1)
    d["pie"].a("On commence l'exercice et on vérifie l'assiette, sans attendre un médicament.", 4)
    return d


def imc(p: dict) -> float:
    return p["kg"] / (p["m"] ** 2)


def vitesse(p: dict) -> float:
    return 4.0 / p["marche"]


def haut_risque(p: dict) -> str:
    majeurs = []
    if imc(p) < 16:
        majeurs.append("indice inférieur à 16")
    if p["perte"] > 15 and 3 <= p["delai"] <= 6:
        majeurs.append("perte de plus de 15 pour cent en trois à six mois")
    if p.get("jeun", 0) > 10:
        majeurs.append("jeûne de plus de dix jours")
    if p.get("ions_bas"):
        majeurs.append("ion déjà bas")
    mineurs = []
    if imc(p) < 18.5:
        mineurs.append("indice inférieur à 18,5")
    if p["perte"] > 10 and 3 <= p["delai"] <= 6:
        mineurs.append("perte de plus de 10 pour cent")
    if p.get("jeun", 0) > 5:
        mineurs.append("jeûne de plus de cinq jours")
    if p.get("tox"):
        mineurs.append("alcool ou médicament listé")
    if majeurs:
        return "majeur"
    if len(mineurs) >= 2:
        return "mineur"
    return "non"


def raconter(p: dict, S: Sig, sac: Sac) -> None:
    glim = S("GLIM", "Global Leadership Initiative on Malnutrition", "consensus de dénutrition de 2019")
    ewg = S("EWGSOP2", "European Working Group on Sarcopenia in Older People, révision 2", "groupe européen sarcopénie, révision de 2019")
    qui = "Elle" if p["sexe"] == "f" else "Il"
    base_a = sac.a

    def a(phrase: str, src: int | None = None) -> None:
        texte = phrase.strip()
        if not texte.startswith(p["prenom"]):
            texte = f"{p['prenom']} : {texte[0].lower()}{texte[1:]}" if texte else texte
        base_a(texte, src)

    a(f"{p['prenom']} a {p['age']} ans et consulte en {p['lieu']}.")
    a(f"Le poids est de {p['kg']} kilogrammes pour {n2(p['m'])} mètres.")
    a(f"L'indice vaut {n1(imc(p))} kilogrammes par mètre carré.")
    a(f"La perte déclarée est de {p['perte']} pour cent sur {p['delai']} mois.", 1)
    pheno = []
    if p["delai"] <= 6 and p["perte"] > 5:
        pheno.append("la perte dépasse 5 pour cent en six mois")
    if p["delai"] > 6 and p["perte"] > 10:
        pheno.append("la perte dépasse 10 pour cent au-delà de six mois")
    if p["age"] < 70 and imc(p) < 20:
        pheno.append("l'indice est inférieur à 20 avant 70 ans")
    if p["age"] > 70 and imc(p) < 22:
        pheno.append("l'indice est inférieur à 22 au-delà de 70 ans dans le tableau diagnostique")
    if p["masse"] == "basse":
        pheno.append("la masse musculaire est basse")
    if pheno:
        a(f"Phénotype de {glim} : {pheno[0]}.", 1)
    else:
        a(f"Aucun phénotype de {glim} n'est rempli par le poids, l'indice ou la masse connue.", 1)
    etio = []
    if p["apport"] in ("moitie", "quart", "nul"):
        etio.append("l'apport est réduit")
    if p.get("malabsorption"):
        etio.append("l'assimilation digestive est en cause")
    if p.get("inflam"):
        etio.append("une maladie inflammatoire chronique est présente")
    if etio and pheno:
        a(f"Étiologie présente : {etio[0]}.", 1)
        a("Le diagnostic de dénutrition de 2019 est donc tenu pour ce récit.", 1)
    elif pheno and not etio:
        a("Le phénotype seul ne suffit pas : l'étiologie d'apport ou d'inflammation manque.", 1)
    elif etio and not pheno:
        a("L'étiologie seule ne suffit pas : le phénotype de 2019 manque.", 1)
    else:
        a("Ni le phénotype ni l'étiologie de 2019 ne sont réunis.", 1)
    seuil_f = 16 if p["sexe"] == "f" else 27
    if p["force"] < seuil_f:
        a(f"La force à {p['force']} kilogrammes est sous le seuil de {seuil_f} kilogrammes lu en 2019.", 2)
    else:
        a(f"La force à {p['force']} kilogrammes n'est pas sous le seuil de {seuil_f} kilogrammes.", 2)
    if p["chaise"] > 15:
        a(f"Cinq levers en {p['chaise']} secondes dépassent le seuil de 15 secondes.", 2)
    else:
        a(f"Cinq levers en {p['chaise']} secondes ne dépassent pas 15 secondes.", 2)
    vit = vitesse(p)
    if vit <= 0.8:
        a(f"Quatre mètres en {p['marche']} secondes donnent {n2(vit)} mètre par seconde, au seuil sévère de 0,8.", 2)
    else:
        a(f"Quatre mètres en {p['marche']} secondes donnent {n2(vit)} mètre par seconde, au-dessus de 0,8.", 2)
    force_basse = p["force"] < seuil_f or p["chaise"] > 15
    if force_basse and p["masse"] == "basse" and vit <= 0.8:
        a(f"Lecture {ewg} : sarcopénie sévère, car la performance est basse.", 2)
    elif force_basse and p["masse"] == "basse":
        a("La sarcopénie est confirmée, sans le grade sévère de performance.", 2)
    elif force_basse:
        a("La sarcopénie est probable, et la masse n'est pas encore confirmée basse.", 2)
    else:
        a("La force et le lever n'ouvrent pas la sarcopénie sur ces seuls chiffres.", 2)
    if p["sarcf"] >= 4:
        a(f"Le questionnaire à {p['sarcf']} points atteint le seuil de 4 lu en 2020, sans confirmer le diagnostic.", 5)
    else:
        a(f"Le questionnaire à {p['sarcf']} points reste sous 4, ce qui rend le tableau musculaire moins probable.", 5)
    if p["mna"] <= 7:
        a(f"Le formulaire court à {p['mna']} points est dans la classe dénutrie de 0 à 7, guide de 2021.", 7)
    elif p["mna"] <= 11:
        a(f"Le formulaire court à {p['mna']} points est dans la classe à risque de 8 à 11.", 7)
    else:
        a(f"Le formulaire court à {p['mna']} points est dans la classe normale de 12 à 14.", 7)
    risque = haut_risque(p)
    if risque == "majeur":
        a("Le haut risque de réalimentation est atteint par un critère majeur du texte de 2006.", 6)
        if imc(p) < 14 or p.get("jeun", 0) > 15:
            a("Le départ extrême est de 5 kilocalories par kilogramme, avec surveillance du rythme.", 6)
        else:
            a("Le départ est d'au plus 10 kilocalories par kilogramme et par jour, pas le repère de 30.", 6)
        a("La thiamine orale de 200 à 300 mg par jour se discute selon l'autorisation 10989 et le moment décrit en 2006.", 11)
    elif risque == "mineur":
        a("Deux critères du second volet de 2006 sont réunis : le départ prudent s'impose.", 6)
    else:
        a("Le cadre de haut risque de 2006 n'est pas réuni sur les chiffres donnés.", 6)
        a("Le repère de 30 kilocalories par kilogramme peut alors servir de point de départ ajustable, texte de 2022.", 3)
    def src_libre(texte: str) -> int | None:
        if "kilocal" in texte and "30" in texte:
            return 3
        if "kilocal" in texte or "thiamine" in texte:
            return 6
        if MOTS.search(texte) and re.search(r"\d", texte):
            return 1
        return None

    a(f"La conduite du jour pour {p['prenom']} : {p['geste']}.", src_libre(p["geste"]))
    a(f"L'idée fausse à corriger : {p['faux']}.", src_libre(p["faux"]))
    a(f"Lecture retenue : {p['juste']}.", src_libre(p["juste"]))
    a(f"{qui} est revu sur le poids, la force et l'apport, sans clore le dossier au premier indice.", 3)


PATIENTS = [
    dict(prenom="Marie", age=84, sexe="f", kg=68, m=1.58, perte=2, delai=6, apport="normal", force=14, chaise=18, marche=7, sarcf=6, mna=12, masse="basse", lieu="au cabinet", jeun=0, geste="commencer l'exercice et vérifier l'assiette, sans étiquette de dénutrition", faux="l'indice à 27 rassure", juste="sarcopénie sévère sans critère étiologique de dénutrition", dx=1),
    dict(prenom="Paul", age=79, sexe="h", kg=58, m=1.75, perte=8, delai=4, apport="moitie", force=32, chaise=12, marche=4, sarcf=2, mna=8, masse="inconnue", lieu="à domicile", jeun=2, geste="restaurer l'apport oral et revoir les courses", faux="une force conservée écarte toute dénutrition", juste="dénutrition par carence d'apport, sarcopénie non ouverte par la force", dx=2),
    dict(prenom="Jean", age=81, sexe="h", kg=70, m=1.72, perte=7, delai=5, apport="moitie", force=24, chaise=16, marche=6, sarcf=5, mna=7, masse="basse", lieu="en gériatrie", jeun=1, inflam=True, geste="traiter l'insuffisance cardiaque et soutenir muscle et apport", faux="la maladie cardiaque suffit à ignorer le muscle", juste="dénutrition inflammatoire et sarcopénie sévère ensemble", dx=3),
    dict(prenom="Anne", age=76, sexe="f", kg=52, m=1.64, perte=12, delai=3, apport="quart", force=12, chaise=20, marche=8, sarcf=8, mna=5, masse="basse", lieu="en oncologie", jeun=4, inflam=True, geste="chercher l'obstacle digestif et soutenir sans banaliser la perte", faux="toute perte de cancer est une simple anorexie", juste="cachexie cancéreuse avec sarcopénie sévère", dx=4),
    dict(prenom="Louis", age=88, sexe="h", kg=61, m=1.70, perte=6, delai=2, apport="nul", force=20, chaise=17, marche=9, sarcf=7, mna=6, masse="inconnue", lieu="après un accident vasculaire ancien", jeun=3, geste="sécuriser la déglutition avant d'épaissir ou de pousser les bouchées", faux="une toux à table est un simple rhume", juste="dysphagie oropharyngée avec apport nul et sarcopénie probable", dx=5),
    dict(prenom="Henri", age=83, sexe="h", kg=74, m=1.78, perte=9, delai=4, apport="moitie", force=29, chaise=14, marche=5, sarcf=3, mna=9, masse="normale", lieu="au cabinet", jeun=0, geste="traiter la dépression et faire reprendre les repas", faux="une force normale signifie que l'humeur n'y est pour rien", juste="anorexie de la dépression avec dénutrition, sans sarcopénie confirmée", dx=6),
    dict(prenom="Alice", age=90, sexe="f", kg=48, m=1.55, perte=11, delai=5, apport="quart", force=10, chaise=22, marche=10, sarcf=9, mna=4, masse="basse", lieu="en établissement", jeun=1, geste="adapter l'aide au repas et protéger la dignité", faux="la démence interdit toute nutrition", juste="troubles alimentaires de la démence avec sarcopénie sévère", dx=7),
    dict(prenom="Simon", age=77, sexe="h", kg=49, m=1.80, perte=18, delai=4, apport="nul", force=26, chaise=16, marche=6, sarcf=4, mna=3, masse="basse", lieu="aux urgences", jeun=12, geste="thiamine et départ à au plus 10 kilocalories par kilogramme", faux="il faut rattraper vite avec le repère de 30 kilocalories", juste="syndrome de réalimentation à haut risque, critère majeur d'indice", dx=8),
    dict(prenom="Jules", age=72, sexe="h", kg=60, m=1.73, perte=9, delai=8, apport="normal", force=28, chaise=13, marche=4.5, sarcf=1, mna=10, masse="inconnue", lieu="en gastroentérologie", jeun=0, malabsorption=True, geste="confirmer la stéatorrhée et compenser l'assimilation", faux="un apport déclaré normal ferme le dossier", juste="malabsorption avec phénotype d'indice, force non basse", dx=9),
    dict(prenom="Denis", age=80, sexe="h", kg=67, m=1.76, perte=4, delai=6, apport="normal", force=23, chaise=16, marche=6, sarcf=5, mna=11, masse="basse", lieu="au cabinet", jeun=0, geste="doser la thyrotropine et traiter l'hormone avant de conclure à l'âge", faux="toute fonte après 80 ans est primaire", juste="fonte endocrinienne avec sarcopénie sévère, dénutrition non affirmée", dx=10),
    dict(prenom="Claire", age=69, sexe="f", kg=50, m=1.62, perte=6, delai=3, apport="moitie", force=18, chaise=11, marche=4, sarcf=2, mna=8, masse="normale", lieu="au cabinet", jeun=1, geste="utiliser le seuil d'indice d'avant 70 ans et restaurer l'apport", faux="le seuil de 22 s'applique déjà à 69 ans", juste="dénutrition modérée par l'indice inférieur à 20, force de femme conservée", dx=2),
    dict(prenom="Michel", age=86, sexe="h", kg=92, m=1.70, perte=3, delai=6, apport="normal", force=25, chaise=16, marche=6, sarcf=4, mna=12, masse="basse", lieu="après une chute", jeun=0, geste="nommer l'obésité sarcopénique et prescrire la résistance", faux="l'indice au-dessus de 30 protège le muscle", juste="sarcopénie sévère avec obésité, sans dénutrition de 2019", dx=1),
]


def ilots_de(sacs: dict[str, Sac], ordre: list[str], titres: list[str], iles: list[str]) -> list[tuple[str, str, str]]:
    out = []
    for cle, titre, ile in zip(ordre, titres, iles):
        out.append((titre, ile, sacs[cle].html()))
    return out


TITRES = [
    "1. Définition",
    "2. Épidémiologie",
    "3. Physiopathologie",
    "4. Démarche diagnostique",
    "5. Anamnèse et drapeaux rouges",
    "6. Examen physique",
    "7. Approche syndromique",
    "8. Diagnostic positif",
    "9. Examens complémentaires",
    "10. Arbre décisionnel",
    "11. Prise en charge",
    "12. Prévention",
    "13. Points clés",
    "14. Pièges et cas",
]
ORDRE = "def epi phy dem ana exa syn dia lab arb pec pre cle pie".split()
ILES = [
    "La dénutrition de 2019 exige un critère phénotypique et un critère étiologique. La sarcopénie de 2019 commence par la force, puis la masse, puis la performance si elle est sévère. Les deux noms peuvent coexister. Le détail des seuils de 2019 est dans la fenêtre.",
    "Chez qui vit seul, la dénutrition lue en 2022 reste en général sous 10 pour cent. Elle monte jusqu'à deux tiers des personnes âgées hospitalisées. La sarcopénie suisse estimée en 2021 n'est pas ce chiffre. On ne moyenne pas des populations différentes.",
    "L'âge baisse la dépense de repos parce que la masse maigre baisse, texte de 2022. L'inflammation coupe l'appétit et accélère la fonte. Une inflammation passagère et légère ne remplit pas le critère étiologique de 2019.",
    "On dépiste avec un outil valide, puis on confirme. À l'hôpital, un total d'au moins 3 sur l'outil de 2003 ouvre un plan, d'après l'annexe de 2019. Chez la personne âgée, le formulaire court de 2021 classe 0 à 7, 8 à 11 et 12 à 14. Le danger du jour passe avant le score.",
    "On date la perte de poids et on demande si elle est voulue. On demande l'appétit, la déglutition, les courses, les chutes et l'humeur. L'alcool, l'insuline, la chimiothérapie, les antiacides et les diurétiques comptent pour le risque de 2006.",
    "On pèse, on mesure, on regarde tempes, clavicules, cuisses et mollets. La force est basse sous 27 kilogrammes chez l'homme et sous 16 chez la femme, consensus de 2019. Cinq levers au-delà de 15 secondes et une marche d'au plus 0,8 mètre par seconde complètent la lecture. Le schéma de cuisse est dans la fenêtre.",
    "On écarte d'abord la reprise alimentaire dangereuse et la fausse route. Viennent ensuite le cancer rapide, la maladie inflammatoire, la démence, la dépression, la malabsorption et l'hormone. La carence d'apport et la sarcopénie primaire restent quand ces voies sont négatives.",
    "Le diagnostic de dénutrition de 2019 est tenu seulement si les deux familles sont présentes. La gravité se lit sur le phénotype, pas sur l'étiologie. Une force basse autorise déjà l'exercice, sans attendre la masse, texte de 2020.",
    "L'albumine n'est pas un critère de 2019. Avant une reprise à risque, on lit potassium, phosphate et magnésium, ligne de 2006. La thyrotropine se discute si la fonte semble endocrine. La vitamine D se lit sur l'autorisation 33481, pas pour poser la sarcopénie.",
    "L'algorithme commence par le haut risque de réalimentation, puis la fausse route, puis la perte rapide. Le schéma interactif de la fenêtre suit cet ordre. On ne saute pas une étape parce que l'indice paraît simple.",
    "Le repère d'énergie de 2022 est de 30 kilocalories par kilogramme, ajusté, et jamais au premier jour d'un haut risque. Le départ du haut risque de 2006 est d'au plus 10 kilocalories par kilogramme. La protéine recommandée est d'au moins un gramme par kilogramme. La thiamine suit l'autorisation 10989.",
    "On dépiste aussi les personnes en surpoids. En établissement stable, le rythme de 2022 est d'environ trois mois. Au cabinet, il est d'au moins une fois par an. Le dépistage musculaire ciblé suit une chute ou une peine à se lever.",
    "Force d'abord. Deux familles de critères pour la dénutrition. Pas de rattrapage calorique aveugle. Un formulaire positif n'est pas un diagnostic. Les seuils 7,0 et 5,5 de 2019 ne sont pas les seuils 7,26 et 5,45 de la ligne cachexie.",
    "Le piège type est l'indice confortable avec une force basse. Une femme de 84 ans peut être sarcopénique sévère sans remplir la dénutrition de 2019. On commence l'exercice et on vérifie l'assiette. Le cas corrigé est dans la fenêtre.",
]


def assembler(titre: str, sous: str, essentiel: str, sacs: dict, iles: list[str], fin: str) -> str:
    return page(titre, sous, essentiel, ilots_de(sacs, ORDRE, TITRES, iles), fin, sources_html())


def jusqua(sacs: dict, bas: int, haut: int, fabrique, **kw) -> None:
    i = 0
    while i < 400:
        html = fabrique()
        y = taille_xy.mesurer(html).y[1]
        if bas <= y <= haut:
            return
        if y > haut:
            raise SystemExit(f"trop long y={y} cible {bas}-{haut}")
        sec, texte, src = grilles.phrase_pad(kw["n"], i, kw["nom"])
        sacs[sec].a(texte, src)
        i += 1
    raise SystemExit("pad épuisé")


def construire_phase_a() -> str:
    S = Sig()
    sacs = criteres(S)
    grilles.completer_a(sacs)
    cibles = ["dem", "dia", "pec", "pie"]
    for i, p in enumerate(PATIENTS):
        raconter(p, S, sacs[cibles[i % 4]])

    def fabrique() -> str:
        return assembler(
            "Malnutrition et sarcopénie",
            "Situation de départ O3.3, personne âgée. Le détail chiffré est dans la fenêtre Sources.",
            "On protège la reprise alimentaire et la déglutition, puis on sépare dénutrition et sarcopénie.",
            sacs,
            ILES,
            "FIN_FICHIER LOT_197_Phase_A_V0.html",
        )

    jusqua(sacs, 72000, 79000, fabrique, n=0, nom="le motif")
    return fabrique()


FOCUS = {
    1: "La sarcopénie primaire se retient quand la force est basse et qu'aucune maladie ne porte la fonte.",
    2: "La carence d'apport se retient quand le phénotype de 2019 a pour étiologie la seule baisse des repas.",
    3: "L'inflammation chronique explique une fonte même quand l'assiette paraît à peu près tenue.",
    4: "La cachexie cancéreuse est une perte grasse et maigre, tirée par la tumeur, souvent avec sarcopénie.",
    5: "La dysphagie se traite comme un danger de fausse route avant d'augmenter les bouchées.",
    6: "La dépression coupe les repas. Elle n'est pas, à elle seule, le critère inflammatoire de 2019.",
    7: "La démence gêne l'initiation, la poursuite et la sécurité du repas, avec une aide qui respecte la personne.",
    8: "Le syndrome de réalimentation se prévient en ralentissant les calories et en donnant la thiamine lue.",
    9: "La malabsorption garde un apport déclaré parfois normal, avec une assimilation qui ne suit pas.",
    10: "La fonte endocrinienne, surtout thyroïdienne, se traite par l'hormone, pas par l'étiquette d'âge.",
}


CIBLES_Y = {
    1: (38000, 41000),
    2: (43000, 46000),
    3: (37500, 39500),
    4: (40000, 43000),
    5: (44500, 46000),
    6: (37000, 39500),
    7: (41500, 44500),
    8: (38200, 40500),
    9: (42500, 45500),
    10: (39000, 42000),
}


def construire_dx(n: int) -> str:
    S = Sig()
    sacs = criteres(S)
    nom = DXS[n - 1]
    sacs["def"].p.insert(0, f"<p>Ce chapitre développe le tableau {nom}. Le cours du motif en donne le cadre commun.</p>")
    grilles.chapitre(n, sacs)
    propres = [p for p in PATIENTS if p["dx"] == n]
    cibles = ["dem", "exa", "dia", "pec", "pie"]
    for i, p in enumerate(propres):
        raconter(p, S, sacs[cibles[i % 5]])
    iles = list(ILES)
    iles[0] = (
        f"Le tableau travaillé ici est {nom}. "
        "Les seuils de 2019 restent ceux du consensus, lus dans la fenêtre, sans être réécrits pour ce seul nom."
    )

    def fabrique() -> str:
        return assembler(
            f"DX.{n} — {nom}",
            "Diagnostic différentiel du motif malnutrition et sarcopénie. Le cadre général est celui du cours.",
            FOCUS[n],
            sacs,
            iles,
            f"FIN_FICHIER LOT_197_Phase_B_V0_DX.{n}.html",
        )

    bas, haut = CIBLES_Y[n]
    jusqua(sacs, bas, haut, fabrique, n=n, nom=nom)
    return fabrique()


def ecrire(nom: str, html: str) -> None:
    chemin = LOT / nom
    chemin.write_text(html, encoding="utf-8")
    # inscrire la taille
    import subprocess
    subprocess.check_call([sys.executable, str(RACINE / "harnais/taille_xy.py"), str(chemin), "--inscrire"])
    brut = chemin.read_text(encoding="utf-8")
    verifier_dates(brut)
    sys.path.insert(0, str(RACINE / "harnais"))
    import taille_xy as tx
    m = tx.mesurer(brut)
    print(f"{nom} x={m.x[1]} y={m.y[1]}")


def main() -> None:
    cibles = sys.argv[1:] or ["A"] + [str(i) for i in range(1, 11)]
    if "A" in cibles:
        ecrire("LOT_197_Phase_A_V0.html", construire_phase_a())
    for n in range(1, 11):
        if str(n) in cibles:
            ecrire(f"LOT_197_Phase_B_V0_DX.{n}.html", construire_dx(n))


if __name__ == "__main__":
    main()
