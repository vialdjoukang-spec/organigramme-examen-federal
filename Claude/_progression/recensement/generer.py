#!/usr/bin/env python3
"""Fabrique RECENSEMENT_TOPOSYSTEMIQUE.html à partir de recensement.json.

Usage : python3 generer.py   (aucune dépendance hors bibliothèque standard)
On modifie le JSON, puis on relance ce script : la page se régénère gratuitement.
"""
import html, json, os, re
from collections import Counter, OrderedDict

ICI = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(ICI, "recensement.json"), encoding="utf-8"))
SORTIE = os.path.join(ICI, "RECENSEMENT_TOPOSYSTEMIQUE.html")

E = lambda s: html.escape(str(s), quote=True)
SIG = D["sigles"]
_motif = re.compile(r"(?<![\w])(" + "|".join(re.escape(k) for k in sorted(SIG, key=len, reverse=True)) + r")(?![\w])")


def T(texte):
    """Échappe le texte puis place chaque sigle dans <abbr title>."""
    morceaux, pos = [], 0
    for m in _motif.finditer(texte):
        morceaux.append(E(texte[pos:m.start()]))
        morceaux.append(f'<abbr title="{E(SIG[m.group(1)])}">{E(m.group(1))}</abbr>')
        pos = m.end()
    morceaux.append(E(texte[pos:]))
    return "".join(morceaux)


REG = OrderedDict((r["code"], r) for r in D["regions"])
LET = OrderedDict((l["code"], l) for l in D["lettres"])
TI = OrderedDict((t["code"], t) for t in D["technologies_imagerie"])
TE = OrderedDict((t["code"], t) for t in D["technologies_explorations"])
EXI = D["meta"]["existant"]


def couverture(existants):
    """Associe chaque couple région|système aux titres existants qui le traitent en partie."""
    c = {}
    for e in existants:
        for cle in e["couvre"]:
            c.setdefault(cle, []).append(e["titre"])
    return c


def titres_existants(row, corr):
    out = list(corr.get(f'{row["region"]}|{row["systeme"]}', []))
    out += [t for t in corr.get(f'{row["region"]}|*', []) if t not in out]
    return out


def calculs(lignes, fiches, cle_tech, existants, n_exist):
    corr = couverture(existants)
    systemes = OrderedDict()
    for r in lignes:
        systemes.setdefault((r["region"], r["systeme"]), []).append(r)
    dxM = sum(r["niveau"] == "M" for r in lignes)
    ftM = sum(f["niveau"] == "M" for f in fiches)
    rais_min, rais_cible = len({r["region"] for r in lignes}), len(systemes)
    mini = dxM + ftM + rais_min
    cible = len(lignes) + len(fiches) + rais_cible
    deja = sorted({f["existant"] for f in fiches if f["existant"]})
    partiel = sum(1 for r in lignes if titres_existants(r, corr))
    img_min = dxM + ftM
    img_cible = sum(len(r[cle_tech]) for r in lignes) + 2 * len(fiches)
    par_region = OrderedDict()
    for code in REG:
        rr = [r for r in lignes if r["region"] == code]
        if rr:
            par_region[code] = {"M": sum(r["niveau"] == "M" for r in rr), "T": len(rr),
                                "sys": len({r["systeme"] for r in rr}),
                                "part": sum(1 for r in rr if titres_existants(r, corr))}
    par_tech = Counter(t["tech"] for r in lignes for t in {x["tech"]: x for x in r[cle_tech]}.values())
    par_tech_M = Counter(t["tech"] for r in lignes if r["niveau"] == "M" for t in {x["tech"]: x for x in r[cle_tech]}.values())
    ft_tech = Counter(f["tech"] for f in fiches)
    par_lettre = Counter(r["lettre"] for r in lignes)
    par_lettre_M = Counter(r["lettre"] for r in lignes if r["niveau"] == "M")
    return dict(corr=corr, systemes=systemes, dxM=dxM, dxT=len(lignes), ftM=ftM, ftT=len(fiches),
                rais_min=rais_min, rais_cible=rais_cible, mini=mini, cible=cible, deja=deja, partiel=partiel,
                img_min=img_min, img_cible=img_cible, par_region=par_region, par_tech=par_tech,
                par_tech_M=par_tech_M, ft_tech=ft_tech, par_lettre=par_lettre, par_lettre_M=par_lettre_M,
                n_exist=n_exist, ecart_min=mini - n_exist, ecart_cible=cible - n_exist,
                a_creer_min=mini - len({f["existant"] for f in fiches if f["existant"] and f["niveau"] == "M"}),
                a_creer_cible=cible - len(deja))


CI = calculs(D["imagerie"], D["fiches_technique_imagerie"], "techniques", D["existants"]["imagerie"], EXI["imagerie"])
CE = calculs(D["explorations"], D["fiches_technique_explorations"], "explorations", D["existants"]["explorations"], EXI["explorations"])


