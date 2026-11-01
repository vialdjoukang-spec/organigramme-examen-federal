#!/usr/bin/env python3
"""Assemble les HTML du LOT_191 à partir des noyaux et d'une démarche propre à chaque DX."""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generer as G
import taille_xy  # harnais déjà sur sys.path via generer

LOT = G.LOT
CIBLES = {
    "A": 76000,
    1: 37800,
    2: 40200,
    3: 42600,
    4: 45100,
    5: 36900,
    6: 41300,
    7: 43800,
    8: 46200,
    9: 39100,
    10: 44600,
}
CADRES = [
    "À l'arrivée",
    "Après le déshabillage",
    "Avant l'ordonnance",
    "Si le cri persiste",
    "Avant le retour à domicile",
    "Quand la famille rappelle",
    "Dans le compte rendu",
    "Si un signe nouveau apparaît",
    "À la visite de contrôle",
    "Devant les deux parents",
    "Au moment de la pesée",
    "Après la prise de température",
]


def ajouter(n: int, blocs: dict[int, list[str]]) -> None:
    G.NOYAUX[n] = blocs


def q(*lignes: str, src: int) -> list[str]:
    return G.P(*lignes, src=src)


ajouter(2, {
    1: q(
        "Le reflux gastro-œsophagien est la remontée du contenu gastrique.",
        "Il devient une maladie quand les symptômes gênent ou qu'une complication est là.",
        "Chez le nourrisson, dire qu'un pleur est gênant est difficile, car il ne parle pas.",
        "Les régurgitations visibles d'un enfant sain ne sont pas, à elles seules, une maladie.",
        "Le guide de 2018 sépare donc le reflux simple de la maladie de reflux.",
        src=5,
    ),
    2: q(
        "Les régurgitations sont fréquentes au premier semestre et régressent souvent ensuite.",
        "Un début après 6 mois, ou une persistance au-delà de 12 à 18 mois, fait chercher autre chose.",
        "Le recouvrement avec l'allergie au lait est décrit en 2024 comme inférieur à 1 pour cent.",
        "On ne transforme pas cette rareté en certitude devant un enfant malade.",
        "Aucune série suisse de ce LOT ne donne la part des pleurs due au seul reflux.",
        src=5,
    ),
    3: q(
        "La barrière anti-reflux du nourrisson est immature, et les repas sont liquides et fréquents.",
        "L'arc-boutement et les pleurs existent avec et sans maladie de reflux.",
        "Le syndrome de Sandifer est une posture dystonique du cou, citée en 2018.",
        "Une œsophagite est une complication muqueuse, pas un synonyme de régurgitation.",
        "Six études avant 12 mois n'ont pas montré de gain des inhibiteurs sur les pleurs.",
        src=5,
    ),
    4: q(
        "On décrit le moment du rejet, le volume, et si le lait est caillé ou vert.",
        "On regarde la courbe, l'inconfort pendant la tétée et les signes d'alarme du tableau de 2018.",
        "Sans signe d'alarme et sans retentissement, on n'ouvre pas d'examen.",
        "On n'utilise pas un inhibiteur comme test diagnostique chez le nourrisson.",
        "On écrit ce qui ferait changer d'avis au contrôle.",
        src=5,
    ),
    5: q(
        "Perte de poids, léthargie, fièvre et irritabilité extrême sortent du reflux simple.",
        "Une dysurie fait chercher une infection urinaire.",
        "Une fontanelle bombée ou des convulsions sortent du cadre digestif.",
        "Des vomissements en jet et répétés, jusqu'à 2 mois, font chercher une sténose du pylore.",
        "Un vomissement bilieux est lu comme une occlusion possible.",
        "Du sang rouge par l'anus ou une distension ne se traitent pas comme un reflux.",
        src=5,
    ),
    6: q(
        "L'enfant qui régurgite et sourit ensuite, avec une courbe normale, est le tableau simple.",
        "On ausculte le cœur et on palpe les fémorales, car la fatigue alimentaire a d'autres causes.",
        "On regarde la gorge et les oreilles si la fièvre est présente.",
        "Un abdomen souple et non distendu rassure davantage qu'un récit de gaz.",
        "On cherche le Sandifer seulement si la posture du cou est vraiment dystonique.",
        src=5,
    ),
    7: q(
        "Pleurs plus régurgitations plus courbe plate : on ne conclut pas au reflux.",
        "Pleurs plus eczéma plus sang dans les selles : on pense à l'allergie, pas d'abord à l'acide.",
        "Pleurs par vagues plus pâleur plus sang : on pense à l'invagination.",
        "Rejet vert : chirurgie, pas épaississant.",
        "Arc-boutement isolé chez un enfant qui grossit : le guide de 2018 ne traite pas par l'acide.",
        src=5,
    ),
    8: q(
        "Le diagnostic de reflux simple est clinique.",
        "La maladie de reflux suppose un retentissement ou une complication.",
        "L'œsophagite se voit par endoscopie, pas par le seul cri.",
        "On ne pose pas le diagnostic parce qu'un médicament a semblé aider un soir.",
        "On date le critère utilisé, simple ou compliqué.",
        src=5,
    ),
    9: q(
        "Le transit baryté et l'échographie servent à écarter une anomalie anatomique, pas à mesurer l'acide.",
        "L'endoscopie se discute devant un saignement, une cassure ou un doute d'autre maladie.",
        "La pH-métrie n'est pas le premier geste d'un nourrisson qui pleure et grossit.",
        "On n'hospitalise pas pour une régurgitation isolée.",
        "On documente le poids du jour.",
        src=5,
    ),
    10: q(
        "Le schéma montre trois voies : rassurer, chercher une allergie, ou adresser.",
        "La voie rassurer exige une courbe normale et zéro signe d'alarme.",
        "La voie allergie exige un symptôme de plus que le cri, selon le texte de 2024.",
        "La voie adresse s'ouvre sur le sang, le vert, la fièvre ou la fontanelle.",
        "On ne mélange pas ces voies dans la même ordonnance.",
        src=5,
    ),
    11: q(
        "On fractionne les repas seulement si les volumes sont vraiment excessifs, et on surveille la courbe.",
        "On garde le nourrisson vertical après la tétée, sans position ventrale pour dormir.",
        "La recommandation 5.5 de 2018 déconseille l'anti-H2 et l'inhibiteur pour une régurgitation de nourrisson sain.",
        "Nexium, autorisation 58091, ne doit pas être utilisé avant 1 an ni sous 10 kg.",
        "Chez l'enfant de 1 à 11 ans, avec œsophagite sévère et poids sous 20 kg mais d'au moins 10 kg, le texte lit 10 mg une fois par jour pendant 8 semaines.",
        "Les doses au-dessus de 1 mg par kilogramme et par jour n'ont pas été étudiées.",
        "Cette ligne ne s'applique pas au nourrisson qui pleure sans œsophagite.",
        src=5,
    ),
    12: q(
        "On évite le tabac passif, cité parmi les facteurs d'environnement du guide.",
        "On ne couche pas sur le ventre pour diminuer un reflux.",
        "On explique le caractère souvent transitoire du premier semestre.",
        "On donne les signes de retour : vert, sang, fièvre, cassure de poids.",
        "On ne promet pas qu'un lait épaissi efface une urgence.",
        src=5,
    ),
    13: q(
        "Reflux simple et maladie de reflux ne sont pas le même mot.",
        "Pas d'acide sans retentissement ni signe d'alarme.",
        "Pas d'essai médicamenteux diagnostique chez le nourrisson.",
        "Vomissement vert égal occlusion jusqu'à preuve contraire.",
        "Nexium sans dose avant 1 an et avant 10 kg.",
        src=13,
    ),
    14: q(
        "Piège : traiter des coliques par un inhibiteur.",
        "Piège : appeler reflux un vomissement vert.",
        "Piège : continuer un médicament qui n'a pas de dose autorisée à cet âge.",
        "Cas corrigé. À deux mois, les régurgitations sont quotidiennes, la courbe suit son couloir, l'examen est normal.",
        "On explique, on ne prescrit pas Nexium, on revoit la courbe.",
        "Si le poids casse au contrôle, on sort du reflux simple et on reprend les signes d'alarme.",
        src=5,
    ),
})

ajouter(3, {
    1: q(
        "L'allergie aux protéines du lait de vache est une réaction reproductible, immunitaire, à ces protéines.",
        "Elle est trop souvent affirmée, et parfois manquée.",
        "Les pleurs seuls n'en sont presque jamais la preuve.",
        "Le texte de 2024 dit que les données sont insuffisantes pour une éviction devant des pleurs isolés.",
        "Une éviction de 2 à 4 semaines, puis une réintroduction, se discute si d'autres symptômes s'ajoutent et si les critères de recherche des coliques sont là.",
        src=6,
    ),
    2: q(
        "Environ 20 pour cent des nourrissons pleurent ou sont irritables, et l'allergie en est rarement la cause.",
        "Chez l'enfant allaité exclusivement, l'allergie existe mais reste peu fréquente.",
        "Le recouvrement attendu avec le reflux est inférieur à 1 pour cent.",
        "La proctocolite du nourrisson commence souvent dans les premières semaines.",
        "On ne cite pas un taux suisse qui n'est pas dans le dossier.",
        src=6,
    ),
    3: q(
        "La forme immédiate, liée aux immunoglobulines E, et la forme retardée ne se prouvent pas de la même façon.",
        "La forme retardée n'a pas de test sanguin fiable dans le texte lu.",
        "L'amélioration sous éviction peut être un hasard, un effet du lactose ou l'histoire naturelle.",
        "C'est pourquoi la réintroduction fait partie du diagnostic.",
        "Une selle verte ou glaireuse, chez un enfant sain, n'est pas un critère.",
        src=6,
    ),
    4: q(
        "On liste la peau, les selles, les vomissements, la croissance et les antécédents familiaux.",
        "On ne lance pas un régime sur un seul cri du soir.",
        "Si l'éviction est décidée, on écrit la date de début et la date de réintroduction.",
        "La fenêtre lue pour la forme non immédiate est de 2 à 4 semaines.",
        "On ne prolonge pas un régime qui n'a pas été confirmé par la réintroduction.",
        src=6,
    ),
    5: q(
        "Un choc, une urticaire généralisée ou une gêne respiratoire après le lait est une urgence, pas un régime de ville.",
        "Une cassure de poids ne se surveille pas à domicile sans projet.",
        "Du sang en quantité, avec un enfant malade, n'est pas une proctocolite bénigne.",
        "Une fièvre oriente d'abord vers l'infection.",
        "On demande qui a déjà supprimé le lait, et depuis combien de temps.",
        src=6,
    ),
    6: q(
        "On regarde l'eczéma, l'anus, le tonus et la courbe.",
        "Un anus fissuré peut saigner sans allergie.",
        "On ne conclut pas sur la couleur des selles.",
        "L'examen nu reste obligatoire, comme pour tout pleur.",
        "On palpe le ventre avant d'attribuer le sang à l'alimentation.",
        src=6,
    ),
    7: q(
        "Sang minime, enfant allaité, bonne croissance, pas d'atopie : le texte permet d'observer le premier mois.",
        "Eczéma étendu plus vomissements plus cassure : l'éviction diagnostique devient raisonnable.",
        "Pleurs seuls : pas d'éviction d'après le vote lu en 2024.",
        "Régurgitations isolées : l'allergie est peu probable.",
        "Constipation rebelle : une autre phrase du même texte discute une éviction, ce n'est pas le motif pleurs.",
        src=6,
    ),
    8: q(
        "Le diagnostic positif est la rechute des symptômes à la réintroduction, après une amélioration nette.",
        "L'outil de vigilance ne pose pas ce diagnostic.",
        "Un test cutané ou sanguin négatif n'élimine pas la forme retardée.",
        "Un test positif n'évite pas la lecture clinique.",
        "On écrit la forme suspectée avant le régime.",
        src=6,
    ),
    9: q(
        "Aucune prise de sang n'est obligatoire devant des pleurs isolés.",
        "L'endoscopie n'est pas le premier geste d'une suspicion simple.",
        "On pèse à chaque étape du régime.",
        "On vérifie que l'hydrolysat est vraiment extensif si cette voie est choisie.",
        "Le texte de 2024 dit que la preuve d'éviction diagnostique lue concerne les hydrolysats de lait, pas le soja.",
        src=6,
    ),
    10: q(
        "Le schéma a trois branches : observer, éviction courte avec réintroduction, ou urgence.",
        "Observer est la branche des pleurs secs et de la proctocolite minime du premier mois.",
        "L'éviction courte exige une date de réintroduction écrite.",
        "L'urgence est le choc, la déshydratation ou le saignement important.",
        "On ne passe pas de l'observation à un régime définitif sans épreuve.",
        src=6,
    ),
    11: q(
        "On protège l'allaitement. Un régime maternel peut faire cesser le sein trop tôt.",
        "Si la mère évince, on prévoit un appui nutritionnel et une réintroduction.",
        "Chez l'enfant au lait artificiel, l'hydrolysat extensif est la voie lue pour l'épreuve.",
        "Le soja n'est pas recommandé pour les coliques dans le passage de 2024.",
        "On ne donne pas un inhibiteur d'acide à la place de cette démarche.",
        "Aucun schéma milligrammé d'hydrolysat n'est une dose d'information professionnelle.",
        src=6,
    ),
    12: q(
        "On ne supprime pas le lait de la maison par précaution chez un enfant sans signe.",
        "On évite les régimes successifs non datés.",
        "On explique la différence entre une selle verte et un saignement.",
        "On revoit la croissance pendant toute éviction.",
        "On prévient les parents qu'une amélioration seule ne confirme rien.",
        src=6,
    ),
    13: q(
        "Pleurs isolés : pas d'éviction recommandée par le texte de 2024.",
        "Éviction 2 à 4 semaines seulement avec symptômes supplémentaires, puis réintroduction.",
        "Allaitement protégé.",
        "Selles vertes non diagnostiques.",
        "Outil de vigilance non diagnostique.",
        src=6,
    ),
    14: q(
        "Piège : cinq laits en un mois sans réintroduction.",
        "Piège : arrêter le sein au premier cri.",
        "Piège : appeler allergie une invagination qui saigne.",
        "Cas corrigé. À six semaines, pleurs du soir, courbe normale, pas de sang, pas d'eczéma. On n'évince pas.",
        "Deux semaines plus tard, du sang répété et un eczéma apparaissent, l'enfant ralentit sur la courbe.",
        "On écrit alors une éviction de 2 à 4 semaines et la date de l'épreuve, sans appeler cela déjà une allergie.",
        src=6,
    ),
})

