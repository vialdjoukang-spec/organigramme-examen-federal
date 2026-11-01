(function(){
var KEY="%%KEY%%",FK="%%KEY%%_fire",st={},fire={};
try{st=JSON.parse(localStorage.getItem(KEY))||{}}catch(e){}try{fire=JSON.parse(localStorage.getItem(FK))||{}}catch(e){}
var qs=[].slice.call(document.querySelectorAll('.qcm')),N=qs.length,map={"Raisonner":"R","Discriminer":"D","Pièges & alarmes":"P"};
function save(){try{localStorage.setItem(KEY,JSON.stringify(st));localStorage.setItem(FK,JSON.stringify(fire))}catch(e){}}
// Marque juste/faux sur les options — n'ouvre JAMAIS le commentaire
function lock(a,pick){var c=a.dataset.c;a.classList.add('locked');
 a.querySelectorAll('.opt').forEach(function(o){var k=o.dataset.k,i=o.querySelector('input');i.disabled=true;
  if(k===c)o.classList.add('good');if(pick&&k===pick&&k!==c)o.classList.add('bad');if(k===pick)i.checked=true;});
 var r=a.querySelector('.res');
 if(!pick){r.className="res";r.textContent="Commentaire ouvert sans réponse : non compté.";}
 else if(pick===c){r.className="res v1";r.textContent="✔ Juste — touchez 💡 pour le commentaire.";}
 else{r.className="res v0";r.textContent="✘ Faux — touchez 💡 pour comprendre.";}}
function upd(){var ok=0,done=0,b={R:[0,0],D:[0,0],P:[0,0]},n={ex:[0,0],ap:[0,0],spe:[0,0]},sp={};
 qs.forEach(function(a){var s=st[a.id],g=map[a.dataset.bloc],v=a.dataset.niv,z=a.dataset.spe;b[g][1]++;n[v][1]++;
  if(z){sp[z]=sp[z]||{ok:0,n:0,f:0};if(fire[a.id])sp[z].f++;}
  if(s&&s!=="?"){done++;if(z)sp[z].n++;if(s===a.dataset.c){ok++;b[g][0]++;n[v][0]++;if(z)sp[z].ok++;}}
  var fb=a.querySelector('.fire');if(fb){fb.classList.toggle('on',!!fire[a.id]);fb.setAttribute('aria-pressed',fire[a.id]?"true":"false");}});
 document.getElementById('ndone').textContent=done;document.getElementById('nok').textContent=ok;
 document.getElementById('pct').textContent=done?Math.round(100*ok/done)+" %":"–";
 document.getElementById('pbar').style.width=(100*done/N)+"%";
 document.getElementById('s-all').textContent=ok+"/"+N;
 ["R","D","P"].forEach(function(g){document.getElementById('s-'+g).textContent=b[g][0]+"/"+b[g][1]});
 ["ex","ap","spe"].forEach(function(v){document.getElementById('s-'+v).textContent=n[v][0]+"/"+n[v][1]});
 var best=null;document.querySelectorAll('table.spe tr[data-spe]').forEach(function(tr){var z=tr.dataset.spe,d=sp[z]||{ok:0,n:0,f:0};
  tr.querySelector('.c').textContent=d.ok+"/"+d.n;tr.querySelector('.f').textContent=d.f?("🔥".repeat(d.f)):"0";
  var sc=d.f*10+(d.n?d.ok/d.n:0);if(d.f&&(!best||sc>best.s))best={z:z,s:sc};});
 document.getElementById('exalt').textContent=best?("🔥 Spécialité qui vous exalte (pour l'instant) : "+best.z):"Touchez 🔥 sur les questions SPE qui vous passionnent : la spécialité qui vous exalte apparaîtra ici.";
 var v=document.getElementById('verdict');if(done===N){var p=ok/N;v.className="verdict "+(p>=.6?"v1":"v0");
  v.textContent=p>=.85?"%%VERDICT%% acquis. Refaire dans 7 jours pour l'ancrer.":p>=.6?"Bonne base. Relire les 💡 ratés et refaire le niveau le plus faible.":"Relire la carte et l'algorithme, puis refaire la série demain.";}else v.textContent="";}
qs.forEach(function(a){
 a.querySelectorAll('input').forEach(function(i){i.addEventListener('change',function(){if(a.classList.contains('locked'))return;st[a.id]=i.value;save();lock(a,i.value);upd();});});
 a.querySelector('.reveal').addEventListener('toggle',function(){if(this.open&&!st[a.id]){st[a.id]="?";save();lock(a,null);upd();}});
 var fb=a.querySelector('.fire');if(fb)fb.addEventListener('click',function(){fire[a.id]=!fire[a.id];if(!fire[a.id])delete fire[a.id];save();upd();});
 a.querySelector('.reveal').open=false;
 if(st[a.id])lock(a,st[a.id]==="?"?null:st[a.id]);});
// Filtres de niveau
document.querySelectorAll('.filt button').forEach(function(bt){bt.addEventListener('click',function(){var f=bt.dataset.f;
 document.querySelectorAll('.filt button').forEach(function(x){x.classList.toggle('on',x===bt)});
 qs.forEach(function(a){a.classList.toggle('hide',f!=="all"&&a.dataset.niv!==f)});});});
// Mode révision explicite (confirmation)
var rev=false,rb=document.getElementById('revbtn');
rb.addEventListener('click',function(){
 if(!rev){if(!confirm("Mode révision : ouvrir TOUS les commentaires ?\nLes questions non répondues seront verrouillées et non comptées."))return;
  qs.forEach(function(a){if(!st[a.id]){st[a.id]="?";lock(a,null)}a.querySelector('.reveal').open=true});save();upd();rev=true;rb.textContent="✖ Quitter le mode révision";}
 else{qs.forEach(function(a){a.querySelector('.reveal').open=false});rev=false;rb.textContent="📖 Mode révision";}});
document.getElementById('resetbtn').addEventListener('click',function(){if(!confirm("Effacer toutes les réponses et les 🔥 ?"))return;st={};fire={};save();location.reload();});
upd();})();