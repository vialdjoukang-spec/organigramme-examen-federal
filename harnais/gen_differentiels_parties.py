#!/usr/bin/env python3
"""Découpe DIFFERENTIELS_PAR_LOT.html en fichiers PARTIE_n.m (≈10 LOTS chacun). Réutilise style et instructions du fichier complet."""
import csv, html, re, math, os
D = "LOT_Claude_Finaux/"; O = D + "PARTIES/"; os.makedirs(O, exist_ok=True)
src = open(D + "DIFFERENTIELS_PAR_LOT.html", encoding="utf-8").read()
style = re.search(r"<style>.*?</style>", src, re.S).group(0)
mode = re.search(r'<section class="mode">.*?</section>', src, re.S).group(0)
e = html.escape
# groupes : lus depuis le fichier complet (panneaux p2), pour garder la même topographie
pan = {}
for m in re.finditer(r"<section class='p2' id='([SFO])-(\d+)'><h2>(.*?)</h2>(.*?)</section>", src, re.S):
    items = re.findall(r"<details class='ssp' id='lot-(\d+)'.*?</details>", m.group(4), re.S)
    blocs = re.findall(r"(<details class='ssp' id='lot-\d+'.*?</details>)", m.group(4), re.S)
    pan.setdefault(m.group(1), []).append((m.group(3), blocs))
gs = re.findall(r"<section class='p2' id='(G-\d+)'>(<details.*?</details>)</section>", src, re.S)
pan["G"] = [("Généralités", [b.replace("<details class='ssp'", "<details class='ssp'", 1) for _, b in gs])]
TITRES = {"G": "PARTIE_1 · G · Généralités", "S": "PARTIE_2 · S · Symptômes", "F": "PARTIE_3 · F · Signes et examens", "O": "PARTIE_4 · O · Situations de consultation"}
NUM = {"G": 1, "S": 2, "F": 3, "O": 4}
total = 0; liste = []
for k in "GSFO":
    flat = [(g, b) for g, bl in pan[k] for b in bl]
    n = len(flat); nf = 2 if k == "G" else math.ceil(n / 12); q, r = divmod(n, nf); deb = 0
    for i in range(nf):
        ch = flat[deb:deb + q + (1 if i < r else 0)]; deb += len(ch); total += len(ch)
        corps, cur = "", None
        for g, b in ch:
            if g != cur: corps += f"<h2>{e(g)}</h2>"; cur = g
            corps += b.replace("<details class='ssp'", "<details class='ssp' open" if k == "G" else "<details class='ssp'", 1)
        nom = f"PARTIE_{NUM[k]}.{i+1}"
        lots = re.findall(r"id='lot-(\d+)'", corps)
        open(O + f"DIFFERENTIELS_{nom}.html", "w", encoding="utf-8").write(f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>DIFFERENTIELS_{nom}</title>{style}<style>.page{{display:block}}</style></head><body>
<header><h1>DIFFERENTIELS_{nom}</h1><p>{TITRES[k]} · fichier {i+1}/{nf} · LOT_{lots[0]} → LOT_{lots[-1]} ({len(lots)} SSP) · tableaux à remplir</p></header>
{mode}
<div class="page">{corps}</div></body></html>""")
        liste.append((nom, len(lots), lots[0], lots[-1]))
assert total == 248, total
for x in liste: print(*x)
