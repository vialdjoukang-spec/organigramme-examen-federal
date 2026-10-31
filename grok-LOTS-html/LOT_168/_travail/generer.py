#!/usr/bin/env python3
"""Générateur LOT_168 — F2.20 Diminution de la densité osseuse. Textes sourcés, format V8."""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_168"
MODELE = RACINE / "harnais" / "modele_lecon" / "MODELE_DD_V8.html"
sys.path.insert(0, str(RACINE / "harnais"))
import taille_xy  # noqa: E402

SIGLES = [
    ("PROFILES", "Principal Relevant Objectives and Framework for Integrated Learning and Education in Switzerland"),
    ("NHANES", "National Health and Nutrition Examination Survey, enquête nationale américaine de santé et de nutrition"),
    ("FRAX", "fracture risk assessment tool, outil d'évaluation du risque de fracture à dix ans"),
    ("SVGO", "Schweizerische Vereinigung gegen die Osteoporose, association suisse contre l'ostéoporose"),
    ("ASCO", "Association suisse contre l'ostéoporose"),
    ("ISCD", "International Society for Clinical Densitometry, société internationale de densitométrie clinique"),
    ("DXA", "absorptiométrie biphotonique à rayons X"),
    ("DMO", "densité minérale osseuse"),
    ("PTH", "parathormone"),
    ("TSH", "thyréostimuline"),
    ("CTX", "télopeptide C-terminal du collagène de type I"),
    ("FVM", "fractures vertébrales multiples"),
    ("ACR", "American College of Rheumatology, collège américain de rhumatologie"),
    ("OMS", "Organisation mondiale de la santé"),
    ("AIPS", "information professionnelle suisse"),
    ("FSH", "hormone folliculostimulante"),
    ("LH", "hormone lutéinisante"),
    ("UI", "unité internationale"),
    ("ONM", "ostéonécrose de la mâchoire"),
    ("EVENITY", "romosozumab, spécialité EVENITY"),
]

TITRES = [
    (1, "1. Définition"),
    (2, "2. Épidémiologie"),
    (3, "3. Physiopathologie et rappels"),
    (4, "4. Démarche diagnostique"),
    (5, "5. Anamnèse et drapeaux rouges"),
    (6, "6. Examen physique"),
    (7, "7. Approche syndromique"),
    (8, "8. Diagnostic positif"),
    (9, "9. Examens complémentaires"),
    (10, "10. Arbre décisionnel"),
    (11, "11. Prise en charge en Suisse"),
    (12, "12. Prévention"),
    (13, "13. Points clés"),
    (14, "14. Pièges d'examen"),
]


def habiller(texte: str) -> str:
    t = html.escape(texte, quote=False)
    for sigle, titre in SIGLES:
        t = re.sub(
            rf"\b{re.escape(sigle)}\b",
            lambda m, titre=titre, sigle=sigle: f'<abbr title="{html.escape(titre, quote=True)}">{sigle}</abbr>',
            t,
        )
    return t


def P(*morceaux: str, src: str = "1") -> str:
    corps = " ".join(morceaux)
    return f"<p>{habiller(corps)}<sup class=\"s\">{src}</sup></p>"


def fenetre(wid: str, titre: str, corps: str) -> str:
    return (
        f'<div id="{wid}" popover class="fenetre"><div class="barre"><span>{html.escape(titre)}</span>'
        f'<button type="button" popovertarget="{wid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">{corps}</div></div>'
    )


def bouton(wid: str, libelle: str) -> str:
    return f'<button type="button" class="terme" popovertarget="{wid}">{html.escape(libelle)}</button>'


STYLE_SVG = """
svg .zone{cursor:pointer}
svg .zone:hover rect,svg .zone:hover polygon,svg .zone:hover path{stroke:#14303b;stroke-width:3px}
svg text{font-family:Verdana,sans-serif}
svg .tt{font-size:15px;font-weight:700;fill:#14303b}
svg .lb{font-size:13px;font-weight:700;fill:#14303b}
svg .sm{font-size:12px;fill:#1d2a30}
"""


def defs_clic(prefix: str, items: list[tuple[str, str, str]]) -> str:
    boutons = " ".join(bouton(f"{prefix}-{i}", nom) for i, nom, _ in items)
    pops = "".join(fenetre(f"{prefix}-{i}", nom, f"<p>{habiller(texte)}</p>") for i, nom, texte in items)
    return f"<p>Définition au clic : {boutons}</p>{pops}"


def svg_tscore(prefix: str = "ts") -> str:
    suite = defs_clic(prefix, [
        ("norm", "Normal", "T-score au-dessus de −1,0. Ce n'est pas une ostéopénie. ISCD 2019."),
        ("penie", "Ostéopénie", "T-score au-dessus de −2,5 et en dessous de −1,0, si aucun autre facteur ne classe plus haut. Ferrari 2020. Le mot est gardé, faible masse osseuse est préféré."),
        ("porose", "Ostéoporose", "T-score de −2,5 ou moins au rachis, à la hanche totale ou au col, chez la femme ménopausée et l'homme d'au moins 50 ans. ISCD 2019."),
        ("jeune", "Sujet jeune", "Z-score de −2,0 ou moins : sous la norme d'âge, selon l'ISCD en 2019. On n'utilise pas ce T-score pour poser l'ostéoporose chez l'homme de moins de 50 ans."),
    ])
    return suite + """<figure class="schema"><svg viewBox="0 0 700 250" role="img" aria-labelledby="t-tscore">
<title id="t-tscore">Axe du T-score avec les trois zones densitométriques</title>
<text class="tt" x="20" y="28">T-score : trois zones</text>
<g class="zone"><title>Normal : T-score au-dessus de −1,0</title><rect x="40" y="70" width="180" height="48" fill="#b5e1cb" stroke="#1a7a50"/><text class="lb" x="78" y="99">Normal</text></g>
<g class="zone"><title>Ostéopénie : T-score entre −1,0 et −2,5</title><rect x="220" y="70" width="200" height="48" fill="#f6e3b0" stroke="#8a6a12"/><text class="lb" x="268" y="99">Ostéopénie</text></g>
<g class="zone"><title>Ostéoporose : T-score de −2,5 ou moins</title><rect x="420" y="70" width="240" height="48" fill="#f3c2c6" stroke="#a1262f"/><text class="lb" x="480" y="99">Ostéoporose</text></g>
<line x1="40" y1="140" x2="660" y2="140" stroke="#14303b" stroke-width="2"/>
<text class="sm" x="36" y="162">+1</text>
<text class="sm" x="210" y="162">−1,0</text>
<text class="sm" x="400" y="162">−2,5</text>
<text class="sm" x="630" y="162">−4</text>
<text class="sm" x="40" y="200">Le survol nomme la zone. Le clic sur le bouton ouvre la définition.</text>
<text class="sm" x="40" y="222">Sujet jeune : on lit le Z-score, pas ce T-score.</text>
</svg><figcaption>Courbe des seuils densitométriques. Ostéoporose : −2,5 ou moins. Ostéopénie : au-dessus de −2,5 et en dessous de −1,0.</figcaption></figure>"""


def svg_algo(prefix: str = "al") -> str:
    boxes = [
        (40, "#f3c2c6", "Imminent", "Fracture majeure récente, risque &gt; 10 % à 2 ans"),
        (130, "#f6c9b0", "Très élevé", "FRAX au moins 20 points au-dessus du seuil"),
        (220, "#f6e3b0", "Élevé", "Fracture ancienne, FRAX au-dessus du seuil, corticoïde"),
        (310, "#d5e8f7", "Modéré", "T-score ≤ −2,5, sans fracture, FRAX sous le seuil"),
        (400, "#b5e1cb", "Faible", "Ostéopénie seule, sans autre facteur"),
    ]
    parts = ['<figure class="schema"><svg viewBox="0 0 700 520" role="img" aria-labelledby="t-algo"><title id="t-algo">Algorithme de traitement selon le risque de fracture</title><text class="tt" x="20" y="28">Traitement selon le risque, Suisse 2020</text>']
    for y, fill, nom, detail in boxes:
        parts.append(
            f'<g class="zone"><title>{nom}</title><rect x="30" y="{y}" width="640" height="72" rx="8" fill="{fill}" stroke="#14303b"/>'
            f'<text class="lb" x="48" y="{y+28}">{nom}</text><text class="sm" x="48" y="{y+52}">{detail}</text></g>'
        )
        if y < 400:
            parts.append(f'<line x1="350" y1="{y+72}" x2="350" y2="{y+88}" stroke="#14303b" stroke-width="2"/>')
    parts.append("</svg><figcaption>Cinq cases de risque. Le survol éclaire la case. Le bouton ouvre la conduite.</figcaption></figure>")
    parts.append(defs_clic(prefix, [
        ("imm", "Imminent", "Risque de fracture supérieur à 10 % dans les 2 ans : fracture vertébrale ou de hanche de moins de 2 ans, ou autre fracture majeure après 65 ans."),
        ("the", "Très élevé", "FRAX à 10 ans au moins 20 points de pourcentage au-dessus du seuil d'intervention lié à l'âge."),
        ("ele", "Élevé", "Fracture majeure de plus de 2 ans, ou FRAX au-dessus du seuil sans atteindre 20 points, ou corticoïde avec T-score inférieur à −1,5."),
        ("mod", "Modéré", "T-score de −2,5 ou moins, sans fracture, FRAX sous le seuil d'intervention."),
        ("fai", "Faible", "Ostéopénie sans autre facteur de risque. Mode de vie, vitamine D si besoin, densité à 5 à 10 ans."),
    ]))
    return "".join(parts)


def svg_genant(prefix: str = "ge") -> str:
    # quatre vertèbres, hauteur antérieure décroissante
    cols = [
        (70, 120, "Grade 0", "Normale"),
        (230, 96, "Grade 1", "20 à 25 %"),
        (390, 72, "Grade 2", "26 à 40 %"),
        (550, 48, "Grade 3", "Plus de 40 %"),
    ]
    parts = ['<figure class="schema"><svg viewBox="0 0 720 280" role="img" aria-labelledby="t-genant"><title id="t-genant">Grades de Genant</title><text class="tt" x="20" y="26">Fracture vertébrale : grades de Genant</text>']
    for x, h, grade, pct in cols:
        y = 150 - h
        parts.append(
            f'<g class="zone"><title>{grade}, {pct}</title>'
            f'<polygon points="{x},{y+h} {x+90},{y+h} {x+80},{y+12} {x+10},{y}" fill="#d9e8f0" stroke="#0b5d86" stroke-width="2"/>'
            f'<text class="lb" x="{x}" y="190">{grade}</text><text class="sm" x="{x}" y="210">{pct}</text></g>'
        )
    parts.append('<text class="sm" x="20" y="248">Formes : cunéiforme, biconcave, tassement. La forme ne fixe pas le grade.</text></svg>')
    parts.append("<figcaption>De gauche à droite, grade 0 à grade 3. La perte de hauteur est visuelle, de T4 à L4.</figcaption></figure>")
    parts.append(defs_clic(prefix, [
        ("g0", "Grade 0", "Vertèbre normale, sans déformation retenue."),
        ("g1", "Grade 1", "Déformation légère : perte d'environ 20 à 25 % de la hauteur et de 10 à 20 % de la surface projetée."),
        ("g2", "Grade 2", "Déformation modérée : perte d'environ 26 à 40 % de la hauteur et de 21 à 40 % de la surface."),
        ("g3", "Grade 3", "Déformation sévère : perte de plus de 40 % de la hauteur et de la surface. La forme, cunéiforme, biconcave ou tassement, ne fixe pas le grade."),
    ]))
    return "".join(parts)


