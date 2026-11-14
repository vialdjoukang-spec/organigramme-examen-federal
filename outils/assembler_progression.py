#!/usr/bin/env python3
"""Embarque dans progression.html les pages produites à part, pour un fichier unique et autonome.

Appelé automatiquement à la fin de outils/receptacle.py (désactivable : --sans-embarques).
  - Examens paracliniques › 2 Imagerie et 3 Explorations fonctionnelles : recensement topo-systémique (onglets A et B) ;
  - Sciences fondamentales › Physiologie, Physiopathologie, Sémiologie : pages correspondantes.
Chaque page est rangée telle quelle (chaîne JSON) dans <script type="application/json" data-emb="…"> ; le JS de
receptacle.py l'ouvre dans une iframe (Blob) au premier clic. Toutes les images img/… sont réduites (≤ 640 px,
vignettes ≤ 320 px, JPEG qualité 70) et intégrées en base64. Les renvois entre pages (SEMIOLOGIE.html#SY-xx, #S-xx)
passent par postMessage vers progression.html, qui ouvre le bon sous-onglet.

Usage : python3 outils/assembler_progression.py [--fichier progression.html] [--regenerer]
"""
import argparse, base64, hashlib, io, json, os, re, subprocess, sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(RACINE, 'Claude', '_progression')
PAGES = {  # clé : (page, générateur, CSS propre à l'intégration)
    'rts': (os.path.join(P, 'recensement', 'RECENSEMENT_TOPOSYSTEMIQUE.html'), os.path.join(P, 'recensement', 'generer.py'),
            '.tabs[role=tablist]{display:none!important}'),
    'sf': (os.path.join(P, 'donnees', 'fondamentales_v2', 'SCIENCES_FONDAMENTALES.html'),
           os.path.join(P, 'donnees', 'fondamentales_v2', 'generer_sf.py'), '.onglets[role=tablist]{display:none!important}'),
    'semio': (os.path.join(P, 'donnees', 'semiologie', 'SEMIOLOGIE.html'),
              os.path.join(P, 'donnees', 'semiologie', 'generer_status.py'), ''),
}
COTE, VIGNETTE, QUALITE = 640, 320, 70
CACHE = os.path.join(os.path.expanduser('~'), '.cache', 'assembler_progression')
IMG = re.compile(r'''(?<![\w/.\-])img/[^"'\s()<>\\]+?\.(?:jpe?g|png|gif|webp)''', re.I)
# Script ajouté à chaque page embarquée : onglet par ancre (#o-img…), renvois inter-pages vers le parent, liens externes hors cadre.
PONT = r'''<script>(function(){
 function go(){var h=decodeURIComponent(location.hash.slice(1)),t=h&&document.getElementById(h);if(t&&t.getAttribute('role')==='tab'&&t.getAttribute('aria-selected')!=='true')t.click();}
 addEventListener('hashchange',go);go();
 var P={SEMIOLOGIE:'semio',SCIENCES_FONDAMENTALES:'sf',RECENSEMENT_TOPOSYSTEMIQUE:'rts'};
 document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href]');if(!a)return;var u=a.getAttribute('href'),
  m=u.match(/(SEMIOLOGIE|SCIENCES_FONDAMENTALES|RECENSEMENT_TOPOSYSTEMIQUE)\.html(?:#(.*))?$/);
  if(m){e.preventDefault();parent.postMessage({aller:P[m[1]],h:m[2]?decodeURIComponent(m[2]):''},'*');return;}
  if(/^https?:/.test(u)&&!a.target){a.target='_blank';a.rel='noopener';}},true);
})();</script>'''


def reduire(chemin, cote):
    """JPEG ≤ cote px (plus grand côté), qualité 70, en cache ; renvoie l'URI data:."""
    from PIL import Image
    st = os.stat(chemin)
    cle = hashlib.sha1(f'{os.path.abspath(chemin)}|{st.st_mtime_ns}|{st.st_size}|{cote}|{QUALITE}'.encode()).hexdigest()
    c = os.path.join(CACHE, cle + '.jpg')
    if not os.path.exists(c):
        os.makedirs(CACHE, exist_ok=True)
        im = Image.open(chemin)
        im.seek(0)
        if im.mode in ('RGBA', 'LA', 'P'):
            im = im.convert('RGBA')
            fond = Image.new('RGB', im.size, (255, 255, 255))
            fond.paste(im, mask=im.split()[-1])
            im = fond
        im = im.convert('RGB')
        im.thumbnail((cote, cote), Image.LANCZOS)
        b = io.BytesIO()
        im.save(b, 'JPEG', quality=QUALITE, optimize=True, progressive=True)
        open(c + '.tmp', 'wb').write(b.getvalue())
        os.replace(c + '.tmp', c)
    return 'data:image/jpeg;base64,' + base64.b64encode(open(c, 'rb').read()).decode()


def embarquer_page(cle):
    page, _, css = PAGES[cle]
    d, s = os.path.dirname(page), open(page, encoding='utf-8').read()
    manq, n = [], [0]

    def sub(m):
        rel = m.group(0)
        f = os.path.join(d, rel)
        if not os.path.exists(f):
            manq.append(rel)
            return rel
        n[0] += 1
        # vignette : <img src="img/…"> ; fenêtre et données : 640 px
        vign = re.search(r'<img\b[^<>]*\bsrc="$', s[max(0, m.start() - 400):m.start()]) is not None
        return reduire(f, VIGNETTE if vign else COTE)
    s = IMG.sub(sub, s)
    ajout = (f'<style>{css}</style>' if css else '') + PONT
    s = s.replace('</body>', ajout + '</body>', 1) if '</body>' in s else s + ajout
    return s, n[0], manq


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--fichier', default='progression.html')
    ap.add_argument('--regenerer', action='store_true', help='relancer les trois générateurs avant intégration')
    a = ap.parse_args()
    if a.regenerer:
        for _, gen, _ in PAGES.values():
            subprocess.run([sys.executable, gen], check=True, cwd=os.path.dirname(gen))
    doc = open(a.fichier, encoding='utf-8').read()
    doc = re.sub(r'<script type="application/json" data-emb="[a-z]+">".*?</script>', '', doc, flags=re.S)  # idempotent
    tete = '<script type="application/json" id="donnees">'
    i = doc.index(tete)
    j = doc.index('</script>', i) + len('</script>')
    blocs = []
    for cle in PAGES:
        if not os.path.exists(PAGES[cle][0]):
            print(f'[assembler] absente : {PAGES[cle][0]}', file=sys.stderr)
            continue
        s, n, manq = embarquer_page(cle)
        if manq:
            print(f'[assembler] {cle} : {len(manq)} image(s) introuvable(s), ex. {manq[:3]}', file=sys.stderr)
        blocs.append(f'<script type="application/json" data-emb="{cle}">' + json.dumps(s, ensure_ascii=False).replace('<', '\\u003c') + '</script>')
        print(f'[assembler] {cle} : {n} image(s), {len(s.encode()) // 1024} Ko')
    doc = doc[:j] + ''.join(blocs) + doc[j:]
    open(a.fichier, 'w', encoding='utf-8').write(doc)
    print(f'[assembler] {a.fichier} : {len(doc.encode()) / 1e6:.1f} Mo')


if __name__ == '__main__':
    main()
