#!/usr/bin/env python3
"""BRAIN-HARNESS · orchestre : le circuit complet d'un cours, de la collecte à la sortie, avec journal de circulation (gratuit, hors ligne).
  python3 harnais/brain/orchestre.py passer <fichier> [--appliquer] [--journal F] [--json]
  python3 harnais/brain/orchestre.py lot <fichier…> [--paralleles 16] [--journal F]     jusqu'à 16 cours simultanés (un processus par cours)
Circuit : 0 harnais externe de collecte (s11 : garde l'entrée, 14 paquets) → gardien (empreintes)
          → zone α en zigzag (α1…α14, 5 familles chacune) + scriptones transversaux de forme et de mémoire
          → écrivains (un par zone) jusqu'au point fixe → 5 nœuds Sonnet (briefs par territoire, jetons comptés)
          → zone β en zigzag (β1…β14, indépendante d'α) → nœud de vote α/β → 5 nœuds Opus (briefs par domaine)
          → économie (jetons par étage) → sortie (seuls les cours sans faute grave ouverte sortent).
Les agents ne sont pas appelés ici : l'orchestre prépare leur entrée minimale et la mesure. Le journal (evenements.jsonl) est rejoué par BRAIN_3D.html."""
import json, os, re, sys, time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
B = Path(__file__).resolve().parent
R = B.parents[1]
sys.path[:0] = [str(B / "scriptones"), str(R / "harnais")]
import bus, reseau, familles as F

SONNET = {1: "S1", 2: "S1", 3: "S1", 4: "S2", 5: "S2", 6: "S2", 7: "S3", 8: "S3", 9: "S3", 10: "S4", 11: "S4", 12: "S5", 13: "S5", 14: "S5"}
OPUS = {"medical": "O1", "doleance": "O2", "memoire": "O2", "langue": "O4", "forme": "O5", "jetons": "O5"}
OPUS_POINT = {2: "O2", 12: "O2", 3: "O1", 8: "O1", 11: "O1", 4: "O3", 5: "O3", 6: "O3", 7: "O3", 9: "O3", 10: "O3"}
RENDU = ["s1_police", "s2_rythme", "s6_barre14", "s20_ancres"]
TRANS = ["s3_concision", "s4_budget", "s5_arbre", "s8_tableaux", "s9_sources", "s10_memoire"]
JOURNAL = R / ".cache/brain/evenements.jsonl"


def vue(t):
    if "<!-- FORME_INTERACTIVE -->" in t: return t
    try:
        import forme_interactive as FI
        return FI.convert(t)
    except Exception:
        return t


class Journal:
    def __init__(self, chemin, run, fichier):
        self.chemin, self.run, self.fichier, self.seq, self.n = chemin, run, fichier, 0, 0

    def ev(self, type_, de, vers, **kw):
        if self.chemin is None: self.n += 1; return
        e = dict(run=self.run, seq=self.seq, type=type_, de=de, vers=vers, fichier=self.fichier, **{k: v for k, v in kw.items() if v is not None})
        bus.evenement(e, self.chemin); self.seq += 1; self.n += 1


def point_de(d):
    m = re.search(r"point (\d{1,2})", d["constat"]) or re.search(r"\b[ab](\d\d)_", d["scriptone"])
    return int(m.group(1)) if m else None


def signal_de(d):
    e = reseau.entree(d["scriptone"]); return e["signal"] if e else "doleance"


