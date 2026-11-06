"""Generate four non-medical Canvas note-flows from the baseline source."""
from pathlib import Path
from bs4 import BeautifulSoup
import re
import html
from svg_networks import link_path
R=Path('/workspace/outils-puissants')
assert (R/'render_atlas_avant_t288u.py').exists()
# The import above runs the Atelier patch on current renderer; reset business
# diagrams from the exact pre-t288u SVGs to prevent partial-match fragments.
current=(R/'render_atlas.py').read_text()
baseline=(R/'render_atlas_avant_t288u.py').read_text()

def esc(v): return html.escape(str(v),quote=True)
for baseline_match in re.finditer(r'<svg class="biz-svg".*?</svg>',baseline,flags=re.S):
    old=BeautifulSoup(baseline_match.group(0),'html.parser').select_one('svg.biz-svg')
    nodes=old.select('g.biz-svg-node');mid=nodes[0]['data-biz']
    positions=[(22,62),(378,32),(730,165),(418,365),(52,342)]
    out=[f'<svg class="biz-svg obsidian-canvas" viewBox="0 0 1000 500" role="group" aria-label="{esc(old.get("aria-label","Modèle en ligne"))}" xmlns="http://www.w3.org/2000/svg">',
         f'<defs><marker id="biz-arrow-{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#297766"/></marker><marker id="biz-arrow-soft-{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" fill="#9cb9ae"/></marker><filter id="biz-shadow-{mid}" x="-20%" y="-25%" width="140%" height="160%"><feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#173b36" flood-opacity=".10"/></filter></defs>',
         '<rect width="1000" height="500" rx="14" fill="#fff"/><text x="23" y="28" class="biz-canvas-kicker">CANVAS · MODÈLE EN LIGNE</text>']
    for a,b in [(0,1),(1,2),(2,3),(3,4)]:
        out.append(f'<path class="biz-svg-link" data-biz-link="{mid}" data-target="{b}" tabindex="0" role="button" aria-label="Lien courbe vers l’étape {b+1}" d="{link_path(positions[a],positions[b],w=244,h=102,bend=.28)}" marker-end="url(#biz-arrow-{mid})"><title>Vers l’étape {b+1}</title></path>')
    out.append(f'<path d="{link_path(positions[4],positions[0],w=244,h=102,bend=.30)}" fill="none" stroke="#b8cec5" stroke-width="1.7" stroke-dasharray="4 6" marker-end="url(#biz-arrow-soft-{mid})"/>')
    for i,g in enumerate(nodes):
        attrs=[]
        for k,v in g.attrs.items():
            if isinstance(v,list): v=' '.join(v)
            attrs.append(f'{k}="{esc(v)}"')
        x,y=positions[i];title=g.get('data-title','')
        out.append(f'<g {" ".join(attrs)} transform="translate({x},{y})"><rect class="biz-note-box" width="244" height="102" rx="10" filter="url(#biz-shadow-{mid})"/><path class="biz-note-title-bar" d="M10 0H234Q244 0 244 10V39H0V10Q0 0 10 0Z"/><circle class="biz-note-index-disc" cx="21" cy="20" r="10"/><text x="21" y="24" text-anchor="middle" class="biz-svg-sub">{i+1}</text><text x="39" y="26" class="biz-svg-title">{esc(title)}</text><text x="16" y="65" class="biz-svg-sub">Étape {i+1} · fonction et valeur</text><text x="16" y="87" class="biz-svg-sub">Cliquer · cible {i+1}</text></g>')
    out.append('</svg>')
    pattern=r'<svg class="biz-svg"[^>]*aria-label="'+re.escape(old['aria-label'])+r'".*?(?=<div class="biz-explanation")'
    current,n=re.subn(pattern,lambda _:''.join(out),current,count=1,flags=re.S)
    assert n==1,mid
assert current.rstrip().endswith("print(len(S.encode()),'octets')")
(R/'render_atlas.py').write_text(current)
print('4 entreprise Canvas SVG rebuilt')
