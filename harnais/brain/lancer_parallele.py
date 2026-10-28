#!/usr/bin/env python3
"""Lanceur PARALLÈLE du Cours Flash : un agent par point, en parallèle (ordre de Vial, 28.10.2026 : un cours Flash par leçon en 5 à 8 min).
  python3 harnais/brain/lancer_parallele.py <leçon.html …> [--sonnet 16] [--opus 12] [--limite-duo 180] [--limite-prof 300]
                                            [--taille 25000] [--journal DIR] [--sans-professeur] [--dry-run]
Complète harnais/brain/lancer_circuit.py (séquentiel, une leçon par agent, inchangé) : mêmes agents, mêmes portes, mêmes garde-fous.
1. Script (gratuit, secondes) : instantané d'entrée (`circuit_vial.py memoire duo … --flash`), découpe de la leçon en ses 14 points (un
   point de plus de --taille octets est coupé en parties aux frontières de blocs), squelette Flash du gabarit posé par le script (îlots 1–4,
   5–6, puis 7–14 repliés en <details>, titres <h3>, CSS brain-flash) ; un fichier de travail par fragment (<journal>/<leçon>.fragments/).
2. Un duo médico-linguiste Sonnet PAR FRAGMENT, en parallèle (`claude -p --agent duo-medico-linguiste --model sonnet`, mode dontAsk :
   Edit permis sur SON fragment seulement, Write interdit, Bash limité aux scripts AIPS/PubMed), limite stricte --limite-duo s. Fragment non
   rendu à temps, en erreur ou cassé (balises, <h3>, îlot, <script>) : l'original reste, refus notifié (notifications.md), la leçon progresse.
3. Réassemblage par script, réparation (S21.reparer --flash), `point N` des 14 points (copies parallèles ; couverture inscrite pour les
   points VERTS), porte `circuit_vial.py fin … --role duo --flash`, registre des fautes, mesure_ko (bande 100–298 Ko).
4. Professeur émérite Opus (effort moyen), UNE tentative, seulement sur les fragments des points signalés (point non VERT, GRAVE/CRITIQUE au
   registre, chiffre ou appel de source perdu), limite --limite-prof s ; garde « sans perte » : un point qui a perdu un chiffre sourcé ou un
   appel de source revient à sa dernière version sans perte (notifié) ; porte `fin --role professeur` ; fautes restantes en tableau .md à Vial.
5. Capacités : --sonnet places Sonnet et --opus places Opus simultanées (sémaphores partagés entre leçons ; au-delà, vagues automatiques,
   plus gros fragments d'abord). Journal : <journal>/<leçon>.jsonl (un événement par appel et par porte), notifications.md, bilan.json.
--dry-run : découpe, squelette, briefs et commandes écrits dans le dossier de travail ; aucun agent lancé ; la leçon n'est pas modifiée."""
import json, os, re, shutil, signal, subprocess, sys, tempfile, threading, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
D = Path(__file__).resolve().parent; R = D.parents[1]
sys.path[:0] = [str(D / "scriptones"), str(D)]
import bus
import s21_forme_vial as S21
import circuit_vial as CV
import lancer_circuit as LC
import mesure_ko as MK

CVP = "harnais/brain/circuit_vial.py"
ROLES = {"duo": dict(agent="duo-medico-linguiste", model="sonnet", effort=None),
         "assembleur": dict(agent="assembleur-mise-en-forme", model="sonnet", effort=None),
         "professeur": dict(agent="professeur-emerite", model="opus", effort="medium")}
OUTILS_FIXES = ["Read", "Grep", "Glob", "Bash(python3 harnais/aips_texte.py *)", "Bash(python3 harnais/pubmed.py *)", "Bash(grep *)", "Bash(wc *)",
                "mcp__PubMed__search_articles", "mcp__PubMed__get_article_metadata", "mcp__PubMed__lookup_article_by_citation"]
VIDES = {"input", "br", "hr", "img", "meta", "wbr", "link", "source", "col", "area", "base", "embed", "param", "track"}
RX_CHIFFRE = re.compile(r"\d+(?:[,.]\d+)?\s?%|\d+(?:[,.]\d+)?\s?(?:mg|µg|g|ml|mmHg|ans|cm|mmol/l|heures|semaines|jours)\b")   # = circuit_vial.chiffres
VERROU = threading.Lock()


def opt(a, k, d): return LC.opt(a, k, d)


def lire(f): return Path(f).read_text(encoding="utf-8", errors="replace")


def chiffres(h): return set(RX_CHIFFRE.findall(bus.texte(CV.nu(h))))


def sources(h): return h.count('<sup class="r">')


def equilibre(h):
    m = S21._inerte(h); return {g: len(re.findall(rf"(?i)<{g}[\s>]", m)) - len(re.findall(rf"(?i)</{g}\s*>", m)) for g in S21.BALISES}


