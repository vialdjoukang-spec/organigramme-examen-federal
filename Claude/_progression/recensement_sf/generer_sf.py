# -*- coding: utf-8 -*-
"""Génère RECENSEMENT_SF.html depuis recensement_sf.json (construit par construire_sf.py).

Forme « EYE SPOT » de Vial : fond blanc, texte noir, une couleur par niveau de titre et rien d'autre,
sigles en <abbr title>, tableaux défilants à cellules répétées fusionnées (rowspan), filtres et compteurs.
Usage : python3 generer_sf.py
"""
import json, os, re, html
from collections import OrderedDict

ICI = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(ICI, "recensement_sf.json"), encoding="utf-8"))
SORTIE = os.path.join(ICI, "RECENSEMENT_SF.html")
E = lambda s: html.escape(str(s), quote=True)
SIG = D["sigles"]
_motif = re.compile(r"(?<![\w-])(" + "|".join(re.escape(k) for k in sorted(SIG, key=len, reverse=True)) + r")(?![\w-])")
SYSN = OrderedDict((s["code"], s["nom"]) for s in D["systemes"])
ORDRE = {c: i for i, c in enumerate(SYSN)}
VITE = OrderedDict((v["code"], v["nom"]) for v in D["vite"])


def T(texte):
    """Échappe puis place chaque sigle dans <abbr title>."""
    out, pos = [], 0
    for m in _motif.finditer(texte):
        out.append(E(texte[pos:m.start()]))
        out.append(f'<abbr title="{E(SIG[m.group(1)])}">{E(m.group(1))}</abbr>')
        pos = m.end()
    out.append(E(texte[pos:]))
    return "".join(out)


def L(items):
    return "<ul>" + "".join(f"<li>{T(x)}</li>" for x in items) + "</ul>"


def sysc(code):
    return f'<abbr title="{E(SYSN.get(code, code))}">{E(code)}</abbr> {T(SYSN.get(code, ""))}'


NIV = {"m": "minimum", "c": "cible"}
plain = lambda h: re.sub(r"<[^>]+>", " ", h).lower()


def ligne(cells, sys_code, niv, merge_keys):
    return {"c": cells, "s": sys_code, "n": niv, "k": merge_keys, "q": plain(" ".join(cells))}


# ---------------------------------------------------------------- jeux de lignes
def tri(lst, *cles):
    return sorted(lst, key=lambda r: tuple(ORDRE.get(r[c], 99) if c == "systeme" else r[c] for c in cles))

TABLES = OrderedDict()
RG = D["regions"]; VO = D["volets"]
TABLES["t-an"] = {"tete": ["Système", "Région", "Volet", "Structure", "Lien clinique utile à l'examen", "Niveau"], "merge": [0, 1],
                  "rows": [ligne([sysc(a["systeme"]), T(RG[a["region"]]), T(VO[a["volet"]]), T(a["structure"]), T(a["lien"]), NIV[a["niveau"]]],
                                 a["systeme"], a["niveau"], [a["systeme"], a["systeme"] + a["region"]])
                           for a in sorted(D["anatomie"], key=lambda a: (ORDRE[a["systeme"]], list(RG).index(a["region"])))]}
TABLES["t-phy"] = {"tete": ["Système", "Volet", "Fonction", "Mécanisme et lien clinique", "Niveau"], "merge": [0, 1],
                   "rows": [ligne([sysc(a["systeme"]), T(VO[a["volet"]]), T(a["fonction"]), T(a["mecanisme_lien"]), NIV[a["niveau"]]],
                                  a["systeme"], a["niveau"], [a["systeme"], a["systeme"] + a["volet"]])
                            for a in sorted(D["physiologie"], key=lambda a: (ORDRE[a["systeme"]], a["volet"] != "P"))]}
