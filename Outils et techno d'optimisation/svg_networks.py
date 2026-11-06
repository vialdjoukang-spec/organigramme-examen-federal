"""Generate accessible, offline Obsidian Canvas/Graph-inspired SVG networks.

Run against either render_atlas.py (patches its source articles) or the
standalone HTML. All data-* attributes and explanation IDs are preserved.
"""
from pathlib import Path
from network_data import TECHS, MEDINA, SSP, FLOWS
import html
import re

ROOT = Path('/workspace/outils-puissants')
W, H = 1100, 720


def esc(value, quote=True):
    return html.escape(str(value), quote=quote)


def edge(a, b, w=244, h=102, pad=0):
    """Return card-boundary coordinates for the center-to-center direction."""
    ax, ay = a[0] + w / 2, a[1] + h / 2
    bx, by = b[0] + w / 2, b[1] + h / 2
    dx, dy = bx - ax, by - ay
    start_scale = min((w / 2 + 8) / (abs(dx) or 1), (h / 2 + 8) / (abs(dy) or 1))
    end_scale = min((w / 2) / (abs(dx) or 1), (h / 2) / (abs(dy) or 1))
    return ax + dx * start_scale, ay + dy * start_scale, bx - dx * end_scale, by - dy * end_scale


def link_path(a, b, bend=0.22, w=244, h=102):
    """A pronounced cubic Bezier between exact card edges, never card centers."""
    x1, y1, x2, y2 = edge(a, b, w=w, h=h)
    dx, dy = x2 - x1, y2 - y1
    length = (dx * dx + dy * dy) ** 0.5 or 1
    nx, ny = -dy / length, dx / length
    length = max(length, 220)
    offset = min(108, length * bend)
    c1 = (x1 + dx * .28 + nx * offset, y1 + dy * .28 + ny * offset)
    c2 = (x1 + dx * .72 + nx * offset, y1 + dy * .72 + ny * offset)
    return f'M {x1:.1f} {y1:.1f} C {c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {x2:.1f} {y2:.1f}'


def note_card(i, pos, label, subtitle, info, tech, kind, original, hub=False):
    x, y = pos
    w, h = 244, 102
    title_size = 18 if len(label) < 18 else 16
    classes = 'svg-node' + (' hub-node' if hub else '')
    return f'''<g class="{classes}" data-tech="{tech}" data-course="{kind}" data-node="{esc(original)}" data-display="{esc(label)}" data-role-info="{esc(info[0])}" data-description="{esc(info[1])}" data-saving="{esc(info[2])}" tabindex="0" role="button" aria-pressed="false" aria-controls="explain-{tech}-{kind}" aria-label="{esc(label + ' : ' + info[0])}" transform="translate({x},{y})">
<rect class="node-box" width="{w}" height="{h}" rx="10" filter="url(#shadow-{tech}-{kind})"/>
<path class="note-title-bar" d="M 10 0 H 234 Q 244 0 244 10 V 39 H 0 V 10 Q 0 0 10 0 Z"/>
<circle class="node-index-disc" cx="21" cy="20" r="10"/><text x="21" y="24" text-anchor="middle" class="node-index">{i+1}</text>
<rect class="note-grip" x="211" y="17" width="3" height="3" rx="1.5"/><rect class="note-grip" x="218" y="17" width="3" height="3" rx="1.5"/><rect class="note-grip" x="225" y="17" width="3" height="3" rx="1.5"/>
<text x="39" y="26" class="node-title" font-size="{title_size}">{esc(label)}</text>
<text x="16" y="65" class="node-subtitle">{esc(subtitle[:33])}</text>
<text x="16" y="87" class="node-action">Cliquer · cible {i+1}</text><text x="224" y="87" text-anchor="end" class="note-file">.md</text></g>'''


