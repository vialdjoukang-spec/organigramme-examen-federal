import os, sys
# Patch 0008 · Asclépios · 17.10.2026 · examen physique : 3 axes, sous-régions, phases, croquis, renvois, TIP « Examen physique ciblé » structuré.
# Rejeu : APP_FILE=app_v2.html python3 tools/patches/0008-asclepios-examen.py (jamais sur orig/app.html). Données : data/GES.json, data/TIP.json (json_inject).
p=os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
assert not p.endswith('orig/app.html'), 'Interdit I1'
s=open(p,encoding='utf-8').read()
if 'function exFmt(' in s: sys.exit('0008 déjà appliqué')
def rep(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:90],c); s=s.replace(a,b)
# 1. progression : clé stable it.k (les gestes ont été réordonnés)
rep("const k=r.items.filter((_,i)=>GS[r.id+'_'+i]).length;return `<button class=\"${r.id===GREG&&!q?'on':''}\" data-r=\"${r.id}\">${esc(r.r)} · ${k}/${r.items.length}</button>`}).join('');",
    "const k=r.items.filter((it,i)=>GS[gK(r,it,i)]).length;return `<button class=\"${r.id===GREG&&!q?'on':''}\" data-r=\"${r.id}\">${esc(r.r)} · ${k}/${r.items.length}</button>`}).join('')+'</div>').join('');")
rep("$('#g-reg').innerHTML=GES.map(r=>{",
    "$('#g-reg').innerHTML=['reg','sys','pop'].map(a=>`<div class=\"ex-axe\" data-ax=\"${a}\"><span class=\"ex-axe__h\">${EXAX[a]}</span>`+GES.filter(r=>(r.ax||'reg')===a).map(r=>{")
rep("(!todo||!GS[r.id+'_'+i])","(!todo||!GS[gK(r,it,i)])")
rep("+L.map(([it,i])=>{const k=r.id+'_'+i;return `<label class=\"gr${GS[k]?' ok':''}\"",
    "+(q?L.map(([it,i])=>gRow(r,it,i)).join(''):gGroup(r,L,gRow))});\n function gRow(r,it,i){const k=gK(r,it,i);return `<label class=\"gr${GS[k]?' ok':''}\"")
rep("<p class=\"i\">${esc(it.n)}</p></label>`}).join('')});",
    "<p class=\"i\">${esc(it.n)}</p>${it.av?`<small class=\"ex-av\">À vérifier · ${esc(it.av)}</small>`:''}${it.x?`<nav class=\"ex-xref\" aria-label=\"Renvois\">${it.x.map(([rid,t])=>`<button type=\"button\" class=\"ex-chip\" data-gx=\"${rid}|${esc(t)}\">→ ${esc((GES.find(g=>g.id===rid)||{}).r||rid)} · ${esc(t)}</button>`).join('')}</nav>`:''}</label>`}")
