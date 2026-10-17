#!/usr/bin/env python3
"""Lance les contrôles Playwright et n'affiche que le décompte et les échecs.

Référence verte (phase 0) : 19 contrôles par profil (ordinateur, mobile) dans
test_tip.py et 5 contrôles dans test_extra.py, soit 43 contrôles, sans erreur
de console. Le code de sortie vaut 1 dès qu'un contrôle échoue.
Phase 1 : chaque chantier ajoute ses contrôles dans SUITES, avec leur nombre
exact ; la référence verte ne peut que grandir.
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TIP_EXPECT = {'aria_expanded_true': 'true', 'console_errors': []}
EXTRA_EXPECT = {'tip_scrollable_css': 'auto'}
# Suites ajoutées en phase 1 : (script, nombre exact de contrôles booléens).
SUITES = [('test_export.py', 13), ('test_exigences.py', 13), ('test_examen.py', 16), ('test_calendrier.py', 36), ('test_ck_socle.py', 12), ('test_ck_ui.py', 66), ('test_memo.py', 17)]
BASE = 43


def run(script, *args):
    p = subprocess.run([sys.executable, os.path.join(HERE, script), *args],
                       capture_output=True, text=True, timeout=600)
    if p.returncode != 0:
        sys.stderr.write(p.stdout[-2000:] + p.stderr[-4000:])
        raise SystemExit(f'ÉCHEC : {script} s’est arrêté (code {p.returncode}).')
    return json.loads(p.stdout)


def judge(key, val, expect):
    if key in expect:
        return val == expect[key]
    if key == 'tip_rect':  # mesure : la fenêtre a une taille réelle
        return isinstance(val, list) and len(val) == 6 and val[2] > 0 and val[3] > 0
    return val is True


def main():
    fails, total = [], 0
    tip = run('test_tip.py', 'ci')
    for prof in ('desktop', 'mobile'):
        res = tip.get(prof, {})
        if len(res) != 19:
            fails.append(f'{prof}: {len(res)} contrôles au lieu de 19')
        for k, v in res.items():
            total += 1
            if not judge(k, v, TIP_EXPECT):
                fails.append(f'{prof}.{k} = {v!r}')
    extra = run('test_extra.py')
    errs = extra.pop('errors', None)
    if errs:
        fails.append(f'extra.errors = {errs!r}')
    if len(extra) != 5:
        fails.append(f'extra: {len(extra)} contrôles au lieu de 5')
    for k, v in extra.items():
        total += 1
        if not judge(k, v, EXTRA_EXPECT):
            fails.append(f'extra.{k} = {v!r}')
    for script, n in SUITES:
        res = run(script)
        errs = res.pop('errors', None)
        if errs:
            fails.append(f'{script}.errors = {errs!r}')
        if len(res) != n:
            fails.append(f'{script}: {len(res)} contrôles au lieu de {n}')
        for k, v in res.items():
            total += 1
            if v is not True:
                fails.append(f'{script}.{k} = {v!r}')
    expected = BASE + sum(n for _, n in SUITES)
    ok = total - sum(1 for f in fails if '=' in f)
    print(f'Contrôles réussis : {ok}/{total} (référence verte : {expected}/{expected}, dont {BASE} de la phase 0).')
    for f in fails:
        print('  ÉCHEC', f)
    sys.exit(1 if fails or total != expected else 0)


if __name__ == '__main__':
    main()