def pastille_tech(code, tabl, detail=""):
    t = tabl[code]
    titre = t["nom"] + (" — " + t["physique"] if "physique" in t else "")
    det = f' <span class="det">{T(detail)}</span>' if detail else ""
    return f'<span class="tp"><span class="pill" style="--c:{t["couleur"]}" title="{E(titre)}">{E(t["nom"] if code not in ("TDM", "IRM") else code)}</span>{det}</span>'


def pastille_lettre(code):
    l = LET[code]
    return f'<abbr class="let" style="--c:{l["couleur"]}" title="{E(l["nom"])}">{E(l["lettre"])}</abbr>'


def niveau(n):
    return '<span class="niv m" title="Minimum indispensable pour l\'examen fédéral">min</span>' if n == "M" else \
           '<span class="niv c" title="Cible complète">cible</span>'


def tableau_lignes(lignes, C, cle_tech, tabl, colonne_fonction):
    out = []
    for code, reg in REG.items():
        rr = [r for r in lignes if r["region"] == code]
        if not rr:
            continue
        ncol = 7 if colonne_fonction else 6
        out.append(f'<tbody class="grp" data-r="{code}"><tr class="band"><th colspan="{ncol}" style="--c:{reg["couleur"]}">'
                   f'{E(reg["nom"])} <span class="cnt" data-cnt="{code}">{len(rr)}</span> fiches affichées</th></tr>')
        for r in rr:
            ex = titres_existants(r, C["corr"])
            ex_html = (f'<details class="exd"><summary class="ok">Partiel : {len(ex)} fiche{"s" if len(ex) > 1 else ""} de technique</summary>'
                       + "<br>".join(E(t) for t in ex) + "</details>") if ex else '<span class="non">Aucune fiche existante</span>'
            techs = " ".join(pastille_tech(t["tech"], tabl, t["detail"]) for t in r[cle_tech])
            codes = " ".join(sorted({t["tech"] for t in r[cle_tech]}))
            fct = f'<td data-label="Fonction explorée">{T(r["fonction"])}</td>' if colonne_fonction else ""
            texte = r.get("signe") or r.get("anomalie")
            cherche = E((r["diagnostic"] + " " + r["systeme"] + " " + texte + " " + " ".join(t["detail"] for t in r[cle_tech])).lower())
            out.append(
                f'<tr class="row" data-r="{code}" data-t="{codes}" data-l="{r["lettre"]}" data-n="{r["niveau"]}" data-s="{cherche}">'
                f'<td data-label="Système">{T(r["systeme"])}</td>{fct}'
                f'<td data-label="Type">{pastille_lettre(r["lettre"])}</td>'
                f'<td data-label="Diagnostic"><strong>{T(r["diagnostic"])}</strong> {niveau(r["niveau"])}</td>'
                f'<td data-label="Technique(s)">{techs}</td>'
                f'<td data-label="{"Signe clé" if not colonne_fonction else "Anomalie clé"}">{T(texte)}</td>'
                f'<td data-label="Existant" class="exi">{ex_html}</td></tr>')
        out.append("</tbody>")
    return "\n".join(out)


def tableau_fiches_tech(fiches, tabl):
    rows = []
    for f in fiches:
        ex = f'<span class="ok">Déjà couverte : {E(f["existant"])}</span>' if f["existant"] else '<span class="non">À créer</span>'
        rows.append(f'<tr><td data-label="Technologie">{pastille_tech(f["tech"], tabl)}</td>'
                    f'<td data-label="Fiche"><strong>{T(f["titre"])}</strong> {niveau(f["niveau"])}</td>'
                    f'<td data-label="Ce que la fiche enseigne">{T(f["phrase"])}</td>'
                    f'<td data-label="Existant" class="exi">{ex}</td></tr>')
    return ('<div class="tw"><table class="t"><thead><tr><th>Technologie</th><th>Fiche</th><th>Ce que la fiche enseigne</th>'
            '<th>Existant</th></tr></thead><tbody>' + "".join(rows) + "</tbody></table></div>")


