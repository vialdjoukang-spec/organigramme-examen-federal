#!/usr/bin/env python3
"""Corrige les erreurs de code et les éléments « disloqués » de PROGRESSION__FedMed.html (fichier de Grok),
sans toucher au contenu (textes, images, contours, flèches, couleurs) ni au style voulu.

Chaque correctif est un remplacement exact ou un petit bloc CSS/JS ajouté, commenté « corriger_fedmed.py » ;
une assertion vérifie qu'il s'applique une seule fois. Le document principal et la page embarquée du
recensement topo-systémique (bloc JSON data-emb="rts", imagerie et explorations) sont corrigés tous les deux.
Le mécanisme des cours (cadre.src=D.base+l.f…) n'est pas modifié : outils/injecter_cours_fedmed.py s'applique après.

Usage : python3 outils/corriger_fedmed.py ENTREE.html SORTIE.html
Détail des problèmes et des preuves : Claude/_progression/livraison/CORRECTIONS_FEDMED.md
"""
import sys, json, os, re, importlib.util

if len(sys.argv) != 3:
    sys.exit(__doc__)
ENTREE, SORTIE = sys.argv[1], sys.argv[2]
page = open(ENTREE, encoding='utf-8').read()


def remplacer_une_fois(texte, ancien, nouveau, nom):
    n = texte.count(ancien)
    assert n == 1, f'{nom} : point d\'accroche trouvé {n} fois (attendu 1)'
    return texte.replace(ancien, nouveau, 1)


# ---------------------------------------------------------------------------------------------------
# Blocs communs au visionneur « gm » (document principal et page rts embarquée)
# ---------------------------------------------------------------------------------------------------
CSS_GM = ('<style id="gm-correctif-css">/* corriger_fedmed.py — visionneur gm */\n'
          # C3 : le glisser du doigt sur un cliché doit faire défiler la fenêtre (touch-action:none bloquait
          #      le défilement sur téléphone, sans aucun geste propre au visionneur).
          '.gm .gm-fig{touch-action:manipulation}\n'
          # C4 : la bulle « Source » était coupée par overflow:hidden du panneau ; elle s'ancre désormais sur la
          #      ligne de métadonnées (pleine largeur du panneau) et ne dépasse plus du panneau.
          '.gm .gm-meta{position:relative}.gm .gm-meta .gm-src{position:static}'
          '.gm .gm-meta .gm-pop{left:10px;right:auto;bottom:calc(100% - 6px);width:min(420px,calc(100% - 20px));box-sizing:border-box}\n'
          # C5 : panneaux de même hauteur, la ligne âge/sexe/source reste en bas (plus de bloc noir vide sous elle).
          '.gm .gm-pan>.gm-meta{margin-top:auto}\n'
          '</style>')

JS_GM = ('<script id="gm-correctif-js">/* corriger_fedmed.py — visionneur gm.\n'
         ' C2 : le calque SVG (contours, flèches) était calé une seule fois, au chargement de l\'image ; rendu caché\n'
         '      (carte filtrée, détails fermés) il gardait une taille nulle, et après un redimensionnement (rotation du\n'
         '      téléphone) il débordait du cliché. Il est recalé à chaque changement de taille (ResizeObserver).\n'
         ' C6 : les pastilles numérotées étaient placées en % du cadre noir et non du cliché affiché (object-fit:contain) :\n'
         '      elles ne tombaient pas au départ de leur flèche. Elles sont placées dans le repère du cliché. */\n'
         '(function(){if(!window.GM||!window.GM.render)return;\n'
         'function caler(zw){var img=zw.querySelector("img.gm-img"),svg=zw.querySelector("svg.gm-svg");\n'
         ' if(!img||!svg||!img.naturalWidth||!img.naturalHeight)return;\n'
         ' var W=zw.clientWidth,H=zw.clientHeight;if(!W||!H)return;\n'
         ' var e=Math.min(W/img.naturalWidth,H/img.naturalHeight),dw=img.naturalWidth*e,dh=img.naturalHeight*e,x=(W-dw)/2,y=(H-dh)/2;\n'
         ' svg.style.left=x+"px";svg.style.top=y+"px";svg.style.width=dw+"px";svg.style.height=dh+"px";\n'
         ' zw.querySelectorAll(".gm-num").forEach(function(b){if(b.dataset.fx==null){b.dataset.fx=parseFloat(b.style.left)/100;b.dataset.fy=parseFloat(b.style.top)/100;}\n'
         '  b.style.left=(x+b.dataset.fx*dw)+"px";b.style.top=(y+b.dataset.fy*dh)+"px";});}\n'
         'var RO=window.ResizeObserver?new ResizeObserver(function(es){es.forEach(function(en){if(!en.target.isConnected){RO.unobserve(en.target);return;}caler(en.target);});}):null;\n'
         'var rendre=window.GM.render;\n'
         'window.GM.render=function(root){var r=rendre.apply(this,arguments);\n'
         ' if(root)root.querySelectorAll(".gm-zw").forEach(function(zw){var img=zw.querySelector("img.gm-img");\n'
         '  if(img)img.addEventListener("load",function(){caler(zw);});if(RO)RO.observe(zw);caler(zw);});\n'
         ' return r;};\n'
         '})();</script>')

