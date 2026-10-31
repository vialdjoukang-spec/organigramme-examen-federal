from format_lecon import Lesson,paras,table,steps,ABBR
from collyres import ketotifene
from medicaments import quote
ABBR['IgE']='immunoglobuline E'
l=Lesson('Conjonctivite allergique',5)
med=ketotifene(l)
l.windows=[w.replace('autorisations55341/55342','autorisations 55341/55342').replace('juillet2022','juillet 2022') for w in l.windows]
l.add('La {conjonctivite allergique} est une inflammation de la conjonctive déclenchée par un allergène. Le prurit, le larmoiement et la rougeur sont souvent bilatéraux. Le gonflement des paupières accompagne cette réaction sans suffire à identifier sa cause.',paras(
 'La conjonctive tapisse la face interne des paupières et la partie antérieure du globe autour de la cornée. Son œdème, appelé chémosis, peut être visible à côté du gonflement palpébral. Une réaction de surface n’est pas synonyme d’infection des tissus orbitaires.',
 'Les formes saisonnières correspondent souvent à une exposition aux pollens. Les formes perannuelles surviennent avec des allergènes présents toute l’année, comme les acariens. Le calendrier et les circonstances aident à comprendre le déclenchement.',
 'La forme saisonnière habituelle est distinguée des kératoconjonctivites vernales ou atopiques plus sévères. Une atteinte de la cornée change le pronostic et le parcours de soins. Toute douleur importante ou vision diminuée impose donc une nouvelle évaluation.'),(18,33,34))
l.add('Le {contexte allergique} associe parfois rhinite, asthme ou eczéma. La répétition à une saison ou dans un lieu constitue un indice. Elle ne permet pas de conclure que tout œil rouge ultérieur a la même cause.',paras(
 'Aucune prévalence suisse comparée n’est déduite des données étrangères de cette leçon. La conjonctivite allergique est un diagnostic fréquent de surface, mais la priorité reste l’exclusion d’une atteinte menaçant la vision.',
 'Demander les liens avec pollens, poussières, animaux et environnement de travail ou de loisir. Une amélioration après éloignement soutient une hypothèse, sans établir une preuve pour chaque allergène suspecté.',
 'Une exposition aux produits locaux peut provoquer une irritation ou une allergie de contact plutôt qu’une allergie immédiate de la conjonctive. L’âge, le port de lentilles et les médicaments oculaires orientent les diagnostics alternatifs.',
 'Chez l’enfant avec prurit marqué, sécrétions filantes et photophobie, rechercher une forme vernale. Le caractère printanier ne suffit pas à la confondre avec une forme saisonnière bénigne.'),(6,18,33,34))
l.add('Les {mécanismes allergiques} relient exposition, prurit et œdème. Les formes saisonnières et perannuelles habituelles impliquent notamment les IgE. La cornée doit rester protégée malgré une plainte dominée par les paupières.',paras(
 'Après sensibilisation, l’allergène peut activer des mastocytes à la surface oculaire. La libération d’histamine contribue au prurit, à la rougeur et à l’augmentation de la perméabilité vasculaire. Le liquide accumulé explique une partie du chémosis et du gonflement.',
 'D’autres cellules et médiateurs participent à l’entretien de l’inflammation. Les médicaments locaux ne corrigent pas à eux seuls l’exposition. Le kétotifène combine une action antagoniste sur le récepteur histaminique et une inhibition de la libération de médiateurs.',
 'Le frottement aggrave l’irritation de la surface. Une sécheresse, une blépharite ou un conservateur irritant peut ajouter un autre mécanisme. Larmoiement ne signifie pas nécessairement que le film lacrymal est normal.',
 'Dans les formes sévères, l’épithélium cornéen peut être atteint. La douleur, la photophobie et la baisse visuelle ne doivent pas être attribuées sans examen à une simple intensité du prurit.'),(15,18,33,34))
