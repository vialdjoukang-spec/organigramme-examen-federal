#!/usr/bin/env python3
"""Moteur des scripts « Grille des 14 points » (lecture seule). Un script par agent : harnais/agents/<id>.py.
  <id>.py memoire                       départ de tâche : identité, périmètre, grille, règles, leçons ; preuve du bracelet
  <id>.py controle <fichier> [--points 1,4]   écarts du fichier à la grille, point par point ; verrou posé
  <id>.py fin <fichier> [--v1 N --v2 N --crit N]   dernier contrôle + checkpoint ; verrou levé ; verdict. 3 essais au plus ; mêmes écarts deux fois = fichier BLOQUÉ (l'agent s'arrête)
  controle et fin réparent d'abord, gratuitement : balise de fin, lignes trop longues, title=, renvois dupliqués
  <id>.py lecon "<texte>"               ajoute une leçon à la mémoire permanente (5 au plus)
  <id>.py attendre <fichier>            auditeur : bloque jusqu'à 9 min tant que le rédacteur n'a pas terminé le fichier
  <id>.py etat                          mémoire et périmètre
Rédacteur (A, R1..R8) : fin = grille + checkpoint, sans commit. Auditeur (B1..B5) : fin = V1 (fond) et V2 (conformité) saisies, puis checkpoint avec commit.
V1 = exactitude du fond ; V2 = conformité au Prompt ULTIME et à la grille des points."""
import hashlib, json, re, subprocess, sys, time
from pathlib import Path
R = Path(__file__).resolve().parent.parent.parent
G = Path(__file__).resolve().parent
sys.path.insert(0, str(R / "harnais")); sys.path.insert(0, str(G))
MEM = R / ".cache/memoire"; MEM.mkdir(parents=True, exist_ok=True)

def verifier_integrite():
    sums = {}
    f = R / "harnais/agents/SHA256SUMS"
    if f.exists():
        for l in f.read_text().splitlines():
            h, n = l.split(None, 1); sums[n.strip()] = h
    for n in ("harnais/grille14/grille_agent.py", "harnais/grille14/gen.py"):
        p = R / n
        if n in sums and hashlib.sha256(p.read_bytes()).hexdigest() != sums[n]:
            print(f"ALTÉRATION DÉTECTÉE : {n} ne correspond plus à son empreinte. STOP."); sys.exit(3)

def charge_roster(lot):
    return json.loads((G / f"roster_{lot}.json").read_text())

def perimetre(ag, ro):
    if ag == "A": return [ro["A"]]
    if ag.startswith("R"): return ro["redacteurs"].get(ag, [])
    return ro["auditeurs"].get(ag, [])

def role(ag):
    if ag == "A": return ("Rédacteur Phase A", "Sonnet 5.5, effort moyen", "Écrit la Phase A : monographie du SSP en 14 points, liste des DD classée, tableau comparatif, algorithme.")
    if ag.startswith("R"): return ("Rédacteur Phase B", "Sonnet 5.5, effort moyen", "Écrit 2 diagnostics différentiels au plus, un fichier par DD, 14 points. Il n'écrit que du texte.")
    return ("Auditeur-correcteur de territoire", "Opus 5.5, effort moyen", "Audite le fond (V1) et la conformité à la grille et au Prompt (V2), puis corrige directement dans son territoire.")

def memoire_perm(ag):
    f = MEM / f"{ag}.json"
    return json.loads(f.read_text()) if f.exists() else {"agent": ag, "lecons": [], "taches": 0}

def sauve_mem(ag, m): (MEM / f"{ag}.json").write_text(json.dumps(m, ensure_ascii=False, indent=1))

def sections(html):
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", "", html)
    marques = list(re.finditer(r"<h3[^>]*>\s*(?:<strong>)?\s*(\d{1,2})\.\s", t))
    out = {}
    for i, m in enumerate(marques):
        fin = marques[i + 1].start() if i + 1 < len(marques) else len(t)
        out.setdefault(int(m.group(1)), t[m.start():fin])
    return out