# ───────────────────────── 1. découpe et squelette (script, gratuit) ─────────────────────────
def deballer(t):
    """Retire les îlots déjà posés (relance idempotente) : ouvrantes, fermantes et <summary> autour des titres de point."""
    ops = []
    for a, b, g, _ in S21.ilots(t):
        if b is None: continue
        ops += [(a, t.find(">", a) + 1), (t.rfind("</", a, b), b)]
    for a, b in sorted(ops, reverse=True): t = t[:a] + t[b:]
    return re.sub(r"(?is)<summary>\s*(<h3\b[^>]*>.*?</h3>)\s*</summary>", r"\1", t)


def decouper(t):
    """(tête, {n: (h3, corps)}, queue) : le titre <h3> appartient au script, le corps au fragment."""
    t = deballer(t); S = bus.sections(t); ns = sorted(S, key=lambda n: S[n][0])
    if not ns: raise ValueError("aucun point « <h3 …>N. … » trouvé")
    pts = {}
    for n in ns:
        a, b = S[n]; seg = t[a:b]; k = seg.find("</h3>") + 5
        pts[n] = (seg[:k], seg[k:])
    return t[:S[ns[0]][0]], pts, t[S[ns[-1]][1]:]


def morceaux(corps, taille):
    """Coupe un corps trop gros en parties de taille voisine, seulement aux fins de ligne où aucune balise n'est ouverte."""
    o = len(corps.encode())
    if o <= taille: return [corps]
    m = S21._inerte(corps); prof = 0; coupes = []
    for x in re.finditer(r"<(/?)([a-zA-Z][\w-]*)\b[^>]*?(/?)>|\n", m):
        if x.group(0) == "\n":
            if prof == 0: coupes.append(x.end())
            continue
        if x.group(2).lower() in VIDES or x.group(3): continue
        prof = max(0, prof + (-1 if x.group(1) else 1))
    nb = -(-o // taille); cible = len(corps) / nb; parts, deb = [], 0
    for c in coupes:
        if c - deb >= cible and len(parts) < nb - 1 and len(corps) - c > cible * 0.3: parts.append(corps[deb:c]); deb = c
    parts.append(corps[deb:])
    return [p for p in parts if p] or [corps]


def assembler(tete, pts, frags):
    """Squelette Flash du gabarit : îlot 1–4, îlot 5–6, puis chaque point 7–14 replié dans <details class="ilot">."""
    out = [tete]; bloc = lambda n: pts[n][0] + "".join(frags[n]).rstrip("\n") + "\n"
    for grp, nom in (((1, 2, 3, 4), "1-4"), ((5, 6), "5-6")):
        g = [n for n in grp if n in pts]
        if g: out.append(f'<section class="ilot" data-ilot="{nom}">\n' + "".join(bloc(n) for n in g) + "</section>\n")
    for n in sorted(x for x in pts if x >= 7):
        out.append(f'<details class="ilot" data-ilot="{n}"><summary>{pts[n][0]}</summary>' + "".join(frags[n]).rstrip("\n") + "\n</details>\n")
    return "".join(out)


def gabarit(n):
    """Modèle du point n dans harnais/brain/gabarit_flash.html (îlots retirés : le script les pose)."""
    g = lire(D / "gabarit_flash.html"); S = bus.sections(g)
    if n not in S: return ""
    a, b = S[n]; s = g[a:b]; s = s[s.find("</h3>") + 5:]
    s = re.sub(r'(?is)<details class="ilot"[^>]*><summary>|</summary>|</details>|<section class="ilot"[^>]*>|</section>', "", s)
    return s.strip()[:3500]


# ───────────────────────── 2. agents par fragment ─────────────────────────
CONSIGNES = {
    1: "définir en une ou deux phrases selon la société savante citée ; termes dédiés en span.dx ; arbre data-brain conservé.",
    2: "chiffres suisses puis européens, chacun avec sa population et sa source ; le détail chiffré secondaire en fenêtre.",
    3: "mécanisme en chaîne causale courte (cause → mécanisme → signe) ; la cascade détaillée en fenêtre span.dx.",
    4: "démarche en étapes courtes ; diagnostic différentiel utile dans une fenêtre div.fxw > div.fx, jamais en bloc dans le corps.",
    5: "symptômes listés simplement, CHACUN cliquable (span.dx : caractère, durée, valeur d'orientation) ; drapeaux rouges explicites.",
    6: "région par région, chaque signe cliquable (span.sc.dx) dont la fenêtre dit « Recherche : » (position, geste, manœuvre) et « Valeur : ».",
    7: "chaque « 7.n Syndrome de … » est le label d'un div.fxw dont la fenêtre contient un tableau à 2 colonnes exactement « Symptômes "
       "fonctionnels | Signes physiques » (symptômes en span.dx, signes en span.sc.dx) ; « 7.n » n'est jamais répété dans la fenêtre.",
    8: "critères de la société savante (année) en phrases complètes ; le détail des critères en fenêtre.",
    9: "examen de référence d'abord, puis examens de seconde ligne ; indications et pièges en fenêtres.",
    10: "algorithme en cases : si un div.algo existe, modifie seulement son <template class=\"algo-modele\"> (JSON : noeuds case / losange / fin, "
        "texte ≤ 60 caractères, « detail » en phrases complètes ; liens Oui / Non) ; le script redessine cases et traits orthogonaux.",
    11: "1- But (une phrase claire) ; 2- Moyens et méthodes : A- En urgences (algorithme en cases <template class=\"algo-modele\"> à traits "
        "orthogonaux, non-spécialiste puis service spécialisé, actes cliquables) ; B- Hors urgences (mesures générales, puis spécifiques par priorité : "
        "pharmacologiques avec dose lue dans l'AIPS, puis non pharmacologiques) ; tableaux de spécialités et situations spéciales en fenêtres div.fxw.",
    12: "prévention primaire, secondaire, tertiaire en phrases courtes ; le détail en fenêtre.",
    13: "points clés : puces courtes et verbales, une idée par puce, sans redite du corps.",
    14: "questions d'examen et réponses en phrases complètes ; la justification détaillée en fenêtre span.dx.",
}


def brief_duo(nom, n, titre, k, m, frag, prefixe, chf, limite, cible):
    part = f", partie {k}/{m} (les autres parties sont confiées à d'autres agents : traite seulement la tienne, dans son ordre)" if m > 1 else ""
    return (f"MODE FRAGMENT PARALLÈLE (ordre de Vial : un cours Flash par leçon en quelques minutes). Tu traites UN SEUL fichier : {frag} = corps du "
            f"point {n} « {titre} »{part} de la leçon {nom}. Le titre <h3>, les îlots (class=\"ilot\"), la CSS et l'assemblage sont posés par le "
            f"script : n'écris aucun <h3>, aucun îlot, aucun <style>. N'exécute ni memoire, ni point, ni fin (le lanceur les exécute) ; aucun Edit hors "
            f"de {frag} ; pas de Write. Temps : {limite} s au plus (arrêt forcé ; un fragment non rendu reste l'original) : utilise-les pour "
            f"restyliser TOUT le fragment, jamais un travail partiel, sans compte rendu.\n"
            f"VOLUME : le fragment fait {cible[0]} octets ; CIBLE ≤ {cible[1]} octets (Pareto : le corps maigrit ; fenêtres comprises), contrôle par "
            f"`wc -c {frag}`. Le cours entier doit tenir dans 100–298 Ko (visé 200).\n"
            f"Méthode : Read {frag} une seule fois, puis 2 à 5 Edit de blocs entiers, du début à la fin du fichier (chaque balise ouverte refermée dans "
            f"le même Edit ; une ligne par paragraphe, puce ou rangée) ; réponse finale : une seule ligne « FAIT : octets avant → après ».\n"
            + LC.PARETO +
            "Règle Pareto : le corps ne garde que les 20 % d'information utile ; phrases complètes (sujet, verbe, complément), ≤ 40 mots, registre "
            "universitaire, ni « on », « il y a », « ça », ni tutoiement ni impératif ; une idée par phrase ; mécanisme → symptômes et signes → prise en charge. "
            "Fenêtres et mots interactifs nombreux : span.dx (courte, avec <label class=\"fx-x\" for=…>×</label>) ou div.fxw > div.fx (riche : tableau, "
            "méthode, différentiel ; jamais dans un <p>) ; survol span.df ≤ 40 mots.\n"
            f"Point {n} : {CONSIGNES.get(n, '')}\n"
            "FOND EXACT : jamais de chiffre, de dose ni de référence inventés ; doses AIPS suisse seulement (jamais le Compendium) ; aucun chiffre sourcé "
            "retiré : un chiffre secondaire descend dans une fenêtre AVEC son appel de source. "
            + (f"Chiffres à conserver (corps ou fenêtre) : {', '.join(sorted(chf))}. " if chf else "") +
            "Tous les appels <sup class=\"r\">…</sup> et liens href=\"#sb-…\" / \"#med-…\" restent (leur nombre ne baisse jamais) ; blocs générés "
            "(data-brain, data-modele) conservés tels quels. "
            f"Identifiants : tout id et for nouveaux commencent par « {prefixe} » (uniques dans la leçon) ; jamais d'attribut title ; tableau dans "
            "<div style=\"overflow-x:auto\"> ; ni <script> ni <img>.\n"
            f"Modèle exact (harnais/brain/gabarit_flash.html, point {n}) :\n{gabarit(n)}")


def brief_prof(nom, n, titre, k, m, frag, fautes, perdus, limite):
    part = f", partie {k}/{m}" if m > 1 else ""
    return (f"MODE FRAGMENT PARALLÈLE, professeur émérite, UNE seule tentative, LIMITE STRICTE {limite} s. Fichier unique : {frag} = corps du point "
            f"{n} « {titre} »{part} de la leçon {nom} (Cours Flash, harnais/etat/COURS_FLASH.md). N'exécute ni memoire, ni scanner, ni point, ni fin "
            f"(le lanceur les exécute) ; aucun Edit hors de {frag} ; pas de Write ; n'écris aucun <h3>, îlot ni <style>.\n"
            "Read une fois, puis Edit exacts : corrige d'abord les fautes signalées, puis vérifie le fond dans le corps ET dans les fenêtres (exactitude "
            "clinique, doses AIPS suisse seulement, chiffres retrouvés dans leurs sources, références existantes, ordre de priorité de la prise en charge). "
            "Ne regonfle pas le volume ; ne retranche que le faux ; jamais de chiffre ni de dose inventés (sinon « À vérifier ») ; îlots et fenêtres du "
            "gabarit intacts ; identifiants nouveaux préfixés « p" + str(n) + "-prof- ».\n"
            + (f"Chiffres sourcés perdus à restituer (avec leur appel de source, en fenêtre si secondaires) : {', '.join(sorted(perdus))}.\n" if perdus else "")
            + "Fautes signalées par la porte et le registre :\n- " + "\n- ".join(fautes[:25]) +
            "\nRéponse : une ligne (corrigé / restant, et pourquoi).")


REFUS_RX = re.compile(r"(?is)^\s*(je ne peux pas|je ne ferai pas|je refuse|désolé, je ne|i can't|i cannot|i won't)")
CONTEXTE = ("CONTEXTE (légitime, validé par Vial) : fiche de révision médicale destinée à des médecins en spécialisation pour l'examen fédéral suisse ; "
            "travail éditorial sur un fichier HTML local, sources citées, aucune donnée personnelle. La tâche est dans ton mandat : exécute-la. ")


def SANS_PROF(a):
    """Opus suspendus (ordre de Vial : production d'abord, audits après le LOT 248) : drapeau --sans-professeur OU fichier .cache/brain/sans_professeur."""
    return "--sans-professeur" in a or (R / ".cache/brain/sans_professeur").exists()


def appel(role, frag, prompt, places, limite, journal, essai, etiquette, reprise=False):
    r = ROLES[role]
    cmd = ["claude", "-p", prompt, "--agent", r["agent"], "--model", r["model"], "--output-format", "json", "--permission-mode", "dontAsk",
           "--add-dir", str(Path(frag).parent), "--allowedTools", *OUTILS_FIXES, f"Edit(/{frag})",
           "--disallowedTools", *LC.INTERDITS]
    if r["effort"]: cmd += ["--effort", r["effort"]]
    if essai: return dict(role=role, fragment=etiquette, cmd=cmd[:2] + ["<brief>"] + cmd[3:], limite_s=limite)
    with places:
        t0 = time.time(); hors_temps = False
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=R, start_new_session=True)
        try: out, err = p.communicate(timeout=limite)
        except subprocess.TimeoutExpired:                    # limite stricte : tout le groupe de processus est arrêté
            hors_temps = True
            try: os.killpg(p.pid, signal.SIGKILL)
            except ProcessLookupError: pass
            out, err = p.communicate()
        try: d = json.loads(out) if not hors_temps else {"result": f"temps imparti dépassé ({limite} s)", "is_error": True}
        except ValueError: d = {"result": ((out or "") + (err or ""))[-800:], "is_error": True}
    ev = dict(role=role, fragment=etiquette, duree_s=round(time.time() - t0, 1), hors_temps=hors_temps, cout_usd=d.get("total_cost_usd"),
              tours=d.get("num_turns"), modeles=list((d.get("modelUsage") or {}).keys()), refus_outils=len(d.get("permission_denials") or []),
              reponse=str(d.get("result", ""))[-500:], erreur=bool(d.get("is_error")))
    ecrire_journal(journal, ev)
    if not reprise and REFUS_RX.match(ev["reponse"] or ""):     # refus d'agent : détecté, notifié, UNE relance avec le contexte légitime
        ecrire_journal(journal, dict(refus_agent=etiquette, role=role, extrait=ev["reponse"][:200]))
        return appel(role, frag, CONTEXTE + prompt, places, limite, journal, essai, etiquette, reprise=True)
    return ev


