#!/usr/bin/env python3
"""Lanceur du circuit duo → professeur par sous-agents RÉELS `claude -p --agent …`, hors moteur Workflow (plafonné à 2 agents sur 4 CPU).
  python3 harnais/brain/lancer_circuit.py <leçon.html …> [--sonnet 16] [--opus 12] [--boucles 1 (duo) / 0 (professeur)] [--etapes duo,professeur]
                                          [--journal DIR] [--consigne constats.md] [--dry-run] [--classique]
COURS FLASH par défaut (harnais/etat/COURS_FLASH.md ; gabarit harnais/brain/gabarit_flash.html) : memoire, porte, mesure et registre en
`--flash` (volume > 298 Ko refusé, îlots, fenêtres modales) ; `--classique` rend le circuit d'avant (forme Vial seule).
LOT_001 (Vial, 28.10.2026) : 16 leçons → 16 duos Sonnet, 12 professeurs Opus (une leçon par appel ; les leçons 13 à 16 attendent la
première place Opus libre). La capacité est réglable (--sonnet, --opus) sans changer le circuit.
Par leçon : duo (Sonnet, une leçon) → `circuit_vial.py fin --role duo` exécuté PAR LE LANCEUR (jamais sur la parole de l'agent) →
UNE seule tentative par défaut (--boucles 0, principe de Vial) → registre portable des fautes = bon de travail du professeur (Opus, effort
moyen) → `fin --role professeur` → mesure avant/après → fautes restantes en tableau Markdown (+ JSON, + HTML de contrôle marqué) pour Vial. Capacités : 16 places Sonnet et 12 places Opus (sémaphores) ; une leçon n'occupe jamais deux places.
Garde-fous : outil Write retiré (aucune réécriture du fichier entier) ; Edit interdit sur le dispositif (harnais/, tools/, .claude/, .github/,
CLAUDE.md, CONTINUATION.md, /workspace/ssp/app.html) ; Bash limité à python3 harnais/*, grep, sed -n, wc ; aucun commit.
Journal : <journal>/<leçon>.jsonl (une ligne par appel : rôle, passe, durée, coût, modèle, réponse, verdict de la porte) et bilan.json."""
import json, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
R = Path(__file__).resolve().parents[2]
C = "python3 harnais/brain/circuit_vial.py"
OUTILS = ["Read", "Edit", "Grep", "Glob", "Bash(python3 harnais/*)", "Bash(grep *)", "Bash(sed -n *)", "Bash(wc *)", "WebFetch", "WebSearch",
          "mcp__PubMed__search_articles", "mcp__PubMed__get_article_metadata", "mcp__PubMed__lookup_article_by_citation"]
INTERDITS = ["Write", "NotebookEdit"] + [f"Edit(/{R}/{x})" for x in ("harnais/**", "tools/**", ".claude/**", ".github/**", "CLAUDE.md", "CONTINUATION.md")] \
            + ["Edit(//workspace/ssp/app.html)"]
ROLES = {"duo": dict(agent="duo-medico-linguiste", model="sonnet", effort=None),
         "professeur": dict(agent="professeur-emerite", model="opus", effort="medium")}


PARETO = ("FICHE DE LECTURE, loi de Pareto : ne garde dans le corps que les 20 % d'information qui donnent 80 % de la compréhension, retire le bruit ; "
          "beaucoup de mots interactifs et de fenêtres, îlots bordurés au texte justifié ; mesure le volume avec harnais/brain/mesure_ko.py (100–298 Ko) et vérifie que le fond reste exact ; "
          "une idée par phrase complète ; du mécanisme à la clinique puis au traitement qui s'en déduit ; page aérée. ")


