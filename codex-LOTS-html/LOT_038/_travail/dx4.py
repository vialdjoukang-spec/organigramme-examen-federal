from format_lecon import Lesson,paras,table,steps,ABBR
ABBR["EXP"]="date de péremption"
from hydrocortisone_oculaire import hydrocortisone
l=Lesson('Dermatite de contact palpébrale',4)
med=hydrocortisone(l)
l.add('La {dermatite de contact palpébrale} est une inflammation de la peau des paupières liée à une exposition. Elle peut relever d’une irritation directe ou d’une allergie retardée. Une même apparence ne permet pas de distinguer ces mécanismes sans enquête.',paras(
 'La peau devient prurigineuse, rouge, squameuse ou vésiculeuse, avec un gonflement parfois marqué. Les lésions peuvent être bilatérales ou asymétriques selon le contact. Une dermatite atopique ou séborrhéique peut coexister et modifier la présentation.',
 'Le contact peut être direct, par un cosmétique ou un collyre, ou indirect par les doigts après manipulation d’un autre produit. Une substance aéroportée peut également atteindre les paupières. L’absence de nouveau produit appliqué directement sur l’œil n’exclut donc pas le mécanisme.',
 'L’allergie de contact nécessite une sensibilisation préalable. L’irritation endommage la barrière cutanée sans supposer cette sensibilisation. Les deux peuvent se favoriser mutuellement.'),(6,11,31))
l.add('Le {contexte d’exposition} guide davantage que l’intensité du gonflement. Les paupières sont sensibles aux produits irritants et allergisants. Un produit longtemps bien toléré peut devenir pertinent dans l’enquête.',paras(
 'Aucune prévalence suisse comparée n’est attribuée à cette monographie. L’importance clinique réside dans l’identification d’une cause évitable et dans le risque de répéter le contact sans le reconnaître.',
 'Recenser maquillage, démaquillant, crème, parfum, teinture capillaire, produits des ongles, collyres et solutions de lentilles. Les substances sont parfois transférées depuis les mains. Une modification de formulation ou une sensibilisation progressive peut expliquer un épisode malgré une marque déjà connue.',
 'Le travail et les loisirs comptent autant que les soins du visage. Les HUG proposent un bilan des dermatoses professionnelles lorsque le contexte le justifie. La médecine du travail peut contribuer à rechercher et réduire l’exposition sans attribution causale prématurée.'),(6,11,31))
l.add('Les {mécanismes cutanés} expliquent le délai et la récidive. L’irritation fragilise la barrière de la peau, tandis que l’allergie implique une mémoire immunitaire. Le gonflement palpébral peut être important sans atteinte de l’orbite.',paras(
 'L’épiderme limite habituellement la pénétration des substances. Nettoyants agressifs, frottements et autres irritants peuvent altérer cette barrière. Une peau atopique ou déjà inflammatoire tolère moins bien les expositions répétées.',
 'Dans l’allergie de contact, certains lymphocytes gardent la mémoire de la substance après sensibilisation. Une nouvelle exposition provoque une réaction retardée ; le document Ameli décrit habituellement un délai de vingt-quatre à quarante-huit heures. Ce repère ne prouve ni n’exclut à lui seul l’allergène.',
 'La finesse de la peau palpébrale explique sa vulnérabilité et la prudence nécessaire avec les topiques. La localisation visible ne correspond pas toujours au lieu du premier contact, par exemple avec un produit des ongles transféré par la main.',
 'Le prurit pousse au frottement, qui entretient l’irritation. Rompre ce cercle demande une éviction pertinente et des soins tolérés, pas une accumulation de crèmes.'),(11,17,31))
l.add('La démarche écarte les {urgences qui peuvent ressembler à une dermatite}. Une douleur oculaire, une vision modifiée ou une photophobie nécessite un examen. Une atteinte infectieuse ou une réaction respiratoire ne se traite pas comme un simple eczéma.',table(['Constat','Risque','Conduite'],[
 ['Douleur dans l’œil, photophobie ou baisse visuelle','Cornée ou autre structure oculaire atteinte.','Avis ophtalmologique urgent.'],
 ['Fièvre, rougeur chaude douloureuse diffuse, extension rapide','Cellulite ou surinfection.','Évaluation rapide et traitement adapté.'],
 ['Vésicules douloureuses ou lésions infectieuses suspectes','Herpès ou autre infection à préciser.','Examen rapide avant tout corticoïde local.'],
 ['Lèvres/langue gonflées, dyspnée ou malaise','Angio-œdème ou réaction systémique.','Parcours urgent du cours général, appel 144 si menace vitale.'],
 ['Diplopie, exophtalmie, douleur aux mouvements','Atteinte orbitaire.','Évaluation hospitalière immédiate.']
 ]),(9,16,17,18,31,32))
