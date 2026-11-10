"""Fragments originaux de Phase A, composés depuis le paquet lu pour LOT081."""
from pathlib import Path
import html,json
ROOT=Path(__file__).resolve().parent
PACKET=json.loads((ROOT/'paquet.json').read_text())
IDS={p['id'] for p in PACKET['passages']}
def cite(*ids):
    assert all(i in IDS for i in ids),ids
    return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)
def p(text,*ids):return '<div class="p">'+html.escape(text)+cite(*ids)+'</div>\n'
def h(text):return '<h4><em>'+html.escape(text)+'</em></h4>\n'
def table(head,rows):
    return '<div class="t" style="overflow-x:auto"><table><thead><tr>'+''.join('<th>'+html.escape(x)+'</th>' for x in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+x+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table></div>\n'
def cell(text,*ids):return html.escape(text)+cite(*ids)
def window(n,k,title,body):
    key=f'pa81-p{n}-f{k}'
    return '<button class="w" popovertarget="'+key+'">'+html.escape(title)+'</button><div id="'+key+'" popover class="fenetre">'+h(title)+body+'</div>\n'
def save(n,s):(ROOT/'fragments'/f'p{n:02}.html').write_text(s)

s=h('Définir la plainte avant de nommer une maladie')
s+=p('Les HUG définissent la lombalgie comme une douleur située entre la 12ème côte et le pli fessier.','hug22-definition')
s+=p('Cette douleur comporte généralement une raideur rachidienne et une limitation de mobilité ; ces manifestations décrivent une plainte, sans désigner seules sa cause.','hug22-definition','hug22-classification')
s+=p('La qualification « commune » intervient lorsque l’anamnèse et l’examen ont écarté les arguments orientant vers une origine spécifique.','hug22-diagnostic-imagerie')
s+=p('Une douleur dite non spécifique ne possède pas de corrélat patho-anatomique clairement établi ; ce terme ne signifie donc pas une douleur imaginaire.','l81-de-nonspecifique','hug22-non-medicamenteux')
s+=p('Les présentations spécifiques peuvent relever du rachis, des structures nerveuses ou d’une origine extra-rachidienne ; cette séparation commande des explorations différentes.','hug22-classification','hug22-anamnese')
s+=p('La lombalgie ne résume pas toutes les douleurs du dos : les consultations urgentes peuvent également révéler une affection non spinale.','l81-uk-population','l81-uk-extrarachidien')
s+=p('Ainsi, une douleur du flanc associée à des symptômes urinaires demande une démarche différente d’une limitation lombaire isolée.','hug22-anamnese','l81-nice-pyelo-clinique')
s+=p('De même, une douleur abdominale irradiant vers le dos peut traduire un anévrisme aortique symptomatique, même si le patient désigne principalement son dos.','l81-esvs-aaa-clinique')
s+=h('Préciser la durée sans confondre durée et gravité')
s+=table(['Terme retenu par HUG2022','Définition temporelle','Conséquence de lecture'],[
 [cell('Une lombalgie est dite aiguë lorsque son évolution reste inférieure à 4 semaines.','hug22-classification'),cell('Certaines définitions emploient cependant une limite de 4 à 6 semaines.','hug22-classification'),cell('La durée est précisée avec le référentiel utilisé.','hug22-classification')],
 [cell('Le terme subaigu correspond à une période intermédiaire.','hug22-classification'),cell('HUG situe cette évolution entre 4 et 12 semaines.','hug22-classification'),cell('La persistance conduit à réexaminer les obstacles à la récupération.','hug22-evolution-suivi-retour')],
 [cell('La lombalgie chronique désigne une persistance prolongée.','hug22-classification'),cell('HUG emploie une durée au-delà de 3 mois.','hug22-classification'),cell('Le parcours prend en compte les facteurs de chronicisation.','hug22-risque-chronicite')]
])
s+=p('Les épisodes sont souvent récurrents, avec des symptômes variables entre les crises ; une histoire ancienne ne dispense pas d’examiner une manifestation nouvelle.','hug22-classification','nice26-1-1-1')
s+=p('Le calendrier ne remplace pas le triage : un signal neurologique d’alarme entraîne une imagerie et un avis spécialisés sans attendre.','l81-hug-urgent-neuro')
s+=window(1,1,'Sciatalgie, sciatique et cruralgie : distinguer les mots',
 p('La lombo-sciatalgie décrit une irradiation dans un ou plusieurs membres inférieurs au-delà du pli fessier, associée à une lombalgie.','hug22-classification')+
 p('Le terme lombo-sciatique est utilisé lorsque des signes concordants évoquent une atteinte radiculaire L5 ou S1.','hug22-classification')+
 p('La localisation dermatomale, les signes irritatifs et un éventuel déficit sensitif ou moteur renforcent alors la caractérisation radiculaire.','hug22-classification')+
 p('La lombo-cruralgie correspond à une irradiation vers la face antérieure de la cuisse ; le terme ne prouve pas à lui seul une radiculopathie.','hug22-classification')+
 p('Une atteinte L2, L3 ou L4 peut accompagner cette présentation et se recherche par un examen neurologique approprié.','hug22-classification','hug22-neurologie'))
s+=window(1,2,'Claudication neurogène et simple image de sténose',
 p('La claudication neurogène apparaît progressivement à la marche et s’améliore en position assise ou lorsque la lordose lombaire diminue.','l81-hug-stenose')+
 p('Une sténose anatomique visible en imagerie ne suffit pas : les manifestations cliniques doivent être concordantes avant de lui attribuer le handicap.','l81-de2016-stenose-clinique')+
 p('Une atteinte vasculaire périphérique ou une polyneuropathie peut entrer dans cette discussion diagnostique, au lieu d’attribuer automatiquement les symptômes au canal.','l81-de2016-stenose-clinique'))
s+=window(1,3,'La douleur mécanique ne constitue pas un diagnostic étiologique',
 p('Une douleur mécanique augmente habituellement en charge ou à l’effort et diminue avec son interruption ; son caractère peut aussi dépendre de la posture.','hug22-anamnese')+
 p('À l’inverse, une douleur inflammatoire peut réveiller en seconde partie de nuit et rester insuffisamment calmée par le repos.','hug22-anamnese')+
 p('L’amélioration sous anti-inflammatoire ne distingue pas à elle seule ces profils, car les douleurs mécaniques peuvent également être soulagées.','hug22-anamnese')+
 p('Ces caractéristiques orientent l’interrogatoire ; l’identification d’une maladie inflammatoire repose sur un ensemble clinique et des investigations ciblées.','l81-hug-axspa','hug22-diagnostic-imagerie'))
save(1,s)

s=h('Lire les fréquences avec leur population')
s+=p('La stratégie HUG2022 rapporte une prévalence annuelle suisse de 30%-40% dans la population générale ; cette mesure ne décrit pas une cause particulière.','hug22-epidemiologie')
s+=p('Elle indique que plus de 80% des personnes connaîtront au moins un épisode au cours de leur vie.','hug22-epidemiologie')
s+=p('L’enquête suisse de 2020 citée par cette stratégie rapporte 88% de répondants ayant déjà ressenti une douleur lombaire.','hug22-epidemiologie')
s+=p('Cette enquête comporte 1041 personnes et une inclusion à partir de 16 ans ; son résultat reste attaché à ce cadre.','hug22-epidemiologie')
s+=p('En consultation de médecine générale, HUG qualifie de non spécifique la majorité des lombalgies, avec une estimation d’environ 90%.','l81-hug-commune')
s+=p('Le protocole du SMPR décrit séparément un groupe neurogène à 5-10% ; ce regroupement ne constitue pas une prévalence universelle de hernie discale.','l81-hug-categories')
s+=table(['Mesure','Population et date','Interprétation fidèle'],[
 [cell('La prévalence annuelle atteint 30%-40%.','hug22-epidemiologie'),cell('La stratégie HUG2022 cite la population générale suisse.','hug22-epidemiologie'),cell('Cette mesure décrit la survenue de lombalgie, sans répartir ses causes.','hug22-epidemiologie')],
 [cell('L’enquête rapporte 88% de douleurs lombaires au cours de la vie.','hug22-epidemiologie'),cell('Les 1041 personnes interrogées en Suisse en 2020 avaient au moins 16 ans.','hug22-epidemiologie'),cell('Une enquête de population ne fournit pas la distribution des diagnostics aux urgences.','hug22-epidemiologie','l81-uk-population')],
 [cell('La cause commune représente environ 90%.','l81-hug-commune'),cell('L’estimation concerne la consultation de médecine générale décrite par HUG.','l81-hug-commune'),cell('Cette majorité justifie sa place initiale après exclusion des situations graves.','l81-hug-commune','hug22-diagnostic-imagerie')]
])
s+=h('Comprendre les changements de contexte')
s+=p('La série anglaise inclut 3872 passages pour plainte de dos ; elle comprend également des blessures et quelques douleurs cervicales.','l81-uk-population')
s+=p('Parmi ces passages, 834 étaient classés comme pathologies non spinales, soit 21.5% ; ce groupe recouvrait des affections très différentes.','l81-uk-extrarachidien')
s+=p('Dans cette même série, 1390 passages n’avaient aucun diagnostic enregistré ; cette limite empêche de transformer le relevé en classement exhaustif.','l81-uk-extrarachidien')
s+=p('La proportion de causes communes en premier recours ne doit donc pas servir de justification pour négliger les causes viscérales aux urgences.','l81-hug-commune','l81-uk-extrarachidien')
s+=p('Dans une présentation radiculaire, HUG rapporte une hernie dans 95% des syndromes étudiés ; le dénominateur est le syndrome radiculaire.','l81-hug-radiculaire')
s+=p('Chez un patient présentant une claudication, l’âge et la relation avec la marche rendent au contraire une sténose symptomatique plus pertinente.','l81-hug-stenose')
s+=p('Le terrain ostéoporotique, l’exposition aux stéroïdes et le traumatisme réorientent vers une fracture, indépendamment de l’ordre de présentation pédagogique.','l81-hug-fracture')
s+=h('Histoire naturelle et retentissement')
s+=p('Le pronostic de la lombalgie aiguë commune est généralement favorable dans les 6 semaines ; les récidives n’annulent pas ce pronostic initial.','hug22-evolution-suivi-retour','hug22-classification')
s+=p('HUG invite cependant à rechercher les facteurs de chronicisation dès la première consultation, car ils modifient l’organisation du suivi.','hug22-risque-chronicite')
s+=p('La peur du mouvement, le catastrophisme, l’anxiété et l’humeur dépressive sont des facteurs modifiables particulièrement importants dans cette évaluation.','hug22-risque-chronicite')
s+=p('Les contraintes du métier, le soutien au travail et les difficultés sociales participent également au risque de handicap durable.','hug22-risque-chronicite')
s+=p('La charge collective dépasse les investigations : elle comprend les répercussions fonctionnelles, professionnelles et les coûts indirects associés à la persistance.','hug22-epidemiologie','hug22-risque-chronicite')
s+=window(2,1,'Pourquoi les chiffres anciens ne sont pas additionnés',
 p('Les éditions et synthèses décrivent des populations et des catégories différentes ; une estimation du groupe tumoral ne devient pas celle des métastases seules.','l81-hug2010-frequences','l81-de2016-frequences')+
 p('De même, les estimations de toutes fractures ne mesurent pas uniquement les fractures ostéoporotiques symptomatiques retenues dans la liste.','l81-hug-fracture','l81-de2016-frequences')+
 p('La spondylarthrite ankylosante et l’ensemble des spondyloarthrites axiales ne possèdent pas automatiquement le même dénominateur épidémiologique.','l81-hug-axspa','l81-de2016-frequences')+
 p('Le contexte clinique est donc conservé pour chaque diagnostic ; les numéros ne représentent pas des écarts statistiques universels entre voisins.','l81-hug-categories','l81-hug-stenose','l81-hug-fracture','l81-uk-population'))
s+=window(2,2,'Travail, fonctionnement et rechute',
 p('Une interruption professionnelle se discute selon le handicap et les sollicitations réelles du poste, puis se réévalue plutôt que de devenir automatique.','hug22-evolution-suivi-retour')+
 p('Les adaptations ergonomiques du travail peuvent réduire la peur de se mobiliser et favoriser la reprise des activités.','hug22-evolution-suivi-retour')+
 p('Le suivi de la fonction et de la participation complète ainsi celui de la douleur, dont l’intensité reste une expérience subjective.','hug22-non-medicamenteux','hug22-evolution-suivi-retour'))
save(2,s)

s=h('Relier la plainte à plusieurs mécanismes possibles')
s+=p('La douleur lombaire commune n’identifie pas une lésion unique ; la relation entre anomalies radiologiques et symptômes peut être faible ou absente.','l81-de-nonspecifique','hug22-diagnostic-imagerie')
s+=p('Ainsi, une image dégénérative ne suffit pas à expliquer le tableau : sa pertinence dépend de la concordance clinique.','l81-de2016-stenose-clinique')
s+=p('Dans une présentation radiculaire, douleur dermatomale et déficit concordant orientent vers la racine concernée plutôt que vers une douleur lombaire diffuse.','hug22-classification','hug22-neurologie')
s+=p('La claudication neurogène met en relation une réduction canalaire et des symptômes provoqués par la marche, améliorés par la position assise.','l81-de2016-stenose-clinique','l81-hug-stenose')
s+=p('Une compression pluriradiculaire avec signes sacrés change la priorité, car elle relève de la recherche urgente d’un syndrome de la queue de cheval.','hug22-neurologie','l81-hug-urgent-neuro')
s+=p('Dans la colique néphrétique, un obstacle met en tension la voie excrétrice supérieure ; la douleur ressentie peut donc être lombo-abdominale.','audit81-hug23-colique-definition')
s+=p('Cet obstacle est fréquemment un calcul, mais un caillot ou une autre lésion obstructive peut produire un tableau voisin.','audit81-hug23-colique-definition')
s+=p('Lorsque infection et obstruction urinaire coexistent, le risque d’urosepsis impose de rechercher rapidement un drainage, en plus du traitement anti-infectieux.','l81-eau-pyelo-differentiel','l81-eau-decompression')
s+=p('Une atteinte aortique peut provoquer une irradiation dorsale ; la rupture s’accompagne parfois d’un effondrement hémodynamique et de pâleur.','l81-esvs-aaa-clinique')
s+=p('La douleur ne localise donc pas toujours sa source anatomique ; les signes associés orientent l’exploration vers le rachis ou un organe distant.','hug22-anamnese','l81-esvs-aaa-clinique')
s+=table(['Perturbation ou cadre','Exploration qui la rend pertinente','Traitement ou conduite liée'],[
 [cell('Une atteinte radiculaire entraîne des signes dans un territoire concordant.','hug22-neurologie'),cell('La force, les réflexes et la sensibilité précisent ce territoire.','hug22-neurologie'),cell('Une progression neurologique déclenche la voie d’imagerie et d’avis urgents.','l81-hug-urgent-neuro')],
 [cell('Une sténose devient cliniquement pertinente devant une claudication concordante.','l81-de2016-stenose-clinique'),cell('L’examen recherche le lien avec la marche et la position assise.','l81-hug-stenose'),cell('Les traitements sont choisis selon le retentissement clinique, plutôt que sur l’image isolée.','l81-de2016-stenose-clinique')],
 [cell('Un obstacle urétéral met en tension les voies urinaires supérieures.','audit81-hug23-colique-definition'),cell('L’imagerie recherche le calcul et une dilatation des cavités.','l81-eau-calcul-clinique','l81-eau-calcul-image'),cell('Une obstruction infectée nécessite une décompression et des antibiotiques immédiats.','l81-eau-decompression')],
 [cell('Une infection spinale peut atteindre les structures vertébrales ou épidurales.','l81-hug-infection'),cell('L’IRM urgente explore cette hypothèse lorsque le contexte la fait suspecter.','l81-hug-urgent-infection'),cell('Une atteinte neurologique nouvelle impose une discussion chirurgicale spécialisée.','l81-eans-infection-neuro')],
 [cell('Une cause tumorale peut s’accompagner d’une compression neurologique.','l81-nice-metastase-urgences'),cell('L’IRM recherche la compression selon un calendrier urgent.','l81-nice-mscc-irm'),cell('Les signes de compression chez un patient cancéreux déclenchent immédiatement la filière spécialisée.','l81-nice-metastase-urgences')],
 [cell('La peur du mouvement peut accompagner une évolution persistante.','hug22-risque-chronicite'),cell('L’interrogatoire explore les croyances, l’anxiété et le retentissement fonctionnel.','hug22-risque-chronicite'),cell('L’information et la progression adaptée des activités visent une participation active.','hug22-non-medicamenteux')]
])
s+=h('Persistance : intégrer le fonctionnement et le contexte')
s+=p('La kinésiophobie désigne la peur du mouvement ; elle influence la progressivité d’un programme d’activité et doit être reconnue explicitement.','hug22-risque-chronicite','hug22-non-medicamenteux')
s+=p('Le catastrophisme et les croyances défavorables peuvent accompagner une récupération plus lente ; les explorer ne revient pas à contester la douleur.','hug22-risque-chronicite','hug22-non-medicamenteux')
s+=p('Une stratégie exclusivement passive réduit la place du patient dans sa récupération, alors que HUG privilégie son engagement dans les exercices.','hug22-risque-chronicite','hug22-non-medicamenteux')
s+=p('Le repos au lit n’est pas thérapeutique dans la lombalgie commune ; la reprise adaptée des activités contribue au parcours de récupération.','hug22-non-medicamenteux')
s+=p('Des investigations systématiques peuvent aussi produire un effet nocebo, en renforçant l’interprétation pathologique d’images peu corrélées aux symptômes.','hug22-diagnostic-imagerie')
s+=window(3,1,'Raisonnement devant une image dégénérative',
 p('Les modifications dégénératives sont fréquentes avec l’âge ; leur présence doit être confrontée au syndrome clinique effectivement observé.','l81-de2016-stenose-clinique')+
 p('Une anomalie d’imagerie ne dispense ni de rechercher un diagnostic concurrent ni d’examiner les fonctions neurologiques.','l81-de2016-stenose-clinique','hug22-neurologie')+
 p('Cette concordance évite de traiter une image lorsque la plainte relève d’un autre mécanisme ou d’une cause extra-rachidienne.','l81-de2016-stenose-clinique','hug22-anamnese'))
s+=window(3,2,'Composantes psychologiques et sécurité diagnostique',
 p('Les drapeaux jaunes concernent le risque de chronicisation ; ils ne remplacent pas la recherche préalable des drapeaux rouges.','hug22-risque-chronicite','hug22-anamnese')+
 p('Une anxiété ou une humeur dépressive associée peut justifier une prise en charge spécifique, tout en maintenant l’évaluation clinique de la douleur.','hug22-risque-chronicite','hug22-non-medicamenteux')+
 p('Une manifestation nouvelle, notamment fébrile ou neurologique, conduit à réévaluer le diagnostic même dans un contexte de douleurs anciennes.','hug22-evolution-suivi-retour'))
save(3,s)

s=h('🚩 Exclure les situations graves avant de retenir une cause commune')
s+=p('La première décision porte sur les urgences : une douleur du dos peut révéler une atteinte vasculaire, neurologique, infectieuse ou fracturaire.','l81-esvs-aaa-clinique','l81-hug-urgent-neuro','l81-hug-urgent-infection','l81-hug-fracture-ct')
s+=p('Le rang E exprime cette priorité d’exclusion ; il ne représente pas la fréquence du diagnostic dans toutes les consultations.','l81-hug-commune','l81-nice-aaa-urgence','l81-hug-urgent-neuro')
s+=table(['Priorité conditionnelle','Constat qui la déclenche','Action diagnostique immédiate'],[
 [cell('E1 : la branche vasculaire devient prioritaire si un anévrisme symptomatique ou rompu est suspecté.','l81-esvs-aaa-clinique'),cell('Une douleur abdominale ou dorsale avec collapsus ou pâleur fait rechercher la rupture.','l81-esvs-aaa-clinique'),cell('NICE recommande une échographie aortique immédiate et un échange immédiat avec le service vasculaire si la suspicion persiste.','l81-nice-aaa-urgence')],
 [cell('E2 : une compression neurologique nécessite une évaluation sans attendre.','l81-hug-urgent-neuro'),cell('Une anomalie sacrée ou un déficit moteur peut traduire une atteinte grave.','hug22-neurologie','l81-hug-urgent-neuro'),cell('Une IRM si possible, au minimum un CT, est assortie d’un avis neurochirurgical selon HUG.','l81-hug-urgent-neuro')],
 [cell('E3 : un contexte infectieux impose de rechercher la localisation et un obstacle éventuel.','l81-hug-infection','l81-eau-pyelo-differentiel'),cell('Fièvre, frissons, gestes invasifs ou obstruction urinaire orientent vers une infection potentiellement compliquée.','l81-hug-infection','l81-eau-obstr-sepsis'),cell('La suspicion spinale conduit à l’IRM urgente ; le sepsis sur calcul obstructif impose décompression et antibiotiques immédiats.','l81-hug-urgent-infection','l81-eau-decompression')],
 [cell('E4 : une fracture suspectée se hiérarchise selon le terrain et les critères de sévérité.','l81-hug-fracture-ct'),cell('La douleur focale, la fragilité et l’impossibilité de mobilisation renforcent la nécessité d’une exploration urgente.','l81-hug-fracture-ct'),cell('Le CT est discuté en urgence selon les critères HUG ; un déficit associé rejoint la branche neurologique.','l81-hug-fracture-ct','l81-hug-urgent-neuro')]
])
s+=h('Dix diagnostics canoniques : tableau comparatif')
rows=[
 ['Lombalgie commune non spécifique','La douleur lombaire reste sans argument pour une cause spécifique après l’anamnèse et l’examen.','Le diagnostic est clinique et ne réclame pas d’imagerie systématique dans ce cadre.','Aucun corrélat patho-anatomique unique n’est clairement établi.','La réassurance et une mobilité adaptée accompagnent l’information, après triage.','Aucun rang d’exclusion ne s’applique après un triage négatif ; un changement clinique le réouvre.',['l81-hug-commune-diagnostic','l81-de-nonspecifique','l81-hug-commune-mobilite','hug22-evolution-suivi-retour']],
 ['Hernie discale lombaire avec radiculopathie','L’irradiation suit un territoire radiculaire avec signes sensitifs, moteurs ou réflexes concordants.','L’examen neurologique guide l’indication d’IRM selon l’évolution.','La présentation correspond à une atteinte de racine associée à une hernie concordante.','La recherche de déficit progressif ou de signes sacrés précède le parcours conservateur.','E2 s’applique si une compression grave est suspectée, sans qualifier toute radiculopathie d’urgence chirurgicale.',['l81-hug-radiculaire','hug22-neurologie','l81-hug-urgent-neuro','hug22-diagnostic-imagerie']],
 ['Sténose lombaire dégénérative avec claudication neurogène','Les symptômes apparaissent à la marche et diminuent en position assise ou en flexion.','L’IRM est interprétée avec la claudication et les diagnostics vasculaires ou neuropathiques concurrents.','La réduction anatomique du canal devient pertinente lorsqu’elle correspond au tableau clinique.','L’examen neurologique et vasculaire précède une stratégie adaptée au handicap.','E2 redevient prioritaire en présence de signes neurologiques aigus graves.',['l81-hug-stenose','l81-de2016-stenose-clinique','l81-hug-urgent-neuro']],
 ['Fracture vertébrale ostéoporotique symptomatique','Une douleur rachidienne nouvelle apparaît sur un terrain de fragilité, parfois après un traumatisme limité.','L’imagerie vertébrale est choisie selon les facteurs de risque et la gravité.','La fragilité osseuse expose à une fracture qui peut expliquer la douleur focale.','Le déficit, la sévérité de la douleur et la possibilité de mobilisation sont évalués.','E4 concerne la suspicion fracturaire sévère ; E2 prime si un déficit est associé.',['l81-hug-fracture','l81-hug-fracture-ct','l81-hug-urgent-neuro']],
 ['Calcul urétéral symptomatique','La douleur du flanc peut s’accompagner de vomissements ou de signes urinaires.','L’échographie puis le CT sans contraste confirment la recherche lithiasique selon EAU.','L’obstacle met en tension la voie excrétrice du haut appareil urinaire.','Le rein unique, la fièvre et le doute diagnostique imposent une évaluation immédiate.','E3 s’applique à l’obstruction infectée ou au sepsis ; l’anurie relève également de l’urgence urologique.',['l81-eau-calcul-clinique','l81-eau-calcul-image','audit81-hug23-colique-definition','l81-eau-obstr-sepsis']],
 ['Pyélonéphrite aiguë','La douleur du flanc s’associe à un tableau infectieux, parfois sans symptômes urinaires bas préalables.','La culture d’urines avec antibiogramme est indiquée et l’imagerie recherche les complications selon le contexte.','L’atteinte infectieuse du haut appareil se distingue d’une cystite isolée.','Le bilan recherche rapidement une obstruction susceptible de favoriser un urosepsis.','E3 devient prioritaire en cas de sepsis, d’obstacle ou d’aggravation clinique.',['audit81-hug21-pyelo-cadre','l81-eau-pyelo-culture','l81-eau-pyelo-differentiel','l81-eau-pyelo-imagerie']],
 ['Métastase vertébrale symptomatique','Une douleur nouvelle ou persistante est particulièrement suspecte dans un contexte oncologique.','L’IRM explore la suspicion, selon un calendrier différent avec ou sans compression.','La localisation tumorale peut s’accompagner de signes de compression neurologique.','Des signes de compression chez une personne atteinte de cancer déclenchent immédiatement la filière spécialisée.','E2 s’applique si une compression est suspectée ; une suspicion sans compression garde un bilan rapide.',['l81-hug-neoplasie','l81-nice-mscc-irm','l81-nice-metastase-sans-mscc','l81-nice-metastase-urgences']],
 ['Spondyloarthrite axiale','Le début jeune, la persistance et les manifestations inflammatoires associées orientent cette hypothèse.','Le bilan ciblé et l’imagerie sacro-iliaque accompagnent l’évaluation rhumatologique.','Le tableau s’inscrit dans une atteinte inflammatoire axiale.','Les manifestations articulaires, cutanées, oculaires et digestives sont recherchées.','Une nouvelle alarme impose de rechercher aussi une autre cause avant d’attribuer les symptômes à l’inflammation.',['l81-hug-axspa','hug22-diagnostic-imagerie','nice26-1-1-1']],
 ['Spondylodiscite pyogène de novo','Une douleur focale avec facteurs infectieux, fièvre ou frissons fait rechercher une infection spinale.','L’IRM urgente est privilégiée ; le CT alternatif est moins sensible précocement.','Une atteinte vertébrale ou épidurale peut menacer les fonctions neurologiques.','Les prélèvements ciblés et l’évaluation spécialisée accompagnent l’exploration urgente.','E3 traduit le risque infectieux ; E2 s’ajoute devant un déficit ou des troubles sphinctériens.',['l81-hug-infection','l81-hug-urgent-infection','l81-eans-infection-neuro']],
 ['Anévrisme de l’aorte abdominale symptomatique','La douleur abdominale peut irradier vers le dos ; un collapsus ou une pâleur font craindre une rupture.','L’échographie identifie l’anévrisme mais ne permet pas d’exclure une fuite rétropéritonéale.','La douleur peut résulter de l’atteinte aortique ou de ses complications locales.','L’avis vasculaire est immédiat si la suspicion persiste, même lorsque l’échographie est non concluante.','E1 prime dès la suspicion vasculaire symptomatique ou rompue.',['l81-esvs-aaa-clinique','l81-esvs-aaa-us','l81-nice-aaa-urgence']]
]
out=[]
for i,row in enumerate(rows,1):
    name,sign,exam,mech,conduct,urg,refs=row
    out.append([cell(f'DX.{i} — {name}. '+sign,*refs),cell(exam,*refs),cell(mech,*refs),cell(conduct,*refs),cell(urg,*refs)])
s+=table(['Diagnostic et signe clé','Examen discriminant','Mécanisme ou cadre','Conduite immédiate','Rang d’exclusion conditionnel'],out)
s+=h('Garder visibles les cadres de fréquence')
s+=p('La liste commence par la cause majoritaire de premier recours, puis distingue les présentations neurogènes, la fragilité et les douleurs du flanc.','l81-hug-commune','l81-hug-radiculaire','l81-hug-stenose','l81-hug-fracture','l81-eau-calcul-clinique')
s+=p('Les branches oncologique, inflammatoire, infectieuse et vasculaire sont ensuite explicitées selon leurs indices propres ; leur numéro ne détermine jamais le délai d’action.','l81-hug-neoplasie','l81-hug-axspa','l81-hug-infection','l81-nice-aaa-urgence')
s+=p('Cette synthèse qualitative contextualisée ne transforme pas deux numéros voisins en différence statistique démontrée pour tous les âges et tous les lieux de soins.','l81-hug-categories','l81-de2016-frequences','l81-uk-population')
s+=window(4,1,'Cancer : séparer suspicion de métastase et compression',
 p('Chez une personne ayant un cancer ancien ou actuel, des signes de compression imposent un contact immédiat avec la filière oncologique spécialisée.','l81-nice-metastase-urgences')+
 p('NICE demande alors une IRM dès que possible, toujours dans les 24 heures, avec accès local lorsque celui-ci est disponible.','l81-nice-mscc-irm')+
 p('Sans suspicion de compression, une suspicion clinique de métastase vertébrale relève d’une IRM dans la semaine selon NICE2023.','l81-nice-metastase-sans-mscc')+
 p('Ces calendriers concernent des situations différentes ; le délai ambulatoire ne doit pas être appliqué à une compression suspectée.','l81-nice-mscc-irm','l81-nice-metastase-sans-mscc'))
s+=window(4,2,'Une échographie non concluante ne ferme pas la branche vasculaire',
 p('L’échographie urgente peut montrer un anévrisme, mais sa sensibilité pour une hémorragie rétropéritonéale reste limitée.','l81-esvs-aaa-us')+
 p('NICE demande un échange immédiat avec le service vasculaire lorsque l’examen est indisponible ou non diagnostique et que la suspicion demeure.','l81-nice-aaa-urgence')+
 p('L’angioscanner fournit les informations anatomiques nécessaires à la prise en charge endovasculaire dans le parcours de rupture suspectée décrit par ESVS.','l81-esvs-aaa-us'))
save(4,s)

s=h('Interroger pour décider de la prochaine action')
s+=p('L’entretien précise la localisation, les irradiations, l’intensité, la durée et l’évolution, puis relie ces éléments aux circonstances aggravantes ou soulageantes.','hug22-anamnese')
s+=p('La comparaison avec les épisodes précédents recherche surtout ce qui a changé, car une manifestation différente peut modifier la démarche diagnostique.','hug22-anamnese','nice26-1-1-1')
s+=p('Un effort inhabituel est recherché sans devenir une explication obligatoire : beaucoup d’épisodes communs surviennent sans déclencheur particulier.','hug22-anamnese')
s+=p('L’effet de la charge et du repos aide à caractériser la douleur, tandis que le réveil nocturne et la raideur prolongée orientent vers l’inflammation.','hug22-anamnese')
s+=p('L’interrogatoire recherche le cancer, l’ostéoporose, les traitements stéroïdes, l’immunosuppression et les gestes invasifs récents, car ces contextes modifient les hypothèses.','l81-hug-neoplasie','l81-hug-fracture','l81-hug-infection')
s+=table(['Question ou signe d’alarme','Raison clinique','Action imposée si suspicion'],[
 [cell('Une anomalie périnéale ou sphinctérienne accompagne-t-elle la douleur ?','hug22-neurologie'),cell('L’atteinte des racines sacrées fait rechercher une queue de cheval.','hug22-neurologie'),cell('L’imagerie est réalisée sans attendre et un avis neurochirurgical est demandé.','l81-hug-urgent-neuro')],
 [cell('Une faiblesse motrice apparaît-elle ou progresse-t-elle ?','hug22-diagnostic-imagerie'),cell('La progression différencie cette présentation d’un déficit discret stable.','hug22-diagnostic-imagerie'),cell('La branche neurologique urgente est activée devant un signal d’alarme.','l81-hug-urgent-neuro')],
 [cell('Une fièvre nouvelle, des frissons ou une infection concomitante sont-ils présents ?','l81-hug-infection'),cell('Le contexte peut évoquer une infection vertébrale ou épidurale.','l81-hug-infection'),cell('Une suspicion de spondylodiscite ou d’abcès épidural conduit à l’IRM urgente.','l81-hug-urgent-infection')],
 [cell('Une douleur du flanc s’accompagne-t-elle de fièvre, d’anurie ou d’un rein unique ?','l81-eau-calcul-clinique','l81-eau-obstr-sepsis'),cell('Un obstacle infecté ou une anurie peuvent constituer une urgence urologique.','l81-eau-obstr-sepsis'),cell('L’évaluation est immédiate ; le sepsis sur obstacle réclame drainage et antibiotiques sans délai.','l81-eau-calcul-clinique','l81-eau-decompression')],
 [cell('Un cancer est-il connu et de nouveaux signes neurologiques sont-ils apparus ?','l81-hug-neoplasie','l81-nice-metastase-urgences'),cell('Une compression tumorale doit être considérée comme une urgence oncologique.','l81-nice-metastase-urgences'),cell('La filière spécialisée est contactée immédiatement et l’IRM est organisée rapidement.','l81-nice-metastase-urgences','l81-nice-mscc-irm')],
 [cell('Une chute ou un traumatisme même limité est-il survenu sur un terrain fragile ?','l81-hug-fracture'),cell('L’ostéoporose et les stéroïdes renforcent l’hypothèse fracturaire.','l81-hug-fracture'),cell('L’imagerie est orientée vers la fracture, avec urgence selon les critères de sévérité.','l81-hug-fracture-ct')],
 [cell('Une douleur abdominale ou dorsale s’accompagne-t-elle d’un collapsus ou d’une pâleur ?','l81-esvs-aaa-clinique'),cell('Ces manifestations font craindre une rupture aortique.','l81-esvs-aaa-clinique'),cell('La suspicion justifie un contact vasculaire immédiat et une exploration adaptée.','l81-nice-aaa-urgence','l81-esvs-aaa-us')]
])
s+=h('Interroger le fonctionnement et les obstacles à la récupération')
s+=p('Le retentissement se mesure dans les activités quotidiennes, la marche et les tâches professionnelles, plutôt que par l’intensité douloureuse seule.','hug22-non-medicamenteux','hug22-evolution-suivi-retour')
s+=p('Les craintes liées au mouvement sont recherchées explicitement, car elles influencent la progressivité d’une reprise d’activité.','hug22-risque-chronicite','hug22-non-medicamenteux')
s+=p('Les attentes envers les traitements et les expériences antérieures renseignent les croyances susceptibles de maintenir une attitude passive.','hug22-risque-chronicite')
s+=p('La communication au travail et les possibilités d’adaptation du poste sont explorées lorsque la douleur entrave l’activité professionnelle.','hug22-risque-chronicite','hug22-evolution-suivi-retour')
s+=window(5,1,'Drapeaux jaunes, bleus et noirs : des fonctions différentes',
 p('Les drapeaux jaunes concernent notamment l’anxiété, la peur de bouger, les croyances défavorables et l’importance du retentissement individuel.','hug22-risque-chronicite')+
 p('Les drapeaux bleus décrivent des facteurs professionnels, tels que l’insatisfaction au travail, ses exigences physiques ou un faible soutien.','hug22-risque-chronicite')+
 p('Les drapeaux noirs portent sur l’environnement socio-économique, dont le chômage, les conflits d’indemnisation ou l’isolement social.','hug22-risque-chronicite')+
 p('Ces informations orientent le suivi et la coordination, mais ne dispensent jamais de rechercher les signes d’une affection spécifique.','hug22-risque-chronicite','hug22-anamnese'))
s+=window(5,2,'Chercher les indices d’une cause inflammatoire',
 p('Un début avant 45 ans, des symptômes persistants ou récidivants et une installation insidieuse appartiennent au cadre décrit par HUG.','l81-hug-axspa')+
 p('L’alternance des douleurs fessières et les antécédents d’arthrite, d’enthésite, de psoriasis, d’uvéite ou de maladie inflammatoire intestinale complètent l’interrogatoire.','l81-hug-axspa')+
 p('Les antécédents familiaux contribuent également à cette orientation ; le bilan est ensuite ciblé vers la question rhumatologique.','l81-hug-axspa','hug22-diagnostic-imagerie')+
 p('Une raideur matinale prolongée au-delà de 30 minutes soutient le profil inflammatoire décrit par HUG, sans constituer seule un diagnostic.','hug22-anamnese','l81-hug-axspa'))
save(5,s)

s=h('Commencer par les constantes et un repère de normalité')
s+=p('Les constantes, dont la température, font partie intégrante de l’examen initial ; elles ne sont pas remplacées par la seule palpation du rachis.','hug22-constantes')
s+=p('La force normale correspond au grade M5 dans l’échelle décrite par HUG ; ce repère précède l’identification des déficits.','hug22-neurologie')
s+=p('L’inspection debout examine les courbures habituelles et recherche un trouble statique majeur, notamment une scoliose ou un déséquilibre antérieur.','hug22-inspection')
s+=p('La mobilité est évaluée en flexion antéropostérieure et latérale, afin de documenter la limitation observée plutôt que de supposer son origine.','hug22-dynamique')
s+=h('Inspection, palpation et mouvement')
s+=p('Pour rechercher une insuffisance de maintien, HUG décrit une position droite avec les bras tendus horizontalement pendant 30 secondes.','hug22-inspection')
s+=p('La déviation du tronc ou l’impossibilité de maintenir cette position constituent l’anomalie recherchée par ce geste.','hug22-inspection')
s+=p('La recherche d’une contracture lombaire se réalise habituellement en décubitus ventral, plutôt qu’en position debout.','hug22-palpation')
s+=p('La palpation explore toutes les vertèbres et les espaces intervertébraux, notamment lorsque l’hypothèse est infectieuse ou inflammatoire.','hug22-palpation')
s+=p('Une douleur élective sur les apophyses épineuses ou les espaces interépineux contribue aux critères de sévérité devant une fracture suspectée.','l81-hug-fracture-ct')
s+=p('La mobilisation active permet de documenter un syndrome lombo-vertébral et de repérer une peur du mouvement pouvant limiter l’examen.','hug22-dynamique')
s+=p('L’indice de Schobert modifié et la distance doigt-sol reflètent des dimensions différentes de la mobilité ; ils sont particulièrement utiles au suivi.','hug22-dynamique')
s+=window(6,1,'Manœuvres de tension radiculaire : technique et piège',
 p('Devant une irradiation au-delà du pli fessier, le Lasègue direct ou croisé recherche une reproduction de la douleur radiculaire.','hug22-neurologie')+
 p('La positivité décrite par HUG survient entre 30° et 70° d’élévation de la jambe, dans le trajet radiculaire concerné.','hug22-neurologie')+
 p('Une douleur uniquement lombaire pendant la manœuvre ne correspond donc pas au critère de positivité radiculaire décrit.','hug22-neurologie')+
 p('Le Lasègue direct est plus sensible, tandis que le test croisé est plus spécifique selon la stratégie HUG.','hug22-neurologie')+
 p('Le rétro-Lasègue se pratique en décubitus ventral ou latéral et utilise l’extension passive de l’articulation coxo-fémorale.','hug22-neurologie')+
 p('Il cherche une douleur antérieure de cuisse, compatible avec une atteinte L2, L3 ou L4 dans le contexte clinique approprié.','hug22-neurologie'))
s+=h('Examen moteur puis réflexes et sensibilité')
s+=p('La marche sur les talons et sur la pointe des pieds dépiste rapidement une parésie sévère des releveurs ou fléchisseurs du pied.','hug22-neurologie')
s+=p('Cependant, une réalisation correcte ne suffit pas à exclure un déficit discret ni une atteinte isolée de l’extenseur de l’hallux.','hug22-neurologie')
s+=p('L’extension du premier orteil doit donc être examinée séparément, en complément de l’observation de la marche.','hug22-neurologie')
s+=p('Les réflexes rotuliens et achilléens complètent l’examen moteur ; la sensibilité est explorée sur les cuisses, les mollets et les pieds.','hug22-neurologie')
s+=table(['Territoire recherché','Geste ou fonction','Repère réflexe et lecture'],[
 [cell('Les racines L1-L2 participent à la flexion de hanche.','hug22-neurologie'),cell('La force de flexion est examinée dans l’évaluation motrice.','hug22-neurologie'),cell('Le résultat s’interprète avec les autres composantes neurologiques.','hug22-neurologie')],
 [cell('Le territoire L3-L4 est évalué par l’extension du genou.','hug22-neurologie'),cell('Le geste recherche une faiblesse concordante dans cette fonction.','hug22-neurologie'),cell('Le réflexe rotulien complète l’examen de ce territoire.','hug22-neurologie')],
 [cell('Le territoire L5 comporte l’extension de l’hallux et la flexion dorsale de cheville.','hug22-neurologie'),cell('L’hallux est testé séparément même si la marche sur les talons reste possible.','hug22-neurologie'),cell('L’examen sensitif aide à apprécier la concordance territoriale.','hug22-neurologie')],
 [cell('La flexion plantaire de cheville participe à l’examen S1.','hug22-neurologie'),cell('La marche sur les pointes renseigne le dépistage d’une faiblesse importante.','hug22-neurologie'),cell('Le réflexe achilléen apporte un élément complémentaire.','hug22-neurologie')]
])
s+=window(6,2,'Coter la force sans confondre les niveaux',
 p('M5 indique une force normale, alors que M4 correspond à un mouvement possible contre une résistance modérée.','hug22-neurologie')+
 p('M3 désigne un mouvement contre la gravité ; M2 décrit un mouvement réalisable seulement dans le plan du lit.','hug22-neurologie')+
 p('M1 signifie une contraction visible sans mouvement, tandis que M0 correspond à l’absence de contraction visible.','hug22-neurologie')+
 p('Cette cotation permet de documenter l’examen initial puis l’évolution, particulièrement lorsque le suivi doit vérifier l’absence de progression.','hug22-neurologie','hug22-diagnostic-imagerie'))
s+=window(6,3,'Examiner les fonctions sacrées lorsque le tableau l’exige',
 p('Une suspicion de syndrome de la queue de cheval nécessite un examen de la sensibilité péri-anale et glutéale.','hug22-neurologie')+
 p('HUG ajoute la recherche du tonus sphinctérien anal par toucher rectal dans cette situation clinique.','hug22-neurologie')+
 p('Cet examen s’intègre à une démarche urgente ; il ne doit pas remplacer l’imagerie ni l’avis spécialisé nécessaires devant l’alerte.','hug22-neurologie','l81-hug-urgent-neuro'))
s+=h('Élargir l’examen lorsque la plainte sort du cadre rachidien')
s+=p('Une douleur du flanc avec contexte urinaire conduit à rechercher une atteinte du haut appareil et ses signes de complication.','l81-nice-pyelo-clinique','l81-eau-pyelo-differentiel')
s+=p('Une masse ou une sensibilité abdominale dans le contexte évocateur d’anévrisme réoriente immédiatement la démarche vers la cause vasculaire.','l81-esvs-aaa-clinique','l81-nice-aaa-urgence')
s+=p('Enfin, une claudication impose de considérer les fonctions vasculaires et les neuropathies concurrentes, au-delà de la seule image rachidienne.','l81-de2016-stenose-clinique')
save(6,s)

s=h('7.1 — Regrouper la douleur et la limitation lombaire')
s+=p('Le syndrome lombovertébral regroupe les manifestations locales étudiées par l’examen statique et dynamique du rachis.','hug22-dynamique','hug22-inspection')
s+=p('Sur le versant fonctionnel, le patient décrit sa douleur et les mouvements devenus difficiles ; sur le versant physique, le clinicien observe la mobilité et recherche une contracture.','hug22-definition','hug22-palpation','hug22-dynamique')
s+=p('Ce regroupement décrit un retentissement : il ne suffit pas à distinguer une cause commune d’une fracture ou d’une infection.','hug22-diagnostic-imagerie')
s+=window(7,1,'Raideur, limitation et contracture : trois constatations différentes',p('La raideur accompagne fréquemment la douleur lombaire et se précise par sa durée au réveil ainsi que par sa relation avec l’activité.','hug22-definition','hug22-anamnese')+p('La limitation est observée en demandant une flexion antérieure, postérieure et latérale ; elle objective la difficulté de mouvement décrite à l’entretien.','hug22-dynamique')+p('La contracture musculaire se recherche par palpation en décubitus ventral ; la station debout ne convient pas à cette appréciation.','hug22-palpation')+p('Ces manifestations peuvent s’associer à la kinésiophobie, qui participe aux obstacles à la mobilisation sans identifier une lésion anatomique précise.','hug22-dynamique','hug22-risque-chronicite'))
s+=h('7.2 — Reconnaître un ensemble radiculaire concordant')
s+=p('Le versant fonctionnel associe une irradiation dont le trajet est précisé et d’éventuelles plaintes sensitives ou motrices.','hug22-classification','hug22-neurologie')
s+=p('Le versant physique associe la recherche d’un signe irritatif et celle de déficits sensitifs, moteurs ou réflexes dans un territoire cohérent.','hug22-neurologie')
s+=p('Cette concordance soutient l’atteinte d’une racine ; une douleur lombaire provoquée isolément par la manœuvre de Lasègue ne possède pas la même signification.','hug22-neurologie')
s+=window(7,2,'Signe irritatif : reproduire la douleur radiculaire',p('Le Lasègue est positif lorsque l’élévation du membre inférieur tendu reproduit une douleur radiculaire entre 30° et 70°.','hug22-neurologie')+p('La douleur doit être caractérisée par son irradiation, car une douleur limitée au dos ne remplit pas cette description.','hug22-neurologie')+p('Le Lasègue direct est sensible tandis que le Lasègue croisé est spécifique ; leur interprétation complète la concordance clinique.','hug22-neurologie')+p('Pour une présentation antérieure, l’extension passive de hanche en décubitus ventral ou latéral recherche une douleur antérieure de cuisse compatible avec une irritation L2 à L4.','hug22-neurologie'))
s+=window(7,3,'Déficit moteur : distinguer plainte et faiblesse objectivée',p('Le déficit moteur se recherche muscle par muscle contre la pesanteur et contre résistance, puis se cote sur l’échelle M0 à M5.','hug22-neurologie')+p('M5 correspond à la force normale ; M4 désigne un mouvement possible contre une résistance modérée.','hug22-neurologie')+p('La marche sur les talons ou sur les pointes repère surtout les parésies importantes et ne remplace pas le testing ciblé.','hug22-neurologie')+p('Un déficit nouveau ou progressif change la conduite, parce qu’il peut signaler une compression nécessitant une exploration et un avis urgents.','l81-hug-urgent-neuro'))
s+=h('7.3 — Identifier la claudication neurogène')
s+=p('La plainte fonctionnelle apparaît progressivement à la marche, souvent dans les fesses ou les jambes, et s’améliore en position assise.','l81-hug-stenose')
s+=p('L’examen recherche une démarche à base élargie et la reproduction des manifestations lors de l’extension lombaire.','l81-hug-stenose')
s+=p('La sténose devient une explication clinique lorsque ce profil concorde avec l’imagerie ; une artériopathie ou une polyneuropathie peut produire une limitation concurrente.','l81-de2016-stenose-clinique')
s+=window(7,4,'Claudication : interroger le déclenchement et le soulagement',p('Le clinicien demande ce qui apparaît pendant la marche et ce qui permet la reprise, en distinguant l’arrêt de la marche de la mise en position assise.','l81-hug-stenose')+p('Le soulagement obtenu lorsque la lordose diminue soutient le profil neurogène décrit par HUG2022.','l81-hug-stenose')+p('L’extension lombaire maintenue pendant 30 secondes peut reproduire les symptômes dans ce contexte.','l81-hug-stenose')+p('Une image de rétrécissement canalaire isolée ne démontre cependant pas que cette structure explique la limitation à la marche.','l81-de2016-stenose-clinique'))
s+=h('7.4 — Repérer un ensemble compressif sacré ou médullaire')
s+=p('Des troubles sphinctériens et des anomalies de sensibilité périnéale imposent de rechercher une compression neurologique urgente.','hug22-neurologie','l81-hug-urgent-neuro')
s+=p('Le versant physique comprend l’examen de la sensibilité périanale et fessière ainsi que du tonus anal, dans le contexte clinique approprié.','hug22-neurologie')
s+=p('Chez une personne ayant un cancer actuel ou ancien, des manifestations de compression médullaire constituent une urgence oncologique.','l81-nice-metastase-urgences')
s+=window(7,5,'Anomalies sacrées : examiner sans transformer un signe en test d’exclusion',p('L’examen neurologique décrit par HUG2022 comporte la recherche d’une modification de la sensibilité périanale et fessière et l’appréciation du tonus anal au toucher rectal.','hug22-neurologie')+p('Ces constatations sont confrontées aux plaintes sphinctériennes et aux autres déficits, car la suspicion compressive commande l’imagerie et l’avis neurochirurgical urgents.','l81-hug-urgent-neuro','hug22-neurologie')+p('Une stratégie fondée sur les seuls antalgiques ne répond pas à cette suspicion compressive.','l81-hug-urgent-neuro'))
s+=h('7.5 — Reconnaître une présentation inflammatoire ou viscérale')
s+=p('Le profil inflammatoire associe une amélioration par l’activité, une absence de soulagement au repos, une douleur de seconde partie de nuit et une raideur matinale prolongée.','hug22-anamnese')
s+=p('La recherche d’arthrite, d’enthésite, de psoriasis, d’uvéite ou de maladie inflammatoire intestinale renforce l’orientation vers une spondyloarthrite.','l81-hug-axspa')
s+=p('La présentation urinaire haute associe une douleur du flanc et des manifestations infectieuses ou obstructives à préciser ; la pyélonéphrite peut débuter avec peu de symptômes urinaires bas préalables.','audit81-hug21-pyelo-cadre','l81-eau-calcul-clinique')
s+=window(7,6,'Douleur inflammatoire : une orientation, pas une preuve isolée',p('La raideur matinale dépassant 30 minutes appartient au profil inflammatoire décrit par HUG2022, tandis qu’une raideur plus brève appartient au profil mécanique présenté dans ce document.','hug22-anamnese')+p('Le clinicien recherche ce rythme à l’interrogatoire et le confronte aux manifestations extra-articulaires.','hug22-anamnese','l81-hug-axspa')+p('L’amélioration sous anti-inflammatoire n’est pas spécifique et ne suffit donc pas à confirmer une spondyloarthrite.','hug22-anamnese'))
s+=table(['Syndrome clinique','Signes fonctionnels','Signes physiques et portée'],[
[cell('Le regroupement lombovertébral décrit une atteinte locale.','hug22-dynamique'),cell('La douleur s’accompagne d’une difficulté à mobiliser le dos.','hug22-definition'),cell('La mobilité et la contracture sont recherchées sans attribuer d’emblée une cause unique.','hug22-dynamique','hug22-palpation')],
[cell('L’ensemble radiculaire repose sur une concordance territoriale.','hug22-neurologie'),cell('L’irradiation et les plaintes neurologiques sont caractérisées.','hug22-classification'),cell('Les signes irritatifs et déficitaires sont confrontés entre eux.','hug22-neurologie')],
[cell('La claudication neurogène traduit une limitation déclenchée à la marche.','l81-hug-stenose'),cell('La position assise ou la diminution de lordose soulage les manifestations.','l81-hug-stenose'),cell('L’examen et l’imagerie doivent concorder, avec recherche de causes concurrentes.','l81-de2016-stenose-clinique')],
[cell('La présentation infectieuse urinaire haute nécessite une recherche de complication.','l81-eau-pyelo-differentiel'),cell('La douleur du flanc peut accompagner fièvre et symptômes urinaires.','audit81-hug21-pyelo-cadre'),cell('La recherche d’obstruction et l’analyse microbiologique orientent la conduite.','l81-eau-pyelo-culture','l81-eau-pyelo-imagerie')]
])
save(7,s)

s=h('Un diagnostic positif adapté à la branche clinique')
s+=p('La douleur dorsale ou lombaire est une plainte : elle n’a pas un jeu unique de critères qui confirmerait toutes ses causes.','hug22-classification','hug22-diagnostic-imagerie')
s+=p('Le référentiel HUG2022 distingue les présentations communes, les atteintes neurologiques et les origines spécifiques ; la démarche positive dépend de cette distinction.','hug22-classification','hug22-diagnostic-imagerie')
s+=p('NICE NG59 conserve la recommandation de rechercher les diagnostics alternatifs, notamment lorsqu’apparaissent des symptômes nouveaux ou modifiés.','nice26-1-1-1')
s+=table(['Branche et référence','Ce qui soutient le diagnostic','Ce qui ne suffit pas','Conséquence'],[
[cell('La lombalgie commune suit la démarche clinique HUG2022.','hug22-diagnostic-imagerie'),cell('L’anamnèse et l’examen ont écarté les arguments pour une origine spécifique.','hug22-diagnostic-imagerie'),cell('Une image dégénérative isolée ne suffit pas à expliquer la douleur.','hug22-diagnostic-imagerie'),cell('Les examens complémentaires ne sont alors pas nécessaires de routine.','hug22-diagnostic-imagerie')],
[cell('La présentation radiculaire est caractérisée selon HUG2022.','hug22-classification'),cell('Un trajet compatible et des signes irritatifs ou déficitaires concordants soutiennent l’atteinte radiculaire.','hug22-neurologie'),cell('Une irradiation non caractérisée n’établit pas à elle seule une hernie discale responsable.','hug22-classification','hug22-diagnostic-imagerie'),cell('L’importance et l’évolution du déficit déterminent le degré d’urgence.','l81-hug-urgent-neuro','hug22-diagnostic-imagerie')],
[cell('La sténose symptomatique exige une concordance clinique.','l81-de2016-stenose-clinique'),cell('La claudication typique et les données d’imagerie se répondent.','l81-hug-stenose','l81-de2016-stenose-clinique'),cell('Le rétrécissement anatomique peut accompagner le vieillissement sans expliquer tous les symptômes.','l81-de2016-stenose-clinique'),cell('Les diagnostics vasculaires et neuropathiques concurrents restent à examiner.','l81-de2016-stenose-clinique')],
[cell('L’orientation axiale inflammatoire repose ici sur le cadre HUG2022.','l81-hug-axspa'),cell('Le début avant 45 ans et la persistance au-delà de 12 semaines accompagnent la recherche des autres signes évocateurs.','l81-hug-axspa'),cell('La réponse aux AINS ne constitue pas une confirmation isolée.','hug22-anamnese'),cell('Un bilan ciblé et un avis rhumatologique complètent l’orientation.','hug22-diagnostic-imagerie','l81-hug-axspa')],
[cell('La pyélonéphrite se recherche par une démarche clinique et microbiologique.','l81-nice-pyelo-clinique'),cell('La clinique compatible est confrontée à la culture urinaire et aux diagnostics alternatifs.','l81-nice-pyelo-clinique'),cell('La bandelette seule ne remplace pas la culture recommandée dans toute pyélonéphrite.','l81-eau-pyelo-culture'),cell('Le caractère obstructif doit être identifié rapidement.','l81-eau-pyelo-differentiel')]
])
s+=h('Distinguer la classification temporelle du degré d’urgence')
s+=p('HUG2022 utilise les catégories aiguë, subaiguë et chronique pour décrire l’évolution temporelle ; elles ne constituent pas des stades de compression neurologique.','hug22-classification','l81-hug-urgent-neuro')
s+=p('La présence d’une alarme neurologique impose sa propre conduite, quelle que soit l’ancienneté de la douleur.','l81-hug-urgent-neuro')
s+=p('À l’inverse, HUG2022 décrit des déficits discrets, stables et sans retentissement fonctionnel pour lesquels une imagerie immédiate n’est pas systématique.','hug22-diagnostic-imagerie')
s+=window(8,1,'Déficit discret : préserver les conditions de l’exception',p('HUG2022 cite un déficit M4 des muscles majeurs ou un déficit même inférieur à M4 de la dorsiflexion de l’hallux, lorsqu’il est discret, stable, non progressif et sans retentissement fonctionnel.','hug22-diagnostic-imagerie')+p('Dans cette situation précise, le document permet l’absence d’imagerie initiale, mais demande un suivi régulier.','hug22-diagnostic-imagerie')+p('Cette conduite ne s’étend pas à un déficit progressif ni à des signes de compression urgente.','hug22-diagnostic-imagerie','l81-hug-urgent-neuro'))
s+=h('Employer un outil pronostique pour son usage prévu')
s+=p('Le Keele STarT Back Screening Tool aide à stratifier le risque de chronicisation dès la première consultation.','hug22-risque-chronicite','nice26-1-1-2')
s+=p('HUG2022 mentionne une version française validée et des catégories de risque faible, intermédiaire ou élevé.','hug22-risque-chronicite')
s+=p('NICE propose un accompagnement plus simple lorsque l’évolution favorable est probable et un soutien plus intensif lorsque le risque d’évolution défavorable est supérieur.','nice26-1-1-3')
s+=p('Ce classement organise l’accompagnement ; l’exclusion préalable des causes spécifiques relève d’une démarche clinique distincte.','nice26-1-1-1','nice26-1-1-2','nice26-1-1-3')
s+=window(8,2,'Drapeaux jaunes, bleus et noirs : ne pas les confondre avec les alarmes',p('Les facteurs individuels tels que les croyances catastrophiques, la peur du mouvement et les troubles de l’humeur participent au risque de chronicisation.','hug22-risque-chronicite')+p('Les facteurs professionnels et socio-économiques complètent cette appréciation.','hug22-risque-chronicite')+p('Leur présence appelle un accompagnement adapté et parfois multidisciplinaire ; elle ne permet pas d’écarter une infection, un cancer ou une compression.','hug22-risque-chronicite','nice26-1-1-1'))
save(8,s)

s=h('9.a — La question clinique détermine la référence diagnostique')
s+=p('La lombalgie commune est un diagnostic clinique : HUG2022 ne demande ni laboratoire ni imagerie lorsque la recherche d’une origine spécifique est négative.','hug22-diagnostic-imagerie')
s+=p('Une exploration ne devient utile que si son résultat peut modifier la prise en charge ; un avis spécialisé ne signifie donc pas automatiquement une imagerie.','nice26-1-1-5','nice26-1-1-6')
s+=p('Pour une suspicion de compression neurologique urgente, HUG2022 demande une IRM si possible, au minimum un scanner, avec avis neurochirurgical immédiat.','l81-hug-urgent-neuro')
s+=p('Pour une infection vertébrale, l’IRM est l’examen de référence dans le consensus européen EANS ; un scanner de remplacement reste moins sensible au stade précoce selon HUG2022.','l81-eans-infection-neuro','l81-hug-urgent-infection')
s+=h('9.b — Prescrire la première intention en formulant son objectif')
s+=table(['Situation','Demande ciblée','Interprétation et conduite'],[
[cell('Une présentation commune ne comporte pas d’alarme après l’évaluation clinique.','hug22-diagnostic-imagerie'),cell('Aucun examen complémentaire systématique n’est demandé.','hug22-diagnostic-imagerie'),cell('La prise en charge reste clinique et les consignes de reconsultation accompagnent la sortie.','hug22-evolution-suivi-retour')],
[cell('Un déficit neurologique d’alarme fait suspecter une compression.','l81-hug-urgent-neuro'),cell('Une imagerie rachidienne urgente est demandée, de préférence par IRM, avec avis neurochirurgical.','l81-hug-urgent-neuro'),cell('Le déficit et sa progression sont communiqués au spécialiste sans attendre une prise en charge conservatrice prolongée.','l81-hug-urgent-neuro')],
[cell('Le contexte évoque une fracture vertébrale avec critères de gravité.','l81-hug-fracture-ct'),cell('Le scanner recherche la lésion osseuse dans le cadre défini par HUG2022.','l81-hug-fracture-ct'),cell('L’immobilisation par une douleur incontrôlée ou les autres éléments de gravité conduisent à une exploration urgente.','l81-hug-fracture-ct')],
[cell('Une infection rachidienne est suspectée devant une clinique compatible.','l81-hug-infection'),cell('Une IRM urgente et un bilan biologique ciblé recherchent l’atteinte et son contexte inflammatoire.','l81-hug-infection','l81-hug-urgent-infection'),cell('Un scanner précoce peu contributif ne possède pas la sensibilité de l’IRM et ne clôt pas à lui seul la suspicion.','l81-hug-urgent-infection')],
[cell('Une colique néphrétique est envisagée.','l81-eau-calcul-clinique'),cell('L’échographie est l’examen primaire recommandé par l’EAU ; le scanner sans injection confirme ensuite le diagnostic lorsque cette confirmation est indiquée.','l81-eau-calcul-clinique','l81-eau-calcul-image'),cell('L’imagerie immédiate s’impose notamment en cas de fièvre, de rein unique ou de doute diagnostique.','l81-eau-calcul-image')],
[cell('Une pyélonéphrite est suspectée.','l81-eau-pyelo-culture'),cell('Une analyse urinaire et une culture avec antibiogramme sont demandées pour toute pyélonéphrite.','l81-eau-pyelo-culture'),cell('La culture permet de documenter le germe et de guider l’adaptation du traitement.','l81-eau-pyelo-culture')],
[cell('Un anévrisme symptomatique ou rompu est suspecté.','l81-nice-aaa-urgence'),cell('Une échographie aortique immédiate au lit est demandée selon NICE, avec contact vasculaire immédiat dans les situations indiquées.','l81-nice-aaa-urgence'),cell('Une échographie indisponible ou non diagnostique ne doit pas arrêter l’orientation urgente si la suspicion persiste.','l81-nice-aaa-urgence')]
])
s+=window(9,1,'Biologie : demander un résultat qui répond à une hypothèse',p('Une suspicion infectieuse, tumorale ou inflammatoire peut justifier des marqueurs inflammatoires ciblés ; une lombalgie commune isolée ne justifie pas ce bilan systématique.','hug22-diagnostic-imagerie')+p('Dans la pyélonéphrite, l’analyse recherche notamment leucocytes, érythrocytes et nitrites, mais la culture avec étude de sensibilité reste recommandée dans tous les cas.','l81-eau-pyelo-culture')+p('Le prélèvement de culture est réalisé avant l’antibiothérapie lorsque la démarche décrite par NICE le permet.','l81-nice-pyelo-clinique')+p('En présence de sepsis sur obstacle, l’EAU demande de commencer les antibiotiques immédiatement et d’adapter ensuite le traitement aux résultats microbiologiques.','l81-eau-decompression'))
s+=h('9.c — Adapter la modalité aux contraintes réelles')
s+=p('Lors d’une grossesse avec suspicion de complication urinaire haute, l’EAU préfère l’échographie ou l’IRM afin d’éviter l’irradiation fœtale.','l81-eau-pyelo-imagerie')
s+=p('La stratégie rachidienne urgente prévoit un scanner lorsque l’IRM n’est pas réalisable, tout en reconnaissant ses limites en cas d’infection débutante.','l81-hug-urgent-neuro','l81-hug-urgent-infection')
s+=p('Pour une recherche de calcul, le scanner de confirmation décrit par l’EAU est sans produit de contraste ; l’injection répond à une autre question lorsqu’il faut préciser l’anatomie avant un traitement.','l81-eau-calcul-image')
s+=p('Ainsi, une indication de scanner pour calcul ne se transforme pas automatiquement en indication d’injection iodée.','l81-eau-calcul-image')
s+=p('Une perturbation de la fonction rénale fait partie des situations où l’EAU recommande une échographie de l’appareil urinaire dans la pyélonéphrite.','l81-eau-pyelo-imagerie')
s+=p('Pour la suspicion de spondyloarthrite axiale, le tableau HUG2022 mentionne une IRM sacro-iliaque sans contraste.','l81-hug-axspa')
s+=window(9,2,'Impossibilité d’IRM : préserver la question urgente',p('Lors d’une alarme neurologique, le choix d’un scanner de remplacement n’enlève pas la nécessité d’un avis neurochirurgical immédiat.','l81-hug-urgent-neuro')+p('Lors d’une suspicion infectieuse, la moindre sensibilité du scanner à un stade précoce doit rester visible dans l’interprétation.','l81-hug-urgent-infection')+p('Le résultat de l’examen est donc confronté à la clinique et à la question qui a motivé la demande.','l81-hug-urgent-infection','nice26-1-1-6'))
s+=h('9.d — Organiser la seconde intention et son délai')
s+=p('En cas de suspicion de compression médullaire métastatique, NICE demande une IRM aussi vite que possible et toujours dans les 24 heures.','l81-nice-mscc-irm')
s+=p('Lorsque des métastases rachidiennes sont suspectées sans signe de compression médullaire, le délai recommandé est d’une semaine.','l81-nice-metastase-sans-mscc')
s+=p('Ces délais correspondent à deux scénarios différents : le délai d’une semaine ne doit pas être appliqué à une présentation compressive.','l81-nice-mscc-irm','l81-nice-metastase-sans-mscc')
s+=p('Dans la pyélonéphrite, une fièvre persistante après 72 heures ou une détérioration clinique immédiate justifie une exploration complémentaire selon l’EAU.','l81-eau-pyelo-imagerie')
s+=p('L’EAU cite alors un scanner injecté, avec adaptation de modalité pendant la grossesse.','l81-eau-pyelo-imagerie')
s+=p('Dans une colique néphrétique, la confirmation par scanner sans contraste après l’échographie précise le calcul et peut identifier une autre cause de douleur.','l81-eau-calcul-image')
s+=window(9,3,'Échographie aortique : identifier l’anévrisme ne suffit pas à exclure une rupture',p('L’échographie peut montrer l’anévrisme, mais sa sensibilité pour l’hémorragie rétropéritonéale est faible.','l81-esvs-aaa-us')+p('L’absence de preuve échographique de fuite n’exclut donc pas une rupture.','l81-esvs-aaa-us')+p('NICE demande un contact immédiat avec le service vasculaire si l’anévrisme est identifié ou si l’examen est indisponible ou non diagnostique malgré une suspicion persistante.','l81-nice-aaa-urgence')+p('L’angioscanner thoraco-abdominal et iliaque fournit les données anatomiques majeures dans l’évaluation spécialisée d’une suspicion de rupture décrite par l’ESVS.','l81-esvs-aaa-us'))
s+=h('Lire le résultat sans perdre le patient')
s+=p('HUG2022 souligne la faible corrélation entre de nombreuses anomalies d’imagerie et la clinique, ainsi que le risque de chronicisation lié à leur interprétation anxiogène.','hug22-diagnostic-imagerie')
s+=p('Une anomalie ne devient causale qu’après confrontation à la localisation, au mécanisme clinique et aux manifestations recherchées.','hug22-diagnostic-imagerie','l81-de2016-stenose-clinique')
s+=p('Une exploration rassurante à un instant ne dispense pas de réévaluer l’apparition d’une fièvre, d’un trouble neurologique ou d’une augmentation inhabituelle des douleurs.','hug22-evolution-suivi-retour')
save(9,s)

s=h('Décision initiale — Rechercher les présentations qui ne peuvent pas attendre')
s+=p('Si une douleur abdominale ou dorsale s’accompagne d’un tableau évocateur d’anévrisme symptomatique ou rompu → demander l’échographie immédiate et contacter le service vasculaire selon le résultat ou la persistance de la suspicion.','l81-esvs-aaa-clinique','l81-nice-aaa-urgence')
s+=p('Si des signes neurologiques d’alarme évoquent une compression → demander l’IRM urgente si possible, au minimum le scanner, et l’avis neurochirurgical sans attendre.','l81-hug-urgent-neuro')
s+=p('Si une personne ayant un cancer présente des signes de compression médullaire → activer immédiatement la filière spécialisée et obtenir l’IRM au plus vite, toujours dans les 24 heures.','l81-nice-metastase-urgences','l81-nice-mscc-irm')
s+=p('Si une infection urinaire s’associe à un obstacle et à un sepsis → commencer immédiatement l’antibiothérapie et organiser la décompression urgente du système collecteur.','l81-eau-obstr-sepsis','l81-eau-decompression')
s+=p('Si une infection rachidienne est suspectée → organiser l’IRM urgente ; un déficit neurologique nouveau renforce la nécessité de l’avis chirurgical.','l81-hug-urgent-infection','l81-eans-infection-neuro')
s+=p('Si une fracture comporte les éléments de gravité définis par HUG2022 → demander le scanner urgent et orienter la prise en charge selon les constatations.','l81-hug-fracture-ct')
s+=h('Décision suivante — Caractériser l’orientation clinique')
s+=p('Si l’irradiation suit un territoire radiculaire → tester les signes irritatifs, la sensibilité, la force et les réflexes pour établir la concordance et le niveau de gravité.','hug22-neurologie')
s+=p('Si le déficit est discret, stable, non progressif et sans retentissement fonctionnel dans les conditions HUG2022 → une surveillance régulière peut précéder l’imagerie.','hug22-diagnostic-imagerie')
s+=p('Si la marche déclenche des manifestations soulagées par la position assise → rechercher une claudication neurogène et vérifier les diagnostics concurrents avant d’attribuer la plainte à une sténose.','l81-hug-stenose','l81-de2016-stenose-clinique')
s+=p('Si le rythme est inflammatoire et que les autres éléments évoquent une spondyloarthrite → organiser un bilan ciblé et un avis rhumatologique.','l81-hug-axspa','hug22-diagnostic-imagerie')
s+=p('Si la douleur est surtout lombaire ou abdominale avec orientation urinaire → distinguer colique néphrétique, pyélonéphrite et présentation obstructive infectée.','audit81-hug23-colique-definition','audit81-hug21-pyelo-cadre','l81-eau-pyelo-differentiel')
s+=p('Si une pyélonéphrite est retenue → demander culture et antibiogramme, rechercher les indications d’imagerie et adapter le traitement au contexte.','l81-eau-pyelo-culture','l81-eau-pyelo-imagerie')
s+=h('Décision de prise en charge commune — Associer fonction et surveillance')
s+=p('Si l’entretien et l’examen n’orientent pas vers une cause spécifique → retenir la démarche clinique de lombalgie commune, sans examen systématique.','hug22-diagnostic-imagerie')
s+=p('Si le risque de chronicisation est faible → privilégier information, réassurance et maintien d’activité selon les capacités.','nice26-1-1-3','hug22-non-medicamenteux')
s+=p('Si les facteurs de chronicisation se cumulent → prévoir un suivi plus rapproché et un accompagnement multimodal adapté.','hug22-risque-chronicite')
s+=p('Si la symptomatologie ne s’améliore pas significativement après 4 à 7 jours de traitement ou si une fièvre ou un trouble neurologique apparaît → reconsulter selon les consignes HUG2022.','hug22-evolution-suivi-retour')
s+=p('Si l’évolution reste défavorable après 4 semaines de prise en charge adéquate → rechercher de nouveau les alarmes et les facteurs de chronicisation, puis envisager l’avis spécialisé approprié.','hug22-evolution-suivi-retour')
s+=window(10,1,'Un changement de branche est une décision clinique',p('Un patient initialement pris en charge pour une douleur commune peut développer des symptômes nouveaux ou modifiés ; NICE demande alors de reconsidérer les diagnostics alternatifs.','nice26-1-1-1')+p('Une augmentation de la douleur malgré un traitement correctement conduit constitue également un signal d’alarme dans le suivi HUG2022.','hug22-evolution-suivi-retour')+p('La conclusion initiale reste donc révisable, avec des consignes concrètes de reconsultation.','nice26-1-1-1','hug22-evolution-suivi-retour'))
save(10,s)

s=h('11.A — Fixer un objectif fonctionnel et un calendrier de réévaluation')
s+=p('HUG2022 vise une mobilisation précoce, la reprise des activités et la prévention de la chronicisation, en tenant compte des préférences et des capacités du patient.','hug22-non-medicamenteux')
s+=p('Une amélioration significative absente après 4 à 7 jours de traitement appelle une reconsultation, tandis qu’un signe nouveau impose une réévaluation adaptée sans attendre ce délai.','hug22-evolution-suivi-retour')
s+=p('La diminution de la douleur est recherchée pour soutenir la fonction ; l’objectif ne se réduit pas à obtenir une image radiologique normale.','hug22-non-medicamenteux','hug22-diagnostic-imagerie')
s+=p('Pour une atteinte spécifique, le but dépend de la menace : décomprimer un système urinaire infecté obstrué, identifier une compression neurologique ou orienter une urgence vasculaire.','l81-eau-decompression','l81-hug-urgent-neuro','l81-nice-aaa-urgence')
s+=h('11.B — Traiter dans l’ordre dicté par le mécanisme et la gravité')
s+=window(11,1,'Urgence — conduite chronologique',p('D’abord, les signes cliniques sont recherchés et la filière adaptée à la menace est contactée : vasculaire pour une suspicion aortique persistante, neurochirurgicale pour une alarme compressive.','l81-nice-aaa-urgence','l81-hug-urgent-neuro')+p('Ensuite, l’imagerie urgente répond à la question correspondante : échographie aortique immédiate selon NICE ou IRM rachidienne si possible selon HUG2022.','l81-nice-aaa-urgence','l81-hug-urgent-neuro')+p('En présence de sepsis urinaire sur obstacle, l’antibiothérapie commence immédiatement et la décompression urgente est organisée.','l81-eau-decompression')+p('La décompression peut utiliser une endoprothèse urétérale ou une néphrostomie percutanée ; le traitement définitif du calcul attend la résolution du sepsis.','l81-eau-obstr-sepsis','l81-eau-decompression')+p('Les prélèvements et leur suivi permettent ensuite d’adapter l’antibiothérapie ; la nécessité de soins intensifs est évaluée dans ce contexte.','l81-eau-decompression')+p('Pour une suspicion de compression métastatique, l’IRM doit être réalisée au plus vite et toujours dans les 24 heures, avec la coordination spécialisée immédiate.','l81-nice-mscc-irm','l81-nice-metastase-urgences'))
s+=p('Une fois les causes urgentes ou spécifiques prises en charge selon leur filière, la lombalgie commune relève principalement de l’éducation, de l’activité adaptée et d’un traitement antalgique sélectionné.','hug22-non-medicamenteux','hug22-pharmaco-commune')
s+=p('La réassurance porte sur le pronostic et la possibilité de récupération ; elle respecte l’expérience douloureuse du patient.','hug22-non-medicamenteux','hug22-evolution-suivi-retour')
s+=p('La physiothérapie privilégie l’approche active et un programme que le patient peut poursuivre à domicile, avec progression selon ses capacités.','hug22-non-medicamenteux')
s+=p('Les exercices peuvent travailler endurance, force, stabilité et proprioception ; HUG2022 ne désigne pas une forme unique comme supérieure dans tous les cas.','hug22-non-medicamenteux')
s+=p('Le repos au lit est défavorable à la récupération ; la reprise graduée des activités et du travail fait partie de la prise en charge.','hug22-non-medicamenteux','nice26-1-2-15')
s+=p('NICE, dans sa recommandation amendée en 2026, ne propose la thérapie manuelle que dans un ensemble incluant des exercices.','nice26-1-2-7')
s+=h('Sélection pharmacologique — Séparer recommandation clinique et information du produit')
s+=p('Les AINS oraux peuvent être envisagés dans la lombalgie après appréciation des risques digestifs, hépatiques et cardiorénaux, notamment liés à l’âge.','nice26-1-2-22')
s+=p('Ils sont utilisés à la dose efficace la plus faible et pendant la durée la plus courte possible, avec surveillance et gastroprotection lorsque celles-ci sont appropriées.','nice26-1-2-23','nice26-1-2-24')
s+=p('Dans la sciatique, NICE souligne que les données de bénéfice des AINS restent limitées et que leurs risques doivent être pris en compte.','nice26-1-2-20','nice26-1-2-21')
s+=p('Brufen® dispose dans son information professionnelle suisse d’indications comprenant les lombalgies et les névralgies secondaires à des lésions discales.','aips81-brufen-4')
s+=p('L’autorisation d’une indication ne dispense pas de vérifier si le rapport bénéfice-risque individuel justifie son emploi.','aips81-brufen-4','aips81-brufen-7-p3','nice26-1-2-22')
s+=table(['Molécule et spécialité','Posologie AIPS contextualisée','Voie et durée','Contre-indications majeures','Extrait primaire et identification'],[
[cell('L’ibuprofène est le principe actif de Brufen®.','aips81-brufen-5'),cell('Dans les affections rhumatismales de l’adulte, l’AIPS décrit une dose initiale de 1200 à 1800 mg/jour répartie en plusieurs doses, adaptée aux besoins du patient.','aips81-brufen-5'),cell('Les comprimés sont avalés entiers avec de l’eau ; la dose efficace minimale est utilisée pendant le minimum de temps nécessaire.','aips81-brufen-5'),cell('L’insuffisance rénale grave avec clairance de créatinine inférieure à 30 ml/min, l’insuffisance cardiaque NYHA III à IV et le troisième trimestre font partie des contre-indications.','aips81-brufen-6'),cell('La rubrique précise : « La posologie est adaptée aux besoins du patient. » Les numéros Swissmedic sont 45031 et 49669 ; l’information date de décembre 2024.','aips81-brufen-5','aips81-brufen-17','aips81-brufen-20')]
])
s+=window(11,2,'Brufen® — Lire la dose dans son contexte',p('La posologie AIPS des affections rhumatismales de l’adulte est présentée ici parce que les lombalgies figurent dans les indications rhumatismales extra-articulaires du produit.','aips81-brufen-4','aips81-brufen-5')+p('La même rubrique indique qu’une dose d’entretien de 600 à 1200 mg/jour suffit chez de nombreux patients et qu’une augmentation à 2400 mg/jour peut être nécessaire dans certains cas.','aips81-brufen-5')+p('Ces valeurs ne constituent pas une instruction d’augmenter systématiquement la dose pour une lombalgie aiguë ; la dose minimale efficace et la durée minimale restent la règle du produit et de NICE.','aips81-brufen-5','nice26-1-2-24')+p('L’AIPS demande d’éviter les doses élevées de 2400 mg/jour dans plusieurs situations cardiovasculaires, dont hypertension non maîtrisée, insuffisance cardiaque NYHA II et maladie ischémique existante.','aips81-brufen-7-p27')+p('Les posologies des céphalées ou de la dysménorrhée appartiennent à d’autres indications et ne remplacent pas la rubrique correspondant à la situation traitée.','aips81-brufen-5'))
s+=window(11,3,'Brufen® — Vérifier les exclusions avant la première prise',p('L’hypersensibilité au produit et les antécédents de bronchospasme, d’urticaire ou de réaction allergique après aspirine ou autre AINS sont des contre-indications.','aips81-brufen-6')+p('Un ulcère ou une hémorragie digestive actifs, les antécédents répétés précisés dans l’AIPS et une hémorragie ou perforation liée auparavant aux AINS contre-indiquent également le produit.','aips81-brufen-6')+p('Les maladies inflammatoires intestinales actives ou avérées et une tendance accrue aux saignements figurent parmi les contre-indications.','aips81-brufen-6')+p('Les troubles hépatiques fonctionnels graves, notamment cirrhose ou ascite, l’insuffisance rénale grave et l’insuffisance cardiaque grave doivent être recherchés.','aips81-brufen-6')+p('Le traitement des douleurs après pontage aorto-coronarien est également contre-indiqué.','aips81-brufen-6')+p('L’association à un autre AINS, y compris un inhibiteur sélectif de COX-2, doit être évitée en raison du risque accru d’ulcère ou de saignement.','aips81-brufen-7-p14'))
s+=h('Choisir les classes avec les restrictions actuelles')
s+=p('NICE ne recommande pas le paracétamol seul pour la lombalgie.','nice26-1-2-26')
s+=p('Un opioïde faible, éventuellement associé au paracétamol, n’est envisagé dans la lombalgie aiguë que si un AINS est contre-indiqué, mal toléré ou inefficace.','nice26-1-2-25')
s+=p('Les opioïdes ne sont pas proposés de routine dans la lombalgie aiguë et ne sont pas recommandés pour la lombalgie chronique ni pour la sciatique chronique.','nice26-1-2-27','nice26-1-2-28','nice26-1-2-17')
s+=p('NICE ne recommande pas gabapentinoïdes, autres antiépileptiques, corticoïdes oraux ou benzodiazépines pour la sciatique, en raison de l’absence de bénéfice global démontré et de dommages constatés.','nice26-1-2-16')
s+=p('Les gabapentinoïdes et antiépileptiques ne sont pas non plus recommandés pour la lombalgie.','nice26-1-2-30')
s+=p('Si un patient prend déjà un opioïde, un gabapentinoïde ou une benzodiazépine pour la sciatique, les risques de poursuite et les difficultés de sevrage doivent être discutés avant une modification.','nice26-1-2-18','nice26-1-2-19')
s+=p('Les inhibiteurs sélectifs de recapture de la sérotonine, les inhibiteurs de recapture de sérotonine et noradrénaline et les tricycliques ne sont pas recommandés par NICE comme traitement de la lombalgie.','nice26-1-2-29')
s+=window(11,4,'Grossesse, allaitement et projet de grossesse : restrictions Brufen®',p('L’AIPS demande d’éviter l’ibuprofène au premier et au deuxième trimestre, sauf nécessité clairement établie, puis de minimiser la dose et la durée s’il est utilisé.','aips81-brufen-9')+p('À partir de la 20ème semaine, les AINS peuvent entraîner un trouble rénal fœtal et un oligohydramnios ; un rétrécissement du canal artériel a également été observé au deuxième trimestre.','aips81-brufen-9')+p('Si le traitement dépasse 48 heures, une surveillance échographique du liquide amniotique et du cœur fœtal doit être envisagée selon l’information du produit.','aips81-brufen-9')+p('La survenue d’un oligohydramnios ou d’un rétrécissement du canal artériel impose l’arrêt de Brufen® et un suivi approprié.','aips81-brufen-9')+p('Le troisième trimestre constitue une contre-indication.','aips81-brufen-6','aips81-brufen-9')+p('Pour l’allaitement, cette information professionnelle suisse indique de ne pas prendre l’ibuprofène par prudence et de sevrer le nourrisson si le traitement est indispensable.','aips81-brufen-9')+p('Le produit peut affecter la fertilité féminine ; l’AIPS ne le recommande pas aux femmes souhaitant concevoir.','aips81-brufen-9'))
s+=window(11,5,'Âge, rein, foie et déshydratation : adapter l’exposition',p('Chez la personne âgée, les effets indésirables digestifs des AINS sont plus fréquents et peuvent être mortels.','aips81-brufen-7-p16')+p('En présence d’une limitation rénale, hépatique ou cardiaque, l’AIPS demande la plus faible dose possible et un contrôle régulier de la fonction rénale, notamment si le traitement se prolonge.','aips81-brufen-7-p11')+p('Une insuffisance rénale grave avec clairance inférieure à 30 ml/min ou des troubles hépatiques fonctionnels graves constituent des contre-indications, et non de simples situations de réduction posologique.','aips81-brufen-6')+p('Une déshydratation importante impose une réhydratation avant le traitement et une surveillance étroite, avec un risque particulier chez l’enfant, l’adolescent et la personne âgée.','aips81-brufen-7-p34')+p('Les comprimés Brufen® dosés à 400 ou 600 mg et les granulés ne doivent pas être utilisés avant 12 ans en raison de leur dosage.','aips81-brufen-5')+p('Le comprimé à 200 mg n’est pas indiqué avant 6 ans.','aips81-brufen-5')+p('Ces limites de formulation ne transforment pas la posologie adulte présentée ici en schéma pédiatrique.','aips81-brufen-5'))
s+=h('11.C — Surveiller la fonction, le risque et la tolérance')
s+=p('Sous AINS, la surveillance tient compte du terrain digestif, hépatique et cardiorénal ainsi que des autres médicaments.','nice26-1-2-21','nice26-1-2-23')
s+=p('Les anticoagulants, antiagrégants, corticoïdes oraux et inhibiteurs sélectifs de recapture de la sérotonine peuvent accroître le risque digestif et appellent une prudence particulière.','aips81-brufen-7-p21')
s+=p('Les patients ayant des antécédents digestifs, notamment âgés, doivent signaler tout symptôme abdominal inhabituel, surtout au début du traitement.','aips81-brufen-7-p20')
s+=p('Une hémorragie digestive ou un ulcère survenant sous Brufen® impose l’arrêt du traitement.','aips81-brufen-7-p22')
s+=p('Les premiers signes d’éruption cutanée, de lésion muqueuse ou d’hypersensibilité imposent également l’arrêt du produit.','aips81-brufen-7-p31')
s+=p('Sur le plan clinique, un syndrome radiculaire nécessite un suivi régulier pour vérifier l’absence de progression neurologique.','hug22-evolution-suivi-retour')
s+=p('Une absence d’amélioration, une nouvelle fièvre, un trouble neurologique ou une douleur croissante malgré un traitement bien conduit impose de réexaminer la situation.','hug22-evolution-suivi-retour')
s+=h('11.D — Pronostic, sortie et reprise des rôles habituels')
s+=p('HUG2022 décrit un taux de guérison élevé de la lombalgie aiguë commune dans les 6 semaines ; ce pronostic ne s’applique pas indistinctement aux causes spécifiques.','hug22-evolution-suivi-retour','hug22-classification')
s+=p('La décision ambulatoire de la présentation commune s’appuie sur l’évaluation initiale, les possibilités d’activité et un plan de reconsultation.','hug22-diagnostic-imagerie','hug22-non-medicamenteux','hug22-evolution-suivi-retour')
s+=h('Repères de sortie de la branche commune — synthèse opérationnelle des recommandations HUG2022')
s+=p('Premier repère : la démarche clinique n’a pas identifié de cause spécifique nécessitant une exploration ou une orientation urgente.','hug22-diagnostic-imagerie')
s+=p('Deuxième repère : le patient reçoit une explication de la situation et des conseils d’activité adaptés à ses capacités.','hug22-non-medicamenteux')
s+=p('Troisième repère : le traitement retenu respecte ses risques individuels et ses contre-indications, avec des consignes de surveillance compréhensibles.','nice26-1-2-22','nice26-1-2-23','aips81-brufen-6')
s+=p('Quatrième repère : les motifs de reconsultation sont expliqués, notamment absence d’amélioration significative après 4 à 7 jours, nouvelle fièvre ou trouble neurologique.','hug22-evolution-suivi-retour')
s+=p('Cinquième repère : le suivi est renforcé lorsqu’existent des facteurs de chronicisation ou un syndrome radiculaire.','hug22-evolution-suivi-retour')
s+=p('Ces repères reprennent une conduite clinique ; les alarmes spécifiques gardent leur filière et ne relèvent pas de cette sortie pour lombalgie commune.','hug22-diagnostic-imagerie','l81-hug-urgent-neuro','l81-eau-decompression')
s+=p('L’arrêt de travail dépend du handicap fonctionnel et des exigences professionnelles ; HUG2022 préconise, s’il est nécessaire, une durée initiale maximale de 3 à 5 jours, prolongée seulement après réévaluation.','hug22-evolution-suivi-retour')
s+=p('L’aménagement ergonomique du poste peut réduire la kinésiophobie et les arrêts de travail ; la reprise se prépare en fonction de la tâche réelle.','hug22-evolution-suivi-retour')
s+=p('Une évolution défavorable après 4 semaines de prise en charge adéquate conduit à rechercher de nouveau les alarmes et les facteurs de chronicisation, avec avis rhumatologique ou de rééducation si nécessaire.','hug22-evolution-suivi-retour')
save(11,s)

s=h('Prévention primaire — Soutenir l’activité sans promettre l’absence de premier épisode')
s+=p('La fréquence élevée des lombalgies en Suisse donne une place importante à l’information sur l’activité et à la limitation des obstacles à la mobilisation.','hug22-epidemiologie','hug22-non-medicamenteux')
s+=p('HUG2022 décrit toutefois surtout la prévention des récidives : son constat d’efficacité de l’activité physique ne doit pas être présenté comme une garantie d’éviter tout premier épisode.','hug22-prevention')
s+=p('Les facteurs associés aux épisodes comprennent notamment des caractéristiques professionnelles, la sédentarité, l’obésité et le tabagisme ; leur présence s’interprète dans une histoire individuelle.','hug22-anamnese')
s+=p('L’information explique que l’activité adaptée et la compréhension de la douleur font partie de la prise en charge, sans promettre qu’une posture unique supprimerait toutes les causes de douleur dorsale.','hug22-non-medicamenteux','hug22-classification')
s+=h('Prévention secondaire — Réduire les récidives et reconnaître les changements')
s+=p('HUG2022 indique que la promotion de l’activité physique diminue le nombre et la durée des récidives de lombalgie non spécifique.','hug22-prevention')
s+=p('L’intervention pratique consiste à construire un programme compatible avec les capacités et les préférences du patient, puis à soutenir sa poursuite à domicile.','hug22-non-medicamenteux','nice26-1-2-1','nice26-1-2-2')
s+=p('Les interventions éducatives intégrant les dimensions biologiques, psychologiques et sociales peuvent modifier durablement les croyances et les comportements face à la maladie.','hug22-prevention')
s+=p('Le Guide du dos cité par HUG2022 constitue un support d’information destiné au patient.','hug22-prevention')
s+=p('Les consignes de reconsultation participent à cette prévention secondaire : nouvelle fièvre, trouble neurologique ou absence d’amélioration significative après 4 à 7 jours nécessitent une nouvelle appréciation.','hug22-evolution-suivi-retour')
s+=p('Une présentation nouvelle ne doit pas être attribuée automatiquement aux épisodes précédents, car NICE demande de rechercher les diagnostics alternatifs lorsque les symptômes changent.','nice26-1-1-1')
s+=window(12,1,'Transformer un conseil d’activité en action concrète',p('Le choix des exercices tient compte des besoins, des préférences et des capacités de la personne.','nice26-1-2-2')+p('La progression peut viser endurance, force, stabilité et proprioception, avec des exercices poursuivis à domicile.','hug22-non-medicamenteux')+p('La peur du mouvement et les croyances catastrophiques sont recherchées lorsqu’elles entravent cette reprise.','hug22-risque-chronicite')+p('Le programme évolue avec la récupération fonctionnelle et l’identification des obstacles, plutôt qu’avec la seule description d’une image dégénérative.','hug22-non-medicamenteux','hug22-diagnostic-imagerie'))
s+=h('Prévention tertiaire — Réduire les conséquences d’une évolution persistante')
s+=p('Lorsque les facteurs de chronicisation se cumulent, HUG2022 recommande un suivi rapproché et multimodal.','hug22-risque-chronicite')
s+=p('L’accompagnement tient compte des facteurs individuels, professionnels et socio-économiques qui peuvent entretenir le handicap.','hug22-risque-chronicite')
s+=p('La reprise du travail ou des activités ordinaires est facilitée selon les possibilités réelles du patient.','nice26-1-2-15')
s+=p('Des adaptations ergonomiques du poste de travail peuvent diminuer la kinésiophobie et les arrêts de travail.','hug22-evolution-suivi-retour')
s+=p('Après 4 semaines d’évolution défavorable malgré une prise en charge adéquate, la recherche d’alarmes et de facteurs de chronicisation est reprise, avec recours spécialisé si nécessaire.','hug22-evolution-suivi-retour')
s+=p('Une affection psychiatrique caractérisée peut nécessiter une prise en charge spécialisée, distincte de la simple présence de facteurs psychologiques associés à la douleur.','hug22-risque-chronicite')
s+=h('Conserver la date et la portée des recommandations')
s+=p('Le socle suisse présenté est la stratégie HUG2022 ; la recommandation NICE sur la thérapie manuelle a été amendée en 2026 et exige son association à des exercices.','hug22-prevention','nice26-1-2-7')
s+=p('NICE a retiré en juillet 2026 ses recommandations 1.2.13 et 1.2.14 parce qu’elles pouvaient être obsolètes, sans mise à jour priorisée dans ce domaine.','nice26-1-2-13','nice26-1-2-14')
s+=p('Ce retrait ne constitue pas en lui-même une preuve de nocivité de toute intervention psychologique ; la décision clinique reste reliée aux recommandations effectivement conservées et au cadre suisse décrit.','nice26-1-2-13','nice26-1-2-14','hug22-risque-chronicite')
save(12,s)

s=p('Une alarme neurologique impose une imagerie urgente et un avis neurochirurgical sans attendre une évolution sous antalgiques.','l81-hug-urgent-neuro')
s+=p('Une obstruction urinaire avec sepsis exige une antibiothérapie immédiate et une décompression urgente.','l81-eau-decompression')
s+=p('Une lombalgie commune se diagnostique cliniquement après recherche d’une cause spécifique et ne justifie pas d’imagerie systématique.','hug22-diagnostic-imagerie')
s+=p('Le traitement favorise l’activité adaptée et la récupération fonctionnelle, avec des médicaments sélectionnés selon leurs risques.','hug22-non-medicamenteux','nice26-1-2-22')
s+=p('Une fièvre nouvelle, un trouble neurologique ou une évolution défavorable oblige à réexaminer le diagnostic initial.','hug22-evolution-suivi-retour')
save(13,s)

s=h('Question — Une irradiation suffit-elle à diagnostiquer une hernie responsable ?')
s+=p('Réponse : non ; l’irradiation doit être caractérisée et confrontée aux signes irritatifs ou déficitaires dans un territoire cohérent.','hug22-classification','hug22-neurologie')
s+=p('Raison : les termes sciatalgie et sciatique n’ont pas la même portée, et la concordance clinique évite d’attribuer toute douleur à une image discale.','hug22-classification','hug22-diagnostic-imagerie')
s+=h('Question — Une douleur lombaire aiguë impose-t-elle une radiographie ?')
s+=p('Réponse : non si l’entretien et l’examen permettent de retenir une présentation commune sans argument pour une origine spécifique.','hug22-diagnostic-imagerie')
s+=p('Raison : la corrélation entre imagerie et symptômes est faible, et les explorations inutiles peuvent favoriser une interprétation anxiogène et des interventions sans bénéfice.','hug22-diagnostic-imagerie')
s+=h('Question — Une échographie sans fuite visible exclut-elle une rupture aortique ?')
s+=p('Réponse : non ; l’échographie identifie l’anévrisme mais peut manquer l’hémorragie rétropéritonéale.','l81-esvs-aaa-us')
s+=p('Raison : une suspicion persistante impose le contact vasculaire immédiat même lorsque l’échographie est indisponible ou non diagnostique.','l81-nice-aaa-urgence')
s+=h('Question — Peut-on traiter seulement l’infection lorsqu’un calcul obstrue avec sepsis ?')
s+=p('Réponse : non ; l’EAU demande l’antibiothérapie immédiate et la décompression urgente, puis le traitement définitif du calcul après résolution du sepsis.','l81-eau-decompression')
s+=p('Raison : le système collecteur infecté obstrué constitue une urgence urologique.','l81-eau-obstr-sepsis')
s+=h('Question — Le délai d’une semaine pour une IRM métastatique convient-il à une compression ?')
s+=p('Réponse : non ; l’IRM d’une suspicion de compression médullaire doit être réalisée au plus vite et toujours dans les 24 heures.','l81-nice-mscc-irm')
s+=p('Raison : le délai d’une semaine correspond à une suspicion de métastases rachidiennes sans signe de compression.','l81-nice-metastase-sans-mscc')
s+=h('Question — Une sténose visible explique-t-elle nécessairement la difficulté à marcher ?')
s+=p('Réponse : non ; il faut une claudication clinique compatible et considérer notamment les causes vasculaires et les polyneuropathies concurrentes.','l81-de2016-stenose-clinique')
s+=p('Raison : les modifications dégénératives peuvent accompagner le vieillissement, tandis que la responsabilité clinique exige une concordance.','l81-de2016-stenose-clinique')
s+=h('Question — Le paracétamol seul constitue-t-il le choix recommandé pour une lombalgie ?')
s+=p('Réponse : NICE ne recommande pas le paracétamol seul dans cette indication.','nice26-1-2-26')
s+=p('Raison : la stratégie privilégie les mesures actives et ne considère un opioïde faible, éventuellement associé au paracétamol, dans la lombalgie aiguë que sous des conditions restrictives.','hug22-non-medicamenteux','nice26-1-2-25')
s+=h('Question — Toute douleur décrite comme neuropathique justifie-t-elle un gabapentinoïde ?')
s+=p('Réponse : non ; NICE ne recommande pas cette classe pour la sciatique ni pour la lombalgie.','nice26-1-2-16','nice26-1-2-30')
s+=p('Raison : pour la sciatique, la recommandation repose sur l’absence de bénéfice global démontré et sur l’existence de dommages.','nice26-1-2-16')
s+=h('Question — Une dose mentionnée dans l’AIPS est-elle automatiquement adaptée à tout patient ?')
s+=p('Réponse : non ; la posologie de Brufen® est adaptée aux besoins et le principe reste la dose efficace minimale pendant la durée minimale nécessaire.','aips81-brufen-5')
s+=p('Raison : les contre-indications et les risques rénaux, digestifs, hépatiques et cardiovasculaires peuvent empêcher l’emploi ou modifier le rapport bénéfice-risque.','aips81-brufen-6','aips81-brufen-7-p3','aips81-brufen-7-p11')
s+=h('Question — Une clairance de créatinine inférieure à 30 ml/min permet-elle simplement de réduire Brufen® ?')
s+=p('Réponse : non ; l’insuffisance rénale grave définie ainsi figure dans les contre-indications du produit.','aips81-brufen-6')
s+=p('Raison : cette exclusion ne doit pas être confondue avec la prudence et la surveillance prévues dans les autres situations de limitation fonctionnelle.','aips81-brufen-6','aips81-brufen-7-p11')
s+=h('Question — Une récupération lente signifie-t-elle qu’il faut prolonger sans réexaminer ?')
s+=p('Réponse : non ; HUG2022 demande de reconsulter en l’absence d’amélioration significative après 4 à 7 jours ou devant un élément nouveau.','hug22-evolution-suivi-retour')
s+=p('Raison : l’évolution peut modifier l’hypothèse diagnostique, et l’absence d’évolution favorable après 4 semaines de prise en charge adéquate impose une nouvelle recherche des alarmes et des facteurs de chronicisation.','hug22-evolution-suivi-retour')
save(14,s)
