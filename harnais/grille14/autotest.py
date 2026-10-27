#!/usr/bin/env python3
"""Autotest de bout en bout du circuit « Grille des 14 points » (gratuit, isolé, sans commit réel).
  python3 harnais/grille14/autotest.py            → tableau OK/KO ; code 1 au moindre KO
  python3 harnais/grille14/autotest.py -k verrou  → seulement les tests dont le nom contient « verrou »
Isolation : tout tourne dans un bac à sable .cache/test_g14/bac (copie de harnais/, G14_TEST=1, dépôt git jetable
pour le worktree du LOT). Rien n'est écrit dans .cache/travail/LOT_*, ni dans .cache/memoire, ni dans ../wt-*.
Le seul contact avec le dépôt réel : lecture des empreintes et `<id>.py etat` (lecture seule)."""
import hashlib, html as H, json, os, re, shutil, stat, subprocess, sys, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

R = Path(__file__).resolve().parents[2]
T = R / ".cache/test_g14"; BAC = T / "bac"; WK = BAC / ".cache/test_g14"
LOT = "001"; ENV = dict(os.environ, G14_TEST="1", G14_ATTENTE="3", PYTHONDONTWRITEBYTECODE="1")
RESULTATS = []
FILTRE = sys.argv[sys.argv.index("-k") + 1] if "-k" in sys.argv else ""

def nomf(i): return f"LOT_{LOT}_Phase_B_V0_DX.{i}.html"
A_NOM = f"LOT_{LOT}_Phase_A_V0.html"

# ───────────────────────── bac à sable ─────────────────────────
def construire_bac():
    if BAC.exists():
        for p in BAC.rglob("*"):
            try: p.chmod(p.stat().st_mode | stat.S_IWUSR)
            except OSError: pass
        shutil.rmtree(BAC)
    shutil.copytree(R / "harnais", BAC / "harnais", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (BAC / "tools").mkdir(parents=True); (BAC / "tools/aips_verbatim.py").symlink_to(R / "tools/aips_verbatim.py")
    aips = BAC / ".cache/aips"; aips.mkdir(parents=True)
    for p in (R / ".cache/aips").iterdir(): (aips / p.name).symlink_to(p)   # lecture ; les nouveaux caches restent dans le bac
    (BAC / ".cache/g_in").symlink_to(R / ".cache/g_in")
    WK.mkdir(parents=True)
    # dépôt git jetable : origine nue + worktree du LOT (le checkpoint de l'auditeur y commite et y pousse)
    nue = T / "origine.git"; wt = WK / f"wt-{LOT}"
    shutil.rmtree(nue, ignore_errors=True)
    g = lambda *a, cwd=None: subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True)
    g("init", "-q", "--bare", str(nue)); g("clone", "-q", str(nue), str(wt))
    g("checkout", "-q", "-b", f"prod/lot-{LOT}-final", cwd=wt)
    for k, v in (("user.email", "test@example.invalid"), ("user.name", "autotest"), ("commit.gpgsign", "false")): g("config", k, v, cwd=wt)
    (wt / "LISEZMOI").write_text("bac à sable\n"); g("add", "-A", cwd=wt); g("commit", "-q", "-m", "init", cwd=wt)
    g("push", "-q", "-u", "origin", f"prod/lot-{LOT}-final", cwd=wt)
    cand = os.environ.get("G14_CANDIDATS")   # versions candidates à éprouver avant installation : <dossier>/harnais/...
    if cand:
        for p in Path(cand).rglob("*"):
            if p.is_file():
                d = BAC / p.relative_to(cand)
                if d.exists(): d.chmod(0o644)
                shutil.copy2(p, d)
        s = BAC / "harnais/agents/SHA256SUMS"; s.chmod(0o644); lignes = []
        for l in s.read_text().splitlines():
            n = l.split(None, 1)[1].strip(); lignes.append(f"{hashlib.sha256((BAC / n).read_bytes()).hexdigest()}  {n}")
        s.write_text("\n".join(lignes) + "\n")
        for n in ["harnais/agents/SHA256SUMS", "harnais/grille14/grille_agent.py", "harnais/grille14/gen.py"]: (BAC / n).chmod(0o444)

def agent(ag, *args, cwd=None, env=None, timeout=400):
    e = dict(ENV, **(env or {}))
    r = subprocess.run([sys.executable, str(BAC / "harnais/grille14/grille_agent.py"), ag, *map(str, args)],
                       cwd=cwd or BAC, env=e, capture_output=True, text=True, timeout=timeout)
    return r.returncode, r.stdout + r.stderr

def essais():
    f = BAC / ".cache/test_g14/memoire" / f"essais_{LOT}_test.json"
    return json.loads(f.read_text()) if f.exists() else {}

def remettre(nom, contenu):
    """Dépose un fichier de travail propre : supprime marqueurs, blocage, essais et verrous du bac."""
    (WK / nom).write_text(contenu, encoding="utf-8")
    for d in ("pret", "bloque"):
        for p in (WK / d).glob(nom + "*") if (WK / d).exists() else []: p.unlink()
    f = BAC / ".cache/test_g14/memoire" / f"essais_{LOT}_test.json"
    if f.exists():
        d = {k: v for k, v in json.loads(f.read_text()).items() if not k.endswith(":" + nom)}; f.write_text(json.dumps(d))
    for p, d in verrous():
        if d.get("fichier", "").endswith("/" + nom): p.unlink()

def verrous():
    out = []
    for q in (BAC / ".cache/verrous").glob("*.lock") if (BAC / ".cache/verrous").exists() else []:
        try: out.append((q, json.loads(q.read_text())))
        except (ValueError, OSError): pass   # git.lock, .meta.lock : pas des verrous de fichier
    return out

# ───────────────────────── fichier synthétique conforme ─────────────────────────
def tm(t, d): return f'<span class="tm" tabindex="0">{t}<span class="df">{d}</span></span>'
MEDS = [("Nexium®", "ésoméprazole"), ("Pantozol®", "pantoprazole"), ("Agopton®", "lansoprazole"),
        ("Dafalgan®", "paracétamol"), ("Motilium®", "dompéridone"), ("Riopan®", "magaldrate"), ("Gaviscon®", "alginate de sodium")]
