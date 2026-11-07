#!/usr/bin/env python3
"""État des lieux du chantier production-v2, sans appel à un modèle.

Usage : python3 harnais/etat_des_lieux.py [sortie]
Sortie par défaut : LOT_Claude_Finaux/ETAT_DES_LIEUX.html
Lit RAPPORT_QUALITE.json, ETAT_FILE.json, audits/*.jsonl, journal/, JOURNAL.md et git.
"""
import collections, datetime, glob, html, json, os, re, subprocess, sys
from zoneinfo import ZoneInfo

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIN = os.path.join(REPO, "LOT_Claude_Finaux")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(FIN, "ETAT_DES_LIEUX.html")
TZ = ZoneInfo("Europe/Zurich")
H = lambda s: html.escape(str(s), quote=True)


def fr(n, d=0):
    return f"{n:,.{d}f}".replace(",", " ").replace(".", ",")


def git(*a):
    try:
        return subprocess.run(["git", "-C", REPO, *a], capture_output=True, text=True, timeout=30).stdout.strip()
    except Exception:
        return ""


def jsonl(p):
    if not os.path.exists(p):
        return []
    out = []
    for x in open(p, encoding="utf-8"):
        x = x.strip()
        if x:
            try:
                out.append(json.loads(x))
            except ValueError:
                pass
    return out


def hm(dt):
    return f"{int(dt.total_seconds() // 3600)} h {int(dt.total_seconds() % 3600 // 60):02d}"


rq = json.load(open(os.path.join(FIN, "RAPPORT_QUALITE.json"), encoding="utf-8"))
etat = json.load(open(os.path.join(FIN, "ETAT_FILE.json"), encoding="utf-8"))["lots"]
rout = jsonl(os.path.join(REPO, "journal", "routage.jsonl"))
now = datetime.datetime.now(TZ)

# ---------- JOURNAL.md : chronologie, dépôts, début ----------
journal = []
for line in open(os.path.join(REPO, "JOURNAL.md"), encoding="utf-8"):
    m = re.match(r"\|\s*(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2})\s*\|\s*(.+?)\s*\|", line)
    if m:
        txt = re.sub(r"[*`]", "", m.group(3))
        journal.append((datetime.datetime.fromisoformat(f"{m.group(1)}T{m.group(2)}").replace(tzinfo=TZ), txt))
depots = {}
for t, txt in journal:
    m = re.match(r"(LOT_\d{3}) déposé", txt)
    if m and m.group(1) not in depots:
        depots[m.group(1)] = t
debut = next((t for t, txt in journal if txt.startswith("Production")), journal[0][0] if journal else now)

# ---------- file ----------
cnt = collections.Counter(l["statut_audit"] for l in etat)
acc, enc, tot = cnt["ACCEPTE"], cnt["EN_COURS"], len(etat)
todo = tot - acc - enc
fam = [("G", "G · Généralités"), ("S", "S · Symptômes"), ("F", "F · Résultats anormaux"), ("O", "O · Situations et demandes")]
cells = collections.defaultdict(list)
for l in etat:
    cells[l["code"][0]].append(l)


def grid_svg(items):
    per, c, g = 40, 11, 2
    rows = (len(items) + per - 1) // per
    out = [f'<svg viewBox="0 0 {per*(c+g)} {rows*(c+g)}" class="grid" role="img" aria-label="{len(items)} LOTS">']
    for i, l in enumerate(items):
        cls = {"ACCEPTE": "c-ok", "EN_COURS": "c-run"}.get(l["statut_audit"], "c-todo")
        lab = f'LOT_{l["lot"]} · {l["code"]} · ' + {"ACCEPTE": "accepté", "EN_COURS": "en cours"}.get(l["statut_audit"], "à traiter")
        out.append(f'<rect x="{(i%per)*(c+g)}" y="{(i//per)*(c+g)}" width="{c}" height="{c}" rx="2" class="{cls}"><title>{H(lab)}</title></rect>')
    return "".join(out) + "</svg>"


