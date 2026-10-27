#!/usr/bin/env python3
"""Autotest du circuit « Grille des 14 points » et du CONTRACTEUR DE TEXTE (gratuit, isolé, sans commit, < 90 s).
  python3 harnais/grille14/autotest.py            → tableau OK/KO ; code 1 au moindre KO
  python3 harnais/grille14/autotest.py -k visa    → seulement les tests dont le nom contient « visa »
  G14_CANDIDATS=<dossier> : éprouve des versions candidates (<dossier>/harnais/...) dans le bac avant installation.
Isolation : tout tourne dans un bac à sable .cache/test_g14/bac (copie de harnais/, G14_TEST=1, dépôt git jetable).
Contrôles médical et de langue simulés (rapides) ; réseau et PubMed non sollicités. Rien n'est écrit dans .cache/travail/LOT_*,
.cache/memoire, ../wt-* : le dernier test le prouve par empreintes."""
import contextlib, hashlib, io, json, os, re, shutil, stat, subprocess, sys, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

R = Path(__file__).resolve().parents[2]
T = R / ".cache/test_g14"; BAC = T / "bac"; WK = BAC / ".cache/test_g14"
LOT = "001"; ENV = dict(os.environ, G14_TEST="1", G14_ATTENTE="1", PYTHONDONTWRITEBYTECODE="1")
for k in ("G14_CIBLE_PCT", "G14_CIBLE_MOTS"): ENV.pop(k, None)
RESULTATS = []
FILTRE = sys.argv[sys.argv.index("-k") + 1] if "-k" in sys.argv else ""
SCRIPTS = ["A"] + [f"R{i}" for i in range(1, 9)] + [f"B{i}" for i in range(1, 6)] + [f"KB{i}" for i in range(1, 6)]
MOTEURS = ["harnais/grille14/grille_agent.py", "harnais/grille14/gen.py", "harnais/contracteur/contracteur.py"]
def nomf(i): return f"LOT_{LOT}_Phase_B_V0_DX.{i}.html"

