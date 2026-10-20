#!/usr/bin/env python3
"""Barrière commune : main autorise un SHA technique ; fusion clinique manuelle."""
import argparse
import base64
import json
import os
from pathlib import PurePosixPath
import re
import subprocess
import sys

REQUIRED = frozenset({'garde', 'html', 'tests', 'visuel', 'checkpoint', 'schemas'})
ORCHESTRATION = frozenset({'auto-fusion', 'file-fusion'})


def predecessors(plan, number):
    """Ancien lecteur conservé pour compatibilité ; jamais une autorisation du mandat."""
    found = []
    for chain in plan['chaines'].values():
        if number in chain:
            found.extend(chain[:chain.index(number)])
    return list(dict.fromkeys(found))


def ready(plan, number, state):
    """Dépendances historiques uniquement ; les entrées opérationnelles utilisent authorize."""
    for previous in predecessors(plan, number):
        try:
            if state(previous) not in {'MERGED', 'CLOSED'}:
                return False
        except Exception:
            return False
    return True


def validate_config(config):
    if (not isinstance(config, dict) or type(config.get('version')) is not int or config.get('version') != 1
            or config.get('actif') is not True
            or config.get('priorite_active') not in {'P0', 'P1', 'P2', 'P3', 'P4'}
            or config.get('fusion_clinique') != 'manuelle_centralisee'
            or not isinstance(config.get('autorisations_techniques'), list)):
        raise ValueError('Configuration de fusion canonique absente ou invalide')
    seen = set()
    for entry in config['autorisations_techniques']:
        if (not isinstance(entry, dict) or set(entry) != {'number', 'head_sha', 'priorite'}
                or type(entry['number']) is not int or entry['number'] <= 0
                or entry['number'] in seen
                or not isinstance(entry['head_sha'], str)
                or re.fullmatch(r'[0-9a-f]{40}', entry['head_sha']) is None
                or entry['priorite'] != config['priorite_active']):
            raise ValueError('Autorisation technique invalide, dupliquée ou hors priorité')
        seen.add(entry['number'])
    return config


def authorize(config, number, head_sha):
    validate_config(config)
    return any(e['number'] == number and e['head_sha'] == head_sha
               and e['priorite'] == config['priorite_active']
               for e in config['autorisations_techniques'])


def technical_path(path):
    """Liste de périmètres techniques ; les données cliniques ne sont jamais auto-fusionnées."""
    if not isinstance(path, str) or '..' in PurePosixPath(path).parts:
        return False
    if path.startswith('.github/workflows/'):
        return path.endswith(('.yml', '.yaml'))
    if path.startswith('tests/'):
        return path.endswith(('.py', '.js', '.sh'))
    if path.startswith('tools/'):
        if path.startswith(('tools/cours/lots/', 'tools/patches/')):
            return False
        return (path.endswith(('.py', '.sh')) or path == 'tools/mandat/integration.json'
                or path == 'tools/allowed_domains.txt')
    return path in {'AGENTS.md', 'HANDOFF.md', 'PROCHAINE_ACTION.md', 'ETAT.md', 'ETAT.json'} or (
        path.startswith(('docs/', 'audit/', 'journal/')) and path.endswith(('.md', '.json')))


def checks_green(checks, required=REQUIRED):
    if not isinstance(checks, list):
        return False
    found = set()
    for check in checks:
        if not isinstance(check, dict):
            return False
        name = check.get('name') or check.get('context')
        state = (check.get('conclusion') or check.get('state') or '').upper()
        if name in ORCHESTRATION and check.get('status') in {'QUEUED', 'IN_PROGRESS'}:
            continue  # Le job exécutant la barrière ne peut attendre sa propre fin.
        if check.get('status') and check['status'] != 'COMPLETED':
            return False
        if name in required:
            if state != 'SUCCESS':
                return False
            found.add(name)
        elif state not in {'SUCCESS', 'NEUTRAL', 'SKIPPED'}:
            return False
    return required <= found


def gh(*args):
    return subprocess.run(['gh', *args], capture_output=True, text=True,
                          timeout=45, check=True).stdout


