#!/usr/bin/env python3
"""Inventaire en lecture seule des leçons ; écrit uniquement les preuves du rapport Codex.

Exécution depuis la racine : python3 -B codex-LOTS-html/outils/etat_des_lieux.py
Ne modifie ni les leçons, ni les contrôleurs communs. Pas d'audit médical automatique.
"""
import sys
sys.dont_write_bytecode = True
import csv
import hashlib
import importlib.util
import json
import re
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from lxml import html

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'codex-LOTS-html'
OUT = BASE / 'etat_lieux_20261031'


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def save(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def collect():
    OUT.mkdir(exist_ok=True)
    measure = module('mesure_rapport', ROOT / 'harnais/taille_xy.py')
    langue = module('langue_rapport', ROOT / 'harnais/audit_langue.py')
    v8 = module('v8_rapport', BASE / 'outils/verifier_lot_generique_v8.py')
    catalogue = {int(r['lot']): r for r in csv.DictReader((ROOT / 'LOT_Claude_Finaux/CATALOGUE_248.csv').open())}
    journal = [json.loads(s) for s in (BASE / 'ROUTAGE_CODEX.jsonl').read_text().splitlines() if s.strip()]
    data = {'date_utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
            'commit_source': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
            'branche': subprocess.check_output(['git', 'branch', '--show-current'], cwd=ROOT, text=True).strip(),
            'unite': '1 Ko = 1000 octets UTF-8 ; valeurs exactes à 3 décimales',
            'methodologie': 'taille_xy.mesurer inchangé, verifier_lot_generique_v8.verifier inchangé, audit_langue.audit inchangé ; lectures seules ; aucune revue clinique nouvelle.',
            'lots': [], 'fichiers': [], 'sources_normatives': []}
    for path in [ROOT / 'PROMPT_PRODUCTION_V2.md', ROOT / 'PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V0.md',
                 BASE / 'PROMPT_CODEX.md', BASE / 'CONTRAT_CONTINUITE.md', ROOT / 'IA_RESERVATIONS.json',
                 ROOT / 'harnais/taille_xy.py', ROOT / 'harnais/audit_langue.py', BASE / 'outils/verifier_lot_generique_v8.py']:
        data['sources_normatives'].append({'chemin': str(path.relative_to(ROOT)), 'sha256': sha(path)})
    for directory in sorted(BASE.glob('LOT_[0-9][0-9][0-9]')):
        paths = sorted(directory.glob('*.html'), key=lambda p: 0 if '_Phase_A_' in p.name else int(re.search(r'DX\.(\d+)', p.name)[1]))
        if not paths:
            continue
        lot = directory.name
        number = int(lot[4:])
        checks = v8.verifier(directory)
        save(lot + '_v8.json', checks)
        checkfiles = {x['fichier']: x for x in checks['fichiers']}
        manifest = json.loads((directory / 'MANIFESTE.json').read_text())
        manifests = {x['fichier']: x for x in manifest['fichiers']}
        docs = sorted(set(directory.glob('VALIDATION*.md')) | set(directory.glob('CORRECTIONS*.md')) | set(directory.glob('audits/RELECTURE*.md')))
        hist = [x for x in journal if x.get('lot') == lot]
        save(lot + '_tracabilite.json', {'documents': [{'chemin': str(p.relative_to(BASE)), 'sha256': sha(p), 'texte': p.read_text()} for p in docs], 'passes': hist})
        current = []
        for path in paths:
            raw = path.read_bytes()
            text = raw.decode('utf-8')
            m = measure.mesurer(text)
            tree = html.document_fromstring(raw)
            pa = '_Phase_A_' in path.name
            key = 'Phase_A' if pa else 'DX.' + re.search(r'DX\.(\d+)', path.name)[1]
            title = tree.xpath('//main/h2' if not pa else '//h1')
            title = title[0].text_content().strip() if title else path.stem
            language = langue.audit(path)
            language['fichier'] = str(path.relative_to(ROOT))
            save(path.stem + '_langue.json', language)
            check = checkfiles[path.name]
            assert check['octets'] == len(raw) and check['texte_fiche_octets'] == m.x[1] and check['texte_fenetres_octets'] == m.y[1]
            routed = [x for x in hist if x.get('fichier') in (key, path.name)]
            relectures = [x for x in routed if x.get('poste') == 'relecture-interne']
            prefix = 'a' if pa else 'dx' + key[3:]
            aips = next(c for c in check['controles'] if c['controle'] == 'citations_aips_presentes_dans_fichiers_originaux')
            row = {'lot': lot, 'lecon': key, 'titre': title, 'chemin': str(path.relative_to(BASE)),
                   'sha256': sha(path), 'octets_html': len(raw), 'x_octets': m.x[1], 'y_octets': m.y[1],
                   'xy_octets': m.x[1] + m.y[1], 'plafond_x_octets': 100000 if pa else 9000,
                   'taille_v8_ok': m.x[1] <= (100000 if pa else 9000),
                   'bande_v0_ok': 80000 <= len(raw) <= 150000, 'plafond_v0_ok': len(raw) <= 150000,
                   'mots_x': m.x[0], 'mots_y': m.y[0], 'fenetres': m.fen, 'depliants': m.dep,
                   'parties': len(tree.xpath('//section[h2[starts-with(@id,$p)]]', p=prefix+'-p')),
                   'questions': len(tree.xpath('//details[contains(concat(" ",normalize-space(@class)," ")," quiz ")]')),
                   'v8_positifs': sum(c['ok'] for c in check['controles']), 'v8_nombre': len(check['controles']),
                   'v8_echecs': [c for c in check['controles'] if not c['ok']],
                   'citations_aips': check['citations_aips'], 'citations_aips_retrouvees': aips['ok'],
                   'langue_verdict_brut': language['conforme'], 'langue_critiques': language['critiques'],
                   'langue_avertissements': language['avertissements'],
                   'relecture_interne_par_fichier_documentee': bool(relectures), 'passes_relecture': relectures,
                   'empreinte_manifeste_ok': manifests.get(path.name, {}).get('sha256') == sha(path),
                   'octets_manifeste_ok': manifests.get(path.name, {}).get('octets') == len(raw),
                   'preuve_langue': 'etat_lieux_20261031/' + path.stem + '_langue.json',
                   'audit_medical_independant': False, 'validation_clinique': False, 'nouvelle_relecture_medicale': False}
            current.append(row)
        cat = catalogue[number]
        data['lots'].append({'lot': lot, 'code': cat['code'], 'titre': cat['ssp_profiles_2023_fr_en'].split('|')[0].strip(),
                             'html_presents': len(paths), 'complet_11_html': checks['onze_fichiers_et_dix_diagnostics'],
                             'v8_ok': checks['statique_ok'], 'octets_html': sum(x['octets_html'] for x in current),
                             'x_octets': sum(x['x_octets'] for x in current), 'y_octets': sum(x['y_octets'] for x in current),
                             'bande_v0_ok': sum(x['bande_v0_ok'] for x in current),
                             'documents': [str(p.relative_to(BASE)) for p in docs],
                             'transversale_interne_documentee': any(x.get('poste') == 'transversale-interne' for x in hist),
                             'preuve_v8': f'etat_lieux_20261031/{lot}_v8.json',
                             'preuve_historique': f'etat_lieux_20261031/{lot}_tracabilite.json'})
        data['fichiers'].extend(current)
        print(lot, len(current), sum(r['v8_positifs'] for r in current), '/', sum(r['v8_nombre'] for r in current), flush=True)
    files = data['fichiers']
    data['bilan'] = {'fichiers': len(files), 'lots_complets': sum(x['complet_11_html'] for x in data['lots']),
                     'taille_v8_ok': sum(x['taille_v8_ok'] for x in files), 'bande_v0_ok': sum(x['bande_v0_ok'] for x in files),
                     'sous_80ko': sum(x['octets_html'] < 80000 for x in files), 'au_dessus_150ko': sum(x['octets_html'] > 150000 for x in files),
                     'v8_positifs': sum(x['v8_positifs'] for x in files), 'v8_controles': sum(x['v8_nombre'] for x in files),
                     'langue_verdict_brut_ok': sum(x['langue_verdict_brut'] for x in files),
                     'relectures_interne_tracees': sum(x['relecture_interne_par_fichier_documentee'] for x in files),
                     'manifestes_identiques': sum(x['empreinte_manifeste_ok'] and x['octets_manifeste_ok'] for x in files),
                     'citations_aips': sum(x['citations_aips'] for x in files), 'parties': sum(x['parties'] for x in files),
                     'questions': sum(x['questions'] for x in files),
                     'codes_langue_critiques': dict(Counter(c['code'] for x in files for c in x['langue_critiques'])),
                     'codes_langue_avertissements': dict(Counter(c['code'] for x in files for c in x['langue_avertissements']))}
    save('mesures.json', data)
    columns = ['lot', 'lecon', 'titre', 'chemin', 'octets_html', 'x_octets', 'y_octets', 'xy_octets', 'plafond_x_octets',
               'taille_v8_ok', 'bande_v0_ok', 'v8_positifs', 'v8_nombre', 'parties', 'questions', 'citations_aips',
               'citations_aips_retrouvees', 'langue_verdict_brut', 'relecture_interne_par_fichier_documentee', 'sha256']
    with (OUT / 'mesures.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(files)
    print(json.dumps(data['bilan'], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    collect()
