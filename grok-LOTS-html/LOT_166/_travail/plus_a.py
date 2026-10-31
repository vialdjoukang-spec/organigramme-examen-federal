# -*- coding: utf-8 -*-
"""Fenêtres supplémentaires de la Phase A, faits déjà sourcés."""


def etendre(ilots, fen, p, table):
    ile, fens = ilots["p8"]
    fens.append(fen("w-ex-light", "Trois liquides pleuraux, calculés", "".join([
        p("Exemple 1. Protéine pleurale 28 g/l, protéine sérique 70 g/l, rapport 0,40. Lactate déshydrogénase pleurale 90 UI/l, sérique 200 UI/l, rapport 0,45. La limite supérieure du laboratoire est 250 UI/l, les deux tiers valent environ 167 UI/l. Aucun des trois critères n'est rempli : transsudat. On cherche le cœur, le foie, l'albumine, pas une biopsie pleurale.", "1"),
        p("Exemple 2. Protéine pleurale 45 g/l, sérique 68 g/l, rapport 0,66. Un seul critère suffit. C'est un exsudat même si la lactate déshydrogénase est basse. Cytologie, culture, et selon le contexte tuberculose ou embolie.", "1"),
        p("Exemple 3. Rapport de protéines 0,48, rapport de lactate déshydrogénase 0,55, mais la lactate déshydrogénase pleurale est à 400 UI/l et la limite du laboratoire est 250 UI/l. Deux tiers de 250 font 167. 400 est au-dessus : exsudat par le troisième critère seul. Oublier ce critère classe à tort le liquide en transsudat.", "1"),
        p("On prélève le sang le même jour. Une protéine sérique de la veille, après une perfusion, fausse le rapport. Un laboratoire qui change de méthode de lactate déshydrogénase change le seuil des deux tiers : on lit la norme du compte rendu, on ne la récite pas de mémoire.", "1"),
        p("Un épanchement bilatéral de l'insuffisance cardiaque connue, sans fièvre, sans douleur, peut être surveillé sans ponction si la clinique est typique. Toute atypie, unilatéralité, fièvre ou échec du traitement diurétique ramène à la ponction. La BTS ne dispense pas de Light quand le diagnostic n'est pas évident.", "1"),
    ])))
    ile, fens = ilots["p8"]
    fens.append(fen("w-ex-saag", "Trois ascites, gradient calculé", "".join([
        p("Exemple 1. Albumine sérique 32 g/l, albumine d'ascite 8 g/l. Gradient 24 g/l, soit 2,4 g/dl, au-dessus de 11 g/l. Hypertension portale. Si les neutrophiles sont à 40 par mm³ et la protéine à 10 g/l, c'est l'ascite de cirrhose non infectée. La protéine sous 1,5 g/dl, ici 10 g/l soit 1,0 g/dl, marque un risque de péritonite bactérienne spontanée, pas une infection actuelle.", "2"),
        p("Exemple 2. Albumine sérique 28 g/l, albumine d'ascite 22 g/l. Gradient 6 g/l, sous 11 g/l. Ce n'est pas l'hypertension portale qui explique le liquide. Carcinose, tuberculose, pancréatite, néphrotique ou fuite biliaire. La cytologie et l'amylase viennent avant un nouveau diurétique.", "2"),
        p("Exemple 3. Albumine sérique 30 g/l, albumine d'ascite 18 g/l. Gradient 12 g/l, juste au-dessus de 11 g/l. Le seuil est inclus dans la formulation « au moins 1,1 g/dl » de l'EASL. Un gradient à 10 g/l serait en dessous. On ne « arrondit » pas un 10,8 vers le haut pour sauver une hypothèse de cirrhose.", "2"),
        p("Le gradient se calcule sur des prélèvements simultanés. Une albumine sérique dosée après une perfusion d'albumine n'est plus celle du jour de la ponction. On le note dans le dossier.", "2"),
        p("Exactitude lue d'environ 97 % : le gradient ne remplace pas la biopsie quand la clinique contredit le chiffre. Un cancer du foie avec hypertension portale peut donner un gradient haut et une cytologie positive. Les deux examens coexistent.", "2"),
    ])))
    ile, fens = ilots["p10"]
    fens.append(fen("w-ex-rapid", "Trois scores RAPID, calculés jusqu'au bout", "".join([
        p("Patient A. Urée 4,2 mmol/l (0), 46 ans (0), pus macroscopique (0), infection de ville (0), albumine 32 g/l (0). Total 0. Risque bas, bande 0 à 2. Le drain est quand même posé parce que c'est du pus. Le score ne contredit pas le drain. Il dit que la mort à trois mois est moins probable.", "1"),
        p("Patient B. Urée 6,5 mmol/l (1), 66 ans (1), liquide trouble non purulent (1), infection de ville (0), albumine 24 g/l (1). Total 4. Bande moyenne, 3 à 4. On dit au patient que le risque n'est pas celui du groupe bas. On ne transforme pas ce 4 en indication opératoire.", "1"),
        p("Patient C. Urée 11 mmol/l (2), 78 ans (2), liquide non purulent (1), infection nosocomiale (1), albumine 21 g/l (1). Total 7. Bande haute, 5 à 7. Le point de non-purulence est contre-intuitif et il est obligatoire. Lui donner zéro parce que « ce n'est pas du pus, donc c'est moins grave » inverse le score.", "1"),
        p("Contrôle d'addition. Le maximum théorique est 2+2+1+1+1 = 7. Un total de 8 est une erreur de saisie. L'urée à 8,0 mmol/l est dans la classe 5,0 à 8,0, donc 1 point, pas 2. Le 2 commence au-dessus de 8,0.", "1"),
        p("L'albumine à 27,0 g/l est dans la classe supérieure à 27 ? Le tableau dit supérieur à 27,0 = 0 et inférieur à 27,0 = 1. La valeur pile 27,0 n'est pas une troisième case. On ne l'invente pas : on reprend le laboratoire et l'on suit la classe écrite la plus proche sans créer un point fantôme. Dans la pratique, 27,0 se lit avec la ligne « supérieur à 27,0 » si l'on applique le signe strict du tableau, et l'on le dit.", "1"),
        p("Rahman, Chest 2014 : dans la dérivation, un score de 3 à 4 et un score au-dessus de 4 augmentaient fortement la mort à trois mois par rapport au groupe 0 à 2. La validation MIST2 confirmait le groupe haut. Ce sont des rapports de cotes, pas des pourcentages à réciter comme des certitudes individuelles.", "17"),
    ])))
    ile, fens = ilots["p6"]
    fens.append(fen("w-technique", "Comment tenir la sonde, fenêtre par fenêtre", "".join([
        p("Hypocondre droit. Patient sur le dos, ou légèrement tourné sur le côté gauche. Sonde abdominale basse fréquence, longitudinale, sur la ligne axillaire antérieure ou moyenne, en regard des dernières côtes. On cherche le diaphragme, le foie, puis le rein. L'espace de Morison est la fente entre les deux. On balaie le pôle supérieur du rein. Une bande noire qui s'ouvre quand on met le patient en déclive est du liquide."),
        p("Hypocondre gauche. Plus postérieur et plus céphalique que la droite, parce que la rate est haute et postérieure. On voit la rate, le rein gauche, le diaphragme. L'espace spléno-rénal vide n'exclut pas un petit saignement déjà tombé dans le Douglas."),
        p("Pelvis. Sonde au-dessus du pubis, vessie pleine si possible, coupe sagittale puis transverse. Chez la femme, le liquide se collecte d'abord dans le cul-de-sac de Douglas, derrière l'utérus. Chez l'homme, entre vessie et rectum. Une vessie vide fait manquer la fenêtre."),
        p("Sous-xiphoïdien. Sonde à plat sous l'appendice xiphoïde, dirigée vers l'épaule gauche, foie comme fenêtre. On cherche les quatre cavités et un liseré noir autour. On ne confond pas le coussin graisseux péricardique antérieur, souvent un peu échogène, avec un épanchement circonférentiel."),
        p("Base pulmonaire. Ligne axillaire postérieure, patient assis si possible, ou allongé pour Balik. Le diaphragme est la ligne brillante. Au-dessus, le poumon glisse. Le liquide est noir, déclive, et la colonne se voit à travers lui. On fige l'image en fin d'expiration pour mesurer la séparation.", "5"),
        p("Le repère D des schémas est à gauche de l'écran, convention radiologique. Sur une coupe longitudinale de l'hypocondre, ce repère rappelle le côté exploré. Il ne transforme pas la coupe en axiale."),
    ])))
    ile, fens = ilots["p9"]
    fens.append(fen("w-coag", "Coagulation, grossesse, enfant", "".join([
        p("L'EASL ne retient pas la transfusion prophylactique de plasma ou de plaquettes avant une paracentèse, faute de donnée, y compris quand l'habitude locale est de transfuser sous 40 % de prothrombine ou 40 000 plaquettes. La coagulation intravasculaire disséminée reste une raison de ne pas faire une grande évacuation.", "2"),
        p("Une série citée : INR supérieur à 1,5 et plaquettes inférieures à 50 000, deux saignements mineurs du point de ponction sur 142 gestes. Ce n'est pas un permis de ponctionner n'importe comment. C'est un argument pour ne pas retarder une ponction diagnostique qui change l'antibiotique.", "2"),
        p("Grossesse. Une bande noire dans le Douglas peut être physiologique en petite quantité. Une grande quantité, une douleur, une instabilité, une grossesse extra-utérine possible : c'est du sang jusqu'à preuve du contraire, et ce n'est pas une ascite cirrhotique. La bêta-gonadotrophine vient en même temps que l'échographie."),
        p("Enfant. Les doses d'Aldactone lues sont 1.5-3.0 mg/kg. Lasix oral : 2 mg de furosémide par kg, sans dépasser 40 mg par jour. Ce ne sont pas les paliers de l'ascite de l'adulte. La péritonite bactérienne spontanée de l'enfant cirrhotique se discute avec le pédiatre : la fourchette de ceftriaxone pédiatrique lue est 20 à 50 mg par kg, sans dépasser 50 mg par kg, et le nouveau-né prématuré a des contre-indications propres au produit, n° 59876.", "12"),
        p("On ne récite pas une dose adulte à un nourrisson. On ouvre l'information professionnelle du flacon qu'on a dans la main."),
    ])))
    ile, fens = ilots["p4"]
    fens.append(fen("w-ordre", "Ce qui se fait en parallèle, sans attendre", "".join([
        p("Dès la porte : pression, saturation, voie veineuse si le patient est instable, oxygène si la saturation baisse. Ces gestes ne dépendent pas du résultat de la ponction."),
        p("En parallèle, pas « après » : électrocardiogramme si douleur thoracique ou suspicion de tamponnade, groupe sanguin si trauma ou hémorragie digestive, bêta-gonadotrophine si femme en âge de procréer et liquide pelvien, lactates si marbrures."),
        p("La ponction d'ascite fébrile ne se place pas après le scanner. Le scanner cherche la perforation si la défense est localisée ou si l'air libre est suspecté. La péritonite bactérienne spontanée, elle, se traite sur les neutrophiles."),
        p("L'échographie pleurale et la radiographie ne se concurrencent pas. La radiographie montre un niveau ou un pneumothorax sous tension. L'échographie guide l'aiguille et voit le petit liquide postérieur que le cliché couché rate.", "1"),
        p("On n'attend pas la culture pour la première dose si les neutrophiles sont au-dessus de 250 ou si le pus sort de la plèvre. On n'attend pas non plus la dose pour prélever. L'ordre est : prélever, puis injecter, dans la même heure.", "2"),
    ])))
    ile, fens = ilots["p11"]
    fens.append(fen("w-suite", "Après la première heure", "".join([
        p("Ascite cirrhotique non infectée, grade 2, premier épisode : antiminéralocorticoïde seul, contrôle du poids chaque jour, ionogramme à 72 heures avant d'augmenter, parce que l'effet d'Aldactone n'est pas là au premier matin.", "10"),
        p("Grade 3 : grande évacuation le jour même, albumine selon le volume retiré, puis la dose minimale de diurétique qui empêche la reconstitution. C'est l'ordre de l'EASL, pas l'inverse.", "2"),
        p("Infection pleurale drainée par un drain de 14 French ou moins : surveillance du débit, de la fièvre, de la radiographie ou de l'échographie. L'absence de vidange avec des cloisons fait discuter la fibrinolyse ou le chirurgien, pas un deuxième antibiotique au hasard. La BTS ne place pas la chirurgie en premier.", "1"),
        p("Tamponnade drainée : le liquide part en culture, cytologie, et selon le terrain tuberculose. L'ESC rappelle qu'une lame isolée sans inflammation répond mal aux anti-inflammatoires. On ne laisse pas la colchicine « pour voir » si rien n'est inflammatoire.", "3"),
        p("Hémorragie variqueuse contrôlée : la ponction d'ascite a déjà été faite. Glypressine se poursuit selon la notice, au plus cinq jours, avec le rythme lu, et l'on baisse si la pression ou l'électrocardiogramme se dégrade.", "16"),
        p("Tout patient sort avec une phrase claire : fièvre, confusion, ventre qui regonfle, essoufflement, syncope. Le numéro du service est dans le compte rendu, pas dans cette leçon."),
    ])))
    ile, fens = ilots["p2"]
    fens.append(fen("w-pas-suisse", "Ce qui n'est pas un chiffre suisse", "".join([
        p("Aucune incidence suisse de l'ascite ni de l'épanchement pleural n'a été lue dans les sources ouvertes pour cette leçon. On n'en invente pas. Le 80 % de cirrhose parmi les ascites est un chiffre occidental de l'EASL, pas un registre suisse.", "2"),
        p("Le 5 à 10 % par an de passage d'une cirrhose compensée vers l'ascite est le même texte. Il sert à dire que l'ascite est la décompensation la plus fréquente, pas à calculer un nombre de cas à Genève.", "2"),
        p("Les sensibilités du protocole BLUE sont celles d'une réanimation universitaire en 2008, 260 patients avec diagnostic final retenu. On ne les transporte pas comme la performance d'un échographe de cabinet sans le dire.", "6"),
        p("La valeur prédictive négative de 97,8 % du signe de la colonne est celle d'une série de trauma de 76 patients, 222 images, contre le scanner. Elle ne s'applique pas telle quelle à l'épanchement médical du sujet âgé.", "7"),
    ])))
    ile, fens = ilots["p11"]
    fens.append(fen("w-jour-empyeme", "Infection pleurale, les jours qui suivent", "".join([
        p("Jour 0. La ponction est guidée. Si le pus coule, le drain de petit calibre est posé dans le même temps, 14 French ou moins. Si le liquide est clair ou trouble, le pH part tout de suite, sans lidocaïne dans la seringue et sans héparine résiduelle. Le glucose est prélevé en même temps, pour le cas où le pH serait illisible.", "1"),
        p("Le score RAPID se calcule sur l'urée, l'âge, la purulence, le lieu et l'albumine, pour la conversation sur le risque, pas pour choisir le calibre du drain. On l'écrit dans le dossier avec les cinq items, pas avec un total nu.", "1"),
        p("Jour 1. Fièvre, débit du drain, échographie de contrôle si le patient reste septique. Une collection résiduelle cloisonnée n'est pas un échec automatique de l'antibiotique. La BTS ne met pas la chirurgie en première intention. Elle ne met pas non plus la thoracoscopie médicale en première intention.", "1"),
        p("Si le pH était entre 7,2 et 7,4 et qu'on n'a pas drainé, on revoit le patient le jour même ou le lendemain. Une fièvre qui persiste, un volume qui augmente ou des cloisons nouvelles font reponctionner. Laisser passer le week-end sur un pH à 7,25 sans revoir est le scénario que la recommandation veut éviter.", "1"),
        p("L'antibiotique suit le germe quand il est connu. La leçon ne récite pas une durée inventée. Elle rappelle que le drain et le pH décident de l'évacuation, et que l'antibiothérapie seule ne vide pas un empyème.", "1"),
        p("Sortie. Le patient sait reconnaître une fièvre, une douleur qui revient, un essoufflement. Le drain, s'il est encore là, a une consigne écrite de qui l'enlève. On ne retire pas un drain productif le soir parce que le lit manque."),
    ])))
    ile, fens = ilots["p8"]
    fens.append(fen("w-malin", "Épanchement suspect de cancer", "".join([
        p("Un liquide unilatéral, un exsudat, un amaigrissement : la cytologie part sur 25 à 50 ml. La BTS en fait une recommandation forte. Un tube de 5 ml « pour voir » n'est pas le prélèvement décrit.", "1"),
        p("Une cytologie négative n'innocente pas. La biopsie, thoracoscopique ou guidée par l'image, vient ensuite selon la disponibilité locale. La biopsie à l'aveugle, sans image, est déconseillée, recommandation forte de consensus.", "1"),
        p("Les cloisons d'un épanchement malin ne se traitent pas comme un empyème. La BTS n'a pas trouvé d'étude qui compare les enzymes intrapleurales à la chirurgie dans cette situation. On ne copie pas le protocole de l'infection.", "1"),
        p("Le mésothéliome et le cancer évolué peuvent donner un pH bas et des cloisons, et mimer une infection. La recommandation le met dans les bons réflexes. Un pH à 7,05 sans fièvre et avec un épaississement circonférentiel n'est pas un empyème par défaut.", "1"),
        p("L'épanchement pleural malin et l'ascite maligne sont deux diagnostics de la leçon. L'un n'entraîne pas l'autre. On décrit le compartiment qu'on a ponctionné."),
    ])))
    ile, fens = ilots["p3"]
    fens.append(fen("w-coeur", "Cœur, plèvre et ascite", "".join([
        p("L'insuffisance cardiaque congestive est listée par la BTS parmi les transsudats fréquents. Le liquide est souvent des deux côtés. Un côté seul, de la fièvre, une douleur pleurale ou un échec des diurétiques font ponctionner et calculer Light.", "1"),
        p("L'ascite cardiaque partage avec la cirrhose un gradient d'albumine haut, parce que la pression veineuse sus-hépatique est une hypertension portale. Ce n'est pas une raison pour donner le schéma de spironolactone de la cirrhose sans lire le cœur. L'information professionnelle des œdèmes cardiaques d'Aldactone est 100 mg par jour, jusqu'à 200 mg par jour dans les cas difficiles, entretien souvent 25 à 100 mg par jour, n° 27257. Ce n'est pas le paragraphe « cirrhose avec ascite ».", "10"),
        p("Lasix dans l'œdème aigu du poumon n'est pas le comprimé de l'ascite. La leçon ne mélange pas la voie intraveineuse de l'œdème pulmonaire, qui est une autre spécialité du même nom, avec le comprimé à 40 mg dont la notice orale a été lue, n° 30629.", "11"),
        p("Le peptide natriurétique aide quand on hésite entre cœur et poumon. Il ne remplace pas Light si le liquide est ponctionné. Un transsudat et un peptide haut vont dans le même sens. Un exsudat et un peptide haut disent que les deux maladies peuvent coexister.", "1"),
        p("La tamponnade donne des jugulaires tendues et un cœur qui se remplit mal. Ce n'est pas l'insuffisance cardiaque gauche habituelle, qui donne un œdème pulmonaire et des lignes B. Le protocole BLUE sépare l'œdème, lignes B avec glissement, de l'épanchement postérieur de la pneumonie.", "6"),
    ])))
    ile, fens = ilots["p7"]
    fens.append(fen("w-tampon-signes", "Tamponnade, signes à citer ensemble", "".join([
        p("La tamponnade est une compression, lente ou rapide, par du liquide, du pus, du sang, des caillots ou du gaz. Le tableau clinique lu dans l'ESC 2015 : tachycardie, hypotension, pouls paradoxal, jugulaires tendues, bruits assourdis, microvoltage et alternance électrique, silhouette élargie si le liquide s'est accumulé lentement.", "3"),
        p("Le pouls paradoxal est défini comme une baisse inspiratoire de plus de 10 mmHg de la pression systolique, en respiration normale. Il peut manquer. On ne l'exige pas pour appeler le drainage.", "3"),
        p("L'échographie montre la lame et son retentissement : collapsus de l'oreillette droite, collapsus diastolique du ventricule droit, veine cave inférieure dilatée qui se collabe peu à l'inspiration, variations respiratoires des flux. Aucun signe isolé ne remplace la pression artérielle.", "3"),
        p("Taille, trois classes, à ne pas réduire à « petit ou gros » : moins de 10 mm, de 10 à 20 mm, plus de 20 mm, en fin de diastole. L'ESC 2025 reprend la lame large au-dessus de 20 mm et la lame modérée à large de 10 à 20 mm parmi les critères d'imagerie.", "4"),
        p("Une lame de moins de 10 mm, idiopathique, sans symptôme, a en général un bon pronostic et n'exige pas de surveillance particulière selon l'ESC 2015. Une lame au-dessus de 10 mm peut évoluer. Le suivi proposé pour une lame modérée idiopathique est de l'ordre de six mois, et de trois à six mois pour une lame sévère, à adapter à la stabilité.", "3"),
        p("Le sac normal contient 10 à 50 ml. On ne draine pas ces millilitres. On draine la compression, le soupçon de pus ou de sang, et les lames dont la cause ou le volume impose le geste. Le schéma de la leçon sépare « sans lame », « lame » et « compression » pour cette raison.", "3"),
    ])))
    ile, fens = ilots["p10"]
    fens.append(fen("w-dix", "Les dix diagnostics, un critère qui les sépare", "".join([
        table("Ne pas les fusionner", ["Diagnostic", "Ce qui le retient", "Ce qui l'écarte"], [
            ["Ascite de l'hypertension portale", "Gradient d'au moins 11 g/l, cirrhose ou bloc sus-hépatique, neutrophiles bas", "Gradient sous 11 g/l"],
            ["Épanchements de l'insuffisance cardiaque", "Transsudat de Light, souvent des deux côtés, peptide natriurétique haut, ascite à gradient haut possible", "Exsudat franc, fièvre, un seul côté sans raison cardiaque"],
            ["Épanchement parapneumonique et empyème", "Pneumonie et liquide. Pus, ou pH ≤ 7,2, ou glucose inférieur à 3,3 mmol/l", "pH ≥ 7,4, pas de pus, patient qui va mieux"],
            ["Péritonite bactérienne spontanée", "Ascite et neutrophiles au-dessus de 250 par mm³", "Défense localisée et air libre, qui font chercher une perforation"],
            ["Hémopéritoine et hémothorax", "Trauma ou choc, liquide libre, hémoglobine qui chute", "Liquide clair, chronique, patient stable"],
            ["Épanchement pleural malin", "Exsudat, souvent unilatéral, cytologie ou biopsie", "Transsudat qui fond sous diurétique"],
            ["Ascite maligne", "Gradient sous 11 g/l, cytologie, contexte tumoral", "Gradient haut d'une cirrhose, même si un cancer du foie coexiste : les deux peuvent être vrais"],
            ["Épanchement péricardique et tamponnade", "Lame en fin de diastole, et signes de compression pour la tamponnade", "Lame de moins de 10 mm, patient stable, sans signe électrique"],
            ["Pleurésie tuberculeuse", "Exsudat lymphocytaire, cloisons, exposition, biopsie ou culture", "Pus à germes banals et pneumonie franche"],
            ["Ascite par hypoalbuminémie", "Albumine sérique très basse, néphrotique ou dénutrition, gradient souvent bas", "Gradient haut, qui ramène vers le foie ou le cœur"],
        ]),
        p("Le rang E n'est pas cette colonne. E1 est la tamponnade, E2 le sang libre, E3 l'empyème, E4 la péritonite bactérienne spontanée, puis les causes plus lentes. On exclut dans l'ordre E, on enseigne dans l'ordre DX."),
        p("Aucun de ces dix noms ne se retire parce qu'une série suisse de fréquence manque. La fréquence manquante est notée à part. Le critère, lui, reste.", "2"),
    ])))
    ile, fens = ilots["p5"]
    fens.append(fen("w-anamnese-longue", "Anamnèse par compartiment", "".join([
        p("Plèvre droite isolée : infection, cancer, embolie, tuberculose, plus souvent qu'un simple cœur. Le cœur donne plutôt les deux côtés, avec un peu plus à droite. Une douleur basithoracique inspiratoire oriente vers la plèvre inflammatoire, pas vers le transsudat."),
        p("Plèvre gauche isolée : pancréatite, rupture œsophagienne, dissection aortique selon le contexte douloureux. L'amylase pleurale se demande si le ventre est suspect. On ne la dose pas à tout le monde."),
        p("Ascite qui s'installe en semaines, avec angiomes stellaires, érythrose palmaire, circulation collatérale : cirrhose jusqu'à l'analyse du liquide. L'analyse reste obligatoire à l'hôpital.", "2"),
        p("Ascite qui s'installe en jours, avec œdèmes des paupières le matin et urines mousseuses : syndrome néphrotique. La bandelette urinaire et l'albuminémie passent avant la spironolactone de cirrhose."),
        p("Ascite et masse, amaigrissement, ganglion : carcinose. Le gradient sera souvent bas. On ne commence pas par 400 mg de spironolactone."),
        p("Douleur scapulaire, malaise, arrêt des règles ou saignement, femme en âge de procréer : grossesse extra-utérine et hémopéritoine, en même temps que le Douglas. Ce n'est pas une ascite."),
        p("Douleur thoracique, syncope, cancer ou tuberculose connue, veines du cou : péricarde. L'électrocardiogramme cherche le microvoltage et l'alternance. L'échographie sous-xiphoïdienne cherche la lame et le collapsus.", "3"),
        p("Fièvre au retour d'une zone d'endémie, sueurs nocturnes, liquide qui se cloisonne : tuberculose pleurale ou péritonéale. L'isolement respiratoire se discute si le poumon est aussi malade, pas sur une ascite seule."),
    ])))
    ile, fens = ilots["p14"]
    fens.append(fen("w-cas-2", "Deux autres cas courts", "".join([
        p("Cas pleural. Femme de 72 ans, pneumonie du lobe inférieur droit traitée depuis trois jours, toujours fiévrile. L'échographie montre un liquide postérieur, la colonne se voit au-dessus du diaphragme, quelques cloisons. La ponction ramène un liquide trouble, pas de pus franc. pH 7,12. Glucose 2,1 mmol/l."),
        p("Correction. pH ≤ 7,2 et glucose inférieur à 3,3 mmol/l : les deux seuils de haut risque sont franchis. Drain de petit calibre si le volume est accessible. On calcule aussi le score RAPID pour le pronostic, sans en faire la raison du drain. On ne cite pas Balik pour chiffrer ce volume : l'empyème et le parapneumonique compliqué étaient exclus de la formule.", "1"),
        p("Cas péricarde. Homme de 40 ans, douleur thoracique depuis six heures, frottement, pression 125/80 mmHg, pas de pouls paradoxal. L'échographie mesure une lame circonférentielle de 8 mm en fin de diastole, pas de collapsus, veine cave qui se collabe. Pas d'ascite."),
        p("Correction. Classe légère, moins de 10 mm, patient stable : ce n'est pas une tamponnade. Anti-inflammatoire si pas de contre-indication, et colchicine selon l'ESC, pas selon le schéma de la goutte. On ne donne pas l'ibuprofène s'il existait une ascite. Ici il n'y en a pas. On ne draine pas une lame de 8 mm stable.", "3"),
    ])))
