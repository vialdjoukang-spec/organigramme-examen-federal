#!/usr/bin/env python3
"""Icônes Lucide et libellés entiers. Ne change aucune couleur : les thèmes et la bande EYE SPOT restent ceux de main."""
import os, re, json, base64

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)


def _svg_inner(path):
    raw = open(path, encoding='utf-8').read()
    inner = re.sub(r'^.*?<svg[^>]*>', '', raw, flags=re.S)
    inner = re.sub(r'</svg>.*', '', inner, flags=re.S)
    return re.sub(r'\s+', ' ', inner).strip()


def _face(weight, path):
    b64 = base64.b64encode(open(path, 'rb').read()).decode()
    return ("@font-face{font-family:'Fraunces';font-style:normal;font-weight:%s;font-display:swap;"
            "src:url(data:font/woff2;base64,%s) format('woff2')}" % (weight, b64))


def css():
    return r"""
/* Libellés entiers, icônes, et bandes de titres. Le reste reste blanc. Les fenêtres .gm ne sont pas visées. */
.glyphe{display:inline-flex;flex:none;align-items:center;justify-content:center;color:currentColor}
.glyphe svg{width:22px;height:22px;display:block}
.rail button{align-items:flex-start;white-space:normal;height:auto;hyphens:auto}
.rail button span{min-width:0;white-space:normal;hyphens:auto;-webkit-hyphens:auto;overflow-wrap:break-word}
@media(min-width:1181px){
  .mod{grid-template-columns:220px minmax(0,1fr)}
}
@media(max-width:1180px){
  .rail{flex-wrap:wrap}
  .rail button{flex:1 1 46%;width:auto;max-width:100%;min-width:0;white-space:normal}
  .rail button span{white-space:normal;overflow-wrap:break-word}
}
#menu,#menu .mt,#menu li.g,.rail,.rail button,.rail button.a,nav.on button,nav.on button.a,#theme,#themes,#themes button,
.c,.bande,.lf button,.lien,.ls a,.ch>div,.ch>.eh,.pu,.pu.a,.etq,.mot,.sn,.num,.defile,.barre input,.vdc b{
  background:#fff!important;box-shadow:none!important}
.k-bleu,.k-rouge,.k-vert,.k-violet,.k-ocre,.k-orange,.c-bleu,.c-rouge,.c-vert,.c-violet,.c-ocre,.c-orange,
.lf button,.ls a,.rail button.a,#menu a.a{box-shadow:none!important}
.lf button,.ls a,.bande,.c,.defile,.rail,.col h2,.col h3,.col h4,.c h2,h1,#vue .tete{
  border:1px solid #c8c8c8!important;border-radius:12px!important;box-sizing:border-box!important}
.col>h2,.col>h3,.col>h4,.col>.bande,.col>.lf,.col>.defile,.lf,.lf button,.c>h2,.c .ls,.c .ls a{
  width:100%!important;max-width:100%!important;margin-left:0!important;margin-right:0!important}
.c{padding:0 0 10px!important;overflow:hidden}
.c>*{margin-left:0!important;margin-right:0!important}
"""


COURS_CSS = r"""
#fm-bandeau,body>header,main,footer{max-width:none!important;width:100%!important;margin-left:0!important;margin-right:0!important;padding-left:0!important;padding-right:0!important;box-sizing:border-box!important}
#fm-bandeau,h2,h3,.u,.w,.k,.bloc,.monograph,main>section{width:100%!important;max-width:none!important;margin-left:0!important;margin-right:0!important;box-sizing:border-box!important;border-radius:12px!important}
.u,.w,.k,.bloc,.monograph,blockquote,main>section{background:#fff!important;border:1px solid #c8c8c8!important;box-shadow:none!important;color:#111!important;padding:0!important}
.monograph>h2,.bloc>h2,.monograph>h3,.bloc>h3{width:calc(100% + 2px)!important;margin-left:-1px!important;margin-right:-1px!important}
.monograph>:not(h2):not(h3),.bloc>:not(h2):not(h3){margin-left:16px!important;margin-right:16px!important}
#brain-barre14,#brain-barre14 a,#brain-barre14 a b{background:#fff!important;box-shadow:none!important;color:#111!important}
#brain-barre14 a b{border:1px solid #c8c8c8!important}
#fm-bandeau{border:none!important;box-shadow:none!important}
h2,h3{border:none!important;box-shadow:none!important}
"""


