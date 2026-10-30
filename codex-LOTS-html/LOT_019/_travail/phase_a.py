from format_lecon import Lesson,paras,table,steps
from diagnostics import comparison
l=Lesson('Altération de la voix : enrouement, aphonie, dysphonie')
l.add('La dysphonie est une modification de la hauteur, de l’intensité ou du timbre de la voix. Les {distinctions sémiologiques} la séparent des troubles du langage et de l’articulation. Une plainte vocale doit aussi faire vérifier la respiration et la déglutition.',
 paras('La voix est le son produit par la vibration des plis vocaux, modulé par les cavités de résonance. La parole organise ce son en mots articulés ; le langage permet de comprendre et de formuler un message. Un patient peut présenter plusieurs troubles à la fois.',
 'L’enrouement décrit souvent une voix rauque ; la dysphonie est un terme plus large. Une aphonie correspond à la perte de la voix sonore, tandis qu’une hypophonie est une réduction de son intensité. Le degré de gêne dépend aussi du métier et des besoins de communication.')+
 table(['Plainte','Vérification','Conséquence'],[
 ['Voix rauque ou soufflée.','Faire parler puis tenir une voyelle, sans forcer.','Explorer le larynx selon durée, signes associés et contexte.'],
 ['Mots déformés.','Évaluer articulation, langue, voile et motricité.','Rechercher une dysarthrie et une cause neurologique.'],
 ['Mots manquants ou compréhension altérée.','Évaluer compréhension et production du langage.','Un début aigu impose la filière neurologique urgente.'],
 ['Voix nasale.','Rechercher trouble de résonance et fuite vélopharyngée.','Ne pas attribuer automatiquement le trouble aux cordes vocales.']]),(1,6,7))
l.add('Les causes et le retentissement varient selon l’âge, le tabagisme et l’usage de la voix. Les {repères de population} aident à sélectionner les hypothèses sans établir un classement universel. Aucune incidence suisse comparable de ce symptôme composite n’a été trouvée dans les sources consultées.',
 paras('Les HUG décrivent notamment une fatigue vocale chez les enseignants, les chanteurs et les autres professionnels de la voix. Cette exposition peut orienter vers un forçage, mais n’exclut ni lésion organique ni paralysie.',
 'Chez l’enfant, une altération durable de la voix ou du cri exige une évaluation adaptée ; des lésions bénignes, une papillomatose ou une anomalie de mobilité sont possibles. Chez l’adulte exposé au tabac, une dysphonie persistante doit faire rechercher une lésion maligne. Une voix modifiée avec l’âge ne se réduit pas d’emblée au vieillissement.',
 'L’ordre des dix diagnostics retenus dans ce cours est pédagogique. Les sources ne donnent pas une distribution suisse permettant de les classer tous par prévalence. Le retentissement professionnel, social et émotionnel doit être décrit, même lorsqu’une lésion menace peu la survie.'),(1,2,3,5))
l.add('Le larynx assure le passage de l’air, la production vocale et une partie de la protection des voies respiratoires. Les {bases de la phonation} relient souffle, fermeture et vibration. Une anomalie de mobilité n’est pas la même chose qu’une anomalie de la muqueuse.',
 paras('Pendant la respiration, les plis vocaux s’écartent ; pendant la phonation, ils se rapprochent et le flux expiratoire entretient leur vibration. La qualité du son dépend de leur fermeture, de leur symétrie, de leur souplesse et de la coordination avec le souffle. La protection contre les fausses routes engage plusieurs structures et ne se résume pas à la voix.',
 'Le nerf récurrent, branche du nerf vague, assure l’essentiel de la commande motrice des muscles intrinsèques du larynx. Son trajet gauche descend dans le thorax avant de remonter ; une cause cervicale ou thoracique peut donc provoquer une dysphonie. Ne pas attribuer toute paralysie au nerf laryngé supérieur.',
 'La muqueuse doit pouvoir glisser sur les plans profonds pour vibrer. L’espace de Reinke contribue à cette souplesse. Une masse, un œdème ou une cicatrice change la vibration ; une fuite glottique augmente la perte d’air et donne souvent une voix soufflée.')+
 table(['Mécanisme','Signe possible','Examen utile'],[
 ['Fermeture incomplète.','Voix faible, soufflée, fatigue.','Visualisation en respiration et phonation.'],
 ['Muqueuse épaissie ou irrégulière.','Voix rauque ou instable.','Laryngoscopie, puis stroboscopie si indiquée.'],
 ['Contraction excessive ou incoordonnée.','Effort vocal ou interruptions.','Examen phoniatrique avec tâches vocales variées.'],
 ['Ouverture insuffisante des deux plis.','Dyspnée inspiratoire, parfois voix conservée.','Évaluation urgente des voies aériennes.']]),(6,7))
