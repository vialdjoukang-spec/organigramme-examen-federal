import json,re
from pathlib import Path
B=Path(__file__).parent
packet=json.loads((B/'paquet.json').read_text())
R={f'h{i}':v for i,v in enumerate(['hug22-definition','hug22-epidemiologie','hug22-classification','hug22-anamnese','hug22-constantes','hug22-inspection','hug22-palpation','hug22-dynamique','hug22-neurologie','hug22-diagnostic-imagerie','hug22-risque-chronicite','hug22-non-medicamenteux','hug22-pharmaco-commune','hug22-pharmaco-radiculaire','hug22-evolution-suivi-retour','hug22-prevention'],1)}
R.update({'normal':'pa17-hugatlas-normal','def':'l81-de-nonspecifique','fract':'l81-hug-fracture','infect':'l81-hug-infection','cancer':'l81-hug-neoplasie','inflam':'l81-hug-axspa','aorte':'l81-esvs-aaa-clinique','aorte-urgence':'l81-nice-aaa-urgence','mscc':'l81-nice-metastase-urgences','mscc-irm':'l81-nice-mscc-irm','radic':'l81-hug-radiculaire','stenose':'l81-hug-stenose','img-gross':'pa814-esur-grossesse','img-rein':'pa814-esur-renal','img-allergie':'pa814-esur-allergie','img-autre':'pa814-esur-alternative','img-implant':'pa814-hug-implant','ib-meca':'aips81-brufen-mecanisme'})
for n in ['1-1-1','1-1-2','1-1-3','1-1-4','1-1-5','1-1-6','1-2-1','1-2-2','1-2-7','1-2-8','1-2-13','1-2-14','1-2-15','1-2-16','1-2-17','1-2-18','1-2-19','1-2-20','1-2-21','1-2-22','1-2-23','1-2-24','1-2-25','1-2-26','1-2-27','1-2-28','1-2-29','1-2-30','1-3-5','1-3-6']:
 R['n'+n]='nice26-'+n
for name,pre,ids in [('brufen','ib',[4,5,6,9,17,20]),('dafalgan','pa',[4,5,6,9,17,20]),('tramal','tr',[5,6,7,10,18,21])]:
 for i in ids:R[pre+str(i)]=f'aips81-{name}-{i}'
def ref(alias,name,needle):
 p=next(x for x in packet['passages']if name in x['id']and needle in x['texte']);R[alias]=p['id']
ref('ib-gastro','brufen','Des ulcérations, des hémorragies')
ref('ib-arretGI','brufen','En cas de survenue d’hémorragies') if any('En cas de survenue d’hémorragies'in x['texte']for x in packet['passages'])else ref('ib-arretGI','brufen',"En cas de survenue d'hémorragies")
ref('ib-rein','brufen',"Il convient d'être prudent pour les patients présentant une limitation")
ref('ib-peau','brufen','Brufen doit être interrompu')
ref('ib-deshyd','brufen',"Les patients souffrant d'une forte déshydratation")
ref('tr-resp','tramal','Comme pour tous les opioïdes')
ref('tr-addict','tramal',"L'utilisation répétée d'opioïdes")
ref('tr-seroto','tramal','Le syndrome sérotoninergique, une affection')
ref('tr-sevrage','tramal','Des cas de rechute')
ref('tr-association','tramal',"L'utilisation concomitante d'autres médicaments affectant le SNC")
ref('pa-foie','dafalgan',"Il est déconseillé de consommer de l'alcool")
ref('pa-inr','dafalgan','Anticoagulants:')
P={str(i):{'blocs':[],'fenetres':[],'tableaux':[]}for i in range(1,15)}
def b(n,t,a):P[str(n)]['blocs'].append([t,a])
def w(n,t,a):P[str(n)]['fenetres'].append([t,a])
def tab(n,t,c,r):P[str(n)]['tableaux'].append([t,c,r])

b(1,'Une définition clinique qui conserve le triage',[
['h1','La lombalgie désigne une douleur située entre la douzième côte et le pli fessier, souvent associée à une raideur ou une mobilité réduite.'],
['def','Elle est dite non spécifique lorsque son évaluation ne retient pas de corrélat pathoanatomique clairement établi.'],
['h10','Le diagnostic de lombalgie commune est posé après une anamnèse et un examen qui écartent une origine spécifique aux symptômes.'],
['n1-1-1','Ainsi, un changement du tableau impose de reconsidérer les diagnostics alternatifs plutôt que de conserver automatiquement une ancienne étiquette.'],
['h3','La distinction entre commune et spécifique concerne donc la nature du problème, tandis que les termes aiguë et chronique décrivent sa durée.'],
['h3','Dans la stratégie HUG, une évolution inférieure à quatre semaines définit habituellement la phase aiguë.'],
['h3','La phase subaiguë s’étend entre quatre et douze semaines, alors que la chronicité correspond à une persistance au-delà de trois mois.'],
['h3','Cependant, la trajectoire peut être récurrente et comporter des symptômes entre plusieurs épisodes.'],
['h10','La référence diagnostique est clinique et ne nécessite pas une imagerie systématique lorsque la présentation reste commune.'],
['h12','La douleur rapportée est reconnue comme réelle et subjective, ce qui exclut de la mettre en doute faute de lésion identifiée.']])
w(1,'Commune ne signifie pas diagnostic musculaire prouvé',[
['def','Le terme non spécifique décrit une absence de corrélat pathoanatomique clairement retenu pour expliquer cet épisode.'],
['h10','La corrélation entre anomalies radiologiques et clinique peut être faible, voire inexistante dans ce cadre.'],
['h10','Une anomalie sur une image ne suffit donc pas à remplacer le raisonnement clinique.'],
['h12','L’explication au patient associe une information compréhensible et un projet actif adapté à ses symptômes.']])
w(1,'Irradiation et atteinte radiculaire ne sont pas synonymes',[
['h3','Une lombo-sciatalgie comporte une irradiation au-delà du pli fessier dans un ou plusieurs membres inférieurs.'],
['h3','En revanche, des signes radiculaires concordants orientent vers une lombo-sciatique avec atteinte neurologique à caractériser.'],
['h3','La douleur antérieure de cuisse est décrite comme une lombo-cruralgie, avec ou sans syndrome radiculaire associé.'],
['h9','L’examen neurologique précise donc la portée de l’irradiation avant de conclure à une douleur commune.']])

b(2,'Fréquence suisse et dénominateurs',[
['h2','La stratégie HUG de 2022 rapporte une prévalence annuelle des lombalgies comprise entre 30 % et 40 % dans la population générale suisse.'],
['h2','Elle décrit également une expérience de lombalgie au cours de la vie chez plus de 80 % des personnes.'],
['h2','Une enquête suisse menée en 2020 retrouve cette expérience chez 88 % des personnes interrogées.'],
['h2','Cette enquête comprend 1041 personnes, avec un âge d’inclusion de 16 ans.'],
['h2','Ces estimations concernent donc la plainte lombalgique dans son ensemble et ne mesurent pas directement la seule lombalgie commune.'],
['h2','Dans la consultation de médecine générale, les HUG décrivent néanmoins une cause non spécifique dans environ 90 % des cas.'],
['def','La synthèse européenne distingue elle aussi une large majorité de lombalgies sans corrélat pathoanatomique clair.'],
['h4','Les facteurs à explorer comprennent notamment le tabac, l’obésité, les contraintes professionnelles et les difficultés psychologiques.'],
['h4','L’âge et le sexe féminin font également partie des éléments de terrain cités dans l’anamnèse HUG.'],
['h11','Toutefois, ces facteurs ne suffisent pas à expliquer individuellement chaque épisode ni à nier la douleur.']])
b(2,'Histoire naturelle et poids fonctionnel',[
['h15','Le taux de guérison d’une lombalgie aiguë commune est élevé dans les six semaines selon la stratégie HUG.'],
['h12','L’information doit cependant préciser que l’amélioration peut demander plusieurs jours ou plusieurs semaines.'],
['h12','La stratégie rapporte un risque de récidive de 20–45 % sur une année, avec une évolution généralement favorable.'],
['h11','La kinésiophobie, le catastrophisme, l’anxiété et l’humeur dépressive sont des facteurs modifiables de chronicisation particulièrement importants.'],
['h11','Lorsque ces facteurs s’accumulent, le suivi doit être plus rapproché et s’appuyer davantage sur plusieurs professionnels.'],
['h15','L’impact professionnel dépend du handicap fonctionnel et des sollicitations du poste plutôt que d’une douleur considérée isolément.'],
['h16','La prévention des récidives repose notamment sur l’activité physique et sur une éducation tenant compte des facteurs biopsychosociaux.']])
tab(2,'Chiffres : population, période et interprétation',['Chiffre rapporté','Population ou période','Interprétation utile'],[
[['h2','La prévalence annuelle est de 30–40 %.'],['h2','Le dénominateur est la population générale suisse décrite par HUG2022.'],['h2','Cette prévalence porte sur les lombalgies et ne correspond pas à une incidence de lombalgie commune.']],
[['h2','Plus de 80 % présentent une lombalgie au cours de leur vie.'],['h2','La stratégie décrit ici l’expérience de la plainte lombalgique.'],['h2','La période vie entière ne se compare pas directement à une prévalence annuelle.']],
[['h2','L’enquête suisse retrouve 88 % sur un effectif de 1041 personnes.'],['h2','Elle est menée en 2020 avec un âge d’inclusion de 16 ans.'],['h2','Son résultat ne fournit pas une fréquence de chaque diagnostic étiologique.']],
[['h2','Environ 90 % des causes sont décrites comme non spécifiques.'],['h2','Ce cadre est une consultation de médecine générale.'],['h2','Le contexte clinique doit rester visible lors de l’utilisation de cette proportion.']],
[['h12','Le risque de récidive rapporté est de 20–45 % sur une année.'],['h12','Cette estimation accompagne les conseils pour la lombalgie non spécifique.'],['h16','Elle motive l’activité physique et la prévention des épisodes ultérieurs.']]])
w(2,'Récidive et chronicité répondent à deux questions',[
['h3','Une récidive peut survenir dans une histoire comportant plusieurs crises et des symptômes variables entre elles.'],
['h3','La chronicité décrit en revanche une persistance des douleurs au-delà de trois mois dans la classification HUG.'],
['h15','La surveillance est donc adaptée à la trajectoire, au risque de chronicisation et à l’apparition d’un signe nouveau.']])

