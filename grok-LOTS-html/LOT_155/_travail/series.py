#!/usr/bin/env python3
"""Séries de faits par DX. Lignes sans point. Précisions et examen avec point."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fabrique_dx import assembler

def C(*lignes):
    return list(lignes)

def examen(neuro, volume, muscle, trace):
    return {"neuro": neuro, "volume": volume, "muscle": muscle, "trace": trace}

def P(*precisions):
    assert len(precisions) == 14
    return list(precisions)

SERIES = {}

SERIES[1] = dict(
    nom="Hyponatrémie",
    precisions=P(
        "Le cours rappelle le cadre, cette page fixe le sodium bas.",
        "Jusqu'à 30 % des hospitalisés sont cités en 2014, pas un taux suisse. {2}",
        "C'est d'abord un excès d'eau par rapport au sodium et au potassium. {2}",
        "Symptôme sévère d'abord, mécanisme ensuite.",
        "Vomissement, détresse, somnolence profonde, crise et coma sont sévères. {2}",
        "Le volume clinique est peu fiable. {2}",
        "Urine très diluée n'est pas un SIAD. {2}",
        "Profonde veut dire le chiffre, sévère veut dire le symptôme. {2}",
        "Osmolalité et sodium urinaire orientent quand on a le temps. {2}",
        "Ce trouble est E2 s'il y a des symptômes sévères.",
        "Samsca, numéro 66962, n'est pas le geste de la première heure.",
        "On plafonne la remontée pour éviter la démyélinisation. {2}",
        "150 ml de salé à 3 % en 20 minutes, puis les plafonds de 10 et de 8 mmol/l. {2}",
        "Ne pas appeler sévère une natrémie seulement inférieure à 125 mmol/l. {2}",
    ),
    colonnes=[
        C(
            "Un sodium inférieur à 135 mmol/l définit l'hyponatrémie dans le guide de 2014 {2}",
            "De 130 à 135 mmol/l, le guide parle d'hyponatrémie légère {2}",
            "De 125 à 129 mmol/l, il parle d'hyponatrémie modérée {2}",
            "Sous 125 mmol/l, il parle d'hyponatrémie profonde et non sévère {2}",
            "Le guide d'adulte ne couvre pas l'enfant {2}",
        ),
        C(
            "Jusqu'à 30 % des patients hospitalisés ont une hyponatrémie dans le texte de 2014 {2}",
            "Environ 20 à 30 % des insuffisances cardiaques avancées en ont une {2}",
            "Cette page ne transforme pas ces séries en prévalence suisse",
            "L'absence d'un taux suisse n'est pas un taux nul",
            "Le rang E2 n'est pas une place de fréquence",
        ),
        C(
            "Le cerveau met environ 24 à 48 heures à extruder ses osmoles {2}",
            "Une osmolalité mesurée sous 275 mOsm/kg signe le caractère hypotonique {2}",
            "Une urine à 100 mOsm/kg ou moins fait retenir un excès d'eau {2}",
            "Le guide dit SIAD plutôt que d'opposer SIAD et SIADH pour la conduite {2}",
            "L'insuffisance surrénale secondaire lève le frein du cortisol sur la vasopressine {2}",
        ),
        C(
            "Avec des symptômes sévères, l'œdème cérébral l'emporte sur la démyélinisation {2}",
            "Sans ces symptômes, il y a le temps du diagnostic de cause {2}",
            "Si l'ancienneté est inconnue, tenir le trouble pour chronique sauf argument contraire {2}",
            "Un lien causal est exceptionnel si l'hyponatrémie est peu profonde et les signes graves {2}",
            "Le patient n'est probablement jamais vraiment asymptomatique {2}",
        ),
        C(
            "Les vomissements définissent un symptôme sévère dans le tableau de 2014 {2}",
            "La détresse cardiorespiratoire est dans le même tableau sévère {2}",
            "La somnolence anormale et profonde est sévère {2}",
            "Les crises et le coma, échelle de Glasgow à 8 ou moins, sont sévères {2}",
            "Nausée sans vomissement, confusion et céphalée sont moyennement sévères {2}",
        ),
        C(
            "On date le premier signe neurologique",
            "On ne classe pas le volume sur le seul pli cutané {2}",
            "On cherche les œdèmes sans en faire une preuve de volume efficace",
            "On réévalue la vigilance après le premier bolus",
            "On reste auprès du patient pendant la perfusion",
        ),
        C(
            "Phase postopératoire, polydipsie, exercice et thiazidique récent sont des contextes aigus {2}",
            "Préparation de coloscopie, cyclophosphamide intraveineux et ocytocine y figurent aussi {2}",
            "Desmopressine, terlipressine et vasopressine récemment débutées y figurent {2}",
            "L'insuffisance cardiaque garde le sodium et retient l'eau par la vasopressine {2}",
            "Le foie et le syndrome néphrotique ont leur logique propre dans le guide {2}",
        ),
        C(
            "Le diagnostic hypotonique repose sur l'osmolalité mesurée {2}",
            "Au-dessus de 30 mmol/l de sodium urinaire, on exclut d'autres causes avant le SIAD {2}",
            "À 30 mmol/l ou moins, le guide suggère un volume artériel efficace bas {2}",
            "Les diurétiques brouillent le sodium urinaire {2}",
            "Samsca vise l'hyponatrémie du SIADH de l'adulte, numéro 66962 {10}",
        ),
        C(
            "L'osmolalité sanguine et urinaire vient tôt quand on a le temps {2}",
            "Le sodium se contrôle 20 minutes après le premier bolus {2}",
            "Puis à 6 heures, à 12 heures et chaque jour tant que le traitement bouge {2}",
            "Une composition corporelle très atypique peut faire discuter 2 ml par kilogramme {2}",
            "Le cas ordinaire reste 150 ml fixes de salé à 3 % {2}",
        ),
        C(
            "E2 perfuse 150 ml de salé à 3 % en 20 minutes si les symptômes sont sévères {2}",
            "On répète jusqu'à une hausse d'environ 5 mmol/l {2}",
            "On arrête si les symptômes cèdent après cette hausse {2}",
            "Le plafond est 10 mmol/l le premier jour puis 8 mmol/l par jour jusqu'à 130 mmol/l {2}",
            "Si rien ne change après 10 mmol/l, le symptôme a probablement une autre cause {2}",
        ),
        C(
            "La dose initiale de Samsca est 15 mg de tolvaptan une fois par jour {10}",
            "Elle peut monter jusqu'à 60 mg par jour en une prise {10}",
            "7,5 mg s'envisagent si la natrémie risque de monter trop vite {10}",
            "L'instauration se fait à l'hôpital et le jus de pamplemousse est évité {10}",
            "La grossesse, l'allaitement et l'hypovolémie sont des contre-indications lues {10}",
        ),
        C(
            "Ne pas dépasser les plafonds de correction du guide de 2014 {2}",
            "Limiter l'eau libre si une desmopressine est en cours {17}",
            "Revoir un thiazidique récent devant un sodium qui chute {2}",
            "Ne pas commencer Samsca avant d'avoir lu le mécanisme {10}",
            "Contrôler le sodium à 6 heures et à 12 heures après le geste aigu {2}",
        ),
        C(
            "Aigu veut dire documenté depuis moins de 48 heures {2}",
            "Chronique veut dire au moins 48 heures {2}",
            "Inconnu se traite comme chronique sauf preuve du contraire {2}",
            "Le salé hypertonique des symptômes sévères ne attend pas cette preuve {2}",
            "Le tolvaptan n'est pas ce premier geste",
        ),
        C(
            "Appeler sévère le seul chiffre sous 125 mmol/l contredit le vocabulaire de 2014 {2}",
            "Croire le pli cutané pour choisir la restriction hydrique est fragile {2}",
            "Poursuivre le salé à 3 % au-delà de 130 mmol/l n'est plus la recommandation lue {2}",
            "Donner Samsca dans l'hypovolémie contredit l'information 66962 {10}",
            "Oublier le cortisol avant de conclure à un SIAD est un trou du guide {2}",
        ),
    ],
    examen=examen(
        [
            "On cherche les cinq signes sévères du tableau de 2014. {2}",
            "On ne demande pas un score chiffré de plus.",
            "Une crise fait traiter si le lien avec le sodium est crédible. {2}",
            "On note l'heure de début pour l'ancienneté.",
            "On réévalue après chaque bolus de 150 ml.",
        ],
        [
            "Le volume clinique est en général peu exact. {2}",
            "Les œdèmes n'écartent pas un volume efficace bas dans l'insuffisance cardiaque. {2}",
            "On pèse si un poids antérieur existe.",
            "On ne décide pas la restriction sur le seul aspect.",
            "Le sodium urinaire complète l'œil clinique. {2}",
        ],
        [
            "Le muscle n'est pas le cœur de cette monographie.",
            "Une faiblesse fait chercher aussi le potassium et le phosphate.",
            "On ne décrit pas ici un signe de tétanie non lu.",
            "La crampe isolée ne pose pas le diagnostic.",
            "On garde la force respiratoire à l'esprit si d'autres ions sont bas.",
        ],
        [
            "Le tracé ne définit pas l'hyponatrémie.",
            "Il devient urgent si le potassium est douteux en même temps.",
            "On ne retarde pas le salé hypertonique pour un tracé normal.",
            "Une arythmie fait doser le potassium tout de suite.",
            "Le rythme se surveille pendant la correction rapide.",
        ],
    ),
)

def construire(numeros):
    for n in numeros:
        s = SERIES[n]
        assembler(n, s["nom"], s["colonnes"], s["precisions"], s["examen"])
        print("écrit", n, s["nom"])

if __name__ == "__main__":
    nums = [int(a) for a in sys.argv[1:]] or [1]
    construire(nums)