l.add('La démarche reconnaît les {signes de gravité} avant de prescrire un collyre antiallergique. Une douleur profonde ou une baisse visuelle n’est pas expliquée par une forme habituelle. Une atteinte respiratoire ou circulatoire impose son propre parcours d’urgence.',table(['Signe','Hypothèse à exclure','Action'],[
 ['Douleur, photophobie importante ou vision diminuée','Kératite, uvéite ou autre atteinte du globe.','Examen ophtalmologique urgent.'],
 ['Œil rouge douloureux avec lentilles','Atteinte cornéenne, notamment infectieuse.','Retirer les lentilles et faire examiner rapidement.'],
 ['Fièvre, douleur aux mouvements, diplopie ou exophtalmie','Infection orbitaire.','Évaluation hospitalière immédiate.'],
 ['Dyspnée, langue gonflée, malaise ou signes circulatoires','Anaphylaxie ou angio-œdème menaçant.','Appel 144 et gestes du cours général.'],
 ['Enfant avec photophobie, mucus filant et difficultés à ouvrir les yeux','Kératoconjonctivite vernale avec atteinte cornéenne possible.','Avis spécialisé rapide, urgent si douleur ou vision atteinte.'],
 ['Nourrisson ou diagnostic incertain','Autre cause potentiellement importante.','Examen médical sans automédication par transposition de dose.']
 ]),(7,9,14,18,34,35))
l.add('L’{anamnèse} recherche le prurit, les déclencheurs et les épisodes antérieurs. Elle documente aussi les signes qui ne cadrent pas avec une allergie simple. Le retentissement visuel prime sur le volume apparent des paupières.',steps(
 'Préciser début, durée, caractère bilatéral ou asymétrique et évolution après une exposition.',
 'Distinguer prurit, brûlure et douleur. Demander photophobie, vision floue persistante et gêne aux mouvements.',
 'Décrire l’écoulement : aqueux, filant ou purulent. Rechercher rhinite, éternuements, symptômes respiratoires et fièvre.',
 'Rechercher épisodes saisonniers, allergie documentée, asthme, eczéma et réponse antérieure aux traitements.',
 'Recenser lentilles, solutions, cosmétiques, collyres et conservateurs, sans exclure une réaction au traitement.',
 'Préciser âge, grossesse, allaitement, autres médicaments, maladie oculaire et possibilité de contrôle.'),(7,15,18,33,34,35))
l.add('L’{examen oculaire ciblé} confirme la localisation conjonctivale et apprécie la vision. Il compare les deux yeux et recherche une cornée atteinte. Un examen incomplet ne doit pas servir à affirmer une forme bénigne.',paras(
 'Mesurer l’acuité visuelle de chaque œil selon les moyens adaptés à l’âge. Décrire rougeur, chémosis, sécrétions et gonflement. Examiner la peau et le bord palpébral pour une dermatite, une blépharite ou un nodule associé.',
 'Vérifier les pupilles et les mouvements oculaires. La motilité douloureuse, la diplopie ou l’exophtalmie ne sont pas des signes habituels d’une conjonctivite allergique simple.',
 'L’examen spécialisé peut montrer des papilles sur la conjonctive palpébrale. De grandes papilles, des signes limbiques et une atteinte cornéenne orientent vers des formes particulières. La biomicroscopie et l’examen de l’épithélium sont indiqués selon les symptômes.',
 'Une baisse visuelle qui ne disparaît pas avec le clignement ou le nettoyage des sécrétions appelle une exploration. Ne pas conclure à l’allergie parce que les deux paupières sont gonflées.'),(7,18,34,35))
l.add('L’{approche syndromique} confronte prurit, écoulement et atteinte cutanée. Une conjonctivite infectieuse ou une irritation peut imiter l’allergie. Des causes associées restent possibles.',table(['Tableau','Orientation','Limite'],[
 ['Prurit bilatéral, larmes et rhinite après exposition','Allergie saisonnière ou perannuelle.','Vérifier vision et absence de signes cornéens.'],
 ['Sécrétions franchement purulentes','Cause bactérienne à envisager.','L’écoulement seul ne remplace pas l’examen.'],
 ['Contexte contagieux, larmes et symptômes viraux','Conjonctivite virale.','Ne pas prescrire un antiallergique comme traitement de l’infection.'],
 ['Peau squameuse après produits locaux','Dermatite de contact palpébrale.','Mécanisme retardé distinct, parfois associé.'],
 ['Croûtes aux cils, bord inflammatoire, sécheresse','Blépharite ou trouble du film lacrymal.','Le prurit n’est pas spécifique.'],
 ['Lentilles avec douleur, photophobie ou vision modifiée','Kératite possible.','Évaluation urgente avant simple traitement symptomatique.'],
 ['Prurit intense, mucus filant, photophobie chez l’enfant','Forme vernale possible.','Avis spécialisé pour protéger la cornée.']
 ]),(6,7,18,28,34,35))
