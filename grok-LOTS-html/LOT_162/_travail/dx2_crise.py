#!/usr/bin/env python3
"""DX.2 Crise thyréotoxique."""
from rendre_dx import rendre, P, S
from dx2_plus import PLUS
from moteur import btn, table

ess = P(
    "La crise thyréotoxique est une thyrotoxicose avec défaillance d'organe. "
    "Le diagnostic est clinique. Le score de Burch-Wartofsky et les critères japonais aident, toutes classes gardées. "
    "On donne le thionamide tout de suite, l'iode minéral au moins une heure après, le propranolol et l'hydrocortisone de stress. "
    "Le comprimé d'iodure nucléaire est contre-indiqué.",
    S(2, 5, 8, 10, 11, 12),
)

points = {
"p1": P("La crise est une thyrotoxicose qui décompense, pas un chiffre isolé. La ", btn("w-def", "définition"), " sépare la thyrotoxicose compensée de la tempête.", S(2)),
"p2": P("Elle est rare. Sa mortalité, dans les séries modernes, est haute. Les ", btn("w-epi", "chiffres"), " ne sont pas une prévalence de cabinet.", S(2)),
"p3": P("Trop d'hormone, un cœur qui lâche, un foie qui ictère, un cerveau qui s'agite. La ", btn("w-physio", "chaîne"), " explique l'ordre des médicaments.", S(2, 5)),
"p4": P("On reconnaît la défaillance, on confirme ou on suppose la thyrotoxicose, on score, on traite sans attendre le dossier parfait. Les ", btn("w-dem", "pas"), " sont ceux de l'heure.", S(5)),
"p5": P("L'arrêt du carbimazole, le contraste, l'infection, la chirurgie, l'accouchement. Les ", btn("w-ana", "précipitants"), " se cherchent en même temps que le traitement.", S(2)),
"p6": P("Température, conscience, pouls, poumons, ictère. L'", btn("w-ex", "examen"), " alimente le score, il ne le remplace pas.", S(5)),
"p7": P("Le syndrome est multisystémique. Le ", btn("w-syn", "tableau"), " et les ", btn("w-mimiques", "imitations"), " le distinguent d'une thyrotoxicose qui va encore au cabinet.", S(5)),
"p8": P("Deux systèmes, entiers. Le ", btn("w-score", "score"), ", les ", btn("w-jta", "critères japonais"), " et d'autres ", btn("w-plus", "calculs"), " se lisent ensemble.", S(5)),
"p9": P("Hormones, anticorps si l'on peut, pas de scintigraphie en urgence, pas de nouveau contraste. Les ", btn("w-examens", "examens"), " ne retardent pas la première dose.", S(2)),
"p10": P("Défaillance d'abord, mécanisme ensuite. L'", btn("w-arbre", "arbre"), " refuse le thionamide si la crise vient d'une destruction.", S(5)),
"p11": P("Propranolol, carbimazole, iode après, hydrocortisone. Le ", btn("w-ttt", "schéma suisse"), " et la ", btn("w-heure", "première demi-journée"), " ne dépassent pas les plafonds lus.", S(8, 10, 11, 12)),
"p12": P("Ne pas arrêter le thionamide, ne pas injecter de contraste à l'aveugle. La ", btn("w-prev", "prévention"), " évite la plupart des crises évitables.", S(1, 2)),
"p13": P("Clinique, score complet, ordre des médicaments, pas le comprimé nucléaire. Le ", btn("w-cles", "rappel"), " tient en une fenêtre.", S(5, 12)),
"p14": P("Les pièges sont le score chez un euthyroïdien, l'iode trop tôt, et le thionamide dans une thyroïdite. Les ", btn("w-pieges", "pièges"), " et le ", btn("w-cas", "cas"), " les montrent.", S(5)),
}

fens = []

def add(pid, wid, titre, *paras):
    fens.append((pid, wid, titre, "".join(paras)))