def compteurs(C, lignes, tabl, nom_tech):
    lr = "".join(f'<tr><td data-label="Région"><span class="dot" style="--c:{REG[c]["couleur"]}"></span>{E(REG[c]["nom"])}</td>'
                 f'<td data-label="Systèmes">{v["sys"]}</td><td data-label="Minimum">{v["M"]}</td><td data-label="Cible">{v["T"]}</td>'
                 f'<td data-label="Touchées par l\'existant">{v["part"]}</td></tr>' for c, v in C["par_region"].items())
    lr += (f'<tr class="tot"><td data-label="Région">Total diagnostics</td><td data-label="Systèmes">{len(C["systemes"])}</td>'
           f'<td data-label="Minimum">{C["dxM"]}</td><td data-label="Cible">{C["dxT"]}</td><td data-label="Touchées par l\'existant">{C["partiel"]}</td></tr>')
    lt = "".join(f'<tr><td data-label="{E(nom_tech)}">{pastille_tech(c, tabl)}</td><td data-label="Diagnostics (min)">{C["par_tech_M"].get(c, 0)}</td>'
                 f'<td data-label="Diagnostics (cible)">{C["par_tech"].get(c, 0)}</td><td data-label="Fiches de technique">{C["ft_tech"].get(c, 0)}</td></tr>'
                 for c in tabl)
    ll = "".join(f'<tr><td data-label="Type">{pastille_lettre(c)} {E(LET[c]["nom"])}</td><td data-label="Minimum">{C["par_lettre_M"].get(c, 0)}</td>'
                 f'<td data-label="Cible">{C["par_lettre"].get(c, 0)}</td></tr>' for c in LET)
    sy = "".join(f'<tr><td data-label="Région"><span class="dot" style="--c:{REG[r]["couleur"]}"></span>{E(REG[r]["nom"])}</td><td data-label="Système">{T(s)}</td>'
                 f'<td data-label="Minimum">{sum(x["niveau"] == "M" for x in v)}</td><td data-label="Cible">{len(v)}</td>'
                 f'<td data-label="Existant">{"oui (partiel)" if titres_existants(v[0], C["corr"]) else "non"}</td></tr>'
                 for (r, s), v in C["systemes"].items())
    return f'''
<div class="grid3">
 <div class="card"><h4>Par région</h4><div class="tw"><table class="t s"><thead><tr><th>Région</th><th>Systèmes</th><th>Minimum</th><th>Cible</th><th><abbr title="Diagnostics dont la région ou le système apparaît déjà dans une fiche technique existante">Touchées</abbr></th></tr></thead><tbody>{lr}</tbody></table></div></div>
 <div class="card"><h4>Par technologie</h4><p class="note">Un diagnostic compte dans chaque technologie qu'il mobilise ; la somme dépasse donc le total.</p><div class="tw"><table class="t s"><thead><tr><th>{E(nom_tech)}</th><th>Diag. min</th><th>Diag. cible</th><th>Fiches techn.</th></tr></thead><tbody>{lt}</tbody></table></div></div>
 <div class="card"><h4>Par type de lésion (<abbr title="Vasculaire, Infectieux, Tumoral, Dégénératif, Iatrogène, Traumatique, Congénital, Auto-immun, Fonctionnel">VITE DIT CAFé</abbr>)</h4><div class="tw"><table class="t s"><thead><tr><th>Type</th><th>Minimum</th><th>Cible</th></tr></thead><tbody>{ll}</tbody></table></div></div>
</div>
<details class="card"><summary>Détail par système ({len(C["systemes"])} systèmes)</summary><div class="tw"><table class="t s"><thead><tr><th>Région</th><th>Système</th><th>Minimum</th><th>Cible</th><th>Existant</th></tr></thead><tbody>{sy}</tbody></table></div></details>'''


def filtres(prefixe, tabl):
    regs = "".join(f'<option value="{c}">{E(r["nom"])}</option>' for c, r in REG.items())
    tch = "".join(f'<button type="button" class="chip" data-f="t" data-v="{c}" style="--c:{t["couleur"]}" aria-pressed="false">{E(t["nom"])} <b data-ct="{c}"></b></button>' for c, t in tabl.items())
    lts = "".join(f'<button type="button" class="chip" data-f="l" data-v="{c}" style="--c:{l["couleur"]}" aria-pressed="false" title="{E(l["nom"])}">{E(l["lettre"])} <small>{E(l["nom"].split(" ")[0])}</small> <b data-cl="{c}"></b></button>' for c, l in LET.items())
    return f'''
<div class="filt" id="f-{prefixe}" data-cible="tb-{prefixe}">
 <div class="frow"><label>Région <select data-f="r"><option value="">Toutes</option>{regs}</select></label>
 <label>Niveau <select data-f="n"><option value="">Minimum et cible</option><option value="M">Minimum seulement</option><option value="C">Complément de la cible</option></select></label>
 <label class="grow">Recherche <input type="search" data-f="q" placeholder="ex. : diffusion, Doppler, fracture"></label>
 <button type="button" class="raz">Tout afficher</button></div>
 <div class="frow chips"><span class="lab">Technologie :</span>{tch}</div>
 <div class="frow chips"><span class="lab">Type de lésion :</span>{lts}</div>
 <p class="live" aria-live="polite"><strong data-vis>0</strong> fiches diagnostiques affichées sur <span data-tot>0</span>, dont <strong data-visM>0</strong> du minimum.</p>
</div>'''