b(3,'Amorce : une douleur sans lésion causale obligatoire',[
['def','La lombalgie non spécifique ne désigne pas une lésion moléculaire ou tissulaire unique démontrée chez chaque patient.'],
['h4','La plupart des épisodes surviennent sans déclencheur particulier ou pendant un mouvement déjà réalisé de nombreuses fois.'],
['h4','Ainsi, l’histoire d’un effort ne prouve pas à elle seule une lésion anatomique précise.'],
['h1','L’épisode associe une douleur, une raideur et une diminution possible de la mobilité rachidienne.'],
['h8','Les mouvements de flexion et l’évaluation de leur amplitude documentent ensuite le retentissement mécanique du syndrome lombov ertébral.'],
['h12','Le vécu douloureux dépend aussi du contexte, des symptômes et des objectifs propres au patient.']])
b(3,'Développement et maintien : fonction, croyances et contexte',[
['h11','Une douleur importante, une forte limitation fonctionnelle et la peur de se mobiliser font partie des facteurs de chronicisation.'],
['h11','Le catastrophisme, l’anxiété et l’humeur dépressive doivent donc être recherchés comme des dimensions modifiables du parcours.'],
['h11','Les contraintes professionnelles et l’environnement socio-économique peuvent également contribuer à une résolution plus lente.'],
['h10','L’imagerie systématique peut exercer un effet nocebo et augmenter la chronicité, les coûts et les traitements invasifs sans bénéfice clinique.'],
['h12','En revanche, une information rassurante et la mobilisation précoce visent à préserver l’activité et à éviter une trajectoire passive.'],
['h12','Le repos au lit est décrit comme délétère, alors que la reprise des activités habituelles favorise une guérison plus rapide.'],
['h16','L’activité physique et les interventions éducatives peuvent ensuite réduire le nombre ou la durée des récidives.']])
b(3,'Mécanisme pharmacologique : une cible symptomatique distincte du diagnostic',[
['ib-meca','L’ibuprofène inhibe la synthèse des prostaglandines, ce qui contribue à ses effets analgésiques et anti-inflammatoires.'],
['ib-meca','Ce même mécanisme participe aussi aux effets digestifs, à la rétention hydrosodée et aux réactions bronchospastiques potentielles.'],
['h4','Cependant, un soulagement par un anti-inflammatoire ne démontre pas à lui seul une étiologie inflammatoire du dos.'],
['n1-2-22+n1-2-24','La décision de recourir à un AINS reste donc symptomatique, avec une dose minimale efficace et une durée courte.']])
tab(3,'Corrélation : perturbation, exploration et moyen d’action',['Perturbation ou facteur','Exploration clinique','Action et mécanisme recherché'],[
[['h1','La douleur peut réduire la mobilité et majorer la raideur.'],['h8','Les mouvements et la distance doigts-sol donnent un repère fonctionnel de suivi.'],['h12','L’activité adaptée et les exercices actifs cherchent à préserver le mouvement.']],
[['h11','La peur du mouvement et les croyances pessimistes favorisent une évolution prolongée.'],['h11','L’entretien et la stratification du risque précisent ces facteurs.'],['h12','L’éducation et l’encouragement à rester actif visent à modifier la trajectoire fonctionnelle.']],
[['h11','Le contexte professionnel peut compliquer le retour aux activités.'],['h11','Les exigences du poste et le soutien disponible sont recherchés.'],['h15','L’adaptation ergonomique et l’intervention au travail peuvent améliorer le parcours.']],
[['h10','Une lecture alarmante de l’imagerie peut participer à un effet nocebo.'],['n1-1-6','La question est de savoir si l’image modifierait réellement la conduite.'],['h10','L’absence d’imagerie routinière évite cette intervention sans bénéfice démontré dans le tableau commun.']],
[['ib-meca','Les prostaglandines participent aux manifestations douloureuses ciblées par l’ibuprofène.'],['n1-2-23','Le bilan clinique et les facteurs de risque conditionnent l’utilisation d’un AINS.'],['ib-meca','L’inhibition de leur synthèse produit un effet symptomatique avec ses risques propres.']]])
w(3,'Le mécanisme de maintien ne rend pas la douleur imaginaire',[
['h12','L’intensité exprimée par le patient est subjective et ne doit pas être remise en doute.'],
['h11','La recherche d’anxiété ou de kinésiophobie sert à identifier une possibilité d’action thérapeutique.'],
['h12','Elle complète donc le traitement actif au lieu de remplacer la reconnaissance de la plainte.'],
['n1-1-1','Une évolution inhabituelle impose toujours de reconsidérer les causes spécifiques.']])

b(4,'🚩 E1 — le danger vital passe avant le diagnostic commun',[
['aorte','Une douleur abdominale ou dorsale associée à un collapsus ou à une pâleur peut correspondre à une rupture d’anévrisme aortique.'],
['aorte-urgence','Si un anévrisme symptomatique ou rompu est envisagé, alors une échographie aortique au lit est proposée immédiatement.'],
['aorte-urgence','L’équipe vasculaire est contactée sans délai si l’anévrisme est montré ou reste suspect malgré une échographie non disponible ou non concluante.']])
b(4,'🚩 E2 — une compression neurologique change immédiatement la conduite',[
['h10+h9','Une suspicion de queue de cheval ou un déficit moteur d’alarme impose une imagerie rachidienne sans attendre et un avis neurochirurgical.'],
['h9','L’examen sacré recherche alors la sensibilité péri-anale et glutéale ainsi que le tonus du sphincter anal.'],
['mscc','Chez une personne ayant un cancer actuel ou antérieur, des signes de compression médullaire constituent une urgence oncologique.']])
b(4,'🚩 E3 et E4 — infection et fracture avant la réassurance',[
['infect','Fièvre nouvelle, frissons, douleurs nocturnes ou contexte infectieux font rechercher une spondylodiscite ou un abcès épidural.'],
['h10','Une telle suspicion nécessite une IRM urgente, et le scanner ne constitue qu’une discussion alternative si elle est indisponible.'],
['fract','Le terrain ostéoporotique, les stéroïdes et un traumatisme orientent également vers une fracture vertébrale.'],
['h10','La suspicion de fracture justifie un scanner selon la recommandation HUG, en tenant compte des critères de sévérité.'],
['n1-1-1','Ainsi, l’absence initiale d’argument spécifique doit être réévaluée lorsque le tableau se modifie.']])
tab(4,'Différentiels : discriminant, piège et action',['Diagnostic ou danger','Élément discriminant','Piège','Action'],[
[['aorte','🚩 Un anévrisme de l’aorte abdominale peut devenir symptomatique.'],['aorte','Douleur abdominale ou dorsale,collapsus et pâleur orientent l’évaluation vasculaire.'],['aorte-urgence','Une échographie non concluante ne suffit pas à abandonner une suspicion persistante.'],['aorte-urgence','L’échographie immédiate et la discussion vasculaire organisent la branche urgente.']],
[['h9+h10','🚩 Une compression des racines sacrées peut produire une queue de cheval.'],['h9','Le bilan recherche l’anomalie de sensibilité sacrée et du tonus anal.'],['h10','Le classement ancien en lombalgie commune ne protège pas d’un problème neurologique nouveau.'],['h10','Une imagerie sans délai est associée à l’avis neurochirurgical.']],
[['infect','🚩 Une infection disco-vertébrale ou épidurale peut expliquer la douleur.'],['infect','Le contexte infectieux,les gestes invasifs et l’immunosuppression orientent le bilan.'],['h10','Une amélioration antalgique ne remplace pas la recherche de cette cause suspectée.'],['h10','Une IRM urgente est demandée si l’infection rachidienne est envisagée.']],
[['fract','Une fracture vertébrale constitue une autre cause spécifique.'],['fract','Le traumatisme et la fragilité osseuse modifient la probabilité clinique.'],['h10','La douleur empêchant la mobilisation fait partie des critères de sévérité à considérer.'],['h10','Le scanner est indiqué dans l’évaluation d’une fracture suspectée.']],
[['h3+radic','Une hernie avec radiculopathie se distingue d’une irradiation non spécifique.'],['h9','Lasègue,force,sensibilité et réflexes recherchent une concordance radiculaire.'],['h3','Toute douleur descendant sous la fesse ne prouve pas une atteinte radiculaire.'],['h10+n1-1-6','Le bilan spécialisé et l’imagerie dépendent de l’évolution et de leur effet sur la conduite.']],
[['inflam','Une spondyloarthrite axiale constitue une branche inflammatoire distincte.'],['inflam','Début jeune,rythme inflammatoire et manifestations associées orientent l’évaluation.'],['h4','Le seul effet favorable d’un AINS ne confirme pas cette étiologie.'],['inflam','Le bilan ciblé et l’imagerie sacro-iliaque sont discutés avec la rhumatologie.']]])
w(4,'Requalifier le tableau quand il change',[
['n1-1-1','Un symptôme nouveau ou différent conduit à rechercher à nouveau les diagnostics alternatifs.'],
['h15','L’aggravation malgré un traitement bien conduit est également un signal d’alarme dans le suivi HUG.'],
['h10','Le raisonnement commun ne dispense donc jamais de l’action indiquée par une alarme apparue secondairement.']])