l.add('Le tri recherche d’abord une menace respiratoire ou une atteinte neurologique aiguë. Les {situations graves à exclure} précèdent l’analyse esthétique ou professionnelle de la voix. Une voix presque normale ne protège pas d’une obstruction laryngée.',
 table(['Priorité','Signaux','Conduite'],[
 ['🚩 E1 — Obstruction des voies aériennes.','Stridor, tirage, dyspnée, difficulté à gérer les sécrétions ou aggravation rapide.','Appel urgent à une équipe capable de sécuriser les voies aériennes ; ne pas retarder pour une exploration vocale.'],
 ['🚩 E2 — Trouble neurologique aigu.','Trouble soudain du langage, articulation altérée, déficit focal ou déglutition perturbée.','Filière neurologique urgente ; ne pas confondre dysphonie et aphasie.'],
 ['🚩 E3 — Fausses routes importantes.','Toux aux liquides, repas impossibles, encombrement ou pneumopathie suspectée.','Évaluer la sécurité de déglutition et les besoins respiratoires/nutritionnels.'],
 ['🚩 E4 — Lésion tumorale ou paralysie inexpliquée.','Persistance, progression, tabac, masse cervicale, otalgie ou lésion suspecte.','Examen ORL accéléré ; biopsie ou exploration étiologique selon la lésion.'],
 ['🚩 E5 — Complication après chirurgie, intubation ou traumatisme.','Début après geste cervical/thoracique, douleur ou modification respiratoire.','Rechercher lésion mécanique, œdème, hématome ou paralysie selon contexte.']])+
 paras('Ces priorités ne sont pas un score validé. Le délai dépend de la gravité constatée. Une dysphonie aiguë après effort vocal peut aussi correspondre à une lésion du pli vocal ; éviter de poursuivre le forçage avant évaluation si la gêne est importante.')+comparison(),(2,3,4,5,6,7,8))
l.add('L’anamnèse précise la chronologie, les circonstances et le retentissement. Les {questions discriminantes} recherchent l’exposition vocale, les lésions et les causes neurologiques. La durée seule ne suffit pas à décider de l’urgence.',
 table(['Question','Pourquoi','Ce que cela change'],[
 ['Quand et comment la voix a-t-elle changé ?','Installation brutale, progressive ou intermittente orientent différemment.','Comparer épisode infectieux, effort, chirurgie et évolution.'],
 ['Dyspnée, bruit inspiratoire, fausses routes ou salive difficile à avaler ?','Les fonctions vitales du larynx peuvent être atteintes.','Prioriser respiration et déglutition.'],
 ['Tabac, alcool, perte de poids, otalgie ou masse du cou ?','Rechercher une cause tumorale.','Accélérer la visualisation et le bilan.'],
 ['Intubation ou chirurgie de la tête, du cou ou du thorax ?','Lésion muqueuse, articulaire ou nerveuse possible.','Rechercher un lien chronologique sans conclure trop vite à une paralysie.'],
 ['Usage professionnel, cris, chant ou difficulté liée à une tâche ?','Forçage et dystonie peuvent dépendre du contexte.','Évaluer demandes et tâches déclenchantes.'],
 ['Traitements, inhalations, maladies neurologiques ou fatigabilité ?','Causes irritatives, motrices et neuromusculaires possibles.','Réviser le traitement et cibler le bilan.'],
 ['Quel retentissement sur travail et communication ?','La plainte ne se réduit pas au son entendu.','Fixer un objectif fonctionnel avec le patient.']]),(1,2,6,7,8))
