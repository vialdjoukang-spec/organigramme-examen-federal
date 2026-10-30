"""Assemblage déterministe d'un texte original rédigé et sourcé pour S1.2.
Ne réalise ni rédaction automatique, ni audit médical, ni attribution de score.
"""
from pathlib import Path
from html import escape
import base64, json, re

D = Path(__file__).resolve().parent.parent
R = D.parents[1]

def ref(*ns):
    return '<sup class="s">' + ','.join(f'<a href="#s{n}">{n}</a>' for n in ns) + '</sup>'

def table(head, rows):
    return '<div class="tw"><table><thead><tr>' + ''.join(f'<th scope="col">{x}</th>' for x in head) + '</tr></thead><tbody>\n' + '\n'.join('<tr>'+''.join(f'<td>{x}</td>' for x in row)+'</tr>' for row in rows) + '\n</tbody></table></div>'

windows = {}
def window(key, title, text, sub=False):
    windows[key] = f'<div id="{key}" popover class="fenetre'+(' sousf' if sub else '')+'"><div class="barre"><span>'+title+f'</span><button type="button" popovertarget="{key}" popovertargetaction="hide" aria-label="Fermer">✕</button></div><div class="corps">'+text+'</div></div>'
    return f'<button type="button" class="terme" popovertarget="{key}">{title}</button>'

def p(s): return '<p>'+s+'</p>\n'

def bullets(items): return '<ul>'+''.join('<li>'+s+'</li>' for s in items)+'</ul>'

semantic=window('a-semantique','ce que le patient entend par perte de vision',
    p('Le symptôme recouvre plusieurs fonctions. Une baisse d’acuité diminue la perception des détails ; un déficit du champ supprime une partie de l’espace perçu. Les deux peuvent coexister. Une mesure centrale conservée ne suffit donc pas à exclure une atteinte rétinienne périphérique, un glaucome ou une lésion des voies visuelles.'+ref(3,4))+
    table(['Description du patient','Précision à obtenir','Conséquence'],[
    ['Je vois flou.','Faire lire chaque œil séparément, de loin et de près ; préciser la correction portée.','Comparer la plainte, l’acuité et le champ avant de conclure à une amétropie.'],
    ['Il manque une partie de l’image.','Faire montrer la zone manquante, puis tester chaque œil.','Un déficit similaire du même côté dans les deux yeux oriente vers les voies rétrochiasmatiques.'],
    ['Les lignes sont ondulées.','Rechercher des métamorphopsies, c’est-à-dire une déformation des lignes ou des objets.','Explorer la macula ; une apparition récente impose un avis rapide.'],
    ['Un rideau est descendu.','Préciser persistance, caractère monoculaire et début soudain ou extension progressive.','Distinguer un déficit rétinien persistant d’un épisode ischémique transitoire, tous deux urgents.'],
    ['Je vois double.','Demander si le dédoublement disparaît en couvrant un œil.','La diplopie relève aussi de l’alignement oculaire ; elle ne se confond pas avec une perte d’acuité.'],
    ['Des éclairs et des corps flottants sont apparus.','Rechercher une ombre périphérique et une baisse centrale associées.','Examiner la rétine périphérique pour rechercher une déchirure ou un décollement.']])+ref(2,3,4))

epidemio=window('a-epidemio','données suisses et limites de comparaison',
    p('L’Obsan rapporte 6,2 % de déficience visuelle déclarée dans les données de l’Enquête suisse sur la santé de 2012/2017. Il s’agit d’une difficulté à lire un livre ou un journal malgré les lunettes, chez les personnes de 15 ans ou plus vivant en ménage privé. Le bulletin indique 13 % chez les personnes de 75 ans ou plus. Ce sont des données de population, pas la probabilité d’un diagnostic chez un patient consultant aujourd’hui pour perte visuelle.'+ref(5))+
    p('L’âge, le diabète et la situation sociale influencent le risque et le retentissement. L’enquête ne couvre pas toutes les personnes institutionnalisées ; son critère déclaratif n’est pas une mesure d’acuité ni un diagnostic étiologique. Une estimation des coûts transposée à la Suisse ne doit pas être présentée comme une dépense suisse directement mesurée.'+ref(5))+
    p('Les sources consultées ne fournissent pas une incidence suisse de ce symptôme composite ni un classement unique des dix causes valables pour les urgences, les consultations courantes et tous les âges. Les numéros des diagnostics ci-dessous servent au repérage provisoire ; leur ordre de fréquence reste à établir à partir de populations comparables. Une inconnue ne vaut pas une fréquence nulle.')+
    table(['Contexte','Causes à considérer','Limite'],[
    ['Difficulté lentement progressive.','Réfraction, cristallin, macula et glaucome.','Les maladies peuvent coexister ; trouver une cataracte n’explique pas automatiquement toute la plainte.'],
    ['Perte brutale ou transitoire.','Ischémie rétinienne ou cérébrale, décollement, hémorragie vitréenne, neuropathie.','La gravité commande l’ordre des actions, quelle que soit la fréquence en population.'],
    ['Œil douloureux ou rouge.','Fermeture d’angle, kératite, uvéite, infection postopératoire.','L’absence de douleur, notamment chez certains diabétiques, n’exclut pas une affection grave.']])+ref(1,2,3))

anatomie=window('a-anatomie','trajet optique et fonctions visuelles',
    p('La lumière traverse les milieux transparents pour former une image sur la rétine. La cornée et le cristallin participent à la mise au point ; une anomalie réfractive dégrade cette mise au point, alors qu’une opacité réduit la transmission et diffuse la lumière. La correction optique et la chirurgie du cristallin agissent donc sur des mécanismes différents.'+ref(3,4))+
    p('La rétine transforme la lumière en signal nerveux. Les cônes, concentrés dans la macula, assurent la perception fine et les couleurs ; les bâtonnets contribuent à la vision en faible lumière et à la vision périphérique. Une atteinte maculaire gêne notamment la lecture et déforme les lignes, tandis qu’une lésion périphérique peut amputer le champ en épargnant d’abord l’acuité centrale.'+ref(3,4))+
    p('Le nerf optique transmet le signal aux voies visuelles. Le territoire du déficit du champ aide à localiser la lésion : monoculaire avant le chiasma, bitemporal au chiasma, homonyme dans les voies rétrochiasmatiques. Cette localisation oriente l’imagerie mais n’en détermine pas seule la cause : le mode d’installation reste décisif.'+ref(2,3))+
    p('La macula reçoit son apport métabolique de la circulation rétinienne et choroïdienne selon les couches. Une interruption vasculaire, une séparation de la rétine de son support ou une inflammation peuvent perturber rapidement le fonctionnement. La perte de tissu neural explique pourquoi une amélioration anatomique ou pressionnelle ne garantit pas une récupération visuelle complète.'+ref(2,3)))

