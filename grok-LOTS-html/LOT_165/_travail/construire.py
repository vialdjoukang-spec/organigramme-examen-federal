# -*- coding: utf-8 -*-
"""Rédige les 11 leçons du LOT_165. Lancer depuis n'importe où."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from moteur import page, paras, table, ecrire, SOURCES  # noqa: E402
from schema import schema_compatibilite, schema_algorithme, gr_ok, plasma_ok, GROUPES, phrase_donneur, phrase_receveur_ac, phrase_plasma, phrase_receveur_ag  # noqa: E402
from plus import phase_extra, dx_extra  # noqa: E402

S = SOURCES  # index 1..10, on cite le numéro


def P(t, *src):
    return (t, src[0] if len(src) == 1 else src)


def H(items):
    return paras(items)


def phrases_matrice():
    out = []
    out.append(P(
        "On lit deux tableaux, pas un seul. Les globules rouges suivent les antigènes du donneur et les anticorps du receveur. "
        "Le plasma suit les anticorps du donneur et les antigènes du receveur. Inverser les deux tableaux est l'erreur qui envoie "
        "du plasma O à un receveur A.",
        2,
    ))
    for don in GROUPES:
        for rec in GROUPES:
            ok = gr_ok(don, rec)
            mot = "compatible" if ok else "incompatible"
            out.append(P(
                f"Globules rouges du groupe {don} vers un receveur {rec} : {mot}. "
                f"{phrase_donneur(don)}. {phrase_receveur_ac(rec)}. "
                + (
                    "Aucun anticorps ABO du receveur ne reconnaît un antigène A ou B sur ces globules."
                    if ok else
                    "L'anticorps du receveur peut se fixer et lyser ces globules dans le vaisseau si le complément s'active."
                ),
                2,
            ))
    for don in GROUPES:
        for rec in GROUPES:
            ok = plasma_ok(don, rec)
            mot = "compatible" if ok else "incompatible"
            out.append(P(
                f"Plasma du groupe {don} vers un receveur {rec} : {mot}. "
                f"{phrase_plasma(don)}. {phrase_receveur_ag(rec)}. "
                + (
                    "L'anticorps apporté par le plasma ne cible pas un antigène A ou B du receveur."
                    if ok else
                    "L'anticorps du donneur circule alors contre les globules du receveur. C'est une incompatibilité plasmatique, pas une erreur de lecture du tableau des globules."
                ),
                2,
            ))
    out.append(P(
        "Le receveur AB n'a pas d'anticorps anti-A ni anti-B : il peut recevoir des globules O, A, B et AB. "
        "C'est le receveur universel de globules rouges. Le plasma AB n'apporte pas ces anticorps : c'est le donneur universel de plasma. "
        "Les globules O n'ont pas d'antigène A ni B : ils peuvent aller vers les quatre groupes. Le plasma O, lui, ne va que vers O.",
        9,
    ))
    out.append(P(
        "Le concentré d'extrême urgence, quand le groupe n'est pas connu, est un concentré érythrocytaire O RhD négatif. "
        "Le référentiel genevois approuvé le 15 février 2024 le range dans le dépôt d'urgence et exige quand même la carte de compatibilité au lit. "
        "Ce concentré n'autorise pas à transfuser du plasma O.",
        9,
    ))
    return out


def classification_complete():
    """Les trois colonnes du rapport 2024, sans en omettre une ligne."""
    return [
        P("Les réactions transfusionnelles sont des événements indésirables ou inattendus liés à l'administration de produits sanguins labiles. "
          "L'article 63, alinéa 2, de l'ordonnance sur les médicaments impose de les déclarer à Swissmedic. "
          "Le rapport 2024 les classe selon des critères analogues à ceux de l'ISBT. Ce qui n'entre dans aucune catégorie définie va sous Autres.", 1),
        P("Colonne immunologique, liste complète du rapport 2024. Insuffisance pulmonaire aiguë associée à une transfusion, dite TRALI. "
          "Réaction allergique. Réaction fébrile non hémolytique. Allo-immunisations. Réaction hémolytique aiguë et retardée. "
          "Purpura post-transfusionnel. Maladie du greffon contre l'hôte associée à la transfusion. "
          "Le rapport signale que, pour TRALI et pour la réaction fébrile, des mécanismes non immunologiques sont aussi discutés.", 1),
        P("Colonne cardiovasculaire et métabolique, liste complète. Surcharge volémique, dite TACO. Réaction hypotensive. "
          "Dyspnée associée à une transfusion, dite TAD. Hémosidérose. Hyperkaliémie et hypocalcémie. Autres.", 1),
        P("Colonne infectieuse, liste complète. Bactéries. Parasites. Virus. Prions. Champignons. "
          "Aucune de ces trois colonnes ne se résume à l'hémolyse. Ranger une dyspnée dans hémolyse parce que du sang a coulé est une faute de classement.", 1),
        P("Grade 1, non sévère : aucun traitement nécessaire, aucune atteinte irréversible sans traitement. "
          "Grade 2, sévère : atteinte significative ou persistante, y compris l'allo-immunisation, hospitalisation ou prolongation, traitement pour éviter une atteinte irréversible. "
          "Grade 3 : le décès est possible sans le geste qui va avec, intubation, vasopresseur ou soins intensifs. "
          "Grade 4 : décès, et seulement si le lien avec la transfusion est au moins possible. Sinon on grade selon le type de réaction, pas selon le décès.", 1),
        P("Une réaction est au minimum sévère, donc au moins grade 2, si l'un de ces faits est là : allo-immunisation, fièvre supérieure à 39 °C avec une élévation supérieure à 2 °C, "
          "dyspnée ou hypoxie sauf forme très légère, œdème pulmonaire, perte de connaissance, chute de tension sauf forme très légère, "
          "suspicion d'hémolyse, suspicion de contamination bactérienne, ou un geste immédiat pour éviter une atteinte irréversible. "
          "Ce seuil de fièvre du grade n'est pas le seuil qui définit la réaction fébrile non hémolytique.", 1),
        P("Le grade se pose sans regarder l'imputabilité. Une suspicion de surcharge avec une dyspnée significative reste sévère même si l'imputabilité finale est improbable. "
          "L'imputabilité, elle, a cinq cases. 0 non évaluable, informations insuffisantes ou contradictoires. "
          "1 improbable, une autre cause explique plutôt la réaction. 2 possible, la transfusion et une autre cause se valent. "
          "3 probable, une autre cause ne semble pas expliquer. 4 certaine, la réaction est due à la transfusion selon toute probabilité.", 1),
        P("Le rapport 2024 cite deux textes de la société internationale, du réseau d'hémovigilance et de l'association des biothérapies : "
          "les définitions de surveillance des réactions non infectieuses de 2013, et la définition révisée de la surcharge volémique de 2018. "
          "Les critères que l'on coche en Suisse pour déclarer sont ceux de l'aide-mémoire du 9 août 2024, version 1.0, pas un extrait de ces deux textes.", 1),
    ]


def bilan_hemolyse():
    return [
        P("L'aide-mémoire du 9 août 2024 définit la réaction hémolytique par des signes cliniques et de laboratoire d'une destruction accélérée des globules après transfusion, "
          "par incompatibilité immunologique entre donneur et receveur. Le plus souvent, l'anticorps est chez le receveur et vise un antigène du globule transfusé. "
          "L'hémolyse peut être intravasculaire ou extravasculaire. Elle est aiguë ou retardée.", 2),
        P("Aiguë : dans les 24 heures, le plus souvent intravasculaire. Le délai médian de début des symptômes est de 90 minutes après le début de la transfusion. "
          "Retardée : entre 1 et 28 jours, le plus souvent extravasculaire. On ne raccourcit pas cette fenêtre à la première semaine.", 2),
        P("Symptômes écrits dans l'aide-mémoire, liste entière. Fièvre. Frissons et crampes. Malaise, agitation, nausées, vomissements, diarrhée. "
          "Douleurs de la loge rénale, du thorax, de l'abdomen, de la tête, ou au point d'injection. "
          "Chute de tension jusqu'au choc, tachycardie, ou les deux. Dyspnée, pâleur, ictère. Urines foncées. Hémorragie diffuse. "
          "Complications : insuffisance rénale avec oligo-anurie, et coagulation intravasculaire disséminée.", 2),
        P("Résultats de laboratoire de la même liste. Hémoglobinémie. Hémoglobinurie. Haptoglobine basse. Bilirubine haute. "
          "Lactate déshydrogénase et aspartate aminotransférase hautes. Hémoglobine qui chute, ou qui ne monte pas autant que le concentré devait le permettre.", 2),
        P("Analyses, volet 1 : on revérifie les documents pour écarter une confusion. "
          "Volet 2 : immunohématologie sur l'échantillon d'avant et celui d'après, et le groupe du produit. Groupe ABO et RhD, test de Coombs direct, recherche et identification des anticorps, "
          "test de compatibilité avec tous les concentrés transfusés. Si le Coombs direct est positif, on élue. "
          "Volet 3 : hémolyse, hémoglobine, lactate déshydrogénase, bilirubine totale, haptoglobine, hémoglobine libre du plasma, hémoglobine urinaire, fonction rénale si besoin. "
          "Volet 4 : bactériologie, hémocultures du patient et culture du produit, pour ne pas manquer une contamination.", 2),
        P("La confirmation écrite est la détection d'un anticorps ou d'une incompatibilité de groupe, donc un test de compatibilité positif, et un test de Coombs direct positif. "
          "Le test de Coombs direct regarde ce qui est déjà fixé sur le globule du patient. La recherche d'anticorps et le test de compatibilité regardent ce qui est libre dans le plasma : "
          "c'est l'étude indirecte. L'aide-mémoire nomme le direct. Il décrit l'indirect par la recherche et la compatibilité, sans employer le mot indirect.", 2),
        P("On arrête la transfusion dès que cette réaction est suspectée. On garde un accès veineux pour le remplissage si la tension tombe, sans ajouter de médicament dans la poche. "
          "Le guide 2026 demande que le système qualité dise qui décide d'interrompre ou d'arrêter, et il cite l'oxygène, l'antihistaminique, les stéroïdes, le diurétique et le remplacement de volume "
          "comme exemples de traitements possibles selon le tableau, pas comme une ordonnance unique pour toute fièvre.", 3),
        P("Le rapport 2024 décrit une patiente de plus de 80 ans, fractures du fémur et du rachis, escarres, insuffisance rénale aiguë, hypernatrémie sévère, anémie avec hémoglobine inférieure à 70 g/l, "
          "sténose aortique sévère. Une confusion de patients a fait transfuser un concentré A à une receveuse O. L'erreur a été vue vite, environ 25 ml, et la transfusion arrêtée. "
          "Les constantes n'ont pas bougé dans l'immédiat : l'hypotonie et l'hypoxie étaient déjà là. Un remplissage et un diurétique ont été ajoutés à cause de l'incompatibilité. "
          "L'hémolyse était réelle, créatinine et bilirubine un peu hautes, lactate déshydrogénase et haptoglobine illisibles sur un échantillon hémolysé, pas d'urine analysée. "
          "Environ 7 heures plus tard, détresse respiratoire et œdème pulmonaire. Décès le lendemain, sans autopsie. Grade 4, imputabilité possible. "
          "Le rapport dit lui-même qu'on ne sait pas séparer la part de l'hémolyse et la part du remplissage plus du diurétique sur une sténose aortique et une insuffisance rénale.", 1),
    ]


def rtfnh():
    return [
        P("La réaction fébrile non hémolytique est un ou plusieurs symptômes de la liste, entre 4 et 6 heures après le début, délai médian 80 minutes, sans autre cause clinique. "
          "Souvent les signes arrivent vers la fin de la poche. Avant de la nommer, on exclut l'hémolyse et la fièvre d'une contamination bactérienne.", 2),
        P("Symptômes, liste entière. Fièvre supérieure à 38 °C et hausse d'au moins 1 °C par rapport à la température d'avant. "
          "Frissons, même isolés. Crampes. Sensation de froid, malaise. Parfois céphalées et nausées. "
          "Le seuil de 38 °C avec 1 °C définit cette catégorie. Le seuil supérieur à 39 °C avec plus de 2 °C, lui, force au moins le grade sévère dans le rapport annuel. On ne les échange pas.", 2),
        P("Le bilan est le même squelette que pour l'hémolyse : documents, immunohématologie avec Coombs direct et compatibilité, marqueurs d'hémolyse, cultures du patient et du produit. "
          "La confirmation est négative : tous ces paramètres sont négatifs, et rien d'autre n'explique les symptômes.", 2),
        P("En 2024, le taux de déclarations de cette réaction est de 194 pour 100 000 transfusions, soit 1 sur 515. "
          "Le tableau par grade compte 518 déclarations : 415 de grade 1, 98 de grade 2, 5 de grade 3, aucun décès. "
          "Une fièvre isolée n'autorise pas à sauter le bilan d'hémolyse.", 1),
    ]


def allergie():
    return [
        P("L'aide-mémoire classe l'allergie en trois gravités, pas en une seule case. Légère : signes cutanés légers. "
          "Modérée, dite anaphylactoïde : un autre organe est touché, cœur, respiration ou tube digestif, ou une urticaire. "
          "Anaphylactique : choc anaphylactique ou œdème de Quincke. Les signes commencent en général une à deux heures après le début, délai médian 45 minutes.", 2),
        P("Légère : prurit, exanthème, œdèmes locaux, urticaire limitée, pas de menace vitale, réponse rapide au traitement symptomatique. "
          "Modérée, en plus : gêne à avaler, œdème laryngé avec stridor, voix rauque, dyspnée, toux, bronchospasme, nausées, vomissements, diarrhée, hypotension, tachycardie, "
          "et une amélioration sous antihistaminique, stéroïde, ou les deux. "
          "Anaphylactique : chute de tension importante et difficile, éventuellement arrêt circulatoire, perte de connaissance, et les autres signes allergiques.", 2),
        P("Une réaction légère ne demande pas d'analyses dans l'aide-mémoire. Une réaction modérée exclut les autres causes : radiographie et éventuellement gaz du sang si dyspnée, "
          "pour ne pas manquer une surcharge ou une atteinte pulmonaire aiguë, et bilan d'hémolyse plus hémocultures si hypotension, pour ne pas manquer l'hémolyse aiguë ou le sepsis. "
          "Une anaphylaxie, ou une réaction modérée sévère qui se répète : on cherche un déficit en immunoglobuline A et des anticorps anti-immunoglobuline A, et une tryptase qui, si elle monte, soutient l'allergie.", 2),
        P("En 2024, 52 réactions allergiques déclarées pour 100 000 transfusions, soit 1 sur 1920, et 139 déclarations au tableau des grades : 87 de grade 1, 38 de grade 2, 14 de grade 3, aucun décès dans ce total. "
          "Parmi les réactions de grade 3 ou 4 avec imputabilité au moins possible, l'allergie est la plus nombreuse : 13, dont 4 possibles, 7 probables et 2 certaines.", 1),
        P("Le choc anaphylactique se traite d'abord par l'adrénaline, pas par l'antihistaminique. Adrenalin Sintetica, numéro 56551, solution à 1 mg/ml. "
          "La dose habituelle écrite pour le choc est de 500 microgrammes, soit 0,5 ml de cette solution. On peut la répéter à plusieurs minutes d'intervalle, l'information dit 5 minutes, selon la tension, le pouls et la respiration. "
          "Des demi-doses sont plus sûres si le patient prend de l'amitriptyline, de l'imipramine ou un bêtabloquant. Le bêtabloquant non cardiosélectif peut empêcher la réponse.", 5),
        P("Tableau d'âge de la même information, injection intramusculaire, liste entière. Plus de 12 ans : 0,5 mg, soit 0,5 ml. "
          "De 6 à 12 ans : 0,3 mg, soit 0,3 ml. De 6 mois à 6 ans : 0,15 mg, soit 0,15 ml. Moins de 6 mois : 0,01 mg/kg, soit 0,01 ml/kg. "
          "Le site est la face antérolatérale du tiers moyen de la cuisse, aiguille assez longue. On évite la fesse, risque de nécrose. "
          "La solution à 1 mg/ml ne convient pas telle quelle en intraveineux : on la dilue au dixième, à 0,1 mg/ml, et cette voie est réservée à qui en a l'habitude. "
          "La dose intraveineuse usuelle écrite est de 0,05 à 0,2 mg, à répéter toutes les 3 à 5 minutes selon l'effet.", 5),
        P("Grossesse : l'adrénaline ne s'utilise que si elle est clairement indispensable. Elle traverse le placenta. Elle est interdite au deuxième stade du travail, "
          "parce qu'elle peut relâcher l'utérus et favoriser un saignement. Ce n'est pas une contre-indication du choc anaphylactique de la femme enceinte avant ce stade : l'indication vitale reste écrite.", 5),
        P("Tavegyl injectable, numéro 35501, est indiqué pour prévenir ou traiter une réaction allergique ou pseudo-allergique, l'information cite l'exemple d'une transfusion. "
          "Dans le choc anaphylactique, c'est un traitement secondaire, après l'adrénaline à 0,01 mg/kg en intramusculaire. "
          "La dose générale est d'une ampoule, 2 ml soit 2 mg, par voie intraveineuse ou intramusculaire, matin et soir. "
          "En prophylaxie, une ampoule en intraveineux lent juste avant le moment où l'on craint la réaction. "
          "L'ampoule contient du sorbitol : intolérance héréditaire au fructose, on ne l'utilise pas. Elle contient aussi de l'éthanol et du propylène glycol : "
          "l'information demande d'y penser chez la femme enceinte, celle qui allaite, l'enfant, la maladie du foie et l'épilepsie. "
          "L'enfant reçoit 0,025 mg/kg par jour en deux injections intramusculaires.", 7),
    ]


def trali():
    return [
        P("L'aide-mémoire décrit le TRALI comme un diagnostic clinique d'exclusion chez une personne qui n'avait pas d'insuffisance respiratoire aiguë avant la transfusion. "
          "Deux types sont nommés, les deux restent dans le cours. Immunogène : anticorps anti-leucocytes du donneur, anti-HNA ou anti-HLA, qui réagissent avec les leucocytes du receveur. "
          "Non immunogène : des substances actives du produit, des lipides par exemple, activent les neutrophiles.", 2),
        P("Les signes commencent pendant la transfusion ou dans les 6 heures. Détresse respiratoire soudaine. "
          "Hypoxémie : rapport de la pression artérielle en oxygène sur la fraction inspirée au plus égal à 300 mm Hg, ou saturation inférieure à 90 % à l'air ambiant, ou d'autres signes cliniques d'hypoxémie. "
          "Infiltrats pulmonaires bilatéraux. Pas de signe de surcharge du ventricule gauche.", 2),
        P("TRALI probable : ces paramètres sont réunis et il n'y a pas de relation de temps avec un autre facteur de risque d'atteinte pulmonaire aiguë. "
          "TRALI possible : les mêmes paramètres, plus une relation de temps claire avec un autre facteur de risque. "
          "Facteurs directs, liste entière : inhalation, pneumonie, toxiques inhalés, contusion pulmonaire, quasi-noyade. "
          "Facteurs indirects, liste entière : sepsis sévère, choc, polytraumatisme, brûlure. Omettre le TRALI possible amputait la classification du 9 août 2024.", 2),
        P("Analyses : anticorps anti-leucocytes chez le donneur et antigène correspondant chez le receveur, ou test de compatibilité positif contre les granulocytes du receveur. "
          "Le peptide natriurétique de type B peut aider à écarter une surcharge. L'aide-mémoire ne donne pas un seuil chiffré de ce peptide. On n'en invente pas.", 2),
        P("En 2024, une déclaration de TRALI, taux 0,4 pour 100 000 transfusions, soit environ 1 sur 265 000. "
          "Le tableau 2020 à 2024 des comptes TACO et TRALI : en 2024, 37 surcharges et 1 TRALI, taux de TRALI 0,4 pour 100 000. "
          "En 2023, 36 surcharges et 1 TRALI. En 2022, 39 et 2. En 2021, 62 et 6. En 2020, 88 et 3. "
          "La rareté ne retire pas le diagnostic quand les quatre signes respiratoires sont là et que la surcharge ne l'est pas.", 1),
        P("Le geste n'est pas celui de la surcharge. Oxygène, ventilation si besoin, on ne commence pas par le diurétique. "
          "Le diurétique de l'information du furosémide vise l'œdème pulmonaire de surcharge, pas une atteinte pulmonaire sans surcharge du ventricule gauche.", 2),
    ]


def taco():
    return [
        P("La surcharge volémique de l'aide-mémoire : signes d'hypervolémie pendant la transfusion ou dans les 6 heures, délai médian 90 minutes. "
          "Au moins quatre des signes de la liste doivent être présents. Liste entière : détresse respiratoire aiguë, tachycardie ou tachyarythmie, hypertension, "
          "œdème pulmonaire aigu ou aggravé sur la radiographie, bilan des volumes positif, autres signes qui sont douleur ou pression thoracique, toux, céphalées, cyanose, "
          "et fièvre dans environ 30 % des cas. La fièvre ne suffit pas, et elle ne doit pas faire oublier l'hémolyse.", 2),
        P("Analyses : radiographie du thorax, et peptide natriurétique dont la hausse renforce le diagnostic clinique. Pas de seuil chiffré dans l'aide-mémoire.", 2),
        P("En 2024, 14 surcharges pour 100 000 transfusions, soit 1 sur 7200, et 37 déclarations : 3 de grade 1, 26 de grade 2, 8 de grade 3, aucun grade 4 dans le tableau des grades. "
          "Parmi les grades 3 ou 4 avec imputabilité au moins possible, 8 surcharges : 4 possibles, 3 probables, 1 certaine. "
          "Le rapport rappelle une transfusion lente, l'exemple écrit est 1 ml par kilogramme de poids et par heure, une évaluation du risque avant de transfuser, et d'envisager un diurétique préventif.", 1),
        P("Si un diurétique est donné, la dose lue est celle de Lasix injectable, numéro 30630. "
          "Adulte et adolescent dès 15 ans : dose initiale de 20 à 40 mg par voie intraveineuse ou intramusculaire. "
          "Œdème pulmonaire aigu : dose initiale de 40 mg, soit deux fois 20 mg, en intraveineux. Si l'état l'exige, 20 minutes plus tard, une nouvelle injection de 20 à 40 mg. "
          "Enfant de moins de 15 ans : 1 mg par kilogramme en intraveineux ou intramusculaire, maximum 20 mg par jour, relais oral dès que possible. "
          "Grossesse : pas d'emploi sauf nécessité absolue, durée brève, surveillance de la croissance du fœtus. "
          "Avec un inhibiteur de l'enzyme de conversion, une chute de tension jusqu'au choc est décrite : on suspend ou on réduit le diurétique trois jours au moment d'introduire ou d'augmenter cet inhibiteur.", 6),
        P("On n'applique pas ce diurétique à la place du geste d'une hémolyse ABO. Le cas de 2024, sténose aortique et insuffisance rénale, montre que remplissage et diurétique peuvent eux-mêmes peser sur l'évolution. "
          "La surcharge se traite parce que le ventricule gauche est plein. L'hémolyse aiguë ne se résume pas à un poumon plein.", 1),
    ]


def allo():
    return [
        P("L'allo-immunisation de l'aide-mémoire est la découverte, après transfusion, d'un allo-anticorps cliniquement pertinent contre un antigène des cellules du sang, "
          "antigène érythrocytaire, HLA ou HPA, qui n'avait pas été identifié avant, parce qu'il n'était pas là ou pas détectable, et sans hémolyse clinique ni biologique. "
          "S'il y a hémolyse, ce n'est plus cette case : c'est une réaction hémolytique.", 2),
        P("Les anticorps irréguliers que le cours ne réduit pas sont ceux qui hémolysent ou qui atteignent le fœtus : en pratique Kell, Duffy et Kidd, et aussi l'anti-D, l'anti-c, l'anti-E. "
          "Kell, antigène K, peut détruire les précurseurs érythroïdes du fœtus en plus d'hémolyser. Duffy, surtout Fya, peut donner une réaction hémolytique et une maladie du nouveau-né. "
          "Kidd, Jka et Jkb, est le classique de l'anticorps qui disparaît du plasma puis revient en quelques jours après une nouvelle exposition : hémolyse retardée, parfois intravasculaire malgré le mot retardée. "
          "Le système ABO et le RhD restent à part : ce ne sont pas des anticorps irréguliers de cette case quand il s'agit des anticorps naturels anti-A et anti-B.", 2),
        P("En 2024, 1519 allo-immunisations déclarées, toutes en grade 2, aucune en grade 1, 3 ou 4. "
          "Le taux est de 569 pour 100 000 transfusions, soit 1 sur 176, contre 491 pour 100 000, soit 1 sur 204, en 2023. "
          "C'est la ligne la plus nombreuse du tableau. Elle n'est pas bénigne au sens du grade : le rapport classe l'allo-immunisation au minimum comme sévère.", 1),
        P("La recherche d'anticorps irréguliers se fait avant la transfusion, et elle a une durée de validité fixée par l'établissement. "
          "Le guide 2026 ne donne pas une seule heure nationale. Le référentiel genevois du 15 février 2024 écrit 96 heures après l'heure du prélèvement : au-delà, on prélève de nouveau. "
          "Transfuser sur une recherche périmée, c'est rater un anticorps apparu depuis, surtout un Kidd.", 3),
    ]


def autres_cases():
    """Cases de la classification qu'aucun DX ne doit faire disparaître."""
    return [
        P("Purpura post-transfusionnel : thrombopénie entre 5 et 12 jours après un produit cellulaire, avec un anticorps antiplaquettaire, en règle anti-HPA-1a, chez le receveur, "
          "et l'antigène correspondant chez le donneur ou une épreuve de compatibilité positive. On compte les plaquettes et on explore la coagulation.", 2),
        P("Maladie du greffon contre l'hôte associée à la transfusion : syndrome entre 1 et 6 semaines, sans autre cause. "
          "Fièvre, éruption, diarrhée, foie et ictère, pancytopénie, et une histologie pathognomonique. Analyses : histologie de peau ou de foie, typage HLA, chimérisme.", 2),
        P("Dyspnée associée à la transfusion : insuffisance respiratoire dans les 24 heures, qui n'est ni un TRALI, ni une surcharge, ni une allergie, "
          "et qui ne s'explique pas par la maladie de fond.", 2),
        P("Réaction hypotensive : la baisse de tension est le signe principal ou unique, après avoir exclu les autres réactions et les maladies qui baissent la tension. "
          "Baisse d'au moins 30 mm Hg de la systolique, de la diastolique, ou des deux, par rapport à avant. "
          "Pendant la transfusion ou dans l'heure, délai médian 15 minutes, souvent dans les premières minutes, parfois un phénomène d'arrêt puis de reprise si l'on relance la poche. "
          "L'amélioration est rapide quand on arrête et que l'on soutient.", 2),
        P("Hémosidérose associée : ferritine au moins 1000 µg/l, avec ou sans organe atteint, chez une personne transfusée de façon répétée en concentrés érythrocytaires.", 2),
        P("Hyperkaliémie associée : potassium supérieur à 5 mmol/l, ou hausse d'au moins 1,5 mmol/l, dans l'heure qui suit la transfusion.", 2),
        P("Infection transmise : infection apparue après la transfusion, inconnue avant, sans autre source. Toute suspicion se déclare, formulaire de réaction, dans les 15 jours après qu'on l'a reconnue, "
          "sans attendre la fin de l'enquête rétrospective. Hépatites B et C et suspicion de virus de l'immunodéficience humaine : Swissmedic et l'Office fédéral de la santé publique. "
          "Les autres virus : Swissmedic, et l'Office si le cas l'exige. Bactérie : bactériémie ou sepsis, souvent pendant ou juste après, fièvre typiquement supérieure à 39 °C et hausse de 2 °C, "
          "frissons, hypotension ou hypertension, tachycardie, céphalées, douleur thoracique. On cultive le reste de la poche et le sang du patient. "
          "Parasites : le même agent chez le receveur et le donneur, ou l'anticorps chez le donneur, paludisme ou Trypanosoma cruzi par exemple. "
          "Prions : aucune preuve en Suisse à la date de l'aide-mémoire, mais les suspicions se déclarent.", 2),
        P("Erreur transfusionnelle : le patient a reçu un composant qui ne lui était pas destiné ou qui ne convenait pas, y compris non irradié ou non négatif pour le cytomégalovirus quand il aurait dû l'être. "
          "On déclare même sans dommage, avec le récit de l'erreur et les mesures. Formulaire des incidents graves. "
          "Near miss : l'écart a été vu avant la transfusion et aurait pu donner une erreur ou une réaction. En 2024, les near miss de grade 1, sans risque de confusion ou à risque faible, ne sont plus obligatoires à déclarer. "
          "Les incidents graves sans changement de RhD sont passés de 48 à 69 entre 2023 et 2024.", 1),
    ]