add("p1", "w-def", "Définition",
P("La crise thyréotoxique, ou tempête thyroïdienne, est une thyrotoxicose sévère avec décompensation systémique. La recommandation américaine de 2016 dit que le diagnostic se fait cliniquement chez un patient fortement thyrotoxique qui défaille. Un score aide. Il ne remplace pas le jugement, et il ne s'applique pas à un patient dont les hormones sont normales.", S(2)),
P("La thyrotoxicose compensée a des hormones hautes et un patient qui marche, parle, mange. La crise ajoute la fièvre haute, le trouble de conscience, les vomissements ou l'ictère, la fibrillation très rapide, l'insuffisance cardiaque. La frontière n'est pas un seul degré de température. C'est l'ensemble."),
P("Elle peut survenir sur un Basedow, un goitre multinodulaire, plus rarement une thyroïdite destructrice. Dans ce dernier cas le thionamide est inutile et dangereux : il n'arrête pas une fuite de stock. Le texte japonais de 2016 le dit explicitement.", S(5)),
P("On ne confond pas la crise avec une infection qui donne fièvre et tachycardie chez un patient euthyroïdien. Le score monterait. La recommandation de 2016 prévient : presque chaque signe de crise, sauf peut-être l'hyperthermie majeure, existe dans une maladie grave ordinaire. D'où l'exigence d'une thyrotoxicose vraie.", S(2)),
)

add("p2", "w-epi", "Rareté et mortalité",
P("La crise est rare. Les textes lus ne donnent pas une incidence suisse. Ils donnent une mortalité de 8 % à 25 % dans les séries modernes citées en 2016. Le texte japonais rappelle une mortalité encore autour de 11 % dans l'enquête nationale, avec défaillance multiviscérale et insuffisance cardiaque aiguë parmi les causes de décès. Ce sont des mortalités de patients déjà diagnostiqués, pas des prévalences de population.", S(2, 5)),
P("Environ un cinquième des crises japonaises survenaient sur un Basedow encore ignoré. D'où l'intérêt de penser à la thyroïde devant une fibrillation fébrile inexpliquée, sans pour autant traiter toute fibrillation par un thionamide.", S(5)),
P("Le patient âgé avec un goitre multinodulaire et un produit de contraste est le scénario que la revue lausannoise met en garde. Le tabac et l'âge augmentent ce type d'hyperthyroïdie. La femme jeune qui arrête son carbimazole est l'autre scénario classique.", S(1)),
)

add("p3", "w-physio", "Pourquoi cet ordre de médicaments",
P("L'hormone en excès accélère le cœur, augmente la consommation d'oxygène, peut précipiter une fibrillation et un œdème pulmonaire. Elle agite le cerveau jusqu'au délire, à la convulsion ou au coma. Elle accélère le transit et, dans les formes graves, lèse le foie jusqu'à l'ictère. La fièvre vient de la thermogenèse et parfois du facteur déclenchant.", S(2)),
P("Le thionamide bloque la fabrication nouvelle. Il ne vide pas le stock folliculaire. L'iode minéral, lui, bloque la libération et, par l'effet de Wolff-Chaikoff, l'organification. S'il est donné avant le thionamide, la glande peut utiliser cet iode pour fabriquer encore plus d'hormone. Le texte japonais de 2016 cite la recommandation américaine : l'iodure minéral au moins une heure après le thionamide.", S(5)),
P("Le propranolol ralentit le cœur et, accessoirement, diminue un peu la conversion de thyroxine en triiodothyronine. Le glucocorticoïde fait de même et couvre une surrénale qui peut être débordée. Le refroidissement et le remplissage traitent la conséquence, pas la glande. Aucun de ces gestes ne remplace les autres. La recommandation de 2016 parle d'une approche multimodale.", S(2, 10, 11)),
P("La demi-vie des hormones est de plusieurs jours. Même un traitement parfait ne normalise pas le chiffre en une heure. On juge la fréquence, la pression, la conscience, la diurèse, pas une thyroxine libre de contrôle à la sixième heure."),
)