# 2. fonctions de l'examen (avant renderGes)
rep("function renderGes(){",
"""const EXAX={reg:'Régions anatomiques',sys:'Systèmes et modules transversaux',pop:'Populations'},EXPO={'Inspection':1,'Palpation':2,'Percussion':3,'Auscultation':4,'Mobilisation':5,'Tests spéciaux':6,'Mesures':'M','Neurologique':'N'};
function gK(r,it,i){return it.k||r.id+'_'+i}
function gFig(f){return f?`<figure class="ex-fig"><img src="${esc(f.f)}" alt="${esc(f.c)}" width="${f.w}" height="${f.h}" loading="lazy" decoding="async"><figcaption class="ex-fig__cap">${esc(f.c)}<small class="ex-fig__credit">${esc(f.cr)} · <a href="${esc(f.u)}" target="_blank" rel="noopener">page source</a></small></figcaption></figure>`:''}
function gGroup(r,L,row){let o=gFig(r.fig),cs=null,cp=null;L.forEach(([it,i])=>{const sr=it.sr||r.r;if(sr!==cs){if(cs!==null)o+='</section>';o+=`<section class="ex-region" data-reg="${r.id}"><h3 class="ex-region__h">${esc(sr)}</h3>`;cs=sr;cp=null}if(it.p!==cp){o+=`<h4 class="ex-phase" data-ordre="${EXPO[it.p]||''}">${esc(it.p)}</h4>`;cp=it.p}o+=row(r,it,i)});return o+(cs!==null?'</section>':'')}
function exFmt(s){if(!s||!(s[0]==='§'||/\\n@/.test(s)))return s;const PN={'1':'Inspection','2':'Palpation','3':'Percussion','4':'Auscultation','5':'Mobilisation','6':'Tests spéciaux','M':'Mesures','N':'Neurologique'},RL={membres:'Membres et articulations',neuro:'Neurologique',autres:'Autres éléments ciblés'};let o='',op=false,ul=false;const cl=()=>{if(ul){o+='</ul>';ul=false}};
 s.split('\\n').forEach(l=>{const c=l[0],v=l.slice(1).trim();
  if(c==='§'){cl();if(op)o+='</section>';const g=GES.find(r=>r.id===v);o+=`<section class="ex-region" data-reg="${esc(v)}"><h3 class="ex-region__h">${esc(RL[v]||(g&&g.r)||v)}</h3>`;op=true}
  else if(c==='¶'){cl();if(PN[v])o+=`<h4 class="ex-phase" data-ordre="${v}">${PN[v]}</h4>`}
  else if(c==='@'){cl();o+='<nav class="ex-xref" aria-label="Gestes liés">'+v.split(' ').filter(Boolean).map(t=>{if(t.startsWith('r:')){const g=GES.find(r=>r.id===t.slice(2));return g?`<button type="button" class="ex-chip" data-gx="${g.id}|">Gestes · ${esc(g.r)}</button>`:''}for(const g of GES){const it=g.items.find(x=>x.k===t);if(it)return `<button type="button" class="ex-chip" data-gx="${g.id}|${esc(it.k)}">${esc(it.s)}</button>`}return ''}).join('')+'</nav>'}
  else if(l.startsWith('• ')){if(!ul){o+='<ul class="ex-items">';ul=true}o+='<li>'+l.slice(2)+'</li>'}
  else if(l.trim()){cl();o+='<p>'+l+'</p>'}});cl();if(op)o+='</section>';return o}
function gGo(rid,key){const r=GES.find(x=>x.id===rid);if(!r)return;if(typeof hideTip==='function')hideTip(true);GREG=rid;$('#g-q').value='';$('#g-ph').value='';$('#g-todo').checked=false;$$('.tab').find(t=>t.dataset.v==='ges').click();renderGes();let el=null;if(key){const i=r.items.findIndex(it=>it.k===key||it.s===key);if(i>=0)el=$(`#g-list [data-t="g|${rid}|${i}"]`)}(el||$('#g-head')).scrollIntoView({block:el?'center':'start'});if(el){el.classList.add('ex-flash');setTimeout(()=>el.classList.remove('ex-flash'),1800)}}
document.addEventListener('click',e=>{const b=e.target.closest('[data-gx]');if(!b)return;e.preventDefault();e.stopImmediatePropagation();const x=b.dataset.gx,j=x.indexOf('|');gGo(x.slice(0,j),x.slice(j+1));setTimeout(()=>{if(typeof hideTip==='function')hideTip(true)},0)},true);
function renderGes(){""")
# 3. fenêtre : rendu structuré du champ 5 et sources propres aux gestes ajoutés
rep("if(b[0]==='c'){ti=CLIN[i];h=T.c[i];src=T.s}","if(b[0]==='c'){ti=CLIN[i];h=i===5?exFmt(T.c[i]):T.c[i];src=T.s}")
rep("src:'OFSP, Exigences MED 2026, § 5.1.4 : seuls les gestes et mesures corrects rapportent des points, sans point négatif · PROFILES 2023, EPA 2'}}",
    "src:(it.src?it.src+' · ':'')+'OFSP, Exigences MED 2026, § 5.1.4 : seuls les gestes et mesures corrects rapportent des points, sans point négatif · PROFILES 2023, EPA 2'}}")
# 4. CSS de base (Apollon fournit le style premium ; ces règles ne servent que de socle)
rep("#tip img{max-width:100%;height:auto}",
    "#tip img{max-width:100%;height:auto}\n.ex-axe{display:contents}.ex-axe__h{flex-basis:100%;margin:8px 0 2px;font:700 .68rem var(--fb);letter-spacing:.12em;text-transform:uppercase;color:var(--mut)}.ex-region{margin:10px 0}.ex-region__h{margin:6px 0;font-size:1rem}.ex-phase{margin:8px 0 2px;font-size:.74rem;letter-spacing:.08em;text-transform:uppercase}.ex-items{margin:2px 0 6px;padding-left:1.1em}.ex-fig{margin:6px 0;text-align:center}.ex-fig img{max-width:min(100%,520px);height:auto;background:#fff}.ex-fig__credit{display:block;font-size:.72rem;color:var(--mut)}.ex-xref{display:flex;flex-wrap:wrap;gap:6px;margin:4px 0}.ex-chip{min-height:28px;padding:3px 10px;border-radius:99px;border:1px solid var(--line);background:var(--soft);color:var(--ink);font:600 .76rem var(--fb);cursor:pointer}.ex-av{display:block;margin-top:2px;font-size:.74rem;color:var(--warn)}.ex-flash{outline:2px solid var(--gold);outline-offset:2px}")
open(p,'w',encoding='utf-8').write(s); print('0008 appliqué')