def valider(orig, neuf):
    """Motif de rejet d'un fragment rendu (None si recevable) : il ne doit pas casser l'assemblage."""
    if not neuf.strip(): return "fragment vide"
    if equilibre(neuf) != equilibre(orig): return f"balises de bloc déséquilibrées ({equilibre(orig)} → {equilibre(neuf)})"
    nb = lambda rx, h: len(re.findall(rx, h, re.I))                 # ajouts seulement : un bloc déjà présent (algorithme rendu) reste admis
    if nb(r"<h3[\s>]", neuf) > nb(r"<h3[\s>]", orig): return "<h3> ajouté (titre réservé au script)"
    if len(S21.RX_ILOT.findall(neuf)) > len(S21.RX_ILOT.findall(orig)): return "îlot ajouté dans un fragment (réservé au script)"
    rx = r"<script[\s>]|<img[\s>]|<link[^>]+stylesheet|<style[\s>]"
    if nb(rx, neuf) > nb(rx, orig): return "<script>, <img>, <style> ou feuille externe ajouté"
    if len(neuf) < 0.08 * len(orig): return f"fragment réduit à {len(neuf)} caractères sur {len(orig)} (perte probable)"
    return None


def vague(role, jobs, places, limite, journal, jd, nom, essai, pool):
    """Lance un agent par fragment (plus gros d'abord) ; rejette et restaure tout fragment non rendu, en erreur ou cassé."""
    jobs = sorted(jobs, key=lambda j: -len(j["texte"]))
    for j in jobs: Path(j["chemin"]).write_text(j["texte"], encoding="utf-8")
    fut = [pool.submit(appel, role, j["chemin"], j["prompt"], places, limite, journal, essai, j["id"]) for j in jobs]
    res = {}
    for j, f in zip(jobs, fut):
        ev = f.result(); j["ev"] = ev
        if essai: res[j["id"]] = j["texte"]; continue
        neuf = lire(j["chemin"]); motif = None
        if ev["hors_temps"]: motif = f"non rendu à temps ({limite} s)"
        elif neuf == j["texte"]: motif = "fragment inchangé" + (f" (erreur : {ev['reponse'][-160:]})" if ev["erreur"] else "")
        else: motif = valider(j["texte"], neuf)
        if motif:
            neuf = j["texte"]; Path(j["chemin"]).write_text(neuf, encoding="utf-8")
            notifier(jd, nom, f"{role} {j['id']}", f"{motif} : l'original du fragment est conservé, la leçon progresse.")
        j["accepte"] = not motif; j["motif"] = motif; res[j["id"]] = neuf
    return res


