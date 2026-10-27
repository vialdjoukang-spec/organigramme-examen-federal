#!/usr/bin/env python3
"""Forme interactive des cours : références en exposant cliquables, « Sources bibliographiques » repliables, termes cliquables, arborescence.
  python3 harnais/forme_interactive.py stats <fichier>      → densité de références, termes, fenêtres, arborescence
  (module) convert(html) -> html : [Sn] → <sup><a href="#src-n">n</a></sup>, liste des sources → un seul <details>, CSS injectée (idempotent)
  (module) controle(html) -> (critiques, moyens, stats)"""
import html as H, re, sys, json
from pathlib import Path
MARQ = "<!-- FORME_INTERACTIVE -->"
_F = json.loads((Path(__file__).parent / "atkinson.b64.json").read_text())
FONTE = "".join(f'@font-face{{font-family:"Atkinson Hyperlegible";font-weight:{w};font-display:swap;src:url(data:font/woff2;base64,{_F[w]}) format("woff2")}}' for w in ("400", "700"))
CSS = """<style>html,body,table,td,th,summary,button,.tm .df{font-family:"Atkinson Hyperlegible",Verdana,system-ui,sans-serif}body{font-size:16px;line-height:1.6}.r{font-size:.72em;line-height:0;vertical-align:super;margin:0 .05em}.r a{text-decoration:none;color:#2563eb;padding:0 1px}.r a:hover{background:#dbeafe;border-radius:3px}
details.refs{margin:18px 0;border:1px solid #cfd4dc;border-radius:12px;padding:6px 14px;background:#f8fafc}details.refs>summary{cursor:pointer;font-weight:700;color:#334155}details.refs ol{list-style:none;padding-left:0}details.refs .n{font-weight:700;color:#475569}details.refs li{font-size:.86em;margin:.35em 0}details.refs li:target{background:#fef9c3}
.tm{border-bottom:1px dotted #7c3aed;color:#4c1d95;cursor:help;position:relative;display:inline}.tm .df{display:none;position:absolute;left:0;top:1.5em;z-index:20;width:min(320px,80vw);background:#1e1b4b;color:#fff;border-radius:8px;padding:8px 10px;font-size:.85em;font-weight:400;box-shadow:0 6px 20px #0006}.tm:hover .df,.tm:focus .df,.tm:focus-within .df{display:block}
div.arb{margin:12px 0}.arbt{font-weight:700;color:#4c1d95;margin-bottom:6px}.niv{border:1px solid #c4b5fd;background:#f5f3ff;border-radius:10px;padding:7px 12px;margin-bottom:6px;position:relative}.niv::before{content:"└";position:absolute;left:-16px;top:6px;color:#7c3aed}.niv b{color:#3b0764}.niv .org{float:right;font-size:.8em;background:#fff;color:#4c1d95;border:1px solid #c4b5fd;border-radius:6px;padding:0 6px;margin-left:8px}.niv.cible .org{background:#ede9fe}.niv .dfn{display:block;font-size:.88em;color:#475569;margin-top:2px}.niv.cible{background:#6d28d9;border-color:#4c1d95}.niv.cible b,.niv.cible .dfn{color:#fff}.liste{margin:2px 0 6px;font-size:.92em;color:#334155}.chip{display:inline-block;background:#ede9fe;border:1px solid #c4b5fd;border-radius:999px;padding:1px 9px;margin:2px 3px 2px 0;font-size:.92em}.voisin .chip{background:#f1f5f9;border-color:#cbd5e1}@media(prefers-color-scheme:dark){.niv{background:#241d3f}.niv b{color:#e9d5ff}.niv .dfn,.liste{color:#cbd5e1}.chip{background:#2e2557}}.sb{display:none}.sb:target{display:block;position:fixed;left:0;right:0;bottom:0;z-index:50;background:#bae6fd;color:#0c4a6e;padding:8px 16px;font-size:.88em;box-shadow:0 -4px 14px #0003}.sb a{margin-left:10px;color:#075985;font-weight:700}p.fil{border-left:4px solid #7c3aed;padding:6px 12px;background:#f5f3ff;border-radius:0 8px 8px 0;margin:10px 0}details.arbre{border-left:4px solid #7c3aed;background:#f5f3ff;border-radius:8px;padding:6px 14px;margin:10px 0}details.arbre>summary{cursor:pointer;font-weight:700;color:#4c1d95}details.arbre ul{margin:.2em 0 .2em 1.1em;padding-left:.8em;border-left:1px dashed #a78bfa}
@media(prefers-color-scheme:dark){details.refs{background:#1b2033;border-color:#3a4256}details.refs>summary{color:#cbd5e1}.r a{color:#93c5fd}details.arbre{background:#241d3f}details.arbre>summary,.tm{color:#ddd0ff}}
table:not(#rm table){border-collapse:separate;border-spacing:0;width:100%;margin:12px 0;border:1px solid #c7d2fe;border-radius:12px;overflow:hidden;font-size:.93em}table:not(#rm table) th{background:linear-gradient(#4f46e5,#4338ca);color:#fff;font-weight:700;padding:8px 10px;text-align:left;border:0}table:not(#rm table) td{padding:7px 10px;border-top:1px solid #e0e7ff;vertical-align:top}table:not(#rm table) tr:nth-child(even) td{background:#f5f7ff}table:not(#rm table) tr:hover td{background:#e8edff}table:not(#rm table) td:first-child{font-weight:600;color:#312e81;background:#eef2ff}table:not(#rm table) caption{caption-side:top;text-align:left;font-weight:700;color:#4338ca;padding:4px 2px}
td.ok,tr.ok td{background:#dcfce7!important}td.mo,tr.mo td{background:#fef3c7!important}td.ko,tr.ko td{background:#fee2e2!important}
h2:not(#rm h2){border-left:6px solid #6366f1;background:linear-gradient(90deg,#eef2ff,transparent);padding:6px 12px;border-radius:0 8px 8px 0}h2:not(#rm h2):nth-of-type(3n+2){border-color:#0ea5e9;background:linear-gradient(90deg,#e0f2fe,transparent)}h2:not(#rm h2):nth-of-type(3n){border-color:#10b981;background:linear-gradient(90deg,#d1fae5,transparent)}
.tm.med{border-bottom:2px solid #0891b2;color:#155e75;background:#ecfeff;border-radius:4px;padding:0 3px}.tm.med .df{background:#164e63;width:min(500px,92vw);line-height:1.4}.tm.med .df ul{margin:4px 0 0 16px;padding:0}.tm.med .df li{margin:2px 0}.tm.med .df b{color:#a5f3fc}
.dx>input{position:absolute;opacity:0;width:0;height:0}.dx>.dxt{cursor:pointer;border-bottom:1px dotted #7c3aed;color:#4c1d95}.dx>.dxt::after{content:" ▾";font-size:.8em;color:#7c3aed}.dx>input:checked+.dxt::after{content:" ▴"}.dx>input:focus-visible+.dxt{outline:2px solid #7c3aed}.dx>.dxc{display:none;margin:6px 0 8px;padding:8px 12px;background:#f5f3ff;border-left:4px solid #a78bfa;border-radius:6px;font-size:.95em}.dx>input:checked~.dxc{display:block}
@media(prefers-color-scheme:dark){table:not(#rm table) tr:nth-child(even) td{background:#1c2236}table:not(#rm table) td:first-child{background:#23294a;color:#c7d2fe}table:not(#rm table) td{border-color:#2f3656}table:not(#rm table) tr:hover td{background:#2a3358}  .dx>.dxc{background:#241d3f}.dx>.dxt{color:#ddd0ff}.tm.med{background:#0c3a47;color:#a5f3fc}}</style>"""
def convert(t):
    if MARQ in t: return t
    ABR = {}
    # 1. liste des sources → un seul bloc repliable
    m = re.search(r"(<h[23][^>]*>[^<]*(?:[Ss]ources|[Rr]éférences)[^<]*</h[23]>\s*)?<ol[^>]*>\s*(<li[^>]*>\s*\[S\d+\].*?)</ol>", t, re.S)
    if m:
        lis = re.findall(r"<li[^>]*>\s*\[S(\d+)\]\s*(.*?)</li>", m.group(2), re.S)
        ol = "\n".join(f'<li id="src-{n}" value="{n}"><span class="n">[S{n}]</span> {x.strip()}</li>' for n, x in lis)
        bandes = "".join(f'<div class="sb" id="sb-{n}"><b>[{n}]</b> {re.sub(r"<[^>]+>", "", x).strip()} <a href="#">fermer</a></div>\n' for n, x in lis)
        t = t[:m.start()] + f'<details class="refs" id="refs"><summary>Sources bibliographiques</summary><ol>\n{ol}\n</ol></details>' + bandes + t[m.end():]
    # 1 bis. déroulés en ligne : <details class="dx"> → case à cocher CSS (la phrase continue, le contenu se déroule)
    cnt = [0]
    def dx(mm):
        titre, corps = mm.group(1).strip(), mm.group(2).strip()
        if corps.startswith('<div class="dxc">') and corps.endswith("</div>"): corps = corps[17:-6]
        if len(re.sub(r"<[^>]+>", "", corps)) <= 420 and 'class="tm' not in corps:   # définition brève → fenêtre flottante
            corps = re.sub(r"</?(?:span|div|p)[^>]*>", "", corps)
            return f'<span class="tm" tabindex="0">{titre}<span class="df">{corps}</span></span>'
        cnt[0] += 1; i = f"dx{cnt[0]}"   # contenu long → se déroule dans la phrase
        return f'<span class="dx"><input type="checkbox" id="{i}"><label class="dxt" for="{i}">{titre}</label><span class="dxc">{corps}</span></span>'
    t = re.sub(r"<details(?:\s+class=[\"']?(?:dx|i|in|f)[\"']?[^>]*|\s+style=[\"'][^\"']*display:\s*inline[^\"']*[\"'][^>]*)>\s*<summary[^>]*>(.*?)</summary>\s*(.*?)\s*</details>", dx, t, flags=re.S)
    # 1 ter. préambule (méthode, abréviations) → en fin de page ; fil d'Ariane sobre pour la classification
    s = re.search(r'<section class="monograph"', t) or re.search(r'<main[ >]', t)
    if s:
        seg = t[:s.start()]; blocs = []
        def prend(mm): blocs.append(mm.group(0)); return ""
        seg2 = re.sub(r'<p[^>]*>.*?</p>|<div class="p">.*?</div>', prend, seg, flags=re.S)
        if blocs:
            t = seg2 + t[s.start():]
            ab = re.search(r"Abréviations\s*:(.*?)(?:</p>|</div>|$)", "".join(blocs), re.S)   # le reste (date, méthode, sources lues) n'est pas du cours : supprimé
            ABR.update(parse_sigles(re.sub(r"<[^>]+>", " ", ab.group(1)))) if ab else None   # la liste est DÉTRUITE à l'affichage ; chaque sigle devient survolable
            notes = ""
            t = t.replace("</body>", notes + "</body>", 1) if "</body>" in t else t + notes
    def arbre(mm):
        corps = mm.group(1); racine = []; pile = [racine]; cur = None
        for tok in re.finditer(r"<ul[^>]*>|</ul>|<li[^>]*>|</li>|[^<]+|<[^>]+>", corps):
            x = tok.group(0)
            if x.startswith("<ul"): pass
            elif x.startswith("</ul"): pass
            elif x.startswith("<li"):
                n = dict(h="", k=[]); pile[-1].append(n); pile.append(n["k"]); cur = n; n["_p"] = pile[:-1]; n["_s"] = [n]
            elif x.startswith("</li"):
                if len(pile) > 1: pile.pop()
                cur = None
            else:
                if len(pile) > 1:
                    # texte propre : attribué au dernier noeud ouvert de ce niveau
                    par = pile[-2] if len(pile) > 1 else racine
                    owner = par[-1] if par else None
                    if owner is not None: owner["h"] += x
        def chemin(niv, anc):
            for n in niv:
                if "<b>" in n["h"]: return anc + [n], n, niv
                r = chemin(n["k"], anc + [n])
                if r: return r
        r = chemin(racine, [])
        if not r: return mm.group(0)
        anc, cible, freres = r
        def nom_def(h):
            m_ = re.search(r'class="tm"[^>]*>(.*?)<span class="df">(.*?)</span></span>', h, re.S)
            if m_: return re.sub(r"<[^>]+>", "", m_.group(1)).strip(), re.sub(r"<[^>]+>", "", m_.group(2)).strip()
            return re.sub(r"<[^>]+>", "", h).strip(), ""
        out = ['<div class="arb"><div class="arbt">Où se situe le problème ? Du général au particulier</div>']
        for i, n in enumerate(anc):
            nm, df = nom_def(n["h"]); cible_ = n is cible
            mo = re.match(r"^(.*?)\s*\(([^()]{2,60})\)\s*$", nm); org = ""
            if mo: nm, org = mo.group(1), f'<span class="org">{mo.group(2)}</span>'
            out.append(f'<div class="niv{" cible" if cible_ else ""}" style="margin-left:{i*20}px"><b>{nm}</b>{org}' + (f'<span class="dfn">{df}</span>' if df else "") + "</div>")
        fr = [nom_def(n["h"])[0] for n in freres if n is not cible]
        if cible["k"]:
            ch = "".join(f'<span class="chip">{nom_def(n["h"])[0]}</span>' for n in cible["k"])
            out.append(f'<div class="liste" style="margin-left:{len(anc)*20}px">Comprend : {ch}</div>')
        if fr:
            out.append(f'<div class="liste voisin" style="margin-left:{(len(anc)-1)*20}px">Voisins, même niveau : ' + "".join(f'<span class="chip">{x}</span>' for x in fr) + "</div>")
        return "".join(out) + "</div>"
    t = re.sub(r'<details class="arbre"[^>]*>(?:<summary[^>]*>.*?</summary>)?(.*?)</details>', arbre, t, count=1, flags=re.S)
    # 2. marqueurs en exposants (grappes), doublons de grappe proches supprimés
    last = {}
    def grappe(mm):
        nums = re.findall(r"S(\d+)", mm.group(0)); key = ",".join(nums)
        if key in last and mm.start() - last[key] < 600: last[key] = mm.start(); return ""
        last[key] = mm.start()
        return '<sup class="r">' + ",".join(f'<a href="#sb-{n}">{n}</a>' for n in nums) + "</sup>"
    head, sep, tail = t.partition('<details class="refs"')
    head = re.sub(r"(?:\s*\[S\d+\])+", grappe, head); t = head + sep + tail
    t = re.sub(r"(<sup class=\"r\">.*?</sup>)(\s*\1)+", r"\1", t)
    t = re.sub(r"<!--(?!\s*(?:FORME_INTERACTIVE|FIN_FICHIER)).*?-->", "", t, flags=re.S)   # allègement : commentaires, indentations
    t = re.sub(r"(?m)^[ \t]+", "", t); t = re.sub(r"[ \t]{2,}", " ", t); t = re.sub(r"\n{2,}", "\n", t)
    css = FONTE.join(("<style>", "")) + re.sub(r"\s*\n\s*", "", CSS)[len("<style>"):] if False else re.sub(r"\s*\n\s*", "", CSS).replace("<style>", "<style>" + FONTE, 1)
    t = t.replace("</head>", css + "</head>", 1) if "</head>" in t else css + t
    t = habille_sigles(t, ABR)
    t = t.replace("</body>", MARQ + "</body>", 1) if "</body>" in t else t + MARQ
    return coupe_lignes(t)

