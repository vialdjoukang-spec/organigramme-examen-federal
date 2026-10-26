#!/usr/bin/env python3
"""Génère LOT_Claude_Finaux/DIFFERENTIELS_PAR_LOT.html : 248 SSP/LOT, onglets G·S·F·O, tableaux vides à remplir."""
import csv, html, re, collections
D = "LOT_Claude_Finaux/"
rows = list(csv.DictReader(open(D + "CATALOGUE_248.csv", encoding="utf-8")))
e = html.escape
S1 = {"Œil": [1, 2, 6, 17, 20, 22, 23], "ORL, bouche et voix": [3, 5, 7, 8, 9, 10, 12, 14, 15, 18, 19], "Tête, face et cou": [4, 11, 13, 16, 21]}
GROUPES = {
 "S": [("Œil", "S1", S1["Œil"]), ("ORL, bouche et voix", "S1", S1["ORL, bouche et voix"]), ("Tête, face et cou", "S1", S1["Tête, face et cou"]),
       ("Thorax, respiration et sein", "S2", None), ("Abdomen et digestif", "S3", None), ("Uro-génital", "S4", None),
       ("Dos et appareil locomoteur", "S5", None), ("Peau et muqueuses", "S6", None), ("Neurologie", "S7", None),
       ("Traumatismes et lésions", "S8", None), ("Psychiatrie et comportement", "S9", None)],
 "F": [("Examen clinique et signes", "F1", None), ("Biologie et examens complémentaires", "F2", None)],
 "O": [("Périnatalité et grossesse", "O1", None), ("Enfant et adolescent", "O2", None), ("Personne âgée", "O3", None),
       ("Prévention et dépistage", "O4", None), ("Soins et accompagnement", "O5", None), ("Contexte psychosocial et travail", "O6", None),
       ("Situations particulières", "O7", None)],
}
NOMS = {"G": "G · Généralités", "S": "S · Symptômes", "F": "F · Signes et examens", "O": "O · Situations de consultation"}
def titre(r): return f"LOT_{r['lot']}_{r['code'].replace('.', '.')}_{r['ssp_profiles_2023_fr_en'].split('|')[0].strip()}"
def table(r):
    h = ("<table class='dd' id='t-%s'><thead><tr><th>Diagnostic différentiel<small>ordre décroissant de prévalence</small></th>"
         "<th>Prévalence (%%)<small>Suisse ou Europe, comparable d’un diagnostic à l’autre</small></th>"
         "<th>Source(s)<small>liens cliquables</small></th></tr></thead><tbody>" % r["lot"])
    for i in range(1, 16):
        cls = "top" if i <= 10 else "plus"
        h += f"<tr class='{cls}'><td data-lot='{r['lot']}' data-row='{i}' data-col='dd'></td><td data-lot='{r['lot']}' data-row='{i}' data-col='prev'></td><td data-lot='{r['lot']}' data-row='{i}' data-col='src'></td></tr>"
    return h + "</tbody></table><p class='note'>Lignes 1–10 : les dix plus fréquents. Lignes 11–15 (vert) : diagnostics à connaître absolument pour l’examen, <b>uniquement</b> s’ils ne figurent pas déjà dans les dix premiers.</p>"
def ssp(r, ouvert=False):
    en = r["ssp_profiles_2023_fr_en"].split("|")[1].strip() if "|" in r["ssp_profiles_2023_fr_en"] else ""
    return (f"<details class='ssp' id='lot-{r['lot']}'{' open' if ouvert else ''}><summary><span class='lot'>LOT_{r['lot']}</span>"
            f"<span class='code'>{r['code']}</span><span class='nom'>{e(r['ssp_profiles_2023_fr_en'].split('|')[0].strip())}</span></summary>"
            f"<div class='corps'><p class='en'>{e(en)}</p>{table(r)}</div></details>")