# ───────────────────────── 3. portes (scripts existants) ─────────────────────────
def run(*c, timeout=1800):
    p = subprocess.run([sys.executable, *c], capture_output=True, text=True, cwd=R, timeout=timeout)
    return p.returncode, (p.stdout + p.stderr).strip()


def controle_points(f, journal):
    """`circuit_vial.py point N --flash` sur des copies (en parallèle, 4 cœurs) ; la couverture du vrai fichier est inscrite pour les points VERTS."""
    t = lire(f); ns = sorted(bus.sections(t)); tmp = Path(tempfile.mkdtemp(prefix="pts_", dir=CV.CACHE))
    def un(n):
        c = tmp / f"{Path(f).stem}__p{n}.html"; c.write_text(t, encoding="utf-8")
        rc, out = run(CVP, "point", str(c), str(n), "--flash", timeout=900); return n, rc == 0, out
    with ThreadPoolExecutor(min(4, os.cpu_count() or 4)) as ex: R_ = list(ex.map(un, ns))
    shutil.rmtree(tmp, ignore_errors=True)
    for n, ok, _ in R_:
        if ok: CV.couverture(f, n=n, sig=CV.signature(t, n))
    ecrire_journal(journal, dict(porte="point", verts=[n for n, ok, _ in R_ if ok], ecarts={n: out[-600:] for n, ok, out in R_ if not ok}))
    return {n: (ok, out) for n, ok, out in R_}


