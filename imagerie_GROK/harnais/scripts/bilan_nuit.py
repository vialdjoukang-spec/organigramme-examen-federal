#!/usr/bin/env python3
"""Bilan HTML de la nuit, Python stdlib seulement.
Lit les catalogues, les manifestes, les journaux et TOKENS.md.
Écrit progression/BILAN_NUIT_20261114.html
"""
import html, json, os, re
from datetime import datetime
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GROK = os.path.dirname(ROOT)
OUT = os.path.join(ROOT, "progression", "BILAN_NUIT_20261114.html")
TOKENS = os.path.join(ROOT, "progression", "TOKENS.md")

def cells(row):
    return [html.unescape(re.sub(r"<[^>]+>", " ", c)).strip() for c in re.findall(r"<td[^>]*>(.*?)</td>", row, re.S)]

def catalogue():
    items = []
    clic = open(os.path.join(GROK, "IMAGERIE_CLICHES.html"), encoding="utf-8").read()
    for row in re.findall(r"<tr[^>]*>.*?</tr>", clic, re.S):
        c = cells(row)
        if len(c) < 6 or not re.fullmatch(r"IMG-\d{3}", c[0]):
            continue
        items.append({"id": c[0], "bloc": "Imagerie", "titre": c[3], "cliche": c[5], "niveau": c[4]})
    exp = open(os.path.join(GROK, "EXPLORATIONS_FONCTIONNELLES.html"), encoding="utf-8").read()
    for row in re.findall(r"<tr[^>]*>.*?</tr>", exp, re.S):
        c = cells(row)
        if not c:
            continue
        if re.fullmatch(r"EXP-\d{3}", c[0]) and len(c) >= 4:
            items.append({"id": c[0], "bloc": "Exploration", "titre": c[3], "cliche": c[4] if len(c) > 4 else "", "niveau": c[1]})
        elif re.fullmatch(r"FTE-\d{2}", c[0]) and len(c) >= 4:
            items.append({"id": c[0], "bloc": "FTE", "titre": c[3], "cliche": c[4] if len(c) > 4 else "", "niveau": c[1]})
    return items

def _lire_dossier(man, out):
    if not os.path.isdir(man):
        return
    for name in sorted(os.listdir(man)):
        if not name.endswith(".json") or name == "SCHEMA.json" or name.startswith("TEST-"):
            continue
        path = os.path.join(man, name)
        try:
            m = json.load(open(path, encoding="utf-8"))
        except Exception as e:
            out[name[:-5]] = {"statut": "erreur", "ecart": f"JSON illisible : {e}"}
            continue
        mid = m.get("id") or name[:-5]
        ecart = ""
        if m.get("statut") == "partiel":
            ecart = m.get("pair_match") or " ; ".join(m.get("a_verifier") or [])
        elif m.get("statut") == "introuvable":
            ecart = " ; ".join(m.get("queries") or [])
        elif m.get("a_verifier"):
            ecart = " ; ".join(m["a_verifier"])
        out[mid] = {"statut": m.get("statut") or "?", "ecart": ecart, "manifeste": path}

def manifests():
    """Manifestes du coordinateur, puis des lots, puis des audits (l'audit remplace le lot)."""
    out = {}
    _lire_dossier(os.path.join(ROOT, "manifest"), out)
    for i in range(1, 5):
        _lire_dossier(f"/tmp/imagerie-lot{i}/manifest", out)
    for i in range(1, 5):
        _lire_dossier(f"/tmp/imagerie-audit{i}/manifest", out)
    return out

def glob_tokens():
    paths = []
    for folder in [os.path.join(ROOT, "progression")] + [
        f"/tmp/imagerie-{kind}{i}/progression" for kind in ("lot", "audit") for i in range(1, 5)
    ]:
        if not os.path.isdir(folder):
            continue
        for name in sorted(os.listdir(folder)):
            if name.startswith("TOKENS_") and name.endswith(".md"):
                paths.append(os.path.join(folder, name))
    return paths

def journaux():
    chunks = []
    folders = [os.path.join(ROOT, "memory")]
    folders += [f"/tmp/imagerie-{kind}{i}/memory" for kind in ("lot", "audit") for i in range(1, 5)]
    seen = set()
    for mem in folders:
        if not os.path.isdir(mem):
            continue
        for name in sorted(os.listdir(mem)):
            if not name.startswith("journal_") or not name.endswith(".md"):
                continue
            path = os.path.join(mem, name)
            key = (name, open(path, encoding="utf-8").read())
            if key in seen:
                continue
            seen.add(key)
            chunks.append(f"<h3>{html.escape(mem)} / {html.escape(name)}</h3><pre>{html.escape(key[1])}</pre>")
    return "\n".join(chunks)

