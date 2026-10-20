#!/usr/bin/env python3
"""BETTA : contrôle structurel des monographies DD d'un SSP (protocole 6 rubriques).
Lecture seule. Ne produit aucune attestation Astra ; sortie = constats + empreintes."""
import json, re, sys, glob
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT))
from tools.mandat.planifier import empreinte, lire
from tools.coordination.calculer import calculer
REQ = ['n', 'def', 'epi', 'phy', 'cli', 'exp_ref', 'exp_premier', 'but', 'mes', 'pha', 'src', 'lu']
DOSE = re.compile(r'\b\d+(?:[.,]\d+)?\s?(?:mg|µg|mcg|g|UI|ml)(?:/kg|/j|/h)?\b', re.I)

def constats(m):
    c = [f'champ manquant : {k}' for k in REQ if not str(m.get(k, '')).strip()]
    if m.get('chronologie_version') != 1: c.append('chronologie_version absente (legacy)')
    b, p = m.get('bilan_ordre') or [], m.get('pec_ordre') or []
    if not 1 <= len(b) <= 6: c.append(f'bilan_ordre : {len(b)} temps')
    elif b[0].get('titre') != 'À faire en premier' or b[0].get('texte') != m.get('exp_premier'):
        c.append('bilan_ordre[0] ≠ « À faire en premier » / exp_premier')
    if not 1 <= len(p) <= 6: c.append(f'pec_ordre : {len(p)} phases')
    if any(not any(x.get(k) for k in ('mes', 'pha', 'aut')) for x in p): c.append('phase PEC vide')
    if p and not any(x.get('mes') for x in p): c.append('aucune phase mes')
    if p and not any(x.get('pha') for x in p): c.append('aucune phase pha')
    txt = ' '.join(str(m.get(k, '')) for k in ('pha', 'aut')) + ' ' + json.dumps(p, ensure_ascii=False)
    if DOSE.search(txt) and 'AIPS' not in txt: c.append('dose chiffrée sans référence AIPS : ' + DOSE.search(txt).group())
    if not re.search(r'\d{2}\.\d{2}\.\d{4}', str(m.get('lu', ''))): c.append('date de lecture absente')
    if 'compendium' in json.dumps(m, ensure_ascii=False).lower(): c.append('mention Compendium')
    return c

def main(ssps):
    c = lire(ROOT, 'tools/coordination/config.json'); c.pop('mandat', None)
    occ = calculer(ROOT, ledger=lire(ROOT, 'tools/coordination/relectures.json'), config=c)['occurrences']
    monos = {}
    for f in sorted(glob.glob(str(ROOT / 'data/ck/mono/*.json'))):
        for k, v in json.loads(Path(f).read_text()).items(): monos[k] = (Path(f).stem, v)
    out = {}
    for s in ssps:
        rows = [x for x in occ if x['ssp'] == s]
        out[s] = {'dd': [], 'sans_differentiel': not rows}
        for x in rows:
            d = x['diagnostic_id']; f, m = monos.get(d, (None, {}))
            ailleurs = sorted({y['ssp'] for y in occ if y['diagnostic_id'] == d} - {s})
            out[s]['dd'].append({'id': d, 'libelle': x['diagnostic'], 'tranche': f,
                                 'empreinte': empreinte(m), 'partage_avec': ailleurs,
                                 'constats': constats(m) if m else ['monographie absente']})
    return out

if __name__ == '__main__':
    print(json.dumps(main(sys.argv[1:]), ensure_ascii=False, indent=1))