b(5,'Commencer par les questions qui changent le niveau d’urgence',[
['h9+h10','L’entretien recherche un trouble neurologique nouveau,car une alarme compressive impose une investigation immédiate.'],
['h9','Les questions périnéales et sphinctériennes accompagnent le bilan sacré lorsqu’une queue de cheval est suspectée.'],
['infect','La fièvre,les frissons,les gestes invasifs récents et les infections associées sont recherchés pour ne pas manquer une origine infectieuse.'],
['fract','Un traumatisme,une ostéoporose ou une corticothérapie orientent l’interrogatoire vers la possibilité fracturaire.'],
['cancer','Un antécédent néoplasique et une douleur qui ne s’améliore pas font reconsidérer l’origine tumorale.'],
['aorte','Une douleur abdominale ou dorsale avec signes circulatoires impose aussi de penser à une origine aortique.']])
b(5,'Décrire le symptôme et son effet sur l’activité',[
['h4','La localisation,l’irradiation,l’intensité et la durée sont précisées afin de caractériser l’épisode actuel.'],
['h4','Les circonstances d’apparition,les facteurs aggravants et le soulagement aident ensuite à distinguer les profils de douleur.'],
['h4','Un rythme mécanique se manifeste notamment en charge ou à l’effort et diminue avec l’arrêt de cet effort.'],
['h4','Un rythme inflammatoire est plutôt amélioré par l’activité,avec réveil nocturne tardif et raideur matinale prolongée.'],
['h4','Cependant,un mouvement déclencheur apparent ne démontre pas une lésion précise,puisque de nombreux épisodes surviennent pendant des gestes habituels.'],
['h3+h4','Les crises précédentes sont comparées à celle-ci pour distinguer récidive habituelle et présentation différente.'],
['h15','L’effet sur les tâches quotidiennes et professionnelles est exploré pour adapter la mobilisation et l’éventuel arrêt de travail.']])
b(5,'Explorer les facteurs de chronicisation sans les confondre avec les alarmes',[
['h11','La peur du mouvement,les croyances pessimistes,l’anxiété et l’humeur dépressive sont recherchées parce qu’elles peuvent ralentir la résolution.'],
['h11','Les attentes excessives envers les traitements et une attitude passive peuvent également influencer le parcours.'],
['h11','Les contraintes physiques,l’insatisfaction et le manque de soutien au travail sont donc abordés explicitement.'],
['h11','Les difficultés d’indemnisation,l’isolement et l’impossibilité d’adapter le poste complètent l’évaluation sociale.'],
['n1-1-2','Un outil comme STarT Back peut aider à stratifier le risque dès le premier contact pour un nouvel épisode.'],
['h11+n1-1-3','Le résultat conduit à moduler l’intensité du soutien plutôt qu’à réaliser une imagerie automatique.']])
tab(5,'Drapeaux : signification et action',['Donnée recherchée','Pourquoi elle compte','Action'],[
[['h9+h10','Un déficit moteur ou un trouble sacré apparaît.'],['h10','Une compression neurologique urgente doit être envisagée.'],['h10','L’imagerie est obtenue sans attendre avec un avis neurochirurgical.']],
[['infect','Fièvre ou frissons apparaissent dans un contexte rachidien suspect.'],['infect','Une infection disco-vertébrale ou épidurale peut être présente.'],['h10','L’hypothèse infectieuse retenue conduit à une IRM urgente.']],
[['aorte','La douleur s’accompagne de collapsus ou de pâleur.'],['aorte','Une rupture aortique entre dans le diagnostic différentiel vital.'],['aorte-urgence','Une échographie immédiate et le contact vasculaire sont requis si la suspicion persiste.']],
[['fract','Une douleur suit un traumatisme sur un terrain fragile.'],['fract','Le risque de fracture vertébrale change la branche diagnostique.'],['h10','Le bilan par scanner est organisé selon le contexte et les critères de sévérité.']],
[['h11','La personne évite tout mouvement par peur de se blesser.'],['h11','La kinésiophobie constitue un facteur modifiable de chronicisation.'],['h12','L’information et la progression des exercices sont adaptées à cette peur.']],
[['tr-association','Le patient prend déjà un dépresseur central ou un autre opioïde.'],['tr-association','Une association avec tramadol peut majorer sédation et dépression respiratoire.'],['tr-association','Les associations sont vérifiées avant tout recours conditionnel à cet antalgique.']]])
w(5,'STarT Back : un outil pronostique, pas une preuve de lésion',[
['h11','Le questionnaire complète une anamnèse détaillée pour quantifier le risque de chronicisation.'],
['n1-1-3','La stratification aide ensuite à choisir entre un soutien simple et une prise en charge plus intensive.'],
['h10','Elle ne constitue cependant pas une indication radiologique lorsque le tableau reste celui d’une lombalgie commune.']])

b(6,'Références normales avant la recherche des anomalies',[
['normal','La colonne possède naturellement une courbure en forme de S lorsqu’elle est observée de profil.'],
['h6','L’inspection doit donc distinguer ces courbures physiologiques d’un trouble statique majeur.'],
['h9','Dans la cotation motrice décrite par les HUG,la force normale correspond au grade M5.'],
['h9','Une marche sur talons et pointes sans parésie sévère n’exclut toutefois pas une faiblesse plus discrète.'],
['h9','Ainsi,le dépistage par la marche précède une exploration plus précise si la plainte ou les premiers résultats l’exigent.']])
b(6,'Constantes,posture,palpation et mobilité',[
['h5','La température fait partie des constantes indispensables à l’évaluation d’une douleur rachidienne.'],
['h6','L’inspection debout recherche la lordose,la cyphose,une scoliose et un déséquilibre antérieur important.'],
['h7','La contracture lombaire est généralement recherchée chez un patient couché sur le ventre et non en position debout.'],
['h7','La palpation des vertèbres et des espaces contribue ensuite à explorer une origine infectieuse ou inflammatoire possible.'],
['h8','Les flexions antéropostérieure et latérale recherchent un syndrome lombov ertébral ainsi qu’une kinésiophobie.'],
['h8','La distance doigts-sol et l’amplitude lombosacrée fournissent surtout des repères utiles pour le suivi.'],
['h8+h10','Une limitation de mobilité ne prouve cependant pas à elle seule une cause spécifique ou une indication d’imagerie.']])
b(6,'Examen neurologique des membres inférieurs',[
['h9','Si la douleur descend sous le pli fessier,les manœuvres de Lasègue direct et croisé recherchent une atteinte radiculaire.'],
['h9','Le test est positif s’il reproduit une douleur radiculaire entre 30° et 70° d’élévation de la jambe.'],
['h9','En revanche,une douleur localisée seulement dans le bas du dos ne satisfait pas cette définition.'],
['h9','Le Lasègue direct est décrit comme plus sensible,tandis que le Lasègue croisé est plus spécifique.'],
['h9','Le rétro-Lasègue se pratique en décubitus ventral ou latéral avec une extension passive de la hanche.'],
['h9','Il recherche une douleur antérieure de cuisse,compatible avec une atteinte radiculaire L2,L3 ou L4.'],
['h9','La force est ensuite recherchée de façon détaillée,avec examen séparé de l’extenseur propre du gros orteil.'],
['h9','Les réflexes rotuliens et achilléens complètent le bilan avec la sensibilité des cuisses,des mollets et des pieds.'],
['h9','Les mouvements contre résistance,contre gravité ou dans le plan du lit permettent de décrire le degré de déficit.'],
['h9+h10','Un déficit d’alarme conduit à la branche urgente plutôt qu’à une simple confirmation de lombalgie commune.']])
b(6,'Région sacrée et recherche d’une cause extra-rachidienne',[
['h9','En cas de suspicion de queue de cheval,la sensibilité péri-anale et glutéale et le tonus anal doivent être examinés.'],
['h10','Ce bilan clinique ne remplace pas l’imagerie immédiate recommandée devant des signaux neurologiques d’alerte.'],
['aorte','Le contexte abdominal et circulatoire est également examiné lorsque la plainte fait craindre une origine aortique.'],
['h4+n1-1-1','Enfin,l’examen est orienté vers les autres organes ou articulations lorsque l’entretien suggère une origine extra-rachidienne.']])
w(6,'Force : une cotation compréhensible et utile au suivi',[
['h9','Le grade M5 désigne une force normale,alors que M4 conserve un mouvement contre résistance modérée.'],
['h9','M3 correspond à un mouvement contre la gravité et M2 à un mouvement dans le plan du lit.'],
['h9','M1 désigne une contraction visible sans mouvement,tandis que M0 correspond à son absence.'],
['h9','Cette description précise l’examen au lieu de résumer toute faiblesse par le seul mot déficit.']])
w(6,'Un Lasègue lombaire douloureux peut rester négatif pour le signe radiculaire',[
['h9','La positivité exige la reproduction d’une douleur dans le trajet radiculaire et non une douleur uniquement lombaire.'],
['h9','Les racines recherchées par ces manœuvres sont L4,L5 et S1 dans la description HUG.'],
['h3+h9','L’interprétation est donc confrontée à la topographie et aux autres résultats neurologiques.']])