def txt(h, sans_fenetres=True):
    if sans_fenetres: h = re.sub(r"(?s)<span class=\"(?:df|dxc)\">.*?</span></span>", " ", h)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()

def ecarts_points(html, pts):
    import forme_interactive as FI
    conv = FI.convert(html); S = sections(conv); E = []
    add = lambda p, g, m: E.append((p, g, m))
    for p in range(1, 15):
        if p not in pts: continue
        s = S.get(p)
        if s is None: add(p, "CRITIQUE", "point absent : titre « %d. … » en <strong> dans un <h3>" % p); continue
        t = txt(s); tl = t.lower(); nsup = len(re.findall(r'<sup class="r">', s)); ntm = len(re.findall(r'class="tm"', s))
        if p == 1:
            corps = re.sub(r"(?s)<div class=\"arb\">.*?</div>(?=\s*<(?:p|div|table|h))", " ", s, count=1)
            w = len(txt(corps).split())
            if w > 140: add(1, "CRITIQUE", f"point 1 trop long : {w} mots (≤ 140) : définis en peu de mots ; le détail va dans une fenêtre")
            if 'class="arb"' not in s: add(1, "CRITIQUE", "classification absente : situe l'entité du général au particulier, avec la classification d'origine entre parenthèses")
            if not re.search(r"cim|dsm|oms|atc|société|classification|profiles", tl): add(1, "GRAVE", "Q1.1 : nomme la source de la définition (société savante ou classification) et son année")
            if not re.search(r"voisin|se distingue|à ne pas confondre|exclu|différe", tl): add(1, "GRAVE", "Q1.3 : distingue l'entité de ses notions voisines")
        elif p == 2:
            if "suisse" not in tl: add(2, "GRAVE", "Q2.1 : chiffres suisses d'abord (OFS, OFSP, Obsan, registres)")
            if not re.search(r"\d[\d ,.]*\s?(%|pour 100|/ ?100)", t): add(2, "GRAVE", "Q2.1 : prévalence ou incidence chiffrée")
            if nsup == 0: add(2, "CRITIQUE", "Q2.4 : chiffres sans source : [Sn] en exposant ou « non quantifié »")
            for mot, q in (("âge", "âge"), ("sexe", "sexe"), ("mortalité|létalité|décès", "mortalité")):
                if not re.search(mot, tl): add(2, "MOYEN", f"Q2.1 : {q} absent")
            if not re.search(r"coût|santé publique|dépistage|gravité|enjeu", tl): add(2, "MOYEN", "Q2.3 : enjeux (santé publique, coût, dépistage, gravité)")
        elif p == 3:
            if sum(bool(re.search(x, tl)) for x in ("moléculaire", "cellulaire", "tissulaire")) < 2: add(3, "GRAVE", "Q3.1 : cascade moléculaire → cellulaire → tissulaire → clinique, étape par étape")
            if not (re.search(r"<table", s) and re.search(r"lésion|perturbation", tl) and re.search(r"exploration", tl) and re.search(r"thérap", tl)): add(3, "CRITIQUE", "Q3.4 : tableau de corrélation lésion/perturbation → exploration → thérapeutique (mécanisme)")
        elif p == 4:
            nd = len(re.findall(r"drapeau|🚩", s, re.I))
            if nd == 0: add(4, "CRITIQUE", "Q4.1 : cite les drapeaux rouges")
            elif ntm < 2: add(4, "GRAVE", "Q4.1 : chaque drapeau rouge est cliquable avec sa fenêtre (pourquoi il est rouge)")
            if not re.search(r"étape|1\)|1\.", tl): add(4, "GRAVE", "étapes graduelles jusqu'au diagnostic, en l'absence d'urgence")
        elif p == 5:
            if t.count("?") < 4: add(5, "GRAVE", "Q5.1 : questions clés, chacune avec sa raison physiopathologique")
            if len(re.findall(r"urgence|imagerie|avis|adresser|hospitalis", tl)) < 2: add(5, "GRAVE", "Q5.2 : drapeaux rouges actionnables (urgence, imagerie, avis)")
            if ntm < 3: add(5, "MOYEN", "mots cliquables des raisons physiopathologiques")
        elif p == 6:
            if len(re.findall(r"région|inspection|palpation|auscultation|peau|thorax|abdomen|cou\b|cardi|pulmon", tl)) < 3: add(6, "GRAVE", "examen région par région, progression topographique ou systémique")
            i, j = tl.find("normal"), tl.find("patholog")
            if i < 0 or (0 <= j < i): add(6, "GRAVE", "Q6.1 : le normal avant le pathologique")
            if ntm < 4: add(6, "GRAVE", "Q6.2 : chaque signe cliquable (technique du geste, valeur diagnostique, piège)")
        elif p == 7:
            if not (re.search(r"7\.1", t) and re.search(r"7\.2", t)): add(7, "CRITIQUE", "Q7.1 : syndromes numérotés 7.1, 7.2…")
            if not (re.search(r"fonctionnel", tl) and re.search(r"physique", tl)): add(7, "GRAVE", "Q7.2 : signes fonctionnels et signes physiques séparés")
            if ntm < 3: add(7, "GRAVE", "Q7.3 : chaque signe défini (fenêtre)")
        elif p == 8:
            if not re.search(r"(19|20)\d\d", t): add(8, "CRITIQUE", "Q8.1 : critères de la société savante avec l'année")
            if not re.search(r"ne suffi|insuffisant", tl): add(8, "GRAVE", "Q8.2 : ce qui ne suffit pas au diagnostic")
        elif p == 9:
            for x in "abcd":
                if not re.search(r"9\.%s" % x, t): add(9, "CRITIQUE", f"structure 9.{x} absente (gold standard, 1re intention, alternatives, 2e intention)")
            if not re.search(r"<table", s): add(9, "GRAVE", "Q9.4 : tableau d'interprétation résultat → signification → conduite")
        elif p == 10:
            if t.count("→") < 3: add(10, "CRITIQUE", "Q10.1 : embranchements « si X → Y », chaque nœud renvoie à un signe, un examen ou une action")
        elif p == 11:
            for x in "ABCD":
                if not re.search(r"11\.%s" % x, t): add(11, "CRITIQUE", f"11.{x} absent")
            if "aips" not in tl and not re.search(r"\bmg\b", tl): add(11, "CRITIQUE", "Q11.5 : spécialités suisses ® et doses lues dans l'AIPS")
            if not re.search(r"urgence", tl): add(11, "MOYEN", "Q11.3 : urgence d'abord, conduite chronologique")
        elif p == 12:
            for x in ("primaire", "secondaire", "tertiaire"):
                if x not in tl: add(12, "GRAVE", f"Q12.1 : prévention {x} absente")
        elif p == 13:
            ph = [x for x in re.split(r"(?<=[.!?])\s+", re.sub(r"^\d+\.\s*[^.]*?(?=[A-ZÉÈ])", "", t)) if len(x.split()) > 2]
            if not 3 <= len(ph) <= 6: add(13, "GRAVE", f"Q13.1 : 3 à 6 phrases courtes et verbales (trouvé {len(ph)})")
            if re.search(r'class="(tm|dx)', s): add(13, "GRAVE", "Q13.1 : aucune fenêtre dans les points clés (la phrase reste intacte)")
        elif p == 14:
            if t.count("?") < 3 or len(re.findall(r"réponse", tl)) < 3: add(14, "GRAVE", "Q14.1 : chaque piège = question d'examen + bonne réponse immédiate")
    crit, moy, st = FI.controle(conv)
    if 0 in pts or len(pts) == 14:
        if "FIN_FICHIER" not in html[-400:]: add(0, "CRITIQUE", "balise <!-- FIN_FICHIER LOT_XXX_<PARTIE> --> absente en fin de fichier (troncature présumée)")
        nl = sum(1 for l in html.splitlines() if len(l) > 3000)
        if nl: add(0, "CRITIQUE", f"{nl} ligne(s) de plus de 3 000 caractères : coupe-les (un saut de ligne entre deux blocs)")
        tc = len(conv.encode("utf-8"))
        if not 100_000 <= tc <= 195_000: add(0, "CRITIQUE", f"taille finale {tc // 1000} Ko hors bande 100–195 Ko (ce que le checkpoint mesure après conversion et onglet) : {'allège la forme, pas le fond' if tc > 195_000 else 'densifie sans remplissage'}")
    pl = phrases_longues(conv)
    if any("phrases trop longues" in c for c in crit) and pl:
        add(0, "DETAIL", "phrases à couper en premier : " + " | ".join(f"{n} mots : « {x[:70]}… »" for n, x in pl))
    if any("taille finale" in c for c in [m for _, _, m in E]):
        add(0, "DETAIL", "points les plus lourds : " + ", ".join(f"point {p} = {b // 1000} Ko" for b, p in poids_points(conv)) + " : allège-les d'abord (tableaux, fenêtres, doublons)")
    for c in crit: add(0, "CRITIQUE", "forme : " + c)
    for c in moy: add(0, "MOYEN", "forme : " + c)
    return E, st


