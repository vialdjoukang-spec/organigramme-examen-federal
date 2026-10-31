#!/usr/bin/env python3
"""Vérifie les données rendues et les filtres du rapport, sans navigateur."""
import csv
import hashlib
import io
import json
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit
from lxml import html

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parent
report = BASE / 'ETAT_DES_LIEUX.html'
out = BASE / 'etat_lieux_20261031'
data = json.loads((out / 'mesures.json').read_text())
tree = html.document_fromstring(report.read_bytes())
results = []


def verify(name, condition):
    results.append({'controle': name, 'ok': bool(condition)})
    assert condition, name


rows = tree.xpath('//tr[contains(concat(" ",@class," ")," lesson ")]')
verify('170 lignes uniques et 16 lots', len(rows) == 170 and len(tree.xpath('//section[@data-lot]')) == 16)
ids = tree.xpath('//@id')
verify('Identifiants HTML uniques', len(ids) == len(set(ids)))
found = Counter(unquote(row.xpath('./th/a/@href')[0]) for row in rows)
verify('Une et une seule ligne par leçon mesurée', found == Counter(f['chemin'] for f in data['fichiers']))
for row, f in zip(rows, data['fichiers']):
    cells = row.xpath('./td')
    values = [int(c.text_content().strip().replace(',', '')) for c in cells[:4]]
    verify('Mesures rendues exactes : ' + f['chemin'], values == [f['x_octets'], f['y_octets'], f['xy_octets'], f['octets_html']])
    current = (BASE / f['chemin']).read_bytes()
    original = subprocess.check_output(['git', 'show', data['commit_source'] + ':codex-LOTS-html/' + f['chemin']], cwd=ROOT)
    verify('HTML identique au commit et au manifeste : ' + f['chemin'], current == original and hashlib.sha256(current).hexdigest() == f['sha256'] and f['empreinte_manifeste_ok'] and f['octets_manifeste_ok'])
badlinks = []
for href in tree.xpath('//a/@href'):
    url = urlsplit(href)
    if url.scheme or url.netloc:
        continue
    path = (BASE / unquote(url.path)).resolve() if url.path else report
    if not path.is_file() or (not url.path and url.fragment and url.fragment not in ids):
        badlinks.append(href)
verify('Tous les liens locaux et ancres du rapport résolus', not badlinks)
embedded_csv = json.loads(tree.xpath('//*[@id="csv-data"]/text()')[0])
csv_rows = list(csv.DictReader(io.StringIO(embedded_csv)))
verify('CSV embarqué égal au CSV sauvegardé', embedded_csv == (out / 'mesures.csv').read_text())
verify('CSV : 170 empreintes et valeurs exactes', len(csv_rows) == 170 and all(c['sha256'] == f['sha256'] and int(c['octets_html']) == f['octets_html'] for c, f in zip(csv_rows, data['fichiers'])))
script = '\n'.join(tree.xpath('//script[not(@type)]/text()'))
syntax = subprocess.run(['node', '--check'], input=script, text=True, capture_output=True)
verify('Syntaxe JavaScript valide', syntax.returncode == 0)
# Exécuter le vrai script livré sur les attributs du vrai HTML. Un DOM minimal
# vérifie la logique des filtres ; cela ne constitue pas un essai navigateur.
sections = [{'lot': section.get('data-lot'), 'rows': [{'search': r.get('data-search'), 'flags': r.get('data-flags')} for r in section.xpath('.//tr[@data-flags]')]} for section in tree.xpath('//section[@data-lot]')]
fixture = r'''
const vm = require('node:vm'), assert = require('node:assert/strict');
const fixture = FIXTURE;
const controls = {};
for (const id of ['search','lot','filter','reset','count','csv','print','csv-data']) controls[id] = {value:'',textContent:'',listeners:{},addEventListener(k,fn){this.listeners[k]=fn}};
const sections = fixture.map(s => ({dataset:{lot:s.lot},hidden:false,rows:s.rows.map(r => ({dataset:r,hidden:false})),querySelectorAll(){return this.rows}}));
const context = {document:{getElementById:id=>controls[id],querySelectorAll:()=>sections},window:{print:()=>{}},console};
vm.createContext(context); vm.runInContext(SCRIPT,context);
function check(n){vm.runInContext('update()',context);assert.equal(sections.flatMap(s=>s.rows).filter(r=>!r.hidden).length,n);assert.equal(controls.count.textContent,n+' / 170 leçons affichées.');for(const s of sections)assert.equal(s.hidden,s.rows.every(r=>r.hidden));}
check(170);controls.filter.value='sous80';check(115);controls.filter.value='taillev8';check(0);controls.filter.value='echecv8';check(1);
controls.filter.value='';controls.lot.value='LOT_033';check(5);controls.search.value='secheresse';check(1);
controls.search.value='';controls.filter.value='sous80';check(1);controls.reset.listeners.click();check(170);
console.log('8 scénarios de filtre réussis sur les attributs du HTML ; aucun navigateur utilisé.');
'''.replace('FIXTURE', json.dumps(sections, ensure_ascii=False)).replace('SCRIPT', json.dumps(script, ensure_ascii=False))
logic = subprocess.run(['node'], input=fixture, text=True, capture_output=True)
verify('Filtres combinés, accents, absence de résultat et réinitialisation', logic.returncode == 0)
summary = {'date_utc': datetime.now(timezone.utc).isoformat(timespec='seconds'), 'rapport_sha256': hashlib.sha256(report.read_bytes()).hexdigest(),
           'controles': results, 'nombre': len(results), 'tous_reussis': all(x['ok'] for x in results),
           'javascript': logic.stdout.strip(), 'test_navigateur': False, 'audit_medical': False,
           'portee': 'Intégrité des mesures, inventaire, liens du rapport et logique des filtres ; aucun jugement clinique ni validation visuelle.'}
(out / 'VERIFICATION_RAPPORT.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k != 'controles'}, ensure_ascii=False, indent=2))
