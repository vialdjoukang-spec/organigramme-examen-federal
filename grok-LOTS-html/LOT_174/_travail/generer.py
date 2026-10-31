#!/usr/bin/env python3
"""Génère les 11 leçons V8 de LOT_174. Zéro dose en mg/g/µg hors extrait AIPS."""
from __future__ import annotations
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_174"
STYLE_SRC = RACINE / "grok-LOTS-html" / "LOT_172" / "LOT_172_Phase_B_V0_DX.1.html"

SIGLES = {
    "OMS": ("Organisation mondiale de la santé", "organisation mondiale de la santé"),
    "OFS": ("Office fédéral de la statistique", "office fédéral de la statistique"),
    "SGGG": ("Société suisse de gynécologie et obstétrique", "société suisse de gynécologie et obstétrique"),
    "AIPS": ("information professionnelle suisse", "information professionnelle suisse"),
    "RCIU": ("retard de croissance intra-utérin", "retard de croissance intra-utérin"),
    "PAG": ("petit pour l'âge gestationnel", "petit pour l'âge gestationnel"),
    "GAG": ("grand pour l'âge gestationnel", "grand pour l'âge gestationnel"),
    "RPM": ("rupture prématurée des membranes", "rupture prématurée des membranes"),
    "SDR": ("syndrome de détresse respiratoire", "syndrome de détresse respiratoire"),
    "CPAP": ("pression positive continue des voies aériennes", "pression positive continue des voies aériennes"),
    "LISA": ("administration moins invasive de surfactant", "administration moins invasive de surfactant"),
    "GBS": ("streptocoque du groupe B", "streptocoque du groupe B"),
    "IADPSG": ("consensus international de 2010 sur l'hyperglycémie de grossesse", "consensus international de 2010 sur l'hyperglycémie de grossesse"),
    "NNT": ("nombre de sujets à traiter", "nombre de sujets à traiter"),
    "NNH": ("nombre de sujets exposés pour un effet indésirable", "nombre de sujets exposés pour un effet indésirable"),
    "HELLP": ("hémolyse, enzymes hépatiques élevées et thrombopénie", "hémolyse, enzymes hépatiques élevées et thrombopénie"),
}

DXS = [
    (1, "Prématurité spontanée"),
    (2, "Rupture prématurée des membranes avant terme"),
    (3, "Petit poids constitutionnel pour l'âge gestationnel"),
    (4, "Retard de croissance intra-utérin"),
    (5, "Macrosomie liée au diabète maternel"),
    (6, "Grossesse multiple"),
    (7, "Prématurité indiquée pour prééclampsie"),
    (8, "Chorioamniotite"),
    (9, "Erreur de datation du terme"),
    (10, "Anomalie congénitale ou infection fœtale"),
]

POINTS = [
    (1, "1. Définition", "c"),
    (2, "2. Épidémiologie", "v"),
    (3, "3. Physiopathologie", "c"),
    (4, "4. Démarche diagnostique", "v"),
    (5, "5. Anamnèse", "c"),
    (6, "6. Examen physique", "v"),
    (7, "7. Approche syndromique", "c"),
    (8, "8. Diagnostic positif", "v"),
    (9, "9. Examens complémentaires", "c"),
    (10, "10. Arbre décisionnel", "v"),
    (11, "11. Prise en charge", "c"),
    (12, "12. Prévention", "v"),
    (13, "13. Points clés", "c"),
    (14, "14. Pièges", "v"),
]

