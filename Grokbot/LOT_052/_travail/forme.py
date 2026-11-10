#!/usr/bin/env python3
"""Charte commune des leçons du LOT 052.

Le fond de page est ivoire, jamais bleu. Le texte est #1c120c sur ce fond
(contraste supérieur à 7:1). La barre latérale a le même dessin dans chaque
leçon ; seule la couleur d'accent change. Elle reste visible au défilement,
marque la section active et montre la progression. Le nom du diagnostic
occupe le haut de la page.
"""
import argparse, html, re, sys

CSS = """
:root{--fond:#f4efe6;--ilot:#fffdf8;--encre:#1c120c;--accent:__ACCENT__;--bord:#3d2b24;--alerte:#7a1020;--bande:#f7f1e6}
*{box-sizing:border-box}
html{font-size:18px}
body{margin:0;background:var(--fond);color:var(--encre);font-family:"Atkinson Hyperlegible",Verdana,sans-serif;font-weight:500;line-height:1.65}
header.entete{background:#f4efe6;padding-top:32px;padding-right:36px;padding-bottom:22px;padding-left:256px;border-bottom:8px solid var(--accent)}
header.entete .kicker{margin:0;font-size:1rem;font-weight:700;letter-spacing:.04em;color:#1c120c}
h2{font-size:2.7rem;line-height:1.12;font-weight:750;color:#1c120c;margin-top:.35rem;margin-bottom:0}
.cadre{display:block}
nav.rail{position:fixed;top:0;left:0;bottom:0;width:232px;background:var(--accent);color:#fffdf8;padding:22px 14px 28px;overflow:auto}
nav.rail p{margin:0;font-size:1rem;font-weight:750;color:#fffdf8}
.piste{height:8px;margin-top:12px;margin-bottom:14px;background:rgba(255,253,248,.35);border-radius:6px;overflow:hidden}
.avance{height:0;width:100%;background:#fffdf8}
nav.rail ol{list-style:none;margin:0;padding:0}
nav.rail li{margin-bottom:4px}
nav.rail a{display:block;color:#fffdf8;text-decoration:none;font-size:1rem;font-weight:600;line-height:1.35;padding:7px 8px;border-radius:8px}
nav.rail a.actif{background:#fffdf8;color:#1c120c}
main{margin-left:232px;max-width:860px;padding-top:28px;padding-right:32px;padding-bottom:64px;padding-left:32px}
section.ilot{background:var(--ilot);border:2px solid var(--bord);border-radius:12px;padding:22px 24px 18px;margin-bottom:22px}
h3{font-size:1.28rem;line-height:1.35;font-weight:750;color:#1c120c;margin-top:0;margin-bottom:.85rem;padding-left:12px;border-left:6px solid var(--accent)}
h4{font-size:1.08rem;line-height:1.4;font-weight:700;color:#1c120c;margin-top:1.1rem;margin-bottom:.45rem}
.p{margin-top:0;margin-bottom:.85rem}
.t{overflow-x:auto;margin-top:.4rem;margin-bottom:1rem}
table{border-collapse:collapse;width:100%;font-size:1rem;line-height:1.45;background:#fffdf8}
caption{caption-side:top;text-align:left;font-size:1rem;font-weight:750;color:#1c120c;padding-bottom:8px}
td,th{border:1px solid var(--bord);padding:8px 10px;vertical-align:top;color:#1c120c}
th{background:var(--accent);color:#fffdf8;font-weight:700}
tbody tr:nth-child(even) td{background:#f7f1e6}
.fenetre{max-width:min(860px,94vw);max-height:86vh;overflow:auto;border:3px solid var(--accent);border-radius:12px;padding:20px 22px;background:#fffdf8;color:#1c120c}
.fenetre::backdrop{background:rgba(28,18,12,.55)}
.fenetre p{font-size:1rem;line-height:1.6}
button.w{color:var(--accent);background:transparent;border-style:solid;border-color:var(--accent);border-bottom-width:2px;border-top-width:0;border-left-width:0;border-right-width:0;font:inherit;font-weight:700;cursor:pointer;padding:0}
sup.r{font-size:.9em;font-weight:700;line-height:0}
sup.r a{color:#1c120c;text-decoration:underline;font-weight:700}
a{color:#1c120c}
.alerte{border-left:6px solid var(--alerte);padding-left:12px}
figure{margin-top:.8rem;margin-bottom:1rem;padding:12px;border:2px solid var(--bord);border-radius:10px;background:#fffdf8}
figure img{max-width:100%;height:auto;border-radius:6px}
figcaption{font-size:1rem;line-height:1.5;font-weight:500;color:#1c120c;margin-top:.6rem}
.finale{margin-top:1rem;padding:14px 16px;border:3px solid var(--accent);border-radius:10px;font-size:1rem;line-height:1.6;color:#1c120c;background:#f7f1e6}
@media(max-width:860px){
nav.rail{position:sticky;top:0;left:auto;bottom:auto;width:auto;max-height:40vh}
main{margin-left:0;padding:18px 14px 40px}
h2{font-size:2.1rem}
header.entete{padding-top:22px;padding-right:16px;padding-bottom:18px;padding-left:16px}
}
""".strip()

