import os, sys
# Patch 0016 · Fond pâle par défaut · 17.10.2026.
# Extrait d’Apollon (patch 0005 / jetons) : uniquement le fond et les couleurs de surface
# par défaut (#fbfbf8, sans teinte jaune), contraste AA. Pas de sélecteur à 10 thèmes,
# pas de polices système, pas d’UI « Thème de fond d’écran ».
# Le mélange « Fond doré » (--gilt) est coupé à 0 et n’écrit plus --bg en clair
# (le réglage d-gilt reste masqué, « réglage retiré »).
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s = open(p, encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, 'Ancrage absent ou répété : ' + a[:70]
    s = s.replace(a, b)

assert s.count('Fond pâle par défaut') == 0, 'Patch déjà appliqué.'

# 1. Jetons clair (extrait de tools/patches/apollon-jetons.css, ligne --bg:#fbfbf8).
rep(
    ':root{--bg:#f6f1e4;--paper:#fffdf8;--ink:#1c1a15;--mut:#6d675b;--line:#e6dfcd;--soft:#efe8d6;--gold:#a8842f;--gold2:#d6b25a;--deep:#5f4813;--ok:#2f7a4a;--warn:#a5671a;--bad:#a3322c;--grid:#ece4d0;--grid2:#f4eedf;',
    ':root{--bg:#fbfbf8;--paper:#ffffff;--ink:#1a1a1a;--mut:#4a4a4a;--line:#dededb;--soft:#f3f3f1;--gold:#7a5b12;--gold2:#d9b65e;--deep:#4a380b;--ok:#1d6a3a;--warn:#8a5207;--bad:#a12a24;--grid:#e6e6e3;--grid2:#f6f6f4;',
)

# 2. Avant JS : gilt à 0 (plus de flash doré) ; encre lisible sur fond pâle.
rep(':root{--gilt:.5;--ink:#100e09;--mut:#3f3a30;--fs:100%}',
    ':root{--gilt:0;--ink:#1a1a1a;--mut:#4a4a4a;--fs:100%}')

# 3. Le mélange doré ne redéfinit plus --bg en clair (ancre unique).
rep(':root{--bg:color-mix(in srgb,#f6f1e4 calc(var(--gilt)*100%),#ffffff)}',
    ':root{--bg:#fbfbf8}/* Fond pâle par défaut */')

# 4. Valeur initiale et secours JS : 0 % (plus 50 %).
rep('disp:{gilt:50,fs:100}', 'disp:{gilt:0,fs:100}')
rep("setProperty('--gilt',(d.gilt??50)/100)", "setProperty('--gilt',(d.gilt??0)/100)")
rep("$('#d-gilt').value=d.gilt??50", "$('#d-gilt').value=d.gilt??0")
rep("$('#d-gv').textContent=(d.gilt??50)+' %'", "$('#d-gv').textContent=(d.gilt??0)+' %'")

open(p, 'w', encoding='utf-8', newline='').write(s)
print('Patch 0016 (fond pâle) appliqué.')
