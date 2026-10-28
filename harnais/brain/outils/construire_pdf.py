#!/usr/bin/env python3
"""BRAIN-HARNESS · construit le PDF du chantier théorique : harnais/brain/CHANTIER_BRAIN_HARNESS.pdf (et sa source d'impression .html).
  python3 harnais/brain/outils/construire_pdf.py [--tests]
Tout est généré depuis les fichiers du dépôt : registre.json (catalogue des 160), synapses.json (fiches des 28 synapses), essais_vial.json (T1–T4),
mutation_v3.json (mutation), tests_v3.json (--tests relance les suites et réécrit ce relevé), journal_exemple.jsonl (flux), BRAIN_3D.html (capture).
Impression : Playwright (Node, `require('playwright')`), A4, tableaux bordés, en-têtes répétés, numéros de page."""
import base64, html, json, re, subprocess, sys, tempfile, time
from collections import Counter
from pathlib import Path
B = Path(__file__).resolve().parents[1]
R = B.parents[1]
SC = B / "scriptones"
sys.path[:0] = [str(SC)]
E = lambda s: html.escape(str(s if s is not None else ""), quote=False)
fr = lambda n: f"{n:,}".replace(",", " ") if isinstance(n, int) else str(n).replace(".", ",")
pc = lambda x: f"{x:.2f}".replace(".", ",") + " %"


def charger():
    j = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))
    D = dict(reg=j(SC / "registre.json"), syn=j(SC / "synapses.json"), spec=j(B / "brain_spec.json"), ess=j(B / "essais_vial.json"))
    D["mut"] = j(B / "mutation_v3.json") if (B / "mutation_v3.json").exists() else None
    D["tests"] = j(B / "tests_v3.json") if (B / "tests_v3.json").exists() else None
    D["jour"] = [json.loads(l) for l in (B / "journal_exemple.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    return D


# ───────────────────────── relevé des tests (--tests) ─────────────────────────
def relever_tests():
    out = []
    for nom, cmd, cwd in (("test_scriptones.py", [sys.executable, "test_scriptones.py"], SC), ("test_synapses.py", [sys.executable, "test_synapses.py"], SC),
                          ("test_robustesse.py", [sys.executable, "test_robustesse.py"], SC), ("autotest grille14 + contracteur", [sys.executable, "harnais/grille14/autotest.py"], R)):
        t0 = time.time(); p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True); txt = p.stdout + p.stderr
        m = re.search(r"Ran (\d+) tests?", txt) or re.search(r"(\d+)/(\d+) OK", txt)
        n = m.group(1) if m else "?"; tot = m.group(2) if m and m.lastindex == 2 else n
        out.append(dict(suite=nom, tests=int(tot) if str(tot).isdigit() else tot, reussis=int(n) if p.returncode == 0 and str(n).isdigit() else 0, vert=p.returncode == 0, duree_s=round(time.time() - t0, 1)))
        print(nom, "vert" if p.returncode == 0 else "ROUGE", n, tot)
    (B / "tests_v3.json").write_text(json.dumps(dict(date=time.strftime("%Y-%m-%d"), suites=out), ensure_ascii=False, indent=1), encoding="utf-8")


# ───────────────────────── capture de la vue 3D ─────────────────────────
JS_CAPTURE = r"""
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await (await b.newContext({viewport:{width:1500,height:950}, colorScheme:'light', deviceScaleFactor:2})).newPage();
  await p.goto('file://' + process.argv[2]); await p.waitForTimeout(800);
  await p.evaluate(() => { BRAIN.pause(); BRAIN.vue(-0.95, 0.45, 1.08); BRAIN.avancer(70); });
  await p.addStyleTag({content: '#legende,#fil,#aide,header{display:none!important}'});
  await p.waitForTimeout(700);
  await p.screenshot({path: process.argv[3], clip: {x: 230, y: 60, width: 1150, height: 860}});
  await b.close();
})();
"""


def node(script, *args):
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, dir=str(R / ".cache")) as f: f.write(script); js = f.name
    try:
        r = subprocess.run(["node", js, *map(str, args)], cwd=R, capture_output=True, text=True, timeout=600)
        if r.returncode: raise RuntimeError(r.stderr[-2000:])
    finally: Path(js).unlink(missing_ok=True)


def capture_3d():
    with tempfile.TemporaryDirectory() as d:
        png = Path(d) / "vue.png"; node(JS_CAPTURE, B / "BRAIN_3D.html", png)
        return "data:image/png;base64," + base64.b64encode(png.read_bytes()).decode()


# ───────────────────────── éléments de mise en page ─────────────────────────
def table(entetes, lignes, cls="", largeurs=None):
    cg = "".join(f'<col style="width:{w}">' for w in largeurs) if largeurs else ""
    h = "".join(f"<th>{x}</th>" for x in entetes)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in lignes)
    return f'<table class="{cls}"><colgroup>{cg}</colgroup><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'


def schema_svg():
    """Schéma plan du circuit (SVG inline) : collecte → α → écrivains → S → β → vote → O → sortie, avec bus, mémoire, économie, gardiens."""
    bx = lambda x, y, w, h, t, c, s="": f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{c}" fill-opacity=".12" stroke="{c}" stroke-width="1.3"/>' \
        f'<text x="{x + w / 2}" y="{y + h / 2 - (5 if s else 0)}" text-anchor="middle" dominant-baseline="middle" font-size="10" font-weight="700" fill="#111827">{t}</text>' + \
        (f'<text x="{x + w / 2}" y="{y + h / 2 + 9}" text-anchor="middle" dominant-baseline="middle" font-size="8.6" fill="#374151">{s}</text>' if s else "") + "</g>"
    fl = lambda x1, y1, x2, y2: f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#4b5563" stroke-width="1.2" marker-end="url(#fl)"/>'
    g = ['<svg viewBox="0 0 760 300" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Atkinson Hyperlegible, sans-serif">',
         '<defs><marker id="fl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" fill="#4b5563"/></marker></defs>']
    col = [("Harnais externe", "s11 · 14 paquets", "#475569"), ("Zone α", "α1…α14 × 5", "#4f46e5"), ("Écrivains", "64, un par zone", "#0f766e"),
           ("Sonnet S1–S5", "briefs compilés", "#0284c7"), ("Zone β", "β1…β14 × 5", "#db2777"), ("Vote α/β", "s18", "#7c3aed"), ("Opus O1–O5", "par domaine", "#e11d48"), ("Sortie", "audité ou retour", "#475569")]
    x = 8
    for i, (t, s, c) in enumerate(col):
        g.append(bx(x, 40, 84, 54, t, c, s))
        if i < len(col) - 1: g.append(fl(x + 84, 67, x + 94, 67))
        x += 94
    g.append(bx(8, 160, 84, 46, "Gardiens", "#b45309", "s15 · s13"))
    g.append(bx(196, 160, 364, 46, "Bus de doléances (thalamus)", "#0f766e", "contrat · déduplication · ordonnanceur s12 · brief s17 · journal s14"))
    g.append(bx(196, 236, 176, 46, "Mémoire (hippocampe)", "#9333ea", "s10 · s19 · 5 passages"))
    g.append(bx(384, 236, 176, 46, "Économie (hypothalamus)", "#0891b2", "s16 · jetons par étage"))
    g.append(bx(572, 160, 180, 46, "Transversaux de forme", "#16a34a", "s1 s2 s3 s4 s5 s6 s8 s9 s20"))
    for xx in (148, 336, 430, 524, 618): g.append(f'<line x1="{xx}" y1="94" x2="{xx if xx < 560 else 520}" y2="160" stroke="#9ca3af" stroke-dasharray="3 3" stroke-width="1"/>')
    g.append(fl(50, 94, 50, 160)); g.append(fl(92, 183, 196, 183)); g.append(fl(572, 183, 560, 183))
    g.append(fl(284, 206, 284, 236)); g.append(fl(472, 206, 472, 236))
    g.append('<text x="380" y="20" text-anchor="middle" font-size="10.5" fill="#374151">trajet d\'un cours (gauche → droite) ; tout scriptone émet ses doléances typées vers le bus (pointillés)</text>')
    g.append("</svg>")
    return "".join(g)


