#!/usr/bin/env python3
"""Contrôles après injection : taille (90 000 ≤ o < 150 000), balises (avant = après), contrôle controle3 du dépôt
(défauts nouveaux introduits par l'encadré), un seul bloc par DX, marqueurs appariés. Sortie : out/VERIFICATION.md"""
import os, re, sys, subprocess, tempfile, json, collections
ICI = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(os.path.dirname(ICI), 'out'); REPO = '/workspace/grok/etude/repo'
sys.path.insert(0, ICI); import _controle3_main as C3
class A: points, min, max, ex, script_ok = 14, 90_000, 149_999, 50, False
def ctrl(b):
    with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as f: f.write(b); t = f.name
    try: return C3.controler(t, {}, A, {})['defauts']
    finally: os.unlink(t)
L = ['# Vérification après injection', '', '| Fichier | Octets avant → après | Bande | Balises | Blocs | Défauts nouveaux (controle3) |', '|---|---|---|---|---|---|']
ok = True
for d, _, fs in os.walk(f'{OUT}/stage'):
    for f in sorted(fs):
        p = os.path.join(d, f); chemin = os.path.relpath(p, f'{OUT}/stage')
        av = subprocess.run(['git', '-C', REPO, 'show', f'origin/main:{chemin}'], capture_output=True).stdout
        ap = open(p, 'rb').read(); h = ap.decode()
        e0, e1 = C3.equilibre(av.decode()), C3.equilibre(h)
        deb = re.findall(r'EPI_PROFILES:DEBUT (DX\d+)', h); fin = re.findall(r'EPI_PROFILES:FIN (DX\d+)', h)
        d0, d1 = ctrl(av), ctrl(ap)
        nouv = {k: v['n'] - d0.get(k, {'n': 0})['n'] for k, v in d1.items() if v['n'] > d0.get(k, {'n': 0})['n']}
        bande = 'ok' if 90_000 <= len(ap) < 150_000 else ('basse (déjà avant)' if len(ap) < 90_000 and len(av) < 90_000 else 'HORS')
        bal = 'identiques' if e0 == e1 else f'CHANGÉES {e0}→{e1}'
        blocs = 'ok' if deb == fin and len(deb) == len(set(deb)) else 'ERREUR'
        if bande == 'HORS' or bal != 'identiques' or blocs != 'ok': ok = False
        L.append(f'| `{chemin}` | {len(av)} → {len(ap)} | {bande} | {bal} | {",".join(deb)} {blocs} | {nouv or "aucun"} |')
L += ['', f'Verdict : {"PASS" if ok else "ÉCHEC"}.']
open(f'{OUT}/VERIFICATION.md', 'w').write('\n'.join(L) + '\n'); print('\n'.join(L))