grids = "".join(
    f'<div class="fam"><div class="fam-h"><span>{H(lbl)}</span><span class="num">'
    f'{sum(1 for l in cells[k] if l["statut_audit"]=="ACCEPTE")}/{len(cells[k])}</span></div>{grid_svg(cells[k])}</div>'
    for k, lbl in fam if cells[k])
cat = {}
catp = os.path.join(FIN, "CATALOGUE_248.csv")
if os.path.exists(catp):
    import csv
    for row in csv.DictReader(open(catp, encoding="utf-8")):
        cat[row["lot"]] = row["ssp_profiles_2023_fr_en"].split(" | ")[0]
encl = [l for l in etat if l["statut_audit"] == "EN_COURS"]
suiv = next((l for l in etat if l["statut_audit"] == "A_TRAITER"), None)
next_lot = (f'Prochain LOT : LOT_{suiv["lot"]}, {suiv["code"]} {H(cat.get(suiv["lot"], ""))}.' if suiv else "File terminée.")

# ---------- LOTS du chantier ----------
etat_by = {"LOT_" + l["lot"]: l for l in etat}
lots = []
for L in rq["lots"]:
    g = collections.Counter(); t = collections.Counter(); av = collections.defaultdict(list); ap = collections.defaultdict(list)
    for l in L["lecons"]:
        g.update(l.get("gravite", {})); t.update(l.get("type", {}))
        for k, v in (l.get("avant") or {}).items(): av[k].append(v)
        for k, v in (l.get("apres") or {}).items(): ap[k].append(v)
    oc = [l["octets"] for l in L["lecons"] if l.get("octets")]
    e = etat_by.get(L["lot"], {})
    lots.append(dict(lot=L["lot"], L=L, g=g, t=t, n=len(L["lecons"]), depose=bool(e.get("depose")), code=e.get("code", ""),
                     av={k: sum(v)/len(v) for k, v in av.items()}, ap={k: sum(v)/len(v) for k, v in ap.items()},
                     kmin=min(oc)/1000 if oc else 0, kmax=max(oc)/1000 if oc else 0))
deps = [d for d in lots if d["depose"]]
starts = {}
prev = debut
for d in lots:
    starts[d["lot"]] = prev
    if d["lot"] in depots:
        prev = depots[d["lot"]]
durees = [depots[d["lot"]] - starts[d["lot"]] for d in deps if d["lot"] in depots]

rows = []
for d in lots:
    g = d["g"]
    st = '<span class="pill ok">Déposé · accepté</span>' if d["depose"] else '<span class="pill run">En cours</span>'
    nom = cat.get(d["lot"][4:], "")
    if d["lot"] in depots:
        dep = f'<span class="num">{depots[d["lot"]]:%H:%M}</span> · {hm(depots[d["lot"]] - starts[d["lot"]])}'
    else:
        dep = f'en cours depuis {hm(now - starts[d["lot"]])}'
    mm = d["L"]["minimum"].get("score_medical")
    rows.append(
        f'<tr><th scope="row"><span class="mono">{d["lot"]}</span><br><span class="sub">{H(d["code"])} · {H(nom)}</span></th><td>{st}</td>'
        f'<td class="num">{d["L"]["achevees"]}/{d["L"]["attendues"]}</td><td class="num">{fr(d["kmin"])}–{fr(d["kmax"])}</td>'
        f'<td class="num">{fr(sum(g.values()))}</td><td class="num">{g.get("critique", 0) or "·"}</td><td class="num">{g.get("grave", 0)}</td>'
        f'<td class="num">{fr(d["av"].get("score_medical", 0), 1)} → <b>{fr(d["ap"].get("score_medical", 0), 1)}</b></td>'
        f'<td class="num">{fr(mm or 0)}</td><td>{dep}</td></tr>')
lot_table = "".join(rows)

