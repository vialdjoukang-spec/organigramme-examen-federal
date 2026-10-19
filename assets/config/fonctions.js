function monday(d){const x=new Date(d);const k=(x.getDay()+6)%7;x.setDate(x.getDate()-k);x.setHours(0,0,0,0);return x}
function uid(){return (crypto.randomUUID?crypto.randomUUID():Date.now().toString(36)+Math.random().toString(36).slice(2)).replace(/[^\w-]/g,'')}
function lsSet(k,v){try{localStorage.setItem(k,v);if(lsBad[k]){delete lsBad[k];bakShow()}svTouch();return true}catch(e){lsBad[k]=(e&&e.name)||'erreur';const y=document.getElementById('sync');if(y)y.textContent='Non enregistré dans ce navigateur ('+lsBad[k]+')';bakShow();return false}}
function bakKeys(){const o={};for(let i=0;i<localStorage.length;i++){const k=localStorage.key(i);if(k&&k.indexOf('orga-')===0&&k!==BAK_KEY&&k!=='orga-probe')o[k]=localStorage.getItem(k)}return o}
function bakDate(t){const d=new Date(t);return isNaN(d)?'?':d.toLocaleDateString('fr-CH')+' à '+d.toLocaleTimeString('fr-CH',{hour:'2-digit',minute:'2-digit'})}
function bakMsg(t,c){const m=document.getElementById('bak-m');m.textContent=t;m.className='st '+(c||'');m.hidden=!t}
function bakShow(){const el=document.getElementById('bak');if(!el)return;const bad=Object.keys(lsBad);let t,c='';
 if(bad.length){c='bad';t='L’enregistrement dans ce navigateur a échoué ('+lsBad[bad[0]]+'), car son stockage est plein ou bloqué : vos dernières modifications risquent de se perdre. Exportez votre progression maintenant, puis libérez de l’espace.'}
 else{let last=null;try{last=localStorage.getItem(BAK_KEY)}catch(e){}const n=last?Math.floor((Date.now()-new Date(last))/864e5):null;
  if(!last){c='warn';t='Votre progression vit seulement dans ce navigateur, et vous ne l’avez encore jamais exportée. Exportez-la chaque semaine, car Safari peut effacer ce stockage après sept jours sans visite.'}
  else if(!(n<BAK_DAYS)){c='warn';t='Votre dernier export date du '+bakDate(last)+', il y a '+n+' jours. Exportez votre progression, car Safari peut effacer ce stockage après sept jours sans visite.'}
  else t='Votre progression est enregistrée dans ce navigateur, et votre dernier export date du '+bakDate(last)+'.'}
 el.className='bak'+(c?' '+c:'');document.getElementById('bak-t').textContent=t}
function bakSum(k){const P=x=>{try{return JSON.parse(k[x]||'null')||{}}catch(e){return {}}},ef=P('orga-ef'),n=o=>Object.keys(o||{}).length;
 return n(ef.seances)+' séances, '+Object.values(ef.exi||{}).filter(v=>v===true).length+' exigences cochées, '+n(P('orga-not'))+' SSP suivis en Notions CK, '+n(P('orga-ges'))+' gestes cochés et '+n(P('orga-cs'))+' simulations CS'}
function bakExport(){local(true);let k;try{k=bakKeys()}catch(e){bakMsg('L’export a échoué, car ce navigateur refuse la lecture de son stockage.','bad');return}
 const d=new Date(),f={format:BAK_F,version:BAK_V,exporte:d.toISOString(),cles:k},a=document.createElement('a');
 a.href=URL.createObjectURL(new Blob([JSON.stringify(f,null,1)],{type:'application/json'}));a.download='organigramme-progression-'+iso(d)+'.json';
 document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},1500);
 lsSet(BAK_KEY,d.toISOString());bakShow();bakMsg('Le fichier « '+a.download+' » contient '+bakSum(k)+'. Gardez-le hors de ce navigateur, par exemple dans votre stockage en ligne.','ok')}
function bakCheck(f){if(!f||typeof f!=='object'||f.format!==BAK_F)return 'Ce fichier ne provient pas d’un export de l’organigramme.';
 if(typeof f.version!=='number'||f.version<1)return 'Ce fichier ne porte pas de numéro de version valide.';
 if(f.version>BAK_V)return 'Ce fichier provient d’une version plus récente de l’application ; rechargez d’abord la page en ligne.';
 if(!f.cles||typeof f.cles!=='object'||!Object.keys(f.cles).length)return 'Ce fichier ne contient aucune donnée de progression.';
 for(const k in f.cles){if(k.indexOf('orga-')!==0||k===BAK_KEY)return 'La clé « '+k+' » n’appartient pas à l’organigramme.';
  if(typeof f.cles[k]!=='string')return 'La clé « '+k+' » n’a pas le format attendu.';
  if(k!=='orga-tab'){try{JSON.parse(f.cles[k])}catch(e){return 'La clé « '+k+' » est endommagée.'}}}return null}
function bakMigrate(f){ return f.cles}
function bakRead(file){bakMsg('');const r=new FileReader();r.onerror=()=>bakMsg('La lecture du fichier a échoué ; votre progression reste inchangée.','bad');
 r.onload=()=>{let f;try{f=JSON.parse(r.result)}catch(e){bakMsg('Ce fichier n’est pas un JSON valide ; votre progression reste inchangée.','bad');return}
  const er=bakCheck(f);if(er){bakMsg(er+' Votre progression reste inchangée.','bad');return}
  bakPend=bakMigrate(f);let cur={};try{cur=bakKeys()}catch(e){}const pv=document.getElementById('bak-pv');
  pv.innerHTML='<p>Ce fichier date du <b>'+esc(bakDate(f.exporte))+'</b> et contient '+esc(bakSum(bakPend))+'.</p><p>Ce navigateur contient actuellement '+esc(bakSum(cur))+'. L’import remplacera toute cette progression, et vous ne pourrez pas l’annuler sans un autre export.</p><div class="row"><button class="b p" id="bak-ok" type="button">Remplacer ma progression</button><button class="b" id="bak-no" type="button">Annuler</button></div>';
  pv.hidden=false;document.getElementById('bak-ok').focus()};r.readAsText(file)}
function bakApply(){if(!bakPend)return;let old={};try{old=bakKeys()}catch(e){}
 try{Object.keys(old).forEach(k=>localStorage.removeItem(k));for(const k in bakPend)localStorage.setItem(k,bakPend[k])}
 catch(e){try{Object.keys(bakKeys()).forEach(k=>localStorage.removeItem(k));for(const k in old)localStorage.setItem(k,old[k])}catch(_){}
  bakMsg('L’import a échoué, car le stockage de ce navigateur est plein ou bloqué ; l’état antérieur est rétabli.','bad');return}
 lsSet(BAK_KEY,new Date().toISOString());try{sessionStorage.setItem('orga-imp','1')}catch(e){}location.reload()}
function svCanon(o){return JSON.stringify(Object.keys(o).sort().map(k=>[k,o[k]]))}
function svSum(o){const s=svCanon(o);let h=0x811c9dc5;for(let i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619)}return ('0000000'+(h>>>0).toString(16)).slice(-8)+'-'+s.length}
function svOk(r){return !!(r&&r.cles&&typeof r.cles==='object'&&r.sum===svSum(r.cles)&&!bakCheck({format:BAK_F,version:BAK_V,cles:r.cles}))}
function svOpen(){if(!svIdb){svIdb=new Promise((ok,ko)=>{if(!window.indexedDB)return ko(new Error('IndexedDB absent'));const q=indexedDB.open(SV_DB,1);
 q.onupgradeneeded=()=>{const d=q.result;d.createObjectStore('etat');d.createObjectStore('versions',{keyPath:'id',autoIncrement:true})};q.onsuccess=()=>ok(q.result);q.onerror=()=>ko(q.error)});svIdb.catch(()=>{})}return svIdb}
function svTx(st,mode,fn){return svOpen().then(d=>new Promise((ok,ko)=>{const t=d.transaction(st,mode),q=fn(t.objectStore(st));let r;if(q)q.onsuccess=()=>{r=q.result};t.oncomplete=()=>ok(r);t.onerror=t.onabort=()=>ko(t.error)}))}
function svRec(){const c=bakKeys();return {t:new Date().toISOString(),d:iso(new Date()),cles:c,sum:svSum(c)}}
function svTouch(){if(!svReady)return;clearTimeout(svT);svT=setTimeout(svFlush,600)}
function svHm(d){return d.toLocaleTimeString('fr-CH',{hour:'2-digit',minute:'2-digit'})}
function svStat(){const y=document.getElementById('sync');if(y&&svLast&&!Object.keys(lsBad).length){y.textContent='Enregistré à '+svHm(svLast);y.title='Votre progression est enregistrée dans ce navigateur et dans sa copie de secours IndexedDB.'}
 const s=document.getElementById('sv-s');if(s)s.textContent=[svErr,svPers,svFileTxt].filter(Boolean).join(' ')}
function svFileBtn(){const b=document.getElementById('sv-fb');if(!b)return;b.hidden=typeof window.showSaveFilePicker!=='function';b.textContent=svFile?(svFileNeed?'Reprendre le fichier automatique':'Changer de fichier automatique'):'Activer un fichier de sauvegarde automatique'}
function svFileWrite(ms){clearTimeout(svFT);svFT=setTimeout(async()=>{if(!svFile)return;try{if((await svFile.queryPermission({mode:'readwrite'}))!=='granted'){svFileNeed=true;svFileTxt='Cliquez sur « Reprendre le fichier automatique » pour autoriser de nouveau l’écriture dans « '+svFile.name+' ».';svFileBtn();return svStat()}
 const w=await svFile.createWritable();await w.write(JSON.stringify({format:BAK_F,version:BAK_V,exporte:new Date().toISOString(),cles:bakKeys()},null,1));await w.close();svFileTxt='Le fichier « '+svFile.name+' » est à jour depuis '+svHm(new Date())+' ; vous pouvez l’importer comme un export.'}
 catch(e){svFileTxt='L’écriture dans le fichier automatique a échoué ('+((e&&e.name)||'erreur')+').'}svStat()},ms==null?1500:ms)}
function svWrite(c){let old={};try{old=bakKeys()}catch(e){}try{Object.keys(old).forEach(k=>localStorage.removeItem(k));for(const k in c)localStorage.setItem(k,c[k]);return true}
 catch(e){try{Object.keys(bakKeys()).forEach(k=>localStorage.removeItem(k));for(const k in old)localStorage.setItem(k,old[k])}catch(_){}return false}}
function local(save){if(save){lsSet('orga-ef',JSON.stringify(S));return}try{const v=JSON.parse(localStorage.getItem('orga-ef')||'null');if(v)S=Object.assign(S,v)}catch(e){}}
function ckDone(code){return Object.values(S.seances).some(x=>x.ssp===code&&x.done&&x.act==='Cours CK')}
function hl(s,q){if(!q)return esc(s);const n=norm(s),i=n.indexOf(q);return i<0?esc(s):esc(s.slice(0,i))+'<mark>'+esc(s.slice(i,i+q.length))+'</mark>'+esc(s.slice(i+q.length))}
function renderList(){const q=norm($('#q').value.trim()),g=$('#grp').value;let h='',n=0;
 for(const f of ['G','S','F','O']){if(famF&&famF!==f)continue;const gs=GKEYS.filter(k=>k[0]===f&&(!g||k===g));let fh='';
  for(const k of gs){const L=SSP.filter(s=>s[2]===k&&(!q||norm(s[0]+' '+s[1]).includes(q)));if(!L.length)continue;n+=L.length;const cov=L.filter(s=>ckDone(s[0])).length,shut=closed[k]&&!q;
   fh+=`<div class="grp-h" data-g="${k}"><i style="background:${GCOL[k]}"></i>${k} · ${esc(GROUPES[k])}<small>${cov}/${SSP.filter(s=>s[2]===k).length} ${shut?'▸':'▾'}</small></div>`;
   if(!shut)fh+=L.map(s=>`<div class="it${sel===s[0]?' sel':''}" style="--gc:${GCOL[k]}" draggable="true" tabindex="0" aria-keyshortcuts="i" data-c="${s[0]}" data-t="s|${s[0]}"><code>${hl(s[0],q)}</code><span><i class="dot${ckDone(s[0])?' on':''}"></i>${hl(s[1],q)}</span><small>${esc(GROUPES[s[2]])}</small></div>`).join('')}
  if(fh)h+=`<div class="fam-h">${esc(FAM[f])}</div>`+fh}
 $('#list').innerHTML=h||'<p class="st">Aucun chapitre ne correspond.</p>';$('#cnt').textContent=n+' SSP'}
