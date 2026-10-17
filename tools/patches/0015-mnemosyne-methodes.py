import os, sys
# Patch 0015 · Mnémosyne · 17.10.2026 · Onglet « Mémorisation » fondé sur les preuves (chantier 2, phase 2).
# Douze méthodes sourcées (data/MEM.json → assets/memo/mem.js, window.MEM_DATA, chargé à la demande par memLoad,
# compatible file://) ; type m|id de tipFor (survol, clic, toucher, clavier, épinglage) ; bouton « i » sur chaque stratégie ;
# options « Rétroaction obligatoire » et « Réapprentissage successif » ; consigne de séance tirée des options cochées.
# Les réglages existants (meth, int, rappel, test, inter, feyn, ret, max, hor) restent intacts. Se rejoue après 0012.
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s = open(p, encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, 'Ancrage absent ou répété : ' + a[:60]
    s = s.replace(a, b)

# Style : bandeau de titre vert pâle, titres en gras noir, texte justifié.
rep('.opt{display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}',
    '.opt{display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}'
    '.m-ev{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(min(420px,100%),1fr));margin-top:10px}'
    '.m-it{border:1px solid var(--line);border-radius:12px;background:#fff;min-width:0;overflow:hidden}'
    '.m-it h3{margin:0;padding:8px 12px;background:#eaf4ec;border-bottom:1px solid #cfe3d4;font-size:.95rem;line-height:1.35;font-weight:700;color:#000;display:flex;gap:8px;align-items:baseline}'
    '.m-it h3 .tw{color:#000}.m-n{flex:none;display:inline-grid;place-items:center;min-width:1.7em;height:1.7em;border-radius:50%;background:#fff;border:1px solid #2f7a4a;font-size:.78rem;color:#000}'
    '.m-it p{margin:8px 12px;text-align:justify;hyphens:auto;line-height:1.45;overflow-wrap:anywhere}.m-it p b{color:#000}.m-it .st a,.m-ref a{color:var(--deep)}'
    '.m-cons{margin:10px 0 4px;text-align:justify;line-height:1.5}.m-intro{text-align:justify}.m-ref{margin:4px 0 0;padding-left:18px}.m-ref li{margin:3px 0;text-align:justify}')

# HTML : options nouvelles et libellé du rappel libre (les identifiants existants ne changent pas).
rep('<label><input type="checkbox" id="m-rappel"><span><b>Rappel libre avant relecture</b> : noter de mémoire le plan du SSP, puis vérifier.</span></label>',
    '<label><input type="checkbox" id="m-rappel"><span><b>Rappel libre avant relecture et avant les QCM</b> : noter de mémoire le plan du SSP, puis vérifier.</span></label>')
rep('<label><input type="checkbox" id="m-feyn"><span><b>Explication à voix haute</b> : exposer le SSP en 3 minutes, comme à un étudiant.</span></label>',
    '<label><input type="checkbox" id="m-feyn"><span><b>Explication à voix haute</b> : exposer le SSP en 3 minutes, comme à un étudiant.</span></label>'
    '<label><input type="checkbox" id="m-retro"><span><b>Rétroaction obligatoire</b> : lire la correction de chaque question, même juste.</span></label>'
    '<label><input type="checkbox" id="m-reap"><span><b>Réapprentissage successif</b> : retenter chaque question ratée jusqu’à la réponse juste, à chaque séance.</span></label>')
rep('<div class="card"><h2>À réviser</h2><div class="kpis" id="m-kpi"></div>',
    '<div class="card" id="m-ev"><h2>Méthodes fondées sur les preuves</h2><p class="st m-intro">Ces douze méthodes s’appuient sur des méta-analyses et des essais publiés. '
    'Chaque nom s’ouvre au survol, au clic ou au toucher : la fenêtre donne le principe, l’usage pour l’examen fédéral, les preuves chez les étudiants en médecine et les références avec leur DOI. '
    'La taille d’effet g se lit ainsi : 0,2 correspond à un effet faible, 0,5 à un effet moyen et 0,8 à un effet fort.</p>'
    '<div class="m-ev" id="m-evl" aria-live="polite"><p class="st">Les douze méthodes se chargent.</p></div></div>\n'
    ' <div class="card"><h2>À réviser</h2><div class="kpis" id="m-kpi"></div><p class="m-cons" id="m-cons"></p>')

# Réglages : deux clés nouvelles, actives par défaut ; les clés existantes gardent leurs valeurs.
rep("const MDEF={meth:'leitner',int:'1,3,7,21,60',rappel:true,test:true,inter:true,feyn:false,ret:90,max:12,hor:12};",
    "const MDEF={meth:'leitner',int:'1,3,7,21,60',rappel:true,test:true,inter:true,feyn:false,retro:true,reap:true,ret:90,max:12,hor:12};")
rep("['rappel','test','inter','feyn'].forEach(k=>$('#m-'+k).checked=!!m[k]);",
    "['rappel','test','inter','feyn','retro','reap'].forEach(k=>$('#m-'+k).checked=!!m[k]);memOpt();memCons(m);if(!$('#v-memo').hidden)memEv();")
rep("feyn:$('#m-feyn').checked,", "feyn:$('#m-feyn').checked,retro:$('#m-retro').checked,reap:$('#m-reap').checked,")

# Fenêtre d'information : type m|id.
rep(" const ck=ckTip(ty,a,b);if(ck!==undefined)return ck;",
    " if(ty==='m')return memTip(a,key);\n const ck=ckTip(ty,a,b);if(ck!==undefined)return ck;")

rep("/* ---------- MNÉMÉ : mémorisation espacée ---------- */", r"""/* ---------- Mnémosyne : méthodes fondées sur les preuves (assets/memo/mem.js, chargé à la demande) ---------- */
let MEMP=null,memFail=false;function memLoad(){if(window.MEM_DATA)return Promise.resolve(window.MEM_DATA);return MEMP||(MEMP=new Promise((ok,ko)=>{const e=document.createElement('script');e.src='assets/memo/mem.js';e.async=true;const no=()=>{MEMP=null;memFail=true;e.remove();ko(new Error('memLoad'))};e.onload=()=>window.MEM_DATA?ok(window.MEM_DATA):no();e.onerror=no;document.head.appendChild(e)}))}
function memMd(t){return esc(t||'').replace(/\*([^*]+)\*/g,'<i>$1</i>')}
function memDoi(r){return `<a href="${esc(r.url)}" target="_blank" rel="noopener">${esc(r.cite||'doi:'+r.doi)}</a>`}
function memMed(m){const P=m.preuves_medecine;if(!P)return 'aucune donnée dans la note de recherche.';const st=P.statut||'',t=P.texte||'';return t.toLowerCase().startsWith(st.toLowerCase())?memMd(t):memMd(st.charAt(0).toUpperCase()+st.slice(1)+'. '+t)}
function memTip(a,key){const D=window.MEM_DATA,hd='Mémorisation fondée sur les preuves';
 if(!D){if(memFail)return {hd,ti:'Fiche indisponible',h:'<p class="st">La fiche n’a pas pu se charger ; rechargez la page.</p>'};const re=()=>{if(!TIPEL.hidden&&tipK===key)showTip({dataset:{t:key}},tipPin,tipOp||TIPEL,false,true)};memLoad().then(re,re);return {hd,ti:'…',h:'<p class="st">Chargement…</p>'}}
 const m=D.methodes.find(x=>x.id===a);if(!m)return null;
 return {hd:hd+' · méthode '+m.n+' sur 12',ti:m.nom,h:`<p>${memMd(m.principe)}</p><p><b>Pour l’examen fédéral</b> : ${memMd(m.examen)}</p>`
  +(m.consequence_application?`<p><b>Conséquence pour l’application</b> : ${memMd(m.consequence_application)}</p>`:'')
  +(m.preuves_generales?`<p><b>Preuves générales</b> : ${memMd(m.preuves_generales)}</p>`:'')
  +`<p><b>Preuves en médecine</b> : ${memMed(m)}</p><p><b>Références</b> :</p><ul class="m-ref">${m.references.map(r=>`<li>${memMd(r.complete)} <a href="${esc(r.url)}" target="_blank" rel="noopener">doi:${esc(r.doi)}</a></li>`).join('')}</ul>`,
  src:'note de recherche de Mnémosyne ; chaque DOI vérifié dans Crossref et lu le 17.10.2026'}}
function memCard(m){const y=m.synthese||{},g=y.preuve_generale&&y.preuve_generale!=='—'?y.preuve_generale:'',d=y.preuve_medecine&&y.preuve_medecine!=='—'?y.preuve_medecine.replace(' : ',', '):'';
 const niv=[g,d?'chez les étudiants ou médecins en formation : '+d.charAt(0).toLowerCase()+d.slice(1):''].filter(Boolean).join(' ; ');
 return `<article class="m-it" id="m-it-${esc(m.id)}"><h3 data-t="m|${esc(m.id)}"><span class="m-n">${m.n}</span><span><span class="tw" tabindex="0" role="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="tip">${esc(m.nom)}</span><button class="ti" type="button" aria-label="Preuves et mode d’emploi">i</button></span></h3>`
  +`<p><b>Niveau de preuve</b> : ${esc(niv)}.</p><p><b>Pour l’examen fédéral</b> : ${memMd(m.examen)}</p><p class="st"><b>Sources</b> : ${m.references.map(memDoi).join(' · ')} · lu le 17.10.2026.</p></article>`}
function memEv(){const L=$('#m-evl');if(!L||L.dataset.ok)return;memLoad().then(D=>{if(L.dataset.ok)return;L.dataset.ok='1';L.innerHTML=D.methodes.map(memCard).join('')},()=>{L.innerHTML='<p class="st">Les fiches des méthodes n’ont pas pu se charger ; rechargez la page.</p>'})}
function memI(k){return `<button class="ti" type="button" data-t="m|${k}" aria-label="Preuves et mode d’emploi de la méthode" aria-haspopup="dialog" aria-expanded="false" aria-controls="tip">i</button>`}
function memOpt(){const V=$('#v-memo');if(!V||V.dataset.mi)return;V.dataset.mi='1';[['m-rappel','rappel-libre'],['m-test','recuperation'],['m-inter','entrelacement'],['m-feyn','enseigner'],['m-retro','recuperation'],['m-reap','reapprentissage']].forEach(([i,k])=>{const c=$('#'+i),sp=c&&c.nextElementSibling;if(sp)sp.insertAdjacentHTML('beforeend',memI(k))});const lg=V.querySelector('legend');if(lg)lg.insertAdjacentHTML('beforeend',memI('pratique-espacee'))}
function memW(k,t){return `<span class="tw" tabindex="0" role="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="tip" data-t="m|${k}">${t}</span>`}
function memCons(m){const e=$('#m-cons');if(!e)return;const P=[['rappel','rappel-libre','le rappel libre du plan, de mémoire'],['test','recuperation','les 10 QCM du SSP'],['retro','recuperation','la lecture de chaque correction, même juste'],['reap','reapprentissage','un nouvel essai de chaque question ratée jusqu’à la réponse juste'],['feyn','enseigner','l’exposé du SSP en 3 minutes sans support']].filter(x=>m[x[0]]);
 e.innerHTML=(P.length?'Pour chaque SSP à réviser, vous enchaînez '+P.map(x=>memW(x[1],x[2])).join(', puis ')+'.':'Aucune stratégie active n’est cochée : la liste donne seulement les échéances.')+(m.inter?' Dans une même séance, vous alternez des SSP qui partagent un symptôme d’entrée ('+memW('entrelacement','entrelacement')+').':'')}
$('.tab[data-v=memo]').addEventListener('click',memEv);
addEventListener('load',()=>(window.requestIdleCallback||(f=>setTimeout(f,1500)))(()=>memLoad().then(()=>{if(!$('#v-memo').hidden)memEv()},()=>{}),{timeout:6000}),{once:true});
/* ---------- MNÉMÉ : mémorisation espacée ---------- */""")

open(p, 'w', encoding='utf-8').write(s)
print('0015 appliqué')