def graph_panel(tech, kind):
    """Small offline Graph View vignette: round variable nodes + dense curves."""
    # Normalized positions in a 258 x 150 panel. Edges are drawn first.
    pts = [(18, 26, 5), (56, 18, 8), (100, 31, 5), (149, 19, 6), (209, 34, 9),
           (34, 66, 9), (76, 66, 6), (122, 64, 12), (174, 65, 6), (222, 81, 5),
           (13, 112, 5), (58, 112, 6), (101, 119, 8), (149, 106, 5), (193, 116, 8), (232, 121, 4)]
    edges = [(0,1),(0,5),(1,2),(1,5),(1,6),(2,3),(2,6),(2,7),(3,4),(3,7),(3,8),
             (4,8),(4,9),(5,6),(5,10),(5,11),(6,7),(6,11),(6,12),(7,8),(7,12),(7,13),
             (8,9),(8,13),(8,14),(9,14),(9,15),(10,11),(11,12),(12,13),(12,14),(13,14),(14,15)]
    out = ['<g class="graph-vignette" aria-label="Mini vue Graph : notes circulaires et relations organiques">',
           '<rect x="810" y="326" width="266" height="212" rx="10" class="graph-panel"/>',
           '<text x="828" y="351" class="graph-kicker">GRAPH VIEW</text><circle cx="1049" cy="347" r="3" fill="#75a99a"/>']
    for a, b in edges:
        x1,y1,_=pts[a];x2,y2,_=pts[b]
        x1+=814;y1+=360;x2+=814;y2+=360
        mx=(x1+x2)/2;my=(y1+y2)/2 + (14 if (a+b)%2 else -14)
        out.append(f'<path d="M {x1} {y1} Q {mx:.1f} {my:.1f} {x2} {y2}" class="graph-edge"/>')
    for i,(x,y,r) in enumerate(pts):
        x+=814;y+=360
        out.append(f'<circle cx="{x}" cy="{y}" r="{r}" class="graph-dot'+(' graph-hub' if i==7 else '')+'"/>')
    out.append('<text x="828" y="521" class="graph-caption">Cercles = notes · traits = liens</text></g>')
    return ''.join(out)


def svg_network(tech, kind, existing):
    source = MEDINA if kind == 'medina' else SSP
    keys = FLOWS[tech]
    if tech == 'obsidian':
        labels = ['Vault', 'Notes', 'Liens ↔', 'Graph', 'Plugins', 'Index', 'Preuves']
        subtitles = ['Coffre local', 'Fiches sourcées', 'Navigation double', 'Vue des relations', 'Dataview · REST', 'Recherche ciblée', 'Documents liés']
        roles = [source['Vault'],source['Agent'],source['Index'],source['Index'],source['MCP'],source['Extraits'],source['Archive']]
        originals = keys
    else:
        labels = keys
        subtitles = [source[k][0] for k in keys]
        roles = [source[k] for k in keys]
        originals = keys

    # Canvas arrangement: staggered note cards around one stronger note, with
    # meaningful gaps for visibly curved, target-directed connectors.
    if tech == 'obsidian':
        positions = [(24,68),(303,32),(24,267),(806,105),(303,452),(24,449),(383,220)]
        routes = [(0,1),(0,2),(1,6),(2,6),(6,4),(6,3),(6,5),(4,3),(5,2),(1,3)]
    else:
        positions = [(24,70),(315,34),(799,65),(810,285),(564,435),(178,438),(429,220)]
        routes = [(0,1),(0,2),(0,6),(1,3),(2,6),(5,6),(6,4),(3,4),(5,0)]
    out = [f'<svg class="pro-network obsidian-canvas" viewBox="0 0 {W} {H}" role="group" aria-label="Canvas de notes {tech} {kind}" xmlns="http://www.w3.org/2000/svg">',
           f'<defs><marker id="arrow-{tech}-{kind}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#297766"/></marker><marker id="arrow-soft-{tech}-{kind}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" fill="#9cb9ae"/></marker><filter id="shadow-{tech}-{kind}" x="-20%" y="-25%" width="140%" height="160%"><feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#173b36" flood-opacity=".10"/></filter></defs>',
           f'<rect width="{W}" height="{H}" rx="14" fill="#fff"/><g class="canvas-heading"><circle cx="25" cy="26" r="5" fill="#75a99a"/><text x="39" y="31">VAULT / CANVAS · {esc(tech.upper())}</text><text x="1067" y="31" text-anchor="end">NOTES RELIÉES · {esc(kind.upper())}</text></g>']

    for j,(a,b) in enumerate(routes):
        target = labels[b]
        bend = .20 if j%2 else .25
        out.append(f'<path class="net-link" data-tech="{tech}" data-course="{kind}" data-target="{esc(target)}" tabindex="0" role="button" aria-label="Connexion courbe vers {esc(target)}" d="{link_path(positions[a],positions[b],bend)}" fill="none" stroke="#75a99a" stroke-width="2.4" marker-end="url(#arrow-{tech}-{kind})"><title>Vers {esc(target)}</title></path>')
    secondary = [(0,5),(1,4),(2,5)] if tech == 'obsidian' else [(1,6),(2,3),(4,5)]
    for a,b in secondary:
        out.append(f'<path class="outer-link" d="{link_path(positions[a],positions[b],-.22)}" fill="none" stroke="#b8cec5" stroke-width="1.6" stroke-dasharray="4 6" marker-end="url(#arrow-soft-{tech}-{kind})"/>')
    if tech == 'obsidian':
        out.append(graph_panel(tech,kind))
    for i,(pos,label,sub,info,original) in enumerate(zip(positions,labels,subtitles,roles,originals)):
        out.append(note_card(i,pos,label,sub,info,tech,kind,original,hub=(i==6)))
    metrics = {
'reseaux': (80,4,4,2,'Deux voies avancent sans relire deux fois les mêmes notes.'),
'obsidian': (95,4,4,2,'Le cerveau secondaire garde décisions, index et preuves hors du prompt.'),
'harness': (85,4,5,3,'Les portes automatiques arrêtent les défauts avant une relecture coûteuse.'),
'rag': (90,4,4,3,'Seuls les extraits nécessaires arrivent au modèle.'),
'web': (70,4,5,2,'La recherche reste ciblée ; les preuves originales sont conservées.'),
'ops': (90,4,4,3,'Files, reprises et mesures suppriment les exécutions répétées.'),
'bracelet': (85,4,3,1,'Un à trois outils par tâche : le bracelet évite l’arsenal complet.'),
'mcp': (65,4,4,3,'Des prises communes simplifient les outils, avec installation initiale.'),
'skills': (85,4,4,2,'Chaque protocole est chargé seulement au moment utile.'),
'scripts': (99,4,4,1,'Les contrôles déterministes ne consomment aucun token.'),
'ultra': (90,5,5,4,'Le socle commun mutualise preuves, mesure et reprise sans mélanger les formats.')}
    if kind == 'ssp':
        # Variante prudente : même architecture, gabarit et liste canonique distincts.
        economy, perf, quality, setup, sentence = metrics[tech]
    else:
        economy, perf, quality, setup, sentence = metrics[tech]
    out.append(f'<g class="diagram-metrics" aria-label="Estimations {tech} {kind}"><rect x="20" y="586" width="1060" height="116" rx="10"/><text x="38" y="614" class="metric-title">LÉGENDE CHIFFRÉE · ESTIMATION, NON MESURÉE</text><text x="38" y="644">Coût évité : ~{economy} % · 0 € d’API pour les étapes scripts</text><text x="38" y="671">Performance : {perf}/5 · Fiabilité/qualité : {quality}/5 · Mise en place : {setup}/5</text><text x="38" y="694" class="metric-note">{esc(sentence[:124])}</text></g>')
    out.append('</svg>')
    head = re.split(r'<svg class="pro-network[^>]*>', existing, maxsplit=1)[0]
    tail = existing[existing.index('<div class="node-explanation"'):]
    return head + ''.join(out) + tail


