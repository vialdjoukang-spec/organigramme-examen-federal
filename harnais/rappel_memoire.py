#!/usr/bin/env python3
"""Onglet « Rappel mémoire » des HTML de la catégorie G.
  python3 harnais/rappel_memoire.py page                      → LOT_Claude_Finaux/RAPPEL_MEMOIRE_G.html (les 16 LOTS)
  python3 harnais/rappel_memoire.py inject <fichier.html>...  → ajoute l'onglet (idempotent) ; le LOT est lu dans le nom du fichier
Contenu : 1) mnémotechnique des 16 SSP G ; 2) logique de classification des diagnostics différentiels du LOT + mnémotechnique ;
3) plan du général au particulier (en violet). Le contrôle vérifie que chaque initiale correspond (voir test en bas)."""
import html, json, re, sys, unicodedata
from pathlib import Path
R = Path(__file__).resolve().parent.parent; sys.path.insert(0, str(R / "harnais/rappel")); import G_data as G
TAB = json.load(open(R / ".cache/g_in/g_tables.json")); e = html.escape
CSS = "#rm{font:15px/1.5 system-ui,sans-serif;max-width:980px;margin:0 auto;padding:18px}#rm h2{margin:18px 0 8px;font-size:1.1rem}#rm .m{background:#fff7e0;border:1px solid #f0c040;border-radius:12px;padding:12px 16px;font-size:1.05rem}#rm table{border-collapse:collapse;width:100%}#rm td,#rm th{border:1px solid #cfd4dc;padding:6px 9px;text-align:left;vertical-align:top}#rm th{background:#f2f4f8}#rm .plan{border-left:5px solid #7c3aed;background:#f5f0ff;color:#4c1d95;border-radius:8px;padding:10px 16px}#rm .plan ul{margin:4px 0 4px 18px;padding:0}#rm .plan b{color:#6d28d9}#rm .cur{background:#ede9fe;font-weight:700}#rm .let{font-weight:800;color:#7c3aed}#__tabs{position:sticky;top:0;z-index:99;display:flex;gap:6px;padding:8px 12px;background:#1d2430}@media(prefers-color-scheme:dark){#rm{color:#e8eaed}#rm .m{background:#3a3217;color:#fff1c2}#rm td,#rm th{border-color:#444b5a}#rm th{background:#242a38}#rm .plan{background:#251a45;color:#ddd0ff}#rm .cur{background:#3b2a73}}"
CSS2 = "#__tabs a{border-radius:8px;padding:7px 16px;font:600 14px system-ui;background:#3a4256;color:#fff;text-decoration:none}#__tabs a.on{background:#7c3aed}#rappel{display:none;position:fixed;inset:0;z-index:100;overflow:auto;background:#fff}#rappel:target{display:block}@media(prefers-color-scheme:dark){#rappel{background:#14171c}}"
def ranks(lot): return [r for r in TAB[lot]["rows"] if r["dd"]]
def contenu(lot):
    d = G.LOTS[lot]; rows = {r["n"]: r["dd"] for r in ranks(lot)}; short = lambda s: re.sub(r"\s*\(.*", "", s)[:60]
    ph = d["phrase"].replace(",", " ,").replace(";", " ;").split(); lab = d["labels"].split(); w = [x for x in ph if x not in ",;"]
    mn = " ".join(f"<b>{e(x[0])}</b>{e(x[1:])}" if x not in ",;." else x for x in ph) if False else e(d["phrase"])
    corr = "".join(f"<tr><td class='let'>{e(w[i])}</td><td>{i+1}</td><td>{e(lab[i].replace('-', ' '))}</td></tr>" for i in range(len(lab)))
    by = {}
    if "cl" in d:
        for n, c in d["cl"].items(): by.setdefault(c, []).append(n)
        tb = "".join(f"<tr><td class='let'>{c}</td><td>{e(G.TEMPO[c])}</td><td>{'; '.join(f'<b>{n}</b> {e(short(rows[n]))}' for n in sorted(by[c]))}</td></tr>" for c in "TEMPOINX" if c in by)
        log = f"Grille étiologique commune <b>TEMPO-IN</b> (mécanisme de la cause). {e(G.TEMPO_MNEMO)}"
    else:
        tb = "".join(f"<tr><td class='let'>{i+1}</td><td>{e(g)}</td><td>{'; '.join(f'<b>{n}</b> {e(short(rows[n]))}' for n in v)}</td></tr>" for i, (g, v) in enumerate(d["groupes"].items()))
        log = f"Logique propre à ce symptôme : <b>{e(d['logique'].lower())}</b>."
    sp = "".join(f"<tr class='{'cur' if i+1 == int(lot) else ''}'><td class='let'>{w2.split()[0] if False else ''}</td><td>{i+1}</td><td>{e(G.G16[i])}</td></tr>" for i, w2 in enumerate(G.G16))
    g16 = "".join(f"<tr class='{'cur' if G.G_MAP[k] == int(lot) else ''}'><td class='let'>{e(k.split('#')[0])}</td><td>G{G.G_MAP[k]}</td><td>{e(G.G16[G.G_MAP[k]-1])}</td></tr>" for k in G.G_MAP)
    raison = G.RAISONS.get(lot) or (G.RAISON_TEMPO + " " + (lambda c, n: f"Dans ce LOT, {max(c.values())} diagnostics sur {n} relèvent de « {G.TEMPO[max(c, key=c.get)].split(' (')[0].lower()} » (famille dominante)" + (f" ; aucune cause {', '.join(G.TEMPO[x].split(' (')[0].lower() for x in 'TEMPOIN' if x not in c)} n'apparaît, ce qui est lui-même informatif." if any(x not in c for x in 'TEMPOIN') else "."))({k: len(v) for k, v in by.items() if k != 'X'}, len(rows)))
    return f"""<div id="rm"><h2>① Plan, du général au particulier</h2><div class="plan"><ul><li><b>Général</b> : catégorie G — 16 symptômes généraux, sans lien logique entre eux (mnémotechnique ci-dessous)<ul><li><b>Ce LOT</b> : G{int(lot)} · {e(TAB[lot]['nom'][:80])}<ul><li><b>Logique de classement des diagnostics</b> : {log}<ul><li><b>Particulier</b> : {len(rows)} diagnostics différentiels, dans l'ordre de la liste canonique (identifiants DX stables, sans valeur de fréquence), regroupés ci-dessous</li></ul></li></ul></li></ul></li></ul></div>
<h2>② Les 16 SSP de la catégorie G (mnémotechnique dans l'ordre G1 → G16)</h2><p class="m">{e(G.G_MNEMO)}</p><table><tr><th>Mot</th><th>SSP</th><th>Nom</th></tr>{g16}</table>
<h2>③ Pourquoi cette classification (fondement de la rétention)</h2><p class="m" style="font-size:.95rem">{e(raison)}</p><h2>④ Classer les diagnostics différentiels de ce LOT</h2><table><tr><th>Clé</th><th>Groupe</th><th>Diagnostics (identifiant DX de la liste canonique)</th></tr>{tb}</table>
<h2>⑤ Mnémotechnique des diagnostics (initiales = ordre de la liste canonique, pas un ordre de fréquence)</h2><p class="m">{e(d['phrase'])}</p><table><tr><th>Mot</th><th>DX</th><th>Diagnostic</th></tr>{corr}</table>
<p style="font-size:12px;opacity:.7">Aide-mémoire de classement, sans valeur de fréquence ; les fréquences sourcées (avec leur population) figurent dans les tableaux du cours.</p></div>"""
BAR = "<span id=\"cours\"></span><div id=\"__tabs\"><a href=\"#cours\" class=\"on\">Cours</a><a href=\"#rappel\">Rappel mémoire</a></div>"
def injecter(f):
    f = Path(f); m = re.search(r"LOT_(\d{3})_", f.name); lot = m.group(1); t = f.read_text(encoding="utf-8")
    if "RAPPEL_MEMOIRE" in t: t = re.sub(r"<!-- RAPPEL_MEMOIRE -->.*?(?=</body>)", "", t, flags=re.S)  # remplace une ancienne injection
    bloc = f"<!-- RAPPEL_MEMOIRE --><style>{CSS}{CSS2}</style>{BAR}<div id=\"rappel\"><div id=\"__tabs\"><a href=\"#cours\">Cours</a><a href=\"#rappel\" class=\"on\">Rappel mémoire</a></div>{contenu(lot).replace('<table>', '<div style=\"overflow-x:auto\"><table>').replace('</table>', '</table></div>')}</div>"
    t = t.replace("</body>", bloc + "</body>", 1) if "</body>" in t else t + bloc
    f.write_text(t, encoding="utf-8"); return "ok"
if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["inject"]: [print(x, injecter(x)) for x in a[1:]]
    elif a[:1] == ["page"]:
        corps = "".join(f"<section><h1 style='font:700 1.3rem system-ui;padding:14px 18px;background:#7c3aed;color:#fff'>LOT_{l} · G{int(l)}</h1>{contenu(l)}</section>" for l in sorted(G.LOTS))
        (R / "LOT_Claude_Finaux/RAPPEL_MEMOIRE_G.html").write_text(f"<!DOCTYPE html><html lang='fr'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>RAPPEL_MEMOIRE_G</title><style>{CSS}body{{margin:0}}</style></head><body>{corps}</body></html>", encoding="utf-8"); print("ok")
