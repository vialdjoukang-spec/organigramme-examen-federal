#!/usr/bin/env python3
"""RÉCEPTACLE — progression.html : page d'accueil unique du projet (ordre de Vial du 11.11.2026), zéro modèle.

Quatre onglets (cahier d'architecture v2 du 13.11.2026, Claude/_progression/CAHIER_ARCHITECTURE_v2.md) :
  1. Cours — une carte par SSP, nommée par le nom véritable du SSP (jamais « LOT ») ; chaque leçon porte le nom de son
     diagnostic (jamais « DX.n ») ; un clic ouvre le cours DANS la page (visionneuse plein écran, retour arrière du
     téléphone compris). Seuls les SSP audités et fusionnés (--audites) sont ouvrables ; les autres montrent leur jauge.
  2. Examens paracliniques — 9 sous-onglets, entrée primaire puis axe secondaire (partie 5, cartographie partie 7).
  3. Pharmacologie — S1–S12 + T ; chaîne Normal → VITE DIT CAFé → pathologie → traitement → classe → molécule ;
     S11 : coque CIM-10 (vue CIM-10 et vue par âge), classes avec matrice profil → chef de file.
  4. Sciences fondamentales — par système et transversaux (partie 6).
Source de vérité des onglets 2 à 4 : Claude/_progression/donnees/ (un fichier JSON par fiche, généré par
Claude/_progression/charpente.py, contrôlé par controle.py). Le script assemble ces fichiers dans la page ; un champ
égal au gabarit (« — ») n'est pas recopié : la page le reconstruit depuis gabarits.json.
Forme (partie 0.6 et ordres du 13.11.2026) : Atkinson Hyperlegible, ≈ 15 px, colonne ≤ 760 px, rail vertical, une seule
fenêtre ouverte, fond blanc ; bouton « Thème » : 20 thèmes (Claude/_progression/themes.json), 3 teintes atténuées au plus en
fonds locaux, texte ≥ 7:1 ; couleurs à sens fixe en marqueurs ; chaîne pharmacologique sur une ligne par station ;
bande latérale de menu constante et contextuelle (plan numéroté de la page ou de la fiche ouverte, tiroir sur téléphone).

Usage : python3 outils/receptacle.py --audites 1-32 --sortie progression.html [--carte carte.json] [--base ./]
"""
import os, re, csv, json, html, glob, argparse, datetime

LECONS = ['A'] + [f'DX{i}' for i in range(1, 11)]
E = html.escape


def plage(s):
    out = set()
    for bloc in filter(None, re.split(r'[,\s]+', s or '')):
        bloc = bloc.split('=')[0]
        a, _, b = bloc.partition('-')
        out.update(range(int(a), int(b or a) + 1))
    return out


def fichier(lot, l):
    return f'Claude/LOT_{lot:03d}/LOT_{lot:03d}_Phase_A_V0.html' if l == 'A' else f'Claude/LOT_{lot:03d}/LOT_{lot:03d}_Phase_B_V0_DX.{l[2:]}.html'


def noms_dx(lot):
    """Nom de chaque diagnostic : liste gelée, sinon bandeau du cours, sinon titre du fichier."""
    noms, graves = {}, {}
    p = f'Claude/LOT_{lot:03d}/LISTE_DX_CANONIQUE.md'
    if os.path.exists(p):
        for m in re.finditer(r'^DX\.(\d+)\s*—\s*(.+?)\s*(🚩.*)?$', open(p, encoding='utf-8').read(), re.M):
            noms[f'DX{m.group(1)}'] = m.group(2).strip()
            graves[f'DX{m.group(1)}'] = bool(m.group(3))
    for l in LECONS[1:]:
        f = fichier(lot, l)
        if l in noms or not os.path.exists(f):
            continue
        h = open(f, encoding='utf-8', errors='ignore').read(200000)
        m = (re.search(r'class="fm-nom"[^>]*>(.*?)</div>', h, re.S) or re.search(r'<h[12][^>]*>\s*(?:<[^>]+>)*\s*DX\.\d+\s*[—–-]\s*(.*?)</h[12]>', h, re.S)
             or re.search(r'<title>[^<]*DX\.\d+\s*[—–-]?\s*([^<|]+)', h))
        if m:
            n = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', m.group(1)))).strip()
            n = re.sub(r'^DX\.\d+\s*[—–-]\s*', '', n)
            if n and not re.match(r'^[GSFO]\d', n):
                noms[l] = n
    return noms, graves



def progression(dossier):
    """Assemble structure, gabarits et fiches ; chaque fiche est allégée des champs encore égaux à son gabarit."""
    lire = lambda p: json.load(open(p, encoding='utf-8'))
    if not os.path.exists(os.path.join(dossier, 'structure.json')):
        return {'S': None, 'G': {}, 'F': {}}
    G = lire(os.path.join(dossier, 'gabarits.json'))
    F = {}
    for p in sorted(glob.glob(os.path.join(dossier, '*', '*.json'))):
        try:
            f = lire(p)
        except ValueError:
            continue
        g = G.get(f.get('type'), {})
        F[f['id']] = {k: v for k, v in f.items() if k not in g or g[k] != v}
    return {'S': lire(os.path.join(dossier, 'structure.json')), 'G': G, 'F': F}


def _lum(h):
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))
    return .2126 * f(r) + .7152 * f(g) + .0722 * f(b)


def contraste(a, b):
    x, y = sorted((_lum(a), _lum(b)), reverse=True)
    return (x + .05) / (y + .05)


ATT_MIN, ATT_MAX, CONTRASTE_MIN = 0.60, 0.80, 7.0  # bornes (ordre de Vial du 13.11.2026) : refus de générer hors bornes
# Bande EYE SPOT : hsl(teinte de page, S, L) atténuée vers le blanc selon le thème ; S et L par famille de page, pour que deux pages
# de familles différentes à teinte proche restent distinctes (profondeur et saturation).
# Plainte de Vial du 13.11.2026 (la bande doit se distinguer dès l'entrée, à chaque thème) : atténuation de la bande fixée au bas
# de la fourchette (EYE_ATT = 60 %), saturation plancher EYE_S_MIN, et teinte écartée d'au moins EYE_ECART degrés des teintes de
# zones du thème (menu, rail, tableau, mot, bande, encadré) par projection de la roue sur les arcs libres (eye_libres, eye_teinte).
EYE_ATT, EYE_S_MIN, EYE_ECART = 0.60, 0.70, 40
EYE_PALIERS = {k: (max(s, EYE_S_MIN), l) for k, (s, l) in {'cours': (0.72, 0.42), 'examens': (0.84, 0.35), 'pharmaco': (0.55, 0.48), 'fondamentales': (0.66, 0.40), 'fiche': (0.78, 0.45), 'vue': (0.72, 0.42)}.items()}
EYE_S, EYE_L = EYE_PALIERS['cours']


def ecart(a, b):
    d = abs(a - b) % 360
    return min(d, 360 - d)


def eye_libres(zones):
    """Teintes (degrés entiers) écartées d'au moins EYE_ECART de chaque teinte de zone ; même calcul que libres() du JS."""
    return [d for d in range(360) if all(ecart(d, z) >= EYE_ECART for z in zones)]