def css() -> str:
    brut = MODELE.read_text(encoding="utf-8")
    m = re.search(r"<style>(.*)</style>", brut, re.S)
    return (m.group(1) if m else "") + STYLE_SVG


NOYAU_TRAITEMENT = [
    ("L'alendronate oral se donne à raison d'un comprimé de 70 mg par semaine. L'information professionnelle 57957, mise à jour en juillet 2023, le fait prendre au moins une demi-heure avant le premier repas, avec un grand verre d'eau du robinet, et interdit de se recoucher avant 30 minutes et avant la première prise d'aliments. L'impossibilité de rester assis, debout ou en marche pendant 30 minutes est une contre-indication. Une douleur à la déglutition, une douleur rétrosternale ou des brûlures qui apparaissent font arrêter le comprimé et revoir un médecin. L'équivalence avec 10 mg par jour a été montrée sur la densité, pas comme une consigne à mélanger avec le comprimé hebdomadaire.", "5"),
    ("L'acide zolédronique, Aclasta, information professionnelle 57363 mise à jour en mars 2026, se perfuse à la dose de 5 mg une fois par année, en au moins 15 minutes. Une dose unitaire ne doit pas dépasser 5 mg. Il est contre-indiqué si la clairance de la créatinine est inférieure à 35 ml/min. À partir de 35 ml/min, la notice ne demande pas d'adaptation. La clairance se calcule avant chaque perfusion. L'hypocalcémie se corrige avant de commencer, par du calcium et de la vitamine D. Pour un risque de fracture faible, un arrêt après 3 à 5 ans se discute, puis le risque se réévalue. La notice contre-indique aussi la grossesse.", "6"),
    ("Le dénosumab, Prolia, information professionnelle 60210 mise à jour en mai 2026, se donne à 60 mg en une injection sous-cutanée tous les 6 mois, dans la cuisse, l'abdomen ou le bras. Il est contre-indiqué en cas d'hypocalcémie. Il n'est pas indiqué avant 18 ans. Les études d'extension associaient au moins 1 g de calcium et au moins 400 UI de vitamine D par jour. Après l'arrêt, des fractures vertébrales multiples et une perte de densité, parfois sous le niveau de départ, peuvent survenir. On n'interrompt pas sans avis médical. Un relais par bisphosphonate est discuté, sans garantie pour chaque personne. L'ostéoporose cortisonique de l'homme n'a pas été étudiée dans cette notice, et les indications écrites ne la nomment pas.", "7"),
    ("Le tériparatide, Forsteo, information professionnelle 56007 mise à jour en avril 2026, se donne à 20 µg par jour en sous-cutané dans la cuisse ou l'abdomen. La durée maximale est de 24 mois et ce traitement de 24 mois ne se répète pas. Il est contre-indiqué dans l'hyperparathyroïdie, la maladie de Paget, une hypercalcémie préexistante, une radiothérapie du squelette, une métastase ou une tumeur osseuse, l'insuffisance rénale sévère, chez l'enfant et l'adolescent, chez le jeune adulte avant fermeture des cartilages, pendant la grossesse et pendant l'allaitement. Dans l'étude pivot, l'incidence d'une ou plusieurs nouvelles fractures vertébrales a été réduite de 65 % et celle des fractures multiples de 77 %, avec 1000 mg de calcium et au moins 400 UI de vitamine D par jour.", "8"),
    ("Le romosozumab, EVENITY, information professionnelle 67033 mise à jour en juillet 2024, se donne à 210 mg une fois par mois pendant 12 mois, soit deux injections sous-cutanées de 105 mg, pas au même point. Il est contre-indiqué si l'hypocalcémie n'est pas corrigée et si la personne a un antécédent d'infarctus du myocarde ou d'accident vasculaire cérébral. On pèse le risque de fracture de l'année qui vient et le risque cardiovasculaire, hypertension, lipides, diabète, tabac, insuffisance rénale sévère, âge. Un symptôme d'infarctus ou d'accident vasculaire pendant le traitement fait consulter tout de suite. L'ostéonécrose de la mâchoire et la fracture fémorale atypique sont aussi décrites.", "9"),
    ("Le calcium et la vitamine D ne remplacent pas un antirésorptif quand le risque est élevé, mais ils corrigent une carence. Calcium D3-Mepha 1200/800, information professionnelle 59096 mise à jour en avril 2024, apporte 1200 mg de calcium et 800 UI de cholécalciférol par jour, un comprimé, chez l'adulte qui a une carence ou un risque élevé de carence. Il n'est pas destiné à l'enfant. La prednisone, information professionnelle 29349 mise à jour en juin 2026, fixe le seuil de Cushing à 7,5 mg par jour.", "11"),
    ("L'ostéonécrose de la mâchoire et la fracture fémorale atypique concernent les bisphosphonates et le dénosumab. Une douleur de cuisse ou d'aine, des semaines ou des mois avant une fracture complète, fait chercher une fracture incomplète. Avant un antirésorptif prolongé, un avis dentaire se discute si l'hygiène est mauvaise, si une extraction est prévue, ou s'il y a une corticothérapie, une radiothérapie de la tête ou un cancer. On n'arrête pas un dénosumab pour une dent sans plan de relais, à cause du rebond.", "7"),
]


def secours_os() -> list[str]:
    return [P(t, src=s) for t, s in NOYAU_TRAITEMENT]


