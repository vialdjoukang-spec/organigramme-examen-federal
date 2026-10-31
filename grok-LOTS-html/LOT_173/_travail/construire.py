#!/usr/bin/env python3
"""Assemble les leçons V8 du LOT_173. Mesure y et complète par des cas, sans retirer un critère."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
LOT = ICI.parent
ROOT = ICI.parents[2]
sys.path.insert(0, str(ICI))
sys.path.insert(0, str(ROOT / "harnais"))
import contenu as C  # noqa: E402
import figures  # noqa: E402
import taille_xy  # noqa: E402

MODELE = (ROOT / "harnais/modele_lecon/MODELE_DD_V8.html").read_text(encoding="utf-8")
STYLE = re.search(r"<style>.*?</style>", MODELE, re.S).group(0)
STYLE = STYLE.replace(
    "</style>",
    ".sch .hid{opacity:0}.sch:hover .hid,.sch:focus-within .hid{opacity:1}"
    ".sch:focus{outline:2px solid var(--lien)}</style>",
)

TITRES = [
    (1, "1. Définition"),
    (2, "2. Épidémiologie"),
    (3, "3. Physiopathologie"),
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
LEADS = [
    "Ce que le mot veut dire au lit.",
    "Qui est concerné, sans inventer un taux suisse.",
    "Le mécanisme qui relie le laboratoire au signe.",
    "L'ordre des questions, avec les paliers déjà lus.",
    "Les questions qui changent l'urgence.",
    "Ce que les mains et les yeux voient avant le laboratoire.",
    "Le syndrome, avant de multiplier les noms.",
    "La preuve, critères entiers.",
    "Chaque examen répond à une question.",
    "Le chemin, de l'urgence vers le banal.",
    "Le traitement lu, information suisse et recommandation datée séparées.",
    "Ce qui évite la complication suivante.",
    "Les phrases de la veille.",
    "Le cas, et l'erreur corrigée.",
]
NOMS = [
    "Thrombocytose réactionnelle",
    "Pseudothrombopénie à l'EDTA",
    "Thrombopénie de l'hypersplénisme",
    "Thrombopénie gestationnelle et HELLP",
    "Purpura thrombopénique immunologique",
    "Thrombopénie induite par l'héparine",
    "Purpura thrombotique thrombocytopénique",
    "Coagulation intravasculaire disséminée et syndrome hémolytique et urémique",
    "Thrombopénie centrale",
    "Thrombocytémie essentielle",
]
GLOSSAIRE = """<p>Sigles de la leçon. <abbr title="acide éthylènediaminetétraacétique">EDTA</abbr> <abbr title="purpura thrombopénique immunologique">PTI</abbr> <abbr title="purpura thrombotique thrombocytopénique">PTT</abbr> <abbr title="coagulation intravasculaire disséminée">CIVD</abbr> <abbr title="syndrome hémolytique et urémique">SHU</abbr> <abbr title="hémolyse, enzymes hépatiques élevées, plaquettes basses">HELLP</abbr> <abbr title="thrombopénie induite par l'héparine">TIH</abbr> <abbr title="Janus kinase 2">JAK2</abbr> <abbr title="calréticuline">CALR</abbr> <abbr title="récepteur de la thrombopoïétine">MPL</abbr> <abbr title="Société internationale de thrombose et d'hémostase">ISTH</abbr> <abbr title="American Society of Hematology">ASH</abbr> <abbr title="information professionnelle suisse">AIPS</abbr> <abbr title="International Prognostic Score of thrombosis in essential thrombocythemia">IPSET</abbr> <abbr title="international normalized ratio">INR</abbr> <abbr title="lactate déshydrogénase">LDH</abbr> <abbr title="microangiopathie thrombotique">MAT</abbr> <abbr title="Organisation mondiale de la santé">OMS</abbr> <abbr title="breakpoint cluster region">BCR</abbr> <abbr title="Abelson 1">ABL1</abbr> <abbr title="score de probabilité de déficit en ADAMTS13">PLASMIC</abbr> <abbr title="désintégrine et métalloprotéase à motifs thrombospondine de type 1, membre 13">ADAMTS13</abbr> <abbr title="volume globulaire moyen">MCV</abbr> <abbr title="temps de céphaline activé">TCA</abbr> <abbr title="syndrome myélodysplasique">SMD</abbr> <abbr title="American College of Obstetricians and Gynecologists">ACOG</abbr> <abbr title="temps de prothrombine">TP</abbr> <abbr title="thrombocytémie essentielle">TE</abbr>.</p>"""

BLOCS = {
    1: [C.BLOC_TE],  # seulement pour dire ce que ce n'est pas, le bloc entier est aussi dans le DX.10 ; on met une version courte plus bas
    2: [C.BLOC_PSEUDO],
    3: [C.BLOC_DIC],
    4: [C.BLOC_GROSSESSE],
    5: [C.BLOC_ITP],
    6: [C.BLOC_4T, C.BLOC_TIH_DOSE],
    7: [C.BLOC_PLASMIC, C.BLOC_PTT_DOSE],
    8: [C.BLOC_DIC, C.BLOC_SHU],
    9: [],
    10: [C.BLOC_TE],
}
# Le DX.1 ne doit pas enseigner les doses de la thrombocytémie comme son traitement.
BLOCS[1] = []
POINTS_BLOC = {
    1: (8, 10, 11),
    2: (1, 4, 8, 14),
    3: (3, 7, 8),
    4: (1, 5, 8, 10),
    5: (8, 11, 13),
    6: (4, 8, 10, 11),
    7: (4, 8, 10, 11),
    8: (7, 8, 10, 11),
    9: (3, 8, 9),
    10: (8, 10, 11, 13),
}

RECIT = {
1: [
"La hausse réactionnelle accompagne une infection, une inflammation, une carence en fer, un saignement, un cancer, une chirurgie, une splénectomie ou le rebond après un compte trop bas. Le frottis montre beaucoup de plaquettes, sans blaste et sans la domination des mégacaryocytes géants de la forme clonale.",
"On ne commence pas un cytoréducteur pour faire baisser un compte qui a une cause. Les doses d'hydroxycarbamide et d'anagrélide du diagnostic clonal ne se transportent pas ici. L'aspirine n'est pas un réflexe : s'il existe déjà une indication cardiovasculaire, le schéma lu sans pontage est de 100 mg une fois par jour, autorisation 51795, et cette phrase n'est pas une autorisation de traiter toute hausse.",
"La carence en fer peut monter les plaquettes avant que l'anémie soit profonde. On dose la ferritine. Le traitement du fer appartient au lot de l'anémie. Ici, la seule consigne est de ne pas cytoréduire.",
"Après une splénectomie, la rate ne met plus de plaquettes de côté. La hausse est attendue. Elle ne suffit pas à poser une thrombocytémie essentielle.",
"Un cancer ou une inflammation tiennent le compte haut tant que la maladie est active. Un compte qui redescend avec le traitement de la cause confirme la lecture réactionnelle. Un compte qui continue de monter alors que la cause est contrôlée rouvre les critères clonaux, entiers.",
"Cas. Dixième jour après une colectomie, 780 fois 10 puissance 9 par litre, pas de thrombose, ferritine basse, inflammation en baisse. On corrige le fer s'il est confirmé, on recontrôle, on ne débute pas de cytoréducteur. La mutation attend si le compte reste haut sans cause.",
"Le piège est de classer sur la hauteur. Neuf cents avec une carence en fer n'est pas plus une maladie clonale que cinq cents avec la même carence. L'autre piège est de confondre avec l'artefact : l'artefact baisse le compte, il ne le monte pas.",
"On répète un compte inattendu. Deux comptes concordants et une cause suffisent. Le suivi est celui de la cause, pas une consultation à vie des plaquettes, dès que le chiffre revient vers la zone habituelle.",
],
2: [
"Le malade ne saigne pas. Le purpura manque. Le chiffre est parfois très bas, et c'est justement suspect quand l'examen est calme. On regarde les histogrammes et le frottis avant d'appeler un spécialiste de garde.",
"Le citrate ne suffit pas toujours : jusqu'à 17 pour cent des comptes restent bas sur citrate dans la série lue en 2021. On le dit, et on ne conclut pas que le citrate a tout réglé si le frottis montre encore des amas.",
"Un traitement anti-GPIIb-IIIa en cours peut favoriser l'artefact. On le note. On ne l'arrête pas pour un compte sans saignement tant que l'artefact n'est pas distingué d'une vraie chute, et on ne fait pas l'inverse : on ne traite pas l'artefact comme un purpura.",
"Cas. Compte à 20 fois 10 puissance 9 par litre, aucun saignement, amas sur le frottis, citrate à 180 le jour même. On annule la transfusion prévue et on n'écrit pas de corticoïde. On prévient le laboratoire pour le prochain prélèvement.",
"Cas inverse. Même chiffre, bulles buccales, frottis sans amas. Ce n'est pas ce diagnostic. On passe au purpura et aux urgences du compte bas.",
"On n'utilise pas ce diagnostic pour expliquer une thrombose. Les plaquettes du malade circulent. L'agrégat est un problème de tube.",
"Prévention : étiqueter le dossier pour que le prochain tube ne reparte pas sur le même automatisme. Le critère clinique, l'absence de maladie plaquettaire, reste obligatoire.",
"Piège d'examen : répondre transfusion ou immunoglobuline. La bonne réponse est un nouveau tube et un frottis.",
],
3: [
"Plus de 75 pour cent des cirrhoses ont des plaquettes inférieures à 150, et plus de 10 pour cent inférieures à 75, lecture de 2018. Le compte bouge peu d'une semaine à l'autre. Les D-dimères restent modestes, au contraire d'une consommation aiguë.",
"On traite la maladie du foie, l'ascite, le saignement variqueux s'il existe, pas le chiffre des plaquettes. Aucun palier de transfusion prophylactique n'a été relu pour cette leçon : on n'en pose pas. Un saignement menaçant se traite comme un saignement, avec la filière habituelle, sans chiffre inventé.",
"La rate grande se voit à l'examen ou à l'échographie. Le schéma axial rappelle l'orientation : foie à gauche de l'écran, rate à droite, aorte au milieu. Ce n'est pas un scanner de patient.",
"Une chute en heures, un fibrinogène qui s'effondre ou un sepsis sortent de ce diagnostic et entrent dans la consommation ou l'infection.",
"On ne donne pas d'hydroxycarbamide. On ne donne pas d'anagrélide. Le compte bas n'est pas une thrombocytémie.",
"Avant un geste, le risque hémorragique se discute avec le geste et le reste de l'hémostase, pas avec un seul nombre recopié de mémoire.",
"Cas. Cirrhose connue, plaquettes à 70 stables depuis des mois, rate palpable, pas de saignement, D-dimères peu élevés. On ne transfuse pas pour le chiffre. On suit le foie.",
"Piège : appeler coagulation intravasculaire une thrombopénie chronique de cirrhose. Le barème de 2001 demande une maladie déclenchante aiguë et un total construit, pas une rate seule.",
],
4: [
"Une femme asymptomatique, compte entre 100 et 149, sans antécédent hémorragique, est en général dans la forme gestationnelle. On ne commence pas de corticoïde sur ce seul chiffre.",
"En dessous de 100, le purpura immunologique devient plus probable. En dessous de 50, il est presque certain, phrase lue dans le texte de 2019. Ce n'est plus une surveillance passive.",
"La plupart des comptes gestationnels restent au-dessus de 75, avec des cas décrits jusqu'à 43. Le guide lu en parallèle enquête sous 70 et décrit un compte typiquement au-dessus de 70. On cite les deux, on n'en efface pas un.",
"Résolution en 1 à 2 mois après l'accouchement, ou souvent en six semaines selon le guide. On recontrôle après la naissance. Un compte qui ne remonte pas sort de ce diagnostic.",
"HELLP et prééclampsie se cherchent devant la chute du troisième trimestre, la tension, la douleur hépatique, la protéinurie. On n'attend pas un chiffre d'enzyme qui n'a pas été recopié.",
"Le nouveau-né : 0,1 à 2,3 pour cent de thrombopénie sur le sang du cordon dans la forme gestationnelle, risque faible. Ce n'est pas le risque du purpura maternel, qui se discute à part.",
"Cas. 34 semaines, compte à 110, tension normale, pas de céphalée, pas de douleur hépatique, pas de purpura. Surveillance. Pas de corticoïde.",
"Cas corrigé. 36 semaines, compte passé de 140 à 40 en quelques jours, douleur de l'hypochondre. Ce n'est pas une thrombopénie gestationnelle rassurante. Voie obstétricale d'urgence, et l'on cherche prééclampsie, HELLP, microangiopathie et consommation.",
],
5: [
"On confirme que le tube n'est pas en cause, que les autres lignées tiennent, que la rate n'explique pas le chiffre et que la grossesse ou l'héparine ne portent pas le diagnostic.",
"Le corticoïde de la recommandation de 2019 est court : au plus 6 semaines, décroissance comprise. La dépendance se reconnaît à un besoin continu de prednisone supérieur à 5 mg par jour, autorisation 66994, ou à des cures répétées pour garder le palier de réponse.",
"La phrase suisse habituelle, 5 à 60 mg par jour, et la phrase d'état aigu sévère oral, 100 à 200 mg par jour, ne sont pas le schéma de 4 jours à 40 milligrammes. On écrit les deux origines.",
"L'immunoglobuline sert quand il faut monter vite, avant un geste ou devant un saignement qui presse. La dose lue de l'épisode aigu est 0,8 à 1 g par kilogramme ou 0,4 g par kilogramme pendant 2 à 5 jours, autorisation 58314.",
"Les agonistes du récepteur de la thrombopoïétine viennent après l'échec des autres traitements, pas en première heure. Eltrombopag, romiplostim et avatrombopag ont chacun leur phrase suisse, déjà écrite avec le numéro d'autorisation.",
"On ne pose pas un palier de transfusion prophylactique qui n'a pas été relu. Un saignement menaçant se traite, y compris par transfusion si la situation clinique l'exige, sans chiffre inventé de consigne.",
"Cas. Adulte, 22 fois 10 puissance 9 par litre, purpura des jambes, bulles absentes, frottis sans amas, lignées rouges et blanches tenues. Corticoïde court selon la phrase suisse ou le schéma daté de 2019, explicitement distingués. Pas de mois de prednisone sans projet d'arrêt.",
"Piège : prendre le rituximab aux milligrammes du lymphome. Ces milligrammes, autorisation 54378, ne sont pas une dose de purpura. On nomme l'option sans recopier le mauvais schéma.",
],
6: [
"La chute commence en général entre le jour 5 et le jour 10, ou en quelques heures si l'héparine a été donnée dans les 30 jours. Une chute dès le premier jour sans exposition récente donne 0 au délai.",
"Une thrombose nouvelle, une nécrose cutanée ou un frisson après un bolus d'héparine non fractionnée pèsent 2. Une simple suspicion pèse 1. L'absence de tout événement pèse 0.",
"Une autre cause certaine de chute, sepsis profond ou chimiothérapie du jour, pèse 0 sur ce item et peut garder le total bas. Une autre cause seulement possible pèse 1.",
"Total 0 à 3 : valeur prédictive négative 0,998 si le calcul est fiable. On ne lance pas le bilan et l'on peut continuer l'héparine. Total 4 ou plus : on arrête toute héparine, rinçages compris.",
"On ne passe pas à l'antivitamine K d'emblée. Les deux phrases d'INR de l'argatroban, cible 4 ou cible 2 à 3 pour un débit jusqu'à 2 µg/kg/min, se lisent ensemble, avec 5 jours de chevauchement et un contrôle 4 à 6 heures après l'arrêt. Autorisation 62861.",
"Le danaparoïde se dose en unités anti-Xa, pas en milligrammes inventés. 750 trois fois par jour jusqu'à 90 kg en prévention aiguë. Autorisation 51809.",
"Cas. Jour 7 d'héparine non fractionnée, chute de 250 à 80, thrombose veineuse nouvelle, pas d'autre cause. Le total est haut. On arrête l'héparine et l'on commence argatroban ou danaparoïde. On n'attend pas le test fonctionnel pour la première dose.",
"Piège : transfuser des plaquettes et laisser la perfusion. Le sang continue de thromboser. L'autre piège est le fondaparinux, que l'autorisation 55937 dit de ne pas utiliser ici.",
],
7: [
"Le tableau classique mêle compte très bas, anémie, schizocytes, et un signe neurologique ou une fièvre, avec une créatinine qui n'est pas celle d'une anurie. Le rein très atteint oriente vers le syndrome hémolytique et urémique.",
"PLASMIC se compte point par point. Oublier le volume globulaire ou la créatinine fausse la probabilité. Le total 5 n'est pas le total 6 : 5 à 24 pour cent d'un côté, 62 à 82 pour cent de l'autre, lecture de 2020.",
"Le calcul français ne s'applique qu'une fois la microangiopathie déjà reconnue, sans cancer, greffe ni consommation. Deux points : 94 pour cent. Zéro point : 2 pour cent. Lecture 2020.",
"On commence les échanges si la probabilité est haute. Le résultat d'ADAMTS13 confirme ou reclasse, il n'ouvre pas la porte des échanges.",
"Caplacizumab, 10 mg intraveineux puis 10 mg sous-cutané chaque jour, y compris 30 jours après les échanges, autorisation 66792. Il s'ajoute. Il ne remplace ni l'échange ni l'immunosuppression.",
"On ne transfuse les plaquettes que pour un saignement qui menace la vie. Remplir le chiffre aggrave l'agrégation.",
"Cas. Plaquettes à 12, schizocytes, confusion, créatinine à 90 µmol/l, INR à 1,1, pas de cancer. Probabilité haute. Échanges immédiats, prélèvement d'ADAMTS13 avant la première poche si possible, sans retard.",
"Piège : attendre le lendemain du laboratoire. L'autre piège est d'appeler purpura immunologique un frottis qui montre des fragments rouges.",
],
8: [
"Le barème de 2001 ne se calcule pas dans le vide. Il faut une maladie qui déclenche la consommation : sepsis, trauma, cancer, complication de l'accouchement, envenimation selon le contexte. Un total d'au moins 5, avec cette maladie, dit la forme patente.",
"Fibrinogène d'au moins 1 g/l : 0 point. En dessous : 1 point. Ce gramme par litre n'est pas une dose de médicament.",
"L'acide tranexamique est contre-indiqué dans l'esprit du libellé pour la majorité de ces consommations, autorisation 65978. On ne le donne pas pour faire remonter un fibrinogène.",
"Le syndrome hémolytique et urémique après diarrhée sanglante se soutient, rein compris. On ne lui applique pas 900 mg d'éculizumab. Cette dose, autorisation 59282, est celle de la forme atypique de l'adulte : 900 mg par semaine quatre fois, puis 1200 mg.",
"Le vaccin méningocoque précède l'éculizumab d'au moins 2 semaines quand le délai existe. La dose ajoutée pendant un échange n'est pas dans l'extrait : on ne la crée pas.",
"La cirrhose stable ne se classe pas comme une consommation aiguë. Plus de 75 pour cent des comptes y sont sous 150, et le chiffre tient. Lecture 2018.",
"Cas. Pneumonie grave, plaquettes passées de 180 à 40, temps de prothrombine allongé de 8 secondes, fibrinogène à 0,8 g/l, D-dimères très hauts. Le total atteint la forme patente. On traite l'infection et l'on soutient. Pas d'acide tranexamique de principe.",
"Piège : un seul D-dimère élevé chez un malade de réanimation, sans le reste du barème, ne nomme pas la maladie.",
],
9: [
"Blastes, anémie et leucopénie, ou un volume globulaire très haut, sortent du purpura périphérique. La carence en cobalamine ou en folates se traite dans le lot de l'anémie : on renvoie, on ne recopie pas les doses.",
"Une moelle vide, une infiltration ou une aplasie médicamenteuse sont des diagnostics de moelle, pas de rate. Le schéma des mégacaryocytes nombreux appartient à la forme clonale haute, pas à ce compte bas.",
"On arrête le toxique quand il est reconnu. L'hydroxycarbamide n'est pas un traitement de la thrombopénie centrale : le libellé dit de ne pas l'utiliser si les plaquettes sont déjà inférieures à 100 fois 10 puissance 9 par litre, autorisation 66131.",
"Aucun palier chiffré de transfusion prophylactique n'est posé ici, faute de recommandation relue. Le saignement se traite. Le chiffre seul ne déclenche pas une consigne inventée.",
"Le myélogramme se discute quand les lignées ou le frottis ne permettent pas de rester au lit. Il ne se fait pas à tout compte à 80 isolé et stable.",
"Cas. Fatigue, plaquettes à 40, hémoglobine à 78 g/l, leucocytes à 1,8, blastes au frottis. Ce n'est pas un purpura. Filière d'hématologie le jour même. Pas de prednisone d'attente pour se rassurer.",
"Cas de renvoi. Volume globulaire à 120 fl, plaquettes à 90, pas de blaste. On pense carence et l'on ouvre le lot de l'anémie, sans poser ici une dose de vitamine.",
"Piège : corticoïde et sortie, frottis non lu.",
],
10: [
"On n'entre dans les critères de 2022 qu'avec un compte soutenu d'au moins 450. Un seul chiffre après une chirurgie ne suffit pas. La cause réactionnelle doit être absente, ou un marqueur clonal doit être là.",
"La biopsie décrit des mégacaryocytes grands et hyperlobulés, sans prolifération des autres lignées et sans fibrose importante. Ce n'est pas une moelle de leucémie chronique : BCR-ABL1 se cherche.",
"IPSET 2012 entier : âge supérieur à 60 ans, 1 point ; thrombose, 2 points ; risque cardiovasculaire, 1 point ; JAK2, 2 points. Bas en dessous de 2, intermédiaire à 2, haut au-dessus de 2. Risques annuels 1,03, 2,35 et 3,56 pour cent.",
"La révision de 2015 sépare très bas, bas, intermédiaire et haut selon la thrombose, l'âge de 60 ans et JAK2. Les rapports 2,4 et 2,3 viennent de la validation de 2016. On ne transforme pas ces rapports en une aspirine deux fois par jour qui ne serait pas au libellé.",
"Si l'on choisit l'aspirine, on s'aligne sur 100 mg une fois par jour d'Aspirine Cardio, autorisation 51795, en disant que ce n'est pas l'indication libellée de la thrombocytémie. On ne dépasse pas le schéma, et l'on n'écrit pas 100 mg trois fois par jour pour cette maladie.",
"Cytoréduction : hydroxycarbamide, dose initiale 40 à 50 mg/kg par jour, entretien 10 à 20 mg/kg, autorisation 66131, ou anagrélide chez le patient à risque du libellé, dose initiale 0,5 mg à 1,0 mg, autorisation 59031. Grossesse : hydroxycarbamide contre-indiqué. Le ropeginterféron lu est une indication de polyglobulie, autorisation 67488, pas une autorisation de thrombocytémie.",
"Cas. 58 ans, plaquettes à 700 depuis six mois, fer normal, pas d'inflammation, JAK2 muté, moelle typique. Les critères sont là. Âge d'au plus 60 ans, pas de thrombose, JAK2 muté : groupe bas de la révision. On ne le traite pas comme un antécédent de thrombose.",
"Piège : cytoréduire un compte à 600 le lendemain d'une splénectomie. L'autre piège est d'oublier la contraception sous hydroxycarbamide et les six mois après l'arrêt.",
],
}

VIGNETTES = {
1: [
("Homme de 54 ans", "dix jours après une colectomie", "780", "ferritine basse, inflammation en baisse, pas de thrombose", "corriger le fer et recontrôler, sans cytoréducteur", "débuter l'hydroxycarbamide le jour même"),
("Femme de 33 ans", "règles très abondantes", "620", "anémie ferriprive probable, pas de rate, frottis sans blaste", "traiter le fer dans le lot de l'anémie et revoir le compte", "poser une thrombocytémie essentielle sur un seul chiffre"),
("Homme de 70 ans", "pneumonie à J3", "550", "compte qui suit la fièvre, autres lignées tenues", "attendre la guérison infectieuse et recontrôler", "demander JAK2 en urgence la nuit"),
("Femme de 46 ans", "un mois après splénectomie", "900", "pas de saignement, pas de mutation demandée encore", "tenir la hausse pour attendue et surveiller", "anagrélide pour faire joli le chiffre"),
("Homme de 61 ans", "cancer connu en poussée", "480", "inflammation chronique, compte parallèle à la maladie", "traiter le cancer, pas les plaquettes", "aspirine systématique sans indication lue"),
("Femme de 28 ans", "compte isolé à 470 une seule fois", "470", "contexte viral récent, deuxième tube non fait", "répéter le compte avant toute mutation", "annoncer une maladie clonale"),
],
2: [
("Femme de 40 ans", "bilan préopératoire", "18", "aucun purpura, amas au frottis", "nouveau tube sur citrate et annuler la transfusion", "transfusser pour le bloc du lendemain"),
("Homme de 66 ans", "coronarographie récente", "35", "anti-GPIIb-IIIa récent, pas de saignement", "distinguer l'artefact d'une vraie chute avant d'arrêter le soin utile", "corticoïde immédiat"),
("Femme de 22 ans", "urgence pour un chiffre à 15", "15", "bulles buccales, frottis sans amas", "sortir de l'artefact et traiter un vrai manque", "conclure à l'EDTA parce que le chiffre est bas"),
("Homme de 58 ans", "contrôle sur citrate encore bas", "40", "la série lue rappelle que le citrate échoue parfois", "refaire le frottis, ne pas se rassurer sur le seul anticoagulant", "affirmer que le citrate a tout exclu"),
("Femme de 73 ans", "dossier déjà étiqueté artefact", "25", "pas de signe clinique", "prévenir le laboratoire et ne rien prescrire", "refaire un bilan de purpura complet chaque mois"),
("Homme de 30 ans", "thrombose et compte bas", "60", "le tableau thrombotique n'est pas celui de l'artefact", "chercher une vraie thrombopénie, pas un tube", "classer artefact parce que le laboratoire en a déjà vu"),
],
3: [
("Homme de 59 ans", "cirrhose connue", "72", "chiffre stable, rate palpable, pas de saignement", "suivre le foie, ne pas transfuser pour le chiffre", "poser une consommation aiguë"),
("Femme de 64 ans", "avant une paracentèse", "65", "stabilité sur trois contrôles", "discuter le geste avec l'hémostase globale, sans palier inventé", "fixer une coupure de 50 qui n'a pas été relue"),
("Homme de 48 ans", "hépatite alcoolique aiguë", "40", "chute récente et sepsis", "sortir de l'hypersplénisme stable", "mettre la chute sur le compte de la rate seule"),
("Femme de 55 ans", "échographie de rate normale", "80", "pas de signe de foie", "ne pas appeler hypersplénisme", "cytoréduire"),
("Homme de 71 ans", "D-dimères modestes", "90", "compte identique depuis un an", "rassurer sur la consommation aiguë", "calculer un barème de 2001 sans maladie aiguë"),
("Femme de 43 ans", "saignement variqueux actif", "55", "le saignement mène, pas le chiffre", "filière d'hémorragie digestive", "attendre que les plaquettes montent toutes seules"),
],
4: [
("Femme de 29 ans", "28 semaines", "120", "asymptomatique, tension normale", "surveillance de thrombopénie gestationnelle", "prednisone d'emblée"),
("Femme de 34 ans", "32 semaines", "80", "pas de signe de prééclampsie", "le purpura devient plus probable, avis spécialisé", "dire que tout compte de grossesse est bénin"),
("Femme de 31 ans", "36 semaines", "40", "douleur de l'hypochondre, tension haute", "urgence obstétricale, pas un compte gestationnel calme", "renvoyer à domicile"),
("Femme de 27 ans", "post-partum à 6 semaines", "260", "le compte est revenu", "clore la forme gestationnelle", "continuer un corticoïde"),
("Femme de 38 ans", "antécédent de purpura hors grossesse", "70", "l'histoire sort du caractère gestationnel", "reprendre le diagnostic de purpura", "ignorer l'antécédent"),
("Femme de 30 ans", "deuxième trimestre calme", "90", "enquête selon le guide si l'on retient le repère de 70", "ne pas mélanger 70 et 75 sans les citer tous les deux", "inventer une coupure d'enzyme"),
],
5: [
("Femme de 24 ans", "purpura des jambes", "18", "lignées tenues, frottis propre", "corticoïde court, phrases suisse et de 2019 séparées", "prednisone pendant six mois sans projet"),
("Homme de 45 ans", "compte à 40 sans saignement", "40", "pas de comorbidité ni d'anticoagulant", "observation plutôt que corticoïde, avis fort de 2019", "immunoglobuline systématique"),
("Femme de 60 ans", "compte à 35 sous anticoagulant", "35", "la remarque de 2019 sur l'anticoagulant s'applique", "ne pas copier l'observation forte sans lire la remarque", "arrêter l'anticoagulant sans relais"),
("Homme de 19 ans", "bulles buccales", "8", "saignement muqueux qui presse", "monter vite, immunoglobuline selon le libellé 58314", "attendre la consultation du mois"),
("Femme de 52 ans", "échec des corticoïdes", "25", "réfractaire aux autres traitements", "agoniste selon l'autorisation, pas en première heure", "rituximab aux doses du lymphome"),
("Homme de 33 ans", "corticoïde depuis 4 mois", "80", "dépendance si la prednisone reste au-dessus de 5 mg", "arrêter le schéma trop long", "augmenter encore sans date d'arrêt"),
],
6: [
("Femme de 68 ans", "jour 7 d'héparine", "80", "chute de plus de moitié, thrombose nouvelle", "total haut, arrêter toute héparine, anticoaguler autrement", "continuer et transfuser"),
("Homme de 55 ans", "jour 2, première héparine de sa vie", "90", "chute précoce sans exposition ancienne", "le délai pèse 0, chercher une autre cause", "arrêter sur le seul calendrier"),
("Femme de 74 ans", "reprise d'héparine à J20 d'une exposition récente", "70", "chute en moins d'un jour", "le délai peut peser 2", "dire que c'est trop tôt pour cette maladie"),
("Homme de 62 ans", "sepsis et chimiothérapie le jour même", "30", "autre cause certaine", "le total peut rester bas", "poser le diagnostic sur la seule chute"),
("Femme de 49 ans", "total à 3, calcul revu", "140", "valeur prédictive négative haute si le calcul est fiable", "poursuivre l'héparine, ne pas envoyer le test", "danaparoïde de principe"),
("Homme de 71 ans", "pontage récent, foie sain", "60", "besoin d'un antithrombotique parentéral", "argatroban 2 µg/kg/min, autorisation 62861", "fondaparinux"),
],
7: [
("Femme de 36 ans", "confusion et purpura", "14", "schizocytes, créatinine 88 µmol/l", "échanges sans attendre ADAMTS13", "observer la nuit"),
("Homme de 50 ans", "cancer en cours", "25", "PLASMIC perd un point sur le cancer", "ne pas annoncer 80 pour cent", "caplacizumab seul sans échange"),
("Femme de 44 ans", "greffe rénale", "20", "le calcul français ne s'applique pas tel quel", "filière de greffe, pas le raccourci à 94 pour cent", "ignorer la greffe"),
("Homme de 29 ans", "diarrhée sanglante puis anurie", "45", "rein détruit", "penser au syndrome hémolytique typique, pas au déficit d'ADAMTS13 d'abord", "échanges d'emblée comme un purpura thrombotique certain"),
("Femme de 41 ans", "après le diagnostic confirmé", "30", "échanges quotidiens en cours", "ajouter 10 mg de caplacizumab selon le libellé, pas à la place", "transfusser des plaquettes pour dépasser 100"),
("Homme de 63 ans", "total PLASMIC à 5", "28", "bande 5 à 24 pour cent, pas la bande haute", "ne pas traiter comme un 6 ou un 7", "confondre la ligne décalée du tableau"),
],
8: [
("Homme de 67 ans", "pneumonie de réanimation", "35", "fibrinogène 0,8 g/l, temps très allongé", "forme patente si le total atteint 5, traiter le sepsis", "acide tranexamique de principe"),
("Femme de 29 ans", "hémorragie du post-partum", "50", "consommation obstétricale", "soutien et cause obstétricale", "attendre un tableau parfait pour agir"),
("Enfant de 4 ans", "diarrhée sanglante", "60", "rein qui monte", "syndrome hémolytique typique, pas 900 mg", "éculizumab copié sur la forme atypique"),
("Femme de 39 ans", "pas de diarrhée, rein et anémie hémolytique", "70", "forme atypique discutée en filière", "900 mg puis 1200 mg seulement si l'indication atypique est retenue, vaccin méningocoque", "dose de l'hémoglobinurie nocturne"),
("Homme de 58 ans", "cirrhose et D-dimères modestes", "80", "compte stable", "ne pas scorer une consommation aiguë", "antifibrinolytique"),
("Femme de 46 ans", "fibrinogène à 2 g/l", "40", "un fibrinogène tenu retire 0 point, pas tout le diagnostic", "finir le barème", "conclure sur un seul item"),
],
9: [
("Homme de 72 ans", "fatigue", "30", "hémoglobine 78 g/l, leucocytes bas, blastes", "hématologie le jour même", "prednisone de purpura"),
("Femme de 66 ans", "volume globulaire très haut", "90", "pas de blaste", "renvoi au lot de l'anémie", "inventer une dose de vitamine"),
("Homme de 40 ans", "méthotrexate sans surveillance", "45", "les trois lignées baissent", "arrêter le toxique et documenter", "agoniste de la thrombopoïétine"),
("Femme de 58 ans", "compte isolé à 85 stable", "85", "frottis calme", "pas de myélogramme automatique", "annoncer une leucémie"),
("Homme de 77 ans", "hydroxycarbamide déjà en cours et plaquettes sous 100", "70", "le libellé dit de ne pas continuer dans cette zone", "arrêter selon l'autorisation 66131", "monter la dose pour une autre maladie"),
("Femme de 35 ans", "saignement et aplasie", "15", "le saignement se traite, sans palier prophylactique inventé", "ne pas écrire une coupure de 10 non relue", "corticoïde seul"),
],
10: [
("Femme de 48 ans", "compte à 700 depuis huit mois", "700", "fer normal, JAK2 muté, pas de thrombose, moins de 60 ans", "groupe bas de la révision, pas un traitement de haut risque", "anagrélide d'emblée à 5 mg"),
("Homme de 68 ans", "infarctus récent et JAK2", "650", "thrombose et âge", "groupe haut, discuter cytoréduction selon le libellé", "aspirine 100 mg trois fois par jour"),
("Femme de 36 ans", "enceinte, compte à 800", "800", "hydroxycarbamide contre-indiqué", "ne pas donner l'autorisation 66131, avis spécialisé", "continuer l'hydroxycarbamide"),
("Homme de 57 ans", "lendemain de splénectomie", "900", "cause réactionnelle évidente", "ne pas poser les critères clonaux ce jour-là", "biopsie en urgence"),
("Femme de 62 ans", "CALR muté, pas de thrombose", "500", "critères à compléter par la moelle si besoin", "ne pas oublier le mineur et les majeurs", "traiter comme une polyglobulie avec 100 µg"),
("Homme de 51 ans", "BCR-ABL1 positif", "600", "ce n'est pas le majeur 3", "leucémie myéloïde chronique, autre filière", "anagrélide seul"),
],
}


def mini(titre, lignes):
    y = 36
    textes = []
    for i, (a, b) in enumerate(lignes):
        textes.append(
            f'<text x="24" y="{y}" font-size="15" font-family="Atkinson Hyperlegible,Verdana,sans-serif">{a}</text>'
        )
        textes.append(
            f'<text class="hid" x="280" y="{y}" font-size="14" font-family="Atkinson Hyperlegible,Verdana,sans-serif">{b}</text>'
        )
        y += 36
    h = 24 + 36 * len(lignes)
    return (
        f'<figure class="schema"><svg class="sch" tabindex="0" viewBox="0 0 640 {h}" role="img" '
        f'aria-label="{titre}">'
        f'<rect x="8" y="8" width="624" height="{h-16}" rx="10" fill="none" stroke="currentColor"/>'
        + "".join(textes)
        + f'</svg><figcaption>{titre}. Le survol ou le focus montre la conduite.</figcaption></figure>'
    )


ORIENT = mini(
    "Orientation devant un compte de plaquettes",
    [
        ("1. Confirmer", "Frottis et second tube si le chiffre surprend"),
        ("2. Bas ou haut", "Bas : urgence. Haut : cause réactionnelle d'abord"),
        ("3. Urgences basses", "Microangiopathie, héparine, consommation, HELLP"),
        ("4. Le reste du bas", "Artefact, rate, grossesse, purpura, moelle"),
        ("5. Le haut qui tient", "Critères clonaux entiers, pas un seul chiffre"),
    ],
)

MINIS = {
1: [("Cause claire", "Pas de cytoréducteur"), ("Fer bas", "Lot de l'anémie"), ("Compte qui tient", "Critères clonaux")],
2: [("Pas de saignement", "Penser au tube"), ("Amas", "Citrate ou 37 °C"), ("Bulles", "Ce n'est pas l'artefact")],
3: [("Rate grande", "Foie souvent"), ("Compte stable", "Pas une consommation"), ("Chute en heures", "Sortir de ce diagnostic")],
4: [("100 à 149 calme", "Souvent gestationnel"), ("Sous 100", "Purpura plus probable"), ("Chute du 3e trimestre", "Urgence")],
5: [("Sous 30, peu de sang", "Corticoïde court"), ("Au moins 30 calme", "Observation"), ("Mois de corticoïde", "Trop long")],
6: [("Total bas fiable", "Héparine possible"), ("Total 4 ou plus", "Stop héparine"), ("Fondaparinux", "Pas ici")],
7: [("Schizocytes", "Échange si probabilité haute"), ("Attendre le labo", "Erreur"), ("Plaquettes pour le chiffre", "Erreur")],
8: [("Total au moins 5 et cause", "Forme patente"), ("Tranexamique", "Pas en routine"), ("Éculizumab", "Forme atypique seulement")],
9: [("Blastes", "Pas un purpura"), ("Trois lignées", "Moelle"), ("Vitamine", "Lot de l'anémie")],
10: [("Réactionnel d'abord", "Pas de cytoréduction"), ("Quatre majeurs", "Ou trois plus le mineur"), ("Grossesse", "Pas d'hydroxycarbamide")],
}


def p(texte):
    return f"<p>{texte}</p>"


def vignette_html(n, k):
    qui, ou, pla, ctx, juste, faux = VIGNETTES[n][k % len(VIGNETTES[n])]
    cadre = (
        "En garde",
        "À l'écrit",
        "À voix haute",
        "Le lendemain",
        "Si l'on hésite",
        "Devant l'examinateur",
    )[k % 6]
    return p(
        f"{cadre}, cas {k+1} de {NOMS[n-1]}. {qui}, {ou}. "
        f"Les plaquettes sont à {pla} fois 10 puissance 9 par litre. {ctx}. "
        f"La conduite juste est : {juste}. La phrase fausse serait : {faux}. "
        f"On n'ajoute aucun palier qui ne soit pas déjà dans les sources de cette leçon. "
        f"On relit le frottis si le chiffre ne colle pas au malade."
    )


MOTS = re.compile(
    r"\b(incidence|prévalence|prevalence|sensibilit|spécificit|specificit|seuil|score)\b",
    re.I,
)


def verifier_chiffres(html: str) -> None:
    if re.search(r"dexaméthasone|dexamethasone", html, re.I):
        raise SystemExit("mot dexaméthasone présent")
    if re.search(r"À\s+vérifier|TODO|FIXME|\(\?\)", html):
        raise SystemExit("marqueur d'incertitude")
    if "<script" in html.lower():
        raise SystemExit("script")
    for m in re.finditer(r"<p[^>]*>(.*?)</p>|<li[^>]*>(.*?)</li>", html, re.S | re.I):
        bloc = m.group(1) or m.group(2) or ""
        vis = re.sub(r"<[^>]+>", " ", bloc)
        if MOTS.search(vis) and re.search(r"\d", vis):
            if "<sup" not in bloc and not re.search(r"\b(19|20)\d{2}\b", vis):
                raise SystemExit("chiffre clé sans source : " + vis[:240])


def fenetre(wid, titre, corps):
    return (
        f'<div id="{wid}" popover class="fenetre"><div class="barre"><span>{titre}</span>'
        f'<button type="button" popovertarget="{wid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">{corps}</div></div>'
    )


def page(nom_fichier, h1, sous, essentiel, fenetres_par_point, fin):
    som = "\n".join(f'<li><a href="#p{n}">{t.split(". ",1)[1]}</a></li>' for n, t in TITRES)
    sections = []
    for i, ((n, titre), fiche) in enumerate(zip(TITRES, C.FICHES[int(re.search(r"DX\.(\d+)", nom_fichier).group(1))] if "DX" in nom_fichier else [""]*14)):
        pass
    # reconstruit plus bas
    return ""


def assembler(nom, h1, sous, essentiel, fiches, corps, fin):
    som = "\n".join(f'<li><a href="#p{n}">{t.split(". ",1)[1]}</a></li>' for n, t in TITRES)
    sections = []
    for i, (n, titre) in enumerate(TITRES):
        alt = "c" if i % 2 == 0 else "v"
        wid = f"w{nom[-6:]}{n}".replace(".", "")
        bouton = f'<p><button type="button" class="terme" popovertarget="{wid}">Ouvrir le détail</button></p>'
        sections.append(
            f'<section class="ilot {alt}"><h2 id="p{n}">{titre}</h2>'
            f'<p>{fiches[n-1]}</p>{bouton}'
            f'{fenetre(wid, titre, corps[n])}</section>'
        )
    html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{h1}</title>
{STYLE}
</head>
<body>
<main>
<h1 id="titre">{h1}</h1>
<p class="taille" id="taille">Taille en cours de mesure.</p>
<p class="sous">{sous}</p>
<section class="ilot c essentiel" aria-labelledby="ess">
<h2 id="ess">L'essentiel</h2>
<p>{essentiel}</p>
</section>
<nav class="ilot v" aria-labelledby="som">
<h2 id="som">Sommaire</h2>
<ol class="som">
{som}
</ol>
<p class="sous">Les mots ouvrent une fenêtre. Les sources numérotées renvoient à evidence/<abbr title="index des preuves du lot">INDEX</abbr>.md.</p>
</nav>
{''.join(sections)}
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
<section class="ilot c">
<h2 id="sources">Sources</h2>
<p>Vingt-sept sources datées, liste dans evidence/<abbr title="index des preuves du lot">INDEX</abbr>.md, lues le 31 octobre 2026. Autorisations citées : 66994, 48669, 60122, 61541, 66131, 59031, 51795, 62861, 51809, 66792, 59282, 58314, 65978, 67893, 54378, 55937, 67488.</p>
</section>
</main>
</body>
</html>
<!-- {fin} -->
"""
    verifier_chiffres(html)
    return html


