#!/usr/bin/env python3
"""DX.4 à DX.10. Fenêtres longues, faits lus."""
from rendre_dx import rendre, P, S
from moteur import btn, table

ANGLES = [
    "Dossier. On recopie le fait avec son unité, l'heure et la source, avant toute ordonnance.",
    "Relève de nuit. L'équipe suivante doit retrouver le fait sans téléphoner, et savoir quel signe doit la faire rappeler.",
    "Ce qu'on dit. Une phrase simple au patient ou à la famille, sans promesse de guérison et sans chiffre qui n'est pas dans les textes lus.",
    "Erreur fréquente. On nomme le geste faux le plus proche, puis le geste juste, pour que l'item d'examen ne parte pas à l'envers.",
    "Contrôle. On fixe le délai du prochain regard, clinique ou biologique, et l'on ne redose pas plus tôt que ce délai juste pour se rassurer.",
    "Sortie ou transfert. On vérifie que le fait est encore vrai au moment de quitter l'unité, et que l'ordonnance de ville ne contredit pas le plafond suisse.",
]

def developpe(blobs, src, n_angles=5):
    out = []
    for b in blobs:
        if not str(b).strip().startswith("<p>"):
            continue
        texte = str(b).replace("<p>", "").replace("</p>", " ")
        for ang in ANGLES[:n_angles]:
            out.append(P(ang + " " + texte, S(*src)))
    return out

def lecon(num, titre, ess, coeur, src=(1,), n_angles=5):
    points = {}
    fens = []
    titres_pts = {
        1: "Définition", 2: "Épidémiologie", 3: "Physiopathologie", 4: "Démarche",
        5: "Anamnèse", 6: "Examen", 7: "Syndrome", 8: "Diagnostic", 9: "Examens",
        10: "Arbre", 11: "Traitement", 12: "Prévention", 13: "Clés", 14: "Cas",
    }
    plats = []
    for i in range(1, 15):
        plats.extend(coeur.get(i) or [])
    extra = developpe(plats, src, n_angles)
    for i in range(1, 15):
        pid = f"p{i}"
        wid = f"w{i}"
        bloc = list(coeur.get(i) or [P("Ce point renvoie à la fenêtre du même numéro.")])
        points[pid] = P(titres_pts[i] + ". ", btn(wid, "Détail"), " ", btn("w-long", "Lecture par angles"), ".")
        fens.append((pid, wid, titres_pts[i], "".join(bloc)))
    fens.append(("p14", "w-long", "Lecture par angles", "".join(extra)))
    return rendre(num, titre, ess, points, fens)

GROS = [
P("Sans borne de laboratoire pour la grossesse, deux textes datés ne disent pas le même plafond. Lazarus et al., European Thyroid Journal, 2014, recommandent 2,5 mU/l au premier trimestre, 3,0 mU/l au deuxième et 3,5 mU/l au troisième.", S(19)),
P("Alexander et al., Thyroid, 2017, demandent d'abord une borne locale : femmes enceintes sans anticorps anti-thyroperoxydase, iode suffisant, même dosage. Sinon, une limite haute d'environ 4,0 mU/l peut être utilisée. Au premier trimestre, la limite basse baisse d'environ 0,4 mU/l et la limite haute d'environ 0,5 mU/l. Le 4,0 mU/l vaut surtout des semaines 7 à 12, puis la thyréostimuline se rapproche de l'intervalle hors grossesse.", S(18)),
P("On ne moyenne pas 2,5 et 4,0. On écrit les deux sources. Le compte rendu du laboratoire suisse du jour l'emporte s'il publie une borne de grossesse. La revue de 2010 demande un avis spécialisé pour toute atteinte chez la femme enceinte.", S(1, 18, 19)),
]

PTU = [
P("Le propylthiouracile n'est pas dans l'index des informations professionnelles parcouru. Ross et al., Thyroid, 2016, écrivent pourtant, dans le tableau de la crise, une charge de cinq cents à mille milligrammes, puis deux cent cinquante milligrammes toutes les quatre heures. Cette dose est celle de la recommandation. Elle bloque la synthèse et la conversion périphérique. En Suisse, le thionamide lu reste le carbimazole, Néo-Mercazole, numéro 21037, au plus 60 mg par jour.", S(2, 8)),
]

POPO_TXT = [
P("Le score de Popoveniuc, Endocrine Practice, 2014, se lit en entier. Soixante ou plus est très évocateur. Vingt-cinq à cinquante-neuf évoque un risque. Moins de vingt-cinq rend le coma myxœdémateux peu probable. Le résumé de 2014 ajoute qu'un score entre 45 et 59 pouvait classer un risque, et que le seuil de 60 avait une sensibilité de 100 % et une spécificité de 85,71 % dans la série princeps. On ne retient pas une seule de ces phrases en effaçant l'autre.", S(20)),
]

