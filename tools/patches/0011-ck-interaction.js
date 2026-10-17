/* ---------- HERMÈS · NC-0 : glossaire imbriqué (gloLink), pile de fenêtres, types CK (glo, syn, hyp, nc, loc), couches et vues des schémas ---------- */
/* Données attendues (Atlas, assets/ck/*.js) : window.CK_GLO, CK_SYN, CK_HYP, CK_NC, CK_LOC, CK_SRC, CK_DOSES (objet par identifiant ou tableau),
   window.CK_GLO_IDX = {f:[[forme pliée, id], …], a:[[abréviation exacte, id], …]} (facultatif : sinon l’index se construit depuis CK_GLO),
   window.CK_SVG[chemin du SVG] = texte SVG (assets/nc/ncXX.js), window.CK_NC_CRED[chemin] = crédit. Après tout chargement : document.dispatchEvent(new Event('ck:pret')). */
const CK_MAX=5,tipStk=[],ckCou={};let gloI=null,gloOn=false,gloT=0;const gloQ=new Set();
const NC_VUE={face:'Face',profil:'Profil',trois_quarts:'Trois quarts',plan:'Plan',tour:'Tour à 8 vues'},NC_COU=['trait','nerf','noyaux','foramens','territoires','lesions','legendes'],
 NC_COUL={trait:'Trait',nerf:'Nerf',noyaux:'Noyaux',foramens:'Foramens',territoires:'Territoires',lesions:'Sites lésionnels',legendes:'Légendes'},
 GLO_TY={signe:'signe',syndrome:'syndrome',terme:'terme',examen:'examen',abreviation:'abréviation',eponyme:'éponyme'},
 CK_MOY={pharmaco:'Pharmacologique',interventionnel:'Interventionnel',reeducation:'Rééducation',suivi:'Suivi'};
