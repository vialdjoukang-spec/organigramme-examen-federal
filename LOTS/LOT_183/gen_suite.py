#!/usr/bin/env python3
"""Suite DX.6–DX.10 et écriture des fichiers. Importe le générateur DX.5."""
import importlib.util
import os
import json

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("g", os.path.join(HERE, "_gen_dx5_10.py"))
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)

p, table, inline, fen, ital = g.p, g.table, g.inline, g.fen, g.ital
point, mono, page, auxo_table, exemple_cible = g.point, g.mono, g.page, g.auxo_table, g.exemple_cible
DATE = g.DATE


def dx6():
    S = "[S301]"
    ps, pezz, jenni, gal, espe = "[S302]", "[S303]", "[S304]", "[S305]", "[S306]"
    c = []
    c.append(point(1, "Définition et sémantique", [
        p("La petite taille familiale est le cadre où l'enfant est petit parce que ses parents sont petits, et où sa courbe reste cohérente avec la " + inline("taille cible parentale", [
            "pédiatrie suisse, dans Paediatrica, donne la formule la plus courante : [taille maternelle + taille paternelle ± 13 cm] / 2.",
            "On ajoute 13 cm pour le garçon et on soustrait 13 cm pour la fille. L'intervalle lu est ± 8,5 cm, soit ± 2 déviations standards.",
            "La mesure des parents est un acte médical. Une taille déclarée de mémoire ne sert pas de cible.",
        ], jenni) + "."),
        p("La petite taille statistique, dans le même texte, est la taille sous le 3e percentile, soit −1,88 déviation standard. Cette définition décrit une position sur la courbe. Elle ne nomme pas, à elle seule, la cause familiale."),
        p("Les sources ouvertes ne donnent pas une liste numérotée intitulée « critères de petite taille familiale » par une société suisse. Le cadre utilisé ici est donc auxologique : taille basse, cible basse, canal stable après 2 ans selon le PEZZ, et absence des critères de retard constitutionnel (puberté tardive et âge osseux retardé) décrits par l'ESPE et par Galazzi."),
        fen("Fenêtre 1.1 — Ne pas confondre trois phrases", [
            table(["Phrase", "Ce qu'elle signifie", "Ce qu'elle ne signifie pas"], [
                ["Sous le 3e percentile", "Petite taille statistique, −1,88 DS dans le texte suisse de 2016.", "Une maladie."],
                ["Dans la cible ± 8,5 cm", "La taille s'explique par les parents mesurés.", "Que la vitesse est normale : il faut encore la calculer."],
                ["Canal stable après 2 ans", "Le PEZZ décrit l'ajustement génétique des deux premières années, puis un canal hérité.", "Qu'un changement de canal est anodin."],
            ]),
            p("Piège : dire « c'est familial » sans avoir mesuré les parents."),
        ], jenni + ", " + pezz),
    ]))
    c.append(point(2, "Épidémiologie (Suisse, puis Europe)", [
        p("Par construction statistique, autant d'enfants se situent sous le 3e percentile qu'au-dessus du 97e. Ce fait, lu dans Paediatrica, ne donne pas la part de petite taille qui est familiale."),
        p("La prévalence suisse de la petite taille familiale, le sex-ratio et la mortalité : donnée non trouvée dans les sources consultées. Il n'y a pas de mortalité propre à cette variante dans les textes lus."),
        p("Enjeu de santé : les consultations pour grande taille sont plus rares que pour petite taille, écrit le même article, parce que la société accepte mieux la grande taille. La petite taille familiale consomme donc des bilans si on ne calcule pas la cible."),
        p("Les nouvelles courbes PEZZ, recommandées par pédiatrie suisse depuis le 15 juin 2026, reposent sur plus de 43 000 enfants. Elles changent la référence, pas le devoir de comparer l'enfant à ses parents."),
        fen("Fenêtre 2.1 — Exemple de cible, calcul dérivé", exemple_cible(jenni) + [
            p("Si ce garçon mesure 168 cm à la fin de la croissance, il est dans l'intervalle 166,5–183,5 cm. S'il mesure 160 cm, il est sous la cible et le mot « familial » ne suffit plus."),
        ], jenni),
    ]))
    c.append(point(3, "Physiopathologie", [
        p("Le PEZZ décrit deux années pendant lesquelles l'enfant ajuste sa croissance au modèle hérité, puis un canal de percentile qu'il devrait suivre jusqu'à la puberté. La petite taille familiale est ce canal, situé bas parce que le patrimoine statural des parents est bas."),
        p("Le cartilage répond normalement à la nutrition, à l'hormone de croissance, aux hormones thyroïdiennes puis aux stéroïdes sexuels. Rien n'est à « corriger » par un médicament dans la variante pure. Le traitement qui respecte le mécanisme est de ne pas medicaliser une trajectoire parallèle."),
        table(["Perturbation apparente", "Exploration", "Conduite qui respecte le mécanisme"], [
            ["Taille sous le 3e percentile dès l'enfance", "Courbe répétée et cible parentale.", "Surveillance si la vitesse garde le canal et si la cible est basse."],
            ["Crainte d'un déficit en hormone de croissance", "La vitesse et l'IGF-1 ne sont pas un traitement. On ne stimule que si le tableau n'est plus familial.", "Ne pas donner d'hormone de croissance à un canal parallèle cohérent avec la cible."],
            ["Puberté à l'heure et âge osseux concordant", "Stade de Tanner et radiographie de la main gauche.", "On distingue ce cadre du retard constitutionnel, dont l'âge osseux retarde."],
        ]),
        fen("Fenêtre 3.1 — Pourquoi un point isolé ne prouve rien", [
            p("Le PEZZ rappelle qu'une courbe compare plusieurs mesures aux pairs. Un percentile unique ne dit pas si le mécanisme de croissance fonctionne."),
            p("Exemple : un garçon au 10e percentile a, parmi 100 enfants sains du même âge et du même sexe, 9 plus petits et 90 plus grands. S'il y reste depuis l'âge de 2 ans et que ses parents sont dans une cible basse, le mécanisme hérité tient."),
        ], pezz),
    ]))
    c.append(point(4, "Démarche diagnostique", [
        p("On écarte d'abord la cassure et la maladie, puis on accepte la variante. Les hypothèses graves ne sont pas la petite taille familiale elle-même."),
        table(["À exclure avant de conclure", "Ce qui tranche", "Piège"], [
            ["Maladie acquise", "Perte de canal après 2 ans, selon le PEZZ.", "Se contenter du percentile du jour."],
            ["Retard constitutionnel", "Puberté absente à 13 ans (fille) ou 14 ans (garçon) et âge osseux retardé, selon l'ESPE.", "Appeler familial un ado impubère."],
            ["Turner chez la fille", "Caryotype, demandé par l'ESPE quand la puberté tarde, et prudent devant une petite taille de fille inexpliquée par la cible.", "Exiger une dysmorphie."],
            ["Déficit somatotrope", "Vitesse très basse et taille très en dessous de la cible. La revue dit que le retard constitutionnel lui-même dépasse rarement une petite taille sévère au-delà de −2,5 DS.", "Traiter par hormone de croissance une cible simplement basse."],
        ]),
    ]))
    c.append(point(5, "Anamnèse ciblée et drapeaux rouges", [
        p("On mesure les parents, on demande les tailles de la fratrie et le calendrier pubertaire parental. Une mère réglée après 15 ans ou un père à poussée très tardive rapproche du retard constitutionnel, pas de la petite taille familiale pure, selon les critères du type 3 cités par Galazzi."),
        p("Drapeaux : cassure de canal, ralentissement net, signes digestifs ou cœliaques, prise de poids avec arrêt de croissance, disproportion, fille petite hors cible."),
        fen("Fenêtre 5.1 — Questions", [
            table(["Question", "Pourquoi", "Alerte"], [
                ["Quelle taille mesurez-vous, père et mère, aujourd'hui ?", "La formule exige des centimètres mesurés.", "Taille « à peu près » refusée."],
                ["L'enfant a-t-il toujours suivi ce canal depuis l'âge de 2 ans ?", "Le PEZZ fait de la stabilité du canal le signe d'un mécanisme intact.", "Changement de canal."],
                ["La puberté a-t-elle commencé à l'heure ?", "Sinon le tempo, et non seulement les gènes staturaux, explique la taille.", "Seuil ESPE franchi."],
            ]),
        ], pezz + ", " + espe),
    ]))
    c.append(point(6, "Examen physique ciblé, région par région", [
        p("Le normal est un enfant harmonieux, au stade pubertaire attendu, sans dysmorphie, dont la taille mesurée tombe dans la cible."),
        p(ital("6.1 Auxologie.") + " Taille, poids, périmètre crânien, report sur la courbe suisse en vigueur, vitesse en cm par an."),
        p(ital("6.2 Proportions.") + " On cherche une disproportion qui ferait quitter le cadre familial vers une dysplasie, comme l'ESPE le mentionne dans les diagnostics à écarter du retard pubertaire."),
        p(ital("6.3 Puberté.") + " Stade de Tanner concordant avec l'âge civil. Un âge osseux concordant soutient ce cadre ; un âge osseux retardé le quitte."),
        fen("Fenêtre 6.1 — Vitesse, même méthode", [
            p("Calcul dérivé : 110,0 cm à 5,0 ans et 115,6 cm à 6,0 ans donnent 5,6 cm en un an, soit 5,6 cm par an. Une vitesse de cet ordre qui prolonge un canal bas reste compatible avec une trajectoire familiale. Une chute franche de canal ne l'est pas."),
            p("Le chiffre 5,6 n'est pas un seuil suisse officiel. C'est un exemple de méthode."),
        ], pezz),
    ]))
    c.append(point(7, "Approche syndromique", [
        p(ital("7.1 Canal bas hérité.") + " Signes fonctionnels : aucun, ou une question parentale sur la taille. Signes physiques : taille basse, proportions normales, puberté à l'heure."),
        fen("Fenêtre 7.1 — Signes définis", [
            table(["Signe", "Comment le chercher", "Mécanisme"], [
                ["Canal parallèle", "Reporter au moins deux mesures espacées sur la courbe recommandée.", "Le patrimoine statural fixe le canal après l'ajustement des deux premières années."],
                ["Cible basse", "Mesurer les parents et appliquer la formule ± 13 cm.", "L'enfant réalise le potentiel parental, il ne le rate pas."],
                ["Âge osseux concordant", "Radiographie de la main et du poignet gauches.", "Les stéroïdes sexuels arrivent à l'heure, donc le cartilage mûrit avec l'âge civil, contrairement au retard constitutionnel."],
            ]),
        ], jenni + ", " + espe),
    ]))
    c.append(point(8, "Diagnostic positif et critères", [
        p("Critères opérationnels, assemblés des sources lues et non issus d'un consensus suisse unique nommé : parents mesurés, taille de l'enfant dans l'intervalle de ± 8,5 cm autour de la cible ou sur un canal bas stable depuis 2 ans, puberté non retardée selon les seuils ESPE, âge osseux non retardé comme dans le retard constitutionnel, examen sans drapeau."),
        p("Ce qui ne suffit pas : « le père est petit » sans mesure, un percentile isolé, ou une taille sous la cible de plus de 2 déviations standards."),
        fen("Fenêtre 8.1 — Certitude limitée", [
            p("La certitude est auxologique et évolutive. Elle augmente si la vitesse reste parallèle sur six à douze mois. Elle tombe si un signe de maladie apparaît."),
        ], pezz),
    ]))
    c.append(point(9, "Examens complémentaires", [
        p(ital("9.a Gold standard.") + " Il est clinique et auxologique. Aucun dosage ne prouve la petite taille familiale."),
        p(ital("9.b Première intention.") + " Courbe, cible, vitesse, stade pubertaire. Un bilan sanguin minimal (TSH, thyroxine libre, sérologie cœliaque selon ESPGHAN si le tableau quitte le canal) sert à ne pas manquer une cause traitable quand un doute existe. S'il n'y a aucun doute auxologique, les sources lues ne rendent pas ce bilan obligatoire."),
        p(ital("9.c et 9.d.") + " Âge osseux si on hésite avec un retard constitutionnel. Tests de stimulation de l'hormone de croissance : pas dans la variante pure. IRM : pas sans signe neurologique ou déficit confirmé."),
        fen("Fenêtre 9.1 — Lecture", [
            table(["Résultat", "Lecture", "Conduite"], [
                ["Taille dans la cible, canal stable, puberté à l'heure", "Cohérent avec la variante familiale.", "Expliquer, surveiller la courbe, ne pas traiter."],
                ["Taille sous la cible de plus de 8,5 cm", "Le patrimoine parental ne suffit plus.", "Reprendre la démarche diagnostique."],
                ["Âge osseux retardé", "Tempo en cause, pas seulement les gènes de taille.", "Lire le DX.5."],
            ]),
        ], jenni),
    ]))
    c.append(point(10, "Arbre décisionnel", [
        p("Parents mesurés et formule calculée d'abord. Si l'enfant est dans la cible et que le canal est stable, on explique. Si la puberté manque aux seuils ESPE, on quitte ce DX. Si le canal casse, on cherche une maladie, dont la cœliaquie et l'hypothyroïdie traitées dans les DX suivants."),
    ]))
    c.append(point(11, "Prise en charge selon les recommandations suisses", [
        p(ital("A- But.") + " Le but n'est pas de changer la taille génétique. Le but est de reconnaître la variante, d'éviter un traitement inutile et de ne pas manquer une vraie cassure. Aucun gain en centimètres n'est promis par les sources lues."),
        p(ital("B- Moyens.") + " Explication de la formule et de la courbe. Aucun médicament n'a d'indication dans la variante pure d'après les textes lus. L'hormone de croissance n'est pas un traitement de la cible basse cohérente. Spécialité, dose AIPS et numéro Swissmedic : sans objet, et donnée non trouvée s'il fallait malgré tout en citer une."),
        p("Situations spéciales : grossesse, sujet âgé, insuffisance rénale ou hépatique : sans objet pour un traitement qu'on ne donne pas. L'enfant reste suivi par les examens de santé ordinaires."),
        p(ital("C- Surveillance.") + " Mesure au moins annuelle, report sur la courbe recommandée depuis le 15 juin 2026. On revoit plus tôt si les parents décrivent une cassure."),
        p("Critère pour rester hors filière endocrinienne : canal stable, cible respectée, puberté à l'heure. Il n'y a pas d'hospitalisation."),
        p(ital("D- Pronostic.") + " La taille adulte reste dans la zone parentale si le cadre était juste. Il n'y a pas de guérison à obtenir. Recherche 2026 : les courbes PEZZ 2025 changent la référence populationnelle, pas le pronostic individuel déjà cohérent avec la cible."),
        fen("Fenêtre 11.1 — Ce que l'on dit aux parents", [
            p("On montre le calcul. On dit que l'enfant grandit comme ses parents le permettent, tant que la vitesse garde le canal. On dit aussi ce qui ferait revenir : une cassure, une puberté absente aux seuils, une disproportion."),
        ], jenni + ", " + pezz),
    ]))
    c.append(point(12, "Prévention", [
        p("Primaire : mesurer les enfants et les parents, tenir la courbe. Secondaire : ne pas enchaîner les dosages quand la cible explique la taille, pour éviter un surdiagnostic. Tertiaire : sans objet au sens d'une séquelle à prévenir, sauf le préjudice d'un traitement hormonal non indiqué."),
    ]))
    c.append(point(13, "Points clés", [
        p("Vous mesurez les parents avant de dire que la taille est familiale."),
        p("Vous calculez [mère + père ± 13 cm] / 2 et vous gardez ± 8,5 cm."),
        p("Vous exigez un canal stable après 2 ans."),
        p("Vous quittez ce diagnostic si la puberté est en retard ou si l'âge osseux retarde."),
        p("Vous ne prescrivez pas d'hormone de croissance pour une cible simplement basse."),
    ]))
    c.append(point(14, "Pièges et questions fréquentes à l'examen fédéral suisse", [
        p("Piège : percentile isolé. Bonne réponse : trajectoire et cible."),
        p("Piège : formule sans le signe selon le sexe. Bonne réponse : +13 cm chez le garçon, −13 cm chez la fille."),
        p("Piège : confondre avec le retard constitutionnel. Bonne réponse : l'âge osseux et le calendrier pubertaire séparent les deux."),
        fen("Fenêtre 14.1 — Question type", [
            p("Fille de 8 ans, toujours vers le 3e percentile depuis l'âge de 3 ans, mère 152 cm mesurée, père 165 cm mesuré, puberté non commencée ce qui est normal à 8 ans, examen normal. Cible : (152 + 165 − 13) / 2 = 152 cm, intervalle environ 143,5 à 160,5 cm. Que faites-vous ?"),
            p("Vous expliquez la cohérence familiale. Vous ne demandez pas un test de stimulation. Vous continuez la courbe annuelle. Calcul dérivé vérifié : 152 + 165 = 317 ; 317 − 13 = 304 ; 304 / 2 = 152."),
        ], jenni),
    ]))
    return mono("DX.6", "Petite taille familiale",
                "Rang du projet — fréquence de l'entité non quantifiée (Suisse) ; le 3e percentile est une définition statistique [S304]",
                "".join(c))