# ───────────────────────── contenu ─────────────────────────
def construire(D, img):
    reg, syn, ess = D["reg"], D["syn"], D["ess"]; S = reg["scriptones"]; byid = {e["id"]: e for e in S}
    PTS = {int(k): v for k, v in syn["points"].items()}; FA, FB = syn["familles_alpha"], syn["familles_beta"]
    T12, AG, T3, T4 = ess["T1_T2"], ess["T1_agrege"], ess["T3"], ess["T4"]; mut = D["mut"]; tests = D["tests"]
    sec = []; toc = []
    def h2(n, t): toc.append((n, t)); return f'<h2 id="s{n}" class="{"suite" if n in (3, 5, 12, 13, 14) else ""}">{n}. {E(t)}</h2>'
    n_ecr = sum(1 for e in S if e.get("ecrit")); zones = [(z, e["id"]) for e in S for z in (e.get("ecrit") or [])]
    mut_txt = (f"{fr(mut['detectes'])} sur {fr(mut['total'])} détectés ({fr(mut['distincts'])} distincts), borne d'évasion 95 % ≤ {pc(100 * mut['borne_evasion_95'])}" if mut else "relevé absent")

    # couverture
    sec.append(f"""<section class="garde">
<div class="sur">Chantier théorique · version 3 · {E(time.strftime('%d.%m.%Y'))}</div>
<h1>BRAIN-HARNESS</h1>
<div class="soustitre">Cerveau secondaire d'audit des cours : 160 scriptones gratuits, deux grillages losangiques de 14 synapses, 10 auditeurs. Plan, anatomie, spécifications, flux, mesures.</div>
{table(["Grandeur", "Visé", "Mesuré (28.10.2026)", "Source"], [
        ["Réduction des jetons d'audit (4 cours réels)", "99,99 %", f"<b>{pc(AG['reduction_vs_relecture_pct'])}</b> contre la relecture du HTML ×10 ; {pc(AG['reduction_vs_texte_pct'])} contre le texte ×10", "T1"],
        ["Réduction sur un cours sans faute (doré)", "99,99 %", pc(AG["dore"]["reduction_pct"]), "T1"],
        ["Détection des erreurs connues (mutants)", "≥ 99,99 %", mut_txt, "mutation.py"],
        ["Faux positifs sur le doré", "0", "0" if mut and not mut["faux_positifs"] else "voir mutation", "mutation.py"],
        ["Conflits d'écriture", "0", f"0 statique ({n_ecr} écrivains, {len(zones)} zones) ; 0 dynamique sur 4 cours × 8 ordres", "T3"],
        ["Pannes injectées absorbées", "100 %", f"{T4['exception']['signalees']}/140 exceptions, {T4['contrat']['signalees']}/140 contrats, {T4['double_panne']['escalades_Z2']}/140 doubles pannes escaladées", "T4"],
        ["Cours réels sortis audités", "—", f"0 sur {len(T12)} : fautes graves ouvertes renvoyées aux auditeurs", "T2"]], "kpi", ["31%", "11%", "46%", "12%"])}
<p class="note">Lecture honnête : la cible de 99,99 % de réduction n'est pas atteinte (facteur {fr(AG['ecart_facteur'])}) ; le circuit gratuit retire 92 à 96 % des jetons d'audit. Les 99,99 % de détection portent sur les classes d'erreurs connues, pas sur le jugement clinique.</p>
</section>""")

    # 1 plan global
    sm = lambda k: round(sum(c["jetons"][k] for c in T12) / len(T12))
    plan = [
        ["0", "Harnais externe de collecte (s11)", "nerfs afférents", "script", "fichier brut", "14 paquets, un par point ; refus si entrée cassée (K1–K5)", "0"],
        ["0′", "Gardiens (s15) et disjoncteurs (s13)", "cervelet", "script", "SHA256SUMS, registre, pannes", "arrêt si altération ; ré-routage vers le jumeau ; escalade", "0"],
        ["1", "Zone α : grillage losangique (α1…α14 × 5 familles) + transversaux de forme et de mémoire", "hémisphère gauche", "script", "paquet du point n ; relais en zigzag", "doléances typées vers le bus", "0"],
        ["1′", f"Écrivains ({n_ecr}, un par zone)", "cortex moteur", "script", "doléances [script]", "texte corrigé jusqu'au point fixe (≤ 4 tours)", "0"],
        ["2", "Nœuds S1…S5 (Sonnet 5.5, effort moyen)", "noyaux relais", "agent", "brief compilé (s17) : doléances [agent] + paquets touchés", "corrections ; paquet relu vers βn", f"{fr(sm('briefs_sonnet'))} (moyenne par cours, 5 nœuds)"],
        ["3", "Zone β : second grillage (β1…β14 × 5 familles), indépendante d'α", "hémisphère droit", "script", "texte corrigé, paquet relu", "doléances typées", "0"],
        ["3′", "Nœud de vote α/β (s18)", "corps calleux", "script", "doléances α et β du même point", "routage des désaccords vers O1…O5", "0"],
        ["4", "Nœuds O1…O5 (Opus 5.5), un par domaine", "cortex préfrontal", "agent", "brief β et désaccords", "avis de domaine", f"{fr(sm('briefs_opus'))} (moyenne par cours, 5 nœuds)"],
        ["5", "Sortie", "tronc cérébral", "script", "verdict du bus", "seuls les cours sans faute grave ouverte sortent", "0"],
        ["∥", "Bus (thalamus) · Mémoire (hippocampe) · Économie (hypothalamus)", "relais, mémoire, homéostasie", "script", "toutes les doléances", "journal, briefs, stagnation, jetons", "0"]]
    sec.append(h2(1, "Plan global") + f"""<p>Un cours traverse le circuit de gauche à droite. Tout ce qui est mécanique se fait par script, sans jeton ; un modèle n'intervient que pour juger ou rédiger, et ne reçoit que ce qu'il doit corriger.</p>
{schema_svg()}
{table(["Étape", "Structure", "Analogie", "Exécutant", "Entrée", "Sortie", "Jetons"], plan, "", ["6.5%", "24%", "11%", "9.5%", "16%", "21%", "12%"])}
<h3>Principes</h3>
{table(["Principe", "Règle"], [[E(p.split(':')[0]), E(':'.join(p.split(':')[1:]).strip() or p)] for p in D['spec']['principes']], "", ["24%", "76%"])}""")

    # 2 anatomie
    reg_reg = Counter(e["region"] for e in S)
    anat = [["EXT · harnais externe", "nerfs afférents", "s11_collecteur", "fichier brut", "14 paquets"],
            ["GARD · gardiens", "cervelet", "s15_gardien, s13_disjoncteur", "empreintes, pannes", "arrêt, Z1–Z4"],
            ["ALP · zone α", "hémisphère gauche", f"{reg_reg['ALP']} synapses générées", "paquets", "doléances AS, AR, AH, AQ, AD"],
            ["AUF · forme", "aires associatives", "s1, s2, s5, s6, s8, s20", "HTML converti", "P, L, A, N, T, Y"],
            ["AUL · langue", "aire du langage", "s3, s4", "texte", "C, B"],
            ["AUM · médical", "cortex frontal", "s9", "sources", "I"],
            ["VIS · captures", "cortex visuel", "s7 (navigateur)", "rendu", "V1–V5"],
            ["BUS · bus", "thalamus", "s12, s14, s17, s18", "doléances", "briefs, routage, journal"],
            ["PRO · écrivains", "cortex moteur", "écrivains du registre", "doléances [script]", "texte corrigé"],
            ["S1–S5 · Sonnet", "noyaux relais", "agents", "briefs", "corrections"],
            ["BET · zone β", "hémisphère droit", f"{reg_reg['BET']} synapses générées", "texte corrigé", "BX, BC, BS, BM, BL"],
            ["VOTE · vote", "corps calleux", "s18_vote", "α et β", "routage"],
            ["O1–O5 · Opus", "cortex préfrontal", "agents", "brief β", "avis de domaine"],
            ["MEM · mémoire", "hippocampe", "s10, s19", "fautes corrigées, cumul", "M, U ; stagnation"],
            ["ECO · économie", "hypothalamus", "s16", "paquets, briefs", "W ; jetons par étage"],
            ["SORTIE", "tronc cérébral", "orchestre", "verdict", "cours audité ou retour"]]
    sec.append(h2(2, "Anatomie fonctionnelle") + f"""<p>La vue 3D animée (<code>harnais/brain/BRAIN_3D.html</code>, hors ligne, sans bibliothèque) montre chaque structure ; le survol donne son rôle, ses entrées, ses sorties et ses mesures tirées du journal réel. Capture ci-dessous : passage du cours LOT_001 DX.2.</p>
<figure><img src="{img}" alt="Vue 3D du BRAIN-HARNESS"><figcaption>Cortex transparent ; à gauche la zone α (indigo), à droite la zone β (rose), numérotées en zigzag ; S1–S5 et O1–O5 en couleurs ; anneau du harnais externe et ses 14 perles ; étoiles : 20 scriptones transversaux.</figcaption></figure>
{table(["Région", "Analogie", "Scriptones", "Entrées", "Sorties"], anat, "", ["20%", "16%", "26%", "19%", "19%"])}""")

    # 3 familles
    def fam_rows(F, z):
        out = []
        for f, v in F.items():
            ex = byid.get(f"{z}01_{f}") or {}
            j = syn["jumeaux"]["alpha" if z == "a" else "beta"].get(f)
            out.append([f"<b>{f}</b>", E(v["nom"]), E(v["signal"]), E(v["codes"]), E(", ".join(z_.split(':')[1] for z_ in ex.get("ecrit") or []) or "lectrice"), f"{'β' if z == 'a' else 'α'}{j}" if j else "—"])
        return out
    sec.append(h2(3, "Familles des synapses α et β") + f"""<p>Chaque synapse αn ou βn regroupe 5 scriptones, un par famille, qui ne lisent que le paquet du point n. β est indépendante d'α par la méthode et par le but : α vise la concision et la forme ; β, l'exhaustivité et le fond (relecture adverse). Le jumeau d'une famille est la famille de l'autre zone qui couvre la même exigence si son disjoncteur s'ouvre.</p>
<h3>Zone α · concision et forme</h3>{table(["Fam.", "Nom", "Signal", "Codes émis", "Zone écrite", "Jumeau"], fam_rows(FA, 'a'), "", ["6%", "22%", "9%", "43%", "11%", "9%"])}
<h3>Zone β · exhaustivité et fond</h3>{table(["Fam.", "Nom", "Signal", "Codes émis", "Zone écrite", "Jumeau"], fam_rows(FB, 'b'), "", ["6%", "22%", "9%", "43%", "11%", "9%"])}""")

    # 4 fiches des synapses
    fiches = []
    for n in range(1, 15):
        p = PTS[n]; cont = p.get("continuite") or {}
        par = [["Titre", E(p["titre"])], ["Plancher (mots)", E(p.get("plancher"))], ["Éléments requis", E(" · ".join(r[0] for r in p.get("requis") or []) or "—")],
               ["Notions attendues", E(" · ".join(x[0] for x in p.get("notions") or []) or "—")],
               ["Continuité", "bloc continu exigé" if cont.get("bloc") else (f"texte haché au-delà de {cont['hache']} phrases courtes" if cont.get("hache") else "—")],
               ["Termes dédiés min.", E(p.get("termes_min", 0))], ["Auditeurs", f"Sonnet {E({1:'S1',2:'S1',3:'S1',4:'S2',5:'S2',6:'S2',7:'S3',8:'S3',9:'S3',10:'S4',11:'S4',12:'S5',13:'S5',14:'S5'}[n])} ; Opus selon le domaine"]]
        rows = []
        for z, F in (("a", FA), ("b", FB)):
            for f in F:
                e = byid[f"{z}{n:02d}_{f}"]
                rows.append([("α" if z == "a" else "β") + str(n), f"<code>{e['id']}</code>", E(F[f]["nom"]), E(", ".join(dict.fromkeys(m[1] for m in e.get("mutants") or []))), E(", ".join(e.get("ecrit") or []) or "—"), f"<code>{E(e.get('jumeau') or '—')}</code>"])
        fiches.append(f'<div class="fiche"><h3>Point {n} · {E(p["titre"])} · synapses α{n} et β{n}</h3>' +
                      table(["Paramètre", "Valeur", "Paramètre", "Valeur"], [par[k][:2] + (par[k + 1][:2] if k + 1 < len(par) else ["", ""]) for k in range(1, len(par), 2)], "param petit", ["13%", "37%", "13%", "37%"]) +
                      table(["Synapse", "Scriptone", "Famille", "Mutants testés", "Écrit", "Jumeau"], rows, "petit", ["8%", "11%", "33%", "20%", "16%", "12%"]) + "</div>")
    sec.append(h2(4, "Fiche de chaque synapse αn et βn") + "<p>Paramètres tirés de <code>synapses.json</code> (calibrés sur les 177 cours de main) et du registre. Une synapse émet des doléances ; elle n'écrit que dans la zone indiquée.</p>" + "".join(fiches))

    # 5 auditeurs
    moy = lambda k: round(sum(c["jetons"]["par_noeud"].get(k, 0) for c in T12) / len(T12)) if all("par_noeud" in c["jetons"] for c in T12) else "—"
    aud = [["S1", "Sonnet 5.5 (moyen)", "points 1 à 3", "doléances [agent] α des points 1–3 + paquets", fr(moy("S1"))],
           ["S2", "Sonnet 5.5 (moyen)", "points 4 à 6", "idem, points 4–6", fr(moy("S2"))], ["S3", "Sonnet 5.5 (moyen)", "points 7 à 9", "idem, points 7–9", fr(moy("S3"))],
           ["S4", "Sonnet 5.5 (moyen)", "points 10 et 11", "idem, points 10–11", fr(moy("S4"))], ["S5", "Sonnet 5.5 (moyen)", "points 12 à 14", "idem, points 12–14", fr(moy("S5"))],
           ["O1", "Opus 5.5", "fond médical (points 3, 8, 11)", "doléances β médicales, désaccords du vote", fr(moy("O1"))],
           ["O2", "Opus 5.5", "épidémiologie, prévention, doléances, mémoire (2, 12)", "idem", fr(moy("O2"))],
           ["O3", "Opus 5.5", "démarche clinique (4 à 7, 9, 10)", "idem", fr(moy("O3"))], ["O4", "Opus 5.5", "langue", "doléances β de langue", fr(moy("O4"))],
           ["O5", "Opus 5.5", "forme et jetons", "doléances β de forme", fr(moy("O5"))]]
    sec.append(h2(5, "Les 10 auditeurs") + f"""<p>Les auditeurs ne relisent jamais le fichier entier : chacun reçoit un brief compilé par s17 (doléances [agent] de son territoire et paquets des seuls points touchés). Extension à 16 par étage : décidée par le gain de détection mesuré sur agents réels, non par la gratuité (non mesuré à ce jour).</p>
{table(["Nœud", "Modèle", "Territoire ou domaine", "Entrée", "Brief moyen (jetons, 4 cours)"], aud, "", ["7%", "15%", "30%", "32%", "16%"])}""")

    # 6 catalogue
    rows = []
    for k, e in enumerate(S, 1):
        rows.append([str(k), f"<code>{e['id']}</code>", E(e["zone"][:5]), E(e.get("synapse") or "—"), E(e.get("famille") or "—"), E(e["region"]), E(e["signal"]),
                     E(e["nom"] if e["zone"] == "transversal" else e["fonction"]), E(", ".join(e.get("ecrit") or []) or "—"),
                     E(" ".join(dict.fromkeys(m[1] for m in e.get("mutants") or []))), E(e.get("jumeau") or "—"), E({"implémenté": "impl.", "généré": "gén."}.get(e["etat"], e["etat"])), f"<code>{e['sha256'][:10]}</code>"])
    sec.append(h2(6, "Catalogue des 160 scriptones") + f"""<p>Généré depuis <code>scriptones/registre.json</code> (version {reg['version']}, {reg['total']} scriptones : {sum(e['zone']=='transversal' for e in S)} transversaux, {sum(e['zone']=='alpha' for e in S)} α, {sum(e['zone']=='beta' for e in S)} β). Coût en jetons : 0 pour tous. Chaque scriptone a un contrat JSON (brain.scriptone/1), des mutants, un jeu doré, un test d'idempotence et une empreinte SHA-256.</p>
{table(["N°", "Id", "Zone", "Syn.", "Fam.", "Rég.", "Signal", "Nom ou fonction", "Écrit", "Mutants (codes)", "Jumeau", "État", "SHA-256"], rows, "cat", ["3.5%", "8.5%", "4.6%", "4%", "4.2%", "4.5%", "6.8%", "22.5%", "11.5%", "11%", "6%", "4.4%", "8.5%"])}""")

    # 7 flux
    J = D["jour"]; ct = Counter(e["type"] for e in J)
    types = [["medical", "#dc2626", "EXT → αn (paquets), Sk → βn (paquet relu), βn (X, C, S), O → SORTIE", ct["medical"]],
             ["langue", "#2563eb", "αn (R, H, D), βn (L), s3, s4", ct["langue"]], ["forme", "#16a34a", "αn (S, Q), transversaux de forme, relais en zigzag, écrivains → PRO", ct["forme"]],
             ["memoire", "#9333ea", "s10, s19, BUS → MEM (doléances ouvertes, stagnation)", ct["memoire"]], ["doleance", "#d97706", "GARD, VOTE, pannes (Z1–Z4), verdict BUS → SORTIE", ct["doleance"]],
             ["jetons", "#0891b2", "BUS → Sk, Ok (briefs comptés), ECO → SORTIE", ct["jetons"]]]
    champs = [["v", "entier", "version du format (1)"], ["ts", "texte ISO 8601", "horodatage local"], ["run", "texte", "passage : fichier#empreinte courte"], ["seq", "entier ≥ 0", "rang strictement croissant dans le passage"],
              ["type", "énuméré", "medical, langue, forme, memoire, doleance, jetons (couleur dans la vue 3D)"], ["de, vers", "texte", "nœud : EXT, GARD, GLIE, α1…α14, β1…β14, S1…S5, O1…O5, BUS, PRO, VOTE, MEM, ECO, SORTIE, ou id de scriptone"],
              ["fichier", "texte", "cours"], ["point", "1…14", "point de la grille"], ["code", "texte", "code de doléance (ex. AS1, P7)"], ["severite", "énuméré", "CRITIQUE, GRAVE, MOYEN, DETAIL"],
              ["jetons", "entier", "jetons transportés (paquet, brief)"], ["msg", "texte", "constat court"]]
    etapes = [["1", "EXT → EXT, EXT → αn", "collecte ; 14 paquets (jetons comptés)"], ["2", "GARD → BUS", "empreintes intactes, sinon arrêt"], ["3", "GLIE, MEM → BUS ou αn", "transversaux de forme, de langue et de mémoire"],
              ["4", "αn → BUS ; αn → αn+1", "doléances α ; relais en zigzag"], ["5", "BUS → PRO", "corrections par script jusqu'au point fixe"], ["6", "BUS → Sk", "briefs Sonnet"],
              ["7", "βn → BUS ; Sk → βn ; βn → βn+1", "doléances β ; paquet relu ; zigzag"], ["8", "VOTE → Ok", "désaccords α/β"], ["9", "BUS → Ok", "briefs Opus"],
              ["10", "Ok → SORTIE ; BUS → MEM ; ECO → SORTIE ; BUS → SORTIE", "avis de domaine ; doléances ouvertes ; jetons ; verdict"]]
    sec.append(h2(7, "Flux d'information") + f"""<p>Chaque passage écrit un journal JSONL (<code>.cache/brain/evenements.jsonl</code>, schéma <code>scriptones/evenements.schema.json</code>, contrôlé par s14). La vue 3D le rejoue : une particule par événement, de la couleur de son type. Jeu d'exemple : <code>harnais/brain/journal_exemple.jsonl</code>, {fr(len(J))} événements réels (doré et 4 cours).</p>
<h3>Types de signaux</h3>{table(["Type", "Couleur", "Émetteurs et trajets", "Événements (exemple)"], [[f"<b>{t}</b>", f'<span class="pastille" style="background:{c}"></span> {c}', E(s), fr(n)] for t, c, s, n in types], "", ["12%", "14%", "58%", "16%"])}
<h3>Format brain.evenement/1</h3>{table(["Champ", "Type", "Rôle"], champs, "", ["16%", "16%", "68%"])}
<h3>Séquence d'un passage (orchestre.py)</h3>{table(["N°", "Trajet", "Contenu"], etapes, "", ["6%", "40%", "54%"])}""")

    # 8 anti-conflit
    ordre = ["s5_arbre", "s8_tableaux", "a01…a14_S", "a01…a14_R", "a02_Q", "b01…b14_C", "b01…b14_L", "s3_concision", "s2_rythme", "s6_barre14", "s1_police"]
    zr = sorted(zones, key=lambda x: (x[0].split(":")[0], x[0]))
    trip = [zr[i:i + 3] for i in range(0, len(zr), 3)]
    zrows = [sum(([f"<code>{E(z)}</code>", f"<code>{E(w)}</code>"] for z, w in t), []) + ["", ""] * (3 - len(t)) for t in trip]
    conf = T3["confluence"]; inj = T3["conflit_injecte_detecte"]
    sec.append(h2(8, "Règle anti-conflit") + f"""<p><b>Une zone, un écrivain.</b> Une zone est une partie nommée d'un fichier (titre du point n, phrases d'absence du point n, blocs du point 2, typographie des chiffres, CSS, barre, ancres). Un seul scriptone peut la modifier ; tous les autres émettent des doléances typées {{région, fichier, ancre, sévérité, constat, correction prescrite, preuve}} sur le bus. Les écrivains s'appliquent dans un ordre canonique, jusqu'au point fixe.</p>
{table(["Garde", "Mécanisme", "Mesure"], [
        ["Preuve statique", "registre : aucune zone revendiquée deux fois (pigeonnier) ; s12 refuse de démarrer sinon (O1)", f"{len(zones)} zones, {n_ecr} écrivains, conflits = {len(T3['conflits_statiques'])}"],
        ["Confluence", "s12 rejoue K ordres aléatoires des écrivains jusqu'au point fixe (O2)", f"{len(conf)} cours × {conf[0]['ordres']} ordres : {sum(len(c['doleances']) for c in conf)} divergence"],
        ["Idempotence", "corriger(corriger(x)) = corriger(x) (O3)", f"{sum(c['idempotent'] for c in T12)}/{len(T12)} cours réels"],
        ["Écriture hors zone", "diff de chaque écrivain contre ses zones déclarées (O4)", "0 sur les cours réels"],
        ["Conflits injectés", "deux écrivains, duel, bavard, intrus", "; ".join(f"{k} → {', '.join(v)}" for k, v in inj.items())],
        ["Concurrence", "verrou exclusif par fichier, écriture atomique, journal sous flock", ", ".join(f"{k} proc. : {v['duree_s']} s, identiques {('oui' if v['identiques_au_sequentiel'] else 'NON')}" for k, v in T3['simultanes'].items())]], "", ["17%", "50%", "33%"])}
<p class="note">Défaut trouvé par T3 et corrigé : avant le 28.10, les 4 cours réels donnaient un texte différent selon l'ordre des écrivains, car les blocs &lt;style&gt; de s1, s2, s5 et s6 s'inséraient au même endroit. <code>bus.pose_style</code> les place désormais à leur rang canonique : 0 divergence.</p>
<h3>Ordre canonique des écrivains</h3><p>{' → '.join(f'<code>{o}</code>' for o in ordre)}</p>
<h3>Nombre de connexions</h3>{table(["Connexion", "Nombre"], [[E(k.replace('_', ' ')), fr(v)] for k, v in T3['connexions'].items()], "etroit", ["70%", "30%"])}
<p>Nombre optimal sans conflit possible : connexions d'écriture = nombre de zones ({len(zones)}) ; connexions de lecture illimitées. Couverture des {fr(T3['couverture']['mutants'])} mutants des synapses selon le nombre de familles actives par point :</p>
{table(["Familles", "Meilleur ensemble", "Couverture"], [[str(c['familles']), E(' '.join(c['meilleur_ensemble'])), pc(c['couverture_pct'])] for c in T3['couverture']['courbe']], "etroit", ["12%", "63%", "25%"])}
<p>α seule : {pc(T3['couverture']['alpha_seule_pct'])} ; β seule : {pc(T3['couverture']['beta_seule_pct'])} ; α + β : {pc(T3['couverture']['alpha_beta_pct'])}. Optimum mesuré : {T3['couverture']['optimal']} familles. βM ne s'ajoute pas à cette batterie : elle contrôle qu'α reste sensible sur le fichier réel (BM1). Redondance moyenne {fr(T3['couverture']['redondance']['moyenne'])} : {fr(T3['couverture']['redondance']['une_famille'])} mutants vus par une seule famille, d'où le jumeau et l'escalade.</p>
<h3>Zones et écrivain unique</h3>{table(["Zone", "Écrivain", "Zone", "Écrivain", "Zone", "Écrivain"], zrows, "petit")}""")

    # 9 auto-adaptation
    jum = [[f"α·{f}", f"β·{b}", E(FA[f]["nom"])] for f, b in syn["jumeaux"]["alpha"].items()] + [[f"β·{f}", f"α·{a}", E(FB[f]["nom"])] for f, a in syn["jumeaux"]["beta"].items()]
    iso = T4["isolement"]; orc = T4["orchestre"]
    sec.append(h2(9, "Auto-adaptation en cas de panne") + f"""{table(["Code", "Situation", "Réaction"], [
        ["Z1", "panne d'une synapse (exception, contrat rompu, altération)", "disjoncteur ouvert ; le jumeau (autre zone, autre méthode) couvre l'exigence ; doléance GRAVE pour réparer"],
        ["Z2", "panne sans jumeau valide", "escalade CRITIQUE : l'auditeur Opus du domaine relit la zone ; le cours ne sort pas"],
        ["Z3", "mêmes doléances deux passages de suite", "fichier BLOQUÉ, retour au chef de production ; aucun agent relancé en boucle"],
        ["Z4", "lenteur au-delà du budget (4 s)", "résultat gardé ; disjoncteur ouvert pour les fichiers suivants"],
        ["G1–G4", "empreinte altérée, fichier manquant, registre incohérent", "arrêt de la chaîne avant toute écriture"],
        ["Contrat", "sortie JSON invalide", "traitée comme une panne (Z1/Z2)"]], "", ["9%", "38%", "53%"])}
<h3>Jumeaux</h3>{table(["Famille", "Jumeau", "Exigence"], jum, "etroit", ["15%", "15%", "70%"])}
<h3>Résultats (T4, cours LOT_001 DX.2 et doré)</h3>{table(["Essai", "Résultat"], [
        ["Exception injectée dans chacune des 140 synapses", f"{T4['exception']['signalees']}/140 signalées ; {T4['exception']['reroutees_vers_jumeau']}/140 ré-routées"],
        ["Contrat rompu dans chacune des 140", f"{T4['contrat']['signalees']}/140 ; {T4['contrat']['reroutees_vers_jumeau']}/140 ré-routées"],
        ["Lenteur dans chacune des 140", f"{T4['lenteur']['signalees']}/140 signalées (Z4)"],
        ["Synapse et jumeau en panne (×140)", f"{T4['double_panne']['escalades_Z2']}/140 escaladées (Z2)"],
        ["14 pannes simultanées (une par point)", f"{iso['autres_modifiees']}/{iso['autres_synapses']} autres synapses modifiées (aucune influence) ; {iso['pannes_couvertes_par_jumeau']}/14 couvertes ; {iso['doleances_propres_des_synapses_en_panne']} doléances propres rendues à l'auditeur"],
        *[[f"Orchestre, doré : {E(k)}", f"{E(v['verdict'])} ({v['pannes']} panne(s), {v['escalades']} escalade(s))"] for k, v in orc.items()],
        ["Stagnation", f"1er passage : {E(T4['stagnation']['passage_1'])} ; 2e : {E(T4['stagnation']['passage_2'])}"]], "", ["40%", "60%"])}
<p class="note">Défaut trouvé par T4 et corrigé : l'orchestre journalisait une panne sans jumeau mais l'omettait du verdict ; un cours pouvait sortir « audité » avec une exigence non couverte.</p>""")

    # 10 budget
    bud = []
    for c in T12:
        j = c["jetons"]; bud.append([E(c["cours"].replace("_Phase_B_V0_", " ").replace(".html", "")), fr(j["relecture_10_noeuds"]), fr(j["texte_10_noeuds"]), fr(j["briefs_sonnet"]), fr(j["briefs_opus"]), fr(j["briefs_total"]), pc(j["reduction_vs_relecture_pct"]), pc(j["reduction_vs_texte_pct"])])
    bud.append(["<b>4 cours</b>", fr(AG["relecture"]), fr(AG["texte"]), "", "", f"<b>{fr(AG['briefs'])}</b>", f"<b>{pc(AG['reduction_vs_relecture_pct'])}</b>", f"<b>{pc(AG['reduction_vs_texte_pct'])}</b>"])
    bud.append(["Doré (sans faute)", fr(AG["dore"]["relecture_10_noeuds"]), "", "", "", fr(AG["dore"]["briefs"]), pc(AG["dore"]["reduction_pct"]), ""])
    def mx(k):
        v, c, nd = max((x, c["cours"], nd) for c in T12 for nd, x in c["jetons"].get("par_noeud", {}).items() if nd[0] == k)
        return f"{fr(v)} ({nd}, {c[:7]})"
    et = [["0 Collecte (s11)", "0", "0", "script"], ["0′ Gardiens", "0", "0", "script"], ["1 Zone α + transversaux", "0", "0", "70 + 20 scripts"], ["1′ Écrivains", "0", "0", "script"],
          ["2 S1–S5 (entrée)", "3 000 par brief (plan v2)", f"{fr(round(sum(c['jetons']['briefs_sonnet'] for c in T12) / len(T12) / 5))} par nœud en moyenne ; maximum {mx('S')}", "agent"],
          ["3 Zone β", "0", "0", "70 scripts"], ["3′ Vote", "0", "0", "script"],
          ["4 O1–O5 (entrée)", "20 000 par audit Opus (plan v2)", f"{fr(round(sum(c['jetons']['briefs_opus'] for c in T12) / len(T12) / 5))} par nœud en moyenne ; maximum {mx('O')}", "agent"],
          ["5 Sortie, bus, mémoire, économie", "0", "0", "script"], ["Sorties des agents", "3 000 par boucle (Edit seulement)", "non mesuré (aucun agent appelé)", "agent"]]
    sec.append(h2(10, "Budget de jetons par étage") + f"""{table(["Étage", "Plafond", "Mesuré", "Exécutant"], et, "", ["30%", "28%", "28%", "14%"])}
<h3>Calcul honnête de la réduction</h3>
<p>Estimation constante de 4 caractères par jeton. Référence A : 10 auditeurs relisent chacun le HTML entier. Référence B : 10 auditeurs relisent chacun le texte visible. Circuit : chaque auditeur reçoit son brief (doléances [agent] compactes et paquets des points touchés). Réduction = 1 − briefs / référence.</p>
{table(["Cours", "Réf. A : HTML ×10", "Réf. B : texte ×10", "Briefs Sonnet", "Briefs Opus", "Briefs total", "Réduction / A", "Réduction / B"], bud, "", ["17%", "12%", "12%", "10%", "10%", "11%", "14%", "14%"])}
<p><b>Visé : 99,99 %. Mesuré : {pc(AG['reduction_vs_relecture_pct'])} (A) et {pc(AG['reduction_vs_texte_pct'])} (B).</b> Pour 99,99 % sur ces 4 cours, les briefs devraient totaliser au plus {fr(AG['briefs_max_pour_cible'])} jetons ; ils en totalisent {fr(AG['briefs'])}, soit {fr(AG['ecart_facteur'])} fois plus. Le plancher tient au contenu : un auditeur doit lire le paquet du point qu'il corrige. Seul un cours sans doléance [agent] s'en approche (doré : {pc(AG['dore']['reduction_pct'])}). La rédaction (Phase A et B) n'est pas comptée ici ; la cible ne peut être atteinte qu'en réduisant à la source les fautes qui exigent un agent.</p>""")

    # 11 tests
    tl = []
    if tests:
        for s in tests["suites"]: tl.append([E(s["suite"]), f"{s['reussis']}/{s['tests']}", "vert" if s["vert"] else "<b>ROUGE</b>", f"{fr(s['duree_s'])} s"])
    if mut: tl.append([f"mutation.py --n {64}", f"{fr(mut['detectes'])}/{fr(mut['total'])}", "vert" if mut["vert"] else "<b>ROUGE</b>", f"{fr(mut['duree_s'])} s"])
    tl.append(["essais_vial.py (T1–T4)", "voir sections 8 à 10", "mesuré", f"{fr(ess['duree_s'])} s"])
    plan_t = [["M1 détection des erreurs connues", "mutants détectés / distincts (borne d'évasion 95 %)", "≥ 99,99 %", mut_txt],
              ["M2 faux positifs", "doléances sur le doré et ses variations neutres", "0", "0" if mut and not mut["faux_positifs"] else "—"],
              ["M3 idempotence", "scriptones et chaîne complète", "100 %", "100 %" if mut and not mut["idempotence_ko"] else "—"],
              ["T1 réduction des dépenses", "1 − briefs / relecture ×10", "99,99 %", f"{pc(AG['reduction_vs_relecture_pct'])} (cible non atteinte)"],
              ["T2 cours réels", "4 cours de LOT 001, 005, 010, 012 ; main intact ; idempotence", "main intact", f"{sum(c['main_intact'] for c in T12)}/4 intacts, {sum(c['idempotent'] for c in T12)}/4 idempotents"],
              ["T3 connexions sans conflit", "statique, 8 ordres aléatoires, conflits injectés, 16 cours", "0 conflit", "0 ; 4/4 conflits injectés détectés"],
              ["T4 auto-adaptation", "140 synapses × 3 pannes, doubles pannes, isolement, stagnation", "100 %", "100 % ; 0 influence"],
              ["M5 erreurs médicales", "mutants médicaux (dose ×10, unité, PMID, chiffre)", "≤ 0,01 %", "non mesuré (phase P4)"],
              ["16 auditeurs par étage", "gain de détection sur agents réels", "gain mesuré", "non mesuré"]]
    sec.append(h2(11, "Plan de tests et résultats") + table(["Métrique", "Méthode", "Seuil", "Résultat"], plan_t, "", ["22%", "38%", "12%", "28%"]) +
               "<h3>Suites exécutées</h3>" + table(["Suite", "Réussis", "État", "Durée"], tl, "etroit", ["46%", "22%", "14%", "18%"]) +
               "<h3>Application aux cours réels (T2)</h3>" + table(["Cours", "α avant", "α après scripts", "β", "Tours", "Texte visible conservé", "Verdict"],
                     [[E(c["cours"].replace("_Phase_B_V0_", " ").replace(".html", "")), fr(c["alpha_avant"]), fr(c["alpha_apres"]), fr(c["beta"]), fr(c["tours_point_fixe"]), pc(c["texte_visible_conserve_pct"]), E(c["verdict"])] for c in T12], "", ["15%", "8%", "11%", "6%", "7%", "13%", "40%"]))

    # 12 phases
    ph = [["P0", "Inventaire du harnais existant", "fait (v1)"], ["P1", "Socle : bus, contrat, journal, empreintes, mutation, jeu doré", "fait"],
          ["P2", "Forme et captures (s1, s2, s5, s6, s7, s8)", "fait"], ["P3", "Concision et budgets (s3, s4)", "fait"],
          ["P3′", "160 scriptones : 140 synapses α/β par gabarit, 20 transversaux, registre, orchestre, calibrage sur 177 cours", "fait (v3)"],
          ["P3″", "Vue 3D branchée sur le journal ; essais T1–T4 ; 2 défauts corrigés (confluence, escalade)", "fait (28.10)"],
          ["P4", "Mutants médicaux (M5), registre des recommandations datées, branchement des agents réels (S1–S5, O1–O5)", "à faire"],
          ["P5", "Mesure du gain 5 → 16 auditeurs ; jetons de sortie réels", "à faire"],
          ["P6", "Correction de masse des LOT 001 à 012", "sur ordre de Vial seulement"]]
    sec.append(h2(12, "Phases de mise en œuvre") + table(["Phase", "Contenu", "État"], ph, "", ["10%", "68%", "22%"]))

    # 13 risques
    rk = [["Faux sentiment de sûreté (99,99 % mal lu)", "moyenne", "élevé", "afficher le périmètre : erreurs connues seulement ; M5 avant toute promesse clinique"],
          ["Un script juge la clinique", "faible", "élevé", "les scriptones ne créent aucun contenu médical ; le fond reste aux nœuds Opus par domaine"],
          ["Sur-contraction (perte de notions)", "moyenne", "élevé", "β·X exhaustivité adverse, planchers par point, contracteur ; texte visible mesuré ≥ 100 %"],
          ["Conflit d'écriture", "faible", "moyen", "une zone, un écrivain ; confluence contrôlée sur chaque fichier (s12)"],
          ["Scriptone altéré ou en panne", "faible", "moyen", "empreintes (s15), disjoncteur, jumeau, escalade ; 140/140 mesurées"],
          ["Boucle d'agents coûteuse", "moyenne", "moyen", "stagnation détectée par identifiant : fichier bloqué au 2e passage identique"],
          ["Faux positifs qui épuisent les agents", "moyenne", "moyen", "jeu doré à 0 doléance, variations neutres, calibrage sur 177 cours"],
          ["Dérive des heuristiques (lignes, jetons)", "moyenne", "faible", "étalon navigateur (captures.js) ; budgets recalibrés sur mesure"],
          ["Script dépendant d'un fichier absent de main", "faible", "moyen", "controle_lot.py se replie sans BANDE.json ; aucun script de PR ne dépend de harnais/brain"],
          ["Correction de masse non souhaitée", "faible", "élevé", "aucune écriture sur les LOT ; sur ordre de Vial seulement"]]
    sec.append(h2(13, "Risques") + table(["Risque", "Probabilité", "Impact", "Parade"], rk, "", ["30%", "11%", "9%", "50%"]))

    # 14 limites
    sec.append(h2(14, "Limites") + """<ul>
<li>Jetons estimés à 4 caractères par jeton ; les jetons de sortie des agents et la rédaction ne sont pas mesurés.</li>
<li>Détection mesurée sur des mutants connus, conçus par famille ; le jugement clinique n'est pas couvert (M5 à faire).</li>
<li>Aucun des 4 cours réels ne sort audité : les fautes graves restantes exigent les auditeurs, non appelés dans ces essais.</li>
<li>Extension à 16 auditeurs par étage non tranchée : elle exige une mesure sur agents réels.</li>
<li>Machine d'essai à 4 cœurs : 16 cours simultanés sont gérés sans conflit, mais le gain de temps plafonne à 4 processus.</li></ul>""")

    toc_html = "<ol class='toc'>" + "".join(f"<li><a href='#s{n}'>{E(t)}</a></li>" for n, t in toc) + "</ol>"
    sec.insert(1, f'<section class="sommaire"><h2 class="nonum">Sommaire</h2>{toc_html}</section>')
    return sec