SCRIPT = """
<script>
(function () {
  var liste = document.querySelector('nav.rail ol');
  var avance = document.querySelector('.avance');
  var sections = Array.prototype.filter.call(document.querySelectorAll('section.ilot'), function (s) {
    return s.id.indexOf('sources') < 0;
  });
  sections.forEach(function (s) {
    var titre = s.querySelector('h3');
    var item = document.createElement('li');
    var lien = document.createElement('a');
    lien.href = '#' + s.id;
    lien.textContent = titre ? titre.textContent : s.id;
    item.appendChild(lien);
    liste.appendChild(item);
  });
  function suivre() {
    var doc = document.documentElement;
    var y = window.scrollY + 160;
    var courant = sections[0];
    sections.forEach(function (s) {
      if (s.offsetTop <= y) courant = s;
    });
    Array.prototype.forEach.call(liste.querySelectorAll('a'), function (lien) {
      var vise = courant && lien.getAttribute('href') === '#' + courant.id;
      if (vise) lien.classList.add('actif');
      else lien.classList.remove('actif');
    });
    var plein = doc.scrollHeight - doc.clientHeight;
    var part = plein > 0 ? doc.scrollTop / plein : 0;
    avance.style.height = Math.round(part * 100) + '%';
  }
  window.addEventListener('scroll', suivre, {passive: true});
  window.addEventListener('resize', suivre);
  suivre();
})();
</script>
""".strip()


def appliquer(chemin, accent, nom, kicker):
    h = open(chemin, encoding='utf-8').read()
    a, b = h.find('<style>'), h.find('</style>')
    if a < 0 or b < 0:
        raise SystemExit('bloc style introuvable')
    h = h[:a] + '<style>' + CSS.replace('__ACCENT__', accent) + h[b:]
    h = re.sub(r'<h2>.*?</h2>', '', h, count=1)
    entete = (
        '<header class="entete"><div class="kicker">' + html.escape(kicker) + '</div><h2>'
        + html.escape(nom) + '</h2></header><div class="cadre">'
        '<nav class="rail" aria-label="Progression du cours"><p>Parcours</p>'
        '<div class="piste"><div class="avance"></div></div><ol></ol></nav>'
    )
    if '<body><main>' not in h:
        raise SystemExit('structure assembleur absente')
    h = h.replace('<body><main>', '<body>' + entete + '<main>', 1)
    h = h.replace('</main></body>', '</main></div>' + SCRIPT + '</body>', 1)
    open(chemin, 'w', encoding='utf-8').write(h)
    print(chemin, len(h.encode()))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('fichier')
    ap.add_argument('--accent', required=True)
    ap.add_argument('--nom', required=True)
    ap.add_argument('--kicker', required=True)
    a = ap.parse_args()
    appliquer(a.fichier, a.accent, a.nom, a.kicker)
