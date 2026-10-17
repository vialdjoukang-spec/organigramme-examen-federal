/* ---------- HERMÈS · NC-0 : glossaire imbriqué (gloLink), pile de fenêtres, types CK (glo, syn, hyp, nc, loc), couches, vues et états des schémas ---------- */
/* Données (Atlas, assets/ck/*.js, chargées par ckLoad et ckGlo du patch 0011) : CK_GLO_INDEX.e = [[id, type, libellé, formes, tranche], …] ;
   définitions par tranche (CK_GLO_A…) ; CK_SYN, CK_HYP, CK_NC, CK_LOC, CK_SRC, CK_DOSES_CH (objet par identifiant ou tableau).
   Schémas : CK_SVG[chemin du SVG] = texte SVG (assets/nc/ncXX.js, tools/nc_svg_js.py), états dans data-etats (Dédale). Aucune donnée ici. */
const CK_MAX=5,tipStk=[],ckCou={};let gloI=null,gloOn=false,gloT=0,ckEt='';const gloQ=new Set(),ckTry=new Map();
const NC_VUE={face:'Face',profil:'Profil',trois_quarts:'Trois quarts','34':'Trois quarts',plan:'Plan',tour:'Tour à 8 vues'},NC_COU=['trait','nerf','noyaux','foramens','territoires','lesions','legendes'],
 NC_COUL={trait:'Trait',nerf:'Nerf',noyaux:'Noyaux',foramens:'Foramens',territoires:'Territoires',lesions:'Sites lésionnels',legendes:'Légendes'},
 NC_ETL={trajet:'Trajet',branches:'Branches',fonctions:'Fonctions',lesions:'Lésions'},
 GLO_TY={signe:'signe',syndrome:'syndrome',terme:'terme',examen:'examen',abreviation:'abréviation',eponyme:'éponyme'},
 CK_MOY={pharmaco:'Pharmacologique',interventionnel:'Interventionnel',reeducation:'Rééducation',suivi:'Suivi'},
 CK_DEP={glo:['glo-index','src'],syn:['syn','hyp','src','glo-index'],hyp:['hyp','syn','src','doses_ch','glo-index'],loc:['loc','syn','hyp'],nc:['nc','syn','hyp','src','glo-index']};
