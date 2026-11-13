#!/usr/bin/env python3
"""Fabrique RECENSEMENT_TOPOSYSTEMIQUE.html à partir de recensement.json.

Usage : python3 generer.py   (aucune dépendance hors bibliothèque standard)
On modifie le JSON, puis on relance ce script : la page se régénère gratuitement.
"""
import glob, html, json, os, re, sys
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


# --- Enrichissement par diagnostic : enrichi/*.json (clé = id), fusionné au recensement -------------------------
# Les fichiers dont le nom commence par « _ » (démo, brouillons) restent hors de la page finale ;
# « python3 generer.py --demo » les inclut et écrit _demo_RECENSEMENT.html pour les essais.
DEMO = "--demo" in sys.argv
if DEMO:
    SORTIE = os.path.join(ICI, "_demo_RECENSEMENT.html")


def _liste(v):
    if v is None:
        return []
    if isinstance(v, (str, int, float)):
        return [str(v)] if str(v).strip() else []
    return [str(x) for x in v if x not in (None, "")]


def charger_enrichi():
    enr = {}
    for p in sorted(glob.glob(os.path.join(ICI, "enrichi", "*.json"))):
        nom = os.path.basename(p)
        if nom.startswith("_") and not DEMO:
            continue
        try:
            bloc = json.load(open(p, encoding="utf-8"))
        except Exception as e:  # un fichier en cours d'écriture ne bloque pas la page
            print(f"Enrichissement ignoré ({nom}) : {e}")
            continue
        if isinstance(bloc, dict):
            enr.update({k: v for k, v in bloc.items() if isinstance(v, dict)})
    for v in enr.values():
        g = v.get("gold") if isinstance(v.get("gold"), dict) else {}
        v["gold"] = {"examen": str(g.get("examen") or ""), "pourquoi": _liste(g.get("pourquoi")),
                     "quand": _liste(g.get("quand")), "montre": _liste(g.get("montre")),
                     "premiere_intention": str(g.get("premiere_intention") or "")}
        autres = [a for a in (v.get("autres") or []) if isinstance(a, dict) and a.get("examen")]
        autres.sort(key=lambda a: a["rang"] if isinstance(a.get("rang"), (int, float)) else 99)
        v["autres"] = [{"examen": str(a["examen"]), "rang": a.get("rang"), "quand": _liste(a.get("quand")),
                        "pourquoi_pas_gold": _liste(a.get("pourquoi_pas_gold")), "montre": _liste(a.get("montre"))}
                       for a in autres]
        for c in ("syndrome", "traitement", "sources"):
            v[c] = _liste(v.get(c))
        if not isinstance(v.get("images"), dict):
            v["images"] = {"manque": "Aucune image n'est encore référencée pour ce diagnostic."}
    return enr


ENR = charger_enrichi()
if DEMO:  # une entrée de démo peut porter sa propre ligne de recensement (« ligne »)
    for k, v in ENR.items():
        cle = "imagerie" if k.startswith("IMG") else "explorations"
        if isinstance(v.get("ligne"), dict) and not any(r["id"] == k for r in D[cle]):
            D[cle].append(dict(v["ligne"], id=k))


def puce_tech(code, tabl, detail):
    t = tabl[code]
    titre = t["nom"] + (" — " + t["physique"] if "physique" in t else "")
    return (f'<li><span class="pill" title="{E(titre)}">{E(t["nom"] if code not in ("TDM", "IRM") else code)}</span>'
            f'<span class="det">{T(detail)}</span></li>')


def examens_html(r, cle_tech, tabl):
    """Référence (pastille OR) + 1re intention + autres examens numérotés ; sinon les techniques du recensement."""
    en = ENR.get(r["id"])
    if not en or not en["gold"]["examen"]:
        return '<ul class="techl">' + "".join(puce_tech(t["tech"], tabl, t["detail"]) for t in r[cle_tech]) + "</ul>"
    g = en["gold"]
    h = (f'<button type="button" class="gold" data-ex="g" aria-haspopup="dialog"><span class="ref">Référence</span>'
         f'<span class="exn">{E(g["examen"])}</span></button>')
    if g["premiere_intention"]:
        h += f'<p class="pi"><span class="k">1re intention :</span> {E(g["premiere_intention"])}</p>'
    if en["autres"]:
        h += '<ol class="autres">' + "".join(
            f'<li><button type="button" class="exb" data-ex="{i}" aria-haspopup="dialog">{E(a["examen"])}</button></li>'
            for i, a in enumerate(en["autres"])) + "</ol>"
    return h


