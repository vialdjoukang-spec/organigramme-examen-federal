"""Fenêtres ajoutées au DX.1 pour atteindre la profondeur demandée."""
from moteur import A, P, W

ALAT = A("alanine aminotransférase", "ALAT")
ASAT = A("aspartate aminotransférase", "ASAT")
FIB = A("fibrosis-4 index", "FIB")
MASLD = A("metabolic dysfunction-associated steatotic liver disease", "MASLD")

def fenetres() -> str:
    return fenetres_a() + fenetres_b()

def fenetres_a() -> str:
    return (
        W("w-facteurs-long", "Chaque facteur, ce qu'on fait concrètement", "\n".join([
            P(f"Indice de masse corporelle au moins 25 kg/m², ou 23 si la personne est d'origine asiatique. "
              f"On pèse et on mesure, on ne se fie pas au souvenir. Un indice à 24 avec un tour de taille européen au-dessus du seuil reste un facteur par le tour de taille, pas par l'indice. Les deux lignes sont indépendantes.", 5),
            P("Tour de taille européen : 94 cm chez l'homme, 80 cm chez la femme. Asie du Sud et Chine : 90 et 80. Japon : 85 chez l'homme et 90 chez la femme. "
              "Appliquer le seuil japonais à une patiente européenne, ou l'inverse, change le diagnostic. On écrit quelle ligne on a utilisée.", 5),
            P("Prédiabète : hémoglobine glyquée de 39 à 47 mmol/mol, soit 5,7 à 6,4 %, ou glycémie à jeun de 5,6 à 6,9 mmol/l, ou glycémie deux heures après charge de 7,8 à 11 mmol/l. "
              "Un seul de ces trois suffit. On ne demande pas les trois.", 5),
            P("Diabète : hémoglobine glyquée au moins 48 mmol/mol, soit au moins 6,5 %, ou glycémie à jeun au moins 7,0 mmol/l, ou glycémie à deux heures au moins 11,1 mmol/l, ou un traitement déjà en cours. "
              "Le patient « équilibré » sous metformine a le facteur. On ne le retire pas parce que la glycémie du matin est belle.", 5),
            P("Triglycérides au moins 1,7 mmol/l, ou un traitement hypolipémiant. Le HDL au plus 1,0 mmol/l chez l'homme et 1,3 mmol/l chez la femme, ou le même type de traitement. "
              "Une statine prescrite pour une autre raison compte. On le note dans le dossier, sinon le prochain lecteur croit qu'il n'y a pas de facteur lipidique.", 5),
            P("Pression au moins 130/85 mmHg ou traitement antihypertenseur. Ce n'est pas le seuil de 140/90 d'une autre recommandation. "
              "Le cours garde 130/85 parce que c'est le tableau de 2024, pas parce que c'est le seul chiffre de tension qui existe en médecine.", 5),
            P(f"Aucun de ces facteurs ne prouve la fibrose. Ils autorisent le nom de {MASLD} une fois la stéatose vue, et ils désignent qui entre dans le repérage. "
              f"Le {FIB}-4 vient après, pas à la place.", 5),
        ]))
        + W("w-medocs", "Stéatoses qui ne sont pas métaboliques", "\n".join([
            P("Le tableau des autres causes, lu en 2024, cite des médicaments à interroger un par un : corticoïdes, tamoxifène, amiodarone, irinotécan, méthotrexate, lomitapide, valproate, fluorouracil. "
              "La stéatose est souvent microvésiculaire pour plusieurs d'entre eux. La biopsie confirme si le doute reste. On n'ajoute pas à cette liste un produit qui n'y figure pas.", 5),
            P("Corticoïde au long cours : la graisse vient de l'insuline et de l'appétit, pas d'une hépatite immuno-allergique. On distingue cette stéatose de la lésion idiosyncrasique du cours sur le médicament, qui se juge par le rapport R et le score de causalité.", 2, 5),
            P("Amiodarone : la stéatose peut s'accompagner d'une phospholipidose. L'arrêt ne se décide pas sur une seule enzyme, parce que le produit sert souvent à une arythmie. On le signale, on ne l'arrête pas seul depuis le cabinet d'hépatologie.", 5),
            P("Méthotrexate : la fibrose est le risque cumulé, pas le pic d'une semaine. Le FIB-4 peut aider à trier, il ne remplace pas l'historique des doses cumulées que le rhumatologue tient.", 5),
            P("Valproate et fluorouracil : y penser devant une stéatose microvésiculaire, une acidose ou une hypoglycémie, surtout si le terrain métabolique est pauvre. Ce n'est pas le diabétique de 60 ans au premier plan.", 5),
            P("Virus C de génotype 3 : triglycérides plutôt bas, anticorps puis ARN puis génotype. Une stéatose avec des triglycérides bas n'est pas le tableau métabolique habituel, où les triglycérides sont hauts.", 5),
            P("Déficit en lipase acide lysosomale : jeune, LDL et triglycérides hauts, HDL bas, rate, fibrose déjà avancée, stéatose surtout microvésiculaire. Dosage enzymatique et gène LIPA. "
              "Le FIB-4 d'un adulte de 55 ans ne cherche pas cette maladie. L'âge jeune, si.", 5),
            P("Hypobêtalipoprotéinémie : triglycérides et cholestérol bas, malabsorption, déficit en vitamine A. Ce n'est pas un syndrome métabolique. ApoB et génétique.", 5),
        ]))
        + W("w-fib-cas", "Trois calculs de FIB-4, trois âges", "\n".join([
            P(f"Trente-deux ans, {ASAT} 40, {ALAT} 50, plaquettes 250. Le calcul donnerait un chiffre bas. On ne s'y fie pas : avant 35 ans le score est peu fiable. "
              f"On regarde le terrain, l'alcool, les médicaments, et l'on n'écrit pas « fibrose écartée ».", 5),
            P(f"Cinquante ans, {ASAT} 30, {ALAT} 32, plaquettes 280. Numérateur 1 500. Racine de 32 environ 5,7. Dénominateur environ 1 580. Score inférieur à 1. "
              f"Sous 1,3 : risque bas, nouveau calcul dans un à trois ans, en sachant qu'environ 10 % des fibroses avancées échappent. Ce n'est pas un blanc-seing à vie.", 5),
            P(f"Soixante-huit ans, {ASAT} 35, {ALAT} 30, plaquettes 200. Numérateur 2 380. Racine de 30 environ 5,5. Dénominateur environ 1 100. Score environ 2,2. "
              f"Après 65 ans le seuil bas est 2,0. 2,2 est donc au-dessus, mais encore sous 2,67 : zone où l'élastographie ou l'année de traitement puis un second score sont les deux options. "
              f"Traiter 2,2 comme un score de cinquantenaire sous 1,3 serait faux. Le traiter comme un score au-dessus de 2,67 le serait aussi.", 5),
            P(f"Même personne de 68 ans si les plaquettes tombent à 110 et l'{ASAT} monte à 55, {ALAT} 40. "
              f"Numérateur 3 740. Racine de 40 environ 6,3. Dénominateur environ 695. Score au-dessus de 5. "
              f"Là, le second test ne se discute plus. Une enzyme encore sous deux fois la limite n'a pas le droit de rassurer.", 5),
            P("On refait le calcul si une hépatite aiguë, une cholestase ou une congestion sont là. "
              "La recommandation alcool de 2018 demande la prudence sur la dureté hépatique quand l'ASAT dépasse 100 U/l, parce que l'inflammation raidit le foie sans que la fibrose ait changé. "
              "Le FIB-4, lui aussi, bouge avec l'ASAT. On ne stade pas une fibrose le jour d'une cytolyse aiguë.", 4, 5),
        ]))
        + W("w-annee", "L'année qui suit un score intermédiaire", "\n".join([
            P(f"Le chemin différé n'est pas une année blanche. C'est une année de poids, de diabète, de tension et de lipides, puis un second {FIB}-4. "
              f"Si le second score est encore haut, l'élastographie devient le pas suivant. Si l'on n'a rien changé au terrain, recommencer le même chiffre ne prouve rien.", 5),
            P("Le chemin immédiat, l'élastographie, est préféré quand le score est proche de 2,67, quand il y a plusieurs facteurs, ou quand le patient a plus de 50 ans ou est une femme ménopausée. "
              "La recommandation le dit comme un risque de fibrose progressive, pas comme une obligation de biopsier tout le monde.", 5),
            P("Ce que l'on surveille en plus du foie : événements cardiovasculaires, rein, diabète incident. "
              "Le hazard ratio rénal cité dans la synthèse de 2024 est 1,43, celui du diabète incident 2,19. "
              "Ils justifient de ne pas limiter la consultation à l'enzyme. Ils ne sont pas une prédiction individuelle.", 5),
            P(f"Si l'élastographie ou la clinique montrent une cirrhose, on sort du tri ambulatoire simple. "
              f"Child-Pugh A, B et C, puis le score de 2010, reprennent la gravité. Le carcinome se surveille. "
              f"La {MASLD} explique alors la cirrhose, elle ne dispense pas de la classer.", 8, 9),
            P(f"Contrôle de la copie. Un candidat qui écrit seulement « régime et contrôle dans un an » pour un score au-dessus de 2,67 a raté la zone. "
              f"Un candidat qui biopsie d'emblée un score à 0,8 a raté l'autre bout. "
              f"Un candidat qui donne la même phrase à une femme à quarante grammes d'alcool par jour a raté MetALD.", 5),
        ]))
    )