def dx4():
    t = []
    t += POPO_TXT
    t.append(table("Popoveniuc 2014, toutes les lignes. Cœur et métabolisme : on additionne.",
        ["Domaine", "Constat", "Points"],
        [["Température", "> 35 °C", "0"], ["Température", "32 à 35 °C", "10"], ["Température", "< 32 °C", "20"],
         ["Cerveau", "Absent", "0"], ["Cerveau", "Somnolence ou léthargie", "10"], ["Cerveau", "Obnubilation", "15"],
         ["Cerveau", "Stupeur", "20"], ["Cerveau", "Coma ou convulsions", "30"],
         ["Digestif", "Anorexie, douleur ou constipation", "5"], ["Digestif", "Motilité diminuée", "15"], ["Digestif", "Iléus", "20"],
         ["Précipitant", "Absent ou présent", "0 ou 10"],
         ["Bradycardie", "Absente", "0"], ["Bradycardie", "50 à 59", "10"], ["Bradycardie", "40 à 49", "20"], ["Bradycardie", "< 40", "30"],
         ["Cœur ajouté", "ECG autre", "10"], ["Cœur ajouté", "Épanchement", "10"], ["Cœur ajouté", "Œdème pulmonaire", "15"],
         ["Cœur ajouté", "Cardiomégalie", "15"], ["Cœur ajouté", "Hypotension", "20"],
         ["Métabolisme ajouté", "Hyponatrémie, hypoglycémie, hypoxémie, hypercapnie, baisse de filtration", "10 chacun"]]))
    t += [
P("Jonklaas et al., Thyroid, 2014 : glucocorticoïde de stress d'abord, puis lévothyroxine intraveineuse, charge de 200 à 400 microgrammes, plus basse si le patient est petit, âgé ou coronarien, puis 1,6 microgramme par kilogramme et par jour réduit de 25 % tant que la voie est intraveineuse. Aucune spécialité intraveineuse n'est dans l'index suisse. Solu-CORTEF, numéro 23533, écrit 100 mg puis 100 mg toutes les 6 heures pour le stress opératoire majeur : c'est la dose suisse lue que l'on retient comme couverture, en disant que la phrase vise le patient déjà cortiqué.", S(3, 11, 20)),
P("On ne retarde pas le traitement pour finir le score. Un patient à 34 °C, bradypnéique, avec une natrémie basse, déjà hypothyréodien et somnolent, est traité. Le score sert à nommer et à transmettre, pas à autoriser l'attente. La thyréostimuline peut être peu élevée dans le coma : elle ne mesure pas la gravité.", S(3, 20)),
P("Les anomalies électrocardiographiques qui ajoutent 10 points sont le QT long, le microvoltage, le bloc de branche, les anomalies ST-T non spécifiques, ou les blocs. On peut les cumuler avec la bradycardie, l'épanchement, l'œdème, la cardiomégalie et l'hypotension. Oublier l'addition sous-estime le score.", S(20)),
P("Causes précipitantes : infection, froid, sédatif, infarctus, arrêt de la lévothyroxine. Le précipitant vaut 10 points et se traite en même temps. Une pneumonie n'efface pas le coma, elle le déclenche.", S(20)),
P("Euthyrox, numéro 54949, est la forme orale de la convalescence : début souvent à 25 µg si le cœur est fragile, entretien 100 à 200 µg, à jeun. On ne l'injecte pas. On ne le commence pas avant le glucocorticoïde si la surrénale n'est pas écartée. La notice contre-indique la lévothyroxine si la surrénale n'est pas traitée.", S(9)),
P("Différentiel. Hypothermie d'un sepsis sans hypothyroïdie : thyroxine libre non basse. Accident vasculaire : signes focalisés, hormones normales. Surdosage en sédatif : contexte, pupilles, hormones. Crise thyréotoxique : chaud et rapide, pas froid et lent. Basse T3 de réanimation : triiodothyronine basse sans le tableau du coma, et l'on ne donne pas d'hormone pour cela.", S(2, 3)),
P("Cas. Femme de 78 ans, lévothyroxine arrêtée depuis un mois, retrouvée à 33 °C, pouls 46, somnolente, constipation ancienne, natrémie 124 mmol/l, glycémie 3,1 mmol/l, crépitants, infection urinaire. Température 33 °C : 10. Somnolence : 10. Constipation : 5. Infection : 10. Bradycardie 46 : 20. Hypotension absente : 0. Hyponatrémie 10, hypoglycémie 10. Total déjà 75, au-dessus de 60, sans compter une éventuelle hypoxémie. On traite tout de suite. On ne discute pas un score intermédiaire.", S(20)),
P("Ordre du cas. Cortisol prélevé si le tube part dans la minute, hydrocortisone 100 mg intraveineuse, numéro 23533, puis lévothyroxine intraveineuse selon 2014, charge basse de la fourchette 200 à 400 microgrammes vu l'âge. Antibiotique de l'infection selon son information professionnelle, pas une dose inventée ici. Réchauffement passif. Sodium corrigé sans hâte brutale. Pas de carbimazole. Pas de propranolol : le cœur est lent.", S(3, 11, 20)),
P("Surveillance. Conscience, température, ventilation, rythme. Hormones tous les un à deux jours pour la trajectoire, pas pour une thyréostimuline normale à H12. Une triiodothyronine très haute sous traitement ferait baisser la dose, phrase de 2014. La liothyronine, si on l'ajoute, charge de 5 à 20 microgrammes puis 2,5 à 10 microgrammes toutes les 8 heures, plus bas chez la personne âgée.", S(3)),
P("Prévention. Ne pas arrêter la lévothyroxine chez le sujet âgé. Revoir toute hypothyroïdie qui devient somnolente. Hiver, infection, sédatif : trois précipitants à chercher. La famille sait qui appelle si la patiente ne se lève plus.", S(9)),
P("Piège. Donner 25 µg par la bouche et renvoyer. C'est la dose de ville, pas celle du coma. Autre piège : coter seulement la température et oublier l'hyponatrémie, qui vaut 10 points de plus. Autre piège : attendre une thyréostimuline au-dessus de 10 mU/l pour croire le diagnostic. Le score et la clinique priment.", S(1, 3, 20)),
P("Le myxœdème prétibial de Basedow n'est pas ce coma. Le mot myxœdème désigne ici l'hypothyroïdie extrême, pas la dermopathie.", S(2)),
    ]
    coeur = {i: t for i in range(1, 15)}
    # répartir pour que chaque point ait du texte propre
    chunks = [t[i::14] or t[:1] for i in range(14)]
    coeur = {i+1: chunks[i] if chunks[i] else t[:1] for i in range(14)}
    ess = P("Le coma myxœdémateux est l'hypothyroïdie qui défaille. Score de Popoveniuc en entier : 60 ou plus, très évocateur ; 25 à 59, risque ; moins de 25, peu probable. Glucocorticoïde puis lévothyroxine intraveineuse. Pas de comprimé dans la tubulure.", S(3, 20))
    return lecon(4, "Coma myxœdémateux", ess, coeur, src=(3, 20))

