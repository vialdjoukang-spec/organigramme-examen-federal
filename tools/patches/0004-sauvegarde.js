/* ---------- HERMÈS : sauvegarde automatique fiable (miroir IndexedDB, versions, persistance, fichier) ---------- */
/* Chaque écriture réussie (lsSet) programme svFlush : copie « cur » dans IndexedDB avec somme FNV-1a, version horaire au plus, 30 versions gardées. */
var SV_DB='orga-sauvegarde',SV_MAX=30,SV_HOT=20,svT=null,svFT=null,svReady=false,svFile=null,svFileNeed=false,svIdb=null,svLast=null,svPers='',svFileTxt='',svErr='';
const SV_BOOT=(()=>{const ok={},bad=[];let ef=null;try{ef=localStorage.getItem('orga-ef');const k=bakKeys();for(const x in k){let g=true;if(x!=='orga-tab'){try{const v=JSON.parse(k[x]);g=v!==null&&typeof v==='object'}catch(e){g=false}}if(g)ok[x]=1;else bad.push(x)}}catch(e){bad.push('stockage')}
 if(ef===null)bad.push('orga-ef');return {ok,bad}})();
function svCanon(o){return JSON.stringify(Object.keys(o).sort().map(k=>[k,o[k]]))}
function svSum(o){const s=svCanon(o);let h=0x811c9dc5;for(let i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619)}return ('0000000'+(h>>>0).toString(16)).slice(-8)+'-'+s.length}
function svOk(r){return !!(r&&r.cles&&typeof r.cles==='object'&&r.sum===svSum(r.cles)&&!bakCheck({format:BAK_F,version:BAK_V,cles:r.cles}))}
function svOpen(){if(!svIdb){svIdb=new Promise((ok,ko)=>{if(!window.indexedDB)return ko(new Error('IndexedDB absent'));const q=indexedDB.open(SV_DB,1);
 q.onupgradeneeded=()=>{const d=q.result;d.createObjectStore('etat');d.createObjectStore('versions',{keyPath:'id',autoIncrement:true})};q.onsuccess=()=>ok(q.result);q.onerror=()=>ko(q.error)});svIdb.catch(()=>{})}return svIdb}
function svTx(st,mode,fn){return svOpen().then(d=>new Promise((ok,ko)=>{const t=d.transaction(st,mode),q=fn(t.objectStore(st));let r;if(q)q.onsuccess=()=>{r=q.result};t.oncomplete=()=>ok(r);t.onerror=t.onabort=()=>ko(t.error)}))}
const svGet=k=>svTx('etat','readonly',o=>o.get(k)),svPut=(k,v)=>svTx('etat','readwrite',o=>o.put(v,k)),svList=()=>svTx('versions','readonly',o=>o.getAll()).then(L=>L.sort((a,b)=>a.t<b.t?1:-1));
function svRec(){const c=bakKeys();return {t:new Date().toISOString(),d:iso(new Date()),cles:c,sum:svSum(c)}}
function svTouch(){if(!svReady)return;clearTimeout(svT);svT=setTimeout(svFlush,600)}
async function svFlush(){clearTimeout(svT);if(!svReady)return;let r;try{r=svRec()}catch(e){return}
 try{await svPut('cur',r);svLast=new Date(r.t);svErr='';await svAuto(r)}catch(e){svErr='La copie de secours dans IndexedDB a échoué ('+((e&&e.name)||'erreur')+') ; exportez votre progression.'}
 svStat();if(svFile&&!svFileNeed)svFileWrite()}
async function svAdd(kind,r){r=r||svRec();await svTx('versions','readwrite',o=>o.add({t:r.t,d:r.d,kind,cles:r.cles,sum:r.sum,n:bakSum(r.cles)}));await svPrune()}
async function svPrune(){const L=await svList(),keep=new Set(L.slice(0,SV_HOT).map(v=>v.id)),seen=new Set(L.slice(0,SV_HOT).map(v=>v.d));
 for(const v of L.slice(SV_HOT))if(keep.size<SV_MAX&&!seen.has(v.d)){seen.add(v.d);keep.add(v.id)}
 const del=L.filter(v=>!keep.has(v.id));if(del.length)await svTx('versions','readwrite',o=>{del.forEach(v=>o.delete(v.id))})}