CSS = """
@page{size:A4;margin:15mm 13mm 16mm 13mm}
*{box-sizing:border-box}
body{font-family:"Atkinson Hyperlegible",Arial,sans-serif;font-size:9.4pt;line-height:1.38;color:#111827;margin:0}
h1{font-size:34pt;margin:4mm 0 2mm;letter-spacing:.5px;color:#1e1b4b}
h2{font-size:14.5pt;color:#1e1b4b;border-bottom:1.6pt solid #4f46e5;padding-bottom:1.5mm;margin:0 0 3mm;break-before:page}
h2.nonum,h2.suite{break-before:auto}
h2.suite{margin-top:7mm}
h3{font-size:10.8pt;color:#312e81;margin:4.5mm 0 1.8mm;break-after:avoid}
p{margin:1.6mm 0 2mm}
code{font-family:"DejaVu Sans Mono",monospace;font-size:.86em;color:#1f2937}
table{width:100%;border-collapse:collapse;margin:2mm 0 3mm;table-layout:fixed;font-size:8.4pt;line-height:1.3}
th,td{border:.6pt solid #6b7280;padding:1.2mm 1.5mm;vertical-align:top;text-align:left;overflow-wrap:anywhere}
thead th{background:#e0e7ff;color:#1e1b4b;font-weight:700}
thead{display:table-header-group}
tr{break-inside:avoid}
tbody tr:nth-child(even) td{background:#f8fafc}
table.cat{font-size:6.6pt;line-height:1.22}
table.cat th,table.cat td{padding:.7mm .8mm}
table.petit{font-size:7.4pt}
table.param td:nth-child(odd){font-weight:700;background:#f1f5f9}
table.etroit{width:auto;min-width:60%}
table.kpi{font-size:9pt}
table.kpi td:nth-child(3){color:#111827}
.fiche{break-inside:avoid;margin-bottom:2mm}
.fiche table{margin:1.2mm 0 1.6mm}
.fiche h3{margin-top:3mm}
.note{border-left:2.4pt solid #d97706;background:#fffbeb;padding:2mm 3mm;margin:3mm 0}
.garde{padding-top:22mm}
.garde .sur{font-size:10pt;color:#4f46e5;font-weight:700;letter-spacing:.6px;text-transform:uppercase}
.garde .soustitre{font-size:12.5pt;color:#374151;margin-bottom:9mm;max-width:165mm}
.sommaire{break-before:page}
ol.toc{font-size:11pt;line-height:1.9;columns:1}
ol.toc a{color:#1e1b4b;text-decoration:none}
figure{margin:2mm 0 3mm;break-inside:avoid}
figure img{width:100%;border:.6pt solid #9ca3af;border-radius:2mm}
figcaption{font-size:8pt;color:#4b5563;margin-top:1mm}
.pastille{display:inline-block;width:3mm;height:3mm;border-radius:50%;vertical-align:-.4mm;margin-right:1mm}
svg{margin:2mm 0 1mm}
ul{margin:1mm 0 2mm 5mm;padding:0}
li{margin:.8mm 0}
"""