def bloc(paras):
    chunks = [paras[i::14] or paras[:1] for i in range(14)]
    return {i+1: (chunks[i] if chunks[i] else paras[:1]) for i in range(14)}

def dx5():
    p = [
P("La thyroïdite destructrice lâche le stock d'hormone sans le fabriquer. Thyrotoxicose, puis souvent phase basse, puis guérison ou hypothyroïdie. Le carbimazole ne bloque pas une fuite. Il expose à l'agranulocytose pour rien.", S(1, 8)),
P("De Quervain : douleur cervicale irradiant vers l'oreille, fièvre modérée, vitesse de sédimentation haute, fixation basse. Silencieuse et post-partum : peu ou pas de douleur, même profil en deux temps. Type 2 de l'amiodarone : destruction sur glande peu nodulaire, Doppler sans hypervascularisation, traité dans un autre fichier mais le mécanisme est le même.", S(1, 4)),
P("La revue de 2010 retient anti-inflammatoires et prednisone pour l'inflammation de De Quervain. Prednisone Streuli, numéro 29349, écrit 15 à 30 mg par jour pour une maladie aiguë qui ne met pas le pronostic vital en jeu. On situe la prednisone dans cette fourchette, courte, puis on baisse. Le seuil de Cushing lu est 7,5 mg.", S(1, 13)),
P("Propranolol, numéro 47025, 10-40 mg trois à quatre fois, si le cœur va vite. Pas d'iode radioactif en phase haute : la fixation est basse et l'irradiation inutile. Pas de scintigraphie chez la femme qui allaite.", S(2, 10)),
P("Phase basse. Fatigue, thyréostimuline haute, thyroxine libre basse. Substitution transitoire possible avec Euthyrox, souvent une dose modeste, à réévaluer pour l'arrêt. On ne grave pas « à vie » au premier mois. Après un post-partum, distinguer un Basedow : anticorps anti-récepteur, œil, fixation si elle est licite.", S(1, 9)),
P("Crise. Rare sur une destruction. Si le score de Burch-Wartofsky atteint 45 ou plus, on traite la défaillance, bêtabloquant et hydrocortisone 100 mg, numéro 23533, mais le thionamide est inutile. Le propylthiouracile de la recommandation de 2016, charge de cinq cents à mille milligrammes puis deux cent cinquante milligrammes toutes les quatre heures, vise une glande qui fabrique. On ne l'ajoute pas à une thyroïdite.", S(2, 5, 11)),
P("Grossesse et post-partum. Sans borne locale, ETA 2014 : 2,5 mU/l, 3,0 mU/l, 3,5 mU/l. ATA 2017 : environ 4,0 mU/l. Une thyrotoxicose du post-partum n'est pas d'office un Basedow. Allaitement et carbimazole : seulement si Basedow, et au plus 20 mg par jour.", S(8, 18, 19)),
P("Cas. Femme de 44 ans, odynophagie irradiée, 38,2 °C, pouls 108, thyroïde très sensible, thyroxine libre haute, thyréostimuline basse. Score de crise : température 38,2 °C vaut 10, fréquence 108 vaut 5, total bas. Pas de protocole de tempête. Prednisone dans la fourchette 15 à 30 mg, propranolol si besoin, pas de Néo-Mercazole. On prévient de la phase basse dans quelques semaines.", S(5, 10, 13)),
P("Piège. Appeler Basedow toute thyrotoxicose. L'œil et le goitre diffus manquent ici, la douleur est au premier plan. Autre piège : enchaîner sur une lévothyroxine à 100 µg à vie dès la première thyroxine libre basse. Autre piège : une cytoponction d'un nodule douloureux au milieu d'une thyroïdite subaiguë, qui peut montrer des atypies inflammatoires.", S(2, 6, 9)),
P("Échographie si un nodule persiste après la phase douloureuse. Classification TI-RADS entière, TR1 à TR5, seuils 2,5 cm, 1,5 cm et 1,0 cm. Pendant la douleur aiguë, l'échographie montre souvent un parenchyme hétérogène hypoéchogène, pas un cancer à opérer dans la semaine.", S(6)),
P("Amiodarone. Si le Doppler est vide et la glande lisse, c'est plutôt le type 2 : glucocorticoïde, pas seulement un thionamide. L'essai cité par l'ETA utilisait 30 mg par jour de prednisone, dans la fourchette AIPS 15 à 30 mg. On ne retire pas l'amiodarone seul si le cardiologue la juge indispensable.", S(4, 13)),
P("Suivi. Clinique à deux semaines, hormones à quatre à six semaines, puis selon la phase. Vitesse de sédimentation qui baisse rassure dans De Quervain. Une thyrotoxicose qui dure plus de six à huit semaines sans douleur fait revoir le diagnostic vers un Basedow.", S(1, 2)),
P("Prévention. Ne pas donner d'iode radioactif ni de contraste inutile en phase haute. Expliquer les deux temps à la patiente pour qu'elle ne croie pas à un deuxième diagnostic quand la fatigue de la phase basse arrive.", S(1)),
P("Clés. Fuite, pas fabrication. Douleur ou post-partum. Fixation basse. Prednisone 15 à 30 mg, pas carbimazole. Phase basse souvent transitoire. Crise rare et sans thionamide.", S(8, 13)),
    ]
    ess = P("La thyroïdite destructrice vide le stock : thyrotoxicose puis phase basse. Pas de carbimazole. Prednisone dans la fourchette suisse si De Quervain. Propranolol si le cœur va vite.", S(1, 13, 10))
    return lecon(5, "Thyroïdite destructrice", ess, bloc(p), src=(1, 13), n_angles=6)

