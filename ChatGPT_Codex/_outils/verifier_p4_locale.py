#!/usr/bin/env python3
"""Vérification locale des preuves ; la CI et la fusion restent distinctes."""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('dossier', type=Path)
    ap.add_argument('--sortie', type=Path, required=True)
    args = ap.parse_args()
    root = args.dossier
    manifest = json.loads((root / 'MANIFESTE.json').read_text())
    validations = json.loads((root / 'VALIDATIONS_P3.json').read_text())
    structure = json.loads((root / 'audits/VERIFICATION_STRUCTURE_FINALE.json').read_text())
    expected = [f'{root.name}_Phase_A_V0.html'] + [f'{root.name}_Phase_B_V0_DX.{n}.html' for n in range(1, 11)]
    errors = []
    if not structure['valide']:
        errors.append('Structure finale non valide')
    structure_by_name = {r['fichier']: r for r in structure['fichiers']}
    rows = []
    for name in expected:
        raw = (root / name).read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        current = {'sha256': sha, 'octets': len(raw)}
        v = validations.get(name, {})
        if manifest.get(name) != current:
            errors.append(f'{name} : manifeste périmé')
        if structure_by_name.get(name, {}).get('sha256') != sha:
            errors.append(f'{name} : contrôle structure périmé')
        if any(v.get(k) != x for k, x in current.items()):
            errors.append(f'{name} : validation P3 absente ou périmée')
        if v.get('finale') != 'oui' or v.get('P3') != 'FRANCHIE' or v.get('score_pct', 0) < 90:
            errors.append(f'{name} : P3 non franchie')
        audit_path = root / v.get('audit', '__absent__')
        if audit_path.is_file():
            audit = json.loads(audit_path.read_text())
            if sha not in json.dumps(audit):
                errors.append(f'{name} : empreinte non attestée par le rapport référencé')
        else:
            errors.append(f'{name} : rapport P3 absent')
        rows.append({'fichier': name, **current, 'validation': v})
    report = {'lot': root.name, 'controle': 'Empreintes et preuves locales uniquement, sans nouvel audit médical',
              'fichiers': rows, 'erreurs': errors, 'preuves_locales_valides': not errors,
              'CI': 'A_VERIFIER_SUR_COMMIT_PR', 'P4': 'EN_ATTENTE_CI' if not errors else 'NON_FRANCHIE'}
    args.sortie.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'preuves_locales_valides': not errors, 'erreurs': errors}, ensure_ascii=False))
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())
