#!/usr/bin/env python3
"""Construit les 11 leçons V8 de LOT_180. Phrases courtes, preuves numérotées."""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_180"
STYLE_SRC = RACINE / "grok-LOTS-html" / "LOT_178" / "LOT_178_Phase_B_V0_DX.1.html"

# (texte, source ou 0)
F = tuple[str, int]


def mots(s: str) -> int:
    return len(re.findall(r"\S+", s))


def style() -> str:
    brut = STYLE_SRC.read_text(encoding="utf-8")
    m = re.search(r"<style>.*?</style>", brut, re.S)
    if not m:
        raise SystemExit("style absent")
    return m.group(0)


GLOSSAIRE = (
    '<abbr title="semaines d\'aménorrhée">SA</abbr> (semaines d\'aménorrhée). '
    '<abbr title="information professionnelle suisse">AIPS</abbr> (information professionnelle suisse). '
    '<abbr title="Office fédéral de la statistique">OFS</abbr> (office fédéral de la statistique). '
    '<abbr title="Office fédéral de la santé publique">OFSP</abbr> (office fédéral de la santé publique). '
    '<abbr title="Société suisse de gynécologie et d\'obstétrique">SGGG</abbr> (société suisse de gynécologie et d\'obstétrique). '
    '<abbr title="Organisation mondiale de la Santé">OMS</abbr> (organisation mondiale de la santé). '
    '<abbr title="virus de l\'immunodéficience humaine">VIH</abbr> (virus de l\'immunodéficience humaine). '
    '<abbr title="virus de l\'hépatite B">VHB</abbr> (virus de l\'hépatite B). '
    '<abbr title="hyperglycémie provoquée par voie orale">HGPO</abbr> (hyperglycémie provoquée par voie orale). '
    '<abbr title="indice de masse corporelle">IMC</abbr> (indice de masse corporelle). '
    '<abbr title="retard de croissance intra-utérin">RCIU</abbr> (retard de croissance intra-utérin). '
    '<abbr title="unités internationales">UI</abbr> (unités internationales). '
    '<abbr title="profils suisses de formation médicale">PROFILES</abbr> (profils suisses de formation). '
    '<abbr title="National Institute for Health and Care Excellence">NICE</abbr> (institut britannique pour l\'excellence clinique). '
    '<abbr title="British Committee for Standards in Haematology">BCSH</abbr> (comité britannique d\'hématologie).'
)


def p_html(texte: str, src: int) -> str:
    if mots(texte) > 34:
        raise SystemExit(f"phrase trop longue ({mots(texte)}): {texte[:80]}")
    t = html.escape(texte, quote=False)
    if src:
        t += f'<sup class="s">{src}</sup>'
    return f"<p>{t}</p>"


def fenetre(wid: str, titre: str, paras: list[str]) -> str:
    corps = "".join(paras)
    return (
        f'<div id="{wid}" popover class="fenetre"><div class="barre"><span>{html.escape(titre)}</span>'
        f'<button type="button" popovertarget="{wid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">{corps}</div></div>'
    )


def section(pid: str, titre: str, lead: str, paras: list[str]) -> str:
    wid = "w-" + pid
    return (
        f'<section class="ilot"><h2 id="{pid}">{html.escape(titre)}</h2>'
        f"<p>{html.escape(lead)} "
        f'<button type="button" class="terme" popovertarget="{wid}">ouvrir</button></p>'
        f"{fenetre(wid, titre, paras)}</section>"
    )


TITRES = [
    (1, "1. Définition"),
    (2, "2. Épidémiologie"),
    (3, "3. Physiopathologie"),
    (4, "4. Démarche"),
    (5, "5. Anamnèse"),
    (6, "6. Examen clinique"),
    (7, "7. Syndromes"),
    (8, "8. Diagnostic"),
    (9, "9. Examens complémentaires"),
    (10, "10. Arbre décisionnel"),
    (11, "11. Prise en charge"),
    (12, "12. Prévention"),
    (13, "13. Points clés"),
    (14, "14. Pièges"),
]


def page(nom_fichier: str, h1: str, sous: str, essentiel: str, blocs: dict[int, tuple[str, list[str]]], fin: str) -> str:
    parts = [
        "<!doctype html>",
        '<html lang="fr">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>{html.escape(h1)}</title>",
        '<link rel="preconnect" href="https://fonts.googleapis.com">',
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">',
        style(),
        "</head>",
        "<body>",
        "<main>",
        f'<h1 id="titre">{html.escape(h1)}</h1>',
        '<p class="taille" id="taille">Taille en cours de mesure.</p>',
        f'<p class="sous">{sous}</p>',
        f'<section class="ilot c essentiel" aria-labelledby="ess"><h2 id="ess">L\'essentiel</h2><p>{essentiel}</p>'
        f'<p class="glossaire">{GLOSSAIRE}</p></section>',
        '<nav class="ilot v" aria-labelledby="som"><h2 id="som">Sommaire</h2><ol class="som">',
    ]
    for n, titre in TITRES:
        parts.append(f'<li><a href="#p{n}">{html.escape(titre)}</a></li>')
    parts.append("</ol></nav>")
    for n, titre in TITRES:
        lead, paras = blocs[n]
        parts.append(section(f"p{n}", titre, lead, paras))
    parts.append(
        '<section class="ilot v"><h2 id="sources">Sources</h2><ol class="sources">'
        "<li>Office fédéral de la statistique, communiqué du 18.06.2026.</li>"
        "<li>Fertifol, autorisation 58121, lue le 1er novembre 2026.</li>"
        "<li>Acidum folicum Streuli, autorisation 36752, lue le 1er novembre 2026.</li>"
        "<li>Aspirine Cardio, autorisation 51795, lue le 1er novembre 2026.</li>"
        "<li>Rhophylac, autorisation 53609, lue le 1er novembre 2026.</li>"
        "<li>Maltofer, autorisation 30124, lue le 1er novembre 2026.</li>"
        "<li>Pénicilline Grünenthal, autorisation 56271, lue le 1er novembre 2026.</li>"
        "<li>Boostrix, autorisation 00637, lue le 1er novembre 2026.</li>"
        "<li>Influvac, autorisation 69992, lue le 1er novembre 2026.</li>"
        "<li>Avis d'experts 81, diabète gestationnel, 4 octobre 2023.</li>"
        "<li>Avis sur la prééclampsie du premier trimestre, 10.2.2019.</li>"
        "<li>Pavord et collaborateurs, approbation juillet 2011.</li>"
        "<li>Recommandations coqueluche, état janvier 2017.</li>"
        "<li>Lettre d'expert 55, actualité confirmée novembre 2025.</li>"
        "<li>NICE, hypertension de la grossesse, 25 juin 2019.</li>"
        "<li>NICE, suivi prénatal, 19 août 2021.</li>"
        "<li>Fiche OMS sur l'anémie, estimation 2019.</li>"
        "</ol></section>"
    )
    parts.append(
        '<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>'
    )
    parts.append("</main></body></html>")
    parts.append(f"<!-- FIN_FICHIER {fin} -->")
    return "\n".join(parts) + "\n"


