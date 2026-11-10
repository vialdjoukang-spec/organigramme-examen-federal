from pathlib import Path
from html.parser import HTMLParser
from collections import Counter
import re,json,hashlib,subprocess,os
B=Path(__file__).resolve().parent
R=B.parents[4]
F=B/'LOT_082_Phase_B_V0_DX.7.html'
def out(n,d):(B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
s=F.read_text();qs=re.findall(r'<div\b[^>]*id="dx7-question-finale"[^>]*>.*?</div>',s,re.S);assert len(qs)==1
s=s.replace(qs[0],'')
fin='<p class="p">Le contenu reprend les sources citées ; il n’a pas été validé cliniquement par un médecin.</p>';assert s.count(fin)==1
s=s.replace(fin,fin+'\n'+qs[0]);s=re.sub(r'\n*<li id="sb-','\n<li id="sb-',s);s=re.sub(r'</li>\n*</ol>','</li>\n</ol>',s)
F.write_text(s);out('MANIFESTE.json',{F.name:{'octets':F.stat().st_size,'sha256':sha(F)}})
cmd=['python3','ChatGPT_Codex/_outils/controle3.py',str(F),'--paquet',str(B/'paquet.json'),'--ex','40']
r=subprocess.run(cmd,capture_output=True,text=True,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'));c=json.loads(r.stdout);c=c[0] if isinstance(c,list) else c;out('CONTROLE3.json',c)
class V(HTMLParser):
    def __init__(self):super().__init__();self.ids=[];self.targets=[];self.fen=[];self.images=0
    def handle_starttag(self,t,a):
        a=dict(a)
        if a.get('id'):self.ids.append(a['id'])
        if a.get('popovertarget'):self.targets.append(a['popovertarget'])
        if a.get('href','').startswith('#'):self.targets.append(a['href'][1:])
        if 'popover'in a:self.fen.append(a.get('id'))
        if t=='img':self.images+=1
v=V();v.feed(s);dups=[i for i,n in Counter(v.ids).items() if n>1];missing=sorted(set(v.targets)-set(v.ids))
q='Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ?'
report={'fichier':str(F),'octets':F.stat().st_size,'sha256':sha(F),'ids_total':len(v.ids),'ids_distincts':len(set(v.ids)),'ids_dupliques':dups,'cibles_absentes':missing,'fenetres':len(v.fen),'images':v.images,'ligne_max':max(map(len,s.splitlines())),'question_finale_exacte_unique':s.count(q)==1,'FIN_exact':s.rstrip().endswith('<!-- FIN_FICHIER LOT_082_Phase_B_V0_DX.7 -->'),'controle_original':c,'audit_P3':'Requis par auditeur indépendant ; aucun score antérieur transféré.'}
out('CONTROLE_LIVRAISON.json',report)
assert not dups and not missing and not v.images and report['question_finale_exacte_unique'] and report['FIN_exact'] and report['ligne_max']<3000
print(json.dumps(report,ensure_ascii=False,indent=2))