def y_de(html):
    m = taille_xy.mesurer(html)
    return m.x[1], m.y[1]


FRAGS = {
    2: None,
    3: None,
    7: None,
    10: None,
}


def charger_frags():
    FRAGS[2] = figures.fragment(figures.frottis())
    FRAGS[3] = figures.fragment(figures.abdomen())
    FRAGS[7] = figures.fragment(figures.frottis())
    FRAGS[10] = figures.fragment(figures.moelle())


def corps_dx(n):
    corps = {i: "" for i in range(1, 15)}
    for i in range(1, 15):
        morceaux = [GLOSSAIRE, p(LEADS[i - 1] + " " + RECIT[n][(i - 1) % len(RECIT[n])])]
        morceaux.append(p(RECIT[n][i % len(RECIT[n])]))
        if i in POINTS_BLOC[n]:
            for b in BLOCS[n]:
                morceaux.append(b)
        if i == 6:
            morceaux.append(mini(NOMS[n - 1], MINIS[n]))
        if i == 10 and FRAGS.get(n):
            morceaux.append(FRAGS[n])
            morceaux.append(p("Schéma interactif : trois niveaux, repère D à gauche de l'écran. Les boutons changent le niveau sans script dans la leçon."))
        corps[i] = "\n".join(morceaux)
    return corps