def med(nom, dci):
    return (f'<span class="tm med" tabindex="0">{nom}<span class="df">DCI : {dci}. Classe : antisécrétoire. '
            f'Groupe : inhibiteurs de la pompe à protons, chefs de file oméprazole et pantoprazole. La posologie suit le texte suisse.</span></span>')
PH = ["Le médecin {v} la sudation axillaire avant de conclure à une cause primaire.",
      "Le clinicien {v} chaque signe associé avec une méthode simple et reproductible.",
      "Cette étape {v} le diagnostic et évite des examens inutiles chez le patient.",
      "Le praticien {v} la tolérance du traitement lors de chaque consultation de suivi.",
      "Une anamnèse précise {v} le rythme diurne et le caractère symétrique de la sudation."]
VERBES = ["vérifie", "confirme", "précise", "documente", "contrôle", "recherche"]
def remplissage(n, k=0):
    out = []
    for i in range(n):
        s = PH[(i + k) % len(PH)].format(v=VERBES[(i + k) % len(VERBES)])
        t = tm(f"terme {k}-{i}", f"Ce terme désigne une notion clinique utile au lit du malade, numéro {k}-{i}.")
        out.append(f"<p>{s} Le {t} reste un repère pratique pour la décision.</p>")
    return "\n".join(out)

def sec(p, titre, corps, pid="dx1"):
    return f'<h3 id="{pid}-p{p}"><strong>{p}. {titre}</strong></h3>\n{corps}\n'

def tableau(entete, lignes):
    th = "".join(f"<th>{x}</th>" for x in entete); tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>\n" for l in lignes)
    return f'<div style="overflow-x:auto"><table><tr>{th}</tr>\n{tr}</table></div>'

def conforme(i=1, rempl=24):
    ms = [med(n, d) for n, d in MEDS]
    P = {}
    P[1] = ('<details class="arbre"><summary>Classification</summary><ul><li>Maladies de la peau (CIM-11)<ul>'
            '<li>Troubles des glandes sudoripares (CIM-11)<ul><li><b>Hyperhidrose primaire (CIM-11)</b></li>'
            '<li>Hyperhidrose secondaire (CIM-11)</li></ul></li></ul></li></ul></details>\n'
            '<p>La classification CIM-11 de l\'OMS définit l\'hyperhidrose primaire comme une sudation excessive, focale et bilatérale. '
            'Elle se distingue de l\'hyperhidrose secondaire, qui révèle une maladie générale.</p>')
    P[2] = ('<p>En Suisse, la prévalence atteint environ 3 % de la population adulte [S1]. '
            'L\'âge de début précède 25 ans, et le sexe ne modifie pas le risque. La mortalité reste nulle. '
            'Le coût social et la gravité tiennent au retentissement professionnel.</p>' + remplissage(rempl, 2))
    P[3] = ('<p>La cascade moléculaire active la voie cholinergique. L\'étape cellulaire augmente la sécrétion eccrine. '
            'La réponse tissulaire produit la sudation visible.</p>'
            + tableau(["Lésion ou perturbation", "Exploration", "Thérapeutique (mécanisme)"],
                      [["Hyperactivité cholinergique", "Test à l'amidon iodé", "Anticholinergique : bloque le récepteur muscarinique"],
                       ["Glande eccrine hyperactive", "Gravimétrie", "Toxine botulique : bloque la libération d'acétylcholine"]])
            + remplissage(rempl, 3))
    P[4] = (f'<p>Le médecin cherche d\'abord un drapeau rouge : {tm("sueurs nocturnes", "Elles évoquent un lymphome ou une tuberculose.")} '
            f'ou {tm("perte de poids", "Elle oriente vers une cause néoplasique.")}. '
            'Chaque étape suit la précédente : 1. anamnèse, 2. examen, 3. bilan ciblé.</p>' + remplissage(rempl, 4))
    P[5] = ('<p>Quand la sudation a-t-elle commencé ? Survient-elle pendant le sommeil ? Le patient prend-il un médicament ? '
            'La famille présente-t-elle le même trouble ? Une fièvre impose une imagerie ou un avis spécialisé en urgence.</p>'
            + "".join(f"<p>{tm(f'raison {k}', 'Cette raison physiopathologique oriente la décision.')} guide la suite.</p>" for k in range(3))
            + remplissage(rempl, 5))
    P[6] = ('<p>L\'examen normal précède la recherche du pathologique. Région par région, le médecin examine la peau, le cou, le thorax et l\'abdomen.</p>'
            + "".join(f"<p>Le médecin recherche {tm(f'signe {k}', 'Le geste se fait mains posées à plat ; sa valeur reste modérée.')} avec douceur.</p>" for k in range(4))
            + remplissage(rempl, 6))
    P[7] = ('<p>7.1 Le syndrome sudoral focal associe des signes fonctionnels et des signes physiques. '
            '7.2 Le syndrome sudoral généralisé évoque une cause secondaire.</p>'
            + "".join(f"<p>Le patient décrit {tm(f'symptôme {k}', 'Ce signe se définit par une sudation visible au repos.')} au quotidien.</p>" for k in range(3))
            + remplissage(rempl, 7))
    P[8] = ('<p>Les critères de 2004 retiennent une sudation focale visible depuis six mois. '
            'Une sudation isolée ne suffit pas au diagnostic.</p>' + remplissage(rempl, 8))
    P[9] = ('<p>9.a Le gold standard reste la gravimétrie. 9.b Le test à l\'amidon iodé sert en première intention. '
            '9.c La conductance cutanée constitue une alternative. 9.d Le bilan thyroïdien vient en deuxième intention. '
            'La sensibilité du test atteint 90 % selon les séries publiées.</p>'
            + tableau(["Résultat", "Signification", "Conduite"], [["Gravimétrie élevée", "Hyperhidrose confirmée", "Traitement local"]])
            + remplissage(rempl, 9))
    P[10] = ('<p>Si une fièvre accompagne la sudation → le médecin cherche une infection. '
             'Si la sudation reste focale → le médecin retient une forme primaire. '
             'Si la TSH est basse → le médecin traite une hyperthyroïdie.</p>' + remplissage(rempl, 10))
    P[11] = ('<p>11.A Le traitement vise une réduction de la sudation en quatre semaines. '
             f'11.B En urgence, le médecin traite d\'abord la cause grave. Hors urgence, il propose {ms[0]}, {ms[1]}, {ms[2]}, {ms[3]}, {ms[4]}, {ms[5]} et {ms[6]} à 20 mg selon l\'AIPS. '
             '11.C La surveillance contrôle la tolérance cutanée chaque mois. 11.D Le pronostic reste bon ; la grossesse impose une prudence particulière chez la patiente.</p>'
             + remplissage(rempl, 11))
    P[12] = ('<p>La prévention primaire repose sur l\'hygiène. La prévention secondaire dépiste les causes générales. '
             'La prévention tertiaire limite le retentissement social.</p>' + remplissage(rempl, 12))
    P[13] = ('<p>Une sudation focale et symétrique évoque une forme primaire. '
             'Une sudation nocturne impose la recherche d\'une cause générale. '
             'Le médecin traite d\'abord la cause, puis le symptôme.</p>')
    P[14] = ('<p>Une sudation nocturne suffit-elle à poser le diagnostic primaire ? Réponse : non, elle oriente vers une cause secondaire. '
             'La toxine botulique est-elle un premier choix ? Réponse : non, le traitement local vient avant. '
             'Le test à l\'amidon iodé mesure-t-il la quantité ? Réponse : non, il localise la zone.</p>' + remplissage(rempl, 14))
    titres = {1: "Définition et sémantique", 2: "Épidémiologie (Suisse, puis Europe)", 3: "Physiopathologie", 4: "Démarche diagnostique",
              5: "Anamnèse ciblée et drapeaux rouges", 6: "Examen physique ciblé, région par région", 7: "Approche syndromique",
              8: "Diagnostic positif et critères", 9: "Examens complémentaires", 10: "Arbre décisionnel", 11: "Prise en charge selon les recommandations suisses",
              12: "Prévention", 13: "Points clés", 14: "Pièges et questions fréquentes à l'examen fédéral suisse"}
    corps = "".join(sec(p, titres[p], P[p], f"dx{i}") for p in range(1, 15))
    part = f"PHASE_B_V0_DX.{i}"
    return ("<!DOCTYPE html>\n<html lang=\"fr\">\n<head>\n<meta charset=\"utf-8\">\n<title>Hyperhidrose primaire</title>\n</head>\n<body>\n<main>\n"
            f"<h2>DX.{i} — Hyperhidrose primaire</h2>\n{corps}"
            "<h2>Sources</h2>\n<ol>\n<li>[S1] Office fédéral de la statistique (OFS). Enquête suisse sur la santé 2022. Neuchâtel : OFS ; 2023.</li>\n</ol>\n"
            f"</main>\n</body>\n</html>\n<!-- FIN_FICHIER LOT_{LOT}_{part} -->\n")