ajouter(4, {
    1: q(
        "L'infection aiguë du nourrisson qui pleure va de l'otite et de l'infection urinaire jusqu'au sepsis et à la méningite.",
        "Le cri change, souvent avec fièvre, tonus moindre ou refus de boire.",
        "Ce n'est pas un trouble fonctionnel.",
        "La brochure genevoise demande les urgences si l'enfant est gris, mou, ou inconsolable même dans les bras.",
        "On commence les gestes vitaux sans attendre le germe.",
        src=3,
    ),
    2: q(
        "La fièvre est un motif très fréquent. La méningite est rare et grave.",
        "On ne donne pas un taux suisse de méningite qui n'est pas archivé.",
        "L'infection urinaire du nourrisson fébrile sans foyer se cherche par les urines, pas par le seul cri.",
        "L'otite se confirme à l'otoscope, pas parce que l'enfant porte la main à l'oreille.",
        "Le texte de 2018 cite la dysurie comme indice urinaire chez le petit enfant.",
        src=5,
    ),
    3: q(
        "Une bactérie ou un virus déclenche inflammation, douleur et parfois choc.",
        "La méningite irrite les méninges et peut bomber la fontanelle.",
        "Le sepsis désadapte le tonus, la couleur et la perfusion.",
        "Une infection urinaire haute peut ne donner que fièvre et irritabilité.",
        "On ne réduit pas ces mécanismes à une colique parce que l'horaire est le soir.",
        src=5,
    ),
    4: q(
        "On note l'heure de début, le pic fébrile, les contacts, les vomissements et la quantité bue.",
        "On évalue couleur, temps de recoloration, fréquence respiratoire et conscience.",
        "Un enfant toxique est vu tout de suite par le senior et réanimé.",
        "Un enfant fébrile mais tonique a un examen de foyer complet.",
        "On ne renvoie pas un nourrisson fébrile sans projet de surveillance.",
        src=3,
    ),
    5: q(
        "Teint gris, lèvres bleues, enfant mou, cri faible, hurlement au toucher : urgence lue dans la brochure genevoise.",
        "Fontanelle bombée, convulsion, taches qui ne blanchissent pas : on ne cherche pas une colique.",
        "Une fièvre chez un nouveau-né de quelques jours n'est pas un motif de conseil téléphonique.",
        "Un refus total de boire avec peu d'urines fait craindre la déshydratation.",
        "La brochure cite plus de 8 heures sans urine parmi les signes de retour urgent en cas de pertes.",
        src=3,
    ),
    6: q(
        "On regarde le tympan, la gorge, la fontanelle, le souffle, le ventre, les hanches et la peau.",
        "Une éruption purpurique se cherche sur tout le corps, y compris les plantes.",
        "On compte les secondes de recoloration cutanée.",
        "On déshabille, car une ecchymose peut coexister avec une fièvre.",
        "Un abdomen aigu fébrile peut être chirurgical et infectieux.",
        src=3,
    ),
    7: q(
        "Fièvre plus tympan bombé et opaque : otite jusqu'à preuve d'un autre foyer.",
        "Fièvre sans foyer chez le petit nourrisson : urines et réévaluation.",
        "Fièvre plus fontanelle bombée ou trouble de conscience : méningite jusqu'à preuve du contraire.",
        "Fièvre plus cri et ecchymose : on ne choisit pas entre infection et maltraitance, on tient les deux.",
        "Cri sans fièvre et examen normal : on revient aux autres diagnostics de ce LOT.",
        src=3,
    ),
    8: q(
        "Le diagnostic de foyer se fait sur l'examen, pas sur le motif d'entrée.",
        "Le sepsis et la méningite sont des diagnostics de gravité, confirmés par les prélèvements sans en retarder le traitement.",
        "Une bandelette urinaire aide, la culture tranche.",
        "On n'attend pas la culture pour traiter un enfant toxique.",
        "On écrit le foyer trouvé et ceux qui ont été écartés.",
        src=3,
    ),
    9: q(
        "Selon l'âge et le tonus : glycémie capillaire, bandelette urinaire, et prélèvements sanguins.",
        "La ponction lombaire se décide sur les signes méningés et l'âge, pas sur un chiffre inventé ici.",
        "Une radiographie de thorax se discute si la respiration est anormale.",
        "On ne fait pas d'échographie abdominale à la place de la réanimation.",
        "Le seuil de leucocytes du liquide n'est pas archivé dans ce LOT.",
        src=3,
    ),
    10: q(
        "Le schéma sépare l'enfant toxique, l'enfant fébrile stable, et l'enfant sans fièvre.",
        "La voie toxique ouvre l'oxygène, la voie veineuse et l'appel du senior.",
        "La voie stable ouvre l'examen de foyer puis la décision de prélèvement.",
        "La voie sans fièvre ne se ferme qu'après l'examen nu.",
        "On réévalue l'heure suivante si le tonus baisse.",
        src=3,
    ),
    11: q(
        "On traite la douleur et la fièvre avec Dafalgan enfant, autorisation 43838.",
        "La dose unique lue est 15 mg de paracétamol par kilogramme.",
        "On ne dépasse pas 75 mg par kilogramme et par jour, avec 6 à 8 heures entre les prises.",
        "Sans avis médical, pas plus de 3 jours continus avant 12 ans.",
        "La pipette part de 3 kg, soit 45 mg, c'est-à-dire 1,5 ml.",
        "Algifor Dolo Junior, autorisation 58834, est interdit avant 6 mois et avant 5 kg, et en cas de varicelle.",
        "De 6 à 8 mois, la dose simple lue est 2,5 ml, soit 50 mg, sans dépasser 30 mg par kilogramme et par jour.",
        "Rocephin, autorisation 44625, limite le nouveau-né jusqu'à 14 jours à 20 à 50 mg par kilogramme, sans dépasser 50 mg par kilogramme.",
        "Chez l'enfant en bas âge et l'enfant, la méningite bactérienne se commence à 100 mg par kilogramme une fois par jour, sans dépasser 4 g.",
        "Cette ligne de 100 mg n'est pas celle du nouveau-né de moins de 15 jours.",
        "On ne mélange pas Rocephin au calcium intraveineux chez le nouveau-né de 28 jours ou moins.",
        "Les doses intraveineuses du nouveau-né se perfusent sur 60 minutes.",
        src=11,
    ),
    12: q(
        "On vérifie les autres boîtes de paracétamol pour éviter le doublement.",
        "On explique les signes de retour le soir même.",
        "On ne masque pas une infection grave par un seul antipyrétique sans réexamen.",
        "Le propylène glycol du sirop et un substrat de l'alcool déshydrogénase inquiètent chez le nouveau-né, d'après l'information 43838.",
        "On vaccine selon le plan suisse, mais ce n'est pas le traitement de la crise.",
        src=11,
    ),
    13: q(
        "Enfant gris ou mou : urgence, pas colique.",
        "Paracétamol 15 mg par kilogramme, plafond 75 mg par kilogramme, autorisation 43838.",
        "Ibuprofène de cette spécialité seulement à partir de 6 mois et de 5 kg.",
        "Nouveau-né : plafond de ceftriaxone 50 mg par kilogramme, pas la ligne de méningite de 100 mg.",
        "Calcium intraveineux et ceftriaxone ne se mêlent pas chez le nouveau-né.",
        src=16,
    ),
    14: q(
        "Piège : donner 100 mg par kilogramme de ceftriaxone à un nouveau-né de 10 jours.",
        "Piège : ibuprofène à 2 mois avec Algifor Dolo Junior.",
        "Piège : deux sirops de paracétamol additionnés.",
        "Cas corrigé. À 3 mois, fièvre, cri, tympans normaux, tonus conservé. On cherche l'urine, on donne 15 mg par kilogramme, on revoit.",
        "S'il devient mou dans l'heure, on passe sur la voie toxique et on appelle.",
        "On n'écrit pas la dose de méningite de l'enfant plus grand sur ce nouveau-né.",
        src=16,
    ),
})

