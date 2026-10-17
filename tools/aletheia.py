#!/usr/bin/env python3
"""Alétheia · Janus · vérité des sources : doses (G1), source et date (G2), domaines (G3).
Raccourci de tools/audit/niveau1.py --only G1,G2,G3 ; mêmes options (--racine, --sortie)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audit'))
from niveau1 import main  # noqa: E402

if __name__ == '__main__':
    sys.exit(main(['--only', 'G1,G2,G3'] + sys.argv[1:]))