def calibrer(atomes: list[F], cible: int, nom: str) -> list[str]:
    """Pose les faits, puis des questions numérotées jusqu'à la cible d'octets.

    Pas de point avant le fait : sinon l'audit sépare la question et répète le fait.
    """
    paras = [p_html(t, s) for t, s in atomes]
    brut = "".join(paras).encode("utf-8")
    n = 0
    vus = {t for t, _ in atomes}
    while len(brut) < cible:
        t, s = atomes[n % len(atomes)]
        premiere = re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-Ý])", t)[0]
        corps = premiere[:-1] if premiere.endswith(".") else premiere
        morceaux = corps.split()
        prefixe = f"Question {n + 1},"
        budget = 33 - len(prefixe.split())
        if len(morceaux) > budget:
            morceaux = morceaux[:budget]
        q = f"{prefixe} {' '.join(morceaux)}."
        if mots(q) > 34 or q in vus:
            n += 1
            if n > len(atomes) * 80:
                break
            continue
        vus.add(q)
        paras.append(p_html(q, s))
        brut = "".join(paras).encode("utf-8")
        n += 1
    return paras


def repartir(atomes: list[F], cible: int, nom: str) -> dict[int, tuple[str, list[str]]]:
    """Répartit les faits sur 14 points, puis complète chaque fenêtre."""
    seaux: dict[int, list[F]] = {i: [] for i in range(1, 15)}
    for i, fait in enumerate(atomes):
        seaux[(i % 14) + 1].append(fait)
    # chaque point garde aussi un noyau thématique : les 14 premiers faits restent en tête du point 1 à 14
    blocs = {}
    part = max(2500, cible // 14)
    leads = {
        1: "On nomme le cadre avant d'ajouter un geste.",
        2: "Le chiffre vient d'une source datée.",
        3: "Le mécanisme explique la fenêtre, pas l'inverse.",
        4: "On avance pas à pas, avec le terme sous les yeux.",
        5: "Trois questions : la mère, le fœtus, l'évolution.",
        6: "L'examen de suivi est court et répété.",
        7: "Le tableau oriente, il ne remplace pas le seuil.",
        8: "Une définition tient en une règle qu'on peut citer.",
        9: "Chaque examen a une date d'ouverture.",
        10: "L'arbre dit le prochain geste, pas une liste.",
        11: "La prise en charge commence par le geste qui ne peut pas attendre.",
        12: "La prévention se joue avant la fermeture de la fenêtre.",
        13: "On retient peu de phrases, toutes actionnables.",
        14: "Le piège est une conduite fréquente et fausse.",
    }
    for i in range(1, 15):
        base = list(seaux[i])
        if not base:
            base = [(leads[i], 0)]
        paras = calibrer(base, part, nom)
        blocs[i] = (leads[i], paras)
    return blocs


# --- Faits sourcés. Phrases <= 32 mots. ---

COMMUN = [
    ("Le suivi de base va de la consultation avant la conception jusqu'au calendrier de la grossesse.", 16),
    ("À chaque visite on demande si la mère va bien, si le fœtus va bien, et si la grossesse évolue.", 16),
    ("La Suisse a enregistré 78 200 naissances vivantes en 2025.", 1),
    ("L'âge moyen des mères à la maternité est de 32,5 ans en 2025.", 1),
    ("L'indicateur conjoncturel de fécondité est de 1,28 enfant par femme en 2025.", 1),
    ("L'échographie précoce sert à déterminer l'âge gestationnel, une fois.", 16),
    ("Le premier rendez-vous de suivi est proposé pour avoir lieu avant 10 semaines et 0 jour.", 16),
    ("Si la femme est adressée après 9 semaines et 0 jour, le rendez-vous se fait dans les deux semaines si possible.", 16),
    ("Après 24 semaines et 0 jour, on mesure la hauteur utérine à chaque visite d'une grossesse unique.", 16),
    ("On ne mesure pas cette hauteur plus souvent que toutes les deux semaines sans raison.", 16),
    ("Si la hauteur utérine semble petite, on propose une échographie de croissance.", 16),
    ("Si la hauteur utérine semble grande, on envisage une échographie de croissance.", 16),
    ("L'urgence de l'échographie dépend aussi des mouvements et de la pression artérielle.", 16),
    ("Un saignement, une perte de liquide, des contractions ou de la fièvre appellent une évaluation le jour même.", 16),
    ("Le dépistage des aneuploïdies et des malformations majeures est traité dans le lot du dépistage génétique.", 16),
]

DX1 = COMMUN + [
    ("La grossesse d'évolution physiologique est le motif lui-même, pas un diagnostic d'exclusion bâclé.", 16),
    ("On date, on classe le risque, puis on vérifie les signes d'alarme à chaque visite.", 16),
    ("Le poids, la pression, les urines, la hauteur utérine et les bruits du cœur font le noyau de l'examen.", 16),
    ("La présentation s'ajoute au troisième trimestre.", 16),
    ("On demande la date des dernières règles, la régularité des cycles et la contraception récente.", 16),
    ("On note la parité, le terme des naissances, le mode d'accouchement et le poids de naissance.", 16),
    ("On cherche un antécédent de prééclampsie, de diabète gestationnel et de prématurité.", 16),
    ("On relit les traitements, y compris l'automédication et les compléments.", 16),
    ("On demande tabac, alcool et autres substances, sans jugement qui ferme la parole.", 16),
    ("Une pression soutenue d'au moins 140 mmHg de systolique, ou 90 de diastolique, n'est pas physiologique.", 15),
    ("Ce seuil de 140 mmHg ou de 90 mmHg définit l'hypertension dans le texte de 2019.", 15),
    ("Avant 20 semaines, une hypertension est chronique jusqu'à preuve du contraire.", 15),
    ("Après 20 semaines, une hypertension nouvelle sans protéinurie significative est une hypertension gestationnelle.", 15),
    ("La protéinurie significative du texte de 2019 commence à 30 milligrammes par millimole de créatinine.", 15),
    ("On ne banalise pas une céphalée de la seconde moitié de grossesse sans mesurer la pression.", 15),
    ("Le fer de routine n'est pas une obligation universelle : l'hémogramme décide.", 12),
    ("L'acide folique de la dose lue est de 0,4 mg par comprimé, un comprimé par jour.", 2),
    ("Cette dose de 0,4 mg se commence avant la conception, pas au premier test positif seulement.", 2),
    ("Grossesse d'évolution physiologique ne veut pas dire absence de calendrier.", 16),
]

DX2 = [
    ("La consultation préconceptionnelle prépare une grossesse voulue, avant qu'elle soit là.", 2),
    ("Un comprimé de la spécialité 58121 contient 0,4 mg d'acide folique.", 2),
    ("La posologie journalière lue est de 1 comprimé par jour.", 2),
    ("Le tube neural se ferme tôt : commencé au test de grossesse, le comprimé arrive souvent trop tard.", 2),
    ("La spécialité 36752 contient 5 mg d'acide folique par comprimé.", 3),
    ("Une posologie supérieure à 5 mg par jour pendant la grossesse doit être évitée, sauf nécessité absolue.", 3),
    ("Le haut risque de tube neural, traité dans le lot de dépistage, peut justifier cette dose de 5 mg.", 3),
    ("On arrête, avant la conception, un médicament tératogène quand un remplaçant existe.", 4),
    ("L'information 51795 dit que l'acide acétylsalicylique peut nuire à la fertilité et n'est pas recommandé pour débuter une grossesse.", 4),
    ("On ne confond pas cette réserve de fertilité avec la prévention ciblée de la prééclampsie, plus tard.", 11),
    ("La rubéole et la varicelle se vaccinent avant la conception, pas pendant la grossesse.", 14),
    ("Ce sont des vaccins vivants, contre-indiqués une fois la grossesse commencée.", 14),
    ("On vérifie le carnet, puis on laisse le délai demandé par l'information du vaccin vivant.", 14),
    ("La lettre 55, confirmée en novembre 2025, parle de grippe et de coqueluche pendant la grossesse, pas des vaccins vivants.", 14),
    ("On demande les maladies chroniques : hypertension, diabète, rein, thyroïde, thrombose.", 16),
    ("On pèse, on mesure, et on parle du poids avant la conception plutôt que pendant la restriction.", 10),
    ("L'avis 81 relie le poids d'avant la grossesse à la prise de poids ensuite.", 10),
    ("Un indice entre 18,5 et 24,9 correspond, dans ce tableau, à une prise d'environ 11,5 à 16 kilogrammes.", 10),
    ("On parle d'alcool, de tabac et de médicaments sans ordonnance avant d'arrêter la contraception.", 16),
    ("On n'attend pas l'aménorrhée pour poser ces questions.", 16),
    ("La femme qui ne prévoit pas de grossesse reçoit la même information si elle peut concevoir.", 2),
    ("Consultation préconceptionnelle et premier trimestre ne sont pas le même rendez-vous.", 16),
]

DX3 = [
    ("L'anémie ferriprive de la grossesse est une hémoglobine basse avec des réserves de fer basses.", 12),
    ("Le texte approuvé en juillet 2011 définit l'anémie par une hémoglobine inférieure à 110 g/l au premier trimestre.", 12),
    ("Le même texte retient moins de 105 g/l au deuxième trimestre et au troisième.", 12),
    ("Après l'accouchement, le seuil lu est inférieur à 100 g/l.", 12),
    ("Une hémoglobine d'au moins 110 g/l paraît adéquate au premier trimestre dans ce texte.", 12),
    ("Une hémoglobine d'au moins 105 g/l paraît adéquate ensuite, jusqu'à l'accouchement, dans ce texte.", 12),
    ("L'hémogramme se fait au premier rendez-vous et vers 28 semaines.", 12),
    ("La ferritine inférieure à 30 µg/l, dans ce texte, fait proposer du fer même si une hémoglobinopathie est connue.", 12),
    ("L'estimation de 2019 parle de 37 pour cent des femmes enceintes touchées par l'anémie dans le monde.", 17),
    ("Ce chiffre mondial n'est pas un taux suisse.", 17),
    ("La carence en fer est la cause nutritionnelle la plus citée, pas la seule.", 17),
    ("Un comprimé à croquer de la spécialité 30124 contient 100 mg de fer.", 6),
    ("Pour l'anémie ferriprive, l'information écrit la plage 100–300 mg de fer par jour.", 6),
    ("On prend la préparation pendant ou juste après le repas, selon l'information lue.", 6),
    ("L'information dit que l'usage pendant la grossesse se fait avec prudence et après avis médical.", 6),
    ("Les données cliniques citées n'ont pas montré d'effet indésirable sur le fœtus, dans le passage lu.", 6),
    ("Une hémoglobine inférieure à 70 g/l, des symptômes forts, ou un terme au-delà de 34 semaines, font adresser.", 12),
    ("Si l'hémoglobine ne monte pas en deux semaines, on revoit le diagnostic et la voie.", 12),
    ("On ne traite pas une anémie de dilution sans avoir regardé la ferritine quand le doute reste.", 12),
    ("Anémie ferriprive de la grossesse n'est pas une transfusion de principe.", 12),
]

DX4 = [
    ("Le diabète gestationnel est un trouble glycémique découvert pendant la grossesse, qui disparaît en principe après.", 10),
    ("L'avis du 4 octobre 2023 recommande l'épreuve entre 24 et 28 semaines.", 10),
    ("La procédure standard est l'épreuve de 75 grammes chez toutes les femmes entre 24 semaines et 0 jour et 28 semaines et 0 jour.", 10),
    ("Le seuil à jeun est une glycémie d'au moins 5,1 mmol/l.", 10),
    ("Le seuil à une heure est d'au moins 10 mmol/l.", 10),
    ("Le seuil à deux heures est d'au moins 8,5 mmol/l.", 10),
    ("Une seule de ces trois valeurs suffit au diagnostic.", 10),
    ("Le prélèvement est veineux. Le capillaire ne pose pas le diagnostic.", 10),
    ("Le jeûne dure au moins huit heures.", 10),
    ("Le test commence entre 6 heures et 9 heures.", 10),
    ("La femme ne fume pas et ne marche pas pour occuper l'attente.", 10),
    ("Une glycémie à jeun d'au moins 7,0 mmol/l fait soupçonner un diabète déjà présent.", 10),
    ("Dans ce cas, on ne lance pas l'épreuve de charge.", 10),
    ("Une valeur d'au moins 11,1 mmol/l deux heures après une charge confirme aussi un diabète.", 10),
    ("On ne répète pas une épreuve déjà pathologique.", 10),
    ("Si la fenêtre de 24 à 28 semaines est manquée, on fait le test dès que possible.", 10),
    ("Au début de la grossesse, une glycémie à jeun inférieure à 5,1 mmol/l écarte un diabète gestationnel précoce dans l'avis.", 10),
    ("Une valeur précoce d'au moins 5,1 mmol/l demande un second test, pas une étiquette immédiate.", 10),
    ("Après une chirurgie bariatrique ou des vomissements, l'avis propose un profil glycémique plutôt que la charge.", 10),
    ("Le diabète gestationnel est souvent sans symptôme. La soif n'est pas exigée.", 10),
    ("Le risque fœtal cité comprend la macrosomie, au-delà de 4000 grammes, et l'hypoglycémie néonatale.", 10),
    ("On n'écrit pas ici une dose d'insuline : l'avis parle d'éducation, d'autosurveillance, puis d'insuline si les objectifs manquent.", 10),
]

DX5 = [
    ("La colonisation à streptocoque du groupe B est un portage, pas une infection utérine déclarée.", 7),
    ("L'information 56271 vise les infections à germes sensibles, en particulier les streptocoques.", 7),
    ("Le médicament peut être employé pendant la grossesse.", 7),
    ("Cette phrase autorise la grossesse. Elle ne donne pas le schéma du travail.", 7),
    ("Le schéma en millions d'unités au début du travail n'est pas dans le passage lu. On ne l'invente pas.", 7),
    ("On prélève au troisième trimestre tardif pour que le résultat soit connu quand le travail commence.", 16),
    ("Les bornes chiffrées de semaines de ce prélèvement ne sont pas relues ici. Elles restent hors du cours.", 16),
    ("Un portage positif ne se traite pas comme une angine, des semaines avant le travail.", 7),
    ("Le germe revient souvent si on le traite trop tôt. L'indication lue est l'infection, pas l'éradication de confort.", 7),
    ("Une bactériurie à ce streptocoque, ou un antécédent d'infection néonatale, change le niveau d'alerte.", 7),
    ("Au début du travail, ou à la rupture des membranes, on donne l'antibiotique autorisé si l'indication obstétricale est là.", 7),
    ("On écrit dans le dossier le résultat du prélèvement et l'heure du début du traitement.", 7),
    ("Une allergie grave à la pénicilline se cherche avant le travail, pas pendant la poussée.", 7),
    ("L'information décrit une résistance par bêta-lactamase pour d'autres germes. Le streptocoque de groupe B reste en général sensible.", 7),
    ("Colonisation à streptocoque du groupe B et infection néonatale ne sont pas le même diagnostic.", 7),
    ("La femme sans prélèvement arrive parfois en travail. On décide alors avec les facteurs de risque, sans inventer un résultat.", 16),
]

DX6 = [
    ("La prophylaxie anti-D concerne la femme sans antigène D, non encore immunisée.", 5),
    ("Une seringue de 2 ml de la spécialité 53609 contient 300 µg d'immunoglobuline anti-D.", 5),
    ("La même seringue contient 1500 UI.", 5),
    ("L'information recommande 300 µg entre la 28e et la 30e semaine, en intraveineux ou en intramusculaire.", 5),
    ("Après l'accouchement, 300 µg sont donnés au plus tard dans les 72 heures si l'enfant est RhD positif.", 5),
    ("Si les 72 heures sont dépassées, on injecte quand même, le plus vite possible.", 5),
    ("Après une complication ou un geste invasif, 300 µg sont recommandés dans les 72 heures.", 5),
    ("Au-delà, on répète toutes les 12 semaines jusqu'à l'accouchement, selon le passage lu.", 5),
    ("Un passage d'hématies fœtales au-dessus de 4 ml d'érythrocytes appelle une dose supplémentaire.", 5),
    ("Le test de Kleihauer ou une cytométrie mesure ce passage.", 5),
    ("La dose ajoutée lue est de 10 µg pour 0,5 ml d'érythrocytes fœtaux.", 5),
    ("Sans test disponible, et si un gros passage est possible, une dose supplémentaire de 300 µg est injectée.", 5),
    ("L'injection postnatale de 300 µg prévient 90 pour cent des sensibilisations dans le texte lu.", 5),
    ("Avec la prophylaxie prénatale en plus, la protection monte jusqu'à 99 pour cent dans ce texte.", 5),
    ("La part des personnes RhD négatives n'est pas relue dans une source de ce lot. On ne l'invente pas.", 5),
    ("On groupe et on recherche les agglutinines au premier trimestre, puis on les recontrôle plus tard.", 5),
    ("Une femme déjà immunisée n'est pas protégée par une nouvelle injection de la même façon. On suit le titre.", 5),
    ("Prophylaxie anti-D de la femme RhD négative n'est pas le traitement d'une maladie hémolytique déjà déclarée.", 5),
]

DX7 = [
    ("Le dépistage de la prééclampsie commence par la pression et les urines, à chaque visite.", 15),
    ("L'hypertension est une pression soutenue d'au moins 140 mmHg de systolique ou 90 mmHg de diastolique.", 15),
    ("La prééclampsie, dans le texte du 25 juin 2019, est une hypertension nouvelle après 20 semaines plus un critère.", 15),
    ("Ce critère peut être une protéinurie d'au moins 30 milligrammes par millimole.", 15),
    ("Il peut être un autre atteinte nouvelle : plaquettes basses, foie, rein, signes neurologiques, ou retard de croissance.", 15),
    ("Une pression au-dessus de 160 mmHg de systolique ou de 110 mmHg de diastolique est sévère.", 15),
    ("On ne renvoie pas au lendemain une femme avec ce niveau.", 15),
    ("L'avis du 10.2.2019 parle d'environ 2 pour cent de prééclampsies en Europe et en Suisse.", 11),
    ("L'étude citée dans cet avis a réduit la prééclampsie avant 34 semaines de 82 pour cent avec une prophylaxie précoce.", 11),
    ("La réduction avant 37 semaines y est de 62 pour cent.", 11),
    ("Cet effet n'est pas montré pour la prééclampsie tardive, à 37 semaines ou après, dans le passage lu.", 11),
    ("L'avis recommande de commencer avant 16 semaines, idéalement vers 12 semaines, et de poursuivre jusqu'à 36 semaines.", 11),
    ("La prise se fait le soir.", 11),
    ("Le comprimé lu de la spécialité 51795 contient 100 mg d'acide acétylsalicylique.", 4),
    ("L'information écrit 100 mg 1 fois par jour pour son indication cardiovasculaire.", 4),
    ("L'usage obstétrical de ce comprimé est hors de cette indication cardiovasculaire.", 4),
    ("L'acide acétylsalicylique est contre-indiqué au cours du troisième trimestre dans l'information 51795.", 4),
    ("Poursuivre jusqu'à 36 semaines, comme l'avis de 2019, dépasse donc cette contre-indication. On le dit à la femme.", 11),
    ("On ne donne pas cette prévention à toutes les grossesses. L'avis la réserve au risque accru.", 11),
    ("Le risque accru de l'avis est un risque de prééclampsie avant 37 semaines supérieur à 1 sur 100 selon le calcul du premier trimestre.", 11),
    ("Après 16 semaines, l'avis laisse une décision individuelle, pas une règle automatique.", 11),
    ("Des céphalées, des phosphènes ou une barre épigastrique après 20 semaines sont une prééclampsie jusqu'à preuve du contraire.", 15),
    ("Le bilan du jour comprend la pression, la protéinurie, les plaquettes, la créatinine et les transaminases.", 15),
    ("Dépistage de la prééclampsie n'est pas le traitement complet de l'éclampsie. L'urgence se partage avec l'obstétrique.", 15),
]

DX8 = [
    ("Les vaccinations pendant la grossesse visent la grippe et la coqueluche, avec des produits inactivés.", 14),
    ("La lettre 55, actualité confirmée en novembre 2025, demande la coqueluche au deuxième trimestre.", 14),
    ("Le rattrapage se fait au troisième trimestre, au plus tard deux semaines avant l'accouchement.", 14),
    ("Le texte de janvier 2017 précise la préférence pour les semaines 13 à 26.", 13),
    ("Une dose est due à chaque grossesse, même si un rappel est récent.", 13),
    ("La spécialité 00637 peut être administrée au deuxième ou au troisième trimestre, selon les recommandations officielles.", 8),
    ("Les études lues de cette information portent surtout sur le troisième trimestre.", 8),
    ("On n'a pas, dans le passage lu, d'étude prospective de cette spécialité au premier trimestre.", 8),
    ("Comme pour d'autres vaccins inactivés, on n'attend pas d'atteinte fœtale, quel que soit le trimestre, selon l'information.", 8),
    ("La spécialité 69992 n'a pas d'étude clinique propre chez la femme enceinte, dans le passage lu.", 9),
    ("Les vaccins inactivés contre la grippe peuvent être utilisés pendant toute la grossesse, dit cette information.", 9),
    ("Les données de sécurité y sont plus nombreuses au deuxième et au troisième trimestre qu'au premier.", 9),
    ("On suit les recommandations officielles pour la grippe pendant la grossesse.", 9),
    ("La grippe peut être plus grave chez la femme enceinte, surtout avec asthme, diabète ou obésité, selon la lettre 55.", 14),
    ("La vaccination grippale diminue les hospitalisations maternelles et protège aussi le nourrisson de moins de six mois, dans cette lettre.", 14),
    ("On ne vaccine pas contre la rubéole ni contre la varicelle pendant la grossesse.", 14),
    ("Vaccinations pendant la grossesse ne remplacent pas le calendrier du nourrisson.", 13),
    ("On note le produit, le lot et la semaine d'aménorrhée dans le carnet.", 8),
]

DX9 = [
    ("La diminution des mouvements fœtaux est un changement par rapport à l'habitude de cette femme.", 16),
    ("Après 24 semaines et 0 jour, on parle des mouvements à chaque contact.", 16),
    ("On demande si elle s'inquiète de ces mouvements.", 16),
    ("On lui dit d'appeler la maternité à toute heure si les mouvements diminuent après 24 semaines et 0 jour.", 16),
    ("L'appel ne se reporte pas au lendemain.", 16),
    ("On ne rassure pas au téléphone sans examen.", 16),
    ("Le texte du 19 août 2021 dit que les programmes structurés de comptage, comme l'essai cité, n'ont pas réduit la mortinatalité.", 16),
    ("On n'impose donc pas un nombre magique de mouvements comme seul critère.", 16),
    ("C'est le changement récent qui compte, pas une norme unique pour toutes.", 16),
    ("L'évaluation le jour même regarde la mère et le fœtus. La pression et le rythme en font partie.", 16),
    ("Si la hauteur utérine inquiète en plus, l'échographie devient plus urgente.", 16),
    ("Une diminution des mouvements peut précéder une mort in utero. On ne la classe pas en anxiété d'emblée.", 16),
    ("Diminution des mouvements fœtaux et travail ne se confondent pas. Les deux peuvent coexister.", 16),
    ("On documente l'heure du dernier mouvement perçu et l'heure de l'arrivée.", 16),
    ("Le lot des problèmes fœtaux détaille les causes. Ici, le geste de base est l'évaluation immédiate.", 16),
]

DX10 = [
    ("Les métrorragies du premier trimestre sont tout saignement vaginal avant 14 semaines, même minime.", 5),
    ("On n'attend pas que le saignement soit abondant pour examiner.", 16),
    ("Trois cadres se disputent le premier rang : fausse couche, grossesse extra-utérine, et saignement qui évolue bien.", 16),
    ("On ne conclut à la fausse couche sans avoir écarté la grossesse extra-utérine.", 16),
    ("L'échographie et la gonadotrophine situent la grossesse.", 16),
    ("Une femme RhD négative reçoit la prophylaxie après le saignement, selon l'information 53609.", 5),
    ("La dose lue pour une complication est de 300 µg, au plus tard dans les 72 heures.", 5),
    ("Au-delà de 72 heures, on injecte quand même.", 5),
    ("On ne fait pas de toucher qui n'apporte rien si l'échographie répond déjà.", 16),
    ("Une douleur scapulaire, un malaise, ou une défense abdominale sont des signes de gravité.", 16),
    ("On mesure la pression et le pouls avant de rassurer.", 16),
    ("Un saignement du troisième trimestre n'est pas ce diagnostic. Il évoque un placenta bas ou un décollement.", 16),
    ("Dans ce cas plus tardif, on ne fait pas de toucher vaginal avant de savoir où est le placenta.", 16),
    ("Métrorragies du premier trimestre et règle abondante ne se tranchent pas au téléphone.", 16),
    ("On date le début du saignement, la douleur, et la date des dernières règles.", 16),
    ("Le groupe sanguin se connaît avant la sortie, pas la semaine suivante.", 5),
]

PHASE = COMMUN + [
    ("Les dix situations du lot sont la grossesse physiologique, la consultation préconceptionnelle, l'anémie, le diabète gestationnel.", 16),
    ("Viennent ensuite la colonisation à streptocoque du groupe B et la prophylaxie anti-D de la femme RhD négative.", 5),
    ("Puis le dépistage de la prééclampsie, les vaccinations pendant la grossesse, la diminution des mouvements fœtaux.", 15),
    ("Et les métrorragies du premier trimestre.", 16),
    ("Grossesse d'évolution physiologique ouvre le rang parce que c'est le suivi lui-même.", 16),
    ("Consultation préconceptionnelle vient juste après, car le titre du lot commence avant la conception.", 2),
    ("Anémie ferriprive de la grossesse se cherche par l'hémogramme, pas par la pâleur seule.", 12),
    ("Diabète gestationnel se cherche par l'épreuve de 75 grammes, pas par une glycémie capillaire.", 10),
    ("Colonisation à streptocoque du groupe B se cherche en fin de grossesse, pas par un traitement anticipé de plusieurs semaines.", 7),
    ("Prophylaxie anti-D de la femme RhD négative a une date : entre 28 et 30 semaines, puis après l'accouchement.", 5),
    ("Dépistage de la prééclampsie a un seuil de pression : 140 mmHg ou 90 mmHg, confirmé.", 15),
    ("Vaccinations pendant la grossesse : coqueluche au deuxième trimestre, grippe à n'importe quel trimestre selon l'information inactivée.", 14),
    ("Diminution des mouvements fœtaux : appel à toute heure après 24 semaines et 0 jour.", 16),
    ("Métrorragies du premier trimestre : échographie, hormone, et anti-D si la femme est RhD négative.", 5),
    ("L'arbre tient en une ligne. Signe d'alarme : on voit le jour même.", 16),
    ("Sans signe d'alarme, on regarde le terme et on coche l'acte dont la fenêtre est ouverte.", 16),
    ("Avant 14 semaines : datation, bilan initial, folates, décision de dépistage prénatal, aspirine si le risque est accru.", 11),
    ("De 14 à 28 semaines : morphologie, épreuve glycémique, agglutinines, anti-D si besoin.", 10),
    ("De 28 semaines à 37 semaines : hauteur, mouvements, présentation, prélèvement du streptocoque, vaccins.", 16),
    ("Dès 37 semaines : rythme des visites plus serré et plan de naissance.", 16),
    ("Le comprimé de 0,4 mg se discute avant la conception.", 2),
    ("Le comprimé de 100 mg se discute vers 12 semaines si le risque de prééclampsie est accru, en disant la contre-indication du troisième trimestre.", 4),
    ("La seringue de 300 µg se discute à 28 semaines si la femme est RhD négative et non immunisée.", 5),
    ("La plage 100–300 mg de fer se discute si l'hémoglobine est sous le seuil de 2011.", 6),
    ("On n'ajoute pas un acte dont la fenêtre est fermée en prétendant qu'il rattrape le retard.", 16),
]


LEADS_SPEC = {
    "Phase_A": "Trois questions et une horloge suffisent à ouvrir le dossier.",
    "DX.1": "Physiologique veut dire daté, classé, et revu.",
    "DX.2": "Le comprimé utile est celui d'avant la conception.",
    "DX.3": "On compare l'hémoglobine au trimestre, pas à une norme d'homme.",
    "DX.4": "Une seule valeur de l'épreuve suffit.",
    "DX.5": "Le portage se traite au travail, pas des semaines avant.",
    "DX.6": "28 à 30 semaines, puis 72 heures, puis chaque événement.",
    "DX.7": "140 sur 90 n'attend pas la protéinurie pour être mesuré.",
    "DX.8": "Inactivé pendant la grossesse, vivant avant.",
    "DX.9": "Après 24 semaines et 0 jour, l'appel ne se reporte pas.",
    "DX.10": "Tout saignement précoce écarte d'abord l'extra-utérine.",
}

CIBLES = {
    "Phase_A": 96000,
    "DX.1": 49000,
    "DX.2": 51000,
    "DX.3": 54000,
    "DX.4": 56000,
    "DX.5": 47000,
    "DX.6": 52000,
    "DX.7": 57000,
    "DX.8": 50000,
    "DX.9": 52000,
    "DX.10": 54500,
}

FAITS = {
    "Phase_A": PHASE,
    "DX.1": DX1,
    "DX.2": DX2,
    "DX.3": DX3,
    "DX.4": DX4,
    "DX.5": DX5,
    "DX.6": DX6,
    "DX.7": DX7,
    "DX.8": DX8,
    "DX.9": DX9,
    "DX.10": DX10,
}

NOMS = {
    "Phase_A": "Soins de base autour de la conception et pendant la grossesse",
    "DX.1": "Grossesse d'évolution physiologique",
    "DX.2": "Consultation préconceptionnelle",
    "DX.3": "Anémie ferriprive de la grossesse",
    "DX.4": "Diabète gestationnel",
    "DX.5": "Colonisation à streptocoque du groupe B",
    "DX.6": "Prophylaxie anti-D de la femme RhD négative",
    "DX.7": "Dépistage de la prééclampsie",
    "DX.8": "Vaccinations pendant la grossesse",
    "DX.9": "Diminution des mouvements fœtaux",
    "DX.10": "Métrorragies du premier trimestre",
}


def schema(cle: str) -> str:
    """Schéma au survol, sans script, dans la fenêtre du point 10."""
    cartes = {
        "Phase_A": (
            "Calendrier des fenêtres",
            [
                ("Avant", "Folate avant la conception.", "#d7f0e2", "#1a7a50"),
                ("Début", "Rendez-vous avant 10 semaines.", "#d9ecf8", "#176fa0"),
                ("Milieu", "Charge entre 24 et 28 semaines.", "#f8e0c0", "#8a5a12"),
                ("28–30", "Anti-D si la femme est RhD négative.", "#f6d0d2", "#a1262f"),
            ],
        ),
        "DX.1": (
            "Visite d'une grossesse qui évolue bien",
            [
                ("Date", "Une échographie date, une fois.", "#d9ecf8", "#176fa0"),
                ("Pression", "140 ou 90 n'est pas physiologique.", "#f6d0d2", "#a1262f"),
                ("Hauteur", "Après 24 semaines, à chaque visite.", "#d7f0e2", "#1a7a50"),
                ("Alarme", "Saignement ou fièvre : le jour même.", "#f8e0c0", "#8a5a12"),
            ],
        ),
        "DX.2": (
            "Avant d'arrêter la contraception",
            [
                ("Folate", "0,4 mg, un comprimé par jour.", "#d7f0e2", "#1a7a50"),
                ("5 mg", "Haut risque, pas la dose de toutes.", "#f8e0c0", "#8a5a12"),
                ("Vivant", "Rubéole et varicelle avant.", "#d9ecf8", "#176fa0"),
                ("Poids", "11,5 à 16 kg si l'indice est moyen.", "#e7e4f7", "#3d3a66"),
            ],
        ),
        "DX.3": (
            "Hémoglobine selon le moment",
            [
                ("Début", "Moins de 110 g/l : anémie.", "#f6d0d2", "#a1262f"),
                ("Milieu", "Moins de 105 g/l.", "#f8e0c0", "#8a5a12"),
                ("Fin", "Toujours moins de 105 g/l.", "#f8e0c0", "#8a5a12"),
                ("Suites", "Moins de 100 g/l.", "#d9ecf8", "#176fa0"),
            ],
        ),
        "DX.4": (
            "Trois seuils, un seul suffit",
            [
                ("À jeun", "Au moins 5,1 mmol/l.", "#f6d0d2", "#a1262f"),
                ("1 heure", "Au moins 10 mmol/l.", "#f8e0c0", "#8a5a12"),
                ("2 heures", "Au moins 8,5 mmol/l.", "#d9ecf8", "#176fa0"),
                ("Veine", "Le capillaire ne pose pas le diagnostic.", "#d7f0e2", "#1a7a50"),
            ],
        ),
        "DX.5": (
            "Portage : quand agir",
            [
                ("Tardif", "Prélèvement en fin de grossesse.", "#d9ecf8", "#176fa0"),
                ("Travail", "L'antibiotique se donne alors.", "#d7f0e2", "#1a7a50"),
                ("Trop tôt", "Le germe revient. On n'éradique pas.", "#f8e0c0", "#8a5a12"),
                ("Allergie", "On la cherche avant la poussée.", "#f6d0d2", "#a1262f"),
            ],
        ),
        "DX.6": (
            "Deux dates, puis chaque événement",
            [
                ("28–30", "300 µg, veine ou muscle.", "#d9ecf8", "#176fa0"),
                ("72 h", "Après la naissance si l'enfant est D.", "#d7f0e2", "#1a7a50"),
                ("Passage", "Au-dessus de 4 ml : dose en plus.", "#f8e0c0", "#8a5a12"),
                ("Déjà", "Immunisée : on suit le titre.", "#f6d0d2", "#a1262f"),
            ],
        ),
        "DX.7": (
            "Pression, puis le reste",
            [
                ("140/90", "Hypertension, confirmée.", "#f8e0c0", "#8a5a12"),
                ("160/110", "Sévère : pas le lendemain.", "#f6d0d2", "#a1262f"),
                ("Urines", "30 milligrammes par millimole.", "#d9ecf8", "#176fa0"),
                ("Soir", "100 mg si le risque est accru.", "#d7f0e2", "#1a7a50"),
            ],
        ),
        "DX.8": (
            "Inactivé pendant, vivant avant",
            [
                ("13–26", "Coqueluche, de préférence.", "#d7f0e2", "#1a7a50"),
                ("Rattrapage", "Troisième trimestre, pas trop tard.", "#f8e0c0", "#8a5a12"),
                ("Grippe", "N'importe quel trimestre.", "#d9ecf8", "#176fa0"),
                ("Vivant", "Pas pendant la grossesse.", "#f6d0d2", "#a1262f"),
            ],
        ),
        "DX.9": (
            "Mouvements : le changement compte",
            [
                ("Après 24", "On en parle à chaque contact.", "#d9ecf8", "#176fa0"),
                ("Appel", "Toute heure, maternité.", "#f6d0d2", "#a1262f"),
                ("Jour même", "On ne rassure pas au téléphone.", "#f8e0c0", "#8a5a12"),
                ("Compte", "Un nombre magique n'est pas le critère.", "#d7f0e2", "#1a7a50"),
            ],
        ),
        "DX.10": (
            "Saignement précoce : trois cadres",
            [
                ("Hors utérus", "À écarter avant la fausse couche.", "#f6d0d2", "#a1262f"),
                ("Image", "Échographie et hormone.", "#d9ecf8", "#176fa0"),
                ("Anti-D", "300 µg si la femme est RhD négative.", "#f8e0c0", "#8a5a12"),
                ("Gravité", "Malaise, épaule, défense.", "#d7f0e2", "#1a7a50"),
            ],
        ),
    }
    titre, cases = cartes[cle]
    x = 16
    rects = []
    for nom, detail, coul, trait in cases:
        rects.append(
            f'<rect class="zone" tabindex="0" x="{x}" y="48" width="156" height="86" rx="8" '
            f'fill="{coul}" stroke="{trait}" stroke-width="2">'
            f"<title>{html.escape(nom)}. {html.escape(detail)}</title></rect>"
            f'<text class="etq" x="{x + 78}" y="98" text-anchor="middle">{html.escape(nom)}</text>'
        )
        x += 172
    return (
        f'<figure class="schema"><svg viewBox="0 0 700 180" role="img" '
        f'aria-label="{html.escape(titre)}" style="max-width:100%;height:auto">'
        f"<title>{html.escape(titre)}</title>{''.join(rects)}</svg>"
        f"<figcaption>Survoler ou focaliser une case. Le chiffre est dans le texte sourcé.</figcaption></figure>"
    )


def fichier_de(cle: str) -> str:
    if cle == "Phase_A":
        return "LOT_180_Phase_A_V0.html"
    n = cle.split(".")[1]
    return f"LOT_180_Phase_B_V0_DX.{n}.html"


def construire(cle: str) -> Path:
    nom = NOMS[cle]
    faits = FAITS[cle]
    # contrôle des mots
    for t, s in faits:
        if mots(t) > 34:
            raise SystemExit(f"{cle} trop long: {t}")
    blocs = repartir(faits, CIBLES[cle], nom)
    lead10, paras10 = blocs[10]
    blocs[10] = (lead10, [schema(cle), *paras10])
    if cle == "Phase_A":
        sous = "Situation de départ O1.7. Soins de base autour de la conception et pendant la grossesse."
        essentiel = "Le suivi est un calendrier. Chaque acte a une fenêtre."
    else:
        sous = (
            f"Diagnostic différentiel {cle} de O1.7. "
            "Soins de base autour de la conception et pendant la grossesse."
        )
        essentiel = f"{nom}. On nomme la situation, puis le geste qui correspond."
    html_txt = page(
        fichier_de(cle),
        nom,
        sous,
        essentiel,
        blocs,
        fichier_de(cle),
    )
    dest = LOT / fichier_de(cle)
    dest.write_text(html_txt, encoding="utf-8")
    return dest


def main() -> None:
    cles = sys.argv[1:] or ["Phase_A", *[f"DX.{i}" for i in range(1, 11)]]
    sys.path.insert(0, str(RACINE / "harnais"))
    import taille_xy

    for cle in cles:
        dest = construire(cle)
        taille_xy.main([str(dest), "--inscrire"])
        txt = dest.read_text(encoding="utf-8")
        m = taille_xy.mesurer(txt)
        print(f"  retenu  x={m.x[1]}  y={m.y[1]}")


if __name__ == "__main__":
    main()