correlation=window('a-correlation','lésion, examen et traitement',
    table(['Lésion ou perturbation','Exploration discriminante','Stratégie et mécanisme'],[
    ['Une réfraction inadéquate empêche la mise au point.','Mesure de l’acuité avec étude de réfraction.','La correction optique restaure la focalisation si elle explique le déficit.'],
    ['Le cristallin devient opaque.','La lampe à fente montre la cataracte ; examiner aussi la rétine.','La chirurgie remplace le cristallin opacifié ; le bénéfice dépend des autres atteintes.'],
    ['La macula est déformée, atrophique ou œdémateuse.','Le fond d’œil et la tomographie en cohérence optique caractérisent la lésion.','Un traitement ciblé de l’œdème ou des néovaisseaux est spécialisé ; l’atrophie nécessite aussi une réadaptation.'],
    ['Une déchirure laisse passer du liquide sous la rétine.','Le fond d’œil périphérique recherche les déchirures ; une échographie aide si les milieux sont opaques.','La chirurgie obture la déchirure et réapplique la rétine ; le délai compte pour la fonction maculaire.'],
    ['L’angle fermé bloque l’évacuation de l’humeur aqueuse.','La tonométrie et l’examen spécialisé de l’angle confirment le mécanisme.','La baisse urgente de pression précède un traitement du blocage, souvent par iridotomie dans le mécanisme pupillaire.'],
    ['L’ischémie atteint la rétine ou les voies cérébrales.','Le fond d’œil, l’examen neurologique et l’imagerie vasculaire orientée documentent le siège et la cause.','La filière vasculaire recherche une stratégie urgente et prévient d’autres événements.'],
    ['Une inflammation ou une ischémie atteint le nerf.','L’examen pupillaire, les couleurs, le champ et l’imagerie orientée complètent le fond d’œil.','Le traitement dépend de la cause ; l’artérite à cellules géantes nécessite une corticothérapie urgente si la suspicion est forte.']])+ref(1,2,3,4,6))

urgence=window('a-urgences','urgences à exclure dès le premier contact',
    p('Les repères E ci-dessous ordonnent le tri de cette leçon ; ce ne sont pas des scores validés. Plusieurs urgences se recherchent en parallèle. La suspicion de l’une d’elles justifie l’appel au service compétent pendant que l’examen bref se poursuit.'+ref(1,2,6))+
    table(['Repère','Déclencheur','Action immédiate et piège'],[
    ['🚩 E1 — Ischémie rétinienne ou cérébrale.','Perte monoculaire brutale, même récupérée, ou déficit homonyme soudain, avec ou sans autre signe neurologique.','Contacter la filière neurovasculaire et ophtalmologique ; noter l’heure du début ou le dernier état normal. Une récupération ne clôt pas le bilan.'],
    ['🚩 E2 — Artérite à cellules géantes.','Perte visuelle ou diplopie dans un contexte compatible : nouvelle céphalée, douleur du cuir chevelu, claudication mandibulaire, signes généraux.','Avis spécialisé urgent et glucocorticoïdes sans attendre la confirmation si la suspicion est forte ; protéger aussi l’autre œil.'],
    ['🚩 E3 — Fermeture aiguë de l’angle.','Œil douloureux, rouge, vision réduite, halos, nausées, pupille peu réactive.','Ophtalmologue en urgence ; mesurer la pression avec un instrument. Ne pas dilater de façon réflexe ni se fier à la palpation du globe.'],
    ['🚩 E4 — Déchirure ou décollement de rétine.','Éclairs, nouveaux corps flottants, voile ou amputation du champ.','Examen rétinien périphérique urgent ; l’acuité centrale conservée n’exclut pas une déchirure.'],
    ['🚩 E5 — Infection ou lésion oculaire menaçante.','Douleur, photophobie, lentilles, infiltrat cornéen, geste oculaire récent ou traumatisme.','Avis ophtalmologique immédiat. En brûlure chimique, irriguer avant le transfert. Ne pas commencer un corticoïde local sans évaluation spécialisée.'],
    ['🚩 E6 — Atteinte intracrânienne.','Céphalée avec œdème papillaire bilatéral, déficit du champ, altération neurologique ou progression atypique.','Organiser l’évaluation neurologique et l’imagerie urgente adaptée ; un fond d’œil normal n’exclut pas une lésion rétrobulbaire ou cérébrale.']])+ref(1,2,6))

history=window('a-anamnese','questions qui changent la conduite',
    table(['Question','Pourquoi elle discrimine','Action si positive'],[
    ['Quand voyiez-vous normalement pour la dernière fois ?','Une perte brutale évoque notamment une ischémie ; une aggravation sur plusieurs jours n’est pas automatiquement bénigne.','Documenter l’heure et organiser la filière urgente si installation aiguë.'],
    ['Quel œil ? Avez-vous essayé de les couvrir séparément ?','Un déficit du même hémichamp dans les deux yeux peut être décrit à tort comme monoculaire.','Vérifier la latéralité par l’examen du champ.'],
    ['La gêne a-t-elle disparu complètement ?','Une ischémie transitoire laisse parfois un examen normal entre les épisodes.','Rechercher le mécanisme vasculaire sans attendre une récidive.'],
    ['Existe-t-il une douleur, des halos, une photophobie ou des nausées ?','Une atteinte cornéenne ou une fermeture d’angle peut associer perte visuelle et douleur ; la névrite peut faire mal aux mouvements.','Comparer segment antérieur, pupilles, motilité et pression instrumentale.'],
    ['Des éclairs, une pluie de points ou un rideau ?','La traction vitréorétinienne, une déchirure et un saignement peuvent précéder la perte centrale.','Faire examiner la rétine périphérique sans rassurer sur la seule acuité.'],
    ['Nouvelle céphalée, mâchoire douloureuse en mâchant, symptômes généraux ?','Ces signes soutiennent une artérite à cellules géantes dans le contexte approprié.','Ne pas attendre la biopsie ou l’imagerie pour traiter une forte suspicion.'],
    ['Lentilles, projection, choc, intervention ou injection dans l’œil ?','Une rupture de barrière ou une inoculation change la probabilité d’infection et d’atteinte traumatique.','Organiser l’examen urgent ; apporter les lentilles retirées et leur étui si infection suspectée.'],
    ['Diabète, maladie vasculaire, médicaments et ancien état visuel ?','Ces éléments orientent les causes et les risques thérapeutiques ; une atteinte préexistante peut masquer un changement aigu.','Comparer aux anciennes mesures et vérifier les traitements, sans attribuer automatiquement le nouveau symptôme au terrain.']])+ref(1,2,3,6))

exam=window('a-examen','examen comparatif des deux yeux',
    table(['Geste','Normal attendu','Anomalie et limite'],[
    ['Mesurer l’acuité de chaque œil, de loin et de près, avec la correction habituelle puis une réfraction adaptée.','La lecture est cohérente avec l’état habituel et les conditions de test sont documentées.','Noter l’échelle et la correction. Une mauvaise coopération ou une mauvaise distance fausse le résultat ; une acuité centrale préservée n’explore pas tout le champ.'],
    ['Observer les pupilles avant tout collyre et rechercher les réponses directe et consensuelle.','L’éclairement d’un œil entraîne une constriction des deux pupilles.','Une asymétrie de réponse peut orienter vers une atteinte afférente ou efférente ; interpréter avec l’examen neurologique.'],
    ['Comparer le champ visuel par confrontation en maintenant la fixation.','Le patient détecte les cibles dans les secteurs explorés des deux yeux.','Ce dépistage est grossier. Un déficit central ou périphérique demande une exploration adaptée ; la périmétrie ne doit pas retarder l’urgence.'],
    ['Inspecter l’œil et examiner la cornée et la chambre antérieure à la lampe à fente si disponible.','La cornée est transparente et la chambre antérieure sans inflammation visible.','Chercher un infiltrat, un défaut épithélial, un hypopion, une inflammation ou une faible profondeur ; l’examen sans lampe à fente est limité.'],
    ['Mesurer la pression avec un tonomètre dans un contexte approprié.','Le résultat est interprété avec l’angle, la papille et le contexte.','La palpation bidigitale n’est pas assez fiable selon les HUG. Une mesure isolée normale n’exclut pas un glaucome chronique.'],
    ['Examiner le fond d’œil et la périphérie selon le contexte de sécurité.','Papille à contours nets, macula et rétine sans lésion expliquant la perte.','Chercher décollement, hémorragies, ischémie, œdème ou anomalie maculaire ; si le fond est inaccessible, ne pas le noter normal.'],
    ['Compléter par motilité, couleurs et examen neurologique ciblé.','Les mouvements et la perception des couleurs sont comparables, sans déficit neurologique focal.','La douleur aux mouvements et la dyschromatopsie orientent vers le nerf ; un déficit homonyme ou neurologique aigu impose la filière cérébrovasculaire.']])+ref(1,2,3,4))

