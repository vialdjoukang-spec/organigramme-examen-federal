#!/usr/bin/env python3
"""RÉCEPTACLE — page d'accueil unique du projet (ordres de Vial des 11.11.2026), zéro modèle.

Trois onglets, palette claire et vivante, jauge colorée et ondulante (esthétique de outils/progression.py) :
  1. Cours — les 19 groupes de SSP du catalogue PROFILES (G, S1–S9, F1–F2, O1–O7), chacun avec son icône, sa
     dénomination exacte, sa jauge et deux portes : « Cours et diagnostics » et « Banque QCM et questions type examen ».
     Dans un groupe : chaque SSP sous son nom en clair, puis ses dix diagnostics numérotés (liste gelée, 🚩 graves),
     et un bouton « Réflexe <code> » : fenêtre centrale tirée de la seule Phase A du LOT (algorithme discriminant ou
     arbre décisionnel) et fréquences de Claude/_reference/reflexes.json (chiffres de la Phase A, sinon rien).
  2. Examens complémentaires — arbre de Claude/_reference/examens.json.
  3. Pharmacologie — format v2 de Claude/_reference/pharmaco.json : par système, trois colonnes alignées
     (structure et fonctionnement → altération et pathologies → classes qui corrigent, mnémotechnique sourcé).
Fiches : Claude/_reference/fiches/<id>.json ; banques QCM : Claude/_reference/qcm/<groupe>.json (MISSION_QCM.md).

Usage : python3 outils/receptacle.py --audites 1-16 --reference Claude/_reference --base <url> --sortie progression.html
"""
import os, re, csv, json, html, glob, argparse, datetime, unicodedata

LECONS = ['A'] + [f'DX{i}' for i in range(1, 11)]
E = html.escape

# Groupes de SSP du catalogue PROFILES 2023 (dénominations françaises du dépôt, app_v2.html).
FAMILLES = [('G', 'Général'), ('S', 'Symptômes, par système et région'), ('F', 'Constatations'), ('O', 'Autres situations')]
GROUPES = [
    ('G', 'Plaintes et symptômes généraux', 14), ('S1', 'Tête et cou', 28), ('S2', 'Thorax', 352), ('S3', 'Abdomen', 40),
    ('S4', 'Pelvis et système urogénital', 330), ('S5', 'Dos et extrémités', 95), ('S6', 'Peau et muqueuses', 18),
    ('S7', 'Système nerveux', 280), ('S8', 'Traumatismes', 2), ('S9', 'Symptômes émotionnels et comportementaux', 300),
    ('F1', "Constatations à l'examen physique", 168), ('F2', 'Constatations aux examens complémentaires', 186),
    ('O1', 'Grossesse et maternité', 325), ('O2', 'Enfance et adolescence', 48), ('O3', 'Grand âge', 24),
    ('O4', 'Prévention et promotion de la santé', 135), ('O5', 'Soins palliatifs', 290), ('O6', 'Enjeux psychosociaux', 10),
    ('O7', 'Questions de santé diverses', 158)]

_I = {  # icônes d'interface (traits, 24 × 24)
    'G': '<path d="M12 3v11"/><circle cx="12" cy="17" r="3.2"/><path d="M15 6h3M15 9h2M15 12h3"/>',
    'S1': '<path d="M7 20v-3.5A6.5 6.5 0 1 1 17 11v2l1.8 3H17v2a2 2 0 0 1-2 2h-2"/><path d="M11 8.5a2 2 0 1 1 3 1.7"/>',
    'S2': '<path d="M12 3v7"/><path d="M12 10c-2 0-3-2-5-2-2.5 0-3.5 4-3.5 8 0 3 1.5 4.5 3.5 4.5S12 19 12 15"/><path d="M12 10c2 0 3-2 5-2 2.5 0 3.5 4 3.5 8 0 3-1.5 4.5-3.5 4.5S12 19 12 15"/>',
    'S3': '<path d="M9 3v4c0 2-4 3-4 8a6 6 0 0 0 12 0c0-2.5-1.5-3.5-3-3.5s-2.5 1-2.5 2.5"/><path d="M15 3v3"/>',
    'S4': '<path d="M8.5 4C5 4 4 8 4 11s1.5 6 4.5 6c2 0 2.5-2 2.5-4s-1-3-1-5 0-4-1.5-4z"/><path d="M15.5 4C19 4 20 8 20 11s-1.5 6-4.5 6c-2 0-2.5-2-2.5-4s1-3 1-5 0-4 1.5-4z"/><path d="M11 15l1 6M13 15l-1 6"/>',
    'S5': '<path d="M12 2.5v19"/><path d="M9 5h6M8.5 9h7M8.5 13h7M9 17h6"/>',
    'S6': '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/><path d="M9.5 14.5a2.5 2.5 0 0 0 2.5 2.5"/>',
    'S7': '<path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 5 3 3 0 0 0 6 1V5a2 2 0 0 0-3-1z"/><path d="M15 4a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 5 3 3 0 0 1-6 1"/>',
    'S8': '<rect x="3" y="8.5" width="18" height="7" rx="3.5" transform="rotate(-40 12 12)"/><path d="M10.5 10.5l3 3M12 9l3 3M9 12l3 3"/>',
    'S9': '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/><path d="M9.5 11.5c.8 1 1.6 1.4 2.5 1.4s1.7-.4 2.5-1.4"/>',
    'F1': '<path d="M6 3v6a4 4 0 0 0 8 0V3"/><path d="M10 13v3a4 4 0 0 0 8 0v-2"/><circle cx="18" cy="12" r="2"/>',
    'F2': '<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 1.8 3h10.4a2 2 0 0 0 1.8-3l-5-9V3"/><path d="M7.5 15h9"/>',
    'O1': '<circle cx="12" cy="4.5" r="2"/><path d="M10 21v-5H8l1.5-6.5a2.5 2.5 0 0 1 4.8-.3c2.2 1 3 3 2.2 5L15 16v5"/>',
    'O2': '<circle cx="12" cy="5" r="2.2"/><path d="M8 11l4-2 4 2M12 9v6M9 21l3-6 3 6"/>',
    'O3': '<circle cx="10" cy="4.5" r="2"/><path d="M10 7v6l-2 8M10 13l3 8M10 9l-3 3M17 10v11M17 10a2 2 0 0 0-2-2"/>',
    'O4': '<path d="M12 3l7 3v5c0 5-3 8.5-7 10-4-1.5-7-5-7-10V6z"/><path d="M9 12l2 2 4-4"/>',
    'O5': '<path d="M12 21C7 18 4 14.5 4 10a8 8 0 0 1 8-7c0 6 4 7 8 7 0 4.5-3 8-8 11z"/><path d="M12 21V11"/>',
    'O6': '<circle cx="8" cy="7" r="2.5"/><circle cx="16" cy="7" r="2.5"/><path d="M3.5 19a4.5 4.5 0 0 1 9 0M11.5 19a4.5 4.5 0 0 1 9 0"/>',
    'O7': '<circle cx="12" cy="12" r="8.5"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
}


