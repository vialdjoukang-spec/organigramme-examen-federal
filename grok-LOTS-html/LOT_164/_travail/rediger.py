#!/usr/bin/env python3
"""Rédige LOT_164. Les phrases viennent des extraits du 31 octobre 2026."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from moteur import P, page, table, abbr_texte
from plus import complements
from encore import encore

OUT = Path(__file__).resolve().parents[1]
S = lambda *n: n

SOURCES = """
<li>Organisation mondiale de la Santé, seuils d'hémoglobine, 2024.</li>
<li>Organisation mondiale de la Santé, ferritine, 2020.</li>
<li>Snook et al., Gut, 2021, société britannique de gastroentérologie.</li>
<li>NICE, transfusion, ligne directrice de 2015.</li>
<li>Devalia et al., British Journal of Haematology, 2014.</li>
<li>Scully et al., British Journal of Haematology, 2023.</li>
<li>Hill et al., British Journal of Haematology, 2016.</li>
<li>Best Practice, évaluation de l'anémie, preuves relues en 2026.</li>
<li>Doig, Journal of Applied Laboratory Medicine, 2024.</li>
<li>McDonagh et Macdougall, European Journal of Heart Failure, 2018, seuils de 2016.</li>
<li>Dignass et al., Journal of Crohn's and Colitis, 2015.</li>
<li>Ferinject, numéro 57851.</li>
<li>Maltofer, numéro 30124.</li>
<li>Venofer, numéro 15398.</li>
<li>Tardyferon, numéro 37448.</li>
<li>Ferro-Gradumet, numéro 31644.</li>
<li>Ferrum Hausmann, numéro 35102.</li>
<li>Vitarubine, numéro 21672.</li>
<li>Vitarubine Dépôt, numéro 33584.</li>
<li>Vitarubine Oral, numéro 68216.</li>
<li>Prednisone Streuli, numéro 29349.</li>
<li>Eprex, numéro 49078.</li>
<li>Aranesp, numéro 55725.</li>
<li>Cablivi, numéro 66792.</li>
<li>Hydroxycarbamide Devatis, numéro 67491.</li>
<li>Acidum folicum Hänseler, numéro 55746.</li>
<li>AndreaFol, numéro 54718.</li>
<li>Maltofer Fol, numéro 46538.</li>
<li>Acidum folicum Streuli, numéro 36752.</li>
<li>Catalogue PROFILES, F2.16, 2026.</li>
<li>Qureshi et al., British Journal of Haematology, 2018.</li>
"""

GLOSS = P(
    "Sigles de la leçon : OMS, VGM, NFS, LDH, MAT, PTT, SHU, CRP, EPO, AIPS, "
    "BSG, BSH, NICE, ECCO, ESC, DAT, MMA, ADN, ECG, IRM, VIH, ABO, UI, G6PD, "
    "CIVD, GBD, PROFILES, ADAMTS13.",
    S(8),
)

QUI = [
    ("Enfant de 6 à 23 mois", "105", "95 à 104", "70 à 94", "inférieure à 70"),
    ("Enfant de 24 à 59 mois", "110", "100 à 109", "70 à 99", "inférieure à 70"),
    ("Enfant de 5 à 11 ans", "115", "110 à 114", "80 à 109", "inférieure à 80"),
    ("Fille de 12 à 14 ans", "120", "110 à 119", "80 à 109", "inférieure à 80"),
    ("Garçon de 12 à 14 ans", "120", "110 à 119", "80 à 109", "inférieure à 80"),
    ("Femme non enceinte de 15 à 65 ans", "120", "110 à 119", "80 à 109", "inférieure à 80"),
    ("Homme de 15 à 65 ans", "130", "110 à 129", "80 à 109", "inférieure à 80"),
    ("Grossesse, premier trimestre", "110", "100 à 109", "70 à 99", "inférieure à 70"),
    ("Grossesse, deuxième trimestre", "105", "95 à 104", "70 à 94", "inférieure à 70"),
    ("Grossesse, troisième trimestre", "110", "100 à 109", "70 à 99", "inférieure à 70"),
]


def oms_table():
    rows = [(a, f"inférieure à {b} g/l", c + " g/l", d + " g/l", e) for a, b, c, d, e in QUI]
    return table(
        "Seuils d'hémoglobine, Organisation mondiale de la Santé, 2024, tableau de définition et de sévérité.",
        ["Personne", "Anémie", "Légère", "Modérée", "Sévère"],
        rows,
    )


def alt_table():
    rows = [
        ("1 à 499", "aucun ajustement"),
        ("500 à 999", "4 grammes par litre"),
        ("1000 à 1499", "8 grammes par litre"),
        ("1500 à 1999", "11 grammes par litre"),
        ("2000 à 2499", "14 grammes par litre"),
        ("2500 à 2999", "18 grammes par litre"),
        ("3000 à 3499", "21 grammes par litre"),
        ("3500 à 3999", "25 grammes par litre"),
        ("4000 à 4499", "29 grammes par litre"),
        ("4500 à 4999", "33 grammes par litre"),
    ]
    return table(
        "Ajustement d'altitude, 2024. On soustrait la valeur de l'hémoglobine mesurée, ou on l'ajoute au seuil.",
        ["Altitude en mètres", "Ajustement"],
        rows,
    )


def tabac_table():
    rows = [
        ("Fumeur, quantité inconnue", "3 grammes par litre"),
        ("Moins de 10 cigarettes par jour", "3 grammes par litre"),
        ("10 à 19 cigarettes par jour", "5 grammes par litre"),
        ("Plus de 20 cigarettes par jour", "6 grammes par litre"),
    ]
    return table(
        "Ajustement du tabac, 2024. Même sens que l'altitude. Les deux ajustements se cumulent.",
        ["Tabac", "Ajustement"],
        rows,
    )


def fer_table():
    return table(
        "Lecture de la ferritine. Les seuils changent avec l'inflammation. Unités en microgrammes par litre.",
        ["Situation", "Carence", "Surcharge à discuter"],
        [
            ("Adulte apparemment sain", "inférieure à 15", "plus de 150 chez la femme qui menstrue, plus de 200 chez l'homme"),
            ("Enfant de moins de 5 ans, sain", "inférieure à 12", "le tableau de 2020 ne fixe pas de surcharge à cet âge"),
            ("Enfant ou adulte avec inflammation", "inférieure à 30 avant 5 ans, inférieure à 70 ensuite", "plus de 500 chez l'adulte non sain"),
            ("Grossesse, premier trimestre", "inférieure à 15", "pas de seuil de surcharge retenu dans le tableau lu"),
            ("Maladie rénale avant dialyse, carence absolue selon le texte de 2021", "ferritine d'au plus 100 et fraction saturée d'au plus 20 pour cent", "autre lecture"),
            ("Hémodialyse, carence absolue selon le texte de 2021", "ferritine d'au plus 200 et fraction saturée d'au plus 20 pour cent", "autre lecture"),
            ("Insuffisance cardiaque, texte de 2016 rapporté en 2018", "ferritine inférieure à 100, ou 100 à 299 si la fraction saturée est sous 20 pour cent", "autre lecture"),
            ("Intestin inflammatoire actif, consensus de 2015", "jusqu'à 100 peut encore être une carence", "autre lecture"),
        ],
    )


def morpho_table():
    return table(
        "Classification morphologique et cinétique, revue relue en 2026.",
        ["Volume", "Borne", "Réticulocytes", "Piste"],
        [
            ("Microcytaire", "inférieur à 80 femtolitres", "souvent bas", "fer, inflammation, thalassémie, sidéroblastique"),
            ("Normocytaire hyperproliférative", "80 à 100 femtolitres", "supérieurs à 2 pour cent", "saignement ou hémolyse"),
            ("Normocytaire hypoproliférative", "80 à 100 femtolitres", "inférieurs à 2 pour cent", "rein, inflammation, moelle"),
            ("Macrocytaire mégaloblastique", "supérieur à 100 femtolitres", "bas ou inappropriés", "cobalamine, folates, défaut de synthèse de l'ADN"),
            ("Macrocytaire non mégaloblastique", "supérieur à 100 femtolitres", "peuvent être élevés si régénération", "alcool, foie, hypothyroïdie, médicaments, réticulocytose"),
        ],
    )


def hemolyse_table():
    return table(
        "Panneau d'hémolyse. Le frottis dit le mécanisme, le test direct à l'antiglobuline dit l'immunité.",
        ["Signe", "Hémolyse", "Ce que cela ne dit pas"],
        [
            ("LDH", "élevée", "aussi un infarctus, une tumeur, une hémolyse in vitro"),
            ("Haptoglobine", "basse ou indétectable", "basse aussi si le foie ne la synthétise plus"),
            ("Bilirubine indirecte", "élevée", "Gilbert peut élever la bilirubine sans anémie"),
            ("Réticulocytes", "élevés si la moelle répond", "bas si la moelle est envahie ou carencée en même temps"),
            ("DAT", "positif dans l'hémolyse immune", "négatif dans la membrane, l'enzyme, la microangiopathie"),
            ("Schizocytes", "microangiopathie ou valve", "quelques fragments ne font pas un PTT sans thrombopénie"),
            ("Sphérocytes", "sphérocytose héréditaire ou anticorps chauds", "le DAT sépare les deux"),
            ("Drépanocytes", "hémoglobine S", "le trait hétérozygote n'anémie presque pas"),
            ("Cellules cibles", "thalassémie, foie, hémoglobine C", "pas un diagnostic à elles seules"),
            ("Cellules mordues", "déficit en G6PD après un oxydant", "le dosage enzymatique peut être normal pendant la crise"),
            ("Polynucléaires hypersegmentés", "mégaloblastose", "chercher cobalamine et folates, puis le MMA"),
        ],
    )


def dx_table():
    return table(
        "Dix diagnostics de la leçon. L'ordre DX suit la fréquence clinique décrite. L'ordre E commence par ce qui tue.",
        ["DX", "Nom", "Volume habituel", "Réticulocytes", "Rang E"],
        [
            ("DX.1", "Carence en fer", "microcytaire", "bas", "E8"),
            ("DX.2", "Anémie inflammatoire", "normocytaire puis microcytaire", "bas", "E9"),
            ("DX.3", "Carence en cobalamine", "macrocytaire", "bas", "E6"),
            ("DX.4", "Carence en folates", "macrocytaire", "bas", "E10"),
            ("DX.5", "Anémie par perte sanguine aiguë", "normocytaire", "élevés après quelques heures", "E2"),
            ("DX.6", "Anémies hémolytiques", "normocytaire", "élevés", "E3"),
            ("DX.7", "Drépanocytose et syndromes thalassémiques", "normo ou microcytaire", "élevés dans la drépanocytose", "E5"),
            ("DX.8", "Microangiopathie thrombotique", "normocytaire", "élevés", "E1"),
            ("DX.9", "Insuffisance médullaire et syndrome myélodysplasique", "variable, souvent macrocytaire", "bas", "E4"),
            ("DX.10", "Anémie de la maladie rénale chronique", "normocytaire", "bas", "E7"),
        ],
    )


def situations():
    cas = [
        ("Femme de 34 ans, règles abondantes, hémoglobine 108 g/l, volume 72 femtolitres, ferritine 8 µg/l.",
         "Le seuil féminin de 2024 est 120 g/l : il y a une anémie, dans la bande modérée 80 à 109 g/l. La ferritine sous 15 µg/l signe des réserves absentes. On traite le fer et on cherche la perte, sans attendre une électrophorèse."),
        ("Homme de 70 ans, hémoglobine 118 g/l, volume 90 femtolitres, CRP élevée, ferritine 180 µg/l, fraction de transferrine saturée à 12 pour cent.",
         "Le seuil masculin est 130 g/l. La ferritine n'est pas basse, mais l'inflammation autorise le seuil de 70 µg/l seulement pour affirmer la carence : 180 µg/l reste au-dessus. La fraction saturée basse oriente vers une restriction en fer. On ne conclut pas à une surcharge."),
        ("Homme insuffisant cardiaque, ferritine 80 µg/l, fraction saturée à 18 pour cent, hémoglobine 112 g/l.",
         "Le texte de 2016, rapporté en 2018, retient une carence si la ferritine est sous 100 µg/l, même sans descendre à 15. Le seuil d'anémie masculin reste 130 g/l. Les deux décisions, carence et anémie, ne se confondent pas."),
        ("Femme au deuxième trimestre, hémoglobine 100 g/l, volume 78 femtolitres, ferritine 12 µg/l.",
         "Le seuil du deuxième trimestre est 105 g/l. 100 g/l est une anémie légère, bande 95 à 104. La ferritine du premier trimestre sous 15 µg/l est le seuil lu pour la grossesse dans le tableau de 2020. Le fer injectable est contre-indiqué au premier trimestre, numéro 57851. Ici le trimestre est le deuxième : la voie se discute selon la tolérance orale."),
        ("Nourrisson de 9 mois, hémoglobine 102 g/l.",
         "De 6 à 23 mois, le seuil de 2024 est 105 g/l. 102 g/l est une anémie légère, bande 95 à 104. L'ancienne borne unique de 110 g/l pour tout enfant de moins de 5 ans ne remplace plus ce découpage."),
        ("Enfant de 3 ans, hémoglobine 102 g/l.",
         "De 24 à 59 mois, le seuil est 110 g/l. 102 g/l est une anémie modérée, bande 70 à 99. Le même chiffre que le nourrisson ne reçoit pas la même étiquette."),
        ("Garçon de 13 ans, hémoglobine 112 g/l.",
         "De 12 à 14 ans, filles et garçons, le seuil est 120 g/l. 112 g/l est une anémie légère. On ne lui applique pas encore le seuil masculin adulte de 130 g/l."),
        ("Homme fumeur à Davos, altitude proche de 1560 mètres, hémoglobine mesurée 128 g/l.",
         "La tranche 1500 à 1999 mètres retire 11 grammes par litre, et le tabac en retire encore selon le nombre de cigarettes. Après ajustement, la valeur peut passer sous 130 g/l. À Genève, sous 500 mètres, l'altitude n'ajuste pas."),
        ("Patient de salle stable, hémoglobine 78 g/l, pas de saignement, pas de syndrome coronarien, pas de transfusion chronique.",
         "Le seuil restrictif de 2015 est 70 g/l, cible après transfusion 70 à 90 g/l. 78 g/l est au-dessus du seuil. On traite la cause. On ne transfuse pas pour arrondir le chiffre."),
        ("Syndrome coronarien aigu, hémoglobine 78 g/l.",
         "Le seuil lu pour le syndrome coronarien aigu est 80 g/l, cible 80 à 100 g/l. 78 g/l est sous ce seuil. L'hémorragie majeure et la transfusion chronique ont leurs propres règles."),
        ("Méléna abondant, pression artérielle basse, hémoglobine 64 g/l.",
         "L'hémorragie majeure sort du seuil restrictif. On remplit, on transfuse, on arrête le saignement. Le chiffre 70 g/l ne sert pas à attendre."),
        ("Femme de 40 ans, hémoglobine 68 g/l, réticulocytes élevés, LDH élevée, haptoglobine indétectable, bilirubine indirecte élevée, sphérocytes, DAT positif.",
         "Hémolyse immune. 68 g/l est une anémie sévère chez la femme, sous 80 g/l, et aussi sous le seuil transfusionnel de 70 g/l si elle est stable. Si elle est instable, on transfuse des culots compatibles sans attendre la fin du bilan d'anticorps. La prednisolone de première ligne est d'un milligramme par kilogramme et par jour selon le texte de 2016. L'information suisse, numéro 29349, écrit une posologie initiale habituellement de 5-60 mg/jour, des doses plus élevées étant autorisées à court terme."),
        ("Femme de 28 ans, hémoglobine 78 g/l, plaquettes 18 giga par litre, schizocytes, créatinine en hausse, DAT négatif, coagulation normale.",
         "Microangiopathie jusqu'à preuve du contraire. L'échange plasmatique vise les 4 heures, au plus tard 8 heures. On ne transfuse pas de plaquettes pour un purpura thrombotique thrombocytopénique suspecté. Le caplacizumab, numéro 66792, est de 10 mg intraveineux avant l'échange, puis 10 mg sous-cutané après chaque échange."),
        ("Homme de 60 ans, valve mécanique, quelques schizocytes, plaquettes normales, hémoglobine stable à 110 g/l.",
         "Des fragments de valve ne sont pas un purpura thrombotique thrombocytopénique. Les plaquettes et la cinétique décident. On ne lance pas un échange pour un frottis isolé."),
        ("Homme de 78 ans, hémoglobine 96 g/l, volume 108 femtolitres, leucocytes et plaquettes bas, réticulocytes bas.",
         "Macrocytose avec pancytopénie et moelle qui ne répond pas : syndrome myélodysplasique ou autre insuffisance médullaire, pas une carence vitaminique tant que le myélogramme n'est pas discuté. On dose quand même cobalamine, folates et MMA, parce qu'une carence se traite et peut coexister."),
        ("Femme de 82 ans, paresthésies, volume 112 femtolitres, cobalamine dans la zone grise du laboratoire, MMA à 0,90 µmol/l.",
         "Un MMA supérieur à 0,75 µmol/l indique presque toujours une carence en cobalamine, hors insuffisance rénale marquée. On ne retarde pas le traitement devant des signes neurologiques. Vitarubine, numéro 21672 : 1000 µg tous les deux jours au début s'il y a des troubles neurologiques."),
        ("Régime pauvre en légumes, volume 104 femtolitres, folate bas, cobalamine normale, MMA normal.",
         "Le folate sérique est le test de première ligne. Le MMA ne s'élève pas dans la carence isolée en folates. Acidum folicum Hänseler, numéro 55746 : un comprimé par jour jusqu'à normalisation, et jusqu'à 15 mg par jour chez l'adulte si la réponse est insuffisante. On ne donne pas de folate seul si la cobalamine n'est pas écartée."),
        ("Jeune homme après primaquine, urines porto, hémoglobine 72 g/l, cellules mordues, DAT négatif.",
         "Crise oxydative. On arrête l'oxydant. Le dosage de G6PD pendant la crise peut être faussement rassurant, parce que les globules les plus déficitaires ont éclaté. On contrôle à distance. On hydrate. La transfusion suit la tolérance et le seuil, pas un réflexe."),
        ("Antécédent familial, sphérocytes, DAT négatif, hémolyse chronique modérée.",
         "Sphérocytose héréditaire. Le DAT négatif l'éloigne des anticorps chauds. L'acide folique accompagne l'hémolyse chronique. La splénectomie n'est pas une décision de ce texte : elle se discute en hématologie, après vaccins."),
        ("Porteur de trait thalassémique, hémoglobine 118 g/l, volume 66 femtolitres, ferritine normale, nombre d'érythrocytes élevé.",
         "Microcytose sans carence. Le fer au long cours surcharge. L'électrophorèse et la numération distinguent le trait d'une carence. Une femme porteuse enceinte a besoin du statut du père."),
        ("Drépanocytose homozygote, hémoglobine de base 78 g/l, crise vaso-occlusive.",
         "La base basse n'est pas une indication à normaliser l'hémoglobine. L'hydroxycarbamide de fond, recommandation de 2018, commence à quinze milligrammes par kilogramme chez l'adulte. La spécialité suisse lue, numéro 67491, est indiquée dans les syndromes myéloprolifératifs et contre-indique la grossesse. On le dit avant de recopier une dose."),
        ("Hémodialyse, hémoglobine 92 g/l, ferritine 90 µg/l, fraction saturée basse.",
         "Carence absolue selon le texte de 2021 si la ferritine est d'au plus 200 µg/l en hémodialyse et la fraction saturée d'au plus 20 pour cent. Eprex, numéro 49078, vise 10 à 12 g/dl et commence à 50 UI/kg trois fois par semaine quand une voie veineuse est déjà là. On corrige le fer avant de monter l'EPO."),
        ("Hémoglobine 140 g/l à l'arrivée, choc hémorragique, prélèvement une heure après le remplissage à 88 g/l.",
         "Le premier chiffre suit encore la concentration d'avant la perte. L'équilibration prend des heures. On ne rassure pas avec 140 g/l devant un choc."),
        ("Ferritine 640 µg/l, CRP normale, saturation de la transferrine élevée, pas d'anémie.",
         "Au-dessus de 500 µg/l chez l'adulte non sain, le texte de 2020 demande une évaluation. La ferritine seule ne nomme pas l'hémochromatose. On ne donne pas de fer."),
    ]
    out = []
    for i, (vignette, lecture) in enumerate(cas, 1):
        out.append(P(f"Situation {i}. {vignette} {lecture}", S(1, 2, 3, 4, 8)))
    return "".join(out)


def wjoin(paras):
    return "".join(paras)


def phase_a():
    f = []
    # 1 définition
    f.append(P(
        "L'anémie est une hémoglobine sous le seuil de l'âge, du sexe et, chez la femme enceinte, du trimestre. "
        "En 2024, ce seuil est 120 g/l chez la femme non enceinte, 130 g/l chez l'homme, 110 g/l au premier et au troisième trimestre, 105 g/l au deuxième, "
        "et il descend jusqu'à 105 g/l entre 6 et 23 mois. La sévérité se lit sur le même tableau, jusqu'à l'anémie sévère sous 70 ou sous 80 g/l selon la ligne.",
        S(1, 30)))
    # 2
    f.append(P(
        "Le fardeau mondial publié en 2023 à partir des données de 2021 est d'environ 24 pour cent de la population, soit 1,9 milliard de personnes. "
        "La cause la plus fréquente dans le monde est la carence en fer. En 2023, 30,7 pour cent des femmes en âge de procréer étaient anémiques selon l'estimation citée en 2025. "
        "Aucun pourcentage suisse des dix causes n'est donné ici.",
        S(8)))
    # 3
    f.append(P(
        "L'érythrocyte circule 110 à 120 jours. Les réticulocytes passent environ trois jours dans la moelle et un jour dans le sang. "
        "L'anémie apparaît quand la production baisse, quand les pertes augmentent, ou quand les deux se combinent. "
        "L'hepcidine de l'inflammation bloque le fer dans les macrophages : la moelle manque de fer alors que les réserves sont présentes.",
        S(8, 9)))
    # 4
    f.append(P(
        "On classe d'abord ce qui tue : microangiopathie, choc hémorragique, hémolyse instable, neutropénie avec fièvre. "
        "Ensuite le volume et les réticulocytes séparent production et perte. Le fer, la cobalamine et les folates viennent avant l'électrophorèse si la microcytose ou la macrocytose les suggère. "
        "Un seuil d'hémoglobine ne choisit pas la cause.",
        S(1, 8, 6)))
    # 5
    f.append(P(
        "On demande les règles, le sang dans les selles, les selles noires, l'aspirine, l'anticoagulant, la grossesse, le régime, l'alcool, "
        "l'origine familiale, une crise après un médicament oxydant, une fièvre, un ictère, des urines foncées, des paresthésies, un angor. "
        "Une douleur thoracique, une syncope, une dyspnée de repos ou un saignement actif sont des drapeaux rouges.",
        S(3, 8)))
    # 6
    f.append(P(
        "On regarde la pâleur conjonctivale, l'ictère, la tachycardie, la tension, la rate, les adénopathies, le sang au toucher rectal si le contexte l'autorise, "
        "et un trouble de la marche quand une carence en cobalamine est possible. "
        "L'examen normal n'écarte pas une anémie à 80 g/l.",
        S(8)))
    # 7
    f.append(P(
        "Le volume sous 80 femtolitres est microcytaire, de 80 à 100 normocytaire, au-dessus de 100 macrocytaire. "
        "Des réticulocytes au-dessus de 2 pour cent orientent vers une perte ou une hémolyse. En dessous, la production est en défaut. "
        "Cette double classification n'est pas raccourcie : chaque case a ses causes.",
        S(8)))
    # 8
    f.append(P(
        "Le diagnostic positif d'anémie est le seuil de 2024 après ajustement d'altitude et de tabac. "
        "Le diagnostic de mécanisme ajoute le volume, les réticulocytes, le fer ou les vitamines, le panneau d'hémolyse et le frottis. "
        "Aucun de ces éléments ne se remplace par un autre.",
        S(1, 9)))
    # 9
    f.append(P(
        "La NFS donne l'hémoglobine, le volume, les leucocytes et les plaquettes. On ajoute les réticulocytes, la ferritine, la CRP, "
        "la fraction de transferrine saturée, puis selon le volume la cobalamine, les folates, le MMA, ou le panneau LDH, haptoglobine, bilirubine, DAT et frottis. "
        "La créatinine cherche le rein.",
        S(2, 5, 9)))
    # 10
    f.append(P(
        "L'arbre commence par l'instabilité. S'il y a des schizocytes et une thrombopénie, on traite comme une microangiopathie. "
        "S'il y a un choc hémorragique, on transfuse sans appliquer le seuil de 70 g/l. Ensuite seulement le volume et les réticulocytes ouvrent les dix diagnostics.",
        S(4, 6, 8)))
    # 11
    f.append(P(
        "Le patient stable sans saignement majeur, sans syndrome coronarien aigu et sans transfusion chronique se discute à partir de 70 g/l, cible 70 à 90 g/l, une unité à la fois. "
        "Le syndrome coronarien aigu se discute à partir de 80 g/l, cible 80 à 100 g/l. "
        "Les doses de fer, de cobalamine, de folate, de prednisone, d'EPO, de caplacizumab et d'hydroxycarbamide sont dans les fenêtres, chacune avec son numéro ou sa recommandation.",
        S(4, 12, 18, 21, 22, 24, 26)))
    # 12
    f.append(P(
        "AndreaFol, numéro 54718, est d'un comprimé par jour en périconceptionnel. La prévention secondaire des malformations du tube neural va jusqu'à 4 à 5 mg par jour dans cette notice, "
        "qui renvoie à une spécialité plus dosée. On cherche une carence en fer avant qu'elle n'abaisse l'hémoglobine. On vaccine avant une splénectomie programmée.",
        S(27, 3)))
    # 13
    f.append(P(
        "Trois gestes : lire le bon seuil OMS, classer par volume et réticulocytes, écarter la microangiopathie et le choc avant le fer oral. "
        "La ferritine sous 15 µg/l est une carence chez l'adulte sain. Avec une inflammation, le seuil monte. "
        "La saturation de la transferrine sous 20 pour cent restreint le fer, elle ne remplace pas la ferritine.",
        S(1, 2, 3)))
    # 14
    f.append(P(
        "Le piège central est de transfuser à 90 g/l un patient stable, ou d'attendre 70 g/l devant un choc. "
        "L'autre piège est le fer injectable sans carence confirmée : c'est une contre-indication du numéro 57851. "
        "Le cas corrigé est dans la fenêtre.",
        S(4, 12)))
    fiches = [
        "Définition", "Épidémiologie", "Physiopathologie", "Démarche diagnostique",
        "Anamnèse et drapeaux rouges", "Examen physique", "Approche syndromique",
        "Diagnostic positif", "Examens complémentaires", "Arbre décisionnel",
        "Prise en charge", "Prévention", "Points clés", "Pièges et cas",
    ]
    wins = []
    wins.append(wjoin([
        GLOSS, oms_table(), alt_table(), tabac_table(),
        P("On lit la ligne entière. Une femme à 108 g/l est anémique, dans la bande modérée. Un homme à 125 g/l est anémique, dans la bande légère 110 à 129 g/l. "
          "Un homme à 108 g/l est dans la bande modérée. Sous 80 g/l, l'anémie de l'adulte non enceinte est sévère. "
          "Chez l'enfant de 6 à 23 mois et au deuxième trimestre, le sévère commence sous 70 g/l, et le seuil de définition est 105 g/l.", S(1)),
        P("Le groupe de 2024 a gardé 130 g/l chez l'homme. Une proposition à 135 g/l n'a pas été retenue. "
          "Entre 6 et 23 mois, le seuil passe à 105 g/l. De 24 à 59 mois, il reste 110 g/l. "
          "Les filles et les garçons de 12 à 14 ans partagent 120 g/l. On n'applique pas le seuil de l'homme adulte à un garçon de 13 ans.", S(1)),
        P("L'altitude et le tabac se cumulent. Sous 500 mètres, cas de la plupart des villes du plateau, l'altitude n'ajuste pas. "
          "De 1500 à 1999 mètres, on retire 11 grammes par litre de la valeur mesurée. "
          "Le fumeur dont on ignore la consommation retire encore 3 grammes par litre. Oublier l'ajustement sous-estime l'anémie en montagne.", S(1)),
        P("La sévérité ne choisit pas le traitement à elle seule. Une anémie légère par carence en fer se traite. "
          "Une anémie dite modérée à 85 g/l chez un coronarien instable se transfuse selon le seuil de 80 g/l, pas selon l'adjectif modéré. "
          "Le mot sévère du tableau OMS et l'urgence clinique sont deux échelles.", S(1, 4)),
        P("PROFILES nomme la situation Anémie, code F2.16. Le cours couvre la définition, le mécanisme, la démarche et la conduite. "
          "Il ne remplace pas le laboratoire local, dont l'intervalle de référence peut différer du seuil de population.", S(30, 8)),
    ]))
    wins.append(wjoin([
        P("Le Global Burden of Disease, publié en 2023 pour l'année 2021, estime 24 pour cent de la population mondiale et 1,9 milliard de personnes. "
          "L'Afrique subsaharienne et l'Asie du Sud portent une grande part. Ce chiffre n'est pas un taux suisse.", S(8)),
        P("L'estimation citée pour 2023 est de 30,7 pour cent de femmes en âge de procréer anémiques dans le monde. "
          "En 2019, environ 40 pour cent des enfants de 6 à 59 mois étaient anémiques selon l'analyse citée par la même page. "
          "La carence alimentaire en fer est la cause la plus fréquente au niveau mondial.", S(8)),
        P("Le texte de gastroentérologie de 2021 rappelle que plus de 20 pour cent des personnes de plus de 85 ans sont anémiques, "
          "et plus de la moitié des résidents en institution dans les séries qu'il cite. Plusieurs causes s'additionnent à cet âge. "
          "La carence en fer y contribue environ une fois sur deux, parfois avec la cobalamine ou les folates.", S(3)),
        P("Chez l'insuffisant cardiaque, une carence en fer au sens du texte de 2021 se voit dans 40 à 70 pour cent des cas. "
          "Ce n'est pas la prévalence de l'anémie. On sépare les deux dénominateurs.", S(3)),
        P("Aucune source lue ne classe les dix diagnostics par une prévalence suisse. L'ordre de la leçon place la carence en fer en tête "
          "parce qu'elle est la cause mondiale la plus fréquente, puis les mécanismes que l'examen fédéral oppose. "
          "L'ordre E, lui, commence par la microangiopathie.", S(8, 6)),
    ]))
    wins.append(wjoin([
        P("La moelle produit sous l'effet de l'EPO, des cytokines et du stroma. Le réticulocyte quitte la moelle après environ trois jours, "
          "perd son réseau ribosomique après environ un jour de circulation, et le globule mature vit 110 à 120 jours. "
          "Une chute en quelques heures est donc une perte ou une dilution, pas un arrêt de production : le stock circulant met des semaines à s'épuiser.", S(8)),
        P("Le fer entre par l'entérocyte, circule lié à la transferrine, et se stocke dans la ferritine. L'hepcidine, induite par l'inflammation, "
          "ferme la ferroportine. Le fer reste dans le macrophage. Le fer sérique baisse, la transferrine baisse, la fraction saturée baisse, "
          "la ferritine reste normale ou haute. C'est l'anémie inflammatoire, distincte de la carence absolue où la ferritine s'effondre.", S(2, 9)),
        P("La synthèse de l'ADN exige la cobalamine et les folates. Le défaut donne des mégaloblastes et des polynucléaires hypersegmentés. "
          "La cobalamine sert aussi à la myéline : le tableau neurologique peut précéder l'anémie. Les folates n'ont pas ce tropisme médullaire. "
          "Le MMA s'élève quand la cobalamine manque, pas quand les folates manquent seuls.", S(5, 9)),
        P("L'hémolyse raccourcit la vie du globule. La moelle répond par les réticulocytes si elle a du fer, des vitamines et de l'EPO. "
          "Intravasculaire : hémoglobinurie, haptoglobine effondrée, LDH très haute. Extravasculaire : rate, bilirubine, sphérocytes. "
          "La microangiopathie fragmente les globules sur des fibrines : schizocytes, et souvent une thrombopénie.", S(6, 9)),
        P("Le rein produit l'EPO. Quand le débit baisse, la moelle reçoit un signal trop faible pour le degré d'anémie. "
          "Les réticulocytes restent bas. Le fer fonctionnel manque souvent en plus, parce que l'hepcidine est haute. "
          "Corriger le fer et discuter l'EPO sont deux gestes, dans cet ordre.", S(3, 22)),
        P("La thalassémie déséquilibre les chaînes de globine. Les précurseurs meurent dans la moelle : hémolyse ineffective, microcytose, "
          "érythrocytes nombreux pour une hémoglobine un peu basse. La drépanocytose polymérise l'hémoglobine S quand l'oxygène baisse : "
          "drépanocytes, vaso-occlusion, hémolyse chronique. Le trait hétérozygote n'est pas la maladie.", S(8, 9, 31)),
    ]))
    wins.append(wjoin([
        P("Minute zéro : conscience, pouls, tension, saignement visible, douleur thoracique, purpura, fièvre avec neutropénie. "
          "Ces signes passent avant le frottis. Une instabilité ouvre la voie veineuse et le groupe sanguin.", S(4, 6)),
        P("Si le patient est stable, la NFS oriente. Volume bas : ferritine et CRP le jour même. Volume haut : cobalamine, folates, et réticulocytes. "
          "Volume normal : réticulocytes. Élevés : panneau d'hémolyse et recherche de saignement. Bas : créatinine, fer, moelle si les lignées chutent.", S(8, 9)),
        P("On n'attend pas le résultat d'ADAMTS13 pour échanger un tableau de microangiopathie. On n'attend pas la ferritine pour transfuser un choc. "
          "On attend la preuve de carence avant un fer injectable : l'anémie sans origine ferriprive confirmée est une contre-indication, numéro 57851.", S(6, 12)),
        P("Le laboratoire local fixe ses bornes de volume. La classification enseignée, relue en 2026, reste : sous 80, de 80 à 100, au-dessus de 100 femtolitres, "
          "et 2 pour cent de réticulocytes comme charnière. Si le compte-rendu donne un intervalle différent, on le dit, on ne mélange pas les deux bornes dans la même phrase.", S(8)),
        situations(),
    ]))
    wins.append(wjoin([
        P("Saignement : mélæna, rectorragie, hématémèse, ménorragie, épistaxis répétée, hématurie, geste opératoire récent, traumatisme. "
          "Médicaments : antiagrégant, anticoagulant, anti-inflammatoire, metformine au long cours pour la cobalamine, méthotrexate pour les folates, "
          "primaquine, dapsone ou rasburicase pour le G6PD.", S(3, 8)),
        P("Terrain : grossesse, accouchement, alimentation sans viande ni légume, alcool, gastrectomie, maladie inflammatoire intestinale, "
          "hémodialyse, valve mécanique, famille drépanocytaire ou thalassémique, antécédent de splénectomie.", S(8, 11)),
        P("Drapeaux : syncope, angor, dyspnée de repos, hypotension, mélæna actif, purpura avec confusion, fièvre et pâleur aiguë, "
          "déficit neurologique aigu, douleur osseuse thoracique d'une drépanocytose. Chacun de ces signes change l'ordre : on traite avant de classer finement.", S(4, 6)),
        P("Le texte de 2014 dit de ne pas attendre un dosage parfait si l'atteinte neurologique est forte, pour éviter qu'elle s'installe. "
          "La pâleur sans signe neurologique reste compatible avec une carence en cobalamine ou en folates : les deux dosages partent ensemble.", S(5)),
        P("On note la date du dernier hémogramme. Une chute de 140 à 90 g/l en deux jours n'est pas une carence en fer, qui met des semaines. "
          "Une baisse lente sur six mois accepte la carence, l'inflammation, le rein ou la moelle.", S(8)),
    ]))
    wins.append(wjoin([
        P("Pâleur des conjonctives et des paumes, tachycardie, souffle fonctionnel, hypotension orthostatique. "
          "Ictère scléral et splénomégalie orientent vers l'hémolyse ou le foie. Une rate absente chez un drépanocytaire adulte est attendue : l'auto-infarctus. "
          "Une rate très grosse chez un enfant drépanocytaire fait craindre la séquestration.", S(8, 31)),
        P("La carence en fer se voit surtout par la pâleur et les signes de saignement. "
          "La cobalamine ajoute l'atteinte neurologique que le texte de 2014 refuse de laisser évoluer. "
          "Les folates partagent la macrocytose sans qu'on leur attribue, dans les extraits lus, le même tropisme neurologique.", S(5, 9)),
        P("Peau : purpura et pétéchies si les plaquettes sont basses, livedo ou ischémie digitale d'une microangiopathie, ictère. "
          "Abdomen : hépatosplénomégalie, cicatrice, masse, méléna au doigtier quand il est indiqué. "
          "Ganglions et fièvre : hémopathie ou infection, pas une carence simple.", S(6, 8)),
        P("Le toucher rectal et le test de grossesse changent la conduite. On les écrit. "
          "Un examen rassurant avec une hémoglobine à 70 g/l n'autorise pas le retour sans surveillance ni groupe sanguin.", S(4)),
    ]))
    wins.append(wjoin([
        morpho_table(), hemolyse_table(),
        P("Microcytose : carence en fer, inflammation évoluée, trait ou maladie thalassémique, anémie sidéroblastique, rarement le plomb. "
          "La ferritine basse tranche pour le fer. La ferritine normale avec beaucoup d'érythrocytes et une électrophorèse anormale tranche pour la thalassémie. "
          "Donner du fer à un trait thalassémique sans carence surcharge.", S(2, 3, 9)),
        P("Normocytose à réticulocytes hauts : saignement récent ou hémolyse. On ajoute LDH, haptoglobine, bilirubine, DAT, frottis. "
          "Normocytose à réticulocytes bas : inflammation, rein, moelle, endocrine, déficit mixte au début. "
          "La créatinine et la ferritine sont le minimum.", S(8, 9)),
        P("Macrocytose mégaloblastique : cobalamine, folates, certains médicaments antimétabolites. "
          "Macrocytose sans mégaloblastose : alcool, foie, hypothyroïdie, réticulocytose qui gonfle le volume moyen, myélodysplasie. "
          "Une réticulocytose hémolytique peut donc élever le volume sans carence vitaminique.", S(5, 8, 9)),
        P("Le frottis complet se lit, pas un seul nom de cellule. Schizocytes et plaquettes basses : MAT. "
          "Sphérocytes et DAT positif : anticorps chauds. Sphérocytes et DAT négatif : membrane. "
          "Drépanocytes : hémoglobine S. Cellules cibles : thalassémie, foie, hémoglobine C. Cellules mordues : oxydant et G6PD. "
          "Polynucléaires à plus de cinq lobes : mégaloblastose.", S(6, 9)),
    ]))
    wins.append(wjoin([
        dx_table(), fer_table(),
        P("Anémie : seuil OMS 2024 ajusté. Carence martiale absolue de l'adulte sain : ferritine sous 15 µg/l, et souvent sous 30 µg/l pour des réserves basses selon le texte de 2021. "
          "Spécificité citée : 0,99 pour le seuil de 15 µg/l, 0,92 pour 45 µg/l. Une ferritine au-dessus de 150 µg/l rend la carence absolue peu probable même avec une inflammation.", S(1, 2, 3)),
        P("Inflammation : ferritine sous 70 µg/l chez l'adulte peut indiquer une carence, seuil conditionnel de 2020. "
          "La fraction de transferrine saturée sous 20 pour cent marque la restriction, en particulier chez le porteur de thalassémie et dans les définitions rénales et cardiaques lues. "
          "On mesure la CRP en même temps. Le mot saturation de la transferrine désigne cette fraction.", S(2, 3, 10)),
        P("Hémolyse : LDH haute, haptoglobine basse, bilirubine indirecte haute, réticulocytes hauts si la moelle peut, frottis, DAT. "
          "Cobalamine : dosage sérique puis MMA si la zone est grise. Un MMA au-dessus de 0,75 µmol/l est presque spécifique, rein exclu. "
          "Folates : folate sérique. Le folate érythrocytaire n'est pas exigé en première ligne.", S(5, 6, 9)),
        P("Une hausse d'au moins 10 g/l en deux semaines sous fer oral, chez un patient anémique, est très évocatrice de carence absolue même si le bilan martial était ambigu. "
          "L'absence de hausse fait revoir l'observance, la poursuite du saignement, l'inflammation et le diagnostic.", S(3)),
    ]))
    wins.append(wjoin([
        P("Tube violet pour la NFS et les réticulocytes, tube pour le fer et la ferritine, CRP, créatinine, bilan hépatique. "
          "Groupe ABO, rhésus et recherche d'agglutinines irrégulières dès qu'une transfusion est possible. "
          "Hémolyse : LDH, haptoglobine, bilirubine totale et conjuguée, DAT.", S(9, 4)),
        P("Frottis demandé explicitement, pas seulement si l'automate alerte. On cherche schizocytes, sphérocytes, drépanocytes, cellules cibles, "
          "cellules mordues, elliptocytes, polychromatophilie, blastes, polynucléaires hypersegmentés. "
          "Le texte de 2024 liste ces formes comme le complément de la numération.", S(9)),
        P("Cobalamine et folates sur le même prélèvement, avant de traiter. MMA si la cobalamine est indéterminée ou si la clinique neurologique contredit un dosage limite. "
          "Le rein élève le MMA : on lit la créatinine à côté. L'homocystéine s'élève dans les deux carences, elle est moins spécifique.", S(5)),
        P("Électrophorèse de l'hémoglobine si la microcytose n'est pas martiale, ou d'emblée si la famille ou l'origine le suggèrent. "
          "Test de falciformation ou chromatographie selon le laboratoire. Dosage de G6PD à distance d'une crise et d'une transfusion. "
          "Myélogramme si pancytopénie, blastes, ou anémie inexpliquée après le bilan de première ligne.", S(8, 9)),
        P("ADAMTS13 avant le premier échange, sans en attendre le rendu. Coproculture si diarrhée sanglante, pour un syndrome hémolytique et urémique. "
          "Troponine si la microangiopathie est suspectée, le cœur est une cible. Test de grossesse avant un médicament tératogène ou un fer dont le trimestre compte.", S(6, 12)),
    ]))
    wins.append(wjoin([
        P("Étape 1. Instable ou saignement majeur : voie veineuse, oxygène si besoin, groupe, transfusion selon le choc, hémostase. Le seuil de 70 g/l ne s'applique pas.", S(4)),
        P("Étape 2. Schizocytes et thrombopénie, ou purpura avec anémie et atteinte d'organe : microangiopathie. Échange dans les 4 à 8 heures. Pas de plaquettes. "
          "Caplacizumab selon l'information suisse si le diagnostic de purpura thrombotique thrombocytopénique est retenu par l'équipe qui échange.", S(6, 24)),
        P("Étape 3. Hémolyse sans schizocytes dominants : DAT. Positif : prednisolone selon 2016 et la fourchette suisse 29349, folate, thromboprophylaxie à discuter, transfusion si le seuil ou l'instabilité l'exigent. "
          "Négatif : frottis, famille, médicaments, G6PD, électrophorèse.", S(7, 21, 9)),
        P("Étape 4. Stable, réticulocytes bas. Volume bas : ferritine. Volume haut : vitamines. Volume normal : rein, inflammation, moelle. "
          "Étape 5. Réticulocytes hauts sans hémolyse biologique : chercher le saignement, y compris rétropéritonéal ou digestif occulte.", S(8, 3)),
        P("Étape 6. Après le mécanisme, la cause de la cause. Carence en fer de l'homme et de la femme ménopausée : voie digestive jusqu'à preuve du contraire, recommandation de 2021. "
          "Femme réglée : utérus et digestif selon les signes. Cobalamine : Biermer, alimentation, chirurgie gastrique, médicaments. Folates : alimentation, alcool, grossesse, méthotrexate.", S(3, 5)),
        P("On ne ferme pas l'arbre sur un seul chiffre. Une ferritine à 40 µg/l avec une CRP haute chez l'adulte reste compatible avec une carence au seuil de 70 µg/l. "
          "Une ferritine à 400 µg/l avec des schizocytes n'écarte pas la microangiopathie.", S(2, 6)),
    ]))
    wins.append(wjoin([
        P("Transfusion restrictive, 2015. Patient qui n'a pas d'hémorragie majeure, pas de syndrome coronarien aigu, pas de transfusions régulières : "
          "seuil 70 g/l, cible 70 à 90 g/l, une seule unité chez l'adulte sans saignement actif, puis on remesure. "
          "Syndrome coronarien aigu : seuil 80 g/l, cible 80 à 100 g/l. Anémie chronique transfusée : seuil individuel.", S(4)),
        P("Fer oral. Maltofer, numéro 30124 : chez l'adolescent dès 12 ans et l'adulte, 100 à 300 mg de fer par jour en anémie ferriprive, 50 à 100 mg s'il n'y a pas d'anémie. "
          "Tardyferon, numéro 37448 : un comprimé retard par jour le matin dans les anémies légères et la carence latente, deux comprimés chez l'adulte si l'anémie est grave. "
          "Ferro-Gradumet, numéro 31644 : un ou deux comprimés par jour avant le petit déjeuner dès 12 ans et plus de 40 kg, avalés sans être croqués. "
          "Ferrum Hausmann, numéro 35102 : une capsule par jour, deux ou trois si la carence est grave, poursuivies un à trois mois après la correction, sans dépasser six mois sans réévaluation.", S(13, 15, 16, 17)),
        P("Fer intraveineux. Ferinject, numéro 57851 : une dose unique ne dépasse pas 1000 mg de fer. En perfusion, la dose unique maximale est de 20 mg de fer par kg sans dépasser 1000 mg. "
          "En injection non diluée, 15 mg de fer par kg sans dépasser 1000 mg. La dose cumulée maximale recommandée est de 1000 mg par semaine. "
          "En hémodialyse, au plus 200 mg par jour. Contre-indiqué si l'anémie n'est pas ferriprive, s'il y a une surcharge, une hypersensibilité, ou au premier trimestre. "
          "On réévalue l'hémoglobine au plus tôt quatre semaines après la dernière dose. Personnel formé à l'anaphylaxie sur place. "
          "Venofer, numéro 15398 : uniquement intraveineux lent, jamais sous-cutané ni intramusculaire. Dose unique maximale 200 mg par injection ou 500 mg par perfusion. La dose cumulée se calcule.", S(12, 14)),
        P("Cobalamine. Vitarubine, numéro 21672, ampoule : sans neurologie, 1000 µg une fois par semaine les premières semaines jusqu'à normalisation, puis entretien à vie si l'absorption est cassée. "
          "Avec troubles neurologiques, 1000 µg tous les deux jours au début. Contre-indiqué en cas d'allergie et dans la maladie de Leber. "
          "Vitarubine Dépôt, numéro 33584 : dans les cas aigus, 1000 µg deux ou trois fois par semaine, puis 1000 µg tous les deux à trois mois dans l'anémie pernicieuse. "
          "Vitarubine Oral, numéro 68216 : en général un à deux comprimés par jour en traitement, un comprimé en prophylaxie, sous surveillance de l'adéquation. "
          "L'enfant n'a pas été étudié pour l'injectable lu.", S(18, 19, 20)),
        P("Folates. Acidum folicum Hänseler, numéro 55746, et Acidum folicum Streuli, numéro 36752 : un comprimé par jour chez l'adulte et l'enfant jusqu'à normalisation. "
          "Chez l'adulte, jusqu'à 15 mg par jour si la réponse est insuffisante. On surveille les anticonvulsivants. "
          "On ne masque pas une cobalamine par du folate seul. Maltofer Fol, numéro 46538 : deux à trois comprimés par jour dans l'anémie ferriprive avec besoin d'acide folique, "
          "puis un comprimé au moins jusqu'à la fin de la grossesse. AndreaFol, numéro 54718 : un comprimé par jour, et 4 à 5 mg par jour cités pour la prévention secondaire du tube neural.", S(26, 29, 28, 27)),
        P("Hémolyse immune. Recommandation de 2016 : prednisolone un milligramme par kilogramme et par jour en première ligne, grade 1B. "
          "Environ 80 pour cent répondent à une dose équivalente de 60 à 100 mg par jour, environ deux tiers en rémission complète. "
          "Pas de réponse à 21 jours : échec. Décroissance quand l'hémoglobine dépasse 100 g/l ou après trois semaines. "
          "Prednisone Streuli, numéro 29349 : la posologie initiale dépend de la maladie et correspond habituellement à 5-60 mg/jour. Des doses plus élevées sont autorisées et peuvent être inévitables à court terme dans les cas aigus. "
          "On ne stoppe pas brutalement après 8 à 10 jours. Folate associé. Transfusion si besoin, culots les plus compatibles, sans attendre une compatibilité parfaite si la vie est en jeu.", S(7, 21)),
        P("Microangiopathie. Échange quotidien, classiquement 1,5 volume plasmatique les trois premiers jours puis un volume, jusqu'à des plaquettes au-dessus de 150 giga par litre. "
          "Plasma seul seulement si l'échange tarde. Cablivi, numéro 66792 : 10 mg intraveineux avant le premier échange, puis 10 mg sous-cutané après chaque échange, "
          "puis quotidien pendant 30 jours après la dernière séance, à prolonger si la maladie n'est pas éteinte. Réservé aux médecins habitués à la microangiopathie. "
          "Adolescents dès 12 ans et 40 kg : même posologie lue.", S(6, 24)),
        P("Drépanocytose, recommandation de 2018, pas l'indication du numéro 67491. Adulte : début à quinze milligrammes par kilogramme et par jour. "
          "Enfant : vingt milligrammes par kilogramme. Montée de cinq milligrammes par kilogramme toutes les 8 à 12 semaines, plafond trente-cinq sous surveillance. "
          "Arrêt si l'hémoglobine passe sous 45 g/l, ou selon les seuils de neutrophiles, plaquettes et réticulocytes du texte. "
          "Le produit suisse lu est indiqué dans la leucémie myéloïde chronique et les syndromes myéloprolifératifs, dose initiale 40 à 50 mg/kg puis entretien 10 à 20 mg/kg, "
          "et la grossesse comme l'allaitement y sont des contre-indications. On ne présente pas cette dose comme celle de la drépanocytose.", S(31, 25)),
        P("Rein. Eprex, numéro 49078 : en insuffisance rénale chronique avec voie veineuse habituelle, 50 UI/kg trois fois par semaine au début. "
          "Cible lue : 10 à 12 g/dl. On ralentit si la hausse dépasse deux grammes par décilitre en un mois. "
          "La dose maximale lue atteint 200 UI/kg trois fois par semaine dans la phrase d'entretien. On corrige le fer d'abord. "
          "Aranesp, numéro 55725, s'instaure par un médecin habitué à l'indication. La fenêtre du diagnostic rénal détaille le schéma lu, sans inventer un microgramme absent de l'extrait.", S(22, 23, 3)),
    ]))
    wins.append(wjoin([
        P("Périconception : AndreaFol un comprimé par jour. Prévention secondaire du tube neural : la notice cite 4 à 5 mg par jour et oriente vers un dosage adapté, numéro 54718. "
          "Grossesse avec carence en fer et besoin de folate : Maltofer Fol, numéro 46538.", S(27, 28)),
        P("On ne commence pas un oxydant chez un déficit en G6PD connu. On prévient la famille d'une sphérocytose. "
          "On dépiste le partenaire d'une femme porteuse d'une hémoglobinopathie avant ou tôt dans la grossesse.", S(8, 9)),
        P("Après correction d'une carence en fer, on poursuit pour les réserves, dans la limite lue de chaque notice, et on traite la cause du saignement. "
          "Une rechute est une perte ou une malabsorption jusqu'à preuve du contraire.", S(3, 17)),
        P("Vaccinations anti-pneumococcique, méningococcique et haemophilus avant une splénectomie programmée, et information sur la fièvre après splénectomie. "
          "Ce geste appartient à l'hématologue qui pose l'indication.", S(8)),
        P("Le patient transfusé de façon chronique a un seuil individuel, un bilan de fer, et une discussion de chélation qui n'est pas dosée dans cette leçon faute d'extrait relu sur une spécialité chélatrice.", S(4)),
    ]))
    wins.append(wjoin([
        P("Seuil OMS complet, pas une seule ligne adulte. Volume en trois classes et réticulocytes en deux. Ferritine 15, 30, 70, 150, 200, 500 selon la case. "
          "Fraction saturée 20 pour cent dans les textes lus. Hémolyse : LDH, haptoglobine, bilirubine, DAT, frottis. "
          "Transfusion 70 et 80 g/l avec leurs exceptions. Échange plasmatique sans attendre ADAMTS13.", S(1, 2, 3, 4, 6, 9)),
        P("Ferinject ne dépasse pas 1000 mg par dose ni par semaine dans la phrase lue, et jamais sans carence confirmée. "
          "Vitarubine 1000 µg selon le schéma neurologique ou non. Folate jusqu'à 15 mg si besoin. Prednisone selon 29349 et le milligramme par kilogramme de 2016. "
          "Cablivi 10 mg. Eprex 50 UI/kg vers 10 à 12 g/dl.", S(12, 18, 26, 21, 7, 24, 22)),
        P("DX.1 carence en fer. DX.2 anémie inflammatoire. DX.3 carence en cobalamine. DX.4 carence en folates. "
          "DX.5 perte sanguine aiguë. DX.6 anémies hémolytiques. DX.7 drépanocytose et syndromes thalassémiques. "
          "DX.8 microangiopathie thrombotique. DX.9 insuffisance médullaire et syndrome myélodysplasique. DX.10 anémie de la maladie rénale chronique.", S(8)),
        P("E1 microangiopathie. E2 choc hémorragique. E3 hémolyse aiguë. E4 moelle avec neutropénie ou blastes. E5 crise drépanocytaire. "
          "E6 cobalamine neurologique. E7 rein symptomatique. E8 fer. E9 inflammation. E10 folates et trait thalassémique stable.", S(6, 4)),
    ]))
    wins.append(wjoin([
        P("Cas. Homme de 67 ans, coronarien, mélæna depuis ce matin, tension 88/50, pouls 120, hémoglobine 64 g/l, volume 78 femtolitres, urée haute. "
          "Question : applique-t-on le seuil de 70 g/l et un seul culot ? Réponse : non. Hémorragie majeure et instabilité. On transfuse, on remplit, on arrête l'antithrombotique selon son antidote propre, on endoscopie. "
          "Le volume déjà bas suggère une carence ancienne en plus du saignement aigu. La ferritine viendra, elle ne retarde pas le culot.", S(4, 3)),
        P("Même homme le lendemain, stable, hémoglobine 84 g/l, saignement tari, pas de douleur thoracique. "
          "Question : un culot pour dépasser 100 g/l ? Réponse : non. Il est au-dessus de 70 g/l et de 80 g/l. On surveille, on enquête sur la lésion, on prépare le fer si la carence se confirme.", S(4)),
        P("Cas. Femme de 24 ans, ictère, hémoglobine 54 g/l, plaquettes 12 giga par litre, créatinine 210 µmol/l, schizocytes, DAT négatif, confusion. "
          "Question : plaquettes puis scanner puis avis demain ? Réponse : échange plasmatique en urgence, pas de plaquettes, ADAMTS13 prélevé sans attendre, caplacizumab discuté par l'équipe spécialisée, 10 mg selon le numéro 66792.", S(6, 24)),
        P("Piège. Ferritine 22 µg/l chez un adulte sain : carence, même au-dessus de 15, les réserves sont basses sous 30 µg/l dans le texte de 2021. "
          "Piège inverse : ferritine 22 µg/l n'autorise pas le fer injectable si l'on n'a pas confirmé le mécanisme et la cause. "
          "Piège du folate : corriger une macrocytose au folate alors que le MMA est haut et la marche s'aggrave.", S(3, 5, 12)),
        P("Piège d'unités. 7 g/dl et 70 g/l sont le même ordre de grandeur, dix fois plus en grammes par litre. On écrit l'unité du laboratoire. "
          "Le tableau OMS est en grammes par litre. La cible d'Eprex lue est en grammes par décilitre : 10 à 12 g/dl. On ne les additionne pas.", S(1, 22)),
        P("Piège de la première heure du choc : hémoglobine encore normale. Piège de la montagne : oublier les 11 grammes par litre entre 1500 et 1999 mètres. "
          "Piège du trait thalassémique traité six mois par fer. Piège du G6PD dosé le jour de la crise.", S(1, 8, 9)),
    ]))
    wins = [a + b + c for a, b, c in zip(wins, complements(), encore())]
    wins[0] += P(
        "Mémo des dix lignes, pour ne pas en oublier une à l'oral. Enfant de 6 à 23 mois : anémie sous 105 g/l, sévère sous 70 g/l. "
        "Enfant de 24 à 59 mois : anémie sous 110 g/l, sévère sous 70 g/l. Enfant de 5 à 11 ans : anémie sous 115 g/l, sévère sous 80 g/l. "
        "Fille ou garçon de 12 à 14 ans : anémie sous 120 g/l, sévère sous 80 g/l. Femme non enceinte : anémie sous 120 g/l, sévère sous 80 g/l. "
        "Homme : anémie sous 130 g/l, sévère sous 80 g/l. Premier trimestre : anémie sous 110 g/l, sévère sous 70 g/l. "
        "Deuxième trimestre : anémie sous 105 g/l, sévère sous 70 g/l. Troisième trimestre : anémie sous 110 g/l, sévère sous 70 g/l. "
        "Les bandes légère et modérée sont dans le tableau de la fenêtre : on ne les remplace pas par ces deux bornes seules, on les lit en plus.",
        S(1))
    points = []
    for titre, fiche, fen in zip(fiches, f, wins):
        points.append((titre, fiche, fen))
    page(
        chemin=OUT / "LOT_164_Phase_A_V0.html",
        titre="Anémie",
        sous="F2.16. Anémie. Texte du 31 octobre 2026.",
        essentiel=P(
            "L'anémie se définit par le seuil d'hémoglobine de l'OMS en 2024, ligne par ligne, puis se classe par le volume et les réticulocytes. "
            "On écarte d'abord la microangiopathie et le choc hémorragique. Le fer, les vitamines, l'hémolyse, la moelle et le rein viennent ensuite, avec les doses suisses lues.",
            S(1, 4, 6)),
        sommaire_note="Les mots soulignés ouvrent une fenêtre. Les sources sont en bas de la leçon.",
        points=points,
        sources_ol=SOURCES,
        fin="FIN_FICHIER LOT_164_Phase_A_V0",
        glossaire="",
    )


if __name__ == "__main__":
    phase_a()
    print("phase A écrite")