syndromes=window('a-syndromes','syndromes et localisation',
    table(['Syndrome','Signes fonctionnels','Recherche clinique et mécanisme'],[
    ['7.1 — Atteinte des milieux optiques.','Flou, gêne à l’éblouissement, perte de détails.','Étudier la réfraction, examiner cornée et cristallin ; la focalisation ou la transparence est altérée.'],
    ['7.2 — Syndrome maculaire.','Lecture difficile, lignes déformées, tache centrale.','Comparer la vision centrale de chaque œil ; fond d’œil et OCT maculaire objectivent la lésion de la rétine centrale.'],
    ['7.3 — Syndrome rétinien périphérique.','Éclairs, nouveaux corps flottants, rideau périphérique.','Rechercher le déficit du champ et examiner la périphérie rétinienne ; une traction ou une déchirure peut précéder le décollement.'],
    ['7.4 — Neuropathie optique.','Couleurs altérées, baisse centrale ou déficit du champ, parfois douleur aux mouvements.','Comparer pupilles et couleurs, examiner papille et champ ; un fond d’œil normal reste possible dans une atteinte rétrobulbaire.'],
    ['7.5 — Atteinte rétrochiasmatique.','Une moitié de l’espace semble manquer.','Tester chaque œil et rechercher un déficit homonyme ; localiser la lésion cérébrale, puis distinguer installation vasculaire aiguë et cause progressive.'],
    ['7.6 — Œil rouge douloureux avec perte visuelle.','Douleur, photophobie, halos ou baisse de vision.','Examiner cornée, chambre antérieure, pupille et pression ; distinguer fermeture d’angle, kératite, uvéite et infection profonde.'],
    ['7.7 — Déficit transitoire.','Épisode négatif monoculaire, phénomènes visuels progressifs ou éclipses positionnelles.','Reconstruire le déroulement ; ischémie, aura et œdème papillaire ont des mécanismes et une urgence différents. Un premier épisode atypique ne se classe pas comme migraine par défaut.']])+ref(1,2,3,4))

criteria=window('a-criteres','ce qui établit le symptôme et ce qui confirme sa cause',
    p('S1.2 est une situation clinique de départ, pas une maladie à critères uniques. Les chapitres COUF 2025 organisent sa démarche autour de l’histoire, des fonctions visuelles et de l’examen anatomique. La perte visuelle se documente par comparaison à l’état antérieur, aux deux yeux et avec correction ; le diagnostic causal réclame ensuite une concordance clinique et instrumentale.'+ref(2,3,4))+
    table(['Constat','Ce qu’il permet','Ce qu’il ne permet pas'],[
    ['Une acuité est réduite.','Objectiver une atteinte de la vision centrale dans les conditions du test.','Conclure à une cataracte, à une neuropathie ou à une origine fonctionnelle sans exploration.'],
    ['Le champ est altéré.','Localiser une atteinte et compléter la mesure centrale.','Exclure une urgence parce que la lecture des optotypes reste bonne.'],
    ['Un OCT maculaire montre une lésion concordante.','Documenter un œdème, une atrophie ou une anomalie de traction.','Exclure une pathologie périphérique ou cérébrale non couverte par l’examen.'],
    ['Le fond d’œil semble normal.','Écarter certaines lésions visibles si l’examen est complet.','Exclure une névrite rétrobulbaire, une atteinte des voies visuelles ou un événement transitoire.'],
    ['Une artérite à cellules géantes est fortement suspectée.','Déclencher sans retard le traitement protecteur et la confirmation spécialisée.','Attendre un score de classification, une biopsie ou la disparition des symptômes pour décider.']])+ref(2,3,6))

explorations=window('a-explorations','9.a à 9.d — prescrire puis interpréter',
    p('9.a — Il n’existe pas d’examen de référence unique de la perte de vision. Le fond d’œil confirme certaines lésions rétiniennes, tandis que l’OCT caractérise la macula. L’exploration de l’angle et du nerf guide le glaucome. L’imagerie cérébrale ou orbitaire répond à une question neurologique. Le test se choisit selon la localisation et l’urgence.'+ref(2,3,4))+
    p('9.b — En première intention, documenter les fonctions de chaque œil, les pupilles, le segment antérieur, la pression si indiquée et le fond d’œil. Simultanément, si l’ischémie ou une autre urgence est suspectée, contacter la filière spécialisée : les examens de cabinet ne doivent pas retarder ce contact.'+ref(1,2))+
    table(['Examen et indication','Résultat utile','Interprétation et action'],[
    ['OCT maculaire pour déformation centrale ou lésion maculaire.','Œdème, atrophie, traction ou tissu anormal concordant.','Orienter le traitement rétinien ; un résultat maculaire normal ne termine pas le bilan d’un déficit du champ.'],
    ['OCT du nerf et périmétrie pour neuropathie ou glaucome.','Anomalie structurelle ou fonctionnelle concordante.','Comparer au contexte et aux mesures antérieures ; ne pas confondre une anomalie isolée avec un diagnostic complet.'],
    ['Échographie oculaire B si le fond d’œil est masqué.','Décollement ou autre lésion derrière les milieux opaques.','Rechercher une cause chirurgicale ; le geste relève d’un examen adapté au contexte traumatique éventuel.'],
    ['Imagerie cérébrale et vasculaire si ischémie suspectée.','Lésion ou mécanisme vasculaire.','Adresser immédiatement à la filière vasculaire ; ne pas considérer l’absence d’autre signe neurologique comme rassurante.'],
    ['Imagerie orbitaire et cérébrale pour neuropathie suspectée.','Atteinte du nerf, compression ou autre anomalie.','Adapter l’examen à la question clinique et demander l’avis neurologique/ophtalmologique.'],
    ['Bilan inflammatoire et confirmation d’ACG.','Concordance clinique, biologique, échographique ou histologique.','Une forte suspicion avec menace visuelle se traite avant la confirmation ; les critères de classification ne remplacent pas le jugement diagnostique.'],
    ['Angiographie rétinienne si le spécialiste doit préciser perfusion ou néovaisseaux.','Zones non perfusées, fuite ou néovascularisation.','Compléter la stratégie rétinienne ; l’OCT-angiographie est une technique distincte sans injection.']])+ref(2,3,4,6)+
    p('9.c — Si l’examen initial est impossible, documenter pourquoi : milieux opaques, douleur, coopération ou matériel manquant. Organiser l’alternative spécialisée au lieu de transformer une absence d’observation en résultat négatif. Une grossesse, une insuffisance rénale, un antécédent de réaction au contraste ou un implant imposent de choisir le protocole d’imagerie avec le radiologue ; aucun seuil d’exclusion non vérifié n’est ajouté ici.')+
    p('9.d — Une perte persistante inexpliquée nécessite un avis spécialisé et, selon les résultats, une périmétrie plus précise, des examens électrophysiologiques ou un bilan étiologique orienté. Les résultats discordants doivent conduire à recontrôler la mesure et la localisation ; ils ne justifient pas d’emblée un diagnostic fonctionnel.'+ref(2,3,4)))