ANCRE_CSS = '<style id="gm-css">'
ANCRE_JS = '<script id="gm-viewer">'


def corriger_gm(html, nom, css_en_plus=''):
    """Ajoute CSS_GM après la feuille gm-css et JS_GM après le script gm-viewer (avant tout appel à GM.render)."""
    assert html.count(ANCRE_CSS) == 1, f'{nom} : gm-css trouvé {html.count(ANCRE_CSS)} fois'
    fin_css = html.index('</style>', html.index(ANCRE_CSS)) + len('</style>')
    html = html[:fin_css] + CSS_GM.replace('</style>', css_en_plus + '</style>') + html[fin_css:]
    assert html.count(ANCRE_JS) == 1, f'{nom} : gm-viewer trouvé {html.count(ANCRE_JS)} fois'
    fin_js = html.index('</script>', html.index(ANCRE_JS)) + len('</script>')
    html = html[:fin_js] + JS_GM + html[fin_js:]
    assert html.count('id="gm-correctif-css"') == 1 and html.count('id="gm-correctif-js"') == 1, nom
    return html


# ---------------------------------------------------------------------------------------------------
# 1. Page embarquée du recensement topo-systémique (imagerie + explorations : 456 fenêtres)
# ---------------------------------------------------------------------------------------------------
CLE = 'data-emb="rts">'
assert page.count(CLE) == 1, 'bloc rts introuvable'
i = page.index(CLE) + len(CLE)
j = page.index('</script>', i)
encode = lambda h: json.dumps(h, ensure_ascii=False).replace('<', '\\u003c')  # encodage d'origine (aller-retour exact)
rts = json.loads(page[i:j])
assert encode(rts) == page[i:j], 'encodage du bloc rts inattendu'
rts = corriger_gm(rts, 'rts')
page = page[:i] + encode(rts) + page[j:]

# ---------------------------------------------------------------------------------------------------
# 2. Document principal
# ---------------------------------------------------------------------------------------------------
CSS_PRINCIPAL = (
    # C1 : « section.p{display:none} » (onglets de la page) masquait le panneau Pathologique des 60 visionneurs
    #      du document principal, qui est un <section class="gm-pan p">.
    '.gm section.gm-pan.p{display:flex}\n'
    # C7 : « .emb iframe{display:block} » annulait l'attribut hidden : en passant de Physiologie à Sémiologie,
    #      les deux pages embarquées restaient affichées l'une sous l'autre.
    '.emb iframe[hidden]{display:none}\n'
    # C8 : un visionneur (deux clichés de 420 px côte à côte) logé dans une carte de 280–360 px était écrasé
    #      (clichés de 160 px, barre de boutons sur quatre lignes) et étirait toute la rangée de cartes vides.
    #      La carte qui le porte occupe la largeur de la grille ; en dessous de 560 px les clichés s'empilent
    #      (même disposition que la règle téléphone d'origine, @media max-width:820px).
    '.grille>article:has(.fedmed-plus){grid-column:1/-1}\n'
    '.fedmed-plus{container-type:inline-size}\n'
    '@container (max-width:560px){.fedmed-plus .gm-pair{grid-template-columns:minmax(0,1fr)}.fedmed-plus .gm-fig{height:300px}}\n')
page_avant = page
page = corriger_gm(page, 'principal', CSS_PRINCIPAL)
assert len(page) > len(page_avant)