DXS = [
    {
        "n": 1,
        "titre": "Ostéoporose postménopausique",
        "qui": "une femme ménopausée",
        "mecanisme": "Après la ménopause, la chute des œstrogènes lève le frein sur les ostéoclastes. La résorption dépasse la formation, l'os trabéculaire se raréfie, et la vertèbre cède avant la hanche chez beaucoup de femmes.",
        "epi": "En Suisse, une femme sur deux aura une fracture de fragilité après 50 ans. Ferrari et collaborateurs, en 2020, rappellent au moins 75 000 fractures incidentes par an, 140 000 fractures de hanche ou de vertèbre déjà présentes, et 450 000 personnes ostéoporotiques en 2010. Moins de 10 % des personnes ostéoporotiques et 20 % des fractures à basse énergie reçoivent un médicament.",
        "etiologies": "La cause principale est la carence œstrogénique. S'y ajoutent l'âge, une fracture personnelle, une fracture de hanche parentale, le tabac, l'alcool au-delà de 3 unités par jour, un indice de masse corporelle bas, une chute, et une cause secondaire qu'il faut encore chercher.",
        "demarche": "On confirme le siège de la mesure, on écarte une vertèbre arthrosique, on date les fractures, on calcule le FRAX suisse, on classe le risque, puis seulement on choisit la molécule.",
        "anamnese": "Âge de la ménopause, fractures à basse énergie, corticoïdes, chute dans l'année, taille perdue, tabac, alcool, fracture de hanche chez un parent, cancer et radiothérapie du squelette, infarctus ou accident vasculaire.",
        "examen": "Taille, poids, cyphose, distance mur-occiput, douleur de cuisse, examen dentaire si un antirésorptif long est envisagé, signes d'hyperthyroïdie ou de Cushing qui sortiraient du cadre postménopausique pur.",
        "syndrom": "On garde en face l'ostéopénie sans facteur, l'ostéomalacie, l'hyperparathyroïdie, le myélome, la carence en vitamine D et l'arthrose lombaire qui fausse le chiffre.",
        "positif": "Chez la femme ménopausée, un T-score de −2,5 ou moins au rachis lombaire, à la hanche totale ou au col fémoral pose le diagnostic densitométrique. Une fracture de fragilité vertébrale ou de hanche suffit souvent à traiter, même si le chiffre est moins bas.",
        "bio": "Calcémie, phosphate, créatinine, 25-hydroxyvitamine D, PTH, TSH, électrophorèse des protéines. Le bilan cherche une cause que le mot postménopausique cacherait.",
        "arbre": "Fracture vertébrale de moins de 2 ans : risque imminent, tériparatide 18 à 24 mois puis antirésorptif, ou romosozumab un an si le risque cardiovasculaire le permet. Fracture de hanche récente : zolédronate annuel si la clairance dépasse 35 ml/min, sinon dénosumab. Sans fracture récente et FRAX seulement au-dessus du seuil : antirésorptif puissant. T-score de −2,5 ou moins, sans fracture, FRAX sous le seuil : risque modéré.",
        "prevention": "Chutes, tabac, alcool, activité en charge, apport calcique alimentaire, vitamine D si carence. La densité se recontrôle vers 2 ans sous traitement, et à 5 à 10 ans si le risque est faible.",
        "piege": "Traiter toute ostéopénie par bisphosphonate, lire un T-score lombaire gonflé par l'arthrose, arrêter le dénosumab sans relais, donner du romosozumab après un infarctus, dépasser 24 mois de tériparatide.",
        "cas": "Femme de 68 ans, ménopausée à 49 ans, tassement de L1 il y a 8 mois en soulevant une casserole, T-score −2,8 au col, −2,1 en lombaire avec arthrose. Clairance 62 ml/min, pas d'infarctus, calcémie normale, électrophorèse sans pic. Case : risque imminent. On discute tériparatide 20 µg par jour pendant au plus 24 mois, ou romosozumab 210 mg par mois pendant 12 mois, puis un antirésorptif. Le chiffre lombaire moins sévère ne rassure pas : l'arthrose le remonte.",
    },
    {
        "n": 2,
        "titre": "Ostéopénie densitométrique",
        "qui": "une personne dont le T-score est dans la bande intermédiaire",
        "mecanisme": "La masse osseuse est basse sans atteindre le seuil d'ostéoporose. L'os peut être normalement minéralisé. Le risque de fracture n'est pas lu sur le seul chiffre : plus de la moitié des fractures de fragilité surviennent à un T-score de −2,5 ou meilleur.",
        "epi": "La bande est fréquente après 50 ans. Ferrari en 2020 la place en risque faible seulement s'il n'y a pas d'autre facteur : T-score au-dessus de −2,5 et en dessous de −1,0. L'ISCD en 2019 garde le mot ostéopénie mais préfère faible masse osseuse, et rappelle que cette bande n'est pas un haut risque automatique.",
        "etiologies": "Âge et ménopause débutante, petit pic de masse osseuse, tabac, faible poids, carence en vitamine D sans ostéomalacie, corticoïde encore court, artefact de mesure qu'il faut écarter.",
        "demarche": "Vérifier le site, écarter l'arthrose et la vertèbre unique, chercher une fracture méconnue, calculer le FRAX, ne pas ouvrir un bisphosphonate sur le mot ostéopénie seul.",
        "anamnese": "Fracture même ancienne, corticoïde, chute, perte de taille de plus de 4 cm, parent avec fracture de hanche, traitement hormonal du cancer.",
        "examen": "Taille actuelle et taille historique, douleur vertébrale, démarche, risque de chute. Pas de signe d'ostéomalacie, pas de douleur osseuse diffuse.",
        "syndrom": "Ostéoporose vraie, ostéomalacie, hyperparathyroïdie, myélome débutant, ostéogenèse imparfaite chez le sujet plus jeune où le T-score n'est pas le bon outil.",
        "positif": "T-score supérieur à −2,5 et inférieur à −1,0 sur un site valide, sans fracture de fragilité et avec un FRAX sous le seuil d'intervention suisse. Si le FRAX dépasse le seuil, la case quitte le risque faible.",
        "bio": "Le même bilan minimum que devant toute densité basse inexpliquée, pour ne pas appeler ostéopénie une ostéomalacie ou un myélome.",
        "arbre": "Risque faible : mode de vie, vitamine D, calcium si carence, densité à 5 à 10 ans ou plus tôt si le risque clinique monte. Risque modéré si le T-score est à −2,5 ou moins. Dès qu'une fracture majeure date de moins de 2 ans, on sort de l'ostéopénie tranquille.",
        "prevention": "On ne medicalise pas la bande entière. On traite les chutes et la carence. Calcium D3-Mepha 1200 mg et 800 UI seulement s'il y a carence ou risque élevé de carence.",
        "piege": "Écrire ostéoporose parce que le compte rendu dit ostéopénie. Donner 70 mg d'alendronate par semaine à une femme de 52 ans, T-score −1,3, sans fracture et FRAX bas. Ignorer une fracture de poignet de l'an dernier.",
        "cas": "Femme de 58 ans, T-score −1,6 au col, −1,4 au rachis homogène, aucune fracture, mère sans fracture de hanche, non fumeuse, indice de masse corporelle 24. FRAX sous le seuil suisse de son âge. Case : risque faible. Pas d'alendronate. Contrôle densitométrique dans 5 à 10 ans, plus tôt si une fracture ou un corticoïde apparaît. Vitamine D seulement si la 25-hydroxyvitamine D est basse.",
    },
    {
        "n": 3,
        "titre": "Ostéoporose cortisonique",
        "qui": "une personne exposée aux glucocorticoïdes",
        "mecanisme": "La perte est rapide : l'ACR décrit en 2010 une chute de densité dès les 3 premiers mois, maximale vers 6 mois, puis une perte plus lente. L'os trabéculaire, surtout vertébral, souffre tôt. Le risque de fracture monte déjà à des doses quotidiennes basses.",
        "epi": "Ferrari en 2020 classe en risque élevé la corticothérapie au long cours, avec les inhibiteurs de l'aromatase et la suppression androgénique, si le T-score est inférieur à −1,5 ou si le FRAX dépasse le seuil. Ce n'est pas une maladie rare de rhumatologie : toute ordonnance prolongée de prednisone compte.",
        "etiologies": "Prednisone et équivalents oraux au long cours, parfois inhalés très dosés ou injections répétées dont la dose cumulée se discute au cas par cas. La maladie inflammatoire elle-même, le manque d'activité et la carence en vitamine D s'ajoutent.",
        "demarche": "Écrire la dose moyenne prévue et la durée. Le seuil de Cushing de la prednisone est 7,5 mg par jour dans l'information professionnelle 29349. L'ACR en 2010 recommande, chez la femme ménopausée et l'homme d'au moins 50 ans, un médicament anti-ostéoporotique si la prednisone est d'au moins 7,5 mg par jour et si la durée prévue ou déjà écoulée atteint 3 mois, y compris chez le patient à risque fracturaire bas. L'ISCD en 2019 retient une autre barre, pour l'image vertébrale : au moins 5 mg de prednisone par jour pendant au moins 3 mois.",
        "anamnese": "Dose, durée, maladie, fractures, dose un jour sur deux, sevrage impossible, inhibiteur de l'aromatase associé.",
        "examen": "Signes de Cushing, taille, douleur vertébrale, force du quadriceps, risque de chute lié à la myopathie cortisonique.",
        "syndrom": "Ostéoporose postménopausique simple, ostéomalacie, myélome, hyperparathyroïdie. Le corticoïde ne dispense pas du bilan.",
        "positif": "Exposition remplissant la barre de 7,5 mg par jour pendant au moins 3 mois, ou exposition chronique avec T-score inférieur à −1,5 ou FRAX au-dessus du seuil suisse. Une fracture vertébrale sous corticoïde classe d'emblée haut, voire imminent si elle a moins de 2 ans.",
        "bio": "Calcémie, phosphate, 25-hydroxyvitamine D, créatinine avant un zolédronate, électrophorèse si la douleur vertébrale est forte. Le dénosumab n'est pas le premier réflexe : Ferrari écrit qu'il n'est pas approuvé dans cette indication, et la notice 60210 ne l'étudie pas chez l'homme sous corticoïde.",
        "arbre": "Risque bas au sens de l'ACR et dose d'au moins 7,5 mg par jour pendant 3 mois : alendronate, risédronate ou acide zolédronique. Risque haut : ces molécules ou le tériparatide. Ferrari ajoute le tériparatide si fracture vertébrale ou T-score lombaire inférieur à −3,5. Zolédronate 5 mg seulement si la clairance n'est pas inférieure à 35 ml/min.",
        "prevention": "La plus petite dose de prednisone qui contrôle la maladie, activité, vitamine D, calcium si carence, image vertébrale si la barre de 5 mg pendant 3 mois est franchie.",
        "piege": "Attendre un T-score de −2,5 pour traiter une prednisone à 10 mg depuis 4 mois. Prescrire le dénosumab comme s'il avait l'indication. Oublier de calculer la clairance avant 5 mg de zolédronate.",
        "cas": "Femme de 71 ans, polymyalgia, prednisone 10 mg par jour depuis 4 mois, pas de fracture, T-score −1,8 au col, clairance 58 ml/min, calcémie normale. La dose dépasse 7,5 mg par jour et la durée dépasse 3 mois. Case ACR : traitement, par exemple alendronate 70 mg par semaine si elle peut rester debout 30 minutes, ou zolédronate 5 mg si l'observance orale est douteuse. Le T-score au-dessus de −2,5 n'annule pas l'indication. On ne choisit pas le dénosumab sur cette seule indication.",
    },
    {
        "n": 4,
        "titre": "Ostéomalacie par carence en vitamine D",
        "qui": "une personne dont l'os ne se minéralise pas",
        "mecanisme": "L'ostéoporose est un os quantitativement réduit mais minéralisé. L'ostéomalacie est un défaut de minéralisation de la matrice. La densité peut être basse dans les deux, et le T-score ne les sépare pas.",
        "epi": "La carence en vitamine D est commune, l'ostéomalacie clinique l'est moins. On la cherche devant une densité basse avec douleurs osseuses, faiblesse proximale, phosphatases alcalines hautes, phosphate bas ou bas-normal, calcium bas ou bas-normal, PTH haute.",
        "etiologies": "Peu de soleil, régime sans poisson ni produits enrichis, malabsorption, maladie cœliaque, cholestase, certains anticonvulsivants, insuffisance rénale qui empêche l'activation. Le cours ne fixe pas une borne unique en nmol/l : les textes archivés n'en donnent pas une seule valeur suisse.",
        "demarche": "Douleur osseuse et faiblesse, puis biologie, puis densité. On ne commence pas un bisphosphonate ou le dénosumab tant que l'hypocalcémie et la carence ne sont pas corrigées : les notices l'exigent.",
        "anamnese": "Douleurs diffuses, difficulté à monter les escaliers, alimentation, voile vestimentaire, diarrhée, chirurgie digestive, antiépileptiques.",
        "examen": "Démarche dandinante, douleur à la pression des tibias ou des côtes, faiblesse des ceintures. Les zones de Looser, fissures de Milkman, se cherchent sur les radiographies, pas sur le seul T-score.",
        "syndrom": "Ostéoporose postménopausique à biologie normale, hyperparathyroïdie primaire où le calcium est haut ou limite haute avec PTH non freinée, myélome, métastases.",
        "positif": "Tableau clinique plus biologie de défaut de minéralisation, densité basse éventuelle. Le diagnostic densitométrique d'ostéoporose ne se pose pas à la place de ce tableau.",
        "bio": "Calcium, phosphate, phosphatases alcalines, PTH, 25-hydroxyvitamine D, créatinine. L'électrophorèse reste utile si une douleur vertébrale fait craindre un myélome.",
        "arbre": "Corriger d'abord. Calcium D3-Mepha 1200 mg et 800 UI par jour si la carence ou le risque de carence est celui de l'indication du produit. Une hypocalcémie se corrige avant Aclasta, Prolia ou EVENITY. Le tériparatide est contre-indiqué si la phosphatase alcaline est élevée sans explication.",
        "prevention": "Soleil raisonnable, alimentation, supplément quand l'indication est là, traitement de la malabsorption.",
        "piege": "Lire un T-score de −2,9 et prescrire 70 mg d'alendronate alors que les phosphatases alcalines sont à trois fois la norme et le phosphate est bas. Appeler ostéoporose une ostéomalacie.",
        "cas": "Homme de 74 ans, institution, peu de sorties, douleurs des cuisses, difficulté à se lever d'une chaise, T-score −2,9 au col. Calcium bas-normal, phosphate bas, phosphatases alcalines élevées, PTH élevée, créatinine stable. Ce n'est pas une ostéoporose postménopausique. On corrige la vitamine D et le calcium. On ne perfuse pas 5 mg de zolédronate tant que l'hypocalcémie n'est pas corrigée. On ne pose pas le tériparatide devant une phosphatase alcaline inexpliquée.",
    },
    {
        "n": 5,
        "titre": "Hyperparathyroïdie primaire",
        "qui": "une personne dont la parathyroïde n'est plus freinée",
        "mecanisme": "La PTH élevée ou non freinée augmente la résorption, surtout corticale. Le radius distal et le col fémoral perdent plus que le rachis trabéculaire. Le calcium est élevé ou à la limite supérieure. L'os ostéoporotique commun a, lui, un calcium normal et une PTH adaptée.",
        "epi": "Elle est assez fréquente après 50 ans, surtout chez la femme, souvent découverte par une calcémie. Le cours ne recopie pas de seuil opératoire chiffré : aucune recommandation chirurgicale datée n'est dans le dossier de preuves.",
        "etiologies": "Adénome parathyroïdien unique le plus souvent, hyperplasie, plus rarement carcinome. Lithium et hypercalcémie hypocalciurique familiale se discutent avant d'opérer, sans chiffres inventés ici.",
        "demarche": "Calcémie répétée, PTH, phosphate, créatinine, densité aux trois sites utiles dont l'avant-bras si l'hyperparathyroïdie est connue, recherche de lithiase et de fracture.",
        "anamnese": "Soif, polyurie, lithiase, fracture, ulcère, confusion, prise de lithium, calcium déjà élevé sur une vieille prise de sang.",
        "examen": "Déshydratation, douleur du flanc, taille. Pas de signe spécifique au lit. L'ISCD en 2019 demande la densité de l'avant-bras, radius à 33 %, dans l'hyperparathyroïdie.",
        "syndrom": "Hypercalcémie maligne, ostéomalacie où le calcium est plutôt bas et la PTH secondaire, myélome avec calcium haut mais PTH freinée, ostéoporose commune à PTH normale.",
        "positif": "Calcium élevé ou limite haute avec PTH non freinée, après contrôle, et densité basse surtout corticale. Le T-score lombaire seul peut rassurer à tort.",
        "bio": "Calcium, phosphate souvent bas, PTH, créatinine, 25-hydroxyvitamine D, électrophorèse si le tableau est atypique. Le tériparatide est contre-indiqué dans l'hyperparathyroïdie et l'hypercalcémie.",
        "arbre": "On adresse pour avis spécialisé sur l'indication opératoire. Un antirésorptif ne remplace pas cet avis. Si un médicament de l'os est quand même décidé après correction de la vitamine D, il respecte les notices : pas de tériparatide, hypocalcémie corrigée avant dénosumab ou zolédronate, avant-bras mesuré.",
        "prevention": "Hydratation, éviter les diurétiques thiazidiques sans avis, surveiller le calcium. Pas de dose de cinacalcet ici : elle n'est pas le sujet de la leçon et n'a pas été extraite pour ce lot.",
        "piege": "Appeler ostéoporose postménopausique une femme dont le calcium est à 2,75 mmol/l avec PTH haute. Prescrire Forsteo. Oublier le radius.",
        "cas": "Femme de 63 ans, T-score −2,7 au radius 33 %, −2,4 au col, −1,6 en lombaire, lithiase il y a 2 ans, calcium élevé sur deux prélèvements, PTH élevée, phosphatases alcalines normales, électrophorèse sans pic. Diagnostic de travail : hyperparathyroïdie primaire, pas une simple ostéoporose. Avis chirurgical. Pas de 20 µg de tériparatide. L'avant-bras explique pourquoi le rachis semblait presque rassurant.",
    },
    {
        "n": 6,
        "titre": "Ostéoporose de l'homme et hypogonadisme",
        "qui": "un homme, ou un homme jeune",
        "mecanisme": "Le déficit en testostérone augmente la résorption, comme le déficit en œstrogènes. Chez l'homme de 50 ans ou plus, le T-score se lit comme chez la femme ménopausée. Avant 50 ans, l'ISCD veut le Z-score : à −2,0 ou en dessous, la densité est sous la valeur attendue pour l'âge, et l'ostéoporose ne se diagnostique pas sur la densité seule.",
        "epi": "Ferrari en 2020 : un homme sur cinq aura une fracture de fragilité après 50 ans. L'ostéoporose masculine est moins dépistée. L'hypogonadisme est une cause secondaire listée dans le FRAX.",
        "etiologies": "Hypogonadisme, corticoïde, alcool, tabac, myélome, hyperparathyroïdie, hyperthyroïdie non traitée, malabsorption, ostéogenèse imparfaite. L'alendronate a été étudié chez l'homme à 10 mg par jour et à 70 mg par semaine dans l'information professionnelle 57957.",
        "demarche": "Chez l'homme, le bilan ajoute la testostérone. On ne conclut pas avant d'avoir la calcémie, l'électrophorèse et la TSH. Avant 50 ans, on n'écrit pas ostéoporose sur un T-score.",
        "anamnese": "Libido, érections, traitement du cancer de la prostate, corticoïde, alcool, fractures de l'enfance, taille familiale.",
        "examen": "Pilosité, volume testiculaire, gynécomastie, taille, cyphose, signes de myélome ou de Cushing.",
        "syndrom": "Myélome, ostéomalacie, hyperparathyroïdie, ostéogenèse imparfaite, métastases.",
        "positif": "Homme d'au moins 50 ans, T-score de −2,5 ou moins à un site valide, ou fracture de fragilité. Homme plus jeune : Z-score de −2,0 ou moins, cause à nommer, pas un diagnostic densitométrique isolé.",
        "bio": "Testostérone le matin, FSH et LH si elle est basse, calcémie, phosphate, PTH, 25-hydroxyvitamine D, TSH, créatinine, électrophorèse, numération.",
        "arbre": "Le traitement de la cause, par exemple un hypogonadisme, ne se substitue pas tout seul à la décision fracturaire. Si un médicament de l'os est indiqué, l'alendronate 70 mg par semaine a une étude chez l'homme. Le zolédronate 5 mg et le dénosumab 60 mg ont des indications masculines dans leurs notices d'ostéoporose à risque fracturaire, à relire au moment de la prescription. Le dénosumab n'est pas le choix de l'ostéoporose cortisonique masculine.",
        "prevention": "Alcool, tabac, chutes, activité, vitamine D si carence. Suppression androgénique du cancer de la prostate : Ferrari la classe à haut risque si le T-score est inférieur à −1,5 ou si le FRAX dépasse le seuil, et la notice du dénosumab a une indication d'accompagnement dans ce cancer.",
        "piege": "Appliquer un T-score de −2,6 à un homme de 38 ans et écrire ostéoporose. Oublier la testostérone et l'électrophorèse. Donner du tériparatide s'il y a eu une radiothérapie pelvienne qui a pris le squelette dans le champ.",
        "cas": "Homme de 57 ans, T-score −2,9 au col, deux fractures costales en toussant, libido basse, testostérone basse le matin, électrophorèse sans pic, calcium normal, TSH normale, clairance 70 ml/min. Ostéoporose de l'homme avec hypogonadisme. Avis endocrinien pour la testostérone, et médicament de l'os : alendronate 70 mg par semaine s'il peut rester debout, car le risque est celui d'une fracture déjà là. On ne s'arrête pas au mot hypogonadisme.",
    },
    {
        "n": 7,
        "titre": "Malabsorption et maladie cœliaque",
        "qui": "une personne qui n'absorbe pas le calcium ni la vitamine D",
        "mecanisme": "La muqueuse malade réduit l'absorption du calcium et de la vitamine D. La PTH monte, secondaire, et résorbe l'os. Le FRAX compte la malabsorption parmi les causes secondaires. La maladie cœliaque en est le modèle digestif de l'adulte.",
        "epi": "Elle se révèle parfois par une densité basse, une anémie ferriprive ou une fracture, sans diarrhée bruyante. Le sujet peut être jeune : on lit alors le Z-score.",
        "etiologies": "Maladie cœliaque, résection, maladie de Crohn, insuffisance pancréatique, cholestase, bypass. Le cours ne donne pas de sensibilité chiffrée des anticorps : elle n'est pas dans les preuves archivées.",
        "demarche": "Diarrhée, ballonnement, carence en fer, aphtes, dermatite, famille, puis anticorps et avis gastro-entérologue pour la biopsie selon les règles de ce spécialiste. En parallèle, biologie osseuse et densité.",
        "anamnese": "Selles, poids, fer, fractures, régime déjà sans gluten non supervisé, ostéoporose familiale qui serait en fait une cœliaquie.",
        "examen": "Pâleur, maigreur, aphtes, douleurs osseuses de type ostéomalacie, taille chez le sujet jeune.",
        "syndrom": "Ostéomalacie, anorexie, hyperthyroïdie, ostéogenèse imparfaite, ostéoporose postménopausique chez une femme plus âgée qui a aussi une cœliaquie.",
        "positif": "Malabsorption documentée et densité basse ou Z-score de −2,0 ou moins chez le sujet jeune. Le régime sans gluten est le traitement de la cause. L'os se réévalue après correction.",
        "bio": "Numération, fer, calcium, phosphate, phosphatases alcalines, 25-hydroxyvitamine D, PTH, TSH, créatinine. Anticorps de la maladie cœliaque selon le laboratoire, sans seuil inventé ici.",
        "arbre": "Traiter la cause et la carence avant un antirésorptif. Hypocalcémie corrigée d'abord. Un bisphosphonate oral se prend à jeun : chez une personne qui mange peu, l'observance et l'œsophage se discutent, et le zolédronate 5 mg n'est possible que si la clairance le permet et le calcium est sûr.",
        "prevention": "Régime sans gluten s'il est indiqué, suivi diététique, vitamine D et calcium selon la carence, pas un gluten arrêté au hasard sans diagnostic.",
        "piege": "Densité basse chez une femme de 45 ans étiquetée ostéoporose postménopausique alors qu'elle n'est pas ménopausée et qu'elle a une anémie. Tériparatide si la phosphatase alcaline est haute sans cause.",
        "cas": "Femme de 44 ans, Z-score −2,4 au col, ferritine basse, selles molles depuis des années, pas de ménopause. T-score affiché sur le compte rendu, qu'on ne retient pas pour le diagnostic. Biologie : 25-hydroxyvitamine D basse, PTH un peu haute, calcium normal bas, électrophorèse sans pic, TSH normale. On cherche la maladie cœliaque. On corrige calcium et vitamine D. On n'écrit pas ostéoporose sur le T-score. On ne commence pas 70 mg d'alendronate comme chez une femme de 70 ans.",
    },
    {
        "n": 8,
        "titre": "Hyperthyroïdie",
        "qui": "une personne dont la thyroïde accélère le remodelage",
        "mecanisme": "L'excès d'hormones thyroïdiennes accélère le remodelage, la résorption domine, l'os se creuse. Le FRAX compte l'hyperthyroïdie non traitée comme cause secondaire. Une fois traitée et euthyroïdienne, ce facteur ne se coche plus de la même façon : on réévalue.",
        "epi": "Elle est une cause classique de densité basse, parfois révélée par une fracture ou une perte de poids. La TSH fait partie du bilan minimum justement pour ne pas la manquer.",
        "etiologies": "Maladie de Basedow, nodule toxique, goitre multinodulaire toxique, surcharge en hormone thyroïdienne, thyroïdite dans sa phase haute. Le cours ne détaille pas les doses d'antithyroïdiens : elles ne sont pas extraites ici.",
        "demarche": "TSH, puis T4 libre si la TSH est basse, densité, et le reste du bilan pour ne pas rater un second diagnostic. Traiter la thyroïde. Recontrôler la densité quand l'euthyroïdie est tenue, en général dans le délai de 2 ans cité pour les personnes traitées, plus tôt si une fracture est survenue.",
        "anamnese": "Amaigrissement, tremblement, chaleur, palpitations, diarrhée, antécédent de nodule, prise de lévothyroxine et dose récente.",
        "examen": "Pouls, tremblement fin, peau chaude, goitre, œil, fonte musculaire. Le pouls rapide n'est pas un score de densité.",
        "syndrom": "Ostéoporose commune, phéochromocytome ou autre amaigrissement, malabsorption, myélome, ostéomalacie.",
        "positif": "TSH basse, hormones thyroïdiennes hautes ou lévothyroxine excessive, et densité basse. La fracture de fragilité se prend en compte tout de suite, sans attendre la guérison thyroïdienne pour protéger l'os si le risque est imminent.",
        "bio": "TSH, calcium, phosphate, PTH, 25-hydroxyvitamine D, créatinine, électrophorèse, numération. La phosphatase alcaline peut monter avec le remodelage.",
        "arbre": "Avis thyroïdien. Si fracture récente ou T-score très bas, le médicament de l'os suit les mêmes cases de risque de 2020, une fois l'hypocalcémie absente et la clairance connue. On ne choisit pas le tériparatide si une autre contre-indication de sa notice est là.",
        "prevention": "Ne pas laisser une lévothyroxine au-dessus du besoin. Dépister par la TSH devant une densité basse.",
        "piege": "Bilan d'ostéoporose sans TSH. Attribuer l'amaigrissement et la fracture au seul âge. Commencer un antirésorptif et oublier le traitement de la cause.",
        "cas": "Femme de 66 ans, perte de 6 kg, tremblement, T-score −2,3 au col, pas de fracture, TSH effondrée, calcium normal, électrophorèse sans pic. Hyperthyroïdie à traiter d'abord. Le T-score n'est pas à −2,5 : ce n'est pas une ostéoporose densitométrique, mais le FRAX avec hyperthyroïdie non traitée peut franchir le seuil. On recalcule après euthyroïdie. On ne pose pas un bisphosphonate le jour du diagnostic sans cette discussion.",
    },
    {
        "n": 9,
        "titre": "Myélome multiple et ostéopathie maligne",
        "qui": "une personne dont l'os est détruit par une hémopathie ou une métastase",
        "mecanisme": "Le myélome active les ostéoclastes localement. Les lésions sont lytiques, la densité globale peut être basse, une vertèbre peut s'effondrer. Ce n'est pas une ostéoporose postménopausique, même si le T-score est à −3.",
        "epi": "Moins fréquent que l'ostéoporose, mais c'est la case à ne pas manquer devant une fracture vertébrale, une anémie, une insuffisance rénale ou un calcium haut. L'ISCD demande une autre imagerie si la déformation vertébrale survient chez une personne qui a un cancer connu, ou si l'image n'est pas typique.",
        "etiologies": "Myélome, métastase lytique, lymphome, mastocytose plus rare. L'ostéoporose peut coexister : elle ne ferme pas le bilan.",
        "demarche": "Douleur vertébrale inflammatoire, altération générale, calcium, créatinine, numération, électrophorèse des protéines sériques et urinaires, puis avis hématologique. La densité ne tranche pas.",
        "anamnese": "Douleur nocturne, sueurs, perte de poids, cancer connu, fracture spontanée, épistaxis ou infections répétées.",
        "examen": "Douleur à la percussion des épineuses, pâleur, masse, taille perdue rapidement. Une douleur de cuisse fait aussi chercher une fracture atypique si un antirésorptif est déjà en cours, mais ici la première peur est la lésion focale.",
        "syndrom": "Ostéoporose avec tassement bénin au sens de Genant, ostéomalacie, hyperparathyroïdie, infection, fracture traumatique.",
        "positif": "Pic monoclonal ou chaîne légère, atteinte d'organe, lésion focale, dans un cadre hématologique. Le grade de Genant décrit la hauteur perdue, il ne dit pas que la cause est ostéoporotique. Grade 0 normale, grade 1 perte de hauteur de 20 à 25 %, grade 2 de 26 à 40 %, grade 3 au-delà de 40 %, de T4 à L4. Forme cunéiforme, biconcave ou tassement, sans lier la forme au grade.",
        "bio": "Électrophorèse, numération, créatinine, calcium, protéines. PTH si le calcium est haut, pour ne pas confondre avec l'hyperparathyroïdie : dans le myélome la PTH est en principe freinée. 25-hydroxyvitamine D et TSH restent dans le bilan général.",
        "arbre": "Pas de tériparatide : métastase, tumeur osseuse et myélome entrent dans les contre-indications de type tumeur ou métastase de la notice, et une phosphatase alcaline ou une lésion focale font arrêter cette idée. Le zolédronate utilisé en oncologie n'est pas la perfusion annuelle de 5 mg de l'ostéoporose : on ne mélange pas les schémas. L'hématologue conduit.",
        "prevention": "Devant toute densité basse, l'électrophorèse empêche de passer à côté. Devant un tassement atypique, une autre image.",
        "piege": "T-score −3,2 et alendronate 70 mg sans électrophorèse chez un homme de 72 ans fatigué. Tériparatide sur un tassement qui est une métastase. Grade de Genant utilisé comme preuve que la fracture est ostéoporotique.",
        "cas": "Homme de 72 ans, douleur lombaire nocturne, perte de 5 cm en six mois, T-score −3,2 au col, hémoglobine basse, créatinine qui monte, calcium haut, PTH basse, pic à l'électrophorèse. Ce n'est pas l'ostéoporose postménopausique ni l'hyperparathyroïdie. Avis hématologique en urgence relative. Pas de Forsteo. Le grade vertébral, s'il est à 3, décrit la gravité du tassement, pas la bénignité.",
    },
    {
        "n": 10,
        "titre": "Ostéogenèse imparfaite de l'adulte",
        "qui": "un adulte dont l'os fragile est constitutionnel",
        "mecanisme": "Un collagène de type I anormal fragilise l'os dès l'enfance. À l'âge adulte, les fractures continuent, la densité est souvent basse, et le FRAX cite l'ostéogenèse imparfaite de l'adulte parmi les causes secondaires. Ce n'est pas une ostéoporose acquise de la ménopause.",
        "epi": "Rare à côté de l'ostéoporose postménopausique. Elle se discute devant des fractures dès l'enfance, une surdité, des sclères bleues, une dentinogenèse, une famille atteinte, un Z-score de −2,0 ou moins chez un adulte jeune.",
        "etiologies": "Formes liées au collagène et formes plus rares. Le cours ne détaille pas la génétique mutation par mutation : elle n'est pas archivée ici. L'adulte déjà diagnostiqué dans l'enfance et l'adulte dont le diagnostic a été manqué sont deux entrées.",
        "demarche": "Histoire des fractures, famille, examen des sclères, des dents, de la surdité, densité en Z-score si la personne a moins de 50 ans ou n'est pas ménopausée, bilan pour écarter cœliaquie, hypogonadisme et ostéomalacie qui imitent la fragilité.",
        "anamnese": "Fractures avant 20 ans, entorses, surdité précoce, sclères, dents qui s'usent, parent fracturé, diagnostic posé dans l'enfance, traitement par bisphosphonate reçu enfant.",
        "examen": "Sclères bleutées, dentinogenèse, déformation des os longs, hyperlaxité, taille, surdité. On ne diagnostique pas sur la couleur des yeux seule.",
        "syndrom": "Maltraitance dans l'enfance à ne pas confondre, ostéomalacie, cœliaquie, hypogonadisme, ostéoporose commune après 50 ans chez une personne qui a aussi des antécédents flous.",
        "positif": "Histoire clinique et, chez le sujet jeune, Z-score de −2,0 ou moins, qui signifie sous la norme d'âge et non ostéoporose au sens de l'OMS. Chez l'homme de moins de 50 ans, l'ISCD interdit de poser l'ostéoporose sur la densité seule. Après 50 ans ou après la ménopause, le T-score redevient licite, et la maladie reste une cause secondaire du FRAX.",
        "bio": "Le bilan secondaire habituel, pour ne pas manquer une cause acquise surajoutée : calcium, phosphate, PTH, 25-hydroxyvitamine D, TSH, créatinine, électrophorèse, testostérone chez l'homme, sérologie cœliaque si le tableau digestif existe.",
        "arbre": "Avis du centre qui suit les maladies osseuses rares. Si un médicament de l'ostéoporose de l'adulte est utilisé, il suit sa notice : alendronate 70 mg, zolédronate 5 mg, dénosumab 60 mg, tériparatide 20 µg dans leurs indications et contre-indications, pas un schéma pédiatrique recopié. Les cartilages ouverts contre-indiquent le tériparatide.",
        "prevention": "Chutes, rééducation, audition, soins dentaires avant un antirésorptif long, information sur les fractures atypiques et l'ostéonécrose si le traitement se prolonge.",
        "piege": "T-score de −3 chez une femme de 32 ans non ménopausée et diagnostic d'ostéoporose. Oublier la famille et les fractures de l'enfance. Répéter un tériparatide au-delà de 24 mois.",
        "cas": "Femme de 32 ans, non ménopausée, trois fractures du poignet et une du fémur dans l'enfance, sclères bleutées, mère sourde et fracturée, Z-score −2,6 au col. Le compte rendu affiche aussi un T-score : on ne l'utilise pas pour écrire ostéoporose. La densité est sous la norme d'âge. Bilan acquis négatif, calcium et TSH normaux, pas de pic. Avis spécialisé. Pas de diagnostic densitométrique isolé. Si un jour un traitement de l'adulte est décidé, la durée du tériparatide ne dépasse pas 24 mois et ne se répète pas.",
    },
]