def dx7():
    es = "[S307]"
    c = []
    c.append(point(1, "Définition et sémantique", [
        p("La " + inline("maladie cœliaque", [
            "L'ESPGHAN 2020 la diagnostique par une auto-immunité dirigée contre la transglutaminase de type 2 et, selon le titre, par une biopsie duodénale.",
            "Le régime sans gluten n'est pas la définition. Il est le traitement, une fois le diagnostic posé pendant que l'enfant mange encore du gluten.",
            "Piège : appeler cœliaquie une simple éviction décidée sans sérologie.",
        ], es) + " peut se présenter par un retard statural ou un défaut de croissance, sans diarrhée obligatoire."),
        p("L'ESPGHAN place le défaut de croissance, la petite taille, le défaut de prise de poids, la perte de poids et la diarrhée chronique parmi les manifestations. Les symptômes classiques de malabsorption sont plus spécifiques. Des symptômes moins spécifiques, comme l'anémie ferriprive, augmentent aussi le risque."),
        fen("Fenêtre 1.1 — Entités voisines", [
            table(["Entité", "Différence lue"], [
                ["Allergie au blé", "Ce n'est pas le diagnostic dont parle l'ESPGHAN 2020. On ne la confond pas avec les anticorps anti-transglutaminase."],
                ["Régime sans gluten déjà commencé", "Il fausse la sérologie et l'histologie. Le test se fait sous gluten."],
                ["Petite taille familiale", "Le canal est stable et la cible explique la taille. Ici, une cassure ou un défaut de croissance font chercher la cœliaquie."],
            ]),
        ], es),
    ]))
    c.append(point(2, "Épidémiologie (Suisse, puis Europe)", [
        p("La prévalence suisse, l'incidence OFS et la mortalité de la maladie cœliaque : donnée non trouvée dans les sources consultées pour ce lot. On ne recopie pas un « 1 % » qui n'a pas été lu dans une source ouverte ici."),
        p("L'ESPGHAN souligne que la maladie est sous-diagnostiquée à cause de la variété des signes. L'enjeu est le rattrapage statural si on traite avant la soudure, et la mise au régime seulement après un diagnostic solide."),
        p("Histoire naturelle : sans éviction, l'auto-immunité et l'entéropathie persistent. Avec un régime compris par la famille, le diagnostic sans biopsie n'est acceptable que si les critères sont réunis."),
    ]))
    c.append(point(3, "Physiopathologie", [
        p("Le gluten entretient une réponse immunitaire contre la transglutaminase tissulaire chez un enfant prédisposé. La muqueuse duodénale se modifie (lésions de type Marsh). L'absorption des nutriments baisse, et la croissance, qui dépend des substrats, ralentit."),
        p("La cible du traitement est cette exposition au gluten. Le régime sans gluten retire le déclencheur. Il ne s'agit pas d'un immunosuppresseur dans les recommandations lues."),
        table(["Lésion", "Exploration", "Correction"], [
            ["Auto-immunité anti-transglutaminase", "IgA anti-transglutaminase avec IgA totales.", "Régime sans gluten après diagnostic selon l'algorithme."],
            ["Entéropathie", "Biopsies si le titre est sous 10 fois la limite, ou si l'IgA est basse.", "Même régime. La muqueuse est le témoin, pas une cible chirurgicale."],
            ["Défaut de croissance", "Courbe de taille et de poids.", "Le rattrapage suit la restauration de l'absorption, si les cartilages sont ouverts. Chiffre de rattrapage suisse : donnée non trouvée."],
        ]),
        fen("Fenêtre 3.1 — Pourquoi doser les IgA totales", [
            p("Si les IgA sont basses pour l'âge, ou inférieures à 0,2 g/L après 3 ans, l'ESPGHAN demande un test IgG (anti-transglutaminase, anti-endomysium ou peptides déamidés). Un test IgA seul serait faussement rassurant."),
            p("Tout enfant déficient en IgA et positif en IgG doit être biopsié. On n'applique pas l'algorithme sans biopsie."),
        ], es),
    ]))
    c.append(point(4, "Démarche diagnostique", [
        p("Devant une cassure staturale, on pense à la cœliaquie avant d'incriminer l'hormone de croissance. Les graves à ne pas manquer sont la dénutrition sévère, une autre malabsorption et, dans le SSP, la tumeur si un signe neurologique existe : ce n'est pas une cœliaquie."),
        table(["Hypothèse", "Examen qui tranche", "Piège"], [
            ["Maladie cœliaque", "IgA totales et IgA anti-transglutaminase sous gluten.", "Tester après un régime déjà exclu."],
            ["Déficit en IgA", "IgA totales basses puis test IgG.", "Croire une sérologie IgA négative."],
            ["Faux titre intermédiaire", "Biopsies : au moins quatre du duodénum distal et une du bulbe.", "Conclure sans biopsie sous 10 fois la limite."],
            ["Petite taille familiale", "Canal stable et cible.", "Bilan cœliaque inutile si rien ne quitte le cadre, et bilan obligatoire si la croissance cède."],
        ]),
    ]))
    c.append(point(5, "Anamnèse ciblée et drapeaux rouges", [
        p("On demande la diarrhée chronique, la perte de poids, le défaut de croissance, la constipation, l'anémie ferriprive et les défauts de l'émail, parce que l'ESPGHAN relie ces signes à un risque accru ou à un tableau classique. On demande si l'enfant mange du gluten. Les douleurs abdominales isolées ont une valeur insuffisante dans la guideline."),
        p("Drapeaux : cassure de poids puis de taille, dénutrition, famille déjà diagnostiquée qui a retiré le gluten avant le test."),
        fen("Fenêtre 5.1 — Questions", [
            table(["Question", "Raison", "Alerte"], [
                ["L'enfant mange-t-il du pain, des pâtes, des biscuits en ce moment ?", "Les anticorps et les biopsies exigent du gluten.", "Régime déjà commencé."],
                ["Le poids a-t-il décroché ?", "La malabsorption touche d'abord les substrats.", "Perte de poids ou défaut de croissance."],
                ["Y a-t-il une anémie ferriprive inexpliquée ?", "L'ESPGHAN cite ce signe parmi ceux qui augmentent le risque.", "Fer bas sans cause évidente."],
            ]),
        ], es),
    ]))
    c.append(point(6, "Examen physique ciblé, région par région", [
        p("Le normal est un abdomen souple, une courbe de poids concordante et un enfant qui grandit sur son canal. Le pathologique est un poids qui cède, parfois un ballonnement, une pâleur d'anémie, un ralentissement statural."),
        p(ital("6.1 Auxologie.") + " Taille et poids sur la courbe suisse, vitesse. " + ital("6.2 Abdomen.") + " Palpation, sans attendre un ventre spectaculaire : la forme extradigestive existe. " + ital("6.3 Bouche et peau.") + " Émail, pâleur. " + ital("6.4 Puberté.") + " Un retard pubertaire peut accompagner la maladie chronique ; il ne remplace pas la sérologie."),
    ]))
    c.append(point(7, "Approche syndromique", [
        p(ital("7.1 Malabsorption.") + " Signes fonctionnels : diarrhée chronique, douleurs, constipation, fatigue. Signes physiques : défaut de poids, petite taille, pâleur."),
        p(ital("7.2 Forme à prédominance staturale.") + " Signes fonctionnels pauvres. Signe physique : vitesse qui quitte le canal. L'ESPGHAN cite explicitement la petite taille et le défaut de croissance."),
        fen("Fenêtre 7.1 — Signes et gestes", [
            table(["Signe", "Recherche", "Mécanisme"], [
                ["Défaut de croissance", "Deux mesures et une vitesse.", "Substrats insuffisants pour le cartilage."],
                ["Pâleur", "Conjonctives et teint, puis hémogramme.", "Malabsorption du fer."],
                ["Ballonnement", "Inspection et palpation.", "Fermentation et atteinte muqueuse, inconstantes."],
            ]),
            p("Piège : exiger une diarrhée pour demander la sérologie. La recommandation inclut des formes sans ce symptôme classique."),
        ], es),
    ]))
    c.append(point(8, "Diagnostic positif et critères", [
        p("Société : ESPGHAN, guideline 2020 (Husby et collaborateurs). Sous gluten, on dose les IgA totales et les IgA anti-transglutaminase 2."),
        p("Sans biopsie, toutes les conditions lues doivent être réunies : IgA anti-transglutaminase au moins 10 fois la limite supérieure de la normale, avec un test dont la courbe de calibration couvre cette valeur ; anticorps anti-endomysium IgA positifs sur un second prélèvement ; accord de la famille qui comprend le diagnostic et s'engage dans le régime ; suivi par un gastroentérologue pédiatre ou un pédiatre expérimenté. Le HLA et les symptômes ne sont pas obligatoires. Le même algorithme vaut chez l'enfant asymptomatique."),
        p("Sous 10 fois la limite, on biopsie : au moins quatre fragments du duodénum distal et au moins un du bulbe. Un déficit en IgA avec test IgG positif impose aussi la biopsie. Ce qui ne suffit pas : un titre faiblement positif, un HLA DQ2 ou DQ8 isolé (il n'affirme pas la maladie ; leur absence rend la maladie très improbable), ou des symptômes seuls."),
        fen("Fenêtre 8.1 — Deux voies", [
            table(["Situation", "Décision ESPGHAN 2020"], [
                ["IgA normales, anti-transglutaminase ≥ 10×, anti-endomysium positif sur un second sérum, famille d'accord", "Diagnostic sans biopsie possible."],
                ["Anti-transglutaminase positif mais < 10×", "Biopsies."],
                ["IgA basses et test IgG positif", "Biopsies. Pas de voie sans biopsie."],
                ["HLA DQ2 et DQ8 absents", "Maladie très improbable. Un HLA présent ne confirme rien."],
            ]),
        ], es),
    ]))
    c.append(point(9, "Examens complémentaires", [
        p(ital("9.a Gold standard.") + " L'histologie duodénale reste la référence de performance diagnostique dans la méthode de la guideline. La voie sans biopsie est une exception encadrée, pas l'abandon de cette référence."),
        p(ital("9.b Première intention.") + " IgA totales et IgA anti-transglutaminase, enfant sous gluten. On n'utilise pas les peptides déamidés ni les anti-gliadine native en premier, car l'ESPGHAN les déconseille pour le dépistage initial."),
        p(ital("9.c Alternatives.") + " Test IgG si IgA basse. " + ital("9.d Deuxième intention.") + " Anti-endomysium sur un second prélèvement si on vise l'absence de biopsie. Biopsies sinon."),
        fen("Fenêtre 9.1 — Interprétation", [
            table(["Résultat", "Signification", "Conduite"], [
                ["IgA normales, anti-transglutaminase négatif, enfant sous gluten", "Cœliaquie peu probable sur ce test.", "Chercher une autre cause de la cassure. HLA seulement si le doute persiste : leur absence rassure fortement."],
                ["≥ 10× et anti-endomysium positif", "Valeur prédictive élevée si le test est approprié.", "Discuter l'absence de biopsie avec la famille."],
                ["Positif < 10×", "Ne suffit pas.", "Adresser pour biopsies."],
                ["Histologie Marsh 0 ou I mais auto-immunité confirmée", "L'ESPGHAN demande un suivi rapproché.", "Ne pas banaliser. Ne pas inventer un traitement hors régime discuté par le spécialiste."],
            ]),
            p("Enfant, grossesse d'une adolescente, insuffisance rénale : la sérologie ne change pas de principe dans les sources lues. Donnée non trouvée pour un seuil différent si DFGe < 30 mL/min."),
        ], es),
    ]))
    c.append(point(10, "Arbre décisionnel", [
        p("Cassure ou symptôme évocateur : vérifier le gluten alimentaire, doser IgA et anti-transglutaminase. Titre très élevé : second prélèvement pour l'anti-endomysium et discussion sans biopsie. Titre moindre ou IgA basse : biopsies. Diagnostic posé : régime sans gluten et suivi spécialisé. Diagnostic non posé : ne pas démarrer le régime « pour voir »."),
    ]))
    c.append(point(11, "Prise en charge selon les recommandations suisses", [
        p(ital("A- But.") + " Obtenir un diagnostic certain, puis retirer le gluten pour faire régresser l'auto-immunité et permettre la croissance. Aucun chiffre de taille cible n'est fixé par l'ESPGHAN dans les passages lus."),
        p(ital("B- Moyens.") + " Le moyen est le régime sans gluten, expliqué, tenu, et compris avant de renoncer à la biopsie. Il n'y a pas de médicament de première ligne dans la guideline lue. Dose AIPS : sans objet. Diététicienne, étiquetage, école : le volet nutritionnel est le traitement. Donnée non trouvée pour une liste suisse d'aliments remboursés dans les sources ouvertes."),
        p("Forme compliquée (dénutrition) : on corrige l'hydratation et les carences en parallèle du diagnostic, sans attendre la biopsie pour nourrir l'enfant. Minute par minute : sans objet hors choc, qui n'est pas le tableau habituel. Heure 0 : constantes, poids, ne pas interdire le gluten avant les prélèvements si l'enfant va bien."),
        p("Situations spéciales. Adolescente enceinte : le régime se poursuit ; le détail obstétrical suisse n'a pas été lu. Sujet âgé : hors âge pédiatrique de cette guideline. Enfant : c'est la population de l'ESPGHAN. Foie et rein : donnée non trouvée pour une adaptation du régime."),
        p(ital("C- Surveillance.") + " Suivi par un praticien expérimenté. Décroissance des anticorps et reprise de la courbe. Seuil d'arrêt du régime : il n'y en a pas dans les passages lus. On ne « essaie » pas une réintroduction hors protocole spécialisé."),
        p("Retour à domicile : immédiat si l'enfant n'est pas dénutri au point d'exiger une renutrition surveillée. Critères : boit, mange le régime expliqué, pas de déshydratation, parents capables du régime."),
        p(ital("D- Pronostic.") + " La muqueuse et les symptômes répondent au régime quand le diagnostic est juste. La taille finale dépend du moment du traitement par rapport à la soudure : donnée chiffrée suisse non trouvée. Recherche 2026 : la guideline citée est celle de 2020 ; une version plus récente n'a pas été identifiée dans les sources ouvertes."),
    ]))
    c.append(point(12, "Prévention", [
        p("Primaire : pas de dépistage universel chiffré suisse dans les sources ouvertes. Secondaire : chercher la maladie devant une cassure, une anémie ferriprive, une diarrhée chronique. Tertiaire : maintien du régime pour éviter la rechute muqueuse et les carences."),
    ]))
    c.append(point(13, "Points clés", [
        p("Vous dosez les IgA totales avec les IgA anti-transglutaminase."),
        p("Vous ne concluez sans biopsie qu'au-delà de 10 fois la limite, avec anti-endomysium positif sur un second sérum et l'accord de la famille."),
        p("Vous biopsiez au moins quatre fragments distaux et un bulbe sinon."),
        p("Vous laissez le gluten en place jusqu'aux tests."),
        p("Vous ne traitez pas la petite taille par l'hormone de croissance avant d'avoir écarté cette cause."),
    ]))
    c.append(point(14, "Pièges et questions fréquentes à l'examen fédéral suisse", [
        p("Piège : sérologie IgA seule. Bonne réponse : IgA totales en même temps."),
        p("Piège : régime d'épreuve avant les tests. Bonne réponse : gluten maintenu."),
        p("Piège : HLA positif égal diagnostic. Bonne réponse : le HLA négatif écarte presque, le HLA positif n'affirme pas."),
        fen("Fenêtre 14.1 — Question type", [
            p("Enfant avec cassure staturale, IgA normales, anti-transglutaminase à 4 fois la limite. Que faites-vous ?"),
            p("Vous adressez pour biopsies duodénales sous gluten. Vous ne démarrez pas le régime sans gluten comme preuve. Vous ne demandez pas l'hormone de croissance à cette étape."),
        ], es),
    ]))
    return mono("DX.7", "Maladie cœliaque",
                "Rang du projet — prévalence suisse non quantifiée dans les sources ouvertes ; manifestation staturale reconnue par l'ESPGHAN 2020 [S307]",
                "".join(c))


