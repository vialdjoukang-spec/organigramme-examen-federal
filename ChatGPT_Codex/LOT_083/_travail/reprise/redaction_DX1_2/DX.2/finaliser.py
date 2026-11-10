from pathlib import Path
import json,re,hashlib,subprocess,os
B=Path(__file__).resolve().parent
R=Path('/workspace/organigramme-examen-federal')
book=json.loads((B/'paquet.json').read_text());assert not (B/'CORRESPONDANCE_IDS.json').exists()
# L'AIPS et les recommandations restent inchangées ; compactage des identifiants seulement.
(B/'paquet_AVANT_COMPACTION.json').write_text(json.dumps(book,ensure_ascii=False,indent=2)+'\n')
mapping={};a=n=0
for x in book['passages']:
    old=x['id']
    if old.startswith('aips-'):a+=1;new=f'aips-f{a}'
    else:n+=1;new=f'f{n}'
    mapping[old]=new;x['id_origine']=old;x['id']=new
for f in sorted((B/'fragments').glob('p*.html')):
    s=f.read_text()
    if f.name=='p09.html':s='<h4>9.a — La référence est clinique</h4>\n'+s
    s=s.replace('trouble anxieux généralisé coexistante','trouble anxieux généralisé coexistant')
    for old in sorted(mapping,key=len,reverse=True):
        s=s.replace('href="#sb-'+old+'">'+old+'</a>','href="#sb-'+mapping[old]+'">'+mapping[old]+'</a>')
    f.write_text(s)
(B/'CORRESPONDANCE_IDS.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n')
(B/'paquet.json').write_text(json.dumps(book,ensure_ascii=False,indent=2)+'\n')
q='Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ?'
ref=mapping['prompt-question-finale'];bloc=f'<div class="p" id="dx2-question-finale">'+q+f'<sup class="r"><a href="#sb-{ref}">{ref}</a></sup></div>'
f=B/'fragments/p14.html';s=f.read_text();assert q not in s;f.write_text(s+bloc+'\n')
contrat=json.loads((B/'contrat.json').read_text());contrat['preuves_preparation']['passages']=len(book['passages'])
for i in range(1,15):contrat['points'][str(i)]['sources']=sorted(set(re.findall('href="#sb-([^"]+)',(B/f'fragments/p{i:02d}.html').read_text())))
(B/'contrat.json').write_text(json.dumps(contrat,ensure_ascii=False,indent=2)+'\n')
F=B/'LOT_083_Phase_B_V0_DX.2.html';env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
r=subprocess.run(['python3','ChatGPT_Codex/_outils/assembler.py','--fragments',str(B/'fragments'),'--paquet',str(B/'paquet.json'),'--contrat',str(B/'contrat.json'),'--titre','DX.2 — Fibromyalgie','--sortie',str(F)],cwd=R,env=env,capture_output=True,text=True);assert r.returncode==0,r.stderr
s=F.read_text();assert s.count(bloc)==1;s=s.replace(bloc,'');disclaimer='<p class="p">Le contenu reprend les sources citées ; il n’a pas été validé cliniquement par un médecin.</p>';assert s.count(disclaimer)==1;s=s.replace(disclaimer,disclaimer+'\n'+bloc)
s=re.sub(r'\n*<li id="sb-','\n<li id="sb-',s);s=re.sub(r'</li>\n*</ol>','</li>\n</ol>',s);F.write_text(s)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(n,j):(B/n).write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
out('MANIFESTE.json',{F.name:{'octets':F.stat().st_size,'sha256':sha(F)}})
r=subprocess.run(['python3','ChatGPT_Codex/_outils/controle3.py',str(F),'--paquet',str(B/'paquet.json'),'--points','14','--ex','30'],cwd=R,env=env,capture_output=True,text=True);assert r.stdout,r.stderr;j=json.loads(r.stdout);j=j[0]if isinstance(j,list)else j;out('CONTROLE3.json',j)
print(F.stat().st_size,sha(F));print(json.dumps(j,ensure_ascii=False,indent=2))