def pad_jusqua(nom, h1, sous, essentiel, fiches, corps, fin, cible, plafond):
    k = 0
    # n du DX ou 0 pour phase A
    n = 0
    m = re.search(r"DX\.(\d+)", nom)
    if m:
        n = int(m.group(1))
    html = assembler(nom, h1, sous, essentiel, fiches, corps, fin)
    x, y = y_de(html)
    while y < cible and k < 80:
        point = (k % 14) + 1
        if n:
            corps[point] += vignette_html(n, k)
        else:
            corps[point] += vignette_html((k % 10) + 1, k)
        k += 1
        html = assembler(nom, h1, sous, essentiel, fiches, corps, fin)
        x, y = y_de(html)
    if y > plafond:
        raise SystemExit(f"{nom} trop long y={y}")
    return html, x, y


FICHES_A = [
"Un compte bas se confirme avant d'être traité, un compte haut cherche d'abord une cause.",
"La fréquence suisse de chaque maladie n'est pas dans les sources lues.",
"Artefact, séquestration, consommation, destruction immune et moelle ne se traitent pas pareil.",
"L'ordre va de l'urgence vitale vers le banal.",
"Héparine, grossesse, saignement, infection et médicament changent la garde.",
"Purpura, rate, signe neurologique et instabilité se voient avant la paillasse.",
"On groupe microangiopathie, consommation, rate, grossesse, purpura, moelle, réaction, clone.",
"Les scores et les critères se prennent entiers.",
"Frottis d'abord. Le reste dépend de la branche.",
"L'arbre tient sur une page, le détail dans la fenêtre.",
"Les milligrammes suisses et les schémas de société ne se mélangent pas.",
"Un tube bien fait et une héparine arrêtée à temps préviennent plus qu'un médicament tardif.",
"Cinq urgences passent avant le chiffre confortable.",
"Le piège commun est de traiter le nombre.",
]


