import gzip
from html import escape
from format_lecon import R,paras
def quote(n,s):
 t=gzip.open(R/f'ressources_ia/aips/fi_fr/{n}.txt.gz','rt').read();assert s in t,(n,s)
 return '<blockquote><p>« '+escape(s)+' »</p></blockquote>'
def paracetamol(l):
 text=paras('DAFALGAN comprimés, information professionnelle suisse n° 46206. Le soulagement de la douleur ne remplace pas le diagnostic ; employer la plus faible dose efficace selon poids, terrain et préparation.')
 text+=paras('Tableau des comprimés de 500 mg, extrait pour plus de 40 kg et plus de 12 ans :')+quote('46206','>40 kg (>12 ans et adultes)\n4 g\nJusqu\'à 4 x 1 – 2 comprimés')
 text+=quote('46206','Respecter un intervalle de 4 à 8 h entre chaque prise.')
 text+=quote('46206',"Afin d'éviter tout risque de surdosage, il faut s'assurer que les médicaments pris simultanément ne contiennent pas de paracétamol.")
 text+=paras('Extrait du tableau des comprimés de 500 mg pour l’enfant : chaque ligne donne poids/âge, dose journalière maximale et répartition possible. Le poids doit guider le choix et les bornes doivent être vérifiées avec le professionnel.')+quote('46206',"15 – 22 kg (3 – 6 ans)\n1 g\nJusqu'à 4 x ½ comprimé\n22 – 30 kg (6 – 9 ans)\n1,5 g\nJusqu'à 3 x ½ – 1 comprimé\n30 – 40 kg (9 – 12 ans)\n2 g\nJusqu'à 4 x 1 comprimé")
 text+=quote('46206',"La durée maximale d'utilisation continue pour les enfants jusqu'à 12 ans sans consultation médicale est de 3 jours.")
 text+=paras('Le comprimé de 1 g a d’autres bornes : plus de 50 kg et plus de 15 ans dans son tableau. Sa rainure facilite la déglutition et ne permet pas de considérer chaque morceau comme une dose exacte de 500 mg. Pour un enfant plus petit, choisir une formulation pédiatrique et sa notice, sans extrapoler ce tableau.')
 text+=quote('46206',"Chez les patients ayant une maladie hépatique chronique ou compensée active, en particulier une insuffisance hépatocellulaire, alcoolisme chronique, déficit d'alimentation chronique (faibles réserves de glutathion hépatique) ou déshydratation, la dose quotidienne pour les adultes ne doit pas dépasser 3 g (cf. aussi «Contre-indications» et «Mises en garde et précautions»).")
 text+=paras('Ce plafond n’autorise pas l’utilisation dans les situations contre-indiquées : la notice cite hypersensibilité, atteinte hépatique sévère, hépatite aiguë ou maladie décompensée active et maladie de Gilbert. Une insuffisance rénale exige un espacement adapté ; vérifier le tableau complet avant prescription.', 'Grossesse — extrait de la préparation :')+quote('46206',"En cas de nécessité clinique, le paracétamol peut être pris ou utilisé pendant la grossesse. Toutefois, il convient de prendre ou d'utiliser la dose efficace la plus faible pendant la durée la plus courte possible et à la fréquence la plus basse possible.")
 text+=quote('46206',"La prudence est de mise en cas d'utilisation de DAFALGAN durant la grossesse et l'allaitement.")
 text+=quote('46206',"Bien que l'utilisation du paracétamol soit considérée comme compatible avec l'allaitement, la prudence est recommandée lors de l'utilisation du Dafalgan pendant l'allaitement.")
 text+=paras('En cas de surdosage possible, demander immédiatement un avis médical ou Tox Info Suisse 145, même sans symptôme. Le plafond de dose n’est pas un objectif à atteindre ni un seuil de toxicité universel.')
 return l.subwindow('paracetamol','Paracétamol : préparation suisse, poids et plafonds',text,(15,))
def extrait(n,debut):
 lines=gzip.open(R/f'ressources_ia/aips/fi_fr/{n}.txt.gz','rt').read().splitlines()
 hits=[x for x in lines if x.startswith(debut)];assert len(hits)==1,(n,debut,len(hits))
 return quote(n,hits[0])