b(7,'7.1 Syndrome lombov ertébral du tableau commun',[
['h1','Ce tableau comporte une douleur lombaire,une raideur et une limitation possible des mouvements du rachis.'],
['h8','Le geste de recherche comprend les flexions antéropostérieure et latérale et une mesure fonctionnelle de mobilité.'],
['h10','Cependant,le caractère commun suppose que l’entretien et l’examen n’orientent pas vers une origine spécifique.']])
b(7,'7.2 Irradiation sans preuve radiculaire et syndrome radiculaire à distinguer',[
['h3','L’irradiation au-delà du pli fessier définit une lombo-sciatalgie sans imposer à elle seule une lésion radiculaire.'],
['h3+h9','Les signes irritatifs,la topographie et un éventuel déficit permettent ensuite de préciser un syndrome radiculaire.'],
['h9','Le Lasègue et l’examen de force,sensibilité et réflexes apportent les éléments physiques nécessaires à cette distinction.'],
['h10','Une atteinte neurologique d’alarme entraîne alors une autre priorité diagnostique et thérapeutique.']])
b(7,'7.3 Limitation fonctionnelle et risque de chronicisation',[
['h11','L’impact sur l’activité,la peur de se mobiliser et les croyances pessimistes constituent un ensemble de retentissement à explorer.'],
['h11','Le contexte de travail et l’environnement socio-économique peuvent aussi ralentir la résolution de l’épisode.'],
['n1-1-3','La réponse thérapeutique est donc stratifiée selon le risque et les besoins plutôt que limitée à la seule douleur.']])
b(7,'7.4 Claudication ou syndrome sacré : reconnaître un changement de branche',[
['stenose','Une douleur progressive à la marche,soulagée au repos ou assis,oriente vers une claudication neurogène.'],
['stenose','Son amélioration en diminuant la lordose lombaire apporte un élément clinique supplémentaire.'],
['h9+h10','Des signes sacrés ou un déficit moteur d’alarme imposent en revanche de rechercher une compression urgente.'],
['h10','Ces présentations ne sont donc pas absorbées automatiquement par le diagnostic de lombalgie commune.']])
tab(7,'Syndromes : fonction,signe physique et interprétation',['Syndrome','Manifestation fonctionnelle','Geste ou donnée physique'],[
[['h1','Le syndrome lombov ertébral décrit le retentissement rachidien douloureux.'],['h1','La personne rapporte douleur,raideur et gêne de mobilité.'],['h8','Les flexions et les mesures de mobilité servent à l’examen et au suivi.']],
[['h3','Une lombo-sciatalgie est une irradiation dans un membre inférieur.'],['h3','La douleur dépasse le pli fessier.'],['h9','Le bilan neurologique cherche si des signes radiculaires concordants sont présents.']],
[['h3+h9','Un syndrome radiculaire comporte des signes concordants.'],['h3','La douleur suit un territoire compatible et peut s’associer à un déficit.'],['h9','Lasègue,force,sensibilité et réflexes permettent de préciser cette concordance.']],
[['stenose','La claudication neurogène modifie le diagnostic différentiel.'],['stenose','La douleur apparaît avec la marche et diminue assis.'],['stenose','Le profil postural et le bilan clinique orientent ensuite l’exploration.']],
[['h11','Le retentissement fonctionnel peut favoriser la chronicisation.'],['h11','La peur du mouvement et les difficultés au travail sont explorées.'],['h11+n1-1-2','L’entretien et la stratification du risque complètent les mesures physiques.']]])
w(7,'Kinésiophobie : un facteur à rechercher dans le geste',[
['h11','La kinésiophobie correspond à la peur du mouvement citée parmi les facteurs modifiables importants.'],
['h8','L’examen dynamique permet notamment de l’identifier pendant l’évaluation de mobilité.'],
['h12','L’intensité et la progression des exercices sont ensuite adaptées à ce degré de peur.']])
w(7,'Claudication : préciser ce qui soulage la marche douloureuse',[
['stenose','Le profil décrit par les HUG associe une douleur de marche à un soulagement au repos et en position assise.'],
['stenose','La diminution de la lordose peut également améliorer le symptôme.'],
['h10','Ce profil appelle une analyse de cause spécifique et ne confirme pas une douleur commune par sa seule localisation.']])

R['queue']='pa17-lomb22-queue'
R['champ']='nice26-champ-et-date'
P['4']['blocs'][1][1].insert(0,['queue','Une rétention urinaire,une incontinence anale nouvelle ou une anesthésie en selle font rechercher le syndrome de la queue de cheval.'])
P['5']['blocs'][0][1].insert(0,['queue','Les questions demandent explicitement si la miction,la continence anale ou la sensibilité en selle a changé.'])
w(7,'Queue de cheval : nommer les signes qui déclenchent l’action',[
['queue','Les signes recherchés comprennent la rétention ou l’incontinence urinaire,l’incontinence anale nouvelle et l’anesthésie en selle.'],
['h9','L’examen vérifie ensuite la sensibilité péri-anale et glutéale ainsi que le tonus du sphincter anal.'],
['h10','La suspicion clinique déclenche une imagerie sans attendre et un avis neurochirurgical.']])

b(8,'Un diagnostic clinique après exclusion orientée',[
['h10','Le diagnostic de lombalgie commune repose sur une anamnèse et un examen physique qui ne retiennent pas d’origine spécifique.'],
['def','L’absence de corrélat pathoanatomique clair définit le cadre non spécifique et ne constitue pas une négation de la douleur.'],
['h1','La topographie lombaire et le retentissement sur la mobilité décrivent la plainte sans en préciser automatiquement la cause.'],
['n1-1-1','Les causes tumorales,infectieuses,traumatiques et inflammatoires sont reconsidérées lorsque le contexte ou un symptôme change.'],
['h9+h10','Un signe radiculaire ou neurologique est analysé pour lui-même et peut faire sortir du parcours commun.'],
['h10','Une fois l’évaluation compatible avec ce cadre,aucun examen radiologique ou de laboratoire n’est recommandé systématiquement.'],
['n1-1-6','Dans un contexte spécialisé,l’imagerie est envisagée seulement si son résultat est susceptible de modifier la prise en charge.'],
['h3','La durée de l’épisode est ensuite décrite séparément de son caractère spécifique ou non spécifique.'],
['n1-1-2','Enfin,STarT Back aide à stratifier le risque pronostique et ne remplace pas le diagnostic étiologique.']])
tab(8,'Éléments du diagnostic : ce qui suffit et ce qui ne suffit pas',['Élément','Rôle clinique','Limite'],[
[['h1','La douleur est située entre la douzième côte et le pli fessier.'],['h1','Cette topographie définit la plainte lombalgique.'],['h4','Elle ne distingue pas seule une origine rachidienne d’une cause extra-rachidienne.']],
[['h10','L’entretien et l’examen ne retiennent pas d’origine spécifique.'],['h10','Cette analyse permet de poser le diagnostic clinique commun.'],['n1-1-1','Un signe nouveau impose cependant de reprendre le diagnostic différentiel.']],
[['h3','La durée précise une phase aiguë,subaiguë ou chronique.'],['h3','Elle caractérise la trajectoire et l’évolution de l’épisode.'],['h10','Elle ne remplace pas la recherche d’un signe d’alarme.']],
[['h9','Le Lasègue peut reproduire une douleur radiculaire.'],['h9','Son résultat s’interprète avec force,sensibilité et réflexes.'],['h9','Une douleur seulement lombaire pendant le test ne suffit pas à le rendre positif.']],
[['h11','STarT Back complète le repérage du risque de chronicisation.'],['n1-1-3','La stratification adapte l’intensité du soutien proposé.'],['h10','Elle ne constitue pas une preuve de lésion ni une indication radiologique automatique.']]])
w(8,'Une image anormale ne crée pas automatiquement une cause',[
['h10','Les HUG soulignent la faible corrélation possible entre clinique et anomalies radiologiques.'],
['n1-1-6','Le résultat attendu d’un examen doit donc être lié à une décision thérapeutique ou diagnostique utile.'],
['h10','Une exploration systématique dans le tableau commun peut augmenter les coûts et les interventions sans bénéfice clinique.']])

