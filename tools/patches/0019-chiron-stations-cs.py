import os, sys
# Patch 0019 · Chiron · 17.10.2026 · Fenêtre « Station CS » sur la fiche SSP (onglet Notions CK).
# Les stations vivent dans data/cs/ (schéma data/cs/schema/) et sont compilées par tools/cs_build.py en
# assets/st/index.js (window.CS_ST_INDEX) et assets/st/<id>.js (window.CS_ST_<ID>), chargés à la demande
# par stLoad (compatible file://, comme ckLoad et memLoad). Aucune donnée CS n'entre dans app_v2.html.
# Le panneau s'insère après le premier p.st de la fiche (renderNotSoft lit ce p.st) et n'emploie ni .st,
# ni .pbar, ni [data-tot], [data-open] ou [data-x]. Les gestes (g|…) et les chaînes (hyp|…) s'ouvrent en
# infobulle ; gloLink relie les termes du glossaire à l'affichage. Se rejoue après 0018 et les patches de main.
p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
assert not p.endswith('/app.html') or p.endswith('app_v2.html'), 'Interdit : app.html'
s = open(p, encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, 'Ancrage absent ou répété : ' + a[:60]
    s = s.replace(a, b)

# Style : texte justifié, titres en gras, aucun rouge ; la feuille va dans <head> (validateur Nu).
rep('</head>',
    '<style id="chiron-css">'
    '.st-cs{margin:8px 0 10px}.st-btns{gap:6px;flex-wrap:wrap}.st-btns .b[aria-expanded="true"]{background:var(--soft)}'
    '.st-pan{border:1px solid var(--line);border-radius:12px;padding:6px 12px 10px;margin-top:8px;background:var(--paper);min-width:0;overflow-wrap:anywhere}'
    '.st-pan p,.st-pan li{text-align:justify;hyphens:auto;line-height:1.45}.st-pan ul,.st-pan ol{padding-left:20px;margin:6px 0}.st-pan li{margin:5px 0}'
    '.st-pan details{border-top:1px solid var(--line);padding:4px 0}.st-pan summary{font-weight:700;cursor:pointer;padding:4px 0}'
    '.st-pan h4{margin:8px 0 4px;font-size:.95rem;font-weight:700}.st-pan .st-q{display:block;text-align:left}.st-pan .st-isrc{font-size:.84rem;color:var(--mut);margin:2px 0 0}.st-pan .st-pts{font-weight:700;white-space:nowrap}'
    '.st-pan .vb{display:inline-block;margin:0 4px;padding:0 7px;border-radius:99px;font-size:.8rem;font-weight:700;background:color-mix(in srgb,var(--ok) 16%,transparent);color:var(--ok)}'
    '.st-pan .vb.pend{background:var(--soft);color:var(--mut)}.st-pan .ck-src,.st-pan .st-av{font-size:.88rem;color:var(--mut)}.st-pan a{color:var(--deep)}'
    '</style></head>')

# Montage : après le rendu de la fiche SSP.
rep('+nBlock(NSEL,false);renderNotStats()}', '+nBlock(NSEL,false);stMount($(\'#n-main\'),NSEL);renderNotStats()}')

rep('function renderNot(){if(!NSEL)', r"""/* ---------- Chiron : stations CS (assets/st/, chargées à la demande) ---------- */
const STP={};let ST_OPEN=null;
function stLoad(n){const v=n==='index'?'CS_ST_INDEX':'CS_ST_'+n.toUpperCase().replace(/[^A-Z0-9]/g,'_');if(window[v])return Promise.resolve(window[v]);return STP[n]||(STP[n]=new Promise((ok,ko)=>{const e=document.createElement('script');e.src='assets/st/'+n+'.js';e.async=true;const no=()=>{delete STP[n];e.remove();ko(new Error('stLoad '+n))};e.onload=()=>window[v]?ok(window[v]):no();e.onerror=no;document.head.appendChild(e)}))}
function stMount(box,c){if(!box)return;stLoad('index').then(X=>{const L=(X.ssp||{})[c];if(!L||!L.length||!box.isConnected||NSEL!==c||box.querySelector('.st-cs'))return;const p=box.querySelector('p.st');if(!p)return;
 const d=document.createElement('div');d.className='st-cs';d.innerHTML=`<div class="row st-btns">${L.map(x=>`<button class="b" type="button" data-st="${esc(x[0])}" aria-expanded="false" title="${esc(x[1])}">Station CS · ${esc(x[1])}</button>`).join('')}</div><div class="st-pan" hidden aria-live="polite"></div>`;p.after(d);
 d.addEventListener('click',e=>{const b=e.target.closest('[data-st]');if(b)stOpen(d,b.dataset.st,true)});if(ST_OPEN&&L.some(x=>x[0]===ST_OPEN))stOpen(d,ST_OPEN,false)}).catch(()=>{})}
function stOpen(d,id,tog){const P=d.querySelector('.st-pan');if(tog&&ST_OPEN===id&&!P.hidden){ST_OPEN=null;P.hidden=true;d.querySelectorAll('[data-st]').forEach(b=>b.setAttribute('aria-expanded','false'));return}
 ST_OPEN=id;d.querySelectorAll('[data-st]').forEach(b=>b.setAttribute('aria-expanded',b.dataset.st===id?'true':'false'));P.hidden=false;P.innerHTML='<p>La station se charge.</p>';
 Promise.all([stLoad('index'),stLoad(id),ckLoad('src').catch(()=>null),ckLoad('hyp').catch(()=>null)]).then(([X,S])=>{if(ST_OPEN===id)P.innerHTML=stHtml(S,X.format)},()=>{P.innerHTML='<p>La station n’a pas pu se charger ; rechargez la page.</p>'})}
function stAv(o){return o&&o.statut==='À vérifier'?' <span class="vb pend">À vérifier</span>':''}
function stSrc(L){return ckArr(L).length?`<p class="ck-src">Sources : ${ckSrc(L)}</p>`:''}
function stSrcC(L){const D=ckData('SRC')||{};L=ckArr(L);return L.length?`<p class="st-isrc">Source : ${L.map(s=>{const r=D[s.id]||{},t=esc(r.titre||s.id);return (r.url?`<a href="${esc(r.url)}" target="_blank" rel="noopener">${t}</a>`:t)+(s.loc?', '+esc(s.loc):'')+(s.lu_le?', lu le '+esc(ckDate(s.lu_le)):'')}).join(' · ')}</p>`:''}
function stUl(L,f,tag){L=ckArr(L);return L.length?`<${tag||'ul'}>${L.map(x=>'<li>'+f(x)+'</li>').join('')}</${tag||'ul'}>`:''}
const ST_PART=[['anamnese','Anamnèse'],['examen','Examen clinique'],['presentation','Présentation du cas'],['management','Management et explication']];
function stHtml(S,F){F=F||{};const fm=(F.formats||[]).find(f=>f.id===S.format)||{},C=S.consigne||{},R=S.ps||{},G=S.grille||{},K=F.kk||{},A=F.asm||{};
 const tot=ST_PART.reduce((n,[k])=>n+ckArr(G[k]).reduce((m,i)=>m+(i.pts||0),0),0);
 let h=`<p><b>${esc(fm.label||S.format)}</b> · ${esc(String(S.duree_min))} minutes${S.valide_par_vial?'':' · <span class="vb pend">Non encore relue par Vial</span>'}</p>`;
 h+=`<details open><summary>Consigne affichée sur la porte</summary><p><i>${esc(C.lieu||'')}</i></p><p>${ckP(C.porte)}</p>${stUl(C.taches,ckP)}${stUl(C.parties,x=>`<b>${esc(x.titre)}</b> : ${esc(String(x.duree_min))} minutes.`)}</details>`;
 h+=`<details><summary>Rôle du patient standardisé</summary><p><b>Rôle</b> : ${ckP(R.role)}</p><p><b>Identité</b> : ${ckP(R.identite)}</p>${R.apparence?`<p><b>Apparence</b> : ${ckP(R.apparence)}</p>`:''}`
  +`<p><b>Première phrase</b> : <i>${esc(R.ouverture||'')}</i></p><p><b>Récit spontané</b> : ${ckP(R.recit)}</p>`
  +`<h4>Réponses aux questions</h4>${stUl(R.reponses,x=>`<b class="st-q">${esc(x.q)}${x.si_demande?' <span class="vb pend">seulement si demandé</span>':''}</b>${ckP(x.r)}`)}`
  +`<p><b>Émotions</b> : ${ckP(R.emotions)}</p>${ckArr(R.questions).length?`<h4>Questions du patient</h4>${stUl(R.questions,esc)}`:''}${R.jeu?`<p><b>Jeu et signes simulés</b> : ${ckP(R.jeu)}</p>`:''}</details>`;
 if(ckArr(S.resultats).length)h+=`<details><summary>Résultats remis par l’examinateur</summary>${stUl(S.resultats,x=>`<b>${esc(x.moment)}</b> : ${ckP(x.texte)}`)}</details>`;
 h+=`<details><summary>Grille ASM (${esc(String(A.poids||75))} % de la note) · ${tot} points indicatifs</summary>${A.t?`<p>${ckP(A.t)}</p>`:''}`;
 ST_PART.forEach(([k,l])=>{const L=ckArr(G[k]);if(!L.length)return;h+=`<h4>${l} (${L.reduce((m,i)=>m+(i.pts||0),0)} points)</h4>`+stUl(L,i=>`<span class="st-pts">${i.pts} pt</span> ${ckP(i.t)}${stAv(i)}<br><i>Pourquoi</i> : ${ckP(i.pourquoi)}`+ckGes(i.ges)+ckLinks('Chaîne CK','HYP','hyp',i.hyp)+stSrcC(i.src),'ol')});
 h+=`</details><details><summary>Communication KK (${esc(String(K.poids||25))} % de la note, échelle ${esc(K.echelle||'1 à 5')})</summary>${K.t?`<p>${ckP(K.t)}</p>`:''}`
  +stUl(K.dimensions,dm=>`<b>${esc(dm.label)}</b> : ${ckArr(S.kk).filter(x=>x.dim===dm.id).map(x=>ckP(x.attendu)).join(' ')||'Aucun point propre à cette station.'}`)+stSrc(K.src)+`</details>`;
 if(ckArr(S.pieges).length)h+=`<details><summary>Pièges fréquents</summary>${stUl(S.pieges,ckP)}</details>`;
 if(ckArr(S.a_verifier).length)h+=`<details><summary>Points à vérifier (${S.a_verifier.length})</summary>${stUl(S.a_verifier,x=>'<span class="vb pend">À vérifier</span> '+ckP(x))}</details>`;
 h+=`<details><summary>Sources et format officiel</summary>${stSrc(S.src)}${fm.t?`<p><b>Format de la station</b> : ${ckP(fm.t)}</p>`+stSrc(fm.src):''}${F.avertissement?`<p class="st-av">${ckP(F.avertissement)}</p>`:''}${F.note_session?`<p class="st-av"><span class="vb pend">À vérifier</span> ${ckP(F.note_session)}</p>`:''}</details>`;
 return h}
function renderNot(){if(!NSEL)""")

open(p, 'w', encoding='utf-8').write(s)
print('0019 appliqué :', p)
