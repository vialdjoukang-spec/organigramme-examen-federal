import os, sys
# Patch 0002 · Hermès · 17.10.2026 · sur mobile, le mot touché reste visible au-dessus de la fenêtre épinglée.
# Déjà appliqué dans app_v2.html ; se rejoue après 0001 sur une copie (APP_FILE).
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s = open(p, encoding='utf-8').read()
A = "TIPEL.style.left=left+'px';if(kbd){"
B = ("TIPEL.style.left=left+'px';if(pin&&matchMedia('(max-width:620px)').matches){const tr=TIPEL.getBoundingClientRect();"
     "if(r.bottom>tr.top-8)scrollBy(0,r.bottom-tr.top+16)};if(kbd){")
assert s.count(A) == 1, ('ancrage', s.count(A))
open(p, 'w', encoding='utf-8').write(s.replace(A, B))
print('ok')
