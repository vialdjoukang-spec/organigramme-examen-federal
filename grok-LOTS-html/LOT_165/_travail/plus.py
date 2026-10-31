# -*- coding: utf-8 -*-
"""Développements cliniques ajoutés pour la profondeur, sans nouvelle dose."""

def P(t, src=2):
    return (t, src)


def phase_extra():
    return [
        P("Lecture d'une poche avant qu'elle coule. On dit le nom, le prénom et la date de naissance complète, on les fait répéter si la personne peut parler, "
          "on compare à la carte, au bulletin et à l'étiquette. Un homonyme se tranche sur la date, pas sur le prénom seul. "
          "Les jumeaux se tranchent de la même façon. Le guide 2026 veut cette identité demandée même si un système électronique a déjà lu un bracelet, "
          "parce que l'électronique remplace une des deux personnes, pas la question posée au patient.", 3),
        P("Deuxième lecture, séparée. La deuxième personne ne signe pas ce que la première a déjà conclu. Elle refait le groupe, la péremption, l'aspect de la poche et la validité des tests. "
          "Si le téléphone sonne au milieu, on recommence. Cette règle du guide 2026 évite la demi-vérification, qui est celle des confusions ABO.", 3),
        P("Ce que l'on voit sur la poche et qui arrête tout, avant même le groupe. Poche percée, fuite, couleur anormale, plasma trouble au-dessus des globules, caillot, "
          "date dépassée. Le produit ne se transfuse pas. On le renvoie au laboratoire avec le motif. Ce n'est pas une incompatibilité immunologique, c'est un défaut, et il se déclare aussi.", 3),
        P("Les quinze premières minutes. On reste là. Tension, pouls, respiration, saturation si la personne est fragile, température, peau, parole. "
          "Une douleur au point d'injection dans ces minutes est un drapeau d'hémolyse jusqu'à preuve du contraire, pas un problème de cathéter que l'on rince en continuant la poche.", 3),
        P("Après le quart d'heure, on ne disparaît pas. Les constantes reviennent régulièrement jusqu'à la fin et après la fin. "
          "La médiane de l'hémolyse aiguë est à 90 minutes, celle de la surcharge aussi, celle de la fièvre non hémolytique à 80 minutes, celle de l'allergie à 45 minutes. "
          "Quitter après un quart d'heure calme rate la médiane.", 2),
        P("Six heures. Dès que la chaîne du froid est rompue, et dès que la tubulure a perforé la poche, le guide 2026 demande en général de terminer dans les six heures. "
          "Une poche ouverte le matin ne se reprend pas le soir. Les plaquettes, elles, partent dès qu'elles arrivent, elles ne s'asseyent pas sur un plan de travail.", 3),
        P("Réchauffer. Seulement un appareil prévu pour le sang, et seulement pour les situations écrites : agglutinines froides, transfusion massive, néonatologie, exsanguino-transfusion. "
          "L'eau chaude du robinet hémolyse le produit et fabrique un tableau qui ressemble à une incompatibilité. On ne le fait pas.", 3),
        P("Chlorure de sodium à 0,9 % pour rincer la lumière après la poche. Le guide le dit. On ne rince pas avec un soluté dont on n'a pas vérifié la compatibilité avec le sang dans la même lumière. "
          "On ne verse rien dans la poche elle-même.", 3),
        P("Nuit. Le guide demande d'éviter la transfusion la nuit quand elle peut attendre, parce que l'attention baisse et les effectifs aussi. "
          "Une anémie stable à minuit n'est pas une urgence vitale. Une hémorragie active, elle, n'attend pas le jour : on transfuse, et l'on double quand même les contrôles.", 3),
        P("Calcul de l'anti-D sans inventer un résultat qui ne serait pas dans l'information. "
          "On part de 10 µg, soit 50 UI, pour 0,5 ml d'hématies RhD positif. On compte le nombre de tranches de 0,5 ml dans le volume mesuré par Kleihauer ou par cytométrie. "
          "Chaque tranche ajoute 10 µg. Au-dessus de 4 ml d'hématies fœtales, cette addition est exigée, de préférence en intraveineux. "
          "Si aucun test n'est disponible et que le passage excessif n'est pas exclu, on ajoute une seringue entière de 300 µg, soit 1500 UI, plutôt qu'un chiffre calculé de mémoire.", 4),
        P("Plafond. Même si le volume transfusé de sang RhD positif dépasse 300 ml de sang complet ou 150 ml de concentré, l'information juge qu'une dose totale de 3'000 µg, soit 15'000 UI, suffit. "
          "On ne va en général pas au-delà, à cause de l'hémolyse que l'anti-D peut provoquer chez la personne qui reçoit beaucoup de globules RhD positif. "
          "Ces personnes se surveillent. L'enfant et l'adolescent suivent le même principe de volume, avec un spécialiste de la transfusion.", 4),
        P("Exemple de déclaration, grade et imputabilité séparés. Fièvre à 38,5 °C, hausse de 1,2 °C, bilan d'hémolyse négatif, cultures négatives, dans les deux heures. "
          "Case : réaction fébrile non hémolytique. Le critère de fièvre qui force le grade sévère, supérieur à 39 °C et plus de 2 °C, n'est pas atteint. "
          "Le grade peut rester non sévère si rien d'autre de la liste du grade 2 n'est là. L'imputabilité se discute à part.", 1),
        P("Deuxième exemple. Dyspnée, hypertension, œdème nouveau, bilan d'entrées positif, dans l'heure. Quatre signes : surcharge. "
          "Grade au moins sévère à cause de la dyspnée, sauf forme très légère que ce tableau n'est pas. "
          "Même si l'on conclut plus tard que l'insuffisance cardiaque seule explique tout, le rapport dit qu'une suspicion de surcharge avec dyspnée significative reste classée sévère.", 1),
        P("Troisième exemple. Confusion de patients, quelques dizaines de millilitres, hémolyse biologique, décès le lendemain sur un terrain lourd. "
          "Le rapport 2024 a classé grade 4 seulement parce que l'imputabilité était possible. Si le lien avait été exclu, le décès n'aurait pas porté le grade 4. "
          "On écrit les deux jugements, on ne les fond pas.", 1),
        P("Traçabilité. Depuis le 1er janvier 2019, les données se gardent 30 ans. Ce qui compte est que le produit a été transfusé, pas seulement qu'il a quitté le laboratoire. "
          "Une enquête rétrospective qui ne retrouve pas le receveur réel est une enquête ratée. La personne responsable, médecin ou formation reconnue, porte cette chaîne.", 3),
        P("Produits qui ne se mélangent pas dans la tête. Globules : tableau des antigènes du donneur. Plasma : tableau des anticorps du donneur. "
          "Plaquettes : antigènes ABO sur la plaquette, et plasma résiduel qui peut porter anti-A ou anti-B, et parfois des hématies résiduelles dont le volume n'est pas chiffré dans les pièces lues. "
          "Urgence absolue sans groupe : concentré O RhD négatif, carte au lit quand même, pas de plasma O à la place.", 9),
        P("Femme RhD négatif qui saigne à 16 semaines. L'information suisse ne découpe pas 12 et 20 semaines : une complication reçoit 300 µg dans les 72 heures, "
          "puis une répétition toutes les 12 semaines jusqu'à l'accouchement si l'indication de complication reste. "
          "Le guide britannique, lui, met un minimum plus bas avant 20 semaines et ne demande pas le Kleihauer avant 20 semaines. "
          "On ne descend pas la seringue suisse à ce minimum. On peut citer le guide pour comprendre un dossier étranger, pas pour sous-doser en Suisse.", 4),
        P("Tube de la 28e semaine. Il se prend avant la seringue. Après, l'anti-D passif peut être pris pour un anti-D immun, ou l'inverse. "
          "Si le doute reste, le guide 2014 continue la prophylaxie. L'information suisse réserve l'exclusion aux personnes déjà immunisées de façon établie, et aux personnes RhD positif.", 8),
        P("Nouveau-né ictérique à 18 heures, mère O, enfant A, Coombs faible, pas d'anti-D. Ce n'est pas un motif de Rhophylac. "
          "C'est une incompatibilité ABO, surveillance de la bilirubine, pas une seringue anti-D. "
          "Nouveau-né ictérique, mère RhD négatif, anti-D immun déjà connu, enfant RhD positif, Coombs positif : là, c'est la maladie par anti-D, et la seringue ne traite pas l'enfant.", 4),
        P("Kell chez une femme enceinte n'est pas un anti-D faible que l'on rassure avec un titre. L'anticorps vise l'érythropoïèse. "
          "On le nomme, on le transmet par écrit au laboratoire et à l'obstétrique, on ne le couvre pas avec 300 µg d'anti-D.", 4),
        P("Test de Coombs direct, geste de laboratoire. On met en présence les globules du patient et un sérum antiglobuline humaine. "
          "Si des immunoglobulines G ou du complément sont déjà fixés, les globules s'agglutinent. "
          "C'est le test que l'aide-mémoire du 9 août 2024 demande dans le volet immunohématologie, avec élution s'il est positif. "
          "Le versant indirect, recherche dans le plasma et épreuve de compatibilité, cherche l'anticorps qui n'est pas encore collé. "
          "Un direct positif ne dit pas le nom de l'anticorps. L'élution et la recherche le disent.", 2),
        P("Formulaires de l'aide-mémoire, pour ne pas déclarer au mauvais endroit. Réaction transfusionnelle : formulaire I-310.AA.01-A05. "
          "Incidents et faits graves, y compris l'erreur de produit et le near miss encore exigible : I-310.AA.01-A06. "
          "Effet indésirable chez le donneur : I-310.AA.01-A07. "
          "Une réaction et une erreur de patient sur la même poche font les deux déclarations, pas une seule phrase dans le dossier de soins.", 2),
        P("Near miss. L'écart a été vu avant que le sang coule. Il aurait pu donner une mauvaise poche ou une réaction. "
          "On l'analyse quand même, parce que la poche suivante peut répéter l'erreur. "
          "En 2024, le grade 1 de near miss, sans risque de confusion, n'est plus obligatoire à déclarer à Swissmedic. "
          "Un tube mal identifié qui aurait pu croiser deux patients n'est pas ce grade-là.", 1),
        P("Erreur de produit, dite aussi transfusion d'un composant incorrect. Mauvais patient, produit non irradié alors qu'il devait l'être, "
          "produit non négatif pour le cytomégalovirus alors que l'indication l'exigeait. "
          "On déclare même si le patient va bien, avec le récit : comment l'erreur est née, comment elle a été vue, quelles mesures suivent. "
          "Le rapport 2024 compte une hausse des incidents graves sans changement de RhD, de 48 à 69.", 1),
        P("Look-back. Un donneur reconnu porteur d'un agent après un don déjà transfusé déclenche la recherche des receveurs. "
          "La chaîne doit retrouver la transfusion réelle. Les receveurs et leurs médecins sont contactés. "
          "Les preuves remontent au service de transfusion et à Swissmedic. Trente ans d'archive ne servent à rien si le service n'a noté que la sortie du dépôt.", 3),
        P("Qui décide au lit. L'infirmière arrête la poche dès le signe, elle n'attend pas l'interne pour clamper. "
          "Le médecin décide de la suite, du remplissage, de l'adrénaline ou du diurétique selon le tableau, et de la déclaration avec la personne responsable de l'hémovigilance. "
          "Le laboratoire décide des tubes et de la compatibilité suivante. Personne ne décide seul de relancer la même poche.", 3),
        P("Ordre des gestes quand tout arrive en même temps. D'abord clamper. Ensuite garder une voie. Ensuite oxygène si la saturation tombe. "
          "Ensuite seulement le médicament qui correspond : adrénaline si choc allergique, diurétique si surcharge déjà qualifiée, rien de ces deux-là si l'on est devant une hémolyse ABO ou un TRALI. "
          "Le bilan part en parallèle, il ne retarde pas le clamp.", 5),
        P("Carte et groupe ne sont pas le même geste. La safety-card genevoise vérifie une compatibilité de globules déjà groupés ailleurs. "
          "Elle ne pose pas le groupe ABO du patient. S'en servir comme déterminante, ou l'appliquer au plasma, sort du référentiel du 15 février 2024. "
          "Les cupules qui ne réagissent pas se regardent jusqu'à 3 minutes. Une carte dont l'anti-A n'est pas bleu turquoise ou l'anti-B n'est pas jaune ne s'utilise pas.", 9),
        P("Receveur universel et donneur universel se disent avec le produit. AB reçoit tous les globules et donne du plasma à tous. "
          "O donne des globules à tous et ne donne son plasma qu'à O. "
          "Le concentré d'extrême urgence sans groupe connu est O et RhD négatif, pas un plasma. "
          "Dire donneur universel sans nommer le produit est la phrase que l'examen sanctionne.", 9),
        P("Deux fièvres, deux usages. Supérieure à 38 °C et hausse d'au moins 1 °C : définition possible de la réaction fébrile non hémolytique, dans les 4 à 6 heures, après exclusion. "
          "Supérieure à 39 °C et hausse supérieure à 2 °C : le rapport annuel force au moins le grade sévère, quelle que soit la case. "
          "Une fièvre peut remplir la première ligne sans remplir la seconde. L'inverse, une fièvre très haute, remplit la seconde et interdit de traiter le dossier comme anodin.", 1),
        P("Contrôle ultime, unité de lieu, de temps et d'action, comme l'écrit le référentiel genevois. Au lit, pas au poste de soins. "
          "Juste avant la pose, pas une heure plus tôt. Par la personne qui transfuse. "
          "Concordance pour tout produit. Carte de compatibilité pour les globules, y compris le O RhD négatif du dépôt d'urgence. "
          "Doute : on ne transfuse pas, on appelle le laboratoire.", 9),
    ]