def parse_sigles(s):
    """« A = définition ; B = définition » → {A: définition}"""
    d = {}
    for x in re.split(r"\s*;\s*", re.sub(r"\s+", " ", s).strip()):
        m = re.match(r"^([^\s=:]{2,14})\s*=\s*(.{3,260})$", x.strip().rstrip("."))
        if m and sum(c.isupper() or c.isdigit() for c in m.group(1)) >= 2: d[m.group(1)] = m.group(2).strip()   # un sigle, pas un mot
    return d

def habille_sigles(t, abr):
    """1re occurrence de chaque sigle, dans chaque point : survolable ou cliquable avec sa définition. Ni dans un titre, ni dans une fenêtre, ni dans un lien."""
    if not abr: return t
    rx = re.compile(r"(?<![\w\-/])(" + "|".join(sorted((re.escape(k) for k in abr), key=len, reverse=True)) + r")(?![\w\-/])")
    out, seen, sk, sp, stack = [], set(), 0, 0, []
    for p in re.split(r"(<[^>]+>)", t):
        if p.startswith("<"):
            low = p.lower()
            if re.match(r"<h3\b", low): seen = set()
            if re.match(r"<(h[1-6]|summary|title|caption|a|script|style|button|label|option)\b", low): sk += 1
            elif re.match(r"</(h[1-6]|summary|title|caption|a|script|style|button|label|option)>", low): sk = max(0, sk - 1)
            if low.startswith("<span"):
                if sp or re.search(r'class="(?:tm|tm med|df|dxc|dxt|org|dfn|chip)"', low): sp += 1
            elif low.startswith("</span") and sp: sp -= 1
            out.append(p); continue
        if sk or sp or len(p) < 2: out.append(p); continue
        def sub(m):
            k = m.group(1)
            if k in seen: return k
            seen.add(k)
            d = abr[k].replace("&", "&amp;").replace("<", "&lt;")
            return f'<span class="tm" tabindex="0">{k}<span class="df"><b>{k}</b> : {d}</span></span>'
        out.append(rx.sub(sub, p))
    return "".join(out)

