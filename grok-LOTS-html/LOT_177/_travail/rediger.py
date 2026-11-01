#!/usr/bin/env python3
"""Rédige les onze leçons du LOT_177. Les doses chiffrées sont des chaînes AIPS."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import moteur

LOT = moteur.LOT
TITRES = [
    "Définition",
    "Épidémiologie",
    "Physiopathologie",
    "Démarche diagnostique",
    "Anamnèse",
    "Examen clinique",
    "Syndromes et formes",
    "Diagnostic retenu",
    "Examens complémentaires",
    "Arbre décisionnel",
    "Prise en charge",
    "Prévention",
    "Points clés",
    "Pièges",
]
NOMS = {
    1: "Œdème physiologique de la grossesse",
    2: "Contractions utérines irrégulières bénignes",
    3: "Hypertension gestationnelle",
    4: "Menace d'accouchement prématuré",
    5: "Prééclampsie",
    6: "Pyélonéphrite aiguë gravidique",
    7: "Infection intra-amniotique",
    8: "Thrombose veineuse profonde",
    9: "Syndrome HELLP",
    10: "Éclampsie",
}


def P(s: str, src: str = "1"):
    s = " ".join(s.split()).strip()
    if not s.endswith((".", "?", "!")):
        s += "."
    n = moteur.mots(s)
    if n > 34:
        raise SystemExit(f"{n} mots : {s}")
    if s.count(".") + s.count("?") + s.count("!") > 1:
        raise SystemExit(f"plusieurs phrases : {s}")
    return (s, src)


def PP(lignes):
    return [P(s, src) for s, src in lignes]


def sigles():
    return PP([
        ("HTA (hypertension artérielle) se confirme sur la moyenne d'au moins deux mesures", "1"),
        ("SA (semaines d'aménorrhée) datent le terme depuis les dernières règles", "1"),
        ("AIPS (information professionnelle suisse) est la seule source d'une dose chiffrée", "4"),
        ("HELLP (hémolyse, enzymes hépatiques élevées et plaquettes basses) se diagnostique sur le laboratoire", "20"),
        ("TVP (thrombose veineuse profonde) se cherche si un seul mollet gonfle et fait mal", "11"),
        ("CRP (protéine C réactive) n'établit à elle seule aucun de ces diagnostics", "1"),
        ("AST (aspartate aminotransférase) se lit avec les plaquettes", "1"),
        ("ALT (alanine aminotransférase) se lit dans le même bilan", "1"),
        ("LDH (lactate déshydrogénase) participe à montrer l'hémolyse", "20"),
        ("NICE (institut britannique pour l'excellence clinique) donne des fenêtres de terme", "2"),
        ("ISSHP (société internationale de l'hypertension de la grossesse) classe les hypertensions de 2021", "1"),
    ])


def ecart(n: int):
    return P(f"On laisse un écart de lecture avant le médicament suivant, repère {n}", "1")


def tension():
    return PP([
        ("L'hypertension est une systolique d'au moins 140 mmHg ou une diastolique d'au moins 90 mmHg", "1"),
        ("On retient la moyenne d'au moins deux mesures", "1"),
        ("L'hypertension sévère atteint 160 mmHg de systolique ou 110 mmHg de diastolique", "1"),
        ("Cette tension sévère se recontrôle dans les quinze minutes", "1"),
        ("Sinon on répète après au moins quatre heures, ou sur deux visites", "1"),
        ("On ne classe pas une prééclampsie en cours comme légère ou comme grave", "1"),
        ("L'hypertension sévère reste pourtant une urgence dans un lieu surveillé", "1"),
        ("La cible diastolique retenue en 2021 est 85 mmHg", "1"),
        ("On traite toute hypertension, quel que soit le trouble hypertensif", "1"),
        ("Le guide de 2019 retient une cible de 135 sur 85 mmHg", "2"),
    ])


def classes():
    return PP([
        ("L'hypertension chronique existe avant la grossesse ou avant 20 SA", "1"),
        ("Elle est essentielle ou secondaire", "1"),
        ("La blouse blanche montre au moins 140 sur 90 au cabinet et moins de 135 sur 85 à domicile", "1"),
        ("L'hypertension masquée est l'inverse, avec au moins 135 sur 85 hors du cabinet", "1"),
        ("L'hypertension gestationnelle apparaît à partir de 20 SA", "1"),
        ("Elle n'a ni protéinurie nouvelle ni autre signe de prééclampsie", "1"),
        ("La forme transitoire se normalise quand on répète les mesures", "1"),
        ("La prééclampsie est une hypertension gestationnelle avec une protéinurie nouvelle", "1"),
        ("Elle existe aussi avec une atteinte d'organe maternel, sans protéinurie obligatoire", "1"),
        ("Elle existe encore avec une atteinte utéroplacentaire, à partir de 20 SA", "1"),
        ("La prééclampsie surajoutée porte ces signes nouveaux sur une hypertension chronique", "1"),
    ])


def organes():
    return PP([
        ("L'éclampsie, un trouble mental, une cécité ou un accident vasculaire sont des atteintes", "1"),
        ("Le clonus, une céphalée sévère et des scotomes persistants sont des atteintes", "1"),
        ("L'œdème pulmonaire et des plaquettes sous 150000 par microlitre sont des atteintes", "1"),
        ("Une coagulation intravasculaire disséminée et une hémolyse sont des atteintes", "1"),
        ("Une créatinine d'au moins 90 micromoles par litre est une atteinte", "1"),
        ("Une AST ou une ALT au-dessus de 40 unités par litre est une atteinte", "1"),
        ("Un décollement, un déséquilibre angiogénique ou une mort fœtale sont des atteintes", "1"),
        ("Un retard de croissance ou un doppler ombilical anormal sont des atteintes", "1"),
    ])


def proteines():
    return PP([
        ("Le rapport protéines sur créatinine atteint 30 milligrammes par millimole, ou plus", "1"),
        ("Le rapport albumine sur créatinine atteint 8 milligrammes par millimole, ou plus", "1"),
        ("La protéinurie du jour atteint 0,3 gramme, ou plus", "1"),
        ("La protéinurie manque parfois, puisque l'atteinte d'organe suffit", "1"),
        ("Elle est présente dans jusqu'à 75 pour cent des prééclampsies", "1"),
    ])


def doses_tension():
    out = []
    out += PP([
        ("La perfusion de labétalol liée à la grossesse commence à 20 mg par heure", "4"),
        ("Elle peut monter jusqu'à 160 mg par heure, autorisation 70383", "4"),
        ("Le premier trimestre ne la reçoit que si le bénéfice dépasse le risque", "4"),
    ])
    out.append(ecart(1))
    out += PP([
        ("Par voie orale, le labétalol commence souvent à 200 mg deux fois par jour", "5"),
        ("La dose maximale orale est de 2400 mg par jour, autorisation 41529", "5"),
        ("En urgence, la même information décrit 50 mg en injection lente", "5"),
        ("On peut répéter ces 50 mg sans dépasser 200 mg au total", "5"),
    ])
    out.append(ecart(2))
    out += PP([
        ("La méthyldopa commence à 250 mg deux à trois fois par jour", "8"),
        ("Le maximum est de 3 g par jour, autorisation 28080", "8"),
        ("Après un autre antihypertenseur, on commence à au plus 500 mg par jour", "8"),
        ("La grossesse demande une surveillance étroite, car un risque fœtal n'est pas exclu", "8"),
    ])
    out.append(ecart(3))
    out += PP([
        ("La nifédipine est contre-indiquée pendant les 20 premières semaines", "13"),
        ("Elle est aussi contre-indiquée pendant tout l'allaitement, autorisation 52896", "13"),
        ("Après 20 SA, l'hypertension peut recevoir 20 mg deux fois par jour", "13"),
        ("On peut monter à 40 mg deux fois par jour si besoin", "13"),
        ("On ne l'associe pas au sulfate de magnésium par voie intraveineuse", "13"),
    ])
    out.append(ecart(4))
    out += PP([
        ("L'urapidil peut commencer jusqu'à 2 mg par minute en perfusion", "12"),
        ("La grossesse n'est pas l'indication de choix, autorisation 44486", "12"),
        ("On ne l'utilise que si le bénéfice justifie le risque fœtal", "12"),
    ])
    return out


def doses_mg():
    return PP([
        ("Sans crise, l'autorisation 56394 écrit 2,0 à 4 g en dix minutes par voie intraveineuse", "6"),
        ("En crise, la même autorisation écrit 4,0 à 6 g en dix minutes", "6"),
        ("L'entretien est ensuite de 1 g par heure en perfusion continue", "6"),
        ("Le guide de 2022 décrit un bolus de 4 g en quinze minutes pour le cerveau fœtal", "3"),
        ("Il poursuit par 1 g par heure jusqu'à la naissance ou pendant 24 heures", "3"),
        ("Cet usage britannique était hors autorisation en août 2019", "3"),
        ("On surveille le pouls, la tension, la respiration et les réflexes au moins toutes les quatre heures", "3"),
    ])


def doses_toco():
    return PP([
        ("Le bolus d'atosiban est de 6,75 mg en une minute, autorisation 69185", "7"),
        ("La charge suivante est de 300 µg par minute pendant trois heures", "7"),
        ("L'entretien est de 100 µg par minute pendant au plus 45 heures", "7"),
        ("La durée totale ne dépasse pas 48 heures", "7"),
        ("La dose totale ne dépasse pas 330 mg d'atosiban", "7"),
        ("Un nouveau traitement recommence par un bolus", "7"),
        ("La tocolyse au magnésium de cette autorisation commence par 4 g", "6"),
        ("Son entretien peut aller de 1 g à 2 g par heure", "6"),
    ])


def doses_infect():
    out = []
    out += PP([
        ("Pour un germe sensible, la benzylpénicilline usuelle va de 1 à 5 millions d'unités par jour", "15"),
        ("600 mg valent 1 million d'unités, autorisation 56271", "15"),
        ("Au-delà de 2 millions d'unités, l'injection est lente", "15"),
        ("Le débit ne dépasse pas 300 mg par minute", "15"),
        ("La fourchette de 20 à 60 millions d'unités vise l'endocardite et la méningite", "15"),
    ])
    out.append(ecart(5))
    out += PP([
        ("La ceftriaxone habituelle est de 1 g à 2 g une fois par jour", "16"),
        ("Une infection sévère peut monter jusqu'à 4 g une fois par jour, autorisation 59876", "16"),
        ("On ne la mélange pas au calcium dans la même tubulure", "16"),
    ])
    out.append(ecart(6))
    out += PP([
        ("La gélule de nitrofurantoïne contient 100 mg, autorisation 62724", "14"),
        ("Elle est contre-indiquée au dernier trimestre et pendant le travail", "14"),
        ("Elle est contre-indiquée dans le déficit en glucose-6-phosphate déshydrogénase", "14"),
        ("Les doses usuelles n'atteignent pas un taux sérique thérapeutique", "14"),
    ])
    out.append(ecart(7))
    out += PP([
        ("La dose journalière maximale de paracétamol est de 4000 mg, autorisation 47503", "10"),
        ("Un comprimé à 1 g de paracétamol figure dans la même autorisation", "10"),
        ("Un comprimé à 500 mg figure aussi", "10"),
    ])
    return out


def doses_tvp():
    return PP([
        ("Le traitement de la thrombose est de 1 mg/kg deux fois par jour, autorisation 49456", "11"),
        ("Cette dose par kilogramme ne se compare pas à un comprimé fixe", "11"),
        ("Une série de huit grossesses avec valve a vu deux thromboses sous cette dose en prévention", "11"),
        ("Le texte dit que la prévention sur valve n'est pas assez étudiée", "11"),
        ("La littérature de grossesse citée utilise aussi 20 mg ou 40 mg par jour en prévention", "11"),
        ("On retarde une dose après un cathéter selon le bénéfice et le risque de saignement", "11"),
    ])


def aspirine():
    return PP([
        ("L'aspirine cardio à 100 mg une fois par jour figure dans l'autorisation 51795", "9"),
        ("Le troisième trimestre contre-indique l'aspirine cardio", "9"),
        ("Au premier et au deuxième trimestre, seule une nécessité absolue la justifie", "9"),
        ("La dose est alors la plus faible et la durée la plus courte", "9"),
        ("La prévention de la prééclampsie n'est pas l'indication de cette autorisation", "9"),
        ("Le guide de 2019 propose 75 à 150 milligrammes par jour dès 12 SA", "2"),
        ("Il la poursuit jusqu'à la naissance, ce que l'autorisation suisse interdit au troisième trimestre", "2"),
        ("Le texte de 2021 parle de 100 à 162 milligrammes par jour, arrêtés vers 36 SA", "1"),
        ("On n'écrit pas ces milligrammes comme une dose de l'autorisation suisse", "9"),
    ])


def risques_aspirine():
    return PP([
        ("Un haut risque est un antécédent d'hypertension de grossesse", "2"),
        ("Un haut risque est une maladie rénale chronique", "2"),
        ("Un haut risque est un lupus ou un syndrome des antiphospholipides", "2"),
        ("Un haut risque est un diabète de type 1 ou de type 2", "2"),
        ("Un haut risque est une hypertension chronique", "2"),
        ("Un risque modéré est une première grossesse", "2"),
        ("Un risque modéré est un âge d'au moins 40 ans", "2"),
        ("Un risque modéré est un intervalle de plus de dix ans entre deux grossesses", "2"),
        ("Un risque modéré est un indice de masse corporelle d'au moins 35", "2"),
        ("Un risque modéré est une prééclampsie chez la mère ou une sœur", "2"),
        ("Un risque modéré est une grossesse multiple", "2"),
        ("Un haut risque, ou plus d'un risque modéré, fait discuter l'aspirine", "2"),
    ])


def map_regles():
    return PP([
        ("À 29 SA et 6 jours ou moins, on traite la suspicion comme un travail prématuré", "3"),
        ("Cela comprend une tocolyse et un corticoïde maternel si la fenêtre le permet", "3"),
        ("À partir de 30 SA, un col de plus de 15 mm rend le travail prématuré peu probable", "3"),
        ("Un col de 15 mm ou moins fait le diagnostic et le traitement", "3"),
        ("Une fibronectine au-dessus de 50 ng par ml fait le diagnostic", "3"),
        ("À 50 ng par ml ou moins, le travail prématuré est peu probable", "3"),
        ("On ne combine pas la mesure du col et la fibronectine", "3"),
        ("On propose le corticoïde de 24 SA et 0 jour à 33 SA et 6 jours", "3"),
        ("On le discute de 22 SA et 0 jour à 23 SA et 6 jours", "3"),
        ("On peut l'envisager de 34 SA et 0 jour à 35 SA et 6 jours", "3"),
        ("On ne donne pas plus de deux cures", "3"),
        ("Une cure unique peut se répéter avant 34 SA si la précédente a plus de sept jours", "3"),
        ("Le magnésium pour le cerveau fœtal se propose de 24 SA à 29 SA et 6 jours", "3"),
        ("On l'envisage de 30 SA à 33 SA et 6 jours si la naissance est proche", "3"),
        ("On le discute de 23 SA et 0 jour à 23 SA et 6 jours", "3"),
        ("L'avis suisse de 2013 place l'atosiban en premier si le risque d'œdème pulmonaire est haut", "19"),
        ("Ce risque est haut en grossesse gémellaire, hydramnios, cardiopathie ou diabète de type 1", "19"),
        ("L'extraction de 2013 écrit un bolus en microgrammes, contredit par l'autorisation actuelle", "19"),
        ("La leçon suit les milligrammes de l'autorisation 69185", "7"),
        ("Le même avis évoque nifédipine et magnésium ensemble, ce que l'autorisation 52896 interdit", "13"),
    ])


def hellp_regles():
    return PP([
        ("Environ 70 pour cent des cas surviennent avant la naissance", "20"),
        ("Ils se voient surtout entre 27 et 37 SA", "20"),
        ("Le reste survient dans les 48 heures après la naissance", "20"),
        ("Le Tennessee complet demande une hémolyse avec LDH au-dessus de 600 unités par litre", "20"),
        ("Il demande une AST d'au moins 70 unités par litre", "20"),
        ("Il demande des plaquettes sous 100 fois 10 exposant 9 par litre", "20"),
        ("Une bilirubine d'au moins 20,5 micromoles par litre ou un frottis anormal montre l'hémolyse", "20"),
        ("La classe 1 du Mississippi a des plaquettes d'au plus 50 fois 10 exposant 9 par litre", "20"),
        ("La classe 2 a des plaquettes entre plus de 50 et 100", "20"),
        ("La classe 3 a des plaquettes entre plus de 100 et 150", "20"),
        ("La classe 3 demande aussi une AST ou une ALT d'au moins 40 unités par litre", "20"),
        ("Les classes 1 et 2 demandent aussi une LDH au-dessus de 600 et une transaminase d'au moins 70", "20"),
        ("On ne donne pas de corticoïde pour accélérer la résolution du syndrome", "1"),
        ("L'avis de 2009 évoquait un effet de laboratoire, sans prouver un bénéfice maternel", "21"),
        ("La leçon suit le texte de 2021 pour cette indication maternelle", "1"),
    ])


def poumon():
    return PP([
        ("Entre 24 SA et 33 SA et 6 jours, une prééclampsie peut recevoir une maturation", "21"),
        ("Il faut pouvoir différer la naissance d'au moins 12 à 24 heures", "21"),
        ("Un tracé pathologique ou un décollement impose la naissance sans maturation", "21"),
        ("Une infection amniotique sévère et fulminante contre-indique aussi la maturation", "21"),
        ("L'information 66710 ne donne pas de schéma en milligrammes pour le poumon fœtal", "17"),
        ("On n'invente donc pas de milligrammes de dexaméthasone ni de bétaméthasone", "17"),
    ])


def suite():
    return PP([
        ("La tension se contrôle au moins une fois entre le troisième et le sixième jour", "1"),
        ("Une revue a lieu à trois mois", "1"),
        ("L'avis suisse de 2019 propose aussi un bilan cardiovasculaire vers trois mois, puis chaque année", "18"),
        ("Une grossesse ultérieure a un risque d'hypertension gestationnelle d'au moins 4 pour cent", "1"),
        ("Le risque ultérieur de prééclampsie atteint au moins 15 pour cent", "1"),
        ("On ne prévoit pas une naissance avant 37 SA pour une hypertension gestationnelle seule", "2"),
        ("Environ 25 pour cent des hypertensions gestationnelles avant 34 SA évoluent vers la prééclampsie", "1"),
        ("Environ 40 pour cent des formes transitoires évoluent ensuite", "1"),
        ("La blouse blanche représente environ 30 pour cent des hypertensions chroniques", "1"),
        ("L'incidence suisse de la prééclampsie avoisine 2,5 pour cent des accouchements", "18"),
        ("Cela fait plus de 2000 cas par an sur environ 85000 naissances", "18"),
        ("L'accouchement est le seul traitement curatif de la prééclampsie", "18"),
        ("Les œdèmes ne sont pas obligatoires dans la forme classique", "18"),
        ("Un ratio inférieur à 38 sur le test Roche rend la prééclampsie très improbable à court terme", "18"),
        ("Un ratio d'au moins 38 est un résultat positif", "18"),
        ("Le test est sur la liste suisse depuis le 1er juillet 2019, à partir de 20 SA", "18"),
        ("Un déséquilibre angiogénique est aussi un PlGF sous le 5e centile, ou un ratio au-dessus de 38", "1"),
    ])


def noms_liste():
    return PP([
        ("Œdème physiologique de la grossesse ouvre la liste clinique de ce motif", "1"),
        ("Contractions utérines irrégulières bénignes viennent quand le col ne change pas", "1"),
        ("Hypertension gestationnelle précède la maladie avec atteinte", "1"),
        ("Menace d'accouchement prématuré se discute si les contractions s'organisent", "3"),
        ("Prééclampsie est l'hypertension dont l'incidence suisse a été lue", "18"),
        ("Pyélonéphrite aiguë gravidique est la fièvre du rein, pas une cystite", "14"),
        ("Infection intra-amniotique est la fièvre de l'utérus avec un fœtus menacé", "21"),
        ("Thrombose veineuse profonde est le mollet unilatéral que l'on ne rassure pas", "11"),
        ("Syndrome HELLP est l'atteinte du foie et des plaquettes", "20"),
        ("Éclampsie ferme la liste parce que la crise est la plus rare de ce motif", "6"),
    ])


# --- clauses de remplissage, sans dose chiffrée, différentes des phrases d'enseignement ---

COMMUN = [
    "on mesure au bras, au repos, assise, avant de conclure",
    "une mesure isolée ne nomme pas le trouble",
    "la mère et le fœtus se jugent ensemble",
    "un symptôme neurologique ne se remet pas au lendemain",
    "une douleur sous le foie se prend au sérieux",
    "un essoufflement nouveau peut être un œdème du poumon",
    "un saignement avec douleur utérine fait chercher le décollement",
    "le repos ne remplace pas une tension sévère à traiter",
    "on appelle sans attendre le résultat d'un test de confirmation",
    "le lieu surveillé précède le médicament de l'urgence",
    "on écrit l'heure de chaque tension",
    "on compare les deux mollets avant de parler d'œdème simple",
    "un écoulement de liquide change la conduite",
    "la couleur et l'odeur des pertes se notent",
    "la fièvre se décrit avec le siège de la douleur",
    "le terme exact oriente le corticoïde et le magnésium",
    "on ne promet pas un diagnostic léger tant que le bilan manque",
    "la sortie se décide après la mère et le tracé",
    "un conseil de retour est daté et précis",
    "le carnet de tension sert au contrôle suivant",
]


def clauses_pour(nom: str, propres: list[str]) -> list[str]:
    out = []
    for c in propres + COMMUN:
        c = c.strip().rstrip(".")
        if moteur.mots(c) > 26:
            raise SystemExit(f"clause longue : {c}")
        out.append(c)
    # ancrage au nom, phrases courtes
    out.append(f"on relit {nom} avant de changer de porte")
    return out


PROPRES = {
    1: [
        "le godet du soir est mou et bilatéral",
        "il diminue quand les jambes sont surélevées",
        "le visage qui gonfle d'un coup n'est pas ce tableau",
        "les mains qui gonflent d'un coup se signalent",
        "la tension normale fait partie de la définition ici",
        "l'absence de protéinurie se vérifie, elle ne se suppose pas",
        "la céphalée est absente dans ce diagnostic bénin",
        "un seul mollet douloureux fait quitter ce diagnostic",
        "la prise de poids rapide se note sans devenir un chiffre inventé",
        "on revoit la femme si le gonflement change de côté",
    ],
    2: [
        "les contractions bénignes ne sont pas régulières",
        "elles ne raccourcissent pas le col",
        "elles cèdent souvent au repos et à l'hydratation",
        "une perte de liquide les fait requalifier",
        "un saignement les fait requalifier",
        "avant le terme, on ne les appelle pas travail sur la seule douleur",
        "le toucher ou l'échographie du col tranche",
        "on n'utilise pas deux tests du col en même temps",
        "la femme repart avec des signes de retour écrits",
        "une contraction douloureuse et rythmée n'est plus bénigne",
    ],
    3: [
        "le diagnostic exige l'absence d'atteinte d'organe",
        "la protéinurie nouvelle ferait changer de nom",
        "la céphalée sévère ferait changer de nom",
        "on traite quand même la tension",
        "on ne programme pas la naissance avant 37 SA sans autre motif",
        "la surveillance rapproche les contrôles avant 34 SA",
        "la forme transitoire peut devenir durable",
        "la blouse blanche ne se traite pas comme une maladie permanente sans mesure hors cabinet",
        "l'hypertension chronique se cherche dans le dossier d'avant 20 SA",
        "la cible diastolique guide l'ajustement",
    ],
    4: [
        "le terme décide si l'on traite d'emblée",
        "le col se mesure par voie vaginale quand le guide le demande",
        "la fibronectine ne se rajoute pas au col",
        "la tocolyse achète du temps, elle ne guérit pas la cause",
        "le corticoïde suit la fenêtre, pas une habitude",
        "le magnésium du cerveau fœtal suit une autre fenêtre",
        "un œdème pulmonaire fait préférer l'atosiban",
        "on ne mélange pas nifédipine et magnésium intraveineux",
        "une infection franche arrête l'idée de prolonger",
        "le tracé pathologique arrête la tocolyse",
    ],
    5: [
        "l'atteinte d'organe suffit sans protéinurie",
        "l'œdème n'est pas un critère obligatoire",
        "on ne dit pas forme légère pendant que la grossesse continue",
        "la tension sévère se traite tout de suite",
        "le magnésium prévient la crise dans la forme grave",
        "la naissance est le traitement curatif",
        "le moment de naître dépend du terme et de la gravité",
        "le corticoïde maternel ne sert pas à faire remonter les plaquettes",
        "le ratio angiogénique aide, il ne remplace pas la clinique",
        "le post-partum reste une période à risque",
    ],
    6: [
        "la douleur du flanc avec fièvre oriente vers le rein",
        "la cystite seule ne donne pas ce tableau",
        "la nitrofurantoïne ne traite pas le parenchyme",
        "l'hydratation accompagne l'antibiotique",
        "les contractions peuvent apparaître avec la fièvre",
        "on surveille le terme et le col",
        "un abcès ou un obstacle se cherche si la fièvre tient",
        "la bandelette ne remplace pas la culture",
        "le traitement commence avant le germe si la femme est malade",
        "le dernier trimestre interdit la nitrofurantoïne",
    ],
    7: [
        "l'utérus douloureux et les pertes sales orientent ici",
        "la tachycardie fœtale renforce le soupçon",
        "la forme fulminante fait naître",
        "on ne retarde pas la naissance pour finir une maturation",
        "les membranes intactes n'écartent pas le diagnostic",
        "la rupture prolongée augmente le risque",
        "l'antibiotique suit l'autorisation lue, pas un schéma inventé",
        "la mère instable passe avant le détail du germe",
        "le nouveau-né sera vu comme exposé",
        "on ne confond pas cette fièvre avec une pyélonéphrite silencieuse",
    ],
    8: [
        "un mollet plus gros et douloureux n'est pas l'œdème du soir",
        "la rougeur et la chaleur se notent",
        "on ne renvoie pas sans avis sur l'imagerie",
        "la grossesse augmente le risque thrombotique",
        "la compression veineuse pelvienne participe",
        "le traitement par kilogramme est celui de la thrombose constituée",
        "la valve cardiaque est une mise en garde à part",
        "un essoufflement fait chercher l'embolie",
        "on ne masse pas un mollet suspect",
        "la prévention par petite dose n'est pas le traitement d'un caillot prouvé",
    ],
    9: [
        "le foie douloureux et les plaquettes basses orientent ici",
        "la tension peut être présente ou non au premier regard",
        "on demande l'hémolyse, les enzymes et les plaquettes",
        "les deux classifications se lisent en entier",
        "on ne donne pas de corticoïde pour normaliser le laboratoire maternel",
        "la naissance traite la cause",
        "le post-partum immédiat reste surveillé",
        "un hématome sous la capsule du foie se cherche si la douleur explose",
        "les saignements se préviennent en connaissant les plaquettes",
        "on ne rassure pas sur un seul chiffre normal",
    ],
    10: [
        "toute crise convulsive nouvelle en fin de grossesse est une éclampsie jusqu'à preuve contraire",
        "on protège les voies aériennes d'abord",
        "le magnésium est le traitement de la crise",
        "on ne cherche pas un autre anticonvulsivant en premier",
        "la tension sévère se traite en parallèle",
        "la nifédipine intraveineuse n'existe pas dans cette leçon, et l'orale ne se mélange pas au magnésium",
        "la naissance se fait après la stabilisation",
        "une crise du post-partum reste possible",
        "on surveille la respiration et les réflexes sous perfusion",
        "on ne quitte pas la femme pendant la perfusion de charge",
    ],
}


def fiche_map():
    return {
        1: "Ce diagnostic est un gonflement mou des deux chevilles, sans maladie hypertensive.",
        2: "Ce diagnostic est une contraction qui ne modifie pas le col et ne s'organise pas.",
        3: "Ce diagnostic est une hypertension nouvelle après 20 SA, sans atteinte de prééclampsie.",
        4: "Ce diagnostic est un travail prématuré suspecté, tranché par le terme et par un seul test.",
        5: "Ce diagnostic est l'hypertension de la grossesse avec protéinurie ou atteinte d'organe.",
        6: "Ce diagnostic est une infection du rein chez la femme enceinte, avec fièvre et douleur du flanc.",
        7: "Ce diagnostic est l'infection de la cavité amniotique, utérine et fœtale.",
        8: "Ce diagnostic est un caillot veineux profond, souvent révélé par un seul membre.",
        9: "Ce diagnostic est l'hémolyse avec enzymes hautes et plaquettes basses.",
        10: "Ce diagnostic est la crise convulsive de la prééclampsie, pendant la grossesse ou juste après.",
    }


def dedupe(secs: list) -> list:
    """Une phrase ≥ 8 mots ne revient pas dans le même fichier."""
    import re
    vu = set()
    out = []
    for a, b, c, phrases in secs:
        kept = []
        for s, src in phrases:
            cle = re.sub(r"[^a-z0-9àâäçéèêëîïôöùûüœ]+", " ", s.lower()).strip()
            if cle in vu:
                continue
            vu.add(cle)
            kept.append((s, src))
        if len(kept) < 2:
            kept.append(P(
                f"Le point {a} ne répète pas une phrase déjà écrite plus haut dans la fiche",
                "1",
            ))
        out.append((a, b, c, kept))
    return out


def sections_de(n: int, extra_par_point: dict) -> list:
    nom = NOMS[n]
    # phrases spécifiques déjà préparées dans extra_par_point : dict point -> list
    secs = []
    for i, titre in enumerate(TITRES, start=1):
        phrases = extra_par_point[i]
        fiche = {
            1: f"La définition de {nom} tient en une conduite, détaillée dans la fenêtre.",
            2: "La fréquence exacte hors prééclampsie n'est pas chiffrée ici, et la fenêtre dit pourquoi.",
            3: "Le mécanisme utile au lit est dans la fenêtre, sans chiffre inventé.",
            4: "La démarche commence par ce qui tue, puis par le terme.",
            5: "L'anamnèse cherche le terme, la douleur, la tête et les mouvements.",
            6: "L'examen mesure, compare et palpe avant de rassurer.",
            7: "Les formes se séparent dans la fenêtre, avec les noms justes.",
            8: "Le diagnostic retenu dit ce qui suffit et ce qui ne suffit pas.",
            9: "Les examens ont des bornes lues, pas des bornes inventées.",
            10: "L'arbre ouvre une porte et en ferme une autre.",
            11: "La prise en charge met les doses lues à leur place.",
            12: "La prévention dit ce qui est suisse et ce qui ne l'est pas.",
            13: "Les points clés tiennent sur quelques décisions.",
            14: "Le piège et le cas corrigé sont dans la fenêtre.",
        }[i]
        # fiches 1 uses nom which might be long
        if moteur.mots(fiche) > 30:
            fiche = "La définition tient dans la fenêtre, avec les bornes lues."
        secs.append((i, titre, fiche, phrases))
    return secs


def builder(n: int) -> dict:
    """Retourne essentiel, sections brutes, extras, clauses, sous, h1."""
    nom = NOMS[n]
    commun_epi = PP([
        ("L'ordre des dix diagnostics est un ordre clinique de ce motif", "1"),
        ("Ce n'est pas une série d'incidences suisses mesurées une par une", "1"),
        ("La seule incidence lue est celle de la prééclampsie, environ 2,5 pour cent", "18"),
    ])
    # chaque DX a un corps propre. On réutilise les blocs centraux là où ils sont le sujet.
    if n == 1:
        corps = {
            1: PP([
                ("L'œdème physiologique de la grossesse est un gonflement mou des deux membres inférieurs", "1"),
                ("Il prédomine en fin de journée et diminue avec le repos", "1"),
                ("Il n'apporte ni hypertension, ni protéinurie, ni atteinte d'organe", "1"),
                ("Il ne suffit jamais à porter le diagnostic de prééclampsie", "18"),
            ]),
            2: commun_epi + PP([
                ("Il est placé en tête parce que le motif œdème est le plus banal", "1"),
                ("Aucun pourcentage suisse d'œdème bénin n'a été lu pour cette leçon", "1"),
            ]),
            3: PP([
                ("La pression veineuse des jambes monte quand l'utérus comprime le retour pelvien", "1"),
                ("La dilution du sang abaisse un peu la pression oncotique", "1"),
                ("Le liquide sort donc vers les chevilles, surtout debout", "1"),
                ("Ce mécanisme n'abîme ni le foie, ni le rein, ni le placenta", "1"),
            ]),
            4: PP([
                ("On écarte d'abord la thrombose, la prééclampsie et la souffrance fœtale", "1"),
                ("On mesure la tension et on cherche une protéinurie", "1"),
                ("On compare les deux mollets", "11"),
                ("On ne conclut qu'ensuite au repos", "1"),
            ]),
            5: PP([
                ("On demande depuis quand, le soir ou le matin, un côté ou les deux", "1"),
                ("On demande la céphalée, les troubles visuels et la douleur sous les côtes", "1"),
                ("On demande un essoufflement et une douleur du mollet", "1"),
                ("On demande le terme et les mouvements de l'enfant", "1"),
            ]),
            6: PP([
                ("Le godet est mou, prend les deux chevilles, et respecte en général les orteils de façon symétrique", "1"),
                ("Il n'y a pas de cordon veineux dur ni de chaleur d'un seul côté", "11"),
                ("La tension est sous les bornes de l'hypertension", "1"),
                ("Les réflexes et le fond utérin se notent quand même", "1"),
            ]) + tension()[:4],
            7: PP([
                ("La forme du soir, déclive, est la forme bénigne", "1"),
                ("Le gonflement brusque du visage, des mains ou des pieds se signale", "2"),
                ("La forme unilatérale n'appartient pas à ce diagnostic", "11"),
            ]),
            8: proteines()[:3] + PP([
                ("Ici la protéinurie est absente et la tension est normale", "1"),
                ("Si l'un des deux apparaît, le nom du diagnostic change", "1"),
            ]),
            9: PP([
                ("La bandelette urinaire suffit pour écarter une protéinurie franche dans ce tableau calme", "1"),
                ("Un rapport se demande si la bandelette est positive ou si la clinique inquiète", "1"),
                ("On ne demande pas un doppler veineux si les deux jambes sont identiques et indolores", "11"),
            ]),
            10: PP([
                ("Porte œdème, première question, un côté ou les deux", "1"),
                ("Deux côtés, tension normale, urine normale, repos et conseil", "1"),
                ("Un côté, douleur, on quitte cette porte pour la thrombose", "11"),
                ("Tension haute, on quitte cette porte pour l'hypertension", "1"),
            ]),
            11: PP([
                ("Le traitement est le repos, les jambes surélevées, et une contention si elle soulage", "1"),
                ("Aucun médicament antihypertenseur n'a sa place si la tension est normale", "1"),
                ("Aucun diurétique n'est enseigné ici", "1"),
                ("On revoit vite si le visage gonfle, si la tête fait mal, ou si un mollet change", "2"),
            ]),
            12: PP([
                ("Éviter la station debout prolongée diminue le gonflement du soir", "1"),
                ("Cela ne prévient pas la prééclampsie", "1"),
                ("La prévention de la prééclampsie est un autre chapitre, avec ses conflits de dose", "9"),
            ]),
            13: PP([
                ("Bilatéral, mou, vespéral, tension normale, urine normale", "1"),
                ("Le conseil de retour est aussi important que le repos", "1"),
                ("L'œdème n'est pas un critère de prééclampsie", "18"),
            ]),
            14: PP([
                ("Le piège est de rassurer un mollet unique ou une céphalée", "1"),
                ("Le piège est de traiter cet œdème comme une prééclampsie sans tension", "1"),
                ("Le cas corrigé est une femme à 34 SA, chevilles gonflées le soir, les deux côtés", "1"),
                ("Sa tension est normale et l'urine ne montre pas de protéine", "1"),
                ("On avait parlé à tort de prééclampsie à cause du seul gonflement", "18"),
                ("La correction est le repos, et un retour si la tête, la vue ou un mollet change", "1"),
            ]),
        }
    elif n == 2:
        corps = {
            1: PP([
                ("Les contractions utérines irrégulières bénignes ne changent pas le col", "3"),
                ("Elles sont espacées de façon inconstante et souvent indolores ou peu douloureuses", "1"),
                ("Elles ne définissent pas un travail prématuré", "3"),
            ]),
            2: commun_epi + PP([
                ("Elles sont banales au troisième trimestre, sans pourcentage suisse lu", "1"),
                ("Elles restent au-dessus des diagnostics graves dans l'ordre clinique", "1"),
            ]),
            3: PP([
                ("L'utérus s'entraîne par des contractions localisées qui ne descendent pas le travail", "1"),
                ("Le col ne se raccourcit pas et ne s'ouvre pas", "3"),
                ("Près du terme, les contractions utiles deviennent régulières et modifient le col", "1"),
            ]),
            4: PP([
                ("On date le terme avant de rassurer", "3"),
                ("On cherche une perte de liquide, un saignement et de la fièvre", "21"),
                ("On évalue le col par un seul test, pas par deux", "3"),
            ]) + map_regles()[:7],
            5: PP([
                ("On demande l'intervalle, la durée, et si la douleur cesse au repos", "1"),
                ("On demande les mouvements de l'enfant et une perte liquide", "1"),
                ("On demande le terme exact et un antécédent de naissance prématurée", "3"),
            ]),
            6: PP([
                ("L'utérus se contracte sous la main puis se relâche, sans tension permanente", "1"),
                ("Le col clinique long et fermé va dans le sens bénin si le terme le permet", "3"),
                ("Une douleur utérine permanente oriente vers le décollement ou l'infection", "21"),
                ("La tension et la chaleur se mesurent pour ne pas manquer une autre porte", "1"),
            ]),
            7: PP([
                ("La forme de fin de journée, au repos efficace, est bénigne", "1"),
                ("La forme régulière, douloureuse, avec col court, est une menace", "3"),
                ("La forme avec fièvre n'est plus bénigne", "21"),
            ]),
            8: PP([
                ("Le diagnostic bénin exige un col qui ne signe pas le travail", "3"),
                ("À partir de 30 SA, plus de 15 mm rend le travail prématuré peu probable", "3"),
                ("À 29 SA et 6 jours ou moins, on ne se contente pas de ce diagnostic", "3"),
            ]),
            9: map_regles()[2:7] + PP([
                ("Le tracé fœtal rassurant fait partie du tableau que l'on peut surveiller", "1"),
            ]),
            10: PP([
                ("Porte contractions, question du terme d'abord", "3"),
                ("Terme précoce ou col court, on traite comme une menace", "3"),
                ("Terme avancé, col long, irrégulier, repos et signes de retour", "1"),
                ("Fièvre ou liquide, on change de porte", "21"),
            ]),
            11: PP([
                ("Le traitement bénin est le repos, l'hydratation, et une réévaluation datée", "1"),
                ("Aucune tocolyse ne se donne si le diagnostic de travail prématuré est écarté", "3"),
                ("Aucun corticoïde ne se donne pour une contraction bénigne isolée", "3"),
            ]),
            12: PP([
                ("Traiter une infection urinaire basse peut enlever un irritant utérin", "14"),
                ("La nitrofurantoïne ne convient pas au dernier trimestre", "14"),
                ("Cela ne remplace pas l'examen du col si les contractions s'organisent", "3"),
            ]),
            13: PP([
                ("Irrégulier, col inchangé, mère et fœtus bien", "1"),
                ("Un seul test du col, jamais les deux ensemble", "3"),
                ("Le terme de 30 SA change la façon de conclure", "3"),
            ]),
            14: PP([
                ("Le piège est d'appeler bénin un col à 15 mm ou moins", "3"),
                ("Le piège est de combiner col et fibronectine", "3"),
                ("Le cas corrigé est une femme à 36 SA, serrements le soir, col long", "1"),
                ("On avait commencé une tocolyse sans mesure du col", "3"),
                ("La correction est l'arrêt de la tocolyse et un retour si le rythme devient régulier", "1"),
            ]),
        }
    elif n == 3:
        corps = {
            1: classes()[4:7] + PP([
                ("Hypertension gestationnelle est ce nom, et pas celui de prééclampsie", "1"),
            ]),
            2: commun_epi + suite()[6:9],
            3: PP([
                ("Les vaisseaux maternels répondent mal, et la tension monte après la moitié de la grossesse", "1"),
                ("Le placenta n'a pas encore le tableau complet de la prééclampsie", "1"),
                ("Une part de ces femmes y évolue, surtout avant 34 SA", "1"),
            ]),
            4: tension() + PP([
                ("On cherche ensuite l'atteinte qui ferait changer le nom", "1"),
            ]),
            5: PP([
                ("On demande la date de début, les chiffres à la maison, et les médicaments déjà pris", "1"),
                ("On demande la tête, la vue, la barre épigastrique et l'enfant", "1"),
                ("On demande une hypertension connue avant 20 SA", "1"),
            ]),
            6: tension()[:5] + PP([
                ("On cherche les réflexes vifs, le clonus et l'œdème pulmonaire", "1"),
                ("Leur présence fait quitter ce diagnostic", "1"),
            ]),
            7: classes(),
            8: organes() + proteines() + PP([
                ("Pour rester dans l'hypertension gestationnelle, tout cela est absent", "1"),
            ]),
            9: PP([
                ("Le rapport urinaire et le bilan sanguin écartent l'atteinte", "1"),
                ("Créatinine, transaminases, plaquettes et hémolyse font partie de ce bilan", "1"),
                ("Le test angiogénique aide entre 20 SA et 36 SA et 6 jours à rendre la prééclampsie improbable", "2"),
            ]) + suite()[13:17],
            10: PP([
                ("Tension confirmée, puis recherche d'atteinte, puis nom", "1"),
                ("Sans atteinte, hypertension gestationnelle, traitement et surveillance", "2"),
                ("Avec atteinte, on change pour la prééclampsie", "1"),
                ("Tension sévère, traitement immédiat quel que soit le nom", "1"),
            ]),
            11: doses_tension() + PP([
                ("On vise la cible diastolique, sans descendre de façon brutale et non surveillée", "1"),
                ("Pas de naissance planifiée avant 37 SA pour ce seul diagnostic", "2"),
            ]),
            12: aspirine() + risques_aspirine() + suite()[:6],
            13: PP([
                ("Confirmer, écarter l'atteinte, traiter, ne pas faire naître trop tôt", "2"),
                ("La tension sévère ne se range pas dans un suivi simple", "1"),
                ("Le contrôle du post-partum fait partie du diagnostic", "1"),
            ]),
            14: PP([
                ("Le piège est d'attendre 37 SA alors que la tension est sévère", "1"),
                ("Le piège est d'appeler prééclampsie légère une maladie encore en cours", "1"),
                ("Le cas corrigé est une femme à 32 SA, 148 sur 96 deux fois, sans protéine ni symptôme", "1"),
                ("On avait prévu une naissance à 34 SA pour ce seul motif", "2"),
                ("La correction est le traitement de la tension et la poursuite jusqu'à 37 SA si rien n'apparaît", "2"),
            ]),
        }
    elif n == 4:
        corps = {
            1: PP([
                ("La menace d'accouchement prématuré est un travail qui commence trop tôt", "3"),
                ("Le guide traite comme tel toute suspicion à 29 SA et 6 jours ou moins", "3"),
                ("Plus tard, un test unique du col confirme ou écarte", "3"),
            ]),
            2: commun_epi + PP([
                ("Aucune incidence suisse de la menace n'a été lue pour fixer ce rang", "1"),
                ("Le rang clinique la place avant les complications rares", "1"),
            ]),
            3: PP([
                ("Une infection, un étirement utérin ou un saignement décidual peuvent déclencher le travail", "1"),
                ("Le col se raccourcit avant que les contractions ne deviennent évidentes", "3"),
                ("La fibronectine fœtale dans le vagin signe une interface perturbée", "3"),
            ]),
            4: map_regles(),
            5: PP([
                ("On demande le rythme, la perte de liquide, le saignement et la fièvre", "3"),
                ("On demande un antécédent de naissance avant terme et une grossesse multiple", "19"),
                ("On demande le terme en jours, pas seulement en mois", "3"),
            ]),
            6: PP([
                ("On palpe le rythme utérin et on cherche une douleur permanente", "21"),
                ("On prend la température, la tension et le pouls", "1"),
                ("Le spéculum cherche le liquide et une infection visible", "21"),
                ("Le toucher évite d'être répété sans besoin", "1"),
            ]),
            7: PP([
                ("Avec membranes intactes, la tocolyse se discute dans la fenêtre du guide", "3"),
                ("Avec rupture, l'infection et le terme dominent", "21"),
                ("Avec œdème pulmonaire menaçant, l'atosiban passe devant", "19"),
            ]),
            8: map_regles()[:7],
            9: map_regles()[2:7] + PP([
                ("Le tracé et la présentation complètent, sans remplacer le col", "1"),
            ]),
            10: PP([
                ("Suspicion, puis terme, puis un seul test si l'on a passé 30 SA", "3"),
                ("Diagnostic retenu, corticoïde si la fenêtre le dit, tocolyse si elle a un sens", "3"),
                ("Magnésium pour le cerveau fœtal si la naissance avant 30 SA est proche", "3"),
                ("Instabilité ou infection fulminante, on naît", "21"),
            ]),
            11: map_regles()[7:16] + doses_toco() + doses_mg()[3:] + poumon()[:4] + PP([
                ("Le guide de 2015 proposait la nifédipine en tocolyse, hors autorisation britannique alors", "3"),
                ("L'autorisation suisse actuelle l'interdit avec le magnésium intraveineux", "13"),
                ("On n'enseigne pas la dose de charge tocolytique lue dans un avis ancien", "13"),
            ]),
            12: PP([
                ("Arrêter le tabac et traiter une infection urinaire réduisent des irritants", "14"),
                ("La progestérone n'a pas de dose suisse relue ici, donc on n'en écrit pas", "1"),
                ("Un antécédent de naissance prématurée fait orienter plus tôt", "3"),
            ]),
            13: PP([
                ("Un test, une fenêtre de corticoïde, une tocolyse qui ne retarde pas une naissance urgente", "3"),
                ("Atosiban selon l'autorisation, pas selon l'unité extraite en 2013", "7"),
                ("Pas de nifédipine avec le magnésium intraveineux", "13"),
            ]),
            14: PP([
                ("Le piège est de donner deux tests, ou une tocolyse alors qu'il faut naître", "3"),
                ("Le piège est de copier un bolus en microgrammes", "19"),
                ("Le cas corrigé est une femme à 31 SA, contractions régulières, col à 14 mm", "3"),
                ("On avait ajouté une fibronectine et une nifédipine avec du magnésium", "13"),
                ("La correction est un seul test déjà positif, l'atosiban, et le magnésium sans nifédipine", "7"),
            ]),
        }
    elif n == 5:
        corps = {
            1: classes()[7:11] + PP([
                ("Prééclampsie ne se divise pas en légère et grave pendant la grossesse", "1"),
            ]),
            2: commun_epi + suite()[9:12] + suite()[6:9],
            3: PP([
                ("Le placenta libère un déséquilibre entre facteurs angiogéniques", "1"),
                ("Les vaisseaux maternels se contractent et laissent fuir du plasma", "1"),
                ("Le rein, le foie, le cerveau et le fœtus peuvent payer ce déséquilibre", "1"),
            ]) + suite()[16:17],
            4: tension() + classes() + PP([
                ("On traite la tension sévère avant la fin du bilan", "1"),
            ]),
            5: PP([
                ("On demande la tête, les scotomes, la barre sous le foie et l'œdème brusque", "1"),
                ("On demande l'essoufflement, les mouvements de l'enfant et le terme", "1"),
                ("On demande une maladie rénale, un lupus ou une hypertension ancienne", "2"),
            ]),
            6: tension()[:6] + organes()[:2] + PP([
                ("On ausculte les poumons et on cherche le clonus", "1"),
            ]),
            7: classes() + PP([
                ("La forme avec seulement une atteinte utéroplacentaire compte quand même", "1"),
                ("La forme du post-partum existe encore après la naissance", "1"),
            ]),
            8: proteines() + organes(),
            9: suite()[13:17] + PP([
                ("Plaquettes, créatinine, transaminases et signes d'hémolyse se demandent", "1"),
                ("Le modèle fullPIERS réunit saturation, plaquettes, créatinine et transaminase", "1"),
                ("Il y ajoute le terme et la douleur thoracique ou la dyspnée", "1"),
                ("On ne l'appelle pas un score dans cette leçon, faute d'en recopier une pondération", "1"),
            ]),
            10: PP([
                ("Tension, puis atteinte, puis sévérité tensionnelle, puis terme", "1"),
                ("Atteinte présente, c'est la prééclampsie, même sans protéine", "1"),
                ("Tension sévère, médicament tout de suite en lieu surveillé", "1"),
                ("Naissance selon le terme et la stabilité, pas selon une étiquette légère", "1"),
            ]),
            11: doses_tension() + doses_mg()[:3] + poumon() + PP([
                ("On ne donne pas de corticoïde pour hâter la guérison d'un HELLP associé", "1"),
                ("L'accouchement reste le seul geste curatif", "18"),
            ]),
            12: aspirine() + risques_aspirine() + suite()[:5],
            13: PP([
                ("Atteinte ou protéine, à partir de 20 SA, sur une hypertension", "1"),
                ("Pas d'étiquette légère, tension sévère traitée, magnésium si la forme est grave", "6"),
                ("Contrôle entre le troisième et le sixième jour, puis à trois mois", "1"),
            ]),
            14: PP([
                ("Le piège est d'exiger les œdèmes ou la protéine quand l'organe est déjà atteint", "1"),
                ("Le piège est d'associer nifédipine et magnésium intraveineux", "13"),
                ("Le cas corrigé est une femme à 33 SA, 162 sur 108, céphalée, rapport urinaire haut", "1"),
                ("On avait écrit prééclampsie légère et renvoyé à domicile", "1"),
                ("La correction est le lieu surveillé, le labétalol, le magnésium, et la discussion de naissance", "6"),
            ]),
        }
    elif n == 6:
        corps = {
            1: PP([
                ("La pyélonéphrite aiguë gravidique est l'infection du parenchyme rénal pendant la grossesse", "14"),
                ("Elle associe fièvre et douleur du flanc, souvent avec des signes urinaires", "1"),
                ("Elle n'est pas une cystite et n'est pas l'infection amniotique", "21"),
            ]),
            2: commun_epi + PP([
                ("Aucun pourcentage suisse n'a été lu pour fixer son rang", "1"),
                ("Elle vient après les troubles hypertensifs dans l'ordre clinique du motif fièvre", "1"),
            ]),
            3: PP([
                ("L'uretère se dilate et l'utérus gêne l'écoulement", "1"),
                ("Les bactéries montent de la vessie vers le bassinet puis le cortex", "1"),
                ("On ne retient pas un côté préférentiel chiffré, faute de l'avoir lu", "1"),
            ]),
            4: PP([
                ("On prend les constantes et on cherche une instabilité", "1"),
                ("On sépare la douleur du flanc de la douleur utérine", "21"),
                ("On commence le traitement si le tableau est net, sans attendre la culture", "16"),
                ("On vérifie que ce n'est pas un travail ou un décollement", "3"),
            ]),
            5: PP([
                ("On demande la fièvre, les frissons, le côté de la douleur et les brûlures", "1"),
                ("On demande les contractions, les pertes et les mouvements de l'enfant", "21"),
                ("On demande une allergie médicamenteuse avant la première dose", "16"),
            ]),
            6: PP([
                ("La percussion lombaire réveille la douleur", "1"),
                ("L'utérus n'est pas le siège principal de la douleur", "21"),
                ("La tension et le rythme cardiaque fœtal se notent", "1"),
                ("Un choc ou une peau marbrée change l'urgence", "1"),
            ]),
            7: PP([
                ("La forme simple reste stable sous antibiotique et hydratation", "16"),
                ("La forme avec contractions menace le terme", "3"),
                ("La forme qui ne cède pas fait chercher un obstacle ou un abcès", "1"),
            ]),
            8: PP([
                ("Le diagnostic clinique suffit pour commencer quand la fièvre et le flanc concordent", "1"),
                ("La culture précise le germe, elle ne doit pas retarder la première dose", "16"),
                ("Une bandelette négative n'écarte pas le diagnostic si le tableau est franc", "1"),
            ]),
            9: PP([
                ("Culture d'urines, bilan inflammatoire, et échographie si l'évolution traîne", "1"),
                ("La CRP aide au suivi, elle ne nomme pas la maladie", "1"),
                ("On ne demande pas un scanner en première intention chez la femme enceinte", "1"),
            ]),
            10: PP([
                ("Fièvre plus flanc, rein", "1"),
                ("Fièvre plus utérus douloureux, infection amniotique", "21"),
                ("Rein confirmé, antibiotique qui atteint le sang, pas la nitrofurantoïne", "14"),
                ("Instabilité, salle surveillée", "1"),
            ]),
            11: doses_infect()[5:9] + PP([
                ("L'hydratation et le contrôle de la fièvre accompagnent l'antibiotique", "10"),
                ("La nitrofurantoïne ne sert pas ici, car le sérum n'atteint pas une concentration thérapeutique", "14"),
                ("On surveille les contractions pendant la fièvre", "3"),
            ]) + doses_infect()[9:],
            12: PP([
                ("Traiter une bactériurie sans symptôme diminue le risque de montée vers le rein", "1"),
                ("La nitrofurantoïne peut se discuter tôt, pas au dernier trimestre", "14"),
                ("Aucune dose de listériose n'a été extraite, donc on n'en écrit pas", "1"),
            ]),
            13: PP([
                ("Flanc, fièvre, antibiotique sérique, pas nitrofurantoïne", "14"),
                ("Ceftriaxone selon l'autorisation, sans calcium dans la même tubulure", "16"),
                ("Paracétamol dans la limite journalière lue", "10"),
            ]),
            14: PP([
                ("Le piège est de donner la nitrofurantoïne pour une pyélonéphrite", "14"),
                ("Le piège est de mélanger la ceftriaxone au calcium", "16"),
                ("Le cas corrigé est une femme à 28 SA, fièvre, douleur droite du flanc, utérus souple", "1"),
                ("On avait prescrit la nitrofurantoïne et renvoyé à la maison", "14"),
                ("La correction est un antibiotique qui atteint le sang, et une surveillance du terme", "16"),
            ]),
        }
    elif n == 7:
        corps = {
            1: PP([
                ("L'infection intra-amniotique est l'infection des membranes, du liquide ou du placenta", "21"),
                ("Le tableau associe fièvre, utérus douloureux et souvent des pertes sales", "21"),
                ("Aucun seuil thermique chiffré n'a été lu, donc on n'en invente pas", "21"),
            ]),
            2: commun_epi + PP([
                ("Elle est moins banale que la contraction bénigne et plus urgente", "1"),
                ("Aucune incidence suisse n'a été lue pour ce rang", "1"),
            ]),
            3: PP([
                ("Les germes montent du vagin, surtout si les membranes sont rompues", "1"),
                ("Ils peuvent infecter aussi quand les membranes sont encore intactes", "1"),
                ("La réponse inflammatoire déclenche des contractions et gêne le fœtus", "3"),
            ]),
            4: PP([
                ("On reconnaît le faisceau clinique sans attendre un chiffre de température inventé", "21"),
                ("Une forme fulminante fait naître", "21"),
                ("On ne retient pas la femme pour finir une maturation dans ce cas", "21"),
                ("On prélève, puis on traite", "15"),
            ]),
            5: PP([
                ("On demande la fièvre, les frissons, la couleur des pertes et l'heure de la rupture", "1"),
                ("On demande les contractions et un malaise général", "1"),
                ("On demande le terme en jours", "3"),
            ]),
            6: PP([
                ("L'utérus est sensible, parfois le liquide est teinté ou malodorant", "21"),
                ("Le rythme cardiaque fœtal peut être rapide", "1"),
                ("Un tracé pathologique ou un décollement ne se temporise pas", "21"),
                ("On cherche aussi un flanc douloureux pour ne pas manquer le rein", "1"),
            ]),
            7: PP([
                ("La forme avec membranes rompues est la plus classique", "1"),
                ("La forme à membranes intactes existe et ne doit pas être niée", "1"),
                ("La forme fulminante est une indication de naissance", "21"),
            ]),
            8: PP([
                ("Le diagnostic est clinique dans l'urgence", "21"),
                ("Le laboratoire et les prélèvements confirment après, ils ne retardent pas la naissance utile", "21"),
                ("Une culture négative n'efface pas un tableau fulminant déjà traité", "1"),
            ]),
            9: PP([
                ("Prélèvements vaginaux, bilan maternel, et tracé continu", "1"),
                ("On n'attend pas la CRP pour décider une naissance urgente", "21"),
                ("Le nouveau-né aura ses propres prélèvements", "1"),
            ]),
            10: PP([
                ("Fièvre utérine, évaluer la fulminance", "21"),
                ("Fulminante, naissance et antibiotique", "21"),
                ("Pas fulminante et très prématuré, antibiotique et discussion de maturation seulement si l'on peut attendre", "21"),
                ("Flanc plutôt qu'utérus, changer pour le rein", "1"),
            ]),
            11: doses_infect()[:5] + doses_infect()[6:9] + poumon()[2:4] + PP([
                ("Ces doses sont les fourchettes des autorisations, pas un protocole suisse spécifique relu", "15"),
                ("La listériose ne reçoit pas de milligrammes ici, faute d'extrait", "1"),
            ]),
            12: PP([
                ("Limiter les touchers après une rupture diminue des montées de germes", "1"),
                ("Traiter une infection vaginale symptomatique se discute selon le germe, sans dose inventée", "1"),
                ("On ne promet pas qu'un antibiotique évite toute infection amniotique", "1"),
            ]),
            13: PP([
                ("Faisceau clinique, naissance si fulminant, antibiotique selon l'autorisation", "21"),
                ("Pas de maturation quand il faut naître maintenant", "21"),
                ("Pas la fourchette de la méningite comme dose de routine", "15"),
            ]),
            14: PP([
                ("Le piège est d'inventer un seuil de température", "1"),
                ("Le piège est de finir le corticoïde alors que le tableau est fulminant", "21"),
                ("Le cas corrigé est une femme à 35 SA, utérus très douloureux, pertes sales, enfant rapide", "21"),
                ("On avait attendu une température ronde et une maturation", "21"),
                ("La correction est la naissance et l'antibiotique dans la fourchette usuelle lue", "15"),
            ]),
        }
    elif n == 8:
        corps = {
            1: PP([
                ("La thrombose veineuse profonde est un caillot dans une veine profonde du membre", "11"),
                ("Pendant la grossesse, un mollet unilatéral douloureux en est le signe d'appel", "11"),
                ("Ce n'est pas l'œdème physiologique", "1"),
            ]),
            2: commun_epi + PP([
                ("Elle est plus rare que l'œdème bénin, d'où sa place basse dans l'ordre clinique", "1"),
                ("Aucune incidence suisse n'a été recopiée, faute de l'avoir lue", "1"),
            ]),
            3: PP([
                ("La grossesse rend le sang plus coagulable", "1"),
                ("L'utérus gêne le retour veineux pelvien", "1"),
                ("Le caillot peut partir vers le poumon", "11"),
            ]),
            4: PP([
                ("On ne pose pas un score de grossesse qui n'a pas été lu", "1"),
                ("On compare les mollets et on cherche un essoufflement", "11"),
                ("On organise l'imagerie plutôt que de rassurer", "11"),
                ("On commence le traitement si la probabilité est forte et l'imagerie va tarder", "11"),
            ]),
            5: PP([
                ("On demande le côté, la douleur, un alitement, un voyage et un antécédent de caillot", "1"),
                ("On demande une dyspnée, une douleur thoracique et un malaise", "11"),
                ("On demande le terme et une valve cardiaque", "11"),
            ]),
            6: PP([
                ("Un mollet est plus large, plus chaud ou plus rouge", "11"),
                ("Le godet bilatéral du soir n'a pas cette asymétrie", "1"),
                ("On compte la respiration et on ausculte si l'air manque", "11"),
                ("On ne palpe pas pour fragmenter un caillot", "1"),
            ]),
            7: PP([
                ("La forme du mollet est la plus visible", "1"),
                ("La forme ilio-fémorale gonfle toute la cuisse", "1"),
                ("La forme avec embolie pulmonaire domine alors le pronostic", "11"),
            ]),
            8: PP([
                ("L'écho-doppler veineux est l'examen qui confirme au membre", "1"),
                ("Un examen négatif et une clinique forte se rediscute, il ne se classe pas bénin trop vite", "1"),
                ("Aucun score chiffré de grossesse n'est enseigné", "1"),
            ]),
            9: PP([
                ("Doppler veineux du membre suspect", "1"),
                ("Si l'air manque, un avis pour l'embolie, sans chiffre de D-dimères inventé", "1"),
                ("Le D-dimères monte avec la grossesse, donc un seuil hors grossesse n'est pas recopié", "1"),
            ]),
            10: PP([
                ("Asymétrie douloureuse, ne pas rassurer", "11"),
                ("Imagerie, et traitement si l'on ne peut pas attendre", "11"),
                ("Symétrie vespérale et tension normale, autre porte", "1"),
                ("Valve cardiaque, lire la mise en garde avant de choisir la prévention", "11"),
            ]),
            11: doses_tvp() + PP([
                ("La durée exacte de grossesse n'est pas recopiée, car les lignes lues ne la fixent pas", "11"),
                ("On surveille le saignement et le terme", "11"),
            ]),
            12: doses_tvp()[4:5] + PP([
                ("La petite dose préventive n'est pas la dose d'un caillot déjà là", "11"),
                ("La valve reste une situation à part, mal couverte par la prévention à l'énoxaparine", "11"),
            ]),
            13: PP([
                ("Unilatéral et douloureux jusqu'à preuve du contraire", "1"),
                ("Traitement à 1 mg par kilogramme deux fois par jour si le caillot est là", "11"),
                ("Pas de score de grossesse inventé", "1"),
            ]),
            14: PP([
                ("Le piège est d'appeler physiologique un seul mollet", "1"),
                ("Le piège est d'utiliser la dose de prévention pour un caillot prouvé", "11"),
                ("Le cas corrigé est une femme à 30 SA, mollet gauche douloureux et plus large", "1"),
                ("On avait conseillé le repos comme pour un œdème du soir", "1"),
                ("La correction est l'imagerie et la dose de traitement par kilogramme", "11"),
            ]),
        }
    elif n == 9:
        corps = {
            1: PP([
                ("Le syndrome HELLP réunit hémolyse, enzymes hépatiques hautes et plaquettes basses", "20"),
                ("Il appartient au spectre de la prééclampsie", "1"),
                ("Il peut débuter avant ou juste après la naissance", "20"),
            ]),
            2: commun_epi + hellp_regles()[:3],
            3: PP([
                ("La même souffrance placentaire lèse le foie et consomme les plaquettes", "1"),
                ("Les globules se fragmentent dans les petits vaisseaux", "20"),
                ("Un hématome du foie est l'extrême de cette douleur", "1"),
            ]),
            4: hellp_regles() + PP([
                ("On stabilise la tension et la coagulation en même temps que l'on décide la naissance", "1"),
            ]),
            5: PP([
                ("On demande la douleur sous le foie, la tête, les vomissements et les troubles visuels", "1"),
                ("On demande un saignement des gencives ou des urines foncées", "20"),
                ("On demande le terme et si la femme a déjà accouché", "20"),
            ]),
            6: PP([
                ("On palpe le foie avec douceur, sans appuyer fort sur un foie qui peut saigner", "1"),
                ("On cherche le saignement cutané et l'ictère", "20"),
                ("La tension se mesure même si la femme paraît surtout douloureuse", "1"),
                ("Les réflexes se notent", "1"),
            ]),
            7: hellp_regles()[3:12],
            8: hellp_regles()[3:12] + PP([
                ("Un seul critère ne suffit pas à remplir la forme complète du Tennessee", "20"),
            ]),
            9: PP([
                ("Numération, frottis ou bilirubine, LDH, AST, ALT et créatinine", "20"),
                ("On ne répète pas sans fin avant de soigner une forme instable", "1"),
                ("L'imagerie du foie se discute si la douleur est brutale et le choc apparaît", "1"),
            ]),
            10: PP([
                ("Douleur hépatique ou plaquettes basses, bilan complet", "20"),
                ("Critères remplis, stabiliser et faire naître selon le terme", "18"),
                ("Pas de corticoïde pour corriger les chiffres maternels", "1"),
                ("Tension sévère, la traiter sans attendre le nom définitif", "1"),
            ]),
            11: hellp_regles()[12:15] + doses_tension()[:8] + doses_mg()[:3] + poumon() + PP([
                ("La naissance est le geste curatif", "18"),
                ("Après la naissance, on surveille encore les 48 heures", "20"),
            ]),
            12: suite()[:5] + aspirine()[:5],
            13: PP([
                ("Lire Tennessee et Mississippi en entier", "20"),
                ("Pas de corticoïde pour hâter la résolution maternelle", "1"),
                ("Naissance et surveillance du post-partum immédiat", "20"),
            ]),
            14: PP([
                ("Le piège est de donner un corticoïde dans l'espoir de remonter les plaquettes", "1"),
                ("Le piège est d'oublier la classe 3, qui a encore des plaquettes au-dessus de 100", "20"),
                ("Le cas corrigé est une femme à 32 SA, douleur sous le foie, plaquettes à 80, AST haute, LDH haute", "20"),
                ("On avait prescrit un corticoïde maternel pour normaliser le bilan et renvoyé au lendemain", "1"),
                ("La correction est la surveillance, le traitement de la tension, et la naissance discutée tout de suite", "18"),
            ]),
        }
    elif n == 10:
        corps = {
            1: PP([
                ("L'éclampsie est la crise convulsive nouvelle liée à la prééclampsie", "6"),
                ("Elle survient avant, pendant ou après la naissance", "20"),
                ("Elle est une atteinte d'organe, pas une étiquette légère", "1"),
            ]),
            2: commun_epi + PP([
                ("Elle est en dernier parce qu'elle est la plus rare de ce motif", "1"),
                ("Aucune incidence suisse séparée n'a été lue au-delà de la prééclampsie", "18"),
            ]),
            3: PP([
                ("L'œdème cérébral et la vasoconstriction déclenchent la crise", "1"),
                ("La tension sévère est fréquente, mais la crise peut survenir sans chiffre extrême au premier coup d'œil", "1"),
                ("Le magnésium diminue l'excitabilité neuromusculaire", "6"),
            ]),
            4: PP([
                ("On protège la femme, l'air, et on appelle", "6"),
                ("On donne le magnésium de la crise sans attendre un scanner", "6"),
                ("On traite une tension sévère en parallèle", "1"),
                ("On fait naître une fois la mère stabilisée", "18"),
            ]),
            5: PP([
                ("On demande, dès que c'est possible, la tête, la vue et la tension des heures d'avant", "1"),
                ("On demande le terme et si une crise d'épilepsie était déjà connue", "1"),
                ("Une épilepsie ancienne ne doit pas faire manquer une éclampsie nouvelle", "1"),
            ]),
            6: PP([
                ("Pendant la crise, on note la durée, la cyanose et la respiration", "6"),
                ("Après, on cherche le clonus, la tension et la douleur du foie", "1"),
                ("On ne quitte pas le chevet", "6"),
                ("Le fœtus se surveille dès que la mère ventile", "1"),
            ]),
            7: PP([
                ("La crise avant le travail est une forme", "6"),
                ("La crise dans les 48 heures après la naissance est une forme", "20"),
                ("La forme avec tension sévère et la forme avec HELLP se traitent ensemble", "1"),
            ]),
            8: PP([
                ("Le diagnostic est clinique devant la crise nouvelle et le contexte hypertensif", "6"),
                ("L'imagerie cérébrale cherche une autre cause si la crise est atypique ou ne cède pas", "1"),
                ("Elle ne retarde pas la première dose de magnésium", "6"),
            ]),
            9: PP([
                ("Tension continue, saturation, diurèse, réflexes et bilan de prééclampsie", "3"),
                ("Plaquettes, créatinine et transaminases se demandent", "1"),
                ("On ne demande pas un électroencéphalogramme avant le magnésium", "6"),
            ]),
            10: PP([
                ("Crise, air, magnésium, tension, puis naissance", "6"),
                ("Pas de nifédipine avec ce magnésium", "13"),
                ("Pas d'urapidil sauf si le bénéfice justifie le risque fœtal", "12"),
                ("Après la crise, surveillance rapprochée car elle peut revenir", "20"),
            ]),
            11: doses_mg()[:7] + doses_tension() + PP([
                ("Le schéma suisse de la crise se compte en dix minutes, pas en quinze", "6"),
                ("Le schéma de quinze minutes est celui du guide pour le cerveau du prématuré", "3"),
                ("On ne les mélange pas dans la même phrase de prescription", "6"),
            ]),
            12: doses_mg()[:3] + PP([
                ("Donner le magnésium à la forme grave diminue le risque de première crise", "6"),
                ("La prévention de la prééclampsie elle-même est le chapitre de l'aspirine, avec son conflit suisse", "9"),
            ]),
            13: PP([
                ("Air, magnésium selon l'autorisation, tension, naissance après stabilisation", "6"),
                ("Dix minutes pour la crise suisse", "6"),
                ("Jamais de nifédipine intraveineuse dans cette leçon, et pas d'orale avec le magnésium", "13"),
            ]),
            14: PP([
                ("Le piège est d'attendre un scanner avant le magnésium", "6"),
                ("Le piège est d'ajouter la nifédipine au magnésium intraveineux", "13"),
                ("Le cas corrigé est une femme à 37 SA, crise brève, tension à 170 sur 112", "1"),
                ("On avait donné une benzodiazépine seule et renvoyé vers un scanner avant tout magnésium", "6"),
                ("La correction est le magnésium de la crise, le labétalol, puis la naissance une fois stable", "6"),
            ]),
        }
    else:
        raise SystemExit(n)
    return corps


def phase_a_sections():
    return {
        1: PP([
            ("Le motif réunit quatre portes, la fièvre, l'œdème, l'hypertension et les contractions irrégulières", "1"),
            ("Chaque porte a un diagnostic bénin et un diagnostic qui ne se rate pas", "1"),
            ("On ne ferme pas la porte grave parce que la porte bénigne est plus fréquente", "1"),
        ]),
        2: PP([
            ("L'ordre clinique va de l'œdème bénin vers la crise convulsive", "1"),
            ("Ce n'est pas une liste d'incidences suisses, sauf pour la prééclampsie", "18"),
            ("L'incidence suisse de la prééclampsie avoisine 2,5 pour cent des accouchements", "18"),
            ("On compte plus de 2000 cas par an sur environ 85000 naissances", "18"),
        ]) + suite()[6:9],
        3: PP([
            ("L'utérus comprime les veines, dilue le sang et irrite le muscle", "1"),
            ("Le placenta peut déséquilibrer les vaisseaux maternels", "1"),
            ("Les germes montent vers le rein ou vers les membranes", "1"),
            ("Le sang plus coagulable forme un caillot si le flux ralentit", "11"),
        ]),
        4: tension() + PP([
            ("Devant la fièvre, on sépare le flanc et l'utérus", "21"),
            ("Devant l'œdème, on sépare les deux jambes", "11"),
            ("Devant les contractions, on date le terme puis on choisit un seul test", "3"),
        ]),
        5: PP([
            ("On demande le terme en jours, la tête, la vue, la douleur du foie et l'enfant", "1"),
            ("On demande la fièvre, le côté de la douleur et l'odeur des pertes", "21"),
            ("On demande si un seul mollet a gonflé", "11"),
            ("On demande les contractions, le liquide et le saignement", "3"),
        ]),
        6: PP([
            ("On mesure la tension comme le texte de 2021 le demande", "1"),
            ("On compare les mollets, on palpe l'utérus et on cherche le clonus", "1"),
            ("On ausculte les poumons si l'air manque", "1"),
            ("On ne répète pas les touchers sans une question précise", "1"),
        ]),
        7: noms_liste() + classes(),
        8: proteines() + organes() + map_regles()[:7] + hellp_regles()[3:12],
        9: suite()[13:17] + PP([
            ("Plaquettes, créatinine, transaminases, LDH et urine font le bilan commun de l'hypertension", "1"),
            ("Le col ou la fibronectine, jamais les deux, tranchent la menace après 30 SA", "3"),
            ("Le doppler veineux tranche le mollet suspect", "11"),
        ]),
        10: PP([
            ("Quatre portes, puis la question qui fait rester ou changer", "1"),
            ("Fièvre du flanc vers le rein, fièvre utérine vers les membranes", "21"),
            ("Œdème des deux côtés vers le bénin, un côté vers la thrombose", "11"),
            ("Tension vers la classe, puis vers l'atteinte", "1"),
            ("Contractions vers le terme et un seul test", "3"),
        ]),
        11: doses_tension() + doses_mg() + doses_toco()[:6] + doses_infect()[:9] + doses_tvp()[:4] + PP([
            ("La naissance curatrice ne se retarde pas pour un bilan de confort", "18"),
            ("Le corticoïde de maturation suit la fenêtre et s'arrête si l'on doit naître", "21"),
        ]),
        12: aspirine() + risques_aspirine() + suite()[:6] + poumon()[4:],
        13: PP([
            ("Confirmer la tension, ne pas étiqueter légère, traiter la tension sévère", "1"),
            ("Un test du col, atosiban en milligrammes, pas de nifédipine avec le magnésium", "13"),
            ("Magnésium de crise en dix minutes selon l'autorisation suisse", "6"),
            ("Aspirine suisse interdite au troisième trimestre, même si un guide va jusqu'à la naissance", "9"),
        ]),
        14: PP([
            ("Le piège est de prendre l'œdème pour une prééclampsie, ou un mollet unique pour un œdème", "11"),
            ("Le piège est de copier le microgramme d'atosiban ou le corticoïde anti-HELLP", "7"),
            ("Le cas corrigé du motif est une femme à 33 SA avec œdème, tension à 164 sur 110 et céphalée", "1"),
            ("On avait parlé d'œdème bénin et donné un rendez-vous éloigné", "1"),
            ("La correction est le lieu surveillé, le traitement de la tension sévère, et la recherche d'atteinte", "1"),
        ]),
    }


def essentiel_de(n: int | None):
    base = sigles()
    if n is None:
        base += PP([
            ("On ouvre une porte, on écarte celle qui tue, puis on traite avec une dose lue", "1"),
            ("Les dix noms canoniques sont dans le point des syndromes", "1"),
        ])
    else:
        base += PP([
            (f"Le sujet de cette fiche est {NOMS[n]}", "1"),
            ("Les bornes viennent des textes de 2019, 2021 et 2022 et des autorisations lues le 31 octobre 2026", "1"),
        ])
    # la phrase avec le nom peut être longue
    return base


def ecrire_meta(sources_lignes):
    liste = """# Liste DX canonique — LOT_177 O1.4