function ckW(n){return window['CK_'+n]}
function ckFold(s){let o='';for(let i=0;i<s.length;i++){const c=s[i],f=c.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();o+=f.length===1?f:c}return o}
function ckData(n){const v=ckW(n);if(!v)return null;if(Array.isArray(v)){const m={};v.forEach(x=>{m[x.id||x.module]=x});window['CK_'+n]=m;return m}return v}
function ckDate(d){const m=/^(\d{4})-(\d\d)-(\d\d)$/.exec(d||'');return m?m[3]+'.'+m[2]+'.'+m[1]:String(d||'')}
function ckRe(s){return s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')}
/* Phrase : échappée, avec un point final seulement s’il manque (aucun « .. »). */
function ckP(s){s=String(s||'').trim();return esc(s)+(/[.!?…:;]$/.test(s)?'':'.')}
/* Index du glossaire : formes pliées (sans accents ni casse) et sigles exacts (AVC) ; la plus longue forme l’emporte. */
function gloIndex(){const G=ckData('GLO'),X=ckW('GLO_INDEX'),E=X&&X.e||[],sig=E.length+':'+(G?Object.keys(G).length:0);if(gloI&&gloI.sig===sig)return gloI.ok?gloI:null;
 const F=[],A=[],M=new Map(),cs=(f,ty)=>ty==='abreviation'||/^[\p{Lu}\d]{2,6}$/u.test(f),add=(id,ty,fs)=>{for(const f of fs.filter(Boolean))cs(f,ty)?A.push([f,id]):F.push([ckFold(f),id])};
 for(const x of E){M.set(x[0],{ty:x[1],lab:x[2],sl:x[4]});add(x[0],x[1],[x[2],...(x[3]||[])])}
 if(G)for(const id in G){if(M.has(id))continue;const e=G[id];M.set(id,{ty:e.type,lab:e.label});add(id,e.type,[e.label,...(e.alias||[]),...(e.flexions||[])])}
 const mk=L=>L.length?new RegExp('(?<![\\p{L}\\p{N}])(?:'+[...L].sort((a,b)=>b[0].length-a[0].length).map(x=>ckRe(x[0])).join('|')+')(?![\\p{L}\\p{N}])','gu'):null;
 gloI={sig,ok:!!(F.length||A.length),rF:mk(F),rA:mk(A),mF:new Map(F),mA:new Map(A),M};return gloI.ok?gloI:null}
function gloSl(id){const I=gloIndex(),m=I&&I.M.get(id);return (m&&m.sl)||(/^[a-z]/.test(id)?id[0]:'0')}
function gloE(id){const G=ckData('GLO');if(G&&G[id])return G[id];const T=ckW('GLO_'+gloSl(id).toUpperCase().replace(/[^A-Z0-9]/g,'_'));return T&&T[id]||null}
function gloMeta(id){const I=gloIndex(),m=I&&I.M.get(id),e=gloE(id);return m||e?{lab:(e&&e.label)||m.lab,ty:(e&&e.type)||m.ty}:null}
function gloShort(id){const e=gloE(id);if(!e||!e.def)return '';const d=String(e.def),i=d.search(/[.;](\s|$)/);return (i>0&&i<160?d.slice(0,i+1):d.slice(0,157)+(d.length>157?'…':''))}
/* Chargement à la demande : la fenêtre s’affiche (« Chargement… »), puis se redessine sur place quand les fichiers sont là. */
function ckNeed(ty,a,key){if(typeof ckLoad!=='function'||ckTry.get(key)===2)return true;if(ckTry.get(key)===1)return false;const L=(CK_DEP[ty]||[]).filter(n=>!ckW(n.toUpperCase().replace(/[^A-Z0-9]/g,'_'))),g=ty==='glo'&&!gloE(a);
 if(!L.length&&!g)return true;ckTry.set(key,1);Promise.allSettled([...L.map(n=>ckLoad(n)),...(g?[ckGlo(a)]:[])]).then(()=>{ckTry.set(key,2);gloI=null;if(!gloOn&&gloIndex())gloStart();if(!TIPEL.hidden&&tipK===key)showTip({dataset:{t:key}},tipPin,tipOp||TIPEL,false,true)});return false}
const GLO_SKIP='h1,h2,h3,h4,h5,h6,a,code,pre,kbd,samp,button,input,select,textarea,option,summary,legend,script,style,svg,noscript,nav,.tw,[contenteditable],[data-noglo],.blk,#grid,.ck-ctl,.ck-fil',
 GLO_BLK='p,li,td,th,dd,dt,blockquote,figcaption,div,section,article,details,fieldset';
/* gloLink(racine, exclus, dansFenetre) : pose une clé de glossaire (type glo) sur la première occurrence de chaque terme par bloc ; ignore titres, liens, code,
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
function ncVue(v){return NC_VUE[v]||v}
function ckLab(n,id){if(n==='GLO'){const m=gloMeta(id);return m?m.lab:id}const e=(ckData(n)||{})[id];return e?(e.label||e.nom||id):id}
function ckLnk(n,ty,id){const ok=n==='GLO'?!!gloMeta(id):!!(ckData(n)||{})[id];return ok?ckL(ty+'|'+id,ckLab(n,id),ty==='glo'?gloShort(id):''):esc(id)}
function ckArr(x){return x==null?[]:Array.isArray(x)?x:[x]}
function modLab(m){const g=typeof GES!=='undefined'&&GES.find(x=>x.id===m);return g?g.r:m}
function ckSrc(L){const S=ckData('SRC')||{};return ckArr(L).map(s=>{if(typeof s==='string')s={id:s};const r=S[s.id]||{},t=r.titre||r.label||s.id;
 return (r.url?`<a href="${esc(r.url)}" target="_blank" rel="noopener">${esc(t)}</a>`:esc(t))+(r.org?' ('+esc(r.org)+')':'')+(s.loc?', '+esc(s.loc):'')+(s.lu_le?', lu le '+esc(ckDate(s.lu_le)):'')}).join(' · ')}
function ckFoot(e){const av=e.statut==='À vérifier'||!ckArr(e.src).length;return `<p class="ck-src">${av?'<span class="vb pend">À vérifier</span> ':''}${ckArr(e.src).length?'Sources : '+ckSrc(e.src):'Source à lire.'}</p>`}
function ckList(t,L,f){L=ckArr(L);return L.length?`<p><b>${t}</b> :</p><ul>${L.map(x=>'<li>'+f(x)+'</li>').join('')}</ul>`:''}
function ckLinks(t,n,ty,L){L=ckArr(L);return L.length?`<p><b>${t}</b> : ${L.map(i=>ckLnk(n,ty,i)).join(', ')}.</p>`:''}
function ckDose(id){if(!id)return '';const d=(ckData('DOSES_CH')||ckData('DOSES')||{})[id];if(d&&d.dose&&d.lu_le)return ` Dose suisse (AIPS) : ${esc(d.dose)}${d.voie?', '+esc(d.voie):''}${d.population?', '+esc(d.population):''} <small>(${d.url?`<a href="${esc(d.url)}" target="_blank" rel="noopener">AIPS</a>`:'AIPS'}, lu le ${esc(ckDate(d.lu_le))})</small>`;
 return ' <span class="vb pend">Dose suisse (AIPS) : À vérifier</span>'}
function ckWait(hd,ti){return {hd,ti:ti||'…',h:'<p class="st">Chargement…</p>'}}
function ckTip(ty,a,b){
 if(!(ty in CK_DEP))return undefined;const key=ty+'|'+a+(b!=null?'|'+b:'');
 if(ty==='glo'){if(!ckNeed(ty,a,key)){const m=gloMeta(a);return ckWait('Glossaire'+(m?' · '+(GLO_TY[m.ty]||m.ty):''),m&&m.lab)}const e=gloE(a);if(!e)return null;
  return {hd:'Glossaire · '+(GLO_TY[e.type]||e.type||'terme'),ti:e.label,h:`<p>${ckP(e.def)}</p>`+ckLinks('Composantes','GLO','glo',e.composantes)
   +(e.recherche?`<p><b>Recherche</b> : ${ckP(e.recherche)}</p>`:'')+(e.orientation?`<p><b>Orientation</b> : ${ckP(e.orientation)}</p>`:'')+ckLinks('Voir aussi','GLO','glo',e.voir)+ckFoot(e)}}
 if(!ckNeed(ty,a,key))return ckWait({syn:'Syndrome',hyp:'Exploration',loc:'Synthèse locale',nc:'Schéma'}[ty]);
 if(ty==='syn'){const e=(ckData('SYN')||{})[a];if(!e)return null;
  return {hd:'Syndrome'+(e.module?' · '+modLab(e.module):''),ti:e.label,h:(e.comment||e.def?`<p>${ckP(e.comment||e.def)}</p>`:'')+ckLinks('Signes à rechercher','GLO','glo',e.signes)
   +ckList('À demander',e.a_demander,esc)+ckLinks('Hypothèses','HYP','hyp',e.hyp||e.orientation)+ckFoot(e)}}
 if(ty==='hyp'){const e=(ckData('HYP')||{})[a];if(!e)return null;
  if(b==='pec'){const p=e.pec||{};return {hd:'Prise en charge',ti:e.label,h:(p.objectif?`<p><b>1. Objectif</b> : ${ckP(p.objectif)}</p>`:'')+ckList('2. Mesures générales',p.mesures_generales,ckP)
   +ckList('3. Moyens spécifiques',p.moyens_specifiques,m=>(m.type?`<i>${esc(CK_MOY[m.type]||m.type)}</i> : `:'')+ckP(m.texte)+ckDose(m.dose_ref)+(m.statut==='À vérifier'?' <span class="vb pend">À vérifier</span>':'')+(ckArr(m.src).length?` <small>[${ckSrc(m.src)}]</small>`:''))
   +(p.objectif||ckArr(p.mesures_generales).length||ckArr(p.moyens_specifiques).length?'':'<p><span class="vb pend">À vérifier</span> Prise en charge à rédiger.</p>')+ckFoot(e)}}
  const x=e.exam||{},R=x.reference,Li=ckArr(x.lignes).slice().sort((p,q)=>p.rang-q.rang),rg=r=>r===1?'1re intention':r+'e intention',
   part=(l,v)=>v?` <i>${l}</i> : ${ckP(v)}`:'',sr=L=>ckArr(L).length?` <small>[${ckSrc(L)}]</small>`:'';
  return {hd:'Exploration',ti:e.label,h:(e.bloquant?'<p><span class="urg" data-bloquant>Urgence</span></p>':'')
   +(R?`<p><b>Examen de référence</b> : ${ckP(R.nom)}${part('Recherche',R.recherche)}${sr(R.src)}</p>`:'')
   +Li.map(l=>`<p><b>${rg(l.rang)}</b> : ${ckP(l.nom)}${part('Pourquoi',l.pourquoi)}${part('Précautions',l.precautions)}${part('Recherche',l.recherche)}${part('Alternative',l.alternative)}${sr(l.src)}</p>`).join('')
   +(R||Li.length?'':'<p><span class="vb pend">À vérifier</span> Aucun examen renseigné.</p>')+(e.confirmation?`<p><b>Confirmation</b> : ${ckP(e.confirmation)}</p>`:'')
   +ckLinks('Syndrome','SYN','syn',e.syn)+(e.pec?`<p>${ckL('hyp|'+a+'|pec','Prise en charge après confirmation →')}</p>`:'')+ckFoot(e)}}
 if(ty==='loc'){const e=(ckData('LOC')||{})[a];if(!e)return null;const t=b==='B'?'B':'A',L=ckArr(e[t]),T={A:'A. Syndromes',B:'B. Diagnostics · Exploration · Prise en charge'};
  return {hd:'Synthèse locale · '+modLab(a),ti:T[t],h:`<div class="ck-tabs ck-ctl" role="tablist" aria-label="Synthèse locale">${['A','B'].map(k=>`<button type="button" class="b" role="tab" id="ck-tab-${k}" aria-selected="${k===t}" aria-controls="ck-pan" tabindex="${k===t?0:-1}" data-ck="tab" data-k="loc|${esc(a)}|${k}">${T[k]}</button>`).join('')}</div>`
   +`<div id="ck-pan" role="tabpanel" aria-labelledby="ck-tab-${t}">${L.length?'<ul class="ck-list">'+L.map(id=>'<li>'+(t==='A'?ckLnk('SYN','syn',id):ckLnk('HYP','hyp',id))+'</li>').join('')+'</ul>':'<p><span class="vb pend">À vérifier</span> Aucune entrée pour ce module.</p>'}</div>`}}
 if(ty==='nc'){const e=(ckData('NC')||{})[a];if(!e)return null;const V=e.vues||{},K=[...Object.keys(NC_VUE).filter(v=>v!=='tour'&&V[v]),...Object.keys(V).filter(v=>V[v]&&!(v in NC_VUE))],
   v=b==='tour'&&e.tour?'tour':V[b]?b:(b==='34'&&V.trois_quarts?'trois_quarts':K[0]);if(!v)return null;
  const bt=[...K,...(e.tour?['tour']:[])].map(x=>`<button type="button" class="b" data-ck="vue" data-k="nc|${esc(a)}|${x}" aria-pressed="${x===v}">${ncVue(x)}</button>`).join(''),
   les=ckArr(e.lesions).map(l=>`<li><b>Site ${esc(l.site)}</b> : ${ckP(l.niveau)} ${ckP(l.deficit)}${l.exam_orientant?' '+ckP(l.exam_orientant):''}${ckArr(l.syn).length?' Syndrome : '+ckArr(l.syn).map(i=>ckLnk('SYN','syn',i)).join(', ')+'.':''}${ckArr(l.hyp).length?' Hypothèses : '+ckArr(l.hyp).map(i=>ckLnk('HYP','hyp',i)).join(', ')+'.':''}${l.statut==='À vérifier'?' <span class="vb pend">À vérifier</span>':''}${ckArr(l.src).length?` <small>[${ckSrc(l.src)}]</small>`:''}</li>`).join(''),
   ana=[['Noyaux',e.noyaux],['Trajet',e.trajet],['Foramens',e.foramens],['Territoires',e.territoires]].map(([t,L])=>ckList(t,L,ckP)).join('');
  return {hd:'Schéma · '+ckLab('NC',a),ti:ckLab('NC',a)+' · '+ncVue(v),h:`<div class="ck-ctl ck-vues" role="group" aria-label="Vue du schéma">${bt}</div>`
   +`<div class="ck-ctl ck-etats" role="group" aria-label="État du schéma" hidden></div>`
   +`<fieldset class="ck-ctl ck-couches"${v==='tour'?' disabled':''}><legend>Couches</legend>${NC_COU.map(c=>`<label><input type="checkbox" data-ck="cou" value="${c}"${ckCou[c]===false?'':' checked'}> ${NC_COUL[c]}</label>`).join('')}</fieldset>`
   +`<figure class="ck-fig" data-nc="${esc(a)}" data-vue="${v}"></figure>`
   +(les?`<details class="ck-det" open><summary>Sites lésionnels</summary><ul>${les}</ul></details>`:'')+(ana?`<details class="ck-det"><summary>Anatomie</summary>${ana}</details>`:'')+(e.src||e.statut?ckFoot(e):'')}}
 return undefined}
/* Schémas : SVG en ligne depuis CK_SVG (assets/nc/ncXX.js), nettoyé ; états (data-etats) et couches réglables ; sinon image simple. */
const ckJs={};
function ckSvg(fig,src){const d=new DOMParser().parseFromString(src,'image/svg+xml'),s=d.documentElement;if(!s||s.nodeName!=='svg')return null;
 s.querySelectorAll('script,foreignObject').forEach(x=>x.remove());for(const el of [s,...s.querySelectorAll('*')])for(const at of [...el.attributes]){if(/^on/i.test(at.name)||(/href$/i.test(at.name)&&/^\s*javascript:/i.test(at.value)))el.removeAttribute(at.name)}
 const n=document.importNode(s,true);n.setAttribute('role','img');n.removeAttribute('width');n.removeAttribute('height');n.setAttribute('preserveAspectRatio','xMidYMid meet');return n}
function ckEtats(s){try{return s&&s.dataset.etats?JSON.parse(s.dataset.etats):null}catch(e){return null}}
/* État X : [data-etat] visibles seulement pour X ; couches cochées d’après data-etats[X] (l’utilisateur peut ensuite les régler). */
function ckEtat(fig,x){const s=fig.querySelector('svg'),M=ckEtats(s);if(!M||!M[x])return;ckEt=x;s.dataset.etat=x;
 s.querySelectorAll('[data-etat]').forEach(g=>g.setAttribute('display',g.dataset.etat===x?'inline':'none'));NC_COU.forEach(c=>{ckCou[c]=M[x].includes(c)});
 TIPEL.querySelectorAll('input[data-ck=cou]').forEach(i=>{i.checked=ckCou[i.value]!==false});TIPEL.querySelectorAll('[data-ck=etat]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.e===x)));ckApply(fig)}
function ckApply(fig){const s=fig.querySelector('svg'),F=TIPEL.querySelector('.ck-couches');if(!F)return;
 for(const i of F.querySelectorAll('input[data-ck=cou]')){const g=s&&s.querySelector(`#${i.value},[data-couche="${i.value}"]`);i.disabled=!g||!g.childElementCount;if(g)g.setAttribute('display',i.checked?'inline':'none')}}
function ckFig(fig){const id=fig.dataset.nc,v=fig.dataset.vue,e=(ckData('NC')||{})[id];if(!e)return;const nom=ckLab('NC',id),F=TIPEL.querySelector('.ck-couches');
 if(v==='tour'){fig.innerHTML=`<div class="ck-tour" role="slider" tabindex="0" aria-label="Tour du schéma ${esc(nom)} : glissez ou utilisez les flèches" aria-valuemin="0" aria-valuemax="7" aria-valuenow="0" aria-valuetext="0°" style="background-image:url('${esc(e.tour)}')"></div><figcaption class="st">Glissez, ou utilisez les flèches gauche et droite : 8 vues à 45°.</figcaption>`;return}
 const p=e.vues[v],SV=ckW('SVG'),src=SV&&SV[p];
 const cred=s=>{let c=(ckW('NC_CRED')||{})[p]||(e.credits||{})[v];/* le SVG de Dédale porte déjà son crédit visible */c=c?(typeof c==='string'?c:(c.tasl||c.credit||'')):'';return c?`<figcaption class="ck-cr">${esc(c)}</figcaption>`:''};
 if(src){const n=ckSvg(fig,src);if(n){n.setAttribute('aria-label','Schéma : '+nom+', vue '+ncVue(v));n.removeAttribute('aria-labelledby');fig.replaceChildren(n);fig.insertAdjacentHTML('beforeend',cred(n));
  const M=ckEtats(n),E=TIPEL.querySelector('.ck-etats');
  if(M&&E){const K=Object.keys(M),x=K.includes(ckEt)?ckEt:(n.dataset.etat&&M[n.dataset.etat]?n.dataset.etat:K[0]);E.innerHTML=K.map(k=>`<button type="button" class="b" data-ck="etat" data-e="${esc(k)}" aria-pressed="${k===x}">${esc(NC_ETL[k]||k)}</button>`).join('');E.hidden=false;ckEtat(fig,x)}else ckApply(fig);return}}
 const js=e.js||'assets/nc/'+id+'.js';
 if(!(js in ckJs)){ckJs[js]=0;fig.innerHTML='<p class="st">Chargement du schéma…</p>';const sc=document.createElement('script');sc.src=js;
  sc.onload=()=>{ckJs[js]=1;if(fig.isConnected)ckFig(fig)};sc.onerror=()=>{ckJs[js]=-1;if(fig.isConnected)ckFig(fig)};document.head.appendChild(sc);return}
 if(ckJs[js]===0)return;
 fig.innerHTML=`<img src="${esc(p)}" alt="Schéma : ${esc(nom)}, vue ${ncVue(v)}" loading="lazy">${cred(null)}<p class="st">Les couches ne sont pas disponibles pour ce schéma : le fichier ${esc(js)} manque.</p>`;if(F)F.disabled=true}
function ckTour(el,d){const f=((+el.getAttribute('aria-valuenow')+d)%8+8)%8;el.setAttribute('aria-valuenow',f);el.setAttribute('aria-valuetext',f*45+'°');el.style.backgroundPositionX=(f*100/7)+'%'}
/* Pile de fenêtres : un terme ouvert depuis la fenêtre l’empile (5 niveaux au plus) ; « ← Retour » et le fil d’Ariane y reviennent. */
function tipGo(i){if(i<0||i>=tipStk.length)return;const s=tipStk[i];tipStk.length=i;showTip({dataset:{t:s.k}},true,tipOp,true,true)}
function tipNav(e){const t=e.target;if(!(t instanceof Element)||!TIPEL.contains(t))return false;
 if(t.closest('input,a[href]'))return true;
 const bk=t.closest('.bk');if(bk){e.preventDefault();e.stopPropagation();tipGo(tipStk.length-1);return true}
 const lv=t.closest('[data-lv]');if(lv){e.preventDefault();e.stopPropagation();tipGo(+lv.dataset.lv);return true}
 const et=t.closest('[data-ck=etat]');if(et){e.preventDefault();e.stopPropagation();const f=TIPEL.querySelector('.ck-fig');if(f)ckEtat(f,et.dataset.e);return true}
 const c=t.closest('[data-ck]');if(c&&c.dataset.k){e.preventDefault();e.stopPropagation();const k=c.dataset.k;showTip({dataset:{t:k}},true,tipOp,false,true);const n=TIPEL.querySelector(`[data-k="${CSS.escape(k)}"]`);if(n)n.focus({preventScroll:true});return true}
 const a=t.closest('.ck-b [data-t]');if(a){e.preventDefault();e.stopPropagation();clearTimeout(tipT);showTip(a,true,a,e.detail===0);return true}
 return false}
TIPEL.addEventListener('change',e=>{const i=e.target.closest('input[data-ck=cou]');if(!i)return;ckCou[i.value]=i.checked;const f=TIPEL.querySelector('.ck-fig');if(f)ckApply(f)});
TIPEL.addEventListener('keydown',e=>{const t=e.target;if(t.matches('[role=tab]')&&(e.key==='ArrowLeft'||e.key==='ArrowRight')){const L=[...TIPEL.querySelectorAll('[role=tab]')],n=L[(L.indexOf(t)+(e.key==='ArrowRight'?1:L.length-1))%L.length];e.preventDefault();n.click()}
 else if(t.classList.contains('ck-tour')&&(e.key==='ArrowLeft'||e.key==='ArrowRight')){e.preventDefault();ckTour(t,e.key==='ArrowRight'?1:-1)}});
TIPEL.addEventListener('pointerdown',e=>{const el=e.target.closest('.ck-tour');if(!el)return;el.setPointerCapture(e.pointerId);let x0=e.clientX;
 const mv=ev=>{const d=Math.trunc((ev.clientX-x0)/40);if(d){ckTour(el,d);x0+=d*40}},up=()=>{el.removeEventListener('pointermove',mv);el.removeEventListener('pointerup',up);el.removeEventListener('pointercancel',up)};
 el.addEventListener('pointermove',mv);el.addEventListener('pointerup',up);el.addEventListener('pointercancel',up)});
function tipCk(lv,k){TIPEL.classList.toggle('ck',k.split('|')[0] in CK_DEP);TIPEL.classList.toggle('ck-nc',k.startsWith('nc|'));const B=TIPEL.querySelector('.ck-b');if(!B)return;const ex=tipStk.map(s=>s.k).concat(k);
 B.querySelectorAll('.ck-l[data-t]').forEach(a=>{if(lv>=CK_MAX||ex.includes(a.dataset.t))a.replaceWith(document.createTextNode(a.textContent))});
 if(lv<CK_MAX)gloLink(B,new Set(ex.filter(s=>s.startsWith('glo|')).map(s=>s.split('|')[1])),true);
 B.querySelectorAll('.ck-fig').forEach(ckFig)}
if(ckW('GLO')||ckW('GLO_INDEX'))gloStart();else if(typeof ckLoad==='function')addEventListener('load',()=>ckIdle(()=>ckLoad('glo-index').then(gloStart,()=>{})),{once:true});