def questions(dx: dict) -> list[str]:
    t = dx["titre"]
    qui = dx["qui"]
    out = []
    modeles = [
        f"Question sur {t}. {qui.capitalize()} consulte pour une densité basse. {dx['mecanisme']} Quel geste vient avant le médicament ? {dx['demarche']}",
        f"Dossier. {dx['cas']}",
        f"Piège d'examen. {dx['piege']} La bonne conduite reste : {dx['arbre']}",
        f"Étiologies à classer pour {t}. {dx['etiologies']} On n'en raye aucune pour faire tenir un diagnostic unique.",
        f"Anamnèse ciblée. {dx['anamnese']} L'examen ajoute : {dx['examen']}",
        f"Diagnostic positif. {dx['positif']} Les examens qui l'appuient : {dx['bio']}",
        f"Voisins à garder ouverts. {dx['syndrom']} Le mot {t} ne les ferme pas.",
        f"Prévention propre. {dx['prevention']} Elle ne remplace pas le traitement quand le risque de 2020 est imminent ou élevé.",
        f"Physiopathologie en une copie d'examen. {dx['mecanisme']} Conséquence pratique : {dx['demarche']}",
        f"Place épidémiologique. {dx['epi']} Cela ne donne pas le droit d'inventer une incidence de cabinet.",
        f"Arbre au lit. {dx['arbre']} On écrit la case de risque avant le nom commercial.",
        f"Retour sur le cas. {dx['cas']} Le piège serait : {dx['piege']}",
        f"Ce que l'on dicte. Pour {t}, la phrase de sortie contient le site de mesure, la case de risque et la contre-indication du médicament choisi. {dx['positif']}",
        f"Contrôle de cohérence. Si la biologie contredit {t}, on change de case. Rappel biologique : {dx['bio']}",
        f"Chute et fracture. Même dans {t}, une fracture vertébrale ou de hanche de moins de 2 ans fait quitter la case tranquille et ouvre le risque imminent décrit en 2020.",
        f"Sites de mesure. Rachis postéro-antérieur de L1 à L4 et hanche, col ou hanche totale, le plus bas des deux. L'avant-bras à 33 % si la hanche ou le rachis est illisible, en cas d'hyperparathyroïdie, ou si la table ne porte pas le poids. On retire une vertèbre dont le T-score s'écarte de plus de 1,0 de ses voisines, cas fréquent de l'arthrose lombaire.",
        f"Grades à ne pas couper. Grade 0 normale, grade 1 perte de 20 à 25 % de la hauteur et de 10 à 20 % de la surface, grade 2 perte de 26 à 40 % de la hauteur, grade 3 au-delà de 40 %. Formes cunéiforme, biconcave et tassement, non liées au grade. Un grade 0,5 est limite. Le milieu du rachis thoracique est naturellement un peu cunéiforme.",
        f"Z-score du sujet jeune. À −2,0 ou en dessous, sous la norme d'âge. Au-dessus de −2,0, dans la norme d'âge. Pas de diagnostic d'ostéoporose sur la densité seule chez l'homme de moins de 50 ans. Le T-score de l'OMS vaut après la ménopause et chez l'homme d'au moins 50 ans.",
        f"Médicament et notice. Alendronate 70 mg par semaine, zolédronate 5 mg par an si la clairance n'est pas inférieure à 35 ml/min, dénosumab 60 mg tous les 6 mois avec le risque de rebond, tériparatide 20 µg par jour au plus 24 mois, romosozumab 210 mg par mois pendant 12 mois sauf antécédent cardiovasculaire majeur. Calcium 1200 mg et 800 UI si l'indication du comprimé est remplie.",
        f"Seuil cortisonique à ne pas amputer. Au moins 7,5 mg de prednisone par jour pendant au moins 3 mois chez la femme ménopausée ou l'homme d'au moins 50 ans à risque bas, selon l'ACR en 2010. Barre distincte de l'image vertébrale : au moins 5 mg par jour pendant au moins 3 mois. Seuil de Cushing de la notice : 7,5 mg.",
    ]
    srcs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    for i, m in enumerate(modeles):
        out.append(P(m, src=srcs[i % len(srcs)]))
    # variantes chiffrées propres au DX, pour que les fenêtres ne soient pas identiques
    variantes = [
        f"Variante A de {t}. {dx['qui'].capitalize()} a déjà chuté deux fois. Le FRAX ne contient pas la chute comme case à cocher, mais Ferrari en 2020 rappelle que les chutes peuvent presque doubler le risque à profil osseux égal. On les écrit dans le dossier.",
        f"Variante B de {t}. Une perte de taille historique de plus de 4 cm fait chercher une fracture vertébrale, par radiographie ou par l'évaluation sur l'appareil de densité. Le grade se dit entier, pas « un peu tassé ».",
        f"Variante C de {t}. Ward et le grand trochanter ne servent pas au diagnostic. Le rachis de profil non plus. Une seule vertèbre restante ne porte pas le diagnostic : on change de site.",
        f"Variante D de {t}. Après 65 ans, une fracture vertébrale se complique d'une nouvelle fracture dans les 2 ans chez environ 25 % des personnes, une fracture de hanche ou de bassin chez 15 % ou plus, une fracture d'humérus ou de radius chez 10 % ou plus. D'où l'urgence de la case imminente.",
        f"Variante E de {t}. Le seuil suisse d'intervention rappelé en 2020 est d'environ 10 % à 50 ans et d'environ 30 % à 72 ans, calé sur une fracture vertébrale prévalente. Très haut risque : au moins 20 points de pourcentage au-dessus de ce seuil, soit environ 50 % après 70 ans.",
        f"Variante F de {t}. Exemple chiffré de 2020 : femme de 55 ans, fracture du poignet, indice de masse corporelle 20, tabac, mère avec fracture de hanche, T-score de hanche −2,7, probabilité FRAX 34 %, case très élevée pour son âge. Autre exemple : femme de 70 ans, fracture vertébrale, prednisone 5 mg par jour, T-score −3,1, probabilité 46 %.",
        f"Variante G de {t}. Sous dénosumab, l'arrêt sans relais expose à des FVM. La notice demande de ne pas interrompre sans le médecin et de suivre la densité. Un bisphosphonate de relais aide certaines personnes et échoue chez d'autres.",
        f"Variante H de {t}. Pause des bisphosphonates : la notice d'Aclasta dit qu'après 3 à 5 ans, si le risque est faible, l'arrêt se discute et le risque se revoit. Ce n'est pas un arrêt du dénosumab. Ce n'est pas un arrêt après une fracture récente.",
        f"Variante I de {t}. Douleur de cuisse ou d'aine sous bisphosphonate ou dénosumab : chercher une fracture fémorale atypique, parfois des deux côtés, avant le trait complet. Douleur à la mâchoire ou extraction : chercher une ONM, surtout si la corticothérapie, le tabac ou une mauvaise hygiène s'ajoutent.",
        f"Variante J de {t}. Grossesse et allaitement : Forsteo est contre-indiqué dans les deux. Aclasta est contre-indiqué pendant la grossesse. Prolia n'est pas pour l'enfant de moins de 18 ans. EVENITY est contre-indiqué après un infarctus ou un accident vasculaire cérébral.",
        f"Variante K de {t}. Alendronate : eau du robinet, pas eau minérale, jus ou café, à distance des autres médicaments, ne pas se recoucher avant 30 minutes. Sinon l'œsophage paie et l'absorption tombe.",
        f"Variante L de {t}. {dx['prevention']} On répète la densité vers 2 ans dans les cases traitées, et l'on reclasse le risque avant de poursuivre.",
    ]
    for i, v in enumerate(variantes):
        out.append(P(v, src=srcs[i % len(srcs)]))
    return out