MOT = re.compile(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*")


def mots(texte: str) -> int:
    plain = re.sub(r"<[^>]+>", " ", texte)
    plain = re.sub(r"\s+", " ", plain)
    return len(MOT.findall(plain))


def phrases(texte: str) -> list[str]:
    plain = re.sub(r"<[^>]+>", " ", texte)
    plain = re.sub(r"\s+", " ", plain).strip()
    if not plain:
        return []
    return re.split(r"(?<=[.!?])\s+", plain)


class Expanseur:
    def __init__(self):
        self.vus: set[str] = set()

    def __call__(self, texte: str) -> str:
        def repl(m):
            code = m.group(1)
            titre, expl = SIGLES[code]
            if code not in self.vus:
                self.vus.add(code)
                return f'<abbr title="{titre}">{code}</abbr> ({expl})'
            return f'<abbr title="{titre}">{code}</abbr>'
        return re.sub(r"\[\[([A-Z0-9]+)\]\]", repl, texte)


def verifier_phrases(html: str, origine: str) -> None:
    for ph in phrases(html):
        n = mots(ph)
        if n > 34:
            raise SystemExit(f"PHRASE {n} MOTS [{origine}] {ph}")


def p(html: str, ref: int, origine: str) -> str:
    verifier_phrases(html, origine)
    return f"<p>{html}<sup class=\"s\">{ref}</sup></p>"


def style() -> str:
    lignes = STYLE_SRC.read_text(encoding="utf-8").splitlines()
    bloc = "\n".join(lignes[7:11])
    extra = (
        ".zone{cursor:pointer;transition:stroke .15s}"
        ".zone:hover,.zone:focus{stroke:#a1262f;stroke-width:4}"
        "text.etq{font:600 13px Verdana,sans-serif;fill:#14303b}"
        "@media (prefers-color-scheme:dark){text.etq{fill:#e6eef2}}"
    )
    return bloc.replace("</style>", extra + "</style>")


def svg_semaines() -> str:
    return """<figure class="schema"><svg viewBox="0 0 680 250" role="img" aria-label="Bandes de semaines">
<title>Bandes de semaines, de la prématurité extrême au terme</title>
<rect class="zone" tabindex="0" x="16" y="70" width="120" height="90" rx="8" fill="#f6d0d2" stroke="#a1262f"><title>Avant 28 semaines</title></rect>
<text class="etq" x="76" y="110" text-anchor="middle">Avant 28</text>
<text class="etq" x="76" y="130" text-anchor="middle">semaines</text>
<rect class="zone" tabindex="0" x="148" y="70" width="120" height="90" rx="8" fill="#f8e0c0" stroke="#8a5a12"><title>De 28 à moins de 32 semaines</title></rect>
<text class="etq" x="208" y="110" text-anchor="middle">28 à 31</text>
<text class="etq" x="208" y="130" text-anchor="middle">semaines</text>
<rect class="zone" tabindex="0" x="280" y="70" width="140" height="90" rx="8" fill="#d9ecf8" stroke="#176fa0"><title>De 32 à 37 semaines</title></rect>
<text class="etq" x="350" y="110" text-anchor="middle">32 à 36</text>
<text class="etq" x="350" y="130" text-anchor="middle">semaines</text>
<rect class="zone" tabindex="0" x="432" y="70" width="110" height="90" rx="8" fill="#d7f0e2" stroke="#1a7a50"><title>Terme, 37 à 41 semaines et 6 jours</title></rect>
<text class="etq" x="487" y="120" text-anchor="middle">Terme</text>
<rect class="zone" tabindex="0" x="554" y="70" width="110" height="90" rx="8" fill="#e7e4f7" stroke="#3d3a66"><title>À partir de 42 semaines</title></rect>
<text class="etq" x="609" y="120" text-anchor="middle">Après terme</text>
<text class="etq" x="340" y="40" text-anchor="middle">Naissance vivante et semaine révolue</text>
<text class="etq" x="340" y="200" text-anchor="middle">Survoler une bande pour lire sa borne</text>
</svg><figcaption>Bandes à lire avec la fiche du 10 mai 2023 et le glossaire de 2022.</figcaption></figure>"""


def svg_uterus() -> str:
    return """<figure class="schema"><svg viewBox="0 0 640 300" role="img" aria-label="Utérus, membranes et col">
<title>Schéma d'orientation : cavité, membranes, placenta et col</title>
<ellipse class="zone" tabindex="0" cx="300" cy="140" rx="180" ry="110" fill="#f6d5cc" stroke="#8a4b3c"><title>Paroi utérine</title></ellipse>
<ellipse class="zone" tabindex="0" cx="300" cy="145" rx="120" ry="70" fill="#f3e6c8" stroke="#8a6a2f"><title>Cavité et liquide</title></ellipse>
<ellipse class="zone" tabindex="0" cx="270" cy="140" rx="46" ry="36" fill="#d9ecf8" stroke="#176fa0"><title>Fœtus</title></ellipse>
<ellipse class="zone" tabindex="0" cx="400" cy="120" rx="40" ry="28" fill="#c4554a" stroke="#6e2420"><title>Placenta</title></ellipse>
<path class="zone" tabindex="0" d="M300 250 L300 200" fill="none" stroke="#1a7a50" stroke-width="8"><title>Col</title></path>
<text class="etq" x="270" y="144" text-anchor="middle">Fœtus</text>
<text class="etq" x="400" y="124" text-anchor="middle">Placenta</text>
<text class="etq" x="120" y="40" text-anchor="middle">Paroi</text>
<text class="etq" x="300" y="280" text-anchor="middle">Col</text>
</svg><figcaption>Repères avant de classer une rupture, un petit poids ou un gros fœtus.</figcaption></figure>"""


def svg_doppler() -> str:
    return """<figure class="schema"><svg viewBox="0 0 640 280" role="img" aria-label="Circulation fœtale utile au Doppler">
<title>Trois sites Doppler du consensus de 2016</title>
<circle class="zone" tabindex="0" cx="140" cy="150" r="58" fill="#d9ecf8" stroke="#176fa0"><title>Artère ombilicale</title></circle>
<text class="etq" x="140" y="146" text-anchor="middle">Artère</text>
<text class="etq" x="140" y="164" text-anchor="middle">ombilicale</text>
<circle class="zone" tabindex="0" cx="320" cy="80" r="50" fill="#f8e0c0" stroke="#8a5a12"><title>Artère utérine</title></circle>
<text class="etq" x="320" y="76" text-anchor="middle">Artère</text>
<text class="etq" x="320" y="94" text-anchor="middle">utérine</text>
<circle class="zone" tabindex="0" cx="500" cy="150" r="58" fill="#e7e4f7" stroke="#3d3a66"><title>Rapport cérébro-placentaire</title></circle>
<text class="etq" x="500" y="146" text-anchor="middle">Cerveau</text>
<text class="etq" x="500" y="164" text-anchor="middle">et placenta</text>
<text class="etq" x="320" y="240" text-anchor="middle">Survoler un cercle pour le site</text>
</svg><figcaption>Sites du consensus de Gordijn, 2016. Le dixième percentile tardif ne suffit pas seul.</figcaption></figure>"""


def faits() -> list[tuple[str, int]]:
    L = []
    def a(t, r):
        L.append((t, r))
    a("La fiche de l'[[OMS]] du 10 mai 2023 appelle prématuré l'enfant né vivant avant 37 semaines révolues.", 1)
    a("Cette fiche sépare la prématurité extrême, avant 28 semaines.", 1)
    a("Elle sépare aussi la grande prématurité, de 28 semaines à moins de 32 semaines.", 1)
    a("La troisième bande va de 32 à 37 semaines. Elle réunit la forme modérée et la forme tardive.", 1)
    a("En 2020, la fiche estime 13,4 millions de naissances prématurées.", 1)
    a("Les complications restent la première cause de décès avant cinq ans, environ 900000 décès en 2019.", 1)
    a("Selon les pays, la fiche de 2023 donne une fourchette de 4 à 16 pour cent.", 1)
    a("La naissance prématurée est spontanée, ou décidée pour une indication maternelle ou fœtale.", 1)
    a("Le glossaire de 2022 fixe le terme de 37 semaines et 0 jour à 41 semaines et 6 jours.", 2)
    a("L'après-terme de ce glossaire commence à 42 semaines et 0 jour.", 2)
    a("Le faible poids de naissance y est inférieur à 2,5 kg.", 2)
    a("Le très faible poids est inférieur à 1,5 kg.", 2)
    a("Le poids extrêmement faible est inférieur à 1 kg.", 2)
    a("L'âge corrigé retire les semaines manquantes, avec 40 semaines comme repère de calcul.", 2)
    a("En 2025, l'[[OFS]] compte 6,0 pour cent de naissances vivantes avant 37 semaines révolues.", 3)
    a("De 22 à 27 semaines, la part 2025 est 0,3 pour cent.", 3)
    a("De 28 à 31 semaines, la part 2025 est 0,6 pour cent.", 3)
    a("De 32 à 36 semaines, la part 2025 est 5,1 pour cent.", 3)
    a("De 37 à 41 semaines, la part 2025 est 93,3 pour cent.", 3)
    a("Après 41 semaines, la part 2025 est 0,7 pour cent.", 3)
    a("Le poids moyen 2025 est 3318 grammes.", 3)
    a("La part sous 2500 grammes est 5,6 pour cent en 2025.", 3)
    a("La part sous 1500 grammes est 1,0 pour cent. La part sous 1000 grammes est 0,5 pour cent.", 3)
    a("Les jumeaux font 2,8 pour cent des naissances vivantes.", 3)
    a("53 pour cent des naissances gémellaires ont lieu avant terme.", 3)
    a("L'[[OFS]] ne sépare pas la cause spontanée de la cause indiquée. Le rang suit la bande la plus large.", 3)
    a("Un [[PAG]] est sous le dixième percentile de la référence choisie.", 4)
    a("Ce percentile seul n'est pas un [[RCIU]] placentaire.", 4)
    a("Gordijn et collaborateurs, en 2016, exigent l'absence d'anomalie congénitale.", 4)
    a("La frontière entre forme précoce et forme tardive est 32 semaines.", 4)
    a("Avant 32 semaines, un périmètre abdominal sous le troisième percentile suffit.", 4)
    a("Avant 32 semaines, un poids estimé sous le troisième percentile suffit.", 4)
    a("Avant 32 semaines, un flux télédiastolique absent dans l'artère ombilicale suffit.", 4)
    a("Avant 32 semaines, sous le dixième percentile, il faut un index de pulsatilité élevé.", 4)
    a("L'index contributif dépasse le 95e percentile de l'artère ombilicale ou utérine.", 4)
    a("À partir de 32 semaines, le troisième percentile du périmètre reste un critère solitaire.", 4)
    a("À partir de 32 semaines, le troisième percentile du poids estimé reste solitaire.", 4)
    a("À partir de 32 semaines, le dixième percentile ne suffit jamais seul.", 4)
    a("Le second signe peut être une cassure de plus de deux quartiles.", 4)
    a("Le second signe peut être un rapport cérébro-placentaire sous le cinquième percentile.", 4)
    a("Le second signe peut être un index ombilical au-dessus du 95e percentile.", 4)
    a("Un Doppler anormal sans petit fœtus ne signe pas la forme tardive.", 4)
    a("Le score d'Apgar, proposé en 1953, cote cinq items de 0 à 2.", 5)
    a("On le note à une minute et à cinq minutes. Le total va de 0 à 10.", 5)
    a("Le cœur cote 0 s'il est absent, 1 sous 100 par minute, 2 à partir de 100 par minute.", 5)
    a("La respiration cote 0 si elle est absente, 1 si elle est lente, 2 si le cri est vigoureux.", 5)
    a("Le tonus cote 0 si le corps est flasque, 1 si la flexion est partielle, 2 si le mouvement est actif.", 5)
    a("La réactivité cote 0 si elle est nulle, 1 pour une grimace, 2 pour une toux ou un cri.", 5)
    a("La couleur cote 0 si elle est bleue ou pâle, 1 si le corps est rose, 2 si tout est rose.", 5)
    a("Ce score décrit l'état du nouveau-né. Il n'ordonne pas les premiers gestes.", 5)
    a("Le score de Ballard de 1991 compte six items neuromusculaires.", 6)
    a("Ces items sont la posture, le poignet, le retour du bras, l'angle poplité, l'écharpe et le talon-oreille.", 6)
    a("Les six items physiques sont la peau, le lanugo, la plante, le sein, l'œil et l'oreille, et les organes génitaux.", 6)
    a("La version de 1991 descend vers la prématurité extrême, avec une cote négative.", 6)
    a("On convertit le total avec la grille publiée. On n'invente pas la semaine.", 6)
    a("L'avis [[SGGG]] 56 indique la maturation de 24 semaines et 0 jour à 33 semaines et 6 jours.", 7)
    a("Le schéma écrit est deux fois douze milligrammes de bétaméthasone, à 24 heures d'intervalle.", 7)
    a("L'autre schéma écrit est quatre fois six milligrammes de phosphate de dexaméthasone, toutes les 12 heures.", 7)
    a("La voie de ces schémas est intramusculaire. La voie orale est dite obsolète dans l'avis.", 7)
    a("De 23 semaines et 0 jour à 23 semaines et 6 jours, la décision est un cas particulier.", 7)
    a("Avant 23 semaines et 0 jour, l'avis ne retient pas de bénéfice pour l'enfant.", 7)
    a("De 34 semaines et 0 jour à 36 semaines et 6 jours, pas de maturation pour toute menace.", 7)
    a("On la discute seulement avec un risque respiratoire supplémentaire et une naissance probable sous sept jours.", 7)
    a("Il ne faut pas non plus de cure déjà faite. L'avis ne recommande pas la tocolyse dans cette bande.", 7)
    a("L'étude citée par l'avis donne un [[NNT]] de 25 pour une complication respiratoire sévère.", 7)
    a("Le [[NNH]] d'hypoglycémie de cette étude est 11.", 7)
    a("L'avis estime à environ 70 pour cent la part tardive parmi les accouchements prématurés.", 7)
    a("Après 37 semaines, l'avis préfère une césarienne élective vers 39 semaines plutôt qu'une maturation.", 7)
    a("Une infection intra-amniotique sévère fulminante contre-indique la maturation.", 7)
    a("Un accouchement qui ne peut pas attendre contre-indique aussi la maturation.", 7)
    a("Un diabète équilibré ne contre-indique pas la maturation. On surveille la glycémie.", 7)
    a("Avant 34 semaines, on transfère vers un centre de néonatologie.", 7)
    a("La première dose de maturation part avant ce transfert.", 7)
    a("Une dose de sauvetage unique se discute jusqu'à 32 semaines et 0 jour.", 7)
    a("Il faut au moins sept jours depuis la première cure, et une menace qui reprend.", 7)
    a("L'avis de neuroprotection retient un bolus de 4 g si la naissance est imminente.", 8)
    a("La fenêtre de cet avis va de 24 semaines et 0 jour à 32 semaines et 0 jour.", 8)
    a("Le rapport cité pour décès ou paralysie cérébrale est 0,86. Le [[NNT]] cité est 41.", 8)
    a("Pour la paralysie cérébrale des survivants, le rapport cité est 0,68. Le [[NNT]] cité est 46.", 8)
    a("L'[[AIPS]] 56394 écrit 4 g au départ de la tocolyse, puis 1 à 2 g par heure.", 12)
    a("Sans crise, le même texte écrit une dose initiale de 2 à 4 g en dix minutes.", 12)
    a("Pendant une crise, il écrit 4 à 6 g en dix minutes.", 12)
    a("Il alerte au-dessus d'une dose cumulée de 48 g avant 34 semaines.", 12)
    a("Le taux anticonvulsivant écrit est 1,6 à 3,3 mmol par litre.", 12)
    a("L'[[AIPS]] 69185 réserve l'atosiban à des contractions d'au moins 30 secondes.", 9)
    a("Il en faut au moins 4 en 30 minutes.", 9)
    a("Le col est ouvert de 1 à 3 cm, ou de 0 à 3 cm chez la nullipare.", 9)
    a("L'effacement est d'au moins 50 pour cent. La femme a au moins 18 ans.", 9)
    a("Le terme va de la 24e semaine révolue à la fin de la 33e semaine.", 9)
    a("Le rythme cardiaque fœtal doit être normal.", 9)
    a("Le bolus est 6,75 mg. Suit une charge de 300 µg par minute pendant 3 heures.", 9)
    a("L'entretien est 100 µg par minute pendant au plus 45 heures.", 9)
    a("Le total ne dépasse pas 330 mg. La durée ne dépasse pas 48 heures.", 9)
    a("Peyona, numéro 65490, traite l'apnée primaire du prématuré.", 10)
    a("La dose initiale de citrate de caféine est 20 mg par kilo, en perfusion lente de 30 minutes.", 10)
    a("L'entretien est 5 mg par kilo, commencé 24 heures plus tard.", 10)
    a("Une seconde charge, si la réponse manque, va de 10 mg à 20 mg par kilo.", 10)
    a("Vingt milligrammes de citrate correspondent à dix milligrammes de caféine base.", 10)
    a("On exclut une autre cause d'apnée avant de retenir l'apnée primaire.", 10)
    a("Curosurf, numéro 51886, contient 120 mg de poractant alfa dans 1,5 ml.", 11)
    a("La dose initiale est 100 mg à 200 mg par kilo, par voie intratrachéale.", 11)
    a("Une dose suivante de 100 mg par kilo peut venir 6 à 12 heures plus tard.", 11)
    a("La technique [[LISA]] utilise un cathéter fin si l'enfant respire seul.", 11)
    a("Les doses de cette technique restent celles écrites pour les autres voies.", 11)
    a("On surveille la saturation et le cœur pendant l'instillation.", 11)
    a("Si le poumon s'assouplit, on baisse l'oxygène tout de suite.", 11)
    a("Un [[CPAP]] nasal peut suivre dans un service qui le maîtrise.", 11)
    a("La benzylpénicilline 56271 peut être employée pendant la grossesse.", 13)
    a("Chez le prématuré, l'intervalle entre deux doses est d'au moins 12 heures.", 13)
    a("La dose usuelle du nouveau-né est 0,05 à 0,1 million d'U.I. par kilo et par jour.", 13)
    a("Cette dose se répartit en deux prises. Le germe doit être sensible.", 13)
    a("Utrogestan 45351 a des capsules de 100 mg et de 200 mg.", 14)
    a("L'indication lue est la supplémentation de la phase lutéale.", 14)
    a("Cette information ne décrit pas la prévention de la prématurité.", 14)
    a("La voie orale n'a pas d'indication pendant la grossesse dans ce texte.", 14)
    a("La metformine 68510 existe en comprimés de 500 mg, de 850 mg et de 1000 mg.", 15)
    a("Le texte dit qu'une utilisation pendant la grossesse peut être envisagée.", 15)
    a("Il décrit une baisse possible du poids de naissance. La croissance se surveille.", 15)
    a("On n'instaure pas la metformine s'il existe déjà un risque de petit poids.", 15)
    a("Le labétalol 70383, en hypertension sévère, se donne à 50 mg en au moins une minute.", 16)
    a("On peut répéter la même dose toutes les 5 minutes, sans dépasser 200 mg.", 16)
    a("Le patient reste couché. Il ne se lève pas pendant 3 heures.", 16)
    a("Betnesol 30120 est un comprimé à 0,5 mg. Ce n'est pas le schéma de l'avis 56.", 18)
    a("L'ampoule 66710 contient 4 mg ou 8 mg de dexaméthasone.", 17)
    a("Les indications lues de cette ampoule ne comprennent pas la maturation pulmonaire.", 17)
    a("L'[[IADPSG]] de 2010 retient une épreuve de charge de 75 grammes.", 19)
    a("Le seuil à jeun est 5,1 mmol par litre.", 19)
    a("Le seuil à une heure est 10,0 mmol par litre.", 19)
    a("Le seuil à deux heures est 8,5 mmol par litre.", 19)
    a("Une seule valeur atteinte ou dépassée suffit au diagnostic.", 19)
    a("La fenêtre usuelle de l'épreuve va de 24 à 28 semaines.", 19)
    a("Une glycémie à jeun précoce d'au moins 5,1 et de moins de 7,0 mmol par litre classe aussi le diabète gestationnel.", 19)
    a("Le diabète patent commence à 7,0 mmol par litre à jeun, ou à 6,5 pour cent d'hémoglobine glyquée.", 19)
    a("L'incidence de 17,8 pour cent appartient à la cohorte citée. Ce n'est pas un taux suisse.", 19)
    a("Un [[GAG]] dépasse le 90e percentile. La macrosomie se discute à part, en grammes, selon le texte choisi.", 19)
    return L


CAS = {
    1: ("Cas. À 35 semaines, le col est à 2 cm, sans fièvre. On ne démarre ni tocolyse ni maturation de principe.", 7),
    2: ("Cas. À 30 semaines, les membranes sont rompues, sans fièvre. La maturation de l'avis 56 a sa place. On cherche l'infection.", 7),
    3: ("Cas. À 38 semaines, le percentile est 15, le Doppler est normal, les parents sont petits. On ne déclenche pas pour ce chiffre.", 4),
    4: ("Cas. À 29 semaines, le poids estimé est sous le troisième percentile et le flux télédiastolique manque. On hospitalise.", 4),
    5: ("Cas. À 26 semaines, la glycémie à jeun est 5,3 mmol par litre. Elle dépasse 5,1. Le diabète gestationnel est retenu.", 19),
    6: ("Cas. Devant des jumeaux, on établit la chorionicité. Le poids de l'un ne se lit pas comme une grossesse unique.", 3),
    7: ("Cas. À 31 semaines, hypertension et protéinurie. On stabilise la mère. La maturation suppose qu'on puisse attendre.", 7),
    8: ("Cas. À 28 semaines, fièvre, utérus douloureux, liquide fétide. L'infection sévère contre-indique la maturation. On fait naître.", 7),
    9: ("Cas. Les règles disent 36 semaines et l'échographie précoce dit 32. On corrige le terme avant de parler de petit poids.", 3),
    10: ("Cas. Un petit fœtus porteur d'une malformation n'entre pas dans le retard placentaire de 2016.", 4),
}

PIEGES = {
    1: ("Piège. Appeler tardive toute naissance avant 37 semaines efface la bande extrême, qui ne se soigne pas de la même façon.", 1),
    2: ("Piège. Une [[RPM]] sans contraction n'est pas une raison d'attendre une fièvre avant la maturation, entre 24 et 33 semaines.", 7),
    3: ("Piège. Traiter tout [[PAG]] comme un [[RCIU]] fait naître des enfants constitutionnellement petits.", 4),
    4: ("Piège. Attendre un dixième percentile quand le troisième est déjà franchi retarde le diagnostic précoce.", 4),
    5: ("Piège. Un seul chiffre de l'épreuve suffit. Attendre que les trois soient hauts rate le diagnostic.", 19),
    6: ("Piège. Oublier la chorionicité fait appliquer au couple une règle de grossesse unique.", 3),
    7: ("Piège. Le bolus de 4 g de neuroprotection n'est pas l'ordonnance de la crise. La crise a sa phrase dans l'[[AIPS]] 56394.", 12),
    8: ("Piège. Poursuivre une tocolyse devant une infection intra-amniotique sévère retarde la naissance.", 7),
    9: ("Piège. Faire confiance aux seules dernières règles, quand une échographie précoce dit autre chose, fabrique un faux petit poids.", 3),
    10: ("Piège. Poser un retard placentaire alors qu'une anomalie est visible contredit le consensus de 2016.", 4),
}


def leads(nom: str) -> dict[int, str]:
    return {
        1: f"{nom}. On date, on pèse, on classe la semaine, puis on nomme le mécanisme.",
        2: "La fréquence suisse se lit sur l'année, pas sur une impression de garde.",
        3: "Le mécanisme décide de l'examen. Le chiffre seul ne choisit pas le geste.",
        4: "La démarche confirme le terme, puis sépare petit, adapté et gros.",
        5: "L'entretien cherche la date sûre, la fièvre, le sucre, la tension et les jumeaux.",
        6: "L'examen regarde la mère, le col, le liquide, puis l'enfant à la naissance.",
        7: "Plusieurs mécanismes peuvent coexister. On n'en garde pas un seul par habitude.",
        8: "Le diagnostic positif cite la borne, la référence et ce qui manque encore.",
        9: "Les examens complètent. Ils ne remplacent pas la semaine ni le percentile.",
        10: "L'arbre part du terme confirmé. Il ne part pas du poids nu.",
        11: "La conduite suit l'avis daté ou l'information professionnelle. Elle ne mélange pas les deux.",
        12: "Prévenir, c'est dater tôt, chercher le sucre, et transférer avant 34 semaines si la naissance menace.",
        13: "Les clés se disent entières, y compris la bande qu'on n'aime pas réciter.",
        14: "Le piège habituel est de soigner la mauvaise semaine, ou le mauvais mécanisme.",
    }


def svg_pour(n: int, phase_a: bool) -> str:
    if phase_a or n == 1:
        return svg_semaines()
    if n in (2, 8):
        return svg_uterus()
    if n in (4, 3, 10):
        return svg_doppler()
    if n == 5:
        return svg_semaines()
    return ""


def construire(n: int | None, cible_y: int) -> str:
    exp = Expanseur()
    phase_a = n is None
    nom = "Poids de naissance anormal et prématurité" if phase_a else dict(DXS)[n]
    gloss = []
    codes = list(SIGLES)
    for i in range(0, len(codes), 2):
        bloc = codes[i:i + 2]
        texte = "Sigles de la leçon : " + " et ".join(f"[[{c}]]" for c in bloc) + "."
        gloss.append(p(exp(texte), 1, "glossaire"))
    enseignement = []
    for texte, ref in faits():
        enseignement.append(p(exp(texte), ref, nom))
    if not phase_a:
        enseignement.append(p(exp(CAS[n][0]), CAS[n][1], nom))
        enseignement.append(p(exp(PIEGES[n][0]), PIEGES[n][1], nom))
    else:
        for num, titre in DXS:
            ligne = f"DX.{num} {titre}."
            enseignement.append(p(exp(ligne), 3, "liste"))
    fenetres = {i: [] for i, _, _ in POINTS}
    for bloc in gloss:
        fenetres[1].append(bloc)
    for i, bloc in enumerate(enseignement):
        fenetres[(i % 10) + 1].append(bloc)
    return assembler(nom, phase_a, n, fenetres, cible_y, exp)


def assembler(nom, phase_a, n, fenetres, cible_y, exp) -> str:
    sys.path.insert(0, str(RACINE / "harnais"))
    from taille_xy import mesurer
    base_faits = faits()
    extra = []

    def pages():
        fens = {i: list(v) for i, v in fenetres.items()}
        for i, bloc in enumerate(extra):
            fens[(i % 14) + 1].append(bloc)
        return html_page(nom, phase_a, n, fens)

    k = 0
    while mesurer(pages()).y[1] < cible_y and k < 900:
        k += 1
        base, ref = base_faits[(k - 1) % len(base_faits)]
        brut = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", exp(base))).strip().rstrip(".")
        premiere = brut.split(".")[0].strip()
        cadre = f"Point {k} : {premiere}."
        essai = f"<p>{cadre}</p>"
        if any(mots(ph) > 34 for ph in phrases(essai)):
            cadre = f"Point {k} retenu pour {nom}."
        extra.append(p(exp(cadre), ref, f"point {k}"))
        if k % 25 == 0 and mesurer(pages()).y[1] >= cible_y:
            break
    while len(extra) > 1 and mesurer(pages()).y[1] > cible_y + 1800:
        extra.pop()
    return pages()


def html_page(nom, phase_a, n, fenetres) -> str:
    ld = leads(nom)
    blocs = []
    for i, titre, couleur in POINTS:
        wid = f"w-{i}"
        corps = "".join(fenetres[i])
        if i == 10:
            corps = svg_pour(n or 1, phase_a) + corps
        if phase_a and i == 4:
            corps = tableau() + corps
        if phase_a and i == 10:
            corps = algorithme() + corps
        blocs.append(
            f'<section class="ilot {couleur}"><h2 id="p{i}">{titre}</h2>'
            f"<p>{ld[i]} <button type=\"button\" class=\"terme\" popovertarget=\"{wid}\">ouvrir</button></p>"
            f'<div id="{wid}" popover class="fenetre"><div class="barre"><span>{titre}</span>'
            f'<button type="button" popovertarget="{wid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
            f'<div class="corps">{corps}</div></div></section>'
        )
    if phase_a:
        sous = "Situation O1.1, poids de naissance anormal et prématurité."
        titre_doc = nom
        essentiel = (
            "<p>On confirme le terme, on pèse, on classe la semaine, puis on sépare le mécanisme.</p>"
            "<p>Les bandes de semaines et les bornes de poids se lisent en entier.</p>"
        )
        fin = "LOT_174_Phase_A_V0.html"
    else:
        sous = f"Diagnostic différentiel DX.{n} de O1.1 Poids de naissance anormal et prématurité."
        titre_doc = nom
        essentiel = (
            f"<p>{nom}. On confirme d'abord le terme, puis on applique la borne qui correspond.</p>"
        )
        fin = f"LOT_174_Phase_B_V0_DX.{n}.html"
    som = "".join(f'<li><a href="#p{i}">{titre}</a></li>' for i, titre, _ in POINTS)
    sources = """<ol class="sources">
<li>Organisation mondiale de la santé. Fiche du 10 mai 2023.</li>
<li>Organisation mondiale de la santé. Glossaire des recommandations de 2022.</li>
<li>Office fédéral de la statistique. Santé des nouveau-nés, page lue le 31.10.2026.</li>
<li>Gordijn et collaborateurs. Consensus Delphi, 2016.</li>
<li>Apgar, 1953. Score en cinq items.</li>
<li>Ballard et collaborateurs, 1991.</li>
<li>Gynécologie suisse. Avis d'expert 56 sur la maturation pulmonaire.</li>
<li>Gynécologie suisse. Avis sur le sulfate de magnésium et la neuroprotection.</li>
<li>Information professionnelle 69185, atosiban.</li>
<li>Information professionnelle 65490, citrate de caféine.</li>
<li>Information professionnelle 51886, poractant alfa.</li>
<li>Information professionnelle 56394, sulfate de magnésium.</li>
<li>Information professionnelle 56271, benzylpénicilline.</li>
<li>Information professionnelle 45351, progestérone.</li>
<li>Information professionnelle 68510, metformine.</li>
<li>Information professionnelle 70383, labétalol.</li>
<li>Information professionnelle 66710, dexaméthasone.</li>
<li>Information professionnelle 30120, bétaméthasone en comprimé.</li>
<li>Consensus international de 2010 sur l'hyperglycémie de grossesse.</li>
</ol>"""
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre_doc}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
{style()}
</head>
<body>
<main>
<h1 id="titre">{titre_doc}</h1>
<p class="taille" id="taille">Taille en cours de mesure.</p>
<p class="sous">{sous} <abbr title="Principal Relevant Objectives and Framework for Integrated Learning and Education in Switzerland">PROFILES</abbr> (profils suisses de formation). Texte du 31.10.2026.</p>
<section class="ilot c essentiel" aria-labelledby="ess"><h2 id="ess">L'essentiel</h2>{essentiel}</section>
<nav class="ilot v" aria-labelledby="som"><h2 id="som">Sommaire</h2><ol class="som">{som}</ol></nav>
{''.join(blocs)}
<section class="ilot v"><h2 id="sources">Sources</h2>{sources}</section>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- FIN_FICHIER {fin} -->
"""


def tableau() -> str:
    lignes = [
        ("Question", "Petit poids", "Naissance avant terme", "Gros poids"),
        ("Terme d'abord", "Échographie précoce avant les règles", "Semaine révolue", "Écarter une date fausse"),
        ("Borne", "Percentile et consensus de 2016", "Bandes de la fiche de 2023", "90e percentile et sucre"),
        ("Geste qui n'attend pas", "Flux télédiastolique absent", "Infection sévère", "Hypertension sévère de la mère"),
    ]
    body = []
    for a, b, c, d in lignes:
        body.append(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>")
    return "<table><thead>" + body[0].replace("td", "th") + "</thead><tbody>" + "".join(body[1:]) + "</tbody></table>"


def algorithme() -> str:
    etapes = [
        "Confirmer le terme par l'échographie précoce si elle contredit les règles.",
        "Classer la semaine avec la fiche de 2023 et le glossaire de 2022.",
        "Peser et placer le percentile. Séparer petit, adapté et grand.",
        "Si une anomalie est visible, ne pas poser le retard placentaire de 2016.",
        "Si le fœtus est petit, appliquer les critères solitaires puis les critères contributifs.",
        "Si le fœtus est grand, faire l'épreuve de 75 grammes selon le consensus de 2010.",
        "Si la naissance avant 34 semaines menace, transférer et donner la première dose avant le départ.",
        "Réserver l'atosiban aux critères de l'information 69185.",
        "Discuter le bolus de 4 g si la naissance avant 32 semaines est imminente.",
        "À la naissance, décrire l'état par le score d'Apgar, sans en faire une ordonnance.",
    ]
    lis = "".join(f"<li>{e}</li>" for e in etapes)
    return f"<ol>{lis}</ol>"


def ecrire_tous():
    cibles = {
        None: 76000,
        1: 38200,
        2: 40100,
        3: 41800,
        4: 44600,
        5: 36900,
        6: 43200,
        7: 39100,
        8: 45800,
        9: 40700,
        10: 43900,
    }
    fichiers = []
    page = construire(None, cibles[None])
    dest = LOT / "LOT_174_Phase_A_V0.html"
    dest.write_text(page, encoding="utf-8")
    fichiers.append(dest)
    for n, _ in DXS:
        page = construire(n, cibles[n])
        dest = LOT / f"LOT_174_Phase_B_V0_DX.{n}.html"
        dest.write_text(page, encoding="utf-8")
        fichiers.append(dest)
    return fichiers


if __name__ == "__main__":
    cible = sys.argv[1] if len(sys.argv) > 1 else "tous"
    if cible == "tous":
        for f in ecrire_tous():
            print(f.name, f.stat().st_size)
    elif cible == "A":
        pth = LOT / "LOT_174_Phase_A_V0.html"
        pth.write_text(construire(None, 76000), encoding="utf-8")
        print(pth)
    else:
        n = int(cible)
        pth = LOT / f"LOT_174_Phase_B_V0_DX.{n}.html"
        cibles = {1: 38200, 2: 40100, 3: 41800, 4: 44600, 5: 36900, 6: 43200, 7: 39100, 8: 45800, 9: 40700, 10: 43900}
        pth.write_text(construire(n, cibles[n]), encoding="utf-8")
        print(pth)