def dx_extra(index):
    """index 1..10. Paragraphes ajoutés aux fenêtres courtes."""
    commun = [
        P("Au dossier, on écrit quatre mots avant le nom de la réaction : l'heure de début par rapport au début de la poche, le symptôme principal, "
          "le résultat du contrôle d'identité, et ce qui a été arrêté. Sans ces quatre mots, le laboratoire reconstruit mal, et la déclaration aussi.", 3),
        P("On ne reprend pas la même poche après une pause pour voir. Une reprise n'appartient qu'à un protocole écrit pour une réaction cutanée légère isolée, "
          "et le guide 2026 dit que c'est le système qualité du lieu qui fixe si l'on peut reprendre, pas une habitude de service.", 3),
        P("Le concentré suivant, s'il est encore nécessaire, repart de zéro : identité, validité de la recherche d'anticorps, compatibilité, carte s'il s'agit de globules. "
          "Une réaction n'accélère pas la poche d'après. Elle la ralentit.", 3),
    ]
    banques = {
        1: [
            P("Anti-K chez une femme de 29 ans, première grossesse, jamais transfusée. L'anticorps peut venir d'une grossesse débutante déjà immunisante, ou d'une transfusion oubliée. "
              "On ne le classe pas en prophylaxie. On ne le traite pas par Rhophylac. On le signale à l'obstétrique le jour même, par écrit, comme le guide 2026 le demande pour tout allo-anticorps.", 3),
            P("Anti-Fya chez un homme transfusé trois fois en cinq ans. La recherche d'aujourd'hui le trouve, il n'y a pas de chute d'hémoglobine, pas d'ictère, Coombs direct négatif. "
              "Case : allo-immunisation, pas réaction hémolytique. Les prochains globules doivent être compatibles, la banque le fera. "
              "Le clinicien, lui, ne demande pas un concentré au hasard du frigo d'urgence s'il a le temps d'attendre.", 2),
            P("Anti-Jkb introuvable en janvier, transfusion en mars sur une recherche négative, ictère en avril. "
              "Ce parcours est celui d'un anticorps qui passe sous le seuil de détection. La case de janvier, si rien n'hémolysait, était l'allo-immunisation ou même une recherche muette. "
              "La case d'avril, avec hémolyse, est la réaction retardée. On n'écrit pas que la recherche de mars innocente la poche.", 2),
            P("HLA et HPA entrent dans la définition de l'allo-immunisation de l'aide-mémoire, pas seulement les antigènes érythrocytaires. "
              "Un anti-HLA après transfusion, sans hémolyse, reste cette case. Un anti-HPA avec une thrombopénie entre le jour 5 et le jour 12 quitte cette case pour le purpura post-transfusionnel.", 2),
            P("Grade. Les 1519 allo-immunisations de 2024 sont toutes en grade 2. On n'écrit pas grade 1 parce que la personne va bien ce jour-là. "
              "Le rapport a déjà décidé que l'allo-immunisation est au minimum sévère. L'imputabilité, elle, est souvent certaine quand l'anticorps est nouveau et la transfusion documentée, mais on la juge sur le dossier, pas par réflexe.", 1),
            P("Cas d'examen. Recherche positive anti-E, femme de 22 ans, pas de symptôme, transfusion de plaquettes il y a trois semaines. "
              "On nomme l'allo-immunisation anti-E. On ne parle pas de TRALI, ni de surcharge, ni de maladie hémolytique tant qu'il n'y a pas de grossesse avec un fœtus porteur de l'antigène et des signes. "
              "On prévient la patiente qu'une carte ou une mention doit suivre, pour que le prochain service ne l'ignore pas.", 2),
            P("Ce que l'on dicte à la banque : nom de l'anticorps, date de la recherche, grossesses, transfusions, et si une hémolyse est présente aujourd'hui. "
              "Un mot vague, anticorps froid ou irrégulier, ne choisit pas un concentré.", 3),
        ],
        2: [
            P("Frissons seuls, sans fièvre mesurée, entrent dans la liste : les frissons même isolés suffisent à ouvrir la case, si le délai est de 4 à 6 heures et si les autres causes tombent. "
              "On ne renvoie pas l'infirmière qui a vu des frissons sans chiffre de température. On mesure, et l'on bilanise.", 2),
            P("Sensation de froid et malaise, céphalées, nausées : ce sont les symptômes possibles, pas obligatoires. "
              "Ils ne font pas l'hémolyse à eux seuls, et ils ne l'écartent pas. La douleur lombaire, elle, n'est pas dans cette liste-là : elle pousse vers l'hémolyse.", 2),
            P("Fin de poche. L'aide-mémoire dit que les signes se remarquent souvent vers la fin. "
              "Une fièvre qui commence à la dernière goutte n'est pas trop tard pour être dans la fenêtre. Une fièvre le lendemain matin, au-delà de 6 heures, sort de cette définition et fait chercher autre chose, y compris une hémolyse retardée si les jours passent, ou une infection.", 2),
            P("Paracétamol. Il peut soulager quand le diagnostic est retenu, il ne le pose pas. "
              "Le donner pour finir la poche sans tubes est la conduite fausse. Les cultures du patient et du reste de poche font partie du bilan, parce que la bactérie est le diagnostic que cette case doit exclure.", 2),
            P("Cas. Homme de 70 ans, concentré pour saignement digestif stabilisé, 37,2 °C au début, 38,4 °C à 70 minutes, frissons, tension stable, urines claires, pas de douleur. "
              "Hausse de 1,2 °C et fièvre au-dessus de 38 °C. On arrête. Documents, Coombs direct, compatibilité, lactate déshydrogénase, bilirubine, haptoglobine, hémoglobine libre, urine, deux séries de cultures. "
              "Si tout est négatif, le nom est réaction fébrile non hémolytique. Le grade sévère par la fièvre seule n'est pas atteint : on n'est pas au-dessus de 39 °C avec plus de 2 °C. "
              "On déclare selon le circuit, le grade 1 reste possible si aucun autre critère de gravité n'est là.", 1),
            P("Cas limite. Même homme, 38,0 °C au début, 40,2 °C à 50 minutes, tension qui passe de 130 à 90 mm Hg. "
              "La fièvre dépasse 39 °C et la hausse dépasse 2 °C : au moins grade 2, quoi que dise la cause finale. "
              "La chute de tension ajoute le drapeau. On ne nomme pas la réaction fébrile tant que l'hémolyse et la culture ne sont pas lues. On traite le sepsis si le tableau le demande, sans attendre le nom immunohématologique.", 1),
            P("Produit plaquettaire et réaction fébrile. Les plaquettes s'infectent plus volontiers que les globules parce qu'elles restent à température ambiante. "
              "Une fièvre pendant des plaquettes renforce l'urgence des cultures. La carte ABO ne se fait pas sur les plaquettes : ce n'est pas une raison pour sauter la concordance d'identité.", 9),
            P("Ce que l'étudiant écrit de travers : la réaction fébrile est bénigne, donc on ne déclare pas. "
              "Faux. Elle se déclare. En 2024, 518 déclarations, dont 5 de grade 3. Bénin n'est pas le mot du rapport.", 1),
            P("Différentiel minute par minute. Minute 10, douleur lombaire : hémolyse jusqu'à preuve. Minute 15, urticaire seule : allergie légère si le reste est calme. "
              "Minute 45, stridor : anaphylaxie, adrénaline, pas cette case. Heure 1, dyspnée et hypertension : surcharge. Heure 2, fièvre isolée : cette case seulement après bilan. "
              "Jour 9, ictère : réaction retardée, plus cette case.", 2),
        ],
        4: [
            P("Mère O, enfant O : pas d'incompatibilité ABO. L'ictère a une autre cause. Mère A, enfant O : la mère A a de l'anti-B, l'enfant O n'a pas d'antigène B. "
              "Mère A, enfant B : possible mais moins classique que mère O. Mère O, enfant A ou B : terrain le plus fréquent de cette maladie, parce que l'anti-A et l'anti-B de classe G sont surtout le fait du groupe O.", 2),
            P("Heure de l'ictère. Avant 24 heures de vie, on ne parle pas d'ictère simple. On groupe, on fait le Coombs direct, on dose la bilirubine, on regarde l'hémoglobine. "
              "Le Coombs peut être à peine positif. Un Coombs négatif n'élimine pas toujours une hémolyse ABO modérée, et un Coombs positif ne la prouve pas si la mère a reçu de l'anti-D. "
              "Ici, si la mère est RhD positif et sans anti-D, le passif anti-D n'explique pas le test.", 8),
            P("Clinique du nouveau-né. Pâleur, ictère, parfois hépatosplénomégalie si l'hémolyse est forte, urines foncées, bilirubinémie qui monte. "
              "L'anémie peut être modérée. On ne rassure pas la famille avec le mot ABO sans un chiffre de bilirubine et un plan de contrôle.", 2),
            P("Ce que l'on ne fait pas. Pas de Rhophylac à la mère RhD positif. Pas de Rhophylac à l'enfant. "
              "Pas de concentré O RhD négatif en routine : si une transfusion est décidée, le groupe se choisit avec la banque, souvent des globules O compatibles avec le plasma de la mère et de l'enfant, décision de néonatologie et de banque, pas une poche d'urgence par réflexe.", 9),
            P("Photothérapie. Le seuil de bilirubine qui lance la lampe dépend de l'âge en heures et du terme. Ce seuil n'est pas dans les pièces transfusionnelles lues pour ce lot. "
              "On ne l'invente pas. On dit : la photothérapie suit le protocole néonatal, et l'incompatibilité ABO est une cause à nommer dans le dossier pour que le contrôle soit plus serré qu'un ictère simple.", 2),
            P("Grossesse suivante. L'incompatibilité ABO ne s'aggrave pas comme une immunisation anti-D d'une grossesse à l'autre de façon aussi prévisible. "
              "On ne met pas cette mère sous prophylaxie anti-D pour cette raison. On regroupe quand même l'enfant suivant, parce qu'un autre antigène peut s'ajouter.", 4),
            P("Cas. Mère O RhD positif, enfant B, ictère à H20, bilirubine en hausse, Coombs direct positif faible, recherche d'anticorps irréguliers maternelle négative, hémoglobine de l'enfant stable. "
              "Nom : maladie hémolytique par incompatibilité ABO. Conduite : surveillance rapprochée, photothérapie si le protocole néonatal le dit, pas d'anti-D, information des parents sur les contrôles. "
              "Copie fausse : exsanguino-transfusion immédiate sans chiffre, ou seringue de 300 µg à la mère.", 4),
            P("Cas sévère. Même groupes, hémoglobine très basse, enfant pâle, polypnée. Le mot modéré ne ferme pas la réanimation. "
              "On appelle le néonatologiste. Le bilan d'hémolyse de l'enfant reste utile. On cherche quand même un irrégulier maternel que la première lecture aurait manqué, Kell compris.", 2),
            P("Différentiel au berceau. Hématome du cuir chevelu, prématurité, infection, incompatibilité par anti-D ou anti-c ou anti-K, déficit enzymatique. "
              "Le groupe explique beaucoup quand il est O contre A ou B, il n'explique pas tout si un autre anticorps est écrit sur la feuille de la mère.", 2),
        ],
        5: [
            P("Avant la poche, trois questions. Le patient a-t-il déjà dyspné au repos ? A-t-il une cardiopathie, une sténose aortique, une insuffisance rénale ? "
              "Le bilan des entrées est-il déjà positif ? Si oui, le rapport 2024 demande une transfusion lente, l'exemple écrit est 1 ml par kilogramme et par heure, et d'envisager un diurétique. "
              "Envisager n'est pas injecter 40 mg à tout le monde. Si l'on injecte, c'est la dose de l'information 30630, adaptée au terrain, et l'on se souvient de l'inhibiteur de l'enzyme de conversion.", 1),
            P("Quatre signes, pas trois. Détresse seule est insuffisante : ce peut être un TRALI ou une allergie. "
              "On cherche la tachycardie, l'hypertension, la radiographie, le bilan de volume, la toux ou la douleur thoracique, et l'on sait que la fièvre accompagne environ 30 % des surcharges sans les définir.", 2),
            P("Hypertension contre choc. La surcharge monte souvent la tension. L'hémolyse aiguë et l'anaphylaxie la baissent. "
              "Une dyspnée avec tension à 80 mm Hg n'est pas le tableau typique de la surcharge. On ne donne pas le diurétique sur ce seul réflexe.", 2),
            P("Position, oxygène, arrêt de la poche. Puis, si le diagnostic tient, Lasix. Œdème pulmonaire aigu : 40 mg intraveineux, puis 20 à 40 mg vingt minutes plus tard si l'état l'exige. "
              "Ce n'est pas la dose de l'enfant. L'enfant de moins de 15 ans : 1 mg par kilogramme, sans dépasser 20 mg dans la journée.", 6),
            P("Grossesse et furosémide. Nécessité absolue, durée brève, surveillance de la croissance. Une femme enceinte dyspnéique après du sang peut être une surcharge, une embolie, un TRALI ou un œdème aigu d'autre cause. "
              "Le diurétique ne se met pas pour couvrir toutes ces cases.", 6),
            P("Cas. Femme de 82 ans, deux concentrés prescrits pour une hémoglobine à 75 g/l, antécédent d'œdème pulmonaire, dyspnée et 180 mm Hg de systolique après le premier concentré, crépitants, radiographie nouvelle. "
              "On arrête le second. Quatre signes sont là ou se cherchent tout de suite : détresse, hypertension, œdème, et le bilan d'entrées. Oxygène. 40 mg de Lasix en intraveineux. Déclaration. "
              "On ne termine pas le deuxième concentré pour atteindre un chiffre d'hémoglobine.", 6),
        ],
        6: [
            P("Jour 3, jour 10, jour 21 : tous sont dans la fenêtre de 1 à 28 jours. Un ictère au jour 30 sort de la définition de l'aide-mémoire. "
              "On ne force pas le nom. On cherche une autre hémolyse. Un ictère au jour 2 est dedans.", 2),
            P("Hémolyse extravasculaire le plus souvent : rate et foie prennent les globules couverts d'anticorps, bilirubine conjuguée ou non selon le moment, hémoglobine qui retombe, fièvre possible, rarement le choc de l'hémolyse intravasculaire. "
              "Kidd peut pourtant lyser dans le vaisseau. Des urines foncées ne font pas sortir de la case retardée si le délai est de plusieurs jours.", 2),
            P("Élution. Le Coombs direct positif dit que quelque chose est collé au globule. L'élution décroche l'anticorps pour le nommer. "
              "Sans élution, on sait qu'il y a un revêtement, on ne sait pas toujours lequel. L'aide-mémoire la demande quand le direct est positif.", 2),
            P("Transfusion suivante. Uniquement des globules négatifs pour l'antigène en cause, compatibilisés. "
              "En urgence vitale, si le nom de l'anticorps n'est pas encore revenu et que l'anémie tue, le concentré O RhD négatif dépanne les antigènes A, B et D, pas Kell ni Kidd. "
              "On le dit à la banque : urgence, réaction retardée suspecte, ne pas rendre un concentré au hasard si un phénotype est possible.", 9),
            P("Cas. Jour 12 après deux concentrés, fatigue, sclères jaunes, hémoglobine 70 g/l alors qu'elle était 95 g/l au sortir de l'hôpital, recherche anti-Jka, Coombs direct positif. "
              "Pas de fièvre à 40 °C, pas de choc. Nom : réaction hémolytique retardée. Déclaration. Pas de furosémide. Pas d'anti-D. "
              "Contrôle de la fonction rénale, parce que l'hémolyse peut la toucher même à distance.", 2),
            P("Ne pas confondre avec l'allo-immunisation du même anticorps sans chute d'hémoglobine. "
              "Si l'hémoglobine tient et qu'il n'y a ni ictère ni marqueur, on reste dans l'allo-immunisation, grade au minimum sévère quand même, mais ce n'est pas une hémolyse.", 1),
        ],
        8: [
            P("Plasma AB vers un receveur O : compatible, le plasma AB n'apporte ni anti-A ni anti-B. "
              "Plasma A vers un receveur B : incompatible, l'anti-B du plasma A vise l'antigène B. "
              "Plasma B vers un receveur A : incompatible pour la même raison, en miroir. "
              "Ces trois phrases se récitent avant de signer une commande de plasma en urgence.", 2),
            P("Plaquettes de groupe O chez un receveur A. Deux risques distincts. Le plasma qui les accompagne peut contenir un anti-A capable d'hémolyser les globules du receveur. "
              "Les plaquettes elles-mêmes portent A ou plutôt ne portent pas A si elles sont O, et le receveur A peut moins bien les garder à cause de son anti-A? "
              "Receveur A a de l'anti-B, pas d'anti-A. Des plaquettes O n'ont pas d'antigène A : l'anti-B du receveur ne les vise pas. "
              "Le danger principal est donc l'anti-A du donneur O dans le plasma de la poche, contre les globules A du receveur. "
              "On ne mélange pas ce danger avec le rendement plaquettaire d'une incompatibilité inverse, receveur O et plaquettes A, où l'anti-A du receveur peut réduire le rendement.", 2),
            P("RhD et plaquettes. Une fille RhD négatif qui reçoit un produit contenant des hématies RhD positif entre dans l'indication de l'information 53609. "
              "La dose suit 10 µg pour 0,5 ml d'hématies, pas un volume de poche inventé. Si le laboratoire ne peut pas dire le volume d'hématies et que l'exposition n'est pas exclue, "
              "on en réfère au spécialiste plutôt que d'écrire un millilitre fictif. La seringue de 300 µg reste la dose standard quand l'information la retient pour une exposition couverte par cette dose.", 4),
            P("Cas de service. Rupture de plasma AB, receveur B, on propose du plasma B, qui est l'isogroupe, ou du plasma AB s'il revient. "
              "On ne propose pas du plasma O. La carte au lit ne se colle pas sur la poche de plasma. La concordance du nom, elle, se fait.", 9),
            P("Hémolyse après plaquettes O chez un receveur A : douleur, chute d'hémoglobine, Coombs direct parfois positif, plasma du donneur en cause. "
              "C'est une réaction hémolytique, bilan en quatre volets, arrêt, déclaration. Ce n'est pas une allergie cutanée. Ce n'est pas une surcharge.", 2),
        ],
        10: [
            P("Heure par heure. Pendant la poche ou jusqu'à la sixième heure : fenêtre du TRALI et de la surcharge. "
              "Au-delà, jusqu'à 24 heures, si la respiration lâche sans rentrer dans TRALI, surcharge ou allergie, l'aide-mémoire ouvre la dyspnée associée à la transfusion. "
              "On ne laisse pas un patient dyspnéique sans nom et sans oxygène pendant qu'on choisit la case.", 2),
            P("Radiographie bilatérale et cœur de taille normale, pas de crépitants massifs d'œdème déclive, tension non élevée : on garde le TRALI en tête. "
              "Radiographie d'œdème, gros cœur ou histoire cardiaque, hypertension : on garde la surcharge. Les deux peuvent se discuter. Le peptide natriurétique aide sans seuil chiffré dans l'aide-mémoire. "
              "On ne retient pas un chiffre de peptide lu ailleurs.", 2),
            P("Facteurs de risque, à cocher sans en oublier. Directs : inhalation, pneumonie, toxique inhalé, contusion, quasi-noyade. "
              "Indirects : sepsis sévère, choc, polytraumatisme, brûlure. "
              "Un patient de cette liste peut quand même avoir un TRALI possible. L'exclure parce qu'il est septique est la copie fausse.", 2),
            P("Donneur. Le laboratoire cherchera des anti-HNA ou anti-HLA, et l'antigène chez le receveur, ou une compatibilité contre les granulocytes. "
              "L'absence d'anticorps laisse ouverte la forme non immunogène, celle des lipides et des substances actives du produit. "
              "On ne classe pas le dossier en erreur de diagnostic parce que le donneur est séronégatif.", 2),
            P("Cas. Jeune homme, traumatisme sans atteinte thoracique, concentré, à la deuxième heure saturation à 85 % à l'air, infiltrats des deux champs, tension 120 mm Hg, pas de signe de surcharge. "
              "Pas de facteur pulmonaire préalable clair : TRALI probable si le reste tient. Oxygène, avis de réanimation, pas de 40 mg de furosémide en ouverture, déclaration, poche gardée pour l'enquête donneurs.", 2),
            P("Ce que l'on dit à l'équipe. Le TRALI ne se prévient pas au lit par un médicament. Il se reconnaît, on arrête le volume, on oxygène, on ne noie pas le poumon avec un remplissage de principe, "
              "et l'on ne le diurèse pas comme un œdème cardiaque. La prévention en amont est le choix des produits et des donneurs, hors de la seringue du service.", 2),
        ],
    }
    out = {4: commun + banques.get(index, []), 14: banques.get(index, [])[:3]}
    if index in banques:
        out[8] = banques[index]
        out[5] = banques[index][:3]
        out[12] = [P("La prévention propre à ce diagnostic est dans la fenêtre de conduite. Elle ne remplace pas les deux contrôles au lit ni la déclaration.", 3)]
    if index == 2:
        out[11] = banques[2]
    if index == 4:
        out[11] = banques[4]
        out[6] = banques[4][:4]
    return out
