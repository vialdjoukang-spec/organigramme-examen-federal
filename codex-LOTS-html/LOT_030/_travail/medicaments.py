import gzip
from html import escape
from format_lecon import R,paras
def q(n,s):
 t=gzip.open(R/f'ressources_ia/aips/fi_fr/{n}.txt.gz','rt').read();assert s in t,(n,s)
 return '<blockquote><p>« '+escape(s)+' »</p></blockquote>'
def line(n,prefix):
 t=gzip.open(R/f'ressources_ia/aips/fi_fr/{n}.txt.gz','rt').read()
 return next(s for s in t.splitlines() if s.startswith(prefix))
def mometasone_aigue(l):
 text=paras('Nasonex spray doseur nasal, furoate de mométasone, information professionnelle suisse n° 54189. Cette indication concerne une rhinosinusite aiguë non compliquée, chez l’adulte et l’adolescent dès douze ans, dans la durée et les conditions ci-dessous. Elle ne s’étend pas automatiquement à toute la durée possible d’une rhinosinusite postvirale.')
 text+=q('54189',line('54189','Le spray doseur nasal Nasonex peut être utilisé chez les adultes'))
 text+=q('54189',line('54189','La dose recommandée est de deux pulvérisations de spray 2x'))
 for s in ["Il est recommandé au patient de consulter son médecin si les symptômes s'aggravent pendant le traitement.","La sécurité et l'efficacité de Nasonex pour le traitement des symptômes de la rhino-sinusite aiguë n'ont pas été étudiées chez les enfants de moins de 12 ans.","Hypersensibilité au principe actif ou à l'un des excipients conformément à la composition.","Le traitement par des corticoïdes en application nasale pendant la grossesse et l'allaitement n'aura lieu qu'en cas d'absolue nécessité."]:
  text+=q('54189',s)
 text+=paras('La dose citée correspond à quatre cents microgrammes par jour, avec une pulvérisation contenant cinquante microgrammes. Elle diffère de la dose habituelle de rhinite allergique : ne pas utiliser un schéma unique pour toutes les indications.', 'Ne pas utiliser sur une infection locale non traitée ni avant cicatrisation d’un traumatisme ou d’une intervention nasale. Réévaluer saignements persistants, infection ou troubles visuels ; vérifier les interactions avec puissants inhibiteurs du CYP3A4. Une douleur unilatérale persistante, un gonflement facial ou orbital ou une aggravation secondaire demande un bilan, pas une simple augmentation du spray.')
 return l.subwindow('mometasone-aigue','Mométasone : indication aiguë et dose suisse',text,(10,))