function days(){if(mode==='d'){const d=new Date(cur);d.setHours(0,0,0,0);return [d]}const m=monday(cur);return [...Array(7)].map((_,i)=>{const d=new Date(m);d.setDate(m.getDate()+i);return d})}
function renderGrid(){const D=days(),g=$('#grid');g.className='grid'+(mode==='d'?' day':'');g.style.gridTemplateColumns=`56px repeat(${D.length},minmax(${mode==='d'?0:96}px,1fr))`;
 const t=iso(new Date());let h='<div class="hd"></div>'+D.map(d=>`<div class="hd${iso(d)===t?' today':''}" data-wd="${(d.getDay()+6)%7+1}"><span>${JOURS[d.getDay()]} ${d.getDate()}</span><small>${MOIS[d.getMonth()]}</small></div>`).join('');
 h+='<div class="hours">'+[...Array(H1-H0)].map((_,i)=>`<div class="hl">${pad(H0+i)}:00</div>`).join('')+'</div>';
 h+=D.map(d=>{const k=iso(d);let prev=-1;const bl=Object.entries(S.seances).filter(([,x])=>x.date===k).sort((a,b)=>a[1].start-b[1].start).map(([id,x])=>{const gi=BY[x.ssp]?GKEYS.indexOf(BY[x.ssp][2])%10:0;let ci=gi;if(ci===prev)ci=(ci+3)%10;prev=ci;const bc='var(--c'+ci+')';const top=(x.start-H0*60)/60*PX,ht=Math.max(12,x.dur/60*PX-2);const s=BY[x.ssp]||[x.ssp,'',''];return `<div class="blk${x.done?' done':''}" tabindex="0" data-id="${id}" data-t="s|${x.ssp}|${id}" style="top:${top}px;height:${ht}px;--bc:${bc}"><b>${hm(x.start)} · ${esc(s[0])}</b><span class="du">${x.dur}′</span><span class="t">${esc(x.act)} · ${esc(s[1])}</span><span class="rz" aria-hidden="true"></span></div>`}).join('');
  const now=new Date();const nl=k===t&&now.getHours()>=H0&&now.getHours()<H1?`<div class="now" style="top:${((now.getHours()-H0)*60+now.getMinutes())/60*PX}px"></div>`:'';
  return `<div class="col" data-d="${k}" data-wd="${(d.getDay()+6)%7+1}" style="height:${(H1-H0)*PX}px">${bl}${nl}</div>`}).join('');
 g.innerHTML=h;blkFit(g);const m0=D[0],m1=D[D.length-1];$('#wlab').textContent=mode==='d'?`${JOURS[m0.getDay()]} ${m0.getDate()} ${MOIS[m0.getMonth()]} ${m0.getFullYear()}`:`${m0.getDate()} ${MOIS[m0.getMonth()]} – ${m1.getDate()} ${MOIS[m1.getMonth()]} ${m1.getFullYear()}`;$('#pick').value=iso(cur);$('#mode').value=mode}
function minuteAt(col,y){const r=col.getBoundingClientRect();let m=H0*60+Math.round(((y-r.top)/PX*60)/15)*15;return Math.max(H0*60,Math.min(H1*60-15,m))}
function addAt(col,y,code){const id=uid();const x={date:col.dataset.d,start:minuteAt(col,y),dur:+$('#dur').value,ssp:code,act:$('#act').value,done:false,score:0,qcm:null,note:'',maj:new Date().toISOString()};S.seances[id]=x;put('seances',id,x);renderAll();openEdit(id)}
function calSay(t){const m=document.getElementById('cq-m');if(m)m.textContent=t}
function calMin(col,y,f){const r=col.getBoundingClientRect(),v=(y-r.top)/PX*4,q=f==='f'?Math.floor(v):f==='c'?Math.ceil(v):Math.round(v);return Math.max(H0*60,Math.min(H1*60,H0*60+q*15))}
function calLab(x){const d=parse(x.date);return JOURS[d.getDay()]+' '+d.getDate()+' '+MOIS[d.getMonth()]+' à '+hm(x.start)}
function lev(a,b){let p=[...Array(b.length+1).keys()];for(let i=1;i<=a.length;i++){const c=[i];for(let j=1;j<=b.length;j++)c[j]=Math.min(p[j]+1,c[j-1]+1,p[j-1]+(a[i-1]===b[j-1]?0:1));p=c}return p[b.length]}
function fzScore(q,s){const c=norm(s[0]),n=norm(s[1]+' '+(GROUPES[s[2]]||'')),cq=q.replace(/\s+/g,'');if(c===cq)return 1000;if(c.startsWith(cq))return 900-c.length;
 const W=n.split(/[^a-z0-9]+/).filter(Boolean);let sc=0;
 for(const t of q.split(/\s+/).filter(Boolean)){const e=t.length>=7?2:1;let v=0;if(c.startsWith(t))v=60;else if(W.includes(t))v=50;else if(W.some(w=>w.startsWith(t)))v=40;else if(n.includes(t))v=25;
  else if(t.length>=4&&W.some(w=>lev(w.slice(0,t.length),t)<=e||lev(w,t)<=e))v=12;if(!v)return 0;sc+=v}
 return sc-n.length/1000}
function fzNotScore(q,c){const T=q.split(/\s+/).filter(Boolean);let b=null;for(const [n,lab,w] of fzNot()[c]){if(!T.every(t=>n.includes(t)))continue;const v=20*T.length+(n.includes(q)?10:0)+w;if(!b||v>b[0])b=[v,lab]}return b}
function fz(q,k){q=norm(String(q).trim()).replace(/\s+/g,' ');if(!q)return [];const why={},R=SSP.map(s=>{const a=fzScore(q,s);if(a>0||q.length<3)return [a,s];const b=fzNotScore(q,s[0]);if(!b)return [0,s];why[s[0]]=b[1];return [b[0],s]}).filter(a=>a[0]>0).sort((a,b)=>b[0]-a[0]).slice(0,k||8).map(a=>a[1]);R.why=why;return R}
function cqRender(){const q=$('#cq').value,R=fz(q),ul=$('#cq-r');if(!q.trim()){ul.hidden=true;ul.innerHTML='';calSay('');return}
 ul.innerHTML=R.map(s=>`<li class="cq-i${sel===s[0]?' on':''}" draggable="true" data-c="${esc(s[0])}"><button class="b cq-p" type="button" data-a="p" title="Placer ce chapitre : cliquez ensuite sur une plage"><code>${esc(s[0])}</code><span>${esc(s[1])}</span>${R.why[s[0]]?`<small>${esc(R.why[s[0]])}</small>`:''}</button><button class="b" type="button" data-a="o" aria-label="Ouvrir ${esc(s[0])}">Ouvrir</button></li>`).join('');
 ul.hidden=!R.length;calSay(R.length?R.length+' résultat'+(R.length>1?'s':'')+' : choisissez « Placer » ou « Ouvrir ».':'Aucun chapitre ne correspond à cette recherche.')}
function cqOpen(code){const L=Object.entries(S.seances).filter(([,x])=>x.ssp===code).sort((a,b)=>(a[1].date+hm(a[1].start))<(b[1].date+hm(b[1].start))?-1:1),t=iso(new Date()),nx=L.find(([,x])=>x.date>=t)||L[L.length-1];
 if(nx){cur=parse(nx[1].date);renderGrid();openEdit(nx[0]);calSay('La séance « '+code+' » du '+calLab(nx[1])+' est ouverte.');return}
 $('#q').value=code;renderList();const it=$('#list .it[data-c="'+code+'"]');if(it){it.scrollIntoView({block:'nearest'});it.focus();tipToggle(it,it,true)}calSay('Ce chapitre n’a encore aucune séance ; sa fiche est ouverte dans la nomenclature.')}
function qpDur(d){const o=$('#qp-d');if(![...o.options].some(x=>+x.value===d)){const n=document.createElement('option');n.value=d;n.textContent=Math.floor(d/60)+' h '+pad(d%60);o.appendChild(n)}o.value=d}
function qpOpen(date,start,dur,code,x,y){const p=$('#qp');start=Math.min(start,H1*60-15);$('#qp-date').value=date;$('#qp-s').value=hm(start);qpDur(Math.max(15,Math.min(dur,H1*60-start)));$('#qp-a').value=$('#act').value;
 qpCode=code||null;$('#qp-q').value=code||'';qpRender();const d=parse(date);$('#qp-h').textContent='Nouvelle séance le '+JOURS[d.getDay()]+' '+d.getDate()+' '+MOIS[d.getMonth()]+' à '+hm(start);
 p.hidden=false;const w=p.offsetWidth,h=p.offsetHeight;let L,T;if(x==null||innerWidth<600){L=(innerWidth-w)/2;T=Math.max(12,innerHeight-h-12)}else{L=Math.min(x+12,innerWidth-w-12);T=Math.min(Math.max(12,y-20),innerHeight-h-12)}
 p.style.left=Math.max(12,L)+'px';p.style.top=Math.max(12,T)+'px';(code?$('#qp-ok'):$('#qp-q')).focus()}
function qpClose(){$('#qp').hidden=true;qpCode=null}
function qpRender(){const q=$('#qp-q').value,R=q.trim()?fz(q,6):[];$('#qp-r').innerHTML=R.map(s=>`<li class="cq-i${qpCode===s[0]?' on':''}" data-c="${esc(s[0])}"><button class="b cq-p" type="button"><code>${esc(s[0])}</code><span>${esc(s[1])}</span></button></li>`).join('');$('#qp-ok').disabled=!qpCode}
function qpCreate(){if(!qpCode||!BY[qpCode])return;const [h,m]=$('#qp-s').value.split(':').map(Number),st=Math.max(H0*60,Math.min(H1*60-15,h*60+Math.round((m||0)/15)*15)),du=Math.max(15,Math.min(+$('#qp-d').value,H1*60-st));
 const id=uid(),x={date:$('#qp-date').value||iso(cur),start:st,dur:du,ssp:qpCode,act:$('#qp-a').value,done:false,score:0,qcm:null,note:'',maj:new Date().toISOString()};
 S.seances[id]=x;put('seances',id,x);qpClose();if(!days().some(d=>iso(d)===x.date))cur=parse(x.date);renderAll();calSay('La séance « '+x.ssp+' » est placée le '+calLab(x)+' pour '+du+' minutes.');const n=$('#grid .blk[data-id="'+id+'"]');if(n)n.focus()}
function calSupp(){calSup=true;setTimeout(()=>{calSup=false},120)}
function calRange(P,y){const cm=calMin(P.c,y,'f');return [Math.min(P.m0,cm),Math.min(H1*60,Math.max(P.m0,cm)+15)]}
function openEdit(id){const x=S.seances[id];if(!x)return;editId=id;const s=BY[x.ssp]||[x.ssp,''];$('#e-t').textContent=s[0]+' · '+s[1]+' — '+x.date;$('#e-start').value=hm(x.start);$('#e-dur').value=x.dur;$('#e-act').value=x.act;$('#e-done').checked=!!x.done;$('#e-score').value=x.score||0;$('#e-sv').textContent=x.score||0;$('#e-qcm').value=x.qcm??'';$('#e-note').value=x.note||'';$('#e-not').innerHTML=NOT[x.ssp]?nBlock(x.ssp,true):'';$('#edit').classList.add('on');$('#edit').scrollIntoView({block:'nearest',behavior:'smooth'})}
function agg(){const per={};SSP.forEach(s=>per[s[0]]={n:0,min:0,ck:0,fp:0,q:[],score:0,last:'',plan:0});
 Object.values(S.seances).forEach(x=>{const p=per[x.ssp];if(!p)return;p.plan++;if(!x.done)return;p.n++;p.min+=x.dur;if(x.act==='Cours CK')p.ck++;if(x.act==='Fondamentaux F′')p.fp++;if(x.qcm!=null)p.q.push(x.qcm);p.score=Math.max(p.score,x.score||0);if(x.date>p.last)p.last=x.date});
 const byDay={};Object.values(S.seances).forEach(x=>{if(x.done)byDay[x.date]=(byDay[x.date]||0)+x.dur});
 const cov=SSP.filter(s=>per[s[0]].ck>0).length,planned=SSP.filter(s=>per[s[0]].plan>0&&!per[s[0]].ck).length;
 const minutes=Object.values(byDay).reduce((a,b)=>a+b,0),seances=Object.values(S.seances).filter(x=>x.done).length;
 const t=new Date();let m14=0;for(let i=0;i<14;i++){const d=new Date(t);d.setDate(t.getDate()-i);m14+=byDay[iso(d)]||0}
 return {per,byDay,cov,planned,minutes,seances,moy14:m14/14}}
function renderKpis(A){const ex=parse(S.params.exam),j=Math.max(0,Math.ceil((ex-new Date())/864e5));
 $('#kpis').innerHTML=[[A.cov+' / 248','SSP couverts (CK lu)'],[Math.round(A.cov/248*100)+' %','couverture'],[(A.minutes/60).toFixed(1)+' h','temps de lecture'],[A.seances,'séances accomplies'],[Math.round(A.moy14)+' min','moyenne/jour (14 j)'],[j,'jours avant le CK']].map(k=>`<div class="kpi"><b>${k[0]}</b><span>${k[1]}</span></div>`).join('')}