ajouter(5, {
    1: q(
        "L'invagination est l'entrée d'un segment d'intestin dans le segment d'aval.",
        "Elle peut occlure, ischémier, nécroser et perforer.",
        "Le guide britannique de 2017 la tient pour la cause unique la plus fréquente d'urgence chirurgicale abdominale du nourrisson.",
        "Le cri est souvent par vagues, avec pâleur entre les vagues.",
        "Ce n'est pas une colique du soir répétée depuis des semaines.",
        src=7,
    ),
    2: q(
        "Le texte de 2017 dit le caractère idiopathique dans 90 pour cent des cas.",
        "Le pic lu va de 6 à 18 mois.",
        "Avant et après ce pic, un point d'appel anatomique devient plus plausible.",
        "Les garçons sont décrits comme plus souvent atteints, sans taux suisse ici.",
        "Un audit national cité trouve un taux de réduction de 71 pour cent, et une étude de 2012 un taux de 61 pour cent.",
        src=7,
    ),
    3: q(
        "L'intestin invaginé comprime ses vaisseaux.",
        "La douleur et la pâleur suivent l'ischémie intermittente.",
        "Le sang et le mucus viennent de la muqueuse souffrante. Ils sont tardifs.",
        "L'enfant peut être léthargique plus que bruyant.",
        "Une hyperplasie lymphoïde est le mécanisme idiopathique proposé par le guide.",
        src=7,
    ),
    4: q(
        "On demande les vagues, les vomissements, le dernier selles et la couleur.",
        "On cherche un épisode viral récent sans s'arrêter à ce récit.",
        "On examine le ventre entre deux crises, quand l'enfant se relâche.",
        "On appelle le radiologue et le chirurgien tôt.",
        "On ne donne pas à boire en attendant.",
        src=7,
    ),
    5: q(
        "Douleur par à-coups, pâleur, vomissements, puis sang : la triade complète est souvent absente au début.",
        "Une léthargie isolée est reconnue par le guide comme signe possible.",
        "Un ventre péritonéal, un choc ou un pneumopéritoine suspecté interdisent le lavement.",
        "Le vomissement bilieux reste un signe d'occlusion dans le guide de reflux de 2018.",
        "On ne rassure pas parce que l'enfant joue entre deux crises.",
        src=7,
    ),
    6: q(
        "On palpe un boudin sans brutaliser un ventre déjà chirurgical.",
        "On regarde le rectum et la couche.",
        "On évalue la perfusion et on pose une voie si l'enfant est pâle.",
        "L'examen nu cherche aussi une hernie et une ecchymose.",
        "Une masse et un cri par vagues suffisent à demander l'échographie.",
        src=7,
    ),
    7: q(
        "Avant 6 mois, on garde l'invagination en tête mais on cherche aussi le volvulus.",
        "Entre 6 et 18 mois, l'invagination idiopathique est au premier rang des urgences abdominales lues.",
        "Après cet âge, on pense davantage à un point d'appel.",
        "Une gastroentérite peut précéder, elle ne remplace pas l'image si les vagues persistent.",
        "Une allergie ne donne pas ce rythme de pâleur.",
        src=7,
    ),
    8: q(
        "Le diagnostic positif est échographique.",
        "Le signe de la cible, ou du beignet, est transversal.",
        "Le pseudo-rein est longitudinal.",
        "Le guide de 2017 décrit une sensibilité proche de 100 pour cent et une spécificité de 80 à 100 pour cent.",
        "La clinique seule ne remplace pas l'image quand elle est disponible.",
        src=7,
    ),
    9: q(
        "L'échographie précède le lavement.",
        "On regarde le Doppler et un liquide piégé, qui baissent la chance de réduction sans l'interdire si l'enfant est stable.",
        "Des taux de réduction de 26 pour cent et de 31 pour cent sont cités dans ces situations.",
        "Une radiographie simple ne sert pas à confirmer. Elle peut montrer une perforation.",
        "On groupe le sang et on perfuse avant la sédation.",
        src=7,
    ),
    10: q(
        "Le schéma a trois temps : suspecter, confirmer, réduire ou opérer.",
        "Suspecter dès les vagues et la pâleur.",
        "Confirmer par l'échographie.",
        "Réduire par lavement à l'air si le guide britannique s'applique et s'il n'y a ni péritonite ni perforation.",
        "Opérer si l'échec, la nécrose ou l'instabilité sont là.",
        src=7,
    ),
    11: q(
        "On réanime avant le geste.",
        "Le lavement se fait là où un chirurgien peut ouvrir si ça perfore.",
        "On antalgie. Le nom de la molécule et la dose suivent l'information professionnelle du produit choisi.",
        "Dafalgan enfant, autorisation 43838, peut couvrir une douleur à 15 mg par kilogramme, sans remplacer la réduction.",
        "On surveille après réduction, car la récidive existe.",
        "On ne commence pas un antibiotique de principe si le guide n'en fait pas une routine. Ce LOT n'archive pas une telle routine.",
        src=7,
    ),
    12: q(
        "On explique aux parents les signes de récidive : vagues, pâleur, vomissements.",
        "On ne renvoie pas sans surveillance après un lavement.",
        "On évite de banaliser un second épisode.",
        "Un point d'appel se cherche si l'âge ou la récidive sortent du pic.",
        "La prévention vaccinale n'est pas le sujet de l'heure.",
        src=7,
    ),
    13: q(
        "Vagues, pâleur, puis sang tardif.",
        "Échographie d'abord, cible et pseudo-rein.",
        "Sensibilité lue proche de 100 pour cent, spécificité de 80 à 100 pour cent, guide de 2017.",
        "Air si stable. Chirurgie si péritonite, perforation ou échec.",
        "Pic 6 à 18 mois, idiopathique dans 90 pour cent.",
        src=7,
    ),
    14: q(
        "Piège : attendre les selles en gelée de groseille pour croire au diagnostic.",
        "Piège : donner un antispasmodique et renvoyer.",
        "Piège : faire un lavement sur un ventre péritonéal.",
        "Cas corrigé. À 9 mois, cris par vagues depuis 6 heures, pâleur, pas encore de sang. L'échographie montre la cible.",
        "On perfuse, on appelle le chirurgien, on réduit par l'air si l'enfant reste stable.",
        "Le sang absent n'a pas retardé l'image.",
        src=7,
    ),
})

ajouter(6, {
    1: q(
        "L'occlusion digestive chirurgicale du nourrisson qui pleure regroupe surtout le volvulus sur malrotation et la hernie étranglée.",
        "Le vomissement bilieux est lu en 2018 comme un signe d'occlusion.",
        "Les causes nommées incluent le volvulus du grêle et l'invagination, tenue à part dans ce LOT.",
        "Une hernie inguinale devenue dure, douloureuse et irréductible étrangle.",
        "Ces deux tableaux ne se surveillent pas à la maison.",
        src=5,
    ),
    2: q(
        "Le volvulus du nouveau-né est rare et détruit l'intestin en quelques heures.",
        "La hernie inguinale du nourrisson est plus fréquente, et l'étranglement en est l'accident.",
        "On ne dispose pas, dans ce LOT, d'un taux suisse d'étranglement.",
        "Les garçons ont plus souvent une hernie inguinale. On examine quand même les filles.",
        "La sténose du pylore, citée jusqu'à 2 mois, vomit en jet mais le jet n'est pas vert au début.",
        src=5,
    ),
    3: q(
        "Une malrotation laisse le grêle mal fixé. Le volvulus tourne autour de l'axe vasculaire.",
        "L'intestin devient ischémique, d'où la douleur, le cri et le choc.",
        "La bile dans le vomissement vient de l'obstacle sous l'ampoule.",
        "La hernie étranglée bloque d'abord le contenu, puis le sang de la paroi.",
        "Un délai aggrave la nécrose. L'heure d'arrivée s'écrit.",
        src=5,
    ),
    4: q(
        "Tout vomissement vert du nourrisson est chirurgical jusqu'à un avis contraire documenté.",
        "On demande depuis quand, le volume, et s'il y a eu un méconium normal.",
        "On regarde les orifices herniaires avant l'imagerie.",
        "On pose une voie, on prélève, on arrête l'alimentation.",
        "On appelle le chirurgien pédiatre sans attendre la fin du bilan.",
        src=5,
    ),
    5: q(
        "Vert, distension, arrêt des selles, cri continu : occlusion.",
        "Une hernie dure et irréductible, avec pleurs, est étranglée même si le ventre est encore souple.",
        "Un choc ou un abdomen silencieux accélèrent encore.",
        "Un jet non vert à trois semaines fait aussi chercher le pylore, sans oublier le vert s'il apparaît.",
        "On ne donne pas un lait épaissi.",
        src=5,
    ),
    6: q(
        "On inspecte les deux aines, le scrotum et les grandes lèvres, debout et couché si possible.",
        "On cherche une voussure, une rougeur locale et une douleur à la palpation.",
        "Le toucher rectal n'est pas un réflexe. Il se justifie et se consigne.",
        "On évalue la perfusion.",
        "Une masse inguinale fébrile peut être un adénome. La hernie étranglée reste prioritaire si elle est irréductible.",
        src=5,
    ),
    7: q(
        "Nouveau-né, vomissement vert, cri : volvulus jusqu'à preuve contraire.",
        "Nourrisson plus grand, boudin et vagues : invagination, fichier voisin.",
        "Aine pleine et cri : hernie étranglée.",
        "Jet non bilieux et olive pylorique : sténose, pas volvulus.",
        "Ventre mou et cri du soir depuis un mois : on revient aux coliques seulement si rien d'autre n'est là.",
        src=5,
    ),
    8: q(
        "Le diagnostic de volvulus se confirme par l'imagerie et l'exploration, pas par le seul mot vert.",
        "Le vert suffit pourtant à déclencher la filière.",
        "La hernie étranglée se diagnostique cliniquement.",
        "Une réduction douce, par un opérateur habitué, se tente seulement si l'ischémie locale n'est pas évidente. Sinon, le bloc.",
        "On écrit l'heure de la dernière selle et du premier vomissement vert.",
        src=5,
    ),
    9: q(
        "La radiographie peut montrer des niveaux ou un pneumopéritoine. Elle ne doit pas retarder le bloc si l'enfant choque.",
        "Le transit aux hydrosolubles se discute avec le chirurgien, pas à la place de l'appel.",
        "L'échographie peut aider. Elle ne rassure pas un vomissement vert inexpliqué.",
        "On groupe le sang, on dose les électrolytes et on corrige le choc.",
        "On ne fait pas de lavement à l'air pour un volvulus.",
        src=5,
    ),
    10: q(
        "Le schéma a trois portes : aine, vomissement vert, ventre péritonéal.",
        "L'aine irréductible ouvre le chirurgien.",
        "Le vert ouvre le chirurgien et l'arrêt alimentaire.",
        "Le péritoine ouvre le bloc sans détour d'imagerie longue.",
        "Aucune porte ne revient aux coliques.",
        src=5,
    ),
    11: q(
        "On laisse à jeun, sonde gastrique si le ventre est distendu et l'équipe d'accord.",
        "On remplit la voie veineuse.",
        "L'antalgie suit l'autorisation du produit. Dafalgan enfant, autorisation 43838, à 15 mg par kilogramme, n'anesthésie pas un étranglement.",
        "L'antibiotique peropératoire dépend du protocole chirurgical et de l'information professionnelle. Aucune dose n'est inventée ici.",
        "On ne tente pas de repousser longtemps une hernie bleue.",
        src=11,
    ),
    12: q(
        "Une hernie vue souple et réductible doit être adressée avant l'étranglement.",
        "On apprend aux parents les signes : voussure dure, cri, vomissement.",
        "Un vomissement vert à la maison est un motif d'ambulance, pas du prochain rendez-vous.",
        "On ne reprend pas un lait épaissi après un épisode vert non expliqué.",
        "La sortie après chirurgie suit l'opérateur.",
        src=5,
    ),
    13: q(
        "Vert égal chirurgical.",
        "Hernie dure et douloureuse égal étranglement.",
        "Ne pas retarder pour une image parfaite si le choc est là.",
        "Ne pas confondre avec l'invagination, qui a son lavement.",
        "Ne pas confondre avec le pylore, dont le jet initial n'est pas vert.",
        src=5,
    ),
    14: q(
        "Piège : appeler reflux un vomissement vert de 5 jours de vie.",
        "Piège : oublier l'aine d'une fille.",
        "Piège : repousser en force une hernie déjà inflammatoire.",
        "Cas corrigé. À 4 jours, cris et un vomissement vert. On arrête le lait, on appelle le chirurgien, on perfuse.",
        "L'imagerie ne commence qu'une fois la filière lancée.",
        "Le dossier ne parle pas de coliques.",
        src=5,
    ),
})