def raisonnement(C, mot):
    par = OrderedDict()
    for (r, s) in C["systemes"]:
        par.setdefault(r, []).append(s)
    li = "".join(f'<li><span class="dot" style="--c:{REG[r]["couleur"]}"></span><strong>{E(REG[r]["nom"])}</strong> (fiche de région, minimum) : '
                 + ", ".join(f'« {mot} {T(s)} »' for s in ss) + "</li>" for r, ss in par.items())
    return f'<details class="card"><summary>Fiches de raisonnement : {C["rais_min"]} au minimum, {C["rais_cible"]} dans la cible</summary><ul class="rais">{li}</ul></details>'


def existants_html(lst, deja):
    li = "".join(f'<li>{"<b class=ok>fiche de technique</b> " if e["titre"] in deja else ""}{T(e["titre"])} '
                 f'<span class="muted">→ {", ".join(E(c.replace("|*", " (tous systèmes)").replace("|", " · ")) for c in e["couvre"])}</span></li>' for e in lst)
    return f'<details class="card"><summary>Les {len(lst)} fiches existantes et ce qu\'elles touchent</summary><ul class="exl">{li}</ul></details>'


def bloc_totaux(C, nom, n_exist):
    return f'''<div class="tiles">
 <div class="tile" style="--c:#16a34a"><span class="k">{C["mini"]}</span><span class="l">fiches au minimum indispensable</span><span class="d">{C["dxM"]} diagnostics + {C["ftM"]} techniques + {C["rais_min"]} raisonnements</span></div>
 <div class="tile" style="--c:#2563eb"><span class="k">{C["cible"]}</span><span class="l">fiches dans la cible complète</span><span class="d">{C["dxT"]} diagnostics + {C["ftT"]} techniques + {C["rais_cible"]} raisonnements</span></div>
 <div class="tile" style="--c:#64748b"><span class="k">{n_exist}</span><span class="l">fiches existantes ({E(nom)})</span><span class="d">dont {len(C["deja"])} correspondent à une fiche de technique du recensement</span></div>
 <div class="tile" style="--c:#dc2626"><span class="k">+{C["ecart_min"]} à +{C["ecart_cible"]}</span><span class="l">écart brut avec l'existant</span><span class="d">{C["a_creer_min"]} à {C["a_creer_cible"]} fiches restent à créer réellement</span></div>
</div>'''


def images_html(C, mot):
    src = "".join(f'<tr><td data-label="Source"><strong>{T(s["nom"])}</strong></td><td data-label="Licence">{T(s["licence"])}</td><td data-label="Statut">{T(s["statut"])}</td></tr>' for s in D["sources_images"])
    return f'''<div class="card"><h4>Besoin en {mot}</h4>
<p>On prévoit au minimum une {mot[:-1] if mot.endswith("s") else mot} légendée par fiche du minimum, soit <strong>{C["img_min"]}</strong> {mot}. La cible demande une {mot[:-1] if mot.endswith("s") else mot} par technique citée dans chaque diagnostic, puis deux exemples normaux annotés par fiche de technique, soit <strong>{C["img_cible"]}</strong> {mot}.</p>
<div class="tw"><table class="t s"><thead><tr><th>Source libre possible</th><th>Licence annoncée</th><th>Statut</th></tr></thead><tbody>{src}</tbody></table></div>
<p class="note">On vérifie la licence de chaque fichier avant toute reprise, parce que les conditions changent d'un cas à l'autre ; aucune image n'est intégrée ici.</p></div>'''


def onglet(prefixe, titre, lignes, fiches, C, tabl, cle_tech, nom_tech, fonction, nom_exist, mot_rais, mot_img, intro):
    entete = (f'<th>Système</th>{"<th>Fonction explorée</th>" if fonction else ""}<th>Type</th><th>Diagnostic ou tableau-cible</th>'
              f'<th>{E(nom_tech)}</th><th>{"Anomalie clé" if fonction else "Signe sémiologique clé"}</th><th>Existant</th>')
    return f'''
<section class="panel" id="p-{prefixe}" role="tabpanel" aria-labelledby="o-{prefixe}">
 <h2 class="band2">{E(titre)}</h2>
 <p>{intro}</p>
 {bloc_totaux(C, nom_exist, C["n_exist"])}
 <h3>Compteurs</h3>
 {compteurs(C, lignes, tabl, nom_tech)}
 <h3>Inventaire filtrable</h3>
 {filtres(prefixe, tabl)}
 <div class="tw"><table class="t main" id="tb-{prefixe}"><thead><tr>{entete}</tr></thead>
 {tableau_lignes(lignes, C, cle_tech, tabl, fonction)}
 </table></div>
 <h3>Fiches transversales de technique ({C["ftM"]} au minimum, {C["ftT"]} dans la cible)</h3>
 {tableau_fiches_tech(fiches, tabl)}
 <h3>Raisonnement, existant et iconographie</h3>
 {raisonnement(C, mot_rais)}
 {existants_html(D["existants"][nom_exist], C["deja"])}
 {images_html(C, mot_img)}
</section>'''


