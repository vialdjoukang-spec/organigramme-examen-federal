/* ---------- HERMÈS : calendrier interactif (clic, plage, recherche floue, déplacement, durée, toucher, clavier) ---------- */
let calP=null,calSup=false,qpCode=null;
function calSay(t){const m=document.getElementById('cq-m');if(m)m.textContent=t}
function calMin(col,y,f){const r=col.getBoundingClientRect(),v=(y-r.top)/PX*4,q=f==='f'?Math.floor(v):f==='c'?Math.ceil(v):Math.round(v);return Math.max(H0*60,Math.min(H1*60,H0*60+q*15))}
function calLab(x){const d=parse(x.date);return JOURS[d.getDay()]+' '+d.getDate()+' '+MOIS[d.getMonth()]+' à '+hm(x.start)}
function lev(a,b){let p=[...Array(b.length+1).keys()];for(let i=1;i<=a.length;i++){const c=[i];for(let j=1;j<=b.length;j++)c[j]=Math.min(p[j]+1,c[j-1]+1,p[j-1]+(a[i-1]===b[j-1]?0:1));p=c}return p[b.length]}
function fzScore(q,s){const c=norm(s[0]),n=norm(s[1]+' '+(GROUPES[s[2]]||'')),cq=q.replace(/\s+/g,'');if(c===cq)return 1000;if(c.startsWith(cq))return 900-c.length;
 const W=n.split(/[^a-z0-9]+/).filter(Boolean);let sc=0;
 for(const t of q.split(/\s+/).filter(Boolean)){const e=t.length>=7?2:1;let v=0;if(c.startsWith(t))v=60;else if(W.includes(t))v=50;else if(W.some(w=>w.startsWith(t)))v=40;else if(n.includes(t))v=25;
  else if(t.length>=4&&W.some(w=>lev(w.slice(0,t.length),t)<=e||lev(w,t)<=e))v=12;if(!v)return 0;sc+=v}
 return sc-n.length/1000}
function fz(q,k){q=norm(String(q).trim());if(!q)return [];return SSP.map(s=>[fzScore(q,s),s]).filter(a=>a[0]>0).sort((a,b)=>b[0]-a[0]).slice(0,k||8).map(a=>a[1])}
function cqRender(){const q=$('#cq').value,R=fz(q),ul=$('#cq-r');if(!q.trim()){ul.hidden=true;ul.innerHTML='';calSay('');return}
 ul.innerHTML=R.map(s=>`<li class="cq-i${sel===s[0]?' on':''}" draggable="true" data-c="${esc(s[0])}"><button class="b cq-p" type="button" data-a="p" title="Placer ce chapitre : cliquez ensuite sur une plage"><code>${esc(s[0])}</code><span>${esc(s[1])}</span></button><button class="b" type="button" data-a="o" aria-label="Ouvrir ${esc(s[0])}">Ouvrir</button></li>`).join('');
 ul.hidden=!R.length;calSay(R.length?R.length+' résultat'+(R.length>1?'s':'')+' : choisissez « Placer » ou « Ouvrir ».':'Aucun chapitre ne correspond à cette recherche.')}
function cqOpen(code){const L=Object.entries(S.seances).filter(([,x])=>x.ssp===code).sort((a,b)=>(a[1].date+hm(a[1].start))<(b[1].date+hm(b[1].start))?-1:1),t=iso(new Date()),nx=L.find(([,x])=>x.date>=t)||L[L.length-1];
 if(nx){cur=parse(nx[1].date);renderGrid();openEdit(nx[0]);calSay('La séance « '+code+' » du '+calLab(nx[1])+' est ouverte.');return}
 $('#q').value=code;renderList();const it=$('#list .it[data-c="'+code+'"]');if(it){it.scrollIntoView({block:'nearest'});it.focus();tipToggle(it,it,true)}calSay('Ce chapitre n’a encore aucune séance ; sa fiche est ouverte dans la nomenclature.')}
$('#cq').addEventListener('input',cqRender);
$('#cq').addEventListener('keydown',e=>{if(e.key==='ArrowDown'){const b=$('#cq-r .cq-p');if(b){e.preventDefault();b.focus()}}else if(e.key==='Enter'){const b=$('#cq-r .cq-p');if(b){e.preventDefault();b.click()}}});
$('#cq-r').addEventListener('keydown',e=>{const li=e.target.closest('.cq-i');if(!li)return;const L=[...$$('#cq-r .cq-p')],i=L.indexOf(li.querySelector('.cq-p'));
 if(e.key==='ArrowDown'&&L[i+1]){e.preventDefault();L[i+1].focus()}else if(e.key==='ArrowUp'){e.preventDefault();(L[i-1]||$('#cq')).focus()}});