l.add('Le {diagnostic positif} d’une forme habituelle est principalement clinique. La concordance entre symptômes, examen et exposition soutient l’hypothèse. Une réponse au traitement ne constitue pas à elle seule une confirmation allergologique.',paras(
 'Le prurit est un élément central, souvent accompagné de larmoiement et d’une atteinte bilatérale. La vision reste préservée dans la forme saisonnière non compliquée. L’absence de douleur profonde ou de signe cornéen doit être vérifiée.',
 'Un déclencheur plausible et des épisodes similaires peuvent renforcer la probabilité. Une présentation unilatérale persistante, une aggravation ou une réponse insuffisante font reprendre la démarche diagnostique.',
 'Les formes vernales et atopiques relèvent d’une caractérisation ophtalmologique. Elles ne sont pas déclarées bénignes sur la seule coexistence d’un terrain allergique. Un diagnostic initial de conjonctivite peut devoir être révisé.'),(18,33,34))
l.add('Les {examens complémentaires} ne sont pas systématiques dans une forme saisonnière typique. Ils répondent à une incertitude ou à une forme persistante ou sévère. Un bilan allergologique doit avoir une utilité pour l’éviction ou la prise en charge.',
 '<h3>9.a — Référence clinique</h3>'+paras('L’examen ophtalmologique caractérise la surface et la cornée lorsque les symptômes l’exigent. Il n’existe pas de résultat sanguin unique remplaçant cet examen devant un œil douloureux.')+
 '<h3>9.b — Première intention</h3>'+paras('Évaluer vision, pupilles, motilité, conjonctive et paupières. Une biomicroscopie avec appréciation de l’épithélium cornéen est nécessaire si douleur, photophobie ou doute. Les formes banales ne justifient pas automatiquement prélèvement, imagerie ou biologie.')+
 '<h3>9.c — Allergologie</h3>'+paras('Des tests ciblés peuvent aider lorsque l’allergène est incertain ou si une stratégie d’éviction et de traitement durable doit être construite. Une sensibilisation se confronte toujours à l’histoire clinique. Les tests épicutanés de dermatite de contact n’explorent pas le même mécanisme que l’allergie immédiate habituelle.')+
 '<h3>9.d — Seconde intention</h3>'+paras('Une suspicion d’infection cornéenne, de forme vernale ou d’autre maladie oculaire suit son bilan spécialisé. Une imagerie orbitaire répond à des signes orbitaires, pas au seul chémosis. Une persistance impose de réévaluer diagnostic, exposition, observance et tolérance.'),(6,7,18,33,34))
l.add('L’{arbre décisionnel} commence par les urgences et le terrain. Une forme typique sans alarme peut recevoir des soins et un traitement adapté. La persistance n’autorise pas une prolongation indéfinie ni l’ajout empirique d’un corticoïde.',steps(
 'Si douleur, photophobie, vision modifiée ou signe orbitaire, alors organiser l’évaluation urgente adaptée.',
 'Si manifestation respiratoire ou circulatoire associée, alors suivre le parcours d’urgence systémique.',
 'Si forme bilatérale prurigineuse typique sans alarme, alors réduire l’exposition, éviter le frottement et proposer les soins de surface.',
 'Si un médicament est indiqué, alors vérifier son indication exacte, l’âge, les contre-indications et la formulation.',
 'Si enfant avec suspicion de forme vernale, alors demander un avis ophtalmologique, sans masquer une atteinte cornéenne.',
 'Si absence d’amélioration, récidive inhabituelle ou aggravation, alors réexaminer et revoir le diagnostic avant de prolonger.'),(7,15,18,34,35))