FONDS = ['#f3f8ff', '#f1fbf6', '#f7f4ff', '#fff6f1', '#eef7fd']  # fonds vivants ultra-pâles (ordre de Vial), un par groupe en rotation


def icone(g):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{_I[g]}</svg>'


def groupe_de(code):
    return 'G' if code.startswith('G') else code.split('.')[0]


def plage(s):
    out = set()
    for bloc in filter(None, re.split(r'[,\s]+', s or '')):
        bloc = bloc.split('=')[0]
        a, _, b = bloc.partition('-')
        out.update(range(int(a), int(b or a) + 1))
    return out


def fichier(lot, l):
    return f'Claude/LOT_{lot:03d}/LOT_{lot:03d}_Phase_A_V0.html' if l == 'A' else f'Claude/LOT_{lot:03d}/LOT_{lot:03d}_Phase_B_V0_DX.{l[2:]}.html'


def texte(s):
    """HTML d'un cours → texte : appels de source, définitions survolées et balises retirés."""
    s = re.sub(r'<sup.*?</sup>|<span class="df">.*?</span>', '', s, flags=re.S)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).replace(' ,', ',').replace(' .', '.').strip()


def norme(s):
    s = ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if not unicodedata.combining(c))
    return ' '.join(re.findall(r'[a-z0-9]+', s)[:3])


def noms_dx(lot):
    """Nom de chaque diagnostic : liste gelée, sinon bandeau du cours ; drapeau grave : liste gelée, sinon Phase A."""
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
    a = fichier(lot, 'A')
    if not graves and os.path.exists(a):
        rouges = set()
        for m in re.finditer(r'<(h3|tr)[^>]*>(.*?)</\1>', open(a, encoding='utf-8', errors='ignore').read(), re.S):
            t = texte(m.group(2))
            d = re.search(r'DX\.\d+\s*[—–-]?\s*(.+)', t)
            if d and '🚩' in t:
                rouges.add(norme(d.group(1).split('🚩')[0]))
        graves = {k: norme(v) in rouges for k, v in noms.items()}
    return noms, graves


def _etapes(bloc):
    """Étapes d'un algorithme de Phase A : lignes de tableau, sinon éléments de liste, sinon paragraphes « si »."""
    out = []
    corps = re.search(r'<tbody>(.*?)</tbody>', bloc, re.S)
    for tr in re.findall(r'<tr[^>]*>(.*?)</tr>', corps.group(1) if corps else bloc, re.S):
        c = [texte(x) for x in re.findall(r'<td[^>]*>(.*?)</td>', tr, re.S)]
        if len(c) >= 3 and len(c[0]) <= 8:
            out.append({'n': c[0], 'si': c[1], 'alors': ' '.join(c[2:])})
        elif len(c) >= 2:
            out.append({'si': c[0], 'alors': ' '.join(c[1:])})
    if not out:
        for li in re.findall(r'<li[^>]*>(.*?)</li>', bloc, re.S):
            t = texte(li)
            si, fl, alors = t.partition('→')
            out.append({'si': si.strip(), 'alors': alors.strip()} if fl else {'si': t, 'alors': ''})
    if not out:
        for p in re.findall(r'<(?:p|div class="p")[^>]*>(.*?)</(?:p|div)>', bloc, re.S):
            t = texte(p)
            if t.startswith('Si '):
                out.append({'si': t, 'alors': ''})
    for e in out:
        e['alors'] = e['alors'].lstrip('→ ').strip()
    return [e for e in out if e['si']]


def reflexe(lot):
    """Raisonnement rapide tiré de la seule Phase A : algorithme discriminant, sinon arbre décisionnel (point 10)."""
    a = fichier(lot, 'A')
    if not os.path.exists(a):
        return None
    h = open(a, encoding='utf-8', errors='ignore').read()
    meilleur = None
    for motif in (r'<h[34][^>]*>[^<]*Algorithme discriminant[^<]*</h[34]>', r'<h[2-4][^>]*>\s*(?:<[^>]+>)*\s*10\.\s*Arbre[^<]*(?:</[^h][^>]*>)*</h[2-4]>'):
        m = re.search(motif, h)
        if not m:
            continue
        fin = re.search(r'<h[1-3][\s>]|</section>', h[m.end():])
        bloc = h[m.end():m.end() + (fin.start() if fin else 20000)]
        et = _etapes(bloc)
        intro = re.search(r'<div class="p">(.*?)</div>', bloc, re.S)
        if len(et) >= 3:
            meilleur = {'titre': texte(m.group(0)), 'intro': texte(intro.group(1)) if intro else '', 'etapes': et[:24]}
            break
    return meilleur


def arbre(chemin):
    return json.load(open(chemin, encoding='utf-8')) if os.path.exists(chemin) else {}


def fiches(dossier):
    out = {}
    for f in sorted(glob.glob(os.path.join(dossier, '*.json'))):
        try:
            out[os.path.basename(f)[:-5]] = json.load(open(f, encoding='utf-8'))
        except ValueError:
            pass
    return out


