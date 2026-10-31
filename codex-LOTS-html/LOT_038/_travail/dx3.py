from format_lecon import Lesson,paras,table,steps
from tobramycine import tobrex
l=Lesson('Blépharite',3)
med=tobrex(l,'blepharite')
l.add('La {blépharite} est une inflammation du bord palpébral, souvent récidivante. Elle peut toucher la région des cils, les orifices des glandes de Meibomius ou les deux. Son traitement dépend du mécanisme et du retentissement sur la surface oculaire.',paras(
 'La forme antérieure intéresse le bord portant les cils et leurs follicules. Elle peut associer une composante bactérienne, notamment staphylococcique, ou une dermatite séborrhéique. La forme postérieure est liée au fonctionnement des glandes de Meibomius.',
 'Des croûtes, un prurit, une sensation de sable, une rougeur et des paupières collées au réveil sont évocateurs. Ils ne suffisent pas à exclure une atteinte cornéenne si une douleur oculaire, une photophobie ou une baisse visuelle les accompagne.',
 'La blépharite chronique habituelle n’est pas assimilée à une infection contagieuse nécessitant d’isoler le patient. Une conjonctivite infectieuse associée reste cependant une autre situation à reconnaître.'),(18,28,29))
l.add('Le {contexte} comprend souvent une dermatose ou un trouble des sécrétions glandulaires. Les symptômes peuvent alterner avec des périodes plus calmes. Une récidive ne signifie pas nécessairement un échec antibiotique.',paras(
 'La maladie est fréquente en pratique mais aucune proportion suisse fiable n’est fournie ici. Elle peut survenir à différents âges. Les chiffres de séries spécialisées ne doivent pas être transformés en prévalence dans la population générale.',
 'Rechercher une rosacée, une dermatite séborrhéique ou atopique, une sécheresse oculaire et les traitements locaux utilisés. Les cosmétiques ou un produit irritant peuvent aussi entretenir des symptômes du bord et de la peau.',
 'La répétition des épisodes et des soins nécessaires peut retentir sur la vie quotidienne. Demander ce que le patient arrive réellement à faire et corriger les gestes trop agressifs plutôt que considérer toute persistance comme une mauvaise observance.'),(18,28,29,30))
l.add('La {physiopathologie} relie inflammation du bord et instabilité des larmes. Des sécrétions glandulaires anormales favorisent l’évaporation et l’irritation. Des mécanismes bactériens, cutanés ou parasitaires peuvent coexister.',paras(
 'Les paupières répartissent les larmes lors du clignement. Les glandes de Meibomius fournissent leur composante lipidique, utile pour freiner l’évaporation. Une obstruction ou une mauvaise qualité des sécrétions peut donc produire une sensation de sécheresse malgré un larmoiement réflexe.',
 'La région ciliaire peut être inflammatoire avec débris et croûtes. Une flore cutanée habituelle peut contribuer à l’inflammation sans que toute blépharite soit une infection aiguë à éradiquer par antibiotique. La prescription doit correspondre à la présentation examinée.',
 'Demodex est un acarien susceptible de participer à certaines blépharites persistantes. L’évaluation spécialisée établit la pertinence de cette hypothèse. Une simple démangeaison ne démontre pas une prolifération responsable et ne justifie pas un antiparasitaire empirique.',
 'Une atteinte du film lacrymal peut favoriser inflammation conjonctivale, inconfort et complications cornéennes. Le raisonnement doit donc examiner le globe autant que les cils.'),(2,18,28,30))
