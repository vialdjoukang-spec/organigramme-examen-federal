"""Point d'équipe à partir de la carte originale, sans attribuer de validation clinique."""
from pathlib import Path
from collections import Counter
from datetime import datetime
from zoneinfo import ZoneInfo
import argparse, hashlib, html, importlib.util, json, csv

ap = argparse.ArgumentParser()
ap.add_argument('--carte', required=True)
args = ap.parse_args()
root = Path('ChatGPT_Codex')
raw = Path(args.carte).read_bytes()
carte = json.loads(raw)
spec = importlib.util.spec_from_file_location('progression_originale', 'outils/progression.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
catalogue = {}
with open('LOT_Claude_Finaux/CATALOGUE_248.csv', encoding='utf-8') as stream:
    for row in csv.DictReader(stream):
        catalogue[int(row['lot'])] = (row['code'], row['ssp_profiles_2023_fr_en'])
out = root / 'Progression_Equipe_Midi_20261110.html'
score = mod.rendre(carte, catalogue, 'Toute l’équipe — point de midi', str(out))
lecons = carte['lecons']
counts = Counter(row['ia'] for row in lecons.values())
sur_main = Counter(row['ia'] for row in lecons.values() if row.get('main'))
complets = sum(all(f'{lot:03d}:{n}' in lecons for n in mod.LECONS) for lot in range(1,249))
now = datetime.now(ZoneInfo('Europe/Zurich')).isoformat(timespec='seconds')
rows = ''.join(f'<tr><th scope="row">{html.escape(ia)}</th><td>{counts[ia]}</td><td>{sur_main[ia]}</td></tr>' for ia in mod.IAS)
panel = f'''<section class="top" aria-labelledby="bilan-midi"><h1 id="bilan-midi">Point de midi — toute l’équipe</h1>
<p>10 novembre 2026 · Europe/Zurich. Généré à {html.escape(now)} ; inventaire terminé à {html.escape(carte['genere'])}.</p>
<div class="k"><div><b>{len(lecons)} / 2728</b><small>leçons trouvées, tous ressorts</small></div><div><b>{complets} / 248</b><small>LOTs avec onze leçons présentes</small></div><div><b>{carte['branches_scannees']}</b><small>branches examinées</small></div></div>
<div style="overflow-x:auto"><table style="width:100%;text-align:left;border-collapse:collapse"><thead><tr><th>Ressort du détecteur</th><th>Versions retenues</th><th>Versions retenues sur main</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Le détecteur retient une version par leçon, parmi main et les branches. Ces nombres ne comptent pas toutes les contributions de chaque IA. Le ressort ChatGPT_Codex réunit notamment Codex, ChatGPT, GPT et Cursor.</p>
<p>Les jauges ci-dessous mesurent des critères automatiques de présence et de structure. Un score de 100 % ou onze fichiers présents ne certifie ni la validation médicale ni la fusion d’un LOT.</p>
<details><summary>Livraisons Codex vérifiées pour la mission LOT080–102</summary><p>33 leçons poussées sur253 : LOT080 clos en REFUSE après deux échecs P3 ; LOT081 livré, onze empreintes vérifiées sur main ; LOT082 : onze P3 franchies, fusion conditionnée à la CI de la <a href="https://github.com/vialdjoukang-spec/organigramme-examen-federal/pull/599">PR599</a>. LOT083 en préparation, puis LOT084–102. Les858 leçons consolidées sont comptées séparément. Les validations médicales des autres ressorts ne sont pas évaluées dans ce tableau.</p></details>
</section>'''
doc = out.read_text().replace('<body><main>', '<body><main>'+panel, 1)
out.write_text(doc)
report = {'date_generation_zurich':now, 'date_carte':carte['genere'], 'carte_sha256':hashlib.sha256(raw).hexdigest(), 'branches_scannees':carte['branches_scannees'], 'lecons_trouvees':len(lecons), 'lots_onze_lecons_presentes':complets, 'versions_retenues_par_ressort':dict(counts), 'versions_retenues_sur_main':dict(sur_main), 'score_automatique_global':score, 'validation_medicale_globale':'NON_EVALUEE', 'html_sha256':hashlib.sha256(out.read_bytes()).hexdigest()}
proof = root / '_outils/rapports/progression-midi-20261110.json'
proof.parent.mkdir(parents=True, exist_ok=True)
proof.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