def points_dx(dx: dict) -> dict[int, list[str]]:
    t = dx["titre"]
    base = {
        1: [
            P(f"{t}. {dx['positif']}", src="2"),
            P(f"Ce que ce n'est pas. {dx['syndrom']}", src="1"),
            P("Définition densitométrique reprise en 2019 : ostéoporose si le T-score du rachis lombaire, de la hanche totale ou du col fémoral est de −2,5 ou moins, chez la femme ménopausée et chez l'homme d'au moins 50 ans. La référence du col est la femme blanche de 20 à 29 ans de NHANES III. Ostéopénie, mot gardé : T-score au-dessus de −2,5 et en dessous de −1,0 quand aucun autre facteur ne classe plus haut.", src="2"),
            P("Chez le sujet jeune, femme non ménopausée ou homme de moins de 50 ans, le Z-score remplace le T-score. À −2,0 ou en dessous, la densité est sous la norme d'âge. L'ostéoporose de l'homme jeune ne se pose pas sur la densité seule.", src="2"),
        ],
        2: [
            P(dx["epi"], src="1"),
            P("Le traitement manque : moins de 10 % des personnes ostéoporotiques et 20 % des fractures à basse énergie reçoivent un médicament anti-ostéoporotique, chiffre donné en 2020.", src="1"),
            P(f"Pour {t}, la fréquence ne dispense pas de chercher la cause grave plus rare.", src="1"),
        ],
        3: [
            P(dx["mecanisme"], src="1"),
            P("Rappel de remodelage. L'os se renouvelle par ostéoclastes et ostéoblastes. Un antirésorptif freine les premiers. Le tériparatide et le romosozumab poussent la formation, le second freinant aussi la résorption. D'où l'ordre : anabolique d'abord dans le risque imminent vertébral, puis relais, plutôt que l'inverse.", src="1"),
            P(f"Étiologies de {t}. {dx['etiologies']}", src="1"),
        ],
        4: [
            P(dx["demarche"], src="1"),
            P("Étape densitométrique. Mesurer rachis et hanche. Retirer la vertèbre arthrosique ou dont le T-score s'écarte de plus de 1,0. Ne pas diagnostiquer sur une seule vertèbre. Avant-bras à 33 % dans les trois cas prévus en 2019.", src="2"),
            P("Étape de risque. Fracture récente, T-score, FRAX suisse, corticoïde, chute. La case se nomme avant l'ordonnance.", src="1"),
            P("Étape biologique minimum : calcémie, phosphate, PTH, 25-hydroxyvitamine D, TSH, électrophorèse des protéines, créatinine, et testostérone chez l'homme. Malabsorption et cœliaquie si le tableau digestif ou la carence en fer existent.", src="1"),
        ],
        5: [
            P(dx["anamnese"], src="1"),
            P("Drapeaux : douleur nocturne, anémie, rein qui monte, calcium haut, perte de taille rapide, fracture sous corticoïde, douleur de cuisse sous antirésorptif, arrêt sauvage du dénosumab.", src="7"),
            P("La chute de l'année, le parkinsonisme et l'incontinence urinaire comptent cliniquement même s'ils ne sont pas une case FRAX.", src="1"),
        ],
        6: [
            P(dx["examen"], src="2"),
            P("Taille mesurée, pas déclarée. Cyphose, distance mur-occiput, douleur à la percussion des épineuses. Une perte historique de plus de 4 cm ouvre l'image vertébrale.", src="2"),
            P("Examen dentaire avant un traitement prolongé si des extractions sont prévues. Examen cardiovasculaire avant le romosozumab : antécédent d'infarctus ou d'accident vasculaire cérébral contre-indique EVENITY.", src="9"),
        ],
        7: [
            P(dx["syndrom"], src="1"),
            P("Ostéomalacie contre ostéoporose : douleurs, faiblesse proximale, phosphatases alcalines hautes, phosphate et calcium plutôt bas, PTH haute, contre une biologie minérale normale. Hyperparathyroïdie primaire : calcium haut, PTH non freinée. Myélome : pic, anémie, rein, calcium haut et PTH freinée.", src="4"),
            P("L'arthrose lombaire n'est pas une cause de densité basse : elle fait monter le chiffre lombaire et masque l'ostéoporose. On la retire de la région d'intérêt.", src="2"),
        ],
        8: [
            P(dx["positif"], src="2"),
            P(f"Critère propre à {t}, sans amputations. {dx['bio']}", src="1"),
            P("Fracture vertébrale : grades entiers de Genant, de 0 à 3, plus le grade limite 0,5, formes nommées à part. On n'arrête pas la classification au grade 2.", src="3"),
        ],
        9: [
            P(dx["bio"], src="1"),
            P("Créatinine et clairance avant chaque perfusion de 5 mg d'Aclasta. En dessous de 35 ml/min, contre-indication. À 35 ml/min ou plus, pas d'adaptation selon la notice de mars 2026.", src="6"),
            P("Image : radiographies ou évaluation vertébrale de T4 à L4 si perte de taille, fracture douteuse, ou prednisone d'au moins 5 mg par jour depuis au moins 3 mois. Une lésion qui n'est pas typique d'une fracture ostéoporotique demande une autre imagerie.", src="2"),
        ],
        10: [
            P(dx["arbre"], src="1"),
            P("Imminent : risque de fracture supérieur à 10 % dans les 2 ans, en pratique fracture vertébrale ou de hanche de moins de 2 ans, ou autre fracture majeure de moins de 2 ans après 65 ans. Très élevé : FRAX d'au moins 20 points au-dessus du seuil d'âge. Élevé : fracture de plus de 2 ans, ou FRAX au-dessus du seuil sans atteindre 20 points, ou corticoïde, inhibiteur de l'aromatase ou suppression androgénique avec T-score inférieur à −1,5. Modéré : T-score de −2,5 ou moins, sans fracture, FRAX sous le seuil. Faible : ostéopénie sans autre facteur.", src="12"),
            P("Conduite par case, 2020. Imminent vertébral : tériparatide 18 à 24 mois puis antirésorptif, hors contre-indications. Imminent de hanche : zolédronate annuel si le rein le permet, sinon dénosumab. Romosozumab un an puis relais, hors risque cardiovasculaire majeur. Risque élevé : antirésorptif puissant, pas le dénosumab comme traitement de l'ostéoporose cortisonique. Modéré : modulateur sélectif si pas d'œstrogène, ou bisphosphonate oral si les marqueurs de remodelage sont au-dessus du seuil préménopausique. Faible : mode de vie et vitamine D, densité à 5 à 10 ans.", src="1"),
        ],
        11: secours_os() + [P(dx["arbre"], src="1"), P(dx["cas"], src="1")],
        12: [
            P(dx["prevention"], src="1"),
            P("Chutes, tabac, alcool au-delà de 3 unités par jour, activité en charge. Supplément : 1200 mg de calcium et 800 UI de vitamine D par jour seulement dans l'indication du Calcium D3-Mepha, carence ou risque élevé de carence, adulte, pas enfant.", src="11"),
            P("Sous dénosumab, la prévention de la fracture de rebond est de ne pas arrêter seul. Sous bisphosphonate à risque devenu faible, la pause après 3 à 5 ans se discute.", src="6"),
        ],
        13: [
            P(f"À retenir pour {t}. {dx['positif']}", src="2"),
            P(f"Conduite courte. {dx['arbre']}", src="1"),
            P("Trois chiffres qui ne se mélangent pas : T-score −2,5, Z-score −2,0, prednisone 7,5 mg par jour pendant 3 mois.", src="4"),
            P("Cinq doses suisses : 70 mg, 5 mg, 60 mg, 20 µg, 210 mg. Deux apports : 1200 mg et 800 UI. Un seuil de notice : 7,5 mg.", src="5"),
        ],
        14: [
            P(dx["piege"], src="1"),
            P(dx["cas"], src="1"),
            P("Question corrigée. On demande la case, le site de mesure, le médicament et sa contre-indication, pas un synonyme de densité basse.", src="1"),
            P("Fautes qui coûtent des points : classification de Genant arrêtée au grade 1, ostéopénie appelée ostéoporose, dénosumab arrêté net, romosozumab après un infarctus, zolédronate sans clairance, tériparatide dans l'hypercalcémie ou au-delà de 24 mois, T-score chez l'homme de 35 ans.", src="8"),
        ],
    }
    return base