def antid():
    return [
        P("Rhophylac 300, numéro 53609, est une seringue de 2 ml qui contient 300 µg, soit 1500 UI, d'immunoglobuline G humaine anti-D. "
          "Au plus 60 mg de protéines plasmatiques par seringue, dont 20 mg d'albumine stabilisatrice, et au moins 95 % du reste sont des immunoglobulines G. "
          "La neutralisation de 0,5 ml d'hématies RhD positif, ou de 1 ml de sang entier RhD positif, demande environ 10 µg, soit 50 UI.", 4),
        P("Prophylaxie de routine chez une femme RhD négatif, D partiel compris : 300 µg, soit 1500 UI, entre la 28e et la 30e semaine, intraveineux ou intramusculaire. "
          "Si le besoin n'est vu qu'après la 30e semaine, on injecte le plus vite possible. "
          "Le produit n'est pas destiné à une personne RhD positif ni à une personne déjà immunisée contre D.", 4),
        P("Complication de grossesse, liste de l'information : geste invasif, amniocentèse, biopsie de trophoblaste, prélèvement de sang fœtal, shunt, réduction embryonnaire, "
          "version par manœuvre externe, interruption, saignement, fausse couche, rupture de trompe, grossesse extra-utérine, mort fœtale, traumatisme abdominal. "
          "Dose : 300 µg, soit 1500 UI, le plus vite possible, au plus tard dans les 72 heures. Passé ce délai, on injecte quand même le plus vite possible. "
          "Puis on répète toutes les 12 semaines jusqu'à l'accouchement. "
          "Diagnostic prénatal invasif : la même dose de 300 µg dans les 72 heures, quel que soit le terme.", 4),
        P("Après l'accouchement : 300 µg, soit 1500 UI, le plus vite possible, au plus tard dans les 72 heures, si l'enfant est concerné par l'indication RhD. "
          "Délai dépassé : on injecte quand même dès que possible.", 4),
        P("Hémorragie fœto-maternelle excessive connue ou supposée : on compte les hématies fœtales par le test de Kleihauer-Betke ou une autre méthode adaptée, la cytométrie en flux est citée. "
          "Au-dessus de 4 ml d'hématies fœtales RhD positif, dose supplémentaire de 10 µg, soit 50 UI, pour chaque 0,5 ml de ces hématies, ou pour chaque 1 ml de sang complet fœtal, de préférence en intraveineux. "
          "Si l'on ne peut pas exclure un passage excessif et qu'aucun test n'est disponible, on ajoute 300 µg, soit 1500 UI.", 4),
        P("Transfusion incompatible de sang RhD positif ou de produit qui contient des hématies RhD positif, chez une personne RhD négatif. "
          "La dose est 10 µg pour 0,5 ml de concentré, ou la formulation 10 µg soit 50 UI pour 0,5 ml. "
          "L'intraveineux donne une disponibilité immédiate. Par le muscle, une dose importante se répartit sur plusieurs jours. "
          "Une dose totale de 3'000 µg, soit 15'000 UI, suffit même au-delà de 300 ml de sang complet ou de 150 ml de concentré. "
          "On ne dépasse en général pas 3'000 µg, soit 15'000 UI, à cause du risque d'hémolyse. "
          "Ces patients se surveillent sur la clinique et la biologie. Chez l'enfant, la dose dépend du volume, elle n'est pas différente dans son principe, et un spécialiste de transfusion la fixe.", 4),
        P("Voie : injection intraveineuse lente ou intramusculaire lente, produit à température ambiante. Trouble de coagulation ou voie musculaire contre-indiquée : on choisit la veine. "
          "Au-dessus de 5 ml en musculaire, on répartit les points. On ne mélange pas avec un autre médicament. "
          "Contre-indications : hypersensibilité aux immunoglobulines humaines ou à un excipient. La voie musculaire est contre-indiquée si thrombopénie sévère ou autre trouble de coagulation. "
          "Grossesse et après l'accouchement : c'est l'usage du produit. Aucun effet négatif connu sur la grossesse ou le nouveau-né dans le texte lu.", 4),
        P("L'immunoglobuline A est sous le seuil de détection de 5 µg/ml, mais des traces restent possibles. Une personne qui a des anticorps anti-immunoglobuline A peut faire une anaphylaxie. "
          "Le produit peut contenir des anti-A, des anti-B, des anti-C et des anti-E, visibles sur un test sensible. "
          "Après l'injection, on attend au moins 3 mois avant un vaccin vivant, rougeole, oreillons, rubéole, varicelle, sinon le vaccin peut échouer. "
          "L'injection de 300 µg après l'accouchement prévient 90 % des sensibilisations RhD. Avec la prophylaxie prénatale en plus, la protection monte jusqu'à 99 %. "
          "Deux études : injection à la 28e semaine et dans les 72 heures après la naissance d'un enfant RhD positif, 206 femmes en intraveineux et 202 en intramusculaire dans l'analyse per protocole.", 4),
        P("Le guide britannique de 2014 ne remplace pas la seringue suisse. Il dit d'injecter le plus tôt possible et toujours dans les 72 heures, "
          "et qu'un peu de protection peut rester jusqu'à 10 jours si le délai a été manqué. "
          "Avant 12 semaines, il ne retient l'indication que pour la grossesse extra-utérine, la môle, l'interruption, et le saignement répété, abondant ou avec douleur, "
          "dose minimale 250 unités internationales, sans test de passage fœtal. "
          "Entre 12 et 20 semaines, minimum 250 unités internationales dans les 72 heures, sans ce test. "
          "Après 20 semaines, minimum 500 unités internationales dans les 72 heures, et le test est requis. "
          "Prophylaxie systématique : une dose vers 28 semaines, ou deux doses à 28 et 34 semaines. Le prélèvement de la 28e semaine se fait avant l'injection. "
          "La prophylaxie systématique s'ajoute aux doses des événements, elle ne les remplace pas. "
          "À la naissance, groupe ABO et RhD sur le cordon. Enfant RhD positif : au moins 500 unités internationales dans les 72 heures, plus le test de passage, doses supplémentaires selon le volume. "
          "500 unités internationales par voie musculaire couvrent jusqu'à 4 ml d'hématies fœtales dans ce guide. "
          "En Suisse, on prescrit la dose de l'information 53609, 300 µg soit 1500 UI, et le calcul du supplément au-dessus de 4 ml suit les 10 µg pour 0,5 ml, pas le minimum britannique.", 8),
        P("Le même guide dit qu'aucun procédé sérologique ne sépare un anti-D passif d'un anti-D immun. Si l'on ne tranche pas, on continue la prophylaxie. "
          "Un groupe D indéterminé chez la femme se traite comme négatif jusqu'à confirmation. Un groupe D indéterminé sur le cordon se traite comme positif jusqu'à confirmation. "
          "Si l'on n'a pas de sang de l'enfant, on le considère positif pour décider l'injection. "
          "Le test de Coombs direct sur le cordon n'est pas systématique : la prophylaxie prénatale peut le positiver. On le fait si l'on suspecte une maladie hémolytique, "
          "hémoglobine de cordon basse ou anticorps immun maternel déjà connu. "
          "Au-dessus de 4 ml, contrôle de disparition des cellules fœtales 48 heures après une dose intraveineuse et 72 heures après une dose intramusculaire.", 8),
    ]