def dx8():
    ped = "[S401]"
    c = []
    c.append(point(1, "Définition et sémantique", [
        p("L'" + inline("hypothyroïdie acquise", [
            "Pedlaus la sépare du nouveau-né dépisté. Elle apparaît chez l'enfant déjà né, le plus souvent par une thyroïdite auto-immune de Hashimoto.",
            "Biologiquement, la forme primaire associe une thyroxine libre basse et une TSH élevée. La forme centrale associe une thyroxine libre basse et une TSH basse ou non élevée.",
            "Piège : appeler hypothyroïdie une prise de poids avec croissance accélérée, tableau de l'obésité nutritionnelle et non de ce DX.",
        ], ped) + " ralentit la croissance des os longs et fait prendre du poids."),
        p("La puberté est souvent retardée, mais elle peut aussi être avancée. Les deux existent dans la fiche lausannoise : on ne retient donc pas un seul sens."),
    ]))
    c.append(point(2, "Épidémiologie (Suisse, puis Europe)", [
        p("Pedlaus écrit que 1 enfant d'âge scolaire sur 500 peut présenter une hypothyroïdie acquise. La fiche ne détaille pas le dénominateur cantonal ni la mortalité."),
        p("La cause la plus fréquente y est la thyroïdite de Hashimoto. Les causes rares listées sont le kyste du tractus thyréoglosse, une hémithyroïde, l'excès d'iode, le lithium, l'amiodarone, le radioiode, et un hémangiome hépatique qui active la désiodase de type 3."),
        p("Histoire naturelle non traitée : baisse durable de la qualité de vie, retard de croissance et de développement, réflexes et force diminués, mémoire touchée. L'enjeu est le rattrapage si l'on substitue avant la soudure, sans chiffre suisse de taille finale dans la fiche."),
    ]))
    c.append(point(3, "Physiopathologie", [
        p("La thyroxine manque au cartilage et au cerveau. La croissance des os longs diminue, le rapport du segment supérieur au segment inférieur peut diminuer, les cheveux deviennent secs et cassants. La TSH s'élève si la thyroïde est en cause, parce que l'hypophyse cherche à la stimuler."),
        p("La cible du traitement est cette carence hormonale. La lévothyroxine la remplace. Elle ne guérit pas la thyroïdite auto-immune, ce que Pedlaus écrit explicitement."),
        table(["Lésion", "Exploration", "Correction"], [
            ["Thyroïde détruite ou infiltrée", "TSH haute, thyroxine libre basse, anticorps anti-TPO et anti-thyroglobuline, échographie.", "Lévothyroxine. Dose AIPS non lue."],
            ["Cartilage ralenti", "Vitesse de croissance et âge osseux.", "La substitution lève le frein. Elle ne réouvre pas un cartilage soudé."],
            ["Axe central en panne", "Thyroxine libre basse et TSH non élevée.", "IRM hypothalamo-hypophysaire et recherche des autres déficits. La TSH seule serait faussement rassurante."],
        ]),
        fen("Fenêtre 3.1 — Deux biologies", [
            p("Primaire : la glande ne produit plus. La TSH monte. Centrale : l'hypophyse ou l'hypothalamus ne demande plus. La TSH ne monte pas. Le geste qui suit change : échographie d'un côté, IRM de l'autre."),
        ], ped),
    ]))
    c.append(point(4, "Démarche diagnostique", [
        p("On confirme la biologie avant d'attribuer la taille à la famille. On ne manque pas une forme centrale ni une puberté précoce paradoxale."),
        table(["Hypothèse", "Examen", "Piège"], [
            ["Hashimoto", "Anticorps et échographie si hypothyroïdie ou goitre.", "Traiter sans avoir vu la TSH et la thyroxine libre."],
            ["Cause médicamenteuse", "Lithium, amiodarone, iode, radioiode dans l'anamnèse.", "Oublier l'ordonnance."],
            ["Forme centrale", "TSH non élevée malgré thyroxine libre basse, puis IRM.", "Se fier à une TSH normale isolée."],
            ["Obésité simple", "La croissance s'accélère au lieu de s'arrêter. Ce contraste est clinique ; la fiche décrit ici le retard de croissance avec prise de poids.", "Donner de la lévothyroxine à un enfant obèse euthyroïdien."],
        ]),
    ]))
    c.append(point(5, "Anamnèse ciblée et drapeaux rouges", [
        p("On cherche la frilosité, la constipation, la baisse d'attention en classe, la prise de poids, le goitre, les antécédents auto-immuns et les médicaments."),
        p("Drapeaux : arrêt de la croissance avec prise de poids, goitre compressif, signes centraux (céphalées, trouble visuel) qui imposeraient l'IRM, adolescente enceinte non traitée à cause du risque neuro-développemental fœtal écrit par Pedlaus."),
    ]))
    c.append(point(6, "Examen physique ciblé, région par région", [
        p("Le normal est une thyroïde impalpable ou souple, une vitesse conservée, une peau et des cheveux ordinaires, des réflexes vifs."),
        p(ital("6.1 Cou.") + " Inspection et palpation du goitre, recherche de nodules. " + ital("6.2 Peau et cheveux.") + " Sècheresse, cheveux cassants. " + ital("6.3 Auxologie.") + " Taille ralentie et poids en hausse. " + ital("6.4 Neurologie.") + " Réflexes lents. " + ital("6.5 Puberté.") + " Retard fréquent, avance possible."),
        fen("Fenêtre 6.1 — Technique du goitre", [
            p("On demande à l'enfant d'avaler pendant que les doigts suivent la glande. Une thyroïde qui ne monte pas à la déglutition n'est pas dans la loge habituelle. L'échographie précisée par Pedlaus vient ensuite si la biologie est primaire."),
        ], ped),
    ]))
    c.append(point(7, "Approche syndromique", [
        p(ital("7.1 Hypométabolisme.") + " Signes fonctionnels : frilosité, constipation, baisse d'attention, fatigue. Signes physiques : poids haut, taille lente, peau sèche, réflexes lents, goitre possible."),
        p(ital("7.2 Retentissement statural.") + " Signe fonctionnel pauvre au début. Signe physique : vitesse basse et âge osseux retardé. Mécanisme : manque de thyroxine sur le cartilage."),
        fen("Fenêtre 7.1 — Définir chaque signe", [
            table(["Signe", "Recherche", "Mécanisme"], [
                ["Goitre", "Palpation à la déglutition.", "Infiltration lymphocytaire de Hashimoto ou autre lésion de la loge."],
                ["Prise de poids avec taille lente", "Courbe des deux paramètres.", "Métabolisme ralenti et cartilage freiné. L'obésité simple accélère plutôt la taille."],
                ["Cheveux secs", "Inspection et traction douce.", "Renouvellement pilaire ralenti par le manque d'hormone."],
            ]),
        ], ped),
    ]))
    c.append(point(8, "Diagnostic positif et critères", [
        p("La fiche lausannoise pose le diagnostic sur la TSH et la thyroxine libre. Primaire : thyroxine libre abaissée et TSH élevée. Centrale : les deux abaissées, ou TSH inappropriée. Les anticorps anti-TPO et anti-thyroglobuline soutiennent la thyroïdite si on les demande devant cette suspicion."),
        p("Ce qui ne suffit pas : un goitre isolé, une fatigue, ou une TSH légèrement hors norme sans contrôle. La fiche dit que, dans certains cas de Hashimoto, l'observation seule suffit et que le traitement n'est pas toujours nécessaire. Le seuil chiffré suisse exact de cette observation : donnée non trouvée au-delà de cette phrase."),
        fen("Fenêtre 8.1 — Critères opératoires lus", [
            table(["Biologie", "Lecture Pedlaus", "Geste suivant"], [
                ["Thyroxine libre basse, TSH haute", "Hypothyroïdie primaire.", "Échographie cervicale. Traitement substitutif."],
                ["Thyroxine libre basse, TSH basse", "Hypothyroïdie centrale.", "IRM et autres axes."],
                ["Hashimoto avec hypothyroïdie ou goitre", "Indication de traiter selon la fiche.", "Lévothyroxine, dose AIPS à lire ailleurs."],
                ["Situation où la fiche permet l'observation", "Pas d'hypothyroïdie franche à traiter.", "Surveillance clinique, sans inventer un seuil."],
            ]),
        ], ped),
    ]))
    c.append(point(9, "Examens complémentaires", [
        p(ital("9.a Gold standard.") + " Il est biologique : TSH et thyroxine libre. L'échographie ne pose pas le diagnostic fonctionnel."),
        p(ital("9.b Première intention.") + " TSH et thyroxine libre. Anticorps si thyroïdite suspectée. La T3 libre et la TBG sont très rarement nécessaires."),
        p(ital("9.c.") + " Échographie si forme primaire. " + ital("9.d.") + " IRM si forme centrale. Âge osseux pour le retentissement statural, pas pour poser le diagnostic hormonal."),
        fen("Fenêtre 9.1 — Interprétation", [
            table(["Résultat", "Signification", "Conduite"], [
                ["TSH haute, thyroxine libre basse", "Primaire patente.", "Substituer et chercher la cause."],
                ["TSH haute, thyroxine libre normale", "Zone que la fiche ne chiffre pas. Observation possible dans certains Hashimoto.", "Ne pas inventer un seuil. Recontrôler et lire une recommandation spécialisée."],
                ["Les deux basses", "Centrale jusqu'à preuve du contraire.", "IRM, ne pas rassurer."],
                ["Surdosage", "Hyperthyroïdie iatrogène, complication écrite par Pedlaus.", "Réduire après lecture de l'AIPS, surveiller."],
            ]),
        ], ped),
    ]))
    c.append(point(10, "Arbre décisionnel", [
        p("Courbe ralentie avec prise de poids : doser TSH et thyroxine libre. Primaire : anticorps, échographie, substitution si la fiche l'indique. Centrale : IRM le jour où le tableau est confirmé, sans attendre un goitre qui n'existera pas. Euthyroïdie : quitter ce DX."),
    ]))
    c.append(point(11, "Prise en charge selon les recommandations suisses", [
        p(ital("A- But.") + " Normaliser la TSH et la thyroxine libre et corriger les signes, selon Pedlaus. La maladie auto-immune, elle, n'est pas guérie."),
        p(ital("B- Moyens.") + " Lévothyroxine par voie orale. Pedlaus est une fiche d'enseignement et non une information professionnelle Swissmedic. La dose chiffrée, la spécialité ®, le numéro d'autorisation, les adaptations rénale et hépatique et les interactions : donnée non trouvée dans les sources consultées, parce qu'aucune AIPS n'a été ouverte. On n'écrit donc pas de microgrammes par kilogramme."),
        p("Classe : hormones thyroïdiennes. La fiche ne liste pas les autres principes actifs ni la pharmacocinétique. Effet indésirable à dire : le surdosage crée une hyperthyroïdie. Contre-indications AIPS : non lues."),
        p("Moyens non médicamenteux : expliquer que le traitement compense et ne guérit pas. Pas de régime iode « miracle » dans la fiche. Le lithium et l'amiodarone se discutent avec le prescripteur de ces molécules."),
        p("Volet social : scolarité à protéger pendant la phase symptomatique, car l'attention baisse. Arrêt de travail des parents : donnée non trouvée."),
        p("Situations spéciales. Femme enceinte non traitée : conséquence néfaste sur le développement neuronal fœtal, phrase lue. On traite. Allaitement et dose : non lus dans l'AIPS. Sujet âgé : hors fiche pédiatrique. Enfant : population cible. Foie et rein : donnée non trouvée pour un palier de DFGe."),
        p(ital("C- Surveillance.") + " TSH et thyroxine libre jusqu'à la cible de la fiche, puis suivi clinique de la croissance. Calendrier en semaines : donnée non trouvée dans Pedlaus. Surdosage : signes d'hyperthyroïdie, on adapte sans chiffre inventé."),
        p("Retour à domicile : le jour de la consultation si l'enfant boit et n'a pas de complication aiguë. Il n'y a pas de critère hospitalier spécifique dans la fiche."),
        p(ital("D- Pronostic.") + " Les signes se corrigent si la biologie se normalise. La taille rattrape d'autant mieux que le cartilage est ouvert : durée et gain en centimètres non chiffrés ici. Recherche 2026 : non identifiée dans la fiche."),
        fen("Fenêtre 11.1 — Ordre des gestes", [
            p("Jour 0 : courbe, palpation, TSH et thyroxine libre. Dès le résultat primaire : expliquer la substitution et adresser si le prescripteur n'a pas l'AIPS sous les yeux. Dès le résultat central : IRM, ne pas donner une consigne de dose improvisée. Semaines suivantes : contrôler la biologie selon le spécialiste, suivre la vitesse."),
        ], ped),
    ]))
    c.append(point(12, "Prévention", [
        p("Primaire : pas de vaccin. Éviter les expositions iode ou médicaments inutiles n'est pas un programme chiffré ici. Secondaire : doser devant la cassure avec prise de poids, le goitre, la frilosité. Tertiaire : substitution pour limiter le retard statural et, chez l'adolescente enceinte, le risque fœtal."),
    ]))
    c.append(point(13, "Points clés", [
        p("Vous dosez la TSH et la thyroxine libre, pas la TSH seule."),
        p("Vous échographiez la forme primaire et vous IRM la forme centrale."),
        p("Vous traitez une hypothyroïdie par lévothyroxine, et vous lisez l'AIPS avant d'écrire la dose."),
        p("Vous dites que Hashimoto ne guérit pas sous hormone."),
        p("Vous n'appelez pas obésité simple un enfant qui grossit et qui ne grandit plus."),
    ]))
    c.append(point(14, "Pièges et questions fréquentes à l'examen fédéral suisse", [
        p("Piège : TSH normale et thyroxine libre non dosée devant un tableau central. Bonne réponse : doser les deux."),
        p("Piège : dose de mémoire en µg/kg. Bonne réponse : AIPS non lue, dose non écrite."),
        p("Piège : puberté toujours retardée. Bonne réponse : Pedlaus décrit aussi une puberté avancée possible."),
        fen("Fenêtre 14.1 — Question type", [
            p("Fille de 10 ans, vitesse en baisse, poids en hausse, TSH à peine dosée « un peu haute » sans thyroxine libre. Que manque-t-il ?"),
            p("La thyroxine libre, l'examen du cou, et la décision de traiter seulement si la biologie confirme. Vous ne concluez pas sur un adjectif."),
        ], ped),
    ]))
    return mono("DX.8", "Hypothyroïdie acquise",
                "1 enfant d'âge scolaire sur 500 peut en présenter une, selon la fiche lausannoise [S401] ; incidence OFS non lue",
                "".join(c))


