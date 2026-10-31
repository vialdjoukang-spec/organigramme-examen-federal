from format_lecon import Lesson,paras,table,steps
from tobramycine import tobrex
l=Lesson('Orgelet',1)
med=tobrex(l)
l.add('L’{orgelet} est une infection aiguë localisée d’une glande palpébrale, souvent centrée sur la racine d’un cil. Il forme un nodule douloureux et rouge. La vision doit rester préservée dans une forme superficielle simple.',paras(
 'Dans l’usage clinique français, le terme désigne surtout le furoncle du follicule d’un cil et de sa glande associée. La terminologie anglaise distingue aussi un hordeolum interne, infection d’une glande de Meibomius plus profonde. Les deux formes sont inflammatoires et douloureuses ; la localisation guide l’examen.',
 'Une petite pointe purulente peut apparaître au bord libre, mais elle peut manquer au début. Son absence ne justifie pas de presser la paupière pour la faire apparaître. Le chalazion correspond principalement à une inflammation obstructive de la glande, sans infection obligatoire.',
 'Le diagnostic est une conclusion clinique après examen. Une photographie de nodule ne renseigne pas à elle seule sur la vision, la cornée ou l’extension de l’infection.'),(1,18,20,21))
l.add('Le {contexte favorisant} inclut une inflammation du bord palpébral et une mauvaise évacuation des sécrétions glandulaires. Un premier épisode banal ne prouve pas une maladie générale. Des récidives ou un terrain fragile modifient toutefois l’évaluation.',paras(
 'L’orgelet est courant en pratique, mais les sources retenues ne donnent pas d’incidence suisse comparable permettant un classement chiffré. Aucun pourcentage de fréquence n’est attribué à ce diagnostic.',
 'Rechercher une blépharite chronique, une rosacée, une dermatite séborrhéique, des habitudes de frottement ou de manipulation des paupières. Ces observations orientent la prévention ; elles ne permettent pas d’imputer l’épisode à un défaut d’hygiène personnel.',
 'Un diabète connu, une immunodépression ou des épisodes multiples justifient une appréciation médicale plus attentive. Un bilan de diabète se décide selon l’ensemble des indices cliniques et les recommandations de dépistage, non sur tout nodule isolé.'),(10,18,23))
l.add('Les {repères glandulaires} expliquent le siège du nodule. Le follicule ciliaire est voisin des glandes de Zeis et de Moll, alors que les glandes de Meibomius occupent l’épaisseur palpébrale. Une infection locale peut produire un œdème dépassant le seul point visible.',paras(
 'Les glandes sébacées de Zeis accompagnent les cils ; les glandes de Moll sont des glandes apocrines du bord. Les glandes de Meibomius produisent la composante lipidique du film lacrymal. Leur position plus profonde explique une tuméfaction moins immédiatement centrée sur un cil dans l’hordeolum interne.',
 'La réaction inflammatoire associe rougeur, douleur et accumulation locale de pus dans le foyer infecté. Staphylococcus aureus est une cause habituelle décrite dans les textes de référence. Ce constat ne démontre pas la sensibilité de chaque souche à chaque antibiotique.',
 'Le film lacrymal est réparti par le clignement ; ses lipides limitent l’évaporation. L’entretien du bord palpébral aide à corriger un dysfonctionnement associé. Une compresse ne stérilise cependant pas une infection profonde et ne remplace pas son évaluation.'),(2,18,20,21))
l.add('La démarche commence par les {signes incompatibles avec un orgelet simple}. Une baisse visuelle, une photophobie marquée ou une douleur aux mouvements de l’œil appelle une évaluation urgente. Une rougeur diffuse fébrile doit faire rechercher une cellulite.',table(['Constat','Risque à rechercher','Décision'],[
 ['Vision diminuée, douleur oculaire ou photophobie','Atteinte cornéenne ou intraoculaire associée.','Examen ophtalmologique urgent.'],
 ['Diplopie, protrusion du globe, mouvements douloureux ou limités','Atteinte orbitaire.','Évaluation hospitalière immédiate ; ne pas attendre l’effet d’une pommade.'],
 ['Extension diffuse chaude et douloureuse, fièvre ou mauvais état général','Cellulite préseptale ou infection plus étendue.','Évaluation rapide du niveau de soins et du traitement systémique.'],
 ['Œil impossible à examiner dans un contexte suspect','Atteinte profonde non exclue.','Recours urgent à une équipe capable de compléter l’examen.'],
 ['Nodule durable ou récidivant au même endroit, perte de cils','Diagnostic tumoral ou autre masse à exclure.','Avis spécialisé et prélèvement selon l’aspect.']
 ]),(5,9,18,21))
