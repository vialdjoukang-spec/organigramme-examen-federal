#!/usr/bin/env python3
"""REPRISE_G — état des 16 LOTs G en une commande, sans rien relire (zéro modèle).
Pour chaque LOT : branche distante, verdicts controle3, audits présents, PR ouverte, PROCHAINE ACTION.
Usage : python3 Claude/_outils/reprise_g.py [--lots 1-16]
Pipeline d'un LOT : renfort (agents par leçon) → finition (phrases partagées) → audit → appliquer
→ audit2 → appliquer → PR (audit-ok) → fusion (workflow fusion-claude.yml)."""
import os, sys, json, subprocess, tempfile, argparse

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = 'vialdjoukang-spec/organigramme-examen-federal'


def sh(*a, **k):
    return subprocess.run(a, capture_output=True, text=True, **k)


def etat(lot):
    br = f'claude/lot-{lot:03d}-renfort'
    if sh('git', 'fetch', '-q', 'origin', br).returncode:
        return br, None
    ref = f'origin/{br}'
    fich = [f for f in sh('git', 'ls-tree', '--name-only', '-r', ref, f'Claude/LOT_{lot:03d}/').stdout.split()]
    html = [f for f in fich if f.endswith('.html') and '/' not in f.split(f'LOT_{lot:03d}/')[1]]
    a1 = sum(f.endswith('.audit.json') for f in fich)
    a2 = sum(f.endswith('.audit2.json') for f in fich)
    with tempfile.TemporaryDirectory() as d:
        for f in html:
            open(os.path.join(d, os.path.basename(f)), 'w').write(sh('git', 'show', f'{ref}:{f}').stdout)
        out = sh(sys.executable, os.path.join(ICI, 'controle3.py'), *sorted(os.listdir(d)), cwd=d).stdout
    try:
        L = json.loads(out)
    except json.JSONDecodeError:
        L = []
    vert = sum(x['verdict'] == 'VERT' for x in L)
    pr = sh('gh', 'api', f'repos/{DEPOT}/pulls?head={DEPOT.split("/")[0]}:{br}&state=all',
            '--jq', '.[0] | select(.) | "#\\(.number) " + (if .merged_at then "MERGED" else .state end)').stdout.strip()
    return br, dict(n=len(html), vert=vert, a1=a1, a2=a2, pr=pr,
                    rouges=[x['fichier'] for x in L if x['verdict'] != 'VERT'])


def action(e):
    if e is None:
        return 'créer worktree (git worktree add -b claude/lot-XXX-renfort … origin/main), renfort_citations.py, 11 agents MISSION_RENFORCEMENT'
    if 'MERGED' in e['pr']:
        return 'terminé (fusionné)'
    if e['vert'] < e['n']:
        return f"renfort/finition : {e['n'] - e['vert']} leçon(s) non VERTE(S) {e['rouges']}"
    if e['a1'] < e['n']:
        return 'lancer audit médical (auditeur-medical → audits/*.audit.json) puis appliquer_html.py'
    if e['a2'] < e['n']:
        return 'lancer audit2 (audits/*.audit2.json) puis appliquer_html.py'
    if not e['pr']:
        return 'fusionner main dans la branche, ouvrir la PR (Automates actifs en puces), étiquette audit-ok'
    return f"PR {e['pr']} : surveiller CI/revue Codex, attendre fusion-claude.yml"


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--lots', default='1-16')
    a, b = map(int, ap.parse_args().lots.split('-'))
    for lot in range(a, b + 1):
        br, e = etat(lot)
        resume = '—' if e is None else f"{e['vert']}/{e['n']} VERT · audit {e['a1']} · audit2 {e['a2']} · PR {e['pr'] or 'aucune'}"
        print(f'LOT_{lot:03d}  {resume}\n          → {action(e)}')