BRIEF_FLASH = {
    "duo": (PARETO + "COURS FLASH (harnais/etat/COURS_FLASH.md ; gabarit exact : harnais/brain/gabarit_flash.html, lu par Read) : fichier entier de 100 à 298 Ko "
            "(visé 100–200 ; > 298 Ko refusé) ; le corps ne garde que l'essentiel en phrases complètes ; le détail et le diagnostic différentiel utile "
            "passent dans des fenêtres modales (aucun bloc « Notions voisines » dans le corps) ; îlots : points 1–4 dans un <section class=\"ilot\">, "
            "5–6 dans un autre, chaque point 7–14 dans <details class=\"ilot\"> replié ; symptômes et signes d'examen cliquables (comment rechercher, manœuvre) ; "
            "syndrome cliquable ouvrant un tableau à 2 colonnes Symptômes fonctionnels | Signes physiques ; cases d'algorithme à détail ; point 11 : But, "
            "Moyens et méthodes A urgences (non-spécialiste puis service spécialisé) et B hors urgences, algorithme en cases à traits orthogonaux. "),
    "professeur": (PARETO + "COURS FLASH (harnais/etat/COURS_FLASH.md) : vérifie le fond DANS LES FENÊTRES comme dans le corps ; ne regonfle pas le volume "
                   "(> 298 Ko refusé) ; garde îlots et fenêtres du gabarit harnais/brain/gabarit_flash.html ; UNE seule tentative : le reste part "
                   "au registre (tableau .md à Vial). ")}


def opt(a, k, d):
    return type(d)(a[a.index(k) + 1]) if k in a else d


FLASH = ["--flash"]                                       # mode Cours Flash (défaut) ; vidé par --classique dans main()


def porte(f, role):
    p = subprocess.run([sys.executable, "harnais/brain/circuit_vial.py", "fin", f, "--role", role, *FLASH], capture_output=True, text=True, cwd=R, timeout=1800)
    return p.returncode == 0, (p.stdout + p.stderr).strip()


def mesure(f):
    p = subprocess.run([sys.executable, "harnais/brain/circuit_vial.py", "mesurer", f, "--json", *FLASH], capture_output=True, text=True, cwd=R, timeout=1800)
    try: return json.loads(p.stdout)
    except ValueError: return {"erreur": (p.stdout + p.stderr)[-400:]}


def appel(role, f, prompt, places, journal, passe, essai=False):
    r = ROLES[role]
    cmd = ["claude", "-p", prompt, "--agent", r["agent"], "--model", r["model"], "--output-format", "json",
           "--add-dir", str(Path(f).parent), "--allowedTools", *OUTILS, "--disallowedTools", *INTERDITS]
    if r["effort"]: cmd += ["--effort", r["effort"]]
    if essai: return dict(role=role, passe=passe, cmd=cmd[:3] + ["…"] + cmd[4:])
    with places:
        t0 = time.time()
        p = subprocess.run(cmd, capture_output=True, text=True, cwd=R, timeout=4 * 3600)
    try: d = json.loads(p.stdout)
    except ValueError: d = {"result": (p.stdout + p.stderr)[-800:], "is_error": True}
    ev = dict(role=role, passe=passe, duree_s=round(time.time() - t0), cout_usd=d.get("total_cost_usd"), tours=d.get("num_turns"),
              modeles=list((d.get("modelUsage") or {}).keys()), refus_outils=len(d.get("permission_denials") or []),
              reponse=str(d.get("result", ""))[-600:], erreur=bool(d.get("is_error")))
    with open(journal, "a", encoding="utf-8") as j: j.write(json.dumps(ev, ensure_ascii=False) + "\n")
    return ev


def etape(role, f, places, journal, boucles, essai, consigne=""):
    ok, motif, evs = False, "", []
    for k in range(boucles + 1):
        if k == 0:
            pr = (f"Leçon : {f}. Départ : {C} memoire {role} {f}{' --flash' if FLASH else ''}. " + (BRIEF_FLASH[role] if FLASH else "") + (f"Consignes de l'orchestrateur (constats d'audit à corriger en priorité) :\n{consigne}\n" if consigne else "") +
                  ("Stylise tout le cours selon la directive et gère le fond des 14 parties, POINT PAR POINT, avec `" + C + f" point {f} N` après chaque point ; "
                   f"point 10 : modèle JSON puis {C} algo {f} --appliquer ; " if role == "duo" else
                   f"{C} scanner {f} ; revue critique du fond, point par point, et corrections ; ") + f"fin : {C} fin {f} --role {role} jusqu'à ACCEPTÉ. Une ligne de réponse.")
        else:
            pr = (f"REPRISE {k}/{boucles} de la leçon {f} (instantané conservé : {C} memoire {role} {f} --garder{' --flash' if FLASH else ''}). La porte unique a REFUSÉ :\n{motif[-2500:]}\n"
                  f"Corrige chaque motif point par point (`{C} point {f} N` après chaque point), sans rien retrancher de sourcé ; "
                  f"fin : {C} fin {f} --role {role} jusqu'à ACCEPTÉ. Une ligne de réponse.")
        evs.append(appel(role, f, pr, places, journal, k, essai))
        if essai: return True, "", evs
        ok, motif = porte(f, role)
        with open(journal, "a", encoding="utf-8") as j: j.write(json.dumps(dict(role=role, passe=k, porte="ACCEPTÉ" if ok else "REFUSÉ", sortie=motif[-1500:]), ensure_ascii=False) + "\n")
        if ok: break
    return ok, motif, evs