def porte_et_registre(f, role, jd, journal, etiquette, marquer=None):
    """Réparation sûre, puis porte unique `fin` et registre portable des fautes, en parallèle (lecture seule après la réparation)."""
    t = lire(f); t2, J = S21.reparer(t, True)
    if t2 != t: bus.ecrire_atomique(f, t2)
    rj, rm = jd / f"{Path(f).stem}.{etiquette}.json", jd / f"{Path(f).stem}.{etiquette}.md"
    with ThreadPoolExecutor(2) as ex:
        a = ex.submit(run, CVP, "fin", f, "--role", role, "--flash")
        b = ex.submit(run, CVP, "registre", f, "--json", str(rj), "--md", str(rm), "--flash", *(["--marquer", str(marquer)] if marquer else []))
        (rc, out), _ = a.result(), b.result()
    ko = MK.verdict(Path(f).stat().st_size)
    ev = dict(porte=f"fin {role}", verdict="ACCEPTÉ" if rc == 0 else "REFUSÉ", reparations=J[:6], sortie=out[-1500:],
              ko=round(Path(f).stat().st_size / MK.KO, 1), bande=ko, registre=str(rm))
    ecrire_journal(journal, ev)
    try: fautes = json.loads(rj.read_text())["fautes"]
    except (OSError, ValueError, KeyError): fautes = []
    return rc == 0, out, fautes, ev


