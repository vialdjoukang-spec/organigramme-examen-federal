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
/* Libellés entiers et icônes. Aucune couleur n'est modifiée. */
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
function parer(){document.querySelectorAll('.rail button').forEach(ornerRail);
  ornerTheme();
  ornerPlan();
  ornerSeul(document.getElementById('vr'),'chevron-left');
  ornerSeul(document.getElementById('vp'),'chevron-left');
  ornerSeul(document.getElementById('vs'),'chevron-right');
  ornerSeul(document.getElementById('vn'),'arrow-up-right');
  document.querySelectorAll('#menu .x,#fen .x,#sco .x').forEach(el=>ornerSeul(el,'x'));}
parer();
if(window.MutationObserver) new MutationObserver(parer).observe(document.body,{childList:true,subtree:true});
</script>
""" % json.dumps(glyphs, ensure_ascii=False, separators=(',', ':'))


def injecter(html):
    html = re.sub(r'<style id="luxe-designer">.*?</style>', '', html, count=1, flags=re.S)
    html = re.sub(r'<script id="luxe-designer-js">.*?</script>', '', html, count=1, flags=re.S)
    style = '<style id="luxe-designer">' + css() + '</style>'
    html = html.replace('</head>', style + '</head>', 1)
    html = html.replace('</body>', js() + '</body>', 1)
    return html