def dx6():
    p = [
P("Le nodule autonome et le goitre multinodulaire toxique fabriquent de l'hormone sans anticorps stimulant. La thyréostimuline baisse. La scintigraphie montre un ou plusieurs foyers chauds et le reste éteint. Ce n'est pas un Basedow, même si les hormones se ressemblent.", S(2)),
P("L'âge et le tabac augmentent cette hyperthyroïdie, dit la revue de 2010. Un produit de contraste ou l'amiodarone peuvent précipiter une crise. Le score de Burch-Wartofsky s'applique alors en entier, et l'iode de la crise vient après le thionamide, jamais le comprimé nucléaire 130.0 mg, numéro 67017, contre-indiqué dans l'autonomie.", S(1, 5, 12)),
P("Échographie : TI-RADS complet. TR1, 0 point, pas de ponction. TR2, 2 points, pas de ponction. TR3, 3 points, ponction si au moins 2,5 cm, suivi si au moins 1,5 cm. TR4, 4 à 6 points, ponction si au moins 1,5 cm, suivi si au moins 1 cm. TR5, 7 points ou plus, ponction si au moins 1 cm, suivi si au moins 0,5 cm. Un foyer chaud n'annule pas un TR5.", S(6)),
P("Traitement du symptôme : propranolol 10-40 mg trois à quatre fois, numéro 47025. Carbimazole 20 à 60 mg puis 5 à 20 mg, numéro 21037, prépare une chirurgie ou un iode radioactif. Il ne fait pas disparaître le nodule. La rémission de 30 à 40 % citée pour Basedow ne s'applique pas ici.", S(1, 8, 10)),
P("Propylthiouracile : pas de spécialité suisse. En crise seulement, la recommandation de 2016 écrit cinq cents à mille milligrammes de charge puis deux cent cinquante milligrammes toutes les quatre heures. Hors crise, on n'utilise pas cette dose pour un nodule.", S(2)),
P("Avant une chirurgie de Basedow la recommandation décrit des gouttes d'iode. Pour un nodule toxique, la préparation se discute avec le chirurgien. On n'ouvre pas la boîte de blocage nucléaire.", S(2, 12)),
P("Cas. Homme de 70 ans, fibrillation, thyroxine libre haute, thyréostimuline indétectable, plusieurs nodules. Scintigraphie : foyers multiples. Pas d'orbitopathie. Anticorps anti-récepteur négatif. On ne dit pas Basedow. On ralentit le cœur, on bloque avec le carbimazole sans dépasser 60 mg, on adresse pour un traitement définitif. On classe chaque nodule. Un nodule de 2,8 cm solide isoéchogène à marge lisse vaut 3 points : TR3, la cytoponction se discute à partir de 2,5 cm.", S(2, 6, 8, 10)),
P("Grossesse. L'iode radioactif est contre-indiqué. Sans borne locale, seuils ETA 2014 et ATA 2017 : 2,5 / 3,0 / 3,5 mU/l ou environ 4,0 mU/l. Un nodule se surveille, la scintigraphie attend.", S(18, 19)),
P("Piège. Ponctionner tous les nodules de 1 cm. Le TR2 ne se ponctionne pas. Piège inverse : ne pas ponctionner un TR5 de 12 mm parce que la thyréostimuline est basse. Piège : croire qu'un nodule chaud est toujours bénin.", S(6)),
P("Après iode radioactif ou chirurgie, hypothyroïdie attendue. Euthyrox, début selon l'âge, entretien 100 à 200 µg, pas la ligne de freination du cancer. Contrôle à quatre à six semaines.", S(9)),
P("Crise après contraste. Score complet. Thionamide suisse au plus 60 mg. Iode minéral une heure après, pas 130.0 mg. Hydrocortisone 100 mg, numéro 23533. Propranolol selon la ligne thyroïdienne.", S(5, 8, 11, 12)),
P("Suivi du nodule non toxique avec hormones normales : ce n'est plus ce diagnostic. On garde TI-RADS. Une thyréostimuline qui s'effondre plus tard rouvre le chapitre de l'autonomie.", S(6)),
P("Prévention. Signaler le goitre multinodulaire avant un scanner injecté. Ne pas arrêter un thionamide de préparation juste avant le bloc sans consigne. Éduquer sur l'agranulocytose même si le traitement est transitoire.", S(1, 8)),
P("Clés. Foyer chaud, reste éteint. Pas d'anticorps. TI-RADS entier. Carbimazole prépare, ne guérit pas. Contraste peut déclencher une crise.", S(2, 6)),
    ]
    ess = P("Nodule autonome et goitre multinodulaire toxique : fabrication focale, scintigraphie chaude, pas d'orbitopathie. Carbimazole pour préparer. TI-RADS en entier pour le cancer. Contraste iodé : risque de crise.", S(2, 6, 8))
    return lecon(6, "Goitre multinodulaire toxique et nodule autonome", ess, bloc(p), src=(2, 6), n_angles=6)