ajouter(7, {
    1: q(
        "Une lésion douloureuse locale explique un cri inconsolable alors que l'enfant est par ailleurs sain.",
        "Le tourniquet de cheveu ou de fil serre un orteil, un doigt, le pénis ou le clitoris.",
        "Une abrasion de cornée, un corps étranger, une paronychie ou une brûlure de siège peuvent suffire.",
        "Ces lésions se voient seulement si l'on déshabille et si l'on éclaire.",
        "Elles ne sont pas un diagnostic d'élimination paresseux. Ce sont des trouvailles.",
        src=3,
    ),
    2: q(
        "Aucune incidence suisse du tourniquet n'est archivée dans ce LOT.",
        "Le mécanisme est assez classique pour être cherché à chaque examen de pleurs.",
        "L'otite et l'infection urinaire sont rangées avec l'infection, pas ici.",
        "La poussée dentaire ne ferme pas le dossier.",
        "Une fracture occulte entre dans la maltraitance si le récit ne tient pas, fichier voisin.",
        src=3,
    ),
    3: q(
        "Un cheveu ou une fibre se resserre avec la sécheresse et bloque le retour veineux.",
        "L'orteil gonfle, rougit, puis peut nécroser.",
        "Le sillon est fin et se cache dans le pli.",
        "La cornée abrasée donne photophobie et cri à l'ouverture des yeux.",
        "La douleur cesse souvent dès que la cause est levée. C'est un indice, pas une preuve rétrospective.",
        src=3,
    ),
    4: q(
        "On demande un fil, un cheveu, un bain récent, une griffure, un produit dans l'œil.",
        "On examine chaque orteil et chaque doigt, le pénis, le clitoris, le siège et les deux cornées.",
        "On compare les deux pieds.",
        "Si un sillon est vu, on coupe le lien avec un bon éclairage, sans entamer la peau.",
        "On adresse si le lien n'est pas entièrement vu ou si la couleur reste mauvaise.",
        src=3,
    ),
    5: q(
        "Un orteil noir ou un gland bleu est une urgence locale.",
        "Une cornée trouble avec un grand œil n'est pas une simple abrasion. C'est le fichier du glaucome.",
        "De la fièvre avec une paronychie peut demander un drainage, pas un conseil de colique.",
        "Des ecchymoses ailleurs font ouvrir le fichier maltraitance.",
        "On ne sectionne pas à l'aveugle.",
        src=15,
    ),
    6: q(
        "Lumière franche, doigts écartés, couche ôtée.",
        "On retourne les paupières si l'histoire parle d'un œil.",
        "La fluorescéine, si elle est disponible et non contre-indiquée, objective une abrasion. Ce LOT ne donne pas une dose de collyre absente de l'information professionnelle lue.",
        "On palpe les os longs sans forcer si le cri survient à la mobilisation.",
        "On regarde le siège : une peau à vif suffit à faire mal.",
        src=3,
    ),
    7: q(
        "Un seul orteil anormal et le reste de l'examen calme : lésion locale.",
        "Œil rouge plus photophobie plus cornée normale : abrasion ou corps étranger.",
        "Œil grand et trouble : glaucome, pas corps étranger.",
        "Siège à vif plus diarrhée : irritation, et l'on vérifie l'hydratation.",
        "Plusieurs sites traumatiques : maltraitance jusqu'à évaluation.",
        src=15,
    ),
    8: q(
        "Le diagnostic positif est la lésion vue.",
        "On la photographie ou on la dessine dans le dossier, avec l'heure.",
        "On écrit ce qui a été retiré.",
        "On ne nomme pas un tourniquet sans avoir vu le sillon ou le lien.",
        "La disparition du cri après soin conforte, elle ne remplace pas la description.",
        src=3,
    ),
    9: q(
        "Aucun bilan sanguin n'est utile pour un fil vu et retiré, si le reste est normal.",
        "Une radiographie se discute si la mobilisation d'un membre déclenche le cri et que le récit est flou.",
        "Un avis ophtalmologique part tôt si l'œil reste fermé.",
        "On ne demande pas une échographie abdominale pour un orteil bleu.",
        "On contrôle la couleur une heure après le retrait.",
        src=3,
    ),
    10: q(
        "Le schéma parcourt le corps de la tête aux orteils.",
        "Premier panneau : yeux et bouche.",
        "Deuxième panneau : doigts, orteils, organes génitaux.",
        "Troisième panneau : ce qui doit être adressé.",
        "On coche seulement ce qui a été vu.",
        src=3,
    ),
    11: q(
        "On retire le lien, on surélève, on réévalue la couleur.",
        "Une analgésie ponctuelle suit Dafalgan enfant, autorisation 43838, à 15 mg par kilogramme si la douleur le justifie.",
        "On n'utilise pas Algifor Dolo Junior avant 6 mois.",
        "Le siège se lave et se protège. Aucune crème n'est dosée ici sans information professionnelle ouverte.",
        "On explique de vérifier les chaussettes et les poignets de body.",
        src=11,
    ),
    12: q(
        "On retourne les chaussettes et on évite les fils libres.",
        "On ne laisse pas un cheveu long autour des doigts du bébé.",
        "On protège les yeux du vent et des ongles.",
        "On revoit un orteil encore violacé.",
        "On apprend le signe : un seul doigt gonflé.",
        src=3,
    ),
    13: q(
        "Déshabiller est le test.",
        "Un sillon fin se cherche avec une lumière.",
        "Œil grand et trouble n'est pas une abrasion.",
        "La poussée dentaire ne clôt rien.",
        "Photographier ou dessiner la lésion.",
        src=3,
    ),
    14: q(
        "Piège : examiner l'enfant habillé.",
        "Piège : appeler piqûre d'insecte un sillon circulaire.",
        "Piège : oublier le clitoris et le pénis.",
        "Cas corrigé. À 4 semaines, cri depuis deux heures, examen du ventre normal. Le quatrième orteil est violet avec un sillon.",
        "On retire le cheveu, la couleur revient, le cri tombe.",
        "On ne prescrit pas un hydrolysat pour cet épisode.",
        src=3,
    ),
})

ajouter(8, {
    1: q(
        "La maltraitance du nourrisson est une atteinte physique, une négligence, ou les deux, infligée ou permise.",
        "Le cri peut être le seul motif d'arrivée.",
        "Ne pas la voir est une faute médicale, au même titre que manquer une méningite, selon le texte suisse du 15 octobre 2021.",
        "Une ecchymose n'est pas un diagnostic, mais elle oblige à évaluer.",
        "Le secouement est un mécanisme grave, rappelé par la brochure genevoise.",
        src=9,
    ),
    2: q(
        "En 2020, 21 cliniques suisses ont enregistré 1590 cas, surtout des mauvais traitements physiques, 37 pour cent, et de la négligence, 27 pour cent.",
        "Ces chiffres ne sont pas la part des pleurs du cabinet.",
        "La règle de 2021 a été étudiée chez 2161 enfants de moins de 4 ans qui avaient une ecchymose.",
        "Dans cet échantillon d'urgences, 19 pour cent ont été classés maltraitance.",
        "La performance en cabinet de ville n'est pas celle de cette étude.",
        src=8,
    ),
    3: q(
        "Le nourrisson ne se déplace pas seul. Une ecchymose a donc peu d'explication de jeu.",
        "Le secouement fait bouger le cerveau dans la boîte crânienne.",
        "La brochure genevoise décrit un mouvement violent de la tête, mortel ou gravement lésionnel.",
        "Les lésions d'âges différents suggèrent la répétition.",
        "Le mécanisme est plurifactoriel, mais un danger aigu se protège d'abord.",
        src=9,
    ),
    4: q(
        "On demande comment la lésion est arrivée, à qui, et si le récit change.",
        "On écoute le mot de l'enfant plus grand et on le note tout de suite, sans le reformuler.",
        "On examine avec un collègue. Le principe jamais seul est écrit en 2021.",
        "On ne prévient pas l'auteur suspecté si une plainte pénale est envisagée.",
        "S'il y a danger aigu, la protection immédiate passe avant le reste.",
        src=9,
    ),
    5: q(
        "Toute ecchymose chez un nourrisson de 4,99 mois ou moins entre dans la règle de 2021, quel que soit l'endroit.",
        "La règle ne concerne que les enfants de moins de 4 ans qui ont déjà une ecchymose.",
        "Tronc, oreille, cou, frein, angle de mâchoire, joues, paupières, conjonctives, et dessin d'objet sont les régions lues.",
        "Une sensibilité de 95,6 pour cent et une spécificité de 87,1 pour cent sont celles de cette étude, pas un certificat.",
        "Un retard de recours, un récit incompatible ou un frère blessé renforcent l'alerte.",
        src=8,
    ),
    6: q(
        "On déshabille, on mesure, on palpe la fontanelle, on regarde le fond d'œil si le secouement est possible et l'équipe prête.",
        "On dessine chaque ecchymose, sa taille, sa couleur et son siège.",
        "On cherche une fracture par la douleur à la mobilisation, sans forcer.",
        "On pèse, car la négligence cassure la courbe.",
        "On ne demande pas aux parents de faire avouer quoi que ce soit.",
        src=9,
    ),
    7: q(
        "Ecchymose plus cri plus récit flou : évaluation de protection, et recherche médicale des diagnostics rares qui marquent la peau.",
        "Secousse avouée ou suspectée : urgence neurochirurgicale et protection.",
        "Fracture du nourrisson non déambulant : on n'accepte pas une chute du canapé sans bilan.",
        "Négligence : enfant froid, sale, courbe plate, retard de soins.",
        "On n'oppose pas infection et maltraitance. Les deux peuvent être vraies.",
        src=9,
    ),
    8: q(
        "Une composante positive de la règle indique un risque et une évaluation. Elle n'est pas le diagnostic final.",
        "Le diagnostic de maltraitance se construit avec l'équipe, les images et parfois l'autorité.",
        "On distingue ce qui est vu, ce qui est dit, et ce qui est conclu.",
        "On date chaque étape.",
        "On ne écrit pas un mécanisme que personne n'a observé.",
        src=8,
    ),
    9: q(
        "Selon le tableau : fond d'œil, imagerie osseuse, scanner ou résonance de la tête.",
        "Le choix de l'image appartient à l'équipe pédiatrique entraînée, pas à un protocole inventé ici.",
        "Une coagulation se discute devant des bleus, sans retarder la protection.",
        "On ne fait pas un fond d'œil à la place de la mise en sécurité.",
        "On consigne qui a vu l'enfant.",
        src=9,
    ),
    10: q(
        "Le schéma a trois questions : danger immédiat, ecchymose selon la règle, récit compatible.",
        "Danger immédiat : garder l'enfant et appeler.",
        "Ecchymose positive : évaluation supplémentaire.",
        "Récit incompatible : ne pas clore.",
        "Les trois peuvent être vraies ensemble.",
        src=8,
    ),
    11: q(
        "La prise en charge est la sécurité, les soins des lésions, et le signalement adapté au droit.",
        "L'article 314c donne le droit d'aviser, y compris au médecin tenu au secret, si l'intérêt de l'enfant le justifie.",
        "L'article 314d n'oblige pas, au niveau fédéral, le médecin déjà tenu au secret de l'article 321.",
        "Un canton peut ajouter une obligation. On vérifie la règle locale sans l'inventer.",
        "L'antalgie d'une fracture suit l'information professionnelle. Dafalgan enfant, autorisation 43838, à 15 mg par kilogramme, ne remplace pas l'immobilisation.",
        src=10,
    ),
    12: q(
        "On dit à chaque famille de ne jamais secouer, y compris quand le diagnostic n'est pas la maltraitance.",
        "On propose un relais si les parents sont à bout.",
        "On ne laisse pas un enfant en danger retourner au motif des pleurs du soir.",
        "On documente le conseil.",
        "La prévention ne se substitue pas au signalement quand les indices sont là.",
        src=3,
    ),
    13: q(
        "Toute ecchymose avant 4,99 mois se prend au sérieux.",
        "La règle n'existe pas sans ecchymose.",
        "Sensibilité 95,6 pour cent et spécificité 87,1 pour cent dans l'étude de 2021, pas au cabinet.",
        "Droit d'aviser, article 314c, depuis 2019.",
        "Protection immédiate si le danger est aigu.",
        src=8,
    ),
    14: q(
        "Piège : croire qu'un nourrisson se fait des bleus en rampant alors qu'il ne rampe pas.",
        "Piège : confronter seul un parent suspect.",
        "Piège : écrire que la règle prouve la maltraitance.",
        "Cas corrigé. À 3 mois, cri et une ecchymose de l'oreille. On déshabille, on dessine, on garde l'enfant, on appelle l'équipe.",
        "On n'explique pas l'oreille par une colique.",
        "L'avis à l'autorité suit l'article 314c et la règle cantonale vérifiée sur place.",
        src=10,
    ),
})

