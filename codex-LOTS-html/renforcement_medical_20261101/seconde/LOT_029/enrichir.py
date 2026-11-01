#!/usr/bin/env python3
"""Ajouts ciblés aux fenêtres, sans resérialiser le document ni toucher au harnais."""
from pathlib import Path
import re, json, hashlib, gzip
from lxml import html

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
LOT = ROOT / 'LOT_029'

def refs(ns):
    return '<sup class="s">'+','.join(f'<a href="#s{n}">{n}</a>' for n in ns)+'</sup>'

def bloc(titre, *paragraphes):
    return '<h3>'+titre+'</h3>'+''.join('<p>'+p+'</p>' for p in paragraphes)

A = {
1: (bloc('Décrire trois axes avant de nommer une maladie',
    '<strong>La taille</strong> se rapporte à l’âge, au sexe et à une courbe identifiée ; <strong>la trajectoire</strong> précise si l’écart est ancien, stable ou progressif ; <strong>la forme</strong> renseigne sur la croissance des sutures. Une macrocéphalie peut être congénitale ou apparaître après la naissance. Une tête disproportionnée par rapport à la taille et au poids peut attirer l’attention sans franchir le seuil statistique de macrocéphalie : c’est une <em>macrocéphalie relative</em>.',
    'Le terme <em>microcéphalie primitive</em> décrit un groupe particulier de troubles du développement cérébral. Il ne doit pas remplacer le constat de microcéphalie quand l’étiologie reste inconnue. Les critères des formes génétiques étudiées dans le protocole français ne définissent pas toutes les petites têtes de l’enfant.'), [1,7,9]),
2: (bloc('Interpréter le contexte sans fabriquer un classement',
    '<strong>Les probabilités dépendent du recrutement.</strong> Un enfant sans symptôme vu en contrôle de croissance et un nourrisson adressé pour régression ne relèvent pas du même raisonnement. Les proportions de formes familiales rapportées dans une revue de macrocéphalie ne permettent pas de classer les dix causes de ce cours dans la population suisse.',
    'Une grande tête présente chez plusieurs apparentés en bonne santé soutient une variation familiale. La même transmission accompagnée de difficultés développementales, de lésions cutanées, de malformations vasculaires ou d’une histoire tumorale pertinente oriente au contraire vers une affection héréditaire. La prématurité et une hémorragie intraventriculaire ou une méningite antérieure modifient aussi l’interprétation d’une accélération céphalique.'), [7,10]),
3: (bloc('Relier le compartiment atteint au signe clinique',
    '<strong>Le périmètre est une mesure externe.</strong> Il additionne les effets de la croissance cérébrale, des espaces liquidiens et de l’os. Une mégalencéphalie peut résulter d’une augmentation du nombre ou de la taille des cellules cérébrales, ou d’une accumulation de substances dans certaines maladies métaboliques. La présence de régression, d’une organomégalie ou d’anomalies de substance blanche aide alors à orienter le mécanisme.',
    'À l’inverse, les gènes <em>ASPM, WDR62</em> et <em>CDK5RAP2</em> interviennent dans la division des progéniteurs neuronaux ; leurs anomalies peuvent réduire la croissance cérébrale. Cette explication ne s’applique pas à toutes les microcéphalies, dont certaines suivent une agression acquise. Une déformation crânienne par fermeture suturaire relève d’un autre mécanisme et se juge sur sa morphologie.'), [2,7,9]),
4: (bloc('Séparer urgence clinique et bilan d’une courbe',
    '<strong>La suspicion de pression intracrânienne élevée impose une évaluation immédiate.</strong> La combinaison vomissements, modification du comportement, regard anormal ou fontanelle tendue compte davantage qu’un centile isolé. Une conscience altérée, une crise en cours ou un déficit aigu impose la filière d’urgence déjà indiquée. L’organisation du transfert précède la reconstitution exhaustive du carnet de croissance.',
    'Chez un enfant stable, une cassure confirmée sans symptôme aigu appelle une évaluation pédiatrique et l’imagerie indiquée, mais ne signifie pas à elle seule une décompensation neurochirurgicale. Une dysmorphie associée à un retard nécessite un avis pédiatrique urgent selon la recommandation britannique ; la famille ne doit pas être renvoyée à une simple prochaine mesure. <em>Le degré d’urgence vient du tableau clinique et de son évolution.</em>'), [6,7]),
5: (bloc('Faire préciser une chronologie exploitable',
    '<strong>Avant la naissance et à la naissance :</strong> recueillir l’âge gestationnel, la croissance fœtale, les anomalies d’imagerie connues et les mesures documentées. <strong>Après la naissance :</strong> dater la première anomalie de courbe, les événements infectieux ou hémorragiques et l’apparition des symptômes. Une donnée manquante reste inconnue ; elle ne devient pas un antécédent normal.',
    'Pour le développement, demander ce que l’enfant savait faire auparavant et ce qu’il fait actuellement, dans les domaines moteur, langagier et relationnel. Distinguer une acquisition tardive, une stagnation et une perte de compétence. Une modification récente de l’alimentation, de l’éveil ou de la marche peut constituer le premier indice de maladie, même si la famille consulte seulement pour la taille de la tête.',
    'Dans la famille, préciser quels apparentés ont une grande ou petite tête, leur développement et les diagnostics connus. Un parent apparemment indemne ne permet pas d’exclure un syndrome à expression variable ; une anomalie familiale connue change les indications de conseil et d’analyse génétique.'), [6,7,10]),
6: (bloc('Examiner les indices qui changent l’orientation',
    '<strong>Crâne vu du dessus :</strong> une tête allongée évoque une atteinte sagittale ; un front triangulaire une atteinte métopique. Dans la plagiocéphalie positionnelle, l’aplatissement postérieur s’accompagne typiquement d’une avancée du front et de l’oreille du même côté, donnant un parallélogramme. Ces descriptions guident l’examen ; une hésitation diagnostique doit conduire à l’équipe spécialisée.',
    '<strong>Examen hors du crâne :</strong> comparer croissance globale et céphalique, rechercher asymétrie segmentaire, anomalies cutanées ou vasculaires, malformations et organomégalie. Examiner le regard et les mouvements oculaires, le tonus, la motricité et, selon l’âge, la marche. Ces constatations distinguent un constat isolé d’une atteinte neurologique ou multisystémique.',
    'Une suture saillante ou une forme atypique ne s’interprète pas sans l’ensemble morphologique. De même, un examen neurologique normal aujourd’hui constitue une donnée rassurante, mais ne dispense pas d’apprécier la trajectoire et les acquisitions rapportées par les parents.'), [2,6,7]),
7: (bloc('Utiliser le tableau pour choisir la prochaine question',
    '<strong>Grande tête isolée et stable :</strong> vérifier l’hypothèse familiale. <strong>Grande tête qui accélère :</strong> rechercher une expansion liquidienne, une masse ou une autre cause évolutive. <strong>Grande tête avec régression, organomégalie ou signes cutanés :</strong> envisager une maladie métabolique ou génétique. Ces associations orientent les examens ; elles ne sont pas des critères suffisants à elles seules.',
    '<strong>Petite tête :</strong> distinguer l’anomalie présente précocement d’une décélération secondaire et rechercher le contexte neurodéveloppemental, infectieux ou d’exposition. Les microcéphalies génétiques n’ont pas toutes le même retentissement : les malformations corticales et les signes moteurs sont notamment différents selon le gène atteint.',
    'Une déformation crânienne avec périmètre peu modifié ouvre la branche suturaire. Enfin, une collection sous-durale peut coexister avec des espaces sous-arachnoïdiens élargis : l’une ne permet pas de déduire la nature, la cause ou l’innocuité de l’autre.'), [2,7,9,11]),
8: (bloc('Du constat positif au pronostic',
    '<strong>Le diagnostic positif de taille anormale</strong> demande une mesure reproductible et une référence explicite. <strong>Le diagnostic causal</strong> demande ensuite une concordance entre histoire, examen, imagerie et, si indiqué, analyses ciblées. Un résultat radiologique ou moléculaire se confronte au phénotype ; il ne remplace pas l’évaluation des fonctions de l’enfant.',
    'Le pronostic ne se déduit pas du nombre de centimètres. Il dépend de la cause, de la trajectoire, des acquisitions, des troubles moteurs, des crises et des atteintes sensorielles associées. Une macrocéphalie familiale cliniquement isolée peut avoir une évolution favorable ; une petite tête ne permet pas de prédire à elle seule les capacités futures d’un enfant.',
    'Les seuils d’orientation de la recommandation britannique reposent sur le consensus du comité, faute d’éléments probants permettant de les établir dans la revue effectuée pour ce chapitre. Ils apportent un cadre pratique, sans constituer un score prédictif validé ni une conversion automatique entre courbes nationales.'), [6,7,9]),
9: (bloc('Imagerie : quelle réponse attend-on ?',
    '<strong>L’échographie transfontanellaire</strong> explore ventricules et espaces liquidiens sans irradiation ni sédation lorsque la fenêtre acoustique est disponible. Un examen rassurant ne clôt pas un bilan si la clinique suggère une lésion parenchymateuse, une malformation ou une autre anomalie insuffisamment caractérisée. L’<abbr title="imagerie par résonance magnétique">IRM</abbr> décrit mieux le parenchyme et les malformations ; chez le petit nourrisson, les techniques d’endormissement après alimentation peuvent parfois éviter une sédation.',
    '<strong>Devant des ventricules dilatés,</strong> rechercher leur répartition, un obstacle et des signes de décompensation ; toute ventriculomégalie ne se résume pas à un diagnostic causal. Devant des espaces péricérébraux élargis, préciser le compartiment et rechercher une collection associée. Devant une masse, apprécier l’effet de masse et une hydrocéphalie associée. Le compte rendu doit répondre à la question urgente autant que nommer l’anomalie.' ) + bloc('Analyses ciblées : résultat et limite',
    'Pour le <abbr title="cytomégalovirus">CMV</abbr> congénital, le prélèvement dans les trois premières semaines permet d’attribuer l’infection à la période congénitale. Une salive positive nécessite confirmation urinaire. Une recherche rétrospective sur sang séché néonatal peut être utile après ce délai ; un résultat négatif n’exclut pas l’infection, car sa portée dépend de la sensibilité de la méthode. Les immunoglobulines M néonatales ne constituent pas le test diagnostique recommandé.',
    'La génétique est orientée par les signes et l’imagerie ; une suspicion de maladie métabolique appelle des analyses adaptées au profil clinique. La juxtaposition de tests sans hypothèse expose à des résultats difficiles à interpréter et ne remplace pas l’avis spécialisé.'), [2,7,9,20]),
10: (bloc('Décisions conditionnelles et actions parallèles',
    '<strong>Si des signes neurologiques aigus ou de pression apparaissent,</strong> adresser immédiatement et transmettre les symptômes, leur début et les données disponibles ; ne pas attendre un bilan génétique. <strong>Si l’enfant est stable mais la trajectoire change réellement,</strong> organiser l’évaluation pédiatrique et l’imagerie selon la question clinique.',
    '<strong>Si la grande tête est stable, familiale et cliniquement isolée,</strong> une surveillance peut être retenue avec objectifs et critères de réévaluation. <strong>Si le développement, la forme ou l’examen est anormal,</strong> quitter cette branche de rassurance et demander le bilan correspondant. Pour une petite tête, distinguer cause développementale précoce et atteinte acquise avant de choisir les examens.',
    'Le bilan causal et l’aide au développement peuvent avancer en parallèle. Chez un nouveau-né avec suspicion d’infection congénitale, organiser sans retard le prélèvement diagnostique dans sa fenêtre utile, même si les examens sensoriels et l’imagerie ne sont pas encore terminés.'), [6,7,9,20]),
11: (bloc('Adapter l’objectif de soin au mécanisme',
    '<strong>Cause expansive ou liquidienne menaçante :</strong> la priorité est la protection neurologique et le traitement spécialisé du mécanisme ; mesurer à nouveau ne constitue pas un traitement. <strong>Craniosténose :</strong> l’avis précoce permet de discuter les possibilités chirurgicales en fonction de la suture, de l’âge et de la forme, sans commander un scanner de routine en amont de l’équipe.',
    '<strong>Atteinte neurodéveloppementale :</strong> les soins visent les compétences, l’autonomie, la nutrition, la communication et les complications. Dans les microcéphalies primitives couvertes par le protocole français, il n’existe pas de traitement curatif spécifique ; l’accompagnement s’adapte aux déficits moteurs, sensoriels et aux crises. Une indication de soutien ne dépend pas de l’obtention préalable d’un nom moléculaire.',
    '<strong>Infection congénitale :</strong> l’atteinte neurologique, auditive, ophtalmologique ou systémique guide la discussion antivirale. Le document suisse souligne que le bénéfice est le mieux établi lorsque le traitement débute dans le premier mois ; une initiation plus tardive relève d’une discussion experte. La surveillance d’une éventuelle toxicité hématologique et hépatique fait partie de cette prise en charge, sans transposer ici une posologie non vérifiée dans l’information professionnelle suisse.'), [2,3,7,9,20]),
12: (bloc('Un suivi défini par ce qui peut changer',
    '<strong>Trajectoire :</strong> comparer les mesures sur une référence cohérente et rechercher une accélération ou une décélération réelle. <strong>Fonction :</strong> revoir acquisitions, interaction, alimentation, audition et vision ; une stabilisation du centile n’efface pas une difficulté fonctionnelle. <strong>Cause :</strong> appliquer les surveillances propres au diagnostic lorsque celui-ci est établi.',
    'Une infection congénitale à <abbr title="cytomégalovirus">CMV</abbr> peut s’accompagner d’une dégradation auditive secondaire. L’organisation du suivi dépend donc du bilan initial et du contexte infectieux, pas seulement d’un dépistage auditif initial rassurant. Une anomalie génétique confirmée peut également nécessiter une surveillance sensorielle ou d’organes précise, distincte du simple contrôle du périmètre.',
    'La prévention vise les causes évitables et le retard de prise en charge : information sur les mesures d’hygiène contre le cytomégalovirus avant ou pendant la grossesse, accompagnement des expositions, conseil génétique lorsqu’il est indiqué et transmission d’un plan clair à la famille. Aucun régime ni exercice ne doit être proposé pour corriger un centile constitutionnel.'), [1,3,6,7,9,20]),
13: (bloc('Les trois conclusions à rendre à la famille',
    '<strong>Ce qui est constaté :</strong> une mesure, une forme et une évolution, avec leur degré de fiabilité. <strong>Ce qui est interprété :</strong> une hypothèse probable ou une cause documentée, en distinguant ce qui reste à établir. <strong>Ce qui est décidé :</strong> urgence, bilan orienté ou suivi, avec une date et des signes justifiant de consulter avant.',
    'Une conclusion de variation familiale exige une cohérence clinique, et non une ressemblance isolée avec un parent. Une conclusion de microcéphalie ne donne pas à elle seule le pronostic du développement. Une imagerie utile explique le compartiment atteint ou la lésion recherchée ; une simple mention d’examen normal ne répond pas nécessairement à toutes les questions.',
    '<em>Le bon résultat du suivi est un enfant évalué et accompagné selon ses besoins, pas une courbe artificiellement ramenée vers la moyenne.</em>'), [1,6,7,9]),
}