algorithm=window('a-algorithme','arbre de décision clinique',
    '<ol class="algo">'+''.join('<li>'+x+'</li>' for x in [
    'Si projection chimique : commencer immédiatement une irrigation abondante et appeler l’ophtalmologue. Si traumatisme ou contexte postopératoire avec perte visuelle : organiser l’examen urgent.',
    'Si perte brutale, même transitoire, ou déficit homonyme soudain : noter le dernier état visuel normal et activer l’évaluation vasculaire avec l’ophtalmologue et le neurologue.',
    'Si une artérite à cellules géantes est fortement suspectée : traiter sans délai par glucocorticoïdes et organiser la confirmation ; une atteinte visuelle impose une prise en charge immédiate.',
    'Si œil rouge, douloureux ou photophobe : examiner le segment antérieur et la pression ; adresser en urgence pour fermeture d’angle, kératite, uvéite ou infection profonde.',
    'Si éclairs, nouveaux corps flottants ou rideau : rechercher déchirure et décollement par un examen rétinien périphérique urgent. Si le fond est masqué, organiser une échographie adaptée.',
    'Si douleur aux mouvements, couleurs altérées ou déficit pupillaire : explorer le nerf optique, même quand la papille paraît normale.',
    'Si installation progressive sans drapeau rouge : mesurer les deux yeux avec correction, puis rechercher successivement une anomalie des milieux, de la macula et du nerf. Un déficit du champ oriente également vers le chiasma et les voies cérébrales.',
    'Si le résultat ne correspond pas à la plainte ou si la vision s’aggrave : réévaluer sans conclure par défaut à une cause bénigne. Fixer la prochaine étape et les conditions de retour urgent.'
    ])+'</ol>'+ref(1,2,3,4,6))

# Les longues citations AIPS proviennent du corpus local fourni avec le dépôt.
aips={n:json.loads((D/'evidence'/f'AIPS_{n}.json').read_text())['sections'] for n in ('21191','35112')}
def quotes(s): return '<blockquote>'+ '\n'.join('<p>« '+escape(line)+' »</p>' for line in s.splitlines() if line.strip())+'</blockquote>'

interactions=window('a-interactions','interactions et surveillance avant traitement',
    p('Le traitement urgent exige aussi une conciliation médicamenteuse ciblée. Les tableaux suivants résument des risques explicitement décrits dans les deux informations professionnelles suisses lues. Ils ne remplacent pas la vérification de l’ensemble des traitements concomitants.'+ref(7,8))+
    table(['Médicament','Association ou terrain','Conséquence pratique'],[
    ['Acétazolamide.','Acide acétylsalicylique à doses élevées.','L’AIPS décrit un risque d’acidose métabolique sévère et de toxicité neurologique accrue ; rechercher cette association avant administration.'],
    ['Acétazolamide.','Autres diurétiques éliminant le potassium ou traitement par digoxine.','L’hypokaliémie, la déshydratation et la toxicité digitalique peuvent être favorisées ; contrôler le contexte électrolytique et adapter la stratégie.'],
    ['Acétazolamide.','Méthotrexate, anticoagulant oral, sulfamide hypoglycémiant ou phénytoïne.','La monographie décrit une augmentation de toxicité ou d’effet selon la molécule ; une révision individualisée des traitements est nécessaire.'],
    ['Acétazolamide.','Autre inhibiteur de l’anhydrase carbonique.','L’association n’est pas recommandée par l’AIPS en raison d’effets additifs possibles.'],
    ['Acétazolamide.','Lithium ou ciclosporine.','L’excrétion du lithium augmente et son effet peut diminuer ; la concentration de ciclosporine peut augmenter. Informer le prescripteur et choisir la surveillance adaptée.'],
    ['Méthylprednisolone.','Inhibiteur du CYP3A4, notamment certains azolés, macrolides ou traitements contenant ritonavir/cobicistat.','L’exposition aux corticoïdes peut augmenter. Évaluer bénéfices et risques et surveiller la toxicité ; une adaptation peut être nécessaire.'],
    ['Méthylprednisolone.','Inducteur du CYP3A4, notamment rifampicine ou certains antiépileptiques.','L’exposition et l’efficacité peuvent diminuer ; la décision d’ajustement relève du prescripteur.'],
    ['Méthylprednisolone.','Anti-inflammatoire non stéroïdien.','Le risque d’ulcère et d’hémorragie digestive peut augmenter ; considérer les facteurs de risque digestifs.'],
    ['Méthylprednisolone.','Antidiabétique ou médicament qui augmente l’excrétion potassique.','Surveiller la glycémie et les électrolytes, puis adapter si nécessaire.'],
    ['Méthylprednisolone.','Antagoniste de la vitamine K ou autre immunosuppresseur.','La coagulation peut varier ; l’immunosuppression peut s’additionner. Évaluer les contrôles et le risque infectieux.']])+ref(7,8)+
    p('Une absence de seuil numérique dans la source ne justifie pas d’en inventer un. Les contre-indications restent prioritaires sur une adaptation empirique. Le contrôle biologique et la surveillance doivent être organisés sans retarder l’orientation urgente nécessaire.'+ref(7,8)),True)

diamox=window('a-diamox','acétazolamide : indication ciblée et précautions',
    p('L’acétazolamide diminue la production d’humeur aqueuse par inhibition de l’anhydrase carbonique. Il relève ici de la prise en charge spécialisée d’une hypertonie aiguë appropriée, et ne constitue pas un traitement empirique de toute perte visuelle. Diamox® comprimés : Swissmedic 21191 ; poudre injectable/perfusion : 22002, vérifiés dans la liste des conditionnements du 30.09.2026.'+ref(7))+
    p('AIPS, rubrique glaucome, adultes :')+quotes(aips['21191']['posologie'].split('Oedèmes')[0])+
    p('La monographie prévoit une injection intraveineuse lente ou une perfusion ; la préparation et le rythme relèvent de l’équipe qui surveille le patient. La baisse de pression ne remplace pas le traitement du mécanisme de fermeture. Le suivi dépend de la réponse instrumentale et de l’état de la cornée, avec l’ophtalmologue. Vérifier aussi les '+interactions+'.'+ref(2,7))+
    quotes(aips['21191']['contre_indications'])+
    p('L’AIPS demande de surveiller cellules sanguines et électrolytes avant puis régulièrement lors du traitement prolongé. Une réaction sévère d’hypersensibilité, une atteinte cutanée toxique ou une suspicion d’œdème pulmonaire non cardiogénique impose l’arrêt et une prise en charge immédiate. Une nouvelle baisse visuelle après administration doit aussi faire évoquer un épanchement ou décollement choroïdien médicamenteux.'+ref(7))+
    quotes(aips['21191']['grossesse'])+
    p('Pédiatrie, citation AIPS :')+quotes(next(line for line in aips['21191']['posologie'].splitlines() if line.startswith('A ce jour,')))+
    p('Aucune dose pédiatrique n’est extrapolée. La contre-indication en affection rénale ou hépatique grave ne se remplace pas par une simple réduction empirique de dose.'+ref(7)),True)

