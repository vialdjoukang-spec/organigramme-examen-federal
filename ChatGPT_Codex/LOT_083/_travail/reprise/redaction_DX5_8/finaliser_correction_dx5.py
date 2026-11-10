from pathlib import Path
import re,json,hashlib,difflib,subprocess,os
B=Path(__file__).parent;D=B/'DX.5';pk=json.loads((D/'paquet.json').read_text());t=(B/'DX5_CORRECTION_SOURCES_SEMIO_0.txt').read_text();a=t.index('### **2\\.6. Dyspnée**');b=t.index('### **2\\.6.1.',a);s=t[a:b];pk['passages'].append(dict(id='f5-c9',source='UMVF/UNESS — Dyspnée et fréquence respiratoire, 2013',url='https://archives.uness.fr/sites/campus-unf3s-2014/semiologie/enseignement/esemio9/site/html/cours.pdf',date='2026-11-10',texte=s,archive=str((B/'DX5_CORRECTION_SOURCES_SEMIO_0.txt').resolve()),offset_debut=a,offset_fin=b,sha256=hashlib.sha256(s.encode()).hexdigest()));(D/'paquet.json').write_text(json.dumps(pk,ensure_ascii=False,indent=2));ns={x['id']:str(i+1) for i,x in enumerate(pk['passages'])}
def r(id):return '<sup class="r"><a href="#sb-'+id+'">'+ns[id]+'</a></sup>'
f=D/'fragments/p07.html';t=f.read_text();t=t.replace('La toux est une expulsion brusque d’air, ressentie et rapportée par le patient','La toux est un phénomène expulsif réflexe qui assure le drainage bronchique'+r('f5-c3'));t=t.replace('La dyspnée est une sensation de difficulté respiratoire','La dyspnée est une sensation de difficulté respiratoire'+r('f5-c9'));f.write_text(t)
for n in [6,7,9,12]:
 f=D/f'fragments/p{n:02}.html';t=f.read_text()
 def add(m):
  v=m[0];ids=re.findall(r'href="#sb-(f5-c\d+)"',v)
  if not ids and not ('L’OFSP privilégie' in v):return v
  ids=ids or ['f5-13'];ref=r(ids[0]);return re.sub(r'(?<!\d)\. (?=[A-ZÀÉÈ])',ref+'. ',v)
 t=re.sub(r'<div class="p">.*?</div>',add,t);f.write_text(t)
# Remove one repeated information paragraph (same focused local infections guidance retained at points5/9).
f=D/'fragments/p04.html';t=f.read_text();pat=r'<div class="p">Les infections localisées peuvent modifier.*?</div>\n?';m=re.search(pat,t,re.S);j=json.loads((D/'CORRECTIONS_P3.json').read_text());j['retraits'].append(dict(point=4,raison='Rappel de symptômes localisés conservé dans anamnèse ; place pour citations correctives',html=m[0]));f.write_text(re.sub(pat,'',t,flags=re.S));j['nouveaux_passages'].append('f5-c9');(D/'CORRECTIONS_P3.json').write_text(json.dumps(j,ensure_ascii=False,indent=2))
(D/'CORRECTIONS_P3.diff').write_text(''.join(''.join(difflib.unified_diff((D/'avant_correction_P3'/f.name).read_text().splitlines(True),f.read_text().splitlines(True),fromfile='avant/'+f.name,tofile='apres/'+f.name)) for f in sorted((D/'fragments').glob('*.html'))))
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1');f=D/'LOT_083_Phase_B_V0_DX.5.html';subprocess.run(['python3','outils/assembler.py','--fragments',str(D/'fragments'),'--paquet',str(D/'paquet.json'),'--contrat',str(D/'contrat.json'),'--titre','LOT 083 — DX.5 — Grippe saisonnière','--sortie',str(f)],env=env,check=True)
t=f.read_text();m=re.search(r'<div class="p">Ce cours, lu seul.*?</div>',t);t=t[:m.start()]+t[m.end():];t=t.replace('</main>',m[0]+'\n</main>')
for tag in ['</li>','</tr>','</section>']:t=t.replace(tag,tag+'\n')
f.write_text(t);sha=hashlib.sha256(f.read_bytes()).hexdigest();(D/'MANIFESTE.json').write_text(json.dumps({f.name:dict(octets=f.stat().st_size,sha256=sha)},indent=2))
with (D/'CONTROLE3.json').open('w') as out:subprocess.run(['python3','outils/controle3.py',str(f),'--paquet',str(D/'paquet.json'),'--points','14','--min','100000','--max','200000'],stdout=out,env=env)
print(f.stat().st_size,sha)