def dx7():
    p = [
P("L'amiodarone change les hormones chez presque tout le monde et rend malade une minorité. Court terme, trois mois ou moins : thyréostimuline haute, thyroxine haute, triiodothyronine basse, reverse T3 haute. Long terme : thyréostimuline vers la normale, thyroxine encore haute, triiodothyronine basse ou limite basse. Ce profil euthyroïdien n'est pas une hyperthyroïdie.", S(4)),
P("Cordarone comprimés, numéro 33393, entretien de 100 mg à 400 mg par jour. La recommandation européenne parle d'une dose habituelle de 200 mg par jour. On ne monte pas la dose pour soigner la thyroïde.", S(4, 14)),
P("Hypothyroïdie induite. Forme franche : thyréostimuline supérieure à 10 mU/l et thyroxine libre basse, jusqu'à 5 % des traités dans le texte de 2018. Forme infraclinique : thyréostimuline entre la borne et 10 mU/l, thyroxine libre normale, jusqu'à 26 %. On ne retire pas l'amiodarone pour la seule hypothyroïdie si le cardiologue la maintient. Lévothyroxine si la forme est franche. Forme infraclinique : parfois pas de traitement chez le sujet âgé, contrôle tous les 4 à 6 mois. Cible sous traitement : hormones libres normales, thyréostimuline dans le haut de la norme ou un peu haute mais sous 10 mU/l.", S(4, 9)),
P("Thyrotoxicose de type 1 : fabrication sur goitre nodulaire ou Basedow latent. Doppler riche. Thionamide. Type 2 : destruction, glande plutôt normale, Doppler sans hypervascularisation, glucocorticoïde. Forme mixte : thionamide d'abord, corticoïde d'emblée si le doute est fort, ou après quatre à six semaines sans progrès. En zone riche en iode, la scintigraphie est basse dans les deux types et ne les sépare pas.", S(4)),
P("Prednisone. L'essai cité par l'ETA pour le type 2 utilisait 30 mg par jour. Prednisone Streuli, numéro 29349, écrit 15 à 30 mg par jour pour une maladie aiguë sans pronostic vital engagé. On situe la dose dans cette fourchette et l'on dit que la notice ne nomme pas l'amiodarone.", S(4, 13)),
P("Carbimazole, numéro 21037, 20 à 60 mg, souvent vers le haut de la fourchette dans le type 1 parce que la glande iodée répond mal. Plafond 60 mg. Pas de propylthiouracile suisse. En crise, la dose de 2016, cinq cents à mille milligrammes de charge puis deux cent cinquante milligrammes toutes les quatre heures, reste celle de la recommandation, à discuter seulement si une spécialité est obtenue. Sinon carbimazole.", S(2, 8)),
P("Arrêt de l'amiodarone : décision conjointe. En arythmie menaçante, on continue souvent. Thyroïdectomie sans délai si le cœur se dégrade, pour les deux types.", S(4)),
P("Cas euthyroïdien. Homme, 200 mg par jour depuis six semaines, thyroxine libre un peu haute, thyréostimuline à 6 mU/l, poids stable. On ne donne pas de carbimazole. On recontrôle.", S(4, 14)),
P("Cas type 2. Pas de goitre, Doppler vide, anticorps absents, amaigrissement, hormones hautes, thyréostimuline effondrée. Prednisone dans la fourchette, pas seulement un thionamide. Cardiologue dans la boucle.", S(4, 13)),
P("Grossesse. L'amiodarone n'est gardée que s'il n'y a pas d'alternative. Une hypothyroïdie se traite. Seuils : borne locale, sinon 4,0 mU/l (ATA 2017) ou 2,5 / 3,0 / 3,5 mU/l (ETA 2014).", S(4, 18, 19)),
P("Piège. Diagnostiquer une hyperthyroïdie sur une thyroxine libre haute et une thyréostimuline normale. C'est l'effet attendu. Piège inverse : une scintigraphie pour séparer les types en Suisse, où l'iode alimentaire rend la fixation basse des deux côtés.", S(4)),
P("Basse T3 sous amiodarone chez un patient en réanimation : ne pas ajouter une liothyronine. La recommandation de 2014 est contre ce traitement du syndrome de basse T3.", S(3)),
P("Surveillance. Bilan avant l'amiodarone, puis régulier. Une thyrotoxicose clinique se dose le jour même, pas au prochain semestre.", S(4)),
P("Clés. Profil euthyroïdien d'abord. Type 1 thionamide, type 2 corticoïde, mixte les deux selon le délai. Ne pas arrêter l'amiodarone seul. Plafond de carbimazole 60 mg.", S(4, 8)),
    ]
    ess = P("L'amiodarone élève la thyroxine libre chez l'euthyroïdien. L'hypothyroïdie franche se substitue sans arrêt obligatoire. La thyrotoxicose de type 1 se bloque, celle de type 2 reçoit un glucocorticoïde. La scintigraphie ne les sépare pas en zone riche en iode.", S(4))
    return lecon(7, "Dysthyroïdie induite par l'amiodarone", ess, bloc(p), src=(4, 14), n_angles=6)