def coupe_lignes(t, max_l=2900):
    out = []
    for l in t.split("\n"):
        while len(l) > 3000:
            c = l.rfind(">", 600, max_l) + 1 or l.rfind(" ", 600, max_l) + 1 or max_l
            out.append(l[:c]); l = l[c:]
        out.append(l)
    return "\n".join(out)
def stats(t):
    txt = re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)); mots = len(txt.split())
    gr = len(re.findall(r'<sup class="r">', t)) or len(re.findall(r"(?:\[S\d+\])+", t))
    arbre = re.search(r'<details[^>]*class="[^"]*arbre[^"]*"[^>]*>(.*?)</details>', t, re.S)
    return dict(mots=mots, grappes=gr, densite=round(1000 * gr / max(1, mots), 1), termes=len(re.findall(r'class="tm"', t)), fenetres=len(re.findall(r"<details", t)) + len(re.findall(r'class="dx"', t)) + len(re.findall(r'class="tm"', t)), arbre=bool(arbre), arbre_noeuds=len(re.findall(r"<li", arbre.group(1))) if arbre else 0, refs=bool(re.search(r'<details class="refs"', t)), brut=len(re.findall(r"\[S\d+\]", re.sub(r'<details class="refs".*?</details>', "", t, flags=re.S))))