def dx9():
    co = "[S402]"
    mech = "[S403]"
    c = []
    c.append(point(1, "Définition et sémantique", [
        p("L'" + inline("hypercorticisme iatrogène", [
            "Dans ce DX, il désigne le freinage de la croissance par des glucocorticoïdes donnés comme traitement, surtout inhalés dans l'asthme persistant, et non un adénome hypophysaire.",
            "La revue Cochrane montre qu'une corticothérapie inhalée régulière à dose faible ou moyenne réduit la vitesse de croissance. Le mécanisme passe par l'axe de l'hormone de croissance lorsque le produit passe dans le sang.",
            "Piège : arrêter l'asthme pour « sauver » la taille. Le contrôle respiratoire reste indiqué. On cherche la plus faible exposition efficace.",
        ], co) + " se voit sur la courbe avant de se voir sur le visage."),
        p("Les sources ouvertes de ce lot quantifient surtout la voie inhalée. Le seuil suisse d'une corticothérapie orale qui arrête la croissance : donnée non trouvée dans les sources consultées."),
    ]))
    c.append(point(2, "Épidémiologie (Suisse, puis Europe)", [
        p("La revue Cochrane (recherche jusqu'en janvier 2014, synthèse reprise par la revue sur les dispositifs) trouve une réduction moyenne de 0,48 cm par an de la vitesse de croissance pendant la première année, chez l'enfant prépubère asthmatique léger à modéré, avec une certitude modérée. L'effet est moins marqué les années suivantes."),
        p("La même synthèse indique que la baisse initiale de taille peut persister à l'âge adulte, sans être progressive ni cumulative, et que l'effet paraît dépendant de la dose (certitude modérée). La molécule et le dispositif peuvent modifier l'ampleur (certitude très faible à modérée)."),
        p("Fréquence suisse des arrêts de croissance sous corticoïde, mortalité : donnée non trouvée. L'enjeu est d'utiliser la dose efficace la plus basse et de mesurer l'enfant, pas d'interdire la classe."),
    ]))
    c.append(point(3, "Physiopathologie", [
        p("Le texte Cochrane lu explique que le corticoïde inhalé absorbé interrompt l'axe somatotrope. Au centre, il diminue la sécrétion pulsatile d'hormone de croissance. En périphérie, il réduit l'expression du récepteur au cartilage et au foie, et il réduit la production et l'activité de l'IGF-1. La prolifération des chondrocytes baisse et leur apoptose augmente. L'os long grandit donc plus lentement."),
        p("La cible de correction est l'exposition systémique : moins de produit absorbé, pas un médicament anti-IGF. On ne compense pas d'emblée par une hormone de croissance, conduite non lue dans ces revues."),
        table(["Lésion", "Exploration", "Correction"], [
            ["Pulsatilité de GH diminuée", "La vitesse de croissance, pas un dosage de GH de routine.", "Baisser l'exposition, changer de molécule si le contrôle le permet."],
            ["IGF-1 moins actif", "IGF-1 possible dans un bilan de petite taille, sans en faire le gold standard de cet effet indésirable.", "Même levier : la dose et la molécule."],
            ["Cartilage ralenti", "Courbe en cm par an.", "L'effet est maximal la première année, puis moindre."],
        ]),
        fen("Fenêtre 3.1 — Chiffre et limite", [
            p("0,48 cm par an est une moyenne de vitesse en moins la première année, pas la perte de chaque enfant. L'intervalle individuel n'est pas dans la phrase citée. On ne dit pas à une famille que leur enfant perdra exactement 0,48 cm."),
            p("La puissance du produit inhalé explique qu'une petite fraction absorbée suffise. Le texte rappelle des puissances très supérieures à la dexaméthasone, citation interne à la revue. On n'en déduit pas une dose suisse."),
        ], mech),
    ]))
    c.append(point(4, "Démarche diagnostique", [
        p("On relit l'ordonnance avant de chercher un Cushing endogène. Les graves à ne pas manquer sont l'asthme mal contrôlé si l'on arrête le traitement, et une autre cause de cassure (cœliaquie, hypothyroïdie, tumeur) qui coexiste."),
        table(["Hypothèse", "Ce qui tranche", "Piège"], [
            ["Freinage par corticoïde inhalé", "Exposition régulière et ralentissement contemporain, surtout la première année.", "Oublier les inhalés « parce qu'ils sont locaux »."],
            ["Cushing endogène", "Signes cliniques francs et bilan hormonal. Le protocole suisse de freinage : donnée non trouvée dans les sources ouvertes de ce DX.", "Attribuer au spray un tableau cushingoïde lourd sans le vérifier."],
            ["Autre maladie de croissance", "La courbe cassait avant le médicament, ou des drapeaux existent.", "Tout mettre sur le spray."],
        ]),
    ]))
    c.append(point(5, "Anamnèse ciblée et drapeaux rouges", [
        p("On liste chaque corticoïde : inhalé, nasal, oral, cutané puissant, et la durée. On demande qui administre et si une chambre d'inhalation est utilisée, car le dispositif peut changer l'exposition, avec une certitude limitée."),
        p("Drapeaux : arrêt presque complet de la vitesse, prise de poids rapide, vergetures, hypertension, ou signes qui ne collent pas à un simple spray à faible dose."),
    ]))
    c.append(point(6, "Examen physique ciblé, région par région", [
        p("Le normal sous petit dose bien prise est un enfant dont la vitesse baisse peu et dont l'asthme est contrôlé. Le pathologique est une vitesse en retrait, parfois un faciès et un tronc qui prennent du poids."),
        p(ital("6.1 Auxologie.") + " Mesure rapprochée la première année d'exposition. " + ital("6.2 Peau.") + " Vergetures, fragilité. " + ital("6.3 Tension.") + " Mesure au brassard adapté. " + ital("6.4 Respiration.") + " Contrôle de l'asthme, pour ne pas juger le médicament sans la maladie."),
    ]))
    c.append(point(7, "Approche syndromique", [
        p(ital("7.1 Freinage statural isolé.") + " Signe fonctionnel : aucun, ou la plainte de taille. Signe physique : vitesse moindre d'environ un demi-centimètre par an en moyenne la première année dans les essais. Mécanisme : axe GH–IGF-1."),
        p(ital("7.2 Tableau cushingoïde.") + " Signes fonctionnels : fatigue, soif si le métabolisme se complique. Signes physiques : prise de poids tronculaire, vergetures, tension haute. Ce tableau dépasse le simple effet moyen des essais sur l'asthme léger et impose un avis spécialisé. Seuils tensionnels suisses de l'enfant : donnée non trouvée dans les sources ouvertes."),
    ]))
    c.append(point(8, "Diagnostic positif et critères", [
        p("Il n'y a pas de score. Le diagnostic d'effet indésirable repose sur une exposition temporelle et une vitesse qui ralentit, après avoir écarté une autre cause. La revue ne donne pas un seuil de vitesse qui « prouve » le lien chez un enfant donné."),
        p("Ce qui ne suffit pas : le fait d'avoir un spray, sans mesure de vitesse."),
    ]))
    c.append(point(9, "Examens complémentaires", [
        p(ital("9.a Gold standard.") + " Pour l'effet sur la croissance, c'est la mesure répétée de la taille, pas un dosage. Pour un Cushing endogène, le test de référence suisse n'a pas été lu."),
        p(ital("9.b.") + " Courbe et vitesse. " + ital("9.c.") + " TSH et sérologie cœliaque si la cassure est douteuse. " + ital("9.d.") + " Avis endocrinien et bilan de Cushing si le tableau clinique dépasse l'effet attendu d'une faible dose inhalée. Cortisol libre urinaire, salivaire nocturne, freinage : donnée non trouvée comme protocole suisse dans les fichiers lus."),
        fen("Fenêtre 9.1 — Lecture de la vitesse", [
            table(["Constat", "Lecture", "Conduite"], [
                ["Environ un demi-centimètre par an en moins, première année, asthme léger à modéré", "Effet moyen des essais, pas un destin individuel.", "Revoir la dose et la molécule. Ne pas arrêter net si l'asthme le nécessite."],
                ["Ralentissement majeur ou signes cushingoïdes", "Dépasse cet effet moyen.", "Chercher une autre cause et revoir l'exposition systémique."],
                ["Vitesse normale", "N'exclut pas un petit effet, mais ne justifie pas un bilan agressif.", "Poursuivre la mesure annuelle."],
            ]),
        ], co),
    ]))
    c.append(point(10, "Arbre décisionnel", [
        p("Enfant sous corticoïde dont la courbe fléchit : quantifier la vitesse, relire toutes les voies d'administration, écarter cœliaquie et hypothyroïdie si le doute persiste, puis réduire l'exposition au minimum efficace avec le prescripteur de l'asthme. Signes cushingoïdes : ne pas rester sur le seul spray, adresser."),
    ]))
    c.append(point(11, "Prise en charge selon les recommandations suisses", [
        p(ital("A- But.") + " Garder le contrôle de la maladie qui justifie le corticoïde et limiter la perte de vitesse. Le but n'est pas une taille au 50e percentile."),
        p(ital("B- Moyens.") + " Plus faible dose efficace, choix de molécule et de dispositif discuté avec le pneumologue, technique d'inhalation. Aucune spécialité n'est préférée ici, parce que l'AIPS n'a pas été lue et que la revue ne désigne pas un produit suisse. On n'écrit pas de microgrammes à prescrire."),
        p("La revue suggère que la fluticasone freine moins que la béclométasone ou le budésonide à dose équivalente dans certains essais, avec une certitude inégale. Ce n'est pas une consigne de changement automatique."),
        p("Situations spéciales : enfant, c'est la population des essais (jusqu'à 18 ans dans les critères). Grossesse de l'adolescente asthmatique : on ne stoppe pas un traitement indispensable sans avis, donnée précise non lue. Rein et foie : non lus. Sujet âgé : sans objet."),
        p(ital("C- Surveillance.") + " Taille au moins la première année, période où l'effet est maximal, puis suivi parce que l'effet diminue mais que la taille adulte peut garder une partie du déficit initial."),
        p("Pas d'hospitalisation pour ce seul effet. Retour à domicile le jour même si l'asthme est stable."),
        p(ital("D- Pronostic.") + " La réduction de taille adulte n'est ni progressive ni cumulative dans la synthèse lue. Elle peut persister. Il n'y a pas de « guérison » autre que la croissance reprise quand l'exposition baisse et que le cartilage est ouvert."),
        fen("Fenêtre 11.1 — Ordre", [
            p("Jour 0 : mesurer, lister les corticoïdes, ne pas arrêter un traitement vital dans le couloir. Semaine 1 : technique d'inhalation et dose minimale efficace avec le prescripteur. Mois 3 à 12 : vitesse. Si la vitesse s'effondre, ouvrir un autre DX du SSP."),
        ], co),
    ]))
    c.append(point(12, "Prévention", [
        p("Primaire : ne pas commencer une corticothérapie inhalée sans asthme persistant qui la justifie, conformément au rôle de première ligne rappelé par la revue pour l'asthme persistant. Secondaire : mesurer dès la première année. Tertiaire : baisser la dose quand le contrôle le permet, pour ne pas cumuler une exposition inutile."),
    ]))
    c.append(point(13, "Points clés", [
        p("Vous demandez les corticoïdes inhalés, nasaux, oraux et cutanés."),
        p("Vous retenez 0,48 cm par an en moyenne la première année, pas comme perte garantie."),
        p("Vous savez que l'effet passe par l'axe GH–IGF-1 et les chondrocytes."),
        p("Vous ne stoppez pas l'asthme pour un demi-centimètre."),
        p("Vous n'inventez pas la dose AIPS du produit de remplacement."),
    ]))
    c.append(point(14, "Pièges et questions fréquentes à l'examen fédéral suisse", [
        p("Piège : « les inhalés n'ont pas d'effet systémique ». Bonne réponse : la revue montre un ralentissement moyen."),
        p("Piège : Cushing biologique systématique devant tout spray. Bonne réponse : la courbe d'abord, le bilan endocrinien si le tableau dépasse l'effet attendu."),
        p("Piège : promettre que la taille adulte est intacte. Bonne réponse : une partie du déficit initial peut persister, sans s'aggraver indéfiniment."),
    ]))
    return mono("DX.9", "Hypercorticisme, le plus souvent iatrogène",
                "Rang du projet — fréquence suisse non quantifiée ; ralentissement moyen 0,48 cm/an la première année sous corticoïde inhalé [S402]",
                "".join(c))