TABLES["t-pp"] = {"tete": ["Système", "Mécanisme (VITE DIT CAFé)", "Chaîne causale", "Affections archétypes", "Niveau"], "merge": [0],
                  "rows": [ligne([sysc(a["systeme"]), f'<b>{E(a["lettre"])}</b> {E(a["mecanisme_nom"])}', T(a["mecanisme"]), L(a["affections"]), NIV[a["niveau"]]],
                                 a["systeme"], a["niveau"], [a["systeme"]]) for a in D["physiopathologie"]]}
A = D["semiologie"]["A"]
TABLES["t-atr"] = {"tete": ["Étape", "Ce que le candidat fait", "Référence PROFILES"], "merge": [], "nofilter": True,
                   "rows": [ligne([T(e["etape"]), T(e["contenu"]), T(e["ref"])], "T", "m", []) for e in A[0]["etapes"]]}
TABLES["t-asp"] = {"tete": ["Anamnèse spécifique", "Contenu", "Référence", "Niveau"], "merge": [],
                   "rows": [ligne([T(a["titre"]), T(a["contenu"]), T(a["ref"]), NIV[a["niveau"]]], a["systeme"], a["niveau"], [])
                            for a in A if a["type"] == "specifique"]}
TABLES["t-amo"] = {"tete": ["Système", "SSP", "Motif de consultation", "Questions clés", "Drapeaux rouges", "Niveau"], "merge": [0],
                   "rows": [ligne([sysc(a["systeme"]), E(a["ssp"]), T(a["titre"]), T(a["questions"]), T(a["drapeaux_rouges"]), NIV[a["niveau"]]],
                                  a["systeme"], a["niveau"], [a["systeme"]])
                            for a in tri([a for a in A if a["type"] == "motif"], "systeme")]}
S = D["semiologie"]["S"]
TABLES["t-sst"] = {"tete": ["N°", "Région ou système (ordre cranio-caudal)", "Manœuvres", "Signes recherchés", "EPA", "En CS", "Niveau"], "merge": [],
                   "rows": [ligne([E(s["id"]), f'{T(s["titre"])}<br><small>{sysc(s["systeme"])}</small>', T(s["manoeuvres"]), T(s["signes"]), E(s["epa"]), T(s["cs"] or "réalisé"), NIV[s["niveau"]]],
                                  s["systeme"], s["niveau"], []) for s in S if s["type"] == "status"]}
TABLES["t-ssy"] = {"tete": ["Système", "Syndrome clinique", "Symptômes", "Signes", "Niveau"], "merge": [0],
                   "rows": [ligne([sysc(s["systeme"]), T(s["titre"]), L(s["symptomes"]), L(s["signes"]), NIV[s["niveau"]]], s["systeme"], s["niveau"], [s["systeme"]])
                            for s in tri([s for s in S if s["type"] == "syndrome"], "systeme")]}
TABLES["t-m"] = {"tete": ["N°", "Schéma de prise en charge", "Ce qui est attendu", "Référence", "Niveau"], "merge": [],
                 "rows": [ligne([E(m["id"]), T(m["titre"]), T(m["contenu"]), T(m["ref"]), NIV[m["niveau"]]], "T", m["niveau"], []) for m in D["semiologie"]["M"]]}
TABLES["t-kk"] = {"tete": ["N°", "Dimension ou situation", "Comportement attendu", "Référence", "Niveau"], "merge": [],
                  "rows": [ligne([E(m["id"]), T(m["titre"]), T(m["contenu"]), T(m["ref"]), NIV[m["niveau"]]], "T", m["niveau"], []) for m in D["semiologie"]["KK"]]}
TABLES["t-tr"] = {"tete": ["Discipline", "Notion", "Contenu et application", "Niveau"], "merge": [0],
                  "rows": [ligne([T(t["discipline"]), T(t["notion"]), T(t["contenu"]), NIV[t["niveau"]]], "T", t["niveau"], [t["discipline"]]) for t in D["transversales"]]}

# ---------------------------------------------------------------- comptages
def cnt(lst):
    return sum(1 for x in lst if x["niveau"] == "m"), len(lst)

