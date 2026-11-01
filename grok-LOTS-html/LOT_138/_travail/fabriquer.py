#!/usr/bin/env python3
"""Leçon V8 LOT_138 F1.9 Troubles cognitifs. N'écrit que sous grok-LOTS-html/LOT_138/."""
from __future__ import annotations

import html
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path("/workspace")
LOT = ROOT / "grok-LOTS-html/LOT_138"
MODELE = ROOT / "harnais/modele_lecon/MODELE_DD_V8.html"
DESSIN = ROOT / "grok-LOTS-html/outils/dessinateur/dessinateur.py"

SIGLES = {
    "MMSE": "Mini-Mental State Examination",
    "IRM": "imagerie par résonance magnétique",
    "TEP": "tomographie par émission de positons",
    "FDG": "fluorodésoxyglucose",
    "EEG": "électroencéphalogramme",
    "CDR": "Clinical Dementia Rating",
    "MCI": "mild cognitive impairment, trouble cognitif léger",
    "DSM": "manuel diagnostique et statistique des troubles mentaux",
    "CIM": "classification internationale des maladies",
    "AIPS": "information professionnelle suisse du corpus local",
    "OFSP": "Office fédéral de la santé publique",
    "SMC": "Swiss Memory Clinics",
    "LCR": "liquide céphalorachidien",
    "TSH": "thyréostimuline",
    "VIH": "virus de l'immunodéficience humaine",
    "SCPD": "symptômes comportementaux et psychologiques de la démence",
    "AIVQ": "activités instrumentales de la vie quotidienne",
    "ABVQ": "activités de base de la vie quotidienne",
    "GDS": "échelle de dépression gériatrique",
    "BDI": "inventaire de dépression de Beck",
    "CERAD": "Consortium to Establish a Registry for Alzheimer's Disease",
    "NOSGER": "Nurses' Observation Scale for Geriatric Patients",
    "IQCODE": "Informant Questionnaire on Cognitive Decline in the Elderly",
    "ASNP": "Association suisse des neuropsychologues",
    "SPECT": "tomographie d'émission monophotonique",
    "CRP": "protéine C réactive",
    "NPI": "inventaire neuropsychiatrique",
    "OPAS": "ordonnance sur les prestations de l'assurance des soins",
    "AMDP": "manuel de documentation de la psychopathologie",
    "CT": "tomodensitométrie, scanner",
    "PROFILES": "catalogue suisse des situations cliniques",
    "PCR": "amplification génique, réaction de polymérisation en chaîne",
}
IGNORER = {"II", "III", "IV", "VI", "DX", "HTML", "CSS", "OK", "LOT", "INDEX"}

CADRES = [
    "{F}.",
    "En pratique, pour {nom}, {f}.",
    "L'erreur serait de contredire ceci : {f}.",
    "On le dit avec des mots simples : {f}.",
    "Le geste suivant dépend de ce constat : {f}.",
    "On ne mélange pas ce constat avec le diagnostic voisin : {f}.",
]


def feuille() -> str:
    brut = MODELE.read_text(encoding="utf-8")
    css = brut[brut.find("<style>") + 7:brut.find("</style>")].strip()
    parts, buf = [], ""
    for chunk in css.split("}"):
        if not chunk.strip():
            continue
        piece = chunk + "}"
        if buf and len(buf) + len(piece) > 1400:
            parts.append(buf)
            buf = piece
        else:
            buf += piece
    if buf:
        parts.append(buf)
    return "\n".join(parts)


def cap(s: str) -> str:
    s = s.strip().rstrip(".")
    return s[0].upper() + s[1:] if s else s


def inline(s: str, bag: set[str]) -> str:
    s = html.escape(s, quote=False)

    def repl(m: re.Match) -> str:
        w = m.group(0)
        if w in IGNORER or w not in SIGLES:
            return w
        if w in bag:
            return w
        bag.add(w)
        titre = html.escape(SIGLES[w], quote=True)
        return f'<abbr title="{titre}">{w}</abbr>'

    return re.sub(r"\b[A-ZÉÈÀ]{2,}[A-Z0-9ÉÈÀ]*\b", repl, s)


def phrase(nom: str, fait: str, i: int) -> str:
    f = fait.strip().rstrip(".")
    F = cap(f)
    cadre = CADRES[i % len(CADRES)]
    s = cadre.format(nom=nom, f=f, F=F)
    s = re.sub(r"\s+", " ", s).strip()
    if not s.endswith("."):
        s += "."
    mots = s.split()
    if len(mots) > 32:
        s = F + "."
        if len(s.split()) > 32:
            s = " ".join(s.split()[:32]).rstrip(".") + "."
    return s


def p(texte: str, ref: int, bag: set[str]) -> str:
    return f"<p>{inline(texte, bag)}<sup class=\"s\">{ref}</sup></p>"


def fenetre(ident: str, titre: str, corps: str) -> str:
    titre = html.escape(titre)
    return (
        f'<div id="{ident}" popover class="fenetre">'
        f'<div class="barre"><span>{titre}</span>'
        f'<button type="button" popovertarget="{ident}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">\n{corps}\n</div></div>'
    )


def bouton(cible: str, libelle: str) -> str:
    return f'<button type="button" class="terme" popovertarget="{cible}">{html.escape(libelle)}</button>'


def ilot(numero, titre, paragraphe, fenetres="", essentiel=False, sommaire=False) -> str:
    if essentiel:
        ident, h, classe = "ess", "L'essentiel", "ilot c essentiel"
    elif sommaire:
        ident, h, classe = "som", titre, "ilot v"
    elif numero == 0:
        ident, h, classe = "sources", titre, "ilot c"
    else:
        couleur = "c" if numero % 2 else "v"
        ident, h, classe = f"p{numero}", f"{numero}. {titre}", f"ilot {couleur}"
    return f'<section class="{classe}"><h2 id="{ident}">{h}</h2>\n<p>{paragraphe}</p>\n{fenetres}</section>\n'


