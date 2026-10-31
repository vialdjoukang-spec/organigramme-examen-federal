import gzip
from html import escape
from format_lecon import R,paras
def raw(n):return gzip.open(R/f'ressources_ia/aips/fi_fr/{n}.txt.gz','rt').read()
def q(n,s):
 assert s in raw(n),(n,s)
 return '<blockquote><p>« '+escape(s)+' »</p></blockquote>'
def line(n,prefix):return next(s for s in raw(n).splitlines() if s.startswith(prefix))
def segment(n,a,b):
 t=raw(n);i=t.index(a);return t[i:t.index(b,i)].strip()
def paracetamol(l):
 t=paras('Dafalgan, information professionnelle suisse n° 47503. Exemple d’antalgie symptomatique, sans preuve qu’il traite la cause de toute cervicalgie. La fenêtre adulte concerne les comprimés effervescents sécables de cinq cents milligrammes, chez les personnes de plus de douze ans et de plus de quarante kilogrammes. Les doses maximales ne sont pas des objectifs ; utiliser la dose minimale utile, brièvement et après vérification du terrain.')
 t+=q('47503',segment('47503',">40 kg\n(>12 ans et adultes)\n500",'Il convient'))
 t+=q('47503',line('47503',"Pour prévenir le risque de surdosage"))
 t+=paras('Les formes d’un gramme ont d’autres limites de poids et d’âge et ne sont pas divisibles pour ajuster la dose. Ne pas transposer ce schéma adulte au jeune enfant. Pour celui-ci, vérifier la forme et le tableau pondéral de la notice avec le prescripteur ; une raideur fébrile exige une évaluation immédiate, même si l’antipyrétique semble efficace.')
 t+=q('47503',line('47503','Chez les enfants (<12 ans) la dose doit être déterminée'))
 t+=q('47503',line('47503','Chez les patients ayant une maladie hépatique chronique'))
 t+=q('47503',segment('47503','Clairance de la créatinine\nIntervalle posologique','Contre-indications'))
 t+=paras('Contre-indications exactes de cette notice ; la mention du soja concerne les suppositoires :')
 t+=q('47503',segment('47503','· Hypersensibilité au paracétamol','Mises en garde et précautions'))
 for prefix in ['En cas de nécessité clinique, le paracétamol','Le paracétamol passe dans le lait maternel.']:
  t+=q('47503',line('47503',prefix))
 t+=paras('Vérifier cumul d’antalgiques, alcool, dénutrition, déshydratation, atteinte hépatique ou rénale et interactions, notamment anticoagulants coumariniques ou flucloxacilline. Un surdosage suspect nécessite une prise en charge immédiate même sans symptôme. Une baisse de fièvre ou de douleur n’exclut ni infection grave ni hémorragie.')
 return l.subwindow('paracetamol','Paracétamol : exemple suisse et limites',t,(11,))
def ibuprofene(l):
 t=paras('Brufen, ibuprofène oral, information professionnelle suisse n° 45031. Option à discuter brièvement pour une douleur musculosquelettique compatible avec son indication, après exclusion d’une urgence et vérification des risques. Le schéma ci-dessous est celui des affections rhumatismales de la notice, pas une prescription automatique pour chaque nuque douloureuse.')
 t+=q('45031',line('45031','Utiliser la dose efficace la plus faible'))
 t+=q('45031',line('45031',"La posologie est adaptée aux besoins du patient."))
 t+=paras('Le plafond de deux mille quatre cents milligrammes par jour décrit dans certains cas n’est pas un objectif pour une cervicalgie aiguë. Ne pas confondre cette spécialité et une présentation d’automédication. La recommandation allemande récente retient au mieux un bénéfice antalgique bref et modeste ; elle ne recommande pas les anti-inflammatoires au long cours pour la cervicalgie non spécifique.')
 t+=paras('Rubriques pédiatriques exactes, qui ne constituent pas une invitation à traiter une raideur inexpliquée à domicile :')
 for prefix in ['La dose quotidienne est de 20 mg/kg','En raison de leur dosage, les comprimés','Du fait de son dosage, Brufen']:
  t+=q('45031',line('45031',prefix))
 t+=paras('Contre-indications exactes :')+q('45031',segment('45031','· Hypersensibilité au principe actif','Mises en garde et précautions'))
 for prefix in ["A moins d'une nécessité clairement établie","La prise d'AINS à partir","L'ibuprofène est contre-indiqué au cours",'Les anti-rhumatismaux non stéroïdiens passent dans le lait maternel.']:
  t+=q('45031',line('45031',prefix))
 t+=paras('Le risque fœtal existe dès la vingtième semaine, avant la contre-indication du troisième trimestre. La notice prévoit une surveillance spécifique si un traitement nécessaire se prolonge ; ne pas interpréter le premier ou deuxième trimestre comme une autorisation de routine. Son libellé d’allaitement est conservé, sans le remplacer par une autre recommandation.', 'Ne pas associer plusieurs anti-inflammatoires. Vérifier risques digestifs, rénaux et cardiovasculaires, déshydratation, anticoagulants, antiagrégants, corticoïdes et autres interactions. Une protection gastrique peut être indiquée selon le risque ; elle ne supprime pas les risques rénaux ou cardiovasculaires.', 'Arrêter et consulter devant saignement digestif, réaction cutanée ou allergique. L’ibuprofène peut masquer une infection ; de rares méningites aseptiques sont décrites. Toute raideur fébrile nouvelle exige une évaluation, sans conclure soi-même à un effet indésirable bénin.')
 return l.subwindow('ibuprofene','Ibuprofène : indication, doses et restrictions suisses',t,(9,12))
def antalgie(l):return paras(paracetamol(l),ibuprofene(l))