l.add('Les {drapeaux rouges} recherchent une complication cornéenne ou une autre urgence. Une douleur dans l’œil, une photophobie ou une baisse visuelle appelle un avis rapide. Une cellulite ou une lésion tumorale ne doit pas être masquée par l’étiquette de blépharite.',table(['Constat','Question clinique','Conduite'],[
 ['Douleur oculaire, photophobie ou vision modifiée','Cornée ou autre structure oculaire atteinte ?','Évaluation ophtalmologique urgente.'],
 ['Porteur de lentilles avec œil rouge douloureux','Kératite infectieuse possible ?','Retirer les lentilles et obtenir un examen urgent.'],
 ['Rougeur diffuse fébrile, extension ou mauvais état général','Cellulite plutôt que simple bord inflammatoire ?','Évaluer rapidement le traitement systémique et le lieu de soins.'],
 ['Diplopie, exophtalmie ou mouvements douloureux','Extension orbitaire ?','Évaluation hospitalière immédiate.'],
 ['Atteinte unilatérale persistante, perte de cils ou déformation','Autre maladie du bord ou tumeur ?','Examen spécialisé et prélèvement selon l’aspect.']
 ]),(5,9,18,21,29))
l.add('L’{anamnèse} décrit les épisodes, les symptômes de surface et les soins précédents. Elle recherche aussi les expositions et les maladies cutanées. Les signes visuels doivent être demandés explicitement.',steps(
 'Préciser depuis quand le bord est irrité, si les deux yeux sont concernés et si les symptômes prédominent au réveil ou au cours de la journée.',
 'Rechercher douleur dans l’œil, photophobie, variation ou diminution de vision, sécrétions et sensation de corps étranger.',
 'Demander des chalazions ou orgelets récidivants, une rosacée ou dermatite, et une sécheresse connue.',
 'Recenser lentilles, maquillage, produits de nettoyage, collyres et médicaments généraux. Noter une relation temporelle avec un produit nouveau.',
 'Faire décrire la chaleur, le massage et le nettoyage réellement pratiqués. Vérifier leur tolérance et l’aide disponible chez l’enfant ou la personne dépendante.',
 'Avant un médicament, préciser allergies, maladies neuromusculaires, grossesse, allaitement et autres antibiotiques utilisés.'),(2,18,22,28,29))
l.add('L’{examen ciblé} observe le bord antérieur, les glandes et la surface oculaire. Il différencie une inflammation diffuse d’un foyer nodulaire. La vision est mesurée et toute limite de l’examen est notée.',paras(
 'Inspecter rougeur, croûtes, squames, implantation des cils et anomalies du bord. Rechercher nodules, cicatrices ou perte focale de cils. Comparer les deux paupières et l’état de la peau voisine.',
 'L’ophtalmologue examine à la lampe à fente les orifices glandulaires, les sécrétions et le film lacrymal. Il recherche une atteinte conjonctivale ou cornéenne. Une manipulation glandulaire ne doit pas devenir un massage douloureux imposé à domicile.',
 'La vision, les pupilles et la motilité sont vérifiées selon le contexte. Si des symptômes évoquent une atteinte de la cornée, l’examen spécialisé ne doit pas être remplacé par un nouveau topique empirique.',
 'Chez l’enfant, le caractère chronique ne rassure pas à lui seul si la vision ou la coopération empêche un examen fiable. Les symptômes persistants avec photophobie appellent une évaluation adaptée.'),(18,27,28,29))
l.add('L’{approche syndromique} identifie le mécanisme dominant sans nier les formes mixtes. Elle guide les soins et les traitements ciblés. Une inflammation cutanée de contact ou une conjonctivite peut être associée.',table(['Présentation','Orientation','Implication'],[
 ['Croûtes et inflammation autour des cils','Blépharite antérieure.','Hygiène et recherche d’une composante bactérienne ou dermatologique.'],
 ['Sécrétions glandulaires anormales, sécheresse et bord postérieur atteint','Dysfonction des glandes de Meibomius.','Soins glandulaires et évaluation spécialisée si persistance.'],
 ['Forme persistante avec suspicion de Demodex','Participation parasitaire possible.','Confirmation et traitement adapté par le spécialiste.'],
 ['Peau surtout prurigineuse après une exposition','Dermatite irritative ou allergique.','Enquête sur les produits et éviction pertinente.'],
 ['Foyer nodulaire distinct','Orgelet ou chalazion associé.','Traiter le foyer selon sa nature.'],
 ['Œil rouge douloureux avec photophobie','Atteinte cornéenne possible.','Priorité à l’examen du globe.']
 ]),(1,6,18,28,30))
