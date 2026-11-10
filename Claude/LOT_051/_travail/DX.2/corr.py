import sys,json,glob
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad')
from rep import R,sup
r=R('DX.2')
A=json.load(open('/home/user/wt/lot-051/Claude/LOT_051/audits/LOT_051_Phase_B_V0_DX.2.html.audit.json'))['corrections']
OV={}
OV["La psychothérapie cognitivo-comportementale devient donc"]=("Pendant l'allaitement, la sertraline impose l'arrêt de l'allaitement lorsqu'un traitement est nécessaire"+sup('aips-69307-59')+" et l'escitalopram impose le sevrage"+sup('aips-62641-48')+". La paroxétine ne devrait pas être administrée et, si elle est indispensable, la mère ne doit pas allaiter"+sup('aips-58636-50')+". Le lorazépam ne doit pas être utilisé en période d'allaitement"+sup('aips-36203-26')+".")
OV["Pendant la grossesse, la sertraline est à utiliser"]=("Chez la femme en âge de procréer, la sertraline ne s'utilise qu'en cas d'indication impérative, accompagnée d'une méthode de contraception appropriée, et aucune étude clinique contrôlée n'existe chez la femme enceinte"+sup('aips-69307-55')+". Chez le nouveau-né, des symptômes de sevrage ont été observés après une exposition à la sertraline pendant la grossesse"+sup('aips-69307-56')+".")
OV["Elle est l'examen de dépistage de choix"]=None
for c in A:
    av=c['avant']; ap=c['apres']
    if av.startswith("Elle est l'examen de dépistage de choix"): continue  # traité plus bas avec l'épreuve d'effort
    for k,v in OV.items():
        if v and av.startswith(k): ap=v
    hit=None
    for f in sorted(glob.glob(r.d+'p*.html')):
        t=open(f,encoding='utf-8').read()
        if t.count(av)==1: hit=f.split('/')[-1]; break
    if not hit: print('INTROUVABLE',av[:60]); r.fail+=1; continue
    t=open(r.d+hit,encoding='utf-8').read()
    if ap=='':
        if '<div class="p">'+av+'</div>' in t: r(hit,'<div class="p">'+av+'</div>','')
        elif ' '+av in t: r(hit,' '+av,'')
        else: r(hit,av,'')
    else: r(hit,av,ap)
# ergométrie
r('p09.html',"L'épreuve d'effort reste utile en ambulatoire. Elle est l'examen de dépistage de choix en l'absence de contre-indication, en raison de son coût et de son accessibilité"+sup('wfba9d7-10')+". Sa sensibilité est de",
  "L'épreuve d'effort n'est plus le test de choix : la stratégie ESC 2024 choisit le test selon la probabilité prétest"+sup('w42e5fe-15','w42e5fe-16')+". Elle retient un score calcique de 5 à 15 %, puis un scanner coronaire ou une imagerie de stress de 15 à 50 %"+sup('w42e5fe-16')+". Selon l'ancien texte HUG, la sensibilité de l'ergométrie est de")
# connecteurs
r('p01.html','Ainsi, la douleur peut survenir lors','La douleur peut survenir lors')
r('p05.html','Ainsi, ils ont un faible effet','Ils ont un faible effet')
r('p11.html','Ainsi, le clinicien nomme le trouble','Le clinicien nomme le trouble')
print('fail',r.fail)