by = collections.defaultdict(list)
for r in rows: by[r["code"][0]].append(r)
nav1 = "".join(f"<button class='t1' data-t='{k}'>{NOMS[k].split(' · ')[0]}<span>{NOMS[k].split(' · ')[1]} · {len(by[k])}</span></button>" for k in "GSFO")
pages = ""
# G : un sous-onglet par SSP
sub = "".join(f"<button class='t2' data-p='G-{r['lot']}'>{e(titre(r))}</button>" for r in by["G"])
pan = "".join(f"<section class='p2' id='G-{r['lot']}'>{ssp(r, True)}</section>" for r in by["G"])
pages += f"<div class='page' id='T-G'><nav class='sub gdense'>{sub}</nav>{pan}</div>"
for k in "SFO":
    sub, pan = "", ""
    for j, (nom, pre, only) in enumerate(GROUPES[k]):
        lst = [r for r in by[k] if r["code"].split(".")[0] == pre and (only is None or int(r["code"].split(".")[1]) in only)]
        sub += f"<button class='t2' data-p='{k}-{j}'>{e(nom)}<span>{len(lst)}</span></button>"
        pan += f"<section class='p2' id='{k}-{j}'><h2>{e(nom)}</h2>" + "".join(ssp(r) for r in lst) + "</section>"
    pages += f"<div class='page' id='T-{k}'><nav class='sub'>{sub}</nav>{pan}</div>"