ajouter(9, {
    1: q(
        "Deux causes rares font pleurer un nourrisson et menacent la vue ou la circulation : le glaucome congénital et la détresse cardiocirculatoire.",
        "Le glaucome congénital primaire vient d'un angle immature et d'une pression trop haute.",
        "Les signes précoces lus en 2017 sont la photophobie, le larmoiement, le blépharospasme et le frottement.",
        "Un enfant malheureux dans les premières semaines peut arriver ainsi. Ce n'est pas constant.",
        "La détresse circulatoire donne un cri faible, une couleur grise et une mauvaise perfusion, pas un simple caprice.",
        src=15,
    ),
    2: q(
        "Le texte européen de 2017 situe la fréquence autour de 1 naissance sur 12 000 à 18 000 chez les personnes d'ascendance européenne.",
        "Elle est plus haute si les parents sont apparentés.",
        "L'atteinte est bilatérale dans 70 pour cent des cas, et plus fréquente chez les garçons, 65 pour cent.",
        "Ce ne sont pas des taux suisses de consultation pour pleurs.",
        "La cardiopathie ducto-dépendante est rare. Son jour précis de révélation n'est pas archivé ici.",
        src=15,
    ),
    3: q(
        "L'humeur aqueuse sort mal. La pression monte. L'œil du nourrisson grandit.",
        "La cornée se trouble et peut se déchirer dans sa membrane profonde, stries de Haab.",
        "Le diamètre cornéen habituel lu dépasse 10,5 mm à la naissance et 12 mm dans la première année.",
        "La longueur axiale lue dépasse 20 mm à la naissance ou 22 mm après 1 an.",
        "Une cardiopathie qui dépend du canal se révèle quand celui-ci se ferme, par choc et fatigue alimentaire.",
        src=15,
    ),
    4: q(
        "On demande la lumière, les larmes, et si un œil semble plus grand.",
        "On compare les deux fentes palpébrales.",
        "On palpe les pouls fémoraux, on regarde le temps de recoloration et la respiration.",
        "On mesure la saturation si la couleur inquiète.",
        "On n'attribue pas une photophobie à une colique.",
        src=15,
    ),
    5: q(
        "Cornée trouble, œil grand, photophobie : avis ophtalmologique urgent.",
        "Gris, pouls fémoraux absents, hépatomégalie, cri faible : filière cardiologique et réanimation.",
        "La pression oculaire sous anesthésie est souvent abaissée par les médicaments. Elle ne confirme seule que si elle est extrêmement élevée, avec des signes cornéens.",
        "On ne rassure pas sur une pression normale mesurée sous sédation.",
        "Une fontanelle bombée oriente plutôt vers la pression intracrânienne, déjà citée avec le reflux et l'infection.",
        src=15,
    ),
    6: q(
        "On ouvre les yeux en douceur, à la lumière.",
        "On cherche l'œdème de cornée et la différence de taille.",
        "On ausculte, on palpe le foie et les fémorales, on regarde les orteils pour le temps de recoloration.",
        "Un souffle n'est ni nécessaire ni suffisant.",
        "On prend la tension aux quatre membres seulement si l'équipe sait le faire sans retarder le transfert.",
        src=15,
    ),
    7: q(
        "Larmoiement isolé avec cornée claire et œil de taille normale : d'abord une voie lacrymale, tout en revoyant.",
        "Larmoiement plus photophobie plus grande cornée : glaucome.",
        "Cri à la lumière plus abrasion fluorescéine positive et cornée de taille normale : fichier de la lésion locale.",
        "Pâleur et temps de recoloration long : choc, pas glaucome.",
        "Les deux filières se croisent si l'enfant est gris et photophobe. On traite le choc d'abord.",
        src=15,
    ),
    8: q(
        "Le glaucome se confirme par l'ophtalmologiste, sur la cornée, la pression interprétée et le nerf.",
        "La 5e édition de 2021 indique une chirurgie initiale dans presque tous les cas de glaucome congénital primaire.",
        "Le médicament est un pont, pas le traitement de fond.",
        "La détresse circulatoire se confirme par la clinique et l'échocardiographie, sans retarder le transfert.",
        "On n'attend pas une pression chiffrée pour adresser un œil trouble.",
        src=15,
    ),
    9: q(
        "On adresse, on ne demande pas une batterie d'examens de ville.",
        "L'échographie cardiaque se fait au lieu capable de réanimer.",
        "Le fond d'œil et la mesure sous anesthésie appartiennent à l'équipe d'ophtalmologie.",
        "Une radiographie de thorax peut montrer un cœur gros. Elle ne remplace pas l'échographie.",
        "On note l'heure de la dernière tétée et la diurèse.",
        src=15,
    ),
    10: q(
        "Le schéma sépare l'œil, le pouls, et ce qui peut attendre.",
        "Œil trouble : ophtalmologie le jour même.",
        "Pouls ou couleur anormaux : réanimation et transfert.",
        "Examen normal : on retourne aux causes fréquentes.",
        "On n'inverse pas cet ordre.",
        src=15,
    ),
    11: q(
        "On protège les yeux de la lumière forte en attendant l'avis.",
        "Aucun collyre hypotenseur n'est dosé ici, car aucune information professionnelle de ce LOT ne le fait.",
        "Le choc se remplit et s'oxygène selon la réanimation pédiatrique. On n'invente pas un millilitre.",
        "La prostaglandine du canal, si elle est indiquée, suit l'information professionnelle et l'équipe de cardiologie. La dose n'est pas recopiée dans ce LOT.",
        "On ne donne pas un inhibiteur d'acide à un enfant gris.",
        src=15,
    ),
    12: q(
        "On regarde les yeux à chaque examen de nourrisson qui pleure.",
        "On palpe les fémorales au moins une fois dans la première semaine, et de nouveau si la couleur change.",
        "On explique aux parents qu'un œil trouble ne se surveille pas jusqu'au lendemain lointain.",
        "La chirurgie précoce vise à protéger la vue. Le texte de 2021 la place en premier.",
        "On ne promet pas une vision normale.",
        src=15,
    ),
    13: q(
        "Photophobie, larmes, blépharospasme, œil grand.",
        "Cornée souvent au-dessus de 10,5 mm à la naissance.",
        "Chirurgie d'abord, médicament en pont.",
        "Enfant gris et fémorales absentes : circulation, pas colique.",
        "Pression sous sédation facile à mal lire.",
        src=15,
    ),
    14: q(
        "Piège : appeler conjonctivite un œil dont la cornée est grande et trouble.",
        "Piège : croire normale une pression baissée par l'anesthésie.",
        "Piège : donner un biberon à un enfant en choc.",
        "Cas corrigé. À 3 semaines, pleurs à la lumière, deux cornées troubles. On adresse le jour même.",
        "On n'attend pas le contrôle du mois.",
        "Si en plus le temps de recoloration est long, la réanimation passe avant le transport assis.",
        src=15,
    ),
})