l.add('L’{anamnèse d’exposition} doit être précise et ouverte. Elle recherche les produits directs, indirects et professionnels. Le calendrier des symptômes aide à établir une relation, sans transformer une simple coïncidence en diagnostic.',steps(
 'Noter date de début, évolution, prurit ou brûlure, aspect des lésions et atteinte d’autres zones cutanées.',
 'Reconstituer les produits utilisés sur le visage, les cheveux, les mains et les ongles, y compris les changements récents de composition.',
 'Lister les collyres, pommades, solutions de lentilles et médicaments locaux, avec leurs emballages ou compositions.',
 'Rechercher expositions au travail, aérosols, parfums, loisirs et transfert par les doigts. Comparer les jours exposés et les périodes d’éloignement.',
 'Préciser antécédents atopiques, allergies connues, traitements précédents et aggravation éventuelle après une crème.',
 'Demander signes oculaires, douleur, fièvre et symptômes respiratoires, puis apprécier la possibilité d’éviction et de suivi.'),(6,11,17,31))
l.add('L’{examen} sépare les lésions de peau de l’atteinte du bord et de la conjonctive. Il recherche une surinfection et documente la vision. L’aspect cutané seul ne confirme pas l’allergène responsable.',paras(
 'Observer rougeur, squames, fissures, vésicules, suintement et traces de grattage. Préciser les zones épargnées et les lésions ailleurs, notamment mains, visage, cuir chevelu et autres régions symptomatiques.',
 'Examiner les cils, les glandes et le bord pour une blépharite associée. Rechercher une rougeur conjonctivale et des signes cornéens. Une vision diminuée, une douleur ou une photophobie exige un examen ophtalmologique adapté.',
 'Des croûtes purulentes ou une extension douloureuse ne sont pas assimilées à une simple poussée allergique. La température et l’état général sont évalués si une infection est possible.',
 'Décrire les observations et les produits suspects sans inscrire une allergie médicamenteuse comme certaine avant interprétation. Un antécédent clairement documenté est en revanche pris en compte immédiatement.'),(6,17,18,31))
l.add('L’{approche syndromique} distingue eczéma, inflammation du bord et gonflement profond. Le prurit oriente mais n’est pas spécifique. Des mécanismes associés sont possibles.',table(['Hypothèse','Indices','Suite'],[
 ['Dermatite irritative','Exposition agressive, brûlure ou irritation, barrière altérée.','Réduire le contact et restaurer des soins tolérés.'],
 ['Dermatite allergique de contact','Épisodes retardés après exposition pertinente.','Enquête puis tests épicutanés si indiqués.'],
 ['Dermatite atopique','Contexte et lésions compatibles au-delà du contact ponctuel.','Prise en charge du terrain, sans exclure une allergie associée.'],
 ['Blépharite ou dermatite séborrhéique','Bord et cils prédominants, croûtes ou squames.','Évaluer glandes et surface oculaire.'],
 ['Conjonctivite allergique','Prurit oculaire, larmoiement et conjonctive atteinte.','Traitement conjonctival distinct, mécanisme souvent immédiat.'],
 ['Angio-œdème','Gonflement profond sans tableau eczémateux typique.','Rechercher autres localisations et menace des voies aériennes.']
 ]),(6,11,16,18,31))
l.add('Le {diagnostic positif} associe une dermatite compatible et une exposition plausible. L’allergie retardée peut être confirmée par des tests épicutanés. Leur résultat doit correspondre à une exposition pertinente pour expliquer la maladie.',paras(
 'L’amélioration après éviction soutient l’hypothèse sans identifier toujours une substance unique. Plusieurs produits peuvent partager un même composant. Un traitement anti-inflammatoire peut améliorer diverses dermatoses sans prouver le mécanisme allergique.',
 'Un test positif indique une sensibilisation à interpréter avec la composition des produits et la chronologie. Il ne signifie pas que toutes les lésions présentes sont causées par cet allergène. Un bilan négatif peut laisser ouverte une irritation ou une substance non testée.',
 'Ne pas confondre tests épicutanés de réaction retardée et tests d’allergie immédiate. Une prise de sang ou un test immédiat isolé ne remplace pas l’enquête de contact.'),(6,11))