TEST = bool(__import__("os").environ.get("G14_TEST"))
CAP = 3          # essais de `fin` au plus par agent et par fichier
def reparer(html, lot, nom):
    """Réparations mécaniques gratuites : l'agent ne dépense aucun jeton dessus."""
    rep = []
    n0 = len(html)
    h = re.sub(r"(\[S\d+\])(?:\s*\1)+", r"\1", html)
    if h != html: rep.append("renvois [Sn] dupliqués fusionnés")
    html = h
    h = re.sub(r"(<(?!title)[a-zA-Z][^>]*?)\s+title=(\"[^\"]*\"|'[^']*')", r"\1", html)
    if h != html: rep.append("attributs title= retirés")
    html = h
    out, n = [], 0
    for l in html.split("\n"):
        k = 0
        while len(l) > 3000 and k < 400:
            cut = -1
            for m in re.finditer(r"</(?:p|li|tr|td|th|div|details|summary|table|ul|ol|h[1-6]|section|span)>", l):
                if m.end() > 2800: break
                cut = m.end()
            if cut < 600:
                cut = l.rfind(">", 600, 2900) + 1
                if cut <= 0: cut = l.rfind(" ", 600, 2900) + 1
                if cut <= 0: cut = 2900
            out.append(l[:cut]); l = l[cut:]; k += 1; n += 1
        out.append(l)
    if n: rep.append(f"{n} saut(s) de ligne ajouté(s) dans les lignes de plus de 3 000 caractères")
    html = "\n".join(out)
    part = nom.replace(f"LOT_{lot}_", "").replace(".html", "").upper()
    if "FIN_FICHIER" not in html[-400:]:
        html = re.sub(r"\s*<!--\s*FIN_FICHIER[^>]*-->", "", html).rstrip() + f"\n<!-- FIN_FICHIER LOT_{lot}_{part} -->\n"; rep.append("balise FIN_FICHIER remise en fin de fichier")
    h = re.sub(r"[ \t]+\n", "\n", html)
    html = h
    return html, rep