# ───────────────────────── empreintes du réel (preuve d'isolation) ─────────────────────────
def empreinte_reel():
    h = hashlib.sha256()
    for p in sorted((R / f".cache/travail/LOT_{LOT}").rglob("*")) + [R / f".cache/memoire/essais_{LOT}.json"] + sorted((R / ".cache/memoire").glob("*.json")):
        if p.is_file(): h.update(p.name.encode()); h.update(p.read_bytes())
    wt = R.parent / f"wt-{LOT}"
    g = subprocess.run(["git", "-C", str(wt), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip() if wt.exists() else "-"
    s = subprocess.run(["git", "-C", str(wt), "status", "--porcelain"], capture_output=True, text=True).stdout if wt.exists() else ""
    return h.hexdigest()[:16], g, hashlib.sha256(s.encode()).hexdigest()[:8]
REEL0 = None

# ───────────────────────── bac à sable ─────────────────────────
STUB = ("import re, sys, os\nr = sys.argv[sys.argv.index('--rapport') + 1]\ns = os.environ.get('G14_STUB_{k}', '95')\n"
        "open(r, 'w', encoding='utf-8').write(f'RESULTAT score={{s}} critiques=0 question=oui\\n\\n# simulé\\n- moyen : exemple\\n')\nprint('RESULTAT score=' + s)\n")
def construire_bac():
    if BAC.exists():
        for p in BAC.rglob("*"):
            try: p.chmod(p.stat().st_mode | stat.S_IWUSR)
            except OSError: pass
        shutil.rmtree(BAC)
    shutil.copytree(R / "harnais", BAC / "harnais", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (BAC / ".cache").mkdir(parents=True); (BAC / ".cache/g_in").symlink_to(R / ".cache/g_in")
    WK.mkdir(parents=True)
    cand = os.environ.get("G14_CANDIDATS")
    if cand:
        for p in Path(cand).rglob("*"):
            if p.is_file() and "__pycache__" not in p.parts:
                d = BAC / p.relative_to(cand); d.parent.mkdir(parents=True, exist_ok=True)
                if d.exists(): d.chmod(0o644)
                shutil.copy2(p, d)
        s = BAC / "harnais/agents/SHA256SUMS"; s.chmod(0o644); lignes = []
        for n in MOTEURS + [f"harnais/agents/{a}.py" for a in SCRIPTS]:
            lignes.append(f"{hashlib.sha256((BAC / n).read_bytes()).hexdigest()}  {n}")
        s.write_text("\n".join(lignes) + "\n")
        for n in ["harnais/agents/SHA256SUMS"] + MOTEURS: (BAC / n).chmod(0o444)
    for k, n in (("MED", "controle_medical.py"), ("LAN", "controle_langue.py")):   # contrôles simulés : le circuit est testé, pas la médecine
        p = BAC / "harnais" / n; p.chmod(0o644); p.write_text(STUB.format(k=k))
    nue = T / "origine.git"; wt = WK / f"wt-{LOT}"; shutil.rmtree(nue, ignore_errors=True)
    g = lambda *a, cwd=None: subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True)
    g("init", "-q", "--bare", str(nue)); g("clone", "-q", str(nue), str(wt)); g("checkout", "-q", "-b", f"prod/lot-{LOT}-final", cwd=wt)
    for k, v in (("user.email", "test@example.invalid"), ("user.name", "autotest"), ("commit.gpgsign", "false")): g("config", k, v, cwd=wt)
    (wt / "LISEZMOI").write_text("bac à sable\n"); g("add", "-A", cwd=wt); g("commit", "-q", "-m", "init", cwd=wt); g("push", "-q", "-u", "origin", f"prod/lot-{LOT}-final", cwd=wt)

def agent(ag, *args, cwd=None, env=None, timeout=120):
    e = dict(ENV, **(env or {}))
    r = subprocess.run([sys.executable, str(BAC / "harnais/grille14/grille_agent.py"), ag, *map(str, args)], cwd=cwd or BAC, env=e, capture_output=True, text=True, timeout=timeout)
    return r.returncode, r.stdout + r.stderr

def kb(ag, *args, env=None):
    r = subprocess.run([sys.executable, str(BAC / "harnais/contracteur/contracteur.py"), ag, *map(str, args)], cwd=BAC, env=dict(ENV, **(env or {})), capture_output=True, text=True, timeout=120)
    return r.returncode, r.stdout + r.stderr

def essais():
    f = WK / "memoire" / f"essais_{LOT}_test.json"
    return json.loads(f.read_text()) if f.exists() else {}

def verrous():
    out = []
    for q in (BAC / ".cache/verrous").glob("*.lock") if (BAC / ".cache/verrous").exists() else []:
        try: out.append((q, json.loads(q.read_text())))
        except (ValueError, OSError): pass
    return out

def remettre(nom, contenu):
    """Fichier de travail propre : marqueurs, blocage, essais, verrous, inventaire et visa effacés."""
    (WK / nom).write_text(contenu, encoding="utf-8")
    for d in ("pret", "bloque", "contracte", "incidents"):
        for p in (WK / d).glob(nom + "*") if (WK / d).exists() else []: p.unlink()
    f = WK / "memoire" / f"essais_{LOT}_test.json"
    if f.exists(): f.write_text(json.dumps({k: v for k, v in json.loads(f.read_text()).items() if not k.endswith(":" + nom)}))
    for p, d in verrous():
        if d.get("fichier", "").endswith("/" + nom): p.unlink()

_G = _C = None
def G():
    global _G
    if _G is None:
        os.environ["G14_TEST"] = "1"; sys.path[:0] = [str(BAC / "harnais/contracteur"), str(BAC / "harnais/grille14"), str(BAC / "harnais")]
        import importlib; _G = importlib.import_module("grille_agent")
    return _G
def C():
    global _C
    if _C is None: G(); import importlib; _C = importlib.import_module("contracteur")
    return _C
def FI(): G(); import forme_interactive; return forme_interactive

def viser(nom):
    """Visa direct (sans spaCy) pour les tests du circuit des auditeurs : fichier réparé + visa à son empreinte."""
    p = WK / nom; h, _ = G().reparer(p.read_text(), LOT, nom); p.write_text(h)
    (WK / "contracte").mkdir(exist_ok=True); (WK / "contracte" / f"{nom}.visa.json").write_text(json.dumps({"sha": hashlib.sha256(h.encode()).hexdigest()[:16]}))

# ───────────────────────── fichier synthétique conforme ─────────────────────────
def tm(t, d): return f'<span class="tm" tabindex="0">{t}<span class="df">{d}</span></span>'
MEDS = [("Nexium®", "ésoméprazole"), ("Pantozol®", "pantoprazole"), ("Agopton®", "lansoprazole"), ("Dafalgan®", "paracétamol"),
        ("Motilium®", "dompéridone"), ("Riopan®", "magaldrate"), ("Gaviscon®", "alginate de sodium")]
def med(nom, dci):
    return (f'<span class="tm med" tabindex="0">{nom}<span class="df"><b>DCI :</b> {dci}. Classe : antisécrétoire. '
            f'Classe : antisécrétoire (ATC A02BC). Groupe : inhibiteurs de la pompe à protons, chefs de file oméprazole et pantoprazole. '
            f'Indications : reflux gastro-œsophagien. Posologie AIPS : 20 mg par jour.</span></span>')
PH = ["Le médecin {v} la sudation axillaire avant de conclure à une cause primaire.", "Le clinicien {v} chaque signe associé avec une méthode simple et reproductible.",
      "Cette étape {v} le diagnostic et évite des examens inutiles chez le patient.", "Le praticien {v} la tolérance du traitement lors de chaque consultation de suivi.",
      "Une anamnèse précise {v} le rythme diurne et le caractère symétrique de la sudation."]
VERBES = ["vérifie", "confirme", "précise", "documente", "contrôle", "recherche"]
SYL = ["ba", "ke", "lo", "mu", "ni", "po", "ra", "si", "tu", "vo"]
def mot(k, i, j):
    h = int(hashlib.sha256(f"{k}-{i}-{j}".encode()).hexdigest(), 16); return "".join("bcdfglmnprstv"[(h >> (8 * n)) % 13] + "aeiou"[(h >> (8 * n + 4)) % 5] for n in range(4))   # mot unique : les phrases de remplissage ne sont pas des redites
def remplissage(n, k=0):
    return "\n".join(f"<p>{PH[(i + k) % 5].format(v=VERBES[(i + k) % 6])[:-1]} pour la {mot(k, i, 1)} et la {mot(k, i, 2)}. Le {tm(f'terme {k}-{i}', f'Ce terme désigne la {mot(k, i, 4)}, notion clinique utile au lit du malade.')} reste un repère pratique pour la {mot(k, i, 3)}.</p>" for i in range(n))
def sec(p, titre, corps, pid="dx1"): return f'<h3 id="{pid}-p{p}"><strong>{p}. {titre}</strong></h3>\n{corps}\n'
def tableau(entete, lignes):
    th = "".join(f"<th>{x}</th>" for x in entete); tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>\n" for l in lignes)
    return f'<div style="overflow-x:auto"><table><tr>{th}</tr>\n{tr}</table></div>'
TITRES = {1: "Définition et sémantique", 2: "Épidémiologie (Suisse, puis Europe)", 3: "Physiopathologie", 4: "Démarche diagnostique", 5: "Anamnèse ciblée et drapeaux rouges",
          6: "Examen physique ciblé, région par région", 7: "Approche syndromique", 8: "Diagnostic positif et critères", 9: "Examens complémentaires", 10: "Arbre décisionnel",
          11: "Prise en charge selon les recommandations suisses", 12: "Prévention", 13: "Points clés", 14: "Pièges et questions fréquentes à l'examen fédéral suisse"}
def conforme(i=1, rempl=24, extra=None):
    ms = [med(n, d) for n, d in MEDS]; P = {}; X = extra or {}
    P[1] = ('<details class="arbre"><summary>Classification</summary><ul><li>Maladies de la peau (CIM-11)<ul><li>Troubles des glandes sudoripares (CIM-11)<ul>'
            '<li><b>Hyperhidrose primaire (CIM-11)</b></li><li>Hyperhidrose secondaire (CIM-11)</li></ul></li></ul></li></ul></details>\n'
            "<p>La classification CIM-11 de l'OMS définit l'hyperhidrose primaire comme une sudation excessive, focale et bilatérale. "
            "Elle se distingue de l'hyperhidrose secondaire, qui révèle une maladie générale.</p>")
    P[2] = ("<p>En Suisse, la prévalence atteint environ 3 % de la population adulte [S1]. L'âge de début précède 25 ans, et le sexe ne modifie pas le risque. "
            "La mortalité reste nulle. Le coût social et la gravité tiennent au retentissement professionnel [S2].</p>" + remplissage(rempl, 2))
    P[3] = ("<p>La cascade moléculaire active la voie cholinergique. L'étape cellulaire augmente la sécrétion eccrine. La réponse tissulaire produit la sudation visible. "
            "La toxine botulique bloque la libération d'acétylcholine, car elle clive une protéine de fusion dans la terminaison nerveuse.</p>"
            + tableau(["Lésion ou perturbation", "Exploration", "Thérapeutique (mécanisme)"], [["Hyperactivité cholinergique", "Test à l'amidon iodé", "Anticholinergique : bloque le récepteur muscarinique"],
                       ["Glande eccrine hyperactive", "Gravimétrie", "Toxine botulique : bloque la libération d'acétylcholine"], ["Dénervation sympathique", "Test sudoral", "Aucun traitement local"]]) + remplissage(rempl, 3))
    P[4] = (f"<p>Le médecin cherche d'abord un drapeau rouge : {tm('sueurs nocturnes', 'Elles évoquent un lymphome ou une tuberculose.')} "
            f"ou {tm('perte de poids', 'Elle oriente vers une cause néoplasique.')}. Chaque étape suit la précédente : 1. anamnèse, 2. examen, 3. bilan ciblé.</p>" + remplissage(rempl, 4))
    P[5] = ("<p>Quand la sudation a-t-elle commencé ? Survient-elle pendant le sommeil ? Le patient prend-il un médicament ? La famille présente-t-elle le même trouble ? "
            "Une fièvre impose une imagerie ou un avis spécialisé en urgence.</p>" + "".join(f"<p>{tm(f'raison {k}', 'Cette raison physiopathologique oriente la décision.')} guide la suite.</p>" for k in range(3)) + remplissage(rempl, 5))
    P[6] = ("<p>L'examen normal précède la recherche du pathologique. Région par région, le médecin examine la peau, le cou, le thorax et l'abdomen.</p>"
            + "".join(f"<p>Le médecin recherche {tm(f'signe {k}', 'Le geste se fait mains posées à plat ; sa valeur reste modérée.')} avec douceur.</p>" for k in range(4)) + remplissage(rempl, 6))
    P[7] = ("<p>7.1 Le syndrome sudoral focal associe des signes fonctionnels et des signes physiques. 7.2 Le syndrome sudoral généralisé évoque une cause secondaire.</p>"
            + "".join(f"<p>Le patient décrit {tm(f'symptôme {k}', 'Ce signe se définit par une sudation visible au repos.')} au quotidien.</p>" for k in range(3)) + remplissage(rempl, 7))
    P[8] = "<p>Les critères de 2004 retiennent une sudation focale visible depuis six mois. Une sudation isolée ne suffit pas au diagnostic.</p>" + remplissage(rempl, 8)
    P[9] = ("<p>9.a Le gold standard reste la gravimétrie. 9.b Le test à l'amidon iodé sert en première intention. 9.c La conductance cutanée constitue une alternative. "
            "9.d Le bilan thyroïdien vient en deuxième intention. La sensibilité du test atteint 90 % selon les séries publiées. Une gravimétrie supérieure à 50 mg/min confirme le diagnostic.</p>"
            + tableau(["Résultat", "Signification", "Conduite"], [["Gravimétrie élevée", "Hyperhidrose confirmée", "Traitement local"]]) + remplissage(rempl, 9))
    P[10] = ("<p>Si une fièvre accompagne la sudation → le médecin cherche une infection. Si la sudation reste focale → le médecin retient une forme primaire. "
             "Si la TSH est basse → le médecin traite une hyperthyroïdie.</p>" + remplissage(rempl, 10))
    P[11] = ("<p>11.A Le traitement vise une réduction de la sudation en quatre semaines. "
             f"11.B En urgence, le médecin traite d'abord la cause grave. Hors urgence, il propose {ms[0]}, {ms[1]}, {ms[2]}, {ms[3]}, {ms[4]}, {ms[5]} et {ms[6]} à 20 mg selon l'AIPS. "
             "11.C La surveillance contrôle la tolérance cutanée chaque mois. 11.D Le pronostic reste bon ; la grossesse impose une prudence particulière chez la patiente.</p>" + remplissage(rempl, 11))
    P[12] = ("<p>La prévention primaire repose sur l'hygiène. La prévention secondaire dépiste les causes générales. La prévention tertiaire limite le retentissement social.</p>" + remplissage(rempl, 12))
    P[13] = ("<p>Une sudation focale et symétrique évoque une forme primaire. Une sudation nocturne impose la recherche d'une cause générale. "
             "Le médecin traite d'abord la cause, puis le symptôme.</p>")
    P[14] = ("<p>Une sudation nocturne suffit-elle à poser le diagnostic primaire ? Réponse : non, elle oriente vers une cause secondaire. "
             "La toxine botulique est-elle un premier choix ? Réponse : non, le traitement local vient avant. "
             "Le test à l'amidon iodé mesure-t-il la quantité ? Réponse : non, il localise la zone.</p>" + remplissage(rempl, 14))
    for p, x in X.items(): P[p] += x
    corps = "".join(sec(p, TITRES[p], P[p], f"dx{i}") for p in range(1, 15))
    return ("<!DOCTYPE html>\n<html lang=\"fr\">\n<head>\n<meta charset=\"utf-8\">\n<title>Hyperhidrose primaire</title>\n<style>p{margin:0}</style>\n</head>\n<body>\n"
            "<p>Abréviations : TSH = thyréostimuline hypophysaire ; AIPS = information professionnelle suisse sur les médicaments ; OMS = Organisation mondiale de la santé ; CIM-11 = Classification internationale des maladies, 11e révision</p>\n"
            f"<main>\n<h2>DX.{i} — Hyperhidrose primaire</h2>\n{corps}"
            "<h2>Sources</h2>\n<ol>\n<li>[S1] Office fédéral de la statistique (OFS). Enquête suisse sur la santé 2022. Neuchâtel : OFS ; 2023.</li>\n"
            "<li>[S2] Office fédéral de la santé publique (OFSP). Rapport 2024. Berne : OFSP ; 2024.</li>\n</ol>\n"
            f"</main>\n</body>\n</html>\n<!-- FIN_FICHIER LOT_{LOT}_PHASE_B_V0_DX.{i} -->\n")

# Version « grasse » : redites et formules creuses ajoutées ; la contraction honnête les retire sans perte.
REDITES = {2: "<p>Il est important de noter que la prévalence atteint environ 3 % de la population adulte en Suisse. Comme indiqué plus haut, l'âge de début précède 25 ans.</p>",
           6: "<p>En effet, le médecin examine la peau, le cou, le thorax et l'abdomen, région par région. Par ailleurs, l'examen normal précède toujours la recherche du pathologique.</p>",
           8: "<p>De plus, les critères de 2004 retiennent une sudation focale visible depuis six mois. Il convient de rappeler qu'une sudation isolée ne suffit pas au diagnostic.</p>",
           12: "<p>En outre, la prévention primaire repose sur l'hygiène, et la prévention secondaire dépiste les causes générales de la sudation excessive.</p>"}
def gras(i=7): return conforme(i, rempl=6, extra={p: x * 6 for p, x in REDITES.items()})
def contracte(h):
    for x in REDITES.values(): h = h.replace(x, "").replace(C().contraction_mecanique(x)[0], "")
    return h

# ───────────────────────── mutations du grille (point attendu, nom, mutation) ─────────────────────────
def sans(motif, rempl=""): return lambda h: re.sub(motif, rempl, h)
def sec_de(h, p): return re.search(rf'<h3 id="dx\d+-p{p}">.*?(?=<h3 id="dx\d+-p{p + 1}"|<h2>Sources)', h, re.S)
def dans_point(p, motif, rempl=""):
    def f(h): m = sec_de(h, p); return h[:m.start()] + re.sub(motif, rempl, m.group(0)) + h[m.end():]
    return f
CASSES = [
    (1, "classification absente", sans(r'<details class="arbre">.*?</details>\n')), (1, "définition trop longue", dans_point(1, r"</p>", " La définition reprend chaque détail clinique utile au lit du malade sans exception." * 14 + "</p>")),
    (1, "source de la définition absente", dans_point(1, r"CIM-11|OMS|classification", "X")), (1, "voisins absents", dans_point(1, r"se distingue", "diffère peu")),
    (2, "Suisse absente", dans_point(2, r"[Ss]uisse", "pays")), (2, "chiffres sans source", dans_point(2, r"\s*\[S\d\]", "")), (2, "mortalité absente", dans_point(2, r"[Mm]ortalité", "issue")),
    (3, "tableau de corrélation absent", dans_point(3, r'(?s)<div style="overflow-x:auto"><table>.*?</table></div>', "")), (3, "cascade absente", dans_point(3, r"moléculaire|cellulaire", "locale")),
    (4, "drapeaux rouges absents", dans_point(4, r"drapeau", "signe")), (4, "point 4 sans mot cliquable", dans_point(4, r'<span class="tm" tabindex="0">([^<]*)<span class="df">[^<]*</span></span>', r"\1")),
    (5, "questions clés absentes", dans_point(5, r"\?", ".")), (6, "pathologique avant le normal", dans_point(6, r"L'examen normal précède la recherche du pathologique\.", "Le pathologique passe avant le normal.")),
    (6, "aucun signe cliquable", dans_point(6, r'<span class="tm" tabindex="0">([^<]*)<span class="df">[^<]*</span></span>', r"\1")), (7, "syndromes non numérotés", dans_point(7, r"7\.2 ", "")),
    (7, "fonctionnel / physique non séparés", dans_point(7, r"fonctionnels", "divers")), (8, "critères sans année", dans_point(8, r"2004", "naguère")),
    (8, "ce qui ne suffit pas absent", dans_point(8, r"ne suffit pas", "aide")), (9, "9.c absent", dans_point(9, r"9\.c ", "")),
    (9, "tableau d'interprétation absent", dans_point(9, r'(?s)<div style="overflow-x:auto"><table>.*?</table></div>', "")), (10, "embranchements absents", dans_point(10, r"→", ",")),
    (11, "11.B absent", dans_point(11, r"11\.B ", "")), (11, "urgence absente", dans_point(11, r"urgence", "pratique")), (12, "prévention tertiaire absente", dans_point(12, r"tertiaire", "finale")),
    (13, "trop de phrases", dans_point(13, r"</p>", " Le médecin revoit le patient. Le médecin note la réponse. Le médecin ajuste la dose. Le médecin informe la famille.</p>")),
    (13, "fenêtre dans les points clés", dans_point(13, r"forme primaire", tm("forme primaire", "Définition brève de la forme."))), (14, "pièges sans réponse", dans_point(14, r"Réponse :", "Donc")),
    (7, "point 7 absent", sans(r'<h3 id="dx1-p7"><strong>7\. ')), (0, "FIN_FICHIER absent", sans(r"<!-- FIN_FICHIER[^>]*-->\n")),
    (0, "ligne > 3000", lambda h: h.replace("</main>", "<p>" + "Le médecin note la sudation du patient. " * 120 + "</p></main>")),
    (0, "mention de conception", dans_point(12, r"</p>", " Ce fichier suit le checkpoint du LOT_001.</p>")),
]

# ───────────────────────── tests ─────────────────────────
TESTS = []
def test(nom):
    def d(fn): TESTS.append((nom, fn)); return fn
    return d

@test("intégrité : 19 scripts d'agents + 3 moteurs en lecture seule (0444)")
def _():
    ko = [n for n in [f"harnais/agents/{a}.py" for a in SCRIPTS] + MOTEURS if (R / n).stat().st_mode & 0o222]
    return not ko, ("inscriptibles : " + ", ".join(ko)) if ko else "22 fichiers en 0444"

@test("intégrité : SHA256SUMS à jour et complet (B1..B5, KB1..KB5, contracteur)")
def _():
    l = {x.split(None, 1)[1].strip(): x.split(None, 1)[0] for x in (R / "harnais/agents/SHA256SUMS").read_text().splitlines() if x.strip()}
    att = set(MOTEURS) | {f"harnais/agents/{a}.py" for a in SCRIPTS}
    manque = sorted(att - set(l)); faux = sorted(n for n, h in l.items() if hashlib.sha256((R / n).read_bytes()).hexdigest() != h)
    return not manque and not faux, f"manquants {manque} · faux {faux}" if manque or faux else f"{len(l)} empreintes justes"

@test("intégrité : chaque script appelle son moteur avec son identité ; `etat` répond pour les 14 agents réels")
def _():
    ko = []
    for a in SCRIPTS:
        t = (R / f"harnais/agents/{a}.py").read_text()
        if (f'sys.argv.insert(1, "{a}")' if not a.startswith("K") else f'"{a}"') not in t: ko.append(a)
    for a in SCRIPTS[:14]:
        r = subprocess.run([sys.executable, str(R / f"harnais/agents/{a}.py"), "etat"], capture_output=True, text=True, cwd=R, timeout=60, env=ENV)
        if r.returncode or f'"agent": "{a}"' not in r.stdout: ko.append(f"{a}:{r.returncode}")
    return not ko, f"échecs {ko}" if ko else "19 scripts cohérents · 14 `etat`"

@test("intégrité : altération de gen.py ou du contracteur détectée (bac)")
def _():
    out = []
    for n, cmd in (("harnais/grille14/gen.py", lambda: agent("R1", "etat")), ("harnais/contracteur/contracteur.py", lambda: kb("KB3", "etat", nomf(7)))):
        p = BAC / n; t = p.read_bytes(); p.chmod(0o644); p.write_bytes(t + b"\n# altere\n")
        try: rc, o = cmd()
        finally: p.write_bytes(t); p.chmod(0o444)
        out.append((rc, "ALTÉRATION" in o))
    return out == [(3, True), (3, True)], str(out)

@test("roster : N = 10 à 16, ≤ 2 DD par rédacteur, ≤ 4 par auditeur, B1 = Phase A + 2 DD, chaque auditeur a son KB")
def _():
    sys.path.insert(0, str(BAC / "harnais/grille14")); import roster
    ko = []; scripts = {p.stem for p in (R / "harnais/agents").glob("*.py")}
    for n in range(10, 17):
        r = roster.build("999", n); dd = [f"LOT_999_Phase_B_V0_DX.{i}.html" for i in range(1, n + 1)]; red, aud = r["redacteurs"], r["auditeurs"]
        if any(len(v) > 2 for v in red.values()) or len(red) > 8: ko.append(f"N={n} rédacteurs")
        if sorted(sum(red.values(), [])) != sorted(dd): ko.append(f"N={n} DD rédigés ≠ 1..N")
        if aud["B1"] != [r["A"], dd[0], dd[1]]: ko.append(f"N={n} B1")
        if any(len(v) > 4 for b, v in aud.items() if b != "B1") or any(not v for v in aud.values()): ko.append(f"N={n} auditeurs")
        if sorted(x for v in aud.values() for x in v if x != r["A"]) != sorted(dd): ko.append(f"N={n} DD audités ≠ 1..N")
        if (set(red) | set(aud) | {"K" + b for b in aud}) - scripts: ko.append(f"N={n} sans script")
    r = json.loads((R / "harnais/grille14/roster_001.json").read_text())
    if roster.build("001", r["n"]) != r: ko.append("roster_001.json dérivé à la main")
    return not ko, "; ".join(ko) or "7 tailles conformes · roster_001 = build(001, 15)"

@test("grille : fichier synthétique conforme → aucun écart critique ni grave")
def _():
    E, st = G().ecarts_points(conforme(), set(range(1, 15)))
    E = [e for e in E if e[1] in ("CRITIQUE", "GRAVE")]
    return not E, "; ".join(f"[{p}] {g} {m[:60]}" for p, g, m in E) or f"0 écart bloquant · {st['mots']} mots"

for _p, _nom, _mut in CASSES:
    def _f(p=_p, mut=_mut):
        h = mut(conforme())
        if h == conforme(): return False, "mutation sans effet (test mal écrit)"
        E, _ = G().ecarts_points(h, set(range(1, 15)))
        bons = [e for e in E if e[0] == p and e[1] in ("CRITIQUE", "GRAVE", "MOYEN")]; autres = [e for e in E if e[0] not in (0, p) and e[1] != "DETAIL"]
        return bool(bons) and not autres, (f"{bons[0][1]} {bons[0][2][:60]}" if bons else "NON signalé") + (f" · autres : {[(e[0], e[2][:30]) for e in autres]}" if autres else "")
    TESTS.append((f"grille : variante cassée point {_p} ({_nom})", _f))

@test("taille (Vial 27.10) : hors bande = MOYEN dans la grille, jamais CRITIQUE ; bande lue dans BANDE.json")
def _():
    petit = conforme(rempl=2); E, _ = G().ecarts_points(petit, set(range(1, 15))); t = [e for e in E if "taille finale" in e[2]]
    B = json.loads((BAC / "harnais/BANDE.json").read_text())
    return bool(t) and all(e[1] == "MOYEN" for e in t) and f"{B['min_ko']}–{B['max_ko']}" in t[0][2] and (B["min_ko"], B["max_ko"]) == (80, 200), t[0][2][:90] if t else "taille non signalée"

@test("taille : controle_lot.py lit BANDE.json ; hors bande = avertissement de lot, lot CONFORME")
def _():
    d = WK / "lot_taille" / f"LOT_{LOT}"; shutil.rmtree(d.parent, ignore_errors=True); d.mkdir(parents=True)
    (d / nomf(1)).write_text(conforme(1, rempl=2)); (d / f"LOT_{LOT}_Phase_A_V0.html").write_text(conforme(1, rempl=2).replace("DX.1 —", "Phase A —"))
    sys.path.insert(0, str(BAC / "harnais")); import importlib.util
    sp = importlib.util.spec_from_file_location("cl_t", BAC / "harnais/controle_lot.py"); cl = importlib.util.module_from_spec(sp); argv = sys.argv; sys.argv = ["x"]; sp.loader.exec_module(cl); sys.argv = argv
    rap = cl.verifier(d, False); taille_c = [c for c in rap["critiques_lot"] if "bande" in c]; taille_a = [c for c in rap["avertissements_lot"] if "80–200" in c]
    return cl.BANDE_MIN == 80_000 and not taille_c and len(taille_a) == 2, f"critiques taille {taille_c} · avertissements {taille_a[:1]}"

@test("taille : checkpoint.py réel (contrôles simulés) → fichier de 40 Ko accepté avec AVERTISSEMENT")
def _():
    nom = nomf(8); remettre(nom, conforme(8, rempl=2))
    r = subprocess.run([sys.executable, str(BAC / "harnais/checkpoint.py"), LOT, str(WK / nom), "--cycle", "7", "--sans-commit"], capture_output=True, text=True, cwd=BAC, env=ENV, timeout=120)
    return r.returncode == 0 and "AVERTISSEMENT" in r.stdout and "hors bande 80–200" in r.stdout, f"code {r.returncode} · {r.stdout.strip()[:140]}"

@test("réparation : FIN_FICHIER, ligne > 3000, title=, [Sn] dupliqués ; idempotente")
def _():
    nom = nomf(1); h = re.sub(r"<!-- FIN_FICHIER[^>]*-->\n", "", conforme()).replace("[S1]", "[S1] [S1]", 1).replace("<p>La cascade", '<p title="infobulle">La cascade', 1)
    h = h.replace("</main>", "<p>" + "Le médecin note la sudation du patient. " * 250 + "</p></main>")
    remettre(nom, h); rc, out = agent("R1", "controle", nom); t = (WK / nom).read_text(); t2, rep2 = G().reparer(t, LOT, nom)
    ok = "RÉPARÉ" in out and "FIN_FICHIER" in t[-200:] and max(map(len, t.splitlines())) <= 3000 and "title=" not in t.replace("<title>", "") and "[S1] [S1]" not in t and t2 == t and not rep2
    return ok, out.splitlines()[0][:120]

@test("réparation : idempotente sur 3 vraies copies de LOT_001 (sinon le visa ne tiendrait jamais)")
def _():
    ko = []
    for i in (1, 7, 12):
        h = (R / f".cache/travail/LOT_{LOT}" / nomf(i)).read_text(encoding="utf-8"); a, _ = G().reparer(h, LOT, nomf(i)); b, rb = G().reparer(a, LOT, nomf(i))
        if a != b: ko.append(f"DX.{i} {rb}")
    return not ko, str(ko) if ko else "3/3 stables"

@test("controle : conforme → code 0, verrou posé ; auditeur : copie d'entrée de l'audit posée")
def _():
    nom = nomf(1); remettre(nom, conforme()); rc, out = agent("R1", "controle", nom); vs = [d for _, d in verrous()]
    rc2, _ = agent("R1", "fin", nom); ent0 = (WK / "contracte" / f"{nom}.entree.html").exists()
    rc3, _ = agent("B1", "controle", nom); ent = (WK / "contracte" / f"{nom}.entree.html").exists()
    return rc == 0 and any(v["agent"] == "R1" and v["fichier"].endswith(nom) for v in vs) and rc2 == 0 and not ent0 and rc3 == 0 and ent, f"codes {rc},{rc2},{rc3} · entrée {ent0}→{ent}"

@test("fin rédacteur : CHECKPOINT OK (--sans-commit), marqueur prêt, verrou levé, essais effacés")
def _():
    nom = nomf(2); remettre(nom, conforme(2)); agent("R1", "controle", nom); rc, out = agent("R1", "fin", nom); vs = [d for _, d in verrous()]
    ok = rc == 0 and "CHECKPOINT OK" in out and (WK / "pret" / nom).exists() and not any(v["fichier"].endswith(nom) for v in vs) and f"R1:{nom}" not in essais()
    return ok, out.strip().splitlines()[-1][:110]

@test("attendre : prêt → immédiat (0) ; absent → ATTENTE (4) ; BLOQUÉ → arrêt immédiat (5)")
def _():
    t0 = time.time(); rc1, _ = agent("B1", "attendre", nomf(2)); d1 = time.time() - t0
    remettre(nomf(3), conforme(3)); rc2, _ = agent("B2", "attendre", nomf(3))
    (WK / "bloque").mkdir(exist_ok=True); (WK / "bloque" / (nomf(3) + ".md")).write_text("# BLOQUÉ\n"); t0 = time.time(); rc3, o3 = agent("B2", "attendre", nomf(3)); d3 = time.time() - t0
    remettre(nomf(3), conforme(3))
    return (rc1, rc2, rc3) == (0, 4, 5) and d1 < 3 and d3 < 3, f"codes {rc1},{rc2},{rc3}"

@test("hors périmètre : R1 sur DX.5 → STOP code 3 ; LOT inconnu → message, code 2")
def _():
    rc, out = agent("R1", "controle", nomf(5)); rc2, o2 = agent("R1", "etat", "--lot", "777")
    return rc == 3 and "HORS PÉRIMÈTRE" in out and rc2 == 2 and "LOT inconnu" in o2 and "Traceback" not in o2, f"codes {rc},{rc2}"

@test("verrou : tenu par R1 → controle ET fin de B1 refusés (3), détenteur nommé, fichier intact, aucun essai")
def _():
    nom = nomf(2); remettre(nom, conforme(2)); agent("R1", "controle", nom); avant = (WK / nom).read_text()
    rc1, o1 = agent("B1", "controle", nom); rc2, o2 = agent("B1", "fin", nom, "--v1", "95", "--v2", "95")
    ok = rc1 == 3 and rc2 == 3 and "VERROU PRIS PAR R1" in o1 and "VERROU PRIS PAR R1" in o2 and (WK / nom).read_text() == avant and f"B1:{nom}" not in essais()
    return ok, f"codes {rc1},{rc2} · {o1.strip()[:60]}"

@test("verrou : orphelin (> 20 min, fichier inchangé) repris ; récent refusé ; illisible repris après 60 s")
def _():
    nom = nomf(2); p = WK / nom; lk = [q for q, d in verrous() if d.get("fichier", "").endswith(nom)][0]
    d = json.loads(lk.read_text()); d["t"] -= 1500; lk.write_text(json.dumps(d))
    rc1, _ = agent("B1", "controle", nom)                         # fichier modifié il y a peu : pas orphelin
    os.utime(p, (time.time() - 1500, time.time() - 1500)); rc2, _ = agent("B1", "controle", nom)
    d2 = json.loads(lk.read_text()) if lk.exists() else {}
    lk.write_text(""); os.utime(lk, (time.time() - 120, time.time() - 120)); rc3, o3 = agent("R1", "controle", nom)
    return rc1 == 3 and rc2 in (0, 1) and d2.get("agent") == "B1" and rc3 in (0, 1) and "Traceback" not in o3, f"codes {rc1},{rc2},{rc3} · détenteur {d2.get('agent')}"

@test("verrou : 10 agents réclament le même fichier en parallèle → un seul gagnant")
def _():
    f_ = str((WK / "course.html").resolve()); (WK / "course.html").write_text("x")
    for q, d in verrous():
        if "course.html" in d.get("fichier", ""): q.unlink()
    un = lambda i: subprocess.run([sys.executable, str(BAC / "harnais/verrou.py"), "claim", f_, f"X{i}"], capture_output=True, text=True, cwd=BAC).returncode
    with ThreadPoolExecutor(10) as ex: codes = list(ex.map(un, range(10)))
    return codes.count(0) == 1 and codes.count(3) == 9, f"codes {sorted(codes)}"

@test("chemins : nom nu, relatif, absolu, autre répertoire → même fichier, même verrou")
def _():
    nom = nomf(4); remettre(nom, conforme(4))
    rcs = [agent("R2", "controle", x, cwd=c)[0] for x, c in ((nom, BAC), (f".cache/test_g14/{nom}", BAC), (str(WK / nom), "/"), (nom, "/tmp"))]
    n = sum(1 for q, d in verrous() if d.get("fichier", "").endswith(nom))
    return rcs == [0, 0, 0, 0] and n == 1, f"codes {rcs} · verrous {n}"

@test("arguments : fichier absent, --v1 illisible, --points faux, --lot sans valeur, commande inconnue → message clair, jamais de trace")
def _():
    remettre(nomf(4), conforme(4)); (WK / nomf(3)).unlink(missing_ok=True)
    cas = [agent("R2", "controle", nomf(3)), agent("B2", "fin", nomf(4), "--v1", "abc", "--v2", "95"), agent("R2", "controle", nomf(4), "--points", "x"),
           agent("R2", "controle", nomf(4), "--lot"), agent("R2", "lancer", nomf(4)), agent("R2", "controle")]
    mauvais = [(rc, o.strip()[:50]) for rc, o in cas if "Traceback" in o or rc == 0]
    return not mauvais, f"{len(cas)} cas, codes {[c for c, _ in cas]}" if not mauvais else str(mauvais)

def casse(n=1):
    h = conforme(4)
    for f_ in [sans(r'<details class="arbre">.*?</details>\n'), dans_point(9, r"9\.c ", ""), dans_point(10, r"→", ",")][:n]: h = f_(h)
    return h

@test("plafond : 3 essais au plus (écarts différents) → BLOQUÉ au 3e")
def _():
    nom = nomf(4); remettre(nom, casse(3)); r = []
    for k in (3, 2, 1): (WK / nom).write_text(casse(k)); r.append(agent("R2", "fin", nom))
    return [x[0] for x in r] == [1, 1, 5] and (WK / "bloque" / (nom + ".md")).exists() and essais().get(f"R2:{nom}", {}).get("n") == 3, f"codes {[x[0] for x in r]}"

@test("BLOQUÉ : coupe controle et fin (code 5), le fichier n'est plus touché")
def _():
    nom = nomf(4); avant = (WK / nom).read_text(); rc1, _ = agent("R2", "controle", nom); rc2, _ = agent("R2", "fin", nom); rc3, _ = agent("B2", "controle", nom)
    return (rc1, rc2, rc3) == (5, 5, 5) and (WK / nom).read_text() == avant, f"codes {rc1},{rc2},{rc3}"

@test("stagnation : mêmes écarts au 2e essai (fichier retouché sans effet) → BLOQUÉ ; pas de faux positif quand ils diminuent")
def _():
    nom = nomf(4); remettre(nom, casse(2)); r1 = agent("R2", "fin", nom)
    (WK / nom).write_text(casse(2).replace("<p>La prévention primaire", "<p>Ainsi, la prévention primaire")); r2 = agent("R2", "fin", nom)
    remettre(nom, casse(3)); r3 = agent("R2", "fin", nom); (WK / nom).write_text(casse(2)); r4 = agent("R2", "fin", nom)
    return (r1[0], r2[0], r3[0], r4[0]) == (1, 5, 1, 1) and "aucun progrès" in r2[1], f"codes {r1[0]},{r2[0]},{r3[0]},{r4[0]}"

@test("INCHANGÉ : relance sans modification → refus sans essai ; 2e relance sans modification → BLOQUÉ")
def _():
    nom = nomf(4); remettre(nom, casse(3)); agent("R2", "fin", nom); n1 = essais()[f"R2:{nom}"]["n"]
    rc2, o2 = agent("R2", "fin", nom); n2 = essais()[f"R2:{nom}"]["n"]; rc3, o3 = agent("R2", "fin", nom)
    vs = [d for _, d in verrous() if d.get("fichier", "").endswith(nom)]
    return n1 == n2 == 1 and rc2 == 1 and "INCHANGÉ" in o2 and rc3 == 5 and "sans modification" in o3 and not vs, f"n {n1}→{n2} · codes {rc2},{rc3} · verrous {len(vs)}"

@test("auditeur : `fin` sans visa → REFUSÉ (aucun visa), sans essai ; visa périmé → REFUSÉ (modifié après le visa)")
def _():
    nom = nomf(1); remettre(nom, conforme()); rc1, o1 = agent("B1", "fin", nom, "--v1", "95", "--v2", "95")
    viser(nom); p = WK / nom; p.write_text(p.read_text().replace("La prévention primaire", "La prévention  primaire", 1)); rc2, o2 = agent("B1", "fin", nom, "--v1", "95", "--v2", "95")
    return rc1 == 1 and "aucun visa" in o1 and rc2 == 1 and "modifié après le visa" in o2 and "KB1.py" in o2 and f"B1:{nom}" not in essais(), f"codes {rc1},{rc2}"

@test("auditeur : scores absents → refus sans essai, verrou levé")
def _():
    nom = nomf(1); remettre(nom, conforme()); viser(nom); rc, o = agent("B1", "fin", nom)
    vs = [d for _, d in verrous() if d.get("fichier", "").endswith(nom)]
    return rc == 1 and "saisis tes scores" in o and f"B1:{nom}" not in essais() and not vs, f"code {rc}"

def retouche(nom, k):
    p = WK / nom; p.write_text(re.sub(r"<p>(?:Ainsi, )*[Ll]a prévention primaire", "<p>" + "Ainsi, " * k + "la prévention primaire", p.read_text(), count=1)); viser(nom)

@test("auditeur : V1 < 90 refusé ; score qui monte sans faux blocage ; 3e refus → BLOQUÉ ; aucune fiche AUD")
def _():
    nom = nomf(1); remettre(nom, conforme()); r = []
    for k, v in enumerate(("85", "88", "89")):
        if k: retouche(nom, k)
        else: viser(nom)
        r.append(agent("B1", "fin", nom, "--v1", v, "--v2", "95"))
    aud = (WK / "audits" / f"AUD_B1_{nom}.md").exists()
    return [x[0] for x in r] == [1, 1, 5] and "V1=85" in r[0][1] and not aud, f"codes {[x[0] for x in r]}"

@test("auditeur : V2 < 90 identique deux fois (fichier retouché) → stagnation BLOQUÉ ; nouveaux scores sans modification → INCHANGÉ")
def _():
    nom = nomf(2); remettre(nom, conforme(2)); viser(nom); r1 = agent("B1", "fin", nom, "--v1", "95", "--v2", "80"); retouche(nom, 1); r2 = agent("B1", "fin", nom, "--v1", "95", "--v2", "80")
    remettre(nom, conforme(2)); viser(nom); r3 = agent("B1", "fin", nom, "--v1", "95", "--v2", "80"); r4 = agent("B1", "fin", nom, "--v1", "95", "--v2", "92")
    return (r1[0], r2[0], r3[0], r4[0]) == (1, 5, 1, 1) and "aucun progrès" in r2[1] and "INCHANGÉ" in r4[1], f"codes {r1[0]},{r2[0]},{r3[0]},{r4[0]}"

@test("auditeur : visa valide + V1/V2 ≥ 90 → CHECKPOINT OK, --sans-commit forcé en test (aucun commit), fiche AUD écrite")
def _():
    nom = nomf(3); remettre(nom, conforme(3)); viser(nom); wt = WK / f"wt-{LOT}"
    n0 = subprocess.run(["git", "rev-list", "--count", "HEAD"], cwd=wt, capture_output=True, text=True).stdout.strip()
    rc, o = agent("B2", "fin", nom, "--v1", "94", "--v2", "93")
    n1 = subprocess.run(["git", "rev-list", "--count", "HEAD"], cwd=wt, capture_output=True, text=True).stdout.strip()
    ok = rc == 0 and "commit réservé" in o and n0 == n1 and (WK / "audits" / f"AUD_B2_{nom}.md").exists()
    return ok, f"code {rc} · commits {n0}→{n1} · {o.strip().splitlines()[-1][:80]}"

@test("panne d'outil : checkpoint qui plante → code 6, aucun essai, verrou levé, incident écrit")
def _():
    nom = nomf(4); remettre(nom, conforme(4)); cp = BAC / "harnais/checkpoint.py"; sauve = cp.read_text(); cp.write_text("raise RuntimeError('panne simulée')\n")
    try: rc, o = agent("R2", "fin", nom)
    finally: cp.write_text(sauve)
    vs = [d for _, d in verrous() if d.get("fichier", "").endswith(nom)]
    return rc == 6 and not essais().get(f"R2:{nom}") and not vs and (WK / "incidents" / f"{nom}.md").exists(), f"code {rc}"

@test("panne d'outil : contrôle médical sans rapport → checkpoint ERREUR (outil), code 2, pas REFUSÉ")
def _():
    nom = nomf(4); remettre(nom, conforme(4)); cm = BAC / "harnais/controle_medical.py"; sauve = cm.read_text(); cm.write_text("raise SystemExit('panne simulée')\n")
    try: r = subprocess.run([sys.executable, str(BAC / "harnais/checkpoint.py"), LOT, str(WK / nom), "--cycle", "7", "--sans-commit"], capture_output=True, text=True, cwd=BAC, env=ENV, timeout=120)
    finally: cm.write_text(sauve)
    return r.returncode == 2 and "ERREUR (outil)" in r.stdout, f"code {r.returncode}"

@test("plantage interne : fichier illisible (UTF-16) → message clair, jamais de trace brute")
def _():
    nom = nomf(2); remettre(nom, conforme(2)); (WK / nom).write_bytes(b"\xff\xfe" + conforme(2).encode("utf-16")); rc, o = agent("R1", "controle", nom); remettre(nom, conforme(2))
    return "Traceback" not in o and rc in (0, 1, 6), f"code {rc} · {o.strip()[:70]}"

@test("registre des essais : 12 écritures concurrentes → aucune perte, JSON valide")
def _():
    code = ("import os, sys; os.environ['G14_TEST']='1'; sys.path[:0] = [%r, %r]; import grille_agent as G\nfrom pathlib import Path\n"
            "G.refus('R%%s' %% sys.argv[1], '777', Path(%r), 'f%%s.html' %% sys.argv[1], 'sig', 'd', 'sha')") % (str(BAC / "harnais"), str(BAC / "harnais/grille14"), str(WK))
    f_ = WK / "memoire/essais_777_test.json"; f_.unlink(missing_ok=True)
    un = lambda i: subprocess.run([sys.executable, "-c", code, str(i)], capture_output=True, text=True, cwd=BAC).returncode
    with ThreadPoolExecutor(12) as ex: codes = list(ex.map(un, range(12)))
    d = json.loads(f_.read_text()); return len(d) == 12 and not any(codes), f"{len(d)}/12 clés · codes {set(codes)}"

@test("isolation : en test, mémoire et preuve du bracelet restent dans .cache/test_g14")
def _():
    rc, _ = agent("R1", "memoire")
    mem = [p.name for p in (BAC / ".cache/memoire").glob("*")] if (BAC / ".cache/memoire").exists() else []
    preuve = (BAC / "harnais/PREUVE_EMBOITEMENT.txt").read_text() == (R / "harnais/PREUVE_EMBOITEMENT.txt").read_text()
    return rc == 0 and not mem and preuve and (WK / "PREUVE_EMBOITEMENT_test.txt").exists() and (WK / "memoire/R1.json").exists(), f"code {rc} · mémoire réelle {mem} · preuve intacte {preuve}"

# ───────────────────────── CONTRACTEUR ─────────────────────────
def kbc(ag, cmd, nom, *x, pct=None, mots=None):
    """Appel en processus (spaCy chargé une fois) ; renvoie (code, sortie)."""
    if pct is not None: os.environ["G14_CIBLE_PCT"] = str(pct)
    else: os.environ.pop("G14_CIBLE_PCT", None)
    if mots is not None: os.environ["G14_CIBLE_MOTS"] = str(mots)
    else: os.environ.pop("G14_CIBLE_MOTS", None)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): rc = C().principal(ag, [cmd, nom, *x])
    return rc, buf.getvalue()

ETAT = {}
def base_contracteur():
    """DX.7 (territoire B3) : version grasse → inventaire → contraction honnête → visa. Mémorise le taux atteint."""
    nom = nomf(7); remettre(nom, gras(7)); agent("B3", "controle", nom)
    rc0, o0 = kbc("KB3", "contracter", nom); p = WK / nom; p.write_text(contracte(p.read_text())); h = p.read_text()
    snap = json.loads((WK / "contracte" / f"{nom}.snap.json").read_text())["inv"]; red = 100 * (1 - len(C().texte(h).split()) / snap["mots"])
    ETAT.update(nom=nom, propre=h, red=red, o0=o0, rc0=rc0)
    return nom, h, red

@test("contracteur (ii) : vraie contraction (redites et formules creuses retirées, sans perte) → VISA POSÉ")
def _():
    nom, h, red = base_contracteur(); rc, o = kbc("KB3", "verifier", nom, pct=max(1, red - 2), mots=100)
    v = WK / "contracte" / f"{nom}.visa.json"
    regle = all("RÈGLE ABSOLUE" in "\n".join(x.splitlines()[:3]) for x in (ETAT["o0"], o))
    return ETAT["rc0"] == 0 and "INVENTAIRE pris" in ETAT["o0"] and regle and rc == 0 and "VISA POSÉ" in o and v.exists(), f"−{red:.1f} % · règle en tête {regle} · code {rc} · " + (o.strip().splitlines()[-1][:60] if rc == 0 else next((l[:150] for l in o.splitlines() if l.startswith(" - ")), ""))

@test("contracteur (iii) : excès non résolu (redites laissées) → REFUSÉ, visa retiré ; aucun quota de volume")
def _():
    nom = ETAT["nom"]; (WK / nom).write_text(gras(7)); rc, o = kbc("KB3", "verifier", nom); (WK / nom).write_text(ETAT["propre"])
    return rc == 1 and "redites quasi identiques" in o and not (WK / "contracte" / f"{nom}.visa.json").exists() and "volume insuffisant" not in o, f"code {rc}"

@test("contracteur : aucune réduction mais aucun excès → VISA (le volume ne force aucune coupe) ; reformulation plus concise → VISA")
def _():
    nom = nomf(13); remettre(nom, conforme(13)); agent("B5", "controle", nom); kbc("KB5", "contracter", nom); rc1, o1 = kbc("KB5", "verifier", nom)
    p = WK / nom; p.write_text(p.read_text().replace("La sensibilité du test atteint 90 % selon les séries publiées.", "Selon les séries publiées, le test a une sensibilité de 90 %."))
    rc2, o2 = kbc("KB5", "verifier", nom)
    return rc1 == 0 and rc2 == 0, f"codes {rc1},{rc2} · " + next((l[:140] for l in (o1 + o2).splitlines() if l.startswith(" - ")), "")

def perte(mut, attendu, nom_test, exc=None):
    def f():
        nom = ETAT["nom"]; h = mut(ETAT["propre"])
        if h == ETAT["propre"]: return False, "mutation sans effet (test mal écrit)"
        (WK / nom).write_text(h); rc, o = kbc("KB3", "verifier", nom, *(["--exceptions", exc] if exc else []), pct=max(1, ETAT["red"] - 6), mots=100)
        (WK / nom).write_text(ETAT["propre"])
        ok = rc == 1 and "REFUSÉ" in o and all(re.search(a, o) for a in attendu)
        lig = [l for l in o.splitlines() if l.startswith(" - ")]
        return ok, f"code {rc} · " + (lig[0][:110] if lig else o.strip()[-110:])
    TESTS.append((f"contracteur (i) : {nom_test} → REFUSÉ en nommant la notion", f))
perte(lambda h: h.replace("Les critères de 2004 retiennent", "Les critères retiennent").replace("critères de 2004", "critères"), [r"nombres perdus.*2004"], "nombre supprimé (2004)")
perte(lambda h: h.replace(" à 20 mg selon", " à 20 selon"), [r"SENS altéré.*perd « 20 mg »"], "unité retirée de sa phrase (20 mg)")
perte(lambda h: re.sub(r', <span class="tm med" tabindex="0">Riopan®<span class="df">.*?</span></span>', "", h), [r"médicaments perdus.*riopan", r"fenêtres supprimées"], "médicament ® supprimé (Riopan®)")
perte(lambda h: h.replace("DCI :</b> magaldrate.", "DCI :</b> antiacide."), [r"médicaments perdus.*magaldrate"], "DCI retirée de la fenêtre .tm med")
perte(lambda h: h.replace(tm("sueurs nocturnes", "Elles évoquent un lymphome ou une tuberculose."), "sueurs nocturnes"), [r"termes cliquables perdus.*sueurs nocturnes"], "terme cliquable déshabillé")
perte(lambda h: h.replace("Elles évoquent un lymphome ou une tuberculose.", "Voir."), [r"fenêtres vidées.*sueurs nocturnes"], "fenêtre vidée")
perte(lambda h: h.replace(" [S2]", ""), [r"renvois \[Sn\] perdus.*S2"], "renvoi [S2] supprimé")
perte(lambda h: re.sub(r"<li>\[S2\].*?</li>\n", "", h), [r"sources de la liste perdus.*S2"], "source [S2] retirée de la liste")
perte(lambda h: h.replace('<tr><td>Dénervation sympathique</td><td>Test sudoral</td><td>Aucun traitement local</td></tr>\n', ""), [r"tableaux amputés.*tableau 1 : 4 → 3"], "ligne de tableau supprimée")
perte(lambda h: re.sub(r'<h3 id="dx7-p12">.*?(?=<h3 id="dx7-p13">)', "", h, flags=re.S), [r"points disparus.*12"], "point 12 entier supprimé")
perte(lambda h: h.replace(" ; OMS = Organisation mondiale de la santé", ""), [r"abréviations définies perdus.*OMS"], "abréviation retirée de la ligne Abréviations")
perte(lambda h: h.replace("Le médecin cherche d'abord un drapeau rouge : ", "Drapeaux rouges : ").replace("Une sudation focale et symétrique évoque une forme primaire.", "Sudation focale et symétrique : forme primaire."),
      [r"phrases sans verbe en plus", r"point 13 :.*aucune admise", r"nv:[0-9a-f]{6}"], "phrase verbale réduite en liste nominale")
perte(lambda h: h.replace(", car elle clive une protéine de fusion dans la terminaison nerveuse", ""), [r"EXPLICATIONS perdues.*ph:[0-9a-f]{6}"], "phrase d'explication amputée (car …)")
perte(lambda h: h.replace(" L'étape cellulaire augmente la sécrétion eccrine.", ""), [r"EXPLICATIONS perdues.*sécrétion eccrine"], "mécanisme supprimé")
perte(lambda h: h.replace("ne suffit pas au diagnostic", "suffit au diagnostic"), [r"SENS altéré.*ne… pas"], "négation retirée (ne … pas)")
perte(lambda h: h.replace("Si la sudation reste focale →", "La sudation reste focale →"), [r"SENS altéré.*« si »"], "condition retirée (si)")
perte(lambda h: h.replace("Une gravimétrie supérieure à 50 mg/min confirme", "Une gravimétrie élevée confirme"), [r"seuils \(comparateur \+ valeur \+ unité\) perdus.*> 50 mg/min"], "seuil retiré (> 50 mg/min)")
perte(lambda h: h.replace(" La réponse tissulaire produit la sudation visible.", ""), [r"phrases supprimées ou fortement réduites.*réponse tissulaire"], "phrase supprimée sans être une redite")
perte(lambda h: h.replace("Abréviations : TSH = thyréostimuline hypophysaire ; ", "Abréviations : "), [r"forme : sigles sans définition survolable.*TSH"], "sigle laissé sans définition")
perte(lambda h: h.replace("le médecin traite d'abord la cause grave.", "le médecin traite d'abord la cause grave par Zorglubine®."), [r"forme : médicaments mentionnés sans fenêtre.*Zorglubine"], "médicament mentionné sans fenêtre")
perte(lambda h: "".join(x for x in re.split(r"(<p>Le (?:médecin|clinicien|praticien) [^<]*<span)", h) if not x.startswith("<p>Le praticien")), [r"phrases supprimées ou fortement réduites|notions \(noms\) perdues"], "début de paragraphes supprimé (phrases, lemmes)")

@test("contracteur : --exceptions : sans --motif refusé ; motivée acceptée et consignée ; plus de 10 → REFUSÉ ; sans objet signalée")
def _():
    nom = ETAT["nom"]; h = ETAT["propre"].replace("Les critères de 2004 retiennent", "Les critères retiennent")
    (WK / nom).write_text(h); rc0, o0 = kbc("KB3", "verifier", nom, "--exceptions", "2004")
    rc1, o1 = kbc("KB3", "verifier", nom, "--exceptions", "2004,zorglub", "--motif", "date des critères corrigée après lecture de la source")
    v = json.loads((WK / "contracte" / f"{nom}.visa.json").read_text()) if rc1 == 0 else {}
    rc2, o2 = kbc("KB3", "verifier", nom, "--exceptions", ",".join(f"x{i}" for i in range(11)), "--motif", "test du plafond des exceptions")
    (WK / nom).write_text(ETAT["propre"])
    return rc0 == 1 and "motivée" in o0 and rc1 == 0 and v.get("exceptions") == ["2004"] and v.get("motif", "").startswith("date") and "sans objet" in o1 and "zorglub" in o1 and rc2 == 1, f"codes {rc0},{rc1},{rc2} · visa {v.get('exceptions')}"

@test("contracteur : garde-fou d'entrée → tableau retiré AVANT `contracter` (pendant l'audit) → REFUSÉ")
def _():
    nom = nomf(8); remettre(nom, gras(8)); agent("B3", "controle", nom)
    p = WK / nom; p.write_text(re.sub(r'<tr><td>Dénervation sympathique</td>.*?</tr>\n', "", p.read_text()))
    kbc("KB3", "contracter", nom); p.write_text(contracte(p.read_text())); rc, o = kbc("KB3", "verifier", nom, pct=1, mots=100)
    return rc == 1 and "depuis ta prise en main" in o and "tableaux amputés" in o, f"code {rc} · " + next((l[:100] for l in o.splitlines() if "prise en main" in l), "")

@test("contracteur (iv) : visa invalidé par toute modification ; `fin` B3 refusé puis accepté avec visa (sans commit)")
def _():
    nom = ETAT["nom"]; (WK / nom).write_text(ETAT["propre"]); rc0, _ = kbc("KB3", "verifier", nom, pct=max(1, ETAT["red"] - 2), mots=100)
    e1 = json.loads(kbc("KB3", "etat", nom)[1])["visa_valide"]; p = WK / nom; h = p.read_text(); p.write_text(h.replace("</main>", " </main>"))
    e2 = json.loads(kbc("KB3", "etat", nom)[1])["visa_valide"]; rc1, o1 = agent("B3", "fin", nom, "--v1", "95", "--v2", "95")
    p.write_text(h); wt = WK / f"wt-{LOT}"; n0 = subprocess.run(["git", "rev-list", "--count", "HEAD"], cwd=wt, capture_output=True, text=True).stdout
    rc2, o2 = agent("B3", "fin", nom, "--v1", "95", "--v2", "95"); n1 = subprocess.run(["git", "rev-list", "--count", "HEAD"], cwd=wt, capture_output=True, text=True).stdout
    return rc0 == 0 and e1 and not e2 and rc1 == 1 and "modifié après le visa" in o1 and rc2 == 0 and "commit réservé" in o2 and n0 == n1, f"codes {rc0},{rc1},{rc2} · visa {e1}→{e2}"

@test("contracteur : verrou tenu par un autre agent → contracter refusé (3) ; inventaire repris si le rédacteur remet une nouvelle version")
def _():
    nom = nomf(9); remettre(nom, conforme(9)); agent("R5", "controle", nom); rc1, o1 = kbc("KB3", "contracter", nom)
    agent("R5", "fin", nom); rc2, o2 = kbc("KB3", "contracter", nom); time.sleep(0.05); (WK / "pret" / nom).write_text("x")
    agent("B3", "fin", nom, "--v1", "95", "--v2", "95"); rc3, o3 = kbc("KB3", "verifier", nom, pct=0, mots=100)
    return rc1 == 3 and "VERROU PRIS PAR R5" in o1 and rc2 == 0 and "nouvelle version" in o3, f"codes {rc1},{rc2},{rc3}"

@test("contracteur (vi) : chaque KBi réel refuse un fichier hors territoire (code 3) ; arguments faux sans trace")
def _():
    ko = []
    for i in range(1, 6):
        autre = nomf(15) if i != 5 else nomf(1)
        r = subprocess.run([sys.executable, str(R / f"harnais/agents/KB{i}.py"), "verifier", autre], capture_output=True, text=True, cwd=R, env=ENV, timeout=60)
        if r.returncode != 3 or "HORS TERRITOIRE" not in r.stdout: ko.append(f"KB{i}:{r.returncode}")
    cas = [kb("KB3", "verifier", nomf(7), "--exceptions"), kb("KB3", "contracter", nomf(7), "--lot"), kb("KB3", "verifier", "LOT_001_Phase_B_V0_DX.99.html"), kb("KB3"), kb("KB3", "zorglub", nomf(7))]
    mauvais = [(c, o[:40]) for c, o in cas if "Traceback" in o or c == 0]
    return not ko and not mauvais, f"{ko} {mauvais}" if ko or mauvais else "5/5 clones · 5 cas d'arguments"

@test("contracteur : `etat` des clones réels KB3 sur une copie (lecture seule) et B3 etat répondent")
def _():
    d = T / "copies"; d.mkdir(exist_ok=True); shutil.copy2(R / f".cache/travail/LOT_{LOT}" / nomf(7), d / nomf(7))
    r = subprocess.run([sys.executable, str(R / "harnais/agents/KB3.py"), "etat", str(d / nomf(7))], capture_output=True, text=True, cwd=R, env=ENV, timeout=60)
    r2 = subprocess.run([sys.executable, str(R / "harnais/agents/B3.py"), "etat"], capture_output=True, text=True, cwd=R, env=ENV, timeout=60)
    return r.returncode == 0 and '"mots_actuels"' in r.stdout and r2.returncode == 0, f"codes {r.returncode},{r2.returncode} · {r.stdout[:60]!r}"

PHRASES = [("<p>En effet, le médecin examine la peau.</p>", "<p>Le médecin examine la peau.</p>"),
           ("<p>Il est, en effet, rare.</p>", "<p>Il est, en effet, rare.</p>"),
           ("<p>La dose baisse. Par ailleurs, l'âge compte : oui ; non ? Si !</p>", "<p>La dose baisse. L'âge compte : oui ; non ? Si !</p>"),
           ('<p>Il faut savoir que <span class="tm" tabindex="0">la TSH<span class="df">En effet, une hormone.</span></span> baisse.</p>', '<p>Il faut savoir que <span class="tm" tabindex="0">la TSH<span class="df">Une hormone.</span></span> baisse.</p>'),
           ("<h3>En effet, titre</h3><summary>De plus, résumé</summary><a href='#x'>En outre, lien</a>", "<h3>En effet, titre</h3><summary>De plus, résumé</summary><a href='#x'>En outre, lien</a>"),
           ("<script>var a='En effet, x afin de y';</script><style>p:after{content:'afin de'}</style>", "<script>var a='En effet, x afin de y';</script><style>p:after{content:'afin de'}</style>"),
           ('<p class="En effet, " data-x="afin de">Le test sert afin de trier.</p>', '<p class="En effet, " data-x="afin de">Le test sert pour trier.</p>'),
           ("<p>Le patient n'est en mesure de marcher. Il est en mesure de marcher.</p>", "<p>Le patient n'est en mesure de marcher. Il peut marcher.</p>"),
           ("<p>Étant donné que la TSH baisse, on traite.</p>", "<p>Puisque la TSH baisse, on traite.</p>"),
           ("<p>On agit de manière à ce que la dose baisse.</p>", "<p>On agit de manière à ce que la dose baisse.</p>"),
           ("<p>Notons que la dose baisse vite chez le sujet âgé. Notons que la dose baisse vite chez le sujet âgé.</p>", "<p>La dose baisse vite chez le sujet âgé.</p>"),
           ("<p>La dose baisse vite chez le sujet âgé. La dose baisse vite chez le sujet âgé.</p>", "<p>La dose baisse vite chez le sujet âgé.</p>"),
           ("<p>De plus, <b>la dose</b> baisse.</p>", "<p>De plus, <b>la dose</b> baisse.</p>"),
           ("<p>Il s'agit d'une urgence : 5 mg ; voir [S1] !</p>", "<p>C'est une urgence : 5 mg ; voir [S1] !</p>"),
           ("<!-- En effet, commentaire --><p>texte afin de voir</p>", "<!-- En effet, commentaire --><p>texte pour voir</p>")]

@test("contracteur (v) : contraction mécanique sur 15 phrases synthétiques (balises, script/style, typographie, majuscule, grammaire)")
def _():
    ko = [(a[:40], C().contraction_mecanique(a)[0]) for a, b in PHRASES if C().contraction_mecanique(a)[0] != b]
    return not ko, str(ko[:2]) if ko else f"{len(PHRASES)}/{len(PHRASES)}"

@test("contracteur (v) : contraction mécanique sur 3 vraies copies : balises intactes, idempotente, aucune notion perdue, aucun verbe retiré")
def _():
    ko = []; n = 0
    for i in (1, 3, 12):
        h = (R / f".cache/travail/LOT_{LOT}" / nomf(i)).read_text(encoding="utf-8"); a, k = C().contraction_mecanique(h); b, k2 = C().contraction_mecanique(a); n += k
        if re.findall(r"<[^>]+>", h) != re.findall(r"<[^>]+>", a): ko.append(f"DX.{i} balises")
        if a != b: ko.append(f"DX.{i} non idempotente")
        if re.findall(r"\s[:;?!]", C().texte(h)).__len__() != re.findall(r"\s[:;?!]", C().texte(a)).__len__(): ko.append(f"DX.{i} typographie")
        i0 = C().inventaire(h); i1 = C().inv_complet(a); pb, _, _ = C().comparer(i0, i1, set(), "")
        if pb: ko.append(f"DX.{i} pertes {pb}")
        if len(i1["nominales"]) > len(i0["nominales"]): ko.append(f"DX.{i} verbe retiré")
        cv = C().couverture(i0["phrases"], i1["phrases"]); mal = [p["t"][:50] for p, (c, mk) in zip(i0["phrases"], cv) if c < (0.85 if p["e"] else 0.8) or not set(p["m"]) <= mk]
        if mal: ko.append(f"DX.{i} phrases non couvertes {mal[:2]}")
    return not ko, str(ko) if ko else f"3 fichiers · {n} contraction(s) · 0 perte"

@test("contracteur (viii) : détecteur de médicaments (marques multi-mots, ™, DCI composées) et normalisation des termes")
def _():
    h = ("<main><p>L'AIPS Deroxat® et Co-Dafalgan® ; Dafalgan Odis® ; VEOZA™ 45 mg.</p>"
         '<p><span class="tm med" tabindex="0">Femoston®<span class="df"><b>DCI :</b> estradiol et dydrogestérone.</span></span> '
         '<span class="tm" tabindex="0">Bouffée  de chaleur :<span class="df">Accès de chaleur.</span></span> '
         '<span class="tm" tabindex="0">bouffée de chaleur:<span class="df">Accès.</span></span> 1&nbsp;000 patients, 0,40 mg et 2 jours.</p></main>')
    i = C().inventaire(h)
    att = {"deroxat", "co-dafalgan", "odis", "veoza", "femoston", "estradiol", "dydrogestérone"}
    ok = att <= set(i["meds"]) and "aips deroxat" not in i["meds"] and i["termes"] == ["bouffée de chaleur:"] and "1000" in i["nombres"] and "000" not in i["nombres"] and "0.4 mg" in i["unites"] and "2 j" in i["unites"]
    return ok, f"médicaments {sorted(i['meds'])} · termes {i['termes']} · unités {i['unites']}"

@test("contracteur (viii) : phrases sans verbe : verbes conjugués mal lus par spaCy reconnus, vraies listes nominales signalées")
def _():
    nlp = C().nlp()
    verb = ["La périménopause dure 2 à 4 ans avant la ménopause.", "Les lymphomes T et NK forment 9 familles.", "Le médecin palpe une adénopathie ferme.",
            "Les accès nocturnes fragmentent le sommeil.", "Un ganglion dure-t-il plus de 2 semaines ?", "Si la TSH est basse → traiter."]
    nom = ["Deuxième effet : athérosclérose et maladies cardiovasculaires.", "Signes fonctionnels : chaleur, dyspnée, sueurs.", "Fièvre, frissons, hypotension, urticaire, dyspnée.",
           "Hormones libres élevées et TSH effondrée."]
    fp = [x for x in verb if not C().verbale(nlp(x))]; fn = [x for x in nom if C().verbale(nlp(x))]
    return not fp and not fn, f"faux nominaux {fp} · faux verbaux {fn}" if fp or fn else f"{len(verb)} verbales, {len(nom)} nominales : 0 erreur"

@test("contracteur (viii) : inventaire < 15 s pour 20 000 mots (spaCy)")
def _():
    h = (R / f".cache/travail/LOT_{LOT}" / nomf(3)).read_text(encoding="utf-8"); m = C().FIN_COURS.search(h).start(); h = h[:m] + h[h.index("<h3"):m] + h[m:]
    t0 = time.time(); i = C().inventaire(h); dt = time.time() - t0
    return dt < 15 and i["mots"] >= 20000, f"{i['mots']} mots en {dt:.1f} s"

@test("abréviations (forme_interactive) : liste détruite à l'affichage, sigles habillés hors titres et fenêtres, idempotent, ligne gardée dans le brut")
def _():
    raw = conforme(1).replace("Les critères de 2004", "Les critères OMS de 2004").replace("<h3 id=\"dx1-p13\"><strong>13. Points clés", "<h3 id=\"dx1-p13\"><strong>13. Points clés TSH")
    raw = raw.replace("Elles évoquent un lymphome", "Elles évoquent une TSH basse ou un lymphome")
    c = FI().convert(raw); cc = FI().convert(c)
    habille = re.findall(r'<span class="tm" tabindex="0" data-auto="1">(TSH|OMS)<span class="df"><b>\1</b> : ', c)
    titres = re.findall(r"<h[1-6][^>]*>.*?</h[1-6]>", c, re.S); dans_titre = any("<b>TSH</b> :" in t for t in titres)
    dans_fen = bool(re.search(r'<span class="df">[^<]*<span class="tm" tabindex="0">TSH', c))
    brut_ok = "Abréviations : TSH" in G().reparer(C().contraction_mecanique(raw)[0], LOT, nomf(1))[0]
    ok = "Abréviations :" not in c and len(habille) >= 2 and not dans_titre and not dans_fen and cc == c and brut_ok
    return ok, f"habillés {len(habille)} · titre {dans_titre} · fenêtre {dans_fen} · idempotent {cc == c} · brut {brut_ok}"

@test("forme (Vial 27.10) : CHAQUE occurrence d'un sigle défini et d'un médicament à fenêtre est habillée (hors titres), y compris au point 13 sans écart Q13")
def _():
    raw = conforme(1).replace("Le médecin traite d'abord la cause, puis le symptôme.", "Le médecin traite d'abord la cause, puis le symptôme par Nexium si la TSH est normale.")
    raw = raw.replace("Si la TSH est basse", "Si la TSH reste basse malgré une TSH de contrôle")
    c = FI().convert(raw); lib = FI().texte_libre(c)
    nus = re.findall(r"\bTSH\b|\bNexium\b", lib); auto = len(re.findall(r'data-auto="1">(?:TSH|Nexium)', c))
    E, _ = G().ecarts_points(raw, set(range(1, 15))); q13 = [e for e in E if e[0] == 13]
    return not nus and auto >= 4 and not FI().manques_forme(c) and not q13, f"nus {nus} · habillés {auto} · manques {FI().manques_forme(c)[:1]} · Q13 {q13[:1]}"

@test("forme (Vial 27.10) : sigle non défini, médicament sans fenêtre, fenêtre incomplète → CRITIQUE au contrôle de forme (grille)")
def _():
    raw = conforme(1).replace("La mortalité reste nulle.", "La mortalité reste nulle selon le registre SWISSREG. Le Zorglub® et la zorglutide sont à l'étude.")
    raw = raw.replace("Indications : reflux gastro-œsophagien. Posologie AIPS : 20 mg par jour.", "", 1)
    E, _ = G().ecarts_points(raw, set(range(1, 15))); cr = " ".join(m for p, g, m in E if g == "CRITIQUE")
    ok = "SWISSREG" in cr and "Zorglub" in cr and "zorglutide" in cr and "Nexium® (manque : indications, posologie AIPS)" in cr
    return ok, cr[:200]

@test("abréviations : l'habillage des sigles ne fait perdre aucun sigle ni terme à l'inventaire du contracteur")
def _():
    raw = conforme(1); i0 = C().inv_complet(raw); i1 = C().inv_complet(FI().convert(raw)); arbre = {"classification"}   # le résumé de l'arbre devient une carte (voulu)
    perdus = {k: sorted(set(i0[k]) - set(i1[k]) - arbre) for k in ("sigles", "termes")}
    return not any(perdus.values()), f"perdus {perdus}" if any(perdus.values()) else f"{len(i0['sigles'])} sigles, {len(i0['termes'])} termes conservés"

@test("SANTE.py : une ligne par rubrique, sans trace")
def _():
    r = subprocess.run([sys.executable, str(BAC / "harnais/grille14/SANTE.py"), "--lot", LOT], capture_output=True, text=True, cwd=BAC, env=ENV, timeout=60)
    ok = r.returncode in (0, 1) and "Traceback" not in r.stdout + r.stderr and all(k in r.stdout for k in ("verrous", "bloqués", "prêts non audités", "essais", "commits", "empreintes"))
    return ok, f"code {r.returncode} · {len(r.stdout.splitlines())} lignes"

@test("isolation finale : LOT_001, .cache/memoire et ../wt-001 inchangés (empreintes avant/après)")
def _():
    apres = empreinte_reel(); return apres == REEL0, f"avant {REEL0} · après {apres}"

# ───────────────────────── exécution ─────────────────────────
def main():
    global REEL0
    t0 = time.time(); REEL0 = empreinte_reel(); construire_bac()
    for nom, fn in TESTS:
        if FILTRE and FILTRE not in nom and not nom.startswith("isolation finale"): continue
        t = time.time()
        try: ok, det = fn()
        except Exception as ex: ok, det = False, f"EXCEPTION {type(ex).__name__} : {str(ex)[:150]}"
        RESULTATS.append((ok, nom, det, time.time() - t))
        print(f"{'OK' if ok else 'KO'}  {nom}  ·  {det}  ({time.time() - t:.1f} s)", flush=True)
    n = sum(1 for r in RESULTATS if r[0])
    print(f"\n{'═' * 80}\nAUTOTEST grille14 + contracteur : {n}/{len(RESULTATS)} OK · {time.time() - t0:.0f} s" + ("" if n == len(RESULTATS) else f" · {len(RESULTATS) - n} KO"))
    for ok, nom, det, _ in RESULTATS:
        if not ok: print(f"  KO  {nom} : {det}")
    return 0 if n == len(RESULTATS) else 1

if __name__ == "__main__":
    sys.exit(main())