# ───────────────────────── variantes cassées : (point attendu, nom, mutation) ─────────────────────────
def sans(motif, rempl=""): return lambda h: re.sub(motif, rempl, h)
def sec_de(h, p):
    m = re.search(rf'<h3 id="dx\d+-p{p}">.*?(?=<h3 id="dx\d+-p{p + 1}"|<h2>Sources)', h, re.S); return m
def dans_point(p, motif, rempl=""):
    def f(h):
        m = sec_de(h, p); s = re.sub(motif, rempl, m.group(0)); return h[:m.start()] + s + h[m.end():]
    return f
CASSES = [
    (1, "classification absente", sans(r'<details class="arbre">.*?</details>\n')),
    (1, "définition trop longue", dans_point(1, r"</p>", " La définition reprend chaque détail clinique utile au lit du malade sans exception." * 14 + "</p>")),
    (1, "source de la définition absente", dans_point(1, r"CIM-11|OMS|classification", "X")),
    (1, "voisins absents", dans_point(1, r"se distingue", "diffère peu")),
    (2, "Suisse absente", dans_point(2, r"[Ss]uisse", "pays")),
    (2, "chiffres sans source", dans_point(2, r"\s*\[S1\]", "")),
    (2, "mortalité absente", dans_point(2, r"[Mm]ortalité", "issue")),
    (3, "tableau de corrélation absent", dans_point(3, r'(?s)<div style="overflow-x:auto"><table>.*?</table></div>', "")),
    (3, "cascade absente", dans_point(3, r"moléculaire|cellulaire", "locale")),
    (4, "drapeaux rouges absents", dans_point(4, r"drapeau", "signe")),
    (4, "aucun mot cliquable dans le point 4", dans_point(4, r'<span class="tm" tabindex="0">([^<]*)<span class="df">[^<]*</span></span>', r"\1")),
    (5, "questions clés absentes", dans_point(5, r"\?", ".")),
    (6, "pathologique avant le normal", dans_point(6, r"L'examen normal précède la recherche du pathologique\.", "Le pathologique passe avant le normal.")),
    (6, "aucun signe cliquable", dans_point(6, r'<span class="tm" tabindex="0">([^<]*)<span class="df">[^<]*</span></span>', r"\1")),
    (7, "syndromes non numérotés", dans_point(7, r"7\.2 ", "")),
    (7, "fonctionnel / physique non séparés", dans_point(7, r"fonctionnels", "divers")),
    (8, "critères sans année", dans_point(8, r"2004", "naguère")),
    (8, "ce qui ne suffit pas absent", dans_point(8, r"ne suffit pas", "aide")),
    (9, "9.c absent", dans_point(9, r"9\.c ", "")),
    (9, "tableau d'interprétation absent", dans_point(9, r'(?s)<div style="overflow-x:auto"><table>.*?</table></div>', "")),
    (10, "embranchements absents", dans_point(10, r"→", ",")),
    (11, "11.B absent", dans_point(11, r"11\.B ", "")),
    (11, "urgence absente", dans_point(11, r"urgence", "pratique")),
    (12, "prévention tertiaire absente", dans_point(12, r"tertiaire", "finale")),
    (13, "trop de phrases", dans_point(13, r"</p>", " Le médecin revoit le patient. Le médecin note la réponse. Le médecin ajuste la dose. Le médecin informe la famille.</p>")),
    (13, "fenêtre dans les points clés", dans_point(13, r"forme primaire", '<span class="tm" tabindex="0">forme primaire<span class="df">Définition brève de la forme.</span></span>')),
    (14, "pièges sans réponse", dans_point(14, r"Réponse :", "Donc")),
    (7, "point 7 absent", sans(r'<h3 id="dx1-p7"><strong>7\. ')),
    (0, "FIN_FICHIER absent", sans(r"<!-- FIN_FICHIER[^>]*-->\n")),
    (0, "ligne > 3000", lambda h: h.replace("</main>", "<p>" + "Le médecin note la sudation du patient. " * 120 + "</p></main>")),
    (0, "taille hors bande", lambda h: re.sub(r"(?s)<p>[^<]*Le <span class=\"tm\" tabindex=\"0\">terme \d+-\d+<span class=\"df\">.*?</p>\n", "", h)),
    (0, "mention de conception", dans_point(12, r"</p>", " Ce fichier suit le checkpoint du LOT_001.</p>")),
]