# Le point d'accroche de injecter_cours_fedmed.py doit rester intact et unique.
assert page.count("cadre.src=D.base+l.f;vieux.replaceWith(cadre);$('#vn').href=D.base+l.f;") == 1
assert page.count('</body>') == 1

# ---------------------------------------------------------------------------------------------------
# 3. Décision de Vial, 15.11.2026 : les couleurs du document (20 thèmes, bande EYE SPOT et sa
#    rotation) ne sont pas touchées. On ne change que la place du tiroir et les onglets du téléphone.
# ---------------------------------------------------------------------------------------------------
_coupure = page.index('data-emb="rts"')
_tete, _queue = page[:_coupure], page[_coupure:]

_remplacements_rail = [
    ('header.h{position:sticky;top:0;z-index:12;background:#fff;border-bottom:1px solid var(--trait);padding:8px 14px 0}',
     'header.h{position:sticky;top:0;z-index:50;background:#fff;border-bottom:1px solid var(--trait);padding:8px 14px 0}'),
    ('#vue{position:fixed;top:0;right:0;bottom:0;left:var(--mw);z-index:20;background:#fff;display:none;flex-direction:column}',
     '#vue{position:fixed;top:var(--ht);right:0;bottom:0;left:var(--mw);z-index:20;background:#fff;display:none;flex-direction:column}'),
    ('#fen{position:fixed;top:0;right:0;bottom:0;left:var(--mw);z-index:30;background:rgba(10,12,16,.62);display:none;align-items:flex-start;justify-content:center;padding:4vh 12px;overflow:auto}',
     '#fen{position:fixed;top:var(--ht);right:0;bottom:0;left:var(--mw);z-index:30;background:rgba(10,12,16,.62);display:none;align-items:flex-start;justify-content:center;padding:4vh 12px;overflow:auto}'),
    ('#menu{position:fixed;top:0;left:0;bottom:0;height:auto;width:min(84vw,320px);z-index:45;transform:translateX(-102%);transition:transform .2s;box-shadow:0 0 0 100vmax rgba(0,0,0,0)}',
     '#menu{position:fixed;top:0;left:0;bottom:0;height:auto;width:min(84vw,320px);z-index:60;transform:translateX(-102%);transition:transform .2s;box-shadow:0 0 0 100vmax rgba(0,0,0,0)}'),
    ('@media(max-width:520px){main{padding:10px}.grille{grid-template-columns:1fr}.sous{font-size:.76rem;line-height:1.3}h1{font-size:1rem}#theme .tx{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}nav.on button{padding:6px 10px}}',
     '@media(max-width:520px){main{padding:10px}.grille{grid-template-columns:1fr}.sous{font-size:.76rem;line-height:1.3}h1{font-size:1rem}#theme .tx{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}.hl{flex-direction:column;align-items:stretch;gap:4px}#theme{align-self:flex-end;margin-bottom:0}nav.on{flex:none;width:100%;max-width:100%;overflow:visible;flex-wrap:wrap}nav.on button{flex:1 1 45%;white-space:normal;text-align:center;padding:6px 8px;line-height:1.15}}'),
]
for _ancien, _nouveau in _remplacements_rail:
    _tete = remplacer_une_fois(_tete, _ancien, _nouveau, 'luxe ' + _ancien[:48])

page = _tete + _queue
assert 'if(e.fixe)return e.fixe' not in page
assert page.count('id="gm-correctif-css"') == 1
assert page.count('id=\\"gm-correctif-css\\"') == 1
assert '.gm{color:#0B2540}' in page
assert page.count("cadre.src=D.base+l.f;vieux.replaceWith(cadre);$('#vn').href=D.base+l.f;") == 1
assert page.count('</body>') == 1

import importlib
_luxe = importlib.import_module('luxe_ui') if __package__ else None
if _luxe is None:
    import importlib.util as _iu
    _sp = _iu.spec_from_file_location('luxe_ui', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'luxe_ui.py'))
    _luxe = _iu.module_from_spec(_sp)
    _sp.loader.exec_module(_luxe)
page = _luxe.injecter(page)
assert page.count('id="luxe-designer"') == 1
open(SORTIE, 'w', encoding='utf-8').write(page)
print(f'8 correctifs appliqués (C1–C8), couleurs de main restaurées, sortie {SORTIE} : {len(page.encode("utf-8")) / 1e6:.1f} Mo')