SEM = D["semiologie"]
GROUPES = OrderedDict([
    ("Anatomie", D["anatomie"]), ("Physiologie", D["physiologie"]), ("Physiopathologie", D["physiopathologie"]),
    ("Sémiologie A", SEM["A"]), ("Sémiologie S", SEM["S"]), ("Sémiologie M", SEM["M"]), ("Sémiologie KK", SEM["KK"]),
    ("Transversales", D["transversales"])])
EXI = {k: len(v) for k, v in D["existant"]["par_sous_onglet"].items()}
EXI_MAP = {"Anatomie": EXI.get("anatomie", 0), "Physiologie": EXI.get("physiologie", 0), "Physiopathologie": EXI.get("physiopathologie", 0),
           "Transversales": EXI.get("transversales", 0)}
TOT_M = sum(cnt(v)[0] for v in GROUPES.values()); TOT_C = sum(cnt(v)[1] for v in GROUPES.values())


def exi_sys(code, cle):
    return sum(1 for n in D["existant"]["par_sous_onglet"].get(cle, []) if n.startswith(f"SF-{code}-"))


def tableau_totaux():
    lignes = ""
    for nom, lst in GROUPES.items():
        m, c = cnt(lst); e = EXI_MAP.get(nom, 0)
        lignes += f"<tr><td>{T(nom)}</td><td>{m}</td><td>{c}</td><td>{e}</td><td>+{m - e} à +{c - e}</td></tr>"
    lignes += f'<tr class="tot"><td>Total</td><td>{TOT_M}</td><td>{TOT_C}</td><td>{D["existant"]["total"]}</td><td>+{TOT_M - D["existant"]["total"]} à +{TOT_C - D["existant"]["total"]}</td></tr>'
    return ('<div class="tw court"><table class="t s"><thead><tr><th>Sous-onglet</th><th>Minimum</th><th>Cible</th><th>Squelettes existants</th><th>Écart brut</th></tr></thead>'
            f"<tbody>{lignes}</tbody></table></div>")


def tableau_systemes():
    cols = [("Anatomie", D["anatomie"], "anatomie"), ("Physiologie", D["physiologie"], "physiologie"), ("Physiopathologie", D["physiopathologie"], "physiopathologie"),
            ("Sémiologie A", SEM["A"], None), ("Sémiologie S", SEM["S"], None)]
    tete = "".join(f"<th>{T(n)}<br><small>min / cible</small></th>" for n, _, _ in cols)
    corps = ""
    for code, nom in SYSN.items():
        cel, tm, tc, te = "", 0, 0, 0
        for _, lst, cle in cols:
            sub = [x for x in lst if x["systeme"] == code]
            m, c = cnt(sub); tm += m; tc += c
            if cle: te += exi_sys(code, cle)
            cel += f"<td>{m} / {c}</td>"
        if code == "T":
            m, c = cnt(SEM["M"] + SEM["KK"] + D["transversales"]); tm += m; tc += c; te += exi_sys("T", "transversales")
            nomaff = nom + " (dont M, KK et transversales)"
        else:
            nomaff = nom
        corps += f'<tr><td><abbr title="{E(nom)}">{E(code)}</abbr> {T(nomaff)}</td>{cel}<td><b>{tm} / {tc}</b></td><td>{te}</td></tr>'
    return (f'<div class="tw court"><table class="t s"><thead><tr><th>Système</th>{tete}<th>Total</th><th>Squelettes</th></tr></thead><tbody>{corps}</tbody></table></div>'
            '<p class="note">La ligne T additionne la trame et les fiches A et S transversales, les sous-onglets M et KK (non rattachés à un système) et les sciences transversales.</p>')


