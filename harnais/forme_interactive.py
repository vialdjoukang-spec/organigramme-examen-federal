#!/usr/bin/env python3
"""Forme interactive des cours : références en exposant cliquables, « Sources bibliographiques » repliables, termes cliquables, arborescence.
  python3 harnais/forme_interactive.py stats <fichier>      → densité de références, termes, fenêtres, arborescence
  (module) convert(html) -> html : [Sn] → <sup><a href="#src-n">n</a></sup>, liste des sources → un seul <details>, CSS injectée (idempotent)
  (module) controle(html) -> (critiques, moyens, stats)"""
import html as H, re, sys
from pathlib import Path
MARQ = "<!-- FORME_INTERACTIVE -->"
CSS = """<style>.r{font-size:.72em;line-height:0;vertical-align:super;margin:0 .05em}.r a{text-decoration:none;color:#2563eb;padding:0 1px}.r a:hover{background:#dbeafe;border-radius:3px}
details.refs{margin:18px 0;border:1px solid #cfd4dc;border-radius:12px;padding:6px 14px;background:#f8fafc}details.refs>summary{cursor:pointer;font-weight:700;color:#334155}details.refs ol{list-style:none;padding-left:0}details.refs .n{font-weight:700;color:#475569}details.refs li{font-size:.86em;margin:.35em 0}details.refs li:target{background:#fef9c3}
.tm{border-bottom:1px dotted #7c3aed;color:#4c1d95;cursor:help;position:relative;display:inline}.tm .df{display:none;position:absolute;left:0;top:1.5em;z-index:20;width:min(320px,80vw);background:#1e1b4b;color:#fff;border-radius:8px;padding:8px 10px;font-size:.85em;font-weight:400;box-shadow:0 6px 20px #0006}.tm:hover .df,.tm:focus .df,.tm:focus-within .df{display:block}
details.arbre{border-left:4px solid #7c3aed;background:#f5f3ff;border-radius:8px;padding:6px 14px;margin:10px 0}details.arbre>summary{cursor:pointer;font-weight:700;color:#4c1d95}details.arbre ul{margin:.2em 0 .2em 1.1em;padding-left:.8em;border-left:1px dashed #a78bfa}
@media(prefers-color-scheme:dark){details.refs{background:#1b2033;border-color:#3a4256}details.refs>summary{color:#cbd5e1}.r a{color:#93c5fd}details.arbre{background:#241d3f}details.arbre>summary,.tm{color:#ddd0ff}}
table:not(#rm table){border-collapse:separate;border-spacing:0;width:100%;margin:12px 0;border:1px solid #c7d2fe;border-radius:12px;overflow:hidden;font-size:.93em}table:not(#rm table) th{background:linear-gradient(#4f46e5,#4338ca);color:#fff;font-weight:700;padding:8px 10px;text-align:left;border:0}table:not(#rm table) td{padding:7px 10px;border-top:1px solid #e0e7ff;vertical-align:top}table:not(#rm table) tr:nth-child(even) td{background:#f5f7ff}table:not(#rm table) tr:hover td{background:#e8edff}table:not(#rm table) td:first-child{font-weight:600;color:#312e81;background:#eef2ff}table:not(#rm table) caption{caption-side:top;text-align:left;font-weight:700;color:#4338ca;padding:4px 2px}
td.ok,tr.ok td{background:#dcfce7!important}td.mo,tr.mo td{background:#fef3c7!important}td.ko,tr.ko td{background:#fee2e2!important}
h2:not(#rm h2){border-left:6px solid #6366f1;background:linear-gradient(90deg,#eef2ff,transparent);padding:6px 12px;border-radius:0 8px 8px 0}h2:not(#rm h2):nth-of-type(3n+2){border-color:#0ea5e9;background:linear-gradient(90deg,#e0f2fe,transparent)}h2:not(#rm h2):nth-of-type(3n){border-color:#10b981;background:linear-gradient(90deg,#d1fae5,transparent)}
.tm.med{border-bottom:2px solid #0891b2;color:#155e75;background:#ecfeff;border-radius:4px;padding:0 3px}.tm.med .df{background:#164e63}
details.dx{display:inline}details.dx>summary{display:inline;cursor:pointer;border-bottom:1px dotted #7c3aed;color:#4c1d95;list-style:none}details.dx>summary::after{content:" ▾";font-size:.8em;color:#7c3aed}details.dx[open]>summary::after{content:" ▴"}details.dx>.dxc{display:block;margin:6px 0 8px;padding:8px 12px;background:#f5f3ff;border-left:4px solid #a78bfa;border-radius:6px;font-size:.95em}
@media(prefers-color-scheme:dark){table:not(#rm table) tr:nth-child(even) td{background:#1c2236}table:not(#rm table) td:first-child{background:#23294a;color:#c7d2fe}table:not(#rm table) td{border-color:#2f3656}table:not(#rm table) tr:hover td{background:#2a3358}details.dx>.dxc{background:#241d3f}.tm.med{background:#0c3a47;color:#a5f3fc}}</style>"""
def convert(t):
    if MARQ in t: return t
    # 1. liste des sources → un seul bloc repliable
    m = re.search(r"(<h[23][^>]*>[^<]*(?:[Ss]ources|[Rr]éférences)[^<]*</h[23]>\s*)?<ol[^>]*>\s*(<li[^>]*>\s*\[S\d+\].*?)</ol>", t, re.S)
    if m:
        lis = re.findall(r"<li[^>]*>\s*\[S(\d+)\]\s*(.*?)</li>", m.group(2), re.S)
        ol = "\n".join(f'<li id="src-{n}" value="{n}"><span class="n">[S{n}]</span> {x.strip()}</li>' for n, x in lis)
        t = t[:m.start()] + f'<details class="refs" id="refs"><summary>Sources bibliographiques</summary><ol>\n{ol}\n</ol></details>' + t[m.end():]
    # 2. marqueurs en exposants (grappes), doublons de grappe proches supprimés
    last = {}
    def grappe(mm):
        nums = re.findall(r"S(\d+)", mm.group(0)); key = ",".join(nums)
        if key in last and mm.start() - last[key] < 600: last[key] = mm.start(); return ""
        last[key] = mm.start()
        return '<sup class="r">' + ",".join(f'<a href="#src-{n}">{n}</a>' for n in nums) + "</sup>"
    head, sep, tail = t.partition('<details class="refs"')
    head = re.sub(r"(?:\s*\[S\d+\])+", grappe, head); t = head + sep + tail
    t = re.sub(r"(<sup class=\"r\">.*?</sup>)(\s*\1)+", r"\1", t)
    t = t.replace("</head>", CSS + "</head>", 1) if "</head>" in t else CSS + t
    return t.replace("</body>", MARQ + "</body>", 1) if "</body>" in t else t + MARQ
