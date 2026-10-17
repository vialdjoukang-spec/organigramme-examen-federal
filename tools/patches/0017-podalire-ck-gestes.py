import os, sys
# Patch 0017 · Podalire · 17.10.2026 · chaîne clinique, étape A : la fenêtre « Syndrome » affiche les gestes de
# l’examen (syn.gestes, clés k de GES) avant les signes ; chaque geste ouvre sa fiche « Pour marquer le point »
# (type g|région|rang) au niveau suivant de la pile. Une clé absente de GES n’est pas affichée (ck_build la refuse).
# L’onglet Gestes affiche aussi, sous le titre de la région, un lien vers la synthèse locale (loc|région|A) quand
# data/ck/loc.json décrit la région : c’est l’entrée des syndromes d’urgence du lot 1. Se rejoue après 0014.
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s = open(p, encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, 'Ancrage absent ou répété : ' + a[:60]
    s = s.replace(a, b)

rep("function ckArr(x){",
    "function ckGes(L){const o=[];for(const k of ckArr(L)){for(const r of (typeof GES!=='undefined'?GES:[])){const i=r.items.findIndex(x=>x.k===k);"
    "if(i>=0){o.push(ckL('g|'+r.id+'|'+i,r.items[i].s,r.items[i].p));break}}}return o.length?`<p><b>Gestes à faire</b> : ${o.join(', ')}.</p>`:''}\n"
    "function ckArr(x){")
rep("+ckLinks('Signes à rechercher','GLO','glo',e.signes)",
    "+ckGes(e.gestes)+ckLinks('Signes à rechercher','GLO','glo',e.signes)")
rep("$('#g-head').innerHTML=`<div class=\"row\" style=\"justify-content:space-between\"><h2>${q?'Résultats de recherche':esc(cr?.r||'')}</h2>",
    "$('#g-head').innerHTML=`<div class=\"row\" style=\"justify-content:space-between\"><h2>${q?'Résultats de recherche':esc(cr?.r||'')}</h2><span id=\"g-loc\"></span>")
rep("function ckArr(x){return",
    "function gLoc(){const el=$('#g-loc');if(!el)return;const f=()=>{const e=(ckData('LOC')||{})[GREG];el.innerHTML=e?ckL('loc|'+GREG+'|A','Syndromes d’urgence de la région →'):''};"
    "if(ckData('LOC'))f();else ckLoad('loc').then(f).catch(()=>{})}\nfunction ckArr(x){return")
rep("background:var(--ok)\"></i></div>`;\n $('#g-list').innerHTML=",
    "background:var(--ok)\"></i></div>`;gLoc();\n $('#g-list').innerHTML=")
open(p, 'w', encoding='utf-8', newline='').write(s)
print('0017 appliqué :', p)