def dx10():
    seep = "[S404]"
    espe = "[S306]"
    c = []
    c.append(point(1, "Définition et sémantique", [
        p("La " + inline("thélarche prématurée", [
            "La société espagnole d'endocrinologie pédiatrique classe la thélarche précoce isolée parmi les variantes incomplètes du développement, avec la pubarche précoce isolée.",
            "Ces signes peuvent rester stables, régresser, puis laisser place à une puberté normale, ou progresser vers une puberté précoce vraie.",
            "La puberté précoce, dans le même texte, est l'apparition des caractères sexuels secondaires avant 8 ans chez la fille et avant 9 ans chez le garçon, pour une population caucasienne de pays développés.",
        ], seep) + " et la pubarche prématurée ne sont pas, à elles seules, une puberté précoce centrale."),
        p("La ménarche précoce isolée est une entité rare du même chapitre : saignements cycliques entre 1 et 9 ans sans autres signes pubertaires. On l'écarte des causes de saignement (infection, corps étranger, tumeur), du syndrome de McCune-Albright, des œstrogènes exogènes et de l'hypothyroïdie."),
    ]))
    c.append(point(2, "Épidémiologie (Suisse, puis Europe)", [
        p("La société espagnole estime l'incidence de la puberté précoce entre 1/5 000 et 1/10 000, avec un rapport filles/garçons de 20:1. Ce chiffre concerne la puberté précoce, pas la thélarche isolée."),
        p("Chez la fille, 98 % des pubertés précoces seraient centrales dans ce texte, et une étude multicentrique italienne y est citée avec 74 % de formes idiopathiques. Chez le garçon, la part neurogène varie de 94 % à 40 % selon les auteurs du chapitre. La fréquence suisse de la thélarche ou de la pubarche isolée : donnée non trouvée."),
        p("Histoire naturelle de la variante isolée : stabilité ou régression possibles, puberté ultérieure à un âge normal, ou progression. L'enjeu est de ne pas traiter par analogue une forme qui ne progresse pas, et de ne pas manquer une forme qui progresse."),
    ]))
    c.append(point(3, "Physiopathologie", [
        p("La puberté précoce centrale vient d'une activation prématurée de la GnRH. La forme périphérique vient d'une sécrétion autonome de stéroïdes. La forme combinée apparaît quand un stimulus périphérique réveille ensuite l'axe."),
        p("La thélarche isolée et la pubarche isolée ne montrent pas cette activation complète. Le sein isolé peut relever d'une sensibilité tissulaire ; la pilosité isolée relève de l'adrénarche. Le chapitre renvoie le détail au chapitre 10, qui n'a pas été ouvert : donnée non trouvée pour le mécanisme cellulaire fin."),
        table(["Perturbation", "Exploration", "Correction"], [
            ["Sein isolé sans activation de l'axe", "Vitesse normale, âge osseux non avancé, pas d'autre signe.", "Surveillance. Pas d'analogue de GnRH."],
            ["Activation centrale prématurée", "Progression, vitesse accélérée, test à la GnRH, imagerie selon le contexte.", "Traiter la cause et discuter l'analogue. Dose AIPS non lue."],
            ["Stéroïde périphérique autonome", "Virilisation, âge osseux très avancé.", "Ce n'est plus ce DX. Chercher la surrénale ou la gonade."],
        ]),
    ]))
    c.append(point(4, "Démarche diagnostique", [
        p("On écarte d'abord la puberté précoce évolutive, la tumeur et l'hyperandrogénie, puis on surveille la variante."),
        table(["Hypothèse grave", "Ce qui tranche", "Piège"], [
            ["Puberté précoce centrale du garçon", "Le chapitre dit que le garçon a souvent une cause neurogène. L'imagerie cérébrale se discute largement.", "Rassurer un garçon comme on rassure une fille de 7 ans."],
            ["Cause neurogène chez la petite fille", "Le texte indique une part neurogène plus haute avant 4 ans, et recommande quand même d'étudier le système nerveux central chez des filles de plus de 7 ans si l'on craint une lésion.", "Croire qu'après 7 ans toute fille est idiopathique."],
            ["McCune-Albright ou saignement organique", "Taches café-au-lait à bords déchiquetés, saignement, échographie.", "Appeler thélarche un saignement."],
            ["Hyperplasie ou tumeur surrénalienne", "Virilisation rapide et âge osseux avancé. Ce n'est pas une pubarche isolée stable.", "Confondre pilosité isolée et virilisation."],
        ]),
    ]))
    c.append(point(5, "Anamnèse ciblée et drapeaux rouges", [
        p("On date le premier bourgeon ou le premier poil, on cherche les crèmes œstrogéniques, l'évolution sur les semaines, les céphalées, et les règles de la mère. Le chapitre ne trouve une ménarche maternelle précoce que dans 4 % d'une série citée de formes centrales idiopathiques : l'histoire familiale ne protège pas."),
        p("Drapeaux : progression vers d'autres caractères, accélération staturale, âge osseux qui avance, virilisation, saignement, signes neurologiques, fille très jeune."),
    ]))
    c.append(point(6, "Examen physique ciblé, région par région", [
        p("Le normal d'une thélarche isolée est un bourgeon mammaire palpable, sans pilosité, sans accélération de vitesse, sans tache cutanée évocatrice."),
        p(ital("6.1 Seins.") + " Palpation, pour distinguer glande et graisse. " + ital("6.2 Pilosité et organes génitaux.") + " Poil pubien isolé sans clitoromégalie. " + ital("6.3 Peau.") + " Taches café-au-lait. " + ital("6.4 Croissance.") + " Vitesse. " + ital("6.5 Neurologie.") + " On cherche un signe neurologique. Le chapitre lu ne décrit pas le fond d'œil : s'il existe un signe central, on adresse pour l'imagerie plutôt que d'inventer un geste."),
        fen("Fenêtre 6.1 — Palper le sein", [
            p("On cherche un tissu glandulaire ferme sous l'aréole. Un coussin graisseux chez une fille en surpoids n'est pas une thélarche. Le chapitre ne détaille pas la cote de Tanner : on décrit ce que l'on palpe."),
        ], seep),
    ]))
    c.append(point(7, "Approche syndromique", [
        p(ital("7.1 Thélarche isolée.") + " Signe fonctionnel : aucun, ou une question parentale. Signe physique : sein seul. Mécanisme : variante incomplète, axe non activé en bloc."),
        p(ital("7.2 Pubarche isolée.") + " Signe fonctionnel : odeur de transpiration possible, non chiffrée ici. Signe physique : pilosité pubienne ou axillaire sans sein, sans croissance du pénis ou du clitoris, sans accélération staturale."),
        p(ital("7.3 Progression vers une puberté précoce.") + " Les signes se multiplient et la vitesse augmente. On quitte alors la variante."),
        fen("Fenêtre 7.1 — Unités sémiologiques", [
            table(["Signe", "Recherche", "Mécanisme"], [
                ["Bourgeon mammaire", "Palpation bilatérale.", "Effet œstrogénique local, sans prouver une GnRH pulsatile."],
                ["Pilosité pubienne isolée", "Inspection, stadification.", "Adrénarche, pas axe gonadotrope."],
                ["Accélération de la vitesse", "cm par an sur la courbe.", "Stéroïdes sexuels qui agissent sur le cartilage : ce n'est plus une variante stable."],
            ]),
        ], seep),
    ]))
    c.append(point(8, "Diagnostic positif et critères", [
        p("La variante se retient quand le signe est isolé, stable ou régressif, sans accélération de croissance et sans âge osseux avancé. Le chapitre ne donne pas de délai chiffré unique de surveillance. Il demande, pour la ménarche isolée, une échographie pelvienne, un âge osseux, un test à la GnRH et un estradiol, afin d'écarter les autres causes."),
        p("Ce qui ne suffit pas : un sein avant 8 ans qui s'accompagne déjà d'une pilosité et d'une vitesse haute. Cela devient une puberté précoce, dont la définition d'âge est 8 ans chez la fille et 9 ans chez le garçon."),
    ]))
    c.append(point(9, "Examens complémentaires", [
        p(ital("9.a Gold standard.") + " Pour la variante isolée, il est clinique et évolutif. Il n'y a pas de dosage qui « prouve » une thélarche bénigne le premier jour."),
        p(ital("9.b Première intention.") + " Courbe et vitesse, âge osseux si un doute de progression existe, palpation répétée. " + ital("9.c.") + " Échographie pelvienne si le sein s'accompagne d'un utérus stimulant ou d'un saignement. " + ital("9.d.") + " Test à la GnRH et IRM si la puberté est vraiment précoce et évolutive, surtout chez le garçon et chez la petite fille, selon les nuances du chapitre."),
        fen("Fenêtre 9.1 — Quand intensifier", [
            table(["Constat", "Lecture", "Conduite"], [
                ["Sein seul, vitesse normale, os non avancé", "Variante possible.", "Revoir, ne pas traiter."],
                ["Plusieurs caractères et vitesse haute", "Puberté précoce jusqu'à preuve du contraire.", "Test à la GnRH, imagerie selon le sexe et l'âge, avis spécialisé."],
                ["Garçon", "Part neurogène souvent haute.", "Ne pas appliquer la même attente qu'à une fille."],
                ["Saignement sans sein", "Ménarche isolée rare ou cause locale.", "Écarter infection, corps étranger, tumeur, McCune-Albright, œstrogène exogène, hypothyroïdie."],
            ]),
        ], seep),
    ]))
    c.append(point(10, "Arbre décisionnel", [
        p("Signe isolé et stable : expliquer, revoir, mesurer. Progression, garçon, signe neurologique ou virilisation : quitter la variante et chercher une puberté précoce centrale, périphérique ou une lésion. On n'injecte pas un analogue de GnRH sur un bourgeon isolé non évolutif."),
    ]))
    c.append(point(11, "Prise en charge selon les recommandations suisses", [
        p(ital("A- But.") + " Laisser se dérouler une puberté ultérieure normale, et détecter vite une progression. Le chapitre dit d'informer et de rassurer pour la ménarche isolée, avec une vigilance périodique."),
        p(ital("B- Moyens.") + " Surveillance clinique. Pas de médicament dans la variante stable. L'analogue de la GnRH appartient à la puberté précoce évolutive, pas à ce DX. Dose AIPS : donnée non trouvée, et sans objet tant que l'indication n'est pas posée. Œstrogènes exogènes : on les retire s'ils sont la cause."),
        p("Situations spéciales : c'est un DX de l'enfant. Grossesse : sans objet. Insuffisance rénale ou hépatique : sans objet en l'absence de médicament. Sujet âgé : sans objet."),
        p(ital("C- Surveillance.") + " Contrôles répétés de la palpation, de la vitesse et, si besoin, de l'âge osseux. Le délai exact en semaines n'est pas chiffré dans le chapitre 8 lu. On intensifie si un nouveau signe apparaît."),
        p("Pas d'hospitalisation pour une thélarche isolée stable. Les parents repartent avec la liste des signes de progression."),
        p(ital("D- Pronostic.") + " Stabilité, régression ou puberté normale plus tard sont possibles. La progression vers une puberté précoce vraie change le pronostic de taille, parce que les stéroïdes avancent l'âge osseux. Recherche 2026 : non couverte par ce chapitre."),
    ]))
    c.append(point(12, "Prévention", [
        p("Primaire : éviter les œstrogènes exogènes cachés dans des produits. Secondaire : revoir toute thélarche ou pubarche précoce pour ne pas manquer la progression. Tertiaire : traiter la vraie puberté précoce à temps pour protéger la taille, hors de ce DX stable."),
    ]))
    c.append(point(13, "Points clés", [
        p("Vous palpez une glande, vous ne cotez pas un pli graisseux."),
        p("Vous séparez le signe isolé de la puberté précoce avant 8 ans chez la fille et avant 9 ans chez le garçon."),
        p("Vous ne rassurez pas un garçon comme une fille."),
        p("Vous surveillez, vous ne traitez pas une forme stable par un analogue."),
        p("Vous cherchez une cause locale devant un saignement sans autre signe."),
    ]))
    c.append(point(14, "Pièges et questions fréquentes à l'examen fédéral suisse", [
        p("Piège : analogue de GnRH dès le premier bourgeon. Bonne réponse : surveillance si le signe est isolé et non évolutif."),
        p("Piège : âge seuil inversé. Bonne réponse : avant 8 ans chez la fille, avant 9 ans chez le garçon, dans le texte lu."),
        p("Piège : pubarche isolée prise pour une hyperplasie congénitale. Bonne réponse : la virilisation et l'âge osseux très avancé changent de diagnostic."),
        fen("Fenêtre 14.1 — Question type", [
            p("Fille de 2 ans, bourgeon mammaire isolé, vitesse normale, pas de pilosité, pas de tache cutanée. Conduite ?"),
            p("Vous expliquez la thélarche prématurée possible, vous organisez une surveillance de la progression, et vous n'envoyez pas d'emblée un analogue. Vous élargissez le bilan si la vitesse accélère ou si un autre signe apparaît."),
        ], seep),
    ]))
    return mono("DX.10", "Prémature thélarche ou prémature pubarche",
                "Rang du projet — fréquence suisse de la variante non quantifiée ; puberté précoce 1/5 000 à 1/10 000 dans le chapitre espagnol [S404]",
                "".join(c))