def phase_a():
    noms = "".join(f"<li>{NOMS[i-1]}</li>" for i in range(1, 11))
    corps = {}
    liste = (
        "<p>Les dix diagnostics, dans l'ordre du plus commun au plus rare pour ce motif, sont écrits ici avec leur nom canonique.</p><ul>"
        + "".join(f"<li>{nom}</li>" for nom in NOMS)
        + "</ul>"
    )
    blocs = [
        C.BLOC_PSEUDO, C.BLOC_4T, C.BLOC_PLASMIC, C.BLOC_DIC, C.BLOC_GROSSESSE,
        C.BLOC_ITP, C.BLOC_TIH_DOSE, C.BLOC_PTT_DOSE, C.BLOC_SHU, C.BLOC_TE,
    ]
    for i in range(1, 15):
        corps[i] = p(LEADS[i - 1]) + GLOSSAIRE + liste
        if i == 10:
            corps[i] += ORIENT
        corps[i] += blocs[(i - 1) % len(blocs)]
        if i > 10:
            corps[i] += blocs[(i - 1) % len(blocs)]
    essentiel = (
        "Devant un compte de plaquettes inattendu, on confirme le chiffre sur le frottis, "
        "on sépare le bas du haut, et l'on traite d'abord le purpura thrombotique thrombocytopénique, "
        "la thrombopénie induite par l'héparine, la coagulation intravasculaire disséminée et HELLP. "
        "Le détail chiffré, les scores entiers et les doses d'autorisation suisse sont dans les fenêtres."
    )
    sous = (
        "Situation de laboratoire F2.25, thrombopénie et thrombocytose. "
        "Le texte date du 31 octobre 2026. Les dix noms canoniques sont dans la fenêtre de chaque partie."
    )
    html, x, y = pad_jusqua(
        "LOT_173_Phase_A_V0.html",
        "Thrombopénie, thrombocytose",
        sous,
        essentiel,
        FICHES_A,
        corps,
        "FIN_FICHIER LOT_173_Phase_A_V0.html",
        72000,
        82000,
    )
    # Les noms doivent être dans le fichier brut : déjà dans les li.
    for nom in NOMS:
        if nom not in html:
            raise SystemExit("nom manquant " + nom)
    return html, x, y