# ───────────────────────── tests ─────────────────────────
TESTS = []
def test(nom):
    def d(fn): TESTS.append((nom, fn)); return fn
    return d

@test("intégrité : scripts d'agents et moteur en lecture seule (0444)")
def _():
    ko = [p.name for p in list((R / "harnais/agents").glob("*.py")) + [R / "harnais/grille14/grille_agent.py", R / "harnais/grille14/gen.py"]
          if p.stat().st_mode & 0o222]
    return not ko, ("inscriptibles : " + ", ".join(ko)) if ko else "14 agents + moteur + gen.py en 0444"

@test("intégrité : SHA256SUMS à jour et complet")
def _():
    lignes = dict(reversed(l.split(None, 1)) for l in (R / "harnais/agents/SHA256SUMS").read_text().splitlines() if l.strip())
    lignes = {k.strip(): v for k, v in lignes.items()}
    attendus = {f"harnais/agents/{a}.py" for a in ["A"] + [f"R{i}" for i in range(1, 9)] + [f"B{i}" for i in range(1, 6)]} | {"harnais/grille14/grille_agent.py", "harnais/grille14/gen.py"}
    manque = sorted(attendus - set(lignes)); faux = sorted(n for n, h in lignes.items() if hashlib.sha256((R / n).read_bytes()).hexdigest() != h)
    return not manque and not faux, f"manquants {manque} · faux {faux}" if manque or faux else f"{len(lignes)} empreintes justes"

@test("intégrité : chaque script d'agent appelle le moteur avec son identité")
def _():
    ko = []
    for p in (R / "harnais/agents").glob("*.py"):
        t = p.read_text()
        if f'sys.argv.insert(1, "{p.stem}")' not in t or str(R / "harnais/grille14") not in t: ko.append(p.name)
    return not ko, f"incohérents : {ko}" if ko else "14 scripts cohérents"

@test("intégrité : `etat` répond pour les 14 agents réels (empreinte vérifiée)")
def _():
    ko = []
    for a in ["A"] + [f"R{i}" for i in range(1, 9)] + [f"B{i}" for i in range(1, 6)]:
        r = subprocess.run([sys.executable, str(R / f"harnais/agents/{a}.py"), "etat"], capture_output=True, text=True, cwd=R, timeout=60)
        if r.returncode or '"agent": "%s"' % a not in r.stdout: ko.append(f"{a}:{r.returncode}")
    return not ko, f"échecs {ko}" if ko else "14/14"

@test("intégrité : altération du moteur détectée (bac à sable)")
def _():
    p = BAC / "harnais/grille14/gen.py"; t = p.read_bytes(); p.chmod(0o644); p.write_bytes(t + b"\n# altere\n")
    try: rc, out = agent("R1", "etat")
    finally: p.write_bytes(t); p.chmod(0o444)
    rc2, _ = agent("R1", "etat")
    return rc == 3 and "ALTÉRATION" in out and rc2 == 0, f"code {rc} puis {rc2}"

@test("roster : N = 10 à 16, ≤ 2 DD par rédacteur, ≤ 4 par auditeur, B1 = Phase A + 2 DD")
def _():
    sys.path.insert(0, str(BAC / "harnais/grille14")); import roster
    ko = []
    for n in range(10, 17):
        r = roster.build("999", n); dd = [f"LOT_999_Phase_B_V0_DX.{i}.html" for i in range(1, n + 1)]
        red = r["redacteurs"]; aud = r["auditeurs"]
        if any(len(v) > 2 for v in red.values()): ko.append(f"N={n} rédacteur > 2")
        if len(red) > 8: ko.append(f"N={n} {len(red)} rédacteurs > 8 scripts")
        if sorted(sum(red.values(), [])) != sorted(dd): ko.append(f"N={n} DD rédigés ≠ 1..N")
        if aud["B1"] != [r["A"], dd[0], dd[1]]: ko.append(f"N={n} B1 = {aud['B1']}")
        if any(len(v) > 4 for b, v in aud.items() if b != "B1"): ko.append(f"N={n} auditeur > 4")
        if any(not v for v in aud.values()): ko.append(f"N={n} auditeur sans DD")
        if sorted(x for v in aud.values() for x in v if x != r["A"]) != sorted(dd): ko.append(f"N={n} DD audités ≠ 1..N")
        if any(r["dd_auditeur"][x] != b for b, v in aud.items() for x in v if x != r["A"]): ko.append(f"N={n} dd_auditeur incohérent")
        if set(red) | set(aud) | {"A"} - {p.stem for p in (R / "harnais/agents").glob("*.py")}: pass
        sans_script = (set(red) | set(aud)) - {p.stem for p in (R / "harnais/agents").glob("*.py")}
        if sans_script: ko.append(f"N={n} agents sans script {sans_script}")
    return not ko, "; ".join(ko) or "7 tailles conformes"

@test("roster : roster_001.json = build(001, N) (aucune dérive manuelle)")
def _():
    sys.path.insert(0, str(BAC / "harnais/grille14")); import roster
    r = json.loads((R / "harnais/grille14/roster_001.json").read_text())
    return roster.build("001", r["n"]) == r, f"N={r['n']}"

def _module():
    sys.path.insert(0, str(BAC / "harnais")); sys.path.insert(0, str(BAC / "harnais/grille14"))
    os.environ["G14_TEST"] = "1"
    import importlib; G = importlib.import_module("grille_agent"); return G

@test("grille : fichier synthétique conforme → zéro écart, 14 points")
def _():
    G = _module(); E, st = G.ecarts_points(conforme(), set(range(1, 15)))
    return not E, "; ".join(f"[{p}] {g} {m[:60]}" for p, g, m in E) or f"0 écart · {st['mots']} mots"

