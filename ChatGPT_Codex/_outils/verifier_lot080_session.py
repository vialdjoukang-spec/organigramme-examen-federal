"""Vérifie les pièces réelles de P4 sans attribuer de score médical."""
from pathlib import Path
from html.parser import HTMLParser
import collections, hashlib, html, json, re, subprocess, importlib.util, argparse

repo = Path(__file__).resolve().parents[2]
lot = repo/'ChatGPT_Codex/LOT_080'
work = lot/'_travail/reprise'
out = lot/'controles'
out.mkdir(exist_ok=True)
manifest = json.loads((lot/'MANIFESTE.json').read_text())
dxs = json.loads((work/'PROPOSITION_P1.json').read_text())['dx']
class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.refs=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if a.get('href','').startswith('#'):self.refs.append(a['href'][1:])
        if 'popovertarget' in a:self.refs.append(a['popovertarget'])

rows=[]
for i in range(11):
    name='LOT_080_Phase_A_V0.html' if i==0 else f'LOT_080_Phase_B_V0_DX.{i}.html'
    file=lot/name
    row={'fichier':name,'erreurs':[]}
    if not file.exists():
        row['erreurs'].append('Fichier absent');rows.append(row);continue
    data=file.read_bytes();sha=hashlib.sha256(data).hexdigest();text=data.decode()
    row.update(octets=len(data),sha256=sha)
    if not 100000<=len(data)<=200000:row['erreurs'].append('Bande octets non respectée')
    if manifest.get(name)!={'octets':len(data),'sha256':sha}:row['erreurs'].append('Manifeste non conforme')
    if f'FIN_FICHIER {file.stem}' not in text[-400:]:row['erreurs'].append('Marqueur final absent')
    if i and dxs[i-1]['nom'] not in html.unescape(re.search(r'<h2>(.*?)</h2>',text,re.S).group(1)):
        row['erreurs'].append('Nom différent de la liste gelée')
    links=Links();links.feed(text)
    if set(links.refs)-set(links.ids):row['erreurs'].append('Ancre ou fenêtre introuvable')
    if any(n>1 for n in collections.Counter(links.ids).values()):row['erreurs'].append('Identifiant HTML dupliqué')
    section_ids={int(m.group(1)) for value in links.ids if (m:=re.fullmatch(r'[\w-]*p(\d+)',value))}
    if not set(range(1,15)).issubset(section_ids):row['erreurs'].append('Points manquants')
    if i==0:packet=work/'assemblage/paquet.json'
    elif i<=3:packet=work/f'redaction_DX1_3/DX.{i}/paquet.json'
    elif i<=7:packet=work/f'redaction_DX4_7/DX.{i}/paquet.json'
    else:packet=work/f'redaction_DX8_10/DX.{i}/paquet.json'
    if packet.exists():
        result=subprocess.run(['python3',str(repo/'ChatGPT_Codex/_outils/controle3.py'),str(file),'--paquet',str(packet),'--min','100000','--max','200000'],capture_output=True,text=True)
        control=json.loads(result.stdout)
        (out/(name+'.controle.json')).write_text(json.dumps(control,ensure_ascii=False,indent=2)+'\n')
        row['P2']=control[0]['verdict']
        row['paquet_sha256']=hashlib.sha256(packet.read_bytes()).hexdigest()
        if row['P2']=='ROUGE':row['erreurs'].append('P2 ROUGE')
    else:row['erreurs'].append('Paquet local absent')
    af=lot/'audits'/(name+'.audit.json')
    if af.exists():
        audit=json.loads(af.read_text());row['P3']=audit.get('verdict');row['score_pct']=audit.get('score_pct')
        if audit.get('sha256')!=sha:row['erreurs'].append('Audit sur une autre empreinte')
        if audit.get('verdict')!='VERT' or audit.get('score_pct',0)<90 or str(audit.get('finale','')).lower()!='oui':row['erreurs'].append('P3 non franchie')
        if audit.get('critique',0) or audit.get('grave_non_corrige',0):row['erreurs'].append('Défaut médical bloquant')
    else:row['erreurs'].append('Audit P3 absent')
    rows.append(row)
# Refaire le contrôle original avec une mémoire commune aux onze fichiers.
spec=importlib.util.spec_from_file_location('controle3_reference',repo/'ChatGPT_Codex/_outils/controle3.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
args=argparse.Namespace(points=14,min=100000,max=200000,script_ok=False,ex=10000)
seen={};inter=[]
for row in rows:
    if (lot/row['fichier']).exists():
        inter.append(module.controler(str(lot/row['fichier']),{},args,seen))
(out/'INTER_FICHIERS_FINAL.json').write_text(json.dumps(inter,ensure_ascii=False,indent=2)+'\n')
mandatory='Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient'
shared=[]
for result in inter:
    defect=result['defauts'].get('B_phrase_partagee_entre_fichiers',{})
    shared += [x for x in defect.get('ex',[]) if x != mandatory]
inter_audit=lot/'audits/INTER_FICHIERS.audit.json'
inter_status={'rapport_original':'controles/INTER_FICHIERS_FINAL.json','repetitions_non_imposees':shared,'question_M1_3_imposee':mandatory,'arbitrage_independant_present':inter_audit.exists()}
report={'lot':'LOT_080','portee':'Vérifications locales pour P4 ; CI et fusion vérifiées séparément.','pret_pour_PR':all(not r['erreurs'] for r in rows) and not shared and inter_audit.exists(),'fichiers':rows,'inter_fichiers':inter_status}
(lot/'VERIFICATION_LOT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
for row in rows:print(row['fichier'],row.get('P2','—'),row.get('P3','—'),'; '.join(row['erreurs']) or 'conforme')
raise SystemExit(0 if report['pret_pour_PR'] else 1)