function ring(p,label){const r=34,c=2*Math.PI*r;return `<div class="ring"><svg width="92" height="92" viewBox="0 0 92 92" role="img" aria-label="${esc(label)} ${p} %"><circle cx="46" cy="46" r="${r}" fill="none" stroke="var(--line)" stroke-width="9"/>${p>0?`<circle cx="46" cy="46" r="${r}" fill="none" stroke="var(--gold)" stroke-width="9" stroke-linecap="round" stroke-dasharray="${c*p/100} ${c}" transform="rotate(-90 46 46)"/>`:''}<text x="46" y="51" text-anchor="middle" style="font:600 15px var(--fm);fill:var(--ink)">${p}%</text></svg>${esc(label)}</div>`}
function renderVit(A){const fam={G:[0,0],S:[0,0],F:[0,0],O:[0,0]};SSP.forEach(s=>{const f=s[2][0];fam[f][1]++;if(A.per[s[0]].ck)fam[f][0]++});
 $('#fams').innerHTML=ring(Math.round(A.cov/248*100),'Total · 248 SSP')+Object.entries(fam).map(([k,v])=>ring(Math.round(v[0]/v[1]*100),FAM[k]+' · '+v[0]+'/'+v[1])).join('');
 $('#gauges').innerHTML=Object.entries(GROUPES).map(([k,v])=>{const L=SSP.filter(s=>s[2]===k),c=L.filter(s=>A.per[s[0]].ck).length,pl=L.filter(s=>A.per[s[0]].plan&&!A.per[s[0]].ck).length,p=c/L.length*100,q=pl/L.length*100;return `<div class="g"><div class="lab"><span>${k} · ${esc(v)}</span><b>${c}/${L.length}</b></div><div class="bar"><i class="a" style="width:${p}%"></i><i class="b" style="width:${q}%"></i></div></div>`}).join('');
 // courbe : 60 derniers jours
 const N=60,t=new Date(),pts=[],bars=[];const first={};Object.values(S.seances).forEach(x=>{if(x.done&&x.act==='Cours CK'&&(!first[x.ssp]||x.date<first[x.ssp]))first[x.ssp]=x.date});
 for(let i=N-1;i>=0;i--){const d=new Date(t);d.setDate(t.getDate()-i);const k=iso(d);pts.push(Object.values(first).filter(f=>f<=k).length);bars.push(A.byDay[k]||0)}
 const Wd=720,Hd=220,pl=40,pr=40,pt=12,pb=26,iw=Wd-pl-pr,ih=Hd-pt-pb,ymax=Math.max(10,Math.ceil(Math.max(...pts)/10)*10),bmax=Math.max(60,Math.ceil(Math.max(...bars)/60)*60);
 const X=i=>pl+i*(iw/(N-1)),Y=v=>pt+ih-v/ymax*ih,YB=v=>pt+ih-v/bmax*ih;let s=`<svg viewBox="0 0 ${Wd} ${Hd}" width="100%" role="img" aria-label="Courbe de progression sur 60 jours">`;
 for(let k=0;k<=4;k++){const y=pt+ih*k/4;s+=`<line x1="${pl}" x2="${Wd-pr}" y1="${y}" y2="${y}" stroke="var(--grid)"/><text x="${pl-6}" y="${y+4}" text-anchor="end">${Math.round(ymax*(1-k/4))}</text><text x="${Wd-pr+6}" y="${y+4}">${Math.round(bmax*(1-k/4))}′</text>`}
 bars.forEach((b,i)=>{if(b)s+=`<rect x="${X(i)-3}" y="${YB(b)}" width="6" height="${pt+ih-YB(b)}" rx="1.5" fill="var(--ok)" opacity=".75"/>`});
 s+=`<path d="${pts.map((v,i)=>(i?'L':'M')+X(i).toFixed(1)+' '+Y(v).toFixed(1)).join('')} L${X(N-1)} ${pt+ih} L${X(0)} ${pt+ih}Z" fill="var(--gold2)" opacity=".18"/><path d="${pts.map((v,i)=>(i?'L':'M')+X(i).toFixed(1)+' '+Y(v).toFixed(1)).join('')}" fill="none" stroke="var(--gold)" stroke-width="2.2"/><circle cx="${X(N-1)}" cy="${Y(pts[N-1])}" r="4" fill="var(--gold)"/>`;
 [0,15,30,45,59].forEach(i=>{const d=new Date(t);d.setDate(t.getDate()-(N-1-i));s+=`<text x="${X(i)}" y="${Hd-6}" text-anchor="middle">${d.getDate()} ${MOIS[d.getMonth()]}</text>`});
 $('#curve').innerHTML=s+'</svg>';
 const m=monday(t);m.setDate(m.getDate()-15*7);let hh='';for(let i=0;i<16*7;i++){const d=new Date(m);d.setDate(m.getDate()+i);const v=A.byDay[iso(d)]||0,a=v?Math.min(1,.25+v/240):0;hh+=`<i title="${iso(d)} · ${v} min" style="${v?`background:color-mix(in srgb,var(--ok) ${Math.round(a*100)}%,var(--line))`:''}"></i>`}$('#heat').innerHTML=hh;
 const q=norm(($('#q2').value||'').trim());$('#tssp').innerHTML=SSP.filter(s=>!q||norm(s[0]+' '+s[1]).includes(q)).map(s=>{const p=A.per[s[0]],qm=p.q.length?Math.round(p.q.reduce((a,b)=>a+b,0)/p.q.length):'—';return `<tr><td><code>${s[0]}</code></td><td>${esc(s[1])}</td><td class="n">${p.n}</td><td class="n">${p.min}</td><td class="n">${p.ck}</td><td class="n">${p.fp}</td><td class="n">${qm}</td><td class="n">${p.score||'—'}</td><td>${p.last||'—'}</td></tr>`}).join('')}
function renderCalc(A){$('#p-exam').value=S.params.exam;$('#p-obj').value=S.params.obj;$('#p-pass').value=S.params.pass;
 const ex=parse(S.params.exam),today=new Date();today.setHours(0,0,0,0);const jours=Math.max(0,Math.round((ex-today)/864e5));const visees=248*S.params.pass;const faits=SSP.reduce((a,s)=>a+Math.min(S.params.pass,A.per[s[0]].ck),0);const restants=visees-faits;
 const minParSSP=A.cov?A.minutes/A.cov:null;const besoin=jours?restants/jours:null;const rythme=A.moy14&&minParSSP?A.moy14/minParSSP:0;
 const fin=rythme>0?new Date(today.getTime()+restants/rythme*864e5):null;const objMin=minParSSP?restants*minParSSP:null;
 VARS={couverts:A.cov,restants,jours,minutes:A.minutes,seances:A.seances,moyenne14:A.moy14,objectif:S.params.obj};
 const R=[["Passages SSP visés (248 × "+S.params.pass+")",visees],["Passages réalisés",faits],["Passages restants",restants],["Jours restants avant le CK",jours],["Passages nécessaires par jour",besoin==null?'—':besoin.toFixed(2)],["Durée moyenne observée par SSP couvert",minParSSP?Math.round(minParSSP)+' min':'— (aucune donnée)'],["Rythme actuel (14 j)",rythme?rythme.toFixed(2)+' SSP/jour':'—'],["Date de fin projetée au rythme actuel",fin?fin.toLocaleDateString('fr-CH'):'—'],["Marge avant le CK",fin?Math.round((ex-fin)/864e5)+' jours':'—'],["Temps de lecture restant estimé",objMin?(objMin/60).toFixed(1)+' h':'—'],["Minutes/jour nécessaires",objMin&&jours?Math.round(objMin/jours)+' min':'—'],["Objectif quotidien déclaré",S.params.obj+' min'],["Écart moyenne 14 j / objectif",Math.round(A.moy14-S.params.obj)+' min']];
 $('#calc').innerHTML=R.map(r=>`<tr><td>${esc(r[0])}</td><td class="n">${esc(r[1])}</td></tr>`).join('')}
function exiMig(){const x=S.exi||(S.exi={});if(x._m27)return false;let any=false;EXI.items.forEach(it=>(it.m||[]).forEach(k=>{if(k in x){any=true;if(x[k]&&!('x:'+it.id in x))x['x:'+it.id]=true}}));if(any)x._m27=1;return any}
function exiBanner(){const I=SESSION.inscription,P=SESSION.precedente,d0=new Date(I.debut+'T00:00:00'),d1=new Date(I.fin+'T23:59:59'),now=new Date(),j=t=>Math.ceil((t-now)/864e5);
 const cd=now<d0?'L’inscription ouvre dans '+j(d0)+' jours, le '+fdt(I.debut)+'.':now<=d1?'L’inscription se ferme dans '+j(d1)+' jours, le '+fdt(I.fin)+'.':'La période d’inscription 2027 est close depuis le '+fdt(I.fin)+'.';
 return '<p><b>La session '+P.annee+' est terminée</b> : le CK a eu lieu les '+fdt(P.ck[0])+' et '+fdt(P.ck[1])+', et le CS du '+fdt(P.cs[0])+' au '+fdt(P.cs[1])+' (<a href="'+P.url+'" target="_blank" rel="noopener">'+esc(P.ref)+'</a>).</p>'
 +'<p>L’inscription à l’examen '+SESSION.annee+' est ouverte du <b>'+fdt(I.debut)+'</b> au <b>'+fdt(I.fin)+'</b> (<a href="'+I.url+'" target="_blank" rel="noopener">'+esc(I.source)+'</a>). <span class="cd" id="exi-cd">'+cd+'</span></p>'
 +'<p>Le CK aurait lieu les '+fdt(SESSION.ck.dates[0])+' et '+fdt(SESSION.ck.dates[1])+', et le CS entre le '+fdt(SESSION.cs.debut)+' et le '+fdt(SESSION.cs.fin)+' ; ces dates sont <b>à confirmer</b>, car seule une <a href="'+SESSION.dates_source.url+'" target="_blank" rel="noopener">source facultaire</a> les annonce et l’OFSP ne les a pas publiées. <span class="exi-vb">À vérifier auprès de la MEBEKO</span></p>'}
function renderExi(){if(exiMig())put('reglages','exigences',S.exi);const x=S.exi;$('#exi-bn').innerHTML=exiBanner();
 $('#exi').innerHTML=Object.entries(EXI.groupes).map(([g,lab])=>{const L=EXI.items.filter(it=>it.g===g);return '<fieldset><legend>'+esc(lab)+' <small>('+L.filter(it=>x['x:'+it.id]).length+'/'+L.length+')</small></legend>'+L.map(it=>`<label class="chk" data-s="${it.s}"><input type="checkbox" id="exi-${it.id}" data-x="${it.id}" ${x['x:'+it.id]?'checked':''}><span><b>${it.id}</b> · ${esc(it.t)}${it.s==='a_verifier'?'<span class="exi-vb">À vérifier auprès de la MEBEKO</span>':''}${it.n?'<span class="exi-n">'+esc(it.n)+'</span>':''}</span><small>Source officielle : <a href="${it.u}" target="_blank" rel="noopener">${esc(it.r)}</a>${it.e?' · Échéance : '+fdt(it.e):''}</small></label>`).join('')+'</fieldset>'}).join('');
 const n=EXI.items.filter(it=>x['x:'+it.id]).length,v=EXI.items.filter(it=>it.s==='a_verifier').length;$('#exi-c').textContent=n+' points sur '+EXI.items.length+' sont cochés ; '+v+' points restent à vérifier auprès de la MEBEKO (sources lues le '+fdt(EXI.lu)+').'}
function applyDisp(){const d=S.params.disp||{};document.documentElement.style.setProperty('--gilt',(d.gilt??0)/100);document.documentElement.style.setProperty('--fs',(d.fs??100)+'%');$('#d-gilt').value=d.gilt??0;$('#d-fs').value=d.fs??100;$('#d-gv').textContent=(d.gilt??0)+' %';$('#d-fv').textContent=(d.fs??100)+' %'}
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
function M(){return Object.assign({},MDEF,S.params.memo||{})}
function ints(){return (M().int||'1,3,7,21,60').split(/[,;\s]+/).map(Number).filter(n=>n>0)}
function memoState(){const m=M(),I=ints(),out={};const byS={};Object.values(S.seances).filter(x=>x.done).sort((a,b)=>a.date<b.date?-1:1).forEach(x=>{(byS[x.ssp]=byS[x.ssp]||[]).push(x)});
 for(const [c,L] of Object.entries(byS)){let box=0,ef=2.5,iv=0,n=0;for(const x of L){const q=x.score||0;if(m.meth==='sm2'){if(q<3){n=0;iv=1}else{n++;iv=n===1?1:n===2?6:Math.round(iv*ef)}ef=Math.max(1.3,ef+(0.1-(5-q)*(0.08+(5-q)*0.02)))}else{box=q>=3?Math.min(I.length-1,box+(L.indexOf(x)?1:0)):0;iv=m.meth==='leitner'?[1,3,7,21,60][Math.min(box,4)]:I[Math.min(box,I.length-1)]}}
  const last=L[L.length-1].date,nd=parse(last);nd.setDate(nd.getDate()+iv);const t=(new Date()-parse(last))/864e5;out[c]={last,next:iso(nd),iv,box,ef,n:L.length,R:Math.exp(-Math.max(0,t)/Math.max(1,iv*1.5))}}
 return out}