def main():
    items = catalogue()
    mans = manifests()
    counts = {"complet": 0, "partiel": 0, "introuvable": 0, "en recherche": 0, "erreur": 0}
    rows = []
    for it in items:
        m = mans.get(it["id"])
        st = m["statut"] if m else "en recherche"
        if st not in counts:
            counts[st] = 0
        counts[st] += 1
        ecart = m["ecart"] if m else ""
        rows.append(
            f"<tr class='{html.escape(st.replace(' ', '-'))}'><td>{html.escape(it['id'])}</td>"
            f"<td>{html.escape(it['bloc'])}</td><td>{html.escape(it['titre'])}</td>"
            f"<td>{html.escape(st)}</td><td>{html.escape(ecart)}</td></tr>"
        )
    now = datetime.now(ZoneInfo("Europe/Zurich")).strftime("%d.%m.%Y %H:%M Europe/Zurich")
    token_parts = []
    if os.path.isfile(TOKENS):
        token_parts.append(open(TOKENS, encoding="utf-8").read())
    extra = sorted(glob_tokens())
    for path in extra:
        token_parts.append(open(path, encoding="utf-8").read())
    tokens = "\n\n".join(token_parts) if token_parts else "TOKENS.md absent."
    total = len(items) or 1
    def bar(k, col):
        return f"<i style='width:{100 * counts.get(k, 0) / total:.2f}%;background:{col}'></i>"
    page = f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><title>Bilan de la nuit · 14.11.2026</title>
<style>
body{{margin:0;background:#fff3b0;color:#1c1400;font:15px/1.45 system-ui,sans-serif}}
header{{background:#f5c400;padding:16px 20px;border-bottom:3px solid #1c1400}}
h1{{margin:0 0 6px;font-size:22px}} main{{padding:16px 20px 40px}}
.bar{{display:flex;height:14px;background:#fff;border:1px solid #1c1400;border-radius:7px;overflow:hidden;margin:8px 0}}
.bar i{{display:block;height:100%}}
table{{width:100%;border-collapse:collapse;background:#fffdf2}}
th,td{{border-bottom:1px solid #e0c96a;padding:5px 7px;text-align:left;vertical-align:top}}
th{{position:sticky;top:0;background:#ffe56a}}
tr.complet{{background:#e5f8df}} tr.partiel{{background:#fff3b0}} tr.introuvable{{background:#ffd0c8}}
tr.erreur{{background:#ffd0f0}} tr.en-recherche{{background:#f4f1e4;color:#5c5340}}
pre{{white-space:pre-wrap;background:#fffdf2;padding:10px;border:1px solid #e0c96a}}
.note{{background:#fff;border-left:6px solid #f5c400;padding:8px 12px}}
</style></head><body>
<header><h1>Bilan de la nuit du 14 novembre 2026</h1>
<p>Généré le {html.escape(now)} par bilan_nuit.py (stdlib), à partir des catalogues, des manifestes et des journaux. Jaune = état attendu tant que la nuit n'est pas close.</p>
<p><b>{counts.get('complet',0)}</b> complets · <b>{counts.get('partiel',0)}</b> partiels · <b>{counts.get('introuvable',0)}</b> introuvables · <b>{counts.get('en recherche',0)}</b> en recherche · <b>{counts.get('erreur',0)}</b> erreurs · sur {len(items)} éléments.</p>
<div class="bar">{bar('complet','#2fbf62')}{bar('partiel','#e0b000')}{bar('introuvable','#d04545')}{bar('erreur','#c04fb0')}</div>
</header>
<main>
<p class="note">Un complet n'est compté que s'il a un manifeste. L'absence de manifeste reste « en recherche ». Ce décompte ne juge pas la justesse anatomique des contours.</p>
<h2>Éléments</h2>
<table><thead><tr><th>Id</th><th>Bloc</th><th>Titre</th><th>Statut</th><th>Écart, requêtes ou réserve</th></tr></thead>
<tbody>{''.join(rows)}</tbody></table>
<h2>Audit des jetons</h2>
<pre>{html.escape(tokens)}</pre>
<h2>Journaux</h2>
{journaux()}
</main></body></html>"""
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(page)
    print(OUT, counts)

if __name__ == "__main__":
    main()
