#!/usr/bin/env python3
"""Galien · six automates d'audit régional (tools/audit/regions.yml), au-dessus du niveau 1 d'Atlas et Janus.

  travail  --unite U --base REF   liste, par région, les seules entrées de data/ck/<fichier>.json modifiées
           depuis REF, avec leurs signalements de niveau 1 (niveau1.py) et la liste de contrôle de la région ;
           écrit qa/audit/travail/<U>-<région>.json (non versionné). Galien relit ces fichiers, pas le dépôt.
  corriger --plan P.yml           applique chaque correction relue, une par une : un commit propre par faute,
           « audit(galien-<Région>): <unité> · <élément> : <faute> → <correction> [source] (gravité) »,
           avec assets/ck recompilés (ck_build) et la ligne du registre en clair dans le message.
  registre                        réécrit qa/audit/fautes.jsonl depuis ces commits (hachage réel de chaque
           correction, schéma tools/audit/faute.schema.json), puis régénère RAPPORT_FAUTES.md.

La région d'une entrée du glossaire vient de qa/audit/glo-meta.json (le schéma glo n'a pas de champ région).
Galien n'audite jamais son propre texte : un plan dont l'auteur est Galien est refusé. Une faute critique
porte accord_vial: null et bloque la fusion (rapport_fautes.py --check) jusqu'à l'accord daté de Vial."""
import argparse, datetime, json, os, re, subprocess, sys
import yaml
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
REGIONS = yaml.safe_load(open(os.path.join(HERE, 'regions.yml'), encoding='utf-8'))
META = os.path.join(ROOT, 'qa', 'audit', 'glo-meta.json')
REG = os.path.join(ROOT, 'qa', 'audit', 'fautes.jsonl')
MARQUE = 'Registre : '


