"""stdin : JSON de `gh pr checks --json name,bucket`. Sortie : VERT (0), ROUGE <échecs> (1), ATTENTE (2)."""
import json, sys
def verdict(txt):
    try: c = json.loads(txt or '[]')
    except ValueError: return 'ROUGE sortie illisible', 1
    if not c: return 'ATTENTE', 2
    bad = [x['name'] for x in c if x.get('bucket') in ('fail', 'cancel')]
    if bad: return 'ROUGE ' + ','.join(bad), 1
    if any(x.get('bucket') == 'pending' for x in c): return 'ATTENTE', 2
    return 'VERT', 0
if __name__ == '__main__':
    m, rc = verdict(sys.stdin.read()); print(m); sys.exit(rc)