def dx8():
    p = [
P("Le syndrome de basse T3, ou nonthyroidal illness, commence par une triiodothyronine basse, puis la thyréostimuline et la thyroxine baissent, puis la thyroxine libre chez les plus graves. La revue de 2010 le nomme déjà dans la maladie aiguë, la dénutrition, sous corticoïde ou amiodarone.", S(1, 3)),
P("Jonklaas et al., 2014, recommandent de ne pas donner de lévothyroxine à un patient hospitalisé qui présente ce syndrome sans hypothyroïdie connue, et de ne pas donner de liothyronine non plus. Les essais n'ont pas montré un bénéfice net.", S(3)),
P("Le patient déjà substitué garde sa lévothyroxine. Une thyréostimuline qui monte pendant l'aggravation, sur une thyroïde malade, fait chercher un manque. La dopamine peut abaisser la thyréostimuline et faire sous-doser si l'on ne regarde qu'elle.", S(3)),
P("Biotine. Elle ne change pas la glande. Sur un dosage streptavidine-biotine, la thyréostimuline sandwich devient faussement basse et les hormones libres compétitives faussement hautes. L'ATA 2016 : arrêter et recontrôler au moins deux jours plus tard. La mise en garde australienne de 2016 : 72 heures, et des doses dépassant 5 mg peuvent suffire. Des profils avec thyroxine libre supérieure à 100 pmol/l et thyréostimuline inférieure à 0,01 mUI/l ont été vus chez des euthyroïdiens.", S(2, 7)),
P("On ne commence pas un carbimazole sur une biotine si la clinique est vide. Si la clinique de Basedow est riche, on traite la maladie et l'on fait quand même arrêter le complément, parce que les deux peuvent coexister.", S(7, 8)),
P("Autres pièges du tube. Hétérophiles, prise de lévothyroxine, grossesse avec thyréostimuline basse physiologique. Sans borne locale, grossesse : 4,0 mU/l (ATA 2017) ou 2,5 / 3,0 / 3,5 (ETA 2014). Une thyréostimuline détectable basse n'est pas une hyperthyroïdie.", S(18, 19)),
P("Cas réanimation. Homme, jour 2 de pneumonie, pas d'antécédent thyroïdien, triiodothyronine très basse, thyréostimuline basse, thyroxine libre encore normale. On traite la pneumonie. On ne prescrit pas Euthyrox. On recontrôle à distance.", S(3, 9)),
P("Cas biotine. Étudiant, fatigue, pouls 64, pas de goitre, hormones très hautes, thyréostimuline indétectable, gélules pour les cheveux. Arrêt, contrôle après 72 heures. Pas de thionamide entre les deux si rien ne change à l'examen.", S(7)),
P("Cas limite. Patiente en réanimation déjà sous 100 µg de lévothyroxine pour une thyroïdectomie. On continue. On ne corrige pas la triiodothyronine basse de la maladie. On ne passe pas à une liothyronine.", S(3, 9)),
P("Amiodarone en réanimation. Thyroxine libre haute et triiodothyronine basse peuvent être le médicament, pas une crise. On cherche la clinique de tempête avant tout carbimazole. Score de Burch-Wartofsky seulement si la thyrotoxicose est réelle.", S(4, 5)),
P("Piège. Traiter une thyréostimuline basse de dopamine comme un Basedow. Piège : ignorer la biotine et opérer. Piège : doser la reverse T3 en routine. Aucun texte suisse lu ne le demande pour décider.", S(2, 3, 7)),
P("Prévention. Demander les compléments à chaque bilan discordant. Écrire « biotine » sur la demande d'examen. Ne pas adapter une lévothyroxine de ville sur un bilan de réanimation.", S(7)),
P("Retour à la normale. Après la maladie, la thyréostimuline peut rebondir. Ce rebond n'est pas une hypothyroïdie à traiter à vie. On recontrôle debout, sans amine.", S(3)),
P("Clés. Basse T3 : ne pas substituer un euthyroïdien. Biotine : profil de Basedow sans malade. Deux jours au moins, 72 heures dans le texte de 2016. Clinique d'abord.", S(2, 3, 7)),
    ]
    ess = P("La basse T3 de la maladie grave ne se traite pas par hormone chez l'euthyroïdien. La biotine fabrique un faux Basedow : thyréostimuline basse, hormones libres hautes, clinique pauvre. On arrête le complément et on recontrôle.", S(3, 7))
    return lecon(8, "Syndrome de basse T3 et interférence de la biotine", ess, bloc(p), src=(3, 7), n_angles=6)