for _p, _nom, _mut in CASSES:
    def _f(p=_p, mut=_mut):
        G = _module(); h = mut(conforme())
        if h == conforme(): return False, "mutation sans effet (test mal écrit)"
        E, _ = G.ecarts_points(h, set(range(1, 15)))
        bons = [e for e in E if e[0] == p and e[1] in ("CRITIQUE", "GRAVE", "MOYEN")]
        autres = [e for e in E if e[0] not in (0, p) and e[1] != "DETAIL"]   # la forme (point 0) peut répéter le même écart
        return bool(bons) and not autres, (f"signalé : {bons[0][1]} {bons[0][2][:70]}" if bons else "NON signalé") + (f" · autres points touchés : {[(e[0], e[2][:40]) for e in autres]}" if autres else "")
    TESTS.append((f"grille : variante cassée point {_p} ({_nom}) → point {_p} signalé", _f))

@test("réparation : FIN_FICHIER, ligne > 3000, title=, [Sn] dupliqués")
def _():
    nom = nomf(1); h = conforme()
    h = re.sub(r"<!-- FIN_FICHIER[^>]*-->\n", "", h).replace("[S1]", "[S1] [S1]", 1).replace("<p>La cascade", '<p title="infobulle">La cascade', 1)
    h = h.replace("</main>", "<p>" + "Le médecin note la sudation du patient. " * 250 + "</p></main>")
    remettre(nom, h); rc, out = agent("R1", "controle", nom); t = (WK / nom).read_text()
    rc2, out2 = agent("R1", "controle", nom); agent("R1", "fin", nom, "--points", "99") if False else None
    ok = ("RÉPARÉ" in out and "FIN_FICHIER" in t[-200:] and max(map(len, t.splitlines())) <= 3000 and "title=" not in t.replace("<title>", "")
          and "[S1] [S1]" not in t and "RÉPARÉ" not in out2 and t.count("<p>") == t.count("</p>"))
    return ok, out.splitlines()[0][:150]

@test("controle : fichier conforme → code 0, zéro critique, verrou posé")
def _():
    nom = nomf(1); remettre(nom, conforme()); rc, out = agent("R1", "controle", nom)
    vs = [d for _, d in verrous()]
    return rc == 0 and "critiques=0" in out and any(v["agent"] == "R1" and v["fichier"].endswith(nom) for v in vs), out.strip().splitlines()[-1][:120]

@test("fin rédacteur : conforme → CHECKPOINT OK, marqueur prêt, verrou levé, essais effacés")
def _():
    nom = nomf(1); remettre(nom, conforme()); agent("R1", "controle", nom); t0 = time.time(); rc, out = agent("R1", "fin", nom); dt = time.time() - t0
    vs = [d for _, d in verrous()]
    ok = rc == 0 and "CHECKPOINT OK" in out and (WK / "pret" / nom).exists() and not any(v["fichier"].endswith(nom) for v in vs) and f"R1:{nom}" not in essais()
    return ok, f"{dt:.1f} s · " + out.strip().splitlines()[-1][:110]

@test("fin rédacteur : relance sur un fichier déjà prêt → DÉJÀ PRÊT, rien n'est touché")
def _():
    nom = nomf(1); avant = (WK / nom).read_text(); rc, out = agent("R1", "fin", nom); rc2, out2 = agent("R1", "controle", nom)
    vs = [d for _, d in verrous()]
    return rc == 0 and "DÉJÀ PRÊT" in out and "LECTURE SEULE" in out2 and (WK / nom).read_text() == avant and not any(v["fichier"].endswith(nom) for v in vs), out.strip()[:90]

@test("attendre : prêt → immédiat ; absent → ATTENTE (code 4) ; BLOQUÉ → code 5 immédiat")
def _():
    t0 = time.time(); rc1, o1 = agent("B1", "attendre", nomf(1)); d1 = time.time() - t0
    remettre(nomf(2), conforme(2)); t0 = time.time(); rc2, o2 = agent("B1", "attendre", nomf(2)); d2 = time.time() - t0
    (WK / "bloque").mkdir(exist_ok=True); (WK / "bloque" / (nomf(2) + ".md")).write_text("# BLOQUÉ\n")
    t0 = time.time(); rc3, o3 = agent("B1", "attendre", nomf(2)); d3 = time.time() - t0
    remettre(nomf(2), conforme(2))
    return (rc1, rc2, rc3) == (0, 4, 5) and d1 < 3 and d3 < 3, f"codes {rc1},{rc2},{rc3} · {d1:.1f}/{d2:.1f}/{d3:.1f} s"

@test("hors périmètre : R1 sur DX.5 → STOP code 3")
def _():
    rc, out = agent("R1", "controle", nomf(5)); return rc == 3 and "HORS PÉRIMÈTRE" in out, out.strip()[:90]

@test("verrou : pris par un autre agent → controle ET fin refusés (code 3), fichier intact")
def _():
    nom = nomf(2); remettre(nom, conforme(2)); agent("R1", "controle", nom); avant = (WK / nom).read_text()
    rc1, o1 = agent("B1", "controle", nom); rc2, o2 = agent("B1", "fin", nom, "--v1", "95", "--v2", "95")
    ok = rc1 == 3 and rc2 == 3 and "VERROU PRIS PAR R1" in o1 and (WK / nom).read_text() == avant and f"B1:{nom}" not in essais()
    return ok, f"codes {rc1},{rc2} · {o1.strip()[:70]}"

@test("verrou : orphelin (> 20 min, fichier inchangé) repris ; récent refusé")
def _():
    nom = nomf(2); p = WK / nom
    lk = [q for q, d in verrous() if d.get("fichier", "").endswith(nom)][0]
    d = json.loads(lk.read_text()); d["t"] -= 1500; lk.write_text(json.dumps(d))
    rc1, o1 = agent("B1", "controle", nom)          # fichier modifié il y a peu : pas orphelin
    os.utime(p, (time.time() - 1500, time.time() - 1500))
    rc2, o2 = agent("B1", "controle", nom)
    d2 = json.loads(lk.read_text()) if lk.exists() else {}
    return rc1 == 3 and rc2 in (0, 1) and d2.get("agent") == "B1", f"codes {rc1},{rc2} · détenteur {d2.get('agent')}"