def grille_vite():
    tete = "".join(f'<th><abbr title="{E(n)}">{E(c)}</abbr></th>' for c, n in VITE.items())
    corps = ""
    for code in SYSN:
        if code == "T": continue
        cel = ""
        for c in VITE:
            f = next(x for x in D["physiopathologie"] if x["systeme"] == code and x["lettre"] == c)
            cel += f'<td title="{E(", ".join(f["affections"]))}">{"●" if f["niveau"] == "m" else "○"}</td>'
        corps += f'<tr><td><abbr title="{E(SYSN[code])}">{E(code)}</abbr></td>{cel}</tr>'
    return (f'<div class="tw court"><table class="t g"><thead><tr><th>Système</th>{tete}</tr></thead><tbody>{corps}</tbody></table></div>'
            '<p class="note">● case du minimum indispensable ; ○ case de la cible complète. Le survol d\'une case affiche ses affections archétypes.</p>')


def filtres(tid, avec_sys=True):
    sel = ""
    if avec_sys:
        opts = "".join(f'<option value="{c}">{E(c)} {E(n)}</option>' for c, n in SYSN.items())
        sel = f'<label>Système<select data-f="s" data-t="{tid}"><option value="">tous</option>{opts}</select></label>'
    return (f'<div class="filt">{sel}<label>Niveau<select data-f="n" data-t="{tid}"><option value="">minimum et cible</option><option value="m">minimum seulement</option></select></label>'
            f'<label class="grow">Recherche<input type="search" data-f="q" data-t="{tid}" placeholder="mot, signe, SSP…"></label>'
            f'<p class="live" id="c-{tid}" aria-live="polite"></p></div>')


def bloc_table(tid, avec_sys=True):
    t = TABLES[tid]
    tete = "".join(f"<th>{T(h)}</th>" for h in t["tete"])
    f = "" if t.get("nofilter") else filtres(tid, avec_sys)
    return f'{f}<div class="tw"><table class="t" id="{tid}"><thead><tr>{tete}</tr></thead><tbody></tbody></table></div>'


def tableau_simple(tete, lignes):
    th = "".join(f"<th>{T(h)}</th>" for h in tete)
    tb = "".join("<tr>" + "".join(f"<td>{T(c)}</td>" for c in l) + "</tr>" for l in lignes)
    return f'<div class="tw court"><table class="t"><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div>'


def schemas_html():
    out = ""
    noms = {"anatomie": "1 Anatomie", "physiologie": "2 Physiologie", "physiopathologie": "3 Physiopathologie", "semiologie_A": "4 Sémiologie · A Anamnèse",
            "semiologie_S": "4 Sémiologie · S Status (exemple : status cardiovasculaire)", "semiologie_M": "4 Sémiologie · M Management",
            "semiologie_KK": "4 Sémiologie · KK Communication", "transversales": "5 Sciences transversales"}
    for k, v in D["schemas"].items():
        champs = "".join(f"<li><code>{E(c)}</code> : {T(json.dumps(d, ensure_ascii=False) if not isinstance(d, str) else d)}</li>" for c, d in v["champs"].items())
        out += (f'<h3>{T(noms[k])}</h3><details class="card"><summary>Champs du schéma</summary><ul class="champs">{champs}</ul></details>'
                f'<details class="card"><summary>Exemple rempli : {E(v["exemple"].get("id"))}</summary><pre>{E(json.dumps(v["exemple"], ensure_ascii=False, indent=1))}</pre></details>')
    return out


# ---------------------------------------------------------------- page
FC = D["format_cs"]
sources = "".join(f'<li><b>{E(s["id"])}</b> — <a href="{E(s["url"])}" rel="noopener">{T(s["titre"])}</a>. Lu le {E(s["lu"])}. {T(s["apport"])}</li>' for s in D["sources"])
nA = cnt(SEM["A"]); nS = cnt(SEM["S"]); nM = cnt(SEM["M"]); nK = cnt(SEM["KK"])
sem_m = nA[0] + nS[0] + nM[0] + nK[0]; sem_c = nA[1] + nS[1] + nM[1] + nK[1]
ssp_cites = set()
for a in SEM["A"]:
    for x in str(a.get("ssp", "")).split(","):
        if x.strip().isdigit(): ssp_cites.add(int(x))

