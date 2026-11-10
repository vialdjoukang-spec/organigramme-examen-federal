from pathlib import Path
from html.parser import HTMLParser
from collections import Counter
import json,re,hashlib,subprocess,os
B=Path(__file__).resolve().parent
R=Path('/workspace/organigramme-examen-federal')
F=B/'LOT_083_Phase_B_V0_DX.2.html'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,j):(B/n).write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
m=json.loads((B/'CORRESPONDANCE_IDS.json').read_text());q='Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ?';ref=m['prompt-question-finale'];bloc=f'<div class="p" id="dx2-question-finale">'+q+f'<sup class="r"><a href="#sb-{ref}">{ref}</a></sup></div>'
c=json.loads((B/'contrat.json').read_text());c['preuves_preparation']['passages']=len(json.loads((B/'paquet.json').read_text())['passages'])
for i in range(1,15):c['points'][str(i)]['sources']=sorted(set(re.findall('href="#sb-([^"]+)',(B/f'fragments/p{i:02d}.html').read_text())))
out('contrat.json',c)
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
r=subprocess.run(['python3','ChatGPT_Codex/_outils/assembler.py','--fragments',str(B/'fragments'),'--paquet',str(B/'paquet.json'),'--contrat',str(B/'contrat.json'),'--titre','DX.2 — Fibromyalgie','--sortie',str(F)],cwd=R,env=env,capture_output=True,text=True);assert r.returncode==0,r.stderr
s=F.read_text();assert s.count(bloc)==1;s=s.replace(bloc,'');d='<p class="p">Le contenu reprend les sources citées ; il n’a pas été validé cliniquement par un médecin.</p>';assert s.count(d)==1;s=s.replace(d,d+'\n'+bloc);s=re.sub(r'\n*<li id="sb-','\n<li id="sb-',s);s=re.sub(r'</li>\n*</ol>','</li>\n</ol>',s);F.write_text(s)
out('MANIFESTE.json',{F.name:{'octets':F.stat().st_size,'sha256':sha(F)}})
r=subprocess.run(['python3','ChatGPT_Codex/_outils/controle3.py',str(F),'--paquet',str(B/'paquet.json'),'--points','14','--ex','30'],cwd=R,env=env,capture_output=True,text=True);assert r.stdout,r.stderr;ctl=json.loads(r.stdout);ctl=ctl[0]if isinstance(ctl,list)else ctl;out('CONTROLE3.json',ctl)
class P(HTMLParser):
    def __init__(self):super().__init__();self.ids=[];self.targets=[];self.windows=[];self.images=0;self.on=False;self.depth=0;self.rows={};self.acc=[];self.key=None
    def handle_starttag(self,t,a):
        a=dict(a)
        if a.get('id'):self.ids.append(a['id'])
        if a.get('popovertarget'):self.targets.append(a['popovertarget'])
        if a.get('href','').startswith('#'):self.targets.append(a['href'][1:])
        if 'popover'in a:self.windows.append(a.get('id'))
        if t=='img':self.images+=1
        if t=='div':
            if self.on:self.depth+=1
            elif a.get('class')=='p'and a.get('id'):self.on=True;self.depth=1;self.acc=[];self.key=a['id']
    def handle_endtag(self,t):
        if t=='div'and self.on:
            self.depth-=1
            if self.depth==0:self.rows[self.key]=''.join(self.acc);self.on=False
    def handle_data(self,d):
        if self.on:self.acc.append(d)
