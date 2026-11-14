#!/usr/bin/env python3
"""Injecte les cours (Claude/LOT_*/…html, version origin/main) dans PROGRESSION__FedMed.html de Grok,
sans toucher à sa mise en page ni à ses images : chaque cours est rendu autonome (forme.css et forme.js en ligne,
images en data URI, police Atkinson par Google Fonts), compressé (gzip) et ajouté dans un bloc JSON ;
seul le chargement du cadre de cours est redirigé vers ce bloc (décompression dans le navigateur).
Usage : python3 outils/injecter_cours_fedmed.py ENTREE.html SORTIE.html [--ref origin/main]"""
import sys, re, json, gzip, base64, subprocess, posixpath, argparse, mimetypes, io
from PIL import Image
ap = argparse.ArgumentParser(); ap.add_argument('entree'); ap.add_argument('sortie'); ap.add_argument('--ref', default='origin/main')
a = ap.parse_args()
def git(p, binaire=False):
    r = subprocess.run(['git', 'show', f'{a.ref}:{p}'], capture_output=True)
    if r.returncode: return None
    return r.stdout if binaire else r.stdout.decode('utf-8', 'replace')
CSS = re.sub(r'@font-face\s*{[^}]*}', '', git('Claude/_polices/forme.css'))
JS = git('Claude/_polices/forme.js')
FONTE = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">'
page = open(a.entree, encoding='utf-8').read()
liste = sorted(set(re.findall(r'"f":"(Claude/LOT_[^"]+\.html)"', page)))
cours, manque, IMGS = {}, [], {}
for f in liste:
    h = git(f)
    if h is None: manque.append(f); continue
    d = posixpath.dirname(f)
    h = re.sub(r'<link[^>]*href="\.\./_polices/forme\.css"[^>]*>', lambda m: FONTE + '<style>' + CSS + '</style>', h)
    h = re.sub(r'<script[^>]*src="\.\./_polices/forme\.js"[^>]*>\s*</script>', lambda m: '<script>' + JS + '</script>', h)
    def img(m):
        attr, rel = m.group(1), m.group(2)
        b = git(posixpath.normpath(posixpath.join(d, rel)), True)
        if b is None: return m.group(0)
        try:
            im = Image.open(io.BytesIO(b)); im = im.convert('RGBA' if im.mode in ('RGBA','LA','P') else 'RGB')
            if im.width > 640: im = im.resize((640, int(im.height * 640 / im.width)))
            o = io.BytesIO(); im.save(o, 'WEBP', quality=60); b = o.getvalue(); t = 'image/webp'
        except Exception:
            t = mimetypes.guess_type(rel)[0] or 'image/webp'
        k = posixpath.normpath(posixpath.join(d, rel))
        IMGS[k] = f'data:{t};base64,{base64.b64encode(b).decode()}'
        return f'{attr}="@@IMG:{k}@@"'
    h = re.sub(r'(src|href)="(images/[^"]+)"', img, h)
    cours[f] = base64.b64encode(gzip.compress(h.encode('utf-8'), 9)).decode()
bloc = ('<script type="application/json" id="cours-embarques">' + json.dumps(cours, separators=(',', ':')) + '</script>'
        '<script type="application/json" id="cours-images">' + json.dumps(IMGS, separators=(',', ':')) + '</script>')
hook = ('<script>/* Cours embarqués (outils/injecter_cours_fedmed.py) */'
        'let COURS_E=null,COURS_I=null;const COURS_U={};'
        'async function coursURL(f){if(COURS_U[f])return COURS_U[f];if(!document.getElementById("cours-images"))await new Promise(r=>addEventListener("DOMContentLoaded",r,{once:true}));COURS_E=COURS_E||JSON.parse(document.getElementById("cours-embarques").textContent);const z=COURS_E[f];if(!z)return D.base+f;'
        'const b=Uint8Array.from(atob(z),c=>c.charCodeAt(0));'
        'const t=await new Response(new Blob([b]).stream().pipeThrough(new DecompressionStream("gzip"))).text();'
        'const I=COURS_I||(COURS_I=JSON.parse(document.getElementById("cours-images").textContent));'
        'const h=t.replace(/@@IMG:([^@]+)@@/g,(m,k)=>I[k]||"");'
        'return COURS_U[f]=URL.createObjectURL(new Blob([h],{type:"text/html"}));}'
        'function coursSrc(c,f){coursURL(f).then(u=>{c.src=u;const n=document.getElementById("vn");if(n)n.href=u;});}</script>')
ancien = "cadre.src=D.base+l.f;vieux.replaceWith(cadre);$('#vn').href=D.base+l.f;"
assert page.count(ancien) == 1, 'point d\'accroche introuvable'
page = page.replace(ancien, "coursSrc(cadre,l.f);vieux.replaceWith(cadre);")
page = page.replace('</body>', bloc + '</body>', 1)
assert page.count('<head>') >= 1
page = page.replace('<head>', '<head>' + hook, 1)
open(a.sortie, 'w', encoding='utf-8').write(page)
print(f'{len(cours)} cours injectés, {len(manque)} manquants, sortie {len(page)/1e6:.1f} Mo')