def lit_et_surveillance():
    return [
        P("Le guide 2026 exige deux personnes formées et habilitées, chacune un contrôle séparé, au chevet, juste avant la transfusion. "
          "Si l'on est interrompu, on recommence depuis le début. Chaque poche se contrôle. Une identification électronique peut remplacer une des deux personnes, "
          "mais on demande encore l'identité entière au patient. Discordance inexpliquée : on ne transfuse pas, on appelle le laboratoire. On documente.", 3),
        P("On contrôle l'identité demandée au patient s'il peut répondre, la concordance du groupe, le nom, le prénom et la date de naissance complète sur la carte, le bulletin et la poche, "
          "la validité des tests prétransfusionnels, la péremption, l'intégrité de la poche, la turbidité, l'hémolyse, une couleur anormale, un caillot. "
          "Un produit abîmé ne part pas. La nuit, on évite la transfusion quand c'est possible, parce que l'attention et les effectifs baissent.", 3),
        P("Surveillance étroite les 15 premières minutes, puis constantes régulièrement pendant et après, sur chaque poche. "
          "Voie périphérique, centrale, intra-osseuse ou chambre. Tubulure à filtre. Après la transfusion, on rince la lumière avec du chlorure de sodium à 0,9 %. "
          "Dès que la chaîne du froid est rompue, et dès que la poche est perforée, la transfusion se termine en général dans les six heures. "
          "Les plaquettes partent dès réception. Un réchauffement à 37 °C n'est permis qu'avec un appareil prévu pour cela : agglutinines froides, transfusion massive, néonatologie, exsanguino-transfusion.", 3),
        P("Le référentiel genevois du 15 février 2024 sépare deux gestes. Concordance documentaire : tout produit, y compris l'urgence et la personne allogreffée. "
          "Compatibilité par la carte ABO : seulement les globules rouges, y compris l'autotransfusion devenue rare et le concentré O RhD négatif d'extrême urgence. "
          "Pas de carte pour le plasma ni pour les plaquettes. La carte ne sert pas à déterminer le groupe ABO. "
          "Les cupules négatives se lisent jusqu'à 3 minutes. Anti-A bleu turquoise, anti-B jaune, sinon on n'utilise pas la carte. Usage unique, personnel formé. "
          "Doute ou discordance : on ne transfuse pas, on appelle le médecin et le laboratoire. Homonymes et jumeaux : on lit le prénom et la date entière.", 9),
        P("La personne responsable de l'hémovigilance est désignée par tout établissement qui transfuse, signalée à Swissmedic. C'est un médecin, ou une autre formation reconnue s'il y a l'expérience. "
          "Elle porte la déclaration, l'archivage et l'enquête rétrospective. Les données de traçabilité se gardent 30 ans depuis la révision entrée en vigueur le 1er janvier 2019. "
          "On déclare les réactions, la formation d'anticorps, les événements graves, les near miss qui restent exigibles, l'enquête rétrospective et les défauts de qualité. "
          "La traçabilité porte sur la transfusion réelle, pas seulement sur la sortie du laboratoire.", 3),
    ]