l.add('L’examen commence par l’état respiratoire, puis écoute la voix et examine le cou et les nerfs crâniens. Les {gestes et leurs limites} orientent l’examen laryngé. Un examen de la bouche normal ne permet pas de conclure que le larynx est sain.',
 table(['Geste','Constat recherché','Interprétation'],[
 ['Observer la respiration au repos et pendant la parole.','Tirage, bruit inspiratoire, effort et capacité à parler.','Priorité vitale si obstruction suspectée ; une bonne voix n’exclut pas une immobilité bilatérale.'],
 ['Écouter parole spontanée et voyelle tenue si toléré.','Raucité, souffle, faible intensité, interruptions et fatigue.','Décrire le phénomène ; le timbre ne prouve pas une étiologie.'],
 ['Inspecter bouche, langue et voile.','Anomalie muqueuse, asymétrie ou trouble moteur.','Différencier résonance, articulation et atteinte des nerfs crâniens.'],
 ['Palper cou, thyroïde et aires ganglionnaires.','Masse, adénopathie, cicatrice ou anomalie des reliefs.','Orienter le bilan tumoral ou postopératoire.'],
 ['Visualiser le larynx par un examen adapté.','Muqueuse, mobilité en ouverture et fermeture, symétrie.','Identifier lésion ou immobilité ; documenter un examen incomplet.'],
 ['Compléter l’examen neurologique si indiqué.','Atteinte focale, mouvements anormaux, fatigabilité ou syndrome associé.','Adapter l’imagerie et l’orientation spécialisée.']])+
 paras('L’examen spécialisé peut employer miroir, optique rigide ou nasofibroscope selon les possibilités. En situation de détresse respiratoire, les explorations sont coordonnées avec l’équipe des voies aériennes ; elles ne doivent pas désorganiser la prise en charge urgente.'),(6,7))
l.add('Les {syndromes vocaux et laryngés} réunissent les symptômes et les constatations physiques. Ils orientent sans remplacer le diagnostic de cause. La même maladie peut perturber plusieurs fonctions.',
 table(['Syndrome','Signes fonctionnels','Signes physiques et mécanisme'],[
 ['7.1 — Inflammatoire aigu.','Enrouement récent, contexte infectieux ou irritatif.','Muqueuse inflammatoire ; rechercher une menace respiratoire associée.'],
 ['7.2 — Lésionnel chronique.','Voix durablement rauque ou instable.','Masse, épaississement ou irrégularité modifiant la vibration.'],
 ['7.3 — Insuffisance de fermeture.','Voix soufflée, faible, parfois fausses routes.','Fente glottique, atrophie ou immobilité selon cause.'],
 ['7.4 — Obstruction laryngée.','Dyspnée inspiratoire, stridor ; voix parfois préservée.','Ouverture insuffisante, lésion ou œdème.'],
 ['7.5 — Dysfonction du geste.','Fatigue, effort, variabilité avec l’usage.','Hyperfonction ou coordination perturbée, sans lésion suffisante pour tout expliquer.'],
 ['7.6 — Trouble neurologique de commande.','Spasmes, tremblement ou fatigabilité avec autres signes possibles.','Anomalie motrice à caractériser par examen spécialisé.']]),(1,2,3,4,6,7))
l.add('La dysphonie est reconnue cliniquement, mais sa cause demande une confrontation avec l’examen. Les {critères de confirmation} varient selon le mécanisme. Une réponse à un traitement empirique ne remplace pas une exploration justifiée.',
 paras('Une lésion visible n’est pas automatiquement la cause unique de la plainte : vérifier concordance, mobilité et état neurologique. Inversement, l’absence de masse au premier regard ne suffit pas à établir une dysphonie fonctionnelle ; certaines anomalies de vibration ou de commande demandent une exploration plus précise.',
 'Les HUG recommandent l’exploration ORL d’un enrouement de plus de trois semaines, surtout chez un fumeur. Le document ORL de 2017 propose un examen dès une persistance de huit à quinze jours. Ces repères de sources différentes ne sont pas des délais d’attente obligatoires : un signe d’alarme, une complication postopératoire ou une évolution défavorable motive une évaluation plus précoce.',
 'Le diagnostic de cancer repose sur l’histologie d’une lésion prélevée ; le diagnostic d’immobilité repose sur l’examen dynamique. L’immobilité doit ensuite être distinguée d’une paralysie nerveuse, car une fixation articulaire ou tumorale est possible.'),(3,5,6,7,8))