add("p4", "w-dem", "Dans l'heure",
P("Reconnaître. Fièvre, agitation ou coma, vomissements ou ictère, fibrillation rapide, crépitants, chez quelqu'un qui a un goitre, un Basedow, ou un amaigrissement récent. On hospitalise en soins intensifs selon le tableau. On ne renvoie pas au cabinet avec une ordonnance de ville.", S(2)),
P("Prélever. Thyroxine libre, triiodothyronine libre, thyréostimuline, formule, ionogramme, foie, cortisol si le tube part. On ne retient pas le traitement pour le résultat. Si les hormones ne sont pas encore rendues, le critère japonais a une case TS2 pour cela.", S(5)),
P("Scorer. Toutes les classes du score de Burch-Wartofsky, puis les combinaisons japonaises. On écrit les points. On ne dit pas « score haut ».", S(5)),
P("Traiter dans l'ordre. Propranolol si la pression le permet. Carbimazole tout de suite, dose haute de la fourchette suisse sans dépasser 60 mg par jour. Au moins une heure après, iode minéral qui n'est pas le comprimé nucléaire. Hydrocortisone 100 mg puis 100 mg toutes les 6 heures selon le schéma de stress déjà écrit pour Solu-CORTEF. Refroidissement. Cause : infection, arrêt de traitement, contraste.", S(5, 8, 10, 11, 12)),
P("Réévaluer. Fréquence, pression, conscience, diurèse, température. Une aggravation malgré ce schéma fait discuter l'échange plasmatique ou la chirurgie en urgence, cités comme recours quand le traitement habituel échoue. On ne les décide pas seul au lit sans l'équipe.", S(2, 5)),
)

add("p5", "w-ana", "Précipitants",
P("Arrêt brutal du carbimazole ou du suivi. C'est le précipitant le plus pédagogique : le patient se sentait mieux, les boîtes étaient finies. On le cherche, on ne le gronde pas avant d'avoir traité.", S(2)),
P("Produit de contraste iodé, surtout sur un goitre multinodulaire. Amiodarone, même commencée récemment ou poursuivie. Chirurgie, thyroïdienne ou non, sur une thyrotoxicose ignorée. Accouchement. Infection. Traumatisme. Iode radioactif, rarement. Le texte de 2016 liste ces cadres.", S(1, 2)),
P("On demande l'heure du dernier comprimé, le nom du scanner, la date de l'amiodarone, une angine qui aurait fait arrêter le thionamide pour une agranulocytose vraie. Si l'arrêt était justifié par une agranulocytose, on ne reprend pas le carbimazole : on change de stratégie avec le spécialiste, iode minéral et bêtabloquant et glucocorticoïde pouvant tenir en attendant une chirurgie.", S(8)),
)

add("p6", "w-ex", "Examen qui remplit le score",
P("Température au dixième. 37,1 °C ne marque pas. 37,2 °C entre dans la première classe, 5 points. On ne regroupe pas « un peu de fièvre »."),
P("Fréquence sur une minute, ou sur le scope. 90 est le début des points. 140 ou plus vaut 25. Une fibrillation ajoute 10, que la fréquence soit déjà comptée ou non : les deux lignes existent, on les cote toutes les deux.", S(5)),
P("Poumons et pression. Crépitants des bases : insuffisance au moins légère ou modérée. Choc, orthopnée, galop : on discute la classe sévère, 15 points. On écrit ce qu'on a vu, pas la classe maximale par prudence systématique."),
P("Abdomen et peau. Vomissement, diarrhée, douleur : 10. Ictère : 20, pas en plus des vomissements. On ne cumule pas modéré et sévère. Une classe par domaine."),
P("Conscience. Agitation simple : 10. Délire, psychose, léthargie extrême : 20. Convulsion ou coma : 30. L'échelle de Glasgow à 14 ou moins entre dans le signe neurologique japonais, ce n'est pas une ligne du score de Burch-Wartofsky. On ne convertit pas l'un en l'autre.", S(5)),
)

add("p7", "w-syn", "Syndromes",
P("Crise certaine au sens du score : total 45 ou plus chez un patient thyrotoxique. Crise imminente : 25 à 44, traitement agressif selon le jugement, surveillance rapprochée au minimum. Crise peu probable : moins de 25. Ces trois lectures sont toutes gardées. On n'enseigne pas un seuil unique à 45 qui ferait ignorer la zone 25 à 44.", S(2, 5)),
P("TS1, première combinaison : thyrotoxicose et au moins un signe neurologique, plus un parmi fièvre d'au moins 38 °C, fréquence d'au moins 130, insuffisance cardiaque définie, atteinte digestive ou hépatique. TS1 alternative : trois de ces quatre signes sans exiger le neurologique. TS2 : deux de ces quatre. TS2 alternative : le tableau de TS1 mais les hormones libres manquent encore. Les quatre combinaisons restent. En exclure une amputte la classification.", S(5)),
P("Sepsis seul, coup de chaleur, syndrome malin des neuroleptiques, sevrage, phéochromocytome : ils imitent des lignes du score. La différence est la thyrotoxicose. On la cherche. On traite aussi l'infection si elle est là : elle est souvent le précipitant, pas un diagnostic de remplacement."),
)

