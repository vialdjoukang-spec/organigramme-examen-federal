#!/usr/bin/env python3
"""Garde I1 : l'empreinte SHA-256 de orig/app.html ne doit jamais changer."""
import hashlib, os, sys
from _app import ROOT
EXPECTED = '1e067c6ecb82190d2f2ff8d6efadcf41bc73055b285604868872151d0d653b31'


def digest(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'orig', 'app.html')
    got = digest(path)
    if got != EXPECTED:
        sys.exit(f'ÉCHEC : orig/app.html a changé ({got[:16]}… au lieu de {EXPECTED[:16]}…).')
    print(f'Empreinte de orig/app.html conforme : {EXPECTED[:16]}…')
