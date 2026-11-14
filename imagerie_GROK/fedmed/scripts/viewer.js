window.GM=(function(){
"use strict";
var ESC={"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"};
function esc(s){return String(s==null?"":s).replace(/[&<>"']/g,function(c){return ESC[c];});}
function svgEl(nom){return document.createElementNS("http://www.w3.org/2000/svg",nom);}
function srcDe(en,cote){
 var im=en.images||{},b=im[cote];
 if(!b||typeof b.fichier!=="string"||b.fichier.indexOf("data:")!==0)return "";
 return b.fichier;
}
function demo(info){
 info=info||{};
 if(info.age&&info.sexe)return esc(info.age)+" · "+esc(info.sexe);
 if(info.age)return esc(info.age)+" · sexe non documenté";
 if(info.sexe)return "âge non documenté · "+esc(info.sexe);
 return "âge/sexe non documentés";
}
function metaLigne(info){
 info=info||{};
 var bits=[demo(info)];
 var s=info.source||{};
 var pop=[s.auteur,s.licence,s.url,s.credit].filter(Boolean).map(esc).join(" — ");
 bits.push('<span class="gm-src" tabindex="0">Source'+(pop?'<span class="gm-pop">'+pop+"</span>":"")+"</span>");
 return bits.join(" · ");
}
function visuel(cote,info,patho,src){
 var titre=patho?"Pathologique":"Normal";
 if(info.refus)return '<div class="gm-ph"><b>Image non affichée</b><p>'+esc(info.refus)+"</p></div>";
 if(!src)return '<div class="gm-ph"><b>'+(patho?"Image pathologique absente":"Normale absente")+"</b></div>";
 return '<div class="gm-zw"><img class="gm-img" alt="'+esc(titre)+'" draggable="false"><svg class="gm-svg masque" viewBox="0 0 1000 1000" preserveAspectRatio="none"></svg></div>';
}
function panneau(cote,info,patho,src){
 info=info||{};
 var act=patho?'<button type="button" class="gm-btn" data-act="indice">Indice</button>':'<button type="button" class="gm-btn" data-act="anat" aria-pressed="false">Anatomie</button>';
 return '<section class="gm-pan '+(patho?"p":"n")+'" data-cote="'+cote+'"><h3>'+(patho?"Pathologique":"Normal")+" "+act+'</h3><div class="gm-fig">'+visuel(cote,info,patho,src)+'<div class="gm-zoom"><button type="button" data-z="plus" aria-label="Zoom avant">+</button><button type="button" data-z="moins" aria-label="Zoom arrière">−</button><button type="button" data-z="zero" aria-label="Remise à zéro du zoom">⟲</button></div></div><p class="gm-struct" hidden></p><p class="gm-meta">'+metaLigne(info)+"</p></section>";
}
function trait(parent,points,couleur,classe,pointille){
 var halo=svgEl("polyline"),lin=svgEl("polyline");
 var pts=points.map(function(p){return (p[0]*1000)+","+(p[1]*1000);}).join(" ");
 [halo,lin].forEach(function(el){
  el.setAttribute("points",pts);el.setAttribute("fill","none");
  el.setAttribute("class",classe);el.setAttribute("stroke-linejoin","round");el.setAttribute("stroke-linecap","round");
  el.style.vectorEffect="non-scaling-stroke";
 });
 halo.setAttribute("stroke","#061018");halo.style.strokeWidth="6px";
 lin.setAttribute("stroke",couleur);lin.style.strokeWidth="2.6px";
 if(pointille){halo.style.strokeDasharray="8 6";lin.style.strokeDasharray="8 6";}
 parent.appendChild(halo);parent.appendChild(lin);
}
function cercle(parent,pt,couleur,classe){
 [6,2.6].forEach(function(w,i){
  var c=svgEl("circle");
  c.setAttribute("cx",pt[0]*1000);c.setAttribute("cy",pt[1]*1000);c.setAttribute("r",28);
  c.setAttribute("fill","none");c.setAttribute("class",classe+(i?" lin":" halo"));
  c.setAttribute("stroke",i?couleur:"#061018");
  c.style.vectorEffect="non-scaling-stroke";c.style.strokeWidth=(i?2.6:6)+"px";c.style.strokeDasharray="8 6";
  parent.appendChild(c);
 });
}
function dessiner(svg,info,lesions){
 if(!svg)return;
 while(svg.firstChild)svg.removeChild(svg.firstChild);
 (info.structures||[]).forEach(function(st){
  if(!st.contour||st.contour.length<3)return;
  var g=svgEl("g");
  g.setAttribute("class","st-g");g.dataset.sid=st.id;
  var halo=svgEl("polygon"),lin=svgEl("polygon");
  var pts=st.contour.map(function(p){return (p[0]*1000)+","+(p[1]*1000);}).join(" ");
  [halo,lin].forEach(function(el){el.setAttribute("points",pts);el.dataset.sid=st.id;el.style.vectorEffect="non-scaling-stroke";});
  halo.setAttribute("class","st halo");halo.setAttribute("stroke","#061018");
  lin.setAttribute("class","st lin");lin.setAttribute("stroke",st.couleur||"#fff");lin.setAttribute("fill",st.couleur||"#fff");
  g.appendChild(halo);g.appendChild(lin);svg.appendChild(g);
 });
 (lesions||[]).forEach(function(L,i){
  var g=svgEl("g");
  g.setAttribute("class","arw");g.dataset.i=String(i);g.dataset.sid="lesion-"+i;
  var col=L.couleur||"#FF1744";
  if(L.contour&&L.contour.length>=3)trait(g,L.contour,col,"band",true);
  else if(L.tip)cercle(g,L.tip,col,"band");
  if(L.tip&&L.from){
   var x1=L.from[0]*1000,y1=L.from[1]*1000,x2=L.tip[0]*1000,y2=L.tip[1]*1000;
   [6,2.6].forEach(function(w,k){
    var ln=svgEl("line");
    ln.setAttribute("x1",x1);ln.setAttribute("y1",y1);ln.setAttribute("x2",x2);ln.setAttribute("y2",y2);
    ln.setAttribute("stroke",k?col:"#061018");ln.style.vectorEffect="non-scaling-stroke";ln.style.strokeWidth=w+"px";
    g.appendChild(ln);
   });
  }
  svg.appendChild(g);
 });
}
function numeros(zw,lesions){
 zw.querySelectorAll(".gm-num,.gm-etq").forEach(function(n){n.remove();});
 (lesions||[]).forEach(function(L,i){
  if(!L.from)return;
  var b=document.createElement("button");
  b.type="button";b.className="gm-num";b.textContent=String(i+1);
  b.style.left=(L.from[0]*100)+"%";b.style.top=(L.from[1]*100)+"%";
  b.dataset.i=String(i);
  b.setAttribute("aria-label","Repère "+(i+1)+" "+(L.label||""));
  zw.appendChild(b);
 });
}
function libelle(st){
 var nom=st.nom||"Structure";
 var aspect=(st.aspect||"").replace(/\(?\s*contour approximatif[\s\S]*$/i,"").replace(/\s+/g," ").trim();
 var html="<b>"+esc(nom)+"</b>";
 if(aspect)html+=" — "+esc(aspect);
 if(st.approximatif)html+=' <i class="gm-approx">contour automatique approximatif</i>';
 return html;
}
function legende(g){
 var vus={},rows="";
 ["normal","patho"].forEach(function(cote){
  (((g[cote]||{}).structures)||[]).forEach(function(st){if(st.id&&!vus[st.id])vus[st.id]=st;});
 });
 Object.keys(vus).forEach(function(id){
  var st=vus[id];
  rows+='<li><i style="background:'+esc(st.couleur)+'"></i><span>'+libelle(st)+"</span></li>";
 });
 var les="";
 (((g.patho||{}).lesions)||[]).forEach(function(L,i){
  les+='<li><i class="pointille" style="border-color:'+esc(L.couleur||"#FF1744")+'"></i><span><b>'+(i+1)+". "+esc(L.label||"Lésion")+"</b>"+(L.semio?" — "+esc(L.semio):"")+"</span></li>";
 });
 return (rows||"<p>Aucune structure anatomique tracée sur ce cliché.</p>")+(les?'<h3>Lésions</h3><ul>'+les+"</ul>":"");
}
function render(root,en){
 if(!root||!en||!en.gabarit)return;
 var g=en.gabarit;
 var srcN=srcDe(en,"normal"),srcP=srcDe(en,"patho");
 var cartes=(g.cartes||[]).map(function(c){return '<article class="gm-carte"><h3>'+esc(c.titre)+"</h3><p>"+esc(c.texte)+"</p></article>";}).join("");
 var sig=(g.signaux&&g.signaux.length)?'<article class="gm-carte gm-signal"><h3>Images signalées</h3><p>'+g.signaux.map(esc).join(" ")+"</p></article>":"";
 root.classList.add("fleches-off");
 root.innerHTML='<div class="gm-barre"><button type="button" class="gm-btn" data-act="fleches" aria-pressed="false">Révéler les flèches</button><button type="button" class="gm-btn" data-act="lie" aria-pressed="false">Zoom lié</button><button type="button" class="gm-btn" data-act="code" aria-pressed="false">Rappel du code couleur structure – aspect</button><button type="button" class="gm-btn" data-act="defi" aria-pressed="false">Mode défi</button></div><div class="gm-pair">'+panneau("normal",g.normal,false,srcN)+panneau("patho",g.patho,true,srcP)+'</div><section class="gm-code" hidden><h3>Code couleur — structure et aspect</h3><div class="gm-code-corps"></div></section>'+cartes+sig+'<p class="gm-indice" aria-live="polite"></p>';
 root.querySelector(".gm-code-corps").innerHTML=legende(g);
 var etat={lie:false,defi:false,hint:0,step:0,revele:false,actif:-1};
 var zooms=[];
 root.querySelectorAll(".gm-pan").forEach(function(pan){
  var cote=pan.dataset.cote;
  var info=(cote==="patho"?g.patho:g.normal)||{};
  var svg=pan.querySelector(".gm-svg");
  var img=pan.querySelector(".gm-img");
  var zw=pan.querySelector(".gm-zw");
  if(img){
   img.src=cote==="patho"?srcP:srcN;
   dessiner(svg,info,cote==="patho"?((g.patho||{}).lesions||[]):[]);
   if(zw&&cote==="patho")numeros(zw,(g.patho||{}).lesions||[]);
  }
  var z=1;
  function apply(){if(zw)zw.style.transform="scale("+z+")";}
  function setZ(v){z=Math.max(1,Math.min(4,v));if(z===1)z=1;apply();if(etat.lie)zooms.forEach(function(o){if(o!==api)o.write(z);});}
  var api={write:function(v){z=v;apply();}};
  zooms.push(api);
  pan.querySelector('[data-z="plus"]').onclick=function(){setZ(z*1.25);};
  pan.querySelector('[data-z="moins"]').onclick=function(){setZ(z/1.25);};
  pan.querySelector('[data-z="zero"]').onclick=function(){z=1;apply();if(etat.lie)zooms.forEach(function(o){o.write(1);});};
 });
 function masque(off){
  root.classList.toggle("fleches-off",off);
  root.querySelectorAll(".gm-svg").forEach(function(svg){svg.classList.toggle("masque",off);});
 }
 function choisir(i){
  etat.actif=i;
  root.querySelectorAll(".arw").forEach(function(n){n.classList.toggle("on",Number(n.dataset.i)===i);});
  root.querySelectorAll(".gm-etq").forEach(function(n){n.remove();});
  var L=((g.patho||{}).lesions||[])[i];
  var zw=root.querySelector('[data-cote="patho"] .gm-zw');
  if(L&&zw){
   var e=document.createElement("div");e.className="gm-etq";e.textContent=(i+1)+". "+(L.label||"Lésion");
   zw.appendChild(e);
   var p=root.querySelector('[data-cote="patho"] .gm-struct');
   if(p){p.hidden=false;p.textContent=(L.label||"Lésion")+(L.semio?" — "+L.semio:"");}
  }
 }
 function allumer(id){
  root.querySelectorAll(".st").forEach(function(el){el.classList.toggle("lit",!!id&&el.dataset.sid===id);});
  ["normal","patho"].forEach(function(cote){
   var info=(g[cote]||{});
   var st=((info.structures)||[]).filter(function(s){return s.id===id;})[0];
   var p=root.querySelector('[data-cote="'+cote+'"] .gm-struct');
   if(!p)return;
   if(!st){if(!id)p.hidden=true;return;}
   p.hidden=false;
   p.innerHTML=libelle(st);
  });
 }
 root.querySelectorAll(".st").forEach(function(el){
  el.addEventListener("pointerenter",function(){allumer(el.dataset.sid);});
  el.addEventListener("pointerleave",function(){allumer("");});
 });
 root.addEventListener("click",function(ev){
  var num=ev.target.closest(".gm-num");
  if(num){choisir(Number(num.dataset.i));return;}
  var act=ev.target.closest("[data-act]");
  if(!act)return;
  var k=act.dataset.act;
  if(k==="fleches"){
   if(etat.defi&&!etat.revele)return;
   var off=act.getAttribute("aria-pressed")==="true";
   act.setAttribute("aria-pressed",off?"false":"true");
   masque(off);
   if(!off)choisir(etat.actif<0?0:etat.actif);
  }else if(k==="lie"){
   etat.lie=act.getAttribute("aria-pressed")!=="true";
   act.setAttribute("aria-pressed",etat.lie?"true":"false");
  }else if(k==="code"){
   var on=act.getAttribute("aria-pressed")!=="true";
   act.setAttribute("aria-pressed",on?"true":"false");
   root.querySelector(".gm-code").hidden=!on;
  }else if(k==="defi"){
   etat.defi=!etat.defi;etat.hint=0;etat.revele=false;
   act.setAttribute("aria-pressed",etat.defi?"true":"false");
   act.textContent=etat.defi?"Quitter le défi":"Mode défi";
   masque(true);
   root.querySelector('[data-act="fleches"]').setAttribute("aria-pressed","false");
   root.querySelector(".gm-indice").textContent=etat.defi?"Défi : les flèches sont cachées. Demandez un indice.":"";
  }else if(k==="indice"){
   if(!etat.defi){etat.defi=true;var b=root.querySelector('[data-act="defi"]');b.setAttribute("aria-pressed","true");b.textContent="Quitter le défi";masque(true);}
   var inds=g.indices||[];
   var zone=root.querySelector(".gm-indice");
   if(etat.hint<inds.length){zone.textContent=inds[etat.hint++];}
   else{etat.revele=true;masque(false);root.querySelector('[data-act="fleches"]').setAttribute("aria-pressed","true");choisir(0);zone.textContent="Révélé.";}
  }else if(k==="anat"){
   var couches=[];
   ["normal","patho"].forEach(function(cote){((g[cote]||{}).structures||[]).forEach(function(st){couches.push(st.ordre||1);});});
   var max=couches.length?Math.max.apply(null,couches):0;
   if(!max){root.querySelector(".gm-indice").textContent="Anatomie indisponible : aucun contour de structure sur ce cliché.";return;}
   etat.step=etat.step>=max?0:etat.step+1;
   act.setAttribute("aria-pressed",etat.step?"true":"false");
   root.querySelectorAll(".st").forEach(function(el){
    var sid=el.dataset.sid,ordre=1;
    ["normal","patho"].forEach(function(cote){((g[cote]||{}).structures||[]).forEach(function(st){if(st.id===sid)ordre=st.ordre||1;});});
    el.classList.toggle("anat",etat.step&&ordre<=etat.step);
   });
  }
 });
}
return {render:render};
})();