JS_PDF = r"""
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await (await b.newContext()).newPage();
  await p.goto('file://' + process.argv[2], {waitUntil: 'load'}); await p.evaluate(() => document.fonts.ready);
  await p.pdf({path: process.argv[3], format: 'A4', printBackground: true, displayHeaderFooter: true, margin: {top: '15mm', bottom: '16mm', left: '13mm', right: '13mm'},
    headerTemplate: '<div></div>',
    footerTemplate: '<div style="font-size:7.5pt;color:#6b7280;width:100%;padding:0 13mm;display:flex;justify-content:space-between;font-family:Arial"><span>BRAIN-HARNESS · chantier théorique v3</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>'});
  await b.close();
})();
"""


def main(a):
    if "--tests" in a: relever_tests()
    D = charger(); img = capture_3d()
    F = json.loads((R / "harnais/atkinson.b64.json").read_text(encoding="utf-8"))
    fontes = "".join(f'@font-face{{font-family:"Atkinson Hyperlegible";font-weight:{w};src:url("data:font/woff2;base64,{F[w]}") format("woff2")}}' for w in ("400", "700"))
    corps = "\n".join(construire(D, img))
    doc = f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Chantier BRAIN-HARNESS</title><style>{fontes}{CSS}</style></head><body>{corps}</body></html>'
    src = B / "CHANTIER_BRAIN_HARNESS.html"; src.write_text(doc, encoding="utf-8")
    pdf = B / "CHANTIER_BRAIN_HARNESS.pdf"; node(JS_PDF, src, pdf)
    print(f"{pdf} · {pdf.stat().st_size // 1024} Ko · source {src.name}")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
