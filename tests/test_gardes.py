#!/usr/bin/env python3
"""Janus · tests des gardes : chaque garde doit échouer quand la règle est violée.

Critères d'acceptation couverts (plan v2, fiche Héphaïstos) :
  G1 · une modification de orig/app.html fait échouer la CI ;
  G2 · un app_v2.html au-delà du budget fait échouer la CI ;
  G3 · une erreur HTML nouvelle fait échouer la CI.
"""
import json, os, shutil, subprocess, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = os.path.join(ROOT, 'tools')


def run(args, env=None):
    return subprocess.run([sys.executable, *args], cwd=T, capture_output=True, text=True,
                          env={**os.environ, **(env or {})}).returncode


results = {}
with tempfile.TemporaryDirectory() as d:
    bad = os.path.join(d, 'app.html')
    shutil.copy(os.path.join(ROOT, 'orig', 'app.html'), bad)
    with open(bad, 'ab') as f:
        f.write(b' ')
    results['G1_orig_modifie_echoue'] = run(['check_hash.py', bad]) == 1
    results['G1_orig_intact_reussit'] = run(['check_hash.py']) == 0
    results['G2_budget_depasse_echoue'] = run(['budget.py'], {'APP_MAX_BYTES': '1000'}) == 1
    base = json.load(open(os.path.join(ROOT, 'qa', 'html-baseline.json'), encoding='utf-8'))
    msgs = [{'type': 'error', 'message': k} for k, v in base.items() for _ in range(v)]
    ok = os.path.join(d, 'ok.json'); json.dump({'messages': msgs}, open(ok, 'w'))
    nw = os.path.join(d, 'new.json')
    json.dump({'messages': msgs + [{'type': 'error', 'message': 'Erreur inventée pour le test.'}]}, open(nw, 'w'))
    results['G3_html_reference_reussit'] = run(['html_check.py', ok]) == 0
    results['G3_html_nouvelle_erreur_echoue'] = run(['html_check.py', nw]) == 1

for k, v in results.items():
    print(('ok    ' if v else 'ÉCHEC ') + k)
print(f'Gardes : {sum(results.values())}/{len(results)}.')
sys.exit(0 if all(results.values()) else 1)