score_tbl = table("Score de Burch-Wartofsky, toutes les classes, d'après le tableau japonais de 2016 repris de 1993.",
["Domaine", "Classe", "Points"],
[["Température", "37,2 à 37,7 °C", "5"],
 ["Température", "37,8 à 38,3 °C", "10"],
 ["Température", "38,4 à 38,8 °C", "15"],
 ["Température", "38,9 à 39,3 °C", "20"],
 ["Température", "39,4 à 39,9 °C", "25"],
 ["Température", "40,0 °C ou plus", "30"],
 ["Fréquence", "90 à 109", "5"],
 ["Fréquence", "110 à 119", "10"],
 ["Fréquence", "120 à 129", "15"],
 ["Fréquence", "130 à 139", "20"],
 ["Fréquence", "140 ou plus", "25"],
 ["Fibrillation", "absente ou présente", "0 ou 10"],
 ["Insuffisance cardiaque", "absente, légère, modérée, sévère", "0, 5, 10, 15"],
 ["Digestif et foie", "absent, modéré, ictère", "0, 10, 20"],
 ["Système nerveux", "absent, agitation, délire, convulsion ou coma", "0, 10, 20, 30"],
 ["Précipitant", "absent ou présent", "0 ou 10"]])

add("p8", "w-score", "Score entier et trois calculs",
P("Le score date de Burch et Wartofsky, 1993. Le tableau utilisé ici est celui publié en 2016 par la Japan Thyroid Association, qui le reprend en entier. Lecture : 45 ou plus, crise. 25 à 44, crise imminente. Moins de 25, peu probable. On ne traite pas un score, on traite un patient thyrotoxique dont le score éclaire la décision.", S(5)),
score_tbl,
P("Calcul 1. Température 38,6 °C : 15. Fréquence 132 : 20. Pas de fibrillation. Pas d'insuffisance cardiaque. Vomissements : 10. Agitation : 10. Arrêt du médicament : 10. Total 65. Au-dessus de 45. Traitement agressif.", S(5)),
P("Calcul 2. Température 37,9 °C : 10. Fibrillation à 124 : fréquence 15 plus fibrillation 10. Nausée : 10. Contraste : 10. Total 55. Encore au-dessus de 45. Le contraste n'interdit pas le thionamide. Il l'indique.", S(5)),
P("Calcul 3. Température 37,4 °C : 5. Pouls 96 : 5. Angine sans autre signe. Total 10. Crise peu probable. L'angine fait plutôt craindre l'agranulocytose : on arrête le carbimazole et on fait la formule. On ne démarre pas l'iode.", S(5, 8)),
P("Dans la série citée en 2016, le score à 45 ou plus repérait plus de patients cliniquement en crise que les seules catégories japonaises TS1 et TS2, mais il classait aussi des thyrotoxicoses compensées dans la zone imminente. D'où la consigne : entre 25 et 44, juger, surveiller, ne pas traiter par automatisme ni s'abstenir par automatisme.", S(2)),
)