async function svAuto(r){if(!Object.keys(r.cles).length)return;const L=await svList(),last=L[0];if(last&&last.sum===r.sum)return;if(last&&Date.now()-new Date(last.t)<36e5)return;
 await svAdd(L.some(v=>v.d===r.d)?'horaire':'jour',r)}
function svHm(d){return d.toLocaleTimeString('fr-CH',{hour:'2-digit',minute:'2-digit'})}
function svStat(){const y=document.getElementById('sync');if(y&&svLast&&!Object.keys(lsBad).length){y.textContent='Enregistré à '+svHm(svLast);y.title='Votre progression est enregistrée dans ce navigateur et dans sa copie de secours IndexedDB.'}
 const s=document.getElementById('sv-s');if(s)s.textContent=[svErr,svPers,svFileTxt].filter(Boolean).join(' ')}
async function svPersist(){const st=navigator.storage;if(!st||!st.persist){svPers='Ce navigateur ne permet pas de protéger son stockage ; exportez votre progression chaque semaine.';return svStat()}
 try{let p=await st.persisted();if(!p)p=await st.persist();svPers=p?'Le navigateur protège ce stockage contre l’effacement automatique.':'Le navigateur n’a pas encore accordé la protection du stockage ; la copie de secours, les versions et l’export restent vos garanties.'}catch(e){svPers=''}svStat()}
function svFileBtn(){const b=document.getElementById('sv-fb');if(!b)return;b.hidden=typeof window.showSaveFilePicker!=='function';b.textContent=svFile?(svFileNeed?'Reprendre le fichier automatique':'Changer de fichier automatique'):'Activer un fichier de sauvegarde automatique'}
async function svFileInit(){svFileBtn();if(typeof window.showSaveFilePicker!=='function')return;try{const h=await svGet('fichier');if(!h)return;svFile=h;svFileNeed=(await h.queryPermission({mode:'readwrite'}))!=='granted';
 svFileTxt=svFileNeed?'Cliquez sur « Reprendre le fichier automatique » pour autoriser de nouveau l’écriture dans « '+h.name+' ».':'Chaque modification s’écrit aussi dans le fichier « '+h.name+' ».'}catch(e){}svFileBtn();svStat()}
async function svFileClick(){try{if(svFile&&svFileNeed){svFileNeed=(await svFile.requestPermission({mode:'readwrite'}))!=='granted'}
 else{const h=await window.showSaveFilePicker({suggestedName:'organigramme-sauvegarde-auto.json',types:[{description:'Sauvegarde JSON',accept:{'application/json':['.json']}}]});svFile=h;svFileNeed=false;await svPut('fichier',h)}
 if(!svFileNeed){svFileTxt='Chaque modification s’écrit aussi dans le fichier « '+svFile.name+' ».';svFileWrite(0)}}catch(e){if(!e||e.name!=='AbortError')svFileTxt='Le fichier automatique n’a pas pu être activé ('+((e&&e.name)||'erreur')+').'}svFileBtn();svStat()}
function svFileWrite(ms){clearTimeout(svFT);svFT=setTimeout(async()=>{if(!svFile)return;try{if((await svFile.queryPermission({mode:'readwrite'}))!=='granted'){svFileNeed=true;svFileTxt='Cliquez sur « Reprendre le fichier automatique » pour autoriser de nouveau l’écriture dans « '+svFile.name+' ».';svFileBtn();return svStat()}
 const w=await svFile.createWritable();await w.write(JSON.stringify({format:BAK_F,version:BAK_V,exporte:new Date().toISOString(),cles:bakKeys()},null,1));await w.close();svFileTxt='Le fichier « '+svFile.name+' » est à jour depuis '+svHm(new Date())+' ; vous pouvez l’importer comme un export.'}
 catch(e){svFileTxt='L’écriture dans le fichier automatique a échoué ('+((e&&e.name)||'erreur')+').'}svStat()},ms==null?1500:ms)}