def dx9():
    p = [
P("L'hypothyroïdie centrale est un manque de thyroxine par défaut d'hypophyse ou d'hypothalamus. La thyroxine libre est basse. La thyréostimuline est basse ou « normale », pas haute. Une thyréostimuline dans les bornes ne prouve pas que la thyroïde va bien.", S(1)),
P("Causes : tumeur, chirurgie, apoplexie, inflammation, infiltration, corticoïde ou autre freinage, arrêt d'une lévothyroxine substitutive d'un panhypopituitarisme. Le post-partum avec céphalée et choc fait chercher un Sheehan, sans inventer une fréquence non lue.", S(1)),
P("Avant toute lévothyroxine, le cortisol. Euthyrox est contre-indiqué si la surrénale n'est pas traitée, numéro 54949. L'ordre du coma s'applique dès qu'il y a défaillance : hydrocortisone 100 mg, numéro 23533, puis hormone. En ville, on dose le cortisol le matin et l'on couvre si le doute est réel.", S(3, 9, 11)),
P("La cible n'est pas une thyréostimuline normale : elle ne montera pas. On suit la thyroxine libre, dans la moitié supérieure de la norme selon l'habitude des équipes, sans qu'une notice suisse lue fixe ce demi-intervalle comme une loi. On le dit comme une conduite prudente, et l'on évite le surdosage clinique.", S(9)),
P("Dose. Même spécialité. Début à 25 µg si le patient est fragile ou cardiaque, sinon dans la zone 25 à 50, entretien souvent 100 à 200 µg, à jeun, loin du calcium. Paliers lents. Contrôle à quatre à six semaines.", S(9)),
P("Imagerie. Une IRM hypophysaire si le contexte est une maladie centrale nouvelle, pas devant chaque fatigue. On cherche les autres axes : cortisol, gonadotrophines, prolactine selon la clinique. On n'invente pas un bilan unique.", S(1)),
P("Grossesse. Avis spécialisé. Seuils de thyréostimuline peu utiles ici puisque la thyréostimuline ne guide pas. La thyroxine libre et le cortisol priment. ATA 2017 et ETA 2014 restent les références si une thyréostimuline est malgré tout interprétée : 4,0 mU/l ou 2,5 / 3,0 / 3,5 mU/l sans borne locale.", S(18, 19)),
P("Coma. Un patient central peut présenter le même froid et la même hyponatrémie. Le score de Popoveniuc s'applique : 60 ou plus très évocateur, 25 à 59 risque, moins de 25 peu probable. Toutes les lignes, y compris l'addition cardiovasculaire et métabolique. La thyréostimuline basse ne doit pas faire récuser le score.", S(20)),
P("Différentiel. Primaire : thyréostimuline haute. Basse T3 : triiodothyronine basse, thyroxine libre souvent encore normale au début, contexte de réanimation. Jeûne et maladie grave. Biotine : hormones libres hautes, pas basses. Arrêt de lévothyroxine chez un primaire : la thyréostimuline monte.", S(1, 3, 7)),
P("Cas. Femme de 36 ans, aménorrhée, fatigue, thyroxine libre basse, thyréostimuline 0,8 mU/l. On ne rassure pas. Cortisol, puis IRM, puis lévothyroxine après la surrénale. Début prudent. Pas de carbimazole.", S(1, 9)),
P("Cas de défaillance. Le même mécanisme avec température à 33 °C et natrémie basse. Score au moins : température 10, hyponatrémie 10, précipitant possible 10, cerveau selon l'éveil. On n'attend pas 60 points pour injecter l'hydrocortisone. On complète le score pour la transmission.", S(11, 20)),
P("Piège. Traiter comme un Hashimoto à pleine dose d'emblée. Piège : croire qu'une thyréostimuline à 1,5 mU/l exclut le diagnostic. Piège : oublier le cortisol et précipiter une crise surrénale, implication pratique déjà écrite en 2010.", S(1, 9)),
P("Prévention. Après chirurgie hypophysaire, ordonnance de cortisol et de lévothyroxine explicite, et consigne de doubler le corticoïde en stress selon la notice, pas une dose inventée. Carte d'insuffisance surrénale si le déficit est confirmé.", S(11)),
P("Clés. Thyroxine libre basse, thyréostimuline qui ne monte pas. Cortisol d'abord. Cible sur la thyroxine libre. Score de Popoveniuc si défaillance. Pas de thionamide.", S(9, 20)),
    ]
    ess = P("L'hypothyroïdie centrale : thyroxine libre basse, thyréostimuline basse ou normale. On couvre la surrénale avant la lévothyroxine. La cible n'est pas la thyréostimuline. En défaillance, score de Popoveniuc et hydrocortisone d'abord.", S(1, 9, 20))
    return lecon(9, "Hypothyroïdie centrale", ess, bloc(p), src=(9, 20), n_angles=6)

