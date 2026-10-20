import os, sys
# Patch 0120 · GAMMA · 20.10.2026 · CS : régions sur une ligne, couleurs, état sélectionné (CSS + JS de configuration).
# Rejeu : APP_FILE=app_v2.html python3 tools/patches/0120-gamma-cs-regions.py (jamais sur orig/app.html).
p=os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s=open(p,encoding='utf-8').read()
A='<link rel="stylesheet" href="assets/style/app-2.css">'
B=A+'<link rel="stylesheet" href="assets/style/cs-regions.css"><script src="assets/config/cs-regions.js" defer></script>'
if B not in s:
    assert s.count(A)==1,(A,s.count(A)); s=s.replace(A,B)
open(p,'w',encoding='utf-8').write(s)