SOURCES_DX5 = [
    ("S201", "European Society for Paediatric Endocrinology. Constitutional delay of growth and puberty, Hormone Disorders Series, lisibilité moyenne, révisé en novembre 2019.", "https://www.eurospe.org/wp-content/uploads/2022/12/constitutional-delay-of-growth-and-puberty-average-read.pdf"),
    ("S202", "Galazzi E, Persani LG. Differential diagnosis between constitutional delay of growth and puberty, idiopathic growth hormone deficiency and congenital hypogonadotropic hypogonadism. Minerva Endocrinol. Revue narrative, littérature jusqu'en mars 2020. DOI 10.23736/S0391-1977.20.03228-9.", "https://doi.org/10.23736/s0391-1977.20.03228-9"),
    ("S203", "Jenni O, Eiholzer U. Quand est-on trop grand ? Paediatrica, fichier pédiatrie suisse. Définition du 3e percentile et formule de la taille cible.", "https://files.paediatrieschweiz.ch/production/uploads/2016/01/24-27.pdf"),
    ("S204", "pédiatrie suisse. Nouvelles courbes de croissance. Communiqué du 16 juin 2026, recommandation à compter du 15 juin 2026. Courbes PEZZ, Eiholzer et coll.", "https://www.paediatrieschweiz.ch/fr/news/nouvelles-courbes-de-croissance/"),
    ("S205", "PEZZ, Centre d'endocrinologie pédiatrique de Zurich. Croissance : canal de percentile après 2 ans, 3e et 97e percentiles, mesures annuelles. Page familles.", "https://www.pezz.ch/fr/fuer-familien/wachstum/"),
]