function ckFold(s){let o='';for(let i=0;i<s.length;i++){const c=s[i],f=c.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();o+=f.length===1?f:c}return o}
function ckData(n){const v=window['CK_'+n];if(!v)return null;if(Array.isArray(v)){const m={};v.forEach(x=>{m[x.id||x.module]=x});window['CK_'+n]=m;return m}return v}
function ckDate(d){const m=/^(\d{4})-(\d\d)-(\d\d)$/.exec(d||'');return m?m[3]+'.'+m[2]+'.'+m[1]:String(d||'')}
function ckRe(s){return s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')}
/* Index du glossaire : formes pliées (sans accents ni casse) et abréviations exactes ; la plus longue forme l’emporte. */
function gloIndex(){const G=ckData('GLO'),X=window.CK_GLO_IDX,sig=(X?'x'+((X.f||[]).length+(X.a||[]).length):'')+':'+(G?Object.keys(G).length:0);if(gloI&&gloI.sig===sig)return gloI.ok?gloI:null;
 let F=[],A=[];if(X&&(X.f||X.a)){F=(X.f||[]).map(x=>[ckFold(x[0]),x[1]]);A=X.a||[]}else if(G){for(const id in G){const e=G[id];for(const f of [e.label,...(e.alias||[]),...(e.flexions||[])].filter(Boolean))(e.type==='abreviation'||e.casse)?A.push([f,id]):F.push([ckFold(f),id])}}
 const mk=L=>L.length?new RegExp('(?<![\\p{L}\\p{N}])(?:'+[...L].sort((a,b)=>b[0].length-a[0].length).map(x=>ckRe(x[0])).join('|')+')(?![\\p{L}\\p{N}])','gu'):null;
 gloI={sig,ok:!!(F.length||A.length),rF:mk(F),rA:mk(A),mF:new Map(F),mA:new Map(A)};return gloI.ok?gloI:null}
function gloShort(id){const e=(ckData('GLO')||{})[id];if(!e||!e.def)return '';const d=String(e.def),i=d.search(/[.;](\s|$)/);return (i>0&&i<160?d.slice(0,i+1):d.slice(0,157)+(d.length>157?'…':''))}
const GLO_SKIP='h1,h2,h3,h4,h5,h6,a,code,pre,kbd,samp,button,input,select,textarea,option,summary,legend,script,style,svg,noscript,nav,.tw,[contenteditable],[data-noglo],.blk,#grid,.ck-ctl,.ck-fil',
 GLO_BLK='p,li,td,th,dd,dt,blockquote,figcaption,div,section,article,details,fieldset';
/* gloLink(racine, exclus, dansFenetre) : pose data-t="glo|id" sur la première occurrence de chaque terme par bloc ; ignore titres, liens, code,
   commandes, éléments déjà reliés et identifiants exclus (terme courant et ancêtres de la pile). Ne modifie aucune donnée (TIP, NOT, GES). */
function gloLink(root,excl,inTip){const I=gloIndex();if(!I||!root||!root.isConnected)return 0;excl=excl||new Set();const inT=TIPEL.contains(root),L=[],seen=new Map();let n=0;
 const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,{acceptNode:t=>{const p=t.parentElement;if(!p||t.data.length<2||!/\p{L}/u.test(t.data))return 2;if(p.closest(GLO_SKIP))return 2;if(!inT&&p.closest('#tip'))return 2;return 1}});
 while(w.nextNode())L.push(w.currentNode);
 for(const t of L){const p=t.parentElement,blk=p.closest(GLO_BLK)||root,B=root.contains(blk)?blk:root;let used=seen.get(B);
  if(!used){used=new Set([...B.querySelectorAll('[data-t^="glo|"]')].map(x=>x.dataset.t.slice(4)));seen.set(B,used)}
  const txt=t.data,fo=ckFold(txt),M=[];
  if(I.rF){I.rF.lastIndex=0;let m;while((m=I.rF.exec(fo)))M.push([m.index,m[0].length,I.mF.get(m[0])])}
  if(I.rA){I.rA.lastIndex=0;let m;while((m=I.rA.exec(txt)))M.push([m.index,m[0].length,I.mA.get(m[0])])}
  if(!M.length)continue;M.sort((a,b)=>a[0]-b[0]||b[1]-a[1]);
  const f=document.createDocumentFragment();let at=0,k=0;
  for(const [i,len,id] of M){if(i<at||!id||excl.has(id)||used.has(id))continue;used.add(id);
   f.append(txt.slice(at,i));const s=document.createElement('span');s.className='tw glo';s.dataset.t='glo|'+id;s.tabIndex=0;s.setAttribute('role','button');s.setAttribute('aria-haspopup','dialog');
   s.setAttribute('aria-expanded','false');s.setAttribute('aria-controls','tip');if(inTip||inT){const d=gloShort(id);if(d)s.title=d}s.textContent=txt.slice(i,i+len);f.append(s);at=i+len;k++}
  if(k){f.append(txt.slice(at));t.replaceWith(f);n+=k}}
 return n}
/* Pages : liaison à l’inactivité, par petits lots, sur les nœuds ajoutés au rendu ; jamais dans la fenêtre (liée à son ouverture). */
const ckIdle=window.requestIdleCallback?f=>requestIdleCallback(f,{timeout:700}):f=>setTimeout(()=>f({timeRemaining:()=>8}),60);
const gloMO=new MutationObserver(R=>{for(const r of R)for(const n of r.addedNodes){const e=n.nodeType===1?n:n.parentElement;if(e&&!(e.classList&&e.classList.contains('glo'))&&!TIPEL.contains(e))gloQ.add(e)}gloSched()});
function gloSched(){if(gloT||!gloQ.size)return;gloT=1;ckIdle(gloRun)}
function gloRun(dl){gloT=0;const R=[...gloQ].filter(e=>e.isConnected&&![...gloQ].some(o=>o!==e&&o.isConnected&&o.contains(e)));gloQ.clear();gloMO.disconnect();
 try{while(R.length){const e=R.shift();if(e.children.length>40&&dl&&dl.timeRemaining()<4){for(const c of e.children)gloQ.add(c);continue}gloLink(e);if(dl&&dl.timeRemaining()<2){R.forEach(x=>gloQ.add(x));break}}}
 finally{gloMO.observe(document.querySelector('.w')||document.body,{childList:true,subtree:true})}gloSched()}