l.add('L’{anamnèse} précise la chronologie, le siège et les symptômes oculaires. Elle recherche aussi les traitements déjà appliqués et les facteurs de risque. Le patient doit pouvoir distinguer une douleur de paupière d’une gêne ressentie dans l’œil.',steps(
 'Faire décrire le début, la progression, le point douloureux et un éventuel écoulement spontané.',
 'Demander une baisse visuelle, une gêne à la lumière, une diplopie, une douleur aux mouvements, une fièvre ou des céphalées.',
 'Rechercher lentilles, maquillage, frottement, traumatisme ou chirurgie récente, et préciser l’état de l’autre œil.',
 'Recenser récidives, blépharite, rosacée, diabète, immunodépression, allergies aux médicaments, grossesse ou allaitement.',
 'Noter les collyres, pommades et traitements généraux déjà pris, leurs effets et leur tolérance. Vérifier les possibilités de retour en consultation.'),(10,18,22,23))
l.add('L’{examen ciblé} localise le foyer et documente les fonctions oculaires. Le bord libre et la face interne de la paupière sont examinés selon la tolérance et les compétences disponibles. Aucun geste ne doit forcer l’évacuation du pus.',paras(
 'Mesurer la vision de chaque œil avec la correction habituelle et un test adapté à l’âge. Comparer pupilles, alignement et mouvements. Un examen non réalisable n’est pas enregistré comme normal.',
 'Décrire un nodule focal ou une inflammation diffuse, le rapport aux cils, une pointe purulente, des croûtes et les glandes voisines. Le praticien peut éverser doucement la paupière si nécessaire pour une lésion profonde ; ce geste n’est pas une instruction d’automanipulation.',
 'Rechercher la rougeur conjonctivale et les signes cornéens. La lampe à fente complète l’évaluation si l’œil est rouge, douloureux, photophobe ou si la vision est modifiée. La simple palpation à travers la paupière n’exclut pas une atteinte du globe.'),(8,18,20,21))
l.add('L’{approche syndromique} oppose foyer ciliaire, nodule tarsal et inflammation diffuse. Un signe isolé peut être trompeur au début. La localisation et l’évolution doivent rester cohérentes avec le diagnostic.',table(['Hypothèse','Élément utile','Conséquence'],[
 ['Orgelet externe','Nodule douloureux au bord, centré sur un cil.','Soins locaux après exclusion des complications.'],
 ['Hordeolum interne','Foyer douloureux plus profond.','Examen de la face conjonctivale et avis si doute ou persistance.'],
 ['Chalazion','Masse glandulaire souvent moins douloureuse, évolution plus prolongée.','Pas d’antibiotique automatique sur le seul nodule.'],
 ['Blépharite','Atteinte du bord plus étendue avec croûtes.','Traiter le trouble associé pour limiter les récidives.'],
 ['Dacryocystite','Douleur et gonflement près du sac lacrymal au coin interne.','Parcours infectieux et lacrymal distinct.'],
 ['Tumeur palpébrale','Lésion persistante, déformation ou perte des cils.','Ne pas multiplier les traitements empiriques.']
 ]),(1,4,5,18,20,21))
l.add('Le {diagnostic positif} est clinique dans une présentation typique. Il associe un foyer aigu douloureux à une localisation glandulaire compatible. La conservation des fonctions oculaires soutient le caractère superficiel sans remplacer le suivi.',paras(
 'Il n’existe pas de score biologique nécessaire pour confirmer un petit orgelet externe typique. Le foyer peut être vu avant que le pus soit apparent. L’apparition ultérieure d’une extension diffuse oblige à revoir le diagnostic initial.',
 'Le diagnostic ne se fonde pas sur la réponse à un antibiotique utilisé comme test. Une amélioration partielle ne dispense pas de réexaminer une masse qui persiste. Une forme interne ou atypique peut nécessiter un ophtalmologue pour distinguer abcès, chalazion et autre lésion.',
 'Une tuméfaction sans foyer identifiable, accompagnée d’un prurit dominant ou d’un œdème bilatéral, invite à reprendre le raisonnement présenté dans le cours général.'),(18,19,20,21))