ONGLETS = [("cadre", "Cadre et totaux"), ("an", "1 Anatomie"), ("phy", "2 Physiologie"), ("pp", "3 Physiopathologie"), ("sem", "4 Sémiologie"),
           ("tr", "5 Transversales"), ("archi", "Architecture"), ("src", "Sources")]
boutons = "".join(f'<button type="button" role="tab" id="o-{c}" aria-controls="p-{c}" aria-selected="{"true" if i == 0 else "false"}">{E(n)}</button>' for i, (c, n) in enumerate(ONGLETS))

def panel(c, contenu, cache=True):
    return f'<section class="panel" role="tabpanel" id="p-{c}" aria-labelledby="o-{c}"{" hidden" if cache else ""}>{contenu}</section>'

def entete(nom, lst):
    m, c = cnt(lst)
    return f'<p class="compte">Ce sous-onglet compte <b>{m}</b> fiches au minimum indispensable et <b>{c}</b> fiches dans la cible complète.</p>'

P_CADRE = f"""
<h2>Format officiel de l'examen fédéral (vérifié le {E(FC["verifie_le"])})</h2>
{tableau_simple(["Point", "Ce que disent les textes 2026", "Source"], FC["points"])}
<h2>Objectifs PROFILES utilisés comme index</h2>
<p>PROFILES 2017 fonde l'examen jusqu'en 2027 : il définit <b>7 rôles</b> (General Objectives), <b>9 <abbr title="{E(SIG["EPA"])}">EPA</abbr></b> et <b>265 <abbr title="{E(SIG["SSP"])}">SSP</abbr></b>. Le recensement indexe donc les motifs d'anamnèse sur les SSP ({len(ssp_cites)} SSP citées) et le status sur les gestes EPA 2a–2mm. PROFILES 2 (248 SSP) prendra le relais à l'examen 2028 ; il faudra alors renuméroter.</p>
<h2>Règle de comptage</h2>
{tableau_simple(["Sous-onglet", "Règle"], D["regle_comptage"])}
<h2>Totaux par sous-onglet</h2>
<p>Le recensement prévoit <b>{TOT_M}</b> fiches au minimum et <b>{TOT_C}</b> dans la cible ; les 62 squelettes existants sont vides, si bien que tout reste à rédiger ; la Sémiologie, absente de l'existant, représente à elle seule {sem_m} à {sem_c} fiches.</p>
{tableau_totaux()}
<h2>Totaux par système</h2>
{tableau_systemes()}
<p class="note">{T(D["meta"]["honnetete"])}</p>
"""
P_AN = f'<h2>1 Anatomie : région et système × structure × lien clinique</h2>{entete("an", D["anatomie"])}<p>Chaque ligne relie une structure à la conséquence clinique que l\'examen interroge ; l\'histologie et l\'embryologie apparaissent comme volets, parce qu\'elles expliquent une maladie précise.</p>{bloc_table("t-an")}'
P_PHY = f'<h2>2 Physiologie : fonction × mécanisme × lien clinique</h2>{entete("phy", D["physiologie"])}<p>Chaque fonction est décrite par sa régulation, puis par l\'erreur clinique qu\'elle permet d\'éviter ; le volet biochimie regroupe les voies métaboliques à conséquence clinique.</p>{bloc_table("t-phy")}'
P_PP = f'<h2>3 Physiopathologie : système × VITE DIT CAFé</h2>{entete("pp", D["physiopathologie"])}<p>La grille croise 12 systèmes et 9 mécanismes (<b>V</b>asculaire, <b>I</b>nfectieux, <b>T</b>umoral, <b>D</b>égénératif, <b>I</b>atrogène, <b>T</b>raumatique, <b>C</b>ongénital, <b>A</b>uto-immun, <b>F</b>onctionnel ou métabolique) ; chaque case donne la chaîne causale, puis les affections qui l\'illustrent.</p><h3>Carte des 108 cases</h3>{grille_vite()}<h3>Détail des cases</h3>{bloc_table("t-pp")}'
P_SEM = f"""
<h2>4 Sémiologie : préparation de la partie CS</h2>
<p class="compte">La sémiologie compte <b>{sem_m}</b> fiches au minimum et <b>{sem_c}</b> dans la cible. Elle suit la grille officielle : le domaine <abbr title="{E(SIG["ASM"])}">ASM</abbr> (75 %) se prépare en A, S et M ; le domaine <abbr title="{E(SIG["KK"])}">KK</abbr> (25 %) en KK.</p>
<div class="soustabs" role="tablist" aria-label="Volets de la sémiologie">
<button type="button" role="tab" data-sub="sa" aria-selected="true">A Anamnèse ({nA[0]}–{nA[1]})</button>
<button type="button" role="tab" data-sub="ss" aria-selected="false">S Status ({nS[0]}–{nS[1]})</button>
<button type="button" role="tab" data-sub="sm" aria-selected="false">M Management ({nM[0]}–{nM[1]})</button>
<button type="button" role="tab" data-sub="sk" aria-selected="false">KK Communication ({nK[0]}–{nK[1]})</button>
</div>
<div class="sub" id="sa"><h3>A1 Trame générale d'anamnèse (1 fiche)</h3>{bloc_table("t-atr")}
<h3>A2 Anamnèses spécifiques PROFILES (EPA 1a–1g)</h3>{bloc_table("t-asp", False)}
<h3>A3 Motifs de consultation indexés sur les SSP</h3><p>Le candidat ouvre par une question ouverte, puis il précise le symptôme et cherche les drapeaux rouges ; chaque motif renvoie au status ciblé et au syndrome correspondant.</p>{bloc_table("t-amo")}</div>
<div class="sub" id="ss" hidden><h3>S1 Status cranio-caudal, région par région</h3><p>Le candidat suit l'ordre de la tête aux pieds, puis complète par système ; il verbalise les examens intimes, le réflexe cornéen et le réflexe nauséeux (INFO26 ch. 5).</p>{bloc_table("t-sst")}
<h3>S2 Syndromes cliniques : symptômes et signes énumérés</h3>{bloc_table("t-ssy")}</div>
<div class="sub" id="sm" hidden><h3>M Management attendu en station</h3><p>La grille ASM récompense chaque élément correct et ne retire jamais de point ; le candidat a donc intérêt à nommer explicitement chaque étape.</p>{bloc_table("t-m", False)}</div>
<div class="sub" id="sk" hidden><h3>KK Communication selon la grille officielle</h3><p>L'examinateur note 4 dimensions de 1 à 5 sur toute la station ; les fiches K-01 à K-04 reprennent ces dimensions, les suivantes les techniques qui les nourrissent.</p>{bloc_table("t-kk", False)}</div>
"""
P_TR = f'<h2>5 Sciences transversales à plus-value</h2>{entete("tr", D["transversales"])}<p>Ces notions servent à la fois au QCM (calculs, mécanismes) et à la station (prescription, interprétation d\'un test) ; elles complètent les 4 squelettes transversaux existants.</p>{bloc_table("t-tr", False)}'
ar = D["architecture"]
P_ARCHI = f"""
<h2>Architecture proposée</h2>
<h3>Sous-onglets</h3>{tableau_simple(["Sous-onglet", "Contenu", "Filtres"], [[s["nom"], s["contenu"], ", ".join(s["filtres"])] for s in ar["sous_onglets"]])}
<h3>Passerelles</h3>{tableau_simple(["Lien", "Fonctionnement"], ar["passerelles"])}
<h3>Migration des 62 squelettes</h3>{tableau_simple(["Squelettes", "Devenir"], ar["migration_squelettes"])}
<h2>Schémas JSON de fiche, avec un exemple rempli par sous-onglet</h2>{schemas_html()}
"""
P_SRC = f'<h2>Sources officielles lues et datées</h2><ol class="src">{sources}</ol><p class="note">Toute affirmation sans source suisse lue porte la mention « (non vérifié CH) » ; la trame d\'anamnèse et SPIKES n\'ont pas de source suisse officielle trouvée à ce jour.</p>'