def essais_f(lot): return MEM / f"essais_{lot}{'_test' if TEST else ''}.json"
def charge_essais(lot): f = essais_f(lot); return json.loads(f.read_text()) if f.exists() else {}
def bloque_f(wk, nom): return wk / "bloque" / (nom + ".md")

def refus(ag, lot, wk, nom, sig, detail):
    """Compte un échec. Bloque le fichier au 3e essai, ou à la 2e fois que les mêmes écarts reviennent."""
    d = charge_essais(lot); k = f"{ag}:{nom}"; e = d.get(k, {"n": 0, "sig": None, "stag": 0})
    e["n"] += 1; h = hashlib.sha256(sig.encode()).hexdigest()[:12]
    e["stag"] = e["stag"] + 1 if e["sig"] == h else 0; e["sig"] = h; d[k] = e; essais_f(lot).write_text(json.dumps(d, indent=1))
    if e["n"] >= CAP or e["stag"] >= 1:
        raison = "mêmes écarts qu'à l'essai précédent (aucun progrès)" if e["stag"] >= 1 else f"{CAP} essais utilisés"
        b = bloque_f(wk, nom); b.parent.mkdir(exist_ok=True)
        b.write_text(f"# BLOQUÉ · {nom}\nagent : {ag}\nraison : {raison}\nessais : {e['n']}\n\n## Derniers écarts\n{detail}\n", encoding="utf-8")
        return f"BLOQUÉ ({raison}). Arrête-toi : ne relance ni controle ni fin sur ce fichier, ne tente rien d'autre ; réponds « BLOQUÉ {nom} ». Le chef de production reprend la main."
    return f"Essai {e['n']}/{CAP}." + (" ATTENTION : si les mêmes écarts reviennent au prochain essai, le fichier sera bloqué : change de méthode." if e["n"] >= 1 else "")