l.add('Les {examens complémentaires} sont ciblés sur les formes inhabituelles ou compliquées. Une imagerie ou une prise de sang n’est pas un préalable aux soins d’un foyer typique. Leur indication apparaît si l’examen suggère une autre maladie ou une extension.',
 '<h3>9.a — Référence diagnostique</h3>'+paras('L’examen clinique et, selon les symptômes, la lampe à fente constituent la base du diagnostic. Il n’existe pas de test sanguin confirmant à lui seul l’orgelet.')+
 '<h3>9.b — Première intention</h3>'+paras('Dans un cas localisé avec vision et motilité conservées, documenter l’examen et l’évolution prévue. Un prélèvement systématique de la surface n’est pas nécessaire pour un premier épisode simple.')+
 '<h3>9.c — Alternatives selon le risque</h3>'+paras('Une suspicion orbitaire ou un examen impossible en contexte infectieux impose le parcours hospitalier décrit dans le cours général, avec imagerie selon l’équipe. Elle ne doit pas attendre un prélèvement local ou un essai prolongé de pommade.')+
 '<h3>9.d — Seconde intention</h3>'+paras('Un abcès nécessitant un geste peut être prélevé pour culture selon l’ophtalmologue. Devant échec, récidives ou terrain fragile, reprendre diagnostic, traitements et facteurs favorisants. Une masse atypique relève d’une analyse tissulaire si le spécialiste la juge nécessaire ; une culture négative ne prouve pas sa bénignité.'),(5,9,18,21))
l.add('L’{arbre décisionnel} suit la gravité puis le caractère localisé. Les soins débutent après un examen rassurant. L’absence d’amélioration conduit à un nouveau diagnostic de situation.',steps(
 'Si signe visuel, orbitaire, cornéen ou altération générale, alors demander l’évaluation urgente adaptée.',
 'Si extension diffuse compatible avec cellulite, alors évaluer une antibiothérapie systémique ; le topique seul est insuffisant.',
 'Si foyer localisé typique et fonctions préservées, alors expliquer soins doux, arrêt temporaire des lentilles et consignes de retour.',
 'Si orgelet franc pour lequel un antibiotique local est retenu, alors choisir la forme ophtalmique et vérifier indication, âge et contre-indications.',
 'Si aggravation à tout moment ou absence d’amélioration après trois jours de traitement, alors organiser un avis ophtalmologique selon HUG.',
 'Si collection résistante ou lésion enkystée, alors le spécialiste discute un geste ; si masse persistante atypique, alors caractériser sa nature.'),(10,18,19,22))
l.add('La {prise en charge suisse} associe soins doux et suivi de l’évolution. Un antibiotique ophtalmique est retenu après évaluation de l’indication, avec contrôle de sa forme et de ses restrictions. Une extension infectieuse ou un signe visuel change immédiatement le parcours.',
 '<h3>11.A — But</h3>'+paras('Soulager la douleur locale, favoriser l’évacuation spontanée et préserver la surface oculaire. Confirmer que la lésion reste superficielle au cours du suivi.')+
 '<h3>11.B — Moyens</h3>'+paras('Se laver les mains puis appliquer une compresse propre, agréablement chaude et non brûlante sur l’œil fermé. Le conseil public britannique propose cinq à dix minutes, deux à quatre fois par jour. Adapter la tolérance, particulièrement chez l’enfant ; ne pas chercher une température maximale.',
 'Ne pas percer, écraser ou arracher soi-même le cil. Une mobilisation douce du bord éventuellement expliquée par le soignant n’est pas une pression sur un abcès. Éviter maquillage et lentilles pendant l’épisode.',
 'Les références diffèrent sur l’usage systématique d’un antibiotique : HUG propose une pommade de tobramycine pour l’orgelet franc ; les conseils français et britanniques réservent les topiques à certaines situations. Une petite lésion favorable sous soins n’impose donc pas une automédication antibiotique. Le prescripteur confirme l’intérêt et suit la réponse.')+med+paras(
 'Ne pas ajouter empiriquement une association antibiotique–corticoïde. Un corticoïde oculaire demande un examen spécialisé, notamment pour écarter une infection cornéenne. La pommade Tobrex décrite ici contient de la tobramycine seule ; elle n’est pas interchangeable avec une association.',
 'Une forme résistante ou enkystée peut nécessiter une incision sous anesthésie locale par l’ophtalmologue. Le geste se décide après réexamen ; aucune technique d’incision à domicile n’est indiquée. Une cellulite relève de son traitement systémique, au-delà de cette monographie du foyer localisé.')+
 '<h3>11.C — Surveillance</h3>'+paras('Suivre douleur, extension, état général et vision. Reconsulter immédiatement si apparition d’un signe d’alarme. Le délai de trois jours indiqué par HUG pour une absence d’amélioration sous traitement est un seuil de réévaluation, jamais une période d’attente en cas d’aggravation.')+
 '<h3>11.D — Pronostic et suivi</h3>'+paras('L’évolution est souvent spontanément favorable en quelques jours. Si le nodule demeure, revoir sa localisation et son caractère infectieux plutôt que prolonger automatiquement le topique. La prévention traite une blépharite associée ; elle ne garantit pas l’absence de récidive.'),(10,18,19,20,22,23))