add("p8", "w-jta", "Critères japonais, les quatre combinaisons",
P("Prérequis : thyrotoxicose avec T3 libre ou T4 libre élevées. Signes numérotés. Un : système nerveux, de l'agitation au coma, au moins 1 sur l'échelle japonaise de coma ou 14 ou moins sur l'échelle de Glasgow. Deux : fièvre au moins 38 °C. Trois : fréquence au moins 130, y compris en fibrillation. Quatre : insuffisance cardiaque, œdème pulmonaire, râles sur plus de la moitié des champs, choc, classe IV de la New York Heart Association ou Killip au moins III. Cinq : nausée, vomissement, diarrhée, ou bilirubine totale au moins 3 milligrammes par décilitre.", S(5)),
P("TS1 première : thyrotoxicose, au moins le signe neurologique, et au moins un parmi fièvre, tachycardie, insuffisance cardiaque, atteinte digestive. TS1 alternative : thyrotoxicose et au moins trois parmi ces quatre, sans exiger le neurologique. TS2 : thyrotoxicose et deux de ces quatre. TS2 alternative : même tableau que TS1 mais les hormones libres ne sont pas disponibles. On garde les quatre. Le système nerveux pèse plus lourd dans ce système que dans le score, ce que le texte japonais souligne.", S(5)),
P("Si une pneumonie explique clairement la fièvre, on peut l'écarter du critère. Si l'on hésite, le texte dit de garder le signe comme partie de la crise déclenchée par la pneumonie. On traite alors les deux : antibiotique et thyroïde.", S(5)),
P("Le seuil japonais de 130 par minute n'est pas le palier du score, qui commence à 90. Une fréquence à 120 cote dans le score et ne remplit pas à elle seule le critère japonais de tachycardie. On ne dit pas que les deux systèmes sont le même seuil.", S(5)),
)

add("p9", "w-examens", "Examens",
P("Thyroxine libre, triiodothyronine libre, thyréostimuline. Dans la maladie grave, la triiodothyronine libre peut être moins haute à cause de la basse conversion. Une thyroxine libre haute et une thyréostimuline effondrée suffisent à nommer la thyrotoxicose. Une triiodothyronine basse isolée en réanimation n'est pas une crise : c'est le syndrome de basse T3, qu'on ne traite pas par thionamide.", S(2, 3)),
P("Anticorps anti-récepteur si le tube part, pour le jour d'après. Il ne retarde pas le carbimazole. Une échographie au lit montrant un flux augmenté suggère un Basedow. Elle ne remplace pas le traitement.", S(2, 5)),
P("Pas de scintigraphie en urgence. Pas de nouveau produit de contraste. Pas de scanner injecté « pour voir ». Le précipitant est souvent déjà un contraste.", S(1)),
P("Formule, foie, glycémie, ionogramme, électrocardiogramme, recherche d'infection, cortisol. L'hydrocortisone ne s'attend pas si le patient défaille. On prélève le cortisol juste avant si c'est immédiat.", S(11)),
)

add("p10", "w-arbre", "Arbre",
P("Patient instable et thyrotoxicose connue ou très probable. On score. 45 ou plus, ou TS1, ou TS2 avec défaillance : protocole complet. 25 à 44 : soins rapprochés, traitement agressif si le tableau clinique défaille. Moins de 25 et patient stable : ce n'est pas ce chapitre, on revient à Basedow ou au nodule.", S(2, 5)),
P("Mécanisme. Basedow ou nodule : thionamide oui. Thyroïdite douloureuse, fixation connue basse, pas d'anticorps : thionamide non. Bêtabloquant, glucocorticoïde, parfois iode selon l'équipe, mais pas un carbimazole réflexe.", S(5)),
P("Agranulocytose documentée : pas de reprise du carbimazole. On tient avec le bêtabloquant, le glucocorticoïde, l'iode minéral après discussion, et la chirurgie si besoin. On ne « tente une petite dose ».", S(8)),
P("Amélioration. On baisse ensuite vers le schéma de ville : carbimazole d'entretien 5 à 20 mg, propranolol diminué, hydrocortisone arrêtée progressivement si elle a duré. On ne sort pas le patient sans consigne d'agranulocytose et sans rendez-vous.", S(8)),
)