l.add('Le {diagnostic positif} repose sur l’inflammation du bord et l’examen de ses structures. Les symptômes seuls ne suffisent pas à identifier le mécanisme. La persistance unilatérale ou un aspect inhabituel impose de revoir l’hypothèse.',paras(
 'Des débris ciliaires, un bord inflammatoire et une histoire compatible soutiennent le diagnostic. L’examen recherche ce qui relève des cils, des glandes, de la peau et de la cornée afin d’éviter une ordonnance identique pour toutes les formes.',
 'Une composante bactérienne se juge dans le contexte clinique. La présence d’une bactérie cutanée sur un prélèvement de surface ne suffit pas à expliquer toute inflammation chronique.',
 'Si les symptômes persistent malgré soins appropriés, revoir technique, exposition irritante, diagnostic, participation de Demodex et maladie de la surface. Ne pas conclure automatiquement à une résistance nécessitant un antibiotique plus large.'),(18,28,29,30))
l.add('Les {examens complémentaires} sont orientés par les complications et l’échec inhabituel. La lampe à fente complète l’examen clinique. Aucun bilan biologique ou scanner n’est systématique dans une blépharite simple.',
 '<h3>9.a — Référence</h3>'+paras('L’examen du bord et de la surface oculaire caractérise la forme. Il n’existe pas d’analyse sanguine confirmant toutes les blépharites.')+
 '<h3>9.b — Première intention</h3>'+paras('Mesurer la vision et rechercher une atteinte cornéenne ou conjonctivale. L’état du film lacrymal et des glandes aide à adapter les soins. Les tests supplémentaires dépendent de ce qui est observé.')+
 '<h3>9.c — Examens ciblés</h3>'+paras('Devant une infection sévère ou réfractaire, le spécialiste peut demander un prélèvement microbiologique. Une suspicion parasitaire peut nécessiter une observation ciblée. Ces examens ne sont pas demandés avant toute hygiène du bord et ne doivent pas retarder l’examen d’une cornée symptomatique.')+
 '<h3>9.d — Seconde intention</h3>'+paras('Une masse ou une anomalie persistante du bord peut nécessiter une biopsie. Une imagerie est réservée à une suspicion d’extension profonde ou à une autre question précise. L’enquête dermatologique et les tests de contact peuvent être utiles si la distribution et les expositions évoquent une dermatite.'),(5,6,18,30))
l.add('L’{arbre décisionnel} commence par l’exclusion des urgences de surface et d’orbite. Il précise ensuite le mécanisme du bord. Le suivi vérifie à la fois les symptômes, les gestes et la tolérance.',steps(
 'Si douleur oculaire, photophobie ou vision diminuée, alors demander un examen ophtalmologique urgent.',
 'Si infection diffuse ou signe orbitaire, alors suivre le parcours de cellulite plutôt qu’un traitement du bord seul.',
 'Si forme simple, alors expliquer les soins doux et corriger les facteurs irritants identifiés.',
 'Si une composante bactérienne antérieure justifie un antibiotique, alors choisir une spécialité ophtalmique selon sa notice et une durée définie.',
 'Si dysfonction glandulaire, suspicion de Demodex ou maladie cutanée persistante, alors adapter le traitement avec l’ophtalmologue et, si pertinent, le dermatologue.',
 'Si échec, récidive atypique ou intolérance, alors réexaminer avant de renouveler le médicament.'),(6,18,22,29,30))