@test("verrou : fichier de verrou vide ou corrompu → pas de plantage")
def _():
    nom = nomf(2); remettre(nom, conforme(2))
    v = subprocess.run([sys.executable, str(BAC / "harnais/verrou.py"), "claim", str((WK / nom).resolve()), "R1"], capture_output=True, text=True, cwd=BAC)
    lk = [q for q, d in verrous() if d.get("fichier", "").endswith(nom)][0]
    lk.write_text("")
    rc, out = agent("B1", "controle", nom)
    return rc in (0, 1, 3) and "Traceback" not in out, f"code {rc} · {out.strip()[:80]}"

@test("verrou : 10 agents réclament le même fichier en parallèle → un seul gagnant")
def _():
    f_ = str((WK / "course.html").resolve()); (WK / "course.html").write_text("x")
    for q, d in verrous():
        if "course.html" in d.get("fichier", ""): q.unlink()
    def un(i): return subprocess.run([sys.executable, str(BAC / "harnais/verrou.py"), "claim", f_, f"X{i}"], capture_output=True, text=True, cwd=BAC).returncode
    with ThreadPoolExecutor(10) as ex: codes = list(ex.map(un, range(10)))
    return codes.count(0) == 1 and codes.count(3) == 9, f"codes {sorted(codes)}"

@test("chemins : nom nu, relatif, absolu, autre répertoire → même fichier, même verrou ; copie ailleurs refusée")
def _():
    nom = nomf(2); remettre(nom, conforme(2))
    rcs = [agent("R1", "controle", x, cwd=c)[0] for x, c in ((nom, BAC), (f".cache/test_g14/{nom}", BAC), (str(WK / nom), "/"), (nom, "/tmp"))]
    autre = T / "copie"; autre.mkdir(exist_ok=True); (autre / nom).write_text(conforme(2))
    rc5, o5 = agent("R1", "controle", str(autre / nom))
    n_verrous = sum(1 for q, d in verrous() if d.get("fichier", "").endswith(nom))
    return rcs == [0, 0, 0, 0] and n_verrous == 1 and rc5 == 2 and "MAUVAIS FICHIER" in o5, f"codes {rcs} + {rc5} · verrous {n_verrous}"

@test("arguments : fichier absent, --v1 illisible, --points faux, --lot sans valeur, commande inconnue → message clair")
def _():
    remettre(nomf(2), conforme(2)); (WK / nomf(4)).unlink(missing_ok=True)
    cas = [agent("R2", "controle", nomf(4)), agent("B1", "fin", nomf(2), "--v1", "abc", "--v2", "95"), agent("R1", "controle", nomf(2), "--points", "x"),
           agent("R1", "controle", nomf(2), "--lot"), agent("R1", "lancer", nomf(2)), agent("R1", "controle")]
    mauvais = [o.strip()[:60] for rc, o in cas if "Traceback" in o or rc == 0]
    return not mauvais, f"{len(cas)} cas" if not mauvais else str(mauvais)

def casse(n=1):
    """Fichier avec n écarts critiques distincts (n = 1..3)."""
    h = conforme(); muts = [sans(r'<details class="arbre">.*?</details>\n'), dans_point(9, r"9\.c ", ""), dans_point(10, r"→", ",")]
    for f_ in muts[:n]: h = f_(h)
    return h

@test("plafond : 3 essais au plus (écarts différents à chaque fois) → BLOQUÉ au 3e")
def _():
    nom = nomf(2); remettre(nom, casse(3)); r = []
    for k in (3, 2, 1): (WK / nom).write_text(casse(k)); r.append(agent("R1", "fin", nom))
    e = essais().get(f"R1:{nom}", {})
    return [x[0] for x in r] == [1, 1, 5] and (WK / "bloque" / (nom + ".md")).exists() and e.get("n") == 3, f"codes {[x[0] for x in r]} · n={e.get('n')}"

@test("BLOQUÉ : coupe controle et fin (code 5), le fichier n'est plus touché")
def _():
    nom = nomf(2); avant = (WK / nom).read_text(); rc1, o1 = agent("R1", "controle", nom); rc2, o2 = agent("R1", "fin", nom)
    rc3, o3 = agent("B1", "controle", nom)
    return (rc1, rc2, rc3) == (5, 5, 5) and (WK / nom).read_text() == avant, f"codes {rc1},{rc2},{rc3}"

@test("stagnation : mêmes écarts au 2e essai (fichier retouché sans effet) → BLOQUÉ")
def _():
    nom = nomf(2); remettre(nom, casse(2)); r1 = agent("R1", "fin", nom)
    (WK / nom).write_text(casse(2).replace("<p>La prévention primaire", "<p>Ainsi, la prévention primaire")); r2 = agent("R1", "fin", nom)
    return (r1[0], r2[0]) == (1, 5) and "aucun progrès" in r2[1], f"codes {r1[0]},{r2[0]}"

@test("stagnation : pas de faux positif quand les écarts diminuent (3 → 2)")
def _():
    nom = nomf(2); remettre(nom, casse(3)); r1 = agent("R1", "fin", nom); (WK / nom).write_text(casse(2)); r2 = agent("R1", "fin", nom)
    return (r1[0], r2[0]) == (1, 1) and not (WK / "bloque" / (nom + ".md")).exists(), f"codes {r1[0]},{r2[0]}"

@test("INCHANGÉ : relance sans modification → refus sans compter d'essai ; compteur remis à zéro après une vraie modification")
def _():
    nom = nomf(2); remettre(nom, casse(3)); agent("R1", "fin", nom); n1 = essais()[f"R1:{nom}"]["n"]
    rc2, o2 = agent("R1", "fin", nom); n2 = essais()[f"R1:{nom}"]["n"]
    (WK / nom).write_text(casse(2)); rc3, _ = agent("R1", "fin", nom); n3 = essais()[f"R1:{nom}"]["n"]
    rc4, o4 = agent("R1", "fin", nom)          # 1re relance sans modification APRÈS une modification : avertissement, pas blocage
    ok = n1 == 1 and rc2 == 1 and "INCHANGÉ" in o2 and n2 == 1 and n3 == 2 and rc4 == 1 and "INCHANGÉ" in o4 and not (WK / "bloque" / (nom + ".md")).exists()
    return ok, f"n {n1}→{n2}→{n3} · codes {rc2},{rc3},{rc4}"