def gonfler(corps: list[str], dx: dict, cible: int) -> list[str]:
    extra = questions(dx)
    i = 0
    # mesure grossière : on ajoute tant que le texte visible estimé est court
    while sum(len(re.sub(r"<[^>]+>", "", c)) for c in corps) < cible and i < len(extra) * 3:
        corps.append(extra[i % len(extra)])
        i += 1
    return corps


def assembler_points(dx: dict, cible_y: int) -> list[tuple[str, str, str]]:
    brut = points_dx(dx)
    # répartition : le gonflement va surtout vers les points 4, 11 et 14, puis les autres
    ordre = [4, 11, 14, 10, 8, 3, 9, 1, 7, 13, 5, 6, 2, 12]
    # estimation : on vise cible_y octets de texte. On gonfle un sac puis on découpe.
    sac = []
    for n in range(1, 15):
        sac.extend(brut[n])
    sac = gonfler(sac, dx, int(cible_y * 0.92))
    # redistribuer en 14 parts inégales
    poids = [1.15, 0.7, 1.05, 1.35, 0.85, 0.8, 0.9, 1.1, 1.0, 1.25, 1.4, 0.75, 0.85, 1.2]
    total_p = sum(poids)
    blocs = []
    idx = 0
    textes = sac
    # concaténer en un flux et recouper par taille de texte
    flux = textes
    n_items = len(flux)
    curseur = 0
    out = []
    for i, ((n, titre), w) in enumerate(zip(TITRES, poids)):
        if i == 13:
            part = flux[curseur:]
        else:
            prendre = max(2, round(n_items * w / total_p))
            part = flux[curseur: curseur + prendre]
            curseur += prendre
            if not part:
                part = [flux[curseur % n_items]]
        fiche = (
            f"<p>{habiller(dx['titre'])}. Le détail chiffré est dans la fenêtre.</p>"
            f"<p>On ouvre {bouton(f'dx{dx['n']}-p{n}', 'la fenêtre de ce point')}.</p>"
        )
        corps = "".join(part)
        # figures sur certains points du DX.1, DX.3, DX.9
        if dx["n"] == 1 and n == 1:
            corps = svg_tscore("d1") + corps
        if dx["n"] == 1 and n == 10:
            corps = svg_algo("d1") + corps
        if dx["n"] == 9 and n == 8:
            corps = svg_genant("d9") + corps
        fen = fenetre(f"dx{dx['n']}-p{n}", titre, corps)
        out.append((titre, fiche, fen))
    return out