def canonical_config(repo):
    # Le SHA de main fixe la lecture ; aucune configuration de la branche PR n'est utilisée.
    branch = json.loads(gh('api', f'repos/{repo}/branches/main'))
    main_sha = branch['commit']['sha']
    if re.fullmatch(r'[0-9a-f]{40}', main_sha) is None:
        raise ValueError('SHA main invalide')
    response = json.loads(gh('api', f'repos/{repo}/contents/tools/mandat/integration.json?ref={main_sha}'))
    if response.get('encoding') != 'base64':
        raise ValueError('Configuration main non encodée en base64')
    return validate_config(json.loads(base64.b64decode(response['content'])))


def changed_files(repo, number):
    result, page = [], 1
    while True:
        values = json.loads(gh('api', f'repos/{repo}/pulls/{number}/files?per_page=100&page={page}'))
        if not isinstance(values, list) or not values and page == 1:
            raise ValueError('Périmètre PR absent')
        for item in values:
            if not technical_path(item.get('filename')) or (
                    'previous_filename' in item and not technical_path(item['previous_filename'])):
                raise ValueError('Périmètre clinique ou inconnu : fusion manuelle obligatoire')
        result.extend(values)
        if len(values) < 100:
            return result
        page += 1


def pr_snapshot(repo, number):
    return json.loads(gh('pr', 'view', str(number), '--repo', repo, '--json',
                         'state,isDraft,labels,headRefOid,baseRefName,mergeStateStatus,statusCheckRollup,changedFiles'))


def authorized_snapshot(config, pr, number, expected_sha):
    if (pr.get('state') != 'OPEN' or pr.get('isDraft') is not False
            or pr.get('baseRefName') != 'main'
            or pr.get('mergeStateStatus') != 'CLEAN'
            or expected_sha is not None and expected_sha != pr.get('headRefOid')
            or not authorize(config, number, pr.get('headRefOid'))):
        return False
    labels = {item['name'] for item in pr.get('labels', [])}
    return ('audit-ok' in labels and 'attente-vial' not in labels
            and checks_green(pr.get('statusCheckRollup')))


def integration_ready(repo, number, expected_sha=None):
    """Deux observations complètes encadrent la lecture du périmètre.

    Ces lectures API ne sont pas une transaction atomique avec la fusion : une
    révocation postérieure à la dernière observation reste possible. Les appelants
    revérifient juste avant mutation ; --match-head-commit protège alors le SHA,
    pas une modification ultérieure des labels, de la CI ou de la configuration.
    """
    config = canonical_config(repo)
    pr = pr_snapshot(repo, number)
    if not authorized_snapshot(config, pr, number, expected_sha):
        return False
    head_sha = pr['headRefOid']
    files = changed_files(repo, number)
    if type(pr.get('changedFiles')) is not int or len(files) != pr['changedFiles']:
        return False  # Refuser aussi les PR dont l'API tronque le périmètre.
    # Une lecture du seul SHA ne voit pas une révocation ni une relance CI à SHA égal.
    final_config = canonical_config(repo)
    final_pr = pr_snapshot(repo, number)
    return (final_config == config
            and final_pr.get('changedFiles') == len(files)
            and authorized_snapshot(final_config, final_pr, number, head_sha))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('number', nargs='?', type=int)
    parser.add_argument('--head', help='SHA exact attendu par le coordinateur')
    parser.add_argument('--list', action='store_true', help='PR techniques explicitement autorisées sur main')
    parser.add_argument('--check', action='store_true', help='code de sortie non nul si fusion interdite')
    args = parser.parse_args()
    repo = os.environ.get('GH_REPO', 'vialdjoukang-spec/organigramme-examen-federal')
    try:
        if args.list:
            for entry in canonical_config(repo)['autorisations_techniques']:
                print(entry['number'])
            return 0
        if args.number is None:
            parser.error('numéro de PR requis')
        allowed = integration_ready(repo, args.number, args.head)
    except Exception as exc:
        print(f'Fusion suspendue : {type(exc).__name__}: {exc}', file=sys.stderr)
        if args.list:
            return 1
        allowed = False
    print('ready=' + str(allowed).lower())
    return int(args.check and not allowed)


if __name__ == '__main__':
    sys.exit(main())
