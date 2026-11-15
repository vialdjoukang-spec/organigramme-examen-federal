#!/usr/bin/env python3
"""Forme luxe de la plateforme (skill designer). Icônes Lucide (ISC), titres Fraunces (OFL), hors ligne.
Ne touche ni aux cours, ni aux fenêtres .gm."""
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
    p400 = os.path.join(RACINE, 'Claude/_polices/fraunces-latin-400-normal.woff2')
    p600 = os.path.join(RACINE, 'Claude/_polices/fraunces-latin-600-normal.woff2')
    return _face(400, p400) + _face(600, p600) + r"""
/* Skill designer : fond blanc, aplats francs, aucun trait. Les fenêtres .gm ne sont pas visées. */
body{background:#fff}
h1,#menu .mt,#menu li.g,.c .code,.c h2,#vue .tete b,.col h2,.col h3,.col h4,.ch>.eh,#fen .ft h3,#fen h4,#fen h5,#sco h3{
  font-family:Fraunces,"Atkinson Hyperlegible",serif;font-weight:600;letter-spacing:-.02em;color:#000;border:none!important}
#vue .tete b{font-size:1.45rem;line-height:1.12;font-weight:600}
header.h,nav.on button,#theme,#themes,#themes button,#menu,.rail,.rail button,.c,.barre input,.pu,#planbtn,#vue .tete,#vue .tete button,#vue .tete a,#fen .x,#sco .x,#menu .x{
  border:none!important;border-radius:0!important;box-shadow:none!important}
.grille{gap:32px}
.c{background:#fff}
.barre input{background:#f3f3f3}
nav.on{gap:10px}
nav.on button.a,#theme{background:var(--eye)}
.rail{background:transparent!important;padding:0;gap:8px;overflow-x:visible}
.rail button{padding:10px 8px;gap:10px;align-items:flex-start;font-size:13px;white-space:normal!important;overflow:visible!important;height:auto!important;hyphens:auto}
.rail button span{min-width:0;white-space:normal;overflow:visible;hyphens:auto;-webkit-hyphens:auto;overflow-wrap:break-word}
.rail button.a{background:var(--eye)!important}
.rail button b{border:none!important;background:transparent!important;min-width:0;padding:0;font-size:13px;font-weight:600}
#menu,#menu a,.rail,.rail button{color:#111}
.glyphe{display:inline-flex;flex:none;align-items:center;justify-content:center;color:currentColor}
.glyphe svg{width:22px;height:22px;display:block}
.pu{background:var(--t-bande)!important;color:#000!important}
.pu.a{background:var(--eye)!important;color:#000!important}
#themes{position:fixed!important;top:var(--ht);right:0;bottom:0;left:auto;width:min(440px,100vw);max-height:none!important;overflow:auto;z-index:70;display:none;grid-template-columns:1fr!important;gap:2px;padding:12px 16px 40px;background:#fff}
#themes.a{display:grid!important}
#themes .fermer{grid-column:1/-1;justify-self:end;font:inherit;font-weight:700;font-size:14px;background:var(--eye);color:#000;padding:8px 14px;cursor:pointer;margin:0 0 8px}
#themes .famille{margin:16px 0 6px}
#themes button{white-space:normal!important;align-items:flex-start;font-size:14px;line-height:1.3;padding:8px 4px;min-width:0}
#themes .pal{gap:5px;flex:none;padding-top:2px}
#themes .pal i{width:22px;height:22px;border:none!important;border-radius:0!important}
@media(min-width:1181px){
  .mod{grid-template-columns:220px minmax(0,1fr)!important}
}
@media(max-width:1180px){
  .rail{flex-direction:row!important;flex-wrap:wrap!important;overflow:visible!important}
  .rail button{flex:1 1 46%!important;width:auto!important;max-width:100%!important;min-width:0!important;white-space:normal!important}
  .rail button span{max-width:none!important;white-space:normal!important;overflow-wrap:break-word}
}
@media(min-width:901px){
  .cadre{grid-template-columns:15% 5% minmax(0,70%) 10%!important}
  #menu{grid-column:1}
  main{grid-column:3;padding-left:0;padding-right:0}
}
@media(max-width:520px){.sous{font-size:13px;line-height:1.35}}
@media(prefers-reduced-motion:no-preference){
  nav.on button,.rail button,#theme,#themes button,.c{transition:background-color .18s ease,transform .18s ease}
  .rail button:hover,nav.on button:hover,#themes button:hover{transform:translateY(-1px)}
}
@media(prefers-reduced-motion:reduce){
  nav.on button,.rail button,#theme,#themes button,.c{transition:none}
}
/* Aucun trait hors fenêtres d'imagerie. Le focus clavier garde son contour. */
html body :is(*):not(.gm,.gm *,#voile,#voile *,.gm-btn,.gm-carte,.gm-carte *,.gm-code,.gm-code *,.gm-signal,.gm-signal *,.gm-pan,.gm-pan *,.gm-fig,.gm-fig *,.gm-zw,.gm-zw *,.gm-meta,.gm-meta *,.fedmed-plus,.fedmed-plus *),
html body :is(*):not(.gm,.gm *,#voile,#voile *,.gm-btn,.gm-carte,.gm-carte *,.gm-code,.gm-code *,.gm-signal,.gm-signal *,.gm-pan,.gm-pan *,.gm-fig,.gm-fig *,.gm-zw,.gm-zw *,.gm-meta,.gm-meta *,.fedmed-plus,.fedmed-plus *)::before,
html body :is(*):not(.gm,.gm *,#voile,#voile *,.gm-btn,.gm-carte,.gm-carte *,.gm-code,.gm-code *,.gm-signal,.gm-signal *,.gm-pan,.gm-pan *,.gm-fig,.gm-fig *,.gm-zw,.gm-zw *,.gm-meta,.gm-meta *,.fedmed-plus,.fedmed-plus *)::after{
  border:none!important;outline:none!important;box-shadow:none!important;text-decoration-line:none!important}
html body :is(*):not(.gm,.gm *,#voile,#voile *,.gm-btn,.gm-carte,.gm-carte *,.gm-code,.gm-code *,.gm-signal,.gm-signal *,.gm-pan,.gm-pan *,.gm-fig,.gm-fig *,.gm-zw,.gm-zw *,.gm-meta,.gm-meta *,.fedmed-plus,.fedmed-plus *):focus-visible{
  outline:2px solid #111!important;outline-offset:2px}
.lf{gap:8px}
.lf button,.lien,.barre-t>*,.ls a,.ch details span{background:var(--t-encadre)!important}
.ch{row-gap:14px}
.bande,.defile,.c{margin-top:16px;margin-bottom:16px}
"""