CSS = """
:root{--fond:#f3f8ff;--carte:#fff;--encre:#141a26;--doux:#55617a;--trait:#dce6f2;--piste:#e4edf8;--rouge:#d92d20;--ombre:0 1px 2px rgba(30,30,50,.04),0 10px 30px rgba(40,70,120,.08)}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--fond);color:var(--encre);font:15.5px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
background-image:radial-gradient(900px 380px at 0% -10%,#fff6f1,transparent 60%),radial-gradient(800px 360px at 100% 0%,#f1fbf6,transparent 60%),radial-gradient(700px 300px at 50% -20%,#f7f4ff,transparent 65%);background-repeat:no-repeat}
button{font:inherit;color:inherit}
.haut{max-width:1180px;margin:0 auto;padding:18px 16px 0}
.haut h1{font-size:1.45rem;letter-spacing:-.02em;margin:0;line-height:1.2}
.haut h1 b{background:linear-gradient(90deg,hsl(12 85% 55%),hsl(38 95% 50%) 45%,hsl(160 70% 38%));-webkit-background-clip:text;background-clip:text;color:transparent}
.haut .sous{color:var(--doux);font-size:.86rem;margin:4px 0 12px}
.tete-carte{background:var(--carte);border:1px solid var(--trait);border-radius:20px;padding:14px 16px;box-shadow:var(--ombre)}
.k{display:flex;gap:22px;flex-wrap:wrap;margin:0 0 10px}.k b{font-size:1.3rem;display:block;font-variant-numeric:tabular-nums}.k small{color:var(--doux);font-size:.78rem}
nav.on{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;margin:14px 0 0;padding-bottom:2px}nav.on::-webkit-scrollbar{display:none}
nav.on button{border:1px solid var(--trait);background:rgba(255,255,255,.7);padding:9px 15px;border-radius:999px;white-space:nowrap;cursor:pointer;color:var(--doux);font-weight:600}
nav.on button.a{background:var(--encre);color:#fff;border-color:var(--encre)}
main{max-width:1180px;margin:0 auto;padding:14px 16px 40px}
section.p{display:none}section.p.a{display:block}
/* jauge : coulée colorée, ondulante */
.j{display:grid;grid-template-columns:1fr 48px;align-items:center;gap:8px}.j span{font-size:.78rem;font-weight:700;text-align:right;font-variant-numeric:tabular-nums}
.t{height:10px;background:var(--piste);border-radius:99px;overflow:hidden;box-shadow:inset 0 1px 2px rgba(0,0,0,.07)}.j.g{grid-template-columns:1fr 60px}.j.g .t{height:16px}.j.g span{font-size:.95rem}
.f{height:100%;width:0;border-radius:inherit;position:relative;overflow:hidden;
background:linear-gradient(90deg,hsl(calc(var(--h) - 30) 88% 60%),hsl(var(--h) 85% 52%),hsl(calc(var(--h) + 30) 90% 58%),hsl(calc(var(--h) - 30) 88% 60%));background-size:300% 100%;
box-shadow:0 0 10px hsl(var(--h) 85% 55% / .35);animation:monte 1.6s cubic-bezier(.2,.8,.2,1) forwards,flot 7s linear infinite}
.f::before{content:"";position:absolute;inset:0;background:radial-gradient(9px 5px at 9px 0,rgba(255,255,255,.55) 98%,transparent) 0 0/18px 100% repeat-x;opacity:.8;animation:vague 1.8s linear infinite}
.f::after{content:"";position:absolute;top:0;bottom:0;width:38%;left:-40%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.6),transparent);animation:lueur 3s ease-in-out infinite}
@keyframes monte{to{width:var(--p)}}@keyframes flot{to{background-position:300% 0}}@keyframes vague{to{background-position:18px 0}}@keyframes lueur{0%{left:-40%}70%,100%{left:110%}}
@media (prefers-reduced-motion:reduce){.f{animation:none;width:var(--p)}.f::before,.f::after{animation:none}.f::after{display:none}}
/* familles et groupes */
.fam{margin:22px 0 10px;display:flex;align-items:baseline;gap:10px}.fam h2{font-size:1rem;margin:0;letter-spacing:.01em}.fam span{color:var(--doux);font-size:.8rem}
.grille{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}
.gr{background:var(--fd,#fff);border:1px solid var(--trait);border-radius:18px;padding:14px;box-shadow:var(--ombre);position:relative;overflow:hidden}
.gr::before{content:"";position:absolute;inset:0 0 auto 0;height:4px;background:linear-gradient(90deg,hsl(var(--h) 85% 60%),hsl(calc(var(--h) + 35) 85% 62%))}
.gr .ti{display:flex;gap:12px;align-items:center;margin:2px 0 10px}
.ic{flex:none;width:44px;height:44px;border-radius:14px;display:grid;place-items:center;background:hsl(var(--h) 90% 95%);color:hsl(var(--h) 65% 38%)}.ic svg{width:26px;height:26px}
.gr h3{font-size:1.02rem;margin:0;line-height:1.25}.gr .co{font-size:.74rem;font-weight:700;color:hsl(var(--h) 60% 38%);letter-spacing:.04em}
.gr .m{color:var(--doux);font-size:.8rem;margin:6px 0 10px}
.bt{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.bt button,.btn{border:1px solid hsl(var(--h) 60% 85%);background:hsl(var(--h) 90% 97%);color:hsl(var(--h) 60% 30%);border-radius:12px;padding:9px 10px;cursor:pointer;font-weight:650;font-size:.85rem;line-height:1.25;text-align:center}
.bt button:hover,.btn:hover{background:hsl(var(--h) 90% 93%)}
/* vue d'un groupe */
.retour{border:1px solid var(--trait);background:var(--carte);border-radius:999px;padding:8px 14px;cursor:pointer;font-weight:600;margin:4px 0 12px}
.gt{display:flex;gap:12px;align-items:center;margin:0 0 6px}.gt h2{margin:0;font-size:1.25rem;line-height:1.2}
.ssp{background:var(--fd,#fff);border:1px solid var(--trait);border-left:5px solid hsl(var(--h) 75% 62%);border-radius:16px;padding:12px 14px;margin:10px 0;box-shadow:var(--ombre)}
.ssp.att{border-left-color:var(--trait)}
.sh{display:flex;gap:10px;align-items:flex-start;justify-content:space-between;flex-wrap:wrap}
.sn{font-size:1.06rem;font-weight:750;line-height:1.3;color:var(--encre);text-decoration:none;flex:1 1 200px}a.sn:hover{color:hsl(var(--h) 65% 35%)}
.sc{display:inline-block;font-size:.72rem;font-weight:700;color:hsl(var(--h) 60% 35%);background:hsl(var(--h) 90% 95%);border-radius:6px;padding:1px 6px;margin-left:6px;vertical-align:2px}
.ssp .j{margin:8px 0 4px}
ol.dx{margin:6px 0 0;padding:0 0 0 18px;list-style:none;counter-reset:d}
ol.dx li{counter-increment:d;position:relative;margin:2px 0}
ol.dx li::before{content:counter(d);position:absolute;left:-2px;top:8px;width:20px;font-size:.75rem;font-weight:700;color:hsl(var(--h) 55% 45%);text-align:right}
ol.dx a,ol.dx span.x{display:flex;gap:6px;align-items:baseline;padding:6px 8px 6px 26px;border-radius:9px;text-decoration:none;color:var(--encre);font-size:.92rem;line-height:1.3}
ol.dx a:hover{background:hsl(var(--h) 90% 96%)}ol.dx span.x{color:var(--doux)}
.gv{color:var(--rouge);flex:none}
.vide{color:var(--doux);font-size:.9rem;padding:8px 0}
/* fenêtre centrale (Réflexe) */
.mo{position:fixed;inset:0;z-index:30;background:rgba(24,22,30,.58);backdrop-filter:blur(3px);display:none;align-items:center;justify-content:center;padding:12px}.mo.a{display:flex}
.mb{background:var(--carte);border-radius:20px;max-width:720px;width:100%;max-height:90vh;overflow:auto;box-shadow:0 20px 60px rgba(0,0,0,.3);overscroll-behavior:contain}
.mh{position:sticky;top:0;background:var(--carte);padding:14px 16px 10px;border-bottom:1px solid var(--trait);display:flex;gap:10px;align-items:flex-start;z-index:1}
.mh h2{flex:1;margin:0;font-size:1.08rem;line-height:1.3}.mh small{display:block;color:var(--doux);font-weight:500;font-size:.8rem}
.fx{border:1px solid var(--trait);background:var(--carte);border-radius:10px;width:38px;height:38px;cursor:pointer;flex:none;font-size:1.1rem}
.mc{padding:12px 16px 18px}.mc h3{font-size:.92rem;margin:16px 0 8px;color:hsl(var(--h) 55% 35%)}
.et{display:grid;grid-template-columns:auto 1fr;gap:10px;margin:8px 0}.et b{min-width:30px;padding:0 6px;height:30px;white-space:nowrap;border-radius:15px;display:grid;place-items:center;background:hsl(var(--h) 90% 94%);color:hsl(var(--h) 60% 32%);font-size:.8rem}
.et p{margin:3px 0 0;font-size:.92rem}.et .al{color:hsl(var(--h) 55% 30%);font-weight:600}
.fr{list-style:none;margin:0;padding:0}.fr li{display:flex;gap:8px;align-items:baseline;padding:6px 0;border-bottom:1px dashed var(--trait);font-size:.92rem}
.fr .n{flex:none;width:22px;font-weight:700;color:var(--doux);text-align:right}.fr .nm{flex:1}.fr .v{font-weight:750;white-space:nowrap}
.fr sup{color:var(--rouge);font-size:.66rem;font-weight:500;line-height:1.2;display:block;text-align:right;white-space:normal;max-width:210px}
.vv{text-align:right}.note{color:var(--doux);font-size:.78rem;margin:12px 0 0}
/* visionneuses */
#vue,#fv{position:fixed;inset:0;z-index:20;background:var(--carte);display:none;flex-direction:column}#vue.a,#fv.a{display:flex}
.bar{display:flex;gap:6px;align-items:center;padding:6px 8px;border-bottom:1px solid var(--trait);background:var(--carte)}
.bar b{flex:1;min-width:0;font-size:.88rem;line-height:1.2;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}.bar small{display:block;color:var(--doux);font-weight:400}
.bar button,.bar a{border:1px solid var(--trait);background:var(--carte);border-radius:10px;padding:8px 11px;cursor:pointer;color:var(--encre);text-decoration:none;flex:none}
#vue iframe{flex:1;border:0;width:100%}
#fv .corps{flex:1;overflow:auto;padding:10px;max-width:860px;width:100%;margin:0 auto}
/* QCM */
.qv{background:var(--carte);border:1px dashed hsl(var(--h) 50% 75%);border-radius:18px;padding:22px 16px;text-align:center;color:var(--doux)}
.qv b{display:block;color:var(--encre);font-size:1.05rem;margin:6px 0}
.q{background:var(--carte);border:1px solid var(--trait);border-radius:16px;padding:14px;margin:10px 0;box-shadow:var(--ombre)}
.q p{margin:0 0 8px}.q button.c{display:block;width:100%;text-align:left;border:1px solid var(--trait);background:#fff;border-radius:10px;padding:9px 11px;margin:5px 0;cursor:pointer}
.q button.c.ok{border-color:hsl(150 60% 45%);background:hsl(150 70% 95%)}.q button.c.ko{border-color:var(--rouge);background:hsl(5 90% 96%)}.q .ex{display:none;font-size:.9rem;color:var(--doux)}.q.r .ex{display:block}
/* arbres (examens) et fiches */
.so{display:flex;gap:4px;overflow-x:auto;margin:0 0 10px;scrollbar-width:none}.so::-webkit-scrollbar{display:none}
.so button,.chip{border:1px solid var(--trait);background:var(--carte);padding:7px 12px;border-radius:999px;white-space:nowrap;cursor:pointer;font-size:.86rem;color:var(--doux)}
.so button.a,.chip.a{background:var(--encre);color:#fff;border-color:var(--encre)}
.arb{list-style:none;margin:0;padding:0}.arb ul{list-style:none;margin:0 0 0 14px;padding:0 0 0 12px;border-left:2px solid var(--trait)}
.arb button{text-align:left;width:100%;border:1px solid var(--trait);background:var(--carte);border-radius:12px;padding:9px 12px;margin:4px 0;cursor:pointer}
.arb button[aria-expanded=true]{background:#eef7fd;font-weight:700}.arb button.fe{border-style:dashed}.arb button small{color:var(--doux);font-weight:400}
.arb li>ul{display:none}.arb li.o>ul{display:block}
.fiche{background:var(--carte);border:1px solid var(--trait);border-radius:16px;padding:14px;margin:10px 0}
.fiche h3{margin:0 0 8px;font-size:1.08rem}.fiche h4{margin:14px 0 4px;font-size:.95rem;color:hsl(12 60% 40%)}.fiche ul{margin:4px 0;padding-left:18px}
.ind{color:var(--rouge);font-weight:700}
.fiche table{border-collapse:collapse;width:100%;font-size:.88rem}.fiche td,.fiche th{border:1px solid var(--trait);padding:6px;vertical-align:top;text-align:left}.fiche th{background:#eef7fd}
.tw{overflow-x:auto}.cas{border:1px solid var(--trait);border-radius:10px;padding:8px 10px;margin:6px 0;background:#f7f4ff}
.cas>button{border:0;background:none;padding:2px 0;cursor:pointer;color:hsl(12 60% 40%);font-weight:700;text-align:left}
.cas .suite{display:none;margin:6px 0 0 10px}.cas.o>.suite{display:block}.concl{font-weight:700}
.fiche figure{margin:8px 0}.fiche img{max-width:100%;border-radius:8px}.fiche figcaption{font-size:.82rem;color:var(--doux)}
.src{font-size:.78rem;color:var(--doux);overflow-wrap:anywhere}
/* pharmacologie : trois colonnes alignées */
.ph-intro{color:var(--doux);font-size:.88rem;margin:4px 0 12px}
.ph-tete{display:none}
.lg{display:grid;grid-template-columns:1fr;gap:0;margin:0 0 14px;background:var(--carte);border:1px solid var(--trait);border-radius:18px;box-shadow:var(--ombre);overflow:hidden}
.cel{padding:12px 14px;position:relative}.cel+.cel{border-top:1px solid var(--trait)}
.cel .lab{font-size:.68rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;margin:0 0 4px}
.c1 .lab{color:hsl(165 60% 32%)}.c2 .lab{color:hsl(12 70% 45%)}.c3 .lab{color:hsl(275 45% 45%)}
.c1{background:#f1fbf6}.c2{background:#fff6f1}.c3{background:#f7f4ff}
.cel h4{margin:0 0 6px;font-size:.98rem;line-height:1.3}.cel ul{margin:0 0 6px;padding-left:18px;font-size:.9rem}.cel p{margin:4px 0;font-size:.9rem}
.cel .q2{color:var(--doux);font-style:italic;font-size:.86rem}
.cl{display:block;width:100%;text-align:left;border:1px solid hsl(275 40% 88%);background:#fff;border-radius:12px;padding:8px 11px;margin:6px 0 0;cursor:pointer}
.cl.vide{border-style:dashed}.cl b{display:block;font-size:.92rem}.cl small{color:var(--doux)}
.mn{font-size:.8rem;color:hsl(275 35% 35%);background:hsl(275 70% 97%);border-radius:8px;padding:5px 8px;margin:4px 0 0 10px}
a.rf{color:var(--doux);font-size:.72rem;text-decoration:none;vertical-align:super;margin-left:1px;cursor:pointer}
.ph-src{font-size:.78rem;color:var(--doux);overflow-wrap:anywhere;padding-left:22px}.ph-src li:target,.ph-src li.vu{background:#dff0fb}
@media(min-width:900px){
 .ph-tete{display:grid;grid-template-columns:1fr 1fr 1.05fr;gap:0;position:sticky;top:0;z-index:2;background:var(--fond);padding:6px 0;font-size:.72rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase}
 .ph-tete div{padding:0 14px}.ph-tete div:nth-child(1){color:hsl(165 60% 32%)}.ph-tete div:nth-child(2){color:hsl(12 70% 45%)}.ph-tete div:nth-child(3){color:hsl(275 45% 45%)}
 .lg{grid-template-columns:1fr 1fr 1.05fr}.cel+.cel{border-top:0;border-left:1px solid var(--trait)}.cel .lab{display:none}
 .c1::after,.c2::after{content:"→";position:absolute;right:-9px;top:14px;width:18px;height:18px;border-radius:50%;background:#fff;border:1px solid var(--trait);display:grid;place-items:center;font-size:.7rem;color:var(--doux);z-index:1}
 .haut h1{font-size:1.75rem}}
@media(max-width:520px){.grille{grid-template-columns:1fr}.k{gap:16px}.bt button{font-size:.82rem}}
"""

