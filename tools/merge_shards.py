#!/usr/bin/env python3
"""Résout les conflits de data/ck/mono/*.json par fusion à 3 voies clé par clé (base, ours=HEAD, theirs=MERGE_HEAD)."""
import json, subprocess, sys
def show(ref, f):
    r = subprocess.run(['git', 'show', f'{ref}:{f}'], capture_output=True, text=True)
    return json.loads(r.stdout) if r.returncode == 0 and r.stdout.strip() else {}
base = subprocess.run(['git', 'merge-base', 'HEAD', 'MERGE_HEAD'], capture_output=True, text=True).stdout.strip()
for f in sys.argv[1:]:
    B, O, T = show(base, f), show('HEAD', f), show('MERGE_HEAD', f)
    out = {}
    for k in sorted(set(O) | set(T)):
        o, t, b = O.get(k), T.get(k), B.get(k)
        if o == t or t == b: v = o
        elif o == b: v = t
        else:
            v = o; print('CONFLIT RÉEL', f, k, '→ garde HEAD (à revoir)')
        if v is not None: out[k] = v
    open(f, 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1) + '\n')
    print(f, len(out), 'entrées')
