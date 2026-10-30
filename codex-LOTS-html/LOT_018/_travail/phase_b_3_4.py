from format_phase_b import Lesson, paras, table, steps, ref
from medicaments_phase_b import eylea, xalatan

def rediger():
    l=Lesson(3,[12,25])
    l.add('La DMLA est une affection de la macula liée au vieillissement, décrite par le COUF 2025. Les {stades et formes} distinguent maculopathie débutante, atrophie et néovascularisation. Une déformation récente des lignes demande une évaluation rapide.',
        paras('Les drusen sont des dépôts associés aux stades précoces ; leur présence ne signifie pas à elle seule une forme néovasculaire active. Les formes avancées comportent atrophie des tissus rétiniens externes ou néovaisseaux avec fuite ou hémorragie.',
              'Un scotome central correspond à une zone centrale manquante du champ. Les métamorphopsies sont des déformations des objets ou des lignes. Elles orientent vers la macula, mais ne sont pas spécifiques de la DMLA : membrane, trou ou œdème maculaire peuvent aussi les produire.'))
    l.add('Le risque augmente fortement avec l’âge et le tabagisme. Les {données européennes} doivent distinguer les formes précoces des formes avancées. Aucun chiffre ne doit être transposé à toutes les consultations suisses pour baisse visuelle.',
        paras('Le COUF rapporte une méta-analyse européenne de 2017 : prévalence des formes avancées d’environ 0,1 % entre 55 et 59 ans et 10 % après 85 ans. Ces valeurs décrivent des groupes d’âge et un périmètre diagnostique précis, pas une incidence annuelle.',
              'L’évolution peut être bilatérale mais asymétrique. Une atrophie progresse souvent lentement ; une complication néovasculaire peut produire une baisse plus rapide. Le retentissement porte sur lecture, reconnaissance des visages, autonomie et besoin d’aide, même si la périphérie du champ reste utile.'))
    l.add('La macula assure la vision fine et centrale. Les {mécanismes de l’atteinte maculaire} associent dysfonction de l’épithélium pigmentaire, atteinte des photorécepteurs et parfois néovaisseaux. Le traitement dépend de la lésion présente.',
        paras('Les photorécepteurs externes dépendent de l’épithélium pigmentaire et de la choroïde pour leurs échanges. L’altération de cet ensemble peut entraîner une atrophie. Des facteurs proangiogéniques favorisent aussi des vaisseaux anormaux dont la fuite déforme l’architecture maculaire.')+
        table(['Lésion','Examen','Stratégie et mécanisme'],[
            ['Drusen et anomalies pigmentaires.','Fond d’œil et OCT.','Surveillance et réduction des risques ; ne pas injecter pour le seul mot drusen.'],
            ['Néovaisseaux actifs avec liquide ou hémorragie.','OCT, fond d’œil, angiographie selon besoin.','Anti-VEGF : réduire la fuite et l’activité angiogénique.'],
            ['Atrophie centrale.','Fond d’œil, OCT et autres images selon le bilan.','Réadaptation et évaluation spécialisée ; un anti-VEGF ne restaure pas le tissu détruit.'],
            ['Déficit fonctionnel durable.','Lecture, acuité corrigée et besoins quotidiens.','Aides visuelles et rééducation utilisant la vision restante.']]))
    l.add('Une baisse centrale nouvelle impose de chercher une complication traitable. Les {alternatives urgentes et fréquentes} se distinguent par le mode d’installation et l’imagerie. Une DMLA connue n’explique pas automatiquement tout nouveau déficit.',
        table(['Diagnostic','Discriminant','Conduite'],[
            ['🚩 E1 — Occlusion artérielle.','Perte brutale, déficit afférent, aspect ischémique.','Filière vasculaire immédiate.'],
            ['🚩 E4 — Décollement.','Éclairs et ombre périphérique, rétine soulevée.','Examen périphérique urgent.'],
            ['Membrane ou trou maculaire.','Métamorphopsies et aspect structurel à l’OCT.','Avis rétinien adapté ; pas d’anti-VEGF empirique.'],
            ['Œdème diabétique ou veineux.','Terrain et lésions vasculaires du fond d’œil.','Traiter le mécanisme propre, avec schéma spécifique.']]),[2,12])
    l.add('L’interrogatoire recherche une modification récente par rapport à l’état habituel. Les {questions de suivi} précisent aussi les injections antérieures et la capacité à revenir. Une gêne découverte en couvrant le meilleur œil peut être ancienne.',
        table(['Question','Décision éclairée'],[
            ['Lignes déformées, tache centrale ou changement récent ?','Rechercher une néovascularisation active sans attendre la prochaine visite.'],
            ['Un œil ou les deux, testé séparément ?','Une compensation binoculaire peut masquer la dégradation.'],
            ['Injections précédentes, dernier contrôle et réponse ?','Distinguer activité récidivante, séquelle et rupture de suivi.'],
            ['Douleur ou rougeur après injection ?','Suspecter une complication infectieuse ou inflammatoire urgente.'],
            ['Tabac, autonomie et aide au transport ?','Réduire les risques et rendre le suivi réellement possible.']]))
    l.add('L’examen évalue chaque œil et la macula. La {recherche d’un syndrome maculaire} associe acuité, grille de lecture et fond d’œil. Un test de dépistage normal ne suffit pas à exclure une activité néovasculaire.',
        table(['Geste','Normal','Pathologique et limite'],[
            ['Mesurer l’acuité corrigée.','Performance stable par rapport à l’état antérieur.','Baisse centrale à confronter à l’imagerie.'],
            ['Faire fixer le centre d’une grille, un œil couvert.','Lignes droites et continues.','Ondulations ou zones manquantes ; test subjectif non suffisant pour exclure la maladie.'],
            ['Fond d’œil après dilatation adaptée.','Macula sans saignement, exsudation ni atrophie significative.','Drusen, remaniements pigmentaires, hémorragie ou atrophie.'],
            ['OCT avec comparaison aux examens précédents.','Architecture fovéale sans nouveau liquide.','Liquide, décollement de l’épithélium ou atrophie à interpréter selon la forme.']]))
    l.add('Les {syndromes maculaires} précisent le mécanisme de la baisse. Les signes fonctionnels et l’anatomie doivent être concordants. Une forme avancée peut associer plusieurs lésions.',
        table(['Syndrome','Fonctionnel','Physique et mécanisme'],[
            ['7.1 — Précoce.','Souvent peu de symptômes.','Drusen et anomalies pigmentaires au fond d’œil/OCT.'],
            ['7.2 — Néovasculaire actif.','Métamorphopsies ou baisse récente.','Liquide ou hémorragie par fuite des néovaisseaux.'],
            ['7.3 — Atrophique.','Difficulté progressive de lecture et scotome central.','Perte tissulaire à l’OCT et au fond d’œil.'],
            ['7.4 — Séquellaire.','Déficit persistant malgré réduction du liquide.','Fibrose ou atrophie ; l’anatomie asséchée ne garantit pas la récupération.']]))
    l.add('Le diagnostic associe âge, lésions maculaires et imagerie compatible. Les {critères de forme et d’activité} déterminent l’indication thérapeutique. Une néovascularisation doit être distinguée d’une atrophie isolée.',
        paras('Le COUF 2025 distingue les stades précoces et les formes avancées atrophiques ou néovasculaires. La présence de liquide intra- ou sous-rétinien, d’une hémorragie ou d’autres signes d’activité se confronte aux images antérieures et au contexte.',
              'L’OCT structurel est central pour le suivi ; l’OCT-angiographie montre un réseau vasculaire mais ne mesure pas directement sa fuite. Une angiographie peut préciser le type de lésion ou une discordance. Aucun score clinique seul ne remplace cette analyse.'))
    l.add('Les {explorations maculaires} cherchent la lésion qui peut être traitée. L’OCT est privilégié pour documenter l’anatomie et suivre la réponse. Les examens avec injection ne sont pas systématiques à chaque contrôle.',
        paras('9.a — Il n’existe pas un examen unique suffisant pour toutes les formes : fond d’œil et imagerie multimodale établissent le diagnostic et l’activité.',
              '9.b — Première intention : acuité corrigée, fond d’œil et OCT maculaire des deux yeux.',
              '9.c — L’OCT-angiographie évite l’injection mais présente des artefacts et ne montre pas la fuite. Toute angiographie avec colorant nécessite une évaluation des antécédents et des précautions du produit.',
              '9.d — Angiographie à la fluorescéine ou au vert d’indocyanine selon lésion suspectée, réponse insuffisante ou doute diagnostique.')+
        table(['Résultat','Interprétation','Conduite'],[
            ['Nouveau liquide ou saignement compatible.','Activité possiblement traitable.','Avis rétinien rapide et décision d’anti-VEGF.'],
            ['Atrophie sans activité néovasculaire.','Mécanisme dégénératif.','Réadaptation, surveillance et discussion spécialisée.'],
            ['Baisse sans modification explicative.','Discordance.','Rechercher autre atteinte maculaire, cristallinienne ou neurologique.']]))
    l.add('L’{arbre maculaire} donne priorité à l’apparition récente de symptômes. Le traitement dépend de l’activité et de la forme. Une stabilité apparente n’autorise pas à abandonner le suivi.',
        steps('Si perte brutale atypique, douleur ou signe périphérique → rechercher l’urgence correspondante.',
              'Si métamorphopsies récentes ou baisse centrale → fond d’œil et OCT rapides.',
              'Si néovascularisation active compatible → traitement rétinien selon spécialité et indication.',
              'Si atrophie ou cicatrice sans activité → réadaptation et suivi, sans injection anti-VEGF automatique.',
              'Si réponse insuffisante → vérifier diagnostic, activité, observance du calendrier et lésions irréversibles.'))
    med=eylea(l,'dmla')
    l.add('Une forme néovasculaire active demande une prise en charge rapide. Les {moyens thérapeutiques et leur surveillance} visent à contrôler l’exsudation et à préserver la fonction. L’atrophie et les besoins d’autonomie demandent une stratégie complémentaire.',
        paras('11.A — Préserver ou améliorer la vision utile et limiter les lésions exsudatives ; ne pas promettre la disparition de toute dégénérescence.',
              '11.B — L’ophtalmologue choisit la spécialité anti-VEGF et son rythme. Exemple suisse détaillé : '+med+'. Les intervalles d’une formulation ou d’une indication ne se copient pas sur une autre.',
              'La supplémentation de type AREDS2 se discute pour des stades sélectionnés à risque de progression, sans la présenter comme prévention universelle ou traitement de l’exsudation. NICE souligne les limites des preuves et le risque de cancer pulmonaire associé au bêta-carotène chez les fumeurs. Aucun dosage de complément n’est prescrit ici sans formulation suisse vérifiée.'+ref(12,29),
              'Pour l’atrophie, proposer aides visuelles et réadaptation. Le statut suisse actuel d’une éventuelle thérapie du complément doit être vérifié avant de la proposer ; une autorisation dans un autre pays ne suffit pas.',
              '11.C — Contrôler acuité et morphologie à chaque traitement ; adapter l’intervalle à l’activité selon l’AIPS. Faire tester séparément chaque œil au domicile et signaler toute modification, sans substituer cette auto-observation au suivi.',
              '11.D — Avant retour : consignes d’alerte comprises, prochain rendez-vous et transport organisés. Le pronostic dépend de la précocité, de l’activité et du tissu restant. Les aides de lecture, l’éclairage et le soutien social restent utiles malgré le traitement.'))
    l.add('La prévention associe arrêt du tabac, surveillance et réadaptation. Les {mesures aux trois niveaux} doivent s’adapter au stade. La surveillance de l’autre œil est essentielle.',
        paras('Primaire : aider à l’arrêt du tabac et encourager une alimentation équilibrée. Ne pas promettre de supprimer une susceptibilité liée à l’âge ou à la génétique.',
              'Secondaire : reconnaître rapidement métamorphopsies et scotome nouveaux ; organiser les contrôles prescrits et l’évaluation de l’œil opposé.',
              'Tertiaire : rééducation basse vision, aides optiques ou électroniques, aménagement des activités et prévention de l’isolement. Le traitement ne doit pas faire oublier le handicap résiduel.'))
    l.add('Une déformation récente des lignes demande un examen rapide. Distinguer activité néovasculaire, atrophie et cicatrice. Respecter le schéma de la formulation anti-VEGF choisie. Surveiller l’autre œil et l’autonomie.')
    l.quiz([
        ('Les drusen prouvent-ils une néovascularisation active ?','Non : ils peuvent appartenir à une maculopathie précoce.'),
        ('Les métamorphopsies sont-elles spécifiques de la DMLA ?','Non : d’autres maladies maculaires déforment les lignes.'),
        ('Une grille normale exclut-elle une lésion active ?','Non : elle ne remplace pas le fond d’œil et l’imagerie.'),
        ('Quel examen structurel suit le liquide maculaire ?','L’OCT, confronté à la vision et au fond d’œil.'),
        ('L’OCT-angiographie mesure-t-elle directement la fuite ?','Non : elle montre la vascularisation avec ses limites et artefacts.'),
        ('Un anti-VEGF reconstruit-il les photorécepteurs détruits ?','Non : il agit surtout sur l’activité angiogénique et la fuite.'),
        ('Le même rythme d’Eylea convient-il à toutes les indications ?','Non : lire la posologie de la formulation et de l’indication exactes.'),
        ('Doit-on injecter tout le contenu de la seringue préremplie ?','Non : elle contient un excédent à éliminer selon les instructions.'),
        ('Une infection oculaire permet-elle une injection programmée ?','Non : elle figure parmi les contre-indications AIPS.'),
        ('Une douleur après injection peut-elle attendre la visite suivante ?','Non : rechercher immédiatement une complication, notamment une endophtalmie.'),
        ('Les anti-VEGF sont-ils utilisés sans réserve pendant la grossesse ?','Non : lire et respecter l’information suisse ; Eylea y est contre-indiqué.'),
        ('Une atrophie justifie-t-elle automatiquement un anti-VEGF ?','Non : rechercher une activité néovasculaire associée.'),
        ('Une supplémentation remplace-t-elle le traitement d’une forme exsudative ?','Non : ses indications et son objectif diffèrent.'),
        ('Une vision centrale réduite exclut-elle tout bénéfice de réadaptation ?','Non : les aides utilisent les capacités restantes et les besoins du patient.')])
    l.write()

    l=Lesson(4,[11,22,24])
    l.add('L’EGS, 6e édition 2025, décrit le GPAO comme une neuropathie optique progressive avec angle ouvert. Les {distinctions diagnostiques} séparent glaucome, hypertonie et simple suspicion. La pression seule ne définit pas la maladie.',
        paras('Le glaucome atteint l’anneau neurorétinien et les fibres nerveuses, avec des déficits fonctionnels correspondants. Le caractère primitif suppose l’absence de cause secondaire identifiée.',
              'L’hypertonie oculaire est une pression élevée sans dommage glaucomateux démontré. Un sujet suspect présente des éléments insuffisants pour conclure. Un glaucome à pression dans la norme statistique reste possible : l’évaluation structurelle et fonctionnelle est décisive.'))
    l.add('La fréquence augmente avec l’âge, les antécédents familiaux et certains terrains. Les {repères épidémiologiques} ne remplacent pas l’examen individuel. Le début peu symptomatique explique l’intérêt du diagnostic précoce.',
        paras('Le COUF 2025 rapporte pour le GPAO environ 0,5 à 1 % des adultes de plus de 40 ans en Europe et en Amérique du Nord. La fréquence varie fortement avec l’âge et les définitions ; aucun taux suisse actuel directement comparable n’est fourni ici.',
              'Les antécédents familiaux, une pression élevée et la myopie augmentent le risque. L’histoire naturelle est celle d’une perte progressive irréversible, parfois tardivement ressentie parce que la vision centrale et l’autre œil compensent. La maladie impose un suivi durable.'))
    l.add('La perte des cellules ganglionnaires réduit progressivement le champ visuel. Le {mécanisme de pression et de vulnérabilité nerveuse} relie examen et traitement. Abaisser la pression protège le nerf même dans certains glaucomes à pression normale.',
        paras('L’humeur aqueuse est produite par le corps ciliaire, passe vers la chambre antérieure puis s’évacue notamment par le trabéculum. L’augmentation de la résistance à l’écoulement favorise l’hypertonie. La vulnérabilité axonale et le niveau de pression se combinent ; une valeur statistiquement normale ne garantit pas une sécurité pour chaque nerf.')+
        table(['Perturbation','Exploration','Stratégie'],[
            ['Résistance accrue à l’évacuation.','Tonométrie et gonioscopie.','Laser trabéculaire ou traitement augmentant l’évacuation.'],
            ['Pression trop élevée pour le nerf concerné.','Mesures répétées confrontées à l’évolution.','Réduire la production ou augmenter la sortie ; objectif individuel.'],
            ['Perte de fibres et d’anneau.','Examen papillaire et OCT.','Prévenir la progression ; les fibres perdues ne sont pas restaurées.'],
            ['Déficit fonctionnel.','Périmétrie répétée fiable.','Adapter l’intensité du traitement à la vitesse de progression.']]))
    l.add('La démarche exclut les {causes urgentes ou secondaires} avant de conclure à un GPAO. Une perte rapide ou une pâleur disproportionnée demande une autre explication. L’aspect de la papille se juge avec l’ensemble du bilan.',
        table(['Alternative','Discriminant','Action'],[
            ['🚩 E3 — Fermeture aiguë d’angle.','Douleur, rougeur, halos et angle fermé.','Prise en charge immédiate ; ce n’est pas un GPAO habituel.'],
            ['🚩 Neuropathie ischémique ou compressive.','Installation brutale, dyschromatopsie ou pâleur atypique.','Bilan orienté urgent ; imagerie selon les signes.'],
            ['Glaucome secondaire.','Corticoïdes, pseudoexfoliation, pigment, inflammation ou traumatisme.','Identifier et traiter le mécanisme.'],
            ['Excavation physiologique.','Morphologie stable sans déficit cohérent.','Comparer taille papillaire, imagerie et champ avant d’étiqueter.']]),[1,11,22])
    l.add('L’anamnèse recherche risque familial, traitements et évolution visuelle. Les {questions qui orientent le suivi} évaluent aussi la capacité à instiller les gouttes. L’absence de plainte n’exclut pas la progression.',
        table(['Question','Raison et conséquence'],[
            ['Glaucome dans la famille, myopie, ancien niveau de pression ?','Évaluer le risque et rechercher les mesures antérieures.'],
            ['Corticoïdes par toute voie, traumatisme ou uvéite ?','Rechercher une cause secondaire.'],
            ['Difficulté nocturne, heurts latéraux ou lecture préservée ?','Le déficit du champ peut précéder la baisse centrale.'],
            ['Gouttes réellement prises, gêne locale ou difficulté manuelle ?','Vérifier observance et technique avant d’escalader.'],
            ['Douleur ou baisse soudaine ?','Rechercher une urgence distincte.']]))
    l.add('L’examen associe pression, angle et nerf optique. Les {gestes discriminants} évitent de réduire le diagnostic à la tonométrie. La cornée et la qualité des mesures influencent leur interprétation.',
        table(['Geste','Normal','Anomalie et limite'],[
            ['Tonométrie instrumentale et pachymétrie.','Mesure interprétée selon cornée et contexte.','Une valeur élevée est un facteur de risque ; ne pas appliquer une correction numérique universelle.'],
            ['Gonioscopie.','Angle ouvert sans cause secondaire visible.','Un angle fermé ou un matériel anormal modifie le diagnostic.'],
            ['Examen stéréoscopique papillaire.','Anneau conservé, aspect compatible avec la taille de la papille.','Amincissement focal, hémorragie ou asymétrie suspecte.'],
            ['Périmétrie et OCT.','Fonction et structure cohérentes et stables.','Déficits concordants ; contrôler fiabilité, segmentation et artefacts de myopie.']]))
    l.add('Les {présentations structurelles et fonctionnelles} décrivent le stade et le risque. Les symptômes peuvent rester modestes malgré une atteinte importante. Une présentation atypique impose de revoir l’étiologie.',
        table(['Syndrome','Fonctionnel','Physique et mécanisme'],[
            ['7.1 — Suspect ou prépérimétrique.','Souvent aucune gêne.','Papille ou fibres suspectes ; répéter et confronter les examens.'],
            ['7.2 — Glaucome établi.','Déficit périphérique parfois non perçu.','Perte d’anneau/fibres et défaut périmétrique correspondant.'],
            ['7.3 — Forme avancée.','Gêne fonctionnelle et menace centrale.','Champ très réduit ; besoin de traitement intensif et de réadaptation.'],
            ['7.4 — Présentation discordante.','Baisse centrale ou couleurs disproportionnées.','Pâleur ou champ atypique ; rechercher une autre neuropathie.']]))
    l.add('Le diagnostic exige une neuropathie compatible avec un angle ouvert et l’exclusion des causes secondaires. Les {critères de concordance} reposent sur la structure et la fonction. Une pression supérieure à 21 mmHg attire l’attention mais ne suffit pas.',
        paras('Le COUF et l’EGS insistent sur l’examen papillaire, la périmétrie et l’évaluation de l’angle. L’OCT complète l’examen ; une couleur anormale dans sa base normative n’est pas un diagnostic à elle seule.',
              'Vérifier répétabilité et progression lorsque le bilan est incertain. Une hypertonie sans lésion ne se confond pas avec un glaucome, et le choix de traiter dépend du risque de perte fonctionnelle au cours de la vie.'))
    l.add('Les {explorations de référence} établissent un point de départ puis une tendance. La périmétrie mesure la fonction que le traitement cherche à préserver. Aucun examen isolé ne remplace les autres.',
        paras('9.a — Pas de gold standard unique : confrontation clinique, pression, gonioscopie, structure et fonction.',
              '9.b — Première intention : tonométrie, pachymétrie, papille documentée, périmétrie et OCT des fibres et cellules ganglionnaires.',
              '9.c — Adapter le champ visuel aux capacités du patient et vérifier les indices de fiabilité. L’OCT ne remplace pas la périmétrie, notamment pour quantifier le handicap.',
              '9.d — Répéter pour estimer la progression ; envisager un bilan neuro-ophtalmologique si le tableau est atypique.')+
        table(['Résultat','Interprétation','Action'],[
            ['Pression élevée sans dommage.','Hypertonie ou suspicion.','Évaluer risque et suivi, pas d’étiquette automatique.'],
            ['Progression malgré pression jugée correcte.','Objectif peut-être insuffisant ou mesures non représentatives.','Vérifier traitement et abaisser l’objectif selon le spécialiste.'],
            ['Champ peu fiable ou OCT artefacté.','Conclusion incertaine.','Recontrôler avant décision définitive.']]))
    l.add('L’{algorithme du GPAO} distingue diagnostic, objectif et progression. Le choix initial peut être un laser sélectif ou un traitement local. Une forme avancée peut nécessiter une chirurgie précoce.',
        steps('Si œil rouge douloureux ou déficit rapide → écarter fermeture d’angle et neuropathie aiguë.',
              'Si neuropathie suspecte → confirmer angle ouvert, structure, fonction et absence de cause secondaire.',
              'Si glaucome confirmé → fixer une pression cible individuelle, proposer laser sélectif ou médicament selon situation.',
              'Si contrôle insuffisant → vérifier technique, observance et tolérance, puis intensifier.',
              'Si progression ou forme avancée → réévaluer la cible et discuter une option chirurgicale.'))
    med=xalatan(l)
    l.add('Le traitement vise à préserver le champ visuel pendant la vie du patient. Les {options et objectifs de surveillance} sont individualisés. L’EGS permet de proposer la trabéculoplastie laser comme premier choix dans un angle ouvert adapté.',
        paras('11.A — Fixer une pression cible selon stade, pression initiale, âge, espérance de vie et vitesse de progression. Une valeur universelle de pression normale ne remplace pas cet objectif.',
              '11.B — Discuter laser sélectif ou traitement local. Exemple suisse : '+med+'. D’autres classes diminuent la production d’humeur aqueuse ; leurs contre-indications propres doivent être vérifiées avant prescription. Les bêtabloquants locaux peuvent avoir des effets systémiques.',
              'Si le traitement échoue ou la maladie est avancée, discuter chirurgie filtrante ou autre technique adaptée. Réduire le nombre de flacons et traiter la surface oculaire peut améliorer l’observance. Le choix pendant la grossesse demande une évaluation spécifique et la lecture de l’AIPS.',
              '11.C — Contrôler pression, tolérance, papille et champ selon le risque ; rapprocher le suivi après modification ou progression. L’EGS cite 6–12 mois pour certains suspects ou hypertensions stables, ce qui ne s’applique pas automatiquement à un glaucome établi ou avancé.',
              '11.D — Le contrôle pressionnel n’est pas une guérison. Avant un suivi ambulatoire, vérifier compréhension du traitement, technique d’instillation, accès aux médicaments et prochain rendez-vous. Adapter conduite et autonomie au champ restant.'))
    l.add('La prévention repose sur le repérage des personnes à risque et le suivi durable. Les {mesures préventives} visent surtout à éviter une découverte tardive et une progression silencieuse. Une acuité centrale conservée ne suffit pas au suivi.',
        paras('Primaire : éviter les corticoïdes oculaires non justifiés et identifier les facteurs pouvant augmenter la pression ; ne pas arrêter un traitement indispensable sans coordination.',
              'Secondaire : proposer une évaluation adaptée aux antécédents familiaux et aux anomalies de pression ou de papille. Aucun calendrier suisse uniforme de dépistage universel n’est inventé ici.',
              'Tertiaire : maintenir le traitement, les champs visuels et la mesure de progression ; prévoir aides et réadaptation en cas de handicap.'))
    l.add('La pression seule ne pose ni n’exclut le diagnostic. Confronter papille, fibres, champ et angle. Proposer un traitement adapté, y compris le laser sélectif. Réviser la cible si la maladie progresse.')
    l.quiz([
        ('Une pression de 22 mmHg prouve-t-elle un glaucome ?','Non : elle impose une évaluation, sans prouver un dommage glaucomateux.'),
        ('Une pression dans la norme exclut-elle le GPAO ?','Non : un glaucome à pression normale existe.'),
        ('Pourquoi faire une gonioscopie ?','Pour confirmer l’angle ouvert et rechercher un mécanisme secondaire.'),
        ('L’OCT remplace-t-il le champ visuel ?','Non : structure et fonction apportent des informations complémentaires.'),
        ('Une zone rouge de l’OCT constitue-t-elle un diagnostic ?','Non : vérifier qualité, anatomie et concordance clinique.'),
        ('Le GPAO habituel est-il douloureux ?','Habituellement non ; douleur et rougeur imposent une autre recherche.'),
        ('Le laser sélectif est-il réservé à l’échec des gouttes ?','Non : l’EGS le propose aussi comme premier choix dans des situations adaptées.'),
        ('Existe-t-il une pression cible valable pour tous ?','Non : elle dépend notamment du stade et de la progression.'),
        ('Doubler les instillations de Xalatan améliore-t-il l’effet ?','Non : l’AIPS limite l’administration à une fois par jour.'),
        ('Peut-on associer deux analogues de prostaglandine sans réserve ?','Non : une hausse paradoxale de pression est décrite.'),
        ('Pourquoi comprimer le sac lacrymal après instillation ?','Pour réduire l’absorption systémique, selon le mode d’administration AIPS.'),
        ('Une pression contrôlée signifie-t-elle guérison ?','Non : le suivi de la fonction et de la structure reste nécessaire.'),
        ('Que vérifier avant d’intensifier les gouttes ?','La technique, l’observance, la tolérance et la réalité de la progression.'),
        ('Un intervalle de suivi d’un suspect stable convient-il à une forme avancée ?','Non : le calendrier dépend de la menace fonctionnelle.')])
    l.write()

if __name__=='__main__': rediger()