l.add('La {prévention} vise les manipulations et les facteurs palpébraux associés. Les soins doivent rester compatibles avec l’état de la cornée. Une récidive appelle une réévaluation du terrain et du diagnostic.',paras(
 'Se laver les mains avant les soins et éviter le frottement des yeux. Ne pas partager serviettes, maquillage ni produits ophtalmiques. Remplacer les cosmétiques contaminés ou trop anciens et respecter l’hygiène des lentilles après guérison.',
 'Un entretien doux du bord peut être indiqué en cas de blépharite ou de dysfonction des glandes. Demander un avis avant ces soins en cas de maladie cornéenne ou de chirurgie oculaire récente. Les compresses trop chaudes exposent à une brûlure.',
 'Ne pas conserver un antibiotique ouvert pour traiter tous les épisodes ultérieurs. Une masse au même emplacement, surtout avec perte de cils, doit être réexaminée même si elle avait initialement été appelée orgelet.'),(2,5,22,23))
l.add('Les {points clés} associent localisation précise et surveillance des fonctions oculaires. Une forme simple se traite sans geste agressif. Toute évolution discordante justifie une réévaluation.',steps(
 'Identifier le foyer glandulaire et vérifier que la vision reste conservée.',
 'Rechercher une cellulite, une atteinte du globe et une lésion atypique.',
 'Proposer chaleur douce et hygiène sans perçage ni pression forcée.',
 'Si un topique est indiqué, distinguer pommade, collyre et produit avec corticoïde.',
 'Vérifier les restrictions pédiatriques propres à la forme choisie.',
 'Prévoir le contrôle et expliquer les signes imposant un retour avant celui-ci.'),(10,18,20,22,23))
l.quiz([
 ('Une pointe purulente est-elle indispensable au début ?','Non. Le foyer peut être inflammatoire avant que les sécrétions deviennent visibles.'),
 ('Quelle glande est atteinte dans un hordeolum interne ?','Une glande de Meibomius ; l’externe intéresse le follicule ciliaire et ses glandes associées.'),
 ('Une baisse visuelle est-elle attendue dans un orgelet superficiel simple ?','Non. Elle impose une évaluation oculaire urgente.'),
 ('Un gonflement sans nodule suffit-il au diagnostic ?','Non. Il faut envisager les autres causes, notamment blépharite, conjonctivite ou cellulite.'),
 ('Faut-il presser une pointe blanche pour vider le foyer ?','Non. Une manipulation peut propager l’infection et léser les tissus.'),
 ('Un collyre seul traite-t-il une cellulite orbitaire ?','Non. Le parcours hospitalier et l’antibiothérapie systémique sont nécessaires.'),
 ('Quel numéro Swissmedic correspond à Tobrex pommade ?','45508 ; le collyre porte le numéro 44538 et ses restrictions diffèrent.'),
 ('Quelle dose de pommade cite la notice pour une infection légère à modérée ?','Environ1,5cm dans le sac conjonctival de l’œil atteint, deux à trois fois par jour.'),
 ('Les sept jours de traitement d’orgelet viennent-ils de l’AIPS ?','Non. Ce repère vient de la stratégie HUG 2025 ; la notice ne fixe pas cette durée spécifique.'),
 ('Le seuil pédiatrique de deux mois permet-il d’utiliser le collyre chez tout nourrisson ?','Non. Les restrictions liées au bore du collyre priment : pas avant deux ans, ni avant douze ans pour une infection grave.'),
 ('La pommade est-elle recommandée avant deux mois ?','Non. L’expérience documentée est limitée et la notice ne la recommande pas.'),
 ('Peut-on ajouter un corticoïde oculaire sans examen ?','Non. Le spécialiste doit notamment écarter une infection de la cornée.'),
 ('Quand réévaluer un traitement sans amélioration selon HUG ?','Après trois jours ; toute aggravation ou signe visuel impose un avis plus tôt.'),
 ('Une masse récidivant avec perte de cils se traite-t-elle toujours comme un orgelet ?','Non. Une caractérisation spécialisée et éventuellement un prélèvement sont nécessaires.')
 ],(10,18,20,21,22,23))
l.write()
