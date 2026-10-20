"""Ajoute dans l'onglet Gestes une carte de liens vers les squelettes gestes/<region>.html."""
import json, os, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT / 'tools'))
from _app import span
F = os.environ.get('APP_FILE', str(ROOT / 'app_v2.html'))
A = ' <div class="card"><div id="g-head"></div>'
s = Path(F).read_text()
if 'id="g-sq"' in s: sys.exit(0)
assert s.count(A) == 1, 'ancrage'
x, y = span(s, 'GES'); g = json.loads(s[x:y])
liens = ''.join(f'<a class="btn" href="gestes/{r["id"]}.html">{r["r"]}</a> ' for r in g)
C = (' <div class="card" id="g-sq"><h2>Squelettes des gestes · deux colonnes</h2>'
     f'<div class="chips2">{liens}</div></div>\n')
Path(F).write_text(s.replace(A, C + A, 1))