l.add('La {prise en charge suisse} vise l’éviction pertinente, le confort et la protection de la surface oculaire. Un antiallergique local peut traiter une forme saisonnière compatible avec sa notice. Les formes sévères ou cornéennes nécessitent un spécialiste.',
 '<h3>11.A — But</h3>'+paras('Réduire prurit, rougeur et larmoiement, tout en évitant frottement et exposition persistante. Préserver la vision et reconnaître un diagnostic différent si l’évolution est atypique.')+
 '<h3>11.B — Moyens</h3>'+paras('Des compresses fraîches propres, un rinçage adapté et des lubrifiants choisis pour leur tolérance peuvent soulager. Les HUG privilégient les formulations sans conservateur lorsque cela est possible. Éviter le contact de l’embout avec l’œil et ne pas partager les produits.',
 'Éviter les lentilles sur un œil rouge ou inflammatoire et interrompre les produits non indispensables suspects. Un facteur allergénique identifié guide les mesures d’éviction. Ne pas imposer des suppressions multiples sans lien clinique.',
 'Le kétotifène suivant dispose d’une indication suisse pour la forme saisonnière. La forme perannuelle ou une kératoconjonctivite sévère ne doit pas être automatiquement assimilée à cette indication :')+med+quote('55341',['Adultes et enfants à partir de 3 ans'])+paras(
 'Pour ce produit, une goutte dans chaque œil deux fois par jour, au maximum six semaines, selon la notice. Le guide HUG évoque une durée générale pouvant aller jusqu’à deux mois pour certains traitements locaux. Cette durée générale ne remplace pas le plafond de six semaines propre à Zaditen.',
 'Le flacon de 5 ml porte l’autorisation 55341 ; les unidoses de 0,4 ml portent le numéro 55342. La solution contient 0,25 mg/ml de kétotifène. La présence de conservateur dans le flacon doit être prise en compte si la surface est fragile ou si les symptômes s’aggravent.',
 'Sous trois ans, ne pas inventer une dose réduite à partir de ce schéma. La grossesse et l’allaitement demandent la prudence propre à la notice, pas une affirmation d’innocuité fondée sur la seule voie locale.',
 'Les antibiotiques ne traitent pas l’allergie. Les corticoïdes oculaires et les immunomodulateurs peuvent avoir une place spécialisée dans des formes sévères ; ils ne sont pas proposés ici en automédication ni avec une dose non vérifiée. Une corticothérapie peut masquer une infection et nécessite une surveillance oculaire.')+
 '<h3>11.C — Surveillance</h3>'+paras('Suivre prurit, rougeur, vision et tolérance. L’apparition de douleur, photophobie, baisse visuelle ou écoulement inhabituel justifie une réévaluation rapide. Ne pas attendre la durée maximale du traitement pour consulter en cas de persistance ou d’aggravation.',
 'Le médicament ou son excipient peut lui-même provoquer une réaction de contact ou un œdème. Une aggravation après instillation impose de revoir le traitement. L’emballage, la date d’ouverture et les autres produits utilisés aident à l’enquête.')+
 '<h3>11.D — Pronostic et suivi</h3>'+paras('Le pronostic visuel des formes saisonnières habituelles est favorable, mais la gêne et les récidives peuvent être importantes. Adapter la stratégie au rythme des expositions et au retentissement.',
 'La forme vernale peut léser la cornée et requiert un suivi différent. Un contrôle spécialisé reste nécessaire si les symptômes sont sévères, répétés ou mal expliqués. Une amélioration symptomatique ne dispense pas de ce suivi lorsque la cornée a été atteinte.'),(6,7,15,18,33,34,35))