def eye_teinte(h, libres):
    """Projette la teinte brute h (0-359) sur les arcs libres, en gardant l'ordre et l'étalement ; même calcul que le JS."""
    return libres[h * len(libres) // 360]


def eye_hex(h0, zones, cle, k):
    """Couleur de bande de la page de rang k (rangs du JS : cours = 0, puis examens:i, pharmaco:i, fondamentales:i entrelacés)."""
    s, l = EYE_PALIERS.get(cle.split(':')[0], EYE_PALIERS['cours'])
    return attenue(hsl_rgb(eye_teinte((h0 + round(137.508 * k)) % 360, eye_libres(zones)), s, l), EYE_ATT)


def attenue(rgb, a):
    return '#' + ''.join('%02x' % int(c * (1 - a) + 255 * a + 0.5) for c in rgb)


def hex_rgb(h):
    return tuple(int(h[k:k + 2], 16) for k in (1, 3, 5))


def hsl_rgb(h, s, l):
    """Même calcul que hsl() du JS de la page (teinte entière en degrés)."""
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2
    r, g, b = [(c, x, 0), (x, c, 0), (0, c, x), (0, x, c), (x, 0, c), (c, 0, x)][int(h // 60) % 6]
    return tuple(int((v + m) * 255 + 0.5) for v in (r, g, b))


def teinte(h):
    import colorsys
    return round(colorsys.rgb_to_hls(*(v / 255 for v in hex_rgb(h)))[0] * 360) % 360


def themes(chemin, rangs={'cours': 0}):
    """20 thèmes (ordres de Vial du 13.11.2026). Au plus 3 couleurs par thème, la bande EYE SPOT comptant parmi elles :
    les deux premières teintent les zones (menu, rail, tableau, mot, bande, encadré), la dernière est la graine EYE SPOT
    (bande unique de tous les titres de la page active, teinte tournée par page dans le JS). Atténuation 60-80 % vers le
    blanc, variable par thème et par usage ; contraste >= 7:1 calculé ici : zones avec #111 et #222, bande EYE SPOT avec
    #000 et #111 sur les 360 teintes possibles (échec = arrêt). La bande est posée dès le premier rendu : --eye de la page
    d'entrée (rangs : cours et premières pages des onglets) écrit dans le CSS du thème, sans attendre le JS ni montrer de gris.
    Rend (liste pour la page, CSS par thème)."""
    T = json.load(open(chemin, encoding='utf-8'))
    roles, usages, out, css = T['roles'], T['usages'], [], []
    assert len(T['themes']) == 20, 'il faut 20 thèmes'
    for i, t in enumerate(T['themes']):
        n = len(t['couleurs'])
        assert 2 <= n <= 3, f"thème {i + 1} : {n} couleurs (3 au plus, EYE SPOT comprise)"
        att = t['attenuation']
        for u in usages:
            assert ATT_MIN <= att[u] <= ATT_MAX, f"thème {i + 1} : atténuation {u} = {att[u]} hors 60-80 %"
        v, cmin = [], 99
        for r in roles:
            j = t['roles'][r]
            assert -1 <= j < n - 1, f"thème {i + 1} : rôle {r} sur la couleur {j} (la dernière est réservée à EYE SPOT)"
            h = attenue(hex_rgb(t['couleurs'][j]['base']), att[r]) if j >= 0 else '#ffffff'
            c = min(contraste(h, '#111111'), contraste(h, '#222222'))
            assert c >= CONTRASTE_MIN, f"thème {i + 1} : contraste {c:.2f} < 7 sur {r} {h}"
            cmin = min(cmin, c)
            v.append(f'--t-{r}:{h};--b-{r}:{h if j >= 0 else "#6b6b6b"}')
        h0, ae = (teinte(t['couleurs'][-1]['base']) + 29 * i) % 360, EYE_ATT  # graine décalée par thème : une même page change de couleur d'un thème à l'autre
        assert ATT_MIN <= ae <= ATT_MAX
        zones = sorted({teinte(t['couleurs'][t['roles'][r]]['base']) for r in roles if t['roles'][r] >= 0})
        libres = eye_libres(zones)
        assert len(libres) >= 120, f"thème {i + 1} : {len(libres)} teintes libres seulement pour EYE SPOT"
        assert all(ecart(eye_teinte(d, libres), z) >= EYE_ECART for d in range(360) for z in zones), f"thème {i + 1} : bande trop proche d'une zone"
        assert min(s for s, l in EYE_PALIERS.values()) >= EYE_S_MIN
        ce = min(min(contraste(attenue(hsl_rgb(d, sp, lp), ae), '#000000'), contraste(attenue(hsl_rgb(d, sp, lp), ae), '#111111')) for d in range(360) for sp, lp in EYE_PALIERS.values())
        assert ce >= CONTRASTE_MIN, f"thème {i + 1} : bande EYE SPOT, contraste {ce:.2f} < 7"
        ex = {c: eye_hex(h0, zones, c, k) for c, k in rangs.items()}
        css.append(f':root[data-theme="{i}"]{{{";".join(v)};--eye:{ex["cours"]}}}')
        css.extend(f':root[data-theme="{i}"][data-page="{c}"]{{--eye:{x}}}' for c, x in ex.items() if c != 'cours')
        teintes = [attenue(hex_rgb(c['base']), att['menu']) for c in t['couleurs'][:-1]] + [ex['cours']]  # aperçu : zones + bande EYE SPOT de l'accueil
        out.append({'nom': t['nom'], 'teintes': teintes, 'eye': {'h0': h0, 'a': ae, 'p': EYE_PALIERS, 'z': zones, 'e': EYE_ECART},
                    'attenuation': att, 'contraste_min': round(min(cmin, ce), 2)})
    return out, ''.join(css)


POLICE = ''.join("@font-face{font-family:'Atkinson Hyperlegible';font-style:%s;font-weight:%s;font-display:swap;src:url('BASEClaude/_polices/atkinson-hyperlegible-latin-%s-%s.woff2') format('woff2')}" % (s, w, w, s) for w in ('400', '700') for s in ('normal', 'italic'))

CSS = """
:root{--encre:#111;--doux:#222;--trait:#c4c4c4;--neutre:#6b6b6b;--mw:258px;--ht:96px;
--eye:#ffffff;--eye-b:rgba(0,0,0,.24);
--bleu:#0646db;--rouge:#b10521;--vert:#03651b;--violet:#7906df;--ocre:#8a6203;--orange:#c24a05}
/* Thèmes (Claude/_progression/themes.json) : au plus 3 teintes atténuées de 60 à 80 % (EYE SPOT comprise), texte #111/#222 >= 7:1,
   fond de page blanc. EYE SPOT : tous les titres et sous-titres de la page active sur une seule bande --eye (teinte propre à la page
   et au thème, calculée par eye() dans le JS), texte #000 >= 7:1 ; les sous-titres varient en épaisseur et en graisse, jamais en couleur. Les couleurs à sens fixe (partie 0.6) ne sont que des marqueurs : liseré, bordure ou pastille. */
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;background:#fff}body{margin:0;background:#fff;color:var(--encre);font:15px/1.45 "Atkinson Hyperlegible",Verdana,system-ui,sans-serif}
button,input{font-family:inherit;color:var(--encre)}
header.h{position:sticky;top:0;z-index:12;background:#fff;border-bottom:1px solid var(--trait);padding:8px 14px 0}
h1{font-size:1.15rem;margin:0 0 4px;display:inline-block}.sous{color:var(--doux);font-size:.87rem;margin:0 0 6px}
.hl{display:flex;gap:8px;align-items:flex-end;min-width:0}
nav.on{flex:1;min-width:0;display:flex;gap:4px;overflow-x:auto;scrollbar-width:none}nav.on::-webkit-scrollbar{display:none}
nav.on button{font:inherit;font-weight:700;border:2px solid var(--neutre);border-bottom:0;background:#fff;padding:7px 13px;border-radius:10px 10px 0 0;white-space:nowrap;cursor:pointer}
nav.on button.a{background:var(--eye);border-color:#111;color:#000}
#theme{font:inherit;font-weight:700;border:2px solid var(--neutre);background:#fff;border-radius:10px;padding:5px 10px;margin-bottom:5px;cursor:pointer;flex:none;display:flex;gap:6px;align-items:center}
.pal{display:inline-flex;gap:2px}.pal i{width:12px;height:12px;border-radius:3px;border:1px solid var(--neutre);display:block}
#themes{position:absolute;right:10px;top:100%;z-index:40;background:#fff;border:2px solid var(--neutre);border-radius:12px;padding:8px;display:none;grid-template-columns:repeat(2,minmax(0,1fr));gap:4px;width:min(360px,calc(100vw - 20px));max-height:70vh;overflow:auto;box-shadow:0 8px 24px rgba(0,0,0,.18)}
#themes.a{display:grid}#themes button{font:inherit;font-size:.86rem;display:flex;gap:6px;align-items:center;border:1px solid var(--trait);background:#fff;border-radius:8px;padding:5px 7px;cursor:pointer;text-align:left}
#themes button[aria-pressed=true]{border:2px solid #111;font-weight:700}
.cadre{display:grid;grid-template-columns:var(--mw) minmax(0,1fr);align-items:start}
/* Bande latérale de menu : constante, contextuelle, numérotée */
#menu{position:sticky;top:var(--ht);height:calc(100vh - var(--ht));overflow:auto;background:var(--t-menu);border-right:1px solid var(--b-menu);padding:10px 8px 40px;font-size:.9rem;z-index:8}
#menu .mt{margin:0 0 8px;padding:6px 8px;border-radius:8px;font-weight:700;font-size:.82rem;text-transform:uppercase;letter-spacing:.06em;line-height:1.3}
#menu ol{list-style:none;margin:0;padding:0;counter-reset:m}
#menu li.g{font-weight:700;font-size:.8rem;text-transform:uppercase;letter-spacing:.05em;margin:10px 0 3px;padding:2px 6px;border-radius:6px}
#menu li.n{counter-increment:m}#menu a,#menu .v{display:flex;gap:7px;padding:4px 6px;border-radius:6px;text-decoration:none;color:var(--encre);line-height:1.25}
#menu li.n a::before,#menu li.n .v::before{content:counter(m);flex:0 0 1.9em;text-align:right;font-weight:700;font-size:.8rem;background:#fff;border:1px solid var(--neutre);border-radius:5px;padding:0 3px;align-self:flex-start}
#menu a:hover{background:#fff}#menu a.a{background:#fff;font-weight:700;box-shadow:inset 4px 0 0 #111}
#menu .x{display:none}
#planbtn{display:none}
/* EYE SPOT : une seule bande pour tous les titres de la page active */
h1,#menu .mt,#menu li.g,.c .code,.c h2,#vue .tete,.col h2,.col h3,.col h4,.ch>.eh,#fen .ft h3,#fen h4,#fen h5,#sco h3{background:var(--eye)!important;color:#000}
h1,.col h2,.col h3,.col h4,#fen .ft h3,#fen h4,#fen h5,#sco h3{border:1px solid var(--eye-b)}
h1{padding:3px 10px;border-radius:8px}
main{min-width:0;padding:14px;background:#fff}
section.p{display:none}section.p.a{display:block}
.barre{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:0 0 12px}
.barre input{flex:1 1 220px;font:inherit;padding:10px 12px;border:1px solid var(--neutre);border-radius:10px;background:#fff}
.pu{font:inherit;font-weight:700;border:2px solid var(--neutre);background:#fff;border-radius:999px;padding:6px 13px;cursor:pointer}.pu.a{background:var(--t-mot);border-color:#111}
.grille{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}
.c{background:#fff;border:1px solid var(--trait);border-radius:14px;padding:0 0 10px;overflow:hidden}
.c>*{margin-left:14px;margin-right:14px}.c .code{margin:0;padding:6px 14px 0;font-size:.82rem;font-weight:700;letter-spacing:.02em}
.c h2{font-size:1rem;margin:0 0 6px;padding:2px 14px 8px;line-height:1.25;border-bottom:1px solid var(--eye-b)}
.j{display:grid;grid-template-columns:1fr 44px;align-items:center;gap:8px;margin-top:6px;margin-bottom:6px}.j span{font-size:.8rem;font-weight:700;text-align:right}
.t{height:8px;background:#e6e6e6;border:1px solid #9a9a9a;border-radius:99px;overflow:hidden}.f{height:100%;width:var(--p);background:#3d3d3d}
details summary{cursor:pointer;font-weight:700;font-size:.87rem;padding:4px 0}
.ls{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:2px}
.ls a,.ls span{display:flex;gap:8px;align-items:baseline;padding:7px 8px;border-radius:8px;text-decoration:none;color:var(--encre);font-size:.93rem;line-height:1.3}
.ls a{background:#fff;border:1px solid var(--trait);border-left:5px solid var(--neutre)}.ls a:hover{background:var(--t-encadre)}.ls span{color:var(--doux)}
.ls .g{flex:none}.ls .mono{font-weight:700}
.vide{color:var(--doux);font-size:.93rem;padding:4px 0;margin:0}
#vue{position:fixed;top:0;right:0;bottom:0;left:var(--mw);z-index:20;background:#fff;display:none;flex-direction:column}#vue.a{display:flex}
#vue .tete{display:flex;gap:6px;align-items:center;padding:6px 8px;border-bottom:1px solid var(--eye-b)}
#vue .tete b{flex:1;min-width:0;font-size:.87rem;line-height:1.2;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
#vue .tete small{display:block;font-weight:400}
#vue button,#vue a.x{font:inherit;font-weight:700;border:2px solid #111;background:#fff;color:#111;border-radius:9px;padding:6px 11px;cursor:pointer;text-decoration:none;flex:none}
#vue iframe{flex:1;border:0;width:100%}
/* ----- Modules : rail vertical + colonne <= 760 px ; le plan numéroté est dans la bande latérale ----- */
.mod{display:grid;grid-template-columns:172px minmax(0,760px);gap:16px;justify-content:start;align-items:start}
.rail{position:sticky;top:calc(var(--ht) + 10px);max-height:calc(100vh - var(--ht) - 20px);overflow:auto;display:flex;flex-direction:column;gap:2px;background:var(--t-rail);border:1px solid var(--b-rail);border-radius:12px;padding:6px}
.rail button{font:inherit;font-size:.9rem;text-align:left;border:0;background:transparent;padding:6px 7px;cursor:pointer;display:flex;gap:7px;align-items:baseline;border-radius:8px;line-height:1.2}
.rail button b{flex:0 0 auto;min-width:2.5em;text-align:center;font-size:.78rem;background:#fff;border:1px solid var(--neutre);border-radius:6px;padding:0 3px}
.rail button.a{background:#fff;font-weight:700;box-shadow:inset 4px 0 0 #111}
.col{min-width:0;max-width:760px}
.col h2{font-size:1.2rem;margin:0 0 6px;padding:9px 12px;border-radius:10px;font-weight:800}
.col h3{font-size:1.05rem;margin:18px 0 6px;display:flex;gap:8px;align-items:baseline;padding:5px 8px;border-radius:8px;scroll-margin-top:calc(var(--ht) + 8px)}
.num{background:#fff;border:1px solid var(--neutre);border-radius:6px;text-align:center;min-width:1.8em;padding:0 4px;font-weight:700}
.col h4{font-size:.9rem;margin:8px 0 3px;padding:2px 8px;border-radius:6px}
.meta{color:var(--doux);font-size:.87rem;margin:0 0 8px}.meta b{color:var(--encre)}
.bas{display:flex;gap:6px;flex-wrap:wrap;margin:8px 0}
.lf{list-style:none;margin:0;padding:0;display:grid;gap:3px}
.lf li{scroll-margin-top:calc(var(--ht) + 8px)}
.lf button,.lien{font:inherit;text-align:left;width:100%;border:1px solid var(--trait);background:#fff;border-radius:8px;padding:6px 10px;cursor:pointer;line-height:1.3}
.lf button{border-left:5px solid var(--neutre)}.lf button:hover,.lien:hover{background:var(--t-encadre)}.lf small,.lien small{color:var(--doux);font-size:.8rem;margin-left:6px;overflow-wrap:anywhere}
.lien{display:inline;width:auto;padding:1px 6px;border-radius:6px}
.etq,.mot{font-size:.78rem;background:var(--t-mot);border:1px solid var(--b-mot);border-radius:99px;padding:0 7px;margin-left:4px;font-weight:700;box-shadow:inset 3px 0 0 var(--orange)}
.mot{box-shadow:none;margin:0}
/* Couleurs à sens fixe (partie 0.6) : marqueurs seulement */
.c-bleu,.k-bleu{box-shadow:inset 6px 0 0 var(--bleu)!important}.c-rouge,.k-rouge{box-shadow:inset 6px 0 0 var(--rouge)!important}.c-vert,.k-vert{box-shadow:inset 6px 0 0 var(--vert)!important}
.c-violet,.k-violet{box-shadow:inset 6px 0 0 var(--violet)!important}.c-ocre,.k-ocre{box-shadow:inset 6px 0 0 var(--ocre)!important}.c-orange,.k-orange{box-shadow:inset 6px 0 0 var(--orange)!important}
[class*="c-"],[class*="k-"]{padding-left:12px!important}
.legende,.chaine{display:flex;flex-wrap:wrap;gap:3px 12px;font-size:.82rem;margin:0 0 10px;align-items:center}
.legende span,.chaine span{display:inline-flex;align-items:center;gap:5px;box-shadow:none!important;padding:0!important;font-weight:700}
.legende span::before,.chaine span::before{content:"";width:11px;height:11px;border-radius:50%;background:var(--pt)}
.legende .c-bleu,.chaine .c-bleu{--pt:var(--bleu)}.legende .c-rouge,.chaine .c-rouge{--pt:var(--rouge)}.legende .c-vert,.chaine .c-vert{--pt:var(--vert)}.legende .c-violet{--pt:var(--violet)}.legende .c-ocre{--pt:var(--ocre)}.legende .c-orange{--pt:var(--orange)}
/* Chaîne pharmacologique : une ligne par station, gauche → droite */
.defile{overflow-x:auto;overscroll-behavior-x:contain;scroll-snap-type:x proximity;margin:6px 0 12px;border:1px solid var(--trait);border-radius:10px}
.glisse{display:none;font-size:.8rem;color:var(--doux);margin:4px 0 0}
.ch{display:grid;grid-template-columns:minmax(150px,1.15fr) 16px minmax(150px,1fr) 16px minmax(118px,.85fr) 16px minmax(165px,1.2fr);min-width:631px;font-size:.88rem}
.ch>.eh{font-weight:700;font-size:.8rem;padding:5px 7px;scroll-snap-align:start;display:flex;align-items:center;gap:5px}
.ch>.eh::before{content:"";width:10px;height:10px;border-radius:50%;background:var(--pt);flex:none}.ch>.eh.fl::before{display:none}
.ch>div{padding:6px 7px;border-bottom:1px solid var(--trait);min-width:0;overflow-wrap:anywhere}
.ch>.fl{padding:6px 0;text-align:center;font-weight:700;color:var(--encre)}
.ch .st{scroll-margin-top:calc(var(--ht) + 8px)}
.sn{display:inline-block;background:var(--t-mot);border:1px solid var(--b-mot);border-radius:6px;padding:0 6px;font-weight:700;margin-right:4px}
.ch p{margin:3px 0 0}.ch .si{font-size:.84rem}
.vdc{list-style:none;margin:0;padding:0;display:grid;gap:2px}.vdc b{display:inline-block;min-width:1.4em;text-align:center;background:var(--t-mot);border:1px solid var(--b-mot);border-radius:4px;margin-right:4px}
.vdc+details,.ch details{font-size:.8rem;margin-top:3px}.ch details summary{font-size:.8rem;padding:0}.ch details span{display:inline-block;margin:2px 3px 0 0;padding:0 4px;border:1px solid var(--trait);border-radius:4px}
.barre-t{display:grid;gap:3px}
.barre-t>*{font:inherit;font-size:.86rem;text-align:left;background:#fff;border:1px solid var(--trait);border-radius:6px;padding:3px 8px;cursor:help;line-height:1.3}.barre-t button{cursor:pointer}.barre-t button:hover{background:var(--t-encadre)}
/* Psychiatrie : pathologie CIM-10 → barre de traitement, même ligne */
.lp{display:grid;grid-template-columns:minmax(140px,1fr) 18px minmax(165px,1.25fr);gap:6px;align-items:start;margin:6px 0;min-width:340px}
.lp>.fl{font-weight:700;padding-top:6px;text-align:center}.lp>.lien{width:100%}
.lpd{overflow-x:auto;overscroll-behavior-x:contain}
.bande{border:1px solid var(--b-bande);background:var(--t-bande);border-radius:10px;padding:7px 10px;margin:8px 0;scroll-margin-top:calc(var(--ht) + 8px)}
.bande>button{font:inherit;font-weight:700;border:0;background:none;padding:0;cursor:pointer;text-align:left}
.bande .meta{color:var(--encre)}
/* Fenêtre unique, occultante ; la bande de menu reste visible à gauche */
#fen{position:fixed;top:0;right:0;bottom:0;left:var(--mw);z-index:30;background:rgba(10,12,16,.62);display:none;align-items:flex-start;justify-content:center;padding:4vh 12px;overflow:auto}#fen.a{display:flex}
#fen .fc{background:#fff;width:100%;max-width:760px;border-radius:14px;padding:14px 18px 22px;border:1px solid var(--trait)}
#fen .ft{display:flex;gap:8px;align-items:flex-start}#fen .ft h3{flex:1;margin:0;font-size:1.15rem;font-weight:800;padding:9px 12px;border-radius:10px}
#fen .x{font:inherit;border:2px solid #111;background:#fff;font-weight:700;border-radius:8px;padding:4px 10px;cursor:pointer}
#fen h4{margin:14px 0 4px;font-size:.98rem;padding:4px 8px;border-radius:6px;scroll-margin-top:8px}
#fen table{border-collapse:collapse;width:100%;font-size:.88rem;margin:2px 0}#fen td,#fen th{border:1px solid var(--trait);padding:5px 6px;vertical-align:top;text-align:left}
#fen th{background:var(--t-tableau);font-weight:700}#fen td.l{width:38%;font-weight:700;background:var(--t-tableau)}#fen h5{margin:10px 0 3px;font-size:.9rem;padding:2px 8px;border-radius:5px}#fen ul{margin:2px 0;padding-left:1.2em}
#fen .calc{border:1px solid var(--trait);border-left:4px solid var(--bleu);border-radius:6px;padding:4px 10px 6px;margin:6px 0}
#fen .calc p{margin:4px 0}#fen .calc .src{font-size:.82rem}
#fen pre.fx,#fen pre.ex{white-space:pre-wrap;overflow-wrap:anywhere;margin:4px 0;padding:6px 8px;border-radius:5px;background:var(--t-tableau);color:#111;font-size:.86rem}
/* Glossaire : sigle en survol (souris : title ; clavier et toucher : focus, bulle dessinée), score ouvert en fenêtre au clic. */
abbr[title]{text-decoration:underline dotted 1px;text-underline-offset:2px;cursor:help;position:relative;border-radius:3px}
abbr[title]:focus{outline:2px solid #111;outline-offset:1px}
#bulle{position:fixed;z-index:60;display:none;max-width:min(320px,calc(100vw - 24px));background:#fff;color:#111;border:2px solid #111;border-radius:8px;padding:5px 9px;font-size:.84rem;font-weight:400;line-height:1.35;box-shadow:0 3px 10px rgba(0,0,0,.2);pointer-events:none}#bulle.a{display:block}
button.sc{font:inherit;color:inherit;background:none;border:0;border-bottom:2px solid currentColor;padding:0 1px;margin:0;cursor:pointer;line-height:inherit}
button.sc::after{content:" ⓘ";font-size:.8em}button.sc:focus-visible{outline:2px solid #111;outline-offset:1px}
#sco{position:fixed;inset:0;z-index:55;background:rgba(10,12,16,.55);display:none;align-items:flex-start;justify-content:center;padding:6vh 12px;overflow:auto}#sco.a{display:flex}
#sco .fc{background:#fff;width:100%;max-width:640px;border-radius:14px;padding:14px 18px 20px;border:1px solid var(--trait)}
#sco .ft{display:flex;gap:8px;align-items:flex-start}#sco h3{flex:1;margin:0;font-size:1.08rem;font-weight:800;padding:8px 12px;border-radius:10px}
#sco .x{font:inherit;border:2px solid #111;background:#fff;font-weight:700;border-radius:8px;padding:4px 10px;cursor:pointer}
#sco h4{margin:12px 0 4px;font-size:.95rem;font-weight:800}#sco table{border-collapse:collapse;width:100%;font-size:.88rem}#sco td,#sco th{border:1px solid var(--trait);padding:5px 6px;vertical-align:top;text-align:left}
#sco th{background:var(--t-tableau)}#sco td.pt{width:22%;font-weight:700;white-space:nowrap}#sco .src{font-size:.82rem}
#fen pre.fx{font-family:ui-monospace,'DejaVu Sans Mono',Consolas,'Courier New',monospace;font-weight:700}#fen pre.ex{font-family:inherit}
.tw{overflow-x:auto}
@media(max-width:1180px){.mod{grid-template-columns:minmax(0,1fr);gap:8px}
 .rail{position:static;max-height:none;flex-direction:row;overflow-x:auto}.rail button{white-space:nowrap}}
@media(max-width:900px){:root{--mw:0px}.cadre{grid-template-columns:minmax(0,1fr)}
 #menu{position:fixed;top:0;left:0;bottom:0;height:auto;width:min(84vw,320px);z-index:45;transform:translateX(-102%);transition:transform .2s;box-shadow:0 0 0 100vmax rgba(0,0,0,0)}
 #menu.ouvert{transform:none;box-shadow:0 0 0 100vmax rgba(10,12,16,.45)}
 #menu .x{display:block;font:inherit;font-weight:700;border:2px solid #111;background:#fff;border-radius:8px;padding:3px 10px;margin:0 0 8px auto;cursor:pointer}
 #planbtn{display:block;position:fixed;left:10px;bottom:12px;z-index:44;font:inherit;font-weight:700;background:var(--t-menu);border:2px solid #111;border-radius:99px;padding:8px 14px;cursor:pointer;box-shadow:0 2px 8px rgba(0,0,0,.25)}
 .glisse{display:block}}
@media(max-width:520px){main{padding:10px}.grille{grid-template-columns:1fr}.sous{font-size:.76rem;line-height:1.3}h1{font-size:1rem}#theme .tx{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}nav.on button{padding:6px 10px}}
"""

JS = r"""
const D=JSON.parse(document.getElementById('donnees').textContent);
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
/* ----- Thèmes : 20 au choix, mémorisés (localStorage sous try/catch), défaut = thème 1 ----- */
const TH=D.themes;
function theme(i,garder){i=(i>=0&&i<TH.length)?i:0;document.documentElement.dataset.theme=i;
  $$('#themes button').forEach(b=>b.setAttribute('aria-pressed',+b.dataset.t===i?'true':'false'));
  $('#theme .pal').innerHTML=TH[i].teintes.map(c=>'<i style="background:'+c+'"></i>').join('');$('#theme').title='Thème '+(i+1)+' · '+TH[i].nom;
  if(garder){try{localStorage.setItem('progression-theme',String(i))}catch(e){}}if(window.EYE_OK)eye();}
$('#themes').innerHTML=TH.map((t,i)=>'<button type="button" data-t="'+i+'" aria-pressed="false"><span class="pal">'+t.teintes.map(c=>'<i style="background:'+c+'"></i>').join('')+'</span>'+(i+1)+' · '+esc(t.nom)+'</button>').join('');
$('#theme').onclick=e=>{e.stopPropagation();$('#themes').classList.toggle('a')};
$('#themes').onclick=e=>{const b=e.target.closest('[data-t]');if(b){theme(+b.dataset.t,true);$('#themes').classList.remove('a')}};
document.addEventListener('click',e=>{if(!e.target.closest('#themes,#theme'))$('#themes').classList.remove('a')});
theme(+document.documentElement.dataset.theme||0);
/* ----- EYE SPOT : une couleur de bande par page active, dérivée de l'identifiant de la page et du thème ----- */
function hsl(h,s,l){const c=(1-Math.abs(2*l-1))*s,x=c*(1-Math.abs((h/60)%2-1)),m=l-c/2;const t=[[c,x,0],[x,c,0],[0,c,x],[0,x,c],[x,0,c],[c,0,x]][Math.floor(h/60)%6];return t.map(v=>Math.floor((v+m)*255+.5));}
const fnv=s=>{let h=2166136261;for(const c of s){h^=c.codePointAt(0);h=Math.imul(h,16777619)>>>0}return h};
let PAGES=['cours'];
/* Teinte projetée sur les arcs écartés d'au moins e.e degrés des teintes de zones du thème (e.z) : même calcul qu'eye_teinte() en Python. */
const ecart=(a,b)=>{const d=Math.abs(a-b)%360;return Math.min(d,360-d)};
function libre(e,h){if(!e.L){e.L=[];for(let d=0;d<360;d++)if(e.z.every(z=>ecart(d,z)>=e.e))e.L.push(d)}return e.L[Math.floor(h*e.L.length/360)]}
function eyeTeinte(cle){const e=TH[+document.documentElement.dataset.theme||0].eye;let k=PAGES.indexOf(cle);
  if(k<0){const p=cle.split('|')[1]||'cours';const hp=eyeTeinte(p);const h=(e.h0+Math.round(137.508*(PAGES.length+fnv(cle.split('|')[0])%997)))%360;
    const m=libre(e,h);return ecart(m,hp)<40?libre(e,(h+180)%360):m}
  return libre(e,(e.h0+Math.round(137.508*k))%360);}
function eyeHex(cle,e){const [s,l]=e.p[cle.split(/[:|]/)[0]]||e.p.cours;return '#'+hsl(eyeTeinte(cle),s,l).map(v=>Math.floor(v*(1-e.a)+255*e.a+.5).toString(16).padStart(2,'0')).join('')}
function eye(){const e=TH[+document.documentElement.dataset.theme||0].eye,cle=pageCle(),x=eyeHex(cle,e);
  document.documentElement.style.setProperty('--eye',x);document.documentElement.dataset.page=cle;document.documentElement.dataset.eye=x;}
function pageBase(){const o=($('nav.on button.a')||{}).dataset.o||'cours';const el=$('#p-'+o);return o==='cours'||!el||el.dataset.i==null?o:o+':'+el.dataset.i}
function pageCle(){const b=pageBase();if($('#fen').classList.contains('a'))return 'fiche:'+$('#fen').dataset.id+'|'+b;
  if($('#vue').classList.contains('a'))return 'vue:'+$('#vue').dataset.i+'|'+b;return b}
/* ----- Hauteur de l'en-tête (bande de menu collée dessous) ----- */
const hauteur=()=>document.documentElement.style.setProperty('--ht',$('header.h').offsetHeight+'px');hauteur();
if(window.ResizeObserver)new ResizeObserver(hauteur).observe($('header.h'));
/* ----- Bande latérale de menu : constante, contextuelle, numérotée, élément visible surligné ----- */
let IO=null;
function menu(titre,items,racine){const m=$('#menu');if(IO){IO.disconnect();IO=null}if(window.EYE_OK)eye();
  m.querySelector('.mt').textContent=titre;
  m.querySelector('ol').innerHTML=items.length?items.map(x=>x.g?'<li class="g">'+esc(x.g)+'</li>':x.id?'<li class="n"><a href="#'+esc(x.id)+'" data-m="'+esc(x.id)+'"'+(x.c?' data-c="'+esc(x.c)+'"':'')+(x.a?' class="a"':'')+'>'+esc(x.t)+'</a></li>':'<li class="n"><span class="v">'+esc(x.t)+'</span></li>').join(''):'<li class="n"><span class="v">—</span></li>';
  const liens=$$('a[data-m]',m).filter(a=>!a.dataset.c);const cibles=liens.map(a=>document.getElementById(a.dataset.m)).filter(Boolean);
  if(!cibles.length||!window.IntersectionObserver)return;
  const vus=new Set();
  IO=new IntersectionObserver(es=>{es.forEach(e=>e.isIntersecting?vus.add(e.target.id):vus.delete(e.target.id));
    const a=liens.find(l=>vus.has(l.dataset.m));if(a){liens.forEach(l=>l.classList.toggle('a',l===a));const r=a.getBoundingClientRect(),mr=m.getBoundingClientRect();if(r.top<mr.top||r.bottom>mr.bottom)a.scrollIntoView({block:'nearest'})}},
    {root:racine||null,rootMargin:racine?'0px 0px -55% 0px':'-'+($('header.h').offsetHeight)+'px 0px -55% 0px'});
  cibles.forEach(c=>IO.observe(c));}
$('#menu').addEventListener('click',e=>{const a=e.target.closest('a[data-m]');if(a&&!a.dataset.c){e.preventDefault();const c=document.getElementById(a.dataset.m);
  if(c){const d=c.closest('details');if(d)d.open=true;c.scrollIntoView({block:'start'})}$('#menu').classList.remove('ouvert')}
  if(e.target.closest('#menu .x'))$('#menu').classList.remove('ouvert');});
$('#planbtn').onclick=()=>$('#menu').classList.add('ouvert');
document.addEventListener('keydown',e=>{if(e.key==='Escape')$('#menu').classList.remove('ouvert')});
const MOD={};
function menuOnglet(){if($('#fen').classList.contains('a')||$('#vue').classList.contains('a'))return;
  const o=($('nav.on button.a')||{}).dataset.o||'cours';
  if(o==='cours'){const it=$$('#p-cours .c').filter(c=>c.style.display!=='none').map(c=>({id:c.id,t:c.querySelector('h2').textContent}));
    return menu('Cours · '+it.length+' situations de départ',it);}
  const m=MOD[o];if(m)menu(m.titre,m.items);}
function onglet(id){$$('nav.on button').forEach(b=>b.classList.toggle('a',b.dataset.o===id));$$('section.p').forEach(s=>s.classList.toggle('a',s.id==='p-'+id));menuOnglet();}
$$('nav.on button').forEach(b=>b.onclick=()=>{onglet(b.dataset.o);history.replaceState(null,'','#'+b.dataset.o)});
/* ----- Cours ----- */
const liste=[];D.ssp.forEach(s=>s.lecons.forEach(l=>{if(l.f)liste.push({s,l})}));
function menuVue(i){const {s}=liste[i];menu('Cours · '+s.nom,s.lecons.map(l=>l.f?{id:'cours-'+l.id,c:l.id,t:l.n,a:l===liste[i].l}:{t:l.n}));}
function ouvrir(i,pousser=true){const {s,l}=liste[i];$('#vue').dataset.i=i;$('#vt').innerHTML=esc(l.n)+'<small>'+esc(s.nom)+'</small>';
  const vieux=$('#vf');const cadre=document.createElement('iframe');cadre.id='vf';cadre.title='Cours';cadre.src=D.base+l.f;vieux.replaceWith(cadre);$('#vn').href=D.base+l.f;$('#vue').classList.add('a');document.body.style.overflow='hidden';
  menuVue(i);if(pousser)history.pushState({c:i},'','#cours='+l.id);}
/* Le cadre est recréé à chaque ouverture et retiré à la fermeture : les ancres suivies dans un cours ne s'empilent pas dans l'historique de la page. */
function fermer(){$('#vue').classList.remove('a');const v=$('#vf');const c=document.createElement('iframe');c.id='vf';c.title='Cours';c.src='about:blank';v.replaceWith(c);document.body.style.overflow='';menuOnglet();}
$('#vr').onclick=()=>{fermer();history.replaceState(null,'','#cours')};
$('#vp').onclick=()=>{const i=+$('#vue').dataset.i;if(i>0)ouvrir(i-1,false),history.replaceState({c:i-1},'','#cours='+liste[i-1].l.id)};
$('#vs').onclick=()=>{const i=+$('#vue').dataset.i;if(i<liste.length-1)ouvrir(i+1,false),history.replaceState({c:i+1},'','#cours='+liste[i+1].l.id)};
addEventListener('popstate',e=>{if(e.state&&e.state.c!=null&&location.hash.startsWith('#cours='))ouvrir(e.state.c,false);else if($('#vue').classList.contains('a'))fermer()});
document.addEventListener('click',e=>{const a=e.target.closest('a[data-c]');if(a){e.preventDefault();$('#menu').classList.remove('ouvert');ouvrir(liste.findIndex(x=>x.l.id===a.dataset.c))}});
function filtrer(){const q=$('#q').value.trim().toLowerCase(),pret=$('#fp').classList.contains('a');
  $$('#p-cours .c').forEach(c=>{const t=c.dataset.t;const ok=(!pret||c.classList.contains('pret'))&&(!q||t.includes(q));c.style.display=ok?'':'none';
    if(q&&ok)c.querySelector('details').open=$$('.ls [data-n]',c).some(x=>x.dataset.n.includes(q))});menuOnglet();}
$('#q').oninput=filtrer;$('#fp').onclick=e=>{e.target.classList.toggle('a');filtrer()};
/* ----- Modules du cahier d'architecture v2 (données : Claude/_progression/donnees) ----- */
const S=D.prog.S,G=D.prog.G,F=D.prog.F,V='—';
const clone=x=>JSON.parse(JSON.stringify(x));
function fi(id){const f=F[id];if(!f)return null;return Object.assign(clone(G[f.type]||{}),f);}
const LBL={nom_exact:'Nom exact',synonymes:'Synonymes',prelevement_conditions:'Prélèvement ou conditions',bon_usage_suisse:'Bon usage suisse (Liste des analyses, Smarter Medicine, dose d\'irradiation OFSP)',
 urgence_aigu:'Urgence, aigu',diagnostic_etiologie:'Diagnostic, étiologie',depistage_pretherapeutique:'Dépistage, pré-thérapeutique',suivi_surveillance:'Suivi, surveillance',ne_pas_demander:'Ne pas demander',
 seuil_alerte:'Seuil d\'alerte',entite_anormale_chiffree:'1 Entité anormale chiffrée',associees_presentes:'2 Associées : présentes',associees_a_rechercher:'2 Associées : à rechercher',
 syndrome_anamnese:'3 Syndrome : anamnèse',syndrome_status:'3 Syndrome : status',confirmation:'4 Confirmation',diagnostic:'4 Diagnostic',conduite:'4 Conduite',si:'Si…',consequence:'→ conséquence pour le patient',alors:'→ alors',
 mnemotechnique:'Mnémotechnique',lignes:'Lignes',trajet:'Trajet de ce qui circule',stations:'Stations',structure:'Structure traversée',structure_fonction:'Structure-fonction locale',si_dereglement:'Si elle se dérègle',
 vite_dit_cafe:'Altérations · VITE DIT : CAFé',nom:'Nom',station:'Station',traitement:'Traitement complet',systeme:'Médicament du système (clic)',hors_systeme:'Hors système (survol : posologie complète)',
 non_medicamenteux:'Non médicamenteux (survol)',classe_biochimique:'Classe biochimique',classe_fonctionnelle:'Classe fonctionnelle',dci:'DCI',marque:'Marque®',cible:'Cible',posologie_complete:'Posologie complète',
 procedure:'Procédure',indications:'Indications',contre_indications:'Contre-indications',classification_fonctionnelle:'Classification fonctionnelle',sous_classe:'Sous-classe',quand_la_choisir:'Quand la choisir',
 chefs_de_file:'Chefs de file suisses',profil:'Profil clinique dominant',chef_de_file:'Chef de file préféré',pourquoi:'Pourquoi (mécanisme, effet recherché)',a_eviter_pourquoi:'À éviter et pourquoi',
 pourquoi_elle:'Pourquoi elle',spectre:'Spectre',pk:'PK · A-D-M-E',absorption:'A Absorption',distribution:'D Distribution',metabolisme:'M Métabolisme',elimination:'E Élimination',courbe_commentee:'Courbe commentée',
 pd:'PD',mecanisme:'Mécanisme',profil_receptoriel:'Profil réceptoriel',effets_indesirables_par_recepteur:'Effets indésirables par récepteur',recepteur:'Récepteur',effet:'Effet',posologie:'Posologie',
 adulte:'Adulte',sujet_age:'Sujet âgé',enfant:'Enfant',adolescent:'Adolescent',sexe:'Sexe',ir_dfg:'IR (par DFG)',ih_child_pugh:'IH (Child-Pugh)',grossesse:'Grossesse',allaitement:'Allaitement',pieges:'Pièges « si → alors »',
 source:'Source',sources:'Sources',delai_titration:'Délai d\'action et titration',delai_action:'Délai d\'action',titration:'Titration',performance_par_profil:'Performance par profil clinique (matrice 4.4)',
 arret_sevrage_switch:'Arrêt, sevrage et changement',schema_arret:'Schéma d\'arrêt',syndrome_arret:'Syndrome d\'arrêt',switch:'Changement (switch)',surveillance:'Surveillance',biologie:'Biologie',ecg_qt:'ECG (QT)',
 poids_metabolique:'Poids et métabolique',taux_plasmatique:'Taux plasmatique',posologie_par_age:'Posologie par âge',autorisation_suisse_par_age:'Autorisation suisse par âge',
 criteres_cim10:'Critères CIM-10 (survol)',criteres_principaux:'Critères principaux',criteres_associes:'Critères associés',nombre_requis:'Nombre requis',duree:'Durée',specifications:'Spécifications',severite:'Sévérité',
 syndrome_somatique:'Syndrome somatique',symptomes_psychotiques:'Symptômes psychotiques',exclusions:'Exclusions',termes_discriminants:'Termes discriminants (gras)',texte_source:'Texte source',complement_recherche:'Complément : critères pour la recherche (signalé)',
 barre_traitement:'Barre de traitement',psychotherapies_mesures:'Psychothérapies et mesures (survol)',type:'Type',indication:'Indication',pharmacologie_psychiatrique:'Pharmacologie psychiatrique (clic)',
 hors_psychiatrie:'Hors psychiatrie (survol : posologie complète)',mesures_legales_sociales:'Mesures légales ou sociales (survol)',ages:'Vue par âge',presente:'Se présente à cet âge',ce_que_lage_change:'Ce que l\'âge change',
 pathologies:'Pathologies',rubriques:'Rubriques',cadre_ensemble:'Cadre d\'ensemble',entites:'Entités',liens_logiques:'Liens logiques',ponts_cliniques:'Ponts cliniques',classes:'Classes',bandes:'Bandes par sous-classe',
 matrice_profil_chef_de_file:'Matrice profil clinique → chef de file',coque:'Coque',justification_coque:'Justification (une ligne)',nombre_stations:'Nombre de stations',normal:'Normal'};
const COUL={normal:'bleu',trajet:'bleu',stations:'bleu',structure_fonction:'bleu',temps2_examen:'bleu',pathologies:'rouge',vite_dit_cafe:'rouge',si_dereglement:'rouge',anomalie:'rouge',criteres_cim10:'rouge',
 systeme:'vert',classes:'vert',bandes:'vert',pharmacologie_psychiatrique:'vert',hors_systeme:'violet',hors_psychiatrie:'violet',non_medicamenteux:'ocre',psychotherapies_mesures:'ocre',mesures_legales_sociales:'ocre',
 ne_pas_demander:'orange',seuil_alerte:'orange',annexeA_pieges:'orange',pieges:'orange'};
const lbl=k=>LBL[k]||(k.charAt(0).toUpperCase()+k.slice(1)).replace(/_/g,' ');
/* Glossaire (Claude/_progression/glossaire.json) : chaque sigle devient un survol <abbr title> accessible au clavier et au toucher
   (tabindex) ; chaque score (clé ou alias) devient un bouton qui ouvre sa cotation détaillée et son interprétation. Un seul passage
   d'expression régulière, du nom le plus long au plus court, sur le texte déjà échappé : aucune bulle n'est enveloppée deux fois. */
const GL=D.glo||{abreviations:{},scores:{}},GA=GL.abreviations||{},GS=GL.scores||{},GN={};
Object.entries(GS).forEach(([k,v])=>[k].concat(v.alias||[]).forEach(n=>GN[n]=k));
const GNOMS=Object.keys(GA).concat(Object.keys(GN)).filter((x,i,a)=>a.indexOf(x)===i).sort((a,b)=>b.length-a.length);
const GRX=GNOMS.length?new RegExp('(?<![0-9A-Za-zÀ-ÖØ-öø-ÿ_])('+GNOMS.map(x=>esc(x).replace(/[.*+?^${}()|[\]\\]/g,'\\$&')).join('|')+')(?![0-9A-Za-zÀ-ÖØ-öø-ÿ_])','g'):null;
const GDE={};GNOMS.forEach(n=>GDE[esc(n)]=n);
/* Bulle du sigle au clavier et au toucher : un seul élément fixe, placé sous le sigle et gardé dans l'écran (un tableau qui défile ne la coupe pas). */
function bulle(a){const b=$('#bulle');if(!a){b.classList.remove('a');return}b.textContent=a.getAttribute('title');b.classList.add('a');
  const r=a.getBoundingClientRect(),w=b.offsetWidth,h=b.offsetHeight;let x=Math.min(Math.max(12,r.left),innerWidth-w-12),y=r.bottom+6;if(y+h>innerHeight-8)y=Math.max(8,r.top-h-6);
  b.style.left=x+'px';b.style.top=y+'px';}
document.addEventListener('focusin',e=>{const a=e.target.closest&&e.target.closest('abbr[title]');bulle(a||null)});
document.addEventListener('focusout',e=>{if(e.target.matches&&e.target.matches('abbr[title]'))bulle(null)});
addEventListener('scroll',()=>{const a=document.activeElement;if($('#bulle').classList.contains('a'))bulle(a&&a.matches&&a.matches('abbr[title]')?a:null)},true);
function gl(x){const h=esc(x);if(!GRX)return h;return h.replace(GRX,m=>{const n=GDE[m]||m;
  if(GN[n])return '<button type="button" class="sc" data-sc="'+esc(GN[n])+'" aria-haspopup="dialog" title="'+esc('Score : cotation et interprétation')+'">'+m+'</button>';
  return '<abbr tabindex="0" title="'+esc(GA[n])+'">'+m+'</abbr>';});}
const lienF=id=>F[id]?'<button type="button" class="lien" data-f="'+esc(id)+'">'+esc(fi(id).titre)+'<small>'+esc(id)+'</small></button>':esc(id);
const vide=x=>x==null||x===V||(Array.isArray(x)?x.every(vide):typeof x==='object'?Object.values(x).every(vide):false);
function val(v,k,t2){
  if(v==null)return esc(V);
  if(typeof v==='string'||typeof v==='number')return F[v]?lienF(v):gl(v);
  if(Array.isArray(v)){if(!v.length)return esc(V);
    if(typeof v[0]!=='object')return v.length===1?val(v[0]):'<ul>'+v.map(x=>'<li>'+val(x)+'</li>').join('')+'</ul>';
    const ks=Object.keys(v[0]).filter(x=>x!=='vite_dit_cafe'&&x!=='traitement');
    let h='<div class="tw"><table><tr>'+ks.map(x=>'<th class="'+(COUL[x]?'c-'+COUL[x]:'')+'">'+esc(t2&&t2[x]||lbl(x))+'</th>').join('')+'</tr>'+v.map(r=>'<tr>'+ks.map(x=>'<td>'+val(r[x],x)+'</td>').join('')+'</tr>').join('')+'</table></div>';
    v.forEach((r,i)=>{if(r.vite_dit_cafe)h+='<h5 class="k-rouge">Station '+esc(r.n||i+1)+' · '+lbl('vite_dit_cafe')+'</h5>'+val(r.vite_dit_cafe);
      if(r.traitement)h+='<h5 class="k-vert">'+lbl('traitement')+' : '+esc(r.nom)+'</h5>'+val(r.traitement);});
    return h;}
  return '<table>'+Object.entries(v).map(([a,b])=>'<tr><td class="l '+(COUL[a]?'c-'+COUL[a]:'')+'">'+esc(lbl(a))+'</td><td>'+val(b,a)+'</td></tr>').join('')+'</table>';}
/* Bloc optionnel « Calculs » (après le Temps 2) : chaque paramètre calculé montre sa formule en chasse fixe, son usage pratique,
   un exemple résolu pas à pas et sa source ; le titre de chaque calcul suit la bande EYE SPOT (#fen h5). */
function calculs(l){const r=(Array.isArray(l)?l:[]).filter(x=>x&&!vide(x));if(!r.length)return '<p class="vide">—</p>';
  return r.map(x=>'<div class="calc"><h5>'+esc(x.nom||V)+'</h5><pre class="fx"><code>'+gl(x.formule||V)+'</code></pre>'
    +'<p><b>À quoi ça sert :</b> '+gl(x.a_quoi_ca_sert||V)+'</p><p><b>Exemple résolu :</b></p><pre class="ex">'+gl(x.exemple||V)+'</pre>'
    +'<p class="src">Source : '+gl(x.source||V)+'</p></div>').join('');}
const BLOCS={examen:[['entete','En-tête'],['temps1_indications','Temps 1 · Indications'],['temps2_examen','Temps 2 · L\'examen — un paramètre lu seul'],
  ['calculs','Calculs · formule, usage, exemple résolu'],
  ['temps3_interpretation','Temps 3 · Interprétation — plusieurs anomalies associées'],['annexeA_pieges','Annexe A · Pièges'],['sources','Sources']]};
const COURT={entete:'En-tête',temps1_indications:'Temps 1 · Indications',temps2_examen:'Temps 2 · L\'examen',calculs:'Calculs',temps3_interpretation:'Temps 3 · Interprétation',annexeA_pieges:'Pièges'};
const META=['id','module','type','titre','sous_onglet','systeme','etiquettes','entree_primaire','axe_secondaire','passerelles','classe','sous_classe','bloc','code_cim10'];
function rendreFiche(id){const f=fi(id);if(!f)return {h:'<p class="vide">Identifiant absent : '+esc(id)+'</p>',s:[]};
  const so=f.sous_onglet?S.examens[f.sous_onglet-1]:null,s=[];
  let h='<p class="meta"><b>'+esc(f.id)+'</b> · '+esc(f.systeme)+' '+esc((S.systemes.find(x=>x.code===f.systeme)||{}).nom||'')+(f.etiquettes&&f.etiquettes.length?' · étiquettes '+f.etiquettes.map(e=>'<span class="etq">'+esc(e)+'</span>').join(''):'')+'</p>';
  if(so)h+='<p class="meta">Sous-onglet '+so.n+' · '+esc(so.titre)+' · '+esc(so.entree_primaire)+' : <b>'+esc(f.entree_primaire.join(', '))+'</b> · '+esc(so.axe_secondaire)+' : <b>'+esc(f.axe_secondaire.join(', '))+'</b></p>';
  if(f.classe)h+='<p class="meta">Classe : '+lienF(f.classe)+' · sous-classe <b>'+esc(f.sous_classe)+'</b></p>';
  if(f.bloc)h+='<p class="meta">Bloc CIM-10 : '+lienF(f.bloc)+'</p>';
  const ordre=BLOCS[f.type]||Object.keys(f).filter(k=>!META.includes(k)).map(k=>[k,lbl(k)]);
  for(const [k,t] of ordre){if(!(k in f))continue;const c=COUL[k],ancre='fb-'+s.length;s.push({id:ancre,t:COURT[k]||t});
    const t2=k==='temps2_examen'&&so?{parametre:so.temps2[0],normal:so.temps2[1],anomalie:so.temps2[2]}:null;
    h+='<h4 id="'+ancre+'" class="'+(c?'k-'+c:'')+'">'+esc(t)+'</h4>'+(k==='calculs'?calculs(f[k]):val(f[k],k,t2));}
  s.push({id:'fb-p',t:'Passerelles'});
  h+='<h4 id="fb-p">Annexe B · Passerelles</h4>'+(f.passerelles.length?'<div class="tw"><table><tr><th>Type</th><th>Fiche cible</th><th>Pourquoi</th></tr>'+f.passerelles.map(p=>'<tr><td>'+esc(p.type)+'</td><td>'+lienF(p.cible)+'</td><td>'+gl(p.pourquoi)+'</td></tr>').join('')+'</table></div>':'<p class="vide">—</p>');
  return {h,s};}
/* Une seule fenêtre ouverte : ouvrir une fiche remplace la précédente ; la bande de menu montre alors le plan de la fiche. */
function ouvrirF(id){const f=fi(id);if(!f)return;$('#fen').dataset.id=id;const r=rendreFiche(id);$('#fen .ft h3').textContent=f.titre;$('#fen .fb').innerHTML=r.h;$('#fen').classList.add('a');$('#fen').scrollTop=0;
  document.body.style.overflow='hidden';history.replaceState(null,'','#f='+encodeURIComponent(id));$('#menu').classList.remove('ouvert');
  menu('Fiche · '+f.titre,r.s,$('#fen'));$('#fen .x').focus();}
function fermerF(){$('#fen').classList.remove('a');document.body.style.overflow='';const o=$('nav.on button.a');history.replaceState(null,'','#'+(o?o.dataset.o:''));menuOnglet();}
/* Fenêtre de score : posée au-dessus de la fiche, fermée par ✕, Échap ou clic hors du cadre ; le focus revient au bouton du score. */
let SCO_RET=null;
function ouvrirS(k){const s=GS[k];if(!s)return;SCO_RET=document.activeElement;
  $('#sco h3').textContent=k;
  $('#sco .fb').innerHTML='<p>'+esc(s.definition)+'</p><h4>Cotation détaillée</h4><div class="tw"><table><tr><th>Item</th><th>Points</th></tr>'
    +(s.cotation||[]).map(c=>'<tr><td>'+esc(c.item)+'</td><td class="pt">'+esc(c.points)+'</td></tr>').join('')+'</table></div>'
    +'<h4>Interprétation</h4><div class="tw"><table><tr><th>Plage</th><th>Sens</th></tr>'+(s.interpretation||[]).map(c=>'<tr><td class="pt">'+esc(c.plage)+'</td><td>'+esc(c.sens)+'</td></tr>').join('')+'</table></div>'
    +'<p class="src">Source : '+esc(s.source)+'</p>';
  $('#sco').classList.add('a');$('#sco').scrollTop=0;$('#sco .x').focus();}
function fermerS(){$('#sco').classList.remove('a');if(SCO_RET&&SCO_RET.focus)SCO_RET.focus();SCO_RET=null;}
$('#sco').onclick=e=>{if(e.target.id==='sco'||e.target.closest('#sco .x'))fermerS()};
document.addEventListener('click',e=>{const b=e.target.closest('button.sc[data-sc]');if(b){e.preventDefault();e.stopPropagation();ouvrirS(b.dataset.sc)}},true);
$('#fen').onclick=e=>{if(e.target.id==='fen'||e.target.closest('#fen .x'))fermerF()};
addEventListener('keydown',e=>{if(e.key!=='Escape')return;if($('#sco').classList.contains('a'))fermerS();else if($('#fen').classList.contains('a'))fermerF()});
document.addEventListener('click',e=>{const b=e.target.closest('[data-f]');if(b){e.preventDefault();ouvrirF(b.dataset.f)}});
const btnF=(id,ancre)=>{const f=fi(id);return '<li'+(ancre?' id="'+esc(ancre)+'"':'')+'><button type="button" data-f="'+esc(id)+'">'+esc(f.titre)+(f.etiquettes&&f.etiquettes.length?f.etiquettes.map(e=>'<span class="etq">'+esc(e)+'</span>').join(''):'')+'<small>'+esc(id)+'</small></button></li>'};
const listeF=(ids,pre)=>ids.length?'<ul class="lf">'+ids.map(id=>btnF(id,pre?pre+id:'')).join('')+'</ul>':'<p class="vide">—</p>';
const LEG='<div class="legende"><span class="c-bleu">bleu normal</span><span class="c-rouge">rouge pathologie</span><span class="c-vert">vert traitement du système</span><span class="c-violet">violet hors système</span><span class="c-ocre">ocre non médicamenteux</span><span class="c-orange">orange danger</span></div>';
/* Gabarit commun : rail (racine) → colonne ; le plan numéroté de la colonne va dans la bande latérale. */
function module(sel,nom,rail,corps){const el=$(sel),o=sel.slice(3);
  el.innerHTML='<div class="mod"><nav class="rail" aria-label="Rail">'+rail.map((r,i)=>'<button type="button" data-r="'+i+'"><b>'+esc(r.n)+'</b><span>'+esc(r.t)+'</span></button>').join('')+'</nav><div class="col"></div></div>';
  const montrer=(i,opt)=>{$$('.rail button',el).forEach(b=>b.classList.toggle('a',+b.dataset.r===i));const r=corps(i,opt||{});$('.col',el).innerHTML=r.h;
    MOD[o]={titre:nom+' · '+rail[i].n+' '+rail[i].t,items:r.s.map(x=>Array.isArray(x)?{id:x[0],t:x[1]}:x)};el.dataset.i=i;
    if(el.classList.contains('a'))menuOnglet();};
  el.addEventListener('click',e=>{const r=e.target.closest('.rail button');if(r){montrer(+r.dataset.r);return el.scrollIntoView({block:'start'})}
    const v=e.target.closest('[data-vue]');if(v)return montrer(+el.dataset.i,{vue:v.dataset.vue});});
  montrer(0);return montrer;}
/* Examens paracliniques : 9 sous-onglets, entrée primaire puis axe secondaire. */
function corpsEx(i,o){const so=S.examens[i];const parSys=so.entree_primaire.startsWith('Système');const vue=o.vue||'prim';
  const toutes=so.systemes.flatMap(s=>s.fiches);
  let entrees;
  if(parSys||vue==='sys')entrees=so.systemes.map(s=>({k:s.code,t:s.code+' · '+s.nom,ids:s.fiches}));
  else{entrees=so.valeurs_primaires.map(v=>({k:v,t:v,ids:toutes.filter(id=>fi(id).entree_primaire.includes(v))}));
    entrees.push({k:'na',t:'— (à attribuer)',ids:toutes.filter(id=>fi(id).entree_primaire.includes(V))});}
  let h='<h2>'+so.n+' · '+esc(so.titre)+'</h2><p class="meta">Entrée primaire : <b>'+esc(so.entree_primaire)+'</b> · axe secondaire : <b>'+esc(so.axe_secondaire)+'</b> ('+esc(so.valeurs_axe.join(', '))+') · unité de fiche : '+esc(so.unite)+' · '+toutes.length+' emplacements</p>';
  if(!parSys)h+='<div class="bas"><button type="button" class="pu'+(vue!=='sys'?' a':'')+'" data-vue="prim">Par '+esc(so.entree_primaire.toLowerCase())+'</button><button type="button" class="pu'+(vue==='sys'?' a':'')+'" data-vue="sys">Par système</button></div>';
  h+=LEG;
  entrees.forEach((en,j)=>{const id='ex'+so.n+'-'+j;h+='<h3 id="'+id+'"><span class="num">'+(j+1)+'</span>'+esc(en.t)+'</h3>';
    if(!en.ids.length){h+='<p class="vide">—</p>';return}
    const axes=[...so.valeurs_axe,V];axes.forEach(a=>{const ids=en.ids.filter(x=>fi(x).axe_secondaire.includes(a));if(ids.length)h+='<h4>'+esc(so.axe_secondaire)+' : '+esc(a===V?'— (à attribuer)':a)+'</h4>'+listeF(ids)});});
  return {h,s:entrees.map((en,j)=>['ex'+so.n+'-'+j,en.t])};}
/* Pharmacologie : chaîne SUR UNE LIGNE par station — Normal → Altération (VITE DIT : CAFé) → Pathologie → Traitement. */
const pleine=x=>x&&x!==V;
function bandeT(t){const B=[];
  (t.systeme||[]).forEach(m=>{if(vide(m))return;const txt=(pleine(m.classe_biochimique)?m.classe_biochimique:'')+(pleine(m.classe_fonctionnelle)?' ('+m.classe_fonctionnelle+')':'')+(pleine(m.dci)?' : '+m.dci:'')+(pleine(m.marque)?' ('+m.marque+'®)':'');
    const cible=[m.dci,m.molecule].find(x=>F[x]);B.push(cible?'<button type="button" class="k-vert" data-f="'+esc(cible)+'">'+esc(txt)+'</button>':'<span class="k-vert" title="'+esc(pleine(m.cible)?'Cible : '+m.cible:'')+'">'+esc(txt)+'</span>');});
  (t.hors_systeme||[]).forEach(m=>{if(!vide(m))B.push('<span class="k-violet" title="'+esc('Posologie complète : '+m.posologie_complete)+'">'+esc(m.dci)+'</span>')});
  (t.non_medicamenteux||[]).forEach(m=>{if(!vide(m))B.push('<span class="k-ocre" title="'+esc('Indications : '+m.indications+' · Contre-indications : '+m.contre_indications)+'">'+esc(m.procedure)+'</span>')});
  return B.length?'<div class="barre-t">'+B.join('')+'</div>':'<span class="vide">—</span>';}
function alteration(v){const e=Object.entries(v||{}),pl=e.filter(([,x])=>pleine(x)),vd=e.filter(([,x])=>!pleine(x));
  return (pl.length?'<ul class="vdc">'+pl.map(([k,x])=>'<li><b>'+esc(k.split(' ')[0])+'</b>'+esc(k.split(' ').slice(1).join(' '))+' : '+esc(x)+'</li>').join('')+'</ul>':'')+
   (vd.length?'<details><summary>'+(pl.length?'+ ':'')+vd.length+' rubrique'+(vd.length>1?'s':'')+' « — »</summary>'+vd.map(([k])=>'<span>'+esc(k)+'</span>').join('')+'</details>':'');}
function chaineLigne(cid,s){const c=fi(cid),st=c.normal.stations,pa=c.pathologies;
  const rang=x=>st.findIndex(t=>String(t.n)===String(x)||(pleine(t.structure)&&t.structure===x));
  const par=st.map(()=>[]),hors=[];pa.forEach(p=>{const r=rang(p.station);(r>=0?par[r]:!pleine(p.nom)&&st.length?par[0]:hors).push(p)});
  const lignes=st.map((t,i)=>({t,ps:par[i].length?par[i]:[{nom:V,traitement:{}}]}));if(hors.length)lignes.push({t:{n:'?',structure:'Station non attribuée'},ps:hors});
  let h='<div class="ch" role="table" aria-label="Chaîne pharmacologique"><div class="eh" style="--pt:var(--bleu)">Normal · station</div><div class="eh fl"></div><div class="eh" style="--pt:var(--rouge)">Altération · VITE DIT : CAFé</div><div class="eh fl"></div><div class="eh" style="--pt:var(--rouge)">Pathologie</div><div class="eh fl"></div><div class="eh" style="--pt:var(--vert)">Traitement</div>',r=2;
  lignes.forEach(({t,ps},i)=>{const k=ps.length,ancre='st-'+cid+'-'+i,sp='grid-row:'+r+' / span '+k;s.push({id:ancre,t:'Station '+t.n+' · '+t.structure});
    h+='<div class="st k-bleu" id="'+ancre+'" style="'+sp+';grid-column:1"><span class="sn">'+esc(t.n)+'</span><b>'+esc(t.structure)+'</b>'+(pleine(t.structure_fonction)?'<p>'+esc(t.structure_fonction)+'</p>':'')+(pleine(t.si_dereglement)?'<p class="si">Si dérèglement : '+esc(t.si_dereglement)+'</p>':'')+'</div>'+
      '<div class="fl" style="'+sp+';grid-column:2">→</div><div class="k-rouge" style="'+sp+';grid-column:3">'+(t.vite_dit_cafe?alteration(t.vite_dit_cafe):'—')+'</div><div class="fl" style="'+sp+';grid-column:4">→</div>';
    ps.forEach((p,j)=>{h+='<div class="k-rouge" style="grid-row:'+(r+j)+';grid-column:5">'+(F[p.fiche]?lienF(p.fiche):esc(p.nom))+'</div><div class="fl" style="grid-row:'+(r+j)+';grid-column:6">→</div><div style="grid-row:'+(r+j)+';grid-column:7">'+bandeT(p.traitement||{})+'</div>'});
    r+=k;});
  return '<p class="glisse">⇆ La ligne défile dans son cadre : Normal → Altération → Pathologie → Traitement.</p><div class="defile">'+h+'</div></div>';}
function ligneP(id){const f=fi(id),b=f.barre_traitement;const surv=(x,k)=>esc(lbl(k))+' : '+(Array.isArray(x)?x.map(r=>typeof r==='object'?Object.values(r).join(' · '):r).join(' ; '):x);
  return '<div class="lpd"><div class="lp"><button type="button" class="lien k-rouge" data-f="'+esc(id)+'" title="'+esc(surv(f.criteres_cim10.criteres_principaux,'criteres_principaux'))+'">'+esc(f.titre)+'</button><span class="fl">→</span><div class="barre-t">'+
   '<span class="k-ocre" title="'+esc(surv(b.psychotherapies_mesures,'psychotherapies_mesures'))+'">Psychothérapies et mesures (survol)</span>'+
   b.pharmacologie_psychiatrique.map(c=>F[c]?'<button type="button" class="k-vert" data-f="'+esc(c)+'">'+esc(fi(c).titre)+'</button>':'<span class="k-vert">'+esc(c)+'</span>').join('')+
   '<span class="k-violet" title="'+esc(surv(b.hors_psychiatrie,'hors_psychiatrie'))+'">Hors psychiatrie (survol)</span><span class="k-ocre" title="'+esc(surv(b.mesures_legales_sociales,'mesures_legales_sociales'))+'">Mesures légales ou sociales (survol)</span></div></div></div>';}
function classeHtml(id){const c=fi(id);return '<div class="bande k-vert" id="cl-'+esc(id)+'"><button type="button" data-f="'+esc(id)+'">'+esc(c.titre)+' <small class="etq">'+esc(id)+'</small></button>'+
  c.bandes.map(b=>'<div class="meta">'+esc(b.sous_classe)+' : '+b.chefs_de_file.map(x=>F[x]?lienF(x):esc(x)).join(' ')+'</div>').join('')+'</div>';}
const molecules=code=>Object.keys(F).filter(id=>F[id].systeme===code&&/^molecule/.test(F[id].type)&&F[id].module==='pharmaco').sort();
function classesMol(sy,s,n){const mol=molecules(sy.code);let h='';
  s.push({g:'Classes'});if(sy.classes.length)sy.classes.forEach(id=>s.push({id:'cl-'+id,t:fi(id).titre}));else s.push({t:'—'});
  h+='<h3 id="ph-cl"><span class="num">'+n+'</span>Classes</h3>'+(sy.classes.length?sy.classes.map(classeHtml).join(''):'<p class="vide">—</p>');
  s.push({g:'Molécules'});if(mol.length)mol.forEach(id=>s.push({id:'mo-'+id,t:fi(id).titre}));else s.push({t:'—'});
  h+='<h3 id="ph-mo"><span class="num">'+(n+1)+'</span>Molécules</h3>'+listeF(mol,'mo-');return h;}
function corpsPh(i,o){const sy=S.pharmaco[i];let h='<h2>'+esc(sy.code)+' · '+esc(sy.nom)+'</h2><p class="meta">Coque : <b>'+esc(sy.coque)+'</b></p>'+LEG,s=[];
  if(sy.code==='S11'){const P=S.psychiatrie,vue=o.vue||'cim';
    h+='<div class="bas"><button type="button" class="pu'+(vue==='cim'?' a':'')+'" data-vue="cim">Vue CIM-10</button><button type="button" class="pu'+(vue==='age'?' a':'')+'" data-vue="age">Vue par âge</button></div>';
    s.push({g:vue==='cim'?'Blocs CIM-10 · pathologie → traitement':'Âges · pathologie → traitement'});
    if(vue==='cim')P.blocs.forEach((b,j)=>{const id='ps-'+j;s.push({id,t:b.code+' · '+b.titre});
      h+='<h3 id="'+id+'"><span class="num">'+(j+1)+'</span><button type="button" class="lien" data-f="'+esc(b.id)+'">'+esc(b.code)+' · '+esc(b.titre)+'</button></h3>'+(b.pathologies.length?b.pathologies.map(ligneP).join(''):'<p class="vide">— (liste des pathologies à arrêter)</p>');});
    else S.ages.forEach((a,j)=>{const id='age-'+j;s.push({id,t:a});h+='<h3 id="'+id+'"><span class="num">'+(j+1)+'</span>'+esc(a)+'</h3>'+
      (P.ages[a].length?P.ages[a].map(p=>ligneP(p)+'<p class="meta">Ce que l\'âge change : '+esc(fi(p).ages[a].ce_que_lage_change)+'</p>').join(''):'<p class="vide">—</p>');});
    h+=classesMol(sy,s,s.filter(x=>x.id).length+1);
  }else{s.push({g:'Chaîne · stations'});
    h+='<h3 id="ph-ch"><span class="num">1</span>Chaîne : Normal → Altération → Pathologie → Traitement</h3>'+'<p class="meta">'+sy.chaines.map(c=>'Fiche complète : '+lienF(c)).join(' · ')+'</p>'+sy.chaines.map(c=>chaineLigne(c,s)).join('');
    h+=classesMol(sy,s,2);}
  return {h,s};}
/* Sciences fondamentales : par système, gabarit cadre → entités → liens → ponts cliniques. */
function corpsSF(i){const sy=S.fondamentales[i];return {h:'<h2>'+esc(sy.code)+' · '+esc(sy.nom)+'</h2><p class="meta">Gabarit : cadre d\'ensemble → entités → liens logiques → ponts cliniques</p>'+
  sy.fiches.map((id,j)=>'<h3 id="sf-'+j+'"><span class="num">'+(j+1)+'</span>'+esc(fi(id).titre)+'</h3>'+listeF([id])).join(''),s:sy.fiches.map((id,j)=>['sf-'+j,fi(id).titre])};}
/* Rangs EYE SPOT entrelacés (cours, puis examens:i, pharmaco:i, fondamentales:i) : pas d'angle d'or de 137,5° ; voisins de rail
   et premières pages des onglets écartés d'au moins 52° de teinte. */
if(S){const MS=['examens','pharmaco','fondamentales'];for(let i=0;i<Math.max(...MS.map(m=>S[m].length));i++)MS.forEach(m=>{if(i<S[m].length)PAGES.push(m+':'+i)});
  window.EYE_OK=1;module('#p-examens','Examens',S.examens.map(x=>({n:x.n,t:x.titre})),corpsEx);
  module('#p-pharmaco','Pharmacologie',S.pharmaco.map(x=>({n:x.code,t:x.nom})),corpsPh);
  module('#p-fondamentales','Sciences fondamentales',S.fondamentales.map(x=>({n:x.code,t:x.nom})),corpsSF);}
else $$('#p-examens,#p-pharmaco,#p-fondamentales').forEach(x=>x.innerHTML='<p class="vide">Charpente absente : lancer Claude/_progression/charpente.py.</p>');
filtrer();
/* ----- Lien profond ----- */
const h=location.hash.slice(1);if(h.startsWith('cours=')){const i=liste.findIndex(x=>x.l.id===h.slice(6));if(i>=0){history.replaceState(null,'','#cours');ouvrir(i)}}
else if(h.startsWith('f=')&&F[decodeURIComponent(h.slice(2))]){const id=decodeURIComponent(h.slice(2));onglet({examens:'examens',pharmaco:'pharmaco',psychiatrie:'pharmaco',fondamentales:'fondamentales'}[F[id].module]);ouvrirF(id)}
else if(['examens','pharmaco','fondamentales'].includes(h))onglet(h);
window.EYE_OK=1;eye();
"""


def rendre(a):
    C = json.load(open(a.carte, encoding='utf-8')) if a.carte and os.path.exists(a.carte) else {'lecons': {}}
    L = C.get('lecons', {})
    cat = {int(r['lot']): (r['code'], r['ssp_profiles_2023_fr_en'].split('|')[0].strip()) for r in csv.DictReader(open(a.catalogue, encoding='utf-8'))}
    prets = plage(a.audites)
    ssp, cartes, n_cours = [], [], 0
    for lot in range(1, 249):
        code, nom = cat.get(lot, ('', f'SSP {lot}'))
        noms, graves = noms_dx(lot)
        rows = [L.get(f'{lot:03d}:{l}') for l in LECONS]
        if lot in prets:
            p = 100
        elif L:
            p = min(95, round(sum(r['score'] if r else 0 for r in rows) / 11))
        else:  # sans carte : part des onze fichiers déjà présents, plafonnée (rien n'est audité)
            p = round(40 * sum(os.path.exists(fichier(lot, l)) for l in LECONS) / 11)
        lecons, items = [], []
        for l in LECONS:
            n = 'Vue d\'ensemble : démarche devant ce motif, dix diagnostics comparés' if l == 'A' else noms.get(l, f'Diagnostic {l[2:]} (nom à venir)')
            f = fichier(lot, l)
            ok = lot in prets and os.path.exists(f)
            n_cours += ok
            lecons.append({'id': f'{code}-{l}'.replace('.', '_'), 'n': n if l != 'A' else f'{nom} — vue d\'ensemble', 'f': f if ok else None})
            drap = '<b class="g" aria-label="diagnostic grave">🚩</b>' if graves.get(l) else ''
            cls = ' class="mono"' if l == 'A' else ''
            items.append(f'<li>{"<a href=\"" + E(a.base + f) + "\" data-c=\"" + E(lecons[-1]["id"]) + "\" data-n=\"" + E(n.lower()) + "\">" if ok else "<span data-n=\"" + E(n.lower()) + "\">"}{drap}<span{cls}>{E(n)}</span>{"</a>" if ok else "</span>"}</li>')
        ssp.append({'code': code, 'nom': nom, 'lecons': lecons})
        recherche = E((nom + ' ' + code + ' ' + ' '.join(noms.values())).lower())
        cartes.append(
            f'<article id="ssp-{lot}" class="c{" pret" if lot in prets else ""}" data-t="{recherche}"><div class="code">{E(code)}{" · prêt" if lot in prets else ""}</div><h2>{E(nom)}</h2>'
            f'<div class="j"><div class="t"><div class="f" style="--p:{p}%;--h:{round(1.2 * p)}"></div></div><span>{p} %</span></div>'
            f'<details{" open" if lot in prets and len(prets) <= 3 else ""}><summary>{"Ouvrir les cours" if lot in prets else "Diagnostics prévus"}</summary><ul class="ls">{"".join(items)}</ul></details></article>')
    prog = progression(a.donnees)
    rangs, MS = {'cours': 0}, ('examens', 'pharmaco', 'fondamentales')  # rangs EYE SPOT des pages d'entrée, dans l'ordre de PAGES du JS
    for m in MS:
        if (prog.get('S') or {}).get(m):
            rangs[m + ':0'] = len(rangs)
    th, css_th = themes(a.themes, rangs)
    glo = json.load(open(a.glossaire, encoding='utf-8')) if os.path.exists(a.glossaire) else {}
    donnees = {'base': a.base, 'ssp': ssp, 'prog': prog, 'themes': th,
               'glo': {k: glo.get(k, {}) for k in ('abreviations', 'scores')}}
    n_empl = len(donnees['prog']['F'])
    maj = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=1))).strftime('%d.%m.%Y %H:%M')
    doc = f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Progression — Examen fédéral de médecine humaine</title><script>(function(){{var t=0;try{{t=parseInt(localStorage.getItem('progression-theme'),10)||0}}catch(e){{}}if(!(t>=0&&t<{len(th)}))t=0;var r=document.documentElement,h=location.hash.slice(1);r.dataset.theme=t;r.dataset.page={json.dumps([c for c in rangs if c != 'cours'])}.indexOf(h+':0')>=0?h+':0':'cours'}})()</script>