l.add('La {prise en charge suisse} repose sur l’éducation et l’hygiène régulière du bord. Le traitement médicamenteux est ciblé sur la composante identifiée et reste limité dans le temps. Une atteinte cornéenne ou une aggravation visuelle nécessite un parcours spécialisé.',
 '<h3>11.A — But</h3>'+paras('Diminuer l’inflammation et l’inconfort, préserver la surface cornéenne et améliorer l’évacuation glandulaire. Le contrôle durable repose souvent sur des soins réguliers, pas sur une cure censée supprimer définitivement toutes les récidives.')+
 '<h3>11.B — Moyens</h3>'+paras('Les HUG décrivent une succession chaleur, massage doux et nettoyage du bord, au moins matin et soir pour l’entretien. Les mains sont propres et la chaleur est agréable, jamais brûlante. Le soignant montre le geste et l’adapte si la cornée est malade ou si l’œil a été opéré récemment.',
 'Retirer doucement les débris après les avoir ramollis, sans frotter vigoureusement le globe. Les soins ne doivent pas provoquer de douleur croissante. Pendant une poussée, éviter lentilles et maquillage ; revoir les produits irritants plutôt que multiplier les nettoyants.',
 'Pour une composante bactérienne de la blépharite antérieure, une pommade de tobramycine est une option citée par HUG. La notice suisse nomme la blépharite à germes sensibles. Elle ne transforme pas ce médicament en traitement de toute sécheresse, de toute rosacée ou de Demodex :')+med+paras(
 'Une forme postérieure persistante nécessite une stratégie pour les glandes et la surface oculaire. Des substituts lacrymaux peuvent être choisis avec le professionnel selon la sécheresse, les conservateurs et la tolérance. Aucune spécialité ni dose de substitut n’est prescrite par cette description générale.',
 'Les antibiotiques systémiques parfois utilisés pour certaines rosacées oculaires relèvent d’une décision spécialisée avec leur propre notice, leurs restrictions et une durée adaptée. Aucun schéma oral étranger n’est transposé ici.',
 'Une blépharite liée à Demodex demande un traitement ciblé après évaluation. L’hygiène seule ne garantit pas l’élimination des acariens. Ne pas appliquer d’huile essentielle pure, de préparation cutanée ou d’antiparasitaire dans l’œil sans prescription ophtalmologique adaptée.',
 'Les corticoïdes oculaires et autres traitements immunomodulateurs nécessitent examen, surveillance et indication spécialisée. Ils ne sont pas ajoutés pour masquer une douleur ou une rougeur sans diagnostic. Les modalités non détaillées ici nécessitent leurs sources et notices propres.')+
 '<h3>11.C — Surveillance</h3>'+paras('Vérifier la diminution de gêne et des croûtes, la tolérance et l’état de la surface. Les soins d’entretien peuvent se poursuivre après amélioration, contrairement à l’antibiotique qui garde sa durée limitée. Une nouvelle irritation après introduction d’un produit évoque aussi une intolérance.',
 'Une baisse visuelle, une photophobie, une douleur importante ou une extension de l’inflammation impose un avis urgent. Une persistance malgré traitement correctement conduit doit être réévaluée avant toute prolongation ou escalade. Adapter la date du contrôle à la sévérité et au terrain.')+
 '<h3>11.D — Pronostic et suivi</h3>'+paras('Les épisodes peuvent récidiver et nécessiter un entretien. Le but est un contrôle compatible avec la vie quotidienne et l’absence de complication. Une récidive ne justifie pas automatiquement la reprise d’une ancienne ordonnance.',
 'Le suivi doit être plus attentif lorsqu’une atteinte cornéenne, une maladie cutanée importante ou une difficulté d’examen chez l’enfant est présente. Confirmer que le patient sait reconnaître les signes imposant un contrôle plus tôt.'),(2,18,22,28,29,30))
