import os, sys
# Patch 0013 · Dédale · 17.10.2026 · NC-0 : schéma clé « voie motrice » du VII (nc07.vues.voie_motrice, en premier).
# Le sélecteur de vues suit l'ordre de NC_VUE : la vue « Voie motrice » passe en tête, avant Face, Profil et Trois
# quarts ; la couche « voies » (fibres cortico-nucléaires) reçoit sa case dans « Couches ». Se rejoue après 0012.
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s = open(p, encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, 'Ancrage absent ou répété : ' + a[:60]
    s = s.replace(a, b)

rep("const NC_VUE={face:'Face',", "const NC_VUE={voie_motrice:'Voie motrice',face:'Face',")
rep("NC_COU=['trait','nerf','noyaux',", "NC_COU=['trait','voies','nerf','noyaux',")
rep("NC_COUL={trait:'Trait',nerf:'Nerf',", "NC_COUL={trait:'Trait',voies:'Voies cortico-nucléaires',nerf:'Nerf',")
open(p, 'w', encoding='utf-8', newline='').write(s)
print('0013 appliqué : vue « Voie motrice » en tête, couche « voies ».')