D = {
1: (bloc('Une interprétation clinique, pas une preuve par ressemblance',
    '<strong>Familiale</strong> signifie qu’un grand périmètre est retrouvé chez des apparentés ; <strong>constitutionnelle</strong> indique qu’il s’inscrit dans une variation de croissance sans autre anomalie actuellement identifiée. Ces deux qualificatifs ne sont pas interchangeables : une maladie génétique peut aussi se transmettre dans une famille.',
    'Le diagnostic reste <em>probable et réévaluable</em> lorsque la trajectoire est cohérente, l’examen rassurant et le développement adapté. Il n’exige pas de démontrer par imagerie un cerveau augmenté de volume chez chaque enfant asymptomatique. La macrocéphalie est une observation externe ; la mégalencéphalie est un constat portant sur le cerveau.'), [6,7,10]),
2: (bloc('Ce que l’histoire familiale apporte réellement',
    'La présence de plusieurs grandes têtes chez des personnes sans difficulté neurologique renforce l’hypothèse constitutionnelle. Elle ne donne ni une certitude individuelle, ni un taux de risque chiffré. Les séries de patients avec mégalencéphalie isolée, macrocéphalie clinique ou syndrome génétique ne sont pas des populations interchangeables.',
    '<strong>Un apparenté non mesuré n’est pas une preuve négative.</strong> Si les parents biologiques ne peuvent pas être mesurés, noter cette limite et fonder la décision sur le reste du tableau. À l’inverse, une famille avec grandes têtes et retard, signes cutanés ou tumeurs pertinentes appelle une recherche syndromique, même si aucun diagnostic n’avait été posé jusque-là.'), [6,7,10]),
3: (bloc('Pourquoi taille et pression se dissocient',
    'La taille externe du crâne peut être élevée sans processus expansif actif. Le volume cérébral, les espaces liquidiens et l’os contribuent au périmètre ; une mesure au ruban ne permet pas de quantifier séparément ces composantes. <strong>Une grande tête ne prouve donc ni hydrocéphalie ni hypertension intracrânienne.</strong>',
    'La qualification constitutionnelle repose sur l’absence d’arguments cliniques pour une autre cause et sur l’évolution. Elle ne permet pas d’affirmer un mécanisme cellulaire particulier chez cet enfant. Les troubles de régulation de la croissance cérébrale liés à certains gènes et les maladies métaboliques constituent des mécanismes pathologiques distincts, à rechercher si le phénotype le suggère.'), [7]),
4: (bloc('Deux situations qui font changer de filière',
    '<strong>Dégradation aiguë :</strong> une somnolence inhabituelle, un trouble de conscience, des crises, une anomalie oculomotrice ou des vomissements dans un tableau neurologique imposent une évaluation urgente. Le contexte parental rassurant ne diminue pas cette priorité. Une ancienne mesure stable ne permet pas d’exclure une affection intracrânienne nouvelle.',
    '<strong>Discordance progressive :</strong> une accélération confirmée, un retard, une régression ou des signes physiques associés font abandonner la surveillance d’une forme supposée isolée et organiser un bilan. L’enfant peut être cliniquement stable et néanmoins nécessiter cet avis. La distinction évite de traiter toute grande tête comme une urgence ou, à l’inverse, toute grande tête familiale comme bénigne.'), [6,7]),
5: (bloc('Documenter la concordance, chercher les discordances',
    'Rassembler les valeurs successives avec leur date, la référence utilisée et les mesures corporelles associées. Une grande tête décrite depuis la naissance n’a pas la même signification qu’un périmètre récemment accéléré. Demander aussi si les anciennes mesures étaient fiables ou simplement reportées d’un document à l’autre.',
    '<strong>L’histoire développementale doit être concrète :</strong> préciser progression motrice, langage et interaction, ainsi que tout changement d’éveil ou d’alimentation. Les parents peuvent reconnaître une perte de compétence avant qu’un déficit soit visible pendant la consultation.',
    'Dans l’histoire familiale, dépasser la question de la taille des chapeaux : recueillir troubles du développement, anomalies vasculaires ou cutanées et diagnostics génétiques connus. Un variant familial pathogène de <em>PTEN</em> implique une démarche génétique spécifique, même si l’enfant paraît actuellement en bonne santé.'), [6,7,10]),
6: (bloc('Ce qui rend l’examen véritablement rassurant',
    'L’examen ne se résume pas à une fontanelle souple. Il recherche une discordance entre grande tête et croissance corporelle, une asymétrie segmentaire, une dysmorphie, une anomalie cutanée ou vasculaire et une organomégalie. Il apprécie regard, motricité, tonus et développement selon l’âge.',
    '<strong>Comparer les observations aux préoccupations familiales.</strong> Un enfant calme pendant quelques minutes ne suffit pas à exclure une irritabilité inhabituelle, un trouble de l’alimentation ou une perte d’acquisition rapportée à domicile. Une description cohérente de ces changements justifie la réévaluation.',
    'Les caractéristiques syndromiques peuvent se révéler progressivement. L’absence de signes cutanés à un examen précoce n’exclut pas définitivement une affection telle qu’un syndrome lié à <em>PTEN</em>. Le caractère rassurant de l’examen se formule avec sa date et son contexte.'), [7,10]),
7: (bloc('Ne pas confondre trois tableaux familiaux',
    '<strong>Variation constitutionnelle :</strong> grande tête, évolution cohérente et absence de signe associé. <strong>Élargissement sous-arachnoïdien du nourrisson :</strong> mécanisme liquidien qui peut également s’accompagner d’antécédents familiaux, identifié par son contexte et, lorsqu’elle est indiquée, son imagerie. <strong>Syndrome génétique :</strong> macrocéphalie avec caractéristiques développementales, cutanées, vasculaires ou autres indices.',
    'Une macrocéphalie accompagnée de retard ou de traits autistiques, de lipomes, de malformations vasculaires ou d’une histoire familiale connue de <em>PTEN</em> justifie une discussion génétique. Une croissance corporelle asymétrique avec anomalies cutanées ou vasculaires peut orienter vers d’autres syndromes de surcroissance. Ces associations sont des raisons de bilan, pas un diagnostic moléculaire à elles seules.'), [7,10]),
8: (bloc('Établir une conclusion avec ses conditions',
    '<strong>Éléments concordants :</strong> mesure correcte, trajectoire non préoccupante, développement adapté, examen sans anomalie associée et contexte familial objectivé si possible. <strong>Éléments incompatibles avec la seule rassurance :</strong> signes de pression, régression, déficit, cassure confirmée ou phénotype syndromique.',
    'Aucun score validé de macrocéphalie familiale bénigne n’est proposé dans les sources citées. La recommandation britannique fournit une règle d’orientation, et la revue une démarche clinique ; ni l’une ni l’autre ne prouve par un test unique le caractère constitutionnel. La conclusion doit donc expliciter les arguments et la conduite en cas de changement.',
    'Une macrocéphalie très marquée renforce l’attention portée aux causes neurogénétiques, sans transformer un seuil isolé en diagnostic. L’amplitude de l’écart ne dispense jamais de l’examen et n’annonce pas à elle seule les capacités futures de l’enfant.'), [6,7]),
9: (bloc('Savoir pourquoi différer ou demander l’imagerie',
    '<strong>Différer l’imagerie</strong> peut se justifier si les critères cliniques sont concordants et s’il n’existe aucun facteur de risque associé. Cela signifie poursuivre une vigilance clinique, et non déclarer le cerveau normal sur le seul contexte familial. Une irritabilité inexpliquée, un changement alimentaire, un retard ou un signe neurologique change cette décision.',
    '<strong>Si une imagerie devient indiquée,</strong> l’échographie peut être une première exploration lorsque la fontanelle est ouverte ; l’<abbr title="imagerie par résonance magnétique">IRM</abbr> caractérise plus précisément cerveau, malformations et espaces liquidiens. Le scanner se réserve notamment à une urgence ou à une question osseuse ciblée, en tenant compte de l’irradiation. Le choix dépend de la question clinique et de l’équipe, pas de la seule hauteur du centile.',
    'Un examen structurel rassurant ne remplace pas le suivi du développement et n’exclut pas toute cause génétique. Réciproquement, l’absence d’imagerie n’impose pas une analyse génétique chez tout enfant asymptomatique : l’indication doit être motivée par le phénotype ou une anomalie familiale connue.'), [6,7,10]),
10: (bloc('Rendre la décision explicite à chaque étape',
    '<strong>Première décision :</strong> existe-t-il un symptôme exigeant une évaluation immédiate ? Si oui, orienter sans attendre les mesures parentales. <strong>Deuxième décision :</strong> les données de croissance sont-elles fiables et cohérentes ? Si non, les vérifier avant de conclure, en respectant les signes cliniques présents.',
    '<strong>Troisième décision :</strong> l’anomalie est-elle réellement isolée ? Si un élément neurologique, développemental ou syndromique est présent, organiser le bilan correspondant. Si l’ensemble est rassurant, expliquer pourquoi une surveillance est adaptée, préciser qui la réalise et ce qui déclenchera une nouvelle investigation.',
    'Une inquiétude parentale persistante doit être explorée par des questions précises et un examen adapté ; elle ne doit être ni assimilée automatiquement à une maladie ni écartée parce que le parent a lui-même une grande tête.'), [6,7]),
11: (bloc('Rassurer avec une explication et un plan',
    'Expliquer que la mesure est élevée, mais que l’examen, les acquisitions et la trajectoire observés soutiennent actuellement une variation de croissance. Donner les raisons de ne pas demander d’examen supplémentaire à ce stade, ainsi que celles qui conduiraient à changer de stratégie. <strong>La rassurance fait partie du soin lorsqu’elle reste conditionnelle et compréhensible.</strong>',
    'Le but n’est pas de faire diminuer la tête ni de forcer un retour vers un centile central. Il n’existe pas d’indication à un traitement médicamenteux ou à une chirurgie pour une variation constitutionnelle isolée. Si une difficulté de langage, de motricité ou de comportement est identifiée, elle doit être évaluée pour elle-même, sans être expliquée automatiquement par la taille crânienne.'), [6,7]),
12: (bloc('Surveillance utile et prévention du retard diagnostique',
    'À la consultation suivante, reprendre les mesures avec une méthode comparable, examiner les nouvelles acquisitions et demander les symptômes survenus depuis la visite précédente. L’intervalle dépend de l’âge, de la qualité des données disponibles et de la situation clinique ; les sources citées ne donnent pas un calendrier universel pour toute macrocéphalie familiale.',
    '<strong>Consulter avant le contrôle prévu</strong> si apparaissent trouble du regard, vomissements inhabituels, somnolence, crise, régression ou déficit. Une modification confirmée de la trajectoire conduit également à reconsidérer le bilan. Les signes aigus commandent la filière d’urgence ; la famille ne doit pas attendre de pouvoir effectuer une mesure à domicile.',
    'Il n’existe pas de prévention visant à supprimer une variation familiale normale. La prévention pertinente est celle d’un retard de diagnostic : conserver la courbe, transmettre les critères de réévaluation et ne pas figer l’étiquette de bénignité dans le dossier.'), [1,6,7]),
13: (bloc('Quatre erreurs évitées par une conclusion nuancée',
    '<strong>Confondre familial et bénin :</strong> rechercher aussi les maladies familiales. <strong>Confondre grande tête et pression :</strong> juger les symptômes et le mécanisme. <strong>Confondre stabilité du centile et normalité fonctionnelle :</strong> continuer à évaluer les acquisitions. <strong>Confondre absence d’imagerie et absence de soin :</strong> une surveillance motivée et comprise est une conduite active.',
    'La formulation utile est : variation constitutionnelle probable sur les éléments actuels, avec suivi défini. Si un élément discordant survient, la stratégie change. Cette réévaluation ne contredit pas une décision initiale raisonnable ; elle tient compte d’informations cliniques nouvelles.'), [6,7,10]),
}