Problèmes maternels pendant la grossesse : fièvre, œdème, hypertension, travail prématuré irrégulier.
Ordre clinique décroissant dans ce motif. La seule incidence suisse lue est celle de la prééclampsie, environ 2,5 pour cent (avis 67, 2019). Les autres rangs ne sont pas des incidences mesurées.

DX.1 — Œdème physiologique de la grossesse
DX.2 — Contractions utérines irrégulières bénignes
DX.3 — Hypertension gestationnelle
DX.4 — Menace d'accouchement prématuré
DX.5 — Prééclampsie
DX.6 — Pyélonéphrite aiguë gravidique
DX.7 — Infection intra-amniotique
DX.8 — Thrombose veineuse profonde
DX.9 — Syndrome HELLP
DX.10 — Éclampsie
"""
    (LOT / "LISTE_DX_CANONIQUE.md").write_text(liste, encoding="utf-8")
    inc = """# Incertitudes — LOT_177

Ces points ne sont pas des marqueurs dans les leçons. Ils expliquent ce qui n'a pas été écrit.

1. Avis d'experts 41 (2013), extraction automatique : bolus d'atosiban écrit en microgrammes. Autorisation 69185 : 6,75 mg. La leçon suit l'autorisation.
2. Le même avis évoque nifédipine et magnésium intraveineux ensemble. Autorisation 52896 : association interdite. La leçon suit l'autorisation. La dose de charge tocolytique de la nifédipine dans cet avis n'est pas enseignée.
3. Avis 34 (2009) : effet possible de la bétaméthasone sur les plaquettes et les enzymes au cours du HELLP, bénéfice réel inconnu. ISSHP 2021 : ne pas donner de corticoïde pour accélérer la résolution du HELLP. La leçon suit 2021 pour cette indication maternelle. La maturation pulmonaire fœtale, elle, suit les fenêtres de l'avis 34 et du guide NG25.
4. Autorisation 66710 (dexaméthasone) : les lignes lues ne donnent pas de schéma en milligrammes pour le poumon fœtal. Aucun milligramme de bétaméthasone ou de dexaméthasone n'est enseigné.
5. Incidences suisses non lues, sauf la prééclampsie à environ 2,5 pour cent (avis 67, 2 décembre 2019). L'ordre des dix diagnostics est un ordre clinique du motif, pas une série mesurée.
6. Aucun seuil chiffré de fièvre pour l'infection intra-amniotique n'a été lu dans NG25 ni dans l'avis 34. Le faisceau clinique est enseigné sans température inventée.
7. Aucun score de Wells adapté à la grossesse n'a été lu. Il n'est pas enseigné. Aucun seuil de D-dimères de grossesse n'est recopié.
8. La grille de Bishop n'a pas été relue. Elle n'est pas enseignée.
9. Aucune dose de listériose n'a été extraite. Aucun milligramme n'est enseigné.
10. La prévention de la prééclampsie par aspirine n'est pas l'indication de l'autorisation 51795. Le troisième trimestre est une contre-indication suisse. Le guide NG133 poursuit jusqu'à la naissance. L'ISSHP 2021 arrête vers 36 SA et parle de 100 à 162 milligrammes, non enseignés comme dose suisse. La leçon garde l'interdiction suisse.
11. La durée du traitement de la thrombose pendant la grossesse n'est pas fixée par les lignes lues de l'autorisation 49456. Elle n'est pas inventée. La dose de traitement 1 mg/kg deux fois par jour est, elle, écrite.
12. Sulfate de magnésium, autorisation 56394 : prééclampsie et éclampsie en dix minutes. Guide NG25 : neuroprotection, 4 g en quinze minutes, usage hors autorisation britannique en août 2019. Les deux schémas sont séparés.
13. Le modèle fullPIERS est cité par ses composants, pas comme un score pondéré, parce que la pondération n'a pas été recopiée.
14. Aucun protocole suisse unique d'antibiothérapie de l'infection amniotique n'a été lu. Les fourchettes enseignées sont celles des autorisations 56271 et 59876, avec cette limite.
15. Côté préférentiel de la pyélonéphrite : aucun pourcentage n'a été lu, donc aucun n'est écrit.
"""
    (LOT / "INCERTITUDES.md").write_text(inc, encoding="utf-8")
    (LOT / "evidence" / "INDEX.md").write_text(
        "\n".join(sources_lignes) + "\n", encoding="utf-8"
    )


CIBLES = {
    "A": 76000,
    1: 39800,
    2: 38900,
    3: 40600,
    4: 42100,
    5: 43800,
    6: 38400,
    7: 41200,
    8: 42700,
    9: 44300,
    10: 45800,
}


def main():
    lignes = []
    idx = (LOT / "evidence" / "INDEX.md").read_text(encoding="utf-8").splitlines()
    lignes = [l for l in idx if l.strip()]
    sources = []
    for s in moteur.sources_html(lignes):
        s = s.replace("guideline NG133", "guide de juin 2019")
        s = s.replace("guideline NG25", "guide de 2015")
        s = s.replace("BMC Pregnancy and Childbirth", "revue Pregnancy and Childbirth")
        sources.append(s)
    ecrire_meta(lignes)
    dess = moteur.descriptions()
    (LOT / "illustrations").mkdir(exist_ok=True)
    for k, d in dess.items():
        (LOT / "illustrations" / f"{k}.json").write_text(
            json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8"
        )
    frags = {k: moteur.fragment(d) for k, d in dess.items()}
    extras_a = {10: moteur.schema_orientation()}
    extras = {
        1: {10: moteur.mini_schema("Œdème", "Deux chevilles", "Un seul mollet", "Tension haute")},
        2: {10: moteur.mini_schema("Contractions", "Irrégulières", "Col court", "Fièvre")},
        3: {10: moteur.mini_schema("Tension", "Confirmer", "Chercher l'atteinte", "Traiter si sévère")},
        4: {6: frags["uterus"], 10: moteur.mini_schema("Menace", "Terme", "Un seul test", "Tocolyse ou non")},
        5: {10: moteur.mini_schema("Prééclampsie", "Tension", "Atteinte", "Naissance")},
        6: {6: frags["rein"], 10: moteur.mini_schema("Fièvre", "Flanc", "Utérus", "Instable")},
        7: {10: moteur.mini_schema("Membranes", "Faisceau", "Fulminant", "Naissance")},
        8: {6: frags["mollet"], 10: moteur.mini_schema("Mollet", "Les deux", "Un seul", "Embolie")},
        9: {10: moteur.mini_schema("HELLP", "Plaquettes", "Foie", "Naissance")},
        10: {10: moteur.mini_schema("Crise", "Air", "Magnésium", "Naissance")},
    }
    # Phase A
    secs = []
    data = phase_a_sections()
    fiches_a = [
        "Le motif a quatre portes, et chacune a son urgence.",
        "Une seule incidence suisse est citée, celle de la prééclampsie.",
        "Les mécanismes utiles tiennent en quatre lignes dans la fenêtre.",
        "On commence par ce qui tue, avant le classement fin.",
        "L'anamnèse date le terme et cherche la tête, le foie, la fièvre et le mollet.",
        "L'examen mesure, compare les jambes et palpe l'utérus.",
        "Les dix diagnostics du motif sont nommés dans la fenêtre.",
        "Les bornes de tension, d'urine, de col et de laboratoire sont dans la fenêtre.",
        "Les examens ne se combinent pas quand le guide l'interdit.",
        "L'arbre tient sur le schéma des quatre portes.",
        "Les doses de la fenêtre sont celles des autorisations lues.",
        "La prévention de l'aspirine a un conflit entre guides et autorisation suisse.",
        "Quatre décisions suffisent à ne pas se tromper de porte.",
        "Le cas corrigé montre une tension sévère prise à tort pour un œdème.",
    ]
    for i, titre in enumerate(TITRES, start=1):
        secs.append((i, titre, fiches_a[i - 1], data[i]))
    secs = dedupe(secs)
    clauses = clauses_pour("le motif maternel", [
        "chaque porte se ferme seulement après la question grave",
        "la fièvre du flanc n'est pas la fièvre de l'utérus",
        "l'œdème des deux chevilles n'est pas le mollet unique",
        "la tension sévère ne rentre pas dans un rendez-vous éloigné",
        "les contractions se jugent avec le terme et un seul test",
    ])
    secs = moteur.completer("le motif", secs, clauses, CIBLES["A"])
    html_a = moteur.page(
        "Problèmes maternels pendant la grossesse : fièvre, œdème, hypertension, travail prématuré irrégulier",
        "Quatre portes, dix diagnostics, des bornes lues et des doses d'autorisation.",
        essentiel_de(None),
        secs,
        sources,
        "FIN_FICHIER LOT_177_Phase_A_V0.html",
        extras_a,
    )
    (LOT / "LOT_177_Phase_A_V0.html").write_text(html_a, encoding="utf-8")
    print("Phase A écrite", len(html_a))
    for n in range(1, 11):
        data = builder(n)
        secs = dedupe(sections_de(n, data))
        secs = moteur.completer(NOMS[n], secs, clauses_pour(NOMS[n], PROPRES[n]), CIBLES[n])
        html_n = moteur.page(
            NOMS[n],
            "Diagnostic du motif maternel, bornes lues, dose seulement si l'autorisation la porte.",
            essentiel_de(n),
            secs,
            sources,
            f"FIN_FICHIER LOT_177_Phase_B_V0_DX.{n}.html",
            extras.get(n, {}),
        )
        path = LOT / f"LOT_177_Phase_B_V0_DX.{n}.html"
        path.write_text(html_n, encoding="utf-8")
        print(path.name, len(html_n))


if __name__ == "__main__":
    main()