def geste_immediat():
    return [
        P("Dès qu'une réaction est suspectée, on arrête la transfusion. On ne termine pas la poche. On garde la voie veineuse pour pouvoir remplir ou injecter le traitement qui correspond au tableau. "
          "On ne met pas de médicament dans la poche de sang. On revérifie l'identité, le groupe écrit et le numéro de poche avant d'accuser l'anticorps.", 3),
        P("On appelle le médecin et le laboratoire. On met de côté la poche, la tubulure et les nouveaux tubes. "
          "Fièvre, douleur, urines foncées, malaise, chute de tension ou doute : le bilan en quatre volets, y compris les cultures, avant d'appeler cela une simple fièvre. "
          "Dyspnée : on sépare surcharge, atteinte pulmonaire aiguë et allergie avant de choisir le diurétique ou l'adrénaline.", 2),
        P("Anaphylaxie : adrénaline intramusculaire selon le tableau d'âge de l'information 56551, cuisse, tout de suite, puis répétition selon tension, pouls et respiration. "
          "L'antihistaminique de l'information 35501 vient après, pas à la place. "
          "Surcharge : oxygène, position, diurétique selon l'information 30630 si l'on décide d'en donner. "
          "Atteinte pulmonaire sans surcharge : oxygène et support ventilatoire, pas le diurétique comme premier réflexe. "
          "Hémolyse : arrêt, voie, bilan, soutien de la tension et du rein, déclaration. Le diurétique n'est pas le traitement de l'incompatibilité ABO.", 5),
        P("On déclare. Le grade se pose d'abord. L'imputabilité se pose à part. Un décès n'est un grade 4 que si l'imputabilité est au moins possible. "
          "La personne responsable de l'hémovigilance transmet à Swissmedic. L'erreur de patient se déclare même si le volume était petit.", 1),
    ]


# --- pages ---

DX = [
    "Allo-immunisation par anticorps irrégulier cliniquement significatif",
    "Réaction transfusionnelle fébrile non hémolytique",
    "Réaction transfusionnelle allergique",
    "Maladie hémolytique du nouveau-né par incompatibilité ABO",
    "Surcharge volémique associée à la transfusion",
    "Réaction hémolytique transfusionnelle retardée",
    "Maladie hémolytique du nouveau-né par anti-D",
    "Incompatibilité plasmatique et plaquettaire ABO",
    "Réaction hémolytique aiguë par incompatibilité ABO",
    "Insuffisance pulmonaire aiguë post-transfusionnelle",
]


def ile_court(nom, ligne, src=2):
    return [
        P(f"{nom}. {ligne}", src),
        P("Le détail chiffré, les listes complètes et les doses lues sont dans la fenêtre."),
    ]