l.add('L’examen laryngé est au centre du bilan lorsque l’évolution ou le contexte l’exigent. Les {explorations de première et de seconde intention} répondent à une question précise. Une imagerie sans examen du larynx n’est pas le bilan standard d’une plainte vocale isolée.',
 paras('9.a — Il n’existe pas de test unique de toutes les dysphonies : examen laryngé pour la structure et la mobilité, évaluation vocale pour la fonction, histologie pour une lésion suspecte.',
 '9.b — Première intention : examen clinique et visualisation adaptée du larynx. Une lésion suspecte conduit à l’endoscopie et au prélèvement indiqués. La stroboscopie caractérise une vibration muqueuse ; elle n’est pas nécessaire pour constater une corde immobile.',
 '9.c — Adapter la méthode à la tolérance et à l’âge. Si le larynx n’est pas suffisamment visible, organiser un examen complémentaire ; ne pas considérer une vue incomplète comme un résultat normal.',
 '9.d — Une immobilité sans cause évidente justifie une exploration du trajet nerveux, de la base du crâne au thorax selon le contexte. La TDM, l’IRM, l’échographie thyroïdienne et l’EMG ont des indications distinctes ; le spécialiste choisit la technique et ses précautions.')+
 table(['Question','Examen','Limite et conséquence'],[
 ['Lésion muqueuse suspecte ?','Endoscopie et biopsie.','Un aspect rassurant isolé ne remplace pas l’histologie lorsqu’elle est indiquée.'],
 ['Vibration anormale ?','Stroboscopie.','Complément phoniatrique, sans retarder le bilan d’une lésion suspecte.'],
 ['Paralysie ou fixation ?','Examen dynamique, parfois EMG ou exploration sous anesthésie.','Interprétation spécialisée ; ne pas étiqueter toute immobilité comme neuropathie.'],
 ['Cause sur le trajet du vague/récurrent ?','Imagerie cervicale et thoracique adaptée.','Une échographie thyroïdienne seule n’explore pas tout le trajet.']]),(6,7,8))
l.add('L’{arbre de décision} traite la menace vitale avant la caractérisation de la voix. Il recherche ensuite une cause lésionnelle ou motrice. Une évolution non favorable impose de réexaminer l’hypothèse initiale.',
 steps('Si stridor, tirage, dyspnée ou aggravation rapide → prise en charge urgente des voies aériennes.',
 'Si trouble aigu du langage ou déficit neurologique → filière neurologique urgente.',
 'Si fausses routes ou déglutition non sûre → évaluation respiratoire et de déglutition, avec adaptation de l’alimentation.',
 'Si lésion suspecte, persistance ou facteur d’alarme → examen ORL et biopsie si indiquée.',
 'Si immobilité → distinguer atteinte motrice et fixation, puis rechercher la cause sur le trajet adapté.',
 'Si lésion bénigne caractérisée → traitement conservateur, logopédique ou chirurgical selon sa nature et la gêne.',
 'Si trouble fonctionnel ou dystonie probable → bilan phoniatrique et prise en charge spécifique, avec contrôle de l’évolution.'),(2,3,4,5,6,7))
l.add('La prise en charge protège d’abord la respiration et la déglutition, puis traite la cause et le handicap vocal. Les {objectifs, traitements et conditions de retour} sont adaptés au diagnostic. Les traitements empiriques ne doivent pas retarder une exploration nécessaire.',
 paras('11.A — Objectifs : assurer les fonctions vitales, identifier une affection grave et restaurer une communication utile. Une amélioration du timbre ne suffit pas à affirmer que la déglutition ou la respiration sont sûres.',
 '11.B — Une menace des voies aériennes relève immédiatement d’une équipe expérimentée ; l’intervention dépend de la cause. Une lésion suspecte demande une confirmation histologique et un parcours spécialisé. Une paralysie exige la recherche de sa cause et une appréciation des fausses routes ; la rééducation et les gestes de rapprochement du pli vocal dépendent de cette évaluation.',
 'Une laryngite aiguë simple peut relever du repos vocal adapté, de l’hydratation et de l’éviction des irritants. Les HUG indiquent que les antibiotiques sont généralement inutiles. Pour une dysphonie fonctionnelle ou certaines lésions bénignes, la logopédie travaille souffle, vibration et résonance après évaluation du larynx.',
 'Ne pas prescrire systématiquement antibiotiques, corticoïdes ou antireflux pour une dysphonie isolée non explorée. L’évocation d’un reflux ne prouve pas sa causalité. Les gestes chirurgicaux et injections spécialisées demandent une indication précise ; aucune dose n’est extrapolée entre produits.',
 '11.C — Contrôler symptômes, examen et retentissement. Une persistance, une aggravation ou de nouveaux signes respiratoires ou de déglutition imposent une réévaluation. Organiser le suivi d’une lésion traitée ou surveillée.',
 '11.D — Le retour ambulatoire suppose une situation respiratoire stable, une déglutition évaluée si nécessaire, des consignes comprises et un rendez-vous adapté. Donner les signes qui imposent un recours urgent et prévoir les adaptations professionnelles. L’absence de cause identifiée ne doit pas devenir une perte de suivi.'),(2,3,4,5,6,8))