# ---------- LOT en cours : pipeline ----------
encours_titre, pipe_html, enc_lot = "Aucun LOT en cours", "", None
if encl:
    enc_lot = "LOT_" + encl[0]["lot"]
    D = os.path.join(REPO, "lot en cours de production", enc_lot)
    encours_titre = f'{enc_lot} en direct · {encl[0]["code"]} {H(cat.get(encl[0]["lot"], ""))}'
    sc = collections.defaultdict(list)
    for s in jsonl(os.path.join(FIN, enc_lot, "audits", "scores.jsonl")):
        sc[s.get("lecon")].append(s)
    co = collections.Counter(c.get("lecon", "").split(" — ")[0] for c in jsonl(os.path.join(FIN, enc_lot, "audits", "corrections.jsonl")))
    noms = {}
    lp = os.path.join(D, "LISTE_DX_CANONIQUE.md")
    if os.path.exists(lp):
        for line in open(lp, encoding="utf-8"):
            m = re.match(r"DX\.(\d+) — (.+)", line.strip())
            if m: noms[int(m.group(1))] = m.group(2)
    lances = {(x.get("fichier"), x.get("agent")) for x in rout if x.get("lot") == enc_lot}

    def ligne(lbl, lecon, nom, f):
        n = h3 = 0; fin = False
        if os.path.exists(f):
            t = open(f, encoding="utf-8").read(); n = len(t.encode()); fin = "FIN_FICHIER" in t
            h3 = len(re.findall(r'<h3 id="(?:dx\d+|ssp)-p\d+"', t))
        ags = [s.get("auditeur", {}).get("agent", "") if isinstance(s.get("auditeur"), dict) else str(s.get("auditeur", "")) for s in sc.get(lecon, [])]
        med = any("medical" in a for a in ags); conf = any("conformite" in a for a in ags)
        if med and conf: stage, cls = "Audits médical + conformité faits", "ok"
        elif med: stage, cls = ("Audit de conformité en cours" if (lecon, "auditeur-conformite") in lances else "Audit médical fait · conformité à lancer"), "run"
        elif fin: stage, cls = ("Audit médical en cours" if (lecon, "auditeur-medical") in lances else "Rédigé · audit médical à lancer"), "run"
        elif n: stage, cls = "Rédaction en cours", "run"
        else: stage, cls = "Recherche des sources", "todo"
        dern = sc.get(lecon, [])[-1]["apres"].get("score_medical") if sc.get(lecon) else None
        w = min(n / 150000 * 100, 100)
        return (f'<tr><th scope="row" class="mono">{lbl}</th><td>{H(nom)}</td><td><span class="pill {cls}">{stage}</span></td>'
                f'<td class="kb"><span class="kb-t"><span class="band"></span><span class="kb-f {cls}" style="width:{w:.1f}%"></span></span></td>'
                f'<td class="num">{fr(n/1000, 1) if n else "—"}</td><td class="num">{h3}/14</td><td class="num">{"oui" if fin else "non"}</td>'
                f'<td class="num">{co.get(lecon, 0) or "·"}</td><td class="num">{dern if dern is not None else "·"}</td></tr>'), (med and conf), fin

    rs = [ligne("Phase A", "Phase_A", "Monographie du SSP, liste DX, algorithme", os.path.join(D, f"{enc_lot}_Phase_A_V0.html"))]
    for i in range(1, 11):
        rs.append(ligne(f"DX.{i}", f"DX.{i}", noms.get(i, ""), os.path.join(D, f"{enc_lot}_Phase_B_V0_DX.{i}.html")))
    pipe_html = "".join(r[0] for r in rs)
    n_audites = sum(1 for r in rs if r[1]); n_rediges = sum(1 for r in rs if r[2])
    help_open = help_tot = 0
    for hp in glob.glob(os.path.join(D, "HELP*.md")):
        t = open(hp, encoding="utf-8").read()
        for blk in re.split(r"\n(?=## )", t):
            if blk.startswith("## "):
                help_tot += 1; help_open += 0 if re.search(r"CLOSE|FERMÉE|comblée", blk) else 1

