from pathlib import Path
from html.parser import HTMLParser
from collections import Counter
import json,re,hashlib,subprocess,os
B=Path(__file__).resolve().parent
R=Path('/workspace/organigramme-examen-federal')
mapping=json.loads((B/'CORRESPONDANCE_IDS.json').read_text())
q='Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ?'
f=B/'fragments/p14.html';s=f.read_text();assert q not in s
ref=mapping['prompt-question-finale']
bloc=f'<div class="p" id="dx1-question-finale">'+q+f'<sup class="r"><a href="#sb-{ref}">{ref}</a></sup></div>'
f.write_text(s+bloc+'\n')
final=B/'LOT_083_Phase_B_V0_DX.1.html'
cmd=['python3','ChatGPT_Codex/_outils/assembler.py','--fragments',str(B/'fragments'),'--paquet',str(B/'paquet.json'),'--contrat',str(B/'contrat.json'),'--titre','DX.1 — Syndrome douloureux myofascial','--sortie',str(final)]
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
r=subprocess.run(cmd,cwd=R,env=env,capture_output=True,text=True);assert r.returncode==0,r.stderr
s=final.read_text();assert s.count(bloc)==1;s=s.replace(bloc,'')
fin='<p class="p">Le contenu reprend les sources citées ; il n’a pas été validé cliniquement par un médecin.</p>';assert s.count(fin)==1;s=s.replace(fin,fin+'\n'+bloc)
s=re.sub(r'\n*<li id="sb-','\n<li id="sb-',s);s=re.sub(r'</li>\n*</ol>','</li>\n</ol>',s);final.write_text(s)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,d):(B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
out('MANIFESTE.json',{final.name:{'octets':final.stat().st_size,'sha256':sha(final)}})
r=subprocess.run(['python3','ChatGPT_Codex/_outils/controle3.py',str(final),'--paquet',str(B/'paquet.json'),'--points','14','--ex','30'],cwd=R,env=env,capture_output=True,text=True)
assert r.stdout,r.stderr;c=json.loads(r.stdout);c=c[0]if isinstance(c,list)else c;out('CONTROLE3.json',c)
class T(HTMLParser):
    def __init__(self):super().__init__();self.ids=[];self.targets=[];self.fen=[];self.images=0;self.on=False;self.depth=0;self.acc=[];self.rows={};self.key=None
    def handle_starttag(self,t,a):
        a=dict(a)
        if a.get('id'):self.ids.append(a['id'])
        if a.get('popovertarget'):self.targets.append(a['popovertarget'])
        if a.get('href','').startswith('#'):self.targets.append(a['href'][1:])
        if 'popover'in a:self.fen.append(a.get('id'))
        if t=='img':self.images+=1
        if t=='div':
            if self.on:self.depth+=1
            elif a.get('class')=='p'and a.get('id'):self.on=True;self.depth=1;self.key=a['id'];self.acc=[]
    def handle_endtag(self,t):
        if t=='div'and self.on:
            self.depth-=1
            if self.depth==0:self.rows[self.key]=''.join(self.acc);self.on=False
    def handle_data(self,d):
        if self.on:self.acc.append(d)
x=T();x.feed(s);dups=[k for k,v in Counter(x.ids).items()if v>1];missing=sorted(set(x.targets)-set(x.ids));last='<!-- FIN_FICHIER LOT_083_Phase_B_V0_DX.1 -->'
struct={'fichier':str(final),'octets':final.stat().st_size,'sha256':sha(final),'ids':len(x.ids),'fenetres':len(x.fen),'IDs_dupliques':dups,'cibles_absentes':missing,'images':x.images,'ligne_max':max(map(len,s.splitlines())),'question_finale_exacte_unique':s.count(q)==1,'FIN_exact':s.rstrip().endswith(last),'controle_original':c,'P3':'Audit indépendant requis, aucun score d’auteur'}
out('CONTROLE_LIVRAISON.json',struct)
assert 100000<=final.stat().st_size<=200000;assert not dups and not missing and not x.images;assert struct['ligne_max']<3000 and struct['question_finale_exacte_unique']and struct['FIN_exact']
def trouves(point,needles):
    out=[]
    for needle in needles:
        keys=[k for k,v in x.rows.items()if k.startswith(f'dx1-p{point}-')and needle in v]
        assert keys,(point,needle)
        out.append(keys[0])
    return out
spec=[
('Q1a',1,['La DGN, dans sa recommandation']),('Q1b',1,['La fibromyalgie correspond','Une douleur référée musculaire']),
('Q2a',2,['La DGN situe','Des situations de travail','Certaines douleurs apparues']),('Q2b',2,['La DGN situe','La revue suisse']),
('Q3a',3,['La surcharge et','Des études décrivent','Les travaux expérimentaux']),('Q3b',3,['Une contrainte prolongée','Les médiateurs locaux','La douleur modifie']),
('Q4a',4,['Une douleur musculaire aiguë','Après un traumatisme']),('Q4b',4,['Rhabdomyolyse après effort','Radiculopathie ou compression']),
('Q5a',5,['Où la douleur','Une carte de la douleur']),('Q5b',5,['Douleur aiguë après effort','Une infection systémique']),
('Q6a',6,['L’examen de la force commence','Une personne sans plainte']),('Q6b',6,['Le clinicien recherche d’abord','Une stimulation du point']),
('Q7',7,['Les signes fonctionnels sont','Le signe fonctionnel est','Les signes fonctionnels comprennent']),
('Q8a',8,['La recommandation DGN','Socle : bande tendue']),('Q8b',8,['Une irradiation seule','La découverte d’un point latent']),
('Q9a',9,['La DGN décrit un diagnostic']),('Q9b',9,['Approche biologique','Si l’IRM est contre-indiquée','Mère enceinte ou allaitante']),
('Q10',10,['Un choc direct','Si le point palpé','Si la présentation change']),
('Q11a',11,['Le plan fixe avec','Une réponse satisfaisante']),('Q11b',11,['Le programme peut associer','Les techniques de tissus mous']),('Q11c',11,['Une suspicion de rhabdomyolyse','Une douleur post-traumatique']),('Q11d',11,['Adulte de plus de 40','Clairance de créatinine','L’hypersensibilité au paracétamol']),('Q11e',11,['Pendant la grossesse','L’âge seul','Le suivi reprend','La continuité organise']),
('Q12',12,['Les situations décrites','Le repérage précoce','Le programme d’un tableau chronique']),('Q13',13,['Le diagnostic myofascial','L’antalgie d’une indication']),('Q14',14,['Une douleur provoquée','Le paracétamol doit-il'])]
idx=[]
for key,n,needles in spec:
    ids=trouves(n,needles)
    if key=='Q10':ids.insert(0,'dx1-p10')
    idx.append({'question':key,'point':n,'fragments':f'fragments/p{n:02d}.html','cibles':ids})
out('INDEX_Q.json',{'fichier':str(final),'sha256':sha(final),'statut':'Index de repérage uniquement ; aucune note ni conclusion P3','grille':'26questions, Q11 en cinq questions ; images différées','questions':idx,'sources':'paquet.json ; id_origine et CORRESPONDANCE_IDS.json','limites':'HELP.md'})
out('REMISE.json',{'lot':'083','dx':1,'nom':'Syndrome douloureux myofascial','redacteur':'/root/sources_cutanees','date':'2026-11-10','fichier':str(final),'octets':final.stat().st_size,'sha256':sha(final),'paquet':str(B/'paquet.json'),'sha256_paquet':sha(B/'paquet.json'),'contrat':str(B/'contrat.json'),'sha256_contrat':sha(B/'contrat.json'),'controle':'CONTROLE3.json','structure':'CONTROLE_LIVRAISON.json','index_Q':'INDEX_Q.json','statut':'Copie privée complète pour audit indépendant et dépôt par root','P3':'Aucun autoaudit','Git':'Aucun Git ni canonique modifié'})
print(json.dumps(struct,ensure_ascii=False,indent=2))