l.add('La {prévention} s’appuie sur les expositions réellement pertinentes et une bonne utilisation des produits. Elle évite le frottement et la contamination des collyres. Une récidive ne justifie pas de réutiliser aveuglément une ancienne ordonnance.',paras(
 'Repérer les périodes et lieux déclenchants pour adapter les mesures pratiques. Les conseils doivent rester réalisables et proportionnés au lien clinique. Une rhinite ou un asthme associé mérite sa propre prise en charge.',
 'Utiliser des compresses propres et éviter les produits irritants ou parfumés autour des yeux s’ils aggravent les symptômes. Respecter conservation et élimination des unidoses. Une durée de conservation après ouverture ne constitue pas une durée de traitement.',
 'La conjonctivite allergique n’est pas contagieuse. Si le diagnostic change vers une infection, les conseils d’hygiène et le traitement sont réévalués. La rougeur seule ne permet pas de trancher.',
 'Informer sur les signes qui imposent de consulter, y compris lors d’une saison allergique connue. Une douleur ou une vision réduite ne doit pas être attendue comme un effet normal du pollen.'),(7,15,18,33,35))
l.add('Les {points clés} associent prurit, localisation et sécurité visuelle. La notice du produit détermine la dose et les limites d’utilisation. Les formes sévères restent distinctes d’une conjonctivite saisonnière habituelle.',steps(
 'Rechercher un prurit bilatéral, un lien d’exposition et une rhinite, sans oublier les diagnostics alternatifs.',
 'Examiner vision et cornée si douleur ou photophobie. Les lentilles abaissent le seuil d’orientation devant une douleur.',
 'Distinguer allergie immédiate, dermatite de contact et irritation par un médicament.',
 'Respecter dès trois ans et six semaines maximum pour la spécialité de kétotifène décrite.',
 'Ne pas appliquer à cette spécialité une durée générale plus longue issue d’un guide.',
 'Ne pas ajouter antibiotique ou corticoïde sans indication, examen et surveillance adaptés.'),(6,7,15,18,34,35))
l.quiz([
 ('Quel symptôme oriente particulièrement vers une conjonctivite allergique ?','Le prurit, souvent bilatéral, avec larmoiement et contexte d’exposition.'),
 ('Le chémosis est-il une preuve de cellulite orbitaire ?','Non. Il décrit un œdème conjonctival dont la cause doit être déterminée.'),
 ('Une baisse visuelle persistante est-elle habituelle dans une forme saisonnière simple ?','Non. Elle impose un examen pour rechercher une atteinte cornéenne ou un autre diagnostic.'),
 ('Que faire devant un œil rouge douloureux chez un porteur de lentilles ?','Retirer les lentilles et organiser un examen rapide pour exclure une kératite.'),
 ('Une forme printanière chez l’enfant est-elle toujours bénigne ?','Non. Une forme vernale peut atteindre la cornée, notamment avec photophobie et sécrétions filantes.'),
 ('La conjonctivite allergique est-elle contagieuse ?','Non. Les mesures propres à une infection dépendent d’un diagnostic infectieux distinct.'),
 ('Une sensibilisation positive suffit-elle à expliquer les symptômes ?','Non. Elle doit correspondre à une exposition et à une histoire clinique pertinentes.'),
 ('Quelle indication couvre la notice suisse de Zaditen Ophtha ?','Le traitement de la conjonctivite allergique saisonnière.'),
 ('Quelle dose et quel âge sont donnés par cette notice ?','Une goutte dans chaque œil deux fois par jour chez l’adulte et l’enfant dès trois ans.'),
 ('Peut-on poursuivre ce produit deux mois sur la base d’un guide général ?','Non. Sa notice fixe une durée maximale de six semaines ; la persistance impose une réévaluation plus tôt.'),
 ('Les unidoses et le flacon contiennent-ils le même conservateur ?','Non. Le chlorure de benzalkonium concerne le flacon ; les unidoses ne le contiennent pas.'),
 ('Le délai de quinze minutes autorise-t-il les lentilles sur un œil inflammatoire ?','Non. C’est une précaution liée au conservateur ; la notice déconseille globalement les lentilles sur un œil rouge ou inflammatoire.'),
 ('Pourquoi une aggravation après un collyre doit-elle être réévaluée ?','Le médicament ou un excipient peut lui-même provoquer une irritation ou une hypersensibilité.'),
 ('Un collyre antiallergique suffit-il en cas de dyspnée et malaise associés ?','Non. Il faut suivre immédiatement le parcours d’urgence systémique, avec appel 144 si menace vitale.')
 ],(6,7,15,18,33,34,35))
l.write()
