#!/usr/bin/env python3
"""Interdit les écritures d'un auteur hors de son préfixe réservé."""
import argparse, subprocess
from pathlib import PurePosixPath

def validate(paths, lot, role):
    assert role in {'A','B1','B2','B3','B4','B5'}
    prefix=f'LOT_Candidats/LOT_{lot:03d}/{role}/'
    for path in paths:
        assert path.startswith(prefix) and '..' not in PurePosixPath(path).parts,f'Écriture hors réservation : {path}'

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('base');p.add_argument('head');p.add_argument('--lot',type=int,required=True);p.add_argument('--role',required=True);a=p.parse_args()
    # --no-renames expose source et cible ; une suppression de l'autre auteur reste interdite.
    paths=subprocess.check_output(['git','diff','--no-renames','--name-only',a.base,a.head],text=True).splitlines()
    validate(paths,a.lot,a.role); print(f'Préfixe réservé respecté : {len(paths)} chemins')
