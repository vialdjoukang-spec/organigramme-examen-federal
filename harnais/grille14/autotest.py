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
    for p in (BAC / ".cache/verrous").glob("*.lock") if (BAC / ".cache/verrous").exists() else []:
        try:
            if json.loads(p.read_text() or "{}").get("fichier", "").endswith("/" + nom): p.unlink()
        except Exception: p.unlink()

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