def allergie(l):
 text=paras('Nasonex spray doseur nasal, furoate de mométasone, information professionnelle suisse n° 54189. Cette fenêtre concerne la rhinite allergique, pas la dose pour polypose ou rhinosinusite. Utiliser régulièrement et vérifier la technique ; diriger le jet vers la paroi externe, en évitant la cloison.')
 text+=q('54189','1 pulvérisation (=100 mg de la suspension aqueuse) contient 50 µg de furoate de mométasone.')
 text+=paras('Adultes et enfants dès douze ans : deux pulvérisations dans chaque narine une fois par jour, puis réduction après contrôle des symptômes selon la notice.')
 for prefix in ['1× par jour, de préférence le matin,','Lorsque les symptômes sont sous contrôle, la dose peut être réduite']:
  text+=q('54189',line('54189',prefix))
 text+=paras('Enfants de six à onze ans :')+q('54189','1× par jour 1 pulvérisation de spray dans chaque narine (correspond à 50 µg de furoate de mométasone/pulvérisation de spray ou 100 µg de furoate de mométasone/jour). Ne pas augmenter la posologie.')
 text+=paras('Cette indication suisse commence à six ans ; ne pas lui attribuer l’âge d’une notice étrangère. Contre-indication :')+q('54189',"Hypersensibilité au principe actif ou à l'un des excipients conformément à la composition.")
 text+=q('54189',"Le traitement par des corticoïdes en application nasale pendant la grossesse et l'allaitement n'aura lieu qu'en cas d'absolue nécessité.")
 text+=paras('Éviter l’utilisation sur une infection locale non traitée ou avant cicatrisation d’un traumatisme ou d’une chirurgie nasale. Surveiller irritation et saignement ; réévaluer une épistaxis persistante, une infection locale ou un trouble visuel. Vérifier les interactions avec puissants inhibiteurs du CYP3A4 et surveiller la croissance lors d’un traitement prolongé chez l’enfant. Utiliser la dose minimale efficace ; l’action n’est pas celle d’un vasoconstricteur immédiat.')
 a=l.subwindow('mometasone-allergie','Mométasone : dose suisse pour rhinite allergique',text,(1,10))
 text=paras('Cetirizin-Mepha 10, comprimés pelliculés, cétirizine, information professionnelle suisse n° 65119. Option orale pour symptômes allergiques selon indication ; l’effet sur l’obstruction peut être moindre que celui du traitement nasal. La fonction rénale et le risque de somnolence doivent être évalués.')
 for s in ['Adultes et adolescents de plus de 12 ans: la dose recommandée est de 10 mg 1 fois par jour (1 comprimé pelliculé).','Enfants de 6 à 12 ans: durant 4 semaines au maximum, 10 mg 1 fois par jour (1 comprimé pelliculé).','La dose peut être répartie sur deux prises (soit un demi-comprimé pelliculé le matin et le soir).']:
  text+=q('65119',s)
 text+=paras('La limite de quatre semaines citée chez l’enfant concerne la rhinite saisonnière ; la notice distingue la forme pérenne. Cette présentation n’est pas adaptée au-dessous de six ans. Chez l’adulte, le tableau suisse prévoit cinq milligrammes par jour pour un débit de 30 à moins de 60 ml/min. Entre 15 et moins de 30 ml/min sans dialyse, il prévoit cinq milligrammes tous les deux jours. Demander l’adaptation individuelle. Ne pas appliquer une formule adulte de fonction rénale à un enfant.')
 renal=gzip.open(R/'ressources_ia/aips/fi_fr/65119.txt.gz','rt').read()
 text+=q('65119',renal[renal.index('Fonction rénale normale'):renal.index('Patients âgés')].strip())
 for s in ["Hypersensibilité au principe actif, la cétirizine, à un autre dérivé de la pipérazine ou à l'un des excipients.",'Insuffisance rénale terminale (débit de filtration glomérulaire (DFG) inférieur à 15 ml/min).',"L'utilisation du comprimé pelliculé n'est pas recommandée chez l'enfant de moins de 6 ans car cette forme ne permet pas l'adaptation posologique dans cette tranche d'âge.","La prudence est de mise en cas d'emploi pendant la grossesse."]:
  text+=q('65119',s)
 text+=q('65119',line('65119',"La cétirizine ne devrait pas être utilisée durant l'allaitement"))
 text+=paras('La somnolence peut affecter la conduite et les activités demandant de l’attention ; prudence avec alcool et autres sédatifs. Évaluer les risques de rétention urinaire et de convulsions. Une réaction allergique impose arrêt et prise en charge adaptée ; coordonner l’interruption avant tests cutanés avec l’équipe qui les réalise. Les doses supérieures parfois citées dans d’autres documents ne sont pas présentées ici comme la dose de rhinite de cette notice.')
 b=l.subwindow('cetirizine','Cétirizine : dose suisse et adaptation',text,(1,11))
 return a+paras(b)