function gloStart(){gloI=null;if(!gloIndex())return;gloOn=true;const W=document.querySelector('.w')||document.body;for(const c of W.children)gloQ.add(c);gloMO.observe(W,{childList:true,subtree:true});gloSched()}
document.addEventListener('ck:pret',gloStart);
/* Rendus des types CK. ckL : lien explicite vers une autre fenêtre (retiré s’il est déjà dans la pile ou au niveau 5). */
function ckL(k,t,ti){return `<span class="tw ck-l" data-t="${esc(k)}" tabindex="0" role="button" aria-haspopup="dialog"${ti?` title="${esc(ti)}"`:''}>${esc(t)}</span>`}
function ckLab(n,id){const e=(ckData(n)||{})[id];return e?(e.label||e.nom||id):id}
function ckLnk(n,ty,id){return (ckData(n)||{})[id]?ckL(ty+'|'+id,ckLab(n,id),ty==='glo'?gloShort(id):''):esc(id)}
function modLab(m){const g=typeof GES!=='undefined'&&GES.find(x=>x.id===m);return g?g.r:m}
function ckSrc(L){const S=ckData('SRC')||{};return (L||[]).map(s=>{if(typeof s==='string')s={id:s};const r=S[s.id]||{},t=r.titre||r.label||s.id;
 return (r.url?`<a href="${esc(r.url)}" target="_blank" rel="noopener">${esc(t)}</a>`:esc(t))+(s.loc?', '+esc(s.loc):'')+(s.lu_le?', lu le '+esc(ckDate(s.lu_le)):'')}).join(' · ')}
function ckFoot(e){const av=e.statut==='À vérifier'||!(e.src||[]).length;return `<p class="ck-src">${av?'<span class="vb pend">À vérifier</span> ':''}${(e.src||[]).length?'Sources : '+ckSrc(e.src):'Source à lire.'}</p>`}
function ckList(t,L,f){return L&&L.length?`<p><b>${t}</b> :</p><ul>${L.map(x=>'<li>'+f(x)+'</li>').join('')}</ul>`:''}
function ckDose(id){if(!id)return '';const d=(ckData('DOSES')||{})[id];if(d&&d.dose&&d.lu_le)return ` Dose suisse (AIPS) : ${esc(d.dose)}${d.voie?', '+esc(d.voie):''}${d.population?', '+esc(d.population):''} <small>(${d.url?`<a href="${esc(d.url)}" target="_blank" rel="noopener">AIPS</a>`:'AIPS'}, lu le ${esc(ckDate(d.lu_le))})</small>`;
 return ' <span class="vb pend">Dose suisse (AIPS) : À vérifier</span>'}