CSS = '''
/* t288u · Obsidian Canvas/Graph, cartes-notes plutôt qu'organigramme */
.pro-network.obsidian-canvas{display:block;width:100%;height:auto;background:#fff;border:1px solid #d9e4de;border-radius:14px;overflow:visible}.pro-network text{font-family:Atkinson,sans-serif;pointer-events:none}.canvas-heading text{font-size:11px;letter-spacing:1.3px;fill:#70847d}.canvas-heading circle{fill:#75a99a}.svg-node{cursor:pointer;outline:none}.svg-node .node-box{fill:#fff;stroke:#a9beb5;stroke-width:1.3;transition:fill .15s,stroke .15s,stroke-width .15s}.svg-node .note-title-bar{fill:#f1f5f2;stroke:none}.svg-node .node-index-disc{fill:#dce9e3}.svg-node .note-grip{fill:#a9beb5}.svg-node .note-file{font-size:10px;fill:#9aada5}.hub-node .node-box{stroke:#5e9585;stroke-width:2;fill:#fbfdfc}.hub-node .note-title-bar{fill:#e7efeb}.svg-node:hover .node-box,.svg-node:focus .node-box{fill:#f1f7f4;stroke:#297766;stroke-width:2.7}.svg-node:hover .note-title-bar,.svg-node:focus .note-title-bar{fill:#e3eee9}.svg-node[aria-pressed=true] .node-box{fill:#155d53;stroke:#155d53;stroke-width:2.7}.svg-node[aria-pressed=true] .note-title-bar{fill:#155d53}.svg-node[aria-pressed=true] .node-title,.svg-node[aria-pressed=true] .node-subtitle,.svg-node[aria-pressed=true] .node-action,.svg-node[aria-pressed=true] .node-file,.svg-node[aria-pressed=true] .node-index{fill:#fff}.svg-node[aria-pressed=true] .node-index-disc{fill:#297766}.node-index{font-size:11px;font-weight:700;fill:#155d53}.node-title{font-weight:700;fill:#173b36}.node-subtitle{font-size:14px;fill:#48615d}.node-action{font-size:11px;fill:#71847e}.net-link{cursor:pointer;outline:none;transition:stroke .15s,stroke-width .15s}.net-link:hover,.net-link:focus,.net-link.active{stroke:#b56a22!important;stroke-width:4!important}.outer-link{pointer-events:none}.network-card:has(.pro-network){background:#fff;padding:20px}.network-card .node-explanation{border-radius:12px}.graph-panel{fill:#f8faf9;stroke:#d7e2dd;stroke-width:1}.graph-kicker{font-size:10px;font-weight:700;letter-spacing:1.2px;fill:#567168}.graph-edge{fill:none;stroke:#9db8ae;stroke-width:1.15;opacity:.82}.graph-dot{fill:#78a696;stroke:#fff;stroke-width:1.2}.graph-dot:nth-of-type(3n){fill:#b5c9c1}.graph-hub{fill:#297766;stroke:#d8e8e1;stroke-width:3}.graph-caption{font-size:10px;fill:#71847e}.ssp .node-title{fill:#554224}.ssp .note-title-bar{fill:#f6f1e8}.ssp .node-index-disc{fill:#ede3d3}.ssp .node-box{stroke:#cbbd9f}.ssp .hub-node .node-box{stroke:#a78c55}.biz-svg{display:block;width:100%;height:auto;background:#fff;border:1px solid #d9e4de;border-radius:15px}.biz-svg text{font-family:Atkinson,sans-serif;pointer-events:none}.biz-svg-node{cursor:pointer;outline:none}.biz-svg-node rect.biz-note-box{fill:#fff;stroke:#a9beb5;stroke-width:1.5}.biz-svg-node .biz-note-title-bar{fill:#f1f5f2;stroke:none}.biz-svg-node .biz-note-index-disc{fill:#dce9e3}.biz-canvas-kicker{font-size:11px;letter-spacing:1.3px;fill:#70847d}.biz-svg-node:hover rect.biz-note-box,.biz-svg-node:focus rect.biz-note-box,.biz-svg-node[aria-pressed=true] rect.biz-note-box{fill:#edf5f1;stroke:#297766;stroke-width:3}.biz-svg-node[aria-pressed=true] rect.biz-note-box{fill:#155d53}.biz-svg-node[aria-pressed=true] .biz-note-title-bar,.biz-svg-node[aria-pressed=true] .biz-note-index-disc{fill:#155d53}.biz-svg-node[aria-pressed=true] text{fill:#fff}.biz-svg-link{cursor:pointer;fill:none;stroke:#75a99a;stroke-width:2.5}.biz-svg-link:hover,.biz-svg-link:focus{stroke:#b56a22;stroke-width:4}.biz-svg-title{font-size:19px;font-weight:700;fill:#173b36}.biz-svg-sub{font-size:13px;fill:#597169}@media(max-width:720px){.network-card:has(.pro-network){padding:10px}.pro-network{min-width:0}.network-head h4{font-size:16px}.tap-hint{margin-top:8px}.biz-svg{min-width:0}}
'''

for tech,_,_ in TECHS:
    for kind in ('medina','ssp'):
        source_path = ROOT/'render_atlas.py'
        s = source_path.read_text()
        start = s.index(f'<article class="network-card {kind}" data-network="{tech}-{kind}">')
        end = s.index('</article>',start) + len('</article>')
        s = s[:start] + svg_network(tech,kind,s[start:end]) + s[end:]
        source_path.write_text(s)

# Remove only the older generated SVG theme, then install the new one.
p = ROOT/'render_atlas.py'
s = p.read_text()
s = re.sub(r'/\* t287u · véritables diagrammes SVG sur fond blanc \*/.*?(?=/\* V3 · guide)', '', s, count=1, flags=re.S)
s = re.sub(r'/\* t288u · Obsidian Canvas/Graph.*?(?=/\* V3 · guide)', '', s, count=1, flags=re.S)
s = s.replace('/* V3 · guide',CSS+'/* V3 · guide',1)
p.write_text(s)
print('22 Canvas SVG patched in render_atlas.py')