SOURCES_P3 = [
    ("S301", "Réservé, non utilisé, pour garder la plage S300 de la partie 3.", "https://www.paediatrieschweiz.ch/fr/documents/courbes-de-croissance/"),
    ("S302", "pédiatrie suisse. Nouvelles courbes de croissance, recommandation du 15 juin 2026.", "https://www.paediatrieschweiz.ch/fr/news/nouvelles-courbes-de-croissance/"),
    ("S303", "PEZZ. Croissance, canal après 2 ans, signification d'un percentile.", "https://www.pezz.ch/fr/fuer-familien/wachstum/"),
    ("S304", "Jenni O, Eiholzer U. Paediatrica. 3e percentile = −1,88 DS, formule ± 13 cm, intervalle ± 8,5 cm.", "https://files.paediatrieschweiz.ch/production/uploads/2016/01/24-27.pdf"),
    ("S305", "Galazzi E, Persani LG. Minerva Endocrinol, critères du retard constitutionnel utilisés ici seulement pour le diagnostic différentiel.", "https://doi.org/10.23736/s0391-1977.20.03228-9"),
    ("S306", "ESPE. Constitutional delay of growth and puberty, dépliant révisé en novembre 2019. Seuils 13 et 14 ans, caryotype, âge osseux.", "https://www.eurospe.org/wp-content/uploads/2022/12/constitutional-delay-of-growth-and-puberty-average-read.pdf"),
    ("S307", "Husby S et al. European Society for Paediatric Gastroenterology, Hepatology and Nutrition. Guidelines for Diagnosing Coeliac Disease 2020. JPGN. DOI 10.1097/MPG.0000000000002497.", "https://doi.org/10.1097/mpg.0000000000002497"),
]