b(9,'9.a La référence est l’évaluation clinique',[
['h10','Pour une lombalgie commune,l’examen décisif reste l’association de l’anamnèse et de l’examen physique.'],
['h10','Après exclusion orientée d’une origine spécifique,une radiographie et un bilan de laboratoire ne sont pas systématiquement recommandés.'],
['n1-1-5','Même un adressage pour avis spécialisé ne signifie pas qu’une imagerie sera nécessaire.'],
['n1-1-6','La question prescriptive est donc de savoir si son résultat changera effectivement la conduite.']])
b(9,'9.b Première intention : aucune image routinière,mais une vraie stratégie de réévaluation',[
['h10','Une imagerie demandée sans indication clinique ne fournit pas d’information pronostique utile pour le tableau commun.'],
['h10','Elle peut au contraire renforcer un effet nocebo et augmenter les traitements invasifs.'],
['h15','Le suivi repose donc sur l’évolution des symptômes,de la fonction et sur le repérage d’une nouvelle alarme.'],
['h15','L’absence d’amélioration significative dans les quatre à sept jours sous le traitement prescrit motive une nouvelle consultation.'],
['h15','Un élément nouveau,tel qu’une fièvre ou un trouble neurologique,justifie aussi de reconsulter.']])
b(9,'9.c Adapter la modalité si une nouvelle hypothèse justifie réellement l’examen',[
['h10','Devant une alarme neurologique,l’imagerie est obtenue sans attendre,si possible par IRM et au minimum par scanner.'],
['h10','Une infection rachidienne suspectée appelle une IRM urgente ; le scanner est moins sensible dans les premières semaines.'],
['h10','En présence d’une fracture suspectée,le scanner est indiqué selon les HUG.'],
['n1-1-1','Ces examens répondent alors à une nouvelle hypothèse spécifique et non à une confirmation routinière du diagnostic commun.']])
b(9,'9.d Bilan ciblé et avis spécialisé selon l’évolution',[
['h10','Une origine infectieuse,tumorale ou inflammatoire suspectée peut justifier un bilan de paramètres inflammatoires ciblé.'],
['h10','Ce bilan peut comprendre la vitesse de sédimentation et la protéine C-réactive.'],
['h10','En cas de suspicion tumorale sans fracture,une IRM est discutée en milieu ambulatoire ou hospitalier selon le contexte clinique.'],
['h15','Sans évolution favorable après quatre semaines,les signes d’alarme et les facteurs de chronicisation sont recherchés à nouveau.'],
['h15','Un avis rhumatologique ou de réadaptation peut alors être nécessaire,notamment pour initier une approche spécialisée et multidisciplinaire.']])
tab(9,'Interprétation : résultat,signification et décision',['Résultat ou situation','Signification','Décision'],[
[['h10','L’examen reste compatible avec une lombalgie commune sans alarme.'],['h10','Une origine spécifique n’est pas retenue à cette évaluation.'],['h10','L’imagerie et le laboratoire ne sont pas ajoutés systématiquement.']],
[['h9+h10','Un déficit moteur d’alarme ou des signes sacrés sont retrouvés.'],['h10','La priorité devient une compression neurologique possible.'],['h10','Une imagerie sans attendre est associée à l’avis neurochirurgical.']],
[['infect','Le contexte fait suspecter une infection vertébrale.'],['h10','L’hypothèse nécessite une exploration étiologique urgente.'],['h10','Une IRM est demandée en urgence pour spondylodiscite ou abcès épidural suspecté.']],
[['fract','La clinique et le terrain font envisager une fracture.'],['h10','L’hypothèse fracturaire remplace la simple conduite commune.'],['h10','Le scanner est organisé selon l’évaluation de gravité.']],
[['n1-1-6','Un examen spécialisé envisagé ne changerait pas le traitement.'],['n1-1-6','Le bénéfice attendu de cette image est insuffisant pour la recommander dans ce cadre.'],['n1-1-6','La décision d’imagerie est reconsidérée avec son objectif clinique.']]])
tab(9,'Situations particulières : aucune modalité automatique',['Situation','Adaptation','Question conservée'],[
[['img-gross','Une grossesse est connue et une injection IRM serait envisagée.'],['img-gross','Le gadolinium est réservé à une indication très forte,avec la plus faible dose possible d’un agent macrocyclique.'],['h10','Une lombalgie restée commune ne crée pas à elle seule cette indication.']],
[['champ','Le patient relève d’un âge pédiatrique.'],['champ','Le cadre NICE consulté concerne les personnes de plus de16ans et ne doit pas être transposé aveuglément.'],['n1-1-1','L’évaluation clinique et l’hypothèse diagnostique restent adaptées au patient.']],
[['img-rein','Le DFGe est inférieur à30ml/min/1,73m² avant une injection iodée intraveineuse.'],['img-rein+img-autre','Le risque de ce contraste est réévalué et une méthode sans produit iodé peut être discutée.'],['h10','La fonction rénale ne transforme pas une lombalgie commune en indication d’imagerie.']],
[['img-allergie','Une hypersensibilité à un produit de contraste est connue.'],['img-allergie','Une autre modalité ou une étude sans injection est envisagée si son rendement suffit.'],['n1-1-6','Le choix doit conserver l’information nécessaire à une décision utile.']],
[['img-implant','Un implant ou un corps métallique peut modifier la possibilité d’IRM.'],['img-implant','Le dispositif exact est signalé avant l’examen et évalué avec la radiologie.'],['h10','En cas d’urgence neurologique,l’exploration reste à organiser sans délai avec une alternative adaptée.']]])
w(9,'Ne pas attribuer un chiffre biologique normal universel au tableau commun',[
['h10','La stratégie ne demande pas de laboratoire systématique quand l’évaluation clinique retient une lombalgie commune.'],
['h10','Les paramètres inflammatoires répondent en revanche à une hypothèse infectieuse,tumorale ou inflammatoire.'],
['n1-1-1','Le changement d’hypothèse précède donc la prescription et l’interprétation du résultat.']])

b(10,'Un parcours dont chaque branche mène à une décision',[
['aorte+aorte-urgence','Si la douleur fait suspecter un anévrisme symptomatique ou rompu,alors l’échographie immédiate et le contact vasculaire priment.'],
['queue+h10','Si une rétention urinaire,une incontinence anale nouvelle ou une anesthésie en selle apparaît,alors la compression sacrée est évaluée sans attendre.'],
['h10','Si un déficit moteur d’alarme est présent,alors une imagerie urgente et un avis neurochirurgical sont organisés.'],
['infect+h10','Si une spondylodiscite ou un abcès épidural est suspecté,alors une IRM urgente est demandée.'],
['fract+h10','Si une fracture est suspectée sur le terrain ou la clinique,alors le bilan par scanner est indiqué.'],
['n1-1-1','Si le contexte oriente vers cancer ou inflammation,alors un bilan spécifique remplace le parcours de douleur commune.'],
['h10','Si l’anamnèse et l’examen écartent une origine spécifique,alors le diagnostic commun est clinique sans imagerie routinière.'],
['n1-1-2+n1-1-3','Si le risque de mauvaise évolution est faible,alors information et soutien à l’autogestion peuvent rester simples.'],
['n1-1-3','Si le risque pronostique est plus élevé,alors une aide plus intensive et adaptée est envisagée.'],
['h12','Si la mobilisation est limitée,alors les conseils et les exercices sont progressifs et adaptés à la douleur et à la peur.'],
['n1-2-22+n1-2-24','Si un AINS est retenu,alors les risques individuels sont évalués et l’exposition est minimale.'],
['n1-2-25','Si un opioïde faible est envisagé dans un épisode aigu,alors il faut vérifier contre-indication,intolérance ou inefficacité des AINS.'],
['h15','Si l’amélioration n’est pas significative dans les quatre à sept jours ou si un symptôme nouveau apparaît,alors la personne reconsulte.'],
['h15','Si l’évolution reste défavorable après quatre semaines,alors le triage et les facteurs de chronicisation sont réévalués.']])
w(10,'Le suivi n’attend pas une échéance quand une alarme survient',[
['h15','Une fièvre,un trouble neurologique ou une aggravation malgré les soins justifie une nouvelle évaluation.'],
['h10','Les signes neurologiques d’alarme disposent alors de leur branche d’imagerie sans attendre.'],
['n1-1-1','Un diagnostic commun initial reste donc révisable selon l’évolution.']])