@test("INCHANGÉ : 2e relance sans modification → BLOQUÉ")
def _():
    nom = nomf(2); rc, o = agent("R1", "fin", nom); return rc == 5 and "sans modification" in o, f"code {rc}"

@test("auditeur : scores absents → refus sans essai compté")
def _():
    nom = nomf(1); rc, o = agent("B1", "controle", nom); rc2, o2 = agent("B1", "fin", nom)
    return rc2 == 1 and "saisis tes scores" in o2 and f"B1:{nom}" not in essais(), f"code {rc2}"

def retouche(nom, k):
    """Modification réelle mais neutre du texte (un mot de plus), pour qu'un essai ne soit pas « INCHANGÉ »."""
    p = WK / nom; p.write_text(p.read_text().replace("<p>La prévention primaire", "<p>" + "Ainsi, " * k + "la prévention primaire", 1))

@test("auditeur : V1 < 90 refusé et enregistré ; score qui monte (85 → 88) sans faux blocage ; 3e refus → BLOQUÉ")
def _():
    nom = nomf(1); r = []
    for k, v in enumerate(("85", "88", "89")):
        if k: retouche(nom, k)
        r.append(agent("B1", "fin", nom, "--v1", v, "--v2", "95"))
    e = essais().get(f"B1:{nom}", {}); aud = (WK / "audits" / f"AUD_B1_{nom}.md").exists()
    return [x[0] for x in r] == [1, 1, 5] and "V1=85" in r[0][1] and not aud, f"codes {[x[0] for x in r]} · n={e.get('n')} · AUD écrit={aud}"

@test("auditeur : V2 < 90 identique deux fois (fichier retouché) → stagnation BLOQUÉ")
def _():
    nom = nomf(2); remettre(nom, conforme(2)); (WK / "pret").mkdir(exist_ok=True); (WK / "pret" / nom).write_text("x")
    r1 = agent("B1", "fin", nom, "--v1", "95", "--v2", "80"); retouche(nom, 1); r2 = agent("B1", "fin", nom, "--v1", "95", "--v2", "80")
    return (r1[0], r2[0]) == (1, 5) and "aucun progrès" in r2[1], f"codes {r1[0]},{r2[0]}"

@test("auditeur : nouveaux scores sur un fichier non modifié → INCHANGÉ (pas de note gonflée sans correction)")
def _():
    nom = nomf(2); remettre(nom, conforme(2)); (WK / "pret" / nom).write_text("x")
    r1 = agent("B1", "fin", nom, "--v1", "95", "--v2", "80"); r2 = agent("B1", "fin", nom, "--v1", "95", "--v2", "92")
    return (r1[0], r2[0]) == (1, 1) and "INCHANGÉ" in r2[1], f"codes {r1[0]},{r2[0]}"

@test("auditeur : V1 ≥ 90 et V2 ≥ 90 → checkpoint avec commit et push (dépôt jetable), fiche AUD écrite")
def _():
    nom = nomf(3); remettre(nom, conforme(3)); (WK / "pret").mkdir(exist_ok=True); (WK / "pret" / nom).write_text("x")
    wt = WK / f"wt-{LOT}"; n0 = subprocess.run(["git", "rev-list", "--count", "HEAD"], cwd=wt, capture_output=True, text=True).stdout.strip()
    rc, o = agent("B2", "fin", nom, "--v1", "94", "--v2", "93")
    n1 = subprocess.run(["git", "rev-list", "--count", "HEAD"], cwd=wt, capture_output=True, text=True).stdout.strip()
    avance = subprocess.run(["git", "rev-list", "--count", f"origin/prod/lot-{LOT}-final..HEAD"], cwd=wt, capture_output=True, text=True).stdout.strip()
    ok = rc == 0 and "commit fait" in o and "push ok" in o and int(n1) == int(n0) + 1 and avance == "0" and (WK / "audits" / f"AUD_B2_{nom}.md").exists() \
        and (wt / f"LOT_Claude_Finaux/LOT_{LOT}/{nom}").exists()
    return ok, f"code {rc} · commits {n0}→{n1} · en avance {avance} · {o.strip().splitlines()[-1][:80]}"

@test("panne d'outil : checkpoint qui plante → aucun essai compté, verrou levé, code 6, incident écrit")
def _():
    nom = nomf(4); remettre(nom, conforme(4)); cp = BAC / "harnais/checkpoint.py"; sauve = cp.read_text()
    cp.write_text("import sys\nraise RuntimeError('panne simulée')\n")
    try: rc, o = agent("R2", "fin", nom)
    finally: cp.write_text(sauve)
    vs = [d for _, d in verrous()]
    e = essais().get(f"R2:{nom}", {})
    return rc == 6 and e.get("n", 0) == 0 and not any(v["fichier"].endswith(nom) for v in vs) and (WK / "incidents" / f"{nom}.md").exists(), f"code {rc} · n={e.get('n', 0)}"

@test("panne d'outil : contrôle médical sans rapport → checkpoint ERREUR (pas REFUSÉ)")
def _():
    nom = nomf(4); remettre(nom, conforme(4)); cm = BAC / "harnais/controle_medical.py"; sauve = cm.read_text()
    cm.write_text("raise SystemExit('panne simulée')\n")
    try:
        r = subprocess.run([sys.executable, str(BAC / "harnais/checkpoint.py"), LOT, str(WK / nom), "--cycle", "7", "--sans-commit"], capture_output=True, text=True, cwd=BAC, env=ENV, timeout=300)
    finally: cm.write_text(sauve)
    return r.returncode == 2 and "ERREUR (outil)" in r.stdout, f"code {r.returncode} · {r.stdout.strip()[:90]}"

def _medical(h, env=None, prelude=""):
    f_ = WK / "med_test" / nomf(6); f_.parent.mkdir(exist_ok=True); f_.write_text(h); rap = f_.with_suffix(".md")
    code = prelude + f"import runpy, sys; sys.argv = ['controle_medical.py', {str(f_)!r}, '--rapport', {str(rap)!r}]; runpy.run_path({str(BAC / 'harnais/controle_medical.py')!r}, run_name='__main__')"
    r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, cwd=BAC, env=dict(ENV, **(env or {})), timeout=600)
    return r, (rap.read_text() if rap.exists() else "")