function renderMemo(){const m=M();$$('input[name="m-meth"]').forEach(r=>r.checked=r.value===m.meth);$('#m-int').value=m.int;['rappel','test','inter','feyn','retro','reap'].forEach(k=>$('#m-'+k).checked=!!m[k]);memOpt();memCons(m);if(!$('#v-memo').hidden)memEv();$('#m-ret').value=m.ret;$('#m-max').value=m.max;$('#m-hor').value=m.hor;
 const st=memoState(),t=iso(new Date());const due=Object.entries(st).filter(([,v])=>v.next<=t).sort((a,b)=>a[1].next<b[1].next?-1:1);const late=due.filter(([,v])=>v.next<t).length;
 const Rm=Object.values(st).length?Object.values(st).reduce((a,v)=>a+v.R,0)/Object.values(st).length:0;
 $('#m-kpi').innerHTML=[[due.length,'à réviser aujourd’hui'],[late,'en retard'],[Object.keys(st).length,'SSP en mémorisation'],[Math.round(Rm*100)+' %','rétention estimée (cible '+m.ret+' %)']].map(k=>`<div class="kpi"><b>${k[0]}</b><span>${k[1]}</span></div>`).join('');
 $('#m-due').innerHTML=due.slice(0,m.max).map(([c,v])=>`<div class="r" data-t="s|${c}"><code>${c}</code><span>${esc((BY[c]||[c,''])[1])}<br><small class="st">dernier passage ${v.last} · intervalle ${v.iv} j · ${v.n} passage(s)</small></span><span class="${v.next<t?'late':''}">${v.next<t?'retard':'aujourd’hui'}</span><button class="b" data-plan="${c}">Planifier</button></div>`).join('')||'<p class="st">Rien à réviser aujourd’hui. Les SSP lus apparaîtront ici à leur échéance.</p>';
 const N=30,cnt=[...Array(N)].map((_,i)=>{const d=new Date();d.setDate(d.getDate()+i);const k=iso(d);return Object.values(st).filter(v=>i?v.next===k:v.next<=k).length});const mx=Math.max(4,...cnt),W=720,H=150,pl=30,pb=22,bw=(W-pl-10)/N;
 let s=`<svg viewBox="0 0 ${W} ${H}" width="100%" role="img" aria-label="Révisions prévues sur 30 jours">`;[0,.5,1].forEach(f=>{const y=10+(H-pb-10)*(1-f);s+=`<line x1="${pl}" x2="${W-10}" y1="${y}" y2="${y}" stroke="var(--grid)"/><text x="${pl-5}" y="${y+4}" text-anchor="end">${Math.round(mx*f)}</text>`});
 cnt.forEach((v,i)=>{const h=(H-pb-10)*v/mx;s+=`<rect x="${pl+i*bw+1}" y="${H-pb-h}" width="${bw-2}" height="${h}" rx="2" fill="${v>m.max?'var(--bad)':'var(--gold)'}"/>`;if(i%5===0){const d=new Date();d.setDate(d.getDate()+i);s+=`<text x="${pl+i*bw+bw/2}" y="${H-6}" text-anchor="middle">${d.getDate()}/${d.getMonth()+1}</text>`}});$('#m-load').innerHTML=s+'</svg>';
 const mo={};const first={};Object.values(S.seances).filter(x=>x.done).sort((a,b)=>a.date<b.date?-1:1).forEach(x=>{const k=x.date.slice(0,7);const o=mo[k]=mo[k]||{n:0,min:0,neu:0,rev:0,sc:[]};o.n++;o.min+=x.dur;if(!first[x.ssp]){first[x.ssp]=1;o.neu++}else o.rev++;if(x.score)o.sc.push(x.score)});
 const now=new Date();let rows='';for(let i=0;i<m.hor;i++){const d=new Date(now.getFullYear(),now.getMonth()-i,1);const k=d.getFullYear()+'-'+pad(d.getMonth()+1);const o=mo[k]||{n:0,min:0,neu:0,rev:0,sc:[]};rows+=`<tr><td>${MOIS[d.getMonth()]} ${d.getFullYear()}</td><td class="n">${o.n}</td><td class="n">${(o.min/60).toFixed(1)}</td><td class="n">${o.neu}</td><td class="n">${o.rev}</td><td class="n">${o.sc.length?(o.sc.reduce((a,b)=>a+b,0)/o.sc.length).toFixed(1):'—'}</td></tr>`}$('#m-month').innerHTML=rows}
function renderCSPlan(){const x=S.exi||{};$('#cs-plan').innerHTML=CSPLAN.map((p,i)=>`<fieldset><legend>${esc(p[0])}</legend>${p[1].split('|').map((t,j)=>`<label><input type="checkbox" data-cp="cp${i}_${j}" ${x['cp'+i+'_'+j]?'checked':''}><span>${esc(t)}</span></label>`).join('')}</fieldset>`).join('')}
function renderPicks(){$('#cs-picks').innerHTML=picks.map(c=>`<button data-x="${c}" title="Retirer">${c} · ${esc(BY[c][1])} ✕</button>`).join('')}
function scenario(){if(!picks.length)return 'Choisissez au moins un SSP.';const L=picks.map(c=>`- ${c} — ${BY[c][1]} (groupe ${BY[c][2]} : ${GROUPES[BY[c][2]]})`).join('\n');const task=$('#cs-task').value,dur=+$('#cs-dur').value||13,circ=$('#cs-fmt').value==='n'&&picks.length>1,sansPS=task.startsWith('Présentation');
 return `RÔLE ET MISSION
Tu animes une simulation de l’épreuve CS (Clinical Skills) de l’examen fédéral suisse de médecine humaine. Je suis le candidat ou la candidate. Tu joues successivement trois rôles distincts, toujours annoncés :
[LECTEUR] lit la consigne affichée à la porte de la station et, s’il existe, le dossier médical préalable. Voix neutre, posée, factuelle.
[PATIENT] est un patient standardisé (PS) : il ne répond qu’à ce qui est demandé, ne livre jamais spontanément le diagnostic, reste cohérent du début à la fin et exprime une émotion crédible. Voix naturelle, propre à son âge et à son état, avec hésitations et intonations.
[EXAMINATEUR] observe en silence, tient le temps, annonce « il reste 2 minutes », puis pose les questions prévues et procède à l’évaluation. Voix formelle et brève.
Si tu disposes d’un mode vocal, utilise trois voix ou intonations nettement différentes pour ces trois rôles. En mode texte, préfixe chaque réplique par la balise du rôle et indique le ton entre crochets, par exemple [PATIENT · inquiet].

SITUATIONS DE DÉPART (PROFILES 2023)
${L}
${circ?`Format : un circuit de ${picks.length} stations, une par SSP, enchaînées dans cet ordre, chacune de ${dur} minutes.`:`Format : une seule station de ${dur} minutes qui intègre ${picks.length>1?'ces SSP dans un même cas clinique cohérent':'ce SSP'}.`}
Tâche demandée au candidat : ${task}.
Dimensions du blueprint : affection ${$('#cs-cond').value} ; cadre : ${$('#cs-set').value} ; difficulté ${$('#cs-diff').value}.
Patient : ${$('#cs-pat').value.trim()||'âge, sexe et contexte de vie au choix, réalistes pour la Suisse'} ; émotion dominante : ${$('#cs-emo').value}${$('#cs-lang').checked?' ; barrière linguistique, avec ou sans interprète':''}.

CADRE OFFICIEL À RESPECTER (OFSP, Exigences MED 2026, § 3.2 et § 5.1.4)
- Parcours réel : 11 stations, au moins 10 avec patient standardisé ; tâches d’anamnèse, de status, de management et de communication ; compte rendu oral ou écrit possible ; l’examinateur peut poser des questions ; aucun feed-back pendant l’épreuve.
- Domaine ASM : critères spécifiques au cas ; seuls les gestes et mesures corrects rapportent des points ; aucun point négatif.
- Domaine KK : 4 dimensions notées de 1 à 5 : (1) écoute des sentiments et des besoins ; (2) structure de l’entretien ; (3) expression verbale ; (4) expression non verbale.${sansPS?' Station sans PS : seules les dimensions 2 et 3 sont évaluées.':''}
- Contenu médical aligné sur les recommandations suisses (sociétés suisses, OFSP, information professionnelle Swissmedic), puis européennes ; contexte suisse (système de santé, unités SI).

DÉROULEMENT
1. [LECTEUR] lit la consigne de porte : nom, âge, motif, cadre, tâche exacte, temps imparti. Puis attends que j’écrive « J’entre ».
2. Station en temps réel : je mène l’entretien ; tu réponds en [PATIENT]. Si je décris un geste d’examen clinique, réponds en [EXAMINATEUR] avec le résultat objectif de ce geste, et seulement de celui-ci.
3. À la fin du temps, ou quand j’écris « Fin », [EXAMINATEUR] pose 1 à 3 questions de synthèse (diagnostic différentiel, examens, prise en charge).
4. Seulement après la station (simulation pédagogique, contrairement à l’examen réel) : grille ASM détaillée (critères attendus, obtenus ou manqués, pourcentage), notes KK 1 à 5 justifiées, les 3 erreurs les plus coûteuses, une phrase modèle pour chacune, et la recommandation suisse ou européenne de référence.
5. Termine OBLIGATOIREMENT ton évaluation par le bloc ci-dessous, que je collerai dans mon organigramme. Écris exactement la ligne MEDORA-RESULTAT, puis un objet JSON valide sur une seule ligne, puis la ligne FIN-MEDORA, sans rien d’autre entre ces deux lignes :
MEDORA-RESULTAT
{"date":"${iso(new Date())}","ssp":${JSON.stringify(picks)},"tache":"${task}","asm":0,"kk":[0,0,0,0],"note_globale":0,"criteres_obtenus":["…"],"criteres_manques":["…"],"erreurs":["…","…","…"],"commentaire":"…"}
FIN-MEDORA
Règles du bloc : asm = pourcentage des critères ASM obtenus (0 à 100) ; kk = les 4 notes de 1 à 5 dans l’ordre écoute, structure, expression verbale, non verbal, avec null pour une dimension non évaluée${sansPS?' (ici : null pour écoute et non verbal)':''} ; note_globale = 0,75 × asm + 0,25 × ((moyenne KK − 1) ÷ 4 × 100), arrondie (pondération ASM 75 % · KK 25 %, OFSP, Exigences MED 2026, § 5.1.3 e) ; commentaire = 3 à 5 phrases qui justifient la note et nomment la priorité de travail. Guillemets droits uniquement.
6. Propose ensuite de rejouer la station avec une variante (autre émotion, autre cadre, complication).

Ne révèle jamais le diagnostic, la grille ni les critères avant la fin. Commence maintenant par l’étape 1.`}
function selOut(){const r=document.createRange();r.selectNodeContents($('#cs-out'));const s=getSelection();s.removeAllRanges();s.addRange(r);$('#cs-st').textContent='Texte sélectionné : copiez-le.'}
function renderCSLog(){const L=Object.values(CSLOG).sort((a,b)=>a.date<b.date?-1:1);const kkm=x=>{const v=(x.kk||[]).filter(Boolean);return v.length?v.reduce((a,b)=>a+b,0)/v.length:null};
 $('#cr-list').innerHTML=L.slice().reverse().map(x=>`<tr><td>${x.date}</td><td>${esc((x.ssp||[]).join(', '))}</td><td>${esc(x.task)}${x.src?' <small class="st">· IA</small>':''}</td><td class="n"><b>${glob(x)??'—'}</b></td><td class="n">${x.asm??'—'}</td><td class="n">${kkm(x)?kkm(x).toFixed(1):'—'}</td><td>${esc(x.note||'')}</td></tr>`).join('')||'<tr><td colspan="7" class="st">Aucune simulation consignée.</td></tr>';
 if(L.length<2){$('#cr-chart').innerHTML='';return}const W=720,H=170,pl=36,pr=36,pt=10,pb=22,X=i=>pl+i*((W-pl-pr)/(L.length-1));let s=`<svg viewBox="0 0 ${W} ${H}" width="100%" role="img" aria-label="Progression ASM et KK">`;[0,.5,1].forEach(f=>{const y=pt+(H-pt-pb)*(1-f);s+=`<line x1="${pl}" x2="${W-pr}" y1="${y}" y2="${y}" stroke="var(--grid)"/><text x="${pl-5}" y="${y+4}" text-anchor="end">${100*f}%</text><text x="${W-pr+5}" y="${y+4}">${(1+4*f).toFixed(0)}</text>`});
 const pa=L.map((x,i)=>x.asm==null?null:[X(i),pt+(H-pt-pb)*(1-x.asm/100)]).filter(Boolean),pk=L.map((x,i)=>kkm(x)==null?null:[X(i),pt+(H-pt-pb)*(1-(kkm(x)-1)/4)]).filter(Boolean);
 if(pa.length)s+=`<path d="${pa.map((p,i)=>(i?'L':'M')+p[0]+' '+p[1]).join('')}" fill="none" stroke="var(--gold)" stroke-width="2.2"/>`;if(pk.length)s+=`<path d="${pk.map((p,i)=>(i?'L':'M')+p[0]+' '+p[1]).join('')}" fill="none" stroke="var(--c6)" stroke-width="2.2" stroke-dasharray="5 4"/>`;
 $('#cr-chart').innerHTML=s+'</svg><div class="legend"><span><i style="background:var(--gold)"></i>ASM %</span><span><i style="background:var(--c6)"></i>KK moyen (1–5)</span></div>'}
