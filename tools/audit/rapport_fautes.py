#!/usr/bin/env python3
"""Galien et Janus · « Rapport d'audit médical : les fautes corrigées ».

Lit qa/audit/fautes.jsonl (une faute corrigée par ligne, schéma tools/audit/faute.schema.json),
écrit qa/audit/RAPPORT_FAUTES.md groupé par unité, fautes critiques en tête.

  python3 tools/audit/rapport_fautes.py            # régénère le rapport
  python3 tools/audit/rapport_fautes.py --check    # CI : journal valide, rapport à jour, et aucune
                                                   # faute critique sans accord_vial (décision du 17.10.2026)
  python3 tools/audit/rapport_fautes.py --pdf ~/rapport.pdf   # copie PDF locale, jamais versionnée
"""
import argparse, json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
ORDRE = {'critique': 0, 'majeure': 1, 'mineure': 2}
REGIONS = {'neuro': 'Neuro', 'tetecou': 'TêteCou', 'coeurthorax': 'CœurThorax', 'abdopelvis': 'AbdoPelvis',
           'locomoteur': 'Locomoteur', 'peaupopulations': 'PeauPopulations'}


def lire(root):
    from jsonschema import Draft202012Validator
    v = Draft202012Validator(json.load(open(os.path.join(HERE, 'faute.schema.json'), encoding='utf-8')))
    p = os.path.join(root, 'qa', 'audit', 'fautes.jsonl')
    fautes, errs = [], []
    if os.path.exists(p):
        for i, l in enumerate(open(p, encoding='utf-8'), 1):
            if not l.strip():
                continue
            try:
                f = json.loads(l)
            except json.JSONDecodeError as e:
                errs.append(f'fautes.jsonl:{i} : JSON invalide ({e.msg})')
                continue
            for e in v.iter_errors(f):
                errs.append(f'fautes.jsonl:{i} : {e.message[:200]}')
            f['_ligne'] = i
            fautes.append(f)
    return fautes, errs


def cell(t):
    return str(t).replace('|', '\\|').replace('\n', ' ')


def rendre(fautes):
    L = ['# Rapport d’audit médical : les fautes corrigées', '',
         'Ce rapport est régénéré par `tools/audit/rapport_fautes.py` à partir de `qa/audit/fautes.jsonl` ; '
         'il ne se modifie pas à la main. Chaque faute a été corrigée par un commit dédié d’un automate d’audit régional de Galien.', '']
    n = {g: sum(1 for f in fautes if f.get('gravite') == g) for g in ORDRE}
    L += [f'Bilan : {len(fautes)} faute(s) corrigée(s), dont {n["critique"]} critique(s), {n["majeure"]} majeure(s) '
          f'et {n["mineure"]} mineure(s).', '']
    crit = [f for f in fautes if f.get('gravite') == 'critique']
    if crit:
        L += ['## Fautes critiques : accord de Vial requis avant fusion', '',
              '| Unité | Élément | Faute | Correction | Source | Accord de Vial |', '|---|---|---|---|---|---|']
        for f in crit:
            L.append(f'| {cell(f["unite"])} | {cell(f.get("element", f["champ"]))} | {cell(f["faute"])} | {cell(f["correction"])} | '
                     f'{cell(f["source"])}, lu le {f["lu_le"]} | {f.get("accord_vial") or "**en attente**"} |')
        L.append('')
    if not fautes:
        L += ['Aucune faute corrigée n’est encore consignée.', '']
    unites = sorted({f['unite'] for f in fautes})
    for u in unites:
        fs = sorted((f for f in fautes if f['unite'] == u), key=lambda f: (ORDRE.get(f['gravite'], 9), f['date'], f['_ligne']))
        L += [f'## {u}', '', '| Gravité | Champ | Faute | Correction | Source | Automate | Commit |', '|---|---|---|---|---|---|---|']
        for f in fs:
            L.append(f'| {f["gravite"].capitalize()} | {cell(f["champ"])} | {cell(f["faute"])} | {cell(f["correction"])} | '
                     f'{cell(f["source"])}, lu le {f["lu_le"]} | Galien-{REGIONS.get(f["region"], f["region"])} | {f["commit"][:7]} |')
        L.append('')
    return '\n'.join(L)


def pdf(md, out):
    """Copie PDF locale (pandoc ou LibreOffice s'ils sont présents) ; jamais versionnée."""
    tmp = out + '.md'
    open(tmp, 'w', encoding='utf-8').write(md)
    for cmd in (['pandoc', tmp, '-o', out], ['pandoc', tmp, '--pdf-engine=weasyprint', '-o', out]):
        try:
            if subprocess.run(cmd, capture_output=True).returncode == 0:
                os.remove(tmp)
                return True
        except FileNotFoundError:
            continue
    print('PDF non produit : pandoc est absent ; le rapport Markdown reste la référence.')
    return False


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--racine', default=ROOT)
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--pdf', default=None)
    a = ap.parse_args(argv)
    fautes, errs = lire(a.racine)
    md = rendre(fautes)
    out = os.path.join(a.racine, 'qa', 'audit', 'RAPPORT_FAUTES.md')
    if a.check:
        if not os.path.exists(out) or open(out, encoding='utf-8').read() != md:
            errs.append('qa/audit/RAPPORT_FAUTES.md n’est pas à jour : lancez python3 tools/audit/rapport_fautes.py')
        for f in fautes:
            if f.get('gravite') == 'critique' and not f.get('accord_vial'):
                errs.append(f'faute critique « {f.get("faute", "")[:60]} » ({f.get("unite")}) sans accord de Vial : fusion bloquée')
        for e in errs:
            print('ÉCHEC', e)
        print(f'Rapport des fautes : {len(fautes)} faute(s), {"conforme" if not errs else f"{len(errs)} échec(s)"}.')
        return 1 if errs else 0
    for e in errs:
        print('ÉCHEC', e)
    if errs:
        return 1
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(md)
    print(f'Rapport écrit : {os.path.relpath(out, a.racine)} ({len(fautes)} faute(s)).')
    if a.pdf:
        pdf(md, a.pdf)
    return 0


if __name__ == '__main__':
    sys.exit(main())