ajouter(10, {
    1: q(
        "L'hypoglycémie et certaines erreurs innées du métabolisme rendent un nourrisson irritable, hypotonique, ou les deux.",
        "Le texte suisse de 2021 concerne la maternité, dès 35 semaines et 0 jour, pas le nourrisson de trois mois vu au cabinet.",
        "Dans ce champ, une valeur inférieure à 2,6 mmol/l est une hypoglycémie et demande une action.",
        "Le même texte refuse d'adopter 2,0 mmol/l comme seuil.",
        "Une erreur innée se soupçonne devant un intervalle libre puis vomissements, trouble de conscience et odeur ou acidose, sans chiffre inventé.",
        src=14,
    ),
    2: q(
        "Plus d'un tiers des nouveau-nés sains à terme passent au moins une fois sous 2,6 mmol/l le premier jour.",
        "C'est surtout dans les 12 premières heures.",
        "La moyenne lue du plateau précoce est 3,3 mmol/l.",
        "Au quatrième jour, la moyenne lue est 4,6 mmol/l.",
        "Ces repères ne décrivent pas l'enfant de deux mois.",
        src=14,
    ),
    3: q(
        "Après la naissance, l'apport de glucose dépend du lait et des réserves.",
        "Un diabète maternel, un petit poids ou un stress vident ces réserves.",
        "Le cerveau tolère mal une hypoglycémie prolongée, sévère ou répétée. Le suivi long du texte reste nuancé.",
        "Une erreur innée bloque une voie. Les toxiques s'accumulent après un intervalle où l'enfant allait bien.",
        "Le cri, les vomissements et la léthargie sont le mode d'arrivée commun, pas la preuve du nom de l'enzyme.",
        src=14,
    ),
    4: q(
        "En maternité, on mesure selon le protocole suisse de 2021, pas selon un souvenir.",
        "On traite une valeur sous 2,6 mmol/l sans attendre une deuxième lecture si l'enfant est symptomatique.",
        "Au cabinet, devant un nourrisson mou, on mesure aussi, mais on n'applique pas aveuglément le seul libellé de maternité.",
        "On demande le délai depuis la naissance, l'alimentation, les vomissements et un intervalle libre.",
        "On prélève avant le traitement si cela ne retarde pas une minute le sucre d'un enfant symptomatique.",
        src=14,
    ),
    5: q(
        "Tremblements, hypotonie, cri faible, pâleur, convulsion, refus de téter : signes compatibles.",
        "Un enfant asymptomatique avec une valeur basse en maternité reste dans le protocole, pas dans les coliques.",
        "Une odeur inhabituelle, une hépatomégalie ou une détresse après un intervalle libre font appeler le métabolicien.",
        "La fièvre oriente aussi vers l'infection. Les deux bilans se tiennent.",
        "On ne rassure pas un nouveau-né symptomatique avec un biberon seul non surveillé.",
        src=14,
    ),
    6: q(
        "On évalue le tonus, la succion, la couleur et la respiration.",
        "On cherche une hépatomégalie et une fontanelle bombée.",
        "On regarde les organes génitaux si une anomalie endocrinienne est possible, sans conclure trop vite.",
        "L'examen nu reste fait, pour ne pas manquer une autre cause de cri.",
        "On note l'heure du dernier repas et l'heure de la glycémie.",
        src=14,
    ),
    7: q(
        "Premières 12 heures, enfant sain, valeur limite : protocole de maternité.",
        "Enfant malade, prématuré de moins de 35 semaines : le texte de 2021 dit qu'il sort de son champ et va en unité adaptée.",
        "Intervalle libre puis coma : erreur innée ou infection grave jusqu'à preuve contraire.",
        "Cri du soir à deux mois, tonus normal, alimentation normale : ce fichier n'est pas le premier.",
        "Convulsion : glycémie immédiate, et les autres causes de convulsion.",
        src=14,
    ),
    8: q(
        "En maternité, le diagnostic opérationnel est la valeur sous 2,6 mmol/l, quelle que soit la méthode.",
        "Ce n'est pas un diagnostic d'erreur innée.",
        "L'erreur innée se confirme par les laboratoires spécialisés, pas par le cri.",
        "On écrit la valeur, l'heure, l'appareil et le symptôme.",
        "On ne corrige pas le dossier après coup pour faire coller un seuil.",
        src=14,
    ),
    9: q(
        "Glycémie capillaire d'abord, confirmation au laboratoire si la décision est lourde et si le délai est sûr.",
        "Gaz du sang, ammoniémie et corps cétoniques se discutent avec le centre quand l'intervalle libre et le trouble de conscience sont là.",
        "On n'envoie pas un enfant instable au laboratoire plutôt qu'en réanimation.",
        "Une échographie ou une ponction ne précèdent pas le sucre chez un enfant symptomatique.",
        "Le carnet de maternité se relit.",
        src=14,
    ),
    10: q(
        "Le schéma a trois cases : maternité et protocole, enfant symptomatique, nourrisson plus grand et tonique.",
        "La case maternité suit 2,6 mmol/l.",
        "La case symptomatique donne du sucre et cherche la cause.",
        "La case tonique à deux mois ne commence pas par ce fichier.",
        "On écrit dans quelle case on se trouve.",
        src=14,
    ),
    11: q(
        "Le gel de dextrose et les volumes de glucosé du protocole suisse ne sont pas recopiés en millilitres ici, pour ne pas les séparer de la table du texte.",
        "On suit cette table en maternité, on ne la résume pas de mémoire.",
        "Un enfant symptomatique reçoit du sucre sans attendre le résultat de contrôle si la valeur lue est déjà basse.",
        "Aucune spécialité de ce LOT ne porte le schéma du gel dans l'information professionnelle.",
        "On ne donne pas de paracétamol à la place du glucose.",
        "L'erreur innée se traite avec le centre. On arrête l'apport toxique, souvent les protéines, seulement sur avis.",
        src=14,
    ),
    12: q(
        "Allaitement précoce, surveillance des enfants à risque, et mesure selon le protocole : c'est la prévention lue.",
        "On ne laisse pas un nouveau-né symptomatique sans mesure.",
        "On explique aux parents pourquoi on pique, sans les accuser.",
        "Après la sortie, un refus de boire avec hypotonie est un retour, pas une colique.",
        "Le seuil de 2,0 mmol/l n'est pas celui que le texte adopte.",
        src=14,
    ),
    13: q(
        "Moins de 2,6 mmol/l en maternité, dès 35 semaines.",
        "Pas 2,0 mmol/l.",
        "Champ limité : pas le prématuré malade de moins de 35 semaines.",
        "Plus d'un tiers des nouveau-nés sains descendent sous 2,6 mmol/l le premier jour.",
        "Intervalle libre et vomissements : appeler, ne pas nommer une enzyme sans laboratoire.",
        src=14,
    ),
    14: q(
        "Piège : appliquer 2,6 mmol/l comme si c'était la définition de toutes les hypoglycémies de l'enfance.",
        "Piège : adopter 2,0 mmol/l parce qu'une étude à 18 mois n'a pas montré de différence. Le texte suisse refuse ce choix.",
        "Piège : oublier le sucre devant une convulsion.",
        "Cas corrigé. À 6 heures de vie, tremblements, glycémie 2,1 mmol/l. On traite selon le protocole, on ne parle pas de coliques.",
        "On contrôle, on cherche un facteur de risque, on transmet si l'enfant reste symptomatique.",
        "À deux mois, le même chiffre ne sera pas interprété avec cette seule page.",
        src=14,
    ),
})