# ───────────────────────── utilitaires ─────────────────────────
def ecrire_journal(journal, ev):
    with VERROU, open(journal, "a", encoding="utf-8") as j: j.write(json.dumps(ev, ensure_ascii=False) + "\n")


def notifier(jd, nom, quoi, motif):
    msg = f"REFUS notifié · {nom} · {quoi} : {motif}"
    print(msg, file=sys.stderr)
    with VERROU, open(jd / "notifications.md", "a", encoding="utf-8") as n: n.write(f"- {time.strftime('%H:%M:%S')} {msg}\n")


def fragments(t, taille, dossier, sous):
    """Découpe en jobs : [{id, n, k, m, chemin, texte}] + structure (tête, pts, queue)."""
    tete, pts, queue = decouper(t); jobs = []
    d = dossier / sous; d.mkdir(parents=True, exist_ok=True)
    for n, (h3, corps) in pts.items():
        ps = morceaux(corps, taille)
        for k, p in enumerate(ps, 1):
            i = f"p{n:02d}" + (chr(96 + k) if len(ps) > 1 else "")
            jobs.append(dict(id=i, n=n, k=k, m=len(ps), chemin=str((d / f"{i}.html").resolve()), texte=p, titre=bus.texte(h3)))
    return tete, pts, queue, jobs


def recomposer(tete, pts, queue, jobs, textes):
    frags = {n: [textes[j["id"]] for j in sorted((j for j in jobs if j["n"] == n), key=lambda j: j["k"])] for n in pts}
    return S21.corriger(assembler(tete, pts, frags) + queue, {"flash": True})


def lignes_point(t):
    return {n: (bus.ligne(t, a), bus.ligne(t, b)) for n, (a, b) in bus.sections(t).items()}


