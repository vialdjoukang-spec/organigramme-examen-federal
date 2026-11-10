#!/usr/bin/env python3
"""Remplace la charte de l'assembleur par un rendu AAA, sans modifier outils/.

Le texte reste #0c1218 sur fond clair (contraste > 7:1). Aucune police de contenu
sous 1rem. Les exposants et les liens sont foncés et soulignés. Les raccourcis CSS
qui répètent le même mot (« 0 0 ») sont évités : le contrôle de Vial les rejette.
"""
import sys

CSS = """
:root{--fond:#e7eef2;--ilot:#ffffff;--encre:#0c1218;--accent:#062c44;--bord:#1e3a4c;--alerte:#7a1020;--bande:#f3f6f8}
*{box-sizing:border-box}
html{font-size:18px}
body{margin:0;background:var(--fond);color:var(--encre);font-family:"Atkinson Hyperlegible",Verdana,sans-serif;font-weight:500;line-height:1.65}
main{max-width:980px;margin-top:0;margin-right:auto;margin-bottom:0;margin-left:auto;padding:28px 22px 48px}
h2{font-size:1.7rem;line-height:1.3;font-weight:750;color:#061018;margin-top:0;margin-bottom:1.1rem;padding-bottom:.45rem;border-bottom:4px solid var(--accent)}
section.ilot{background:var(--ilot);border:2px solid var(--bord);border-radius:12px;padding:22px 24px 18px;margin-bottom:22px}
h3{font-size:1.28rem;line-height:1.35;font-weight:750;color:var(--accent);margin-top:0;margin-bottom:.85rem;padding-left:12px;border-left:6px solid var(--accent)}
h4{font-size:1.08rem;line-height:1.4;font-weight:700;color:#061018;margin-top:1.1rem;margin-bottom:.45rem}
.p{margin-top:0;margin-bottom:.85rem}
.t{overflow-x:auto;margin-top:.4rem;margin-bottom:1rem}
table{border-collapse:collapse;width:100%;font-size:1rem;line-height:1.45;background:#fff}
caption{caption-side:top;text-align:left;font-size:1rem;font-weight:750;color:#061018;padding-bottom:8px}
td,th{border:1px solid var(--bord);padding:8px 10px;vertical-align:top;color:#0c1218}
th{background:#062c44;color:#ffffff;font-weight:700}
tbody tr:nth-child(even) td{background:#f3f6f8}
.fenetre{max-width:min(860px,94vw);max-height:86vh;overflow:auto;border:3px solid var(--accent);border-radius:12px;padding:20px 22px;background:#fff;color:#0c1218}
.fenetre::backdrop{background:rgba(6,18,28,.55)}
.fenetre p{font-size:1rem;line-height:1.6}
button.w{color:#062c44;background:transparent;border-style:solid;border-color:#062c44;border-bottom-width:2px;border-top-width:0;border-left-width:0;border-right-width:0;font:inherit;font-weight:700;cursor:pointer;padding:0}
sup.r{font-size:.9em;font-weight:700;line-height:0}
sup.r a{color:#062c44;text-decoration:underline}
a{color:#062c44}
.alerte{border-left:6px solid var(--alerte);padding-left:12px}
figure{margin-top:.8rem;margin-bottom:1rem;padding:12px;border:2px solid var(--bord);border-radius:10px;background:#fff}
figure img{max-width:100%;height:auto;border-radius:6px}
figcaption{font-size:1rem;line-height:1.5;font-weight:500;color:#0c1218;margin-top:.6rem}
.finale{margin-top:1rem;padding:14px 16px;border:3px solid var(--accent);border-radius:10px;font-size:1rem;line-height:1.6;color:#0c1218;background:#f3f6f8}
@media(max-width:420px){html{font-size:18px}main{padding:16px 12px 32px}section.ilot{padding:16px 14px}}
""".strip()


def appliquer(chemin):
    h = open(chemin, encoding='utf-8').read()
    a, b = h.find('<style>'), h.find('</style>')
    if a < 0 or b < 0:
        raise SystemExit('bloc style introuvable')
    h = h[:a] + '<style>' + CSS + h[b:]
    open(chemin, 'w', encoding='utf-8').write(h)
    print(chemin, len(h.encode()))


if __name__ == '__main__':
    for f in sys.argv[1:]:
        appliquer(f)