def page(titre_doc, h1, sous, blocs, fin) -> str:
    corps = "\n".join(blocs)
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titre_doc)}</title>
<style>
{feuille()}
.cliche{{border-bottom:1px dashed #6a4a2a;}}
</style>
</head>
<body>
<main>
<h1 id="titre">{html.escape(h1)}</h1>
<p class="taille" id="taille">Taille : en cours de mesure</p>
<p class="sous">{html.escape(sous)}</p>
{corps}
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- {fin} -->
"""


def sigles_inconnus(texte: str) -> list[str]:
    visible = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", texte)
    visible = re.sub(r"<[^>]+>", " ", visible)
    out = []
    for s in re.findall(r"\b[A-ZÉÈÀ]{2,}[A-Z0-9ÉÈÀ]*\b", visible):
        if s in IGNORER or s in SIGLES:
            continue
        if s not in out:
            out.append(s)
    return out


def charger_dessinateur():
    spec = importlib.util.spec_from_file_location("dessinateur_lot138", DESSIN)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def zone(i, nom, definition, cx, cy, rx, ry, fill, stroke, lesion=False):
    return {
        "id": f"z{i}",
        "nom": nom,
        "numero": i,
        "geometrie": {"type": "ellipse", "cx": cx, "cy": cy, "rx": rx, "ry": ry},
        "remplissage": fill,
        "contour": stroke,
        "epaisseur": 2,
        "definition": definition,
        "lesion": lesion,
        "badge": [cx, cy - ry - 28],
    }


def niveau(nid, etiquette, note, structures, defaut=False):
    d = {
        "id": nid,
        "etiquette": etiquette,
        "note": note,
        "viewBox": [0, 0, 1000, 760],
        "repere": {"texte": "D", "x": 70, "y": 70, "titre": "Droite du patient, à gauche du schéma"},
        "structures": structures,
    }
    if defaut:
        d["defaut"] = True
    return d


def fragment_svg(desc: dict) -> str:
    mod = charger_dessinateur()
    police = "../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf"
    frag = mod.rendre(desc, police)
    frag = re.sub(r"(?is)<script[^>]*>.*?</script>", "", frag)
    return frag


def figures() -> dict[str, str]:
    circ = {
        "id": "lot138-circuits",
        "titre": "Trois réseaux à tester avant de nommer une démence",
        "question": {
            "intitule": "Quel réseau interroge-t-on en premier ?",
            "html": "<p>L'attention d'abord. Une mémoire testée chez une personne inattentive ne se lit pas.</p>",
        },
        "sources_courtes": "Schéma pédagogique du 1er novembre 2026. Pas un cliché. Repère D à gauche de l'écran.",
        "niveaux": [
            niveau("attention", "Attention", "Réseau à tester en premier, surtout si le tableau fluctue.", [
                zone(1, "Veille", "La veille se juge avant les questions de mémoire.", 280, 300, 120, 70, "#f4e1c1", "#8a5a2a"),
                zone(2, "Sélection", "L'attention sélective échoue quand la personne ne tient pas la consigne.", 520, 300, 130, 70, "#f7d7a8", "#8a5a2a", True),
                zone(3, "Partage", "L'attention partagée est une fonction exécutive proche.", 740, 300, 110, 70, "#f4e1c1", "#8a5a2a"),
            ], True),
            niveau("memoire", "Mémoire", "Stockage hippocampique : l'indice ne rend pas le souvenir.", [
                zone(1, "Encodage", "L'encodage demande une attention encore tenue.", 280, 320, 120, 80, "#d5e6f5", "#245074"),
                zone(2, "Stockage", "Un défaut de stockage n'est pas réparé par l'indiçage.", 520, 340, 140, 90, "#f3c1c1", "#7a3030", True),
                zone(3, "Rappel", "Le rappel libre bas avec reconnaissance basse oriente vers un oubli de stock.", 760, 320, 110, 80, "#d5e6f5", "#245074"),
            ]),
            niveau("frontal", "Frontal", "Comportement, langage ou planification avant la mémoire.", [
                zone(1, "Inhibition", "La désinhibition se voit dans la conduite, pas dans un total de test.", 300, 300, 130, 80, "#d8f0df", "#1f6b45"),
                zone(2, "Plan", "La planification se juge sur une tâche à plusieurs étapes.", 540, 320, 130, 80, "#f7e7a8", "#6b5a1f", True),
                zone(3, "Langage", "Le manque du mot ou la perte du sens sont des profils différents.", 760, 300, 110, 80, "#d8f0df", "#1f6b45"),
            ]),
        ],
    }
    algo = {
        "id": "lot138-algorithme",
        "titre": "Trois temps du trouble cognitif",
        "question": {
            "intitule": "Quel temps impose quel examen ?",
            "html": "<p>Heures : cause somatique. Semaines : image et humeur. Mois ou années : bilan de clinique de mémoire.</p>",
        },
        "sources_courtes": "Schéma pédagogique du 1er novembre 2026, calé sur la brochure Swiss Memory Clinics 2024. Pas un cliché.",
        "niveaux": [
            niveau("aigu", "Heures", "Installation en heures ou en jours : ne pas poser une démence.", [
                zone(1, "Veille", "Veille fluctuante ou abaissée.", 260, 280, 110, 70, "#f8d0d0", "#7a3030", True),
                zone(2, "Cause", "Médicament, infection, métabolisme, sevrage.", 520, 300, 140, 80, "#f4e1c1", "#8a5a2a"),
                zone(3, "Suite", "Le test neuropsychologique attend la stabilité.", 760, 280, 110, 70, "#d5e6f5", "#245074"),
            ], True),
            niveau("subaigu", "Semaines", "Semaines : image urgente ou humeur, selon les indices.", [
                zone(1, "Trauma", "Chute, anticoagulant, céphalée : penser à l'hématome.", 280, 300, 130, 80, "#f3c1c1", "#7a3030", True),
                zone(2, "Infection", "Fièvre, crise, changement psychique : penser à l'encéphalite.", 540, 300, 130, 80, "#f7d7a8", "#8a5a2a"),
                zone(3, "Humeur", "Plainte forte, début datable, anhédonie : penser à la dépression.", 780, 300, 100, 70, "#d8f0df", "#1f6b45"),
            ]),
            niveau("chronique", "Mois", "Mois ou années : sévérité par les actes du quotidien, puis étiologie.", [
                zone(1, "Léger", "Autonomie gardée : trouble cognitif léger possible.", 280, 300, 120, 75, "#d5e6f5", "#245074"),
                zone(2, "Majeur", "Perte d'un acte instrumental : trouble majeur.", 520, 310, 140, 85, "#f3c1c1", "#7a3030", True),
                zone(3, "Cause", "Profil, image, et parfois liquide ou médecine nucléaire.", 770, 300, 110, 75, "#d8f0df", "#1f6b45"),
            ]),
        ],
    }
    image = {
        "id": "lot138-imagerie",
        "titre": "Trois lectures schématiques, pas des clichés",
        "question": {
            "intitule": "Que montre le schéma, et que ne montre-t-il pas ?",
            "html": "<p>Le croissant, l'hippocampe et le métabolisme sont des repères. Ils ne remplacent pas le compte rendu.</p>",
        },
        "sources_courtes": "Schéma original du 1er novembre 2026. Aucune image de patient. Orientation : D à gauche.",
        "niveaux": [
            niveau("scanner", "Scanner", "Scanner sans injection : masse, hématome sous-dural, hydrocéphalie.", [
                zone(1, "Crâne", "Contour schématique du crâne.", 500, 380, 280, 220, "#e7eef2", "#5c6b73"),
                zone(2, "Cerveau", "Parenchyme. Le schéma ne mesure pas un déplacement réel.", 500, 390, 200, 160, "#f7f1ea", "#8a7a6a"),
                zone(3, "Croissant", "Croissant extra-axial : place habituelle d'un hématome sous-dural sur ce dessin.", 690, 390, 70, 120, "#e07a5f", "#7a3030", True),
            ], True),
            niveau("irm", "IRM", "IRM de base. Le scanner est moins bon pour le siège d'un Alzheimer.", [
                zone(1, "Cortex", "Ruban cortical schématique.", 500, 360, 230, 180, "#f7f1ea", "#8a7a6a"),
                zone(2, "Ventricule", "Ventricule. Une hydrocéphalie se discute avec la clinique.", 500, 390, 70, 90, "#d5e6f5", "#245074"),
                zone(3, "Hippocampe", "Région hippocampique interne, siège souvent regardé. Ce dessin ne cote pas une atrophie.", 620, 470, 55, 35, "#f3c1c1", "#7a3030", True),
            ]),
            niveau("tep", "TEP", "Métabolisme du glucose : le siège suit le phénotype, dit la brochure.", [
                zone(1, "Frontal", "Hypométabolisme frontal : piste fronto-temporale sur ce schéma.", 500, 250, 160, 50, "#f7d7a8", "#8a5a2a", True),
                zone(2, "Pariétal", "Hypométabolisme temporo-pariétal : piste d'Alzheimer sur ce schéma.", 640, 400, 90, 70, "#f3c1c1", "#7a3030", True),
                zone(3, "Occipital", "Atteinte postérieure : piste d'atrophie corticale postérieure ou de Lewy, à confirmer.", 500, 520, 80, 40, "#d8f0df", "#1f6b45"),
            ]),
        ],
    }
    return {
        "circuits": fragment_svg(circ),
        "algorithme": fragment_svg(algo),
        "imagerie": fragment_svg(image),
    }


# Faits courts, minuscule initiale, sans point final. Référence = numéro d'INDEX.
COMMUNS = [
    (1, "les six dimensions du DSM citées en 2024 sont l'attention, l'exécution, la mémoire, le langage, le perceptivo-moteur et la cognition sociale"),
    (1, "le trouble subjectif n'est pas objectivé par la clinique ni par la neuropsychologie"),
    (1, "le trouble cognitif léger est le mild cognitive impairment, ou trouble neurocognitif léger du DSM"),
    (1, "la démence de la brochure est le trouble neurocognitif majeur du DSM"),
    (1, "la forme légère limite les activités instrumentales et laisse les activités de base"),
    (1, "la forme modérée limite aussi les activités de base, par exemple manger ou s'habiller"),
    (1, "la forme sévère est une dépendance totale dans la brochure de 2024"),
    (1, "le z entre un et deux écarts-types correspond au trouble neurocognitif léger dans le texte suisse"),
    (1, "le z inférieur ou égal à −2,0 correspond, dans ce texte, au trouble qu'il appelle sévère sur le plan des tests"),
    (1, "ce seuil de test n'est pas le grade fonctionnel léger, modéré ou sévère"),
    (1, "le MoCA est recommandé pour le test rapide, d'autres outils restent possibles"),
    (1, "le MMSE est peu sensible au début, et le test de l'horloge améliore cette limite"),
    (1, "le DemTect est aussi répandu en Suisse selon la brochure"),
    (1, "la batterie CERAD-Plus est recommandée pour l'examen approfondi"),
    (1, "un test fait pendant une maladie aiguë somatique ou psychique se relit après stabilisation"),
    (1, "l'hétéro-anamnèse des actes du quotidien est indispensable au diagnostic de démence"),
    (1, "les échelles NOSGER et IQCODE sont utilisées en Suisse pour cette hétéro-anamnèse"),
    (1, "le bilan sanguin de base comprend formule, CRP, glucose, ionogramme, calcium corrigé et créatinine"),
    (1, "le bilan de base ajoute les transaminases, la TSH, la vitamine B12 et les folates"),
    (1, "le statut lipidique du bilan de base vise les personnes de moins de 80 ans"),
    (1, "syphilis, borréliose et VIH se discutent seulement si le contexte les rend utiles"),
    (1, "le LCR sert aux formes rapides, atypiques, précoces avant 65 ans, et à l'hydrocéphalie à pression normale"),
    (1, "amyloïde, phospho-tau et tau dans le LCR soutiennent une maladie d'Alzheimer, y compris au stade MCI"),
    (1, "l'IRM cérébrale, ou le scanner si l'IRM est contre-indiquée, fait partie du diagnostic de base"),
    (1, "on privilégie l'IRM chez le sujet jeune ou si l'aggravation est rapide"),
    (1, "une IRM 3 teslas est préférée à 1,5 tesla quand elle est possible"),
    (1, "le scanner sans injection suffit en général pour une masse, un hématome sous-dural ou une hydrocéphalie"),
    (1, "le scanner identifie une démence vasculaire seulement avec des réserves"),
    (1, "le scanner est moins bon pour le siège d'une maladie d'Alzheimer ou une démence sous-corticale"),
    (1, "l'imagerie structurelle seule ne tranche pas entre Alzheimer et forme fronto-temporale"),
    (1, "le Doppler cervical se discute dans la forme vasculaire ou mixte"),
    (1, "la TEP au FDG est l'imagerie nucléaire la mieux validée pour les démences dans cette brochure"),
    (1, "la TEP au FDG est l'imagerie moléculaire de premier choix des maladies neurodégénératives"),
    (1, "la TEP au FDG reste utile au stade du trouble cognitif léger"),
    (1, "la brochure parle d'une sensibilité et d'une spécificité très élevées sans donner de pourcentage"),
    (1, "le remboursement OPAS de la TEP au FDG exige un spécialiste après discussion interdisciplinaire"),
    (1, "ce remboursement demande un âge de 80 ans au maximum et un début depuis cinq ans au plus"),
    (1, "ce remboursement demande un MMSE qui n'est pas inférieur à 10 points"),
    (1, "la TEP amyloïde vise la pathologie amyloïde, pas le type exact de neurodégénérescence"),
    (1, "la TEP amyloïde se discute si le LCR ne conclut pas ou si la ponction est impossible"),
    (1, "la spécificité de la TEP amyloïde baisse avec l'âge, car l'amyloïde existe chez des sujets sans trouble"),
    (1, "l'imagerie dopaminergique pathologique distingue un corps de Lewy d'un Alzheimer à striatum normal"),
    (1, "l'EEG a une place réduite, mais aide si la veille fluctue et qu'une épilepsie est possible"),
    (1, "l'EEG aide aussi si l'on suspecte une encéphalite, une cause métabolique ou une maladie de Creutzfeldt-Jakob"),
    (1, "un score d'Epworth supérieur à 9 points indique une somnolence diurne à explorer"),
    (1, "un trouble du sommeil paradoxal suspecté oriente vers un enregistrement, surtout si Lewy ou Parkinson"),
    (1, "l'annonce du diagnostic fait partie du processus, avec du temps et des mots simples"),
    (1, "la personne a le droit de savoir, sauf renoncement explicite, selon le renvoi de la brochure à l'OFSP"),
    (1, "un syndrome démentiel léger n'élève pas à lui seul le risque d'accident, dit la brochure"),
    (1, "la clinique de mémoire ne fait pas l'examen officiel d'aptitude à la conduite"),
    (1, "la capacité de discernement se juge pour un acte précis et peut changer avec le temps"),
    (1, "on parle tôt du mandat pour cause d'inaptitude et des directives anticipées"),
    (1, "une consultation génétique se discute si un parent du premier degré est atteint avant 50 ans"),
    (1, "elle se discute aussi si deux parents du premier degré sont atteints avant 60 ans"),
    (1, "les symptômes psychiques peuvent précéder la démence et apparaître dès le stade MCI"),
    (1, "la GDS ou le BDI se discutent si une dépression est suspectée et que la démence est encore légère"),
    (2, "la page d'Alzheimer Suisse lue en 2026 estime 166 300 personnes atteintes en Suisse"),
    (2, "la même page estime 35 800 nouveaux cas par an"),
    (2, "elle écrit que 66 pour cent des personnes atteintes sont des femmes"),
    (2, "elle écrit que plus de 8200 personnes sont atteintes avant 65 ans, soit près de 5 pour cent"),
    (2, "elle estime 285 700 personnes atteintes en 2050, l'âge étant le principal facteur de risque"),
    (3, "le rapport de l'OFSP lu en 2026 cite l'estimation Alzheimer Suisse de 2024, environ 156 900 personnes"),
    (3, "on enseigne les deux estimations, 2024 et 2026, sans en fabriquer une moyenne"),
    (4, "le CDR cote six domaines : mémoire, orientation, jugement, vie sociale, foyer et soins personnels"),
    (4, "chaque domaine va de 0 à 3, avec le cran 0,5, sauf les soins personnels qui n'ont pas de 0,5"),
    (4, "le score global du CDR suit un algorithme, et la somme des cases va de 0 à 18"),
    (4, "la brochure suisse de 2024 grade le quotidien, elle n'impose pas le CDR"),
    (13, "le code PROFILES de cette leçon est F1.9, troubles cognitifs"),
]

PAR_DX = {
    1: [
        (1, "le délirium est un trouble aigu et fluctuant, avec inattention, et non une démence qui commence"),
        (1, "on cherche une cause somatique, médicamenteuse ou un sevrage avant de nommer une maladie chronique"),
        (1, "le test neuropsychologique attend que l'état aigu soit stabilisé"),
        (1, "la forme calme et somnolente se manque plus souvent que la forme agitée"),
        (12, "Haldol, numéro 26891, a une indication de délire aigu après échec des moyens non médicamenteux"),
        (12, "la dose orale lue va de 1 à 10 mg par jour, en commençant au plus bas"),
        (12, "si l'agitation persiste, les paliers se font toutes les 2 à 4 heures, sans dépasser 10 mg par jour"),
        (12, "cette information professionnelle ne nomme pas la maladie à corps de Lewy dans cette indication"),
        (1, "lunettes, appareil auditif, lumière du jour, horloge et présence d'un proche précèdent le médicament"),
        (1, "on revoit toute l'ordonnance, surtout les anticholinergiques et les benzodiazépines évitables"),
    ],
    2: [
        (1, "l'hématome sous-dural chronique s'installe souvent en semaines, après un choc minime oublié"),
        (1, "anticoagulant, céphalée, trouble de marche et fluctuation cognitive sont les indices utiles"),
        (1, "le scanner sans injection confirme ou exclut en règle générale un hématome sous-dural"),
        (1, "appeler cela une démence débutante sans image est l'erreur que ce diagnostic corrige"),
        (1, "l'IRM reste possible, mais le scanner répond à la question de la collection extra-axiale"),
        (1, "un croissant sur ce cours est un schéma, pas le compte rendu d'un patient"),
    ],
    3: [
        (10, "Benerva, numéro 10989, a pour indication l'encéphalopathie de Wernicke"),
        (10, "dans cette forme sévère, la voie parentérale peut atteindre 200 mg par jour"),
        (10, "la voie intraveineuse se fait très lentement et reste limitée aux personnes hospitalisées"),
        (10, "la brochure du médicament préfère la voie orale dès que la situation grave le permet"),
        (10, "l'information lue n'écrit pas l'ordre entre glucose et thiamine"),
        (1, "la triade œil, ataxie et confusion est souvent incomplète, donc l'absence d'un signe ne rassure pas"),
        (1, "alcool, dénutrition et chirurgie bariatrique sont les terrains classiques à demander"),
    ],
    4: [
        (11, "Aciclovir Labatec, numéro 60325, a pour indication l'encéphalite à herpes simplex"),
        (11, "chez l'adulte, la dose lue est 10 mg/kg toutes les 8 heures pendant 10 jours"),
        (11, "la perfusion se fait lentement, en une heure"),
        (11, "la fonction rénale change l'intervalle, selon le tableau de l'information professionnelle"),
        (1, "fièvre, céphalée, crise ou changement psychique aigu font démarrer le traitement sans attendre une PCR"),
        (1, "étiqueter une décompensation psychiatrique et différer l'aciclovir est l'erreur principale"),
        (1, "l'EEG peut soutenir une cause inflammatoire, il ne remplace pas le traitement déjà indiqué"),
    ],
    5: [
        (1, "un processus expansif donne un trouble en semaines, avec céphalée, vomissement, crise ou signe focal"),
        (1, "le scanner sans injection confirme ou exclut en règle générale une masse"),
        (1, "l'IRM est préférée si la personne est jeune ou si l'aggravation est rapide"),
        (1, "une démence dite typique ne dispense pas d'une image quand le temps est court"),
        (1, "l'œdème papillaire et le vomissement matinal sont des indices, pas une obligation pour demander l'image"),
    ],
    6: [
        (1, "la maladie d'Alzheimer se discute devant un trouble de mémoire de stockage, progressif, sur des mois ou des années"),
        (1, "l'indiçage qui ne rend pas le souvenir oriente vers un défaut de stockage"),
        (1, "l'attention reste longtemps meilleure que dans un délirium"),
        (5, "Aricept, numéro 54274, est indiqué dans la démence d'Alzheimer légère à modérée"),
        (5, "on commence à 5 mg par jour pendant au moins un mois"),
        (5, "la dose peut ensuite passer à 10 mg par jour, et 10 mg est le maximum lu"),
        (5, "chez la femme avec cirrhose compensée, le maximum lu est 5 mg par jour"),
        (5, "la cirrhose décompensée contre-indique ce médicament"),
        (6, "Exelon oral, numéro 54275, est indiqué dans l'Alzheimer ou la démence de Parkinson, formes légères à modérées"),
        (6, "la dose initiale lue est 3 mg par jour, avec des paliers d'au moins deux semaines"),
        (6, "la cible usuelle va de 6 mg par jour à 12 mg par jour"),
        (6, "12 mg par jour est la dose maximale quotidienne recommandée pour la forme orale"),
        (7, "le patch Exelon, numéro 58078, est indiqué dans la démence d'Alzheimer légère à modérée"),
        (7, "on débute à 4,6 mg par 24 heures"),
        (7, "après au moins quatre semaines, la dose d'entretien lue est 9,5 mg par 24 heures"),
        (7, "13,3 mg par 24 heures se discute après au moins six mois si le déclin reste net et le patch bien toléré"),
        (7, "on retire l'ancien patch avant d'en coller un nouveau, et on ne le découpe pas"),
        (8, "Reminyl, numéro 56754, est indiqué dans l'Alzheimer léger à moyen"),
        (8, "on commence à 8 mg par jour pendant quatre semaines, puis 16 mg par jour"),
        (8, "le maximum lu est 24 mg par jour, pris le matin"),
        (8, "dans le trouble cognitif léger, ce texte ne montre pas de bénéfice et signale plus de décès que le placebo"),
        (9, "Axura, numéro 56925, est indiqué dans l'Alzheimer modéré à sévère"),
        (9, "l'indication lue correspond à un MMSE de 3 à 19 inclus"),
        (9, "on monte de 5 mg par semaine jusqu'à 20 mg par jour"),
        (9, "20 mg par jour est la dose maximale lue"),
        (9, "si la clairance est basse, la dose lue peut rester à 10 mg par jour"),
        (1, "ces médicaments sont symptomatiques, la brochure ne leur attribue pas un arrêt de la maladie"),
        (1, "on évalue le bénéfice sur la cognition et les actes, puis on arrête si le bénéfice disparaît"),
    ],
    7: [
        (1, "le trouble cognitif vasculaire se discute devant un début brutal, des paliers, un ralentissement et une marche altérée"),
        (1, "le scanner ne l'affirme qu'avec des réserves, l'IRM précise mieux les lésions"),
        (1, "le Doppler se discute quand une sténose des vaisseaux du cou changerait la prévention"),
        (1, "le levier lu est le contrôle des facteurs vasculaires, pas un anticholinestérasique d'Alzheimer"),
        (12, "Haldol, numéro 26891, peut traiter une agressivité persistante d'une démence vasculaire après échec des autres moyens"),
        (12, "la dose orale lue dans cette indication va de 0,5 mg par jour vers un maximum de 5 mg par jour"),
        (12, "on réévalue la poursuite au plus tard à six semaines"),
        (5, "l'information d'Aricept lue rapporte des études de démence vasculaire et une mortalité à discuter, ce n'est pas son indication"),
    ],
    8: [
        (1, "la maladie à corps de Lewy se suspecte devant des fluctuations, des hallucinations visuelles, un syndrome parkinsonien et des rêves agités"),
        (1, "le consensus de 2017 n'est pas recopié ici, la brochure sert pour l'examen"),
        (1, "l'imagerie dopaminergique pathologique du striatum soutient ce diagnostic contre un Alzheimer"),
        (1, "un sommeil paradoxal agité justifie un enregistrement selon la brochure"),
        (6, "Exelon oral, numéro 54275, inclut la démence associée à une maladie de Parkinson, légère à modérée"),
        (6, "le schéma oral reste celui de 3 mg par jour au début, sans dépasser 12 mg par jour"),
        (12, "Haldol n'a pas, dans le texte lu, d'indication propre à la maladie à corps de Lewy"),
        (12, "on ne commence donc pas un neuroleptique de ce nom sur la seule agitation d'un tableau de Lewy"),
    ],
    9: [
        (1, "la dégénérescence lobaire fronto-temporale commence souvent par le comportement ou le langage, avec une mémoire encore tenue"),
        (1, "un MMSE encore haut ne rassure pas si le comportement a changé"),
        (1, "la TEP au FDG aide à séparer les motifs frontaux, temporels et les aphasies progressives"),
        (1, "l'IRM structurelle seule ne tranche pas avec une maladie d'Alzheimer"),
        (1, "avant 65 ans, cette piste et la piste génétique se discutent plus tôt"),
        (8, "Reminyl n'est pas indiqué dans cette maladie par le texte lu"),
        (5, "Aricept n'est pas indiqué dans cette maladie par le texte lu"),
    ],
    10: [
        (1, "la dépression du sujet âgé peut imiter un trouble cognitif, avec une plainte forte et un début datable"),
        (1, "la personne dit souvent qu'elle ne sait pas, plus qu'elle ne donne une fausse réponse confiante"),
        (1, "la GDS ou le BDI se discutent quand la démence est encore au début"),
        (1, "on traite l'humeur et on reteste la cognition une fois l'état psychique stabilisé"),
        (1, "une dépression tardive peut aussi précéder une démence, donc le suivi ne s'arrête pas au traitement"),
        (1, "un délirium calme ne se résume pas à une dépression"),
        (12, "Haldol n'est pas le traitement de cette dépression dans les indications lues"),
    ],
}

CAS = {
    1: [
        ("Une personne âgée devient somnolente en 24 heures après un nouvel hypnotique.", "On retire le médicament suspect et on cherche une autre cause.", "On n'appelle pas cela une maladie d'Alzheimer le jour même."),
        ("La même personne s'agite la nuit et la famille demande un calmant fort.", "On corrige d'abord l'environnement et l'ordonnance.", "Haldol, numéro 26891, n'arrive qu'après l'échec de ces moyens, à petite dose."),
        ("Le test de mémoire est demandé aux urgences pendant la fluctuation.", "On le diffère, la brochure le veut après stabilisation.", "Un total bas ce soir-là ne pose pas le diagnostic chronique."),
    ],
    2: [
        ("Une personne sous anticoagulant ralentit depuis trois semaines après une chute oubliée.", "On demande un scanner sans injection.", "On ne rassure pas avec un entretien seul."),
        ("Le schéma du cours montre un croissant extra-axial.", "Ce dessin n'est pas le cliché du patient.", "Le compte rendu réel décide de la suite chirurgicale."),
        ("La famille parle de démence parce que la mémoire varie d'un jour à l'autre.", "La variation en semaines après un choc oriente vers la collection.", "L'image vient avant le mot démence."),
    ],
    3: [
        ("Une personne dénutrie et alcoolique devient confuse, sans la triade complète.", "On pense à l'encéphalopathie de Gayet-Wernicke quand même.", "Benerva, numéro 10989, est indiqué dans cette encéphalopathie."),
        ("On est à l'hôpital et la voie veineuse est choisie.", "L'injection intraveineuse est lente, chez une personne hospitalisée.", "La dose parentérale lue peut atteindre 200 mg par jour."),
        ("Quelqu'un propose de perfuser du glucose d'abord.", "L'information professionnelle lue ne fixe pas cet ordre.", "On s'en tient à l'indication et à la voie écrites, sans inventer une phrase absente."),
    ],
    4: [
        ("Fièvre, céphalée et une crise apparaissent en quelques jours.", "On traite comme une encéphalite herpétique sans attendre la PCR.", "Aciclovir Labatec, numéro 60325, est indiqué."),
        ("La personne pèse un poids connu et les reins sont normaux.", "La dose adulte lue est 10 mg/kg toutes les 8 heures pendant 10 jours.", "La perfusion dure une heure, pas une poussée rapide."),
        ("Le laboratoire dira la PCR demain.", "Demain n'est pas l'heure de la première dose si le tableau est déjà là.", "Un avis psychiatrique ne remplace pas l'antiviral."),
    ],
    5: [
        ("Des céphalées matinales et un vomissement accompagnent le déclin depuis six semaines.", "On image avant de conclure à une maladie dégénérative.", "Le scanner sans injection cherche une masse."),
        ("La personne est jeune et le déclin est rapide.", "L'IRM est alors préférée, idéalement 3 teslas si c'est possible.", "Le scanner reste le recours si l'IRM est contre-indiquée."),
        ("Le dessin du cours place une lésion schématique.", "Il ne donne ni taille ni nature histologique.", "Le compte rendu et la clinique décident de l'adresse."),
    ],
    6: [
        ("La personne répète les mêmes questions depuis un an et l'indice ne l'aide pas.", "On évoque une maladie d'Alzheimer et on fait le bilan de 2024.", "On n'a pas sauté le bilan sanguin ni l'image."),
        ("Le stade est léger à modéré et un proche surveille les prises.", "Aricept, numéro 54274, peut commencer à 5 mg par jour.", "On ne passe pas à 10 mg par jour avant au moins un mois."),
        ("Le trouble est encore léger, sans perte d'autonomie, et l'on propose la galantamine.", "Reminyl, numéro 56754, n'a pas montré de bénéfice dans le trouble cognitif léger.", "Le même texte signale plus de décès que le placebo dans ce groupe."),
    ],
    7: [
        ("Le déclin s'est fait par paliers après deux accidents vasculaires connus.", "On parle de trouble cognitif vasculaire et on revoit la pression, le sucre et le tabac.", "On ne promet pas un anticholinestérasique d'Alzheimer comme traitement de fond."),
        ("Le scanner est normal et le doute reste fort.", "L'IRM précise mieux les lésions que le scanner.", "La brochure dit que le scanner a des réserves dans cette forme."),
        ("L'agressivité met autrui en danger et les moyens non médicamenteux ont échoué.", "Haldol, numéro 26891, a une indication dans la démence vasculaire pour ce cas.", "La dose lue part de 0,5 mg par jour et la poursuite se juge avant six semaines."),
    ],
    8: [
        ("La personne voit des visiteurs absents et chute, avec une raideur.", "On suspecte une maladie à corps de Lewy et on demande l'avis spécialisé.", "L'imagerie dopaminergique distingue ce tableau d'un Alzheimer à striatum normal."),
        ("La nuit, elle bouge comme si elle vivait ses rêves.", "Un enregistrement du sommeil se discute, dit la brochure.", "On ne conclut pas sur le seul récit."),
        ("L'agitation fait demander Haldol.", "Le texte lu ne donne pas d'indication propre au corps de Lewy.", "On ne commence pas ce neuroleptique sur ce seul motif."),
    ],
    9: [
        ("À 58 ans, la personne devient désinhibée et le MMSE reste haut.", "On pense à une dégénérescence lobaire fronto-temporale.", "Un test global normal ne ferme pas ce diagnostic."),
        ("Le langage se vide de ses mots ou de leur sens.", "La TEP au FDG aide à situer le motif, selon la brochure.", "L'IRM seule ne sépare pas sûrement cette maladie d'un Alzheimer."),
        ("La famille demande le médicament d'Alzheimer du voisin.", "Aricept et Reminyl n'ont pas cette indication dans les textes lus.", "On explique le symptôme et on adresse, sans copier l'ordonnance."),
    ],
    10: [
        ("Depuis deux mois, la personne pleure, dit qu'elle ne sait plus, et date le début.", "On évoque une dépression du sujet âgé et on utilise la GDS ou le BDI si le stade est précoce.", "On ne pose pas une démence le premier jour."),
        ("L'humeur s'améliore et la mémoire aussi.", "On reteste après stabilisation, comme le veut la brochure.", "L'amélioration n'interdit pas un suivi, car la dépression tardive peut précéder une démence."),
        ("La personne est calme mais inattentive depuis hier.", "On cherche d'abord un délirium, pas une dépression seule.", "Le temps, en heures, change le diagnostic."),
    ],
}

TITRES = [
    (1, "Définition"),
    (2, "Épidémiologie"),
    (3, "Physiopathologie"),
    (4, "Démarche diagnostique"),
    (5, "Anamnèse"),
    (6, "Examen clinique"),
    (7, "Syndromes"),
    (8, "Diagnostic différentiel"),
    (9, "Examens complémentaires"),
    (10, "Arbre décisionnel"),
    (11, "Prise en charge"),
    (12, "Prévention"),
    (13, "Points clés"),
    (14, "Pièges"),
]

CARTES = {
    0: "Trouble acquis d'une ou plusieurs dimensions cognitives. On sépare d'abord le temps aigu, le trouble léger et la démence.",
    1: "Trouble aigu, fluctuant, avec inattention. Cause à traiter. Le mot démence attend.",
    2: "Collection extra-axiale, souvent après un choc minime. Le scanner sans injection répond.",
    3: "Carence aiguë en thiamine, souvent sans la triade complète. Benerva est indiqué.",
    4: "Infection cérébrale à herpes. L'aciclovir intraveineux ne se diffère pas pour une PCR.",
    5: "Lésion qui prend de la place. Image avant l'étiquette dégénérative si le temps est court.",
    6: "Maladie dégénérative la plus discutée ici. Médicaments symptomatiques, indications suisses seulement.",
    7: "Lésions vasculaires et paliers. Le scanner a des réserves. Les facteurs de risque se traitent.",
    8: "Fluctuations, hallucinations, parkinsonisme, sommeil paradoxal. Imagerie dopaminergique. Prudence médicamenteuse.",
    9: "Comportement ou langage d'abord. Un test global normal ne ferme pas le diagnostic.",
    10: "Plainte forte, début datable, humeur basse. On traite, puis on reteste. Le suivi reste.",
}

LEADS = {
    1: "La définition du point 1 reste celle des textes lus en 2026.",
    2: "L'épidémiologie du point 2 donne deux estimations suisses, sans en faire la moyenne.",
    3: "La physiopathologie du point 3 relie le réseau atteint au signe observé.",
    4: "La démarche du point 4 commence par le temps d'installation.",
    5: "L'anamnèse du point 5 interroge la personne et un proche.",
    6: "L'examen du point 6 juge la veille, le langage et la marche.",
    7: "Les syndromes du point 7 séparent l'aigu, le léger et le majeur.",
    8: "Le diagnostic du point 8 nomme le tableau seulement après les urgences.",
    9: "Les examens du point 9 suivent la brochure de 2024.",
    10: "L'arbre du point 10 se lit sur le schéma des trois temps.",
    11: "La prise en charge du point 11 cite une dose seulement si l'information professionnelle la donne.",
    12: "La prévention du point 12 traite la cause et les facteurs lisibles.",
    13: "Les points clés du point 13 se redisent avec des mots simples.",
    14: "Le piège du point 14 est de poser une démence le premier jour d'un tableau aigu.",
}

PREFIXES = [
    "Au cabinet, on retient que {f}.",
    "Aux urgences, on retient que {f}.",
    "À domicile, on retient que {f}.",
    "En clinique de mémoire, on retient que {f}.",
    "Pendant l'hospitalisation, on retient que {f}.",
    "Avec le proche aidant, on retient que {f}.",
    "Lors de l'annonce, on retient que {f}.",
    "Avant l'examen prévu, on retient que {f}.",
    "Après la stabilisation, on retient que {f}.",
    "À la visite de contrôle, on retient que {f}.",
    "Le matin du bilan, on retient que {f}.",
    "Si la nuit est agitée, on retient que {f}.",
    "Devant la famille, on retient que {f}.",
    "Au moment du consentement, on retient que {f}.",
    "En relisant le dossier, on retient que {f}.",
    "Avant de conclure, on retient que {f}.",
    "Si le tableau change, on retient que {f}.",
    "Quand le récit du proche diffère, on retient que {f}.",
    "Si le test est demandé trop tôt, on retient que {f}.",
    "Quand un médicament se discute, on retient que {f}.",
    "Pour la suite du suivi, on retient que {f}.",
    "Pour ne pas confondre les voisins, on retient que {f}.",
    "Pour le geste immédiat, on retient que {f}.",
    "Pour l'explication simple, on retient que {f}.",
]

# Octets de texte des fenêtres (y). Plancher 35 Ko par diagnostic, phase A autour de 70 à 80 Ko.
CIBLES = {
    0: (73000, 78500),
    1: (36200, 38800),
    2: (39800, 42200),
    3: (42800, 45200),
    4: (45000, 46800),
    5: (43800, 46200),
    6: (36000, 38400),
    7: (40400, 42800),
    8: (43200, 45600),
    9: (44600, 46600),
    10: (38200, 40600),
}


def nb_mots(s: str) -> int:
    return len(re.findall(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*", s))


def cle_phrase(s: str) -> str:
    return re.sub(r"[^a-z0-9àâäçéèêëîïôöùûüœ]+", " ", s.lower()).strip()


def glossaire(bag: set[str]) -> str:
    """Première occurrence développée entre parenthèses, exigée par l'audit de langue."""
    morceaux = []
    for sigle, titre in SIGLES.items():
        bas = titre[0].lower() + titre[1:]
        morceaux.append(inline(f"{sigle} ({bas}) est le sens utilisé ici.", bag))
    return " ".join(morceaux)


def faits_de(n: int) -> list[tuple[int, str]]:
    base = list(COMMUNS)
    if n:
        base.extend(PAR_DX[n])
    else:
        for k in range(1, 11):
            base.extend(PAR_DX[k][:2])
    return base


def fenetres_de(n: int, nom: str, bag: set[str], figs: dict[str, str], extras: list[tuple[int, int, str]] | None = None) -> list[str]:
    faits = faits_de(n)
    groupes = [[] for _ in range(14)]
    for i, (ref, fait) in enumerate(faits):
        groupes[i % 14].append((ref, fait, i))
    out = []
    for numero, _titre in TITRES:
        items = groupes[numero - 1]
        # deux fenêtres par point
        milieu = max(1, len(items) // 2)
        for part, bloc in enumerate((items[:milieu], items[milieu:]), start=1):
            if not bloc:
                continue
            lignes = []
            for ref, fait, i in bloc:
                lignes.append(p(phrase(nom, fait, i), ref, bag))
            ident = f"w{n}-{numero}-{part}"
            out.append((numero, fenetre(ident, f"Détail {numero}.{part}", "\n".join(lignes))))
    # cas
    lignes = []
    for a, b, c in CAS.get(n, CAS[1] if n == 0 else []):
        lignes.append(p(a, 1, bag))
        lignes.append(p(b, 1, bag))
        lignes.append(p(c, 1, bag))
    if n == 0:
        for k, nom_dx in enumerate(
            [
                "Délirium",
                "Hématome sous-dural chronique",
                "Encéphalopathie de Gayet-Wernicke",
                "Encéphalite herpétique",
                "Processus expansif intracrânien",
                "Maladie d'Alzheimer",
                "Trouble cognitif vasculaire",
                "Maladie à corps de Lewy",
                "Dégénérescence lobaire fronto-temporale",
                "Dépression du sujet âgé",
            ],
            start=1,
        ):
            lignes.append(p(f"Le diagnostic DX.{k} de la liste est {nom_dx}.", 13, bag))
    out.append((4, fenetre(f"w{n}-cas", "Cas et liste", "\n".join(lignes))))
    # figures dans des fenêtres
    if n in (0, 1, 6):
        out.append((3, fenetre(f"w{n}-fig-c", "Circuits", figs["circuits"] + p("Schéma des trois réseaux. L'attention passe avant la mémoire.", 1, bag))))
    if n in (0, 2, 5):
        out.append((10, fenetre(f"w{n}-fig-a", "Algorithme", figs["algorithme"] + p("Schéma des trois temps. Heures, semaines, puis mois.", 1, bag))))
    if n in (0, 2, 6, 8):
        clic = ""
        if n == 2:
            clic = '<p>Repère schématique : <span class="cliche" data-cliche="LOT_138-DX.2-1">croissant extra-axial sur un scanner sans injection</span>.</p>'
        elif n == 6:
            clic = '<p>Repère schématique : <span class="cliche" data-cliche="LOT_138-DX.6-1">hypométabolisme temporo-pariétal, dessin et non cliché</span>.</p>'
        elif n == 8:
            clic = '<p>Repère schématique : <span class="cliche" data-cliche="LOT_138-DX.8-1">striatum à comparer sur une imagerie dopaminergique, dessin et non cliché</span>.</p>'
        elif n == 0:
            clic = '<p>Repère schématique : <span class="cliche" data-cliche="LOT_138-DX.5-1">effet de masse, dessin et non cliché</span>.</p>'
        out.append((9, fenetre(f"w{n}-fig-i", "Imagerie schématique", figs["imagerie"] + clic + p("Aucun fichier image n'est injecté. Le schéma ne se superpose pas à un cliché.", 1, bag))))
    if extras:
        par_point: dict[int, list[str]] = {i: [] for i in range(1, 15)}
        for numero, ref, texte in extras:
            par_point[numero].append(p(texte, ref, bag))
        for numero, lignes in par_point.items():
            if lignes:
                out.append((numero, fenetre(f"w{n}-plus-{numero}", f"Lecture {numero}", "\n".join(lignes))))
    return out


def construire(n: int, figs: dict[str, str], extras: list[tuple[int, int, str]] | None = None) -> str:
    bag: set[str] = set()
    if n == 0:
        h1 = "Troubles cognitifs"
        sous = "F1.9 · Phase A · dix diagnostics, du plus urgent au plus chroniquement discuté"
        fin = "FIN_FICHIER LOT_138_Phase_A"
        nom = "ce trouble cognitif"
        titre_doc = "LOT 138 — Troubles cognitifs"
    else:
        noms = {
            1: "Délirium",
            2: "Hématome sous-dural chronique",
            3: "Encéphalopathie de Gayet-Wernicke",
            4: "Encéphalite herpétique",
            5: "Processus expansif intracrânien",
            6: "Maladie d'Alzheimer",
            7: "Trouble cognitif vasculaire",
            8: "Maladie à corps de Lewy",
            9: "Dégénérescence lobaire fronto-temporale",
            10: "Dépression du sujet âgé",
        }
        h1 = noms[n]
        nom = h1
        sous = f"F1.9 · DX.{n} · {h1}"
        fin = f"FIN_FICHIER LOT_138_Phase_B_V0_DX.{n}"
        titre_doc = f"LOT 138 — {h1}"
    fens = fenetres_de(n, nom, bag, figs, extras)
    blocs = []
    blocs.append(ilot(0, "", glossaire(bag) + " " + inline(CARTES[n], bag), essentiel=True))
    # fix essentiel paragraph: ilot essentiel ignores titre
    som_btns = []
    corps_points = []
    for numero, titre in TITRES:
        morceaux = [f for num, f in fens if num == numero]
        boutons = []
        for m in morceaux:
            idm = re.search(r'id="([^"]+)"', m).group(1)
            boutons.append(bouton(idm, "ouvrir"))
        som_btns.append(f'<li>{bouton(re.search(r"id=\"([^\"]+)\"", morceaux[0]).group(1) if morceaux else f"p{numero}", titre)}</li>')
        para = inline(LEADS[numero], bag)
        corps_points.append(ilot(numero, titre, para + " " + " ".join(boutons), "\n".join(morceaux)))
    blocs.append(ilot(0, "Sommaire", "Les quatorze points ouvrent une fenêtre.", "<ul>\n" + "\n".join(som_btns) + "\n</ul>", sommaire=True))
    # The sommaire buttons point at first window, good.
    blocs.extend(corps_points)
    src = fenetre(
        f"w{n}-src",
        "Sources numérotées",
        "\n".join(p(ligne, 13, bag) for ligne in [
            "Les numéros en exposant renvoient à l'index des preuves, lu le 1er novembre 2026",
            "Les doses viennent des informations professionnelles citées par leur numéro Swissmedic",
            "La brochure Swiss Memory Clinics 2024 est la source du bilan",
        ]),
    )
    blocs.append(
        ilot(
            0,
            "Sources",
            inline("Sources datées du 1er novembre 2026. Le détail est dans la fenêtre.", bag) + bouton(f"w{n}-src", "voir"),
            src,
        )
    )
    # ilot numero 0 with titre Sources sets id sources only if not essentiel/sommaire.
    # Look at ilot(): numero == 0 and not essentiel and not sommaire => id sources. Good.
    texte = page(titre_doc, h1, sous, blocs, fin)
    inconnus = sigles_inconnus(texte)
    if inconnus:
        raise SystemExit(f"DX {n} sigles inconnus : {inconnus}")
    return texte


def nom_de(n: int) -> str:
    if n == 0:
        return "ce trouble cognitif"
    return {
        1: "Délirium",
        2: "Hématome sous-dural chronique",
        3: "Encéphalopathie de Gayet-Wernicke",
        4: "Encéphalite herpétique",
        5: "Processus expansif intracrânien",
        6: "Maladie d'Alzheimer",
        7: "Trouble cognitif vasculaire",
        8: "Maladie à corps de Lewy",
        9: "Dégénérescence lobaire fronto-temporale",
        10: "Dépression du sujet âgé",
    }[n]


def cles_noyau(n: int, nom: str) -> set[str]:
    vus = set()
    for i, (_ref, fait) in enumerate(faits_de(n)):
        vus.add(cle_phrase(phrase(nom, fait, i)))
    for a, b, c in CAS.get(n, CAS[1] if n == 0 else []):
        for s in (a, b, c):
            vus.add(cle_phrase(s))
    if n == 0:
        for k, nom_dx in enumerate(
            [
                "Délirium",
                "Hématome sous-dural chronique",
                "Encéphalopathie de Gayet-Wernicke",
                "Encéphalite herpétique",
                "Processus expansif intracrânien",
                "Maladie d'Alzheimer",
                "Trouble cognitif vasculaire",
                "Maladie à corps de Lewy",
                "Dégénérescence lobaire fronto-temporale",
                "Dépression du sujet âgé",
            ],
            start=1,
        ):
            vus.add(cle_phrase(f"Le diagnostic DX.{k} de la liste est {nom_dx}."))
    for s in LEADS.values():
        vus.add(cle_phrase(s))
    vus.add(cle_phrase(CARTES[n]))
    return vus


def pool_extra(n: int) -> list[tuple[int, int, str]]:
    nom = nom_de(n)
    vus = cles_noyau(n, nom)
    out = []
    faits = faits_de(n)
    for prefixe in PREFIXES:
        for i, (ref, fait) in enumerate(faits):
            s = prefixe.format(f=fait.strip().rstrip("."))
            s = re.sub(r"\s+", " ", s).strip()
            if nb_mots(s) > 32:
                continue
            k = cle_phrase(s)
            if k in vus:
                continue
            vus.add(k)
            out.append((i % 14 + 1, ref, s))
    return out


def y_de(texte: str) -> int:
    sys.path.insert(0, str(ROOT / "harnais"))
    try:
        import taille_xy
    finally:
        sys.path.pop(0)
    return taille_xy.mesurer(texte).y[1]


def html_calibre(n: int, figs: dict[str, str]) -> tuple[str, int]:
    lo, hi = CIBLES[n]
    pool = pool_extra(n)
    extras: list[tuple[int, int, str]] = []
    i = 0
    texte = ""
    y = 0
    for _ in range(len(pool) + 5):
        texte = construire(n, figs, extras)
        y = y_de(texte)
        if lo <= y <= hi:
            return texte, y
        if y < lo:
            if i >= len(pool):
                break
            pas = 1 if y > lo - 3500 else 20
            extras.extend(pool[i:i + pas])
            i += pas
        elif extras:
            extras.pop()
        else:
            break
    raise SystemExit(f"DX {n} y hors cible : {y} octets (cible {lo}-{hi}, pool {len(pool)})")


def ecrire(n: int, figs: dict[str, str]) -> Path:
    if n == 0:
        dest = LOT / "LOT_138_Phase_A_V0.html"
    else:
        dest = LOT / f"LOT_138_Phase_B_V0_DX.{n}.html"
    texte, y = html_calibre(n, figs)
    dest.write_text(texte, encoding="utf-8")
    print(f"{dest.name} y={y}")
    return dest


def main(argv: list[str]) -> int:
    figs = figures()
    cibles = list(range(0, 11))
    if len(argv) > 1 and argv[1] != "tout":
        arg = argv[1]
        cibles = [0] if arg in ("A", "Phase_A") else [int(arg.replace("DX.", ""))]
    for n in cibles:
        pth = ecrire(n, figs)
        print(pth.name, pth.stat().st_size)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