def page_phase_a():
    noms = " ".join(f"DX.{i} {n}." for i, n in enumerate(DX, 1))
    essentiels = [
        P("Incompatibilité de groupe sanguin : les anticorps d'une personne reconnaissent les antigènes des globules d'une autre, donneur, receveur ou fœtus."),
        P("On arrête la transfusion au premier signe, on garde la voie, on fait le bilan d'hémolyse de l'aide-mémoire du 9 août 2024, on déclare."),
        P("ABO, RhD, Kell, Duffy et Kidd restent entiers. Le plasma ne suit pas le tableau des globules."),
    ]
    c = {}
    c[1] = (ile_court("Incompatibilité de groupe sanguin", "Antigène sur le globule, anticorps dans le plasma ou chez la mère, hémolyse ou immunisation."), H([
        P("Une incompatibilité de groupe sanguin est la rencontre d'un anticorps et d'un antigène érythrocytaire que cet anticorps reconnaît, "
          "alors que cet antigène est porté par des globules transfusés, par les globules du receveur si l'anticorps vient du donneur, ou par les globules du fœtus.", 2),
        P("Deux familles d'anticorps ne se mélangent pas. Les anticorps naturels du système ABO, surtout des immunoglobulines M, sont déjà là sans transfusion préalable et fixent bien le complément : "
          "l'hémolyse ABO est souvent dans le vaisseau. Les anticorps irréguliers, anti-D, Kell, Duffy, Kidd, sont en général des immunoglobulines G, acquises après une transfusion ou une grossesse. "
          "Ils traversent le placenta. Kidd peut quand même hémolyser dans le vaisseau lors d'une réponse mémoire.", 2),
        P("Le test de Coombs direct montre l'immunoglobuline ou le complément déjà collé au globule du patient. "
          "La recherche d'anticorps irréguliers et la compatibilité montrent l'anticorps libre dans le plasma : c'est le versant indirect, décrit par l'aide-mémoire comme recherche et test de compatibilité.", 2),
        *classification_complete()[:2],
    ]))
    c[2] = (ile_court("Déclarations 2024", "L'allo-immunisation domine les comptes. La surcharge domine les formes graves respiratoires. L'hémolyse ABO reste rare et peut tuer."), H([
        P("En 2024, le taux de réactions est de 9,0 pour 1000 transfusions, en hausse de 13 % sur l'année d'avant, et de 3,3 pour 1000 si l'on retire les allo-anticorps, en hausse de 9 %.", 1),
        P("Réaction fébrile non hémolytique : 194 pour 100 000, soit 1 sur 515, 518 déclarations. Allergie : 52 pour 100 000, soit 1 sur 1920, 139 déclarations. "
          "Surcharge : 14 pour 100 000, soit 1 sur 7200, 37 déclarations. TRALI : 0,4 pour 100 000, soit environ 1 sur 265 000, 1 déclaration. "
          "Allo-immunisation : 569 pour 100 000, soit 1 sur 176, 1519 déclarations. Réactions hémolytiques, aiguës et retardées ensemble : 12.", 1),
        P("Grades 3 ou 4 avec imputabilité au moins possible, 33 au total : allergie 13, surcharge 8, hypotensive 5, autres 4, fébrile 1, hémolytique 1, dyspnée associée 1, TRALI 0 dans cette sélection. "
          "Le seul décès classé grade 4 en 2024 est une hémolyse aiguë ABO, imputabilité possible.", 1),
        P("Aucun texte lu ne donne la part des groupes ABO ni du RhD dans la population suisse, ni l'incidence nationale de la maladie hémolytique du nouveau-né. Ces taux ne sont pas enseignés.", 4),
        P("L'information de Rhophylac écrit qu'une dose de 300 µg après l'accouchement prévient 90 % des sensibilisations RhD, et jusqu'à 99 % si la prophylaxie prénatale est ajoutée. "
          "C'est une efficacité de prévention, pas une incidence de maladie.", 4),
    ] + classification_complete()[4:7]))
    c[3] = (ile_court("ABO, RhD, Kell, Duffy, Kidd", "Les globules et le plasma ne se lisent pas dans le même sens. L'anti-D traverse le placenta."), H(
        phrases_matrice() + [
            P("L'antigène D est le plus immunisant du système Rh dans la pratique de la prophylaxie. L'anti-D est une immunoglobuline G. "
              "Une femme RhD négatif, y compris un D partiel, peut s'immuniser par des hématies fœtales RhD positif ou par une transfusion. "
              "Rhophylac n'est pas fait pour une personne déjà immunisée : là, l'anticorps est une maladie, plus une prévention.", 4),
            P("Kell. L'anti-K atteint le fœtus tôt parce qu'il supprime l'érythropoïèse, pas seulement les globules déjà circulants. "
              "Un titre faible n'autorise pas à classer l'anti-K comme anodin. On le traite comme significatif dès qu'il est identifié, et le suivi obstétrical ne se calque pas sur un anti-D bénin.", 8),
            P("Duffy. L'anti-Fya est un anticorps irrégulier cliniquement significatif : réaction transfusionnelle et maladie du nouveau-né sont toutes deux décrites dans la pratique des banques de sang. "
              "Le phénotype Fy(a−b−) est une autre question, de répartition des antigènes, et il ne se confond pas avec l'absence d'anticorps.", 2),
            P("Kidd. L'anti-Jka et l'anti-Jkb disparaissent souvent du sérum entre les expositions. La recherche peut être négative le jour du bilan, puis positive après la transfusion, "
              "avec une chute d'hémoglobine entre le jour 1 et le jour 28. C'est le piège de la réaction retardée. L'élution sur un Coombs direct positif retrouve parfois l'anticorps que le plasma ne montre plus.", 2),
            P("Le test de Kleihauer-Betke distingue les hématies fœtales, dont l'hémoglobine résiste à l'élution acide, des hématies adultes. "
              "L'information suisse l'utilise, ou la cytométrie, pour décider une dose d'anti-D au-dessus de 4 ml d'hématies fœtales RhD positif.", 4),
        ]
    ))
    c[4] = (ile_court("Dix diagnostics", "On classe d'abord ce qui tue, puis on nomme la case de l'aide-mémoire."), H([
        P("Ordre de lecture, du plus déclaré vers le plus rare, avec les deux maladies du nouveau-né à leur place clinique. "
          "DX.1 Allo-immunisation par anticorps irrégulier cliniquement significatif. "
          "DX.2 Réaction transfusionnelle fébrile non hémolytique. "
          "DX.3 Réaction transfusionnelle allergique. "
          "DX.4 Maladie hémolytique du nouveau-né par incompatibilité ABO. "
          "DX.5 Surcharge volémique associée à la transfusion. "
          "DX.6 Réaction hémolytique transfusionnelle retardée. "
          "DX.7 Maladie hémolytique du nouveau-né par anti-D. "
          "DX.8 Incompatibilité plasmatique et plaquettaire ABO. "
          "DX.9 Réaction hémolytique aiguë par incompatibilité ABO. "
          "DX.10 Insuffisance pulmonaire aiguë post-transfusionnelle.", 1),
        P("Ordre de l'algorithme, qui n'est pas l'ordre de fréquence. On traite d'abord la réaction hémolytique aiguë ABO, l'anaphylaxie, le TRALI et la surcharge. "
          "La fièvre non hémolytique est un diagnostic d'élimination.", 2),
        P(noms, 1),
    ] + geste_immediat()))
    c[5] = (ile_court("Ce que l'on demande", "Grossesse, transfusions, anticorps déjà écrits, médicaments, tolérance du volume."), H([
        P("On demande les transfusions anciennes, les grossesses, les fausses couches, les interruptions, une injection d'anti-D, la date, et si une carte de groupe existe. "
          "Un anti-D connu immun interdit la prophylaxie. Un anti-D dont on ne sait pas s'il est passif ne l'interdit pas, selon le guide de 2014.", 8),
        P("On demande la tolérance à l'effort, une insuffisance cardiaque, une sténose aortique, une insuffisance rénale, un bilan des entrées et sorties. "
          "Ce sont les terrains de la surcharge. On demande une allergie connue, un déficit en immunoglobuline A, un bêtabloquant qui peut freiner l'adrénaline.", 2),
        P("Drapeaux : douleur au point d'injection, lombes, urines foncées, chute de tension, fièvre qui monte, dyspnée, stridor, dans les minutes ou les heures. "
          "Chez le nouveau-né : ictère précoce, pâleur, hémoglobine basse, mère O et enfant A ou B, ou mère RhD négatif avec anti-D.", 2),
        *lit_et_surveillance()[:2],
        *phase_extra(),
    ]))
    c[6] = (ile_court("Au lit du malade", "Identité, carte, poche, constantes les 15 premières minutes."), H(lit_et_surveillance() + [
        P("Examen si réaction : tension, pouls, fréquence respiratoire, saturation, température, couleur des urines, point de ponction, auscultation, recherche d'urticaire et de stridor. "
          "On ne quitte pas le patient pendant le premier quart d'heure.", 3),
        schema_compatibilite(),
    ]))
    c[7] = (ile_court("Cinq tableaux", "Hémolyse aiguë, hémolyse retardée, surcharge, atteinte pulmonaire, allergie. La fièvre seule n'en est pas un."), H([
        P("Hémolyse aiguë : pendant ou dans les 24 heures, souvent avant 90 minutes, douleur, fièvre, chute de tension, urines foncées, Coombs direct positif, hémolyse biologique.", 2),
        P("Hémolyse retardée : entre le jour 1 et le jour 28, ictère, chute d'hémoglobine inexpliquée, Coombs direct, anticorps qui peut manquer sur le bilan d'avant, surtout Kidd.", 2),
        P("Surcharge : dans les 6 heures, au moins quatre signes de la liste, hypertension plutôt que choc, œdème pulmonaire, peptide qui monte sans seuil chiffré imposé.", 2),
        P("TRALI : dans les 6 heures, hypoxémie, infiltrats bilatéraux, pas de surcharge gauche. Probable ou possible selon les autres risques pulmonaires. Deux mécanismes, immun et non immun.", 2),
        P("Allergie : peau seule, ou un autre organe, ou choc. L'anaphylaxie ne se discute pas sur la tryptase avant d'injecter l'adrénaline.", 5),
        P("Maladie du nouveau-né : ABO, souvent mère O et enfant A ou B, en général plus modérée que l'anti-D, ou anti-D chez une mère négative immunisée, ou un autre irrégulier, Kell en particulier.", 4),
    ] + autres_cases()[:4]))
    c[8] = (ile_court("Ce qui confirme", "Coombs direct, anticorps, et la case exacte de l'aide-mémoire, pas un synonyme."), H(
        bilan_hemolyse() + rtfnh()[:2] + allergie()[:2] + trali()[:3] + taco()[:2] + allo()[:2]
    ))
    c[9] = (ile_court("Examens", "Groupe, recherche d'anticorps, compatibilité, Coombs, Kleihauer, et le bilan en quatre volets si réaction."), H([
        P("Avant de transfuser des globules : groupe ABO et RhD, recherche d'anticorps irréguliers, compatibilité ou procédure de type and screen selon la directive du lieu, "
          "dans le délai que cette directive a fixé. À Genève, 96 heures. Ailleurs, le délai écrit localement, pas un chiffre national inventé.", 9),
        P("Au lit : concordance pour tout produit, carte ABO pour les globules seulement, lecture des négatifs jusqu'à 3 minutes, par la personne qui pose la transfusion.", 9),
        *bilan_hemolyse()[4:6],
        P("Kleihauer-Betke ou cytométrie si le passage fœtal peut dépasser 4 ml d'hématies RhD positif. Le seuil et la dose supplémentaire sont ceux de l'information 53609.", 4),
        schema_algorithme(),
    ]))
    c[10] = (ile_court("Arbre", "Arrêt, voie, identité, bilan, puis la branche du tableau, puis la déclaration."), H(
        geste_immediat() + [
            schema_algorithme(),
            P("Branche hémolyse aiguë : ne pas relancer la poche, ne pas donner le concentré suivant, prévenir la banque pour bloquer les autres poches du même prélèvement si une confusion est possible.", 1),
            P("Branche surcharge : ralentir était le geste d'avant les signes. Une fois les quatre signes là, on arrête, on oxygène, on discute le diurétique de l'information 30630.", 6),
            P("Branche TRALI : on arrête, on oxygène, on ne débute pas par le furosémide.", 2),
            P("Branche anaphylaxie : adrénaline intramusculaire immédiate, numéro 56551, puis le reste.", 5),
        ]
    ))
    c[11] = (ile_court("En Suisse", "Doses de Rhophylac 53609, adrénaline 56551, furosémide 30630, clémastine 35501. Déclaration à Swissmedic."), H(
        antid() + allergie()[4:] + taco()[3:4] + [
            P("Toute réaction se déclare selon le circuit interne puis Swissmedic. L'erreur ABO se déclare comme incident grave même si l'on a arrêté à 25 ml, comme dans le cas de 2024.", 1),
        ]
    ))
    c[12] = (ile_court("Prévenir", "Deux contrôles, carte au lit, anti-D à 28-30 semaines et dans les 72 heures, transfusion lente si le cœur est limite."), H([
        P("La prévention de l'incompatibilité ABO est administrative autant que biologique : identité, deux contrôles, carte pour les globules, jamais de transfusion sur une discordance.", 3),
        P("La prévention de l'anti-D est la seringue de 300 µg entre 28 et 30 semaines et dans les 72 heures après un événement ou un accouchement d'enfant RhD positif, plus Kleihauer si le volume peut dépasser 4 ml.", 4),
        P("La prévention de la surcharge est l'évaluation du risque et, si le rapport 2024 est suivi, une transfusion lente, exemple 1 ml par kilogramme et par heure, et l'idée d'un diurétique préventif sans dose inventée hors information.", 1),
        P("La prévention du TRALI immun relève des donneurs et du choix des produits, pas d'un médicament au lit. Au lit, on reconnaît les 6 heures et on n'ajoute pas de volume.", 2),
        P("On ne transfuse pas la nuit si l'on peut attendre. On finit dans les six heures après l'ouverture. On ne réchauffe pas à la main.", 3),
    ]))
    c[13] = (ile_court("À retenir", "Listes entières, deux seuils de fièvre, deux tableaux ABO, anti-D suisse et non le minimum britannique."), H([
        P("Receveur universel de globules : AB. Donneur universel de globules, au sens des antigènes A et B : O. Donneur universel de plasma : AB. Plasma O : seulement vers O. "
          "Urgence sans groupe : concentré O RhD négatif, pas plasma O.", 9),
        P("Aigu : 24 heures, médiane 90 minutes. Retardé : jour 1 à jour 28. Fébrile non hémolytique : 4 à 6 heures, fièvre supérieure à 38 °C et au moins 1 °C. "
          "Grade sévère par la fièvre : supérieure à 39 °C et plus de 2 °C. Surcharge et TRALI : 6 heures. Hypotension isolée : 30 mm Hg, dans l'heure.", 2),
        P("Anti-D suisse : 300 µg, 1500 UI, semaines 28 à 30, 72 heures, Kleihauer au-dessus de 4 ml, 10 µg soit 50 UI par 0,5 ml d'hématies fœtales, plafond usuel 3'000 µg soit 15'000 UI.", 4),
        P("Adrénaline intramusculaire : 0,5 mg au-dessus de 12 ans, 0,3 mg de 6 à 12 ans, 0,15 mg de 6 mois à 6 ans, 0,01 mg/kg avant 6 mois. Cuisse. Pas la fesse. Pas le 1 mg/ml en intraveineux pur.", 5),
        P("Furosémide si surcharge : 20 à 40 mg, et 40 mg d'emblée si œdème pulmonaire aigu. Pas ce schéma pour le TRALI ni comme réflexe de l'hémolyse ABO.", 6),
        *classification_complete()[:4],
    ]))
    c[14] = (ile_court("Pièges", "Finir la poche, diurétique dans l'ABO, anti-D chez une femme déjà immunisée, carte sur du plasma, confondre 38 °C et 39 °C."), H([
        P("Piège 1. Continuer la transfusion parce que la fièvre est petite. On arrête, on bilanise, on nomme après.", 2),
        P("Piège 2. Donner du furosémide à toute réaction. Le cas 2024 montre le risque sur une sténose aortique. Le TRALI n'est pas une surcharge.", 1),
        P("Piège 3. Traiter un choc allergique par la clémastine seule. L'adrénaline est le premier geste, numéro 56551.", 5),
        P("Piège 4. Injecter 300 µg à une femme qui a déjà un anti-D immun. Le produit n'est pas fait pour cela. Si l'on ne sait pas séparer passif et immun, on continue, dit le guide 2014.", 4),
        P("Piège 5. Utiliser la carte genevoise pour du plasma ou des plaquettes, ou s'en servir pour déterminer le groupe. Elle vérifie une compatibilité de globules, lecture jusqu'à 3 minutes.", 9),
        P("Piège 6. Appliquer le minimum britannique de 250 ou 500 unités internationales à la place de la seringue suisse de 300 µg. En Suisse, l'information 53609 commande.", 8),
        P("Piège 7. Appeler fébrile non hémolytique une fièvre supérieure à 39 °C avec 2 °C de hausse sans avoir exclu l'hémolyse et la bactérie. Ce chiffre force le grade, il ne nomme pas la cause.", 1),
        P("Question. Receveuse O, concentré A, 25 ml, arrêt immédiat, pas de changement des constantes. Que fait-on du diurétique ? "
          "Réponse. On ne le donne pas pour l'incompatibilité. On fait le bilan d'hémolyse sur un tube non hémolysé, on regarde les urines, on soutient selon la tension et le rein, on déclare. "
          "Le rapport 2024 laisse ouverte la part du diurétique dans l'aggravation respiratoire.", 1),
        P("Question. Femme RhD négatif, 29 semaines, pas d'anti-D immun, pas encore de prophylaxie. Quelle seringue, quel délai si elle saigne ? "
          "Réponse. 300 µg, soit 1500 UI, numéro 53609, le plus vite possible et dans les 72 heures, puis toutes les 12 semaines jusqu'à l'accouchement si la complication le demande, "
          "et Kleihauer si le passage peut dépasser 4 ml.", 4),
        P("Question. Dyspnée à la deuxième heure, saturation basse, radiographie bilatérale, pas d'hypertension, peptide non demandé. "
          "Réponse. On n'a pas quatre signes de surcharge. On garde le TRALI dans la liste, probable ou possible selon les autres risques pulmonaires, on oxygène, on ne commence pas par 40 mg de furosémide.", 2),
    ]))
    return c, essentiels