l.add('La prévention associe réduction des irritants, usage vocal adapté et accès précoce au diagnostic. Les {mesures aux trois niveaux} dépendent du terrain. Elles ne doivent pas faire banaliser une voix durablement modifiée.',
 paras('Primaire : accompagner l’arrêt du tabac, réduire les expositions irritantes et favoriser l’hydratation et les pauses vocales adaptées aux contraintes professionnelles. Les conseils sont individualisés ; ils ne garantissent pas la prévention de toute lésion.',
 'Secondaire : consulter si la voix ne s’améliore pas ou si survient un signe d’alarme. Rechercher les complications après chirurgie ou intubation. Un examen incomplet doit être complété selon le risque.',
 'Tertiaire : suivre la rééducation, prévenir le retour au forçage, surveiller les lésions à risque et les récidives, soutenir la communication après traitement. La prise en charge du handicap reste utile même si le son ne redevient pas identique.'),(1,2,3,5,6))
l.add('Évaluer respiration et déglutition avant de traiter la voix. Visualiser le larynx lorsque la persistance ou le contexte le justifient. Une immobilité n’est pas forcément une paralysie et une voix conservée n’exclut pas une obstruction. Confirmer les lésions suspectes et assurer le suivi.',refs=(3,4,5,6,7))
l.quiz([
 ('Une aphonie est-elle une aphasie ?','Non : la première touche la voix sonore, la seconde le langage.'),
 ('Une voix presque normale exclut-elle une obstruction ?','Non : une immobilité bilatérale en fermeture peut surtout gêner la respiration.'),
 ('Pourquoi demander si les liquides font tousser ?','Une insuffisance de protection laryngée peut provoquer des fausses routes.'),
 ('Le tabac suffit-il à poser un diagnostic de cancer ?','Non : il augmente la vigilance ; la lésion suspecte doit être explorée et prélevée.'),
 ('Faut-il attendre trois semaines devant un stridor ?','Non : la menace respiratoire impose une prise en charge immédiate.'),
 ('Une bouche normale prouve-t-elle que le larynx est normal ?','Non : les cordes vocales nécessitent une visualisation adaptée.'),
 ('Quel nerf commande l’essentiel de la mobilité intrinsèque laryngée ?','Le nerf récurrent, branche du nerf vague.'),
 ('Une immobilité prouve-t-elle une lésion du nerf ?','Non : une fixation mécanique ou tumorale peut aussi immobiliser le pli vocal.'),
 ('La stroboscopie est-elle nécessaire pour constater une paralysie ?','Non : l’examen dynamique établit l’immobilité ; la stroboscopie étudie surtout la vibration.'),
 ('Une échographie thyroïdienne suffit-elle à toute paralysie inexpliquée ?','Non : le trajet nerveux peut demander une exploration plus étendue.'),
 ('Une dysphonie chez un enseignant est-elle forcément fonctionnelle ?','Non : une lésion organique ou une atteinte motrice reste possible.'),
 ('L’amélioration sous antireflux démontre-t-elle sa responsabilité ?','Non : la réponse n’est pas un test causal suffisant.'),
 ('Une laryngite aiguë impose-t-elle des antibiotiques ?','Non : elle est souvent virale ; le traitement dépend du diagnostic réel.'),
 ('Un examen mal toléré et incomplet peut-il être déclaré rassurant ?','Non : il faut documenter ses limites et organiser la suite selon le risque.')])
l.write()