def controle(t):
    s = stats(t); crit, moy = [], []
    corps = re.sub(r"(?is)<details class=\"refs\".*?</details>|<style.*?</style>|<script.*?</script>", "", t); corps = re.sub(r"<[^>]+>", " ", corps)
    meta = re.findall(r"LOT_\d+|Phase [AB]\b|\bV0\b|autre IA|\bcycles? \d|checkpoint|harnais|\baudits?\b|brouillon|tableau d.entrée|evidence/|[Pp]rompt|(?:ce|le|du|ton|votre) fichier|référentiel PROFILES de ce|dose AIPS prime|\[S\d+", corps)
    if meta: crit.append("mention de conception dans le cours (interdit : le texte s'adresse à des médecins résidents, sans date de rédaction, sans « fichier », « Phase », « LOT », « V0 », « cycle », « autre IA », « audit », sans [Sn] brut) : " + ", ".join(sorted(set(meta))[:10]) + f" ({len(meta)})")
    arbs_ = re.findall(r'<div class="niv[^"]*"[^>]*><b>.*?</div>', t, re.S)
    if arbs_ and sum(1 for a_ in arbs_ if 'class="org"' in a_) < max(2, len(arbs_) - 1): crit.append("classification : indique entre parenthèses, après chaque niveau, la classification d'où il vient : « Troubles anxieux (CIM-11) », « (DSM-5) », « (ATC) », « (PROFILES 2023) »")
    p1_ = re.search(r"1\. Définition et sémantique(.*?)<h[23][^>]*>\s*(?:<strong>)?\s*2\.", t, re.S)
    if p1_:
        corps1 = re.sub(r"(?is)<div class=\"arb\">.*?</div>(?=\s*<(?:p|div|table|h))", " ", p1_.group(1), count=1); corps1 = re.sub(r"(?s)<span class=\"(?:df|dxc)\">.*?</span></span>", " ", corps1); w1_ = len(re.sub(r"<[^>]+>", " ", corps1).split())
        if w1_ > 140: crit.append(f"point 1 trop long : {w1_} mots après la classification (≤ 140) : définis en peu de mots, densité maximale, aucune information perdue (déplace le détail dans un mot cliquable)")
    for m_ in re.finditer(r'class="tm med"[^>]*>([^<]+)<span class="df">(.*?)</span></span>', t, re.S):
        d_ = m_.group(2)
        if not (re.search(r"DCI\s*:", d_) and re.search(r"Classe\s*:", d_) and re.search(r"Groupe\s*:", d_) and re.search(r"[Cc]hefs? de file", d_)):
            crit.append(f"fenêtre du médicament « {m_.group(1).strip()} » incomplète : il faut DCI : …, Classe : …, Groupe : … puis les chefs de file du groupe avec indication et posologie AIPS"); break
    txt_ = re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>|<table.*?</table>|<details class=\"refs\".*?</details>", " ", t))
    ph_ = [len(x.split()) for x in re.split(r"(?<=[.!?;])\s+", txt_) if len(x.split()) > 3]
    if ph_:
        moy_l = sum(ph_) / len(ph_); long_ = sum(1 for n in ph_ if n > 30) / len(ph_)
        if moy_l > 20 or long_ > 0.06: crit.append(f"phrases trop longues : moyenne {moy_l:.0f} mots (≤ 20), {100*long_:.0f} % de phrases > 30 mots (≤ 6 %) : une idée par phrase, pas de nuance qui complique")
    if re.search(r"<h[1-6][^>]*>(?:(?!</h[1-6]>).)*class=\"tm", t, re.S): crit.append("terme cliquable dans un titre du plan : interdit (enlève .tm des <h1>–<h6>)")
    marques = set(re.findall(r"\b([A-Z][A-Za-zÀ-ÿ\-]{2,})®", re.sub(r"(?is)<details class=\"refs\".*?</details>", "", re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", "", t))))
    cliq = set(re.findall(r'class="tm med"[^>]*>([A-Za-zÀ-ÿ\-]+)', t))
    manque = sorted(m for m in marques if m not in cliq)
    if manque: crit.append("médicaments non cliquables (première occurrence : <span class=\"tm med\" tabindex=\"0\">Nom®<span class=\"df\">classe ATC · famille · alternatives de la même classe</span></span>) : " + ", ".join(manque[:12]))
    if t.count('class="tm med"') < 6: crit.append("médicaments cliquables insuffisants : %d < 6 (marques ® ET dénominations communes)" % t.count('class="tm med"'))
    if not s["arbre"] and 'class="arb"' not in t: crit.append("point 1 : classification absente : <details class=\"arbre\"> (liste ul/li imbriquée, du général au particulier, l'entité du chapitre en <b>)")
    elif 'class="arb"' in t and t.count('class="niv') < 3: crit.append("classification trop courte : au moins 3 niveaux, du général au particulier")
    if s["termes"] < 20: crit.append(f"termes cliquables insuffisants : {s['termes']} < 20 (<span class=\"tm\" tabindex=\"0\">terme<span class=\"df\">définition brève</span></span>)")
    if s["fenetres"] < 10: crit.append(f"fenêtres repliables insuffisantes : {s['fenetres']} < 10")
    if s["densite"] > 14: crit.append(f"références saturantes : {s['densite']} grappes / 1000 mots > 14 (cible ≤ 10 : une grappe par bloc d'affirmations)")
    elif s["densite"] > 10: moy.append(f"densité de références élevée : {s['densite']} / 1000 mots (cible ≤ 10)")
    return crit, moy, s
if __name__ == "__main__":
    if sys.argv[1] == "stats":
        t = Path(sys.argv[2]).read_text(encoding="utf-8", errors="replace"); print(stats(convert(t)))