<style>{POLICE.replace('BASE', a.base)}{css_th}{CSS}</style></head><body>
<header class="h"><h1>Progression — Examen fédéral</h1><p class="sous">{len(prets)} situations de départ prêtes · {n_cours} cours ouvrables · {n_empl} emplacements de fiches · mise à jour {maj} (Zurich)</p>
<div class="hl" style="position:relative"><nav class="on"><button data-o="cours" class="a">Cours</button><button data-o="examens">Examens paracliniques</button><button data-o="pharmaco">Pharmacologie</button><button data-o="fondamentales">Sciences fondamentales</button></nav>
<button id="theme" type="button" aria-haspopup="true" aria-controls="themes"><span class="pal"></span><span class="tx">Thème</span></button><div id="themes" role="menu" aria-label="Thèmes"></div></div></header>
<div class="cadre"><aside id="menu" aria-label="Plan de la page"><button type="button" class="x" aria-label="Fermer le plan">✕</button><p class="mt"></p><ol></ol></aside>
<main>
<section class="p a" id="p-cours">
<div class="barre"><input id="q" type="search" placeholder="Chercher un motif ou un diagnostic…" aria-label="Chercher"><button class="pu a" id="fp" type="button">Prêts seulement</button></div>
<div class="grille">{"".join(cartes)}</div></section>
<section class="p" id="p-examens"></section>
<section class="p" id="p-pharmaco"></section>
<section class="p" id="p-fondamentales"></section>
</main></div>
<button id="planbtn" type="button" aria-controls="menu">☰ Plan</button>
<div id="vue" role="dialog" aria-label="Cours"><div class="tete"><button id="vr" type="button" aria-label="Retour à la liste">←</button><b id="vt"></b><button id="vp" type="button" aria-label="Cours précédent">‹</button><button id="vs" type="button" aria-label="Cours suivant">›</button><a class="x" id="vn" target="_blank" rel="noopener" aria-label="Ouvrir dans un nouvel onglet">↗</a></div><iframe id="vf" title="Cours" src="about:blank"></iframe></div>
<div id="fen" role="dialog" aria-modal="true" aria-label="Fiche"><div class="fc"><div class="ft"><h3></h3><button type="button" class="x" aria-label="Fermer la fiche">✕</button></div><div class="fb"></div></div></div>
<div id="bulle" role="tooltip"></div>
<div id="sco" role="dialog" aria-modal="true" aria-label="Score"><div class="fc"><div class="ft"><h3></h3><button type="button" class="x" aria-label="Fermer le score">✕</button></div><div class="fb"></div></div></div>
<script type="application/json" id="donnees">{json.dumps(donnees, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")}</script>
<script>{JS}</script></body></html>'''
    open(a.sortie, 'w', encoding='utf-8').write(doc)
    return len(prets), n_cours, len(doc.encode())


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--carte', default='')
    ap.add_argument('--catalogue', default='LOT_Claude_Finaux/CATALOGUE_248.csv')
    ap.add_argument('--audites', default='', help='SSP audités et fusionnés, par numéro de LOT : 1-16,18')
    ap.add_argument('--reference', default='Claude/_reference', help='ancien chemin (examens.json, pharmaco.json), conservé en lecture seule, non affiché')
    ap.add_argument('--donnees', default='Claude/_progression/donnees', help='source de vérité des onglets Examens, Pharmacologie, Sciences fondamentales')
    ap.add_argument('--base', default='', help='préfixe des liens vers les cours (vide : relatif à la page)')
    ap.add_argument('--themes', default='Claude/_progression/themes.json', help='20 thèmes : 3 couleurs au plus (EYE SPOT comprise), atténuées 60-80 %%, contraste >= 7:1')
    ap.add_argument('--glossaire', default='Claude/_progression/glossaire.json', help='sigles (survol) et scores (fenêtre au clic) des fiches')
    ap.add_argument('--sortie', default='progression.html')
    a = ap.parse_args()
    print('%d SSP prêts, %d cours ouvrables, %d octets' % rendre(a))