def carbamazepine(l):
 text=paras('Timonil / Timonil retard, carbamazépine : notice suisse n° 45723. La posologie ci-dessous concerne la névralgie, pas le tableau pédiatrique de l’épilepsie. Le choix de forme et la titration relèvent du prescripteur.')
 text+=extrait('45723','- Névralgie essentielle du trijumeau')
 text+=extrait('45723','La posologie initiale est de 200 à 400 mg/j')
 text+=extrait('45723','Les comprimés à libération prolongée de Timonil à 200 mg')
 text+=paras('La barre des comprimés standards de 200 mg ne permet pas de garantir une demi-dose ; les formes retard de 200 et 400 mg sont sécables pour le dosage selon cet extrait. Ne pas transférer sans vérification la fréquence des prises entre libération immédiate, retard et suspension.')
 text+=extrait('45723','Grâce à la libération lente et contrôlée')
 text+=extrait('45723','- Patients avec bloc auriculo-ventriculaire')
 text+=paras('Autres contre-indications et précautions : hypersensibilité à carbamazépine, oxcarbazépine ou substances apparentées ; association aux inhibiteurs de la monoamine-oxydase à éviter selon la notice. Vérifier interactions avant prescription, notamment macrolides, azolés et médicaments dont l’efficacité peut être diminuée par induction enzymatique.', 'Avant puis pendant le traitement : formule sanguine, fonction hépatique et rénale ; surveillance du sodium selon risque. Le dépistage génétique HLA-A*3101 ou HLA-B*1502 dépend des origines et du risque décrit par la notice ; un test négatif ne dispense pas de surveiller une réaction cutanée.', 'Fièvre, éruption, ulcérations buccales, ecchymoses inhabituelles, confusion ou signes hépatiques justifient un contact médical immédiat. Somnolence, vertiges, diplopie et ataxie peuvent compromettre conduite et sécurité. Informer aussi sur les symptômes suicidaires et leur prise en charge urgente.')
 text+=paras('Grossesse : la notice distingue explicitement douleurs neuropathiques et épilepsie. L’extrait comporte des irrégularités typographiques conservées :')
 text+=extrait('45723','Lors de l ’ utilisation de la carbamzépine pendant la grossesse')
 text+=extrait('45723','Les femmes en âges de procréer doivent utiliser une méthode')
 text+=paras('L’induction enzymatique peut réduire l’efficacité d’une contraception hormonale ; organiser une méthode adaptée avec le professionnel. En cas de grossesse sous traitement, demander rapidement une décision spécialisée, sans modification improvisée.')
 text+=extrait('45723','La carbamazépine passe dans le lait maternel')
 text+=paras('Le choix pendant l’allaitement est individualisé et surveillé ; la notice décrit les signes du nourrisson qui imposent une réévaluation. Pour l’enfant avec douleur faciale, ne pas recopier le schéma d’épilepsie comme dose validée de névralgie. Une atteinte hépatique ou rénale demande une évaluation individuelle plutôt qu’une règle de réduction inventée.')
 return l.subwindow('carbamazepine','Carbamazépine : dose AIPS, formulation et surveillance',text,(12,16))