const SV_KIND={jour:'première version du jour',horaire:'version horaire',manuel:'version créée à la main','avant-restauration':'état mis de côté avant une restauration'};
async function svVer(force){const el=document.getElementById('ver'),bt=document.getElementById('sv-v');if(!el.hidden&&!force){el.hidden=true;bt.setAttribute('aria-expanded','false');return}
 let L;try{L=await svList()}catch(e){el.innerHTML='<p>La liste des versions est indisponible, car ce navigateur bloque IndexedDB.</p>';el.hidden=false;return}
 el.innerHTML='<div class="row"><b>Versions enregistrées automatiquement (les '+SV_MAX+' dernières)</b><button class="b" id="sv-new" type="button">Créer une version maintenant</button><button class="b" id="sv-x" type="button">Fermer</button></div>'
  +(L.length?'<ol class="ver-l">'+L.map(v=>'<li><span><b>'+esc(bakDate(v.t))+'</b> · '+esc(SV_KIND[v.kind]||v.kind)+'<br><small>'+esc(v.n||'')+'</small></span><span class="sv-a"><button class="b" type="button" data-r="'+v.id+'">Restaurer</button></span></li>').join('')+'</ol>'
  :'<p>Aucune version n’existe encore ; la première se crée dès votre prochaine modification.</p>');el.hidden=false;bt.setAttribute('aria-expanded','true')}
function svWrite(c){let old={};try{old=bakKeys()}catch(e){}try{Object.keys(old).forEach(k=>localStorage.removeItem(k));for(const k in c)localStorage.setItem(k,c[k]);return true}
 catch(e){try{Object.keys(bakKeys()).forEach(k=>localStorage.removeItem(k));for(const k in old)localStorage.setItem(k,old[k])}catch(_){}return false}}
async function svRestore(id){let v;try{v=(await svList()).find(x=>x.id===id)}catch(e){}
 if(!svOk(v)){bakMsg('Cette version est endommagée, car sa somme de contrôle ne correspond plus ; votre progression reste inchangée.','bad');return false}
 try{local(true);await svAdd('avant-restauration')}catch(e){bakMsg('L’état actuel n’a pas pu être mis de côté ; la restauration est donc annulée.','bad');return false}
 svReady=false;if(!svWrite(v.cles)){svReady=true;bakMsg('La restauration a échoué, car le stockage est plein ou bloqué ; l’état antérieur est rétabli.','bad');return false}
 try{await svPut('cur',Object.assign(svRec(),{t:new Date().toISOString()}))}catch(e){}try{sessionStorage.setItem('orga-rest',v.t)}catch(e){}location.reload();return true}
svFileBtn();document.getElementById('sv-v').onclick=()=>svVer();document.getElementById('sv-fb').onclick=svFileClick;
document.getElementById('ver').addEventListener('click',async e=>{const t=e.target;if(t.id==='sv-x'){svVer()}
 else if(t.id==='sv-new'){try{local(true);await svAdd('manuel');svVer(true)}catch(_){bakMsg('La version n’a pas pu être créée, car ce navigateur bloque IndexedDB.','bad')}}
 else if(t.dataset.r){t.parentNode.innerHTML='La restauration met d’abord l’état actuel de côté. <button class="b p" type="button" data-ok="'+t.dataset.r+'">Confirmer</button> <button class="b" type="button" data-no="1">Annuler</button>'}
 else if(t.dataset.ok)svRestore(+t.dataset.ok);else if(t.dataset.no)svVer(true)});
(async()=>{try{const fl=sessionStorage.getItem('orga-rec');
 if(SV_BOOT.bad.length&&!fl){const r=await svGet('cur');if(svOk(r)){let n=0;for(const k in r.cles)if(!SV_BOOT.ok[k]){localStorage.setItem(k,r.cles[k]);n++}
  if(n){sessionStorage.setItem('orga-rec',r.t);location.reload();return}}}
 if(fl){sessionStorage.removeItem('orga-rec');bakMsg('Votre progression manquait ou était endommagée dans ce navigateur ; elle a été récupérée depuis la copie de secours du '+bakDate(fl)+'.','ok')}
 const rs=sessionStorage.getItem('orga-rest');if(rs){sessionStorage.removeItem('orga-rest');bakMsg('La version du '+bakDate(rs)+' est restaurée ; l’état précédent reste disponible dans « Restaurer une version ».','ok')}}catch(e){}
 svReady=true;svFlush();svPersist();svFileInit()})();
