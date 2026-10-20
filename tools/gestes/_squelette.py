"""Génère gestes/<region>.html : squelette vide (2 colonnes, bandes, image, fenêtres), sans texte clinique."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from _app import read, span
CSS = """body{margin:0;font:16px system-ui,sans-serif}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:1rem;padding:1rem}
.bande{width:50vw;max-width:100%;box-sizing:border-box;margin:.4rem 0;padding:.6rem .8rem;font-weight:700;
 background:color-mix(in srgb,var(--reg,#888) 8%,#fff);border-left:4px solid var(--reg,#888)}
.bande .txt:empty::before{content:"À rédiger";font-weight:400;opacity:.5}
.img{border:1px dashed #aaa;min-height:200px;display:flex;align-items:center;justify-content:center;opacity:.6}
.fen{display:none}"""
def generer(rid):
    s = read(); x, y = span(s, 'GES'); r = next(g for g in json.loads(s[x:y]) if g['id'] == rid)
    esc = lambda t: t.replace('&', '&amp;').replace('<', '&lt;')
    b = ''.join(f'<div class="bande" data-k="{it["k"]}"><span class="ph">{esc(it["p"])}</span> · '
                f'{esc(it["s"])}<div class="txt"></div><template class="fen" data-niveau="1"></template></div>'
                for it in r['items'])
    h = (f'<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="robots" content="noindex">'
         f'<title>Squelette · {esc(r["r"])}</title><style>{CSS}</style><body data-reg="{rid}">'
         f'<h1>{esc(r["r"])}</h1><main class="g2"><section class="etapes">{b}</section>'
         f'<aside class="img" data-src="" data-licence="">Image sourcée à placer</aside></main></body></html>\n')
    (ROOT / 'gestes').mkdir(exist_ok=True); (ROOT / f'gestes/{rid}.html').write_text(h)