steroid=window('a-corticoides','glucocorticoïdes : urgence inflammatoire et AIPS',
    p('Une forte suspicion d’artérite à cellules géantes justifie des glucocorticoïdes sans attendre les examens confirmatoires. La sélection de la voie et du protocole dans une atteinte visuelle se fait en urgence avec le spécialiste. Les recommandations EULAR 2025, publiées en 2026, et l’information professionnelle suisse répondent à deux questions différentes : stratégie pour la maladie et conditions d’emploi d’une spécialité.'+ref(6,8))+
    p('EULAR discute des bolus intraveineux de méthylprednisolone dans des cas sélectionnés de perte visuelle aiguë attribuable à une ACG active ; le bénéfice reste incertain. Le protocole chiffré propre à l’ACG et son statut dans l’information professionnelle suisse restent à vérifier. Aucun schéma EULAR n’est transposé ici en posologie AIPS. L’initiation urgente et le choix du protocole relèvent de l’équipe spécialisée, qui doit expliciter tout usage hors information professionnelle.'+ref(6,8))+
    p('Solu-MEDROL®, poudre et solvant 500 mg ou 1 g, Swissmedic 35112, information mise à jour en août 2025 :')+
    quotes(next(line for line in aips['35112']['posologie'].splitlines() if line.startswith('La durée d’administration') or line.startswith("La durée d'administration")))+
    quotes(aips['35112']['contre_indications'])+
    p('La surveillance comprend état infectieux, pression artérielle, glycémie, électrolytes et effets neuropsychiatriques. La dose et la durée augmentent la charge d’effets indésirables. La monographie avertit contre une réduction trop rapide après plusieurs jours : le relais et la décroissance doivent être individualisés pour éviter la réactivation de la maladie et l’insuffisance corticosurrénale. Vérifier aussi les '+interactions+'.'+ref(8))+
    quotes(aips['35112']['grossesse'])+
    p('Chez l’insuffisant hépatique grave, le métabolisme est ralenti et une réduction peut être nécessaire. En insuffisance rénale, l’AIPS indique la prudence sans adaptation obligatoire. Le produit ne doit pas être utilisé chez le prématuré et le nouveau-né ; les formulations contenant de l’alcool benzylique nécessitent une attention spécifique. Aucun de ces éléments ne permet d’extrapoler un protocole de névrite ou d’ACG à toutes les pertes visuelles.'+ref(8)),True)

treatment=window('a-traitement','11.A à 11.D — conduite, surveillance et retour',
    p('11.A — Le but immédiat est de préserver le tissu visuel encore fonctionnel, protéger l’autre œil lorsque la maladie est bilatéralisante et identifier une menace neurologique ou systémique. La rapidité vise l’action utile : appel spécialisé, irrigation si brûlure et traitement de la cause. Aucun objectif universel chiffré d’acuité ou de pression ne convient à tous les mécanismes.'+ref(1,2,6))+
    p('11.B — Dès le contact, noter la chronologie, l’état de chaque œil et les drapeaux rouges. Pendant l’organisation de la prise en charge, recueillir traitements, allergies, antécédents et fonction rénale/hépatique utiles. Les décisions urgentes ne sont pas différées pour réaliser tous les examens ambulatoires.'+ref(1,2,6))+
    table(['Situation','Première action','Suite spécialisée'],[
    ['Brûlure chimique.','Irriguer immédiatement, abondamment, avec eau disponible, solution saline ou Ringer ; les HUG indiquent au moins 30 minutes.','Examen ophtalmologique urgent après et pendant l’organisation du transfert ; ne pas attendre le produit de rinçage idéal.'],
    ['Suspicion vasculaire rétinienne ou cérébrale.','Organiser l’évaluation urgente et documenter l’heure.','L’équipe évalue les options et la prévention vasculaire. La thrombolyse ne se présente pas ici comme traitement systématique de toute occlusion rétinienne.'],
    ['Suspicion forte d’ACG avec menace visuelle.','Commencer les glucocorticoïdes sans attendre la confirmation, avec avis spécialisé immédiat.','Documenter ensuite la cause et le protocole : '+steroid+'.'],
    ['Crise de fermeture d’angle.','Appel ophtalmologique urgent et baisse contrôlée de la pression.','Le spécialiste choisit collyres et traitement systémique : '+diamox+' ; le mécanisme obstructif nécessite sa propre correction.'],
    ['Décollement de rétine.','Avis rétinien urgent ; documenter l’atteinte du champ et de la macula.','La chirurgie traite le décollement ; les consignes de positionnement sont individualisées par l’équipe rétinienne.'],
    ['Kératite ou infection postopératoire suspectée.','Avis ophtalmologique urgent ; retirer et conserver les lentilles si pertinentes.','Examens et antimicrobiens selon cause et gravité ; éviter un corticoïde local empirique.'],
    ['Cause progressive documentée.','Adapter correction et orientation ; rechercher les lésions associées.','Chirurgie de cataracte, traitement du glaucome, de la maladie rétinienne ou réadaptation selon diagnostic.']])+ref(1,2,3,6,7,8)+
    p('11.C — Réévaluer la fonction visuelle et les symptômes, puis les paramètres spécifiques : pression et cornée dans l’hypertonie, évolution rétinienne, signes neurologiques ou inflammatoires. La surveillance biologique dépend du traitement choisi. Une aggravation, l’atteinte de l’autre œil, une douleur nouvelle ou une réaction médicamenteuse impose une réévaluation urgente.'+ref(1,2,6,7,8))+
    p('11.D — Le retour à domicile suppose une cause évaluée ou une investigation urgente organisée, un plan de traitement compréhensible, le suivi fixé et un transport adapté à la fonction visuelle. Le patient reçoit des consignes de retour explicites. Ces éléments forment une synthèse pratique de continuité des soins, et non un score de sortie validé.')+
    p('Le pronostic dépend du mécanisme, de la macula et du nerf, de la fonction antérieure et du délai. Restaurer la transparence optique peut améliorer la vision ; la destruction rétinienne ou nerveuse peut laisser un déficit malgré un contrôle de la maladie. La réadaptation visuelle et le soutien dans la vie quotidienne commencent selon les besoins, sans attendre que toutes les options curatives soient épuisées.'+ref(2,3,5)))