AQ = [
 'La mesure constate une taille, pas son mécanisme. La répétition technique et la trajectoire permettent de distinguer erreur, variation de croissance et anomalie évolutive ; les symptômes peuvent imposer d’agir avant cette reconstitution.',
 'Il s’agit de la plus grande mesure techniquement valide, et non d’une valeur aberrante due au mauvais placement du ruban. Cette procédure doit être nommée, car d’autres textes proposent une autre méthode de sélection.',
 'La version de la courbe doit accompagner l’interprétation. Un changement de référence peut déplacer un centile sans changement réel du nombre de centimètres ; comparer les mesures avec cohérence avant de parler de cassure.',
 'La mégalencéphalie désigne le cerveau ; la macrocéphalie décrit la circonférence externe. Une dilatation ventriculaire, une collection ou une anomalie osseuse peut produire une grande tête par un autre mécanisme.',
 'La décision repose sur la concordance de la trajectoire, du développement, de l’examen et du contexte familial. Une décision de surveillance doit préciser les conditions qui la rendent sûre et les motifs de réévaluation.',
 'Il faut d’abord vérifier que le changement est réel. Une fois confirmé, le cadre britannique appelle évaluation et imagerie ; l’apparition de signes de pression augmente l’urgence sans attendre un nouveau contrôle.',
 'Les signes de pression ont priorité sur la ressemblance familiale. Le transfert ou l’avis urgent ne doit pas attendre de mesurer les parents ni de retrouver l’intégralité du carnet.',
 'Une fermeture suturaire peut modifier surtout la forme, avec croissance compensatrice ailleurs. La morphologie et l’examen des sutures restent donc nécessaires même avec un périmètre habituel.',
 'La question clinique et l’équipe spécialisée déterminent l’examen. Le texte suisse réserve la prescription du scanner à la planification chirurgicale, afin d’éviter une irradiation inutile.',
 'La présence d’espaces élargis n’attribue pas la cause de la collection. Évaluer le compartiment, le contexte et les autres lésions ; la démarche de protection éventuelle repose sur l’ensemble des constatations.',
 'Une exposition ne s’infère pas d’un signe morphologique isolé. L’histoire se recueille avec tact et le bilan conserve les causes génétiques, infectieuses et acquises pertinentes.',
 'La fenêtre néonatale permet de documenter le caractère congénital. Une salive positive doit être confirmée sur les urines ; un diagnostic rétrospectif sur sang séché négatif ne suffit pas toujours à exclure l’infection.',
 'Des affections génétiques peuvent être familiales et d’expression variable. Développement atypique, signes cutanés ou vasculaires et histoire familiale pertinente doivent rouvrir la question étiologique.',
 'Les acquisitions, la nutrition, l’audition et la vision peuvent nécessiter une aide immédiate. Le bilan causal et l’accompagnement avancent en parallèle, avec réévaluation selon les résultats.'
]
DQ = [
 'Une grande tête parentale constitue un argument de contexte. Elle ne prouve pas que l’enfant partage une simple variation, car des maladies génétiques peuvent aussi se transmettre.',
 'Le ruban ne mesure pas la pression et ne distingue pas cerveau, liquide et os. Des symptômes neurologiques nouveaux gardent leur valeur d’alarme quel que soit le centile.',
 'Ces données distinguent une grande tête ancienne et cohérente d’un changement récent. Elles doivent être datées et rapportées à une référence identifiable.',
 'Une appréciation visuelle peut être trompeuse ; une mesure documente l’argument familial. Même objectivé, cet argument doit être confronté à la santé et au développement des apparentés.',
 'La coexistence de difficultés développementales est un élément discordant. Elle justifie une évaluation neuropédiatrique ou génétique, et non une rassurance fondée uniquement sur la transmission.',
 'L’urgence dépend de la présentation : trouble de conscience ou signes de pression exigent une évaluation immédiate ; une discordance développementale ou de trajectoire stable appelle un bilan adapté.',
 'Différer l’examen est possible lorsque le tableau est isolé et rassurant. Il faut alors maintenir la vigilance et réévaluer l’indication en cas de symptôme ou d’anomalie nouvelle.',
 'Documenter la version permet de distinguer changement réel de trajectoire et changement de référence. Les lignes de centiles britanniques ne sont pas automatiquement celles de la courbe suisse.',
 'Une cassure n’est interprétable qu’après vérification technique et comparaison cohérente. Une cassure confirmée ne doit toutefois pas être attribuée sans preuve au seul changement de courbe.',
 'Les deux formulations britanniques se chevauchent à cette limite. La règle d’orientation dès deux lignes franchies doit empêcher une rassurance automatique à ce point de frontière.',
 'Le but est un développement satisfaisant et l’absence de complication. Une variation isolée ne justifie ni médicament ni intervention destinée à normaliser un chiffre.',
 'Le plan précise le prochain contrôle, ses objectifs et les motifs de consultation anticipée. Une information générale sans critères de réévaluation ne suffit pas.',
 'La perte d’acquisitions constitue une donnée nouvelle. Elle impose de rechercher une cause, même si la famille et les examens antérieurs avaient initialement rassuré.',
 'Le suivi associe croissance, fonctions et nouveaux signes. Un centile stable ne permet pas d’ignorer une difficulté de langage, de motricité ou de comportement.'
]