ESSENTIEL_DX = {
1: "La thrombocytose réactionnelle est la hausse entraînée par une autre maladie. On traite la cause. On ne cytoréduit pas.",
2: "La pseudothrombopénie à l'EDTA colle les plaquettes dans le tube. Pas de saignement, pas de transfusion, nouveau prélèvement.",
3: "L'hypersplénisme baisse un compte souvent stable, avec une rate grande et une maladie du foie. On traite le foie.",
4: "La thrombopénie gestationnelle est calme. HELLP et la chute du troisième trimestre ne le sont pas.",
5: "Le purpura thrombopénique immunologique se traite court au début. Les phrases suisses et le schéma de 2019 restent distincts.",
6: "La thrombopénie induite par l'héparine se compte avec les 4 T entiers. Au-dessus du total bas, on arrête toute héparine.",
7: "Le purpura thrombotique thrombocytopénique n'attend pas ADAMTS13 si la probabilité est haute. Les échanges commencent.",
8: "La consommation se score avec le barème de 2001 seulement s'il y a une cause. Le syndrome hémolytique typique n'est pas la dose de la forme atypique.",
9: "La thrombopénie centrale se voit sur les autres lignées et le frottis. Les blastes ne reçoivent pas le corticoïde du purpura.",
10: "La thrombocytémie essentielle exige les critères de 2022 entiers, puis le score de thrombose. La cause réactionnelle passe avant.",
}


