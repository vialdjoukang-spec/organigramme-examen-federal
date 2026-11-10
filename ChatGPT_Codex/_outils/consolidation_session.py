#!/usr/bin/env python3
"""Pilote les passes de l'outil de référence sans modifier sa carte originale.

La file dérivée ne contient que les leçons restant à copier. Chaque copie est
comparée au blob choisi par le détecteur avant commit et push de la passe.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
ICI = Path(__file__).resolve().parent
RACINE = ICI.parent.parent
sys.path.insert(0, str(ICI))
from detecteur_lots import attribuer


def lancer(*args):
    p = subprocess.run(args, cwd=RACINE, text=True, capture_output=True)
    if p.stdout.strip():
        print(p.stdout.strip(), flush=True)
    if p.returncode:
        if p.stderr.strip():
            print(p.stderr.strip(), file=sys.stderr, flush=True)
        raise SystemExit(p.returncode)
    return p.stdout


def main():
    original = Path(sys.argv[1])
    carte = json.loads(original.read_text())
    rapports = ICI / 'rapports' / 'consolidation-20261110'
    rapports.mkdir(parents=True, exist_ok=True)
    snapshot = rapports / 'carte_initiale.json'
    if not snapshot.exists():
        snapshot.write_bytes(original.read_bytes())
    autorises = {p for p in carte['obsoletes_main']
                 if attribuer(p, 'origin/main', '')[0] == 'ChatGPT_Codex'}
    a_copier = {k: v for k, v in carte['lecons'].items()
                if v['ia'] == 'ChatGPT_Codex' and v['chemin'] != v['destination']}
    bilan = []
    file = rapports / 'file_restante.json'
    while True:
        queue = dict(carte, lecons=a_copier)
        file.write_text(json.dumps(queue, ensure_ascii=False, indent=1))
        sortie = lancer(sys.executable, str(ICI / 'consolider.py'),
                        '--carte', str(file), '--ia', 'ChatGPT_Codex',
                        '--max', '60', '--appliquer')
        if not a_copier:
            break
        passe = list(a_copier.items())[:60]
        for cle, v in passe:
            dest = RACINE / v['destination']
            brut = dest.read_bytes()
            blob = subprocess.check_output(['git', 'hash-object', str(dest)], cwd=RACINE, text=True).strip()
            if blob != v['blob']:
                raise SystemExit(f'Empreinte différente : {cle}')
            bilan.append({'lecon': cle, 'source_ref': v['ref'],
                          'source_chemin': v['chemin'], 'blob': blob,
                          'destination': v['destination'], 'octets': len(brut),
                          'sha256': hashlib.sha256(brut).hexdigest()})
        (rapports / 'copies_verifiees.json').write_text(json.dumps(bilan, ensure_ascii=False, indent=1))
        lancer('git', 'add', '--', 'ChatGPT_Codex')
        chemins = subprocess.check_output(['git', 'diff', '--cached', '--name-only', '-z'], cwd=RACINE).decode().split('\0')
        for chemin in filter(None, chemins):
            if not chemin.startswith('ChatGPT_Codex/') and chemin not in autorises:
                raise SystemExit(f'Changement hors ressort : {chemin}')
        lancer('git', 'commit', '-m', f'Consolide les leçons Codex : {len(bilan)}/{len(bilan) + len(a_copier) - len(passe)}')
        lancer('git', 'push', '-u', 'origin', 'HEAD')
        for cle, _ in passe:
            del a_copier[cle]
    print(f'Consolidation : {len(bilan)} copies vérifiées ; 0 leçon à écrire.', flush=True)


if __name__ == '__main__':
    main()
