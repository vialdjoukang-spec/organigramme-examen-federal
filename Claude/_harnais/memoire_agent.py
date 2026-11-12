#!/usr/bin/env python3
"""MÉMOIRE_AGENT — carnet persistant de chaque agent (zéro modèle). Un agent note en une ligne ce qu'il a établi
(source lue + citation, décision, AIPS vérifiée, reste à faire) ; l'agent suivant, ou lui-même après une coupure,
lit ce carnet (≈ 1–3 Ko) au lieu de tout relire. Les lignes ne s'effacent jamais (ajout seul).

  note <LOT> <DX.n|PhaseA> <type> <texte>   type ∈ source, aips, decision, image, reste, verdict
  lire <LOT> <DX.n|PhaseA> [type]           → dernières 40 lignes utiles
Fichier : Claude/LOT_0NN/memoire/<cible>.md (versionné avec le LOT).
"""
import sys, os, datetime

def chemin(lot, cible):
    d = f'Claude/LOT_{int(lot):03d}/memoire'; os.makedirs(d, exist_ok=True); return f'{d}/{cible}.md'

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print(__doc__); sys.exit(0)
    act, lot, cible = sys.argv[1:4]
    f = chemin(lot, cible)
    if act == 'note':
        typ, texte = sys.argv[4], ' '.join(sys.argv[5:]).replace('\n', ' ')
        with open(f, 'a', encoding='utf-8') as h:
            h.write(f'- {datetime.datetime.now():%d.%m %H:%M} · {typ} · {texte[:400]}\n')
    else:
        typ = sys.argv[4] if len(sys.argv) > 4 else ''
        L = open(f, encoding='utf-8').read().splitlines() if os.path.exists(f) else []
        print('\n'.join([l for l in L if f'· {typ} ·' in l or not typ][-40:]) or '(carnet vide)')