add("p11", "w-ttt", "Doses que l'on peut écrire",
P("Propranolol Zentiva, numéro 47025. L'indication hyperthyroïdie et crises thyréotoxiques est écrite. Dose : 10-40 mg, 3 à 4 fois par jour. C'est la dose de cette ligne, pas celle de l'hypertension. Si le patient vomit tout, les comprimés ne passent pas : on ne invente pas une ampoule à partir de cette information professionnelle de comprimés. On demande ce qui est disponible et on s'en tient à une information lue.", S(10)),
P("Néo-Mercazole, numéro 21037. 20 à 60 mg par jour, en visant le haut de la fourchette dans la crise, sans dépasser 60 mg par jour. Ce plafond rejoint le maximum japonais du méthimazole dans la crise due à Basedow. Les doses plus hautes citées pour d'autres pays ne sont pas enseignées. Par sonde si besoin, dès que la voie digestive est ouverte. Le propylthiouracile n'a pas de spécialité dans l'index. Ross et al., Thyroid, 2016, écrivent pour la crise une charge de cinq cents à mille milligrammes, puis deux cent cinquante milligrammes toutes les quatre heures. C'est la recommandation, pas une information professionnelle suisse. Le carbimazole suisse reste plafonné à 60 mg par jour.", S(5, 8)),
P("Iode. Au moins une heure après la première dose de thionamide. La recommandation japonaise parle d'environ 200 milligrammes par jour d'iodure minéral, par la bouche, sous la langue, par sonde ou par voie rectale. Ce n'est pas Iodure de potassium axapharm, numéro 67017, dont la dose adulte nucléaire est 130.0 mg et qui est contre-indiqué dans l'hyperthyroïdie, Basedow et l'autonomie. On n'ouvre pas la boîte de blocage nucléaire au motif que c'est de l'iode.", S(5, 12)),
P("Hydrocortisone. Solu-CORTEF, numéro 23533. Le schéma de stress d'une intervention majeure, 100 mg intraveineux puis 100 mg toutes les 6 heures pendant au moins 72 heures, est la dose écrite que ce cours retient pour la crise. On le dit : la phrase d'origine vise le patient déjà cortiqué au bloc. On ne fabrique pas une dose de charge qui ne figure pas dans cette information professionnelle. On ne descend pas sous 25 mg par jour dans la mise en garde lue si l'on poursuit.", S(11)),
P("Refroidissement par moyens physiques, paracétamol si l'on en a l'indication et la dose lue ailleurs : ce cours ne fixe pas une dose de paracétamol. Remplissage prudent s'il y a des crépitants. Antibiotique si l'infection est le précipitant, selon son information professionnelle, pas une dose thyroïdienne.", S(2)),
P("Après la phase aiguë, le Basedow reprend son schéma : descente du carbimazole par paliers de 5 à 15 mg tous les dix jours vers 5 à 20 mg, durée ensuite selon les textes déjà cités. La crise ne raccourcit pas magiquement les mois de traitement.", S(8)),
)

add("p12", "w-prev", "Prévention",
P("Éduquer à ne pas arrêter le carbimazole. La différence avec l'arrêt pour fièvre doit être dite : fièvre, on arrête et on consulte le jour même. Boîte finie, on renouvelle, on ne disparaît pas.", S(2, 8)),
P("Avant un scanner injecté chez un patient qui a un goitre ou un Basedow non contrôlé, prévenir. La revue de 2010 met ce risque en tête des implications pratiques pour le goitre multinodulaire.", S(1)),
P("Avant une chirurgie programmée, euthyroïdie. La préparation par gouttes d'iode concerne le bloc du Basedow, pas le service de médecine le matin d'une crise. Cinq à sept gouttes de solution de Lugol, ou une à deux gouttes de solution saturée, trois fois par jour une dizaine de jours, est la phrase de 2016 pour la préparation opératoire. Ce n'est pas le traitement de la tempête déjà constituée, et ce n'est pas le comprimé 67017.", S(2, 12)),
P("Amiodarone : bilan avant, puis surveillance. Une thyrotoxicose qui s'installe se traite avant qu'elle ne devienne une crise. Le cardiologue reste dans la décision d'arrêter ou non.", S(4)),
)

add("p13", "w-cles", "Points d'examen",
P("Diagnostic clinique sur thyrotoxicose plus défaillance. Score entier : température dès 37,2 °C, fréquence dès 90, fibrillation 10, cœur jusqu'à 15, foie jusqu'à 20, cerveau jusqu'à 30, précipitant 10. 45 ou plus, 25 à 44, moins de 25. Quatre combinaisons japonaises, pas une seule.", S(5)),
P("Ordre : thionamide, puis au moins une heure, puis iode minéral. Propranolol 10-40 mg trois à quatre fois. Carbimazole au plus 60 mg par jour. Hydrocortisone 100 mg puis toutes les 6 heures. Pas 130.0 mg du comprimé nucléaire.", S(5, 8, 10, 11, 12)),
P("Pas de thionamide si destruction. Pas de score si hormones normales. Pas d'attente du laboratoire pour la première dose si le tableau est là.", S(2, 5)),
P("Mortalité citée 8 % à 25 %. Ce n'est pas une raison pour traiter large un patient stable. C'est une raison pour ne pas rater celui qui défaille.", S(2)),
)

