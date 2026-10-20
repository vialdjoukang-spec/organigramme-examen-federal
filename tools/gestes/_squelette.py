"""Génère gestes/<region>.html : squelette vide (2 colonnes, bandes, image, fenêtres), sans texte clinique."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from _app import read, span
CSS = """body{margin:0;font:16px system-ui,sans-serif}h1{margin:1rem}
.g2{display:grid;grid-template-columns:1fr 1fr;min-height:80vh}
.etapes{padding:1rem;border-right:3px solid #333;counter-reset:t}
.bande{counter-increment:t;min-height:2.6rem;box-sizing:border-box;margin:.5rem 0;padding:.6rem .8rem;font-weight:700;
 background:color-mix(in srgb,var(--reg,#888) 10%,#fff);border-left:4px solid var(--reg,#888)}
.bande::before{content:"Temps " counter(t)}
.img{margin:1rem;border:3px dashed #777;border-radius:8px;display:flex;align-items:center;justify-content:center;color:#777}
.fen{display:none}
@media(max-width:700px){.g2{grid-template-columns:1fr 1fr}.etapes{padding:.5rem}.img{margin:.5rem}}"""
def generer(rid):
    s = read(); x, y = span(s, 'GES'); r = next(g for g in json.loads(s[x:y]) if g['id'] == rid)
    esc = lambda t: t.replace('&', '&amp;').replace('<', '&lt;')
    b = ''.join(f'<div class="bande" data-k="{it["k"]}"><template class="fen" data-niveau="1"></template></div>' for it in r['items'])
    h = (f'<!doctype html><html lang="fr"><meta charset="utf-8">'
         f'<title>Squelette · {esc(r["r"])}</title><style>{CSS}</style><body data-reg="{rid}">'
         f'<h1>{esc(r["r"])}</h1><main class="g2"><section class="etapes">{b}</section>'
         f'<aside class="img" data-src="" data-licence="">Image</aside></main></body></html>\n')
    (ROOT / 'gestes').mkdir(exist_ok=True); (ROOT / f'gestes/{rid}.html').write_text(h)