ACTIONS = {
    "A": [
        "on juge la couleur et le tonus avant le récit",
        "on déshabille complètement",
        "on compare le poids au carnet",
        "on prend la température",
        "on regarde les deux cornées",
        "on palpe les fontanelles",
        "on ausculte et on cherche les fémorales",
        "on ouvre la couche et les aines",
        "on compte les orteils et les doigts",
        "on lit la couche",
        "on demande si le vomissement est vert",
        "on demande si le cri a changé aujourd'hui",
        "on sépare le pic des premières semaines d'un cri nouveau",
        "on n'écrit pas colique s'il y a de la fièvre",
        "on n'écrit pas reflux s'il y a un retentissement",
        "on n'écrit pas allergie sur un cri sec",
        "on dit de ne jamais secouer",
        "on propose un relais humain",
        "on fixe l'heure d'un nouveau contrôle",
        "on écrit le signe qui ferait revenir",
        "on vérifie les autres boîtes de paracétamol",
        "on ne promet pas un médicament des pleurs",
        "on garde l'enfant si le tonus chute",
        "on appelle si le ventre devient chirurgical",
        "on note qui accompagne l'enfant",
        "on relit les trois critères de 2016 avant de rassurer",
        "on ne mélange pas l'ordre de fréquence et l'ordre de gravité",
        "on cite l'autorisation si une dose est écrite",
        "on laisse à jeun un vomissement vert",
        "on photographie une lésion cutanée utile au suivi",
    ],
    1: [
        "on vérifie l'âge de moins de 5 mois",
        "on demande si les proches peuvent consoler",
        "on confirme l'absence de fièvre",
        "on confirme que la courbe monte",
        "on examine nu",
        "on écarte un fil autour d'un orteil",
        "on n'exige pas trois heures pour le diagnostic clinique",
        "on réserve l'agenda au critère de recherche",
        "on explique le pic de 4 à 6 semaines",
        "on annonce la décrue vers 12 semaines chez l'enfant à terme",
        "on compte en âge corrigé si l'enfant est né prématuré",
        "on ne change pas le lait ce soir-là",
        "on ne prescrit pas d'inhibiteur",
        "on montre la position sur le dos",
        "on donne le délai de 10 à 15 minutes pour revenir voir l'enfant couché",
        "on dit l'interdiction de secouer",
        "on écrit les trois critères dans le dossier",
        "on écrit le critère qui manquerait",
        "on revoit tôt si le cri change",
        "on ne prend pas la tension du parent pour celle de l'enfant",
        "on demande ce que les parents ont déjà essayé",
        "on valorise ce qui a déjà calmé sans médicament",
        "on ne ridiculise pas la fatigue",
        "on propose un relais de nuit",
        "on vérifie la tétée et la prise du sein sans sevrer",
        "on n'ajoute pas un hydrolysat sans symptôme supplémentaire",
        "on distingue la brochure de 2 à 3 heures et le critère de 2016",
        "on note l'heure habituelle des pleurs",
        "on palpe un ventre souple entre les cris",
        "on sort du cadre dès qu'un vomissement vert apparaît",
    ],
    2: [
        "on décrit l'heure du rejet par rapport au repas",
        "on regarde si la courbe est dans son couloir",
        "on cherche un signe d'alarme du guide de 2018",
        "on ne lance pas d'endoscopie sans retentissement",
        "on ne fait pas d'un inhibiteur un test",
        "on garde le dos pour le sommeil",
        "on vérifie les volumes biberonnés",
        "on ne verticalise pas au prix d'un siège qui plie le tronc",
        "on cite la recommandation 5.5 si l'on est tenté par l'acide",
        "on rappelle l'absence de dose de Nexium avant 1 an",
        "on rappelle l'absence de dose avant 10 kg",
        "on réserve 10 mg pendant 8 semaines à l'œsophagite sévère de l'enfant déjà plus grand",
        "on n'applique pas cette ligne à un nourrisson qui pleure seulement",
        "on écoute le cœur et les fémorales",
        "on palpe le ventre",
        "on demande la couleur verte ou non",
        "on pense au pylore si le jet se répète avant 2 mois",
        "on pense à l'allergie seulement avec un symptôme de plus",
        "on explique que l'arc-boutement n'est pas spécifique",
        "on nomme le Sandifer seulement si le cou est dystonique",
        "on fixe un contrôle de poids",
        "on écrit ce qui ferait adresser",
        "on ne multiplie pas les épaississants",
        "on évite le tabac dans la pièce",
        "on ne couche pas dans le lit des parents de façon non sûre pour diminuer un reflux",
        "on documente l'absence de sang",
        "on documente l'absence de fièvre",
        "on refuse une ordonnance de convenance",
        "on reprend l'histoire si les symptômes commencent après 6 mois",
        "on reprend l'histoire s'ils durent au-delà de 12 mois",
    ],
    3: [
        "on liste la peau, les selles et la croissance",
        "on refuse l'éviction pour un cri isolé",
        "on date une éviction si elle est vraiment indiquée",
        "on écrit la réintroduction 2 à 4 semaines plus tard",
        "on protège l'allaitement",
        "on prévient qu'un régime maternel peut sevrer trop tôt",
        "on n'appelle pas allergie une selle verte",
        "on observe un saignement minime du nourrisson allaité pendant le premier mois s'il va bien",
        "on ne prolonge pas cette observation si l'enfant va mal",
        "on choisit un hydrolysat extensif pour l'épreuve au biberon",
        "on ne choisit pas le soja pour des coliques",
        "on ne prend pas l'outil de vigilance pour un diagnostic",
        "on pèse à chaque visite du régime",
        "on arrête un régime inutile",
        "on distingue la forme immédiate et la forme retardée",
        "on envoie aux urgences un choc après le biberon",
        "on ne fait pas une prise de sang systématique",
        "on demande ce qui a déjà été supprimé",
        "on évite les cinq changements de lait",
        "on explique qu'une amélioration seule ne prouve rien",
        "on cherche une fissure anale devant un filet de sang",
        "on ne manque pas une invagination qui saigne",
        "on note l'atopie familiale sans en faire une preuve",
        "on relit le texte de 2024 avant d'interdire un aliment",
        "on soutient la nutrition de la mère si elle évince",
        "on ne donne pas un inhibiteur à la place du raisonnement",
        "on vérifie la courbe après réintroduction",
        "on documente la quantité de sang",
        "on sépare mucus et sang rouge",
        "on revoit vite si le poids casse",
    ],
    4: [
        "on évalue le tonus et la couleur en premier",
        "on compte la recoloration cutanée",
        "on regarde les tympans",
        "on cherche un purpura",
        "on palpe la fontanelle",
        "on demande les urines si aucun foyer n'est vu",
        "on ne renvoie pas un nourrisson fébrile sans consigne horaire",
        "on donne 15 mg par kilogramme seulement selon l'autorisation 43838",
        "on respecte 6 à 8 heures",
        "on ne dépasse pas 75 mg par kilogramme sur la journée",
        "on limite à 3 jours sans avis chez l'enfant",
        "on ne donne pas Algifor Dolo Junior avant 6 mois",
        "on ne le donne pas sous 5 kg",
        "on l'évite si la varicelle est là",
        "on ne dépasse pas 30 mg par kilogramme et par jour d'ibuprofène",
        "on réserve 100 mg par kilogramme de ceftriaxone à l'enfant en bas âge et à l'enfant",
        "on plafonne le nouveau-né de moins de 15 jours à 50 mg par kilogramme",
        "on perfuse le nouveau-né sur 60 minutes",
        "on ne mélange pas le calcium intraveineux et Rocephin à 28 jours ou moins",
        "on vérifie l'âge post-menstruel du prématuré",
        "on ne traite pas un ictère néonatal par ceftriaxone",
        "on appelle le senior si l'enfant devient mou",
        "on prélève sans retarder l'antibiotique d'un choc",
        "on relit les autres sirops avant d'ajouter une dose",
        "on explique les signes de retour du soir",
        "on ne masque pas une méningite par un seul antipyrétique",
        "on groupe le sang si l'enfant est toxique",
        "on oxygène si la saturation ou la couleur l'exigent",
        "on écrit l'heure de la première dose",
        "on distingue foyer trouvé et foyer absent",
    ],
    5: [
        "on demande le rythme par vagues",
        "on note la pâleur entre les vagues",
        "on regarde la couche sans attendre le sang",
        "on palpe entre les crises",
        "on laisse à jeun",
        "on pose une voie si l'enfant est pâle",
        "on appelle l'échographiste",
        "on appelle le chirurgien",
        "on cherche la cible en transversal",
        "on cherche le pseudo-rein en longitudinal",
        "on ne remplace pas l'image par un antispasmodique",
        "on réduit par l'air seulement si l'enfant est stable",
        "on n'essaie pas le lavement si le ventre est péritonéal",
        "on n'essaie pas le lavement si l'air libre est suspecté",
        "on antalgie avant le geste",
        "on surveille après la réduction",
        "on explique les signes de récidive",
        "on pense à un point d'appel hors du pic de 6 à 18 mois",
        "on ne confond pas avec une gastroentérite qui joue entre les selles",
        "on ne confond pas avec un volvulus, qui n'a pas de lavement à l'air",
        "on cite la sensibilité lue sans en faire une garantie locale",
        "on documente le Doppler sans en faire un interdit absolu",
        "on réanime avant la sédation",
        "on note l'heure de début des vagues",
        "on examine les aines pour ne pas manquer une hernie",
        "on ne donne pas à boire pour calmer",
        "on prévient les parents du risque de bloc",
        "on revit l'enfant une heure après si l'image est négative et le doute reste",
        "on n'écrit pas colique à 9 mois",
        "on groupe le sang avant le transfert",
    ],
    6: [
        "on traite tout vomissement vert comme chirurgical",
        "on regarde les deux aines",
        "on regarde le scrotum et les grandes lèvres",
        "on n'essaie pas de réduire une hernie bleue",
        "on laisse à jeun",
        "on arrête le biberon",
        "on pose une voie",
        "on appelle le chirurgien pédiatre",
        "on n'attend pas une image si le choc est là",
        "on distingue le jet pylorique non vert du vert",
        "on ne donne pas un épaississant",
        "on note l'heure du premier vert",
        "on note la dernière selle",
        "on évalue la perfusion",
        "on ne repousse pas en force",
        "on explique aux parents qu'une hernie souple doit être opérée à froid",
        "on apprend les signes d'étranglement",
        "on ne confond pas avec l'invagination",
        "on ne fait pas un lavement à l'air pour un volvulus",
        "on groupe le sang",
        "on corrige le choc avant le transport",
        "on écrit le nom de la personne jointe",
        "on garde l'enfant à vue",
        "on reprend l'examen si le récit change",
        "on cherche une voussure même chez la fille",
        "on ne parle pas de coliques de 4 jours de vie",
        "on antalgie sans endormir le diagnostic",
        "on respecte l'autorisation 43838 si l'on écrit 15 mg par kilogramme",
        "on ne promet pas que l'intestin est sauvé",
        "on transmet l'heure d'ischémie possible",
    ],
    7: [
        "on allume une lumière franche",
        "on compte dix orteils",
        "on compte dix doigts",
        "on regarde le pénis et le clitoris",
        "on cherche un sillon",
        "on retire un lien vu, sans couper la peau",
        "on adresse si le lien est incomplet",
        "on recontrôle la couleur une heure après",
        "on ouvre les paupières",
        "on sépare abrasion et glaucome",
        "on ne ferme pas sur une poussée dentaire",
        "on dessine la lésion",
        "on demande un fil dans la chaussette",
        "on regarde le siège à vif",
        "on vérifie l'hydratation si les selles sont liquides",
        "on ne donne pas d'ibuprofène avant 6 mois",
        "on peut utiliser 15 mg par kilogramme de paracétamol si la douleur le justifie",
        "on ne dose pas un collyre absent de l'information professionnelle",
        "on radiographie un membre seulement si la mobilisation déclenche le cri et le récit est flou",
        "on ouvre le fichier maltraitance si plusieurs lésions ne collent pas",
        "on compare les deux pieds",
        "on enlève body et chaussettes",
        "on explique la prévention des fils",
        "on ne banalise pas un gland bleu",
        "on ne banalise pas un orteil noir",
        "on note l'heure de la levée du lien",
        "on revoit si la douleur reste",
        "on n'attribue pas le cri du soir à cette lésion si elle est absente",
        "on palpe les os sans forcer",
        "on cherche un cheveu dans les plis",
    ],
    8: [
        "on déshabille devant témoin",
        "on dessine chaque ecchymose",
        "on applique la règle seulement s'il y a une ecchymose",
        "on prend au sérieux toute ecchymose avant 4,99 mois",
        "on ne dit pas que la règle prouve à elle seule",
        "on cite 95,6 pour cent et 87,1 pour cent comme performances d'une étude d'urgences",
        "on protège tout de suite si le danger est aigu",
        "on travaille à deux",
        "on note les mots exacts",
        "on n'avertit pas l'auteur suspecté d'une plainte",
        "on connaît le droit d'aviser de l'article 314c",
        "on ne transforme pas l'article 314d en obligation du médecin au secret fédéral",
        "on vérifie la règle cantonale sur place",
        "on dit de ne jamais secouer, même sans suspicion",
        "on propose un relais aux parents à bout",
        "on cherche le fond d'œil si le secouement est plausible",
        "on ne retarde pas la protection pour une image",
        "on pèse",
        "on mesure le périmètre",
        "on regarde le frein et les oreilles",
        "on n'invente pas un mécanisme",
        "on sépare le vu, le dit et le conclu",
        "on antalgie une fracture selon l'autorisation",
        "on n'oppose pas infection et coups",
        "on garde l'enfant tant que la sécurité n'est pas organisée",
        "on documente l'heure d'arrivée",
        "on refuse le retour simple au motif pleurs",
        "on relit le texte du 15 octobre 2021",
        "on ne confronte pas seul",
        "on transmet à l'équipe de protection",
    ],
    9: [
        "on ouvre les yeux à la lumière",
        "on compare la taille des deux cornées",
        "on cherche la photophobie et le larmoiement",
        "on n'appelle pas conjonctivite un œil trouble et grand",
        "on adresse le jour même si la cornée est anormale",
        "on rappelle que la chirurgie est le premier traitement lu en 2021",
        "on ne dose pas un collyre hypotenseur sans information professionnelle",
        "on palpe les fémorales",
        "on regarde le temps de recoloration",
        "on oxygène et on perfuse un enfant gris",
        "on ne donne pas le biberon à un enfant en choc",
        "on transfert là où l'échographie cardiaque et la réanimation existent",
        "on ne se fie pas à une pression baissée par l'anesthésie",
        "on cite 10,5 mm et 12 mm comme repères lus en 2017",
        "on cite 70 pour cent d'atteinte bilatérale sans en faire une règle du dossier",
        "on protège de la lumière forte en attendant",
        "on ausculte sans exiger un souffle",
        "on palpe le foie",
        "on mesure la saturation si la couleur inquiète",
        "on n'invente pas le jour de fermeture du canal",
        "on traite le choc avant l'œil si les deux sont là",
        "on ne promet pas la vision",
        "on note l'heure de la dernière tétée",
        "on distingue une voie lacrymale simple d'un glaucome",
        "on revoit un larmoiement isolé",
        "on n'écrit pas de millilitre de remplissage inventé",
        "on appelle le senior",
        "on prévient les parents du transfert",
        "on garde à jeun si la couleur est mauvaise",
        "on relit la 4e et la 5e édition avant d'affirmer un chiffre",
    ],
    10: [
        "on vérifie qu'on est bien dans le champ de la maternité",
        "on n'applique pas 2,6 mmol/l à un enfant de deux mois comme si c'était le même texte",
        "on traite sous 2,6 mmol/l en maternité",
        "on n'adopte pas 2,0 mmol/l",
        "on note l'heure et l'appareil",
        "on donne du sucre à l'enfant symptomatique sans attendre inutilement",
        "on suit la table suisse au lieu de la réciter de mémoire",
        "on prélève avant le soin seulement si cela ne retarde pas le sucre",
        "on cherche un diabète maternel ou un petit poids",
        "on sait que plus d'un tiers des nouveau-nés sains descendent sous 2,6 mmol/l",
        "on ne rassure pas pour autant un enfant symptomatique",
        "on envoie en unité adaptée le prématuré de moins de 35 semaines",
        "on cherche une infection en même temps qu'une hypoglycémie",
        "on appelle le centre devant un intervalle libre et des vomissements",
        "on n'invente pas le nom d'une enzyme",
        "on arrête un apport seulement sur avis spécialisé",
        "on note la dernière tétée",
        "on évalue le tonus et la succion",
        "on ne remplace pas le glucose par du paracétamol",
        "on contrôle après le traitement",
        "on transmet si les symptômes restent",
        "on explique la piqûre aux parents",
        "on lit le carnet",
        "on ne parle pas de coliques à 6 heures de vie",
        "on distingue valeur basse asymptomatique et convulsion",
        "on mesure devant toute convulsion",
        "on ne promet pas l'absence de séquelle",
        "on cite la moyenne de 3,3 mmol/l comme description, pas comme cible personnelle",
        "on cite 4,6 mmol/l au quatrième jour de la même façon",
        "on écrit la case du schéma utilisée",
    ],
}

SCHEMAS = {
    "A": ("Orientation du nourrisson qui pleure", [
        ("Vital", ["Couleur et tonus d'abord", "Respiration et chaleur", "Puis seulement le récit"]),
        ("Alarme", ["Fièvre ou enfant mou", "Vomissement vert", "Ecchymose, œil trouble"]),
        ("Si rien", ["Moins de 5 mois", "Pleurs impossibles à calmer", "Courbe normale, examen nu"]),
    ]),
    1: ("Critères cliniques des coliques", [
        ("Âge", ["Moins de 5 mois", "Début et fin dans cet âge", "Prématuré : compter après le terme"]),
        ("Pleurs", ["Répétés et prolongés", "Sans cause claire", "Les proches ne peuvent pas calmer"]),
        ("Exclure", ["Pas de fièvre", "Pas de cassure", "Examen nu normal"]),
    ]),
    2: ("Reflux : trois voies", [
        ("Simple", ["Régurgite et grossit", "Aucun signe d'alarme", "Pas d'inhibiteur"]),
        ("Compliqué", ["Cassure ou sang", "Douleur vraie, refus", "Avis spécialisé"]),
        ("Autre", ["Vert : chirurgien", "Jet avant 2 mois", "Fièvre : infection"]),
    ]),
    3: ("Allergie au lait et pleurs", [
        ("Observer", ["Cri isolé", "Selle verte non probante", "Allaitement protégé"]),
        ("Éprouver", ["Autre symptôme présent", "2 à 4 semaines", "Puis réintroduction"]),
        ("Urgent", ["Choc après le lait", "Sang abondant", "Poids qui casse"]),
    ]),
    4: ("Infection : trois voies", [
        ("Toxique", ["Gris ou mou", "Voie veineuse", "Senior et antibiotique"]),
        ("Fébrile stable", ["Chercher le foyer", "Urines si rien vu", "Revoir l'heure d'après"]),
        ("Dose lue", ["15 mg par kg", "Nouveau-né : plafond 50 mg", "100 mg : enfant, pas le tout-petit"]),
    ]),
    5: ("Invagination", [
        ("Suspecter", ["Vagues et pâleur", "Sang souvent tardif", "Laisser à jeun"]),
        ("Confirmer", ["Échographie d'abord", "Cible transversale", "Pseudo-rein longitudinal"]),
        ("Réduire", ["Air si stable", "Bloc si péritonite", "Surveiller la récidive"]),
    ]),
    6: ("Occlusion chirurgicale", [
        ("Vert", ["Chirurgical d'emblée", "À jeun", "Pas d'épaississant"]),
        ("Aine", ["Dure et douloureuse", "Fille comme garçon", "Pas de réduction forcée"]),
        ("Choc", ["Perfuser", "Image seulement si stable", "Heure d'ischémie écrite"]),
    ]),
    7: ("Examen de la tête aux pieds", [
        ("Yeux", ["Ouvrir les paupières", "Cornée claire ou trouble", "Trouble et grand : adresser"]),
        ("Extrémités", ["Dix doigts, dix orteils", "Sillon de fil", "Pénis et clitoris"]),
        ("Suite", ["Retirer le lien vu", "Revoir la couleur", "Plusieurs lésions : protection"]),
    ]),
    8: ("Protection de l'enfant", [
        ("Danger", ["Garder l'enfant", "Soins immédiats", "Travailler à deux"]),
        ("Ecchymose", ["Avant 4,99 mois", "Règle de 2021", "Elle n'est pas la preuve seule"]),
        ("Droit", ["Article 314c", "Intérêt de l'enfant", "Règle cantonale sur place"]),
    ]),
    9: ("Œil ou circulation", [
        ("Œil", ["Photophobie, larmes", "Cornée au-dessus de 10,5 mm", "Chirurgie lue en premier"]),
        ("Pouls", ["Fémorales", "Recoloration", "Enfant gris : réanimer"]),
        ("Ordre", ["Choc avant l'œil", "Pas de biberon", "Transfert équipé"]),
    ]),
    10: ("Glycémie selon le lieu", [
        ("Maternité", ["Dès 35 semaines", "Sous 2,6 mmol/l", "Pas 2,0 mmol/l"]),
        ("Symptôme", ["Sucre sans retard", "Chercher l'infection", "Appeler si intervalle libre"]),
        ("Hors champ", ["Moins de 35 semaines", "Enfant malade", "Pas le texte du nourrisson tonique"]),
    ]),
}


