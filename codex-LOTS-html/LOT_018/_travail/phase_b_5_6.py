from format_phase_b import Lesson, paras, table, steps
from medicaments_phase_b import eylea

def rediger():
    l=Lesson(5,[13,25])
    l.add('Le COUF 2025 décrit la rétinopathie diabétique comme une atteinte rétinienne liée à l’hyperglycémie chronique. Les {formes de rétinopathie et de maculopathie} déterminent le risque visuel. L’œdème maculaire peut exister à plusieurs stades de rétinopathie.',
        paras('La rétinopathie non proliférante présente des lésions microvasculaires sans néovaisseaux. La forme proliférante comporte des néovaisseaux rétiniens ou papillaires et peut se compliquer d’hémorragie ou de traction.',
              'La maculopathie peut être œdémateuse ou ischémique. La prolifération décrit les vaisseaux anormaux ; l’œdème décrit l’accumulation de liquide. Ces deux dimensions doivent être évaluées séparément.'))
    l.add('Le risque dépend notamment de la durée du diabète et du contrôle glycémique et tensionnel. Les {données de fréquence et d’évolution} doivent préciser leur population. Une bonne vision ressentie ne garantit pas l’absence de rétinopathie.',
        paras('Le COUF 2025 rapporte qu’environ 30 % des personnes diabétiques présentent une rétinopathie dans les données qu’il synthétise. Il indique aussi qu’environ 20 % des personnes ayant un diabète de type 2 en présentent au diagnostic. Ces valeurs ne constituent pas une mesure suisse actuelle et ne s’appliquent pas aux seuls patients avec baisse visuelle.',
              'L’évolution initiale peut être silencieuse. L’œdème maculaire, l’hémorragie vitréenne, la traction et le glaucome néovasculaire menacent ensuite la fonction. Grossesse, adolescence, changement rapide du contrôle glycémique ou chirurgie oculaire peuvent imposer une surveillance renforcée.'))
    l.add('L’hyperglycémie altère les cellules et les capillaires rétiniens. Les {mécanismes de fuite, d’ischémie et de traction} expliquent les complications. Le traitement de l’œdème ne remplace pas l’évaluation de la prolifération.',
        paras('La glycation, le stress oxydatif et la perte des péricytes et des cellules endothéliales altèrent la barrière hématorétinienne. Les capillaires fuient ou s’obstruent. L’hypoxie stimule des facteurs dont le VEGF, puis les néovaisseaux peuvent saigner et s’accompagner de membranes fibreuses contractiles.')+
        table(['Lésion','Exploration','Traitement et mécanisme'],[
            ['Fuite maculaire.','OCT et fond d’œil.','Anti-VEGF ou autre traitement sélectionné pour diminuer la perméabilité.'],
            ['Non-perfusion rétinienne.','Rétinographies et angiographie selon besoin.','Contrôle systémique et stratégie rétinienne selon stade.'],
            ['Néovaisseaux.','Fond d’œil périphérique, papille et angiographie.','Photocoagulation panrétinienne : réduire le stimulus ischémique ; anti-VEGF dans des situations sélectionnées.'],
            ['Sang vitréen ou traction.','Fond d’œil ; échographie si rétine masquée.','Vitrectomie selon indication, en traitant les membranes et complications.']]))
    l.add('Chez une personne diabétique, une baisse visuelle nouvelle mérite un diagnostic précis. Les {urgences et diagnostics concurrents} passent avant l’attribution au diabète. Plusieurs causes peuvent coexister.',
        table(['Priorité','Signe ou examen','Conduite'],[
            ['🚩 E1 — Ischémie artérielle ou cérébrale.','Début brutal, champ ou déficit afférent.','Filière urgente adaptée.'],
            ['🚩 Décollement ou hémorragie vitréenne.','Voile, corps flottants, fond d’œil masqué.','Examen rétinien urgent ; échographie si nécessaire.'],
            ['🚩 Glaucome néovasculaire.','Douleur, pression élevée, néovaisseaux iriens.','Avis ophtalmologique immédiat.'],
            ['Cataracte ou variation réfractive.','Opacité ou réfraction fluctuante.','Confronter aux lésions rétiniennes ; ne pas arrêter le bilan à la glycémie.']]),[1,2,13])
    l.add('L’anamnèse reconstitue le diabète et l’évolution oculaire. Les {questions de risque et d’accès aux soins} orientent la surveillance. Une amélioration rapide de la glycémie demande parfois un suivi rétinien plus rapproché.',
        table(['Question','Raison'],[
            ['Type, durée et évolution récente de l’HbA1c ?','Le risque et sa dynamique dépendent de l’exposition et de ses changements.'],
            ['Hypertension, atteinte rénale, grossesse ou projet de grossesse ?','Ces contextes modifient le risque et la prise en charge.'],
            ['Dernier fond d’œil, laser, injections ou chirurgie ?','Identifier le stade antérieur et une interruption de suivi.'],
            ['Baisse centrale lente, voile brutal ou douleur ?','Distinguer œdème, saignement, traction et hypertonie.'],
            ['Possibilité d’honorer les rendez-vous ?','Le choix thérapeutique et la continuité des soins en dépendent.']]))
    l.add('L’examen documente le stade rétinien et le mécanisme de la baisse. Les {gestes au lit du patient et au cabinet} commencent par l’acuité et le segment antérieur. Une acuité normale ne dispense pas d’examiner la périphérie.',
        table(['Geste','Normal','Anomalie et décision'],[
            ['Acuité corrigée séparée et test central.','Fonction stable sans déformation nouvelle.','Baisse ou métamorphopsie : OCT maculaire.'],
            ['Lampe à fente et pression.','Cornée claire, iris sans néovaisseaux.','Rubéose ou hypertonie : prise en charge rapide du risque néovasculaire.'],
            ['Fond d’œil dilaté ou photographies adaptées.','Absence de lésions diabétiques visibles.','Microanévrismes, hémorragies, anomalies veineuses ou néovaisseaux : classer.'],
            ['OCT.','Architecture maculaire sans liquide.','Œdème central ou traction : relier à la fonction.'],
            ['Échographie si rétine inaccessible.','Rétine appliquée.','Décollement ou traction : décision rétinienne urgente.']]))
    l.add('Les {syndromes de baisse visuelle diabétique} séparent macula, vitré et complications proliférantes. Chaque syndrome associe une plainte et une lésion vérifiable. Les signes physiques peuvent précéder les symptômes.',
        table(['Syndrome','Fonctionnel','Physique et mécanisme'],[
            ['7.1 — Maculaire œdémateux.','Flou central et métamorphopsies.','Épaississement ou liquide à l’OCT par rupture de barrière.'],
            ['7.2 — Ischémique.','Baisse parfois disproportionnée à l’œdème.','Non-perfusion à l’imagerie adaptée ; tissu mal oxygéné.'],
            ['7.3 — Hémorragique/tractionnel.','Voile ou baisse brutale.','Sang dans le vitré ou membranes tirant la rétine.'],
            ['7.4 — Néovasculaire antérieur.','Douleur et baisse visuelle.','Néovaisseaux iriens, obstruction de l’angle et hypertonie.']]))
    l.add('Le diagnostic positif repose sur les lésions rétiniennes dans le contexte du diabète. Les {stades et critères de gravité} orientent le suivi et le traitement. Le statut de la macula doit être précisé séparément.',
        paras('Le COUF 2025 reprend une classification francophone : non proliférante minime, modérée ou sévère, puis proliférante et proliférante compliquée. La présence de néovaisseaux distingue la prolifération.',
              'La règle dite 4–2–1 repère une forme non proliférante sévère : hémorragies rétiniennes sévères dans quatre quadrants, anomalies veineuses dans deux quadrants ou anomalies microvasculaires intrarétiniennes dans un quadrant. La sévérité et la nature des lésions doivent être appréciées par un lecteur entraîné ; quelques points rouges ne suffisent pas.',
              'L’œdème maculaire peut accompagner tous les stades. Son atteinte centrale et son retentissement fonctionnel sont déterminants pour décider d’un traitement.'))
    l.add('Les {explorations rétiniennes et systémiques} répondent à des objectifs distincts. L’OCT mesure l’œdème ; les photographies documentent les lésions et leur distribution. Les examens biologiques décrivent le terrain sans remplacer le fond d’œil.',
        paras('9.a — Référence clinique : examen ou photographie du fond d’œil pour le stade ; OCT pour l’anatomie maculaire.',
              '9.b — Acuité, fond d’œil, OCT si plainte ou suspicion d’œdème ; récupérer HbA1c, pression artérielle et fonction rénale utiles au traitement global.',
              '9.c — Si les images sont ininterprétables, organiser un examen ophtalmologique. L’échographie explore le segment postérieur masqué ; elle ne quantifie pas à elle seule l’œdème.',
              '9.d — Angiographie si cartographie de non-perfusion ou doute thérapeutique ; son indication et les précautions du colorant se discutent notamment en grossesse.')+
        table(['Résultat','Signification','Conduite'],[
            ['Néovaisseaux ou complications.','Forme proliférante.','Avis rétinien et traitement rapide selon menace.'],
            ['Œdème central avec baisse.','Cause potentiellement traitable.','Évaluer un traitement intravitréen approprié.'],
            ['Pas d’œdème mais baisse persistante.','Autre mécanisme possible.','Rechercher ischémie, cataracte, nerf ou autre lésion.']]))
    l.add('L’{arbre de décision rétinien} traite d’abord la complication menaçante. Il distingue ensuite prolifération et œdème maculaire. Le suivi systémique se poursuit en parallèle.',
        steps('Si baisse brutale, voile ou douleur → rechercher hémorragie, décollement, occlusion et glaucome néovasculaire.',
              'Si néovaisseaux → avis rétinien pour photocoagulation et/ou stratégie intravitréenne adaptée.',
              'Si œdème maculaire central symptomatique → discuter un traitement spécifique, sans copier le schéma DMLA.',
              'Si forme non proliférante sans menace immédiate → surveillance selon stade et contexte.',
              'Dans tous les cas → coordonner glycémie, pression, fonction rénale, grossesse et accès aux soins.'))
    med=eylea(l,'diabete')
    l.add('La prise en charge associe contrôle du diabète et traitement rétinien ciblé. Les {moyens et la surveillance} dépendent de la prolifération, de l’œdème et de la traction. L’éducation vise à éviter les interruptions de suivi.',
        paras('11.A — Prévenir une perte irréversible, traiter une maculopathie active et réduire les complications néovasculaires. Les objectifs glycémiques et tensionnels sont individualisés avec le médecin du diabète.',
              '11.B — La photocoagulation panrétinienne traite la rétinopathie proliférante ; une vitrectomie peut être nécessaire devant hémorragie persistante ou traction menaçante. Les anti-VEGF sont employés dans des indications sélectionnées, mais l’autorisation spécifique de la spécialité doit être respectée.',
              'Pour l’œdème maculaire diabétique : '+med+'. L’extrait suisse lu décrit les trois premiers mois à intervalle de quatre semaines ; ne pas remplacer ce texte par un schéma mémorisé d’une autre source.',
              'La grossesse avec diabète préexistant demande une coordination et une surveillance renforcées. Les contre-indications d’Eylea pendant grossesse et allaitement restent applicables ; une décision spécialisée doit rechercher une alternative compatible.',
              '11.C — Contrôler acuité, OCT et rétine selon le stade et à chaque traitement. La source COUF décrit un contrôle annuel pour les formes absentes ou minimes, et plus rapproché en cas de gravité ou de situation évolutive ; ce repère européen ne remplace pas le calendrier suisse individualisé.',
              '11.D — La régression de l’œdème ou des néovaisseaux ne guérit pas le diabète. Avant retour : rendez-vous, consignes d’alerte, traitements et coordination disponibles. Adapter aides, transport et activités aux capacités visuelles.'))
    l.add('Les {trois niveaux de prévention} reposent sur le contrôle systémique, le dépistage et la protection de la fonction restante. Le dépistage ne doit pas attendre une plainte centrale. Une image non interprétable nécessite une solution.',
        paras('Primaire : accompagner le contrôle glycémique et tensionnel et les facteurs cardiovasculaires. Une correction rapide d’un déséquilibre peut demander un contrôle rétinien rapproché ; elle ne justifie pas de laisser le diabète non traité.',
              'Secondaire : organiser le dépistage rétinien du diabète et vérifier sa réalisation. Le type, la durée, la grossesse et le stade déterminent le calendrier.',
              'Tertiaire : maintenir laser ou injections et suivi, traiter les complications, proposer basse vision et aide sociale. Les absences aux rendez-vous doivent être repérées et leurs causes discutées.'))
    l.add('Une bonne acuité n’exclut pas une rétinopathie grave. Distinguer œdème, prolifération et traction. Vérifier le schéma suisse de chaque injection. Coordonner le suivi rétinien avec celui du diabète.')
    l.quiz([
        ('L’œdème maculaire exige-t-il une forme proliférante ?','Non : il peut exister à plusieurs stades.'),
        ('Que signifie proliférante ?','La présence de néovaisseaux rétiniens ou papillaires.'),
        ('Une HbA1c mesure-t-elle directement les lésions rétiniennes ?','Non : elle décrit un aspect du contrôle glycémique.'),
        ('La bonne acuité autorise-t-elle à supprimer le dépistage ?','Non : une atteinte périphérique peut rester silencieuse.'),
        ('Quel examen documente le liquide maculaire ?','L’OCT.'),
        ('Que faire si une hémorragie masque le fond d’œil ?','Rechercher un décollement par une exploration adaptée, notamment l’échographie.'),
        ('La règle 4–2–1 signifie-t-elle néovaisseaux obligatoires ?','Non : elle décrit une forme non proliférante sévère.'),
        ('Pourquoi le laser panrétinien peut-il faire régresser les néovaisseaux ?','Il réduit le stimulus lié à la rétine ischémique.'),
        ('Une traction menaçante relève-t-elle toujours des seules injections ?','Non : une chirurgie rétinovitréenne peut être nécessaire.'),
        ('Le schéma d’Eylea DMLA peut-il être recopié sans lecture pour l’œdème diabétique ?','Non : les indications ont des posologies distinctes.'),
        ('La grossesse permet-elle de négliger les contre-indications anti-VEGF ?','Non : évaluation spécialisée et information suisse restent nécessaires.'),
        ('Une amélioration rapide de la glycémie dispense-t-elle d’un contrôle rétinien ?','Non : certains patients nécessitent au contraire une surveillance renforcée.'),
        ('Le laser guérit-il le diabète ?','Non : le suivi métabolique et rétinien reste nécessaire.'),
        ('Une douleur avec néovaisseaux iriens est-elle rassurante ?','Non : rechercher un glaucome néovasculaire urgent.')])
    l.write()

    l=Lesson(6,[14,17,25])
    l.add('L’occlusion veineuse rétinienne entrave le drainage veineux de la rétine. Les {formes centrales et de branche}, décrites par le COUF et le RCOphth, produisent œdème et parfois ischémie. Leur conduite diffère de celle d’une occlusion artérielle.',
        paras('L’occlusion centrale intéresse la veine centrale à proximité de la lame criblée. L’occlusion de branche concerne un territoire, souvent au niveau d’un croisement artérioveineux. Une forme hémirétinienne touche une moitié supérieure ou inférieure.',
              'Le caractère ischémique décrit l’importance de la non-perfusion, pas seulement la quantité d’hémorragies. Une forme initialement non ischémique peut évoluer ; la classification ne dispense pas de surveillance.'))
    l.add('L’âge, l’hypertension et le glaucome sont des facteurs importants. Les {repères de fréquence et de pronostic} varient selon la forme. Le risque visuel ne se déduit pas de la seule prévalence.',
        paras('Le COUF 2025 cite une prévalence de 0,1–0,4 % pour l’occlusion centrale et 0,6–1,2 % pour les occlusions de branche dans les populations de référence. Ces valeurs ne sont pas des incidences suisses ni un classement des patients consultant pour perte visuelle.',
              'Le RCOphth 2022 rapporte une conversion possible des formes centrales non ischémiques vers l’ischémie, même sous traitement de l’œdème. Le pronostic dépend surtout de la macula, de la non-perfusion et des complications néovasculaires. Une amélioration initiale n’annule donc pas le suivi.'))
    l.add('L’obstacle veineux augmente la pression capillaire et perturbe la perfusion. Les {mécanismes de fuite et de néovascularisation} expliquent les deux objectifs du traitement. Assécher la macula ne signifie pas reperfuser toute la rétine.',
        paras('L’épaississement d’une artère adjacente et les contraintes anatomiques favorisent la compression veineuse. La stase entraîne hémorragies et fuite ; l’ischémie stimule notamment le VEGF. Celui-ci favorise à la fois œdème et néovascularisation.')+
        table(['Lésion','Exploration','Stratégie'],[
            ['Œdème maculaire.','OCT et acuité.','Anti-VEGF ou option spécialisée pour diminuer la fuite.'],
            ['Non-perfusion.','Angiographie ou OCT-angiographie selon contexte.','Surveillance rapprochée des complications.'],
            ['Néovaisseaux iriens ou rétiniens.','Segment antérieur, gonioscopie et fond d’œil.','Laser adapté et anti-VEGF adjuvant selon localisation.'],
            ['Glaucome néovasculaire.','Pression et angle.','Contrôle urgent de la pression et du stimulus ischémique.']]))
    l.add('La démarche exclut une occlusion artérielle et les autres causes de baisse aiguë. Les {diagnostics différentiels} se tranchent surtout au fond d’œil. Douleur et rougeur font rechercher une complication néovasculaire.',
        table(['Diagnostic','Discriminant','Conduite'],[
            ['🚩 E1 — Occlusion artérielle.','Rétine ischémique blanchâtre, baisse brutale parfois profonde.','Filière neurovasculaire urgente.'],
            ['🚩 Glaucome néovasculaire.','Néovaisseaux antérieurs, douleur et hypertonie.','Traitement spécialisé immédiat.'],
            ['Rétinopathie diabétique.','Distribution et contexte, lésions souvent bilatérales.','Classer les deux mécanismes s’ils coexistent.'],
            ['Syndrome d’ischémie oculaire.','Hypoperfusion et contexte carotidien.','Bilan vasculaire adapté ; ne pas s’arrêter au mot hémorragies.']]),[1,14,15,17])
    l.add('L’anamnèse précise le début, les facteurs vasculaires et les traitements. Les {questions utiles au bilan} évitent une recherche de thrombophilie systématique sans indication. Chez un sujet jeune ou atypique, le bilan s’individualise.',
        table(['Question','Pourquoi'],[
            ['Début et sévérité de la baisse ?','Estimer l’urgence et le mécanisme maculaire.'],
            ['Hypertension, dyslipidémie, diabète ou tabac ?','Identifier des facteurs systémiques à prendre en charge.'],
            ['Glaucome connu ou corticoïdes ?','Une pression élevée peut contribuer et modifier la surveillance.'],
            ['Antécédents thrombotiques, symptômes systémiques ou atteinte bilatérale ?','Orienter des examens complémentaires ciblés.'],
            ['Traitement hormonal, anticoagulants et derniers contrôles ?','Faire une décision individualisée, sans arrêt ou ajout automatique.']]))
    l.add('Le fond d’œil montre une distribution compatible des hémorragies et des veines anormales. L’{examen de gravité} recherche atteinte maculaire, défaut afférent et néovascularisation. L’acuité seule ne quantifie pas toute l’ischémie.',
        table(['Geste','Normal','Anomalie et implication'],[
            ['Acuité et pupilles.','Fonction stable et réponses symétriques.','Baisse sévère ou défaut afférent : suspicion d’atteinte importante.'],
            ['Fond d’œil.','Veines non congestives, absence d’hémorragies diffuses.','Occlusion centrale : atteinte étendue ; branche : territoire sectoriel.'],
            ['Iris et gonioscopie selon indication.','Pas de néovaisseaux.','Rubéose ou néovaisseaux angulaires : traitement rapide.'],
            ['Pression instrumentale.','Valeur interprétée dans le contexte.','Hypertonie ou glaucome associé à traiter.'],
            ['OCT.','Macula sans liquide.','Œdème à quantifier et à suivre.']]))
    l.add('Les {syndromes veineux} associent territoire, macula et complications. Une forme non ischémique peut devenir ischémique. Le traitement de l’œdème ne clôt pas l’évaluation.',
        table(['Syndrome','Fonctionnel','Physique'],[
            ['7.1 — Occlusion centrale.','Baisse monoculaire souvent indolore.','Hémorragies étendues, veines dilatées/tortueuses et œdème variable.'],
            ['7.2 — Occlusion de branche.','Gêne centrale si macula atteinte, parfois déficit sectoriel.','Lésions limitées au territoire drainé.'],
            ['7.3 — Ischémie importante.','Baisse sévère, parfois défaut afférent.','Non-perfusion à documenter ; risque néovasculaire.'],
            ['7.4 — Complication néovasculaire.','Douleur ou baisse secondaire.','Néovaisseaux et hypertonie ou hémorragie.']]))
    l.add('Le diagnostic d’occlusion veineuse est principalement clinique. Les {critères de territoire et d’ischémie} sont complétés par l’imagerie. Une étiquette ischémique doit être réévaluée dans le temps.',
        paras('Le RCOphth 2022 décrit le tableau central par ses hémorragies rétiniennes étendues et anomalies veineuses ; la branche suit un secteur. L’OCT précise l’œdème, tandis que l’angiographie évalue la non-perfusion.',
              'Les seuils d’ischémie historiques dépendent du champ photographié et de la méthode. Il ne faut pas transposer sans précaution un seuil d’une angiographie classique à une image grand champ. Acuité, pupilles et néovaisseaux complètent l’interprétation.'))
    l.add('Les {examens ophtalmologiques et médicaux} répondent à la menace visuelle et aux facteurs de risque. Le bilan systémique est ciblé. Une thrombophilie ou des anticorps antiphospholipides ne se recherchent pas automatiquement dans toute occlusion isolée.',
        paras('9.a — Diagnostic clinique au fond d’œil ; imagerie pour œdème et perfusion.',
              '9.b — Acuité, OCT, pression et recherche de néovaisseaux ; mesurer la pression artérielle et dépister un diabète méconnu. Le RCOphth propose aussi une numération sanguine et un bilan inflammatoire selon son circuit.',
              '9.c — OCT-angiographie possible pour la perfusion, avec limites et artefacts ; individualiser toute injection de colorant.',
              '9.d — Examens complémentaires dirigés par âge, récidive, bilatéralité ou signes systémiques, avec le médecin traitant.')+
        table(['Résultat','Signification','Action'],[
            ['Œdème actif et retentissement.','Cause traitable de baisse.','Discuter traitement intravitréen rapide.'],
            ['Non-perfusion importante.','Risque néovasculaire.','Surveillance rapprochée, même si l’œdème régresse.'],
            ['Néovaisseaux présents.','Complication constituée.','Laser et traitement adjuvant selon le spécialiste.']]))
    l.add('L’{algorithme veineux} sépare le traitement de l’œdème de la prévention des complications. Le suivi évolue avec la perfusion. Les indications d’antithrombotiques restent celles réellement établies.',
        steps('Si tableau artériel ou neurologique → filière urgente correspondante.',
              'Si occlusion veineuse → déterminer territoire, œdème et ischémie.',
              'Si œdème symptomatique → discuter traitement intravitréen adapté.',
              'Si néovaisseaux ou glaucome → traiter rapidement la complication et la rétine ischémique.',
              'Dans tous les cas → corriger les facteurs de risque et organiser la surveillance sans anticoagulation systématique pour la seule occlusion.'))
    med=eylea(l,'rvo')
    l.add('La prise en charge vise l’œdème, les néovaisseaux et les risques systémiques. Les {traitements et contrôles} suivent ces objectifs séparément. Le RCOphth ne recommande pas d’anticoagulation ou d’antiagrégant pour toute occlusion veineuse isolée.',
        paras('11.A — Préserver la vision et prévenir glaucome néovasculaire et hémorragie. Une reperfusion complète ne peut pas être promise.',
              '11.B — Pour l’œdème maculaire, exemple suisse : '+med+'. Un implant corticoïde constitue une autre option spécialisée avec ses propres risques de cataracte et d’hypertonie ; aucune posologie n’est transposée entre produits.',
              'Pour une néovascularisation antérieure sur occlusion centrale ischémique, le RCOphth associe traitement anti-VEGF adjuvant et photocoagulation panrétinienne rapide. Une néovascularisation sectorielle après occlusion de branche relève d’un laser adapté au territoire. Le contrôle des facteurs vasculaires reste coordonné au médecin traitant.',
              '11.C — Le RCOphth recommande une recherche mensuelle des néovaisseaux de l’iris ou de l’angle dans l’occlusion centrale ischémique. Après arrêt des injections, maintenir une surveillance rapprochée ; la diminution de l’œdème n’abolit pas ce risque.',
              '11.D — Avant suivi ambulatoire : symptômes d’alerte expliqués, prochain contrôle et accès aux injections organisés. Une douleur, une rougeur ou une baisse nouvelle demande un avis rapide. Le pronostic dépend de l’ischémie maculaire et des séquelles, pas seulement de l’épaisseur mesurée.'))
    l.add('La prévention repose sur les facteurs vasculaires et la surveillance des complications. Les {mesures préventives} sont individualisées. La découverte d’une occlusion ne crée pas à elle seule une indication permanente d’anticoagulation.',
        paras('Primaire : rechercher et traiter hypertension, dyslipidémie et autres risques selon leurs recommandations propres ; vérifier le glaucome.',
              'Secondaire : documenter la perfusion et ne pas perdre de vue les formes susceptibles de se compliquer. Dépister un diabète méconnu a un intérêt même si son association épidémiologique avec l’occlusion varie selon les études.',
              'Tertiaire : traiter œdème et néovaisseaux, soutenir l’observance et proposer des aides si le déficit persiste.'))
    l.add('Une occlusion veineuse ne se traite pas comme une occlusion artérielle. Évaluer séparément œdème et non-perfusion. Surveiller les néovaisseaux même après amélioration. Ne pas anticoaguler systématiquement pour la seule occlusion.')
    l.quiz([
        ('L’occlusion veineuse et artérielle suivent-elles la même filière ?','Non : le mécanisme et l’urgence neurovasculaire diffèrent.'),
        ('Comment reconnaître une occlusion de branche ?','Par une atteinte sectorielle du territoire drainé, à confronter au fond d’œil.'),
        ('La quantité d’hémorragies suffit-elle à classer l’ischémie ?','Non : perfusion, fonction et autres signes doivent être évalués.'),
        ('L’OCT documente-t-il l’œdème ?','Oui ; l’analyse de non-perfusion demande une approche complémentaire.'),
        ('Une forme non ischémique peut-elle évoluer ?','Oui : le suivi reste nécessaire.'),
        ('Un anti-VEGF supprime-t-il tout risque néovasculaire ?','Non : il ne garantit pas la reperfusion.'),
        ('La douleur secondaire doit-elle rassurer ?','Non : rechercher notamment un glaucome néovasculaire.'),
        ('Faut-il anticoaguler toute occlusion veineuse rétinienne ?','Non : aucune indication systématique n’est établie pour la seule occlusion.'),
        ('Le bilan de thrombophilie est-il automatique ?','Non : le contexte clinique doit orienter les explorations.'),
        ('Pourquoi mesurer la pression artérielle ?','Pour identifier et traiter un facteur de risque fréquent.'),
        ('Quand surveiller les néovaisseaux d’une occlusion centrale ischémique ?','Le RCOphth recommande un contrôle mensuel, adapté au contexte.'),
        ('Quel risque ajoute un corticoïde intravitréen ?','Notamment hypertonie et cataracte, à surveiller selon le produit.'),
        ('L’absence de réponse visuelle malgré disparition de l’œdème prouve-t-elle l’échec technique ?','Non : une ischémie ou une lésion fovéale irréversible peut limiter la récupération.'),
        ('Peut-on abandonner les contrôles après l’arrêt des injections ?','Non : le risque néovasculaire persiste dans les formes ischémiques.')])
    l.write()

if __name__=='__main__': rediger()