def prednisone(l):
 text=paras('Prednisone Streuli, notice suisse n° 29349. L’artérite à cellules géantes figure dans les indications rhumatismales. La notice donne une posologie générale, sans schéma initial propre à cette maladie ni aux complications visuelles.')
 text+=extrait('29349','Affections rhumatismales:')
 text+=extrait('29349','La posologie initiale dépend de la maladie à traiter')
 text+=paras('Cet extrait général ne constitue pas une prescription spécifique d’artérite. La dose initiale, la voie en cas de menace visuelle et la décroissance doivent être arrêtées immédiatement par l’équipe ; les doses du PNDS français ne sont pas présentées comme des doses AIPS. L’absence de schéma spécifique dans cette notice ne justifie aucun retard thérapeutique.', 'Rechercher infection, diabète, hypertension, ostéoporose, risque digestif, glaucome et troubles psychiatriques. La prévention osseuse, les vaccinations et les risques infectieux sont discutés selon durée et traitement associé ; les stratégies d’épargne cortisonique relèvent du spécialiste.')
 text+=extrait('29349',"Ce médicament ne doit pas être utilisé en cas d'hypersensibilité")
 text+=extrait('29349','Comme pour toute thérapie par glucocorticoïdes, la thérapie par Prednisone Streuli')
 text+=extrait('29349',"Pour ces raisons, Prednisone Streuli, à l'instar")
 text+=quote('29349',"Pendant l'application systémique des corticostéroïdes on ne doit pas allaiter.")
 text+=paras('La restriction d’allaitement est celle de cette préparation ; la décision se discute avec médecin et pharmacien, sans sevrage ou arrêt autonome. Le traitement de l’artérite ne doit pas être interrompu brutalement, et les adaptations lors d’une maladie intercurrente demandent un plan prescrit.')
 return l.subwindow('prednisone','Prednisone : indication suisse et limites posologiques',text,(13,17))

def grossesse(n):
 assert n=='56758'
 return paras('Grossesse et allaitement — extraits de cette préparation :')+quote(n,"Co-Amoxi-Mepha i.v. ne devrait donc être utilisé pendant la grossesse qu'en cas de nécessité absolue.")+quote(n,"Il ne faudrait donc pas allaiter pendant le traitement par Co-Amoxi-Mepha i.v.")+paras('Ces restrictions sont celles de cette préparation. Faire vérifier le choix avec médecin et pharmacien sans arrêt autonome du traitement essentiel ou de l’allaitement.')
def coamoxicilline(l):
 text=paras('Co-Amoxi-Mepha injectable/perfusion associe amoxicilline et acide clavulanique. Exemple de préparation suisse utilisable après décision hospitalière pour une infection sensible ; le choix doit couvrir la flore attendue, tenir compte des allergies et du protocole local. Le drainage reste essentiel pour l’abcès.')
 text+=paras('Extrait AIPS, adultes et enfants de plus de 40 kg, infections de gravité modérée :')+quote('56758','1200 mg (1000/200) 3-4 × par jour en injection intraveineuse lente.')
 text+=paras('Extrait AIPS, infections graves dans la même population :')+quote('56758','2200 mg (2000/200) 3-4 × par jour en perfusion brève (au moins 30 minutes).')
 text+=quote('56758',"La posologie dépend de l'âge, du poids et de la fonction rénale du patient, ainsi que du degré de sévérité de l'infection.Co-Amoxi-Mepha i.v. ne doit pas être administré plus souvent que toutes les 4 heures.")
 text+=paras('Les chiffres entre parenthèses désignent amoxicilline/acide clavulanique en mg. Ne pas confondre les ratios adultes et pédiatriques ni calculer une dose pédiatrique à partir de ce seul extrait. La fonction rénale nécessite un schéma d’adaptation spécifique avant prescription.', 'La durée de l’abcès n’est pas fixée par ces lignes AIPS : le protocole CHUV publié en 2021 décrit un relais oral selon l’évolution et une durée totale de 10 à 14 jours. Le protocole local actuel, le drainage, les cultures et la réponse clinique déterminent la décision.', 'Contre-indications : hypersensibilité connue aux pénicillines, céphalosporines ou à l’acide clavulanique, et antécédent d’ictère ou d’atteinte hépatique sous cette association. Surveiller réactions allergiques ou cutanées sévères, fonction rénale et tolérance hépatique ; vérifier les interactions et la préparation avant administration. Une allergie grave exige une alternative validée avec l’équipe, sans substitution automatique.')
 text+=quote('56758',"L'usage de Co-Amoxi-Mepha i.v. est contre-indiqué en cas d'hypersensibilité connue aux pénicillines et céphalosporines ou à l'acide clavulanique, de même que chez les patients qui ont présenté un ictère ou des troubles de la fonction hépatique pendant un traitement antérieur par Co-Amoxi-Mepha i.v.")+grossesse('56758')
 return l.subwindow('coamoxi','Amoxicilline–acide clavulanique : exemple hospitalier suisse',text,(5,21))