fens.append(("p8", "w-plus", "Trois patients encore, et la relève", PLUS))

add("p14", "w-pieges", "Pièges",
P("Coter un sepsis sans thyrotoxicose et annoncer une crise. Le score n'est pas un diagnostic autonome.", S(2)),
P("Donner l'iode à l'arrivée et le carbimazole « quand la pharmacie ouvrira ». L'ordre est l'inverse.", S(5)),
P("Ouvrir la boîte d'iodure de potassium prévue pour l'accident nucléaire. Contre-indication écrite dans l'hyperthyroïdie.", S(12)),
P("Dépasser 60 mg de carbimazole parce qu'un texte étranger cite davantage. Le plafond suisse lu est 60 mg.", S(8)),
P("Reprendre le carbimazole chez un patient hospitalisé pour agranulocytose. Contre-indication.", S(8)),
P("Oublier le glucocorticoïde. Il fait partie du schéma multimodal et il précède toute lévothyroxine si une hypothyroïdie centrale ou une surrénale se discutent, ce qui n'est pas le cas typique de la crise mais reste la règle du coma, autre chapitre.", S(2, 3)),
P("Contrôler la thyroxine libre à la deuxième heure pour juger l'échec. La demi-vie ne le permet pas. On juge le patient."),
)

add("p11", "w-heure", "Heure par heure, la première demi-journée",
P("Minute 0. Le patient est en box. Scope, voie veineuse, oxygène si la saturation le demande. On annonce une crise probable sans attendre le laboratoire si le goitre, l'amaigrissement et la fibrillation fébrile sont déjà là. On prévient la réanimation.", S(2)),
P("Minute 10. Prélèvements. Hormones, formule, foie, gaz du sang si la conscience ou la fréquence respiratoire inquiète, cortisol, hémocultures si la fièvre peut être une infection. Électrocardiogramme. On ne part pas au scanner injecté."),
P("Minute 20. Propranolol par la bouche si le patient n'est pas en choc et s'il peut avaler : 10-40 mg, à répéter selon la ligne 3 à 4 fois par jour, numéro 47025. On note la pression avant et après. Un choc cardiogénique fait appeler la réanimation avant d'ajouter un bêtabloquant : la fiche de ville ne décrit pas le choc.", S(10)),
P("Minute 30. Carbimazole, jusqu'à 60 mg dans la journée, fractionné, numéro 21037, par sonde si les vomissements continuent. On note l'heure exacte. C'est l'heure zéro de l'iode.", S(8)),
P("Heure 2, au plus tôt une heure après le thionamide. Iode minéral, pas la boîte nucléaire. On écrit la voie et on dit pourquoi ce n'est pas 130.0 mg du numéro 67017. Hydrocortisone 100 mg intraveineux, numéro 23533, puis le rythme de 100 mg toutes les 6 heures.", S(5, 11, 12)),
P("Heures 3 à 6. Température, conscience, diurèse, crépitants. Refroidissement. Remplissage mesuré. Antibiotique seulement si l'infection est argumentée. On ne redose pas les hormones pour déclarer un échec. On ne donne pas une deuxième charge de carbimazole au-dessus du plafond quotidien.", S(8)),
P("Si l'agitation empêche les soins, on sédatif avec l'anesthésiste. Le texte japonais rappelle que la clairance de certains agents change dans la thyrotoxicose. On ne choisit pas une dose de sédatif dans cette leçon : elle n'a pas été lue dans une information professionnelle ouverte pour cet usage.", S(5)),
P("Fin de journée. Le patient est soit en amélioration clinique, soit discuté pour un recours (échange, chirurgie) avec endocrinologue, réanimateur et chirurgien. La lettre dit le score détaillé, l'heure du thionamide, l'heure de l'iode, les numéros Swissmedic. Elle ne dit pas « protocole de crise » sans ces heures.", S(5)),
)

