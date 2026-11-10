"""Dépôt individuel d'une leçon assemblée et contrôlée ; réservé à cette session."""
from pathlib import Path
import argparse, hashlib, json, shutil, subprocess

ap = argparse.ArgumentParser()
ap.add_argument('source')
ap.add_argument('--sha256', required=True)
a = ap.parse_args()
repo = Path(__file__).resolve().parents[2]
scope = repo/'ChatGPT_Codex'
source = (repo/a.source).resolve()
assert source.is_relative_to(scope) and source.name.startswith('LOT_080_Phase_')
assert hashlib.sha256(source.read_bytes()).hexdigest() == a.sha256
branch = subprocess.check_output(['git','branch','--show-current'],cwd=repo,text=True).strip()
assert branch == 'codex/lot-080', branch
lot = scope/'LOT_080'
dest = lot/source.name
assert not dest.exists(), 'Leçon déjà déposée ; correction ciblée explicite nécessaire.'
shutil.copyfile(source,dest)
manifest = lot/'MANIFESTE.json'
m = json.loads(manifest.read_text())
m[dest.name] = {'octets':dest.stat().st_size,'sha256':a.sha256}
manifest.write_text(json.dumps(m,ensure_ascii=False,indent=1)+'\n')
lessons = sorted(p.name for p in lot.glob('LOT_080_Phase_*.html'))
state = lot/'ETAT_FILE.json'
d = json.loads(state.read_text())
d['html_produits'] = lessons
d['statut'] = 'PRODUCTION_DX_ET_AUDITS_EN_COURS'
d['motifs'].append(f'{dest.name} : fichier assemblé et contrôlé déposé ; audit indépendant à consulter séparément.')
state.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
journal = scope/'JOURNAL_NUIT.md'
s = journal.read_text()
s = s[:s.rfind('\nLOTs livrés :')]
s += f'\n\nDépôt individuel : {dest.name}, {dest.stat().st_size} octets, SHA256 {a.sha256}. Les audits médicaux sont consignés séparément ; le LOT n’est pas encore livré.\n'
s += f'\nLOTs livrés : 0/23 (080–102) ; leçons poussées : {len(lessons)}/253 nouvelles, 858 existantes consolidées ; blocages : {11-len(lessons)} DX du LOT080 à pousser et audits DX en cours ; LOT081–102 à produire.\n'
journal.write_text(s)
paths = [dest,manifest,state,journal]
subprocess.run(['git','add',*[str(p.relative_to(repo)) for p in paths]],cwd=repo,check=True)
subprocess.run(['git','commit','-m',f'LOT080 : déposer {dest.stem} après rédaction et contrôle'],cwd=repo,check=True)
subprocess.run(['git','push','origin',branch],cwd=repo,check=True)