def js():
    dossier = os.path.join(RACINE, 'Claude/_icones')
    glyphs = {fn[:-4]: _svg_inner(os.path.join(dossier, fn))
              for fn in sorted(os.listdir(dossier)) if fn.endswith('.svg')}
    return r"""
<script id="luxe-designer-js">
/* Icônes Lucide, licence ISC. Trait fin, bouts arrondis, couleur du thème. */
const GLYPHES=%s;
function glyphe(nom){const p=GLYPHES[nom]||GLYPHES['book-open'];
  return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+p+'</svg>';}
const CODE_ICONE={S1:'brain',S2:'eye',S3:'heart',S4:'wind',S5:'apple',S6:'droplet',S7:'baby',S8:'sun',S9:'bone',S10:'activity',S11:'moon',S12:'flower-2',T:'layers',PHY:'activity',PPA:'leaf','SÉM':'stethoscope',SEM:'stethoscope'};
function iconeRail(n,titre){const k=String(n||'').trim().toUpperCase();if(CODE_ICONE[k])return CODE_ICONE[k];
  const s=(String(n)+' '+String(titre)).toLowerCase();
  const t=[[/imager|radio|scan/, 'microscope'],[/explor|fonction/, 'activity'],[/biolog|laborat/, 'flask-conical'],[/pharmac|molécul|molecule/, 'pill'],[/anatom/, 'bone'],[/physio/, 'activity'],[/sémio|semio|status/, 'stethoscope'],[/neuro/, 'brain'],[/cardio|cœur|coeur/, 'heart'],[/respir|pneumo/, 'wind'],[/digest|hépat|hepat/, 'apple'],[/néph|neph|uro/, 'droplet'],[/gyné|gyne|obst|repro/, 'baby'],[/endocr|nutri/, 'sun'],[/locom|os |arth/, 'bone'],[/sang|immun/, 'activity'],[/psych|sommeil/, 'moon'],[/peau|phan/, 'flower-2']];
  for(const [re,nom] of t) if(re.test(s)) return nom;
  return 'book-open';}
function ornerRail(btn){if(!btn||btn.querySelector('.glyphe')||btn.closest('.gm'))return;
  const b=btn.querySelector('b');const sp=btn.querySelector('span');
  const nom=iconeRail(b&&b.textContent, (sp&&sp.textContent)||btn.textContent);
  const s=document.createElement('span');s.className='glyphe';s.innerHTML=glyphe(nom);btn.insertBefore(s, btn.firstChild);}
function ornerSeul(el,nom){if(!el||el.querySelector('.glyphe')||el.closest('.gm'))return;
  const label=(el.getAttribute('aria-label')||el.textContent||'').trim();
  if(label) el.setAttribute('aria-label', label);
  const s=document.createElement('span');s.className='glyphe';s.innerHTML=glyphe(nom);
  el.textContent='';el.appendChild(s);}
function ornerTheme(){const el=document.getElementById('theme');if(!el||el.querySelector('.glyphe'))return;
  const s=document.createElement('span');s.className='glyphe';s.innerHTML=glyphe('palette');el.insertBefore(s, el.firstChild);}
function ornerPlan(){const el=document.getElementById('planbtn');if(!el||el.querySelector('.glyphe'))return;
  el.textContent='';
  const s=document.createElement('span');s.className='glyphe';s.innerHTML=glyphe('menu');el.appendChild(s);
  el.appendChild(document.createTextNode(' Plan'));el.setAttribute('aria-label','Ouvrir le plan');}
const PALETTE=%s;
const COURS_CSS=%s;
function teintes(){const i=+(document.documentElement.dataset.theme||0);const n=((i%%7)+7)%%7;return PALETTE.map((_,k)=>PALETTE[(k+n)%%7]);}
function peindre(doc,sel){if(!doc)return;const cols=teintes();let k=0;
  doc.querySelectorAll(sel).forEach(el=>{if(el.closest('.gm,#voile,.fenetre,[popover]')||el.classList.contains('fm-double'))return;
    if(!el.getClientRects().length)return;
    const c=cols[k%%7];k++;
    el.style.setProperty('background',c,'important');
    el.style.setProperty('color','#000','important');
    el.style.setProperty('border-radius','12px','important');
    el.style.setProperty('box-shadow','none','important');});}
function peindreCours(frame){if(!frame||frame.id!=='vf')return;let doc;try{doc=frame.contentDocument}catch(e){return}
  if(!doc||!doc.head||!doc.getElementById('fm-bandeau'))return;
  if(!doc.getElementById('luxe-bandes')){const st=doc.createElement('style');st.id='luxe-bandes';st.textContent=COURS_CSS;doc.head.appendChild(st);}
  peindre(doc,'#fm-bandeau, h2, h3');}
function parer(){document.querySelectorAll('.rail button').forEach(ornerRail);
  ornerTheme();
  ornerPlan();
  peindre(document,'h1, .col h2, .col h3, .col h4, .c h2, #vue .tete');
  peindreCours(document.getElementById('vf'));
  ornerSeul(document.getElementById('vr'),'chevron-left');
  ornerSeul(document.getElementById('vp'),'chevron-left');
  ornerSeul(document.getElementById('vs'),'chevron-right');
  ornerSeul(document.getElementById('vn'),'arrow-up-right');
  document.querySelectorAll('#menu .x,#fen .x,#sco .x').forEach(el=>ornerSeul(el,'x'));}
parer();
document.addEventListener('load',function(e){if(e.target&&e.target.id==='vf')peindreCours(e.target);},true);
document.addEventListener('click',function(){requestAnimationFrame(parer);});
if(window.MutationObserver){
  new MutationObserver(parer).observe(document.body,{childList:true,subtree:true});
  new MutationObserver(parer).observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']});
}
</script>
""" % (json.dumps(glyphs, ensure_ascii=False, separators=(',', ':')),
       json.dumps(['#dcab09', '#1bdc09', '#23a9f6', '#f0850a', '#f970b9', '#eab8b8', '#09dccb']),
       json.dumps(COURS_CSS))


def injecter(html):
    html = re.sub(r'<style id="luxe-designer">.*?</style>', '', html, count=1, flags=re.S)
    html = re.sub(r'<script id="luxe-designer-js">.*?</script>', '', html, count=1, flags=re.S)
    style = '<style id="luxe-designer">' + css() + '</style>'
    html = html.replace('</head>', style + '</head>', 1)
    html = html.replace('</body>', js() + '</body>', 1)
    return html