$('#cq-r').addEventListener('dragstart',e=>{const li=e.target.closest('.cq-i');if(li){e.dataTransfer.setData('text/plain',li.dataset.c);e.dataTransfer.effectAllowed='copy'}});
$('#cq-r').addEventListener('click',e=>{const b=e.target.closest('button'),li=e.target.closest('.cq-i');if(!b||!li)return;const code=li.dataset.c,s=BY[code]||[code,''];
 if(b.dataset.a==='o'){cqOpen(code);return}
 if(e.detail===0){const d=days()[0];qpOpen(iso(mode==='d'?d:new Date(Math.max(d,new Date().setHours(0,0,0,0)))),8*60,+$('#dur').value,code);return}
 sel=code;renderList();cqRender();calSay('« '+s[0]+' · '+s[1]+' » est prêt : cliquez ou touchez une plage du calendrier pour le placer, ou glissez-le.')});
/* Fenêtre de création rapide */
[15,30,45,60,75,90,120,150,180,240].forEach(m=>{const o=document.createElement('option');o.value=m;o.textContent=m<60?m+' min':Math.floor(m/60)+' h'+(m%60?' '+m%60:'');$('#qp-d').appendChild(o)});
$('#qp-a').innerHTML=$('#act').innerHTML;
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
$('#qp-q').addEventListener('input',()=>{qpCode=null;qpRender()});
$('#qp-q').addEventListener('keydown',e=>{if(e.key==='Enter'){const b=$('#qp-r .cq-p');if(b){e.preventDefault();b.click()}}else if(e.key==='ArrowDown'){const b=$('#qp-r .cq-p');if(b){e.preventDefault();b.focus()}}});
$('#qp-r').addEventListener('click',e=>{const li=e.target.closest('.cq-i');if(!li)return;qpCode=li.dataset.c;qpCreate()});
$('#qp-ok').onclick=qpCreate;$('#qp-no').onclick=qpClose;
$('#qp').addEventListener('keydown',e=>{if(e.key==='Escape'){qpClose();e.stopPropagation()}});
document.addEventListener('click',e=>{if(!$('#qp').hidden&&!e.target.closest('#qp,#grid,#cq-r'))qpClose()});
/* Clic, plage, déplacement et durée */
function calSupp(){calSup=true;setTimeout(()=>{calSup=false},120)}
$('#grid').addEventListener('click',e=>{if(calSup){calSup=false;return}const b=e.target.closest('.blk');if(b){openEdit(b.dataset.id);return}const c=e.target.closest('.col');if(!c)return;
 if(sel){addAt(c,e.clientY,sel);sel=null;renderList();cqRender();return}qpOpen(c.dataset.d,calMin(c,e.clientY,'f'),+$('#dur').value,null,e.clientX,e.clientY)});
$('#grid').addEventListener('pointerdown',e=>{if(e.button>0||calP)return;const c=e.target.closest('.col');if(!c)return;const rz=e.target.closest('.rz'),b=e.target.closest('.blk');
 if(b){const x=S.seances[b.dataset.id];if(!x)return;const touch=e.pointerType!=='mouse';
  calP={k:rz?'rz':'mv',b,id:b.dataset.id,x0:e.clientX,y0:e.clientY,off:e.clientY-b.getBoundingClientRect().top,on:false,touch,ok:!touch||!!rz,start:x.start,dur:x.dur,date:x.date,pid:e.pointerId};
  if(!touch)e.preventDefault();if(rz)clearTimeout(lpT);
  if(touch&&!rz)calP.t=setTimeout(()=>{if(calP&&!calP.on){calP.ok=true;clearTimeout(lpT);b.classList.add('grab');try{navigator.vibrate&&navigator.vibrate(15)}catch(_){}}},300);return}
 if(e.pointerType==='mouse'){e.preventDefault();calP={k:'rg',c,x0:e.clientX,y0:e.clientY,m0:calMin(c,e.clientY,'f'),on:false,ok:true,pid:e.pointerId}}});