def passer(chemin=None, html=None, nom=None, journal=JOURNAL, appliquer=False, pannes=None, historique=None):
    """Un passage complet ; renvoie le rapport (dict). Ne modifie le fichier que si appliquer=True (verrou + écriture atomique)."""
    t0 = time.perf_counter()
    if html is None: html, enc = bus.lire(chemin)
    nom = nom or (Path(chemin).name if chemin else "<entrée>")
    run = f"{nom}#{bus.sha(html)[:8]}"; J = Journal(journal, run, nom); dj = reseau.Disjoncteur(); rap = dict(fichier=nom, run=run, etapes={})
    def lancer(i, t, etape):
        s, eff, nature = reseau.executer_protege(i, t, nom, dj, pannes)
        if nature: J.ev("doleance", i, "GARD", code="Z1" if eff else "Z2", severite="GRAVE" if eff else "CRITIQUE", msg=f"panne {nature} → {eff or 'escalade'}")
        return s["doleances"] if s else []
    # 0 · harnais externe de collecte
    s = bus.executer(reseau.module("s11_collecteur"), nom, html=html, ecrire=False); P = s["mesures"].get("paquets", {})
    J.ev("forme", "EXT", "EXT", msg=f"collecte : {len(P)} paquets", jetons=bus.estime_jetons(html))
    for n, p in sorted(P.items(), key=lambda x: int(x[0])):
        J.ev("medical", "EXT", f"α{n}", point=int(n), jetons=p["jetons"], msg=f"paquet {p['titre'][:40]}")
    entree = s["doleances"]; rap["etapes"]["collecte"] = dict(doleances=len(entree), paquets=len(P))
    if any(d["severite"] == "CRITIQUE" for d in entree):
        for d in entree: J.ev("doleance", "EXT", "SORTIE", code=d["code"], severite=d["severite"], msg=d["constat"][:120])
        rap.update(verdict="refusé à l'entrée", doleances=entree, duree_s=round(time.perf_counter() - t0, 2)); return rap
    # gardien
    alt = bus.verifier_empreintes()
    J.ev("doleance", "GARD", "BUS", msg="empreintes intactes" if not alt else f"ALTÉRATION : {alt[:3]}", severite=None if not alt else "CRITIQUE")
    if alt:
        rap.update(verdict="arrêt : scriptone altéré", alterations=alt); return rap
    # zone α en zigzag + transversaux
    v = vue(html); DA = []
    for i in RENDU: DA += lancer(i, v, "alpha")
    for i in TRANS: DA += lancer(i, html, "alpha")
    for d in DA:
        n = point_de(d); J.ev(signal_de(d), "MEM" if d["scriptone"] == "s10_memoire" else "GLIE", f"α{n}" if n else "BUS", point=n, code=d["code"], severite=d["severite"], msg=d["constat"][:100])
    for n in range(1, 15):
        for f in F.FAM_A:
            for d in lancer(F.ident("A", f, n).ID, html, "alpha"):
                DA.append(d); J.ev(signal_de(d), f"α{n}", "BUS", point=n, code=d["code"], severite=d["severite"], msg=d["constat"][:100])
        if n < 14: J.ev("forme", f"α{n}", f"α{n + 1}", point=n, msg="relais en zigzag")
    rap["etapes"]["alpha"] = dict(doleances=len(DA), script=sum(d["executant"] == "script" for d in DA))
    # écrivains (un par zone) jusqu'au point fixe
    t1, tours = reseau.corriger_tout(html)
    J.ev("forme", "BUS", "PRO", msg=f"corrections par script : {len(html) - len(t1):+d} car., point fixe en {tours} tour(s)")
    if appliquer and chemin and t1 != html:
        with bus.verrou(chemin):
            if bus.sha(bus.lire(chemin)[0]) != bus.sha(html): raise bus.Occupe("fichier modifié pendant le passage")
            bus.ecrire_atomique(chemin, t1)
    # 5 nœuds Sonnet : briefs par territoire (doléances α restantes après les scripts)
    S17 = reseau.module("s17_brief"); DA1 = []
    for i in RENDU: DA1 += lancer(i, vue(t1), "alpha2")
    for i in TRANS + [F.ident("A", f, n).ID for n in range(1, 15) for f in F.FAM_A]: DA1 += lancer(i, t1, "alpha2")
    ag_a = [d for d in DA1 if d["executant"] == "agent"]; briefs = {}
    for k in ("S1", "S2", "S3", "S4", "S5"):
        sous = [d for d in ag_a if SONNET.get(point_de(d) or 0) == k or (point_de(d) is None and k == "S1")]
        b = S17.compiler(t1, nom, sous); briefs[k] = bus.estime_jetons(b) + sum(P.get(str(n), P.get(n, {})).get("jetons", 0) for n in {point_de(d) for d in sous} if n)
        J.ev("jetons", "BUS", k, jetons=briefs[k], msg=f"{len(sous)} doléances [agent]")
    # zone β en zigzag (indépendante : autre méthode, sur le texte corrigé)
    DB = []
    for n in range(1, 15):
        for f in F.FAM_B:
            for d in lancer(F.ident("B", f, n).ID, t1, "beta"):
                DB.append(d); J.ev(signal_de(d), f"β{n}", "BUS", point=n, code=d["code"], severite=d["severite"], msg=d["constat"][:100])
        if n < 14: J.ev("forme", f"β{n}", f"β{n + 1}", point=n, msg="relais en zigzag")
        J.ev("medical", f"S{SONNET[n][1]}", f"β{n}", point=n, msg="paquet relu transmis")
    rap["etapes"]["beta"] = dict(doleances=len(DB))
    # vote α/β puis 5 nœuds Opus
    vote = bus.executer(reseau.module("s18_vote"), nom, html=t1, ecrire=False); route = vote["mesures"].get("routage", {})
    for n, o in route.items(): J.ev("doleance", "VOTE", o[:2], point=int(n), msg=f"désaccord α/β au point {n}")
    ag_b = [d for d in DB if d["executant"] == "agent"]; opus = {}; nopus = {}
    for k in ("O1", "O2", "O3", "O4", "O5"):
        sous = [d for d in ag_b if (OPUS_POINT.get(point_de(d) or 0) or OPUS.get(signal_de(d), "O5")) == k]
        b = S17.compiler(t1, nom, sous); opus[k] = bus.estime_jetons(b) + sum(P.get(str(n), P.get(n, {})).get("jetons", 0) for n in {point_de(d) for d in sous} if n)
        J.ev("jetons", "BUS", k, jetons=opus[k], msg=f"{len(sous)} doléances [agent]"); nopus[k] = len(sous)
    # mémoire : historique des passages (stagnation)
    ids = sorted({d["id"] for d in DA1 + DB if d["executant"] == "agent"}); hist = list(historique or [])
    memf = R / ".cache/brain/memoire" / (re.sub(r"[^\w.-]", "_", nom) + ".json")
    if historique is None and journal is not None:
        try: hist = json.loads(memf.read_text())["passages"]
        except (OSError, ValueError, KeyError): hist = []
    stagne = bool(hist) and set(hist[-1]) == set(ids) and bool(ids)
    J.ev("memoire", "BUS", "MEM", msg=f"{len(ids)} doléances ouvertes" + (" · STAGNATION : fichier bloqué" if stagne else ""))
    if journal is not None:
        try:
            memf.parent.mkdir(parents=True, exist_ok=True); bus.ecrire_atomique(memf, json.dumps(dict(fichier=nom, passages=(hist + [ids])[-5:]), ensure_ascii=False))
        except OSError: pass
    # économie et sortie
    base = bus.estime_jetons(html)
    graves = [d for d in DA1 + DB if d["severite"] in ("CRITIQUE", "GRAVE")]
    verdict = "bloqué (stagnation)" if stagne else ("sortie : audité" if not graves else f"retour aux nœuds : {len(graves)} faute(s) grave(s) ouverte(s)")
    for k, x in nopus.items(): J.ev("medical", k, "SORTIE", msg=f"avis de domaine : {x} doléance(s) [agent] à trancher" if x else "avis de domaine : rien à trancher")
    J.ev("jetons", "ECO", "SORTIE", jetons=sum(briefs.values()) + sum(opus.values()), msg=f"relecture intégrale {base} jetons par nœud")
    J.ev("doleance", "BUS", "SORTIE", msg=verdict)
    compte = lambda L: dict(sorted({c: sum(d["code"] == c for d in L) for c in {d["code"] for d in L}}.items()))
    rap.update(verdict=verdict, octets=len(html.encode("utf-8", "surrogatepass")), corrections_script=t1 != html, tours_point_fixe=tours,
               doleances_alpha_avant=compte(DA), doleances_alpha_apres=compte(DA1), doleances_beta=compte(DB), routage_vote=route,
               jetons=dict(relecture_integrale_par_noeud=base, base_10_noeuds=10 * base, briefs_sonnet=briefs, briefs_opus=opus,
                           total_briefs=sum(briefs.values()) + sum(opus.values())),
               pannes=dj.journal, evenements=J.n, duree_s=round(time.perf_counter() - t0, 2))
    rap["jetons"]["reduction_pct"] = round(100 * (1 - rap["jetons"]["total_briefs"] / max(1, rap["jetons"]["base_10_noeuds"])), 2)
    return rap