# ---------- graphiques ----------
metrics = [("score_medical", "Médical"), ("score_pec", "Prise en charge"), ("score_examen", "Examen"), ("score_langue", "Langue*")]
W, LW, RW, x0, x1 = 440, 112, 34, 75, 100
sx = lambda v: LW + (max(min(v, x1), x0) - x0) / (x1 - x0) * (W - LW - RW)
db, y = [], 18
for mk, ml in metrics:
    db.append(f'<text x="0" y="{y+4}" class="ax-h">{ml}</text>'); y += 8
    for d in deps:
        a, b = d["av"].get(mk), d["ap"].get(mk)
        if a is None or b is None: continue
        y += 16
        db.append(f'<text x="{LW-8}" y="{y+4}" text-anchor="end" class="ax">{d["lot"][-3:]}</text>'
                  f'<line x1="{sx(a):.1f}" x2="{sx(b):.1f}" y1="{y}" y2="{y}" class="db-l"/>'
                  f'<circle cx="{sx(a):.1f}" cy="{y}" r="4.5" class="db-a"><title>{d["lot"]} {ml} avant : {fr(a,1)}</title></circle>'
                  f'<circle cx="{sx(b):.1f}" cy="{y}" r="5.5" class="db-b"><title>{d["lot"]} {ml} après : {fr(b,1)}</title></circle>'
                  f'<text x="{sx(b)+9:.1f}" y="{y+4}" class="val">{fr(b,1)}</text>')
    y += 16
ticks = "".join(f'<line x1="{sx(v):.1f}" x2="{sx(v):.1f}" y1="10" y2="{y-8}" class="gridl"/><text x="{sx(v):.1f}" y="{y+6}" text-anchor="middle" class="ax">{v}</text>' for v in range(x0, x1 + 1, 5))
dumbbell = f'<svg viewBox="0 0 {W} {y+12}" class="chart" role="img" aria-label="Scores moyens avant et après audit">{ticks}{"".join(db)}</svg>'

T = rq["totaux"]["par_type"]; tmax = max(T.values()) if T else 1
bars = "".join(f'<div class="hb"><span class="hb-l">{H(k.capitalize())}</span><span class="hb-t"><span class="hb-f{" hb-med" if k in ("dose","conduite","seuil","critère") else ""}" style="width:{v/tmax*100:.1f}%"></span></span><span class="hb-v num">{fr(v)}</span></div>' for k, v in sorted(T.items(), key=lambda x: -x[1]))
order = [("critique", "Critique"), ("grave", "Grave"), ("moyen", "Moyen"), ("léger", "Léger")]
stack = ""
for d in lots:
    g = d["g"]
    segs = "".join(f'<span class="sg sg-{gk.replace("é","e")}" style="flex-grow:{g[gk]}" title="{gl} : {g[gk]}"></span>' for gk, gl in order if g.get(gk))
    det = " · ".join(f'{gl.lower()} {g[gk]}' for gk, gl in order if g.get(gk))
    stack += f'<div class="stk"><span class="stk-l mono">{d["lot"][-3:]}</span><span class="stk-b">{segs}</span><span class="stk-v num">{fr(sum(g.values()))}</span></div><div class="stk-d">{det}</div>'

crit = [(L["lot"], c) for L in rq["lots"] for c in L.get("critiques", [])]
crit_html = "".join(
    f'<li><div class="cr-h"><span class="pill crit">Critique · corrigée</span><span class="mono">{H(lot)} · {H(c.get("lecon",""))}</span>'
    f'<span class="sub">{H(c.get("heure","")[11:16])} · {H(c.get("type",""))}</span></div><p class="cr-p">{H(c.get("point",""))}</p><p>{H(c.get("apres",""))}</p></li>'
    for lot, c in crit) or "<li>Aucune.</li>"

# ---------- points ouverts ----------
ouv = []
nonfus = [d["lot"] for d in deps if not etat_by.get(d["lot"], {}).get("merge")]
po = os.path.join(REPO, "journal", "points_ouverts.json")
for cls, nat, pt, suite in (json.load(open(po, encoding="utf-8")) if os.path.exists(po) else []):
    if pt.startswith("Fusion de la PR") and nonfus:
        pt += f' ({", ".join(nonfus)})'
    ouv.append(f'<tr><td><span class="pill {cls}">{H(nat)}</span></td><td>{H(pt)}</td><td>{H(suite)}</td></tr>')