b(11,'11.A But fonctionnel et pronostic annoncé avec ses limites',[
['h12','Le premier objectif est de préserver une mobilité adaptée et de reprendre les activités habituelles plutôt que d’imposer un repos au lit.'],
['n1-2-1','L’information est ajustée aux capacités et aux besoins de la personne pour soutenir l’autogestion à chaque étape.'],
['h15','Le pronostic de la lombalgie aiguë commune est favorable,avec un taux de guérison élevé dans les six semaines.'],
['h12','Cette attente ne constitue cependant pas une promesse de disparition immédiate de toute douleur.'],
['h12','Les objectifs sont définis avec le patient selon son handicap,ses préférences et les activités qu’il cherche à retrouver.']])
b(11,'11.B D’abord informer,mobiliser et organiser les moyens actifs',[
['h12','La réassurance explique le caractère habituellement réversible de la lombalgie non spécifique et la possibilité d’une amélioration progressive.'],
['h12','La douleur est reconnue comme réelle et son intensité n’est pas contestée.'],
['h12','La poursuite des activités et une mobilisation précoce sont encouragées,même si une douleur persiste.'],
['h12','La physiothérapie doit comporter une partie active avec des exercices adaptés et pratiqués aussi à domicile.'],
['h12','Les étirements,l’endurance,le renforcement et la stabilisation peuvent être adaptés aux symptômes et aux préférences.'],
['h12','L’intensité progresse selon le degré de kinésiophobie plutôt qu’en imposant une reprise uniforme.'],
['n1-2-7','NICE réserve la thérapie manuelle à un ensemble thérapeutique comprenant des exercices.'],
['h12','La chaleur peut apporter un soulagement à court terme et complète les moyens non médicamenteux.'],
['n1-2-15','La reprise du travail ou des activités ordinaires doit être facilitée selon le contexte fonctionnel.']])
b(11,'Médicaments : un recours conditionnel et une exposition minimale',[
['h13','Un traitement médicamenteux peut compléter les mesures actives ou être proposé en cas de réponse insuffisante à celles-ci.'],
['h13','Les HUG citent les AINS comme premier choix médicamenteux,tout en rappelant leur bénéfice modeste et leurs effets indésirables.'],
['n1-2-22+n1-2-23','Avant un AINS oral,les risques digestifs,hépatiques,cardiovasculaires et rénaux sont appréciés avec les facteurs individuels.'],
['n1-2-23+n1-2-24','La surveillance et une éventuelle gastroprotection sont discutées,avec la dose efficace la plus basse et la durée la plus courte.'],
['n1-2-25','Un opioïde faible ne se discute dans une lombalgie aiguë que si un AINS est contre-indiqué,mal toléré ou inefficace.'],
['n1-2-27+n1-2-28','Les opioïdes ne sont donc pas proposés de façon routinière dans l’aigu et ne sont pas recommandés pour la lombalgie chronique.'],
['n1-2-26','Le paracétamol seul n’est pas proposé comme traitement de la lombalgie selon NICE.'],
['n1-2-25','Il peut être associé à un opioïde faible dans le cadre aigu conditionnel défini par cette recommandation.'],
['n1-2-29+n1-2-30','NICE ne recommande pas les antidépresseurs ni les gabapentinoïdes pour la lombalgie.'],
['h13','Les benzodiazépines ne sont pas recommandées par les HUG en raison du risque de dépendance.']])
tab(11,'Médicaments : spécialité,forme,dose et condition',['Référence AIPS','Dose et voie documentées','Durée et condition','Sécurité majeure'],[
[['ib4+ib17+ib20','Brufen® contient de l’ibuprofène ; autorisations45031 et49669,notice de décembre2024.'],['ib5','Dans les affections rhumatismales,la dose initiale adulte est de1200–1800mg/jour répartie en plusieurs prises.'],['ib5+n1-2-24','L’exposition reste aussi courte que possible ; la dose est individualisée et l’efficacité minimale recherchée.'],['ib6','Insuffisance rénale grave,ulcère ou hémorragie digestifs et autres contre-indications doivent être vérifiés.']],
[['ib4','La notice Brufen mentionne explicitement les lombalgies et les névralgies secondaires aux lésions discales.'],['ib5','Une dose d’entretien de600–1200mg/jour suffit chez de nombreux patients ; certains cas nécessitent2400mg/jour.'],['ib5','Ces données quotidiennes ne créent pas une prise unique ou un intervalle non écrits dans la notice.'],['ib6+ib9','Les contre-indications et restrictions de grossesse ou d’allaitement restent celles de la spécialité.']],
[['tr5+tr18+tr21','Tramal® est un recours antalgique conditionnel ; autorisations40858,40859,43787 et43788,notice d’avril2025.'],['tr6','Pour les capsules orales chez l’adulte,la dose est de50–100mg toutes les4–6heures.'],['tr6','La dose totale quotidienne de400mg ne doit pas être dépassée,sauf circonstances particulières indiquées dans la notice.'],['tr7+tr-resp','Les contre-indications et le risque de dépression respiratoire doivent être évalués avant prescription.']],
[['tr6','La stratégie du traitement par Tramal est définie avec le patient avant le début.'],['tr6','La dose antalgique efficace la plus faible est généralement choisie.'],['tr6','Le traitement ne dure pas plus longtemps que nécessaire et son besoin est réévalué régulièrement.'],['tr-addict+tr-association','Tolérance,dépendance et associations avec des dépresseurs centraux imposent une surveillance spécifique.']],
[['pa4+pa17+pa20','Dafalgan® est documenté par les autorisations47503,47505 et56318,notice de juillet2026.'],['pa5','Pour le comprimé pelliculé de1g chez l’adulte de plus de50kg,la dose unitaire est de1g,avec intervalle de4–8heures.'],['pa5+n1-2-25+n1-2-26','Le maximum est de4g/jour avant adaptations ; cette référence ne justifie pas une monothérapie de lombalgie.'],['pa5+pa6','Poids,fonction hépatique,fonction rénale et autres produits contenant du paracétamol modifient sa sécurité.']]])
w(11,'Urgence — conduite chronologique',[
['aorte+aorte-urgence','D’abord,une suspicion aortique symptomatique ou rompue fait organiser l’échographie immédiate et la discussion vasculaire.'],
['queue+h10','Une alarme sacrée ou motrice conduit ensuite à l’imagerie rachidienne sans attendre,associée à l’avis neurochirurgical.'],
['mscc','Un cancer connu avec signes de compression déclenche la filière d’urgence oncologique.'],
['infect+h10','Si une infection rachidienne est suspectée,son IRM est demandée en urgence.'],
['fract+h10','Une fracture suspectée dispose de son bilan propre,avec recherche des critères de sévérité.'],
['h10','Ces branches doivent être traitées avant de poursuivre le projet actif d’une lombalgie qualifiée de commune.']])
w(11,'Ibuprofène : prendre en compte les situations particulières',[
['ib6','Brufen est contre-indiqué en cas d’hypersensibilité ou de réaction allergique antérieure à l’acide acétylsalicylique ou à d’autres AINS.'],
['ib6','Les ulcères ou hémorragies digestifs actifs ou répétés dans l’anamnèse font partie des contre-indications.'],
['ib6','Les maladies inflammatoires intestinales actives ou avérées et les troubles hépatiques graves contre-indiquent également ce traitement.'],
['ib6','Une clairance de la créatinine inférieure à30ml/min constitue une contre-indication rénale.'],
['ib6','Une insuffisance cardiaque grave NYHAIII–IV ou une douleur après pontage coronarien constituent aussi des contre-indications.'],
['ib-deshyd','Une forte déshydratation nécessite une réhydratation avant traitement et une surveillance étroite.'],
['ib-rein','La fonction rénale est contrôlée chez les patients présentant un risque cardiaque,hépatique ou rénal.'],
['ib5','Les comprimés sont avalés entiers avec de l’eau et les prises ultérieures se font après les repas.'],
['ib5','Les comprimés de400mg ou600mg et les granulés ne doivent pas être utilisés avant12ans en raison de leur dosage.'],
['ib5','Les comprimés de200mg ne sont pas indiqués avant6ans,ce qui ne crée pas un protocole pédiatrique de lombalgie.']])
w(11,'Grossesse et allaitement : conserver les formulations de la notice Brufen',[
['ib9','Aux premier et deuxième trimestres,l’ibuprofène est à éviter sauf nécessité clairement établie,avec dose et durée minimales.'],
['ib9','À partir de la vingtième semaine,des troubles rénaux fœtaux et un oligoamnios peuvent survenir sous AINS.'],
['ib9','Une surveillance échographique du liquide amniotique et du cœur fœtal est envisagée si Brufen se prolonge au-delà de48heures.'],
['ib9','La survenue d’un oligoamnios ou d’un rétrécissement du canal artériel impose l’arrêt de Brufen et le suivi indiqué.'],
['ib6+ib9','L’ibuprofène est contre-indiqué au troisième trimestre et n’est pas recommandé pendant le travail et l’accouchement.'],
['ib9','La notice demande de ne pas prendre l’ibuprofène pendant l’allaitement ; si le traitement est indispensable,le nourrisson doit être sevré.']])
w(11,'Tramadol : adaptations,contre-indications et arrêt',[
['tr7','L’intoxication aiguë par alcool,hypnotiques,opioïdes ou psychotropes contre-indique Tramal.'],
['tr7','Une épilepsie insuffisamment contrôlée ou un traitement par inhibiteur de la MAO actuel ou récent constituent d’autres contre-indications.'],
['tr7','La période à considérer après un inhibiteur de la MAO est de14jours dans la notice.'],
['tr6','Une insuffisance rénale ou hépatique ralentit l’élimination et peut nécessiter d’allonger les intervalles entre les doses.'],
['tr6','Après75ans,l’élimination peut être ralentie même sans atteinte rénale ou hépatique manifeste.'],
['tr6','Les capsules ne sont pas utilisées avant12ans en raison de leur dosage.'],
['tr10','Le tramadol ne doit pas être administré pendant la grossesse,sauf nécessité absolue.'],
['tr10','Tramal ne doit pas être utilisé pendant l’allaitement ; une administration unique ne nécessite généralement pas son interruption.'],
['tr6+tr-sevrage','Si le traitement devient inutile,une diminution progressive peut éviter les symptômes de sevrage.'],
['tr6','Une réponse antalgique insuffisante conduit aussi à envisager tolérance et progression de la maladie sous-jacente.']])
w(11,'Paracétamol : adaptation de forme,poids,foie et rein',[
['pa5','Le comprimé pelliculé de1g ne doit pas être pris par une personne de moins de50kg.'],
['pa5','Le sillon du comprimé pelliculé n’est pas prévu pour réduire la dose de moitié.'],
['pa5','Les autres médicaments sont vérifiés pour éviter une accumulation involontaire de paracétamol.'],
['pa5','Chez les patients à risque hépatique,alcooliques chroniques,cachectiques,dénutris ou déshydratés,la dose peut nécessiter une réduction.'],
['pa5','Dans les situations hépatiques et nutritionnelles précisées par la notice,le maximum quotidien ne dépasse pas2g.'],
['pa5','Pour une clairance de10–50ml/min,l’intervalle est de6heures et le maximum quotidien de3000mg.'],
['pa5','Pour une clairance inférieure à10ml/min,l’intervalle est de8heures et le maximum quotidien de2000mg.'],
['pa6','Une atteinte hépatique sévère,une hépatite aiguë et la maladie de Gilbert figurent parmi les contre-indications.'],
['pa9','Pendant la grossesse,une nécessité clinique permet l’usage avec la dose efficace minimale et l’exposition la plus brève et espacée possible.'],
['pa9','Le paracétamol est considéré comme compatible avec l’allaitement,mais la notice conserve une recommandation de prudence.']])
b(11,'11.C Surveillance : clinique d’abord,puis sécurité du traitement retenu',[
['h15','L’apparition d’une fièvre ou d’un trouble neurologique impose de revoir la situation clinique.'],
['h15','Une aggravation malgré une prise en charge bien conduite constitue aussi un signal d’alarme.'],
['h15','Si l’amélioration n’est pas significative dans les quatre à sept jours sous le traitement prescrit,une nouvelle consultation est proposée.'],
['h15','Les facteurs de chronicisation justifient un suivi multimodal plutôt qu’une simple attente.'],
['ib-arretGI','Une hémorragie digestive ou un ulcère survenant sous Brufen impose d’interrompre le médicament.'],
['ib-peau','Un rash,une lésion muqueuse ou un autre signe d’hypersensibilité sous Brufen impose également son arrêt.'],
['tr-resp','Sous tramadol,la respiration et la sédation sont particulièrement surveillées au début et après augmentation de dose.'],
['tr-addict','La surveillance recherche également tolérance,signes de mésusage et dépendance.'],
['pa-foie','La consommation d’alcool est déconseillée sous paracétamol,car elle peut majorer la toxicité hépatique.'],
['pa-inr','Une prise quotidienne prolongée de paracétamol avec un anticoagulant coumarinique justifie une surveillance rapprochée de l’INR.']])
w(11,'Interactions : ne pas transformer un recours antalgique en association dangereuse',[
['ib-gastro','Les complications digestives des AINS peuvent survenir sans symptômes précurseurs.'],
['ib-rein','Une limitation cardiaque,hépatique ou rénale impose une prudence particulière avec l’ibuprofène.'],
['tr-association','Le tramadol associé à d’autres dépresseurs centraux peut produire dépression respiratoire,hypotension,sédation majeure ou coma.'],
['tr-seroto','Un syndrome sérotoninergique potentiellement mortel peut aussi survenir avec le tramadol seul ou associé à d’autres agents sérotoninergiques.'],
['tr6','La stratégie est donc réévaluée régulièrement avec l’intensité douloureuse,le besoin de poursuite et les effets indésirables.']])
b(11,'Volet professionnel,social et accès aux soins',[
['h15','L’arrêt de travail dépend du handicap et des sollicitations professionnelles,et doit être utilisé avec précaution.'],
['h15','Dans le parcours HUG,un arrêt nécessaire est limité initialement à trois à cinq jours et prolongé seulement après réévaluation.'],
['h15','L’adaptation du poste peut réduire la kinésiophobie et les arrêts de travail.'],
['h11','Les difficultés d’indemnisation,de remplacement au travail ou de soutien social sont donc recherchées avec les obstacles physiques.'],
['h12','La stratégie HUG de2022 distingue l’ostéopathie non remboursée par l’assurance de base et sa consultation médicale de thérapie manuelle couverte par celle-ci.'],
['h12','Cette distinction permet de discuter les moyens proposés avec le patient au lieu de supposer une couverture identique de toute thérapie manuelle.']])
b(11,'11.D Pronostic,amélioration et continuité de sortie',[
['h15','Une récupération favorable est fréquente dans les six semaines de l’épisode aigu commun.'],
['h12','La reprise progressive des activités soutient ce parcours et ne nécessite pas d’imposer une immobilité jusqu’à disparition complète des douleurs.'],
['h15','Un patient au pronostic favorable ne nécessite pas toujours une consultation programmée systématique.'],
['h15','Cependant,le risque de chronicisation et les signes nouveaux modifient ce choix de suivi.'],
['h15','À quatre semaines sans évolution favorable,le diagnostic et les facteurs de chronicisation doivent être réévalués.'],
['h16','L’amélioration d’un épisode ne supprime pas le risque de récidive,ce qui justifie de préserver activité et éducation.']])
tab(11,'Critères pratiques de sortie : vérifier chaque élément',['Élément à vérifier','Critère pratique','Consigne ou relais'],[
[['h10','Le diagnostic reste compatible avec une lombalgie commune après le triage.'],['h10','Une cause spécifique n’est pas retenue à l’évaluation actuelle.'],['n1-1-1','Tout signe nouveau ou différent permet de rouvrir le diagnostic différentiel.']],
[['h12','Le projet de mobilité est compris.'],['h12','La personne dispose de conseils pour rester active selon sa douleur et ses capacités.'],['h12','Le repos au lit n’est pas utilisé comme traitement de routine.']],
[['h12+n1-2-1','Les informations d’autogestion sont adaptées.'],['h12','Les facteurs aggravants ou soulageants et les stratégies quotidiennes ont été expliqués.'],['n1-2-1','Les conseils correspondent aux besoins et aux possibilités de la personne.']],
[['h15','Le retour d’alarme est connu.'],['h15','Fièvre,trouble neurologique ou évolution défavorable motivent une nouvelle consultation.'],['h10','Une alarme neurologique suit sa branche d’imagerie sans attendre.']],
[['h15','Le délai d’évaluation de la réponse est expliqué.'],['h15','L’absence d’amélioration significative dans les quatre à sept jours sous traitement appelle une reconsultation.'],['h15','Un suivi plus structuré est prévu si le risque de chronicisation le justifie.']],
[['tr6+ib5','Le traitement retenu possède un objectif et une durée réévaluables.'],['tr6+ib5','Le besoin de poursuite est vérifié et l’exposition médicamenteuse reste minimale.'],['tr6','Si un opioïde a été utilisé,sa poursuite et son arrêt sont discutés avec le prescripteur.']],
[['h15','La reprise professionnelle est adaptée.'],['h15','Le handicap et les contraintes du poste sont pris en compte.'],['h15','Un arrêt de travail initial n’est prolongé qu’après une nouvelle évaluation.']]])
w(11,'Programmes psychologiques : conserver la date et la portée de chaque référentiel',[
['h11','Les HUG recherchent les facteurs psychologiques et recommandent une prise en charge conjointe en présence d’une véritable maladie psychiatrique.'],
['n1-2-13+n1-2-14','NICE a retiré en juillet2026 ses anciennes recommandations sur les thérapies psychologiques et les programmes physiques et psychologiques combinés.'],
['n1-2-13+n1-2-14','La surveillance les jugeait possiblement périmées,sans qu’une actualisation soit priorisée dans ce domaine.'],
['n1-2-7','La thérapie manuelle reste envisagée dans un programme comprenant l’exercice selon la recommandation amendée en2026.'],
['h11','La recherche d’anxiété,de dépression et de peur du mouvement garde ainsi sa place dans l’évaluation HUG du patient.']])