function renderAtt(){const x=S.exi||{};$('#att').innerHTML=ATT.map((b,i)=>`<fieldset><legend>${esc(b[0])}</legend>${b[1].map((r,j)=>`<label class="chk"><input type="checkbox" data-at="a${i}_${j}" ${x['a'+i+'_'+j]?'checked':''}><span><b>${esc(r[0])}</b> — ${esc(r[1])}</span><small>Source : <a href="${OFSP26}" target="_blank" rel="noopener">OFSP, Exigences MED 2026, ${esc(r[2])}</a></small></label>`).join('')}</fieldset>`).join('')}
function nGet(c){return NS[c]||(NS[c]={m:{},a:{},add:[],h:{}})}
function notList(c){const N=NOT[c]||[[],[]],x=NS[c]||{},o=[];
 CLIN.forEach((t,i)=>o.push({k:'c'+i,s:'1 · Cours clinique, dans l’ordre',t}));
 (PRV[c]?PRV[c].map(x=>x[0]):N[0].map((t,i)=>i)).forEach(i=>o.push({k:'d'+i,s:'2 · Diagnostics différentiels',t:N[0][i],pv:pvSpan(c,i)}));
 N[1].forEach((n,i)=>o.push({k:'f'+i,s:'3 · Fondamentaux F′',t:n[1],sub:n[0]}));
 (x.add||[]).forEach(n=>o.push({k:n[0],s:'4 · Mes notions',t:n[1]}));return o}