def bloc_dx(n, nom, specifique, extra_fin=""):
    """specifique : dict point -> list of tuples already, or we wrap."""
    ligne = specifique.get("ligne", "Voir la fenêtre.")
    ile = ile_court(nom, ligne)
    c = {}
    for i in range(1, 15):
        corps = specifique[i]
        if extra_fin and i in (8, 11, 13, 14):
            corps = corps + [P(extra_fin)]
        c[i] = (ile, H(corps))
    return c


def commun_autour(nom):
    """Rappels courts propres au DX, pas la copie de toute la phase A."""
    return [
        P(f"Pour {nom}, on garde les voisins dans la tête : hémolyse aiguë, hémolyse retardée, fièvre non hémolytique, allergie, surcharge, TRALI, "
          "allo-immunisation sans hémolyse, maladie du nouveau-né ABO, maladie du nouveau-né par anti-D, incompatibilité du plasma ou des plaquettes. "
          "On n'efface pas une case pour faire tenir le diagnostic préféré.", 2),
    ]


def dx_pages():
    pages = []
    # Each entry builds 14 lists
    builders = [dx1, dx2, dx3, dx4, dx5, dx6, dx7, dx8, dx9, dx10]
    for b in builders:
        pages.append(b())
    return pages


def enveloppe(nom, coeur, plus):
    """coeur: list used in several places with a different first sentence. plus: dict of extra lists per point."""
    base = {
        1: [P(f"{nom} se définit par les critères cités plus loin, pas par un malaise vague pendant une poche.", 2)] + coeur[:2] + commun_autour(nom),
        2: [P(f"La place de {nom} dans les déclarations suisses se lit dans le rapport 2024, sans inventer une incidence de cabinet.", 1)] + coeur[:1],
        3: [P(f"Le mécanisme de {nom} relie un antigène, un anticorps, ou un volume, au signe que l'on voit.", 2)] + coeur,
        4: [P("Étape une : arrêter si une poche coule et qu'un signe apparaît. Étape deux : identité et documents. Étape trois : le bilan qui correspond. Étape quatre : nommer la case.", 3)] + coeur[:3],
        5: [P("On cherche une transfusion, une grossesse, un anticorps déjà rendu, un cœur limite, une allergie, un bêtabloquant.", 2)] + coeur[:2],
        6: [P("Constantes, urines, peau, poumon, point de ponction. Les 15 premières minutes sont les plus étroites.", 3)] + coeur[:2],
        7: commun_autour(nom) + coeur[:2],
        8: coeur,
        9: [P("Le laboratoire ne remplace pas l'arrêt de la poche. Il confirme ou il écarte.", 2)] + coeur[:4],
        10: geste_immediat()[:2] + coeur[:2],
        11: coeur,
        12: [P(f"Prévenir {nom}, c'est empêcher la rencontre ou reconnaître le terrain avant la poche.", 3)] + coeur[:2],
        13: coeur[:4],
        14: coeur[:3] + [P(f"Question de dossier sur {nom}. On écrit le critère, le délai et le geste, pas un synonyme.", 2)],
    }
    for k, v in plus.items():
        base[k] = base.get(k, []) + v
    # ligne courte pour l'île
    return base


def dx1():
    nom = DX[0]
    coeur = allo() + [
        P("Kell, Duffy et Kidd ne sont pas interchangeables. Kell menace le fœtus par l'érythropoïèse. Duffy, anti-Fya surtout, menace la transfusion et le nouveau-né. "
          "Kidd se cache entre les bilans et revient après le concentré. Un compte rendu qui dit anticorps irrégulier sans le nom est incomplet.", 2),
        P("Sans hémolyse, on reste dans l'allo-immunisation. Avec chute d'hémoglobine, ictère ou Coombs direct positif dans les 28 jours, on passe à la réaction retardée. "
          "Avec des signes dans les 24 heures, on passe à l'aiguë jusqu'à preuve du contraire.", 2),
        P("La femme en âge de procréer et la fille reçoivent, si l'on peut, des globules compatibles pour K et pour les antigènes contre lesquels elles pourraient s'immuniser. "
          "Le choix fin est celui de la banque. Le clinicien, lui, transmet les grossesses et les anticorps anciens par écrit, comme le demande le guide 2026.", 3),
        P("Cas. Femme de 34 ans, deuxième grossesse, recherche positive anti-K, pas d'hémolyse, pas de transfusion récente. "
          "Ce n'est pas une réaction fébrile. Ce n'est pas une prophylaxie anti-D. L'anti-K se suit comme un anticorps dangereux pour le fœtus, pas comme un titre que l'on peut ignorer parce qu'il est bas. "
          "On ne donne pas Rhophylac pour un anti-K : la seringue est anti-D.", 4),
        P("Cas. Homme de 62 ans, concentré il y a 10 jours, recherche négative avant, aujourd'hui anti-Jka et hémoglobine en baisse, Coombs direct positif. "
          "La case n'est plus l'allo-immunisation sans hémolyse. C'est la réaction retardée. L'élution a un sens.", 2),
    ]
    plus = {
        8: allo(),
        11: [P("Pas de dose d'anti-D pour un anti-K ou un anti-Jka. La dose 300 µg ne couvre que l'antigène D.", 4)],
        14: [
            P("Piège. Rendre un Kidd négatif aujourd'hui comme une autorisation à vie. L'anticorps peut être sous le seuil de détection et revenir après le prochain concentré.", 2),
            P("Piège. Classer toute recherche positive en réaction hémolytique. Sans signe ni biologie d'hémolyse, l'aide-mémoire dit allo-immunisation.", 2),
            P("Question. 1519 déclarations en 2024, toutes grade 2. Pourquoi pas grade 1 ? Réponse. Le rapport place l'allo-immunisation dans ce qui est au minimum sévère, même sans symptôme ce jour-là.", 1),
        ],
    }
    d = enveloppe(nom, coeur, plus)
    d["ligne"] = "Anticorps apparu ou redevenu visible, sans hémolyse. Kell, Duffy et Kidd ne se résument pas l'un à l'autre."
    return nom, d


def dx2():
    nom = DX[1]
    coeur = rtfnh() + [
        P("Le mécanisme le plus cité est celui des cytokines du produit ou des anticorps contre les leucocytes, sans destruction des globules. "
          "L'aide-mémoire rappelle que des mécanismes non immunologiques sont aussi discutés. On n'a pas besoin du mécanisme pour appliquer le bilan : tant que l'hémolyse et la bactérie ne sont pas écartées, le nom est prématuré.", 2),
        P("Conduite. On arrête. On revérifie l'identité. On envoie le bilan en quatre volets. Si tout est négatif et que les signes sont ceux de la liste, dans les 4 à 6 heures, on peut nommer la réaction fébrile non hémolytique. "
          "On ne reprend pas la même poche. Une poche suivante ne se décide qu'après ce tri, et avec une surveillance.", 2),
        P("Cas. Femme de 45 ans, concentré pour anémie chronique, frissons à la fin de la poche, 37,6 °C avant, 38,7 °C après. Pas de douleur lombaire, urines claires, tension tenue. "
          "La hausse dépasse 1 °C et la fièvre dépasse 38 °C : la définition est remplie si le reste du bilan est négatif. "
          "Elle ne dépasse pas 39 °C avec plus de 2 °C : le critère qui force le grade sévère par la fièvre seule n'est pas là. On fait quand même le bilan, parce que la définition l'exige.", 2),
        P("Cas voisin. Même femme, 38,4 °C avant, 40,6 °C après, frissons, tension qui baisse. Là, la fièvre force au moins le grade 2, et le tableau peut être une bactérie ou une hémolyse. "
          "Appeler cela une réaction fébrile bénigne est la copie fausse.", 1),
    ]
    plus = {8: rtfnh(), 14: [
        P("Piège. Traiter par paracétamol et finir la poche sans tube. L'aide-mémoire veut les cultures et l'hémolyse.", 2),
        P("Question. Délai médian ? Réponse. 80 minutes, fenêtre de définition 4 à 6 heures, souvent en fin de poche.", 2),
    ]}
    d = enveloppe(nom, coeur, plus)
    d["ligne"] = "Fièvre ou frissons dans les 4 à 6 heures, hémolyse et bactérie écartées. Seuil 38 °C et 1 °C, distinct de 39 °C et 2 °C."
    return nom, d


def dx3():
    nom = DX[2]
    coeur = allergie() + [
        P("Une urticaire limitée peut relever d'un protocole local qui décide d'interrompre puis de reprendre, le guide 2026 laisse cette décision au système qualité. "
          "Dès qu'il y a stridor, bronchospasme, chute de tension ou choc, on arrête définitivement cette poche et l'adrénaline passe avant le débat.", 3),
        P("Cas. Homme de 28 ans, plaquettes, prurit et quelques papules à la 20e minute, tension et saturation normales. "
          "C'est la case légère si rien d'autre n'apparaît. Pas de tryptase obligatoire. On surveille, on ne déclare pas un choc. "
          "On n'utilise pas la carte ABO : les plaquettes ne passent pas par la safety-card genevoise.", 9),
        P("Cas. Femme de 60 ans sous bêtabloquant, plasma, stridor et tension à 70 mm Hg à la 10e minute. "
          "Anaphylaxie. Adrénaline 0,5 mg intramusculaire dans la cuisse, numéro 56551, répétée selon la tension, le pouls et la respiration. "
          "Le bêtabloquant peut rendre la réponse incomplète : ce n'est pas une raison d'attendre. La clémastine, 2 mg, vient après. "
          "On cherchera plus tard le déficit en immunoglobuline A si l'épisode est sévère ou s'il se répète.", 5),
    ]
    plus = {8: allergie()[:3], 11: allergie()[4:], 14: [
        P("Piège. Diluer l'adrénaline à 1 mg/ml et la pousser en intraveineux dans le service sans en avoir l'habitude. L'information l'interdit sous cette forme.", 5),
        P("Piège. Oublier une ligne du tableau d'âge. Les quatre lignes, plus de 12 ans, 6 à 12 ans, 6 mois à 6 ans, moins de 6 mois, vont ensemble.", 5),
    ]}
    d = enveloppe(nom, coeur, plus)
    d["ligne"] = "Peau, ou un autre organe, ou choc. Adrénaline d'abord si le pronostic vital est en jeu."
    return nom, d


