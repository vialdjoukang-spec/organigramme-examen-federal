#!/usr/bin/env python3
"""PROMPT_L1 — porte bloquante (ordre de Vial du 10.11.2026).
Toute demande de fusion qui touche un LOT (Claude/LOT_*, ChatGPT_Codex/**/LOT_*, Grokbot/**/LOT_*, LOT_Claude_Finaux,
grok-LOTS-html) doit porter dans son corps la ligne exacte « Prompt L1 lu et appliqué ».
Lit l'événement GitHub (GITHUB_EVENT_PATH) ; hors pull_request, ne fait rien. Code 1 = refus."""
import json, os, re, subprocess, sys

PHRASE = 'Prompt L1 lu et appliqué'
LOT = re.compile(r'(^|/)(LOT_\d{3}|LOT_Claude_Finaux|grok-LOTS-html)(/|$)')


def main():
    ev = os.environ.get('GITHUB_EVENT_PATH')
    if not ev or not os.path.exists(ev):
        print('prompt_l1 : hors demande de fusion, rien à vérifier.'); return 0
    pr = (json.load(open(ev, encoding='utf-8')) or {}).get('pull_request')
    if not pr:
        print('prompt_l1 : hors demande de fusion, rien à vérifier.'); return 0
    base = os.environ.get('BASE_REF') or pr['base']['ref']
    diff = subprocess.run(['git', 'diff', '--name-only', f'origin/{base}...HEAD'], capture_output=True, text=True).stdout.split()
    lots = [f for f in diff if LOT.search(f)]
    if not lots:
        print('prompt_l1 : aucun fichier de LOT modifié.'); return 0
    if PHRASE in (pr.get('body') or ''):
        print(f'prompt_l1 : « {PHRASE} » présent ({len(lots)} fichier(s) de LOT).'); return 0
    print(f'ÉCHEC prompt_l1 : cette PR modifie {len(lots)} fichier(s) de LOT sans déclarer « {PHRASE} ».\n'
          'Lis PROMPT_Casern/PROMPT_LOTS_L1_10.11.26.<ia>.md (bloc L1 en tête), applique-le, puis ajoute cette ligne '
          'exacte au corps de la PR.')
    return 1


if __name__ == '__main__':
    sys.exit(main())