function ckTip(ty,a,b){
 if(ty==='glo'){const e=(ckData('GLO')||{})[a];if(!e)return null;const ln=c=>ckLnk('GLO','glo',c);
  return {hd:'Glossaire · '+(GLO_TY[e.type]||e.type||'terme'),ti:e.label,h:`<p>${esc(e.def||'')}</p>`+(e.composantes&&e.composantes.length?`<p><b>Composantes</b> : ${e.composantes.map(ln).join(', ')}.</p>`:'')
   +(e.recherche?`<p><b>Recherche</b> : ${esc(e.recherche)}</p>`:'')+(e.orientation?`<p><b>Orientation</b> : ${esc(e.orientation)}</p>`:'')+(e.voir&&e.voir.length?`<p><b>Voir aussi</b> : ${e.voir.map(ln).join(', ')}.</p>`:'')+ckFoot(e)}}
 if(ty==='syn'){const e=(ckData('SYN')||{})[a];if(!e)return null;
  return {hd:'Syndrome'+(e.module?' · '+modLab(e.module):''),ti:e.label,h:(e.def?`<p>${esc(e.def)}</p>`:'')+(e.signes&&e.signes.length?`<p><b>Signes à rechercher</b> : ${e.signes.map(c=>ckLnk('GLO','glo',c)).join(', ')}.</p>`:'')
   +ckList('À demander',e.a_demander,esc)+(e.orientation&&e.orientation.length?`<p><b>Orientation diagnostique</b> : ${e.orientation.map(h=>ckLnk('HYP','hyp',h)).join(', ')}.</p>`:'')+ckFoot(e)}}
 if(ty==='hyp'){const e=(ckData('HYP')||{})[a];if(!e)return null;
  if(b==='pec'){const p=e.pec||{};return {hd:'Prise en charge',ti:e.label,h:(p.objectif?`<p><b>1. Objectif</b> : ${esc(p.objectif)}</p>`:'')+ckList('2. Mesures générales',p.mesures_generales,esc)
   +ckList('3. Moyens spécifiques',p.moyens_specifiques,m=>(m.type?`<i>${esc(CK_MOY[m.type]||m.type)}</i> : `:'')+esc(m.texte||'')+ckDose(m.dose_ref)+((m.src||[]).length?` <small>[${ckSrc(m.src)}]</small>`:''))
   +(p.objectif||(p.mesures_generales||[]).length||(p.moyens_specifiques||[]).length?'':'<p><span class="vb pend">À vérifier</span> Prise en charge à rédiger.</p>')+ckFoot(e)}}
  const x=e.exam||{},R=x.reference,Li=(x.lignes||[]).slice().sort((p,q)=>p.rang-q.rang),rg=r=>r===1?'1re intention':r+'e intention',
   part=(l,v)=>v?` <i>${l}</i> : ${esc(v)}.`:'';
  return {hd:'Exploration',ti:e.label,h:(e.bloquant?'<p><span class="ck-urg">Urgence</span></p>':'')
   +(R?`<p><b>Examen de référence</b> : ${esc(R.nom)}.${part('Recherche',R.recherche)}${(R.src||[]).length?` <small>[${ckSrc(R.src)}]</small>`:''}</p>`:'')
   +Li.map(l=>`<p><b>${rg(l.rang)}</b> : ${esc(l.nom)}.${part('Pourquoi',l.pourquoi)}${part('Précautions',l.precautions)}${part('Recherche',l.recherche)}${part('Alternative',l.alternative)}${(l.src||[]).length?` <small>[${ckSrc(l.src)}]</small>`:''}</p>`).join('')
   +(R||Li.length?'':'<p><span class="vb pend">À vérifier</span> Aucun examen renseigné.</p>')+(e.confirmation?`<p><b>Confirmation</b> : ${esc(e.confirmation)}</p>`:'')
   +((e.syn||[]).length?`<p><b>Syndrome</b> : ${e.syn.map(s=>ckLnk('SYN','syn',s)).join(', ')}.</p>`:'')+(e.pec?`<p>${ckL('hyp|'+a+'|pec','Prise en charge après confirmation →')}</p>`:'')+ckFoot(e)}}
 if(ty==='loc'){const e=(ckData('LOC')||{})[a];if(!e)return null;const t=b==='B'?'B':'A',L=e[t]||[],T={A:'A. Syndromes',B:'B. Diagnostics · Exploration · Prise en charge'};
  return {hd:'Synthèse locale · '+modLab(a),ti:T[t],h:`<div class="ck-tabs ck-ctl" role="tablist" aria-label="Synthèse locale">${['A','B'].map(k=>`<button type="button" class="b" role="tab" id="ck-tab-${k}" aria-selected="${k===t}" aria-controls="ck-pan" tabindex="${k===t?0:-1}" data-ck="tab" data-k="loc|${esc(a)}|${k}">${T[k]}</button>`).join('')}</div>`
   +`<div id="ck-pan" role="tabpanel" aria-labelledby="ck-tab-${t}">${L.length?'<ul class="ck-list">'+L.map(id=>'<li>'+(t==='A'?ckLnk('SYN','syn',id):ckLnk('HYP','hyp',id))+'</li>').join('')+'</ul>':'<p><span class="vb pend">À vérifier</span> Aucune entrée pour ce module.</p>'}</div>`}}
 if(ty==='nc'){const e=(ckData('NC')||{})[a];if(!e)return null;const V=e.vues||{},K=Object.keys(NC_VUE).filter(v=>v!=='tour'&&V[v]),v=b==='tour'&&e.tour?'tour':V[b]?b:K[0];if(!v)return null;
  const bt=[...K,...(e.tour?['tour']:[])].map(x=>`<button type="button" class="b" data-ck="vue" data-k="nc|${esc(a)}|${x}" aria-pressed="${x===v}">${NC_VUE[x]}</button>`).join('');
  return {hd:'Schéma · '+(e.nom||a),ti:(e.nom||a)+' · '+NC_VUE[v],h:`<div class="ck-ctl ck-vues" role="group" aria-label="Vue du schéma">${bt}</div>`
   +`<fieldset class="ck-ctl ck-couches"${v==='tour'?' disabled':''}><legend>Couches</legend>${NC_COU.map(c=>`<label><input type="checkbox" data-ck="cou" value="${c}"${ckCou[c]===false?'':' checked'}> ${NC_COUL[c]}</label>`).join('')}</fieldset>`
   +`<figure class="ck-fig" data-nc="${esc(a)}" data-vue="${v}"></figure>`}}
 return undefined}