prevention=window('a-prevention','prévenir la maladie et réduire le handicap',
    table(['Niveau','Mesures concrètes','Lien avec les sources'],[
    ['Prévention primaire.','Informer sur protection oculaire lors d’exposition, usage prudent des lentilles et prise en compte du risque métabolique et vasculaire.','Les HUG identifient lentilles, traumatismes et terrain à risque ; l’Obsan décrit l’association au diabète et aux déterminants sociaux.'],
    ['Prévention secondaire.','Surveiller les affections oculaires connues même sans plainte centrale et organiser l’examen quand apparaît une modification.','COUF rappelle que glaucome chronique et rétinopathie diabétique peuvent rester peu symptomatiques avant une atteinte avancée. Aucun intervalle suisse de dépistage non vérifié n’est inventé.'],
    ['Prévention tertiaire.','Adapter éclairage, lecture et activités ; rechercher chutes, isolement, difficulté à prendre les traitements et double déficit auditif-visuel.','L’Obsan décrit le retentissement fonctionnel et psychique. L’organisation de l’aide dépend des besoins individuels.'],
    ['Prévention d’un retard urgent.','Apprendre au patient à consulter devant une perte soudaine, un rideau, des éclairs récents, une douleur ou une déformation nouvelle.','Les conduites HUG et COUF imposent une évaluation rapide ; une perte transitoire n’est pas un motif de rassurance.']])+ref(1,2,3,4,5))

quiz_items=[
('Une bonne acuité centrale exclut-elle un décollement périphérique ?','Non. Le champ et la rétine périphérique doivent être évalués si éclairs, corps flottants ou rideau sont apparus.',(2,4)),
('Une perte monoculaire qui a disparu peut-elle attendre une consultation de routine ?','Non si un événement ischémique est suspecté. La récupération n’annule pas le risque rétinien ou cérébral.',(2,)),
('Un fond d’œil normal exclut-il une cause organique ?','Non. Une atteinte rétrobulbaire ou rétrochiasmatique peut laisser un fond d’œil normal.',(2,3)),
('Faut-il attendre la biopsie pour traiter une forte suspicion d’ACG ?','Non. Les glucocorticoïdes débutent sans délai tandis que la confirmation est organisée.',(6,)),
('Peut-on confirmer la pression élevée par palpation du globe ?','Les HUG déconseillent cette appréciation, trop peu fiable ; une mesure instrumentale et un examen spécialisé sont requis.',(1,)),
('Une baisse visuelle sur œil rouge est-elle une conjonctivite simple jusqu’à preuve du contraire ?','Non. Rechercher atteinte cornéenne, inflammation intraoculaire et fermeture d’angle ; adresser en urgence selon les signes.',(1,2)),
('Faut-il attendre une solution stérile pour irriguer une brûlure chimique ?','Non. Les HUG permettent l’eau du robinet disponible ; l’irrigation immédiate et abondante précède le transfert.',(1,)),
('Une cataracte visible suffit-elle à expliquer une baisse sévère ?','Non. Examiner la macula et les autres structures ; une maladie rétinienne peut coexister.',(3,)),
('Les 6,2 % de l’Obsan sont-ils la fréquence suisse des consultations pour perte aiguë ?','Non. C’est une déficience visuelle déclarée dans une enquête de population avec une définition et une période précises.',(5,)),
('Une occlusion artérielle et une occlusion veineuse ont-elles la même conduite ?','Non. Les mécanismes, le bilan vasculaire urgent et les complications rétiniennes diffèrent ; le fond d’œil et le contexte orientent.',(2,)),
('Le numéro Swissmedic du comprimé Diamox identifie-t-il sa poudre injectable ?','Non. Les numéros lus sont 21191 pour le comprimé et 22002 pour la poudre injectable/perfusion.',(7,)),
('Une atteinte rénale grave sous Diamox se gère-t-elle toujours par réduction de dose ?','Non. L’information professionnelle la classe parmi les contre-indications ; vérifier la situation avant prescription.',(7,)),
('Un schéma EULAR de corticoïdes devient-il automatiquement une posologie AIPS spécifique de l’ACG ?','Non. Il faut distinguer recommandation de stratégie, indication autorisée et conditions de la spécialité ; expliciter un usage hors information professionnelle.',(6,8)),
('Une perte du même côté du champ des deux yeux correspond-elle nécessairement à un problème d’un seul œil ?','Non. Un déficit homonyme oriente vers les voies rétrochiasmatiques ; l’installation brutale impose une recherche vasculaire urgente.',(2,3))]
quiz=window('a-pieges','Pièges d’examen','\n'.join('<details class="quiz"><summary>'+q+'</summary>'+p(a+ref(*rr))+'</details>' for q,a,rr in quiz_items))

sections=[
('Définition et sémantique',p('Une perte de vision est une diminution ressentie ou mesurée d’une ou plusieurs fonctions visuelles : acuité, champ, couleurs ou contraste. Selon le cadre sémiologique du COUF 2025, le premier geste est de préciser '+semantic+', sa latéralité et son installation. Le symptôme peut être partiel ou transitoire et garder une cause urgente.'+ref(2,3,4))),
('Épidémiologie en Suisse et en Europe',p('L’Obsan rapporte 6,2 % de déficience visuelle déclarée dans l’Enquête suisse sur la santé de 2012/2017, avec une fréquence accrue à un âge avancé. Ces '+epidemio+' ne permettent pas de classer directement les causes d’une consultation aiguë. La gravité doit donc guider le premier tri, puis la fréquence s’apprécie dans le contexte clinique.'+ref(5))),
('Physiopathologie et bases indispensables',p('Le '+anatomie+' explique pourquoi une opacité, une lésion maculaire, une neuropathie et une atteinte cérébrale ne se recherchent pas de la même manière. La localisation relie le signe à son mécanisme, puis au choix d’examen et de traitement. Le tableau '+correlation+' permet de suivre ce raisonnement.'+ref(2,3,4))),
('Démarche diagnostique : les graves d’abord',p('Le tri commence par les '+urgence+', notamment l’ischémie rétinienne ou cérébrale, l’artérite à cellules géantes, la fermeture d’angle et le décollement rétinien. L’absence de douleur ou la récupération de la vision ne suffit pas à rassurer. Le diagnostic et l’appel spécialisé avancent ensemble quand le délai menace la fonction visuelle.'+ref(1,2,6))),
('Anamnèse ciblée et drapeaux rouges',p('Les '+history+' précisent le dernier état normal, le caractère monoculaire ou binoculaire, la persistance et les signes associés. Les lentilles, une projection, un traumatisme, une intervention récente et les traitements modifient le niveau d’urgence. Le patient décrit la séquence avec ses mots ; l’examen vérifie ensuite la localisation.'+ref(1,2))),
('Examen physique ciblé',p('L’'+exam+' documente l’acuité, le champ, les pupilles, le segment antérieur et le fond d’œil selon les moyens disponibles. L’examen du patient symptomatique se compare à l’autre œil et aux données antérieures, sans oublier que les deux yeux peuvent être atteints. Une impossibilité d’examen doit être notée et conduire à une solution adaptée.'+ref(1,2,3,4))),
('Approche syndromique',p('Les '+syndromes+' regroupent les symptômes selon leur mécanisme : milieux optiques, macula, rétine périphérique, nerf, voies cérébrales ou segment antérieur inflammatoire. Les signes fonctionnels guident les gestes qui cherchent une anomalie objective. La chronologie traverse tous ces syndromes et détermine l’urgence.'+ref(1,2,3))),
('Diagnostic positif et critères',p('Il faut distinguer '+criteria+'. Il n’existe pas de score unique validé pour ce symptôme composite ; chaque cause possède ses propres examens et critères. Une anomalie isolée ou un résultat négatif mal adapté ne remplace pas une concordance clinique.'+ref(2,3,4,6))),
('Examens complémentaires',p('Le plan '+explorations+' commence par la question clinique et l’examen qui peut réellement y répondre. Les explorations rétiniennes, du nerf et des voies cérébrales ne sont pas interchangeables. Une suspicion urgente se prend en charge pendant l’organisation du bilan, sans attendre une batterie systématique.'+ref(1,2,3,4))),
('Arbre décisionnel',p('L’'+algorithm+' traite d’abord les urgences identifiables, puis localise l’atteinte. Chaque branche aboutit à un geste ou à une orientation concrète. Les causes fréquentes progressives sont recherchées après ce tri, avec réévaluation si les résultats ne correspondent pas à la plainte.'+ref(1,2,3,6))),
('Prise en charge en Suisse',p('La prise en charge suit '+treatment+' : préserver la vision, traiter la cause et assurer la continuité des soins. Une brûlure s’irrigue immédiatement ; une suspicion ischémique ou une menace inflammatoire impose une filière urgente. Les doses, contre-indications et situations particulières restent dans les fenêtres thérapeutiques, avec leur source suisse.'+ref(1,2,6,7,8))),
('Prévention',p('Les mesures pour '+prevention+' associent protection, dépistage approprié et réadaptation. Le glaucome et la rétinopathie diabétique peuvent progresser avant qu’une baisse centrale soit ressentie. Une difficulté de lecture, une chute ou un isolement doivent aussi faire rechercher le retentissement visuel.'+ref(1,4,5))),
('Points clés',p('Une perte brutale ou transitoire se considère comme urgente jusqu’à une évaluation adaptée. Une acuité centrale conservée ne garantit ni un champ intact ni une rétine périphérique normale. Un fond d’œil normal n’exclut pas une atteinte du nerf ou du cerveau. Une forte suspicion d’artérite à cellules géantes se traite sans attendre sa confirmation, avec un protocole spécialisé vérifié contre l’information professionnelle suisse.'+ref(1,2,4,6,7,8))),
('Pièges et questions de révision',p('Les '+quiz+' vérifient les décisions qui protègent le patient et évitent les confusions de mécanisme. Ces questions pédagogiques sont rédigées pour cette leçon à partir des sources citées ; elles ne sont pas présentées comme des questions officielles de l’examen fédéral. Une réponse correcte doit relier le signe, l’examen et l’action.'+ref(1,2,3,4,5,6,7,8)))
]