def reussite(ag, lot, nom):
    d = charge_essais(lot); d.pop(f"{ag}:{nom}", None); essais_f(lot).write_text(json.dumps(d, indent=1))

def phrases_longues(html, n=3):
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>|<table.*?</table>|<details class=\"refs\".*?</details>", " ", html)
    t = re.sub(r"(?s)<span class=\"(?:df|dxc)\">.*?</span></span>", " ", t)
    t = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t))
    ph = [(len(x.split()), x.strip()) for x in re.split(r"(?<=[.!?;])\s+", t) if len(x.split()) > 24]
    return sorted(ph, reverse=True)[:n]

def poids_points(conv):
    S = sections(conv); return sorted(((len(v.encode()), p) for p, v in S.items()), reverse=True)[:3]

def verrou(ag, f, action):
    a = ["python3", str(R / "harnais/verrou.py"), action, str(f)] + [ag]
    return subprocess.run(a, capture_output=True, text=True, cwd=R)

def main():
    verifier_integrite()
    ag = sys.argv[1]; cmd = sys.argv[2] if len(sys.argv) > 2 else "memoire"; a = sys.argv[3:]
    lot = "001"
    for i, x in enumerate(a):
        if x == "--lot": lot = a[i + 1]
    ro = charge_roster(lot); per = perimetre(ag, ro); nom, mod, mission = role(ag); m = memoire_perm(ag)
    wk = R / ".cache/travail" / f"LOT_{lot}"
    if TEST: wk = R / ".cache/test_g14"; wk.mkdir(parents=True, exist_ok=True)
    if cmd == "memoire":
        print(f"# {ag} · {nom} · {mod}\n{mission}\nPérimètre (rien d'autre) : " + ", ".join(per))
        if ag == "B1": print("B1 audite d'abord la Phase A (liste des DD) : sans délai, car les rédacteurs en dépendent ; puis ses 2 DD.")
        print("\nV1 = exactitude du fond (doses AIPS, chiffres retrouvés, références existantes, rien d'inventé).\nV2 = conformité au Prompt ULTIME et à la grille des 14 points (chaque question notée 2/1/0, seuil 90 %).\nUn fichier est validé à V1 ≥ 90, V2 ≥ 90 et zéro critique.\n")
        print((R / "harnais/GRILLE_14_POINTS.md").read_text(encoding="utf-8").split("## Style des cours")[0])
        print("## Règles du cours (extrait du gabarit)\n- Le texte est le cours, pour des médecins résidents : aucune mention de la conception, aucune date de rédaction, aucune genèse des sources.\n- Phrases de 8 à 20 mots, une idée, aucune nuance qui complique. Concis, dense, exhaustif.\n- Sources : [Sn] collés en exposant, rares ; liste unique « Sources » en fin de fichier.\n- Médicaments : fenêtre complète (DCI, classe, groupe avec chefs de file, indications, posologies AIPS).\n- Mots cliquables sobres, jamais dans un titre. Tableaux colorés ok/mo/ko.\n- Titre <h2>DX.n — nom exact de la liste.</h2>\n")
        print("## Ta mémoire permanente")
        print("\n".join(f"- {l}" for l in m["lecons"]) or "(vide)")
        print("\n## Tes outils (tous gratuits)\n- `python3 harnais/agents/%s.py controle <fichier>` : écarts à la grille, point par point ; ouvre ton verrou\n- `python3 harnais/agents/%s.py fin <fichier>` : dernier contrôle + checkpoint ; lève le verrou\n- lecture ciblée : `python3 harnais/controle_lot.py extraire <fichier> --points N,N` ; AIPS : `python3 harnais/aips_texte.py <n°|--nom X> --section <mot>` ; PubMed : `python3 harnais/pubmed.py chercher|verifier` ou MCP\n- passage utile d'une longue source : `python3 harnais/grille14/passage.py <fichier_ou_url_en_cache> \"<mots>\"`" % (ag, ag))
        tache = f"{nom} {ag} LOT_{lot} " + ", ".join(per)
        r = subprocess.run(["python3", str(R / "harnais/bracelet/bracelet_suggest.py"), tache], capture_output=True, text=True, cwd=R)
        pr = R / "harnais/PREUVE_EMBOITEMENT.txt"
        with open(pr, "a", encoding="utf-8") as fh:
            fh.write(f"\n{time.strftime('%Y-%m-%d %H:%M')} Europe/Zurich\nboucle=memoire-{ag}-LOT_{lot}\nok={r.returncode == 0}\ncommande=python3 harnais/bracelet/bracelet_suggest.py \"{tache}\"\n{r.stdout.strip()}\nexit={r.returncode}\nARSENAL_lu=harnais/ARSENAL.md\nHARNAIS_lu=harnais/HARNAIS_OBLIGATOIRE.md\nproducteur={ag} ({mod})\n")
        print("\n## Bracelet pour ta tâche (preuve écrite)\n" + r.stdout.strip())
        m["taches"] += 1; sauve_mem(ag, m); return 0
    if cmd == "etat":
        print(json.dumps(dict(agent=ag, role=nom, modele=mod, perimetre=per, memoire=m), ensure_ascii=False, indent=1)); return 0
    if cmd == "lecon":
        m["lecons"] = (m["lecons"] + [a[0]])[-5:]; sauve_mem(ag, m); print("leçon enregistrée (5 au plus)"); return 0
    f = Path(a[0]) if a and not a[0].startswith("--") else None
    if f is None: print(__doc__); return 2
    nom_f = f.name
    if nom_f not in per: print(f"HORS PÉRIMÈTRE : {nom_f} n'est pas à {ag}. STOP."); return 3
    chemin = wk / nom_f if not f.is_absolute() and not f.exists() else f.resolve()
    pts = set(range(1, 15))
    if "--points" in a: pts = {int(x) for x in a[a.index("--points") + 1].split(",")}
    if cmd == "attendre":
        pr = wk / "pret" / nom_f; fin = time.time() + 540
        while time.time() < fin:
            if pr.exists(): print(f"PRÊT : {nom_f} a passé les scripts du rédacteur ; tu peux l'auditer."); return 0
            time.sleep(10)
        print(f"ATTENTE : {nom_f} n'est pas encore prêt. Relance `attendre` (sans rien faire d'autre)."); return 4
    if cmd == "controle":
        if bloque_f(wk, nom_f).exists(): print(f"BLOQUÉ : {nom_f} est bloqué (voir {bloque_f(wk, nom_f).name}). Arrête-toi, réponds « BLOQUÉ {nom_f} »."); return 5
        v = verrou(ag, chemin, "claim")
        if v.returncode == 3: print("VERROU PRIS PAR UN AUTRE AGENT. STOP."); return 3
        h0 = chemin.read_text(encoding="utf-8", errors="replace"); h, rep = reparer(h0, lot, nom_f)
        if rep:
            bak = R / ".cache/bak"; bak.mkdir(exist_ok=True); (bak / f"{ag}_{nom_f}").write_text(h0, encoding="utf-8"); chemin.write_text(h, encoding="utf-8")
            print("RÉPARÉ AUTOMATIQUEMENT (gratuit) : " + " ; ".join(rep))
        sha = hashlib.sha256(h.encode()).hexdigest()[:16]
        E, st = ecarts_points(h, pts)
        ordre = {"CRITIQUE": 0, "GRAVE": 1, "MOYEN": 2, "DETAIL": 3}
        for p, g, msg in sorted(E, key=lambda x: (ordre[x[1]], x[0])): print(f"[{'forme' if p == 0 else 'point %d' % p}] {g} : {msg}")
        n = {g: sum(1 for e in E if e[1] == g) for g in ("CRITIQUE", "GRAVE", "MOYEN")}
        print(f"ÉCARTS critiques={n['CRITIQUE']} graves={n['GRAVE']} moyens={n['MOYEN']} · mots={st['mots']} termes={st['termes']} fenêtres={st['fenetres']} · empreinte {sha}")
        return 0 if not n["CRITIQUE"] else 1
    if cmd == "fin":
        if bloque_f(wk, nom_f).exists(): print(f"BLOQUÉ : {nom_f} est déjà bloqué. Arrête-toi, réponds « BLOQUÉ {nom_f} »."); return 5
        h0 = chemin.read_text(encoding="utf-8", errors="replace"); h, rep = reparer(h0, lot, nom_f)
        if rep: chemin.write_text(h, encoding="utf-8"); print("RÉPARÉ AUTOMATIQUEMENT (gratuit) : " + " ; ".join(rep))
        E, st = ecarts_points(h, pts); crit = [e for e in E if e[1] == "CRITIQUE"]
        auditeur = ag.startswith("B")
        def echec(msg, sig, detail):
            print(msg); print(refus(ag, lot, wk, nom_f, sig, detail)); verrou(ag, chemin, "release")
            return 5 if bloque_f(wk, nom_f).exists() else 1
        if crit:
            lst = "\n".join(f"- [point {p}] {m}" for p, _, m in crit)
            return echec(f"REFUSÉ : {len(crit)} écart(s) critique(s) à la grille. Lance `controle`, corrige, relance.", "|".join(sorted(m for _, _, m in crit)), lst)
        if auditeur:
            v1 = int(a[a.index("--v1") + 1]) if "--v1" in a else None; v2 = int(a[a.index("--v2") + 1]) if "--v2" in a else None
            c = int(a[a.index("--crit") + 1]) if "--crit" in a else 0
            if v1 is None or v2 is None: print("REFUSÉ : saisis tes scores : --v1 <exactitude du fond %> --v2 <conformité grille et Prompt %> [--crit N]. (Pas un essai perdu.)"); return 1
            if v1 < 90 or v2 < 90 or c:
                return echec(f"REFUSÉ : V1={v1} V2={v2} critiques={c} (seuil 90 %, zéro critique). Corrige les points qui pèsent, puis relance.", f"v1<90={v1 < 90} v2<90={v2 < 90} c={c}", f"V1={v1} V2={v2} critiques={c}")
            aud = wk / "audits"; aud.mkdir(exist_ok=True)
            (aud / f"AUD_{ag}_{nom_f}.md").write_text(f"# Audit {ag} · {nom_f}\nV1 (fond) = {v1} %\nV2 (conformité grille et Prompt) = {v2} %\ncritiques = {c}\nagent = {nom}, {mod}\n", encoding="utf-8")
        cmdc = ["python3", str(R / "harnais/checkpoint.py"), lot, str(chemin), "--cycle", "7"] + ([] if auditeur else ["--sans-commit"])
        r = subprocess.run(cmdc, capture_output=True, text=True, cwd=R); out = r.stdout.strip()[-700:]
        if r.returncode != 0: return echec(out, out, out)  # les scores gardent leurs chiffres : une hausse de score est un progrès, pas une stagnation
        print(out); verrou(ag, chemin, "release"); reussite(ag, lot, nom_f)
        m["taches"] += 1; sauve_mem(ag, m)
        if not auditeur: (wk / "pret").mkdir(exist_ok=True); (wk / "pret" / nom_f).write_text(time.strftime("%H:%M:%S"))
        return 0
    print(__doc__); return 2

if __name__ == "__main__":
    sys.exit(main())