def dx4():
    nom = DX[3]
    coeur = [
        P("La maladie hémolytique du nouveau-né par incompatibilité ABO survient quand des anticorps maternels anti-A ou anti-B, souvent chez une mère de groupe O, traversent le placenta et reconnaissent les globules A ou B de l'enfant. "
          "Une partie de ces anticorps est de classe G, donc capable de passer, alors que l'anti-A et l'anti-B classiques du receveur adulte sont surtout de classe M. "
          "L'hémolyse est en général plus modérée que celle de l'anti-D, mais elle peut ictérer tôt, dès les premières 24 heures, et elle peut demander une photothérapie.", 4),
        P("Le test de Coombs direct sur le sang du cordon peut être positif, faiblement. Le guide britannique de 2014 rappelle qu'un Coombs direct de cordon peut aussi être positif à cause d'une prophylaxie anti-D : "
          "dans l'incompatibilité ABO, la mère est souvent RhD positif ou l'anti-D n'est pas en cause, et le groupe de l'enfant est A ou B avec une mère O. "
          "On ne conclut pas sur le Coombs seul.", 8),
        P("Ce n'est pas une indication de Rhophylac. La seringue anti-D ne neutralise pas l'anti-A ni l'anti-B. "
          "Donner 300 µg pour un ictère ABO est une erreur de produit.", 4),
        P("Démarche. Groupe de la mère et de l'enfant, Coombs direct chez l'enfant, bilirubinémie, hémoglobine, et recherche de l'heure de début de l'ictère. "
          "Un ictère des premières 24 heures n'est pas un ictère simple du troisième jour. On écarte aussi une hémolyse par anti-D ou par Kell si la recherche maternelle est positive.", 2),
        P("Cas. Mère O, RhD positif, enfant A, RhD positif, ictère à 18 heures, Coombs direct faiblement positif, mère sans anticorps irrégulier. "
          "Lecture : incompatibilité ABO. Geste : surveillance de la bilirubine et photothérapie selon le protocole néonatal du lieu, pas d'anti-D, pas de concentré O négatif systématique. "
          "La copie est fausse si l'on écrit prophylaxie anti-D de la mère le lendemain : elle est RhD positif, et l'enfant aussi.", 4),
        P("Piège de sévérité. La forme ABO est souvent modérée, elle n'est pas toujours bénigne. Une anémie franche ou un ictère très haut se prend en charge comme une hémolyse du nouveau-né, "
          "avec le néonatologiste, sans attendre que le nom ABO rassure.", 2),
        P("Différentiel. Anti-D, anti-K, hématome, infection, déficit enzymatique. Le groupe O maternel et A ou B de l'enfant oriente, il ne ferme pas la liste si un irrégulier est présent.", 2),
    ]
    plus = {8: coeur[:4], 14: [
        P("Question. Pourquoi la mère O est-elle le terrain classique ? Réponse. Elle a anti-A et anti-B, et une fraction immunoglobuline G peut passer le placenta vers un enfant A ou B. "
          "Une mère AB n'a pas ces anticorps naturels.", 2),
        P("Question. La carte au lit a-t-elle une place ici ? Réponse. Non pour le diagnostic du nouveau-né. La carte genevoise ne détermine pas un groupe et ne s'utilise pas comme test de la mère.", 9),
    ]}
    d = enveloppe(nom, coeur, plus)
    d["ligne"] = "Mère O, enfant A ou B, ictère précoce possible. Pas une indication d'anti-D."
    return nom, d


def dx5():
    nom = DX[4]
    coeur = taco() + [
        P("Physiopathologie : le volume transfusé dépasse ce que le cœur gauche peut éjecter. La pression capillaire monte, l'eau passe dans l'alvéole. "
          "D'où l'hypertension, l'œdème radiologique et la réponse possible au diurétique. Ce n'est pas une lésion des capillaires par un anticorps leucocytaire, qui est le TRALI immun.", 2),
        P("Cas. Homme de 78 ans, fraction d'éjection basse, deux concentrés prévus, dyspnée et hypertension à 190 mm Hg après 400 ml, crépitants, radiographie nouvelle, bilan d'entrées positif, toux. "
          "Quatre signes au moins : détresse, hypertension, œdème radiologique, bilan positif, et la toux dans les autres signes. Délai dans les 6 heures. "
          "On arrête. Oxygène. Lasix, œdème pulmonaire aigu : 40 mg intraveineux, numéro 30630, puis 20 à 40 mg à 20 minutes si besoin. On déclare.", 6),
        P("On n'attend pas six heures pour agir. Six heures est la fenêtre de définition, le délai médian est 90 minutes. "
          "Une dyspnée à la dixième minute peut déjà être une surcharge si les autres signes sont là, ou une allergie, ou un TRALI. On les départage.", 2),
    ]
    plus = {8: taco()[:3], 11: taco()[3:], 14: [
        P("Piège. Compter la fièvre, présente dans environ 30 % des surcharges, comme la preuve d'une réaction fébrile et continuer le volume.", 2),
        P("Piège. Poser 1 mg par kilogramme chez un adulte parce que c'est la dose de l'enfant. Chez l'adulte, l'information commence à 20 à 40 mg. Le 1 mg par kilogramme est la dose de l'enfant de moins de 15 ans, plafond 20 mg par jour.", 6),
    ]}
    d = enveloppe(nom, coeur, plus)
    d["ligne"] = "Au moins quatre signes dans les 6 heures. Diurétique selon Lasix 30630, pas selon une habitude."
    return nom, d


def dx6():
    nom = DX[5]
    coeur = [
        P("La réaction hémolytique retardée est la destruction accélérée des globules transfusés entre le jour 1 et le jour 28, le plus souvent hors du vaisseau, "
          "par un anticorps irrégulier qui était trop faible pour être vu avant, ou qui n'était plus détectable. Kidd est le modèle, Duffy et d'autres spécificités le font aussi. "
          "L'aide-mémoire ne limite pas la case à un seul antigène.", 2),
        *bilan_hemolyse()[:6],
        P("Ce qui la sépare de l'allo-immunisation : il y a une hémolyse clinique ou biologique. Ce qui la sépare de l'aiguë ABO : le délai dépasse 24 heures, le tableau est souvent un ictère et une anémie plutôt qu'un choc à la 90e minute, "
          "et le groupe ABO de la poche était compatible. Une ABO peut quand même être méconnue si peu de volume a coulé et que les signes ont été manqués : on revérifie les documents quand même.", 2),
        P("Cas. Femme de 51 ans, deux concentrés il y a neuf jours pour une chirurgie, recherche négative ce jour-là, aujourd'hui fatigue, ictère, hémoglobine revenue au-dessous du chiffre d'après transfusion, "
          "Coombs direct positif, élution anti-Jka. Recherche actuelle positive. "
          "Conduite : on ne retransfuse pas à l'aveugle. La banque choisit des globules Jka négatif, compatibles. On déclare une réaction hémolytique retardée. "
          "On ne donne pas d'anti-D s'il n'y a pas d'exposition D. On ne donne pas 40 mg de furosémide pour faire passer l'ictère.", 2),
        P("Piège du tube hémolysé. Dans le décès ABO de 2024, lactate déshydrogénase et haptoglobine étaient illisibles. "
          "Pour une suspicion retardée, on prélève un tube correct, on regarde le plasma à l'œil, on demande l'urine. Un bilan ininterprétable n'est pas un bilan négatif.", 1),
    ]
    plus = {8: bilan_hemolyse(), 14: [
        P("Question. Fenêtre ? Réponse. De 1 à 28 jours. La médiane de 90 minutes appartient à l'aiguë, pas à cette case.", 2),
        P("Question. Recherche négative avant la transfusion. Est-ce que cela innocente la poche ? Réponse. Non. Un Kidd peut être invisible ce jour-là et démontrable après, par le plasma ou par l'élution.", 2),
    ]}
    d = enveloppe(nom, coeur, plus)
    d["ligne"] = "Hémolyse entre le jour 1 et le jour 28. Kidd se cache. Coombs direct et élution."
    return nom, d


def dx7():
    nom = DX[6]
    coeur = antid() + [
        P("La maladie hémolytique par anti-D est l'hémolyse du fœtus ou du nouveau-né dont la mère RhD négatif s'est immunisée et dont l'enfant est RhD positif. "
          "L'immunoglobuline G maternelle passe le placenta, se fixe sur les globules fœtaux, le Coombs direct de l'enfant est positif, l'anémie et l'ictère suivent. "
          "Sans prophylaxie, les grossesses suivantes sont plus sévères. Avec la prophylaxie lue, 90 % des sensibilisations du post-partum sont prévenues, jusqu'à 99 % si l'on ajoute l'injection prénatale.", 4),
        P("On distingue l'anti-D immun, qui est la maladie, et l'anti-D passif, qui est la seringue encore détectable. Aucun test sérologique simple ne les sépare, dit le guide 2014. "
          "Dans le doute, on continue la prophylaxie. On n'arrête pas les 300 µg sur un anti-D faible dont l'histoire est floue. "
          "On les arrête si l'immunisation est établie : le produit n'est pas destiné à une personne déjà immunisée, et il ne traite pas le fœtus déjà atteint.", 8),
        P("Suivi. Une femme immunisée ne reçoit pas la prophylaxie, elle reçoit le suivi de la grossesse : titres, et les examens fœtaux que l'obstétrique décide. "
          "Ce cours ne fabrique pas un titre seuil qui ne figure pas dans les pièces lues. Il retient que l'anti-D immun n'est pas une seringue, et que l'anti-K, voisin, n'obéit pas non plus à un titre rassurant inventé.", 8),
        P("Cas. Femme RhD négatif, 28 semaines exactement, pas d'anticorps sur le tube pris avant l'injection. On donne 300 µg, 1500 UI, numéro 53609, veine ou muscle. "
          "Le tube se prend avant, pas après : sinon l'anti-D passif brouille le dépistage. "
          "À la naissance, enfant RhD positif : encore 300 µg dans les 72 heures, et Kleihauer. Si le test montre plus de 4 ml d'hématies fœtales, on ajoute 10 µg, soit 50 UI, par 0,5 ml.", 4),
        P("Cas d'échec de délai. Saignement à 32 semaines, injection seulement au jour 5. L'information suisse dit : passé 72 heures, on injecte quand même le plus vite possible. "
          "Le guide 2014 ajoute qu'une protection partielle peut exister jusqu'à 10 jours. On ne renonce pas parce que le calendrier est dépassé. On ne promet pas non plus la même efficacité.", 8),
        P("Nouveau-né. Ictère, anémie, mère RhD négatif, anti-D immun connu, enfant RhD positif, Coombs direct positif. "
          "Ce n'est pas la forme ABO. La photothérapie ou l'exsanguino-transfusion relèvent du néonatologiste. "
          "Le réchauffement d'un produit à 37 °C, si une exsanguino-transfusion est décidée, se fait avec un appareil prévu, dit le guide 2026, pas avec de l'eau chaude de fortune.", 3),
    ]
    plus = {14: [
        P("Piège. Oublier le Kleihauer après un accouchement ou un traumatisme et se contenter de la seringue standard alors que le passage dépasse 4 ml.", 4),
        P("Piège. Confondre D partiel et personne déjà immunisée. Le D partiel entre dans l'indication de prophylaxie. L'immunisation établie en sort.", 4),
        P("Question. Plafond après une grosse transfusion RhD positif chez une fille négative ? "
          "Réponse. On calcule 10 µg par 0,5 ml de concentré. Une dose totale de 3'000 µg, soit 15'000 UI, suffit même au-delà de 150 ml de concentré, et l'on ne dépasse en général pas ce plafond, risque d'hémolyse, surveillance clinique et biologique.", 4),
    ]}
    d = enveloppe(nom, coeur, plus)
    d["ligne"] = "Anti-D immun maternel, enfant RhD positif. La prévention est 300 µg, pas le minimum britannique."
    return nom, d