SOURCES_P4 = [
    ("S401", "Pedlaus, Faculté de biologie et de médecine, Lausanne. Fiche Hypothyroïdie acquise. 1/500 à l'âge scolaire, Hashimoto, biologie, lévothyroxine sans dose AIPS recopiée.", "https://www.pedlaus.ch/detail/fiche/hypothyroidie-acquise"),
    ("S402", "Zhang L, Pruteanu AI, Prietsch SOM, Chauhan BF, Ducharme FM. Inhaled corticosteroids in children with persistent asthma: effects on growth. Cochrane. Réduction moyenne de 0,48 cm/an la première année, reprise dans la synthèse des revues Cochrane sur le sujet.", "https://www.cochrane.org/evidence/CD009471_do-inhaled-corticosteroids-reduce-growth-children-persistent-asthma"),
    ("S403", "Revue Cochrane sur les molécules et dispositifs (CD010126), mécanisme GH–IGF-1 et chondrocytes, et synthèse : 0,48 cm/an, effet moins marqué ensuite, possible persistance à l'âge adulte non cumulative.", "https://doi.org/10.1002/14651858.CD010126.pub2"),
    ("S404", "Société espagnole d'endocrinologie pédiatrique. Puberté précoce, chapitre 8. Variantes isolées, seuils 8 et 9 ans, incidence 1/5 000 à 1/10 000, sex-ratio 20:1.", "https://www.seep.es/images/site/publicaciones/oficialesSEEP/consenso/cap08.pdf"),
    ("S405", "pédiatrie suisse. Courbes nationales recommandées depuis le 15 juin 2026, utilisées pour reporter la vitesse.", "https://www.paediatrieschweiz.ch/fr/news/nouvelles-courbes-de-croissance/"),
    ("S306", "ESPE. Dépliant sur le retard constitutionnel, cité seulement pour ne pas confondre une puberté tardive avec une thélarche précoce.", "https://www.eurospe.org/wp-content/uploads/2022/12/constitutional-delay-of-growth-and-puberty-average-read.pdf"),
]

INTRO = (
    "Examen fédéral suisse, PROFILES 2023, SSP O2.1 « Croissance anormale, puberté avancée ou retardée, "
    "retard staturo-pondéral ». Agent B (B07), équipe E07 Flash. Périmètre DX.5 à DX.10 seulement. "
    "L'Appel A et la partie 1 (DX.1–DX.2) ne sont pas relus : le dossier Drive indiqué a répondu 404 et "
    "aucune branche LOT_183 n'existait. L'ordre des noms est celui de la liste NOT déjà publiée dans l'application. "
    "Les fenêtres s'ouvrent au clic. Sources lues le " + DATE + ". Aucune dose AIPS n'est prescrite."
)


def with_extra(mono_html, key):
    import importlib.util
    path = os.path.join(HERE, "expand_lot183.py")
    specx = importlib.util.spec_from_file_location("ex", path)
    ex = importlib.util.module_from_spec(specx)
    specx.loader.exec_module(ex)
    idx = mono_html.rfind("</details>")
    if idx < 0:
        raise SystemExit("mono sans details")
    return mono_html[:idx] + ex.extra(key) + mono_html[idx:]


def write(name, title, h2, intro, monos, sources, tag):
    text = page(title, h2, intro, monos, sources, tag)
    path = os.path.join(HERE, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"{name}: {len(text.encode('utf-8'))} octets, {text.count(chr(10))+1} lignes")


def main():
    write(
        "LOT_183_Appel_B_V7_DX.5.html",
        "LOT_183 O2.1 — DX.5",
        "LOT_183 — SSP O2.1 « Croissance anormale, puberté avancée ou retardée, retard staturo-pondéral » — DX.5 seul (DX.3 et DX.4 hors périmètre)",
        INTRO,
        [with_extra(g.dx5(), "dx5")],
        SOURCES_DX5,
        "LOT_183_DX5",
    )
    write(
        "LOT_183_Appel_B_V7_Partie_3_DX.6_a_DX.7.html",
        "LOT_183 O2.1 — Partie 3 DX.6 et DX.7",
        "LOT_183 — SSP O2.1 « Croissance anormale, puberté avancée ou retardée, retard staturo-pondéral » — Partie 3 : DX.6 et DX.7",
        INTRO,
        [with_extra(dx6(), "dx6"), with_extra(dx7(), "dx7")],
        SOURCES_P3,
        "LOT_183_PARTIE_3",
    )
    write(
        "LOT_183_Appel_B_V7_Partie_4_DX.8_a_DX.10.html",
        "LOT_183 O2.1 — Partie 4 DX.8 à DX.10",
        "LOT_183 — SSP O2.1 « Croissance anormale, puberté avancée ou retardée, retard staturo-pondéral » — Partie 4 : DX.8, DX.9 et DX.10",
        INTRO,
        [with_extra(dx8(), "dx8"), with_extra(dx9(), "dx9"), with_extra(dx10(), "dx10")],
        SOURCES_P4,
        "LOT_183_PARTIE_4",
    )
    evid = {
        "lot": 183,
        "ssp": "O2.1",
        "agent": "B07",
        "branche": "flash/vague1/LOT_183-B",
        "perimetre": "DX.5 à DX.10",
        "appel_A_lu": False,
        "drive": "1GHkS8Q6q7lrFyhRF2jWeQsA6UVDFxjIO",
        "drive_resultat": "404 File not found",
        "aips_ouvertes": False,
        "consulte_le": "2026-10-24",
        "sources": SOURCES_DX5 + SOURCES_P3 + SOURCES_P4,
    }
    with open(os.path.join(HERE, "evidence_DX5-DX10.json"), "w", encoding="utf-8") as f:
        json.dump(evid, f, ensure_ascii=False, indent=1)
    print("evidence ok")


if __name__ == "__main__":
    main()
