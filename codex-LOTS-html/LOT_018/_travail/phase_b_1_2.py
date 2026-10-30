from format_phase_b import Lesson, paras, table, steps

def rediger():
    l=Lesson(1,[9,4])
    l.add('Selon le COUF 2025, une amétropie empêche un œil au repos de focaliser une image nette sur la rétine. Les {notions de réfraction} distinguent myopie, hypermétropie et astigmatisme. La presbytie correspond à une perte d’accommodation liée à l’âge.',
        paras('L’emmétropie correspond à une focalisation sur la rétine sans accommodation pour un objet éloigné. Une myopie focalise en avant de la rétine ; une hypermétropie focalise en arrière si l’accommodation n’intervient pas. Dans l’astigmatisme, la puissance varie selon les méridiens et un point ne forme plus une image ponctuelle.',
              'La presbytie est un trouble de la mise au point de près et peut s’ajouter à toute réfraction de loin. Une anisométropie est une différence de réfraction entre les yeux. L’amblyopie est une réduction de la vision liée au développement visuel : elle ne se confond pas avec une simple erreur de lunettes.'))
    l.add('Les défauts réfractifs touchent tous les âges, avec des {enjeux différents chez l’enfant et l’adulte}. Le COUF 2025 cite une fréquence de myopie de 15 à 20 % dans les populations occidentales. Ce repère ne mesure pas la fréquence des amétropies non corrigées en Suisse.',
        paras('Le chiffre du COUF est un repère de manuel, sans estimation suisse contemporaine distinguant les personnes corrigées et non corrigées. Il ne doit pas servir au classement des dix causes de perte visuelle.',
              'Chez l’enfant, une image défocalisée, surtout asymétrique, peut perturber la maturation visuelle. Chez l’adulte, la correction agit sur lecture, travail et conduite. Une forte myopie expose aussi à des complications rétiniennes indépendantes de la qualité des lunettes ; une baisse nouvelle ne se banalise donc pas.'))
    l.add('La relation entre longueur de l’œil, cornée et cristallin détermine la mise au point. Le {mécanisme optique} explique le choix du verre correcteur. Une amélioration optique ne répare pas une lésion rétinienne associée.',
        paras('La cornée assure une grande part de la convergence ; le cristallin ajuste la focalisation. Lors de l’accommodation, la contraction ciliaire relâche la tension zonulaire et augmente la courbure du cristallin. La presbytie traduit surtout la diminution progressive de cette capacité.',
              'Un allongement axial favorise la myopie ; une modification de l’indice du cristallin peut aussi induire une myopisation. Une myopie récente chez une personne âgée peut donc révéler une cataracte nucléaire.')+
        table(['Perturbation','Exploration','Correction et mécanisme'],[
            ['Foyer en avant de la rétine.','Réfraction objective puis subjective.','Verre divergent, puissance négative : reculer le foyer.'],
            ['Foyer en arrière au repos.','Réfraction, avec cycloplégie si nécessaire.','Verre convergent, puissance positive : avancer le foyer.'],
            ['Puissance différente selon les méridiens.','Mesure du cylindre et de son axe ; topographie si irrégularité.','Correction cylindrique orientée ; prise en charge cornéenne si irrégularité.'],
            ['Accommodation devenue insuffisante.','Acuité de près avec correction de loin adaptée.','Addition positive pour la distance de travail.']]))
    l.add('Une explication réfractive est retenue après exclusion des {alternatives menaçantes}. La soudaineté, la douleur et un déficit du champ imposent une autre démarche. Une correction imparfaite ne suffit pas à expliquer tous les symptômes.',
        table(['Priorité','Ce qui discrimine','Action et piège'],[
            ['🚩 E1 — Ischémie.','Perte brutale ou transitoire, défaut pupillaire ou champ amputé.','Filière urgente ; des lunettes anciennes ne rassurent pas.'],
            ['🚩 E4 — Déchirure ou décollement.','Éclairs, corps flottants récents, rideau.','Fond d’œil périphérique urgent, particulièrement chez le myope.'],
            ['🚩 E5 — Kératite.','Lentilles, douleur, rougeur et photophobie.','Retirer les lentilles et avis urgent ; pas de simple renouvellement de correction.'],
            ['Cataracte ou maculopathie.','Réfraction optimisée sans récupération attendue ; opacité ou déformation des lignes.','Examiner cristallin et macula.']]),[1,2,3,9])
    l.add('L’anamnèse précise distance gênante, ancienneté, correction et contexte de travail. Les {questions discriminantes} recherchent aussi une amblyopie ancienne et des complications de myopie. Chez l’enfant, interroger les proches complète la plainte souvent peu explicite.',
        table(['Question','Raison','Conséquence'],[
            ['De loin, de près ou aux deux distances ?','Les exigences de focalisation diffèrent.','Tester chaque distance.'],
            ['Depuis quand, et avec quelles lunettes ?','Une évolution brutale ne correspond pas à une amétropie stable.','Comparer correction actuelle et mesures antérieures.'],
            ['Un œil a-t-il toujours moins vu ?','Une asymétrie ancienne évoque aussi l’amblyopie.','Rechercher les anciens résultats et un strabisme.'],
            ['Lentilles, douleur, éclairs ou voile ?','Infection et traction rétinienne changent l’urgence.','Adresser sans attendre la seule réfraction.'],
            ['Corticoïdes, diabète ou fluctuation glycémique ?','Le cristallin et la réfraction peuvent varier.','Évaluer le contexte et éviter une prescription sur une fluctuation transitoire.']]))
    l.add('L’examen mesure chaque œil, sans puis avec correction, de loin et de près. La {réfraction contrôlée} recherche la meilleure acuité corrigée. Le reste de l’examen devient déterminant si cette acuité reste insuffisante.',
        table(['Geste','Normal attendu','Anomalie et limite'],[
            ['Occlure un œil sans appuyer et faire lire une échelle à distance calibrée.','Lecture compatible avec l’âge et la correction.','Noter l’acuité de chaque œil ; ne pas déduire la vision monoculaire du résultat binoculaire.'],
            ['Essayer un trou sténopéique.','Peu de changement si la correction est adéquate.','Une amélioration oriente vers une composante optique mais ne pose pas seule le diagnostic.'],
            ['Autoréfractométrie puis choix subjectif de verres.','Mesures cohérentes avec la meilleure lecture.','L’accommodation peut fausser une mesure chez l’enfant ; cycloplégie spécialisée selon le cas.'],
            ['Comparer pupilles, cornée, cristallin et fond d’œil.','Milieux transparents, pas d’anomalie expliquant un déficit.','Un défaut afférent ou une lésion rétinienne impose une autre explication.']]))
    l.add('Le tableau associe des signes fonctionnels et des résultats optiques concordants. Les {syndromes réfractifs} se distinguent des atteintes neurologiques ou maculaires. Une forte myopie associe parfois défaut de focalisation et maladie structurelle.',
        table(['Syndrome','Signes fonctionnels','Signes physiques et recherche'],[
            ['7.1 — Myopique.','Vision de loin floue, souvent meilleure de près.','Réfraction négative ; mesurer la correction puis examiner la rétine si terrain à risque.'],
            ['7.2 — Hypermétropique accommodatif.','Fatigue ou céphalée lors du travail rapproché.','Réfraction positive parfois masquée ; évaluer accommodation et alignement.'],
            ['7.3 — Astigmatique.','Contours dédoublés ou déformés à plusieurs distances.','Cylindre et axe à la réfraction ; topographie si irrégularité suspectée.'],
            ['7.4 — Presbytique.','Besoin d’éloigner le texte.','Amélioration de près avec addition, après correction de loin.']]))
    l.add('Le diagnostic repose sur une erreur de réfraction mesurée et une amélioration cohérente avec sa correction. Les {critères pratiques} incluent l’exclusion d’une affection expliquant le déficit résiduel. Un autoréfractomètre ne remplace pas cette confrontation.',
        paras('Le COUF 2025 décrit une mesure objective complétée par une réfraction subjective. Chez l’enfant ou en cas de forte accommodation, l’ophtalmologue choisit une mesure sous cycloplégie. Il n’existe pas de seuil unique de dioptries qui attribue automatiquement une plainte à l’amétropie.',
              'La meilleure acuité corrigée doit être comparée aux besoins, à l’âge et à l’état antérieur. Si la différence entre les yeux persiste, rechercher amblyopie ou maladie organique. Une forte myopie ne se définit pas uniquement par la plainte de flou : son retentissement rétinien doit être évalué.'))
    l.add('La réfraction est l’exploration centrale. Les {examens complémentaires ciblés} répondent à une discordance ou à une suspicion anatomique. Une imagerie cérébrale n’est pas systématique devant une amétropie isolée.',
        paras('9.a — Référence pratique : réfraction objective et subjective confrontée à l’examen oculaire ; pas de test biologique de confirmation.',
              '9.b — Première intention : acuité séparée de loin et de près, réfraction, examen du segment antérieur et évaluation du fond d’œil selon le contexte.',
              '9.c — Alternatives : méthodes adaptées à l’âge, à la coopération et au handicap ; la cycloplégie se décide après vérification des précautions du produit.',
              '9.d — Seconde intention : topographie si astigmatisme irrégulier, biométrie ou imagerie rétinienne si myopie évolutive ou déficit inexpliqué.')+
        table(['Résultat','Interprétation','Conduite'],[
            ['Correction efficace et examen concordant.','Cause réfractive probable.','Prescrire et vérifier la tolérance.'],
            ['Résultat variable.','Accommodation ou fluctuation des milieux possible.','Recontrôler dans des conditions adaptées.'],
            ['Déficit persistant malgré correction.','Cause réfractive insuffisante.','Explorer amblyopie, cornée, cristallin, rétine ou nerf.']]))
    l.add('L’{arbre de décision} commence par les signes qui changent l’urgence. Il conduit ensuite à la correction et à sa vérification. Une discordance relance le bilan.',
        steps('Si début brutal, douleur, rideau ou déficit du champ → filière urgente décrite dans le cours du symptôme.',
              'Sinon, mesurer chaque œil et réaliser une réfraction adaptée à l’âge.',
              'Si la correction restaure une fonction cohérente et l’examen est rassurant → correction optique et contrôle de tolérance.',
              'Si l’acuité corrigée reste réduite ou asymétrique → rechercher une cause associée ; chez l’enfant, prendre en charge le risque d’amblyopie.'))
    l.add('Le traitement vise une vision utile aux distances nécessaires. Les {modalités de correction et de suivi} reposent d’abord sur les lunettes ou les lentilles adaptées. Une chirurgie réfractive se discute après bilan spécialisé et information sur ses limites.',
        paras('11.A — Objectif : meilleure acuité corrigée et confort binoculaire adaptés au patient, sans promettre la récupération d’une amblyopie ou d’une lésion rétinienne.',
              '11.B — Prescrire une correction sphérique ou cylindrique mesurée, avec addition si nécessaire. Expliquer manipulation et hygiène des lentilles. Chez l’enfant, le traitement de l’amblyopie relève du suivi ophtalmologique et orthoptique ; une correction tardive ne remplace pas la surveillance du développement.',
              'La chirurgie réfractive modifie la puissance optique. Elle n’annule pas les risques rétiniens d’un œil très myope. Évaluer stabilité de la réfraction, cornée et attentes. Grossesse, fluctuation glycémique et maladie cornéenne peuvent modifier le calendrier du bilan.',
              '11.C — Vérifier confort, acuité corrigée et observance ; recontrôler plus tôt chez l’enfant ou si évolution. Une douleur sous lentilles, des éclairs ou un voile imposent une consultation urgente.',
              '11.D — La sortie est ambulatoire si aucune cause urgente n’est suspectée et si le plan de correction et de suivi est clair. Adapter poste de travail et conduite selon les capacités visuelles et les règles suisses applicables ; aucun seuil légal français n’est transposé.'))
    l.add('La prévention vise surtout les conséquences d’une correction insuffisante. Les {mesures selon l’âge} associent dépistage, accès à la correction et protection oculaire. L’éducation du myope doit inclure les signes d’alerte rétinienne.',
        paras('Primaire : informer sur les activités visuelles, les pauses et le temps passé dehors chez l’enfant, sans promettre d’empêcher toute myopie. Aucun protocole chiffré suisse de contrôle de la myopie n’est déduit ici d’une simple correction optique.',
              'Secondaire : mesurer la vision de chaque œil et rechercher un strabisme ou une asymétrie dans le suivi pédiatrique. Ne pas attendre qu’un enfant signale spontanément une mauvaise vision monoculaire.',
              'Tertiaire : adapter les aides et le suivi d’amblyopie ou de myopie pathologique. Une correction bien portée n’exclut pas une complication rétinienne.'))
    l.add('Mesurer chaque œil avant de conclure à une simple erreur de lunettes. Corriger la réfraction puis expliquer tout déficit résiduel. Protéger le développement visuel de l’enfant. Adresser en urgence une baisse brutale chez le myope.')
    l.quiz([
        ('La myopie focalise-t-elle derrière la rétine ?','Non : en avant, pour un objet éloigné et une accommodation relâchée.'),
        ('Quel verre corrige habituellement la myopie ?','Un verre divergent de puissance négative.'),
        ('Quel verre corrige l’hypermétropie ?','Un verre convergent de puissance positive.'),
        ('L’astigmatisme est-il une simple différence entre les deux yeux ?','Non : la puissance varie selon les méridiens d’un même œil.'),
        ('La presbytie est-elle synonyme d’hypermétropie ?','Non : elle correspond à une perte d’accommodation et peut coexister avec toute réfraction.'),
        ('Une mesure binoculaire exclut-elle une mauvaise vision d’un œil ?','Non : chaque œil doit être mesuré séparément.'),
        ('Le trou sténopéique prouve-t-il une amétropie isolée ?','Non : il oriente vers une composante optique mais ne suffit pas.'),
        ('Pourquoi envisager une cycloplégie chez l’enfant ?','Pour limiter l’effet de l’accommodation sur la mesure, dans un cadre spécialisé.'),
        ('Une anisométropie non corrigée peut-elle avoir une conséquence durable ?','Oui : une amblyopie peut se constituer pendant le développement visuel.'),
        ('Une nouvelle myopie chez un adulte âgé est-elle forcément axile ?','Non : une cataracte nucléaire peut modifier la réfraction.'),
        ('La chirurgie réfractive efface-t-elle le risque de décollement du myope ?','Non : elle corrige la puissance optique, pas toutes les anomalies de la rétine.'),
        ('Une douleur chez un porteur de lentilles se traite-t-elle par de nouvelles lunettes seules ?','Non : rechercher notamment une kératite et organiser un avis urgent.'),
        ('Une meilleure acuité corrigée insuffisante clôt-elle le bilan ?','Non : rechercher une cause associée, organique ou développementale.'),
        ('Le chiffre de myopie du COUF donne-t-il la fréquence suisse des amétropies non corrigées ?','Non : la population et le critère mesuré diffèrent.')])
    l.write()

    l=Lesson(2,[10,3])
    l.add('Le COUF 2025 définit la cataracte comme une opacification du cristallin. Les {formes cliniques} expliquent des gênes variables, parfois mal reflétées par une seule mesure d’acuité. Le diagnostic doit être concordant avec la plainte et les autres structures oculaires.',
        paras('Une cataracte nucléaire touche surtout le centre du cristallin et peut induire une myopisation. Une cataracte corticale atteint sa périphérie ; une forme sous-capsulaire postérieure peut gêner fortement par éblouissement ou en vision de près.',
              'La pseudophakie désigne un œil portant un implant après extraction du cristallin ; l’aphaquie son absence sans implant. Une opacification capsulaire postérieure après chirurgie est parfois appelée cataracte secondaire, mais le cristallin retiré ne repousse pas.'))
    l.add('L’âge est la cause principale, mais une cataracte peut aussi être traumatique, métabolique ou médicamenteuse. Les {terrains et l’histoire naturelle} conditionnent le bilan. Aucun taux suisse actuel par sous-type n’a été identifié dans les sources consultées.',
        paras('Une opacité liée à l’âge évolue souvent lentement et peut être bilatérale avec une gêne asymétrique. Le retentissement concerne lecture, éblouissement, conduite et autonomie. Les chiffres d’activité chirurgicale ne sont pas équivalents à une prévalence de cataracte symptomatique.',
              'Un traumatisme, le diabète, une inflammation oculaire ou l’exposition aux corticoïdes orientent vers une cause secondaire. Chez l’enfant, une cataracte congénitale menace le développement visuel ; sa prise en charge est urgente pour prévenir l’amblyopie.'))
    l.add('La désorganisation des protéines cristalliniennes diffuse et absorbe la lumière. Le {lien entre opacité, gêne et chirurgie} explique pourquoi la correction par lunettes peut devenir insuffisante. La chirurgie remplace le milieu optique altéré, mais ne répare pas une rétine malade.',
        paras('Le cristallin transparent focalise la lumière et adapte sa puissance. Une modification de sa structure altère transparence, contraste et parfois réfraction. L’éblouissement peut être important même quand l’acuité mesurée dans une pièce calme reste assez bonne.')+
        table(['Lésion','Exploration','Traitement et mécanisme'],[
            ['Opacité nucléaire, corticale ou sous-capsulaire.','Lampe à fente, après dilatation adaptée.','Extraction du cristallin opaque et implantation.'],
            ['Modification de la réfraction.','Réfraction et meilleure acuité corrigée.','Correction temporaire possible ; elle n’élimine pas l’opacité.'],
            ['Opacification capsulaire après chirurgie.','Examen de la capsule chez un patient pseudophaque.','Capsulotomie laser si indiquée, après exclusion d’une autre cause.'],
            ['Lésion maculaire associée.','Fond d’œil et OCT selon la suspicion.','Traitement propre à la macula ; pronostic de la chirurgie à réévaluer.']]))
    l.add('Une cataracte connue ne doit pas masquer une urgence. Les {diagnostics à exclure} dépendent surtout du délai et des symptômes associés. Une baisse sévère disproportionnée à l’opacité doit être expliquée.',
        table(['Alternative','Signe ou examen discriminant','Conduite'],[
            ['🚩 E1 — Ischémie.','Perte soudaine ou transitoire.','Évaluation vasculaire urgente.'],
            ['🚩 E3 — Fermeture d’angle.','Douleur, halos, nausées et hypertonie instrumentale.','Avis immédiat ; cataracte intumescente parfois impliquée.'],
            ['🚩 E5 — Endophtalmie postopératoire.','Baisse avec douleur, rougeur ou hypopion après chirurgie.','Urgence ophtalmologique ; ne pas attendre le contrôle programmé.'],
            ['Maculopathie.','Métamorphopsies et lésion à l’OCT.','Évaluer la macula et le pronostic avant d’attribuer toute la plainte au cristallin.']]),[1,2,10])
    l.add('L’interrogatoire décrit la gêne dans les activités réellement importantes pour le patient. Les {questions préopératoires} recherchent aussi les facteurs de complication. Une décision chirurgicale se partage sur le bénéfice attendu.',
        table(['Question','Pourquoi elle compte'],[
            ['Éblouissement, conduite nocturne, lecture, diplopie d’un seul œil ?','Ces symptômes caractérisent le retentissement optique.'],
            ['Début lent ou changement soudain ?','Une aggravation soudaine impose une autre recherche.'],
            ['Traumatisme, corticoïdes, diabète, uvéite ?','Ils orientent l’étiologie et le risque opératoire.'],
            ['Antécédent rétinien ou chirurgical, traitements urologiques ?','Ils influencent le pronostic et la préparation de la chirurgie ; transmettre la liste complète à l’opérateur.'],
            ['Objectifs de vision, aides et possibilité de suivre les soins ?','Le choix de l’implant et l’organisation postopératoire doivent être réalistes.']]))
    l.add('La lampe à fente montre l’opacité, tandis que la réfraction précise sa conséquence fonctionnelle. L’{examen avant chirurgie} recherche aussi les autres causes de baisse. Il faut examiner chaque œil et décrire les limites d’un fond d’œil masqué.',
        table(['Geste','Normal puis pathologique','Conséquence'],[
            ['Mesurer loin, près et correction.','Acuité adaptée puis baisse non totalement corrigible.','Confronter au retentissement quotidien.'],
            ['Examiner le cristallin à la lampe à fente.','Milieu transparent puis opacités localisées ou diffuses.','Décrire leur type et leur concordance avec la gêne.'],
            ['Évaluer cornée, pupille et pression.','Surface et segment antérieur sans anomalie significative.','Repérer dystrophie, inflammation ou risque de glaucome.'],
            ['Examiner macula et périphérie si visibles.','Absence de lésion expliquant le déficit.','Une pathologie associée modifie le pronostic ; si la rétine n’est pas visible, adapter les explorations.']]))
    l.add('La cataracte habituelle produit un syndrome optique progressif et indolore. Les {présentations syndromiques} aident à reconnaître les situations atypiques. Douleur et rougeur demandent une explication supplémentaire.',
        table(['Syndrome','Signes fonctionnels','Constat physique et mécanisme'],[
            ['7.1 — Opacité progressive.','Flou, contraste réduit, éblouissement.','Opacité cristallinienne diffusant la lumière.'],
            ['7.2 — Myopisation nucléaire.','Changement de lunettes, amélioration relative de près.','Modification de l’indice du cristallin ; réfraction et lampe à fente concordantes.'],
            ['7.3 — Cataracte compliquée.','Douleur, rougeur ou baisse rapide.','Inflammation ou hypertonie à rechercher en urgence.'],
            ['7.4 — Baisse chez le pseudophaque.','Reprise du flou après amélioration opératoire.','Examiner capsule, macula et rétine ; ne pas conclure d’emblée à une opacification capsulaire.']]))
    l.add('Le diagnostic positif est clinique, par visualisation du cristallin opacifié. Les {critères de pertinence} associent cette lésion à une gêne compatible. Aucun seuil unique d’acuité ne décide à lui seul de l’opération.',
        paras('Le COUF 2025 retient la gêne fonctionnelle, l’obstacle à l’examen ou au traitement du fond d’œil, et les complications de la cataracte parmi les situations où la chirurgie se discute.',
              'La densité de l’opacité ne prédit pas seule le bénéfice : la cornée, la macula et le nerf optique comptent. La cataracte congénitale constitue un contexte différent où le développement de la vision impose un calendrier spécialisé.'))
    l.add('L’examen clinique établit le diagnostic ; la biométrie prépare la chirurgie. Les {explorations utiles} sont choisies selon les questions restantes. Un examen systématique non pertinent peut retarder le traitement sans améliorer le diagnostic.',
        paras('9.a — Référence diagnostique : examen du cristallin à la lampe à fente, confronté à la vision et à la réfraction.',
              '9.b — Avant opération : biométrie et kératométrie pour calculer l’implant ; documenter les antécédents réfractifs et les attentes.',
              '9.c — Si le fond d’œil est inaccessible : échographie oculaire pour rechercher notamment une lésion postérieure, selon l’évaluation spécialisée. Les méthodes de mesure s’adaptent à la coopération.',
              '9.d — OCT maculaire ou topographie cornéenne si le contexte ou la discordance le justifie.')+
        table(['Résultat','Signification','Action'],[
            ['Opacité concordante, rétine évaluée.','Bénéfice optique envisageable.','Discussion de chirurgie.'],
            ['Anomalie maculaire associée.','Potentiel de récupération différent.','Traiter ou intégrer au consentement.'],
            ['Mesures biométriques discordantes.','Risque d’erreur de puissance d’implant.','Recontrôler avant intervention.']]))
    l.add('L’{algorithme de décision} distingue l’urgence, l’évaluation du bénéfice et la préparation opératoire. Le choix de l’implant tient compte des activités et des autres maladies. Le suivi reste nécessaire après une amélioration initiale.',
        steps('Si baisse brutale, œil douloureux ou rouge → rechercher une autre cause urgente ou une complication.',
              'Si baisse progressive → mesurer la meilleure acuité et examiner le cristallin puis le segment postérieur.',
              'Si gêne concordante significative, fond d’œil inaccessible ou complication cristallinienne → discuter la chirurgie.',
              'Si chirurgie retenue → biométrie, choix de l’implant, information et organisation du suivi.',
              'Après chirurgie, si douleur ou baisse nouvelle → avis urgent plutôt qu’attente du rendez-vous.'))
    l.add('Le traitement curatif est chirurgical. Les {étapes de prise en charge} vont de l’évaluation du bénéfice à la surveillance des complications. Il faut donner au patient un contact et des consignes de retour explicites.',
        paras('11.A — Viser la fonction souhaitée et un résultat réaliste compte tenu de l’état rétinien et neurologique. Aucun collyre n’est présenté ici comme dissolvant la cataracte.',
              '11.B — L’extraction par phacoémulsification fragmente et retire le cristallin, puis un implant remplace sa puissance. Un implant monofocal ne restaure pas l’accommodation ; les options toriques ou multifocales répondent à des indications et compromis spécifiques. La chirurgie est souvent ambulatoire et sous anesthésie locale.',
              'Le chirurgien prescrit la prévention infectieuse et le traitement postopératoire de la formulation choisie. Aucun dosage français de collyre n’est transposé ici en ordonnance suisse. Une cataracte pédiatrique demande une équipe spécialisée et une prise en charge de l’amblyopie.',
              '11.C — Contrôler acuité, cornée, inflammation et pression selon le calendrier opératoire. Douleur croissante, rougeur ou baisse de vision doivent être signalées immédiatement. Les complications comprennent infection, œdème maculaire, décollement rétinien et opacification capsulaire.',
              '11.D — Avant sortie : consignes comprises, traitements disponibles, rendez-vous fixé et transport organisé. La récupération dépend des autres structures. Une opacification capsulaire ultérieure peut relever d’une capsulotomie, après confirmation de sa responsabilité.'))
    l.add('Il n’existe pas de prévention médicamenteuse démontrée de la cataracte liée à l’âge dans les sources retenues. Les {mesures préventives} ciblent les facteurs évitables et les complications. Le dépistage pédiatrique garde une priorité propre.',
        paras('Primaire : prévenir les traumatismes et éviter une exposition injustifiée aux corticoïdes, sans arrêter un traitement nécessaire sans son prescripteur.',
              'Secondaire : évaluer une gêne fonctionnelle et rechercher précocement une leucocorie chez l’enfant ; une anomalie du reflet pupillaire demande un avis spécialisé rapide.',
              'Tertiaire : organiser soins postopératoires et aides visuelles, expliquer les alertes et vérifier la correction finale. La surveillance rétinienne reste nécessaire si une autre maladie existe.'))
    l.add('Une cataracte visible doit expliquer la gêne pour être tenue responsable. L’indication opératoire dépend du patient et de l’examen. La chirurgie ne répare pas une maculopathie associée. Une baisse douloureuse après opération est une urgence.')
    l.quiz([
        ('La cataracte touche-t-elle la rétine ?','Non : elle opacifie le cristallin ; une maladie rétinienne peut coexister.'),
        ('Une cataracte nucléaire peut-elle modifier les lunettes ?','Oui : elle peut entraîner une myopisation.'),
        ('Une bonne acuité mesurée exclut-elle toute gêne ?','Non : éblouissement et baisse de contraste peuvent être importants.'),
        ('Une cataracte ordinaire est-elle douloureuse ?','Habituellement non ; rechercher une complication ou une autre cause.'),
        ('Quel examen montre directement l’opacité ?','La lampe à fente.'),
        ('Faut-il vérifier la macula avant d’annoncer le résultat ?','Oui : son état influence le bénéfice attendu.'),
        ('Existe-t-il un seuil universel d’acuité imposant la chirurgie ?','Non : la gêne, les besoins et les autres indications comptent.'),
        ('À quoi sert la biométrie ?','Au calcul de la puissance de l’implant.'),
        ('Un implant monofocal rétablit-il l’accommodation ?','Non ; une correction de près peut rester nécessaire.'),
        ('La cataracte secondaire signifie-t-elle que le cristallin repousse ?','Non : il s’agit souvent d’une opacification de la capsule postérieure.'),
        ('Une baisse douloureuse après chirurgie peut-elle attendre un mois ?','Non : rechercher une complication urgente, notamment une endophtalmie.'),
        ('Une cataracte congénitale peut-elle attendre la plainte de l’enfant ?','Non : l’amblyopie menace le développement visuel.'),
        ('Que faire si le fond d’œil est masqué ?','Adapter l’exploration spécialisée, notamment par échographie si indiquée.'),
        ('Un collyre peut-il remplacer la chirurgie d’une cataracte symptomatique ?','Aucun traitement curatif de ce type n’est établi dans les sources retenues.')])
    l.write()

if __name__=='__main__': rediger()