COURS_CSS = r"""
#fm-bandeau{background:var(--eye)!important;color:#000!important;border:none!important;border-radius:0!important;box-shadow:none!important;padding:22px 24px!important;margin:0 0 28px!important}
#fm-bandeau .fm-code,#fm-bandeau .fm-nom,#fm-bandeau .fm-phase,#fm-bandeau .fm-code span{color:#000!important;border:none!important;background:transparent!important;box-shadow:none!important}
h2{background:var(--t-bande)!important;color:#000!important;border:none!important;border-radius:0!important;box-shadow:none!important;text-decoration:none!important;padding:.45em .7em!important;margin:1.4em 0 .75em!important}
h3,h4,h5,h6{color:#000!important;border:none!important;box-shadow:none!important;background:transparent!important;padding-bottom:0!important}
.monograph,.bloc,.monographie{background:var(--t-encadre)!important;color:#111!important;border:none!important;border-radius:0!important;box-shadow:none!important;padding:1.15rem 1.2rem!important;margin:1.7rem 0!important}
.w,.k,.key,blockquote,details:not([class]),details.fenetre[open]{background:var(--t-encadre)!important;color:#111!important;border:none!important;border-radius:0!important;box-shadow:none!important}
.u,.alert{background:#e7b4b4!important;color:#111!important;border:none!important;border-radius:0!important;box-shadow:none!important;padding:.8rem 1rem!important}
#brain-barre14{background:var(--t-rail)!important;background-image:none!important;border:none!important;box-shadow:none!important}
#brain-barre14::before{border:none!important;color:#000!important;padding-bottom:0!important;margin:0 10px 16px!important}
#brain-barre14 a,#brain-barre14 a:hover,#brain-barre14 a:focus-visible,#brain-barre14 a.fm-actif,#brain-barre14 a[aria-current]{border:none!important;box-shadow:none!important;color:#000!important}
#brain-barre14 a.fm-actif,#brain-barre14 a[aria-current]{background:var(--eye)!important}
#brain-barre14 a b,#brain-barre14 a.fm-actif b,#brain-barre14 a[aria-current] b{background:var(--t-mot)!important;color:#000!important;box-shadow:none!important}
table,th,td{border:none!important;box-shadow:none!important}
th{background:var(--t-tableau)!important;color:#000!important}
hr,nav a{border:none!important;box-shadow:none!important;border-radius:0!important}
[popover].fenetre,.mb:target:not(.fenetre){border:none!important;box-shadow:none!important;border-radius:0!important}
#__ID__ :is(*):not(.gm,.gm *,#voile,#voile *),
#__ID__ :is(*):not(.gm,.gm *,#voile,#voile *)::before,
#__ID__ :is(*):not(.gm,.gm *,#voile,#voile *)::after{
  border:none!important;outline:none!important;box-shadow:none!important;text-decoration-line:none!important}
#__ID__ :is(*):not(.gm,.gm *,#voile,#voile *):focus-visible{outline:2px solid #111!important;outline-offset:2px}
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
function ornerMenu(){const m=document.getElementById('themes');if(!m||m.querySelector('.fermer'))return;
  const b=document.createElement('button');b.type='button';b.className='fermer';b.textContent='Fermer';
  b.setAttribute('aria-label','Fermer le menu des thèmes');
  b.addEventListener('click',function(e){e.stopPropagation();m.classList.remove('a');});
  m.insertBefore(b,m.firstChild);}
const COURS_CSS=%s;
function imagerie(frame){if(!frame)return true;if(frame.closest&&frame.closest('.gm,#voile'))return true;if(frame.dataset&&frame.dataset.p==='rts')return true;return false;}
function peindreCours(frame){frame=frame||document.getElementById('vf');if(!frame||imagerie(frame))return;
  let doc;try{doc=frame.contentDocument}catch(e){return}
  if(!doc||!doc.documentElement||!doc.body)return;
  if(!doc.getElementById('fm-bandeau')&&!doc.querySelector('h2,.ch,.lf,main'))return;
  if(!doc.documentElement.id)doc.documentElement.id='luxe-racine';
  let st=doc.getElementById('luxe-cours');
  if(!st){st=doc.createElement('style');st.id='luxe-cours';st.textContent=COURS_CSS.replaceAll('__ID__',doc.documentElement.id);(doc.head||doc.documentElement).appendChild(st);}
  const cs=getComputedStyle(document.documentElement),root=doc.documentElement;
  ['--eye','--t-menu','--t-rail','--t-tableau','--t-mot','--t-bande','--t-encadre'].forEach(function(v){
    root.style.setProperty(v,(cs.getPropertyValue(v)||'').trim());});}
function parer(){document.querySelectorAll('.rail button').forEach(ornerRail);
  ornerTheme();ornerMenu();
  ornerPlan();
  peindreCours();
  document.querySelectorAll('iframe').forEach(peindreCours);
  ornerSeul(document.getElementById('vr'),'chevron-left');
  ornerSeul(document.getElementById('vp'),'chevron-left');
  ornerSeul(document.getElementById('vs'),'chevron-right');
  ornerSeul(document.getElementById('vn'),'arrow-up-right');
  document.querySelectorAll('#menu .x,#fen .x,#sco .x').forEach(el=>ornerSeul(el,'x'));}
parer();
document.addEventListener('load',function(e){const t=e.target;if(t&&t.tagName==='IFRAME')peindreCours(t);},true);
if(window.MutationObserver){
  new MutationObserver(parer).observe(document.body,{childList:true,subtree:true});
  new MutationObserver(function(){peindreCours();}).observe(document.documentElement,{attributes:true,attributeFilter:['data-theme','style']});
}
</script>
""" % (json.dumps(glyphs, ensure_ascii=False, separators=(',', ':')), json.dumps(COURS_CSS, ensure_ascii=False))


def injecter(html):
    html = re.sub(r'<style id="luxe-designer">.*?</style>', '', html, count=1, flags=re.S)
    html = re.sub(r'<script id="luxe-designer-js">.*?</script>', '', html, count=1, flags=re.S)
    style = '<style id="luxe-designer">' + css() + '</style>'
    html = html.replace('</head>', style + '</head>', 1)
    html = html.replace('</body>', js() + '</body>', 1)
    return html