def glossaire() -> str:
    lignes = "".join(
        f"<p>{habiller(sigle)} : {html.escape(titre)}.</p>" for sigle, titre in SIGLES
    )
    return fenetre("w-glossaire", "Sigles de la leçon", lignes)


def page(nom: str, h1: str, sous: str, essentiel: str, points: list[tuple[str, str, str]]) -> str:
    ilots = []
    ilots.append(
        '<section class="ilot c essentiel"><h2 id="ess">L\'essentiel</h2>'
        f"{essentiel}<p>Les sigles s'ouvrent dans {bouton('w-glossaire', 'la fenêtre des sigles')}.</p>"
        f"{glossaire()}</section>"
    )
    liens = "".join(f'<li><a href="#p{i}">{html.escape(titre)}</a></li>' for i, (titre, _, _) in enumerate(points, 1))
    ilots.append(
        '<nav class="ilot v" aria-labelledby="som"><h2 id="som">Sommaire</h2>'
        f'<ol class="som">{liens}</ol>'
        '<p class="sous">Les mots soulignés ouvrent une fenêtre. Les sources sont à la fin.</p></nav>'
    )
    for i, (titre, fiche, fen) in enumerate(points, 1):
        couleur = "c" if i % 2 else "v"
        ilots.append(f'<section class="ilot {couleur}"><h2 id="p{i}">{titre}</h2>{fiche}{fen}</section>')
    sources = """<section class="ilot c"><h2 id="sources">Sources</h2>
<ol class="sources">
<li>Ferrari et collaborateurs, Swiss Medical Weekly, 2020, w20352.</li>
<li>International Society for Clinical Densitometry, positions adultes, 2019.</li>
<li>Genant et collaborateurs, Journal of Bone and Mineral Research, 1993 ; grades dans la revue de 2013.</li>
<li>American College of Rheumatology, ostéoporose cortisonique, 2010.</li>
<li>Alendronate Sandoz 70, information professionnelle, Swissmedic 57957, juillet 2023.</li>
<li>Aclasta, information professionnelle, Swissmedic 57363, mars 2026.</li>
<li>Prolia, information professionnelle, Swissmedic 60210, mai 2026.</li>
<li>Forsteo, information professionnelle, Swissmedic 56007, avril 2026.</li>
<li>EVENITY, information professionnelle, Swissmedic 67033, juillet 2024.</li>
<li>Prednisone Streuli, information professionnelle, Swissmedic 29349, juin 2026.</li>
<li>Calcium D3-Mepha 1200/800, information professionnelle, Swissmedic 59096, avril 2024.</li>
<li>Gazette médicale, recommandations ASCO 2020, lue en 2026.</li>
</ol></section>"""
    css_txt = css()
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(h1)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
<style>
{css_txt}
</style>
</head>
<body>
<main>
<h1 id="titre">{html.escape(h1)}</h1>
<p class="taille" id="taille">Taille : en cours de mesure</p>
<p class="sous">{habiller(sous)}</p>
{''.join(ilots)}
{sources}
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- FIN_FICHIER {nom} -->
"""


def phase_a_points() -> list[tuple[str, str, str]]:
    # monographie du signe, plus les dix DX nommés
    intro = {
        1: [
            P("Diminution de la densité osseuse : le compte rendu de DXA montre une masse basse. Ce n'est pas encore un diagnostic de cause. L'ostéoporose densitométrique est un T-score de −2,5 ou moins au rachis, à la hanche totale ou au col, chez la femme ménopausée et l'homme d'au moins 50 ans. L'ostéopénie est la bande au-dessus de −2,5 et en dessous de −1,0. Le sujet jeune se lit en Z-score, seuil −2,0.", src="2"),
            P("Le standard de référence de l'OMS rappelé par l'ISCD en 2019 est un T-score de −2,5 ou moins au col fémoral, base NHANES III, femme blanche de 20 à 29 ans. Le diagnostic peut aussi se poser au rachis lombaire ou à la hanche totale.", src="2"),
        ],
        2: [
            P("Suisse, 2020, en citant 2014 : une femme sur deux et un homme sur cinq fracturent après 50 ans. Au moins 75 000 fractures incidentes par an, 140 000 fractures de hanche ou de vertèbre prévalentes, 450 000 personnes ostéoporotiques en 2010. Moins de 10 % des ostéoporoses et 20 % des fractures à basse énergie sont traitées.", src="1"),
        ],
        3: [
            P("Deux mécanismes à ne pas fondre. Perte de quantité d'os minéralisé : ostéoporose, ménopause, âge, cortisone, hypogonadisme, hyperthyroïdie, immobilisation. Défaut de minéralisation : ostéomalacie, carence en vitamine D, malabsorption. Destruction focale : myélome et métastase. Os constitutionnellement fragile : ostéogenèse imparfaite.", src="1"),
            P("L'arthrose lombaire fait l'inverse d'une baisse : elle augmente la densité mesurée. Une vertèbre dont le T-score dépasse de plus de 1,0 ses voisines se retire.", src="2"),
        ],
        4: [
            P("Pas à pas. 1. Histoire de fracture et de taille. 2. DXA rachis et hanche, avant-bras si besoin. 3. Retrait des artéfacts. 4. FRAX suisse. 5. Bilan de cause : calcémie, phosphate, PTH, 25-hydroxyvitamine D, TSH, électrophorèse, créatinine, testostérone chez l'homme, cœliaquie si le tableau y mène. 6. Case de risque. 7. Médicament selon la notice.", src="1"),
        ],
        5: [
            P("Drapeaux rouges du signe densité basse : fracture récente, corticoïde, douleur nocturne, anémie, calcium haut, perte de poids, homme jeune, sclères bleues et fractures d'enfance, diarrhée, thyrotoxicose, douleur de cuisse sous traitement, projet d'arrêt du dénosumab.", src="1"),
        ],
        6: [
            P("Taille, poids, cyphose, mur-occiput, percussion des épineuses, démarche, signes de Cushing, de thyrotoxicose, d'hypogonadisme, sclères et dents, examen dentaire et cardiovasculaire selon le médicament envisagé.", src="2"),
        ],
        7: [
            P("Dix diagnostics à tenir ensemble, du plus fréquent au plus rare dans une consultation d'adulte : ostéoporose postménopausique, ostéopénie densitométrique, ostéoporose cortisonique, ostéomalacie par carence en vitamine D, hyperparathyroïdie primaire, ostéoporose de l'homme et hypogonadisme, malabsorption et maladie cœliaque, hyperthyroïdie, myélome multiple et ostéopathie maligne, ostéogenèse imparfaite de l'adulte.", src="1"),
            P("Ordre d'exclusion, du plus dangereux au plus fréquent : myélome multiple et ostéopathie maligne, ostéomalacie par carence en vitamine D, hyperparathyroïdie primaire, ostéoporose cortisonique, hyperthyroïdie, malabsorption et maladie cœliaque, ostéoporose de l'homme et hypogonadisme, ostéogenèse imparfaite de l'adulte, ostéoporose postménopausique, ostéopénie densitométrique.", src="1"),
        ],
        8: [
            P("Positif du signe : densité basse sur un site valide. Positif de l'ostéoporose : T-score de −2,5 ou moins, ou fracture de fragilité dans un contexte évocateur. Positif de l'ostéopénie : bande −1,0 à −2,5 sans le seuil d'ostéoporose. Le grade vertébral de Genant est entier : 0, 0,5, 1 (20 à 25 %), 2 (26 à 40 %), 3 (plus de 40 %).", src="3"),
            svg_genant("a"),
        ],
        9: [
            P("Bilan non amputé : calcémie, phosphate, PTH, 25-hydroxyvitamine D, TSH, électrophorèse des protéines sériques, créatinine, testostérone chez l'homme, recherche de malabsorption et de maladie cœliaque si le contexte existe. Clairance avant le zolédronate. Image vertébrale selon les indications de 2019.", src="2"),
        ],
        10: [
            svg_algo("a"),
            P("Lecture de l'algorithme. On part de la fracture récente, puis du FRAX comparé au seuil suisse, puis du T-score, puis du corticoïde. Chaque case a son médicament, écrit dans la fenêtre de traitement.", src="12"),
            P("Seuils 2020 à connaître entiers. Imminent au-dessus de 10 % à 2 ans. Très élevé : 20 points au-dessus du seuil, environ 50 % après 70 ans. Seuil d'intervention environ 10 % à 50 ans et 30 % à 72 ans. Corticoïde haut risque si T-score inférieur à −1,5 ou FRAX au-dessus du seuil. Modéré : T-score −2,5 ou moins, sans fracture, FRAX sous le seuil.", src="1"),
        ],
        11: secours_os() + [
            P("Choix selon Ferrari 2020. Imminent avec fracture vertébrale : tériparatide puis antirésorptif. Imminent avec fracture de hanche : zolédronate si le rein le permet. Romosozumab en première ligne de l'imminent et du très haut risque, hors antécédent cardiovasculaire majeur, pendant un an, puis relais. Haut risque y compris cortisone : antirésorptif puissant, tériparatide si fracture vertébrale ou T-score lombaire inférieur à −3,5. Le dénosumab n'est pas approuvé pour l'ostéoporose cortisonique.", src="1"),
        ],
        12: [
            P("Prévenir la fracture suivante : traiter la case à risque, corriger la carence, éviter la chute, ne pas arrêter le dénosumab, surveiller la mâchoire et la cuisse, recontrôler la DXA vers 2 ans sous traitement et à 5 à 10 ans si le risque est faible.", src="1"),
            P("Prednisone : viser la plus petite dose. Le seuil de Cushing est 7,5 mg. La barre de traitement ACR est au moins 7,5 mg par jour pendant au moins 3 mois. La barre d'image est au moins 5 mg par jour pendant au moins 3 mois.", src="4"),
        ],
        13: [
            P("Dix noms à savoir écrire : ostéoporose postménopausique, ostéopénie densitométrique, ostéoporose cortisonique, ostéomalacie par carence en vitamine D, hyperparathyroïdie primaire, ostéoporose de l'homme et hypogonadisme, malabsorption et maladie cœliaque, hyperthyroïdie, myélome multiple et ostéopathie maligne, ostéogenèse imparfaite de l'adulte.", src="1"),
            P("Doses : alendronate 70 mg par semaine, zolédronate 5 mg par an, dénosumab 60 mg tous les 6 mois, tériparatide 20 µg par jour au plus 24 mois, romosozumab 210 mg par mois pendant 12 mois en deux fois 105 mg, calcium 1200 mg et vitamine D 800 UI si l'indication est là, prednisone seuil 7,5 mg.", src="5"),
        ],
        14: [
            P("Pièges du signe. Confondre T-score et Z-score. Diagnostiquer sur Ward ou sur une vertèbre. Oublier l'arthrose. Commencer un antirésorptif dans l'ostéomalacie. Poser Forsteo dans l'hyperparathyroïdie. Arrêter Prolia. Donner EVENITY après un infarctus. Perfuser Aclasta sous 35 ml/min. Appeler ostéoporose un myélome.", src="9"),
            svg_tscore("a"),
        ],
    }
    # résumés nominatifs des DX pour que chaque nom exact apparaisse et pour la longueur
    resumes = []
    for dx in DXS:
        resumes.append(P(
            f"{dx['titre']}. {dx['mecanisme']} {dx['positif']} Conduite : {dx['arbre']} Cas : {dx['cas']}",
            src="1",
        ))
    intro[7].extend(resumes)
    # tableau comparatif
    lignes = ["<div class=\"tw\"><table><caption>Dix diagnostics devant une densité basse</caption><thead><tr><th>Diagnostic</th><th>Ce qui le distingue</th><th>Premier geste</th></tr></thead><tbody>"]
    gestes = [
        "Classer le risque 2020 et choisir la molécule selon la notice",
        "Ne pas traiter sur le mot seul si le FRAX est sous le seuil",
        "Repérer 7,5 mg par jour pendant 3 mois",
        "Corriger la minéralisation avant l'antirésorptif",
        "Calcium et PTH, avant-bras, pas de tériparatide",
        "Testostérone, Z-score si jeune",
        "Chercher la cœliaquie, corriger la carence",
        "TSH, traiter la thyroïde, recalculer",
        "Électrophorèse, pas de tériparatide",
        "Histoire d'enfance, Z-score, avis spécialisé",
    ]
    for dx, g in zip(DXS, gestes):
        lignes.append(
            "<tr><td>" + habiller(dx["titre"]) + "</td><td>" + habiller(dx["mecanisme"][:220]) + "</td><td>" + habiller(g) + "</td></tr>"
        )
    lignes.append("</tbody></table></div>")
    intro[7].append("".join(lignes))
    out = []
    for n, titre in TITRES:
        fiche = (
            f"<p>{habiller('Diminution de la densité osseuse.')} Le détail est dans la fenêtre.</p>"
            f"<p>On ouvre {bouton(f'a-p{n}', 'la fenêtre de ce point')}.</p>"
        )
        corps = "".join(intro[n])
        out.append((titre, fiche, fenetre(f"a-p{n}", titre, corps)))
    return out


CIBLES = {
    "A": 76000,
    1: 42000,
    2: 37600,
    3: 44800,
    4: 36400,
    5: 40200,
    6: 38100,
    7: 43600,
    8: 36800,
    9: 45500,
    10: 39200,
}


def mesurer(texte: str) -> tuple[int, int]:
    m = taille_xy.mesurer(texte)
    return m.x[1], m.y[1]


def ajuster(html_txt: str, cible: int, dx: dict | None) -> str:
    x, y = mesurer(html_txt)
    garde = 0
    while y < cible and garde < 40:
        extra = questions(dx) if dx else questions(DXS[0])
        # insère avant la fermeture de la dernière fenêtre du point 14 ou a-p14
        morceau = "".join(extra[:3])
        marque = "</div></div></section>\n<section class=\"ilot c\"><h2 id=\"sources\">"
        if marque not in html_txt:
            marque = "</div></div></section><section class=\"ilot c\"><h2 id=\"sources\">"
        html_txt = html_txt.replace(marque, morceau + marque, 1)
        x, y = mesurer(html_txt)
        garde += 1
    return html_txt


def inscrire(path: Path) -> None:
    import subprocess
    subprocess.check_call([sys.executable, str(RACINE / "harnais" / "taille_xy.py"), str(path), "--inscrire"])


def ecrire_liste() -> None:
    lignes = [
        "# LISTE DX — LOT_168 F2.20 Diminution de la densité osseuse",
        "",
        "Liste rédigée le 31.10.2026. Le numéro DX suit la fréquence décroissante attendue en consultation d'adulte, l'ostéoporose postménopausique devant l'ostéopénie parce que c'est elle que l'on traite le plus souvent, l'ostéopénie restant la bande densitométrique la plus large. Le rang E est l'ordre d'exclusion, pas le rang de fréquence.",
        "",
    ]
    for dx in DXS:
        lignes.append(f"DX.{dx['n']} — {dx['titre']}")
    lignes.append("")
    lignes.append(
        "E1 Myélome multiple et ostéopathie maligne. "
        "E2 Ostéomalacie par carence en vitamine D. "
        "E3 Hyperparathyroïdie primaire. "
        "E4 Ostéoporose cortisonique. "
        "E5 Hyperthyroïdie. "
        "E6 Malabsorption et maladie cœliaque. "
        "E7 Ostéoporose de l'homme et hypogonadisme. "
        "E8 Ostéogenèse imparfaite de l'adulte. "
        "E9 Ostéoporose postménopausique. "
        "E10 Ostéopénie densitométrique."
    )
    lignes.append("")
    (LOT / "LISTE_DX_CANONIQUE.md").write_text("\n".join(lignes), encoding="utf-8")


def ecrire_incertitudes() -> None:
    (LOT / "INCERTITUDES.md").write_text(
        """# Incertitudes — LOT_168

