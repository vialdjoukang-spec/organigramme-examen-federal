from pathlib import Path
import importlib.util,hashlib,json,re,collections
r=Path('ChatGPT_Codex/LOT_083');spec=importlib.util.spec_from_file_location('controle_original','outils/controle3.py');c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
seen=collections.defaultdict(list);versions=[]
question='Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ?'
for f in sorted(r.glob('LOT_083_Phase_*.html')):
 raw=f.read_bytes();versions.append({'fichier':str(f),'sha256':hashlib.sha256(raw).hexdigest(),'octets':len(raw)})
 for tag,brut,t in c.phrases_html(c.SOURCES.sub(' ',raw.decode())):
  if tag.lower()!='td'and len(t)>60:
   k=hashlib.sha1(re.sub(r'\W+','',t.lower()).encode()).hexdigest()
   if not any(x['fichier']==str(f)for x in seen[k]):seen[k].append({'fichier':str(f),'phrase':t})
shared=[v for v in seen.values()if len(v)>1];ex=[];errors=[]
for rows in shared:
 (ex if all(x['phrase']==question for x in rows)else errors).append(rows)
report={'outil':'outils/controle3.py fonctions phrases_html/SOURCES originales inchangées','versions':versions,'phrases_partagees_hors_question_obligatoire':errors,'exemption_unique_question_obligatoire':ex,'valide':len(versions)==11 and not errors}
(r/'audits/CONTROLE_PHRASES_CROISEES.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'valide':report['valide'],'groupes_hors_question':len(errors),'exemples':errors[:5]},ensure_ascii=False))