l.add('Les {examens complémentaires} sont guidés par l’évolution et l’enquête. Les tests épicutanés sont utiles si une allergie de contact est suspectée. Ils se font sur un site adapté et sous supervision, pas par réapplication sur la paupière.',
 '<h3>9.a — Référence pour l’allergie retardée</h3>'+paras('Les tests épicutanés recherchent une sensibilisation de contact. Le dermatologue choisit la série et les substances complémentaires selon les produits réellement rencontrés. La pertinence du résultat reste une conclusion clinique.')+
 '<h3>9.b — Première intention</h3>'+paras('Examiner peau et œil, recueillir les compositions et organiser l’éviction des produits non indispensables suspects. Il n’existe pas d’analyse sanguine unique validant toute dermatite palpébrale.')+
 '<h3>9.c — Organisation du bilan</h3>'+paras('Aux HUG, le parcours décrit pose les tests dans le dos le lundi, les retire le mercredi et interprète les réactions le vendredi. Ce calendrier illustre plusieurs lectures d’une réaction retardée, non une unique lecture immédiate. L’équipe donne les consignes de protection du dos, d’activité et d’exposition solaire.',
 'La brochure HUG demande de reporter ces tests après l’accouchement pendant une grossesse. Les médicaments et la situation cutanée pouvant influencer le bilan sont discutés avec l’équipe ; ne pas modifier seul un traitement pour préparer les tests.')+
 '<h3>9.d — Seconde intention</h3>'+paras('Une infection, une atteinte du globe ou une lésion atypique persistante suit son bilan spécifique. Une éviction inefficace impose de revoir composition, contact indirect, mécanisme et diagnostic. Les essais d’application éventuels se décident avec le spécialiste, jamais sur l’œil à domicile.'),(6,17,18,31))
l.add('L’{arbre décisionnel} commence par la sécurité oculaire et les signes systémiques. Il passe ensuite à l’enquête et à l’éviction. Le traitement de l’inflammation accompagne cette démarche sans la remplacer.',steps(
 'Si atteinte visuelle, douleur oculaire, infection suspecte ou réaction systémique, alors orienter selon l’urgence.',
 'Si dermatite localisée sans alarme, alors identifier les produits suspects et arrêter les expositions non indispensables.',
 'Si un médicament oculaire indispensable est suspect, alors contacter son prescripteur pour une substitution sûre plutôt qu’interrompre durablement sans solution.',
 'Si l’inflammation exige un médicament, alors choisir une spécialité adaptée au site, à l’âge et au mécanisme après examen.',
 'Si persistance ou récidive, alors organiser un bilan dermatologique de contact et vérifier les expositions indirectes.',
 'Après identification pertinente, alors remettre une liste d’éviction compréhensible et suivre l’évolution.'),(6,11,17,18,31,32))
l.add('La {prise en charge suisse} associe éviction pertinente et soins cutanés tolérés. Un corticoïde sur la paupière nécessite une indication, une durée et une surveillance adaptées. L’absence d’amélioration impose de rechercher une exposition persistante, une réaction au traitement ou un autre diagnostic.',
 '<h3>11.A — But</h3>'+paras('Interrompre l’exposition responsable, apaiser l’inflammation et restaurer la barrière cutanée. Protéger l’œil et éviter que le traitement ajoute un nouvel allergène ou masque une infection.')+
 '<h3>11.B — Moyens</h3>'+paras('Suspendre les cosmétiques et produits non essentiels suspects. Privilégier une routine simple avec un soin émollient choisi pour sa tolérance et sa composition, en évitant les parfums et le frottement. Aucun produit dit naturel n’est présumé non allergisant.',
 'Pour un collyre indispensable, contacter rapidement le prescripteur afin de chercher une alternative compatible avec la maladie oculaire. L’éviction d’un conservateur suspect ne se résume pas à supprimer sans relais un traitement de fond.',
 'Une inflammation allergique palpébrale non infectieuse de l’adulte peut relever d’une courte corticothérapie choisie après examen. La spécialité suivante fournit un exemple suisse documenté, avec ses restrictions propres :')+med+paras(
 'La forme irritative repose d’abord sur la réduction de l’agression et des soins tolérés. Elle n’est pas assimilée automatiquement à l’indication allergique de cette pommade. Chez l’enfant et l’adolescent, une alternative adaptée doit être déterminée ; la notice adulte ne sert pas de schéma pédiatrique.',
 'Les inhibiteurs topiques de la calcineurine sont des options discutées par le dermatologue dans certains eczémas. Ils ne sont pas prescrits ici comme traitements autorisés de toute dermatite de contact : indication suisse, âge et usage éventuel hors information professionnelle doivent être vérifiés pour le produit choisi.',
 'Ne pas ajouter un antibiotique en l’absence d’infection ni prolonger un corticoïde pour masquer une récidive. La recherche de l’allergène et son éviction restent nécessaires. Une surinfection demande un traitement spécifique après réévaluation.')+
 '<h3>11.C — Surveillance</h3>'+paras('Contrôler lésions, prurit, tolérance et symptômes oculaires. Une aggravation après application peut correspondre à un excipient allergisant. Sous corticothérapie, respecter les contrôles oculaires du produit, en particulier pression et cornée.',
 'Consulter rapidement si douleur, vision floue persistante, fièvre, vésicules douloureuses, sécrétions purulentes ou extension. Un traitement efficace ne dispense pas de résoudre la question de l’exposition.')+
 '<h3>11.D — Pronostic et suivi</h3>'+paras('L’évolution est favorable lorsque l’exposition pertinente cesse et que le traitement est adapté. La sensibilisation peut persister et permettre des récidives au prochain contact. La liste d’éviction doit tenir compte des synonymes et des produits professionnels réellement utilisés.',
 'En cas de persistance, revoir aussi une irritation par les soins eux-mêmes, une dermatose associée et une atteinte conjonctivale. L’objectif n’est pas une succession indéfinie de cures sans diagnostic.'),(6,11,17,18,31,32))
