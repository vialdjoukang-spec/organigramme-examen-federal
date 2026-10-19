#!/usr/bin/env python3
"""Suivi des cours SSP : relecture liée au contenu, jamais déduite du numéro."""
import hashlib
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from _app import read, span


def empreinte(text):
    return hashlib.sha256(text.encode()).hexdigest()


def bilan(root=ROOT, today=None):
    today = today or date.today()
    app = (root / 'app_v2.html').read_text()
    a, b = span(app, 'TIP')
    tip = json.loads(app[a:b])
    registry = json.loads((root / 'tools/cours/registre.json').read_text())
    reviews = registry.get('relectures', {})
    errors, reviewed, pending = [], [], []
    for code, item in tip.items():
        parts = item.get('c', [])
        if len(parts) != 14:
            errors.append(code + ' : 14 parties attendues')
        entry = reviews.get(code)
        valid = False
        if entry:
            try:
                path = Path(entry['rapport'])
                assert not path.is_absolute() and '..' not in path.parts
                raw = (root / path).read_text()
                audit = json.loads(raw)
                hashes = [empreinte(text) for text in parts]
                assert len(hashes) == 14
                assert entry['parties_sha256'] == hashes
                assert entry['rapport_sha256'] == empreinte(raw)
                assert date.fromisoformat(entry['lu_le']) <= today
                assert audit['parties_sha256'] == hashes
                assert audit['verdict'] == 'favorable_documentaire'
                assert audit['sources_lues'] and audit['relecteur_independant']
                valid = True
            except (AssertionError, KeyError, OSError, TypeError, ValueError):
                errors.append(code + ' : attestation absente, périmée ou incohérente')
        (reviewed if valid else pending).append(code)
    errors += [code + ' : SSP inconnu dans le registre' for code in reviews if code not in tip]
    return {'ssp_total': len(tip), 'parties_total': sum(len(t['c']) for t in tip.values()),
            'ssp_relus': len(reviewed), 'parties_relues': 14 * len(reviewed),
            'ssp_restant': pending, 'anomalies': errors,
            'reserve': 'Relecture documentaire de forme et fond ; aucune validation médicale humaine déduite.'}


if __name__ == '__main__':
    result = bilan()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(bool(result['anomalies']))