def ajouter_corps(raw, ident, ajout):
    start = raw.index(f'<div id="{ident}" popover')
    body = raw.index('<div class="corps">',start)+len('<div class="corps">')
    return raw[:body] + ajout + '\n' + raw[body:]

def traiter(fn,prefix,ajouts,quiz):
    p=LOT/fn;raw=p.read_text();original=raw
    assert 'RENFORCEMENT_MEDICAL_20261101' not in raw
    if prefix=='a':
        old='La taille, la trajectoire et la forme du crâne apportent des informations complémentaires.'
        new='La taille, la trajectoire et la forme du crâne apportent des <button type="button" class="terme" popovertarget="a-detail13">informations complémentaires</button>.'
        assert raw.count(old)==1;raw=raw.replace(old,new)
        pos=raw.index('<div id="a-detail14" popover')
        w='<div id="a-detail13" popover class="fenetre"><div class="barre"><span>Points clés et conclusion clinique</span><button type="button" popovertarget="a-detail13" popovertargetaction="hide" aria-label="Fermer">✕</button></div><div class="corps"></div></div>\n'
        raw=raw[:pos]+w+raw[pos:]
    for n,(addition,ns) in ajouts.items():
        raw=ajouter_corps(raw,f'{prefix}-detail{n}', '<!-- RENFORCEMENT_MEDICAL_20261101 partie '+str(n)+' -->'+addition+refs(ns))
    # Garder exactement les questions et leur réponse antérieure, puis expliciter le raisonnement.
    matches=list(re.finditer(r'(<details class="quiz">.*?</summary>)(.*?)(</details>)',raw,re.S));assert len(matches)==14
    for m,add in reversed(list(zip(matches,quiz))):
        replacement=m.group(1)+m.group(2)+'<p><strong>Raisonnement :</strong> '+add+'</p>'+m.group(3)
        raw=raw[:m.start()]+replacement+raw[m.end():]
    raw=ajouter_corps(raw,f'{prefix}-detail14','<p><em>Après chaque réponse, expliquer l’élément qui change la conduite et la limite de l’interprétation.</em></p>')
    if prefix=='a':
        raw=ajouter_corps(raw,'a-compartiments',bloc('Du mécanisme au bilan', 'Une expansion ventriculaire conduit à rechercher un obstacle ou un trouble de circulation du liquide, tandis qu’une expansion sous-arachnoïdienne impose de préciser les espaces concernés. Une anomalie du parenchyme avec régression conduit vers un autre bilan. <strong>Localiser le compartiment évite de traiter toutes les grandes têtes comme une même maladie.</strong>')+refs([7]))
        raw=ajouter_corps(raw,'a-mesure',bloc('Tracer une mesure utilisable', 'Inscrire la date, l’âge retenu, la valeur en centimètres et la courbe employée ; rapprocher le résultat de la taille et du poids. La répétition au même rendez-vous contrôle surtout la technique. Les mesures successives dans le temps renseignent sur la trajectoire : <em>ces deux répétitions répondent à des questions différentes</em>.')+refs([1,6,7]))
    # Les références existantes restent datées de leur lecture initiale ; dater aussi les relectures effectives.
    relus=[1,2,3,6,7,9,10,20] if prefix=='a' else [1,6,7,10]
    for n in relus:
        pattern=rf'(<li id="s{n}"[^>]*>.*?)(</li>)'
        raw,c=re.subn(pattern,lambda m:m.group(1)+' Passages pertinents relus le 01.11.2026.'+m.group(2),raw,count=1,flags=re.S)
        assert c==1,(fn,n)
    raw=raw.replace('Sources consultées le 31 octobre 2026.','Sources consultées le 31 octobre 2026 ; compléments relus le 1 novembre 2026.')
    # Le détail d’attribution de la revue n’est pas limité à l’Europe : coauteur au Canada.
    raw=raw.replace('Accogli et coll. — Diagnostic Approach to Macrocephaly in Children, équipes européennes, 2022','Accogli et coll. — Diagnostic Approach to Macrocephaly in Children, équipes italiennes, portugaise et canadienne, 2022')
    raw=raw.replace('La revue européenne', 'La revue d’Accogli et ses collègues')
    t=html.fromstring(raw);assert len(t.xpath('//details[@class="quiz"]'))==14
    assert len(t.xpath('//section[h2[starts-with(@id,"'+prefix+'-p")]]'))==14
    # Vérifier que la feuille de style, les polices et les figures sont intacts.
    assert re.findall(r'<style>.*?</style>',raw,re.S)==re.findall(r'<style>.*?</style>',original,re.S)
    assert re.findall(r'<figure\b.*?</figure>',raw,re.S)==re.findall(r'<figure\b.*?</figure>',original,re.S)
    p.write_text(raw)
    return {'fichier':fn,'sha256_avant':hashlib.sha256(original.encode()).hexdigest(),'sha256_apres_redaction':hashlib.sha256(raw.encode()).hexdigest(),'octets_avant':len(original.encode()),'octets_apres_redaction':len(raw.encode()),'mapping':{str(k):v[1] for k,v in ajouts.items()},'questions':14,'reponses_etendues':14}

if __name__=='__main__':
    reports=[traiter('LOT_029_Phase_A_V0.html','a',A,AQ),traiter('LOT_029_Phase_B_V0_DX.1.html','dx1',D,DQ)]
    (OUT/'CHANGEMENTS.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(reports,ensure_ascii=False,indent=2))
