import os, sys
# Patch 0013 · Hermès · 17.10.2026 · Couches des schémas à repères numérotés (Dédale, PR #28) : une couche peut avoir plusieurs
# groupes (#c et g.numeros[data-couche=c][data-etat]) ; chacun suit sa case, et un groupe propre à un état ne s’affiche que dans cet état.
# Se rejoue après 0012. L’ancrage doit apparaître une seule fois.
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s = open(p, encoding='utf-8').read()
OLD = 'function ckApply(fig){const s=fig.querySelector(\'svg\'),F=TIPEL.querySelector(\'.ck-couches\');if(!F)return;\n for(const i of F.querySelectorAll(\'input[data-ck=cou]\')){const g=s&&s.querySelector(`#${i.value},[data-couche="${i.value}"]`);i.closest(\'label\').hidden=!g;i.disabled=!g||!g.childElementCount;if(g)g.setAttribute(\'display\',i.checked?\'inline\':\'none\')}}\n'
NEW = '/* Couche c : tous ses groupes (#c ou [data-couche=c]) ; un groupe propre à un état (data-etat) ne s’affiche que dans cet état. */\nfunction ckApply(fig){const s=fig.querySelector(\'svg\'),F=TIPEL.querySelector(\'.ck-couches\');if(!F)return;const et=s&&ckEtats(s)&&s.dataset.etat||\'\';\n for(const i of F.querySelectorAll(\'input[data-ck=cou]\')){const G=s?[...s.querySelectorAll(`#${i.value},[data-couche="${i.value}"]`)]:[];i.closest(\'label\').hidden=!G.length;i.disabled=!G.some(g=>g.childElementCount);\n  G.forEach(g=>g.setAttribute(\'display\',i.checked&&(!et||!g.dataset.etat||g.dataset.etat===et)?\'inline\':\'none\'))}}\n'
assert s.count(OLD) == 1, 'Ancrage absent ou répété : ckApply'
s = s.replace(OLD, NEW)
open(p, 'w', encoding='utf-8').write(s)
print('0013 appliqué')
