"""stdin : JSON de `gh pr checks --json name,bucket`. Sortie : VERT (0), ROUGE <échecs> (1), ATTENTE (2)."""
import json, sys

REQUIS = ('garde', 'html', 'tests', 'visuel', 'checkpoint', 'schemas')

def verdict(txt):
    try: c = json.loads(txt or '[]')
    except ValueError: return 'ROUGE sortie illisible', 1
    if not isinstance(c, list): return 'ROUGE sortie illisible', 1
    if not c: return 'ATTENTE', 2
    if any(not isinstance(x, dict) or not isinstance(x.get('name'), str)
           or x.get('bucket') not in ('pass', 'fail', 'cancel', 'pending', 'skipping')
           for x in c):
        return 'ROUGE contrôle illisible', 1
    bad = [x['name'] for x in c if x.get('bucket') in ('fail', 'cancel')]
    if bad: return 'ROUGE ' + ','.join(bad), 1
    if any(x.get('bucket') == 'pending' for x in c): return 'ATTENTE', 2
    return 'VERT', 0


def snapshot_verdict(txt, expected_sha):
    """Une seule observation GitHub lie les contrôles à la tête attendue."""
    try:
        snapshot = json.loads(txt)
        if snapshot['headRefOid'] != expected_sha:
            return 'ROUGE tête de PR différente du SHA attendu', 1
        checks = snapshot['statusCheckRollup']
        if not isinstance(checks, list):
            raise ValueError('contrôles absents')
        rows, successes = [], set()
        for check in checks:
            name = check.get('name') or check.get('context')
            if check.get('status') and check['status'] != 'COMPLETED':
                bucket = 'pending'
            else:
                state = check.get('conclusion') or check.get('state')
                bucket = {'SUCCESS': 'pass', 'FAILURE': 'fail', 'ERROR': 'fail',
                          'CANCELLED': 'cancel', 'TIMED_OUT': 'fail',
                          'ACTION_REQUIRED': 'fail', 'STARTUP_FAILURE': 'fail',
                          'STALE': 'fail', 'PENDING': 'pending', 'EXPECTED': 'pending',
                          'NEUTRAL': 'skipping', 'SKIPPED': 'skipping'}.get(state)
            rows.append({'name': name, 'bucket': bucket})
            if bucket == 'pass':
                successes.add(name)
            elif name in REQUIS and bucket == 'skipping':
                return 'ROUGE contrôle requis ignoré : '+name, 1
        message, code = verdict(json.dumps(rows))
        if code:
            return message, code
        missing = set(REQUIS) - successes
        if missing:
            return 'ATTENTE contrôles requis : '+','.join(sorted(missing)), 2
        return message, code
    except (ValueError, KeyError, TypeError, AttributeError):
        return 'ROUGE observation GitHub illisible', 1

if __name__ == '__main__':
    txt = sys.stdin.read()
    m, rc = snapshot_verdict(txt, sys.argv[1]) if len(sys.argv) > 1 else verdict(txt)
    print(m); sys.exit(rc)