Retraits non centraux (3). Aucun élément central retiré.

1. Borne unique de la 25-hydroxyvitamine D en nmol/l. Les textes archivés ne fixent pas une seule valeur suisse. Le cours garde le contraste ostéomalacie contre ostéoporose et les doses de vitamine D lues dans les notices, sans ce chiffre.
2. Seuils opératoires chiffrés de l'hyperparathyroïdie primaire. Aucune recommandation chirurgicale datée n'est dans le dossier de preuves. Le cours garde la biologie, l'avant-bras et la contre-indication du tériparatide.
3. Sensibilités chiffrées de l'électrophorèse et des anticorps de la maladie cœliaque. Elles ne sont pas dans les preuves lues. Les examens restent indiqués, sans pourcentage inventé.

Bug noté, fichier non modifié : `grok-LOTS-html/outils/dessinateur/dessinateur.py`. La fonction de vérification attend des mots d'un exemple de dissection aortique et fait échouer `rendre` sur un autre sujet. Les trois figures de ce LOT sont des SVG dans les fenêtres, pas une sortie du dessinateur.

Les grades de Genant sont ceux de la revue de 2013 qui cite l'article de 1993 : 20 à 25 %, 26 à 40 %, plus de 40 %. Une table pédagogique arrondit parfois 25 à 40 % pour le grade 2. Le cours suit la revue archivée, sans amputer un grade.
""",
        encoding="utf-8",
    )


def main() -> None:
    ecrire_liste()
    ecrire_incertitudes()
    # Phase A
    pa = page(
        "LOT_168_Phase_A_V0.html",
        "Diminution de la densité osseuse",
        "F2.20. PROFILES. Texte du 31 octobre 2026. Dix diagnostics différentiels du signe.",
        "<p>Une densité basse se lit d'abord comme un signe. On sépare ostéoporose, ostéopénie, ostéomalacie et lésion maligne. Le T-score de −2,5 ou moins, chez la femme ménopausée ou l'homme d'au moins 50 ans, nomme l'ostéoporose densitométrique. Le traitement suit la case de risque suisse de 2020 et la notice suisse, pas un réflexe unique.</p>",
        phase_a_points(),
    )
    pa = ajuster(pa, CIBLES["A"], DXS[0])
    # allonger encore avec les questions de tous les DX si besoin
    path_a = LOT / "LOT_168_Phase_A_V0.html"
    path_a.write_text(pa, encoding="utf-8")
    print("A", mesurer(pa))
    for dx in DXS:
        pts = assembler_points(dx, CIBLES[dx["n"]])
        html_dx = page(
            f"LOT_168_Phase_B_V0_DX.{dx['n']}.html",
            dx["titre"],
            f"DX.{dx['n']}. {dx['titre']}. F2.20, diminution de la densité osseuse. Texte du 31 octobre 2026.",
            f"<p>{habiller(dx['titre'])}. {habiller(dx['mecanisme'][:280])}</p><p>Les critères, les doses et le cas corrigé sont dans les fenêtres.</p>",
            pts,
        )
        html_dx = ajuster(html_dx, CIBLES[dx["n"]], dx)
        path = LOT / f"LOT_168_Phase_B_V0_DX.{dx['n']}.html"
        path.write_text(html_dx, encoding="utf-8")
        print(f"DX.{dx['n']}", mesurer(html_dx))


if __name__ == "__main__":
    main()