JS = r"""
const D=JSON.parse(document.getElementById('donnees').textContent);
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const GR=Object.fromEntries(D.groupes.map(g=>[g.code,g]));const SSP=Object.fromEntries(D.ssp.map(s=>[s.code,s]));
const jauge=(p,h,grande)=>'<div class="j'+(grande?' g':'')+'"><div class="t"><div class="f" style="--p:'+p+'%;--h:'+h+'"></div></div><span>'+p+' %</span></div>';
let base='';
function onglet(id){$$('nav.on button').forEach(b=>b.classList.toggle('a',b.dataset.o===id));$$('section.p').forEach(s=>s.classList.toggle('a',s.id==='p-'+id));}
$$('nav.on button').forEach(b=>b.onclick=()=>{location.hash=b.dataset.o});
/* ----- Cours : accueil des groupes ----- */
function accueil(){let h='';for(const [f,nom] of D.familles){const gs=D.groupes.filter(g=>g.famille===f);
  h+='<div class="fam"><h2>'+esc(f)+' · '+esc(nom)+'</h2><span>'+gs.reduce((a,g)=>a+g.n,0)+' SSP</span></div><div class="grille">';
  for(const g of gs)h+='<article class="gr" style="--h:'+g.h+';--fd:'+g.fd+'"><div class="ti"><div class="ic">'+g.icone+'</div><div><div class="co">'+esc(g.code)+'</div><h3>'+esc(g.nom)+'</h3></div></div>'+jauge(g.p,g.h)+
    '<div class="m">'+g.prets+' / '+g.n+' SSP prêts · '+g.cours+' cours ouvrables'+(g.qcm?' · '+g.qcm+' questions':'')+'</div><div class="bt"><button type="button" data-go="g='+g.code+'">Cours et diagnostics</button><button type="button" data-go="qcm='+g.code+'">Banque QCM et questions type examen</button></div></article>';
  h+='</div>';}
  $('#p-cours').innerHTML=h;}
function lien(f,txt,cls,id){return f?'<a class="'+cls+'" href="'+esc(D.base+f)+'" data-c="'+esc(id)+'">'+txt+'</a>':'<span class="'+(cls==='sn'?'sn':'x')+'">'+txt+'</span>';}
function vueGroupe(c){const g=GR[c];if(!g)return accueil();
  let h='<button class="retour" type="button" data-go="cours">← Tous les groupes</button><div class="gt" style="--h:'+g.h+'"><div class="ic">'+g.icone+'</div><div><div class="co" style="color:hsl('+g.h+' 60% 38%);font-weight:700;font-size:.78rem">'+esc(g.code)+'</div><h2>'+esc(g.nom)+'</h2></div></div>'+
    '<div style="--h:'+g.h+'">'+jauge(g.p,g.h,true)+'</div><p class="ph-intro">'+g.prets+' SSP prêts sur '+g.n+'. Un nom souligné ouvre le cours ; le bouton Réflexe ouvre la démarche rapide tirée de la Phase A.</p>';
  for(const s of D.ssp.filter(x=>x.groupe===c)){
    h+='<article class="ssp'+(s.pret?'':' att')+'" style="--h:'+g.h+';--fd:'+g.fd+'"><div class="sh">'+lien(s.fA,esc(s.nom),'sn',s.code+'-A')+'<span class="sc">'+esc(s.code)+'</span>'+
      (s.reflexe?'<button class="btn" type="button" data-go="reflexe='+esc(s.code)+'">Réflexe '+esc(s.code)+'</button>':'')+'</div>'+jauge(s.p,g.h)+
      '<ol class="dx">'+s.dx.map(d=>'<li>'+lien(d.f,(d.g?'<b class="gv" aria-label="diagnostic grave">🚩</b>':'')+'<span>'+esc(d.n)+'</span>','',s.code+'-'+d.i)+'</li>').join('')+'</ol></article>';}
  $('#p-cours').innerHTML=h;}
function vueQcm(c){const g=GR[c];if(!g)return accueil();const Q=(D.qcm[c]||{}).questions||[];
  let h='<button class="retour" type="button" data-go="cours">← Tous les groupes</button><div class="gt" style="--h:'+g.h+'"><div class="ic">'+g.icone+'</div><div><div class="co" style="color:hsl('+g.h+' 60% 38%);font-weight:700;font-size:.78rem">'+esc(g.code)+' · Banque QCM et questions type examen</div><h2>'+esc(g.nom)+'</h2></div></div>';
  if(!Q.length)h+='<div class="qv" style="--h:'+g.h+'"><div class="ic" style="margin:0 auto">'+g.icone+'</div><b>Banque prête à recevoir</b>Les questions de type A et Kprim de ce groupe apparaîtront ici dès leur dépôt dans Claude/_reference/qcm/'+esc(c)+'.json.</div>';
  else Q.forEach((q,i)=>{h+='<div class="q" data-i="'+i+'"><p><b>'+(i+1)+'.</b> '+(q.ssp?'<span class="sc">'+esc(q.ssp)+'</span> ':'')+esc(q.enonce)+'</p>'+(q.choix||[]).map((x,j)=>'<button class="c" type="button" data-j="'+j+'">'+String.fromCharCode(65+j)+'. '+esc(x)+'</button>').join('')+
    '<div class="ex">'+esc(q.explication||'')+(q.sources?'<ol class="src">'+q.sources.map(s=>'<li>'+esc(s)+'</li>').join('')+'</ol>':'')+'</div></div>'});
  $('#p-cours').innerHTML=h;
  $$('.q').forEach(el=>el.onclick=e=>{const b=e.target.closest('button.c');if(!b)return;const q=Q[+el.dataset.i],j=+b.dataset.j;
    const bon=Array.isArray(q.reponse)?q.reponse:[q.reponse];if(q.type==='Kprim'){$$('button.c',el).forEach((x,k)=>x.classList.add(q.reponse[k]?'ok':'ko'));el.classList.add('r');return}
    $$('button.c',el).forEach((x,k)=>{if(bon.includes(k))x.classList.add('ok')});if(!bon.includes(j))b.classList.add('ko');el.classList.add('r')});}
/* ----- Réflexe : fenêtre centrale ----- */
function ouvrirReflexe(c){const s=SSP[c];if(!s||!s.reflexe)return;const g=GR[s.groupe],R=s.reflexe;
  $('#mr').style.setProperty('--h',g.h);
  let h='<div class="mh"><h2>Réflexe '+esc(s.code)+' — '+esc(s.nom)+'<small>'+esc(R.titre)+' · Phase A du LOT_'+String(s.lot).padStart(3,'0')+'</small></h2><button class="fx" type="button" data-ferme aria-label="Fermer">✕</button></div><div class="mc">';
  if(R.intro)h+='<p style="margin:0 0 6px;font-size:.92rem">'+esc(R.intro)+'</p>';
  h+='<h3>Raisonnement, étape par étape</h3>'+R.etapes.map((e,i)=>'<div class="et"><b>'+esc(e.n||i+1)+'</b><div><p>'+esc(e.si)+'</p>'+(e.alors?'<p class="al">→ '+esc(e.alors)+'</p>':'')+'</div></div>').join('');
  h+='<h3>Les dix diagnostics et leur fréquence</h3><ul class="fr">'+s.dx.map(d=>{const f=(s.freq||{})[d.i.slice(2)];return '<li><span class="n">'+d.i.slice(2)+'</span><span class="nm">'+(d.g?'<b class="gv">🚩</b> ':'')+esc(d.n)+'</span>'+(f?'<span class="vv"><span class="v">'+esc(f.v)+'</span><sup>'+esc(f.pop)+'</sup></span>':'')+'</li>'}).join('')+'</ul>';
  h+='<p class="note">Étapes reprises de la Phase A ; fréquences du point 2 de la même Phase A, dénominateur en rouge. Sans chiffre sourcé, rien n\'est affiché.</p></div>';
  $('#mr .mb').innerHTML=h;$('#mr').classList.add('a');document.body.style.overflow='hidden';$('#mr .fx').focus();}
function fermerReflexe(){$('#mr').classList.remove('a');document.body.style.overflow='';}
$('#mr').addEventListener('click',e=>{if(e.target.id==='mr'||e.target.closest('[data-ferme]'))history.back()});
addEventListener('keydown',e=>{if(e.key==='Escape'&&($('#mr').classList.contains('a')||$('#fv').classList.contains('a')||$('#vue').classList.contains('a')))history.back()});
/* ----- Visionneuse de cours ----- */
const liste=[];D.ssp.forEach(s=>{if(s.fA)liste.push({s,id:s.code+'-A',n:s.nom,f:s.fA});s.dx.forEach(d=>{if(d.f)liste.push({s,id:s.code+'-'+d.i,n:d.n,f:d.f})})});
function ouvrirCours(id){const i=liste.findIndex(x=>x.id===id);if(i<0)return;const x=liste[i];$('#vue').dataset.i=i;
  $('#vt').innerHTML=esc(x.n)+'<small>'+esc(x.s.code)+' · '+esc(x.s.nom)+'</small>';
  const cadre=document.createElement('iframe');cadre.id='vf';cadre.title='Cours';cadre.src=D.base+x.f;$('#vf').replaceWith(cadre);$('#vn').href=D.base+x.f;
  $('#vue').classList.add('a');document.body.style.overflow='hidden';}
function fermerCours(){if(!$('#vue').classList.contains('a'))return;$('#vue').classList.remove('a');const c=document.createElement('iframe');c.id='vf';c.title='Cours';c.src='about:blank';$('#vf').replaceWith(c);document.body.style.overflow='';}
$('#vr').onclick=()=>history.back();
$('#vp').onclick=()=>{const i=+$('#vue').dataset.i;if(i>0)history.replaceState(null,'','#cours='+liste[i-1].id),ouvrirCours(liste[i-1].id)};
$('#vs').onclick=()=>{const i=+$('#vue').dataset.i;if(i<liste.length-1)history.replaceState(null,'','#cours='+liste[i+1].id),ouvrirCours(liste[i+1].id)};
/* ----- Fiches (examens, pharmacologie) ----- */
function algo(n){if(!n)return'';if(typeof n==='string')return '<p class="concl">'+esc(n)+'</p>';
  return '<p>'+esc(n.question||'')+'</p>'+(n.branches||[]).map(b=>'<div class="cas"><button type="button">'+esc(b.si)+'</button><div class="suite">'+algo(b.alors)+'</div></div>').join('');}
function tableau(t){if(!t||!t.length)return'';const k=Object.keys(t[0]);return '<div class="tw"><table><tr>'+k.map(x=>'<th>'+esc(x)+'</th>').join('')+'</tr>'+t.map(r=>'<tr>'+k.map(x=>'<td>'+esc(r[x])+'</td>').join('')+'</tr>').join('')+'</table></div>';}
function para(v){return Array.isArray(v)?'<ul>'+v.map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul>':'<p>'+esc(v)+'</p>';}
function fiche(id){const f=D.fiches[id];if(!f)return '<div class="fiche"><p class="vide">Fiche en préparation : elle sera rédigée sur sources suisses lues, puis auditée.</p></div>';
  let h='<div class="fiche"><h3>'+esc(f.titre)+'</h3>';
  if(f.indication)h+='<h4>'+(id.startsWith('ph-')?'Indications actuelles':'Indication de la demande')+'</h4><div class="ind">'+para(f.indication)+'</div>';
  for(const s of f.sections||[])h+='<h4>'+esc(s.titre)+'</h4>'+(s.texte?para(s.texte):'')+tableau(s.tableau)+(s.algorithme?algo(s.algorithme):'');
  for(const g of f.images||[])h+='<figure><img loading="lazy" src="'+esc(D.base+g.fichier)+'" alt="'+esc(g.legende)+'"><figcaption>'+esc(g.legende)+' — '+esc(g.source||'')+'</figcaption></figure>';
  if(f.sources)h+='<h4>Sources</h4><ol class="src">'+f.sources.map(s=>'<li>'+esc(s)+'</li>').join('')+'</ol>';
  return h+'</div>';}
function titreFiche(id){const f=D.fiches[id];if(f)return f.titre;for(const s of D.pharmaco.systemes||[])for(const l of s.lignes)for(const c of l.classes)if(c.fiche===id)return c.titre;return 'Fiche';}
function ouvrirFiche(id){$('#ft').textContent=titreFiche(id);$('#fc').innerHTML=fiche(id);$('#fc').scrollTop=0;$('#fv').classList.add('a');document.body.style.overflow='hidden';}
function fermerFiche(){$('#fv').classList.remove('a');document.body.style.overflow='';}
$('#fr').onclick=()=>history.back();$('#fc').onclick=e=>{const c=e.target.closest('.cas>button');if(c)c.parentElement.classList.toggle('o')};
/* ----- Examens complémentaires : arbre ----- */
function nbFiches(n){return (n.fiche&&D.fiches[n.fiche]?1:0)+(n.enfants||[]).reduce((a,x)=>a+nbFiches(x),0);}
function nbFeuilles(n){return (n.enfants&&n.enfants.length)?n.enfants.reduce((a,x)=>a+nbFeuilles(x),0):1;}
function branche(n){const feuille=!(n.enfants&&n.enfants.length);
  return '<li><button type="button" aria-expanded="false" class="'+(feuille?'fe':'')+'"'+(feuille?' data-fiche="'+esc(n.fiche||n.id)+'"':'')+'>'+esc(n.titre)+(n.aide?' <small>— '+esc(n.aide)+'</small>':'')+(feuille?'':' <small>('+nbFiches(n)+'/'+nbFeuilles(n)+')</small>')+'</button>'+(feuille?'<ul></ul>':'<ul>'+n.enfants.map(branche).join('')+'</ul>')+'</li>';}
function monter(racine,arbre){const el=$(racine);if(!(arbre.onglets||[]).length){el.innerHTML='<p class="vide">Structure en préparation.</p>';return}
  el.innerHTML='<div class="so">'+arbre.onglets.map((o,i)=>'<button data-i="'+i+'"'+(i?'':' class="a"')+'>'+esc(o.titre)+'</button>').join('')+'</div><div class="corps"></div>';
  const montrer=i=>{const o=arbre.onglets[i];$$('.so button',el).forEach(b=>b.classList.toggle('a',+b.dataset.i===i));
    $('.corps',el).innerHTML=(o.intro?'<p class="ph-intro">'+esc(o.intro)+'</p>':'')+'<ul class="arb">'+(o.enfants||[]).map(branche).join('')+'</ul>';};
  el.onclick=e=>{const b=e.target.closest('.so button');if(b)return montrer(+b.dataset.i);
    const a=e.target.closest('.arb button');if(!a)return;const li=a.parentElement,o=li.classList.toggle('o');a.setAttribute('aria-expanded',o);
    if(a.dataset.fiche){li.classList.remove('o');a.setAttribute('aria-expanded',false);location.hash='fiche='+a.dataset.fiche}};
  montrer(0);}
monter('#p-examens .arbre',D.examens);
/* ----- Pharmacologie : trois colonnes alignées ----- */
const PH=D.pharmaco.systemes||[];
function refs(a,sys){return (a||[]).map(n=>'<a class="rf" data-ref="'+esc(sys)+'-'+n+'">['+n+']</a>').join('');}
function vuePharmaco(id){const s=PH.find(x=>x.id===id)||PH[0];if(!s){$('#p-pharmaco').innerHTML='<p class="vide">Structure en préparation.</p>';return}
  let h='<div class="so">'+PH.map(x=>'<button type="button" data-go="pharmaco='+esc(x.id)+'"'+(x.id===s.id?' class="a"':'')+'>'+esc(x.titre)+(x.statut==='pilote'?' ✦':'')+'</button>').join('')+'</div>';
  h+='<p class="ph-intro">'+esc(s.intro||'')+(s.statut==='squelette'?' Squelette : les colonnes 1 et 2 restent à rédiger sur sources suisses lues ; les classes et leurs fiches sont déjà rangées.':'')+'</p>';
  h+='<div class="ph-tete"><div>Structure et fonctionnement</div><div>Altération et pathologies</div><div>Classes qui corrigent</div></div>';
  for(const l of s.lignes){const st=l.structure,al=l.alteration;
    h+='<div class="lg"><div class="cel c1"><div class="lab">Structure et fonctionnement</div>'+(st?'<h4>'+esc(st.titre)+'</h4><ul>'+st.elements.map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul><p><b>Fonction.</b> '+esc(st.fonction)+'</p><p><b>Fonctionnement.</b> '+esc(st.fonctionnement)+refs(st.src,s.id)+'</p>':'<h4>'+esc(l.groupe||'')+'</h4><p class="q2">À rédiger.</p>')+'</div>'+
      '<div class="cel c2"><div class="lab">Altération et pathologies</div>'+(al?'<h4>'+esc(al.titre)+'</h4><ul>'+al.pathologies.map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul>'+refs(al.src,s.id):'<p class="q2">À rédiger.</p>')+'</div>'+
      '<div class="cel c3"><div class="lab">Classes qui corrigent</div>'+l.classes.map(c=>'<button type="button" class="cl'+(D.fiches[c.fiche]?'':' vide')+'" data-go="fiche='+esc(c.fiche)+'"><b>'+esc(c.titre)+'</b>'+(c.exemple?'<small>'+esc(c.exemple)+'</small>':'')+(D.fiches[c.fiche]?'':'<small> · fiche en préparation</small>')+'</button>'+
        (c.mnemo?'<div class="mn">Mémo : '+esc(c.mnemo.texte)+refs(c.mnemo.src,s.id)+'</div>':'')).join('')+'</div></div>';}
  if((s.sources||[]).length)h+='<h3 style="font-size:.95rem;margin:18px 0 6px">Sources</h3><ol class="ph-src">'+s.sources.map((x,i)=>'<li id="'+esc(s.id)+'-'+(i+1)+'">'+esc(x.replace(/^\[\d+\]\s*/,''))+'</li>').join('')+'</ol>';
  $('#p-pharmaco').innerHTML=h;}
document.addEventListener('click',e=>{const r=e.target.closest('a.rf');if(r){e.preventDefault();const li=document.getElementById(r.dataset.ref);if(li){$$('.ph-src li.vu').forEach(x=>x.classList.remove('vu'));li.classList.add('vu');li.scrollIntoView({behavior:'smooth',block:'center'})}return}
  const go=e.target.closest('[data-go]');if(go){location.hash=go.dataset.go;return}
  const c=e.target.closest('a[data-c]');if(c){e.preventDefault();location.hash='cours='+c.dataset.c}});
/* ----- Routeur : chaque vue a son adresse, le retour du téléphone ferme la fenêtre ouverte ----- */
function route(){const h=decodeURIComponent(location.hash.slice(1));const [k,v]=h.split('=');
  const sur=['reflexe','cours','fiche'].includes(k)&&v;
  if(!sur){fermerReflexe();fermerCours();fermerFiche();}
  if(k==='reflexe'&&v){if(!base){const s=SSP[v];if(s){onglet('cours');vueGroupe(s.groupe);base='g='+s.groupe}}ouvrirReflexe(v);return}
  if(k==='cours'&&v){if(!base){onglet('cours');accueil();base='cours'}ouvrirCours(v);return}
  if(k==='fiche'&&v){if(!base){onglet('pharmaco');vuePharmaco();base='pharmaco'}ouvrirFiche(v);return}
  base=h||'cours';
  if(k==='examens'){onglet('examens')}
  else if(k==='pharmaco'){onglet('pharmaco');vuePharmaco(v)}
  else{onglet('cours');if(k==='g')vueGroupe(v);else if(k==='qcm')vueQcm(v);else accueil();scrollTo(0,0)}}
addEventListener('hashchange',route);vuePharmaco();route();
"""