function calRange(P,y){const cm=calMin(P.c,y,'f');return [Math.min(P.m0,cm),Math.min(H1*60,Math.max(P.m0,cm)+15)]}
addEventListener('pointermove',e=>{const P=calP;if(!P||e.pointerId!==P.pid)return;
 if(!P.on){if(Math.hypot(e.clientX-P.x0,e.clientY-P.y0)<5)return;if(!P.ok){clearTimeout(P.t);calP=null;return}P.on=true;clearTimeout(lpT);if(P.b)P.b.classList.add('drag')}
 e.preventDefault();
 if(P.k==='rg'){const [a,z]=calRange(P,e.clientY);let r=P.c.querySelector('.rng');if(!r){r=document.createElement('div');r.className='rng';P.c.appendChild(r)}r.style.top=(a-H0*60)/60*PX+'px';r.style.height=(z-a)/60*PX+'px';r.textContent=hm(a)+' – '+hm(z);return}
 const code=(BY[S.seances[P.id]?.ssp]||[''])[0];
 if(P.k==='mv'){const el=document.elementFromPoint(e.clientX,e.clientY),c=el&&el.closest('#grid .col');if(!c)return;if(P.b.parentNode!==c)c.appendChild(P.b);
  P.start=Math.min(calMin(c,e.clientY-P.off,'r'),H1*60-P.dur);P.date=c.dataset.d;P.b.style.top=(P.start-H0*60)/60*PX+'px';P.b.querySelector('b').textContent=hm(P.start)+' · '+code}
 else{P.dur=Math.max(15,Math.min(H1*60-P.start,calMin(P.b.parentNode,e.clientY,'r')-P.start));P.b.style.height=Math.max(12,P.dur/60*PX-2)+'px';P.b.querySelector('.du').textContent=P.dur+'′'}},{passive:false});
addEventListener('pointerup',e=>{const P=calP;if(!P||e.pointerId!==P.pid)return;clearTimeout(P.t);calP=null;if(P.b)P.b.classList.remove('drag','grab');if(!P.on)return;calSupp();
 if(P.k==='rg'){const [a,z]=calRange(P,e.clientY),r=P.c.querySelector('.rng');if(r)r.remove();qpOpen(P.c.dataset.d,a,z-a,null,e.clientX,e.clientY);return}
 const x=S.seances[P.id];if(!x)return renderGrid();Object.assign(x,{date:P.date,start:P.start,dur:P.dur,maj:new Date().toISOString()});put('seances',P.id,x);renderAll();
 calSay(P.k==='mv'?'La séance « '+x.ssp+' » est déplacée au '+calLab(x)+'.':'La séance « '+x.ssp+' » dure maintenant '+x.dur+' minutes.')});
addEventListener('pointercancel',e=>{const P=calP;if(!P||e.pointerId!==P.pid)return;clearTimeout(P.t);calP=null;if(P.on){const r=P.c&&P.c.querySelector('.rng');if(r)r.remove();renderGrid()}else if(P.b)P.b.classList.remove('grab')});
document.addEventListener('touchmove',e=>{if(calP&&calP.ok&&calP.touch)e.preventDefault()},{passive:false});
/* Clavier : flèches = déplacer de 15 min ou d’un jour ; Maj + flèches = durée ; Entrée = détails */
$('#grid').addEventListener('keydown',e=>{const b=e.target.closest('.blk');if(!b||e.ctrlKey||e.metaKey||e.altKey)return;const id=b.dataset.id,x=S.seances[id];if(!x)return;
 if(e.key==='Enter'){e.preventDefault();openEdit(id);return}
 const K={ArrowUp:-15,ArrowDown:15}[e.key],D={ArrowLeft:-1,ArrowRight:1}[e.key];if(K==null&&D==null)return;e.preventDefault();
 if(K!=null&&e.shiftKey)x.dur=Math.max(15,Math.min(H1*60-x.start,x.dur+K));else if(K!=null)x.start=Math.max(H0*60,Math.min(H1*60-x.dur,x.start+K));else{const d=parse(x.date);d.setDate(d.getDate()+D);x.date=iso(d)}
 x.maj=new Date().toISOString();put('seances',id,x);if(!days().some(d=>iso(d)===x.date))cur=parse(x.date);renderAll();const n=$('#grid .blk[data-id="'+id+'"]');if(n)n.focus();
 calSay('La séance « '+x.ssp+' » commence le '+calLab(x)+' et dure '+x.dur+' minutes.')});