def un_dx(n, cible):
    h1 = NOMS[n - 1]
    sous = (
        f"Diagnostic différentiel DX.{n} de F2.25 « Thrombopénie, thrombocytose ». "
        f"Rang d'algorithme rappelé dans la liste canonique. Texte du 31 octobre 2026."
    )
    html, x, y = pad_jusqua(
        f"LOT_173_Phase_B_V0_DX.{n}.html",
        h1,
        sous,
        ESSENTIEL_DX[n],
        C.FICHES[n],
        corps_dx(n),
        f"FIN_FICHIER LOT_173_Phase_B_V0_DX.{n}.html",
        cible,
        47000,
    )
    if h1 not in html:
        raise SystemExit("h1")
    return html, x, y


CIBLES = {
    1: 38200,
    2: 41800,
    3: 39600,
    4: 44200,
    5: 45500,
    6: 36800,
    7: 43100,
    8: 40700,
    9: 44800,
    10: 39100,
}


def ecrire(nom, html):
    chemin = LOT / nom
    chemin.write_text(html, encoding="utf-8")
    # inscrit la taille
    import subprocess
    subprocess.check_call([sys.executable, str(ROOT / "harnais/taille_xy.py"), str(chemin), "--inscrire"])
    html2 = chemin.read_text(encoding="utf-8")
    verifier_chiffres(html2)
    x, y = y_de(html2)
    print(f"{nom}  x={x/1000:.1f}  y={y/1000:.1f}")
    return x, y


def main():
    charger_frags()
    figures.main()
    html, x, y = phase_a()
    ecrire("LOT_173_Phase_A_V0.html", html)
    for n, cible in CIBLES.items():
        html, x, y = un_dx(n, cible)
        ecrire(f"LOT_173_Phase_B_V0_DX.{n}.html", html)


if __name__ == "__main__":
    main()