tot_min = CI["mini"] + CE["mini"]
tot_cible = CI["cible"] + CE["cible"]
sources = "".join(f'<li><strong>{T(s["nom"])}</strong> : {T(s["role"])} <span class="muted">({T(s["statut"])})</span></li>' for s in D["sources"])
lettres_leg = "".join(f'<li>{pastille_lettre(c)} {E(l["nom"])}</li>' for c, l in LET.items())
tech_leg = "".join(f'<li>{pastille_tech(c, TI)} <span class="muted">{E(t["physique"])}</span></li>' for c, t in TI.items())

PAGE = f'''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Recensement topo-systémique</title>
<meta name="description" content="Recensement croisé région × système × type de lésion des fiches d'imagerie et d'explorations fonctionnelles à rédiger pour l'examen fédéral suisse.">
<style>
:root{{--fond:#ffffff;--txt:#111827;--muted:#4b5563;--ligne:#e5e7eb;--accent:#e6007e;--accent2:#0057ff;--doux:#f8fafc}}
*{{box-sizing:border-box}}
html{{-webkit-text-size-adjust:100%}}
body{{margin:0;background:var(--fond);color:var(--txt);font:16px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;overflow-x:hidden}}
header.top{{background:linear-gradient(100deg,#0057ff,#7c3aed 45%,#e6007e);color:#fff;padding:20px 16px 18px}}
header.top h1{{margin:0 0 6px;font-size:clamp(1.35rem,3.2vw,2rem);line-height:1.2}}
header.top p{{margin:0;max-width:70ch;opacity:.95}}
header.top abbr{{color:#fff}}
main{{max-width:1500px;margin:0 auto;padding:0 16px 40px}}
h2,h3,h4{{line-height:1.25}}
h3{{margin:28px 0 10px;padding-left:10px;border-left:6px solid var(--accent)}}
h4{{margin:0 0 8px}}
.band2{{background:var(--accent2);color:#fff;padding:10px 14px;border-radius:8px;font-size:1.3rem;margin:18px 0 10px}}
#p-exp .band2{{background:#e6007e}}
abbr[title]{{text-decoration:underline dotted;cursor:help}}
.regle{{border:2px solid #f59e0b;background:#fffbeb;border-radius:10px;padding:14px 16px;margin:18px 0}}
.regle h2{{margin:0 0 6px;font-size:1.15rem;color:#b45309}}
.regle ol{{margin:6px 0 0;padding-left:22px}}
.tiles{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin:14px 0}}
.tile{{border-radius:10px;padding:12px 14px;background:#fff;border:2px solid var(--c);border-top-width:8px;display:flex;flex-direction:column;gap:2px}}
.tile .k{{font-size:1.9rem;font-weight:800;color:var(--c);font-variant-numeric:tabular-nums}}
.tile .l{{font-weight:600}} .tile .d{{color:var(--muted);font-size:.9rem}}
.grand{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}}
.tabs{{display:flex;gap:8px;flex-wrap:wrap;position:sticky;top:0;background:#fff;padding:10px 0;z-index:5;border-bottom:1px solid var(--ligne)}}
.tabs button{{font:inherit;font-weight:700;border:2px solid var(--c);color:var(--c);background:#fff;border-radius:999px;padding:8px 16px;cursor:pointer}}
.tabs button[aria-selected=true]{{background:var(--c);color:#fff}}
.panel[hidden]{{display:none}}
.grid3{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:12px}}
.card{{border:1px solid var(--ligne);border-radius:10px;padding:12px 14px;background:#fff;margin:10px 0;min-width:0}}
details.card>summary{{cursor:pointer;font-weight:700;color:var(--accent2)}}
.tw{{max-width:100%;overflow-x:auto}}
table.t{{border-collapse:collapse;width:100%;font-size:.95rem}}
table.t th,table.t td{{border-bottom:1px solid var(--ligne);padding:7px 8px;text-align:left;vertical-align:top}}
table.t thead th{{background:#111827;color:#fff;position:sticky;top:0}}
table.s td:nth-child(n+2),table.s th:nth-child(n+2){{text-align:right;font-variant-numeric:tabular-nums}}
table.s td:first-child{{text-align:left}}
tr.tot td{{font-weight:800;border-top:2px solid #111827}}
tr.band th{{background:var(--c);color:#fff;font-size:1.05rem;padding:9px 10px}}
tr.band .cnt{{background:#fff;color:var(--c);border-radius:999px;padding:0 9px;font-weight:800;margin-left:6px}}
table.main td:nth-child(1){{width:13%}}
.pill{{display:inline-block;background:var(--c);color:#fff;font-weight:700;font-size:.78rem;border-radius:999px;padding:1px 8px;white-space:nowrap}}
.tp{{display:block;margin:0 0 4px}} .tp .det{{color:var(--muted);font-size:.88rem}}
abbr.let{{display:inline-grid;place-items:center;width:1.7em;height:1.7em;border-radius:50%;background:var(--c);color:#fff;font-weight:800;text-decoration:none}}
.niv{{font-size:.72rem;font-weight:800;border-radius:4px;padding:0 5px;vertical-align:middle;text-transform:uppercase}}
.niv.m{{background:#16a34a;color:#fff}} .niv.c{{background:#dbeafe;color:#1e40af}}
.ok{{color:#15803d}} .exd summary{{cursor:pointer}} .exd{{color:var(--muted)}} .non{{color:#b91c1c;font-weight:600}} .exi{{font-size:.85rem}}
.muted{{color:var(--muted)}} .note{{color:var(--muted);font-size:.88rem;margin:4px 0 8px}}
.dot{{display:inline-block;width:.8em;height:.8em;border-radius:50%;background:var(--c);margin-right:6px;vertical-align:baseline}}
.filt{{border:2px solid var(--accent2);border-radius:10px;padding:10px 12px;background:var(--doux);margin:8px 0 12px}}
.frow{{display:flex;flex-wrap:wrap;gap:8px 12px;align-items:flex-end;margin-bottom:8px}}
.frow label{{display:flex;flex-direction:column;font-size:.85rem;font-weight:600;min-width:0}}
.frow .grow{{flex:1 1 200px}}
select,input[type=search]{{font:inherit;padding:6px 8px;border:1px solid #9ca3af;border-radius:6px;background:#fff;max-width:100%}}
.chips .lab{{font-weight:700;font-size:.85rem}}
.chip{{font:inherit;font-size:.85rem;border:2px solid var(--c);color:#111827;background:#fff;border-radius:999px;padding:3px 10px;cursor:pointer}}
.chip[aria-pressed=true]{{background:var(--c);color:#fff}}
.chip b{{font-variant-numeric:tabular-nums}}
.raz{{font:inherit;border:0;background:#111827;color:#fff;border-radius:6px;padding:7px 12px;cursor:pointer}}
.live{{margin:4px 0 0;font-size:1rem}} .live strong{{color:var(--accent);font-size:1.15rem}}
ul.leg{{list-style:none;padding:0;margin:6px 0;display:flex;flex-wrap:wrap;gap:6px 16px}}
ul.rais li,ul.exl li{{margin:4px 0}}
footer{{max-width:1500px;margin:0 auto;padding:0 16px 40px}}
@media (max-width:760px){{
 table.main thead,table.t:not(.s) thead{{display:none}}
 table.main,table.main tbody,table.main tr,table.main td,
 table.t:not(.s),table.t:not(.s) tbody,table.t:not(.s) tr,table.t:not(.s) td{{display:block;width:100%!important}}
 table.main tr.row,table.t:not(.s) tbody tr{{border:1px solid var(--ligne);border-radius:8px;margin:8px 0;padding:6px 8px}}
 table.main td,table.t:not(.s) td{{border:0;padding:3px 0}}
 table.main td::before,table.t:not(.s) td::before{{content:attr(data-label);display:block;font-size:.75rem;font-weight:700;color:var(--muted);text-transform:uppercase}}
 tr.band,tr.band th{{display:block;border-radius:8px}}
 table.s{{font-size:.85rem}} table.s th,table.s td{{padding:5px 4px}}
}}
</style></head>
<body>
<header class="top">
 <h1>Recensement topo-systémique : imagerie et explorations fonctionnelles</h1>
 <p>Cette page recense, par raisonnement croisé région × système × type de lésion, les fiches que la préparation à l'examen fédéral (<abbr title="{E(SIG["PROFILES"])}">PROFILES</abbr>/<abbr title="{E(SIG["SCLO"])}">SCLO</abbr>) doit contenir, puis elle les compare aux 53 fiches d'imagerie et aux 43 fiches d'explorations déjà publiées. Version du {E(D["meta"]["date"])}.</p>
</header>
<main>
<section class="regle">
 <h2>Règle de comptage</h2>
 <ol>
  <li>Une <strong>fiche diagnostique</strong> correspond à un diagnostic-cible et réunit sa sémiologie dans toutes les techniques utiles ; on ne crée donc pas une fiche par couple diagnostic-technique.</li>
  <li>Une <strong>fiche de technique</strong> enseigne la physique, la sémiologie de base, les contre-indications et le bon usage d'une technologie ; elle sert à toutes les fiches diagnostiques.</li>
  <li>Une <strong>fiche de raisonnement</strong> guide la démarche devant une région (minimum) ou devant chaque système loco-régional (cible).</li>
  <li>Le <strong>minimum indispensable</strong> rassemble ce qu'un candidat doit reconnaître le jour de l'examen fédéral ; la <strong>cible complète</strong> y ajoute ce qu'un médecin assistant doit savoir en première année. Ce partage repose sur un jugement d'expert (déduction), car PROFILES ne publie pas de liste d'imagerie fiche par fiche.</li>
  <li>L'<strong>écart brut</strong> soustrait les fiches existantes du total ; le nombre <strong>à créer réellement</strong> retire seulement les fiches de technique dont le titre correspond déjà à une fiche existante, parce que les fiches existantes traitent une technique et non un diagnostic.</li>
 </ol>
</section>
<div class="grand">
 <div class="tile" style="--c:#0057ff"><span class="k">{CI["mini"]} à {CI["cible"]}</span><span class="l">fiches d'imagerie (minimum à cible)</span><span class="d">contre {EXI["imagerie"]} existantes, soit un écart de +{CI["ecart_min"]} à +{CI["ecart_cible"]}</span></div>
 <div class="tile" style="--c:#e6007e"><span class="k">{CE["mini"]} à {CE["cible"]}</span><span class="l">fiches d'explorations fonctionnelles</span><span class="d">contre {EXI["explorations"]} existantes, soit un écart de +{CE["ecart_min"]} à +{CE["ecart_cible"]}</span></div>
 <div class="tile" style="--c:#7c3aed"><span class="k">{tot_min} à {tot_cible}</span><span class="l">fiches au total</span><span class="d">contre {EXI["imagerie"] + EXI["explorations"]} existantes ; l'existant couvre donc {round(100 * (EXI["imagerie"] + EXI["explorations"]) / tot_cible)} % de la cible en nombre de fiches</span></div>
 <div class="tile" style="--c:#ea580c"><span class="k">{CI["img_min"] + CE["img_min"]} à {CI["img_cible"] + CE["img_cible"]}</span><span class="l">images et tracés légendés à réunir</span><span class="d">{CI["img_min"]} à {CI["img_cible"]} images d'imagerie, {CE["img_min"]} à {CE["img_cible"]} tracés ou courbes</span></div>
</div>
<div class="card"><h4>Légendes</h4>
 <p>Le mnémonique <abbr title="Vasculaire, Infectieux, Tumoral, Dégénératif, Iatrogène, Traumatique, Congénital, Auto-immun, Fonctionnel">VITE DIT CAFé</abbr> classe chaque lésion ; on survole une pastille pour lire sa catégorie. Le « E » sert seulement de liaison dans le mot.</p>
 <ul class="leg">{lettres_leg}</ul>
 <p>Les pastilles de couleur distinguent les technologies d'imagerie selon leur physique.</p>
 <ul class="leg">{tech_leg}</ul>
</div>
<nav class="tabs" role="tablist">
 <button type="button" role="tab" id="o-img" aria-controls="p-img" aria-selected="true" style="--c:#0057ff">A. Imagerie ({CI["mini"]}–{CI["cible"]})</button>
 <button type="button" role="tab" id="o-exp" aria-controls="p-exp" aria-selected="false" style="--c:#e6007e">B. Explorations fonctionnelles ({CE["mini"]}–{CE["cible"]})</button>
</nav>
{onglet("img", "A. Imagerie : région × système × type de lésion → technique → signe", D["imagerie"], D["fiches_technique_imagerie"], CI, TI, "techniques", "Technique(s)", False, "imagerie", "Démarche d'imagerie :", "images",
        "Chaque ligne nomme un diagnostic que l'imagerie doit reconnaître, puis elle indique la technique, la phase ou la séquence qui le montre et le signe qui le fait reconnaître. Les techniques apparaissent dans l'ordre où on les demande habituellement.")}
{onglet("exp", "B. Explorations fonctionnelles : région × fonction × type d'altération → exploration → anomalie", D["explorations"], D["fiches_technique_explorations"], CE, TE, "explorations", "Exploration(s)", True, "explorations", "Démarche fonctionnelle :", "tracés",
        "Chaque ligne nomme une altération fonctionnelle, puis elle indique l'exploration qui la mesure et l'anomalie qui la signe. Les épreuves biologiques dynamiques figurent ici lorsqu'elles testent la réponse d'un axe, car un dosage isolé ne suffit pas.")}
</main>
<footer>
 <h3>Sources et force des critères</h3>
 <p>On cite un critère seulement lorsqu'une recommandation suisse ou européenne le porte ; sinon on l'accompagne de la mention « (non vérifié CH) ». Aucun chiffre de prévalence n'apparaît, parce qu'aucune source suisse datée ne l'a fourni pour ce travail.</p>
 <ul>{sources}</ul>
 <h3>Limites</h3>
 <p>Ce recensement reste une estimation d'expert : il couvre les diagnostics que l'on attend d'un médecin généraliste en formation, mais il ne remplace pas une confrontation ligne à ligne avec le catalogue PROFILES. Les fiches existantes traitent des techniques, si bien qu'elles touchent des systèmes entiers sans fournir de fiche diagnostique ; la colonne « Existant » le signale par la mention « Partiel ». On régénère cette page en modifiant <code>recensement.json</code>, puis en lançant <code>python3 generer.py</code>.</p>
</footer>
<script>
(function(){{
 var tabs=document.querySelectorAll('.tabs [role=tab]');
 function montre(id){{tabs.forEach(function(b){{var on=b.id===id;b.setAttribute('aria-selected',on);document.getElementById(b.getAttribute('aria-controls')).hidden=!on;}});
  try{{localStorage.setItem('rts-onglet',id);}}catch(e){{}}}}
 tabs.forEach(function(b){{b.addEventListener('click',function(){{montre(b.id);}});}});
 var memo=null;try{{memo=localStorage.getItem('rts-onglet');}}catch(e){{}}
 montre(memo&&document.getElementById(memo)?memo:'o-img');
 document.querySelectorAll('.filt').forEach(function(f){{
  var tb=document.getElementById(f.dataset.cible),rows=[].slice.call(tb.querySelectorAll('tr.row')),
      sel=function(k){{return f.querySelector('[data-f='+k+']');}},
      chips=[].slice.call(f.querySelectorAll('.chip'));
  f.querySelector('[data-tot]').textContent=rows.length;
  function actifs(k){{return chips.filter(function(c){{return c.dataset.f===k&&c.getAttribute('aria-pressed')==='true';}}).map(function(c){{return c.dataset.v;}});}}
  function passe(r,ign){{
   var reg=sel('r').value,niv=sel('n').value,q=sel('q').value.trim().toLowerCase(),ts=actifs('t'),ls=actifs('l');
   if(reg&&r.dataset.r!==reg)return false;
   if(niv&&r.dataset.n!==niv)return false;
   if(q&&r.dataset.s.indexOf(q)<0)return false;
   if(ign!=='t'&&ts.length&&!ts.some(function(t){{return (' '+r.dataset.t+' ').indexOf(' '+t+' ')>=0;}}))return false;
   if(ign!=='l'&&ls.length&&ls.indexOf(r.dataset.l)<0)return false;
   return true;}}
  function maj(){{
   var vis=0,visM=0,parR={{}};
   rows.forEach(function(r){{var ok=passe(r);r.hidden=!ok;if(ok){{vis++;if(r.dataset.n==='M')visM++;parR[r.dataset.r]=(parR[r.dataset.r]||0)+1;}}}});
   tb.querySelectorAll('tbody.grp').forEach(function(g){{var n=parR[g.dataset.r]||0;g.hidden=!n;var c=g.querySelector('[data-cnt]');if(c)c.textContent=n;}});
   f.querySelector('[data-vis]').textContent=vis;f.querySelector('[data-visM]').textContent=visM;
   chips.forEach(function(c){{var k=c.dataset.f,v=c.dataset.v,n=0;
    rows.forEach(function(r){{if(!passe(r,k))return;if(k==='t'?(' '+r.dataset.t+' ').indexOf(' '+v+' ')>=0:r.dataset.l===v)n++;}});
    var b=c.querySelector('b');if(b)b.textContent='('+n+')';}});
  }}
  f.addEventListener('input',maj);f.addEventListener('change',maj);
  chips.forEach(function(c){{c.addEventListener('click',function(){{c.setAttribute('aria-pressed',c.getAttribute('aria-pressed')==='true'?'false':'true');maj();}});}});
  f.querySelector('.raz').addEventListener('click',function(){{sel('r').value='';sel('n').value='';sel('q').value='';chips.forEach(function(c){{c.setAttribute('aria-pressed','false');}});maj();}});
  maj();
 }});
}})();
</script>
</body></html>'''

open(SORTIE, "w", encoding="utf-8").write(PAGE)
print(f"Imagerie : minimum {CI['mini']} ({CI['dxM']} diag + {CI['ftM']} techn + {CI['rais_min']} rais), cible {CI['cible']} "
      f"({CI['dxT']} + {CI['ftT']} + {CI['rais_cible']}), existant {EXI['imagerie']}, à créer {CI['a_creer_min']}–{CI['a_creer_cible']}, images {CI['img_min']}–{CI['img_cible']}")
print(f"Explorations : minimum {CE['mini']} ({CE['dxM']} + {CE['ftM']} + {CE['rais_min']}), cible {CE['cible']} "
      f"({CE['dxT']} + {CE['ftT']} + {CE['rais_cible']}), existant {EXI['explorations']}, à créer {CE['a_creer_min']}–{CE['a_creer_cible']}, tracés {CE['img_min']}–{CE['img_cible']}")
print(f"Page : {SORTIE} ({os.path.getsize(SORTIE) // 1024} Ko)")