/* Schémas : SVG en ligne (couches actives) depuis CK_SVG, chargé au besoin par assets/nc/ncXX.js ; sinon image simple. */
const ckJs={};
function ckSvg(fig,src){const d=new DOMParser().parseFromString(src,'image/svg+xml'),s=d.documentElement;if(!s||s.nodeName!=='svg')return null;
 s.querySelectorAll('script,foreignObject').forEach(x=>x.remove());for(const el of [s,...s.querySelectorAll('*')])for(const at of [...el.attributes]){if(/^on/i.test(at.name)||(/href$/i.test(at.name)&&/^\s*javascript:/i.test(at.value)))el.removeAttribute(at.name)}
 const n=document.importNode(s,true);n.setAttribute('role','img');n.removeAttribute('width');n.removeAttribute('height');return n}
function ckApply(fig){const s=fig.querySelector('svg'),F=TIPEL.querySelector('.ck-couches');if(!F)return;
 for(const i of F.querySelectorAll('input[data-ck=cou]')){const g=s&&s.querySelector(`#${i.value},[data-couche="${i.value}"]`);i.disabled=!g;if(g)g.style.display=i.checked?'':'none'}}
function ckFig(fig){const id=fig.dataset.nc,v=fig.dataset.vue,e=(ckData('NC')||{})[id];if(!e)return;const nom=e.nom||id,F=TIPEL.querySelector('.ck-couches');
 if(v==='tour'){fig.innerHTML=`<div class="ck-tour" role="slider" tabindex="0" aria-label="Tour du schéma ${esc(nom)} : glissez ou utilisez les flèches" aria-valuemin="0" aria-valuemax="7" aria-valuenow="0" aria-valuetext="0°" style="background-image:url('${esc(e.tour)}')"></div><figcaption class="st">Glissez, ou utilisez les flèches gauche et droite : 8 vues à 45°.</figcaption>`;return}
 const p=e.vues[v],cr=(window.CK_NC_CRED||{})[p]||(e.credits||{})[v],crT=cr?(typeof cr==='string'?cr:(cr.tasl||cr.credit||'')):'',cap=crT?`<figcaption class="ck-cr">${esc(crT)}</figcaption>`:'';
 const src=window.CK_SVG&&CK_SVG[p];
 if(src){const n=ckSvg(fig,src);if(n){n.setAttribute('aria-label','Schéma : '+nom+', vue '+NC_VUE[v]);fig.replaceChildren(n);fig.insertAdjacentHTML('beforeend',cap);ckApply(fig);return}}
 const js=e.js||'assets/nc/'+id+'.js';
 if(!(js in ckJs)){ckJs[js]=0;fig.innerHTML='<p class="st">Chargement du schéma…</p>';const sc=document.createElement('script');sc.src=js;
  sc.onload=()=>{ckJs[js]=1;if(fig.isConnected)ckFig(fig)};sc.onerror=()=>{ckJs[js]=-1;if(fig.isConnected)ckFig(fig)};document.head.appendChild(sc);return}
 if(ckJs[js]===0)return;
 fig.innerHTML=`<img src="${esc(p)}" alt="Schéma : ${esc(nom)}, vue ${NC_VUE[v]}" loading="lazy">${cap}<p class="st">Les couches ne sont pas disponibles pour ce schéma : le fichier ${esc(js)} manque.</p>`;if(F)F.disabled=true}