def rendre(a):
    C = json.load(open(a.carte, encoding='utf-8')) if a.carte and os.path.exists(a.carte) else {'lecons': {}}
    L = C.get('lecons', {})
    cat = [(int(r['lot']), r['code'], r['ssp_profiles_2023_fr_en'].split('|')[0].strip()) for r in csv.DictReader(open(a.catalogue, encoding='utf-8'))]
    prets = plage(a.audites)
    freq = arbre(os.path.join(a.reference, 'reflexes.json'))
    qcm = fiches(os.path.join(a.reference, 'qcm'))
    ssp, n_cours = [], 0
    for lot, code, nom in cat:
        noms, graves = noms_dx(lot)
        rows = [L.get(f'{lot:03d}:{l}') for l in LECONS]
        pret = lot in prets
        if pret:
            p = 100
        elif L:
            p = min(95, round(sum(r['score'] if r else 0 for r in rows) / 11))
        else:  # sans carte : part des onze fichiers présents, plafonnée (rien n'est audité)
            p = round(40 * sum(os.path.exists(fichier(lot, l)) for l in LECONS) / 11)
        ok = lambda l: pret and os.path.exists(fichier(lot, l))
        dx = [{'i': l, 'n': noms.get(l, f'Diagnostic {l[2:]} (nom à venir)'), 'g': bool(graves.get(l)), 'f': fichier(lot, l) if ok(l) else None} for l in LECONS[1:]]
        n_cours += ok('A') + sum(bool(d['f']) for d in dx)
        ssp.append({'lot': lot, 'code': code, 'nom': nom, 'groupe': groupe_de(code), 'pret': pret, 'p': p,
                    'fA': fichier(lot, 'A') if ok('A') else None, 'dx': dx,
                    'reflexe': reflexe(lot) if pret else None, 'freq': freq.get(code, {}) if pret else {}})
    groupes = []
    for g, nom, h in GROUPES:
        ss = [s for s in ssp if s['groupe'] == g]
        groupes.append({'code': g, 'nom': nom, 'famille': g[0], 'h': h, 'icone': icone(g), 'fd': FONDS[len(groupes) % len(FONDS)], 'n': len(ss), 'prets': sum(s['pret'] for s in ss),
                        'cours': sum(bool(s['fA']) + sum(bool(d['f']) for d in s['dx']) for s in ss),
                        'p': round(sum(s['p'] for s in ss) / len(ss)) if ss else 0, 'qcm': len((qcm.get(g) or {}).get('questions', []))})
    glob_p = round(sum(s['p'] for s in ssp) / len(ssp))
    donnees = {'base': a.base, 'familles': FAMILLES, 'groupes': groupes, 'ssp': ssp, 'qcm': qcm,
               'examens': arbre(os.path.join(a.reference, 'examens.json')), 'pharmaco': arbre(os.path.join(a.reference, 'pharmaco.json')),
               'fiches': fiches(os.path.join(a.reference, 'fiches'))}
    maj = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=1))).strftime('%d.%m.%Y %H:%M')
    doc = f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Progression — Examen fédéral</title><link rel="icon" href="data:,"><style>{CSS}</style></head><body>