x=P();x.feed(s);dups=[k for k,v in Counter(x.ids).items()if v>1];missing=sorted(set(x.targets)-set(x.ids));structure={'fichier':str(F),'octets':F.stat().st_size,'sha256':sha(F),'ids':len(x.ids),'fenetres':len(x.windows),'IDs_dupliques':dups,'cibles_absentes':missing,'images':x.images,'ligne_max':max(map(len,s.splitlines())),'question_finale_exacte_unique':s.count(q)==1,'FIN_exact':s.rstrip().endswith('<!-- FIN_FICHIER LOT_083_Phase_B_V0_DX.2 -->'),'controle_original':ctl['verdict'],'P3':'Audit indépendant requis ; aucune note ni verdict clinique du rédacteur'}
out('CONTROLE_LIVRAISON.json',structure)
assert 100000<=F.stat().st_size<=200000 and not dups and not missing and not x.images;assert structure['ligne_max']<3000 and structure['question_finale_exacte_unique']and structure['FIN_exact'];assert not any(k.startswith(('A_','C_'))for k in ctl['defauts'])
spec=[('Q1a',1,['Le Royal College of Physicians','La HAS, dans sa']),('Q1b',1,['Les anciennes appellations','Une maladie inflammatoire']),('Q2a',2,['La publication suisse','La HAS rapporte']),('Q2b',2,['La Ligue décrit','Le RCP rapporte','L’isolement social']),('Q3a',3,['Des événements physiques','Des travaux sur','Au niveau des réseaux']),('Q3b',3,['Modulation douloureuse centrale','Le lien perturbation']),('Q4a',4,['Après un effort intense','Après un traumatisme','Une présentation évocatrice']),('Q4b',4,['Myopathie inflammatoire','Myopathie hypothyroïdienne','Rhumatisme inflammatoire']),('Q5a',5,['Où la douleur','Le réveil apporte','Quels médicaments']),('Q5b',5,['Une douleur musculaire aiguë','Une idéation suicidaire']),('Q6a',6,['L’examen commence','La force normale']),('Q6b',6,['Pour les mains','La palpation de la capsule','Le clinicien documente']),('Q7',7,['Les signes fonctionnels comprennent','Les signes fonctionnels sont','Le signe fonctionnel est','Les signes fonctionnels comprennent les difficultés']),('Q8a',8,['Le diagnostic positif','Le WPI est au moins','Le SSS cote','Le score ajoute']),('Q8b',8,['Le WPI compte','Les douleurs de mâchoire','Un tableau cohérent']),('Q9a',9,['Le diagnostic de référence']),('Q9b',9,['La HAS recommande','DFGe inférieur','Chez une mère','Une suspicion de myosite']),('Q10',10,['L’arbre garde','Si une menace','Si le tableau']),('Q11a',11,['La HAS propose','Le plan précise']),('Q11b',11,['EULAR donne','L’activité est choisie','L’autogestion peut']),('Q11c',11,['Le clinicien recherche d’abord','Une forte suspicion']),('Q11d',11,['L’AIPS recommande 60','La dose initiale AIPS','Aucun ajustement','La duloxétine ne doit pas']),('Q11e',11,['La Ligue suisse recommande','Les consultations sont','Chaque réévaluation','La menace aiguë éventuelle']),('Q12',12,['La Ligue recommande','Chez une personne symptomatique','L’activité adaptée']),('Q13',13,['La fibromyalgie associe','Une recommandation européenne']),('Q14',14,['Une forte douleur','La duloxétine possède','Le gadolinium est-il'])]
idx=[]
for key,n,needles in spec:
    ids=[]
    for needle in needles:
        matches=[i for i,v in x.rows.items()if i.startswith(f'dx2-p{n}-')and needle in v]
        if not matches:
            # Certains repères sont des en-têtes de table, des questions ou des branches de liste.
            assert needle in (B/f'fragments/p{n:02d}.html').read_text(),(key,needle)
            ids.append(f'dx2-p{n}')
        else:ids.append(matches[0])
    assert set(ids)<=set(x.ids),(key,ids)
    idx.append({'question':key,'point':n,'fragments':f'fragments/p{n:02d}.html','cibles':list(dict.fromkeys(ids)),'reperes_textuels':needles})
out('INDEX_Q.json',{'fichier':str(F),'sha256':sha(F),'statut':'Repérage documentaire uniquement ; aucune notation P3','grille':'26questions, Q11 exactement cinq questions ; images différées','questions':idx,'sources':'paquet.json ; id_origine et CORRESPONDANCE_IDS.json','limites':'HELP.md'})
out('REMISE.json',{'lot':'083','dx':2,'nom':'Fibromyalgie','redacteur':'/root/sources_cutanees','date':'2026-11-10','fichier':str(F),'octets':F.stat().st_size,'sha256':sha(F),'paquet':str(B/'paquet.json'),'sha256_paquet':sha(B/'paquet.json'),'contrat':str(B/'contrat.json'),'sha256_contrat':sha(B/'contrat.json'),'controle':'CONTROLE3.json','structure':'CONTROLE_LIVRAISON.json','index_Q':'INDEX_Q.json','statut':'Copie privée complète pour audit indépendant et dépôt par root','P3':'Aucun autoaudit','Git':'Aucun canonique ni Git modifié'})
print(json.dumps(structure,ensure_ascii=False,indent=2))