def fenetres_b() -> str:
    return (
        W("w-pas-a-pas", "Démarche pas à pas devant l'enzyme modeste", "\n".join([
            P(f"Pas 1. Relire le compte rendu avec les limites du laboratoire, pas avec une limite de mémoire. "
              f"Une {ALAT} à 46 pour une limite à 35 est au-dessus. La même valeur pour une limite à 50 est dans l'intervalle. Le rapport R et le {FIB}-4 utilisent ces limites seulement là où la formule le dit : "
              f"le {FIB}-4 utilise les valeurs brutes en U/l, pas des multiples de la limite.", 5),
            P("Pas 2. Chercher la stéatose. Échographie en premier lieu parce qu'elle est disponible. Elle est peu sensible pour une graisse légère. "
              "Une échographie normale n'autorise pas à nier une stéatose si la clinique est forte : elle autorise à ne pas poser le nom tant qu'une autre image ou une histologie ne l'a pas vue.", 5),
            P("Pas 3. Compter les facteurs un par un, traitements compris. Écrire lesquels sont présents. "
              "Zéro facteur : on ne force pas le nom. On parle de stéatose possible, et l'on cherche l'insulinorésistance, ou de stéatose cryptogénique si rien ne vient.", 5),
            P("Pas 4. Quantifier l'alcool en grammes par jour sur plusieurs semaines, et demander l'ancien usage. "
              "En dessous des bornes de MetALD, le nom métabolique tient. Dans la bande de vingt à cinquante grammes chez la femme ou de trente à soixante chez l'homme, c'est MetALD. "
              "Au-dessus de cinquante et de soixante, c'est la maladie alcoolique, et l'hépatite alcoolique se juge à part si l'ictère est là.", 5),
            P("Pas 5. Écarter ou nommer la cause spécifique : virus C de génotype 3, médicament de la liste, maladie du jeune. "
              "Ce pas est court quand le terrain métabolique est bruyant. Il devient le pas principal quand le patient est maigre, jeune, ou sans aucun facteur.", 5),
            P(f"Pas 6. Calculer le {FIB}-4 avec les plaquettes en milliards par litre. Placer le résultat dans une des trois zones, en changeant le seuil bas après 65 ans, "
              f"et en refusant le score avant 35 ans. Écrire la zone dans le dossier, pas seulement le nombre.", 5),
            P("Pas 7. Choisir le chemin. Bas : contrôle dans un à trois ans et traitement du terrain. "
              "Intermédiaire : élastographie ou année active puis second score. Haut : second test maintenant, adressage. "
              "Cirrhose déjà évidente : Child-Pugh complet et score de 2010, pas un nouveau tri de ville.", 5, 8, 9),
            P("Pas 8. Dire au patient ce que l'enzyme ne mesure pas. Elle ne mesure pas la fibrose, elle ne mesure pas le risque d'infarctus, elle ne mesure pas l'observance. "
              "Le rendez-vous suivant a une date et un objectif, pas une formule de politesse.", 5),
        ]))
        + W("w-differentiel-long", "Différentiel commenté, pas seulement un tableau", "\n".join([
            P(f"Hépatite alcoolique. Elle a un ictère récent, souvent une {ASAT} qui dépasse l'{ALAT}, rarement au-dessus de 300 U/l, et un score de Maddrey. "
              f"Une {ALAT} à 46 sans ictère n'y entre pas. Inversement, un foie stéatosique chez quelqu'un qui boit soixante grammes par jour ne se contente pas du mot métabolique.", 4, 5),
            P(f"Virus B. Les cinq phases restent. Un porteur en phase III, {ALAT} normale, peut avoir en plus une stéatose métabolique : les deux diagnostics coexistent. "
              f"On ne « choisit » pas le plus facile. L'ADN et l'antigène disent la phase. Le terrain et l'image disent la graisse.", 5, 17),
            P("Obstacle. Le rapport R cholestatique et la dilatation n'appartiennent pas à la stéatose. Une phosphatase normale rend l'obstacle peu probable. "
              "On ne fait pas une cholangio-IRM pour une enzyme à une fois et demie avec une image de stéatose et un FIB-4 bas, sauf douleur ou ictère.", 2, 5),
            P("Hémochromatose. La ferritine monte avec l'inflammation et la stéatose. La saturation de la transferrine fait le tri, le matin. "
              "Sans saturation haute, on ne lance pas le gène. Avec saturation haute et ferritine dans les zones lues, chez un homozygote, le diagnostic provisoire est posé et la stéatose peut être associée.", 6),
            P("Hépatite auto-immune. Une enzyme qui flambe, une immunoglobuline G haute, des autoanticorps : le score simplifié. "
              "Une enzyme plate depuis des années chez un diabétique obèse n'est pas le tableau. Les deux maladies peuvent pourtant se rencontrer : on ne ferme pas le score si le profil change.", 7),
            P("Ischémie. Pic très haut, lacticodéshydrogénase, créatinine, chute rapide après restauration de la pression. "
              "Rien à voir avec une enzyme chronique à 50 U/l. Si ce pic survient chez un patient déjà stéatosique, on traite l'épisode aigu d'abord.", 3),
            P("Médicament idiosyncrasique. Délai, rapport R, loi de Hy si la bilirubine monte, score de causalité en cinq classes. "
              "Ce n'est pas la stéatose lente du méthotrexate. Les deux chapitres du cours ne se mélangent pas dans la même phrase de conclusion.", 2),
        ]))
        + W("w-pieges-long", "Pièges que la copie rate souvent", "\n".join([
            P("Confondre 1,3 et 2,67 avec des stades histologiques. Ce sont des seuils de tri, pas des stades F1 et F3. Le stade, s'il est nécessaire, vient d'un autre test.", 5),
            P("Oublier les 10 % de fibroses avancées manquées sous 1,3. La phrase juste est : risque bas, pas risque nul. On le dit si la question demande la limite de l'outil.", 5),
            P("Utiliser 2,0 comme seuil bas chez un adulte de 60 ans. Ce déplacement ne vaut qu'après 65 ans.", 5),
            P("Citer seulement le tour de taille européen. Le tableau a trois jeux ethniques. La copie complète les nomme ou dit lequel elle applique et pourquoi.", 5),
            P("Écrire que la NAFLD et la MASLD sont strictement le même mot. La concordance lue est de 99,8 % dans une cohorte de soins, et de 5,3 % de non-recouvrement dans NHANES III. "
              "On peut transposer les tests. On ne peut pas dire que personne n'a changé de case.", 5),
            P(f"Proposer l'acide ursodésoxycholique, information 60812, pour faire baisser une {A('gamma-glutamyltransférase','GGT')}. "
              f"L'indication lue est la cholangite biliaire primitive, pas la {MASLD}.", 12),
            P("Calculer le score le jour où l'ASAT est à 400 après une chute. Ni le FIB-4 ni l'élastographie ne lisent la fibrose ce jour-là.", 4, 5),
            P("Donner un Child-Pugh B sans dire A et C, parce que « le patient n'est pas C ». La classification a trois classes. On les écrit, puis on dit où le patient se place.", 9),
        ]))
        + W("w-suite-cas", "Suite du cas : ce que le correcteur attend encore", "\n".join([
            P(f"Reprenons la femme de 58 ans, score aux environs de 3, donc au-dessus de 2,67. "
              f"Le correcteur veut l'élastographie maintenant, pas dans un an. Il veut aussi le nom MetALD si les vingt grammes par jour sont acceptés comme réels, "
              f"parce que vingt grammes est la borne basse de la bande femme. Si l'étudiante conteste l'estimation et la fait recompter les verres, c'est encore mieux : "
              f"deux verres de vin peuvent dépasser ou non vingt grammes selon le volume. Le cours ne fixe pas le volume d'un verre. Il demande de ne pas deviner.", 5),
            P("Six mois plus tard, elle a perdu du poids, la tension est traitée, l'hémoglobine glyquée est à 40 mmol/mol, elle a arrêté le vin. "
              "L'élastographie a été faite et n'est pas celle d'une cirrhose, dans le compte rendu fictif de l'énoncé. "
              "Que reste-t-il du nom ? Le terrain cardiométabolique est toujours là : l'indice, le tour de taille, le prédiabète à 40 mmol/mol qui est encore entre 39 et 47, le traitement de la tension. "
              "L'alcool est sorti de la bande MetALD. On peut alors revenir au nom métabolique, et l'on le date : ce n'était pas le même nom il y a six mois.", 5),
            P(f"Le second {FIB}-4, si les plaquettes et les enzymes n'ont pas bougé, reste haut. "
              f"La perte de poids ne réécrit pas les plaquettes en un mois. On ne conclut pas « guérie » sur la balance. "
              f"On conclut : terrain en cours de correction, fibrose encore à surveiller selon le résultat d'élastographie déjà obtenu.", 5),
            P("Si, au contraire, elle revient ictérique avec une ASAT à 180 et une ALAT à 70, le vin ayant repris, on quitte ce chapitre. "
              "Le rapport est supérieur à 2, l'ASAT est sous 300 U/l, l'ictère ouvre le score de Maddrey. "
              "Ce n'est plus un contrôle de fibrose. C'est l'hépatite alcoolique du DX.2, avec ses seuils 32, 9 et les trois classes de Lille si un corticoïde est commencé.", 4),
            P("Si elle revient avec une fièvre à 39 °C, une bilirubine à 6 mg/dl et une voie dilatée, on quitte aussi ce chapitre. "
              "Deux critères du grade II de Tokyo sont là, le drainage est précoce. Le FIB-4 ne se calcule pas ce jour-là.", 18),
            P(f"Phrase de fin de copie, celle qui prend les points. "
              f"« Stéatose avec plusieurs facteurs cardiométaboliques, alcool à la borne de MetALD tant qu'il n'est pas recompté, "
              f"{FIB}-4 au-dessus de 2,67 donc élastographie maintenant, pas d'acide ursodésoxycholique, pas de dose inventée, "
              f"Child-Pugh seulement si la cirrhose est montrée, et les trois classes si on le cite. » "
              f"Tout le reste est du commentaire. Cette phrase suffit, à condition que les seuils cités soient les bons.", 5, 9, 12),
            P("Lettre au spécialiste, ce qu'elle contient. L'âge, le sexe, les facteurs cochés un par un avec le seuil utilisé, "
              "l'alcool en grammes et comment il a été estimé, les enzymes avec la limite du laboratoire, les plaquettes en milliards par litre, "
              "le FIB-4 et sa zone, ce qui a déjà été fait pour le poids et le diabète, les médicaments de la liste stéatogène, "
              "et la question précise : élastographie, ou avis parce que le score est au-dessus de 2,67. "
              "Une lettre qui dit seulement « stéatose, merci de voir » ne permet pas de prioriser.", 5),
            P("Ce que la lettre ne contient pas. Une dose de médicament hépatique. Un Child-Pugh si la cirrhose n'est pas établie. "
              "Un grade de Tokyo si personne n'a de fièvre ni de voie dilatée. Un nomogramme. "
              "Ces outils sont vrais dans d'autres fichiers du lot. Les mettre ici montre qu'on n'a pas choisi le bon chapitre.", 5, 9, 18),
            P(f"Retour du spécialiste. S'il décrit une fibrose avancée, le généraliste reprend le dépistage du carcinome et la prévention des complications, "
              f"et il classe la cirrhose en Child-Pugh A, B ou C sans en cacher une. "
              f"S'il décrit une fibrose absente ou légère, le généraliste garde le terrain et refait le {FIB}-4 dans un à trois ans, "
              f"plus tôt si l'enzyme ou les plaquettes changent. Le compte rendu ne s'archive pas sans date de revue.", 5, 9),
            P("Cas limite d'âge. À 64 ans et 11 mois, le seuil bas reste 1,3. Le lendemain des 65 ans, il passe à 2,0. "
              "La copie qui applique 2,0 « parce que le patient est âgé » à 60 ans a inventé un seuil. "
              "La copie qui garde 1,3 à 70 ans en a ignoré un.", 5),
            P(f"Pourquoi ce diagnostic ouvre la leçon. La recommandation de 2024 le dit maladie chronique du foie la plus fréquente. "
              f"Il est pourtant le dernier de l'algorithme de la Phase A, parce qu'il ne tue pas dans l'heure. "
              f"La fréquence et l'urgence ne sont pas le même classement. Le DX.1 est la fréquence. Le rang E10 est l'urgence. "
              f"Les écrire l'un pour l'autre est la confusion que le correcteur cherche.", 5),
            P(f"Ce que l'on a lu et que l'on garde en entier pour ce diagnostic : les sous-classes de stéatose, les familles de facteurs avec leurs seuils ethniques, "
              f"les trois zones du {FIB}-4 et le déplacement après 65 ans, l'inutilité avant 35 ans, les deux chemins de la zone du milieu, "
              f"le refus du dépistage de population, et l'interdiction d'étendre les conseils à MetALD. "
              f"Ce que l'on ne fabrique pas : une dose en milligrammes, un seuil d'élastographie en kilopascals qui n'est pas dans l'extrait, "
              f"un classement suisse de prévalence. "
              f"On répète enfin la formule avant de quitter la copie : âge fois {ASAT}, divisé par les plaquettes en milliards par litre fois la racine carrée de l'{ALAT}. "
              f"Sans cette phrase, le seuil 1,3 ou 2,67 flotte. Avec elle, le correcteur voit que l'unité des plaquettes a été comprise, "
              f"et que le chiffre 2,0 n'a pas été collé sur le mauvais âge. "
              f"Même exigence pour l'alcool : écrire la bande en toutes lettres, vingt à cinquante grammes chez la femme, trente à soixante chez l'homme, "
              f"puis plus de cinquante et plus de soixante pour la maladie alcoolique. "
              f"Un étudiant qui n'écrit qu'une de ces trois bandes a amputé la classification lue en 2024. "
              f"Il en va de même des facteurs : indice, trois tours de taille, prédiabète, diabète, triglycérides, HDL, pression. "
              f"Citer seulement le diabète et l'obésité laisse quatre familles dehors. "
              f"La copie complète nomme aussi le HDL, les triglycérides, la pression à 130/85 et les tours de taille non européens. "
              f"Sans ces lignes, le tableau de 2024 est amputé, et le diagnostic devient une impression clinique au lieu d'un critère lu dans la recommandation de 2024, pas d'une habitude de service. "
              f"On termine en rappelant que le dépistage de toute la population n'est pas recommandé : ce cas est un repérage ciblé, pas une campagne.", 5),
            P("Le correcteur retire des points pour une classe manquante, une unité fausse, un score d'une autre maladie, "
              "et une dose en milligrammes qui ne figure ni dans une information suisse ni dans la recommandation lue. "
              "Il ne retire pas des points parce que la copie est plus courte que le cours, s'il y a les seuils, le pas à pas et le cas.", 5),
        ]))
    )