# ───────────────────────── leçon ─────────────────────────
def lecon(f, P, a, pool):
    T0 = time.time(); nom = Path(f).name; essai = "--dry-run" in a
    jd = Path(opt(a, "--journal", str(R / ".cache/brain/circuit/parallele"))).resolve(); jd.mkdir(parents=True, exist_ok=True)
    fait = jd / (Path(f).stem + ".fait.json")                  # reprise après redémarrage du conteneur : une leçon terminée n'est jamais refaite
    if "--reprendre" in a and fait.exists(): return json.loads(fait.read_text(encoding="utf-8"))
    journal = jd / (nom + ".jsonl"); dossier = jd / (Path(f).stem + ".fragments"); taille = opt(a, "--taille", 25000)
    ld, lp = opt(a, "--limite-duo", 180), opt(a, "--limite-prof", 300); temps = {}
    res = dict(lecon=f, ko_avant=round(Path(f).stat().st_size / MK.KO, 1))
    ecrire_journal(journal, dict(debut=time.strftime("%Y-%m-%d %H:%M:%S"), lecon=f, mode="dry-run" if essai else "réel"))
    # 1. instantané d'entrée + découpe + squelette
    if not essai:
        rc, out = run(CVP, "memoire", "duo", f, "--flash"); (dossier).mkdir(parents=True, exist_ok=True)
        (dossier / "memoire.txt").write_text(out, encoding="utf-8")
    t0 = lire(f); tete, pts, queue, jobs = fragments(t0, taille, dossier, "duo")
    origine = {j["id"]: j["texte"] for j in jobs}
    orig_point = {n: corps for n, (_, corps) in pts.items()}
    sq = recomposer(tete, pts, queue, jobs, origine); (dossier / "squelette.html").write_text(sq, encoding="utf-8")
    fixe = len(sq.encode()) - sum(len(x.encode()) for x in origine.values())       # tête, CSS, sources, fenêtres de médicaments : hors fragments
    ratio = min(0.85, max(0.4, (150 * MK.KO - fixe) / max(1, sum(len(x.encode()) for x in origine.values()))))
    res["ratio_cible"] = round(ratio, 2)
    pref = Path(f).stem.split("_")[-1].lower().replace(".", "")[:6] or "l"
    for j in jobs:
        j["prompt"] = brief_duo(nom, j["n"], j["titre"], j["k"], j["m"], j["chemin"], f"{pref}-{j['id']}-", chiffres(j["texte"]), ld,
                               (len(j["texte"].encode()), int(len(j["texte"].encode()) * ratio)))
    temps["decoupe_s"] = round(time.time() - T0, 1)
    res["fragments"] = [dict(id=j["id"], point=j["n"], octets=len(j["texte"].encode())) for j in jobs]
    if essai:
        (dossier / "briefs_duo.json").write_text(json.dumps([dict(id=j["id"], chemin=j["chemin"], prompt=j["prompt"]) for j in jobs], ensure_ascii=False, indent=1))
        evs = [appel("duo", j["chemin"], j["prompt"], P["sonnet"], ld, journal, True, j["id"]) for j in jobs]
        res.update(dry_run=True, dossier=str(dossier), squelette_ko=round(len(sq.encode()) / MK.KO, 1), squelette_bande=MK.verdict(len(sq.encode())),
                   flash_squelette=sorted({d["code"] for d in S21.flash(sq, nom)[0]}), commande_type=evs[0]["cmd"] if evs else None, temps=temps)
        return res
    # 2. duos en parallèle, un par fragment
    t1 = time.time(); txt_duo = vague("duo", jobs, P["sonnet"], ld, journal, jd, nom, False, pool)
    temps["duo_s"] = round(time.time() - t1, 1)
    res["duo"] = [dict(id=j["id"], accepte=j["accepte"], motif=j["motif"], duree_s=j["ev"]["duree_s"], cout=j["ev"]["cout_usd"]) for j in jobs]
    # 3. réassemblage + portes
    t2 = time.time(); bus.ecrire_atomique(f, recomposer(tete, pts, queue, jobs, txt_duo))
    if "--sans-assembleur" not in a:                          # ordre de Vial : la mise en forme finale est faite à l'assemblage par un agent Sonnet 5.5
        avant, ta = lire(f), time.time()
        brief = (f"Leçon assemblée : {f}. Tu es l'assembleur-metteur en forme (lis ton agent). Départ : Read du fichier par blocs ; modifie par Edit ciblés ; "
                 f"limite stricte {opt(a, '--limite-assembleur', 240)} s ; volume 100–200 Ko ; aucun chiffre ni appel de source retranché. Une ligne de réponse.")
        appel("assembleur", f, brief, P["sonnet"], opt(a, "--limite-assembleur", 240), journal, False, "assemblage")
        apres = lire(f)
        motif = valider(avant, apres) or ("chiffre ou appel de source perdu" if (chiffres(avant) - chiffres(apres)) or sources(apres) < sources(avant) else None)
        if motif: bus.ecrire_atomique(f, avant); notifier(jd, nom, "assemblage", f"mise en forme rejetée ({motif}) : version recollée conservée.")
        temps["assemblage_s"] = round(time.time() - ta, 1)
    PTS = controle_points(f, journal)
    ok, out, fautes, ev = porte_et_registre(f, "duo", jd, journal, "registre_duo")
    temps["porte_duo_s"] = round(time.time() - t2, 1)
    res["porte_duo"] = dict(verdict=ev["verdict"], ko=ev["ko"], bande=ev["bande"], points_verts=[n for n, (o, _) in PTS.items() if o], motif=out[-700:])
    if not ok: notifier(jd, nom, "porte duo", "REFUSÉ : points signalés au professeur. " + out[-300:].replace("\n", " "))
    # 4. professeur Opus : une tentative, points signalés seulement
    t = lire(f); tete, pts, queue, jobs2 = fragments(t, taille, dossier, "professeur"); L = lignes_point(t)
    chf_orig = {n: chiffres(c) for n, c in orig_point.items()}; src_orig = {n: sources(c) for n, c in orig_point.items()}
    def en_point(r):
        return next((n for n, (la, lb) in L.items() if la <= (r.get("ligne") or 0) < lb), None)
    signal_ = {}
    for n, (o, sortie_) in PTS.items():
        if not o: signal_.setdefault(n, []).extend(l[2:] for l in sortie_.splitlines() if l.startswith("- "))
    for r in fautes:
        n = en_point(r)
        if n and r["severite"] in ("CRITIQUE", "GRAVE"): signal_.setdefault(n, []).append(f"{r['severite']} {r['code']} l.{r['ligne']} : {r['constat']} → {r['correction']}")
    for n, (_, corps) in pts.items():
        perdus = chf_orig.get(n, set()) - chiffres(corps)
        if perdus or sources(corps) < src_orig.get(n, 0):
            signal_.setdefault(n, []).append(f"perte : chiffres {sorted(perdus)} ; appels de source {src_orig.get(n, 0)} → {sources(corps)}")
    res["points_signales"] = sorted(signal_)
    if signal_ and not SANS_PROF(a):
        t3 = time.time(); jp = [j for j in jobs2 if j["n"] in signal_]
        for j in jp:
            j["prompt"] = brief_prof(nom, j["n"], j["titre"], j["k"], j["m"], j["chemin"], list(dict.fromkeys(signal_[j["n"]])),
                                     chf_orig.get(j["n"], set()) - chiffres(j["texte"]) if j["m"] == 1 else set(), lp)
        txt = {j["id"]: j["texte"] for j in jobs2}; txt.update(vague("professeur", jp, P["opus"], lp, journal, jd, nom, False, pool))
        temps["professeur_s"] = round(time.time() - t3, 1)
        res["professeur"] = [dict(id=j["id"], accepte=j["accepte"], motif=j["motif"], duree_s=j["ev"]["duree_s"], cout=j["ev"]["cout_usd"]) for j in jp]
        t = recomposer(tete, pts, queue, jobs2, txt)
    # garde « sans perte » : un point qui a perdu un chiffre sourcé ou un appel de source revient à sa dernière version sans perte
    t4 = time.time(); tete, pts, queue = decouper(t); duo_point = {n: "".join(txt_duo[j["id"]] for j in sorted((j for j in jobs if j["n"] == n), key=lambda j: j["k"])) for n in pts}
    retours = []
    for n, (h3, corps) in list(pts.items()):
        sans_perte = lambda c: not (chf_orig.get(n, set()) - chiffres(c)) and sources(c) >= src_orig.get(n, 0)
        if sans_perte(corps): continue
        jn = sorted((j for j in jobs if j["n"] == n), key=lambda j: j["k"])          # duo mixte : seules les parties fautives reviennent à l'original
        mixte = "".join(txt_duo[j["id"]] if not (chiffres(j["texte"]) - chiffres(txt_duo[j["id"]])) and sources(txt_duo[j["id"]]) >= sources(j["texte"])
                        else j["texte"] for j in jn)
        repli = next((c for c in (duo_point.get(n), mixte, orig_point.get(n)) if c and sans_perte(c)), orig_point.get(n, corps))
        pts[n] = (h3, repli); retours.append(n)
        notifier(jd, nom, f"point {n}", "chiffre ou appel de source perdu : dernière version sans perte restaurée.")
    t = S21.corriger(assembler(tete, pts, {n: [c] for n, (_, c) in pts.items()}) + queue, {"flash": True})
    bus.ecrire_atomique(f, t); res["retours_sans_perte"] = retours
    role_final = "professeur" if signal_ and not SANS_PROF(a) else "duo"
    if role_final == "duo" and retours: controle_points(f, journal)
    okf, outf, fautes_f, evf = porte_et_registre(f, role_final, jd, journal, "restantes", jd / f"{Path(f).stem}.controle.html")
    temps["porte_finale_s"] = round(time.time() - t4, 1); temps["total_s"] = round(time.time() - T0, 1)
    if not okf: notifier(jd, nom, f"porte {role_final}", "REFUSÉ : fautes restantes en tableau pour Vial (" + evf["registre"] + ").")
    res.update(porte_finale=dict(role=role_final, verdict=evf["verdict"], ko=evf["ko"], bande=evf["bande"], motif=outf[-900:]),
               restantes=dict(tableau=evf["registre"], fautes=len(fautes_f), controle=str(jd / f"{Path(f).stem}.controle.html")), temps=temps)
    ecrire_journal(journal, dict(fin=time.strftime("%Y-%m-%d %H:%M:%S"), temps=temps))
    if not essai: fait.write_text(json.dumps(res, ensure_ascii=False), encoding="utf-8")
    return res