if enc_lot:
    ouv.insert(2, f'<tr><td><span class="pill run">En cours</span></td><td>{enc_lot} : {n_rediges}/11 fichiers rédigés, {n_audites}/11 audités deux fois.</td><td>Audits, passe transversale, dépôt, puis LOT suivant.</td></tr>')
    ouv.insert(3, f'<tr><td><span class="pill todo">Source manquante</span></td><td>{enc_lot} : {help_open} questions de source ouvertes sur {help_tot} (fichiers HELP).</td><td>Le texte écrit « donnée non trouvée dans les sources consultées ».</td></tr>')
ouverts = "".join(ouv)

# ---------- garde-fous ----------
main = git("rev-parse", "--short", "origin/main")
base = git("merge-base", "--short", "origin/main", "HEAD") if False else git("rev-parse", "--short", git("merge-base", "origin/main", "HEAD") or "HEAD")
app = git("diff", "--name-only", "origin/main...HEAD", "--", "*app.html")
ncomp = 0
for f in glob.glob(os.path.join(FIN, "LOT_01[3-9]", "*.html")) + glob.glob(os.path.join(FIN, "LOT_0[2-9][0-9]", "*.html")):
    for m in re.finditer(r"[^.<>]{0,60}[Cc]ompendium[^.<>]{0,40}", open(f, encoding="utf-8").read()):
        if "jamais" not in m.group(0): ncomp += 1
anom = rq.get("anomalies", [])
commits = git("rev-list", "--count", "origin/main..HEAD")
dirty = "\n".join(l for l in git("status", "--porcelain").splitlines() if "ETAT_DES_LIEUX" not in l)
chk = [
    (main == base, f"<b>main intact.</b> origin/main = {main} = base de la branche." if main == base else f"<b>main a bougé</b> : {main} ≠ base {base}."),
    (not app, "<b>app.html intact.</b> Aucune différence entre main et la branche." if not app else f"<b>app.html modifié</b> : {H(app)}"),
    (ncomp == 0, "<b>Compendium.</b> Aucune mention hors « jamais dans le Compendium » dans les LOTS déposés." if ncomp == 0 else f"<b>Compendium cité {ncomp} fois</b> dans les LOTS déposés : à vérifier."),
    (not anom, "<b>Rapport qualité.</b> 0 anomalie." if not anom else f"<b>Rapport qualité : {len(anom)} anomalie(s).</b>"),
    (not dirty, "<b>Arbre de travail propre.</b> Tout est commité." if not dirty else f"<b>{len(dirty.splitlines())} fichier(s) non commité(s)</b> au relevé."),
]
checks = "".join(f'<li{"" if ok else " class=" + chr(34) + "ko" + chr(34)}><span>{t}</span></li>' for ok, t in chk)

# ---------- routage, chronologie, rythme ----------
rc = collections.Counter((x.get("agent"), x.get("modele"), x.get("effort")) for x in rout)
rout_html = "".join(f'<tr><td class="mono">{H(a)}</td><td>{H(m)}</td><td>{H(e)}</td><td class="num">{n}</td></tr>' for (a, m, e), n in rc.most_common())
timeline = "".join(
    f'<li class="{"k" if " déposé" in txt[:20] else ""}"><time>{t:%H:%M}</time><span>{H(txt if len(txt) < 230 else txt[:txt.rfind(" ", 0, 220)] + " …")}</span></li>'
    for t, txt in journal)
if durees:
    moy = sum(durees, datetime.timedelta()) / len(durees)
    rest = todo + enc
    hrs = moy.total_seconds() * rest / 3600
    rythme = (f"{len(durees)} LOTS déposés en {', '.join(hm(d) for d in durees)} ; moyenne {hm(moy)} par LOT. "
              f"Projection linéaire pour les {rest} LOTS restants : environ {fr(hrs)} heures de travail continu, soit {fr(hrs/24)} jours. "
              f"Elle ignore incidents et LOTS plus lourds.")