def xylometazoline(l):
 text=paras('Exemple de traitement bref de l’obstruction associée, non de toute rhinorrhée : Otrivin Rhume Classic, chlorhydrate de xylométazoline, information professionnelle suisse n° 24926. Les concentrations et formes ne sont pas interchangeables. La durée maximale n’est pas un objectif à atteindre : utiliser le minimum nécessaire après vérification du terrain.')
 text+=paras('Spray nasal 0,1 %, adultes et adolescents dès douze ans :')+q('24926','1 pulvérisation dans chaque narine. Répéter si besoin, ne pas dépasser 3 applications par jour.')
 text+=q('24926','Enfants âgés de moins de 12 ans: la préparation ne doit pas être utilisée.')
 text+=paras('Gouttes 0,1 %, même groupe d’âge :')+q('24926','2–3 gouttes de solution 0.1% dans chaque narine. Répéter si besoin, ne pas dépasser 3-4 applications par jour.')
 text+=paras('Solution ou spray 0,05 %, enfant de deux à onze ans sous surveillance adulte :')+q('24926','1–2 gouttes de la solution 0.05% ou 1 pulvérisation du spray nasal 0.05% 1–2 fois par jour dans chaque narine; ne pas dépasser 3 applications par jour.')
 for s in ['Enfants de 1 à 2 ans: utiliser selon prescription médicale.','Enfants de moins de 1 an: la préparation ne doit pas être utilisée.',"Otrivin Rhume Classic ne doit pas être utilisé pendant plus d'une semaine, une utilisation plus longue pouvant entraîner une rhinite médicamenteuse.",'Du fait de ses propriétés vasoconstrictrices, Otrivin Rhume Classic ne doit pas être utilisé par précaution en cours de la grossesse.',"On ne sait pas si la xylométazoline passe dans le lait maternel. Pendant l'allaitement, Otrivin Rhume Classic doit être utilisé uniquement sur prescription médicale."]:
  text+=q('24926',s)
 text+=paras('Contre-indications de la notice, avec son libellé exact :')
 for s in ["· Hypersensibilité au principe actif (chlorhydrate de xylométazoline) ou à l'un des excipients mentionnés dans la composition",'· Rhinite sèche (rhinitis sicca)','· Rhinite atrophique','· Patients atteints de glaucome à angle fermé','· Après une hypophysectomie transsphénoïdale (ou après des interventions chirurgicales transnasales ou transbuccales exposant la dure-mère']:
  text+=q('24926',s)
 text+=paras('Prudence notamment en cas de maladie cardiovasculaire, hypertension, syndrome du QT long, hyperthyroïdie, diabète, phéochromocytome ou hypertrophie prostatique. Vérifier les interactions avec inhibiteurs de la monoamine-oxydase et antidépresseurs tricycliques ou tétracycliques.', 'Des céphalées soudaines sévères, troubles visuels, nausées ou vomissements sous sympathomimétique imposent arrêt du produit et consultation immédiate selon la notice. Ne pas traiter une suspicion de fuite liquidienne ou un corps étranger par répétition de sprays. Le protocole hospitalier d’extraction peut décrire d’autres préparations : il ne modifie pas les limites de cette spécialité.')
 return l.subwindow('xylometazoline','Xylométazoline : doses et restrictions suisses',text,(9,))