DATA = {k: {"merge": v["merge"], "rows": v["rows"]} for k, v in TABLES.items()}

PAGE = f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Recensement Sciences fondamentales</title>
<style>
:root{{--h1:#0d3b8c;--h2:#a3122a;--h3:#0f6b4f;--h4:#6b3fa0;--ligne:#d4d4d4}}
*{{box-sizing:border-box}}
html{{-webkit-text-size-adjust:100%}}
body{{margin:0;background:#fff;color:#000;font:16px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;overflow-x:hidden}}
header{{padding:20px 16px 8px;max-width:1400px;margin:0 auto}}
h1{{color:var(--h1);margin:0 0 6px;font-size:clamp(1.35rem,3.4vw,2rem);line-height:1.2}}
h2{{color:var(--h2);font-size:1.3rem;margin:26px 0 10px;line-height:1.25}}
h3{{color:var(--h3);font-size:1.1rem;margin:22px 0 8px}}
summary,h4{{color:var(--h4);font-weight:700}}
main{{max-width:1400px;margin:0 auto;padding:0 16px 40px}}
p{{max-width:95ch}}
abbr[title]{{text-decoration:underline dotted;cursor:help}}
a{{color:#000}}
.tabs{{display:flex;flex-wrap:wrap;gap:6px;position:sticky;top:0;background:#fff;padding:8px 0;border-bottom:2px solid var(--h2);z-index:5}}
.tabs button,.soustabs button{{font:inherit;font-weight:700;background:#fff;color:var(--h2);border:2px solid var(--h2);border-radius:6px;padding:5px 10px;cursor:pointer}}
.tabs button[aria-selected=true]{{background:var(--h2);color:#fff}}
.soustabs{{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0}}
.soustabs button{{color:var(--h3);border-color:var(--h3)}}
.soustabs button[aria-selected=true]{{background:var(--h3);color:#fff}}
.panel[hidden],.sub[hidden]{{display:none}}
.tw{{max-width:100%;overflow:auto;max-height:75vh;border:1px solid var(--ligne)}}
.tw.court{{max-height:none}}
table.t{{border-collapse:collapse;width:100%;min-width:640px;font-size:.93rem}}
table.t th,table.t td{{border:1px solid var(--ligne);padding:6px 8px;text-align:left;vertical-align:top}}
table.t thead th{{background:#fff;color:#000;position:sticky;top:0;z-index:2;box-shadow:inset 0 -2px 0 #000}}
table.s td:nth-child(n+2),table.s th:nth-child(n+2){{text-align:right;font-variant-numeric:tabular-nums}}
table.g{{min-width:0}} table.g td{{text-align:center}}
tr.tot td{{font-weight:800;border-top:2px solid #000}}
td ul{{margin:0;padding-left:18px}}
.filt{{display:flex;flex-wrap:wrap;gap:8px 12px;align-items:flex-end;margin:8px 0;border:1px solid #000;padding:8px 10px}}
.filt label{{display:flex;flex-direction:column;font-size:.85rem;font-weight:600;min-width:0}}
.filt .grow{{flex:1 1 200px}}
select,input[type=search]{{font:inherit;padding:5px 7px;border:1px solid #000;background:#fff;color:#000;max-width:100%}}
.live{{margin:0;flex-basis:100%}}
.note{{font-size:.88rem}}
.card{{border:1px solid var(--ligne);padding:8px 12px;margin:8px 0}}
pre{{white-space:pre-wrap;word-break:break-word;font-size:.82rem;margin:8px 0 0}}
ul.champs code{{font-weight:700}}
ol.src li{{margin:8px 0}}
@media (max-width:640px){{table.t{{font-size:.86rem}}}}
</style></head>
<body>
<header><h1>Recensement croisé des Sciences fondamentales</h1>
<p>Ce recensement prépare la restructuration de l'onglet « Sciences fondamentales » de progression.html avant toute rédaction. Il croise systèmes, structures, fonctions, mécanismes VITE DIT CAFé et la grille officielle de la partie <abbr title="{E(SIG["CS"])}">CS</abbr> ; il compte {TOT_M} fiches au minimum et {TOT_C} dans la cible (état du {E(D["meta"]["date"])}).</p></header>
<main>
<nav class="tabs" role="tablist" aria-label="Sous-onglets">{boutons}</nav>
{panel("cadre", P_CADRE, False)}{panel("an", P_AN)}{panel("phy", P_PHY)}{panel("pp", P_PP)}{panel("sem", P_SEM)}{panel("tr", P_TR)}{panel("archi", P_ARCHI)}{panel("src", P_SRC)}
</main>
<script id="donnees" type="application/json">{json.dumps(DATA, ensure_ascii=False).replace("</", "<\\/")}</script>
<script>
(function(){{
var D=JSON.parse(document.getElementById('donnees').textContent);
var F={{}};
function rendre(id){{
  var t=D[id],f=F[id]||{{}},tb=document.querySelector('#'+id+' tbody');
  var q=(f.q||'').toLowerCase().trim();
  var rows=t.rows.filter(function(r){{return (!f.s||r.s===f.s)&&(!f.n||r.n===f.n)&&(!q||r.q.indexOf(q)>=0);}});
  var span={{}};
  t.merge.forEach(function(ci,mi){{
    var i=0;while(i<rows.length){{var j=i+1;while(j<rows.length&&rows[j].k[mi]===rows[i].k[mi])j++;span[i+'_'+ci]=j-i;for(var x=i+1;x<j;x++)span[x+'_'+ci]=0;i=j;}}
  }});
  var h='';
  rows.forEach(function(r,i){{
    h+='<tr>';
    r.c.forEach(function(c,ci){{
      var s=span[i+'_'+ci];
      if(s===0)return;
      h+='<td'+(s>1?' rowspan="'+s+'"':'')+'>'+c+'</td>';
    }});
    h+='</tr>';
  }});
  tb.innerHTML=h||'<tr><td colspan="'+(t.rows[0]?t.rows[0].c.length:1)+'">Aucune fiche ne correspond aux filtres.</td></tr>';
  var c=document.getElementById('c-'+id);
  if(c){{var m=rows.filter(function(r){{return r.n==='m';}}).length;c.textContent=rows.length+' fiches affichées sur '+t.rows.length+', dont '+m+' au minimum indispensable.';}}
}}
Object.keys(D).forEach(rendre);
document.querySelectorAll('[data-f]').forEach(function(el){{
  el.addEventListener('input',function(){{var id=el.dataset.t;F[id]=F[id]||{{}};F[id][el.dataset.f]=el.value;rendre(id);}});
}});
var tabs=document.querySelectorAll('.tabs [role=tab]');
tabs.forEach(function(b){{b.addEventListener('click',function(){{
  tabs.forEach(function(x){{x.setAttribute('aria-selected',x===b?'true':'false');document.getElementById(x.getAttribute('aria-controls')).hidden=(x!==b);}});
  try{{localStorage.setItem('sf-onglet',b.id);}}catch(e){{}}
}});}});
var subs=document.querySelectorAll('.soustabs [data-sub]');
subs.forEach(function(b){{b.addEventListener('click',function(){{
  subs.forEach(function(x){{x.setAttribute('aria-selected',x===b?'true':'false');document.getElementById(x.dataset.sub).hidden=(x!==b);}});
}});}});
try{{var o=localStorage.getItem('sf-onglet');if(o&&document.getElementById(o))document.getElementById(o).click();}}catch(e){{}}
}})();
</script>
</body></html>"""
open(SORTIE, "w", encoding="utf-8").write(PAGE)
print("écrit", SORTIE, len(PAGE.encode()) // 1024, "Ko ;", TOT_M, "minimum,", TOT_C, "cible")