def _un(args):
    chemin, journal, appliquer = args
    try: return passer(chemin, journal=Path(journal) if journal else None, appliquer=appliquer)
    except Exception as e: return dict(fichier=Path(chemin).name, verdict=f"panne : {type(e).__name__} : {e}")


def lot(chemins, paralleles=16, journal=JOURNAL, appliquer=False):
    """Jusqu'à 16 cours simultanés : un processus par cours ; journal sous flock ; un verrou par fichier écrit."""
    out = []
    with ProcessPoolExecutor(max_workers=min(paralleles, 16, max(1, len(chemins)))) as ex:
        for f in as_completed([ex.submit(_un, (str(c), str(journal) if journal else None, appliquer)) for c in chemins]): out.append(f.result())
    return sorted(out, key=lambda r: r["fichier"])


def main(a):
    if not a or a[0] in ("-h", "--help"): print(__doc__); return 0
    j = Path(a[a.index("--journal") + 1]) if "--journal" in a else JOURNAL
    fichiers = [x for x in a[1:] if not x.startswith("--") and (len(a) < 2 or x != (a[a.index("--journal") + 1] if "--journal" in a else None))
                and not (("--paralleles" in a) and x == a[a.index("--paralleles") + 1])]
    if a[0] == "passer":
        if not fichiers or not Path(fichiers[0]).exists(): print("INTROUVABLE"); return 2
        r = passer(fichiers[0], journal=j, appliquer="--appliquer" in a)
        if "--json" in a: print(json.dumps(r, ensure_ascii=False, indent=1))
        else:
            print(f"{r['fichier']} · {r['verdict']} · α {sum(r.get('doleances_alpha_avant', {}).values())} → {sum(r.get('doleances_alpha_apres', {}).values())} · β {sum(r.get('doleances_beta', {}).values())}"
                  f" · jetons : briefs {r.get('jetons', {}).get('total_briefs')} contre {r.get('jetons', {}).get('base_10_noeuds')} ({r.get('jetons', {}).get('reduction_pct')} %) · {r.get('duree_s')} s")
        return 0
    if a[0] == "lot":
        p = int(a[a.index("--paralleles") + 1]) if "--paralleles" in a else 16
        for r in lot(fichiers, p, j, "--appliquer" in a): print(f"{r['fichier']} · {r['verdict']} · {r.get('duree_s', '?')} s")
        return 0
    print(__doc__); return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
