#!/usr/bin/env python3
"""Rédige les fragments Phase A et DX.1 du LOT 051 à partir du seul paquet."""
import os, re, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ROOT = Grokbot/LOT_051
PAQ = {
    "pa": json.load(open(os.path.join(ROOT, "_travail/PA/paquet.json"), encoding="utf-8")),
    "dx1": json.load(open(os.path.join(ROOT, "_travail/DX.1/paquet.json"), encoding="utf-8")),
}
TXT = {k: {p["id"]: p["texte"] for p in v["passages"]} for k, v in PAQ.items()}

NUM = re.compile(r"(?<![\w])(\d+(?:[.,’' ]\d+)*(?:[.,]\d+)?)(?![\w])")

def nombres(s):
    out = set()
    for n in NUM.findall(s):
        n = re.sub(r"[’' ]", "", n).replace(",", ".")
        out.add(re.sub(r"^0+(?=\d)", "", n))
    return out

def mots(s):
    t = re.sub(r"<[^>]+>", " ", s)
    t = re.sub(r"\s+", " ", html.unescape(t)).strip()
    return t, t.split()

def cite(ids):
    return "".join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)

ERREURS = []

def S(phrase, ids, paquet="dx1", borne=True):
    """Phrase verbale. La citation se place avant le point final, pour que le contrôle découpe les phrases."""
    phrase = phrase.strip()
    fin = "."
    if phrase.endswith((".", "?", "!")):
        fin = phrase[-1]
        phrase = phrase[:-1].rstrip()
    t, w = mots(phrase)
    if borne and not (12 <= len(w) <= 28):
        ERREURS.append(f"LONGUEUR {len(w)} :: {t}")
    if ids:
        src = " ".join(TXT[paquet].get(i, "") for i in ids)
        manq = nombres(t) - nombres(src)
        if manq:
            ERREURS.append(f"NOMBRE {sorted(manq)} absent de {ids} :: {t}")
    return phrase + cite(ids) + fin

def P(*phrases):
    return '<div class="p">' + " ".join(phrases) + "</div>\n"

def W(prefix, n, k, label, inner):
    i = f"{prefix}-p{n}-f{k}"
    return (f'<button class="w" popovertarget="{i}">{label}</button>\n'
            f'<div id="{i}" popover class="fenetre">{inner}</div>\n')

def T(rows):
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="t"><table>{body}</table></div>\n'

def H(txt):
    return f"<h4><em>{txt}</em></h4>\n"
