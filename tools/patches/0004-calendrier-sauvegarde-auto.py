import os, sys
# Patch 0004 · Hermès · 17.10.2026 · Calendrier interactif (clic, plage, recherche, déplacement, redimensionnement,
# toucher, clavier) et sauvegarde automatique fiable (miroir IndexedDB, versions, persistance, fichier automatique).
# Se rejoue après 0001 à 0003 sur une copie (APP_FILE). Chaque ancrage doit apparaître une seule fois.
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s = open(p, encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, 'Ancrage absent ou répété : ' + a[:60]
    s = s.replace(a, b)

CSS = ("#sv-s,#ver{flex-basis:100%;margin:0}#ver{border-top:1px solid var(--line);padding-top:8px}#ver .row{display:flex;flex-wrap:wrap;gap:8px;align-items:center}"
       ".ver-l{list-style:none;margin:6px 0 0;padding:0;max-height:320px;overflow:auto}.ver-l li{display:flex;flex-wrap:wrap;gap:8px 12px;align-items:center;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--line)}"
       ".cq{padding:10px 14px}.cq input{width:100%;box-sizing:border-box}#cq-r,#qp-r{list-style:none;margin:6px 0 0;padding:0;max-height:260px;overflow:auto}"
       ".cq-i{display:flex;align-items:stretch;gap:6px;margin:3px 0}.cq-i .b{min-height:36px}.cq-i .cq-p{flex:1;min-width:0;text-align:left;display:flex;gap:8px;align-items:center}"
       ".cq-p code{font-weight:700}.cq-p span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.cq-i.on .cq-p{outline:2px solid var(--ok)}"
       ".blk .rz{position:absolute;left:0;right:0;bottom:0;height:9px;cursor:ns-resize;touch-action:none}.blk.drag{opacity:.88;pointer-events:none;z-index:5}"
       ".blk.grab{outline:2px dashed var(--bc)}.blk:focus-visible{outline:3px solid var(--ink);outline-offset:1px}"
       ".rng{position:absolute;left:2px;right:2px;z-index:4;pointer-events:none;border:2px dashed var(--ok);border-radius:8px;background:color-mix(in srgb,var(--ok) 18%,transparent);font-size:.7rem;font-weight:600;padding:2px 6px}"
       "#qp{position:fixed;z-index:60;width:min(380px,calc(100vw - 24px));max-height:calc(100vh - 24px);overflow:auto;box-sizing:border-box;background:var(--paper);color:var(--ink);"
       "border:1px solid var(--line);border-radius:12px;box-shadow:0 20px 50px -20px rgba(0,0,0,.45);padding:12px 14px}#qp h3{margin:0 0 8px}"
       "#qp .row{display:flex;flex-wrap:wrap;gap:6px 8px;align-items:center;margin:6px 0}#qp input[type=search]{width:100%;box-sizing:border-box}")
rep('#bak-m.ok{color:var(--ok)}', '#bak-m.ok{color:var(--ok)}' + CSS)

rep('<input type="file" id="bak-f"',
    '<button class="b" id="sv-v" type="button" aria-expanded="false" aria-controls="ver">Restaurer une version</button>'
    '<button class="b" id="sv-fb" type="button" hidden>Activer un fichier de sauvegarde automatique</button>'
    '<input type="file" id="bak-f"')
rep('<div id="bak-pv" hidden></div>', '<div id="bak-pv" hidden></div><div id="ver" hidden></div><p id="sv-s" class="st"></p>')

rep('<div class="gridwrap"><div class="grid" id="grid"></div></div>',
    '<div class="card cq"><label class="st" for="cq">Cherchez un cours ou un SSP par son nom ou son code, puis placez-le ou ouvrez-le.</label>'
    '<input type="search" id="cq" placeholder="Ex. dyspnee, G4, insuffisance cardiaque" autocomplete="off" aria-controls="cq-r">'
    '<ul id="cq-r" hidden></ul><p class="st" id="cq-m" role="status" aria-live="polite"></p></div>'
    '<div class="gridwrap"><div class="grid" id="grid"></div></div>'
    '<div id="qp" role="dialog" aria-labelledby="qp-h" hidden><h3 id="qp-h">Nouvelle séance</h3>'
    '<div class="row"><label class="st" for="qp-date">Jour</label><input type="date" id="qp-date">'
    '<label class="st" for="qp-s">Début</label><input type="time" id="qp-s" step="900">'
    '<label class="st" for="qp-d">Durée</label><select id="qp-d"></select></div>'
    '<div class="row"><label class="st" for="qp-a">Activité</label><select id="qp-a"></select></div>'
    '<input type="search" id="qp-q" placeholder="Chapitre : nom ou code (ex. G4)" aria-label="Chercher le chapitre de la séance" autocomplete="off">'
    '<ul id="qp-r"></ul>'
    '<div class="row"><button class="b p" id="qp-ok" type="button" disabled>Créer la séance</button><button class="b" id="qp-no" type="button">Annuler</button></div></div>')

rep('<p class="st">Glissez un chapitre sur une plage, ou touchez-le puis touchez la plage. Aimantation au quart d’heure.</p>',
    '<p class="st">Glissez un chapitre sur une plage, ou touchez-le puis touchez la plage. Cliquez sur une plage vide, ou tirez sur plusieurs plages, pour créer une séance. '
    'Déplacez une séance en la faisant glisser, et changez sa durée par son bord inférieur ; au toucher, maintenez-la d’abord un instant. '
    'Au clavier, les flèches déplacent la séance sélectionnée, et Maj avec les flèches change sa durée. Tout s’aimante au quart d’heure.</p>')

rep('localStorage.setItem(k,v);if(lsBad[k]){delete lsBad[k];bakShow()}return true}',
    'localStorage.setItem(k,v);if(lsBad[k]){delete lsBad[k];bakShow()}svTouch();return true}')

rep('<div class="blk${x.done?\' done\':\'\'}" data-id="${id}"', '<div class="blk${x.done?\' done\':\'\'}" tabindex="0" data-id="${id}"')
rep('<span class="t">${esc(x.act)} · ${esc(s[1])}</span></div>', '<span class="t">${esc(x.act)} · ${esc(s[1])}</span><span class="rz" aria-hidden="true"></span></div>')
rep('<div class="col" data-d="${k}"', '<div class="col" data-d="${k}" data-wd="${(d.getDay()+6)%7+1}"')
rep('<div class="hd${iso(d)===t?\' today\':\'\'}">', '<div class="hd${iso(d)===t?\' today\':\'\'}" data-wd="${(d.getDay()+6)%7+1}">')

SV = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '0004-sauvegarde.js'), encoding='utf-8').read()
CAL = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '0004-calendrier.js'), encoding='utf-8').read()
A = "bakMsg('La sauvegarde importée est chargée dans ce navigateur.','ok')}}catch(e){}\n"
rep(A, A + SV)
G = "$('#grid').addEventListener('click',e=>{const b=e.target.closest('.blk');if(b){openEdit(b.dataset.id);return}const c=e.target.closest('.col');if(c&&sel){addAt(c,e.clientY,sel);sel=null;renderList()}});"
rep(G, CAL)
open(p, 'w', encoding='utf-8', newline='').write(s)
print('0004 appliqué.')
