"""Spécifications exactes des schémas pédagogiques ; couleurs conventionnelles."""
import json,importlib.util
from pathlib import Path
D=Path(__file__).resolve().parent;B=D.parents[2]
spec=importlib.util.spec_from_file_location('dessinateur',B/'outils/dessinateur/dessinateur.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def f(tag,**attrs):return {'tag':tag,'attrs':attrs}
def ell(x,y,rx,ry,color):return f('ellipse',cx=x,cy=y,rx=rx,ry=ry,fill=color)
def path(d,color='none',stroke='#8c2d32',w=4,**kw):return f('path',d=d,fill=color,stroke=stroke,**{'stroke-width':w,**kw})
def ring(x,y,rx,ry):
 # Ellipse rendue comme deux arcs pour permettre le pointillé du contrôleur.
 d=f'M{x-rx} {y} a{rx} {ry} 0 1 0 {2*rx} 0 a{rx} {ry} 0 1 0 {-2*rx} 0'
 return [path(d,stroke='#152538',w=5),path(d,stroke='#ffe766',w=3,**{'stroke-dasharray':'8 6'})]
def rep(x,y,n,d):return {'xy':[x,y],'nom':n,'definition':d}
def view(t,shapes,reps,ex):return {'titre':t,'formes':shapes,'reperes':reps,'explication':ex}
def save(n,title,url,views):
 s={'id':f'i018-dx{n}','titre':title,'auteur':'Codex — schéma pédagogique original, CC BY 4.0','source_medicale':url,'acces_le':'2026-10-31','vues':views}
 (D/f'dx{n}.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n');(D/f'dx{n}.html').write_text(m.render(s))
H='https://www.hug.ch/ophtalmologie/'; C='https://couf.fr/xhtml/'
# 1 : géométrie qualitative de la focalisation, pas de puissance chiffrée.
views=[]
for title,focus,detail in [('Repos : focalisation sur la rétine',510,'Situation de référence simplifiée.'),('Myopie : foyer en avant de la rétine',425,'Un verre divergent peut déplacer le foyer vers la rétine.'),('Hypermétropie au repos : foyer en arrière',610,'Un verre convergent peut ramener le foyer sur la rétine ; l’accommodation peut masquer une partie du défaut.')]:
 shapes=[ell(390,160,150,115,'#e2eef5'),ell(280,160,20,68,'#73c7d0'),f('line',x1=510,x2=510,y1=60,y2=260,stroke='#986347',**{'stroke-width':7})]
 for y in [110,210]:shapes += [path(f'M70 {y} L280 {y} L{focus} 160',stroke='#16809e',w=3)]
 shapes+=ring(focus,160,15,15)
 views.append(view(title,shapes,[rep(280,80,'Système optique','Cornée et cristallin sont regroupés en une lentille équivalente pour expliquer la convergence.'),rep(510,260,'Plan rétinien','Ligne brune représentant le plan où l’image doit être focalisée.'),rep(focus,160,'Foyer théorique',detail)],'Objet éloigné, accommodation au repos ; dimensions arbitraires. L’astigmatisme et la presbytie ne sont pas représentés. La réfraction réelle détermine la correction.'))
save(1,'Où se forme le foyer ?',H+'chirurgie-refractive-loeil',views)
# 2 : comparaison de deux cristallins, sans patient photographié.
shapes=[]
for x,opaque in [(210,False),(510,True)]:
 shapes += [ell(x,160,60,110,'#c2eaf1' if not opaque else '#b9a486')]
 for y in [110,160,210]:shapes += [path(f'M{x-140} {y} L{x-50} {y}',stroke='#16809e',w=3)]
 if opaque:
  for dx,dy in [(-20,-45),(20,-10),(-15,35)]:shapes += [ell(x+dx,160+dy,22,27,'#8d8170')]
  shapes+=ring(x,160,68,117)
 else:
  for y in [110,160,210]:shapes += [path(f'M{x+50} {y} L{x+130} 160',stroke='#16809e',w=3)]
save(2,'Cristallin transparent et cristallin opacifié',H+'operation-cataracte',[view('Comparaison de transparence',shapes,[rep(210,160,'Cristallin transparent','La lumière traverse le cristallin et participe à la formation d’une image nette.'),rep(510,160,'Opacités cristalliniennes','Les plages brunes figurent une perte de transparence, entourée de pointillés. Leur forme est illustrative, sans classification de cataracte.')],'Une opacité doit être confrontée à la gêne et à la lampe à fente. Une autre atteinte, notamment rétinienne, peut limiter la vision ; ce dessin ne prédit pas le résultat opératoire.')])
# 3 : drusen et liquide dans deux vues distinctes, jamais assimilés à un OCT réel.
base=[f('rect',x=60,y=220,width=600,height=45,fill='#d69b8b')]
drusen=base+[path('M60 210 L260 210 Q310 155 360 210 Q410 168 455 210 L660 210',stroke='#885339',w=12),path('M60 170 L250 170 Q310 130 370 170 Q415 140 465 170 L660 170',stroke='#4baea0',w=28)]+ring(355,192,125,42)
fluid=base+[f('rect',x=60,y=208,width=600,height=12,fill='#885339'),path('M60 170 L250 170 Q355 85 465 170 L660 170',stroke='#4baea0',w=28),path('M255 201 Q355 125 460 201 Z',color='#b5dff6',stroke='#6fa5c7')]+ring(355,178,115,34)
save(3,'Macula : distinguer dépôts et liquide',C+'Ch015_267-281_B9782294786624500241.xhtml/',[view('Dépôts sous l’épithélium pigmentaire',drusen,[rep(355,195,'Drusen','Dépôts représentés sous la ligne brune de l’épithélium pigmentaire, qu’ils soulèvent. Ils ne suffisent pas à prouver une activité néovasculaire.')],'Vert : rétine externe simplifiée ; brun : épithélium pigmentaire ; rose : plan choroïdien. Les drusen ne sont pas une collection liquidienne.'),view('Exsudation : liquide sous-rétinien schématique',fluid,[rep(355,175,'Liquide sous-rétinien','Zone bleue située au-dessus de l’épithélium pigmentaire et sous la rétine. Une activité néovasculaire est une cause possible, à confirmer par l’imagerie.')],'Ce schéma ne représente ni tous les sites possibles du liquide ni la forme atrophique. Il ne remplace pas un OCT et ne permet pas de décider seul d’une injection.')])
# 4 : excavation comparée, sans seuil cup/disc inventé.
shapes=[]
for x,rx,ry in [(210,34,45),(510,65,95)]:shapes += [ell(x,160,100,120,'#db927b'),ell(x,160,rx,ry,'#f8e7c0')]
shapes+=ring(510,160,65,95)
save(4,'Papille : excavation et anneau neurorétinien',C+'Ch014_249-265_B978229478662450023X.xhtml/',[view('Deux configurations conceptuelles',shapes,[rep(210,160,'Excavation centrale','Dépression centrale physiologique, ici entourée d’un anneau large.'),rep(510,160,'Excavation élargie','Un élargissement peut accompagner une perte de tissu neurorétinien ; les pointillés en indiquent les limites dessinées.'),rep(600,160,'Anneau résiduel','Zone rose périphérique amincie dans cet exemple.')],'Les dimensions sont arbitraires : aucun rapport seuil n’est proposé. Une grande excavation peut être physiologique ; interpréter avec taille papillaire, asymétrie, fibres, champ visuel et évolution.')])
# Fond d’œil conceptuel : papille à gauche, macula à droite ; aucune latéralité patient.
def fond(bg='#ebbd9b'):
 return [ell(360,160,255,140,bg),ell(235,160,24,31,'#fae5b6'),ell(450,160,23,20,'#a5604c')]
def vessels(color,w):return [path('M240 157 Q310 95 350 80 Q410 60 490 75 M240 164 Q315 230 380 245 Q440 256 510 240',stroke=color,w=w)]
# 5 : rupture de barrière et prolifération séparées.
a=fond()+vessels('#a73c43',6)+[ell(350,95,7,7,'#b51c40'),ell(395,238,10,6,'#b51c40')]+ring(350,95,22,18)
b=fond()+vessels('#a73c43',6)+[path('M235 140 Q210 110 243 103 Q275 100 258 125 Q224 122 222 98 M240 126 L280 85 M250 113 L280 110',stroke='#b51c40',w=3)]+ring(245,111,48,40)
save(5,'Rétinopathie diabétique : deux familles de signes',H+'formes-retinopathie-diabetique',[view('Atteinte microvasculaire non proliférante',a,[rep(350,95,'Anomalie capillaire focale','Point rouge illustrant une dilatation capillaire ou un saignement punctiforme ; la distinction exige l’examen réel.')],'Des lésions peuvent exister sans plainte visuelle. Ce dessin ne quantifie ni le stade ni l’œdème maculaire.'),view('Prolifération vasculaire',b,[rep(245,111,'Néovaisseaux','Réseau rouge fin dessiné près de la papille, fragile et susceptible de saigner. Il figure une prolifération, pas une photographie.')],'La géométrie est conventionnelle. Les néovaisseaux peuvent avoir d’autres localisations ; leur présence impose une évaluation spécialisée.')])
# 6 : stase et hémorragies, sans image mimant une angiographie.
a=fond()+vessels('#6c3c71',12)
for x,y in [(325,105),(390,74),(480,88),(325,215),(420,245),(485,225)]:a+=[ell(x,y,14,7,'#9e2147')]
a+=ring(368,100,65,43)
save(6,'Occlusion veineuse : stase et saignements',H+'occlusion-veineuse-retinienne',[view('Signes représentés au fond d’œil',a,[rep(335,100,'Stase et hémorragies','Veines épaissies en violet et plages rouges de saignement. La disposition est simplifiée et ne classe pas une occlusion centrale ou de branche.'),rep(450,160,'Région maculaire','L’œdème peut atteindre cette région et réduire l’acuité ; sa mesure nécessite notamment l’OCT.')],'Les couleurs sont conventionnelles. Ce schéma ne montre pas la perfusion et ne permet pas de conclure à une forme ischémique.')])
# 9 : contraste fovéal, sans affirmer sa présence constante.
a=fond('#eee6d3')+vessels('#a16d5e',3)+[ell(450,160,22,18,'#b33143')]+ring(450,160,33,29)
save(9,'Occlusion artérielle : pâleur et contraste fovéal',C+'Ch016_283-302_B9782294786624500253.xhtml/',[view('Aspect possible après installation de l’ischémie',a,[rep(365,80,'Pâleur rétinienne','Le fond clair représente l’œdème ischémique de la rétine interne.'),rep(450,160,'Contraste rouge fovéal','La fovéola paraît rouge par contraste avec la rétine pâle. Le dessin ne représente pas une hémorragie fovéale.')],'Ces signes peuvent manquer au début. Une baisse brutale impose une évaluation urgente sans attendre cet aspect ; le dessin ne précise pas la cause de l’occlusion.')])
# 10 : visualiser l’atteinte papillaire, sans inventer de coupe histologique.
a=[ell(220,160,85,105,'#d99c83'),ell(220,160,30,42,'#fae5bd'),ell(510,160,105,125,'#eee4c9'),ell(510,160,30,42,'#f7efdb')]+ring(510,160,112,132)
save(10,'Atteinte ischémique de la tête du nerf optique',C+'Ch016_283-302_B9782294786624500253.xhtml/',[view('Papille de référence et œdème pâle schématique',a,[rep(220,160,'Papille de référence','Disque optique dessiné à limites régulières.'),rep(510,160,'Œdème papillaire pâle','Gonflement et pâleur représentés autour de la papille. Une neuropathie optique ischémique antérieure peut présenter cet aspect.')],'Cet aspect ne prouve pas une artérite à cellules géantes : il existe des formes non artéritiques. Le contexte, les examens inflammatoires et l’imagerie ou l’histologie artérielle guident la confirmation, sans retarder la prise en charge urgente si la suspicion est forte.')])
print('8 composants,',sum(len(json.loads(p.read_text())['vues']) for p in D.glob('dx*.json')),'vues')