function nStat(c){const L=notList(c),m=(NS[c]||{}).m||{},a=(NS[c]||{}).a||{};let sum=0,ok=0,ab=0;L.forEach(n=>{const v=m[n.k]||0;sum+=v;if(v>=95)ok++;if(v>0||a[n.k])ab++});return {n:L.length,sum,ok,ab,moy:L.length?sum/L.length:0}}
function nSave(c){const x=nGet(c),st=nStat(c);x.h[iso(new Date())]=[Math.round(st.sum),st.ok,st.n];x.maj=new Date().toISOString();lsSet('orga-not',JSON.stringify(NS));clearTimeout(nTimer[c]);nTimer[c]=setTimeout(()=>put('notions',c,x),700)}
function nRow(c,n){const x=NS[c]||{},v=(x.m||{})[n.k]||0,a=v>0||!!(x.a||{})[n.k];return `<div class="nr${v>=95?' ok':''}" style="--pc:${pcol(v)}" data-c="${c}" data-k="${esc(n.k)}" data-t="n|${c}|${esc(n.k)}"><input type="checkbox" ${a?'checked':''} aria-label="Notion abordée"><span>${n.k[0]!=='u'?`<span class="tw" tabindex="0" role="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="tip">${esc(n.t)}</span>`:esc(n.t)}${n.k[0]!=='u'?'<button class="ti" style="width:24px;height:24px;min-width:24px;min-height:24px" aria-label="L’essentiel pour 100 % des points">i</button>':''}${n.pv||''}${n.sub?`<small>${esc(n.sub)}</small>`:''}${n.k[0]==='u'?'<button class="x" data-x>retirer</button>':''}</span><input type="range" min="0" max="100" step="5" value="${v}" aria-label="Maîtrise de la notion"><b>${v} %</b></div>`}
function nBlock(c,compact){const s=BY[c];if(!s)return '';if(PRV[c]&&typeof ckLoad==='function'){ckLoad('prev').catch(()=>{});ckLoad('src').catch(()=>{})}const L=notList(c),st=nStat(c),todo=NTODO&&!compact,secs={};L.forEach(n=>(secs[n.s]=secs[n.s]||[]).push(n));
 const pOk=st.n?st.ok/st.n*100:0,pMoy=st.moy;
 let h=`<div class="row" style="justify-content:space-between"><h3><code style="color:var(--gold);font-family:var(--fm)">${s[0]}</code> ${esc(s[1])}</h3>${compact?`<button class="b" data-open="${s[0]}">Ouvrir dans Notions CK</button>`:''}</div>
 <div class="pbar" title="Notions à 95 % ou plus, puis maîtrise moyenne"><i style="width:${pOk}%;background:var(--ok)"></i><i style="width:${Math.max(0,pMoy-pOk)}%;background:var(--gold2)"></i></div>
 <p class="st">${st.n} notions · ${st.ab} abordées · <b style="color:var(--ok)">${st.ok} à 95 % ou plus</b> · maîtrise moyenne ${pMoy.toFixed(0)} %${st.ok===st.n&&st.n?' · SSP maîtrisé':''}</p>`;
 Object.keys(secs).sort().forEach((k,i)=>{let R=secs[k];if(todo)R=R.filter(n=>((NS[c]||{}).m||{})[n.k]<95||!((NS[c]||{}).m||{})[n.k]);const ok=secs[k].filter(n=>(((NS[c]||{}).m||{})[n.k]||0)>=95).length;
  h+=`<details ${!compact||i===0?'open':''}><summary class="nsec"><span>${esc(k)}</span><span data-tot="${secs[k].length}" data-ok0="${ok-R.filter(n=>(((NS[c]||{}).m||{})[n.k]||0)>=95).length}">${ok}/${secs[k].length}</span></summary><div class="nl">${k[0]==='2'&&R.length?PV_LEG:''}${R.map(n=>nRow(c,n)).join('')||'<p class="st">Rien à travailler ici.</p>'}</div></details>`});
 if(!compact)h+=`<div class="row" style="margin-top:10px"><input id="n-new" placeholder="Ajouter une notion à ce SSP" style="flex:1;min-width:200px"><button class="b p" id="n-add">Ajouter</button></div>`;
 return h}
function nWire(box){box.addEventListener('input',e=>{const r=e.target.closest('.nr');if(!r||e.target.type!=='range')return;const v=+e.target.value;r.style.setProperty('--pc',pcol(v));r.querySelector('b').textContent=v+' %';r.classList.toggle('ok',v>=95)});
 box.addEventListener('change',e=>{const r=e.target.closest('.nr');if(!r)return;const c=r.dataset.c,k=r.dataset.k,x=nGet(c);const rg=r.querySelector('input[type=range]'),cb=r.querySelector('input[type=checkbox]');if(e.target===rg){x.m[k]=+rg.value;if(+rg.value>0){x.a[k]=1;cb.checked=true}}else if(e.target===cb){if(cb.checked)x.a[k]=1;else{delete x.a[k];delete x.m[k];rg.value=0}}const v=x.m[k]||0;r.style.setProperty('--pc',pcol(v));r.querySelector('b').textContent=v+' %';r.classList.toggle('ok',v>=95);nSave(c);renderNotSoft(box)});
 box.addEventListener('click',e=>{const o=e.target.closest('[data-open]');if(o){NSEL=o.dataset.open;$$('.tab').find(t=>t.dataset.v==='not').click();renderNot();return}
  if(e.target.matches('[data-x]')){const r=e.target.closest('.nr'),x=nGet(r.dataset.c);x.add=x.add.filter(n=>n[0]!==r.dataset.k);delete x.m[r.dataset.k];delete x.a[r.dataset.k];nSave(r.dataset.c);renderNot();return}
  if(e.target.id==='n-add'){const t=$('#n-new').value.trim();if(!t||!NSEL)return;nGet(NSEL).add.push(['u'+uid().slice(0,10),t.slice(0,300)]);nSave(NSEL);renderNot()}})}
function renderNotSoft(box){box.querySelectorAll('details').forEach(d=>{const s=d.querySelector('[data-tot]');if(s)s.textContent=(+s.dataset.ok0+d.querySelectorAll('.nr.ok').length)+'/'+s.dataset.tot});if(box.id!=='e-not'){const sc=$('#n-list').scrollTop;renderNList();$('#n-list').scrollTop=sc}if(box.id==='e-not'){renderNotStats()}else{const y=scrollY;renderNotStats();const st=nStat(NSEL);const p=box.querySelector('.pbar');if(p){p.children[0].style.width=(st.ok/st.n*100)+'%';p.children[1].style.width=Math.max(0,st.moy-st.ok/st.n*100)+'%';box.querySelector('p.st').innerHTML=`${st.n} notions · ${st.ab} abordées · <b style="color:var(--ok)">${st.ok} à 95 % ou plus</b> · maîtrise moyenne ${st.moy.toFixed(0)} %`}scrollTo(0,y)}}
function nGlobal(){let n=0,sum=0,ok=0,ab=0,full=0,touched=0;const G={};SSP.forEach(s=>{const t=nStat(s[0]);n+=t.n;sum+=t.sum;ok+=t.ok;ab+=t.ab;if(t.n&&t.ok===t.n)full++;if(t.ab)touched++;const g=G[s[2]]||(G[s[2]]={n:0,sum:0,ok:0});g.n+=t.n;g.sum+=t.sum;g.ok+=t.ok});return {n,sum,ok,ab,full,touched,G}}
function renderNotStats(){const T=nGlobal();
 $('#n-kpi').innerHTML=[[T.n.toLocaleString('fr-CH'),'notions au programme'],[T.ab.toLocaleString('fr-CH'),'notions abordées'],[T.ok.toLocaleString('fr-CH'),'notions à 95 % ou plus'],[(T.n?T.sum/T.n:0).toFixed(1)+' %','maîtrise moyenne globale'],[T.touched+' / 248','SSP entamés'],[T.full+' / 248','SSP maîtrisés (tout ≥ 95 %)']].map(k=>`<div class="kpi"><b>${k[0]}</b><span>${k[1]}</span></div>`).join('');
 $('#n-grp').innerHTML=GKEYS.map((g,i)=>{const x=T.G[g]||{n:0,sum:0,ok:0},m=x.n?x.sum/x.n:0,o=x.n?x.ok/x.n*100:0;return `<div class="g"><div class="lab"><span>${g} · ${esc(GROUPES[g])}</span><b>${m.toFixed(0)} %</b></div><div class="bar"><i class="a" style="width:${o}%"></i><i class="b" style="width:${Math.max(0,m-o)}%"></i></div></div>`}).join('');
 const bins=[0,0,0,0,0],lab=['1–24 %','25–49 %','50–74 %','75–94 %','95–100 %'],colr=['var(--bad)','var(--warn)','var(--gold2)','var(--gold)','var(--ok)'];SSP.forEach(s=>{const x=NS[s[0]];if(!x)return;notList(s[0]).forEach(n=>{const v=(x.m||{})[n.k]||0;if(v>0)bins[v>=95?4:v>=75?3:v>=50?2:v>=25?1:0]++})});const mx=Math.max(1,...bins);
 let d=`<svg viewBox="0 0 720 150" width="100%" role="img" aria-label="Répartition des notions par niveau de maîtrise">`;bins.forEach((v,i)=>{const w=120,x=40+i*136,h=88*v/mx;d+=`<rect x="${x}" y="${110-h}" width="${w}" height="${h}" rx="6" fill="${colr[i]}"/><text x="${x+w/2}" y="${104-h}" text-anchor="middle">${v}</text><text x="${x+w/2}" y="132" text-anchor="middle">${lab[i]}</text>`});$('#n-dist').innerHTML=d+'</svg>';
 const days=new Set();SSP.forEach(s=>Object.keys((NS[s[0]]||{}).h||{}).forEach(k=>days.add(k)));const D=[...days].sort().slice(-90);
 if(D.length<1){$('#n-curve').innerHTML='<p class="st">La courbe apparaît dès la première notion évaluée.</p>';return}
 const pts=D.map(day=>{let sum=0,ok=0;SSP.forEach(s=>{const h=(NS[s[0]]||{}).h||{};const ks=Object.keys(h).filter(k=>k<=day).sort();if(ks.length){const v=h[ks[ks.length-1]];sum+=v[0];ok+=v[1]}});return [day,T.n?sum/T.n:0,ok]});
 const W=720,H=180,pl=40,pr=46,pt=12,pb=24,X=i=>pl+(D.length>1?i*(W-pl-pr)/(D.length-1):(W-pl-pr)/2),ym=Math.max(1,...pts.map(p=>p[1]))*1.15,om=Math.max(1,...pts.map(p=>p[2]))*1.15,Y=v=>pt+(H-pt-pb)*(1-v/ym),YO=v=>pt+(H-pt-pb)*(1-v/om);
 let s=`<svg viewBox="0 0 ${W} ${H}" width="100%" role="img" aria-label="Évolution de la maîtrise">`;[0,.5,1].forEach(f=>{const y=pt+(H-pt-pb)*(1-f);s+=`<line x1="${pl}" x2="${W-pr}" y1="${y}" y2="${y}" stroke="var(--grid)"/><text x="${pl-5}" y="${y+4}" text-anchor="end">${(ym*f).toFixed(ym<5?1:0)}%</text><text x="${W-pr+5}" y="${y+4}">${Math.round(om*f)}</text>`});
 s+=`<path d="${pts.map((p,i)=>(i?'L':'M')+X(i)+' '+YO(p[2])).join('')}" fill="none" stroke="var(--ok)" stroke-width="2" stroke-dasharray="5 4"/><path d="${pts.map((p,i)=>(i?'L':'M')+X(i)+' '+Y(p[1])).join('')}" fill="none" stroke="var(--gold)" stroke-width="2.4"/>`;pts.forEach((p,i)=>{s+=`<circle cx="${X(i)}" cy="${Y(p[1])}" r="3" fill="var(--gold)"/>`;if(i===0||i===pts.length-1||i%Math.ceil(pts.length/8)===0){const [y,m,dd]=p[0].split('-');s+=`<text x="${X(i)}" y="${H-6}" text-anchor="middle">${+dd}/${+m}</text>`}});$('#n-curve').innerHTML=s+'</svg>'}
function renderNList(){const q=norm($('#n-q').value.trim()),only=$('#n-only').checked;const L=SSP.filter(s=>(!q||norm(s[0]+' '+s[1]).includes(q))&&(!only||nStat(s[0]).ab));
 $('#n-list').innerHTML=L.map(s=>{const t=nStat(s[0]);return `<div class="it${NSEL===s[0]?' sel':''}" style="--gc:${GCOL[s[2]]}" tabindex="0" aria-keyshortcuts="i" data-n="${s[0]}" data-t="s|${s[0]}"><code>${s[0]}</code><span>${esc(s[1])}</span><small>${t.ok}/${t.n} ≥ 95 % · ${t.moy.toFixed(0)} %</small></div>`}).join('')||'<p class="st">Aucun SSP.</p>'}
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
function renderNot(){if(!NSEL)NSEL=sel||SSP[0][0];renderNList();$('#n-main').innerHTML=`<label class="st"><input type="checkbox" id="n-todo" ${NTODO?'checked':''}> Afficher seulement les notions sous 95 %</label>`+nBlock(NSEL,false);stMount($('#n-main'),NSEL);renderNotStats()}
function gK(r,it,i){return it.k||r.id+'_'+i}
function gFig(f){return f?`<figure class="ex-fig"><img src="${esc(f.f)}" alt="${esc(f.c)}" width="${f.w}" height="${f.h}" loading="lazy" decoding="async"><figcaption class="ex-fig__cap">${esc(f.c)}<small class="ex-fig__credit">${esc(f.cr)} · <a href="${esc(f.u)}" target="_blank" rel="noopener">page source</a></small></figcaption></figure>`:''}
function gGroup(r,L,row){let o=gFig(r.fig),cs=null,cp=null;L.forEach(([it,i])=>{const sr=it.sr||r.r;if(sr!==cs){if(cs!==null)o+='</section>';o+=`<section class="ex-region" data-reg="${r.id}"><h3 class="ex-region__h">${esc(sr)}</h3>`;cs=sr;cp=null}if(it.p!==cp){o+=`<h4 class="ex-phase" data-ordre="${EXPO[it.p]||''}">${esc(it.p)}</h4>`;cp=it.p}o+=row(r,it,i)});return o+(cs!==null?'</section>':'')}
function exFmt(s){if(!s||!(s[0]==='§'||/\n@/.test(s)))return s;const PN={'1':'Inspection','2':'Palpation','3':'Percussion','4':'Auscultation','5':'Mobilisation','6':'Tests spéciaux','M':'Mesures','N':'Neurologique'},RL={membres:'Membres et articulations',neuro:'Neurologique',autres:'Autres éléments ciblés'};let o='',op=false,ul=false;const cl=()=>{if(ul){o+='</ul>';ul=false}};
 s.split('\n').forEach(l=>{const c=l[0],v=l.slice(1).trim();
  if(c==='§'){cl();if(op)o+='</section>';const g=GES.find(r=>r.id===v);o+=`<section class="ex-region" data-reg="${esc(v)}"><h3 class="ex-region__h">${esc(RL[v]||(g&&g.r)||v)}</h3>`;op=true}
  else if(c==='¶'){cl();if(PN[v])o+=`<h4 class="ex-phase" data-ordre="${v}">${PN[v]}</h4>`}
  else if(c==='@'){cl();o+='<nav class="ex-xref" aria-label="Gestes liés">'+v.split(' ').filter(Boolean).map(t=>{if(t.startsWith('r:')){const g=GES.find(r=>r.id===t.slice(2));return g?`<button type="button" class="ex-chip" data-gx="${g.id}|">Gestes · ${esc(g.r)}</button>`:''}for(const g of GES){const it=g.items.find(x=>x.k===t);if(it)return `<button type="button" class="ex-chip" data-gx="${g.id}|${esc(it.k)}">${esc(it.s)}</button>`}return ''}).join('')+'</nav>'}
  else if(l.startsWith('• ')){if(!ul){o+='<ul class="ex-items">';ul=true}o+='<li>'+l.slice(2)+'</li>'}
  else if(l.trim()){cl();o+='<p>'+l+'</p>'}});cl();if(op)o+='</section>';return o}
function gGo(rid,key){const r=GES.find(x=>x.id===rid);if(!r)return;if(typeof hideTip==='function')hideTip(true);GREG=rid;$('#g-q').value='';$('#g-ph').value='';$('#g-todo').checked=false;$$('.tab').find(t=>t.dataset.v==='ges').click();renderGes();let el=null;if(key){const i=r.items.findIndex(it=>it.k===key||it.s===key);if(i>=0)el=$(`#g-list [data-t="g|${rid}|${i}"]`)}(el||$('#g-head')).scrollIntoView({block:el?'center':'start'});if(el){el.classList.add('ex-flash');setTimeout(()=>el.classList.remove('ex-flash'),1800)}}
function renderGes(){const q=norm($('#g-q').value.trim()),ph=$('#g-ph').value,todo=$('#g-todo').checked;const tot=GES.reduce((a,r)=>a+r.items.length,0),ok=Object.values(GS).filter(Boolean).length;
 $('#g-reg').innerHTML=['reg','sys','pop'].map(a=>`<div class="ex-axe" data-ax="${a}"><span class="ex-axe__h">${EXAX[a]}</span>`+GES.filter(r=>(r.ax||'reg')===a).map(r=>{const k=r.items.filter((it,i)=>GS[gK(r,it,i)]).length;return `<button class="${r.id===GREG&&!q?'on':''}" data-r="${r.id}">${esc(r.r)} · ${k}/${r.items.length}</button>`}).join('')+'</div>').join('');
 const R=q?GES:GES.filter(r=>r.id===GREG);let h='';
 R.forEach(r=>{const L=r.items.map((it,i)=>[it,i]).filter(([it,i])=>(!ph||it.p===ph)&&(!todo||!GS[gK(r,it,i)])&&(!q||norm(it.p+' '+it.s+' '+it.g+' '+it.n).includes(q)));if(!L.length)return;
  h+=(q?`<div class="nsec"><span>${esc(r.r)}</span><span>${L.length}</span></div>`:'')+(q?L.map(([it,i])=>gRow(r,it,i)).join(''):gGroup(r,L,gRow))});
 function gRow(r,it,i){const k=gK(r,it,i);return `<label class="gr${GS[k]?' ok':''}" data-t="g|${r.id}|${i}"><input type="checkbox" data-g="${k}" ${GS[k]?'checked':''}><span><span class="ph">${esc(it.p)}</span><b class="tw" tabindex="0" role="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="tip">${esc(it.s)}</b><button class="ti" aria-label="Ce qui rapporte les points">i</button></span><p>${esc(it.g)}</p><p class="i">${esc(it.n)}</p>${it.av?`<small class="ex-av">À vérifier · ${esc(it.av)}</small>`:''}${it.x?`<nav class="ex-xref" aria-label="Renvois">${it.x.map(([rid,t])=>`<button type="button" class="ex-chip" data-gx="${rid}|${esc(t)}">→ ${esc((GES.find(g=>g.id===rid)||{}).r||rid)} · ${esc(t)}</button>`).join('')}</nav>`:''}</label>`}
 const cr=GES.find(r=>r.id===GREG);$('#g-head').innerHTML=`<div class="row" style="justify-content:space-between"><h2>${q?'Résultats de recherche':esc(cr?.r||'')}</h2><span id="g-loc"></span><span class="st">${ok} / ${tot} gestes maîtrisés au total</span></div><div class="pbar" style="margin:8px 0"><i style="width:${tot?ok/tot*100:0}%;background:var(--ok)"></i></div>`;gLoc();
 $('#g-list').innerHTML=h||'<p class="st">Aucun geste ne correspond.</p>'}
function parseRes(t){const m=t.match(/MEDORA-RESULTAT([\s\S]*?)(?:FIN-MEDORA|$)/);let b=(m?m[1]:t).replace(/```(?:json)?/gi,'');const a=b.indexOf('{'),z=b.lastIndexOf('}');if(a<0||z<a)throw new Error('bloc MEDORA-RESULTAT introuvable');b=b.slice(a,z+1);try{return JSON.parse(b)}catch(e){return JSON.parse(b.replace(/[“”]/g,'"').replace(/,\s*([}\]])/g,'$1'))}}
function pvRankText(c){const cl=((ckW('PREV')||{})[c]||{}).classement;return cl&&cl.etat==='valide'?'Ordre qualitatif documenté dans le cadre indiqué ; une fréquence inconnue reste inconnue.':'Classement qualitatif non établi : l’ordre des valeurs inconnues reste celui de la rédaction et ne démontre pas leur probabilité.'}
function pvOf(c,i){const P=PRV[c];return P?P.find(x=>x[0]===i)||null:null}
function pvFmt(x){if(!x||x[1]==null)return '% à vérifier';return (x[2]?x[2]+' ':'')+String(x[1]).replace('.',',')+' %'+(x[3]?' <small>population</small>':'')}
function pvSpan(c,i,act){const x=pvOf(c,i);return `<span class="pv${x&&x[1]!=null?'':' av'}"${act?` data-t="pv|${c}|${i}" tabindex="0" role="button"`:''}>${pvFmt(x)}</span>`}
function pvLine(c,i){const e=((ckW('PREV')||{})[c]||{})[i];return `<p class="pvl"><b>Fréquence</b> : ${pvSpan(c,i,1)}${e&&e.cadre?' · '+esc(e.cadre)+'.':' · cliquez ou touchez le pourcentage pour lire le cadre et la source.'}</p>`}
function ckGlo(id){return ckLoad('glo-'+(/^[a-z]/.test(id)?id[0]:'0')).then(T=>T[id]||null)}
function monoId(n){return (n||'').toLowerCase().normalize('NFKD').replace(/[\u0300-\u036f]/g,'').replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'')}
function monoGet(n,key){const k=monoId(n);if(!k)return null;const t=/[a-z]/.test(k[0])?k[0]:'0',M=window['CK_MONO_'+t.toUpperCase()];if(M)return M[k]||null;if(!MONO_T[t]){MONO_T[t]=1;monoLoad(t).then(()=>{if(!TIPEL.hidden&&tipK===key)showTip({dataset:{t:key}},tipPin,tipOp||TIPEL,false,true)}).catch(()=>{delete MONO_T[t]})}return null}
function tipFor(key){const [ty,a,b]=key.split('|');let h='',ti='',src='';
 if(ty==='n'){const T=TIP[a];if(!T)return null;const s=BY[a];const i=+b.slice(1);
  if(b[0]==='c'){ti=CLIN[i];h=i===5?exFmt(T.c[i]):T.c[i];src=T.s}else if(b[0]==='d'){const dn=(NOT[a]||[[]])[0][i]||'',MO=monoGet(dn,key);ti='Diagnostic différentiel : '+dn;h=pvLine(a,i)+T.d[i];src=T.s;if(MO)return {hd:'Monographie · '+a,ti:dn,h:pvLine(a,i)+MO.h,src:MO.s}}else if(b[0]==='f'){const n=(NOT[a]||[[],[]])[1][i]||['',''];ti=n[0]+' · '+n[1];h=T.f[i];src=T.fs}else return null;
  const V=T.v&&(b[0]==='c'||b[0]==='d')?T.v[b[0]][i]:null;if(V&&V[0]==='silence')return {hd:'L’essentiel pour 100 % des points · '+a,ti,h:'<i>Silence volontaire : aucune source vérifiée ne permet ici une information précise. Une information vague vaut moins qu’un silence.</i>',src:''};if(V&&V[1].length){const L=V[1].map(id=>T.v.S.find(x=>x.id===id)).filter(Boolean);return {hd:'L’essentiel pour 100 % des points · '+a,ti,h,ok:V[0],links:L}}
  return {hd:'L’essentiel pour 100 % des points · '+a,ti,h,src:(src?src+' · ':'')+'GLOBALITY, cours SSP '+a+' — '+(s?s[1]:''),pend:true}}
 if(ty==='s'){const T=TIP[a],s=BY[a];if(!T)return null;const X=b&&S.seances[b];return {hd:'Fiche éclair · '+a,ti:s[1],h:(X?'<b>Séance</b> : '+esc(X.act)+' · '+esc(s[1])+', '+calLab(X)+'–'+hm(X.start+X.dur)+' ('+X.dur+'′)<br>':'')+'<b>Définition</b><br>'+T.c[0]+'<br><b>Points clés</b><br>'+T.c[12],src:(T.s?T.s+' · ':'')+'GLOBALITY'}}
 if(ty==='g'){const r=GES.find(x=>x.id===a),it=r&&r.items[+b];if(!it)return null;return {hd:'Pour marquer le point · '+it.p,ti:it.s,h:'<b>Geste</b> : '+esc(it.g)+'<br><b>À énoncer</b> : '+esc(it.n)+'<br><b>Règle du temps « '+esc(it.p)+' »</b> : '+esc(PHT[it.p]||PHT['Tests spéciaux']),src:(it.src?it.src+' · ':'')+'OFSP, Exigences MED 2026, § 5.1.4 : seuls les gestes et mesures corrects rapportent des points, sans point négatif · PROFILES 2023, EPA 2'}}
 if(ty==='m')return memTip(a,key);
 const ck=ckTip(ty,a,b);if(ck!==undefined)return ck;
 return null}
function showTip(el,pin,op,kbd,keep){const k=el.dataset.t,x=tipFor(k);if(!x||!x.h){if(!keep)hideTip(true);return}op=op||el;const nest=!keep&&!TIPEL.hidden&&!!tipK&&TIPEL.contains(op);if(nest){if(tipStk.length>=CK_MAX-1)return;tipStk.push({k:tipK,ti:tipTi});op=tipOp&&tipOp.isConnected?tipOp:TIPEL;pin=true}else if(!keep)tipStk.length=0;const lv=tipStk.length+1;tipTi=x.ti;if(tipOp&&tipOp!==op&&tipOp.hasAttribute('aria-expanded'))tipOp.setAttribute('aria-expanded','false');tipK=k;tipPin=!!pin;tipOp=op;
 TIPEL.innerHTML=`<div class="h"><span>${esc(x.hd+(lv>1?' · niveau '+lv:''))}</span><span class="ck-hb">${lv>1?'<button class="bk" type="button" aria-label="Retour à la fenêtre précédente">← Retour</button>':''}<button aria-label="Fermer">×</button></span></div>${lv>1?`<nav class="ck-fil" aria-label="Fil d’Ariane">${tipStk.map((s,i)=>`<button type="button" data-lv="${i}">${esc(s.ti)}</button> › `).join('')}<span aria-current="page">${esc(x.ti)}</span></nav>`:''}<div class="t">${esc(x.ti)}</div><div class="ck-b">${x.h}</div>${x.links?`<div class="s"><span class="vb">✓ Vérifié · ${esc(x.ok||'confirmé')}</span> Sources consultées : ${x.links.map(l=>(l.u?`<a href="${esc(l.u)}" target="_blank" rel="noopener">${esc(l.t)}</a>`:esc(l.t))+` <small>(${esc([l.o,l.n,l.a].filter(Boolean).join(', '))})</small>`).join(' · ')}</div>`:x.src?`<div class="s">${x.pend?'<span class="vb pend">Contenu GLOBALITY · vérification externe en cours</span> ':''}Sources : ${esc(x.src)}</div>`:''}`;tipCk(lv,k);TIPEL.hidden=false;TIPEL.setAttribute('role',tipPin?'dialog':'tooltip');TIPEL.setAttribute('aria-label',x.hd+' · '+x.ti);if(op.hasAttribute('aria-expanded'))op.setAttribute('aria-expanded',String(tipPin));
 if(op!==TIPEL&&op.isConnected){const r=op.getBoundingClientRect(),w=TIPEL.offsetWidth,hh=TIPEL.offsetHeight,vw=innerWidth,vh=innerHeight;let top=r.bottom+6;if(top+hh>vh-8)top=Math.max(8,r.top-hh-6);top=Math.max(8,Math.min(top,vh-hh-8));top=Math.max(8,Math.min(top,vh-hh-8));let left=Math.min(Math.max(8,r.left+Math.min(60,r.width/4)),vw-w-8);if(pin&&top<r.bottom&&top+hh>r.top&&left<r.right&&left+w>r.left){if(r.right+w+16<=vw)left=r.right+8;else if(r.left-w-8>=8)left=r.left-w-8}TIPEL.style.top=top+'px';TIPEL.style.left=left+'px';if(pin&&!nest&&matchMedia('(max-width:620px)').matches){const tr=TIPEL.getBoundingClientRect();if(r.bottom>tr.top-8)scrollBy(0,r.bottom-tr.top+16)}};if(kbd){const cb=TIPEL.querySelector('.h button');if(cb)cb.focus({preventScroll:true})}}
function hideTip(force){if(tipPin&&!force)return;const back=TIPEL.contains(document.activeElement);TIPEL.hidden=true;TIPEL.setAttribute('role','tooltip');if(tipOp){if(tipOp.hasAttribute('aria-expanded'))tipOp.setAttribute('aria-expanded','false');if(back&&tipOp.isConnected)tipOp.focus({preventScroll:true})}tipK=null;tipPin=false;tipOp=null;tipStk.length=0;tipTi=''}
function tipToggle(el,op,kbd){clearTimeout(tipT);if(tipPin&&tipK===el.dataset.t){tipSup=el.dataset.t;hideTip(true)}else showTip(el,true,op,kbd)}
function blkFit1(k){const t=k.querySelector('.t'),b=k.querySelector('b');if(!t||!b)return;k.classList.remove('mini','nodu');t.style.removeProperty('--cl');const cs=getComputedStyle(k),H=k.clientHeight-parseFloat(cs.paddingTop)-parseFloat(cs.paddingBottom),lh=parseFloat(getComputedStyle(t).lineHeight)||14,n=Math.floor((H-b.offsetHeight)/lh+0.02);if(n>=1)t.style.setProperty('--cl',n);else k.classList.add('mini');if(b.scrollWidth>b.clientWidth)k.classList.add('nodu')}
function blkFit(r){(r||document).querySelectorAll('.blk').forEach(blkFit1)}
function ckW(n){return window['CK_'+n]}
function ckFold(s){let o='';for(let i=0;i<s.length;i++){const c=s[i],f=c.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();o+=f.length===1?f:c}return o}
function ckData(n){const v=ckW(n);if(!v)return null;if(Array.isArray(v)){const m={};v.forEach(x=>{m[x.id||x.module]=x});window['CK_'+n]=m;return m}return v}
function ckDate(d){const m=/^(\d{4})-(\d\d)-(\d\d)$/.exec(d||'');return m?m[3]+'.'+m[2]+'.'+m[1]:String(d||'')}
function ckRe(s){return s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')}
function ckP(s){s=String(s||'').trim();return esc(s)+(/[.!?…:;]$/.test(s)?'':'.')}
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
function ckNeed(ty,a,key){if(typeof ckLoad!=='function'||ckTry.get(key)===2)return true;if(ckTry.get(key)===1)return false;const L=(CK_DEP[ty]||[]).filter(n=>!ckW(n.toUpperCase().replace(/[^A-Z0-9]/g,'_'))),g=ty==='glo'&&!gloE(a);
 if(!L.length&&!g)return true;ckTry.set(key,1);Promise.allSettled([...L.map(n=>ckLoad(n)),...(g?[ckGlo(a)]:[])]).then(()=>{ckTry.set(key,2);gloI=null;if(!gloOn&&gloIndex())gloStart();if(!TIPEL.hidden&&tipK===key)showTip({dataset:{t:key}},tipPin,tipOp||TIPEL,false,true)});return false}
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
   f.append(txt.slice(at,i));const s=document.createElement('span');s.className='tw glo';if(p.closest('.nr'))s.style.cssText='display:inline-flex;align-items:center;min-width:24px;min-height:24px';s.dataset.t='glo|'+id;s.tabIndex=0;s.setAttribute('role','button');s.setAttribute('aria-haspopup','dialog');
   s.setAttribute('aria-expanded','false');s.setAttribute('aria-controls','tip');s.textContent=txt.slice(i,i+len);f.append(s);at=i+len;k++}
  if(k){f.append(txt.slice(at));if(['grid','inline-grid','flex','inline-flex'].includes(getComputedStyle(p).display)){const flow=document.createElement('span');flow.append(f);t.replaceWith(flow)}else t.replaceWith(f);n+=k}}
 return n}
function gloSched(){if(gloT||!gloQ.size)return;gloT=1;ckIdle(gloRun)}
function gloRun(dl){gloT=0;const R=[...gloQ].filter(e=>e.isConnected&&![...gloQ].some(o=>o!==e&&o.isConnected&&o.contains(e)));gloQ.clear();gloMO.disconnect();
 try{while(R.length){const e=R.shift();if(e.children.length>40&&dl&&dl.timeRemaining()<4){for(const c of e.children)gloQ.add(c);continue}gloLink(e);if(dl&&dl.timeRemaining()<2){R.forEach(x=>gloQ.add(x));break}}}
 finally{gloMO.observe(document.querySelector('.w')||document.body,{childList:true,subtree:true})}gloSched()}
function gloStart(){gloI=null;if(!gloIndex())return;gloOn=true;const W=document.querySelector('.w')||document.body;for(const c of W.children)gloQ.add(c);gloMO.observe(W,{childList:true,subtree:true});gloSched()}
function ckL(k,t,ti){return `<span class="tw ck-l" data-t="${esc(k)}" tabindex="0" role="button" aria-haspopup="dialog">${esc(t)}</span>`}
function ncVue(v){return NC_VUE[v]||v}
function ckLab(n,id){if(n==='GLO'){const m=gloMeta(id);return m?m.lab:id}const e=(ckData(n)||{})[id];return e?(e.label||e.nom||id):id}
function ckLnk(n,ty,id){const ok=n==='GLO'?!!gloMeta(id):!!(ckData(n)||{})[id];return ok?ckL(ty+'|'+id,ckLab(n,id),ty==='glo'?gloShort(id):''):esc(id)}
function ckGes(L){const o=[];for(const k of ckArr(L)){for(const r of (typeof GES!=='undefined'?GES:[])){const i=r.items.findIndex(x=>x.k===k);if(i>=0){o.push(ckL('g|'+r.id+'|'+i,r.items[i].s,r.items[i].p));break}}}return o.length?`<p><b>Gestes à faire</b> : ${o.join(', ')}.</p>`:''}
function gLoc(){const el=$('#g-loc');if(!el)return;const f=()=>{const e=(ckData('LOC')||{})[GREG];el.innerHTML=e?ckL('loc|'+GREG+'|A','Syndromes d’urgence de la région →'):''};if(ckData('LOC'))f();else ckLoad('loc').then(f).catch(()=>{})}
function ckArr(x){return x==null?[]:Array.isArray(x)?x:[x]}
function modLab(m){const g=typeof GES!=='undefined'&&GES.find(x=>x.id===m);return g?g.r:m}
function ckSrc(L){const S=ckData('SRC')||{};return ckArr(L).map(s=>{if(typeof s==='string')s={id:s};const r=S[s.id]||{},t=r.titre||r.label||s.id;
 return (r.url?`<a href="${esc(r.url)}" target="_blank" rel="noopener">${esc(t)}</a>`:esc(t))+(r.org?' ('+esc(r.org)+')':'')+(s.loc?', '+esc(s.loc):'')+(s.lu_le?', lu le '+esc(ckDate(s.lu_le)):'')}).join(' · ')}
function ckFoot(e){const av=e.statut==='À vérifier'||!ckArr(e.src).length;return `<p class="ck-src">${av?'<span class="vb pend">À vérifier</span> ':''}${ckArr(e.src).length?'Sources : '+ckSrc(e.src):'Source à lire.'}</p>`}
function ckJ(l,v){return v?`<br><i>${l}</i> : ${ckP(v)}`:''}
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
 if(ty==='pv'){const nm=(NOT[a]||[[]])[0][+b]||'',H='Fréquence du diagnostic · '+a;if(!PRV[a])return {hd:H,ti:nm,h:'<p>Aucune fréquence n’est encore sourcée pour les diagnostics de ce SSP : chaque pourcentage reste à vérifier, et l’ordre de rédaction ne démontre pas une fréquence décroissante.</p>'};if(!ckNeed(ty,a,key))return ckWait(H,nm);const e=((ckData('PREV')||{})[a]||{})[b];if(!e)return null;const x=pvOf(a,+b),S=e.src?(ckData('SRC')||{})[e.src]:null;return {hd:H,ti:nm,h:(x&&x[1]!=null?`<p><span class="pv">${pvFmt(x)}</span> ${e.type==='population'?'de la population générale : aucune donnée par motif de consultation n’a été trouvée.':'des patients qui consultent pour cette plainte.'}</p>`:'<p><span class="pv av">% à vérifier</span> : la fréquence dans ce cadre n’est pas établie.</p>')+`<p>${esc(pvRankText(a))}</p>`+(e.cadre?`<p><b>Cadre</b> : ${esc(e.cadre)}.</p>`:'')+(S?`<p><b>Source</b> : ${S.url?`<a href="${esc(S.url)}" target="_blank" rel="noopener">${esc(S.titre)}</a>`:esc(S.titre)} (${esc(S.org)})${e.loc?', '+esc(e.loc):''}, lue le ${ckDate(e.date_lu)}.</p>`:'')+(e.note?`<p>${esc(e.note)}</p>`:'')}}
 if(!ckNeed(ty,a,key))return ckWait({syn:'Syndrome',hyp:'Exploration',loc:'Synthèse locale',nc:'Schéma'}[ty]);
 if(ty==='syn'){const e=(ckData('SYN')||{})[a];if(!e)return null;
  return {hd:'Syndrome'+(e.module?' · '+modLab(e.module):''),ti:e.label,h:(e.comment||e.def?`<p>${ckP(e.comment||e.def)}</p>`:'')+ckGes(e.gestes)+ckLinks('Signes à rechercher','GLO','glo',e.signes)
   +ckList('À demander',e.a_demander,esc)+ckLinks('Hypothèses','HYP','hyp',e.hyp||e.orientation)+(ckArr(e.vues).length?`<p><b>Sur le schéma</b> : ${ckArr(e.vues).map(v=>ckL(v,ncVue(String(v).split('|')[2]||v))).join(', ')}.</p>`:'')+ckFoot(e)}}
 if(ty==='hyp'){const e=(ckData('HYP')||{})[a];if(!e)return null;
  if(b==='pec'){const p=e.pec||{};return {hd:'Prise en charge',ti:e.label,h:(p.objectif?`<p><b>1. Objectif</b> : ${ckP(p.objectif)}</p>`:'')+ckList('2. Mesures générales',p.mesures_generales,ckP)
   +ckList('3. Moyens spécifiques',p.moyens_specifiques,m=>(m.type?`<b>${esc(CK_MOY[m.type]||m.type)}</b>`:'')+ckJ('Mécanisme',m.mecanisme)+ckJ('Principe',m.principe)+(m.mecanisme||m.principe?'<br><i>Moyen</i> : ':m.type?' : ':'')+ckP(m.texte)+ckDose(m.dose_ref)+ckJ('Pourquoi ce choix',m.pourquoi_ce_choix)+ckJ('Limites',m.limites)+(m.statut==='À vérifier'?' <span class="vb pend">À vérifier</span>':'')+(ckArr(m.src).length?` <small>[${ckSrc(m.src)}]</small>`:''))
   +(p.objectif||ckArr(p.mesures_generales).length||ckArr(p.moyens_specifiques).length?'':'<p><span class="vb pend">À vérifier</span> Prise en charge à rédiger.</p>')+ckFoot(e)}}
  const x=e.exam||{},R=x.reference,Li=ckArr(x.lignes).slice().sort((p,q)=>p.rang-q.rang),rg=r=>r===1?'1re intention':r+'e intention',
   part=(l,v)=>v?` <i>${l}</i> : ${ckP(v)}`:'',jx=o=>ckJ('Mécanisme',o.mecanisme)+ckJ('Principe',o.principe)+ckJ('Recherche',o.recherche)+ckJ('Pourquoi cet examen',o.pourquoi_ce_choix||o.pourquoi)+ckJ('Précautions',o.precautions)+ckJ('Alternative',o.alternative),sr=L=>ckArr(L).length?` <small>[${ckSrc(L)}]</small>`:'';
  return {hd:'Exploration',ti:e.label,h:(e.bloquant?'<p><span class="urg" data-bloquant>Urgence</span></p>':'')
   +(R?`<p><b>Examen de référence</b> : ${ckP(R.nom)}${jx(R)}${sr(R.src)}</p>`:'')
   +Li.map(l=>`<p><b>${rg(l.rang)}</b> : ${ckP(l.nom)}${jx(l)}${sr(l.src)}</p>`).join('')
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
function ckSvg(fig,src){const d=new DOMParser().parseFromString(src,'image/svg+xml'),s=d.documentElement;if(!s||s.nodeName!=='svg')return null;
 s.querySelectorAll('script,foreignObject').forEach(x=>x.remove());for(const el of [s,...s.querySelectorAll('*')])for(const at of [...el.attributes]){if(/^on/i.test(at.name)||(/href$/i.test(at.name)&&/^\s*javascript:/i.test(at.value)))el.removeAttribute(at.name)}
 const n=document.importNode(s,true);n.setAttribute('role','img');n.removeAttribute('width');n.removeAttribute('height');n.setAttribute('preserveAspectRatio','xMidYMid meet');return n}
function ckEtats(s){try{return s&&s.dataset.etats?JSON.parse(s.dataset.etats):null}catch(e){return null}}
function ckEtat(fig,x){const s=fig.querySelector('svg'),M=ckEtats(s);if(!M||!M[x])return;ckEt=x;s.dataset.etat=x;
 s.querySelectorAll('[data-etat]').forEach(g=>g.setAttribute('display',g.dataset.etat===x?'inline':'none'));NC_COU.forEach(c=>{ckCou[c]=M[x].includes(c)});
 TIPEL.querySelectorAll('input[data-ck=cou]').forEach(i=>{i.checked=ckCou[i.value]!==false});TIPEL.querySelectorAll('[data-ck=etat]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.e===x)));ckApply(fig)}
function ckApply(fig){const s=fig.querySelector('svg'),F=TIPEL.querySelector('.ck-couches');if(!F)return;const et=s&&ckEtats(s)&&s.dataset.etat||'';
 for(const i of F.querySelectorAll('input[data-ck=cou]')){const G=s?[...s.querySelectorAll(`#${i.value},[data-couche="${i.value}"]`)]:[];i.closest('label').hidden=!G.length;i.disabled=!G.some(g=>g.childElementCount);
  G.forEach(g=>g.setAttribute('display',i.checked&&(!et||!g.dataset.etat||g.dataset.etat===et)?'inline':'none'))}}
function ckFig(fig){const id=fig.dataset.nc,v=fig.dataset.vue,e=(ckData('NC')||{})[id];if(!e)return;const nom=ckLab('NC',id),F=TIPEL.querySelector('.ck-couches');
 if(v==='tour'){fig.innerHTML=`<div class="ck-tour" role="slider" tabindex="0" aria-label="Tour du schéma ${esc(nom)} : glissez ou utilisez les flèches" aria-valuemin="0" aria-valuemax="7" aria-valuenow="0" aria-valuetext="0°" style="background-image:url('${esc(e.tour)}')"></div><figcaption class="st">Glissez, ou utilisez les flèches gauche et droite : 8 vues à 45°.</figcaption>`;return}
 const p=e.vues[v],SV=ckW('SVG'),src=SV&&SV[p];
 const cred=s=>{let c=(ckW('NC_CRED')||{})[p]||(e.credits||{})[v]; c=c?(typeof c==='string'?c:(c.tasl||c.credit||'')):'';return c?`<figcaption class="ck-cr">${esc(c)}</figcaption>`:''};
 if(src){const n=ckSvg(fig,src);if(n){n.setAttribute('aria-label','Schéma : '+nom+', vue '+ncVue(v));n.removeAttribute('aria-labelledby');fig.replaceChildren(n);fig.insertAdjacentHTML('beforeend',cred(n));ckNum(fig,n);
  const M=ckEtats(n),E=TIPEL.querySelector('.ck-etats');
  if(M&&E){const K=Object.keys(M),x=K.includes(ckEt)?ckEt:(n.dataset.etat&&M[n.dataset.etat]?n.dataset.etat:K[0]);E.innerHTML=K.map(k=>`<button type="button" class="b" data-ck="etat" data-e="${esc(k)}" aria-pressed="${k===x}">${esc(NC_ETL[k]||k)}</button>`).join('');E.hidden=false;ckEtat(fig,x)}else ckApply(fig);return}}
 const js=e.js||'assets/nc/'+id+'.js';
 if(!(js in ckJs)){ckJs[js]=0;fig.innerHTML='<p class="st">Chargement du schéma…</p>';const sc=document.createElement('script');sc.src=js;
  sc.onload=()=>{ckJs[js]=1;if(fig.isConnected)ckFig(fig)};sc.onerror=()=>{ckJs[js]=-1;if(fig.isConnected)ckFig(fig)};document.head.appendChild(sc);return}
 if(ckJs[js]===0)return;
 fig.innerHTML=`<img src="${esc(p)}" alt="Schéma : ${esc(nom)}, vue ${ncVue(v)}" loading="lazy">${cred(null)}<p class="st">Les couches ne sont pas disponibles pour ce schéma : le fichier ${esc(js)} manque.</p>`;if(F)F.disabled=true}
function ckNum(fig,s){const {lv,ex}=ckCtx;
 s.querySelectorAll('.nc-num').forEach(g=>{const id=g.dataset.glo,k=id?'glo|'+id:'',ok=k&&gloMeta(id)&&lv<CK_MAX&&!ex.includes(k);g.setAttribute('tabindex','0');g.setAttribute('role','button');
  g.setAttribute('aria-label',(g.dataset.num||'')+' · '+(g.dataset.nom||'')+(ok?' : ouvrir la fiche':''));if(ok){g.dataset.t=k;g.classList.add('tw')}else{delete g.dataset.t;g.classList.remove('tw')}});
 if(!fig.querySelector('.ck-bulle'))fig.insertAdjacentHTML('beforeend','<div class="ck-bulle" role="status" hidden></div>')}
function ckBulle(g){const fig=g&&g.closest('.ck-fig'),b=fig&&fig.querySelector('.ck-bulle');if(!b)return;const id=g.dataset.glo,d=id?gloShort(id):'';
 b.innerHTML=`<b>${esc(g.dataset.num||'')} · ${esc(g.dataset.nom||'')}</b>${d?'<br>'+esc(d):''}`;b.hidden=false;
 const r=g.getBoundingClientRect(),q=fig.getBoundingClientRect(),w=b.offsetWidth;b.style.left=Math.max(0,Math.min(q.width-w,r.left-q.left+r.width/2-w/2))+'px';b.style.top=(r.bottom-q.top+6)+'px'}
function ckBulleX(){const b=TIPEL.querySelector('.ck-bulle');if(b)b.hidden=true}
function ckTour(el,d){const f=((+el.getAttribute('aria-valuenow')+d)%8+8)%8;el.setAttribute('aria-valuenow',f);el.setAttribute('aria-valuetext',f*45+'°');el.style.backgroundPositionX=(f*100/7)+'%'}
function tipGo(i){if(i<0||i>=tipStk.length)return;const s=tipStk[i];tipStk.length=i;showTip({dataset:{t:s.k}},true,tipOp,true,true)}
function tipNav(e){const t=e.target;if(!(t instanceof Element)||!TIPEL.contains(t))return false;
 if(t.closest('input,a[href]'))return true;
 const bk=t.closest('.bk');if(bk){e.preventDefault();e.stopPropagation();tipGo(tipStk.length-1);return true}
 const lv=t.closest('[data-lv]');if(lv){e.preventDefault();e.stopPropagation();tipGo(+lv.dataset.lv);return true}
 const et=t.closest('[data-ck=etat]');if(et){e.preventDefault();e.stopPropagation();const f=TIPEL.querySelector('.ck-fig');if(f)ckEtat(f,et.dataset.e);return true}
 const c=t.closest('[data-ck]');if(c&&c.dataset.k){e.preventDefault();e.stopPropagation();const k=c.dataset.k;showTip({dataset:{t:k}},true,tipOp,false,true);const n=TIPEL.querySelector(`[data-k="${CSS.escape(k)}"]`);if(n)n.focus({preventScroll:true});return true}
 const mk=t.closest('.nc-num');if(mk&&!mk.dataset.t){e.preventDefault();e.stopPropagation();ckBulle(mk);return true}
 const a=t.closest('.ck-b [data-t]');if(a){e.preventDefault();e.stopPropagation();clearTimeout(tipT);showTip(a,true,a,e.detail===0);return true}
 return false}
function tipCk(lv,k){TIPEL.classList.toggle('ck',k.split('|')[0] in CK_DEP);TIPEL.classList.toggle('ck-nc',k.startsWith('nc|'));const B=TIPEL.querySelector('.ck-b');if(!B)return;const ex=tipStk.map(s=>s.k).concat(k);
 B.querySelectorAll('.ck-l[data-t]').forEach(a=>{if(lv>=CK_MAX||ex.includes(a.dataset.t))a.replaceWith(document.createTextNode(a.textContent))});
 if(lv<CK_MAX)gloLink(B,new Set(ex.filter(s=>s.startsWith('glo|')).map(s=>s.split('|')[1])),true);
 ckCtx={lv,ex};B.querySelectorAll('.ck-fig').forEach(f=>ckFig(f))}
function renderAll(){const A=agg();applyDisp();renderAtt();renderKpis(A);renderList();renderGrid();renderVit(A);renderCalc(A);renderExi();renderMemo();renderCSPlan();renderCSLog();renderNotStats();if(!$('#v-not').hidden)renderNot();if(!$('#v-ges').hidden)renderGes()}
