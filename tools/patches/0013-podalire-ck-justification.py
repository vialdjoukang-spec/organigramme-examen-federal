import os, sys
# Patch 0013 · Podalire · 17.10.2026 · G8 : la fenêtre « Exploration » affiche pour chaque examen le mécanisme, le principe,
# ce qu’il recherche et pourquoi ce choix ; la fenêtre « Prise en charge » affiche pour chaque moyen le mécanisme, le principe,
# le moyen nommé, pourquoi ce choix et ses limites, une ligne par partie. Le syndrome renvoie à la vue de schéma liée
# (syn.vues, p. ex. nc|nc07|voie_motrice) ; une vue pas encore livrée retombe sur la première vue du nerf.
# L’ancien champ pourquoi reste lu pour les jeux d’essai. Se rejoue après 0012.
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s = open(p, encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, 'Ancrage absent ou répété : ' + a[:60]
    s = s.replace(a, b)

rep("function ckList(t,L,f){", "function ckJ(l,v){return v?`<br><i>${l}</i> : ${ckP(v)}`:''}\nfunction ckList(t,L,f){")
rep("CK_MOY={pharmaco:'Pharmacologique',interventionnel:'Interventionnel',reeducation:'Rééducation',suivi:'Suivi'}",
    "CK_MOY={pharmaco:'Pharmacologique',interventionnel:'Interventionnel',reeducation:'Rééducation',suivi:'Suivi',chirurgie:'Chirurgical',autre:'Mesure locale'}")
rep("plan:'Plan',tour:'Tour à 8 vues'}", "plan:'Plan',voie_motrice:'Voie motrice',tour:'Tour à 8 vues'}")
rep("+ckLinks('Hypothèses','HYP','hyp',e.hyp||e.orientation)+ckFoot(e)}}",
    "+ckLinks('Hypothèses','HYP','hyp',e.hyp||e.orientation)"
    "+(ckArr(e.vues).length?`<p><b>Sur le schéma</b> : ${ckArr(e.vues).map(v=>ckL(v,ncVue(String(v).split('|')[2]||v))).join(', ')}.</p>`:'')+ckFoot(e)}}")
rep("m=>(m.type?`<i>${esc(CK_MOY[m.type]||m.type)}</i> : `:'')+ckP(m.texte)+ckDose(m.dose_ref)",
    "m=>(m.type?`<b>${esc(CK_MOY[m.type]||m.type)}</b>`:'')+ckJ('Mécanisme',m.mecanisme)+ckJ('Principe',m.principe)"
    "+(m.mecanisme||m.principe?'<br><i>Moyen</i> : ':m.type?' : ':'')+ckP(m.texte)+ckDose(m.dose_ref)"
    "+ckJ('Pourquoi ce choix',m.pourquoi_ce_choix)+ckJ('Limites',m.limites)")
rep("part=(l,v)=>v?` <i>${l}</i> : ${ckP(v)}`:'',",
    "part=(l,v)=>v?` <i>${l}</i> : ${ckP(v)}`:'',jx=o=>ckJ('Mécanisme',o.mecanisme)+ckJ('Principe',o.principe)+ckJ('Recherche',o.recherche)"
    "+ckJ('Pourquoi cet examen',o.pourquoi_ce_choix||o.pourquoi)+ckJ('Précautions',o.precautions)+ckJ('Alternative',o.alternative),")
rep("${ckP(R.nom)}${part('Recherche',R.recherche)}${sr(R.src)}", "${ckP(R.nom)}${jx(R)}${sr(R.src)}")
rep("${ckP(l.nom)}${part('Pourquoi',l.pourquoi)}${part('Précautions',l.precautions)}${part('Recherche',l.recherche)}${part('Alternative',l.alternative)}${sr(l.src)}",
    "${ckP(l.nom)}${jx(l)}${sr(l.src)}")
open(p, 'w', encoding='utf-8', newline='').write(s)
print('0013 appliqué :', p)