def notifier(jd, f, role, motif):
    """Refus notifié (console + notifications.md du journal) ; la leçon continue vers l'étape suivante, jamais d'arrêt sec."""
    msg = f"REFUS notifié · {Path(f).name} · {role} : correction à l'étape suivante, le fichier progresse.\n{motif[-600:]}"
    print(msg, file=sys.stderr)
    with open(jd / "notifications.md", "a", encoding="utf-8") as n: n.write(f"- {time.strftime('%H:%M:%S')} {msg}\n")


def lecon(f, P, a):
    jd = Path(opt(a, "--journal", str(R / ".cache/brain/circuit/lancer"))); jd.mkdir(parents=True, exist_ok=True)
    journal = jd / (Path(f).name + ".jsonl"); essai = "--dry-run" in a
    res = dict(lecon=f, avant=None if essai else mesure(f), etapes={})
    for role in opt(a, "--etapes", "duo,professeur").split(","):
        cs = Path(opt(a, "--consigne", "")).read_text(encoding="utf-8")[:16000] if "--consigne" in a else ""
        if role == "professeur" and not essai:                  # bon de travail unique du professeur : le registre portable des fautes
            rj, rm = jd / (Path(f).stem + ".registre.json"), jd / (Path(f).stem + ".registre.md")
            subprocess.run([sys.executable, "harnais/brain/circuit_vial.py", "registre", f, "--json", str(rj), "--md", str(rm), *FLASH], capture_output=True, cwd=R, timeout=1800)
            cs = (cs + "\n" if cs else "") + f"BON DE TRAVAIL (registre portable des fautes, à traiter ligne par ligne) : {rm}"
        ok, motif, evs = etape(role, f, P[ROLES[role]["model"]], journal, opt(a, "--boucles", 1 if role == "duo" else 0), essai, cs)
        res["etapes"][role] = dict(accepte=ok, appels=evs, motif=motif[-800:])
        if not ok and not essai:                              # ordre de Vial : jamais de refus sec = refus NOTIFIÉ + correction, le fichier progresse
            notifier(jd, f, role, motif)
    res["apres"] = None if essai else mesure(f)
    if not essai:                                             # UNE seule correction : les fautes restantes partent en tableau à Vial (autres moyens)
        rj, rm, hc = jd / (Path(f).stem + ".restantes.json"), jd / (Path(f).stem + ".restantes.md"), jd / (Path(f).stem + ".controle.html")
        subprocess.run([sys.executable, "harnais/brain/circuit_vial.py", "registre", f, "--json", str(rj), "--md", str(rm), "--marquer", str(hc), *FLASH], capture_output=True, cwd=R, timeout=1800)
        res["restantes"] = dict(tableau=str(rm), registre=str(rj), controle=str(hc))
    return res


def main(a):
    fs = [str(Path(x).resolve()) for x in a if x.endswith(".html")]
    if not fs or "-h" in a or "--help" in a: print(__doc__); return 0
    if "--classique" in a: FLASH.clear()
    if len(fs) > 16: print(f"# {len(fs) - 16} leçon(s) au-delà de 16 : vague suivante", file=sys.stderr); fs = fs[:16]
    P = {"sonnet": threading.BoundedSemaphore(opt(a, "--sonnet", 16)), "opus": threading.BoundedSemaphore(opt(a, "--opus", 12))}
    with ThreadPoolExecutor(len(fs)) as ex: res = list(ex.map(lambda f: lecon(f, P, a), fs))
    jd = Path(opt(a, "--journal", str(R / ".cache/brain/circuit/lancer"))); (jd / "bilan.json").write_text(json.dumps(res, ensure_ascii=False, indent=1))
    for r in res:
        print(f"{Path(r['lecon']).name} : " + " → ".join(f"{k} {'ACCEPTÉ' if v['accepte'] else 'REFUSÉ'} ({len(v['appels'])} appel(s))" for k, v in r["etapes"].items()))
    return 0 if all(v["accepte"] for r in res for v in r["etapes"].values()) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