def antibiotiques(l):
 text=paras('Amoxi-Mepha, amoxicilline orale, information professionnelle suisse n° 44911. La fiche bernoise cite l’amoxicilline en première intention lorsque l’antibiothérapie est retenue. Son schéma adulte spécifique à la sinusite diffère du libellé général de la notice ci-dessous ; les deux sources ne sont pas fusionnées en une posologie unique.', 'Pour les infections légères à moyennes chez l’adulte et l’enfant de plus de quarante kilogrammes, la notice indique :')
 for s in ["Consignes générales: 1500 mg – 3000 mg d'amoxicilline/jour en 3 à 4 doses individuelles.",'Posologie recommandée: 375 à 750 mg 3 à 4 fois par jour.']:
  text+=q('44911',s)
 text+=paras('Ces formulations ne sont pas identiques. Le prescripteur doit choisir explicitement le schéma, la spécialité et la durée adaptés, en tenant compte des recommandations locales et de la notice. La durée de dix jours figurant pour certaines infections streptococciques n’est pas appliquée automatiquement à toute sinusite.', 'Les limites rénales de cette notice, chez l’adulte et l’enfant de plus de quarante kilogrammes, sont :')
 raw=gzip.open(R/'ressources_ia/aips/fi_fr/44911.txt.gz','rt').read()
 start=raw.index('Clairance de la créatinine (ClCr) (ml/min)');end=raw.index('La dose unique de 3 g',start)
 text+=q('44911',raw[start:end].strip())
 text+=q('44911',line('44911','Hypersensibilité envers le principe actif'))
 text+=q('44911',line('44911','Mononucléose infectieuse, leucémie lymphoïde:'))
 text+=q('44911',line('44911','Les études expérimentales effectuées'))
 text+=q('44911',line('44911','Amoxi-Mepha diffuse dans le lait maternel'))
 text+=paras('Prudence pendant la grossesse ; la notice comporte une restriction pendant l’allaitement. Dans cette situation, discuter le choix avec le prescripteur et le pharmacien, sans décider seul d’un sevrage. Rechercher allergie aux bêta-lactamines et interactions, notamment méthotrexate, anticoagulants, allopurinol ou probénécide. Une réaction allergique sévère impose arrêt et prise en charge urgente ; une diarrhée sévère, persistante ou sanglante nécessite une évaluation.', 'Les doses pédiatriques et celles des formes injectables ne sont pas obtenues en divisant ce schéma adulte. Elles nécessitent leur notice propre, le poids, la fonction rénale et l’indication exacte.')
 a=l.subwindow('amoxicilline','Amoxicilline : recommandation et notice distinctes',text,(3,13))
 text=paras('Augmentin comprimés filmés, amoxicilline avec acide clavulanique, information professionnelle suisse n° 45674. Exemple lorsque cette association est indiquée ; elle ne remplace pas automatiquement l’amoxicilline en première intention. La dose annoncée du comprimé comprend les deux constituants.')
 for prefix in ['Comprimés filmés à 625 mg','Comprimés filmés à 1 g','Dans des cas particuliers (sinusites aiguës,']:
  text+=q('45674',line('45674',prefix))
 text+=paras('Le schéma cité concerne l’adulte et l’enfant de plus de quarante kilogrammes. Un gramme correspond ici à huit cent septante-cinq milligrammes d’amoxicilline et cent vingt-cinq milligrammes de clavulanate. Le schéma particulier de l’aide bernoise n’est pas déclaré équivalent à ces comprimés ; le choix de formulation doit être vérifié.')
 text+=q('45674',line('45674','Augmentin comprimés filmés ne convient pas'))
 raw=gzip.open(R/'ressources_ia/aips/fi_fr/45674.txt.gz','rt').read();start=raw.index('Clairance de la créatinine\n');end=raw.index('Hémodialyse',start)
 text+=q('45674',raw[start:end].strip())
 for prefix in ['Les comprimés filmés à 1 g ne doivent','Il est recommandé de prendre Augmentin','Le sillon de sécabilité des comprimés','L\'usage d\'Augmentin est contre-indiqué','Augmentin ne devrait donc être utilisé','Il ne faudrait donc pas allaiter']:
  text+=q('45674',line('45674',prefix))
 text+=paras('La restriction d’allaitement reproduit la notice de cette spécialité : discuter une solution avec le prescripteur plutôt que décider seul d’un sevrage. Vérifier antécédent hépatique sous association et interactions, notamment méthotrexate, anticoagulants et mycophénolate. Surveiller fonction rénale et hépatique selon le terrain et la durée.', 'Arrêter et consulter en cas de réaction allergique ou cutanée sévère. Une diarrhée importante, persistante ou sanglante peut évoquer une colite associée aux antibiotiques ; elle demande une évaluation et ne doit pas être masquée par un ralentisseur du transit. Une aggravation clinique nécessite de rechercher une complication ou une autre cause, pas seulement d’augmenter la dose.')
 return a+paras(l.subwindow('amoxiclav','Amoxicilline–clavulanate : formulation et limites',text,(3,14)))
def mometasone_polypes(l):
 text=paras('Nasonex spray doseur nasal, furoate de mométasone, information professionnelle suisse n° 54189. Cette fenêtre concerne les polypes nasaux chez l’adulte dès dix-huit ans. Une masse unilatérale inhabituelle doit être explorée, sans traitement empirique prolongé supposant une polypose banale.')
 for prefix in ['Le spray doseur nasal Nasonex est indiqué pour le traitement des polypes','La dose recommandée est de 2 pulvérisations de spray 2×','Une fois les symptômes sous contrôle','En l\'absence d\'amélioration après 5 à 6','La tolérance et l\'efficacité de Nasonex n\'ont pas été étudiées dans le traitement des polypes chez']:
  text+=q('54189',line('54189',prefix))
 for s in ["Hypersensibilité au principe actif ou à l'un des excipients conformément à la composition.","Le traitement par des corticoïdes en application nasale pendant la grossesse et l'allaitement n'aura lieu qu'en cas d'absolue nécessité."]:
  text+=q('54189',s)
 text+=paras('La dose initiale est de quatre cents microgrammes par jour ; la dose réduite citée est de deux cents. Elle n’est pas interchangeable avec le schéma de rhinite allergique ou avec une préparation destinée au lavage. Ne pas utiliser sur une infection locale non traitée ou avant cicatrisation après traumatisme ou chirurgie.', 'Vérifier les interactions avec puissants inhibiteurs du CYP3A4. Surveiller irritation et épistaxis ; un saignement persistant, une infection ou un trouble visuel impose une réévaluation. Les effets systémiques des corticoïdes restent possibles, notamment avec doses élevées, traitement prolongé ou interactions. La surveillance clinique accompagne l’emploi prolongé.')
 return l.subwindow('mometasone-polypes','Mométasone : dose suisse pour polypes adultes',text,(10,))
