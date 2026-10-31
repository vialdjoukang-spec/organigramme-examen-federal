import gzip
from html import escape
from format_lecon import R,paras
def q(n,s):
 t=gzip.open(R/f'ressources_ia/aips/fi_fr/{n}.txt.gz','rt').read();assert s in t,(n,s)
 return '<blockquote><p>« '+escape(s)+' »</p></blockquote>'
def line(n,prefix):
 t=gzip.open(R/f'ressources_ia/aips/fi_fr/{n}.txt.gz','rt').read()
 return next(s for s in t.splitlines() if s.startswith(prefix))
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
 return l.subwindow('xylometazoline','Xylométazoline : doses et restrictions suisses',text,(14,))

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
 a=l.subwindow('mometasone-allergie','Mométasone : dose suisse pour rhinite allergique',text,(6,15))
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
 b=l.subwindow('cetirizine','Cétirizine : dose suisse et adaptation',text,(6,16))
 return a+paras(b)