else:
    rythme = "Aucun LOT déposé : rythme non calculable."

tg = rq["totaux"]
ndep_files = sum(d["n"] for d in deps)
medav = sum(d["av"].get("score_medical", 0) for d in deps) / len(deps) if deps else 0
medap = sum(d["ap"].get("score_medical", 0) for d in deps) / len(deps) if deps else 0
medmin = min((d["L"]["minimum"].get("score_medical") or 0) for d in deps) if deps else 0
pct = lambda n: f"{n/tot*100:.2f}%"
tiles = (
    f'<div class="tile"><span class="eyebrow">File complète</span><span class="big">{acc}<small> / {tot} LOTS</small></span>'
    f'<div class="meter" aria-hidden="true"><i style="width:{pct(acc)};background:var(--ok)"></i><i style="width:{pct(enc)};background:var(--run)"></i></div>'
    f'<p>Acceptés et déposés. {enc} en cours, {todo} à traiter.</p></div>'
    f'<div class="tile"><span class="eyebrow">Chantier production-v2</span><span class="big">{len(deps)}<small> LOTS déposés</small></span>'
    f'<p>{ndep_files} fichiers HTML de {fr(min(d["kmin"] for d in deps) if deps else 0)} à {fr(max(d["kmax"] for d in deps) if deps else 0)} Ko.</p></div>'
    f'<div class="tile"><span class="eyebrow">Corrections d\'audit</span><span class="big">{fr(tg["corrections"])}</span>'
    f'<p><b style="color:var(--crit)">{tg["par_gravite"].get("critique",0)} critiques</b> et {tg["par_gravite"].get("grave",0)} graves, toutes corrigées par l\'auditeur.</p></div>'
    f'<div class="tile"><span class="eyebrow">Score médical après audit</span><span class="big">{fr(medap)}<small> moyen</small></span>'
    f'<p>Contre {fr(medav)} avant audit (LOTS déposés). Minimum d\'un fichier déposé : {fr(medmin)}.</p></div>')
lede = (f"{len(deps)} LOTS du chantier sont rédigés, audités deux fois et déposés ({', '.join(d['lot'] for d in deps)}). "
        + (f"{enc_lot} : {n_rediges}/11 fichiers rédigés, {n_audites}/11 audités deux fois. " if enc_lot else "")
        + "Rien n'est fusionné sur main sans Vial.")
meta = (f'<span>Relevé à {now:%H:%M} (Zurich), le {now:%d.%m.%Y}</span><span>Branche <span class="mono">{H(git("rev-parse","--abbrev-ref","HEAD"))}</span> · '
        f'{commits} commits depuis <span class="mono">main@{main}</span></span><span>Dernier commit <span class="mono">{H(git("log","-1","--format=%h %s"))}</span></span>')

data = dict(lede=H(lede), meta=meta, tiles=tiles, tot=tot, grids=grids, next_lot=next_lot, lot_table=lot_table,
            encours_titre=encours_titre, pipe_html=pipe_html, dumbbell=dumbbell, bars=bars, stack=stack, ncrit=len(crit),
            crit_html=crit_html, ouverts=ouverts, checks=checks, nrout=len(rout), rout_html=rout_html, timeline=timeline,
            rythme=H(rythme), genere=f"{now:%d.%m.%Y à %H:%M}")
tpl = open(os.path.join(REPO, "harnais", "etat_des_lieux_modele.html"), encoding="utf-8").read()
for k, v in data.items():
    tpl = tpl.replace("{{" + k + "}}", str(v))
reste = re.findall(r"\{\{\w+\}\}", tpl)
if reste:
    sys.exit(f"Champs non remplis : {reste}")
open(OUT, "w", encoding="utf-8").write(tpl)
print(f"{OUT} · {len(tpl.encode())} octets · {acc}/{tot} acceptés · {enc_lot or 'aucun LOT en cours'}")