dx=[
('Amétropie non corrigée','Une gêne liée à la mise au point peut s’améliorer avec la correction adaptée.','L’étude de réfraction confronte correction et acuité.','La correction focalise l’image sur la rétine.','Corriger puis rechercher une autre cause si le déficit persiste.','Pas de rang E si forme isolée progressive.',(3,4)),
('Cataracte','Une opacité du cristallin accompagne une perte progressive, mais peut être associée à une maladie maculaire.','La lampe à fente montre l’opacité ; le fond d’œil recherche une autre atteinte.','Le cristallin altéré transmet moins bien la lumière.','Évaluer la gêne et le bénéfice attendu d’une chirurgie.','Une présentation aiguë demande une autre explication.',(3,4)),
('Dégénérescence maculaire liée à l’âge','Des métamorphopsies et une atteinte centrale orientent vers la macula.','Le fond d’œil et l’OCT caractérisent la forme et la lésion.','La lésion maculaire altère la vision fine ; une complication exsudative change l’urgence.','Organiser un avis rapide devant une déformation ou baisse récente.','Une aggravation récente justifie un avis urgent.',(2,3)),
('Glaucome primitif à angle ouvert','L’atteinte du champ peut précéder la plainte d’acuité centrale.','Papille, pression instrumentale, périmétrie et OCT s’interprètent ensemble.','La neuropathie glaucomateuse altère les fibres et le champ.','Organiser la prise en charge spécialisée et le suivi.','La crise de fermeture d’angle est une autre urgence : E3.',(3,4)),
('Rétinopathie diabétique','La maculopathie, l’hémorragie vitréenne et la traction peuvent produire des présentations différentes.','Le fond d’œil et l’OCT, complétés selon le cas, localisent le mécanisme.','La maladie rétinienne peut entraîner œdème, néovaisseaux et traction.','Adresser rapidement une baisse nouvelle ; adapter traitement rétinien et facteurs systémiques.','Un saignement ou un décollement impose un avis urgent.',(2,3)),
('Occlusion veineuse rétinienne','Une baisse souvent indolore accompagne des hémorragies et des veines dilatées.','Fond d’œil et OCT, puis angiographie selon besoin.','L’obstacle veineux entraîne œdème et parfois ischémie et néovaisseaux.','Évaluation ophtalmologique et surveillance des complications.','Douleur et hypertonie peuvent signaler un glaucome néovasculaire.',(1,2,3)),
('Décollement de rétine rhegmatogène','Des éclairs, corps flottants et une ombre périphérique précèdent parfois l’atteinte centrale.','L’examen périphérique recherche rétine soulevée et déchirures ; échographie si milieux opaques.','Une déchirure permet le passage de liquide sous la rétine.','Adresser en urgence à l’équipe rétinienne.','🚩 E4.',(2,)),
('Névrite optique','Une baisse rapidement progressive avec douleur aux mouvements et dyschromatopsie oriente vers le nerf.','L’examen neuro-ophtalmologique et l’imagerie orientée confrontent le diagnostic et ses alternatives.','Une inflammation du nerf altère la transmission du signal.','Organiser l’avis spécialisé, notamment si présentation atypique.','Un fond d’œil normal ne rassure pas.',(2,4)),
('Occlusion artérielle rétinienne','Une perte monoculaire soudaine et indolore est évocatrice.','Fond d’œil, imagerie rétinienne et bilan neurovasculaire urgent.','L’interruption artérielle menace la rétine et peut révéler une maladie embolique ou inflammatoire.','Activer les filières ophtalmologique et vasculaire.','🚩 E1.',(2,)),
('Artérite à cellules géantes avec atteinte visuelle','Perte transitoire ou permanente dans un contexte de signes crâniens ou systémiques compatibles.','Évaluation spécialisée avec imagerie ou biopsie, sans retarder le traitement.','La vascularite peut provoquer une ischémie du nerf ou de la rétine et menacer l’autre œil.','Débuter les glucocorticoïdes sans délai si la suspicion est forte.','🚩 E2.',(2,6))
]