b(12,'Prévention primaire : promouvoir une activité régulière sans promesse universelle',[
['h16','La lombalgie non spécifique est une affection complexe et seules certaines interventions permettent de réduire les récidives.'],
['h15+h16','L’information favorise une activité physique régulière et des habitudes préservant le mouvement.'],
['h12','Les conseils ergonomiques peuvent porter sur les gestes répétés,le port de charge ou l’organisation du poste.'],
['h12','L’enseignement apprend aussi à adapter les activités quotidiennes pendant une période douloureuse.'],
['h16','Les mesures sont donc expliquées comme un soutien au fonctionnement et à la prévention des épisodes ultérieurs,plutôt que comme une garantie absolue.']])
b(12,'Prévention secondaire : éviter une chronicisation négligée et reconnaître un changement',[
['h11','Dès la première consultation,les facteurs de chronicisation sont recherchés activement.'],
['h11','Leur nombre et leur importance conduisent à rapprocher le suivi et à mobiliser les professionnels nécessaires.'],
['h10+h15','Un élément nouveau ou une aggravation impose cependant de reconsidérer d’abord une cause spécifique.'],
['h15','L’absence d’amélioration après quatre semaines déclenche également une réévaluation du diagnostic et de la trajectoire.'],
['h16','Les interventions éducatives biopsychosociales peuvent modifier durablement les croyances et les comportements face au dos douloureux.']])
b(12,'Prévention tertiaire : limiter handicap,arrêt prolongé et effets indésirables',[
['h15','L’adaptation du poste et l’intervention professionnelle peuvent réduire le handicap lié à la trajectoire de soins.'],
['h12','L’exercice actif est maintenu avec une progression compatible avec les symptômes et la kinésiophobie.'],
['n1-2-24','Lorsque des médicaments sont utilisés,la dose efficace la plus basse et une durée courte limitent l’exposition.'],
['n1-2-28+n1-2-30','Les opioïdes chroniques et les gabapentinoïdes ne sont pas proposés pour la lombalgie dans le cadre NICE.'],
['h16','Le programme de prévention reste relié au risque de récidive et à la continuité des activités après l’épisode.']])
w(12,'Le lien avec les récidives explique la continuité des conseils',[
['h12','Les HUG rappellent un risque de récidive de20–45% sur une année.'],
['h16','La promotion de l’activité physique peut diminuer le nombre et la durée de ces récidives.'],
['h16','L’éducation ne se limite donc pas au soulagement de la crise présente.']])

b(13,'Six décisions à conserver',[
['h10','Une lombalgie commune est un diagnostic clinique après un triage et un examen qui ne retiennent pas de cause spécifique.'],
['h10+aorte-urgence','Une alarme vitale,neurologique ou infectieuse ouvre immédiatement la branche appropriée et ne relève pas d’une simple attente de guérison.'],
['n1-1-4+n1-1-6','L’imagerie n’est pas routinière et n’est envisagée en milieu spécialisé que si elle peut changer la prise en charge.'],
['h12','L’information rassurante,la reconnaissance de la douleur et l’activité adaptée constituent le socle initial du traitement.'],
['n1-2-24+n1-2-25+n1-2-28','Le recours médicamenteux reste conditionnel et bref,avec restrictions des opioïdes aigus et absence d’opioïdes chroniques.'],
['h15','Les consignes de reconsultation et le suivi selon le risque font partie du traitement dès la première évaluation.']])