def git(*a):
    r = subprocess.run(['git', *a], cwd=ROOT, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(r.stderr or r.stdout)
    return r.stdout


def charger(n):
    return json.load(open(os.path.join(ROOT, 'data', 'ck', n + '.json'), encoding='utf-8'))


def ecrire(n, d):
    with open(os.path.join(ROOT, 'data', 'ck', n + '.json'), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write('\n')


def region(n, e):
    if n == 'glo':
        return json.load(open(META, encoding='utf-8')).get(e['id'], {}).get('region')
    return e.get('region')


def travail(unite, base, n):
    r = subprocess.run(['git', 'show', f'{base}:data/ck/{n}.json'], cwd=ROOT, capture_output=True, text=True)
    avant = {e['id']: e for e in json.loads(r.stdout)} if r.returncode == 0 else {}
    modif = [e for e in charger(n) if avant.get(e['id']) != e]
    tmp = os.path.join(ROOT, '.cache', 'flags-travail.json')
    subprocess.run([sys.executable, os.path.join(HERE, 'niveau1.py'), '--sortie', tmp], cwd=ROOT, capture_output=True)
    flags = json.load(open(tmp, encoding='utf-8')) if os.path.exists(tmp) else []
    d = os.path.join(ROOT, 'qa', 'audit', 'travail')
    os.makedirs(d, exist_ok=True)
    for reg, conf in REGIONS.items():
        lot = [e for e in modif if region(n, e) == reg]
        if not lot:
            continue
        ids = {f'{n}|{e["id"]}' for e in lot}
        out = {'unite': unite, 'region': conf['nom'], 'controle': conf['controle'], 'entrees': lot,
               'signalements': [f for f in flags if f.get('element') in ids or any(i in f.get('motif', '') for i in ids)]}
        p = os.path.join(d, f'{unite}-{reg}.json')
        json.dump(out, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f"{conf['nom']:16} {len(lot):3} entrée(s), {len(out['signalements'])} signalement(s) → {os.path.relpath(p, ROOT)}")


def appliquer(e, c):
    op, ch = c.get('op', 'remplacer'), c['champ']
    if op == 'remplacer':
        v = e.get(ch, '')
        if v.count(c['avant']) != 1:
            raise SystemExit(f"{e['id']}.{ch} : « {c['avant'][:60]} » doit figurer une seule fois ({v.count(c['avant'])}).")
        e[ch] = v.replace(c['avant'], c['apres'])
    elif op == 'definir':
        e[ch] = c['apres']
    elif op == 'retirer':
        for x in c['avant'] if isinstance(c['avant'], list) else [c['avant']]:
            if x not in e.get(ch, []):
                raise SystemExit(f"{e['id']}.{ch} : élément absent : {x}")
            e[ch].remove(x)
        if not e[ch]:
            del e[ch]
    else:
        raise SystemExit('opération inconnue : ' + op)
    for k, v in (c.get('aussi') or {}).items():
        e.pop(k, None) if v is None else e.__setitem__(k, v)


def corriger(plan):
    P = yaml.safe_load(open(plan, encoding='utf-8'))
    if P.get('auteur') == 'Galien':
        raise SystemExit('Refus : Galien n’audite pas son propre texte (contre-lecture par Asclépios).')
    n = P.get('fichier', 'glo')
    meta = json.load(open(META, encoding='utf-8'))
    for c in P['corrections']:
        data = charger(n)
        e = next((x for x in data if x['id'] == c['element']), None)
        if e is None:
            raise SystemExit('entrée absente : ' + c['element'])
        appliquer(e, c)
        ecrire(n, data)
        fichiers = [f'data/ck/{n}.json', 'assets/ck']
        if 'a_verifier' in c:  # motif « À vérifier » : hors schéma glo, conservé dans glo-meta.json
            meta.setdefault(e['id'], {})
            meta[e['id']].pop('a_verifier', None) if c['a_verifier'] is None else meta[e['id']].__setitem__('a_verifier', c['a_verifier'])
            json.dump(meta, open(META, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
            fichiers.append(os.path.relpath(META, ROOT))
        b = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'ck_build.py')], cwd=ROOT, capture_output=True, text=True)
        if b.returncode:
            raise SystemExit('ck_build refuse la correction : ' + b.stdout[-400:])
        reg = region(n, e)
        f = dict(unite=P['unite'], element=f'{n}|{e["id"]}', region=reg, champ=c['champ'], faute=c['faute'],
                 correction=c['correction'], source=c['source'], lu_le=c.get('lu_le', P.get('lu_le')),
                 gravite=c['gravite'], commit='en-attente', date=datetime.date.today().isoformat())
        if c['gravite'] == 'critique':
            f['accord_vial'] = None
        titre = (f"audit(galien-{REGIONS[reg]['nom']}): {P['unite']} · {e['id']} : {c['court']} "
                 f"[{c['source_courte']}] ({c['gravite']})")
        git('add', *fichiers)
        git('commit', '-q', '-m', titre, '-m', f"Faute relevée : {c['faute']}\nCorrection : {c['correction']}\n"
            f"Source : {c['source']}\n{MARQUE}{json.dumps(f, ensure_ascii=False)}")
        print(git('log', '-1', '--format=%h %s').strip())


def registre():
    out = []
    log = git('log', '--reverse', '--format=%H%x00%B%x1e')
    for bloc in log.split('\x1e'):
        if MARQUE not in bloc:
            continue
        h, _, corps = bloc.strip().partition('\x00')
        for l in corps.splitlines():
            if l.startswith(MARQUE):
                f = json.loads(l[len(MARQUE):])
                f['commit'] = h[:12]
                out.append(f)
    with open(REG, 'w', encoding='utf-8') as fh:
        fh.writelines(json.dumps(f, ensure_ascii=False) + '\n' for f in out)
    subprocess.run([sys.executable, os.path.join(HERE, 'rapport_fautes.py')], cwd=ROOT, check=True)
    print(f'Registre : {len(out)} faute(s) → {os.path.relpath(REG, ROOT)}')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest='cmd', required=True)
    t = sp.add_parser('travail'); t.add_argument('--unite', required=True); t.add_argument('--base', default='origin/main'); t.add_argument('--fichier', default='glo')
    k = sp.add_parser('corriger'); k.add_argument('--plan', required=True)
    sp.add_parser('registre')
    a = ap.parse_args()
    {'travail': lambda: travail(a.unite, a.base, a.fichier), 'corriger': lambda: corriger(a.plan), 'registre': registre}[a.cmd]()