sources=[
('HUG, Prats M, Malushaj L et al. L’œil rouge. Service de médecine de premier recours, 2025.','https://www.hug.ch/sites/interhug/files/2025-09/strategie_oeil_rouge_2025.pdf'),
('Collège des ophtalmologistes universitaires de France. Référentiel, 6e édition, 2025. Chapitre 8 : Altération aiguë de la vision.','http://couf.fr/wp-content/uploads/2025/10/CH8_Ophtalmologie_-Sous-legide-du-College-des-ophtalmologistes-universitaires-de-France-1.pdf'),
('COUF. Référentiel, 6e édition, 2025. Chapitre 7 : Altération chronique de la vision. Extraits ciblés consultés.','http://couf.fr/wp-content/uploads/2025/10/CH7_Ophtalmologie_-Sous-legide-du-College-des-ophtalmologistes-universitaires-de-France-1.pdf'),
('COUF. Référentiel, 6e édition, 2025. Chapitre 1 : Sémiologie oculaire. Extraits ciblés consultés.','https://couf.fr/xhtml/Ch001_3-45_B9782294786624500101.xhtml'),
('Höglinger D, Jäggi J, Guggisberg J. Déficiences auditives et visuelles en Suisse. Obsan Bulletin 03/2022, version corrigée de juillet 2022 ; ESS 2012/2017.','https://www.obsan.admin.ch/sites/default/files/2022-04/Obsan_BULLETIN_2022_03_f.pdf'),
('Mukhtyar CB et al. 2025 EULAR recommendations for the management of polymyalgia rheumatica and primary large vessel vasculitis. Ann Rheum Dis, publication 2026. DOI 10.1016/j.ard.2026.06.009. Extraits éditeur et complément local consultés.','https://ard.eular.org/article/S0003-4967(26)00357-2/fulltext'),
('AIPS suisse. Diamox®, information professionnelle, mise à jour juillet 2026. Comprimés 21191 ; injectable/perfusion 22002. Texte local français, édition du 08.10.2026 ; formes contrôlées dans la liste Swissmedic du 30.09.2026.','https://www.swissmedicinfo.ch/'),
('AIPS suisse. Solu-MEDROL®, information professionnelle, mise à jour août 2025. Poudre et solvant 500 mg et 1 g : 35112. Texte local français, édition du 08.10.2026 ; formes contrôlées dans la liste Swissmedic du 30.09.2026.','https://www.swissmedicinfo.ch/')
]

css=(R/'harnais/modele_lecon/style_lecon.css').read_text()
font_css=[]
for weight in (400,700):
    data=base64.b64encode((R/f'codex-LOTS-html/outils/polices/atkinson-hyperlegible-latin-{weight}-normal.woff2').read_bytes()).decode()
    data='\\\n'.join(data[i:i+160] for i in range(0,len(data),160))
    font_css.append('@font-face{font-family:"Atkinson Hyperlegible";font-style:normal;font-weight:'+str(weight)+';font-display:swap;src:url("data:font/woff2;base64,'+data+'") format("woff2")}')
css='\n'.join(font_css)+'\n'+css
# Le style source reste intact ; limiter le décalage aux écrans étroits.
# Vérification statique seulement : le navigateur local interdit file://.
css+='\n@media (max-width:480px){.fenetre.sousf{translate:0 .6rem}.som{columns:1}}'
parts=['<!doctype html>','<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">',
 '<title>Perte de vision aiguë ou progressive — S1.2</title>',
 '<style>'+css.replace('}', '}\n')+'</style></head><body><main>',
 '<h1>Perte de vision aiguë ou progressive</h1>',
 '<p class="sous">Rapide, lente, temporaire ou partielle · Situation S1.2 · Sources consultées le 30 octobre 2026.</p>',
 '<p class="taille" id="taille">Mesure de la fiche et de ses fenêtres en cours.</p>',
 '<section class="ilot c essentiel"><h2>L’essentiel</h2>'+p('Une perte visuelle soudaine ou transitoire exige une évaluation urgente. Chercher d’abord l’ischémie, l’artérite à cellules géantes, la fermeture d’angle, le décollement et l’infection ou le traumatisme. Mesurer chaque œil séparément et examiner le champ : une acuité centrale conservée ne protège pas contre toutes ces urgences.'+ref(1,2,6))+'</section>',
 '<nav class="ilot v" aria-label="Sommaire"><h2>Sommaire</h2><ol class="som">'+''.join(f'<li><a href="#a-p{i}">{title}</a></li>' for i,(title,_) in enumerate(sections,1))+'</ol></nav>']
for i,(title,body) in enumerate(sections,1):
 parts.append(f'<section class="ilot {"c" if i%2 else "v"}"><h2 id="a-p{i}">{i}. {title}</h2>'+body+'</section>')
parts += ['<section class="ilot c"><h2>Diagnostics différentiels : dix causes à comparer</h2>',
 p('Les numéros servent au repérage des dix monographies envisagées. L’ordre est provisoire : les sources consultées ne démontrent pas un classement décroissant unique de prévalence dans la population suisse correspondant à toutes les formes de ce symptôme. La fréquence n’est pas quantifiée ici ; les urgences restent visibles et prioritaires dans l’arbre de décision.'),
 p('Cette sélection ne remplace pas le tri des causes supplémentaires : fermeture aiguë de l’angle, kératite, uvéite, infection postopératoire, traumatisme et accident vasculaire cérébral doivent également être recherchés selon le tableau clinique.'+ref(1,2)),
 table(['Diagnostic','Signe clé','Examen qui tranche ou oriente','Mécanisme','Conduite','Exclusion prioritaire'],[[f'DX.{i} — {row[0]}',row[1],row[2],row[3],row[4],row[5]+ref(*row[6])] for i,row in enumerate(dx,1)]),'</section>',
 *windows.values(),
 '<section class="ilot v sources" id="sources"><h2>Sources</h2><ol>'+''.join(f'<li id="s{i}">{escape(title)} <a href="{escape(url,quote=True)}">Document ou portail officiel</a>. Consulté le 30.10.2026.</li>' for i,(title,url) in enumerate(sources,1))+'</ol></section>',
 '<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>',
 '</main></body></html>', '<!-- FIN_FICHIER LOT_018_Phase_A -->']
out='\n'.join(parts).replace('\u00a0',' ').replace('\u202f',' ')
abbr={'COUF':'Collège des ophtalmologistes universitaires de France','HUG':'Hôpitaux universitaires de Genève','OCT':'tomographie en cohérence optique','ACG':'artérite à cellules géantes','AIPS':'plateforme suisse de publication des informations sur les médicaments','EULAR':'Alliance européenne des associations de rhumatologie','ESS':'Enquête suisse sur la santé','CYP3A4':'isoenzyme 3A4 du cytochrome P450','DD':'diagnostic différentiel','p.ex.':'par exemple','i. v.':'intraveineuse','i. m.':'intramusculaire'}
pattern=re.compile(r'(?<!\w)('+ '|'.join(re.escape(a) for a in abbr) +r')(?!\w)')
chunks=[]
in_body=False
for part in re.split(r'(<[^>]+>)',out):
    if part.startswith('<body'):
        in_body=True
    if part.startswith('<') or not in_body:
        chunks.append(part)
    else:
        chunks.append(pattern.sub(lambda m:f'<abbr title="{abbr[m[0]]}">{m[0]}</abbr>',part))
out=''.join(chunks)
out=out.replace('</li><li','</li>\n<li')
(D/'LOT_018_Phase_A_V0.html').write_text(out)
(D/'LISTE_DX_CANONIQUE_PROVISOIRE.md').write_text('# Liste provisoire — LOT_018, S1.2\n\nNon gelée : audit médical indépendant non effectué. Les numéros sont des repères et ne prouvent pas un rang de prévalence. Voir HELP H1.\n\n'+'\n'.join(f'DX.{i} — {row[0]}' for i,row in enumerate(dx,1))+'\n')
print(f'Phase A écrite : {len(out.encode())} octets ; {len(windows)} fenêtres ; 14 parties ; aucun audit ni score attribué.')