tab(14,'Questions d’examen : réponse et raison',['Question','Bonne réponse','Raison'],[
[['def','Non spécifique signifie-t-il que le patient ne souffre pas réellement ?'],['h12','Non,la douleur est subjective et son intensité ne doit pas être mise en doute.'],['def+h12','L’absence de corrélat pathoanatomique clair ne supprime pas la plainte ni ses besoins fonctionnels.']],
[['h10','Une radiographie est-elle nécessaire pour confirmer toute lombalgie commune ?'],['h10','Non,le diagnostic est clinique après l’anamnèse et l’examen.'],['h10','L’imagerie systématique ne fournit pas de bénéfice clinique utile et peut entraîner un effet nocebo.']],
[['n1-1-5','L’adressage au spécialiste impose-t-il une imagerie ?'],['n1-1-5','Non,le patient peut être orienté pour avis sans avoir besoin d’un examen radiologique.'],['n1-1-6','L’image est envisagée si elle est susceptible de modifier la conduite.']],
[['queue','Une rétention urinaire nouvelle et une anesthésie en selle permettent-elles d’attendre le contrôle programmé ?'],['h10','Non,ces alarmes imposent une évaluation compressive sans délai avec avis neurochirurgical.'],['h10','Une nouvelle alarme neurologique sort du parcours commun et nécessite son imagerie urgente.']],
[['infect','Une fièvre avec contexte rachidien infectieux peut-elle être simplement traitée comme une crise mécanique ?'],['h10','Non,une spondylodiscite ou un abcès épidural suspecté appelle une IRM urgente.'],['infect','Le contexte infectieux et les gestes invasifs peuvent modifier le diagnostic de la douleur.']],
[['aorte-urgence','Une échographie aortique non concluante élimine-t-elle un anévrisme symptomatique encore suspecté ?'],['aorte-urgence','Non,la discussion immédiate avec le service vasculaire reste indiquée si la suspicion persiste.'],['aorte','La douleur dorsale peut accompagner une complication vasculaire grave.']],
[['h9','Une douleur uniquement lombaire pendant le Lasègue suffit-elle à le rendre positif ?'],['h9','Non,la manœuvre doit reproduire une douleur dans le trajet radiculaire.'],['h9','La condition de positivité distingue l’irritation radiculaire d’une douleur lombaire provoquée.']],
[['h4','Le soulagement par un AINS prouve-t-il une spondyloarthrite ?'],['h4','Non,les douleurs mécaniques peuvent aussi être soulagées par ces médicaments.'],['inflam','Le diagnostic inflammatoire nécessite un contexte et des éléments cliniques plus spécifiques.']],
[['h12','Le repos au lit accélère-t-il la récupération d’une lombalgie commune ?'],['h12','Non,il est décrit comme délétère et la mobilisation précoce est encouragée.'],['h12','La reprise des activités soutient le rétablissement plutôt qu’une trajectoire d’immobilité.']],
[['n1-2-26','Le paracétamol seul constitue-t-il le traitement médicamenteux de référence de NICE ?'],['n1-2-26','Non,NICE ne le recommande pas seul pour la lombalgie.'],['n1-2-25','Sa place éventuelle doit respecter le parcours conditionnel des moyens proposés.']],
[['n1-2-25','Un opioïde faible est-il proposé systématiquement lors d’une douleur aiguë ?'],['n1-2-25+n1-2-27','Non,son recours est conditionnel et non routinier.'],['n1-2-25','Une contre-indication,intolérance ou inefficacité des AINS doit être vérifiée dans ce cadre.']],
[['n1-2-28+n1-2-30','La chronicité justifie-t-elle automatiquement opioïdes ou gabapentinoïdes ?'],['n1-2-28+n1-2-30','Non,ces options ne sont pas proposées pour la lombalgie chronique dans le cadre NICE.'],['h11','Le risque de chronicisation appelle plutôt une réévaluation et un soutien adaptés.']],
[['pa5','Un comprimé pelliculé Dafalgan de1g peut-il être partagé pour obtenir une demi-dose ?'],['pa5','Non,le sillon n’est pas destiné à couper la dose de moitié.'],['pa5','La forme et le poids doivent être respectés pour éviter un surdosage.']],
[['h15','Une absence d’amélioration significative sous traitement pendant quatre à sept jours peut-elle être ignorée ?'],['h15','Non,la stratégie HUG propose une nouvelle consultation dans cette situation.'],['h15','Le suivi doit aussi reconnaître tout signe nouveau ou toute aggravation.']],
[['h15','Un arrêt de travail est-il prolongé sans nouvelle évaluation ?'],['h15','Non,la prolongation dépend d’une réévaluation du handicap et des contraintes professionnelles.'],['h15','Le projet vise une reprise adaptée et limite l’arrêt initial selon le parcours HUG.']],
[['n1-2-13+n1-2-14','Les anciennes recommandations psychologiques NICE peuvent-elles être citées comme inchangées en2026 ?'],['n1-2-13+n1-2-14','Non,elles ont été retirées en juillet2026 après la surveillance du référentiel.'],['n1-2-13+n1-2-14','Leur retrait pour possible obsolescence ne doit pas être transformé en une recommandation de remplacement inventée.']]])
w(14,'Une bonne consigne de suivi ne banalise pas une alarme',[
['h15','L’absence d’amélioration dans le délai prévu invite à reconsulter et à ajuster le parcours.'],
['h10','En revanche,un signe compressif urgent appelle l’action sans attendre cette échéance.'],
['n1-1-1','Le changement de symptôme peut donc modifier le diagnostic,même après une première évaluation rassurante.']])

def enregistrer():
 substitutions={
 'Une lombo-sciatalgie comporte une irradiation au-delà du pli fessier dans un ou plusieurs membres inférieurs.':'Une lombo-sciatalgie comprend une irradiation au-delà du pli fessier dans un ou plusieurs membres inférieurs.',
 'Une enquête suisse menée en 2020 retrouve cette expérience chez 88 % des personnes interrogées.':'Une enquête suisse menée en 2020 montre cette expérience chez 88 % des personnes interrogées.',
 'Le questionnaire complète une anamnèse détaillée pour quantifier le risque de chronicisation.':'Le questionnaire est un complément à l’anamnèse détaillée pour quantifier le risque de chronicisation.',
 'Une marche sur talons et pointes sans parésie sévère n’exclut toutefois pas une faiblesse plus discrète.':'Une marche sur talons et pointes sans parésie sévère ne permet toutefois pas d’exclure une faiblesse plus discrète.',
 'La palpation des vertèbres et des espaces contribue ensuite à explorer une origine infectieuse ou inflammatoire possible.':'La palpation des vertèbres et des espaces permet ensuite d’explorer une origine infectieuse ou inflammatoire possible.',
 'L’examen vérifie ensuite la sensibilité péri-anale et glutéale ainsi que le tonus du sphincter anal.':'L’examen recherche ensuite une anomalie de sensibilité péri-anale ou glutéale ainsi qu’une modification du tonus anal.',
 'NICE réserve la thérapie manuelle à un ensemble thérapeutique comprenant des exercices.':'Selon NICE,la thérapie manuelle peut être envisagée dans un ensemble thérapeutique comprenant des exercices.',
 'Le sillon du comprimé pelliculé n’est pas prévu pour réduire la dose de moitié.':'Le sillon du comprimé pelliculé ne doit pas être utilisé pour réduire la dose de moitié.',
 'L’absence d’amélioration dans le délai prévu invite à reconsulter et à ajuster le parcours.':'L’absence d’amélioration dans le délai prévu conduit à reconsulter et à ajuster le parcours.'
 }
 def forme(s):
  s=substitutions.get(s,s).replace('lombov ertébral','lombovertébral').replace('autorisations40858,40859,43787 et43788','autorisations 40858, 40859, 43787 et 43788').replace('autorisations47503,47505 et56318','autorisations 47503, 47505 et 56318').replace('NYHAIII','NYHA III')
  if s.startswith('Le cadre NICE consulté concerne les personnes de plus de16ans'):
   s='Le champ du référentiel NICE est respecté et ne devient pas automatiquement un protocole de lombalgie du jeune enfant.'
  s=re.sub(r',(?=[^\d\s])',', ',s)
  s=re.sub(r'(?<!\b[LMS])(?<=[A-Za-zÀ-ÿ])(?=\d)',' ',s)
  s=re.sub(r'(?<=\d)(?=[A-Za-zÀ-ÿ])',' ',s)
  return s
 for point in P.values():
  for key in ['blocs','fenetres']:
   for _,items in point[key]:
    for x in items:
     if x[1].startswith('La stratégie HUG de 2022 rapporte une prévalence'):x[0]='h2+h3'
     x[1]=forme(x[1])
  for _,_,rows in point['tableaux']:
   for row in rows:
    for x in row:
     if x[1].startswith('Le dénominateur est la population générale suisse décrite par HUG2022'):x[0]='h2+h3'
     x[1]=forme(x[1])
  for k in ['blocs','fenetres']:
   for a in point[k]:a[0]=a[0].replace('lombov ertébral','lombovertébral')
 (B/'contenu.json').write_text(json.dumps({'entite':'Lombalgie commune non spécifique','references':R,'points':P,'statut':'Rédaction privée sourcée,aucun autoauditP3.'},ensure_ascii=False,indent=1)+'\n')

if __name__=='__main__':enregistrer()