function ckTour(el,d){const f=((+el.getAttribute('aria-valuenow')+d)%8+8)%8;el.setAttribute('aria-valuenow',f);el.setAttribute('aria-valuetext',f*45+'°');el.style.backgroundPositionX=(f*100/7)+'%'}
/* Pile de fenêtres : un terme ouvert depuis la fenêtre l’empile (5 niveaux au plus) ; « ← Retour » et le fil d’Ariane y reviennent. */
function tipGo(i){if(i<0||i>=tipStk.length)return;const s=tipStk[i];tipStk.length=i;showTip({dataset:{t:s.k}},true,tipOp,true,true)}
function tipNav(e){const t=e.target;if(!(t instanceof Element)||!TIPEL.contains(t))return false;
 if(t.closest('input,a[href]'))return true;
 const bk=t.closest('.bk');if(bk){e.preventDefault();e.stopPropagation();tipGo(tipStk.length-1);return true}
 const lv=t.closest('[data-lv]');if(lv){e.preventDefault();e.stopPropagation();tipGo(+lv.dataset.lv);return true}
 const c=t.closest('[data-ck]');if(c&&c.dataset.k){e.preventDefault();e.stopPropagation();const k=c.dataset.k;showTip({dataset:{t:k}},true,tipOp,false,true);const n=TIPEL.querySelector(`[data-k="${CSS.escape(k)}"]`);if(n)n.focus({preventScroll:true});return true}
 const a=t.closest('.ck-b [data-t]');if(a){e.preventDefault();e.stopPropagation();clearTimeout(tipT);showTip(a,true,a,e.detail===0);return true}
 return false}
TIPEL.addEventListener('change',e=>{const i=e.target.closest('input[data-ck=cou]');if(!i)return;ckCou[i.value]=i.checked;const f=TIPEL.querySelector('.ck-fig');if(f)ckApply(f)});
TIPEL.addEventListener('keydown',e=>{const t=e.target;if(t.matches('[role=tab]')&&(e.key==='ArrowLeft'||e.key==='ArrowRight')){const L=[...TIPEL.querySelectorAll('[role=tab]')],n=L[(L.indexOf(t)+(e.key==='ArrowRight'?1:L.length-1))%L.length];e.preventDefault();n.click()}
 else if(t.classList.contains('ck-tour')&&(e.key==='ArrowLeft'||e.key==='ArrowRight')){e.preventDefault();ckTour(t,e.key==='ArrowRight'?1:-1)}});
TIPEL.addEventListener('pointerdown',e=>{const el=e.target.closest('.ck-tour');if(!el)return;el.setPointerCapture(e.pointerId);let x0=e.clientX;
 const mv=ev=>{const d=Math.trunc((ev.clientX-x0)/40);if(d){ckTour(el,d);x0+=d*40}},up=()=>{el.removeEventListener('pointermove',mv);el.removeEventListener('pointerup',up);el.removeEventListener('pointercancel',up)};
 el.addEventListener('pointermove',mv);el.addEventListener('pointerup',up);el.addEventListener('pointercancel',up)});
function tipCk(lv,k){TIPEL.classList.toggle('ck',/^(glo|syn|hyp|nc|loc)\|/.test(k));const B=TIPEL.querySelector('.ck-b');if(!B)return;const ex=tipStk.map(s=>s.k).concat(k);
 B.querySelectorAll('.ck-l[data-t]').forEach(a=>{if(lv>=CK_MAX||ex.includes(a.dataset.t))a.replaceWith(document.createTextNode(a.textContent))});
 if(lv<CK_MAX)gloLink(B,new Set(ex.filter(s=>s.startsWith('glo|')).map(s=>s.split('|')[1])),true);
 B.querySelectorAll('.ck-fig').forEach(ckFig)}
if(window.CK_GLO||window.CK_GLO_IDX)gloStart();