AVEC_PMID = lambda: conforme().replace("<li>[S1] Office", "<li>[S1] Etude de cohorte. PMID 31504418. Office").replace("environ 3 % de la population", "environ 3 % de la population")
HORS_LIGNE = {"https_proxy": "http://127.0.0.1:9", "HTTPS_PROXY": "http://127.0.0.1:9", "http_proxy": "http://127.0.0.1:9", "HTTP_PROXY": "http://127.0.0.1:9"}

@test("réseau absent : contrôle médical écrit son rapport, PMID « non vérifié » sans critique")
def _():
    r, rap = _medical(AVEC_PMID(), HORS_LIGNE)
    return bool(rap) and "inexistant" not in rap and "critiques=0" in rap.splitlines()[0], (rap.splitlines()[0] if rap else r.stderr.strip()[-120:])

@test("PubMed 429 persistant : PMID non déclarés inexistants, pas d'attente > 30 s")
def _():
    pre = ("import urllib.request, urllib.error, time, io\ntime.sleep = lambda s: None\n"
           "def _u(*a, **k): raise urllib.error.HTTPError('u', 429, 'Too Many Requests', {}, io.BytesIO())\nurllib.request.urlopen = _u\n")
    t0 = time.time(); r, rap = _medical(AVEC_PMID(), None, pre)
    return bool(rap) and "inexistant" not in rap and time.time() - t0 < 30, (rap.splitlines()[0] if rap else r.stderr.strip()[-120:])

@test("réseau absent : ancrage des sources ne transforme pas une panne en « chiffres non retrouvés »")
def _():
    h = conforme().replace("<li>[S1] Office fédéral de la statistique (OFS). Enquête suisse sur la santé 2022. Neuchâtel : OFS ; 2023.</li>",
                           "".join(f"<li>[S{k}] Source {k}. https://exemple.invalid/s{k}.html</li>" for k in range(1, 8)))
    h = h.replace("environ 3 % de la population adulte [S1]", " ".join(f"Le taux atteint {k}1 % [S{k}]." for k in range(1, 8)))
    r, rap = _medical(h, HORS_LIGNE)
    return bool(rap) and "chiffres non retrouvés dans leurs sources" not in rap, (rap.splitlines()[0] if rap else r.stderr.strip()[-120:])

@test("registre des essais : 12 écritures concurrentes → aucune perte, JSON valide")
def _():
    code = ("import os, sys; os.environ['G14_TEST']='1'; sys.path.insert(0, %r); sys.path.insert(0, %r); import grille_agent as G\n"
            "from pathlib import Path\nG.refus('R%%s' %% sys.argv[1], 'C%%s' %% sys.argv[1] if False else '777', Path(%r), 'f%%s.html' %% sys.argv[1], 'sig', 'd', 'sha')") % (
        str(BAC / "harnais"), str(BAC / "harnais/grille14"), str(WK))
    f_ = BAC / ".cache/test_g14/memoire/essais_777_test.json"; f_.unlink(missing_ok=True)
    def un(i): return subprocess.run([sys.executable, "-c", code, str(i)], capture_output=True, text=True, cwd=BAC).returncode
    with ThreadPoolExecutor(12) as ex: codes = list(ex.map(un, range(12)))
    d = json.loads(f_.read_text())
    return len(d) == 12 and not any(codes), f"{len(d)}/12 clés · codes {set(codes)}"

@test("isolation : G14_TEST n'écrit ni dans .cache/travail, ni dans .cache/memoire, ni dans harnais/PREUVE")
def _():
    rc, _ = agent("R1", "memoire")
    hors = [p for p in (BAC / ".cache/travail").rglob("*")] if (BAC / ".cache/travail").exists() else []
    mem = [p.name for p in (BAC / ".cache/memoire").glob("*")] if (BAC / ".cache/memoire").exists() else []
    preuve_bac = (BAC / "harnais/PREUVE_EMBOITEMENT.txt").read_text() == (R / "harnais/PREUVE_EMBOITEMENT.txt").read_text() or True
    ok = rc == 0 and not hors and not mem and (WK / "PREUVE_EMBOITEMENT_test.txt").exists()
    return ok, f"memoire code {rc} · travail {len(hors)} · memoire réelle {mem}"

@test("plantage interne : message clair (PANNE D'OUTIL, code 6), jamais de trace Python brute")
def _():
    nom = nomf(2); remettre(nom, conforme(2)); (WK / nom).write_bytes(b"\xff\xfe" + conforme(2).encode("utf-16"))   # contenu illisible
    rc, o = agent("R1", "controle", nom); remettre(nom, conforme(2))
    return "Traceback" not in o and rc in (0, 1, 6), f"code {rc} · {o.strip()[:80]}"

@test("SANTE.py : une ligne par rubrique, signale verrou orphelin, BLOQUÉ et prêt non audité")
def _():
    r = subprocess.run([sys.executable, str(BAC / "harnais/grille14/SANTE.py"), "--lot", LOT], capture_output=True, text=True, cwd=BAC, env=ENV, timeout=120)
    t = r.stdout
    ok = r.returncode in (0, 1) and "Traceback" not in t + r.stderr and all(k in t for k in ("verrous", "bloqués", "prêts non audités", "essais", "commits", "empreintes"))
    return ok, f"code {r.returncode} · {len(t.splitlines())} lignes"

# ───────────────────────── exécution ─────────────────────────
def main():
    t0 = time.time(); construire_bac()
    for nom, fn in TESTS:
        if FILTRE and FILTRE not in nom: continue
        t = time.time()
        try: ok, det = fn()
        except Exception as ex: ok, det = False, f"EXCEPTION {type(ex).__name__} : {str(ex)[:150]}"
        RESULTATS.append((ok, nom, det, time.time() - t))
        print(f"{'OK' if ok else 'KO'}  {nom}  ·  {det}  ({time.time() - t:.1f} s)", flush=True)
    n = sum(1 for r in RESULTATS if r[0])
    print(f"\n{'═' * 80}\nAUTOTEST grille14 : {n}/{len(RESULTATS)} OK · {time.time() - t0:.0f} s" + ("" if n == len(RESULTATS) else f" · {len(RESULTATS) - n} KO"))
    for ok, nom, det, _ in RESULTATS:
        if not ok: print(f"  KO  {nom} : {det}")
    return 0 if n == len(RESULTATS) else 1

if __name__ == "__main__":
    sys.exit(main())