def stats(t):
    txt = re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)); mots = len(txt.split())
    gr = len(re.findall(r'<sup class="r">', t)) or len(re.findall(r"(?:\[S\d+\])+", t))
    arbre = re.search(r'<details[^>]*class="[^"]*arbre[^"]*"[^>]*>(.*?)</details>', t, re.S)
    return dict(mots=mots, grappes=gr, densite=round(1000 * gr / max(1, mots), 1), termes=len(re.findall(r'class="tm"', t)), fenetres=len(re.findall(r"<details", t)), arbre=bool(arbre), arbre_noeuds=len(re.findall(r"<li", arbre.group(1))) if arbre else 0, refs=bool(re.search(r'<details class="refs"', t)), brut=len(re.findall(r"\[S\d+\]", re.sub(r'<details class="refs".*?</details>', "", t, flags=re.S))))
def controle(t):
    s = stats(t); crit, moy = [], []
    if re.search(r"<h[1-6][^>]*>(?:(?!</h[1-6]>).)*class=\"tm", t, re.S): crit.append("terme cliquable dans un titre du plan : interdit (enlève .tm des <h1>–<h6>)")
    marques = set(re.findall(r"\b([A-Z][A-Za-zÀ-ÿ\-]{2,})®", re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", "", t)))
    cliq = set(re.findall(r'class="tm med"[^>]*>([A-Za-zÀ-ÿ\-]+)', t))
    manque = sorted(m for m in marques if m not in cliq)
    if manque: crit.append("médicaments non cliquables (première occurrence : <span class=\"tm med\" tabindex=\"0\">Nom®<span class=\"df\">classe ATC · famille · alternatives de la même classe</span></span>) : " + ", ".join(manque[:12]))
    if t.count('class="tm med"') < 6: crit.append("médicaments cliquables insuffisants : %d < 6 (marques ® ET dénominations communes)" % t.count('class="tm med"'))
    if not s["arbre"] or s["arbre_noeuds"] < 6: crit.append("point 1 : classification en arborescence absente ou trop courte (<details class=\"arbre\", ≥ 6 nœuds, du général au particulier)")
    if s["termes"] < 20: crit.append(f"termes cliquables insuffisants : {s['termes']} < 20 (<span class=\"tm\" tabindex=\"0\">terme<span class=\"df\">définition brève</span></span>)")
    if s["fenetres"] < 10: crit.append(f"fenêtres repliables insuffisantes : {s['fenetres']} < 10")
    if s["densite"] > 14: crit.append(f"références saturantes : {s['densite']} grappes / 1000 mots > 14 (cible ≤ 10 : une grappe par bloc d'affirmations)")
    elif s["densite"] > 10: moy.append(f"densité de références élevée : {s['densite']} / 1000 mots (cible ≤ 10)")
    return crit, moy, s
if __name__ == "__main__":
    if sys.argv[1] == "stats":
        t = Path(sys.argv[2]).read_text(encoding="utf-8", errors="replace"); print(stats(convert(t)))