def donnees_tableau(prefixe, lignes, C, cle_tech, tabl, fonction):
    """Lignes triées région > système > lettre ; le JS construit le tbody et recalcule les rowspan après filtrage."""
    ordre_r, ordre_l, prem = list(REG), list(LET), {}
    for i, r in enumerate(lignes):
        prem.setdefault((r["region"], r["systeme"]), i)
    tri = sorted(enumerate(lignes), key=lambda p: (ordre_r.index(p[1]["region"]), prem[(p[1]["region"], p[1]["systeme"])],
                                                    ordre_l.index(p[1]["lettre"]), p[0]))
    rows = []
    for _, r in tri:
        ex = titres_existants(r, C["corr"])
        exi = (f'<details class="exd"><summary>Partiel : {len(ex)} fiche{"s" if len(ex) > 1 else ""} de technique</summary>'
               '<ul class="exl">' + "".join(f"<li>{E(t)}</li>" for t in ex) + "</ul></details>") if ex else \
              '<span class="non">Aucune fiche existante</span>'
        en = ENR.get(r["id"])
        texte = r.get("signe") or r.get("anomalie") or ""
        noms_ex = " ".join([en["gold"]["examen"]] + [a["examen"] for a in en["autres"]]) if en else ""
        rows.append({
            "id": r["id"], "r": r["region"], "s": r["systeme"], "l": r["lettre"], "n": r["niveau"],
            "t": " ".join(sorted({t["tech"] for t in r[cle_tech]})),
            "q": (r["diagnostic"] + " " + r["systeme"] + " " + texte + " " + r.get("fonction", "") + " "
                  + " ".join(t["detail"] for t in r[cle_tech]) + " " + noms_ex).lower(),
            "sh": T(r["systeme"]), "dxt": T(r["diagnostic"]),
            "c": {"dx": f'<button type="button" class="dxb" data-p="{prefixe}" data-dx="{E(r["id"])}" aria-haspopup="dialog">{T(r["diagnostic"])}</button>',
                  "niv": niveau(r["niveau"]), "ex": examens_html(r, cle_tech, tabl), "sg": T(texte), "exi": exi,
                  "fct": T(r.get("fonction", "")) if fonction else ""}})
    return rows


DONNEES_LIGNES = {}