<header class="haut"><h1><b>Examen fédéral</b> · médecine humaine</h1><p class="sous">Cours, diagnostics, examens et pharmacologie, situation par situation (PROFILES 2023).</p>
<div class="tete-carte"><div class="k"><div><b>{glob_p} %</b><small>progression globale</small></div><div><b>{len(prets)}</b><small>SSP prêts sur {len(ssp)}</small></div>
<div><b>{n_cours}</b><small>cours ouvrables</small></div><div><b>{len(GROUPES)}</b><small>groupes PROFILES</small></div><div><b>{maj}</b><small>mise à jour (Zurich)</small></div></div>
<div class="j g"><div class="t"><div class="f" style="--p:{glob_p}%;--h:28"></div></div><span>{glob_p} %</span></div></div>
<nav class="on"><button data-o="cours" class="a">Cours</button><button data-o="examens">Examens complémentaires</button><button data-o="pharmaco">Pharmacologie</button></nav></header>
<main>
<section class="p a" id="p-cours"></section>
<section class="p" id="p-examens"><p class="ph-intro">Réviser l'interprétation des examens : indication de la demande en rouge, valeurs, raisonnement par cases, images.</p><div class="arbre"></div></section>
<section class="p" id="p-pharmaco"></section>
</main>
<div id="mr" class="mo" role="dialog" aria-modal="true" aria-label="Réflexe"><div class="mb"></div></div>
<div id="vue" role="dialog" aria-label="Cours"><div class="bar"><button id="vr" type="button" aria-label="Retour">←</button><b id="vt"></b><button id="vp" type="button" aria-label="Cours précédent">‹</button><button id="vs" type="button" aria-label="Cours suivant">›</button><a id="vn" target="_blank" rel="noopener" aria-label="Ouvrir dans un nouvel onglet">↗</a></div><iframe id="vf" title="Cours" src="about:blank"></iframe></div>
<div id="fv" role="dialog" aria-label="Fiche"><div class="bar"><button id="fr" type="button" aria-label="Retour">←</button><b id="ft"></b></div><div class="corps" id="fc"></div></div>
<script type="application/json" id="donnees">{json.dumps(donnees, ensure_ascii=False).replace("</", "<\\/")}</script>
<script>{JS}</script></body></html>'''
    open(a.sortie, 'w', encoding='utf-8').write(doc)
    return len(prets), n_cours, len(doc.encode())


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--carte', default='')
    ap.add_argument('--catalogue', default='LOT_Claude_Finaux/CATALOGUE_248.csv')
    ap.add_argument('--audites', default='', help='SSP audités et fusionnés, par numéro de LOT : 1-16,18')
    ap.add_argument('--reference', default='Claude/_reference')
    ap.add_argument('--base', default='', help='préfixe des liens vers les cours (vide : relatif à la page)')
    ap.add_argument('--sortie', default='progression.html')
    a = ap.parse_args()
    print('%d SSP prêts, %d cours ouvrables, %d octets' % rendre(a))