def dx10():
    p = GROS + [
P("L'hypothyroïdie infraclinique est une thyréostimuline haute avec une thyroxine libre normale. La revue de 2010 parle d'une zone 3,5 à 20 mU/l selon les bornes d'alors du CHUV, où la thyréostimuline allait de 0,2 à 3,5 mU/l. Le traitement est controversé. Les anticorps anti-thyroperoxydase font passer à la forme franche 4,3 % par an contre 2,3 % sans anticorps, et à dix ans 43 % contre 23 %.", S(1)),
P("L'hyperthyroïdie infraclinique est une thyréostimuline basse avec hormones libres normales. La revue l'estime à environ 1 %. Elle augmente le risque de fibrillation, surtout si la thyréostimuline est inférieure à 0,1 mU/l. Les autres risques sont discutés. On n'impose pas un thionamide à toute valeur un peu basse.", S(1)),
P("Grossesse. ETA 2014, sans borne de laboratoire : limites hautes 2,5 mU/l, 3,0 mU/l, 3,5 mU/l. ATA 2017 : d'abord la borne locale, sinon environ 4,0 mU/l, avec baisse d'environ 0,4 mU/l en bas et 0,5 mU/l en haut au premier trimestre, applicable surtout des semaines 7 à 12. On n'utilise plus 2,5 mU/l comme seule règle de 2017.", S(18, 19)),
P("Hors grossesse, une thyréostimuline entre la borne et 10 mU/l avec thyroxine libre normale peut se surveiller, surtout chez le sujet âgé. Au-dessus de 10 mU/l, la revue et l'ETA parlent plus volontiers d'une forme à traiter, et si la thyroxine libre est basse c'est déjà l'hypothyroïdie franche, autre fichier.", S(1, 19)),
P("Si l'on traite, Euthyrox, numéro 54949. La revue cite des doses proches de 75 à 100 µg pour observer un effet sans hyperthyroïdie iatrogène, cible de thyréostimuline souvent 0,5 à 1,5 dans ce texte. La notice, elle, décrit un début de 25 à 50 µg et un entretien de 100 à 200 µg pour l'hypothyroïdie. Chez le sujet âgé on commence à 25 µg. On ne dépasse pas ce que le cœur tolère. On évite une thyréostimuline sous 0,4 mU/l.", S(1, 9)),
P("On ne traite pas une basse T3, ni une biotine, dans ce fichier. Une thyréostimuline basse avec hormones libres hautes n'est plus infraclinique.", S(3, 7)),
P("Nodule. Toute thyréostimuline basse avec un nodule palpable mène à la scintigraphie et à TI-RADS, pas à un simple contrôle dans un an. Les seuils de ponction restent ceux de 2017, toutes catégories.", S(6)),
P("Amiodarone. Infraclinique induite : surveillance possible tous les 4 à 6 mois chez le sujet âgé, sans arrêt obligatoire du médicament. Franche : lévothyroxine, cible qui peut laisser la thyréostimuline sous 10 mU/l.", S(4)),
P("Cas femme de 62 ans. Thyréostimuline 7 mU/l, thyroxine libre normale, anticorps positifs, pas de symptôme net. On explique le risque de 4,3 % par an. On peut surveiller ou discuter une petite dose. On ne commence pas à 150 µg. Si l'on traite, début bas, contrôle à six semaines, pas de thyréostimuline sous 0,4 mU/l.", S(1, 9)),
P("Cas homme de 74 ans. Thyréostimuline 0,05 mU/l, hormones libres normales, fibrillation. On cherche un nodule toxique. Propranolol selon la ligne thyroïdienne si le cœur le demande, numéro 47025. Avis pour un traitement définitif. Pas de dose de crise.", S(1, 10)),
P("Cas grossesse. Thyroxine libre normale, thyréostimuline 3,2 mU/l au premier trimestre, pas de borne locale. Pour l'ETA 2014, 3,2 dépasse 2,5. Pour l'ATA 2017, 3,2 reste sous 4,0. On ne tranche pas seul : on adresse, on dose les anticorps, on écrit les deux textes. On ne démarre pas une pleine substitution sans cet avis.", S(18, 19)),
P("Piège. Traiter toute thyréostimuline au-dessus de 2,5 mU/l hors grossesse. Ce seuil de grossesse ancien n'est pas la borne du CHUV de 2010, qui allait jusqu'à 3,5 mU/l hors grossesse. Piège : ignorer 0,1 mU/l chez un fibrillant. Piège : oublier la biotine devant une thyréostimuline indétectable et une clinique vide.", S(1, 7)),
P("Prévention. Redoser avant de traiter un chiffre isolé. Demander les compléments. Chez la femme enceinte, avis spécialisé. Contrôle annuel si l'on surveille sans traiter, plus tôt si des symptômes apparaissent.", S(1, 18)),
P("Clés. Une seule hormone anormale, l'autre dans les bornes. Anticorps pour le risque. Grossesse : 2,5 / 3,0 / 3,5 ou environ 4,0 selon le texte, borne locale d'abord. Pas de thionamide systématique. Pas de dose pleine d'emblée chez le sujet âgé.", S(1, 9, 18, 19)),
    ]
    ess = P("L'infraclinique : une seule hormone sort des bornes. Le traitement n'est pas automatique. En grossesse, borne locale d'abord, sinon environ 4,0 mU/l (ATA 2017) ou 2,5, 3,0 et 3,5 mU/l (ETA 2014). Anticorps anti-thyroperoxydase : 4,3 % par an de passage à la forme franche.", S(1, 18, 19))
    return lecon(10, "Dysfonction thyroïdienne infraclinique", ess, bloc(p), src=(1, 18, 19))

if __name__ == "__main__":
    from pathlib import Path
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    for fn in (dx4, dx5, dx6, dx7, dx8, dx9, dx10):
        print(fn())
