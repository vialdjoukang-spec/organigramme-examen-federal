#!/usr/bin/env python3
"""PUBLIER_COURS — prépare dans le site Pages la page réceptacle et les cours prêts (zéro modèle).
Copie : progression.html (générée par outils/receptacle.py), Claude/_polices, Claude/_reference, et pour chaque SSP de
Claude/_reference/prets.txt ses onze cours et son dossier d'images. Un SSP absent de prets.txt n'est jamais publié.
Usage : python3 outils/publier_cours.py _site"""
import os, sys, glob, shutil, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from receptacle import plage

site = sys.argv[1]
prets = open('Claude/_reference/prets.txt', encoding='utf-8').read().strip()
subprocess.run([sys.executable, 'outils/receptacle.py', '--audites', prets, '--sortie', os.path.join(site, 'progression.html')], check=True)
for d in ('Claude/_polices', 'Claude/_reference'):
    shutil.copytree(d, os.path.join(site, d), dirs_exist_ok=True)
n = 0
for lot in sorted(plage(prets)):
    src, dst = f'Claude/LOT_{lot:03d}', os.path.join(site, f'Claude/LOT_{lot:03d}')
    os.makedirs(dst, exist_ok=True)
    for f in glob.glob(os.path.join(src, f'LOT_{lot:03d}_Phase_*.html')):
        shutil.copy2(f, dst); n += 1
    if os.path.isdir(os.path.join(src, 'images')):
        shutil.copytree(os.path.join(src, 'images'), os.path.join(dst, 'images'), dirs_exist_ok=True)
print(f'{n} cours publiés pour {len(plage(prets))} SSP')