def dx8():
    nom = DX[7]
    coeur = phrases_matrice()[:8] + [
        P("Incompatibilité plasmatique : le donneur apporte l'anticorps, le receveur apporte l'antigène. "
          "Plasma O vers A, B ou AB est incompatible. Plasma AB vers tous est compatible. "
          "Un concentré plaquettaire suspendu dans du plasma pose le même problème s'il est de groupe O et riche en anti-A ou anti-B, chez un receveur non O : "
          "l'hémolyse est alors celle des globules du receveur, pas celle d'un concentré érythrocytaire mal choisi. "
          "Le volume exact d'hématies résiduelles dans une poche de plaquettes n'est pas dans les pièces lues : on ne l'invente pas. "
          "Si ces hématies sont RhD positif et la receveuse RhD négatif, l'information 53609 couvre les produits qui contiennent des hématies RhD positif, et la dose se calcule sur le volume d'hématies, avec le spécialiste si besoin.", 4),
        P("Les plaquettes portent aussi des antigènes ABO. Le receveur qui a l'anticorps correspondant peut détruire une partie des plaquettes et le rendement baisse. "
          "Ce n'est pas la même chose qu'une hémolyse des globules. L'isogroupe est préférable. Un écart se décide avec la banque, pas avec le tableau des globules copié à l'envers.", 2),
        P("La carte genevoise ne se fait pas sur le plasma ni sur les plaquettes. La concordance documentaire, elle, se fait sur tout produit, urgence comprise.", 9),
        P("Cas. Receveur A, plasma O proposé par erreur de lecture. On ne transfuse pas. Le plasma O contient anti-A et anti-B. "
          "Le plasma compatible est A ou AB. Les globules O, eux, auraient été compatibles : c'est l'inversion des tableaux qui crée l'erreur.", 2),
        P("Cas. Jeune fille B, RhD négatif, plaquettes O RhD positif en rupture de stock. On vérifie avec la banque le titre des anticorps du donneur si la procédure locale le demande, "
          "on surveille l'hémolyse, et l'on discute une prophylaxie anti-D selon le volume d'hématies réellement présent, dose de l'information 53609, pas une seringue automatique sans calcul si le volume est connu, "
          "et 300 µg supplémentaires si le passage ou le volume ne peut pas être mesuré dans les situations où l'information le dit. "
          "Pour une transfusion de produit contenant des hématies, la règle chiffrée reste 10 µg pour 0,5 ml.", 4),
        P("Hémolyse mineure, celle du plasma du donneur, peut être aiguë et entrer dans la réaction hémolytique des 24 heures. "
          "Elle se bilanise comme telle : Coombs direct, hémolyse, documents. Elle ne se classe pas en allergie parce que le produit était du plasma.", 2),
    ]
    plus = {3: phrases_matrice(), 8: phrases_matrice()[-6:], 14: [
        P("Piège. Appeler le groupe O donneur universel sans dire de quoi. Universel pour les globules, dangereux pour le plasma.", 9),
        P("Question. Receveur universel de globules ? Réponse. AB. Donneur universel de plasma ? Réponse. AB. Concentré d'extrême urgence ? O RhD négatif.", 9),
    ]}
    d = enveloppe(nom, coeur, plus)
    d["ligne"] = "L'anticorps voyage dans le plasma. AB donne du plasma à tous. O ne donne son plasma qu'à O."
    return nom, d


def dx9():
    nom = DX[8]
    coeur = bilan_hemolyse() + geste_immediat() + [
        P("L'incompatibilité ABO aiguë est presque toujours une erreur d'identité : mauvais tube, mauvaise poche, mauvais patient. "
          "Les anticorps naturels sont déjà là. Quelques millilitres suffisent. Le cas 2024 a été arrêté vers 25 ml et a quand même été classé hémolyse aiguë de grade 4, imputabilité possible, "
          "chez une femme de plus de 80 ans avec hémoglobine inférieure à 70 g/l avant la transfusion, sténose aortique et insuffisance rénale.", 1),
        P("Physiopathologie : anti-A ou anti-B, souvent immunoglobuline M, fixe le complément, lyse les globules dans le vaisseau, hémoglobine libre, haptoglobine consommée, "
          "rein et coagulation peuvent suivre. Douleur au point d'injection et dans les lombes, fièvre, chute de tension, urines foncées. "
          "La médiane de début est 90 minutes, la fenêtre va jusqu'à 24 heures.", 2),
        P("Conduite, dans l'ordre. Arrêt immédiat. Voie veineuse gardée, rien dans la poche. Identité et numéro. Médecin et laboratoire. "
          "Bilan en quatre volets sur un tube non hémolysé, urine comprise. Soutien de la tension par le remplissage si elle tombe. "
          "On ne commence pas par le furosémide. On ne relance pas un autre concentré tant que la banque n'a pas revu le groupe. On déclare l'incident et la réaction.", 3),
        P("Cas d'examen. Receveuse O, poche A, douleur lombaire à la dixième minute. "
          "La copie juste : arrêt, voie, bilan, déclaration, pas de diurétique systématique, pas de reprise. "
          "La copie fausse : ralentir et finir, ou donner 40 mg de Lasix parce qu'une dyspnée pourrait venir, ou appeler cela une réaction fébrile.", 6),
        schema_algorithme(),
    ]
    plus = {8: bilan_hemolyse(), 10: [schema_algorithme()] + geste_immediat(), 11: geste_immediat(), 14: [
        P("Question. Le Coombs direct est négatif et le plasma du tube est rouge parce que le prélèvement est raté. Que vaut ce bilan ? "
          "Réponse. Il ne confirme ni n'infirme. On reprend un tube. Le cas 2024 a perdu lactate déshydrogénase et haptoglobine pour cette raison.", 1),
        P("Question. Faut-il un concentré O RhD négatif pour la suite immédiate si l'anémie est menaçante et le groupe douteux ? "
          "Réponse. Oui si l'on ne peut pas attendre le groupe, c'est le concentré d'extrême urgence du référentiel genevois, avec quand même la carte au lit et la concordance. "
          "On ne compense pas l'erreur par du plasma O.", 9),
    ]}
    d = enveloppe(nom, coeur, plus)
    d["ligne"] = "Dans les 24 heures, souvent vers 90 minutes. Arrêt, voie, bilan, déclaration. Pas de diurétique réflexe."
    return nom, d


def dx10():
    nom = DX[9]
    coeur = trali() + [
        P("On sépare le TRALI de la surcharge par l'absence de surcharge du ventricule gauche, et de l'allergie par l'absence du tableau cutané ou du bronchospasme isolé qui cède à l'adrénaline. "
          "La dyspnée associée à la transfusion est la case restante, dans les 24 heures, quand aucune des trois ne tient. "
          "Oublier cette case-là, ou oublier le TRALI possible chez un patient septique, ampute l'aide-mémoire.", 2),
        P("Cas. Patient de réanimation, pneumonie déjà là, concentré, dans les 3 heures aggravation, saturation inférieure à 90 % à l'air, infiltrats bilatéraux plus étendus, "
          "pas d'hypertension, bilan hydrique pas franchement positif, peptide non contributif. "
          "Il a un facteur de risque d'atteinte pulmonaire, la pneumonie. Si les autres critères sont réunis, l'aide-mémoire permet le TRALI possible, pas seulement le probable. "
          "On oxygène, on ventile si besoin, on ne débute pas par 40 mg de furosémide, on cherche les anticorps du donneur selon le laboratoire, on déclare.", 2),
        P("Cas inverse. Même heure, hypertension, crépitants, radiographie d'œdème, bilan positif, toux. Quatre signes de surcharge. Ce n'est pas le TRALI. Lasix selon l'information 30630.", 6),
        P("Le taux 2024, 0,4 pour 100 000, ne sert pas à écarter le diagnostic au lit. Il sert à savoir que la case est rare et que la surcharge, 14 pour 100 000, est plus souvent déclarée. "
          "La rareté ne remplace pas les critères.", 1),
    ]
    plus = {8: trali(), 11: [
        P("Pas d'adrénaline sans signe anaphylactique. Pas de furosémide comme traitement du TRALI. L'oxygène et le support sont le geste. La déclaration est obligatoire comme pour toute réaction.", 2),
    ], 14: [
        P("Piège. Exiger l'absence de tout facteur de risque pulmonaire pour oser le mot TRALI. Le texte du 9 août 2024 a une case probable et une case possible.", 2),
        P("Piège. Oublier le type non immunogène et ne chercher que les anticorps. Les deux types sont écrits. L'absence d'anticorps ne ferme pas le diagnostic clinique.", 2),
        P("Question. Fenêtre et hypoxémie ? Réponse. Six heures. Rapport au plus 300 mm Hg, ou saturation inférieure à 90 % à l'air ambiant, ou un autre signe d'hypoxémie, plus des infiltrats bilatéraux, sans surcharge gauche.", 2),
    ]}
    d = enveloppe(nom, coeur, plus)
    d["ligne"] = "Dans les 6 heures, hypoxémie, infiltrats bilatéraux, pas de surcharge gauche. Probable ou possible. Pas de diurétique d'abord."
    return nom, d


def materialiser(nom, d, index):
    ligne = d.pop("ligne")
    ile = ile_court(nom, ligne)
    extra = dx_extra(index)
    c = {}
    for i in range(1, 15):
        items = list(d[i]) + extra.get(i, [])
        c[i] = (ile, H(items))
    return c


def main():
    essentiels_a_c, essentiels = page_phase_a()
    # fix: page_phase_a returns c, essentiels
    html_a = page(
        "Incompatibilité de groupe sanguin",
        "Incompatibilité de groupe sanguin",
        "Phase A. F2.17. Systèmes ABO et RhD, anticorps irréguliers, réactions et maladie du nouveau-né. Texte du 31 octobre 2026.",
        essentiels,
        essentiels_a_c,
        "FIN_FICHIER LOT_165_Phase_A_V0.html",
    )
    ecrire("LOT_165_Phase_A_V0.html", html_a)
    print("Phase A écrite", len(html_a))
    for i, (nom, d) in enumerate(dx_pages(), 1):
        ligne = d.get("ligne", "Critères et conduite dans les fenêtres.")
        contenus = materialiser(nom, d, i)
        html_d = page(
            nom,
            nom,
            f"DX.{i}. {nom}. F2.17, incompatibilité de groupe sanguin. Texte du 31 octobre 2026.",
            [
                P(f"{nom}. {ligne}", 2),
                P("Les critères complets, les délais et les doses lues sont dans les fenêtres."),
                P("On n'arrête pas une liste au milieu."),
            ],
            contenus,
            f"FIN_FICHIER LOT_165_Phase_B_V0_DX.{i}.html",
        )
        ecrire(f"LOT_165_Phase_B_V0_DX.{i}.html", html_d)
        print(i, nom, len(html_d))


if __name__ == "__main__":
    main()