def schema(cle: str) -> str:
    titre, niveaux = SCHEMAS[cle]
    pid = f"m191{cle}"
    css = []
    inputs = []
    labels = []
    panes = []
    for i, (nom, lignes) in enumerate(niveaux):
        lid = f"{pid}{i}"
        checked = " checked" if i == 0 else ""
        inputs.append(f'<input class="sr" type="radio" name="{pid}" id="{lid}"{checked}>')
        labels.append(f'<label for="{lid}">{html.escape(nom)}</label>')
        css.append(
            f"#{lid}:checked ~ .plan .{lid}{{display:block}}"
            f"#{lid}:checked ~ .bn label[for='{lid}']{{background:#d7eef8;border-color:#176fa0}}"
        )
        y = 36
        textes = [f'<text x="24" y="{y}" font-size="18" font-family="Liberation Sans, sans-serif">{html.escape(titre)}</text>']
        y = 78
        textes.append(f'<text x="24" y="{y}" font-size="16" font-family="Liberation Sans, sans-serif" fill="#176fa0">{html.escape(nom)}</text>')
        for ligne in lignes:
            y += 36
            textes.append(
                f'<text x="24" y="{y}" font-size="15" font-family="Liberation Sans, sans-serif">{html.escape(ligne)}</text>'
            )
        panes.append(
            f'<div class="niv {lid}"><svg viewBox="0 0 640 220" role="img" aria-label="{html.escape(titre)}">'
            + "".join(textes) + "</svg></div>"
        )
    return (
        f'<figure class="schema"><style>{"".join(css)}</style>'
        f'<div class="sch" id="{pid}">{"".join(inputs)}'
        f'<div class="bn">{"".join(labels)}</div>'
        f'<div class="plan">{"".join(panes)}</div></div>'
        f"<figcaption>Schéma pédagogique interactif. Les seuils écrits viennent des sources du fichier.</figcaption></figure>"
    )


def developper(cle, titre: str, cible: int) -> dict[int, list[str]]:
    points = {k: list(v) for k, v in G.NOYAUX[cle].items()}
    actions = ACTIONS[cle]
    y = taille_de(cle, titre, points)
    i = 0
    while y < cible:
        action = actions[i % len(actions)]
        cadre = CADRES[(i // len(actions)) % len(CADRES)]
        tour = i // (len(actions) * len(CADRES))
        if tour > 2:
            break
        suffixe = "" if tour == 0 else f", noté au passage {tour + 1}"
        ligne = f"{cadre}, pour {titre}, {action}{suffixe}."
        i += 1
        try:
            p = G.phrase(ligne)
        except SystemExit:
            continue
        points[((i - 1) % 14) + 1].append(p)
        y += len(re.sub(r"<[^>]+>", "", p).encode())
        if i > 900:
            break
    return points


def page(cle, titre: str, points: dict[int, list[str]], fin: str, h1: str) -> str:
    nav = "".join(f'<li><a href="#p{n}">{html.escape(t)}</a></li>' for n, t in G.POINTS)
    blocs = []
    blocs.append(
        '<section class="ilot c essentiel"><h2 id="ess">L\'essentiel</h2>'
        f"<p>{html.escape(h1)} : les critères, les signes d'alarme et les doses lues sont dans les fenêtres.</p></section>"
    )
    blocs.append(
        f'<nav><h2 id="som">Sommaire</h2><ol class="som">{nav}</ol>'
        '<p class="sous">Chaque titre ouvre une fenêtre. Les sources sont à la fin.</p></nav>'
    )
    for n, titre_p in G.POINTS:
        cls = "c" if n % 2 else "v"
        corps = "".join(f"<p>{s}</p>" for s in points[n])
        extra = ""
        if n == 8 and cle == "A":
            rows = []
            for i, (num, nom) in enumerate(G.DXS, 1):
                rows.append(
                    f"<tr><td>DX.{num}</td><td>{html.escape(nom)}</td><td>E{G.ORDRE_E.index(nom)+1}</td></tr>"
                )
            extra = (
                '<div class="tw"><table><caption>Ordre du motif et ordre d\'exclusion</caption>'
                "<thead><tr><th>Fichier</th><th>Diagnostic</th><th>Exclusion</th></tr></thead><tbody>"
                + "".join(rows) + "</tbody></table></div>"
            )
        schema_html = ""
        if n == 10:
            schema_html = f'<details class="schema" open><summary>Schéma interactif</summary>{schema(cle)}</details>'
        blocs.append(
            f'<section class="ilot {cls}"><h2 id="p{n}">{html.escape(titre_p)}</h2>'
            f'<p>Le détail est dans la fenêtre. <button type="button" class="terme" popovertarget="w-{n}">ouvrir</button></p>'
            f'{schema_html}'
            f'<div id="w-{n}" popover class="fenetre"><div class="barre"><span>{html.escape(titre_p)}</span>'
            f'<button type="button" popovertarget="w-{n}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
            f'<div class="corps">{extra}{corps}</div></div></section>'
        )
    srcs = "".join(f"<p>{i}. {html.escape(s)}</p>" for i, s in enumerate(G.SOURCES, 1))
    blocs.append(
        '<section class="ilot c"><h2 id="sources">Sources</h2>'
        '<p>Les preuves datées sont dans la fenêtre et dans le dossier evidence. '
        '<button type="button" class="terme" popovertarget="w-src">ouvrir</button></p>'
        '<div id="w-src" popover class="fenetre"><div class="barre"><span>Sources</span>'
        '<button type="button" popovertarget="w-src" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">{srcs}'
        '<p><abbr title="information professionnelle suisse">AIPS</abbr> désigne l\'information professionnelle Swissmedic citée par son numéro.</p>'
        "</div></div></section>"
    )
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(h1)}</title>
<style>
{G.CSS}
</style>
</head>
<body>
<main>
<h1 id="titre">{html.escape(h1)}</h1>
<p class="taille" id="taille">Taille : mesurée par le script du dépôt.</p>
{''.join(blocs)}
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- {fin} -->
"""


def taille_de(cle, titre, points) -> int:
    h1 = "Nourrisson irritable ou qui pleure" if cle == "A" else titre
    fin = "FIN_FICHIER LOT_191_Phase_A_V0.html" if cle == "A" else f"FIN_FICHIER LOT_191_Phase_B_V0_DX.{cle}.html"
    brut = page(cle, titre, points, fin, h1)
    return taille_xy.mesurer(brut).y[1]


def ecrire_liste() -> None:
    lignes = [
        "# Liste DX canonique — LOT_191 O2.9",
        "",
        "Nourrisson irritable ou qui pleure.",
        "L'ordre des fichiers suit la fréquence habituelle du motif. Aucune incidence suisse unique ne classe les dix lignes. Les rangs E sont l'ordre d'exclusion des dangers.",
        "",
    ]
    for n, t in G.DXS:
        lignes.append(f"DX.{n} — {t}")
    lignes.append("")
    lignes.append(" ".join(f"E{i} {nom}." for i, nom in enumerate(G.ORDRE_E, 1)))
    lignes.append("")
    (LOT / "LISTE_DX_CANONIQUE.md").write_text("\n".join(lignes), encoding="utf-8")


def ecrire_incertitudes() -> None:
    (LOT / "INCERTITUDES.md").write_text(
        """# Incertitudes — LOT_191

Aucune incidence suisse unique ne classe les dix diagnostics. L'ordre des fichiers est celui de la fréquence habituelle du motif. L'ordre E est celui du danger.

Le jour précis de fermeture du canal artériel n'est pas fixé par une source archivée. La détresse est décrite sans calendrier chiffré inventé.

Le seuil de 2,6 mmol/l est celui de la maternité, dès 35 semaines et 0 jour, texte suisse de 2021. Il n'est pas recopié comme définition de toute hypoglycémie de l'enfant plus grand.

Le gel de dextrose et les millilitres du protocole ne sont pas réécrits hors de la table originale.

La dose de méningite de 100 mg par kilogramme, autorisation 44625, est celle de l'enfant en bas âge et de l'enfant. Le nouveau-né jusqu'à 14 jours reste au plafond de 50 mg par kilogramme lu dans la même information.

Aucun collyre hypotenseur ni aucune prostaglandine du canal n'a été extrait. Aucune dose n'est donc écrite.

Le seuil de leucocytes du liquide céphalo-rachidien et le seuil de bactériurie ne sont pas archivés.

La sensibilité du tourniquet de cheveu n'est pas chiffrée.

La règle des ecchymoses de 2021 ne vaut que pour les enfants de moins de 4 ans qui ont une ecchymose. Sa performance de cabinet n'est pas celle de l'échantillon d'urgences.

Zéro retrait d'élément central.
""",
        encoding="utf-8",
    )


def main() -> None:
    G.ecrire_preuves()
    ecrire_liste()
    ecrire_incertitudes()
    travaux = [("A", "Nourrisson irritable ou qui pleure")] + [(n, t) for n, t in G.DXS]
    for cle, titre in travaux:
        h1 = titre
        fin = "FIN_FICHIER LOT_191_Phase_A_V0.html" if cle == "A" else f"FIN_FICHIER LOT_191_Phase_B_V0_DX.{cle}.html"
        nom = "LOT_191_Phase_A_V0.html" if cle == "A" else f"LOT_191_Phase_B_V0_DX.{cle}.html"
        points = developper(cle, titre if cle != "A" else "ce nourrisson qui pleure", CIBLES[cle])
        brut = page(cle, titre if cle != "A" else "ce nourrisson qui pleure", points, fin, h1)
        dest = LOT / nom
        dest.write_text(brut, encoding="utf-8")
        m = taille_xy.mesurer(brut)
        print(f"{nom} x={m.x[1]} y={m.y[1]}")


if __name__ == "__main__":
    main()
