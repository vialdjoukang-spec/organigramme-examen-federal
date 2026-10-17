#!/usr/bin/env python3
"""Verrou des chaînes pour l'auto-fusion : le filet et le workflow suivent le même ordre."""
import base64
import json
import os
from pathlib import Path
import subprocess
import sys


def predecessors(plan, number):
    found = []
    for chain in plan['chaines'].values():
        if number in chain:
            found.extend(chain[:chain.index(number)])
    return list(dict.fromkeys(found))


def ready(plan, number, state):
    for previous in predecessors(plan, number):
        try:
            status = state(previous)
        except Exception:
            return False
        if status not in {'MERGED', 'CLOSED'}:
            return False
    return True


def main():
    number = int(sys.argv[1])
    plan = json.loads((Path(__file__).parent/'etapes.json').read_text())
    repo = os.environ.get('GH_REPO', 'vialdjoukang-spec/organigramme-examen-federal')
    if os.environ.get('GITHUB_ACTIONS') == 'true':
        try:
            response = subprocess.run(['gh', 'api', f'repos/{repo}/contents/tools/etapes.json?ref=main',
                                       '--jq', '.content'], capture_output=True, text=True,
                                      timeout=30, check=True)
            plan = json.loads(base64.b64decode(response.stdout))
        except Exception:
            print('Plan de main inaccessible : auto-fusion suspendue.', file=sys.stderr)
            print('ready=false')
            return

    def state(previous):
        result = subprocess.run(['gh', 'pr', 'view', str(previous), '--repo', repo,
                                 '--json', 'state', '--jq', '.state'],
                                capture_output=True, text=True, timeout=30, check=True)
        print(f'Prédecesseur #{previous} : {result.stdout.strip()}', file=sys.stderr)
        return result.stdout.strip()

    print('ready='+str(ready(plan, number, state)).lower())


if __name__ == '__main__':
    main()