def main(a):
    fs = [str(Path(x).resolve()) for x in a if x.endswith(".html")]
    if not fs or "-h" in a or "--help" in a: print(__doc__); return 0
    if any(Path(x) == Path("/workspace/ssp/app.html") for x in fs): print("REFUSÉ : /workspace/ssp/app.html ne se modifie jamais"); return 2
    P = {"sonnet": threading.BoundedSemaphore(opt(a, "--sonnet", 16)), "opus": threading.BoundedSemaphore(opt(a, "--opus", 12))}
    jd = Path(opt(a, "--journal", str(R / ".cache/brain/circuit/parallele"))).resolve(); jd.mkdir(parents=True, exist_ok=True)
    T0 = time.time()
    with ThreadPoolExecutor(64) as pool, ThreadPoolExecutor(len(fs)) as ex:
        res = list(ex.map(lambda f: lecon(f, P, a, pool), fs))
    bilan = dict(date=time.strftime("%Y-%m-%d %H:%M:%S"), duree_totale_s=round(time.time() - T0, 1), lecons=res)
    (jd / "bilan.json").write_text(json.dumps(bilan, ensure_ascii=False, indent=1), encoding="utf-8")
    for r in res:
        if r.get("dry_run"):
            print(f"{Path(r['lecon']).name} : DRY-RUN · {len(r['fragments'])} fragments · squelette {r['squelette_ko']} Ko ({r['squelette_bande']}) · dossier {r['dossier']}")
        else:
            d = sum(1 for x in r["duo"] if x["accepte"]); p = r.get("professeur", [])
            print(f"{Path(r['lecon']).name} : duo {d}/{len(r['duo'])} fragments rendus · porte duo {r['porte_duo']['verdict']} · professeur "
                  f"{sum(1 for x in p if x['accepte'])}/{len(p)} · porte finale {r['porte_finale']['verdict']} · {r['porte_finale']['ko']} Ko "
                  f"({r['porte_finale']['bande']}) · {r['temps']['total_s']} s · restantes : {r['restantes']['tableau']}")
    print(f"bilan : {jd / 'bilan.json'} · durée totale {bilan['duree_totale_s']} s")
    return 0 if all(r.get("dry_run") or r["porte_finale"]["verdict"] == "ACCEPTÉ" for r in res) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