add("p7", "w-mimiques", "Ce qui imite la crise",
P("Sepsis. Fièvre, tachycardie, confusion, parfois ictère. La thyréostimuline peut baisser dans la maladie grave sans que la thyroxine libre soit haute. Si la thyroxine libre est normale ou basse et la triiodothyronine basse, c'est le syndrome de basse T3 ou une autre maladie, pas une crise. On traite l'infection. On ne donne pas de carbimazole pour une thyréostimuline basse de réanimation.", S(3)),
P("Sevrage d'alcool ou intoxication. Agitation, tachycardie, parfois fièvre. Les hormones tranchent. En attendant, on ne cote pas un score de crise comme s'il prouvait la thyroïde.", S(2)),
P("Phéochromocytome et autres orages adrénergiques. Hypertension paroxystique, céphalée, sueurs. Le propranolol seul, sans alpha-blocage, est une mauvaise idée si c'est un phéochromocytome. L'information professionnelle du propranolol rappelle d'ailleurs, pour le phéochromocytome, de ne l'utiliser qu'après un alphabloquant. Devant un doute, on ne « couvre » pas par un bêtabloquant thyroïdien avant d'avoir vu les hormones et la pression.", S(10)),
P("Agranulocytose fébrile sous carbimazole. Angine, fièvre, patient déjà traité. Ce n'est pas une crise jusqu'à preuve d'une thyrotoxicose décompensée. C'est une urgence hématologique. On arrête le médicament. On ne le remplace pas par une dose plus forte.", S(8)),
P("Surdosage de lévothyroxine. Thyroxine très haute, thyroïde petite, pas de goitre, fixation nulle si on la faisait plus tard. Le thionamide ne retire pas les comprimés déjà absorbés. On arrête l'apport, on ralentit le cœur, on surveille. L'iode et le carbimazole ne sont pas le réflexe.", S(2, 9)),
P("Coma myxœdémateux. L'autre extrême : froid, lent, hormones basses. Le confondre mènerait à donner un thionamide à quelqu'un qui manque d'hormone. Température et sens des hormones séparent les deux chapitres.", S(3)),
)

add("p14", "w-cas", "Cas corrigé",
P("Énoncé. Homme de 67 ans, goitre multinodulaire, scanner injecté il y a deux jours. Il est agité, il a vomi deux fois, les conjonctives sont jaunes. Température 39,5 °C. Fréquence 146, irrégulière. Crépitants aux deux bases. Thyroxine libre 68 pmol/l, thyréostimuline indétectable. L'interne propose 130.0 mg d'iodure de potassium « parce que c'est de l'iode » et 80 mg de carbimazole « pour être large ». Corrigez."),
P("Score. Température 39,5 °C : classe 39,4 à 39,9, 25 points. Fréquence 146 : 25. Fibrillation : 10. Crépitants : insuffisance au moins modérée, 10, sévère seulement si le choc est là, ce qui n'est pas décrit. Ictère : 20. Agitation : 10. Contraste : 10. Total 25 + 25 + 10 + 10 + 20 + 10 + 10 = 110. Crise. Critère japonais : fièvre, tachycardie au-dessus de 130, insuffisance cardiaque, ictère, agitation. TS1.", S(5)),
P("Carbimazole : on refuse 80 mg. Le plafond de Néo-Mercazole est 60 mg par jour. On donne jusqu'à 60 mg, en prises fractionnées, par sonde s'il vomit, numéro 21037. Propranolol 10-40 mg trois à quatre fois si la pression tient, numéro 47025. Hydrocortisone 100 mg intraveineux puis 100 mg toutes les 6 heures, numéro 23533.", S(8, 10, 11)),
P("Iode : on refuse 130.0 mg du comprimé 67017, contre-indiqué dans l'hyperthyroïdie et l'autonomie. On donne l'iode minéral de la crise au moins une heure après le carbimazole, à la dose discutée d'environ 200 milligrammes par jour dans le texte japonais, par la voie que le patient tolère. On le dit à l'interne : ce n'est pas la même boîte.", S(5, 12)),
P("On cherche une infection, on ne fait pas un second scanner injecté, on prévient la réanimation. On n'attend pas l'anticorps pour la première dose. On expliquera plus tard la descente de dose et la consigne d'agranulocytose. Aujourd'hui, l'ordre et les plafonds suffisent à la correction.", S(2, 8)),
)

if __name__ == "__main__":
    print(rendre(2, "Crise thyréotoxique", ess, points, fens))