l.add('La {prévention} consiste à maintenir des gestes doux et à traiter les facteurs associés. Le patient doit savoir quels soins poursuivre et quel médicament arrêter à la date prévue. Une bonne hygiène ne remplace pas l’examen d’une poussée inhabituelle.',paras(
 'Organiser une routine réaliste de nettoyage du bord et d’entretien glandulaire lorsqu’elle est indiquée. Vérifier le geste par une démonstration. Éviter eau trop chaude, frottement excessif et mélanges de produits.',
 'Revoir maquillage, démaquillage et lentilles. Ne pas partager les préparations oculaires et éviter que l’embout touche les cils. Les produits contaminés ou périmés ne sont pas réutilisés.',
 'La prise en charge d’une dermatose et d’une sécheresse doit rester cohérente avec le traitement palpébral. Informer les différents prescripteurs des produits déjà utilisés afin de limiter doublons et irritations.'),(2,6,22,29))
l.add('Les {points clés} relient le bord palpébral à la santé de la cornée. L’hygiène est centrale mais les médicaments répondent à une indication précise. L’évolution et la tolérance guident la réévaluation.',steps(
 'Distinguer forme antérieure, postérieure et mécanismes associés.',
 'Examiner la surface et mesurer la vision avant de banaliser les symptômes.',
 'Enseigner des soins doux sans brûlure ni abrasion.',
 'Réserver un antibiotique à la composante infectieuse pertinente.',
 'Ne pas transposer des traitements cutanés ou étrangers dans l’œil.',
 'Réévaluer une forme réfractaire ou unilatérale atypique.'),(2,18,22,29,30))
l.quiz([
 ('La blépharite antérieure touche-t-elle les mêmes structures que la forme postérieure ?','La première intéresse surtout la région ciliaire ; la seconde les glandes de Meibomius et leur fonctionnement. Elles peuvent coexister.'),
 ('Une sensation de sécheresse exclut-elle un larmoiement ?','Non. Une surface irritée peut provoquer un larmoiement réflexe.'),
 ('Toute blépharite nécessite-t-elle un antibiotique ?','Non. Le mécanisme et l’examen guident le traitement.'),
 ('Une douleur dans l’œil est-elle une simple gêne palpébrale à attendre ?','Non. Elle peut signaler une atteinte cornéenne ou une autre urgence.'),
 ('Pourquoi les lentilles changent-elles l’évaluation d’un œil rouge douloureux ?','Elles renforcent la nécessité d’exclure une kératite infectieuse en urgence.'),
 ('Quels gestes constituent les soins de base décrits par HUG ?','Chaleur confortable, massage doux adapté et nettoyage du bord avec les mains propres.'),
 ('Faut-il arrêter tous les soins quand les croûtes disparaissent ?','Non. Un entretien peut rester utile, tandis que l’antibiotique garde la durée prescrite.'),
 ('Quelle durée de tobramycine propose HUG pour la composante infectieuse antérieure ?','Dix jours ; cette durée vient du guide, pas d’une durée spécifique de la notice suisse.'),
 ('Quelle forme de Tobrex est décrite dans la fenêtre de dose ?','La pommade ophtalmique à 3 mg/g, autorisation 45508, distincte du collyre 44538.'),
 ('Le seuil général de deux mois autorise-t-il le collyre au bore chez un nourrisson ?','Non. Le collyre a des restrictions spécifiques plus strictes.'),
 ('Une démangeaison démontre-t-elle Demodex responsable ?','Non. Une évaluation adaptée est nécessaire.'),
 ('Peut-on utiliser de l’huile essentielle pure dans l’œil ?','Non. Les traitements ciblés doivent être adaptés à l’usage ophtalmique et prescrits de façon sûre.'),
 ('Que faire devant une réaction d’hypersensibilité à la tobramycine ?','Arrêter le produit ; évaluer immédiatement toute réaction respiratoire ou généralisée.'),
 ('Que signifie une atteinte unilatérale persistante avec perte de cils ?','Il faut rechercher une autre lésion, notamment tumorale, au lieu de renouveler indéfiniment un topique.')
 ],(2,5,18,22,28,29,30))
l.write()
