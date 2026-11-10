#!/usr/bin/env python3
"""ATTRIBUTIONS — propriétaire exclusif de chaque LOT, lu dans ATTRIBUTIONS.json à la racine du dépôt
(ordre de Vial du 10.11.2026). Jamais déduit de l'auteur, de la branche ni du dossier.

Usage : python3 outils/attributions.py [--verifier] [--lot 75]
"""
import os, sys, json, argparse

IAS = ('Claude', 'ChatGPT_Codex', 'Grokbot')
_CACHE = {}


def chemin_defaut():
    ici = os.path.dirname(os.path.abspath(__file__))
    for d in (os.getcwd(), os.path.dirname(ici)):
        p = os.path.join(d, 'ATTRIBUTIONS.json')
        if os.path.exists(p):
            return p
    raise FileNotFoundError('ATTRIBUTIONS.json introuvable (racine du dépôt)')


def charger(chemin=None):
    chemin = chemin or chemin_defaut()
    if chemin not in _CACHE:
        _CACHE[chemin] = json.load(open(chemin, encoding='utf-8'))
    return _CACHE[chemin]


def proprietaire(lot, chemin=None):
    """Propriétaire exclusif du LOT (int ou '075')."""
    return charger(chemin)['lots'][f'{int(lot):03d}']


def lots_de(ia, chemin=None):
    return sorted(int(k) for k, v in charger(chemin)['lots'].items() if v == ia)


def verifier(chemin=None):
    A = charger(chemin)
    cles = sorted(int(k) for k in A['lots'])
    erreurs = []
    if cles != list(range(1, 249)):
        erreurs.append(f'LOTs manquants ou en trop : {sorted(set(range(1, 249)) ^ set(cles))}')
    if set(A['lots'].values()) - set(IAS):
        erreurs.append(f'IA inconnue : {set(A["lots"].values()) - set(IAS)}')
    for ia in IAS:
        n = len(lots_de(ia, chemin))
        if n != A['ias'][ia]['nombre']:
            erreurs.append(f'{ia} : {n} LOTs listés, {A["ias"][ia]["nombre"]} déclarés')
    return erreurs


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--verifier', action='store_true')
    ap.add_argument('--lot', type=int)
    a = ap.parse_args()
    if a.lot:
        print(proprietaire(a.lot))
    e = verifier()
    if e:
        print('\n'.join(e)); sys.exit(1)
    print('ATTRIBUTIONS.json : 248 LOTs, aucun doublon, aucun trou ; ' +
          ', '.join(f'{ia} {len(lots_de(ia))}' for ia in IAS))