def donnees_json():
    ids = {r["id"] for rows in DONNEES_LIGNES.values() for r in rows}
    d = {"lignes": DONNEES_LIGNES, "reg": {c: r["nom"] for c, r in REG.items()},
         "let": {c: pastille_lettre(c) for c in LET}, "letn": {c: l["nom"] for c, l in LET.items()},
         "enr": {k: {kk: vv for kk, vv in v.items() if kk != "ligne"} for k, v in ENR.items() if k in ids}}
    return json.dumps(d, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/").replace("<!--", "<\\u0021--")


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
<div class="filt" id="f-{prefixe}" data-p="{prefixe}" data-cible="tb-{prefixe}">
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
    entete = ('<th scope="col">Région</th><th scope="col">Système</th><th scope="col" class="ctr">Type</th>'
              '<th scope="col" class="dx">Diagnostic ou tableau-cible</th><th scope="col" class="ctr">Niveau</th>'
              + ('<th scope="col">Fonction explorée</th>' if fonction else '')
              + f'<th scope="col">{"Explorations" if fonction else "Examens : référence, puis autres"}</th>'
              + f'<th scope="col">{"Anomalie clé" if fonction else "Signe sémiologique clé"}</th><th scope="col">Existant</th>')
    DONNEES_LIGNES[prefixe] = donnees_tableau(prefixe, lignes, C, cle_tech, tabl, fonction)
    return f'''
<section class="panel" id="p-{prefixe}" role="tabpanel" aria-labelledby="o-{prefixe}">
 <h2 class="band2">{E(titre)}</h2>
 <p>{intro}</p>
 {bloc_totaux(C, nom_exist, C["n_exist"])}
 <h3>Compteurs</h3>
 {compteurs(C, lignes, tabl, nom_tech)}
 <h3>Inventaire filtrable</h3>
 {filtres(prefixe, tabl)}
 <div class="tw tmain"><table class="t main" id="tb-{prefixe}" data-fct="{1 if fonction else 0}"><colgroup><col class="c-reg"><col class="c-sys"><col class="c-let"><col class="c-dx"><col class="c-niv">{'<col class="c-fct">' if fonction else ''}<col class="c-ex"><col class="c-sg"><col class="c-exi"></colgroup><thead><tr>{entete}</tr></thead>
 <tbody><tr><td colspan="9">Chargement du tableau…</td></tr></tbody>
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


# --- Feuille de style du tableau principal, de la fenêtre centrale et du popover (chaîne brute, hors f-string) ----
CSS2 = r"""
/* Couleurs à rôle unique (EYE SPOT) : --or = examen de référence seulement ; --rep = numéros et flèches des repères seulement. */
:root{--or:#d4af37;--rep:#00c8ff}
/* Tableau principal : grille géométrique fixe, défilement horizontal et vertical internes, colonne Diagnostic collante */
.tmain{max-height:82vh;overflow:auto;border:1px solid #111;border-radius:8px;-webkit-overflow-scrolling:touch;overscroll-behavior-x:contain}
table.main{table-layout:fixed;width:1574px;border-collapse:separate;border-spacing:0;font-size:.93rem}
#tb-exp{width:1774px}
table.main col.c-reg{width:120px} table.main col.c-sys{width:150px} table.main col.c-let{width:56px}
table.main col.c-dx{width:240px} table.main col.c-niv{width:88px} table.main col.c-fct{width:200px}
table.main col.c-ex{width:340px} table.main col.c-sg{width:360px} table.main col.c-exi{width:220px}
table.main th,table.main td{border:0;border-bottom:1px solid var(--ligne);border-right:1px solid var(--ligne);padding:8px 10px;vertical-align:top;text-align:left;overflow-wrap:break-word;-webkit-hyphens:auto;hyphens:auto}
table.main thead th{hyphens:manual} table.main thead th.ctr{padding-left:2px;padding-right:2px}
table.main thead th{position:sticky;top:0;z-index:3;background:#fff;color:#000;border-bottom:2px solid #111;font-size:.85rem}
table.main thead th.dx{left:0;z-index:4}
table.main td.dx{position:sticky;left:0;z-index:2;background:#fff}
table.main th.dx,table.main td.dx{box-shadow:inset -2px 0 0 #111}
table.main .ctr,table.main td.let,table.main td.niv{text-align:center}
table.main th.reg{background:var(--n3);color:#000;font-weight:800;border-bottom:2px solid #111}
table.main td.sys{font-weight:700}
table.main tr.r0>*{border-top:2px solid #111}
table.main tbody tr:first-child>*{border-top:0}
.stk{position:sticky;top:calc(var(--th,44px) + 6px)}
th.reg .cnt{display:block;font-weight:600;font-size:.8rem;margin-top:4px}
table.main abbr.let{width:30px;height:30px;font-size:.95rem;line-height:1}
table.main .niv{display:inline-block;width:62px;text-align:center;padding:2px 0;font-size:.72rem;border-radius:4px}
button.dxb{all:unset;cursor:pointer;font-weight:800;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:3px}
ul.techl,ul.exl,ul.enum{margin:0;padding:0}
ul.exl,ul.enum{padding-left:1.2em;list-style:disc}
ul.exl li,ul.enum li{margin:2px 0}
ul.techl{list-style:none}
ul.techl li{display:grid;grid-template-columns:112px 1fr;gap:8px;align-items:start;margin:0 0 6px}
ul.techl .pill{display:block;width:112px;text-align:center;white-space:normal;overflow-wrap:normal;word-break:normal;line-height:1.2;padding:2px 4px;border-radius:6px}
ul.techl .det{color:#000;font-size:.88rem}
.exd summary{cursor:pointer}
button.gold{display:block;width:100%;text-align:left;font:inherit;font-weight:700;background:var(--or);color:#000;border:1px solid #000;border-radius:8px;padding:4px 10px 6px;cursor:pointer;line-height:1.3}
button.gold .ref,.badge{display:block;font-size:.68rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em}
.pi{margin:6px 0 0;font-size:.88rem} .pi .k{font-weight:800}
ol.autres{margin:8px 0 0;padding-left:1.7em} ol.autres li{margin:3px 0}
button.exb{all:unset;cursor:pointer;text-decoration:underline dotted;text-underline-offset:3px}
button.dxb:focus-visible,button.gold:focus-visible,button.exb:focus-visible,.rep:focus-visible,.fen button:focus-visible{outline:3px solid #000;outline-offset:2px}
/* Popover d'examen */
#pop{position:fixed;z-index:60;width:min(380px,calc(100vw - 32px));max-height:min(60vh,520px);overflow:auto;background:#fff;color:#000;border:2px solid #000;border-radius:10px;padding:12px 14px;box-shadow:0 8px 24px rgba(0,0,0,.25)}
#pop[hidden]{display:none}
#pop .badge{display:inline-block;border:1px solid #000;border-radius:6px;padding:1px 6px;margin:0 0 4px}
#pop .badge.or{background:var(--or)}
#pop h4{margin:0 28px 6px 0;font-size:1rem}
#pop h5{margin:10px 0 2px;font-size:.85rem}
#pop .ferme{position:absolute;top:6px;right:6px}
/* Fenêtre centrale : page floutée derrière un voile blanc */
html.fige,html.fige body{overflow:hidden}
.voile{position:fixed;inset:0;z-index:50;background:rgba(255,255,255,.6);-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px);display:flex;align-items:flex-start;justify-content:center;padding:4vh 16px;overflow:auto}
.voile[hidden]{display:none}
.fen{position:relative;background:#fff;color:#000;border:2px solid #000;border-radius:12px;width:100%;max-width:980px;padding:16px 18px 20px;box-shadow:0 12px 40px rgba(0,0,0,.25);outline:0}
.fen>h2{margin:0 44px 6px 0}
.fen h3{margin:18px 0 6px}
.ferme{font:inherit;font-weight:800;background:#fff;color:#000;border:2px solid #000;border-radius:999px;width:34px;height:34px;cursor:pointer;line-height:1}
.fen>.ferme{position:absolute;top:12px;right:12px}
.fen .meta{margin:0 0 10px;font-size:.9rem}
.manque{border:2px dashed #000;border-radius:8px;padding:10px 12px}
.bascule{font:inherit;font-weight:700;background:#fff;color:#000;border:2px solid #000;border-radius:8px;padding:6px 14px;cursor:pointer;margin:0 0 8px}
.bascule[aria-pressed=true]{background:#000;color:#fff}
.fig{margin:0;text-align:center}
.cadre{position:relative;display:inline-block;max-width:100%;vertical-align:top;background:#000}
.cadre img{display:block;max-width:100%;max-height:60vh;width:auto;height:auto}
.cadre svg{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;overflow:visible}
.cadre svg .l0{stroke:#000;stroke-width:5;vector-effect:non-scaling-stroke;stroke-linecap:round}
.cadre svg .l1{stroke:var(--rep);stroke-width:2.5;vector-effect:non-scaling-stroke;stroke-linecap:round}
.cadre svg polygon{fill:var(--rep);stroke:#000;stroke-width:1.2;vector-effect:non-scaling-stroke}
.rep,.num{display:inline-grid;place-items:center;width:28px;height:28px;border-radius:50%;background:var(--rep);color:#000;border:2px solid #000;font:800 .9rem/1 system-ui,sans-serif}
.rep{position:absolute;transform:translate(-50%,-50%);cursor:pointer;padding:0}
.rep[aria-pressed=true]{box-shadow:0 0 0 3px #fff,0 0 0 6px #000}
.fig figcaption{font-size:.88rem;margin-top:6px}
.lesion{border:2px solid #000;border-radius:8px;padding:8px 12px;margin:10px 0 0}
.lesion p{margin:4px 0} .lesion .aide{font-style:italic}
.cred{font-size:.78rem;margin:4px 0;overflow-wrap:anywhere}
.cred a{color:#000;text-decoration:underline}
@media (max-width:760px){
 table.main{width:1258px} #tb-exp{width:1438px}
 table.main col.c-reg{width:84px} table.main col.c-sys{width:100px} table.main col.c-let{width:44px} table.main col.c-dx{width:170px}
 table.main th,table.main td{padding:6px 7px} table.main abbr.let{width:26px;height:26px}
 table.main col.c-ex{width:300px} table.main col.c-sg{width:300px} table.main col.c-exi{width:180px} table.main col.c-fct{width:180px}
 .tmain{max-height:75vh}
 .fen{padding:12px 12px 16px} .voile{padding:12px}
}
"""

MARKUP = """
<div class="voile" id="voile" hidden>
 <div class="fen" role="dialog" aria-modal="true" aria-labelledby="fen-t" tabindex="-1">
  <button type="button" class="ferme" aria-label="Fermer la fenêtre">✕</button>
  <h2 id="fen-t"></h2>
  <div id="fen-c"></div>
 </div>
</div>
<div id="pop" role="dialog" aria-label="Détail de l'examen" tabindex="-1" hidden></div>
"""

JS = r"""
(function(){
 var DON=JSON.parse(document.getElementById('donnees').textContent);
 var MAP={'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'};
 function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return MAP[c];});}
 function liste(a){return (a&&a.length)?'<ul class="enum">'+a.map(function(x){return '<li>'+esc(x)+'</li>';}).join('')+'</ul>':'';}
 function hauteurs(){document.querySelectorAll('table.main').forEach(function(t){var h=t.tHead.offsetHeight;if(h)t.style.setProperty('--th',h+'px');});}
 /* Onglets */
 var tabs=document.querySelectorAll('.tabs [role=tab]');
 function montre(id){tabs.forEach(function(b){var on=b.id===id;b.setAttribute('aria-selected',on);document.getElementById(b.getAttribute('aria-controls')).hidden=!on;});
  try{localStorage.setItem('rts-onglet',id);}catch(e){}
  hauteurs();}
 tabs.forEach(function(b){b.addEventListener('click',function(){montre(b.id);});});
 /* Filtres + reconstruction du tbody (rowspan recalculés sur les lignes visibles) */
 var INDEX={};
 document.querySelectorAll('.filt').forEach(function(f){
  var pref=f.dataset.p,table=document.getElementById(f.dataset.cible),rows=DON.lignes[pref]||[],
      fct=table.dataset.fct==='1',ncol=table.tHead.rows[0].cells.length,
      sel=function(k){return f.querySelector('[data-f='+k+']');},
      chips=[].slice.call(f.querySelectorAll('.chip'));
  INDEX[pref]={};rows.forEach(function(r){INDEX[pref][r.id]=r;});
  f.querySelector('[data-tot]').textContent=rows.length;
  function actifs(k){return chips.filter(function(c){return c.dataset.f===k&&c.getAttribute('aria-pressed')==='true';}).map(function(c){return c.dataset.v;});}
  function aT(r,t){return (' '+r.t+' ').indexOf(' '+t+' ')>=0;}
  function passe(r,ign){
   var reg=sel('r').value,niv=sel('n').value,q=sel('q').value.trim().toLowerCase(),ts=actifs('t'),ls=actifs('l');
   if(reg&&r.r!==reg)return false;
   if(niv&&r.n!==niv)return false;
   if(q&&r.q.indexOf(q)<0)return false;
   if(ign!=='t'&&ts.length&&!ts.some(function(t){return aT(r,t);}))return false;
   if(ign!=='l'&&ls.length&&ls.indexOf(r.l)<0)return false;
   return true;}
  function etendue(v,i,egal){var k=i;while(k<v.length&&egal(v[k]))k++;return k-i;}
  function construit(v){
   var h=[],n=v.length;
   for(var i=0;i<n;i++){
    var r=v[i],p=i?v[i-1]:null,c='',neuveR=!p||p.r!==r.r;
    if(neuveR){var k=etendue(v,i,function(x){return x.r===r.r;});
     c+='<th scope="rowgroup" class="reg" rowspan="'+k+'"><div class="stk">'+esc(DON.reg[r.r])+'<span class="cnt">'+k+' fiche'+(k>1?'s':'')+'</span></div></th>';}
    if(neuveR||p.s!==r.s){c+='<td class="sys" rowspan="'+etendue(v,i,function(x){return x.r===r.r&&x.s===r.s;})+'"><div class="stk">'+r.sh+'</div></td>';}
    if(neuveR||p.s!==r.s||p.l!==r.l){c+='<td class="let" rowspan="'+etendue(v,i,function(x){return x.r===r.r&&x.s===r.s&&x.l===r.l;})+'"><div class="stk">'+DON.let[r.l]+'</div></td>';}
    c+='<td class="dx">'+r.c.dx+'</td><td class="niv">'+r.c.niv+'</td>'+(fct?'<td class="fct">'+r.c.fct+'</td>':'')
      +'<td class="ex">'+r.c.ex+'</td><td class="sg">'+r.c.sg+'</td><td class="exi">'+r.c.exi+'</td>';
    h.push('<tr data-id="'+esc(r.id)+'"'+(neuveR?' class="r0"':'')+'>'+c+'</tr>');
   }
   if(!n)h.push('<tr><td colspan="'+ncol+'">Aucune fiche ne correspond aux filtres.</td></tr>');
   table.tBodies[0].innerHTML=h.join('');
  }
  var etat=null;
  function maj(){
   /* on ne reconstruit que si les filtres ont changé : un « change » tardif (sortie du champ de recherche)
      ne doit pas remplacer le bouton sur lequel on est en train de cliquer */
   var e=[sel('r').value,sel('n').value,sel('q').value.trim().toLowerCase(),actifs('t').join(),actifs('l').join()].join('§');
   if(e===etat)return;etat=e;
   var vis=rows.filter(function(r){return passe(r);}),visM=vis.filter(function(r){return r.n==='M';}).length;
   construit(vis);
   f.querySelector('[data-vis]').textContent=vis.length;f.querySelector('[data-visM]').textContent=visM;
   chips.forEach(function(c){var k=c.dataset.f,v=c.dataset.v,n=0;
    rows.forEach(function(r){if(passe(r,k)&&(k==='t'?aT(r,v):r.l===v))n++;});
    var b=c.querySelector('b');if(b)b.textContent='('+n+')';});
  }
  f.addEventListener('input',maj);f.addEventListener('change',maj);
  chips.forEach(function(c){c.addEventListener('click',function(){c.setAttribute('aria-pressed',c.getAttribute('aria-pressed')==='true'?'false':'true');maj();});});
  f.querySelector('.raz').addEventListener('click',function(){sel('r').value='';sel('n').value='';sel('q').value='';chips.forEach(function(c){c.setAttribute('aria-pressed','false');});maj();});
  maj();
 });
 var memo=null;try{memo=localStorage.getItem('rts-onglet');}catch(e){}
 montre(memo&&document.getElementById(memo)?memo:'o-img');
 window.addEventListener('resize',hauteurs);

 /* Popover d'examen */
 var pop=document.getElementById('pop'),popDe=null;
 function fermePop(rend){if(pop.hidden)return;pop.hidden=true;if(rend!==false&&popDe&&document.contains(popDe))popDe.focus({preventScroll:true});popDe=null;}
 function placePop(b){
  var rc=b.getBoundingClientRect(),w=pop.offsetWidth,h=pop.offsetHeight,W=document.documentElement.clientWidth,H=window.innerHeight;
  var x=Math.max(16,Math.min(rc.left,W-w-16)),y=rc.bottom+6;
  if(y+h>H-16)y=Math.max(16,rc.top-h-6);
  pop.style.left=x+'px';pop.style.top=y+'px';}
 function ouvrePop(id,k,b){
  var en=DON.enr[id];if(!en)return;var t,badge,secs,g=en.gold;
  if(k==='g'){t=g.examen;badge='Examen de référence';
   secs=[['Pourquoi c’est la référence',g.pourquoi],['Quand on la réalise',g.quand],['Ce qu’elle montre',g.montre]];}
  else{var a=en.autres[+k];if(!a)return;t=a.examen;badge='Autre examen n° '+(+k+1);
   secs=[['Pourquoi ce n’est pas la référence',a.pourquoi_pas_gold],['Quand on la réalise quand même',a.quand],['Ce qu’elle montre',a.montre]];}
  var h='<button type="button" class="ferme" aria-label="Fermer">✕</button><span class="badge'+(k==='g'?' or':'')+'">'+esc(badge)+'</span><h4>'+esc(t)+'</h4>',vide=true;
  if(k==='g'&&g.premiere_intention){h+='<h5>Examen de 1re intention</h5>'+liste([g.premiere_intention]);}
  secs.forEach(function(s){if(s[1]&&s[1].length){vide=false;h+='<h5>'+esc(s[0])+'</h5>'+liste(s[1]);}});
  if(vide)h+='<p>Aucune justification n’est encore rédigée.</p>';
  pop.innerHTML=h;pop.hidden=false;popDe=b;placePop(b);pop.focus({preventScroll:true});
 }
 /* au défilement, le popover suit son examen tant que celui-ci reste visible, sinon il se ferme */
 window.addEventListener('scroll',function(e){if(pop.hidden||pop.contains(e.target))return;
  var rc=popDe&&popDe.getBoundingClientRect();
  if(rc&&rc.bottom>0&&rc.top<window.innerHeight&&rc.right>0&&rc.left<document.documentElement.clientWidth)placePop(popDe);else fermePop(false);},true);

 /* Fenêtre centrale du diagnostic */
 var voile=document.getElementById('voile'),fen=voile.querySelector('.fen'),fenT=document.getElementById('fen-t'),fenC=document.getElementById('fen-c'),fenDe=null;
 function fermeDx(){if(voile.hidden)return;fermePop(false);voile.hidden=true;document.documentElement.classList.remove('fige');if(fenDe&&document.contains(fenDe))fenDe.focus({preventScroll:true});}
 function lien(u){return /^https?:\/\//i.test(u||'')?' <a href="'+esc(u)+'" target="_blank" rel="noopener">page de l’image</a>':'';}
 function credit(nom,o){if(!o)return '';return '<p class="cred"><strong>'+nom+'</strong>'+(o.technique?' : '+esc(o.technique):'')+(o.credit?' — crédit : '+esc(o.credit):'')+(o.licence?' — licence : '+esc(o.licence):'')+(lien(o.url)?' —'+lien(o.url):'')+'</p>';}
 function ouvreDx(pref,id,b){
  fermePop(false);
  var r=INDEX[pref][id],en=DON.enr[id];if(!r)return;fenDe=b;
  fenT.innerHTML=r.dxt;
  var h='<p class="meta">'+esc(DON.reg[r.r])+' · '+r.sh+' · '+esc(DON.letn[r.l])+' · '+(r.n==='M'?'Minimum indispensable':'Cible complète')+'</p>';
  if(!en){
   h+='<p class="manque">Enrichissement en cours : le cliché, le regroupement syndromique et le traitement de ce diagnostic ne sont pas encore rédigés.</p><h3>Examens</h3>'+r.c.ex+'<h3>Signe clé</h3><p>'+r.c.sg+'</p>';
  }else{
   var im=en.images||{};
   if(im.manque||!(im.normal||im.patho))h+='<p class="manque"><strong>Aucune image libre fiable.</strong> '+esc(im.manque||'')+'</p>';
   else h+=(im.normal&&im.patho?'<button type="button" class="bascule" aria-pressed="false">Voir la pathologie</button>':'')
     +'<figure class="fig"><div class="cadre"><img alt=""><svg viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"></svg></div><figcaption></figcaption></figure><div class="lesion" aria-live="polite" hidden></div>';
   if(en.syndrome.length)h+='<h3>Regroupement syndromique</h3>'+liste(en.syndrome);
   if(en.traitement.length)h+='<h3>Traitement</h3>'+liste(en.traitement);
   if(!im.manque)h+=credit('Cliché normal',im.normal)+credit('Cliché pathologique',im.patho);
   if(en.sources.length)h+='<div class="cred"><strong>Sources</strong>'+liste(en.sources)+'</div>';
  }
  fenC.innerHTML=h;voile.hidden=false;document.documentElement.classList.add('fige');voile.scrollTop=0;fen.focus({preventScroll:true});
  if(en&&en.images&&!en.images.manque&&(en.images.normal||en.images.patho))images(en.images);
 }
 function images(im){
  var img=fenC.querySelector('.cadre img'),svg=fenC.querySelector('.cadre svg'),cadre=fenC.querySelector('.cadre'),
      cap=fenC.querySelector('figcaption'),les=fenC.querySelector('.lesion'),bt=fenC.querySelector('.bascule'),vue=im.normal?'normal':'patho';
  function rend(){
   var o=im[vue]||{},nom=vue==='normal'?'Cliché normal':'Cliché pathologique';
   cadre.querySelectorAll('.rep').forEach(function(n){n.remove();});svg.innerHTML='';les.hidden=true;les.innerHTML='';
   img.onload=function(){if(vue==='patho')reperes(o);};
   img.onerror=function(){cap.innerHTML='<strong>Image introuvable</strong> : '+esc(o.fichier||'');};
   img.alt=nom+(o.technique?' : '+o.technique:'');img.src=o.fichier||'';
   cap.innerHTML='<strong>'+nom+'</strong>'+(o.technique?' — '+esc(o.technique):'');
   if(bt){bt.textContent=vue==='normal'?'Voir la pathologie':'Revoir le cliché normal';bt.setAttribute('aria-pressed',vue==='patho');}
   if(vue==='patho'&&(o.reperes||[]).length){les.hidden=false;les.innerHTML='<p class="aide">Cliquez un numéro sur l’image pour lire la lésion élémentaire.</p>';}
  }
  function reperes(o){
   var a=(img.naturalWidth/img.naturalHeight)||1,s='';
   (o.reperes||[]).forEach(function(p){
    var x=+p.x,y=+p.y,fx=+p.fx,fy=+p.fy;if([x,y,fx,fy].some(isNaN))return;
    /* calcul en unités réelles (x × rapport largeur/hauteur) pour que la pointe ne soit pas déformée par preserveAspectRatio="none" */
    var X=x*a,FX=fx*a,dx=X-FX,dy=y-fy,L=Math.hypot(dx,dy)||1,ux=dx/L,uy=dy/L,H=Math.min(4.5,L*.6),W=H*.55,bx=X-ux*H,by=y-uy*H;
    var pts=[[X,y],[bx-uy*W,by+ux*W],[bx+uy*W,by-ux*W]].map(function(q){return (q[0]/a).toFixed(2)+','+q[1].toFixed(2);}).join(' ');
    var ln='x1="'+fx+'" y1="'+fy+'" x2="'+(bx/a).toFixed(2)+'" y2="'+by.toFixed(2)+'"';
    s+='<line class="l0" '+ln+'/><line class="l1" '+ln+'/><polygon points="'+pts+'"/>';
    var b=document.createElement('button');b.type='button';b.className='rep';b.textContent=p.n;
    b.style.left=fx+'%';b.style.top=fy+'%';b.setAttribute('aria-pressed','false');b.setAttribute('aria-label','Repère '+p.n+' : afficher la lésion');
    b.addEventListener('click',function(){
     cadre.querySelectorAll('.rep').forEach(function(z){z.setAttribute('aria-pressed',z===b);});
     les.hidden=false;les.innerHTML='<p><span class="num">'+esc(p.n)+'</span> <strong>'+esc(p.lesion)+'</strong></p><p>'+esc(p.semio)+'</p>';});
    cadre.appendChild(b);
   });
   svg.innerHTML=s;
  }
  if(bt)bt.addEventListener('click',function(){vue=vue==='normal'?'patho':'normal';rend();});
  rend();
 }

 /* Délégation des clics et du clavier */
 document.addEventListener('click',function(e){
  var t=e.target;
  if(t.closest('#pop .ferme')){fermePop();return;}
  var b=t.closest('[data-ex]');
  if(!pop.hidden&&!pop.contains(t)&&b!==popDe)fermePop(false);
  if(b){var tr=b.closest('tr[data-id]');if(tr){if(!pop.hidden&&popDe===b)fermePop();else ouvrePop(tr.dataset.id,b.dataset.ex,b);}return;}
  var d=t.closest('.dxb');if(d){ouvreDx(d.dataset.p,d.dataset.dx,d);return;}
  if(t===voile||t.closest('#voile .fen>.ferme'))fermeDx();
 });
 document.addEventListener('keydown',function(e){
  if(e.key==='Escape'){if(!pop.hidden){fermePop();e.preventDefault();}else if(!voile.hidden){fermeDx();e.preventDefault();}return;}
  if(e.key==='Tab'&&!voile.hidden){
   var f=[].slice.call(fen.querySelectorAll('button,a[href]')).filter(function(x){return x.offsetParent!==null;});if(!f.length)return;
   if(e.shiftKey&&(document.activeElement===f[0]||document.activeElement===fen)){f[f.length-1].focus();e.preventDefault();}
   else if(!e.shiftKey&&document.activeElement===f[f.length-1]){f[0].focus();e.preventDefault();}
  }
 });
})();
"""
PAGE = f'''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Recensement topo-systémique</title>
<meta name="description" content="Recensement croisé région × système × type de lésion des fiches d'imagerie et d'explorations fonctionnelles à rédiger pour l'examen fédéral suisse.">
<style>
:root{{--fond:#ffffff;--txt:#111827;--muted:#4b5563;--ligne:#e5e7eb;--accent:#e6007e;--accent2:#0057ff;--doux:#f8fafc}}
*{{box-sizing:border-box}}
html{{-webkit-text-size-adjust:100%}}
body{{margin:0;background:var(--fond);color:var(--txt);font:16px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;overflow-x:hidden}}
header.top{{background:var(--n1);color:#000;padding:20px 16px 18px}}
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
 table.t:not(.s):not(.main) thead{{display:none}}
 table.t:not(.s):not(.main),table.t:not(.s):not(.main) tbody,table.t:not(.s):not(.main) tr,table.t:not(.s):not(.main) td{{display:block;width:100%!important}}
 table.t:not(.s):not(.main) tbody tr{{border:1px solid var(--ligne);border-radius:8px;margin:8px 0;padding:6px 8px}}
 table.t:not(.s):not(.main) td{{border:0;padding:3px 0}}
 table.t:not(.s):not(.main) td::before{{content:attr(data-label);display:block;font-size:.75rem;font-weight:700;color:var(--muted);text-transform:uppercase}}
 table.s{{font-size:.85rem}} table.s th,table.s td{{padding:5px 4px}}
}}
/* EYE SPOT strict (Vial 13.11.2026) : 3 couleurs au plus, aucun mélange ni dégradé ; la couleur ne sert qu'à discriminer les niveaux de titres.
   N1 = bandeau, titres d'onglet et onglet actif ; N2 = titres de section (h2, h3) ; N3 = bandes de région (colonne Région fusionnée). Rôles uniques ajoutés : OR = examen de référence ; cyan = numéros et flèches des repères. Tout le reste : noir sur blanc. */
:root{{--n1:#bcd0f7;--n2:#f9dcae;--n3:#cfeedd}}
header.top{{background:var(--n1)!important;color:#000!important}} header.top *,header.top abbr{{color:#000!important}}
.band2,#p-exp .band2{{background:var(--n1)!important;color:#000!important}}
.tabs button{{border:2px solid #111!important;color:#000!important;background:#fff!important}} .tabs button[aria-selected=true]{{background:var(--n1)!important}}
h2,.regle h2{{background:var(--n2);color:#000!important;padding:4px 10px;border-radius:6px}}
h3{{background:var(--n2);color:#000;border-left:0!important;padding:4px 10px;border-radius:6px}}
tr.band th{{background:var(--n3)!important;color:#000!important}} tr.band .cnt{{background:#fff!important;color:#000!important;border:1px solid #111}}
.regle{{border:1px solid #9ca3af!important;background:#fff!important}}
.tile{{border:1px solid #9ca3af!important;border-top-width:1px!important}} .tile .k{{color:#000!important}}
.pill,abbr.let,.niv.m,.niv.c,.chip[aria-pressed=true]{{background:#fff!important;color:#000!important;border:1px solid #111!important}}
.chip{{border:1px solid #9ca3af!important}} .chip[aria-pressed=true]{{font-weight:800;outline:2px solid #111}}
table.t thead th{{background:#fff!important;color:#000!important;border-bottom:2px solid #111}}
.ok,.non{{color:#000!important}} .non{{font-weight:800}}
.dot{{display:none!important}} .filt{{border:1px solid #9ca3af!important;background:#fff!important}} details.card>summary,.live strong,a{{color:#000!important}} details.card>summary{{text-decoration:underline}}
{CSS2}
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
{MARKUP}
<script type="application/json" id="donnees">{donnees_json()}</script>
<script>{JS}</script>
</body></html>'''

open(SORTIE, "w", encoding="utf-8").write(PAGE)
print(f"Imagerie : minimum {CI['mini']} ({CI['dxM']} diag + {CI['ftM']} techn + {CI['rais_min']} rais), cible {CI['cible']} "
      f"({CI['dxT']} + {CI['ftT']} + {CI['rais_cible']}), existant {EXI['imagerie']}, à créer {CI['a_creer_min']}–{CI['a_creer_cible']}, images {CI['img_min']}–{CI['img_cible']}")
print(f"Explorations : minimum {CE['mini']} ({CE['dxM']} + {CE['ftM']} + {CE['rais_min']}), cible {CE['cible']} "
      f"({CE['dxT']} + {CE['ftT']} + {CE['rais_cible']}), existant {EXI['explorations']}, à créer {CE['a_creer_min']}–{CE['a_creer_cible']}, tracés {CE['img_min']}–{CE['img_cible']}")
print(f"Page : {SORTIE} ({os.path.getsize(SORTIE) // 1024} Ko)")
