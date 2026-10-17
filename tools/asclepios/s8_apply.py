"""Asclépios · applique le bloc S8 (s8_a.py, s8_b.py) à data/TIP.json et data/NOT.json extraits de main.
Usage : python3 tools/json_inject.py extract TIP && python3 tools/json_inject.py extract NOT &&
        python3 tools/asclepios/s8_apply.py && python3 tools/json_inject.py inject TIP && python3 tools/json_inject.py inject NOT"""
import json,sys,os,re
sys.path.insert(0,os.path.dirname(__file__))
import tip_sources as TS
from s8_a import S8 as A
from s8_b import S8 as B
S8={**A,**B}
FIX6={ # puces tronquées de la rubrique 6 (S8.1 à S8.7), remplacées en entier
'S8.1':('• <b>Syndrome de la triade létale','• <b>Syndrome de la triade létale (chirurgie écourtée)</b> : baisse progressive de la conscience, frissons, saignement diffus en nappe qui ne vient pas d’une plaie précise ; l’hypothermie, l’acidose et le trouble de la coagulation s’aggravent l’un l’autre et imposent une chirurgie écourtée.'),
'S8.2':[('• <b>Brûlure grave','• <b>Brûlure grave (profonde, étendue ou dans une zone critique)</b> : la zone profonde fait peu mal, car les terminaisons nerveuses sont détruites, alors que la périphérie reste très douloureuse ; on cherche des signes de choc et une atteinte des voies aériennes.'),('• <b>Gelure périphérique','• <b>Gelure périphérique</b> : fourmillements, puis perte de sensibilité de la zone, qui devient dure comme du bois ; le réchauffement est très douloureux.')],
'S8.4':('• <b>Luxation antérieure gléno-humérale','• <b>Luxation antérieure de l’épaule</b> : douleur aiguë, impossibilité de bouger le bras, bras tenu écarté du corps et tourné vers l’extérieur, relief de l’épaule perdu sous l’acromion.'),
'S8.5':('• <b>Encéphalopathie anoxo-ischémique','• <b>Lésion du cerveau par manque d’oxygène</b> : conscience altérée (score de Glasgow de 8 ou moins), coma, convulsions ou secousses musculaires ; le pronostic se juge après plusieurs jours, pas à l’arrivée.'),
'S8.6':('• <b>Syndrome d’obstruction œsophagienne','• <b>Syndrome d’obstruction œsophagienne</b> : blocage brutal pendant un repas, douleur à la déglutition, salive qui s’écoule, et impossibilité d’avaler même la salive si l’obstruction est complète (ESGE 2016, recommandation 7).'),
'S8.7':('• <b>Hématome extradural','• <b>Hématome extradural</b> : l’intervalle libre classique n’existe que chez une partie des patients : perte de connaissance brève, puis amélioration, puis aggravation rapide avec dilatation d’une pupille.'),
}
def ddx(n,urg,ce,di,de,co,pi,src):
  if not src and 'À vérifier' not in ce+di+de+co+pi: co+=' (À vérifier : aucune source européenne lue pour ce point.)'
  h=('<b style="color:var(--bad)">À ne pas manquer.</b><br>' if urg else '')
  return h+''.join(f'• <b>{k}</b> : {v}<br>' for k,v in (('Ce que c’est',ce),('Ce qui la distingue',di),('Délai',de),('Conduite',co),('Piège',pi)))
T=json.load(open('data/TIP.json'));N=json.load(open('data/NOT.json'))
st={'ddx':0,'rubriques':0,'puces6':0}
for c,E in S8.items():
  t=T[c];v=t.setdefault('v',{'S':[],'c':[None]*14,'d':[]})
  def sid(k):
    d=getattr(TS,k)
    for s in v['S']:
      if s['u']==d['u']:s.update({x:d[x] for x in 't o u n a'.split()});return s['id']
    i=max([s['id'] for s in v['S']]+[0])+1;v['S'].append({'id':i,**d});return i
  allids=sorted({sid(k) for k in E['src']})
  for i in (3,4,12,13):
    t['c'][i]=E[f'c{i}'];st['rubriques']+=1
    ids=[sid(k) for k in E['src'] if True];v['c'][i]=['complété',sorted(set(ids))]
  if E['c6']:t['c'][6]=E['c6'];v['c'][6]=['complété',allids];st['rubriques']+=1
  elif c in FIX6:
    L=FIX6[c] if isinstance(FIX6[c],list) else [FIX6[c]]
    parts=t['c'][6].split('<br>')
    for pre,new in L:
      k=[j for j,p in enumerate(parts) if p.startswith(pre)];assert len(k)==1,(c,pre);parts[k[0]]=new;st['puces6']+=1
    t['c'][6]='<br>'.join(parts)
  assert N[c][0]==[] and t['d']==[],c
  N[c][0]=[d[0] for d in E['dd']];t['d']=[ddx(*d) for d in E['dd']]
  v['d']=[(['complété',sorted({sid(k) for k in d[7]})] if d[7] else None) for d in E['dd']];st['ddx']+=len(E['dd'])
json.dump(T,open('data/TIP.json','w'),ensure_ascii=False);json.dump(N,open('data/NOT.json','w'),ensure_ascii=False)
print(st)