assert sum(len(v) for v in by.values()) == 248
open(D + "DIFFERENTIELS_PAR_LOT.html", "w", encoding="utf-8").write(f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>DIFFERENTIELS_PAR_LOT</title>
<style>
:root{{--bg:#fafaf8;--fg:#1d2430;--mut:#6b7280;--line:#e5e7eb;--red:#c00000;--green:#1f7a3a;--card:#fff;--acc:#1d2430}}
@media(prefers-color-scheme:dark){{:root{{--bg:#14171c;--fg:#e8eaed;--mut:#9aa3af;--line:#2a2f38;--card:#1b1f26;--acc:#e8eaed;--red:#ff5a5a;--green:#58c27d}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif}}
header{{padding:28px clamp(16px,4vw,48px) 8px}}h1{{margin:0;font-size:1.35rem;letter-spacing:.02em}}header p{{margin:4px 0 0;color:var(--mut);font-size:.9rem}}
.mode{{padding:8px clamp(16px,4vw,48px)}}.mode>details{{background:var(--card);border:1px solid var(--red);border-radius:12px}}.mode summary{{font-weight:600;padding:10px 16px}}.m{{padding:0 20px 14px;font-size:.88rem}}.m li{{margin:6px 0}}.mode>.interdit{{margin:0 0 8px}}.interdit{{border-left:4px solid var(--red);padding:8px 12px;background:rgba(192,0,0,.07);font-weight:600}}code{{font:.8rem ui-monospace,monospace}}
.n1{{display:flex;gap:10px;padding:16px clamp(16px,4vw,48px);position:sticky;top:0;background:var(--bg);z-index:5;border-bottom:1px solid var(--line)}}
.t1{{flex:1;max-width:220px;border:1px solid var(--line);background:var(--card);color:var(--fg);border-radius:12px;padding:10px 14px;font:600 1.4rem system-ui;cursor:pointer;text-align:left}}
.t1 span{{display:block;font:400 .72rem system-ui;color:var(--mut);margin-top:2px}}.t1.on{{background:var(--acc);color:var(--bg);border-color:var(--acc)}}.t1.on span{{color:inherit;opacity:.8}}
.page{{display:none;padding:16px clamp(16px,4vw,48px) 64px}}.page.on{{display:block}}
.sub{{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:24px}}.sub.gdense{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr))}}
.t2{{border:1px solid var(--line);background:var(--card);color:var(--fg);border-radius:10px;padding:8px 12px;font:500 .82rem/1.3 system-ui;cursor:pointer;text-align:left}}
.t2 span{{margin-left:8px;color:var(--mut);font-size:.75rem}}.t2.on{{border-color:var(--acc);box-shadow:inset 0 0 0 1px var(--acc)}}
.p2{{display:none}}.p2.on{{display:block}}h2{{font-size:1.05rem;margin:0 0 14px;color:var(--mut);font-weight:600}}
details.ssp{{background:var(--card);border:1px solid var(--line);border-radius:12px;margin:0 0 10px}}
summary{{display:flex;gap:12px;align-items:baseline;padding:12px 16px;cursor:pointer;list-style:none}}summary::-webkit-details-marker{{display:none}}
summary::before{{content:"▸";color:var(--mut)}}details[open]>summary::before{{content:"▾"}}
.lot{{font:600 .78rem ui-monospace,monospace;color:var(--mut)}}.code{{font:600 .78rem ui-monospace,monospace}}.nom{{font-weight:600}}
.corps{{padding:0 16px 16px}}.en{{margin:0 0 12px;color:var(--mut);font-size:.82rem}}
table.dd{{width:100%;border-collapse:collapse;border:3px solid var(--red);table-layout:fixed}}
.dd th,.dd td{{border:2px solid var(--red);padding:8px 10px;vertical-align:top;word-break:break-word}}
.dd th{{text-align:left;font-size:.82rem;background:rgba(192,0,0,.07)}}.dd th small{{display:block;font-weight:400;color:var(--mut);font-size:.7rem}}
.dd th:nth-child(1){{width:42%}}.dd th:nth-child(2){{width:22%}}.dd td{{height:2.2rem}}
.dd tr.plus td{{border-color:var(--green);background:rgba(31,122,58,.07)}}
.note{{font-size:.75rem;color:var(--mut);margin:8px 0 0}}.note b{{color:var(--green)}}
@media(max-width:640px){{.t1{{padding:8px}}.dd th:nth-child(1){{width:40%}}}}
</style></head><body>
<header><h1>DIFFERENTIELS_PAR_LOT</h1><p>Catalogue = 248 SSP (PROFILES 2023) · un LOT par SSP · tableaux à remplir</p></header>
<section class="mode"><p class="interdit">INTERDICTION FORMELLE D’INVENTER. Aucun diagnostic, aucun pourcentage, aucune source, aucun lien, aucune date ne s’écrit de mémoire, par déduction ou par estimation. Une valeur non lue dans une source ouverte reste vide ou porte « À vérifier ». Une URL n’est jamais déduite ni reconstruite : elle est copiée de la page réellement consultée.</p><details><summary>Instructions de remplissage — à lire avant toute saisie</summary><div class="m">

<ol>
<li><b>Remplir uniquement les cellules vides.</b> Ne modifier ni les titres, ni les numéros de LOT, ni la structure, ni l’ordre des SSP. Rendre le fichier complet (248 LOTS).</li>
<li><b>Colonne 1 — Diagnostic différentiel</b> : les 10 diagnostics les plus fréquents pour ce SSP, par <b>prévalence décroissante</b> (lignes 1 à 10). Noms exacts, en français.</li>
<li><b>Lignes 11 à 15 (vert)</b> : <b>seulement</b> les diagnostics à connaître absolument pour l’examen fédéral qui ne figurent <b>pas</b> dans les dix premiers. Aucun doublon ; laisser vide si rien à ajouter.</li>
<li><b>Colonne 2 — Prévalence (%)</b> : chiffre sourcé, <b>Suisse</b> en priorité, sinon <b>Europe</b>. Indiquer entre parenthèses : CH ou EU, année, population (ex. « 12 % (CH, 2022, médecine de premier recours) »). Les dix valeurs d’un même SSP doivent être <b>comparables</b> (même population, même définition). Pas de chiffre comparable disponible : « non quantifiée », jamais une estimation.</li>
<li><b>Colonne 3 — Source(s)</b> : un ou plusieurs liens <b>cliquables</b> (<code>&lt;a href="…"&gt;titre, année&lt;/a&gt;</code>) vers la page ou le document <b>réellement lu</b>, avec la date de lecture (jj.mm.aaaa). Ordre de priorité : Suisse (OFSP, OFS, Obsan, sociétés suisses, HUG, Unisanté), puis Europe, puis international. Sources autorisées : <code>harnais/SOURCES_AUTORISEES.md</code>.</li>
<li>Source introuvable ou illisible pour une ligne : écrire « À vérifier » dans la cellule concernée ; ne rien compléter d’autre.</li>
<li>Une ligne = un diagnostic = un chiffre = au moins une source qui contient ce chiffre.</li></ol></div></details></section>
<nav class="n1">{nav1}</nav>
{pages}
<script>
const $=(s,r=document)=>[...r.querySelectorAll(s)];
function show(t,p){{ $('.t1').forEach(b=>b.classList.toggle('on',b.dataset.t===t)); $('.page').forEach(x=>x.classList.toggle('on',x.id==='T-'+t));
 const pg=document.getElementById('T-'+t); p=p||pg.querySelector('.t2').dataset.p;
 $('.t2',pg).forEach(b=>b.classList.toggle('on',b.dataset.p===p)); $('.p2',pg).forEach(x=>x.classList.toggle('on',x.id===p)); history.replaceState(null,'','#'+t+'/'+p); scrollTo(0,0); }}
$('.t1').forEach(b=>b.onclick=()=>show(b.dataset.t));
$('.t2').forEach(b=>b.onclick=()=>show(b.closest('.page').id.slice(2),b.dataset.p));
const h=location.hash.slice(1).split('/'); show(h[0]&&document.getElementById('T-'+h[0])?h[0]:'G',h[1]);
</script></body></html>""")