l.add('La {prévention} repose sur une éviction compréhensible et réaliste. Elle tient compte des contacts indirects et du travail. Un traitement antérieur bien toléré ne doit pas être réutilisé sans vérifier la cause du nouvel épisode.',paras(
 'Conserver la liste des substances pertinentes avec les conseils de l’équipe. Lire les compositions lors d’un changement de produit ou de formulation. Signaler l’allergie documentée aux professionnels concernés.',
 'Réduire le transfert par les mains depuis produits des ongles, cheveux ou activités professionnelles. Les mesures de protection doivent être adaptées à la substance et ne pas créer elles-mêmes une irritation.',
 'Ne pas tester un produit suspect directement sur la paupière. Ne pas multiplier les crèmes ni employer une ancienne ordonnance pour des lésions seulement ressemblantes. Prévoir le contrôle si l’éviction ne suffit pas.'),(6,17,31))
l.add('Les {points clés} distinguent irritation, allergie retardée et atteinte oculaire. Le bilan de contact accompagne le traitement. Les restrictions du médicament choisi priment sur une généralisation à toute la classe.',steps(
 'Rechercher les expositions directes, indirectes et professionnelles.',
 'Ne pas assimiler gonflement palpébral et allergie immédiate.',
 'Interpréter les tests épicutanés avec leur pertinence clinique.',
 'Éviter une automédication corticoïde sur un œil non examiné.',
 'Vérifier âge, grossesse, allaitement, infection et glaucome pour la spécialité choisie.',
 'Surveiller une réaction aux excipients et les symptômes visuels.'),(6,11,17,31,32))
l.quiz([
 ('Une dermatite de contact est-elle toujours allergique ?','Non. Une irritation directe sans sensibilisation peut produire un aspect proche.'),
 ('Une allergie peut-elle apparaître avec un produit utilisé depuis longtemps ?','Oui. Sensibilisation et changement de formulation sont possibles.'),
 ('Un produit pour les ongles peut-il provoquer un eczéma des paupières ?','Oui, par transfert indirect lors du contact des doigts avec la peau palpébrale.'),
 ('Quel délai décrit Ameli pour une réexposition allergique retardée ?','Habituellement vingt-quatre à quarante-huit heures, sans valeur de preuve à lui seul.'),
 ('Un test épicutané positif suffit-il à désigner la cause ?','Non. Il faut établir une exposition et une pertinence clinique.'),
 ('Peut-on reproduire le contact sur sa paupière pour vérifier ?','Non. Les tests et essais éventuels doivent être organisés par l’équipe spécialisée.'),
 ('Les tests épicutanés sont-ils équivalents aux tests d’allergie immédiate ?','Non. Ils évaluent une réaction retardée.'),
 ('Une douleur dans l’œil et une photophobie sont-elles attendues dans une simple atteinte cutanée ?','Elles imposent un examen ophtalmologique pour rechercher une atteinte du globe.'),
 ('Quelle est l’indication palpébrale de la pommade suisse décrite ?','Une maladie inflammatoire allergique non infectieuse, après examen et décision de prescription.'),
 ('Hydrocortison-POS 1% est-il recommandé avant dix-huit ans ?','Non selon cette notice, qui a étudié sécurité et efficacité chez les adultes seulement.'),
 ('Deux semaines représentent-elles une durée à atteindre systématiquement ?','Non. La notice demande la durée la plus courte possible et de ne pas dépasser ce repère.'),
 ('Quel excipient de cette pommade peut provoquer une dermatite de contact ?','La lanoline.'),
 ('Une corticothérapie peut-elle masquer une infection oculaire ?','Oui. Elle peut aussi l’activer ou l’aggraver, d’où examen, contre-indications et surveillance.'),
 ('Que faire si un collyre indispensable est suspect ?','Contacter le prescripteur pour une substitution sûre, au lieu de rester durablement sans traitement de la maladie oculaire.')
 ],(6,11,17,18,31,32))
l.write()
