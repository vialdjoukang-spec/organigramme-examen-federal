#!/usr/bin/env python3
"""BRAIN-HARNESS · réseau : registre des 160 scriptones, écrivains et zones, chaîne de correction à point fixe (stdlib seule).
  registre()            catalogue (registre.json, écrit par outils/gabarit.py)
  module(id)            importe un scriptone (transversal, alpha/, beta/)
  ecrivains()           [(id, zones)] dans l'ORDRE canonique ; un seul écrivain par zone (vérifié par conflits_statiques)
  corriger_tout(t)      applique tous les écrivains jusqu'au point fixe (4 tours au plus) : corrections confluentes et idempotentes
  analyser(ids, t, nom) exécute des scriptones sous contrat, avec disjoncteur (exception, contrat rompu, lenteur) et ré-routage vers le jumeau
Règle anti-conflit : chaque zone d'un fichier a UN écrivain ; tous les autres scriptones émettent des doléances sur le bus."""
import functools, importlib.util, json, sys, time
from pathlib import Path
D = Path(__file__).resolve().parent
if str(D) not in sys.path: sys.path.insert(0, str(D))
import bus

# ordre canonique des écrivains : structure avant contenu, contenu avant typographie, typographie avant rendu (police en dernier)
ORDRE = ["s5_arbre", "s8_tableaux"] + [f"a{n:02d}_S" for n in range(1, 15)] + [f"a{n:02d}_R" for n in range(1, 15)] + ["a02_Q"] + \
        [f"b{n:02d}_C" for n in range(1, 15)] + [f"b{n:02d}_L" for n in range(1, 15)] + ["s3_concision", "s2_rythme", "s6_barre14", "s1_police"]


@functools.lru_cache(maxsize=1)
def registre():
    return json.loads((D / "registre.json").read_text(encoding="utf-8"))


def entree(i):
    return next((e for e in registre()["scriptones"] if e["id"] == i), None)


@functools.lru_cache(maxsize=256)
def module(i):
    e = entree(i)
    if e is None or e.get("langage", "python") != "python": raise KeyError(f"scriptone inconnu ou non Python : {i}")
    p = D / e["fichier"]
    spec = importlib.util.spec_from_file_location(f"brain_{i}", p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def ecrivains():
    return [(i, entree(i)["ecrit"]) for i in ORDRE if entree(i) and entree(i)["ecrit"]]


def conflits_statiques(reg=None):
    """Zones revendiquées par plus d'un écrivain (doit être vide : preuve statique de l'absence de conflit d'écriture)."""
    z = {}
    for e in (reg or registre())["scriptones"]:
        for x in e.get("ecrit", []): z.setdefault(x, []).append(e["id"])
    return {k: v for k, v in z.items() if len(v) > 1}


def corriger_tout(t, ordre=None, max_tours=4, convertir=None, sauf=()):
    """Écrivains appliqués dans l'ordre jusqu'au point fixe ; renvoie (texte, tours). `convertir` : fonction appelée après s5_arbre."""
    ids = [i for i, _ in ecrivains()] if ordre is None else ordre
    for tour in range(1, max_tours + 1):
        avant = t
        for i in ids:
            if i in sauf: continue
            t = module(i).corriger(t, {})
            if i == "s5_arbre" and convertir: t = convertir(t)
        if t == avant: return t, tour
    return t, max_tours


# ───────────────────────── exécution protégée : disjoncteur, ré-routage, repli ─────────────────────────
class Disjoncteur:
    """Disjoncteur par scriptone : ouvert après `seuil` pannes (exception, contrat rompu, lenteur). Ouvert = le scriptone n'est plus appelé ;
    son jumeau (autre zone, autre méthode) couvre la même exigence ; sans jumeau, escalade (le fichier ne sort pas sans relecture)."""
    def __init__(self, seuil=1, budget_ms=4000):
        self.seuil, self.budget_ms, self.pannes, self.ouverts, self.journal = seuil, budget_ms, {}, set(), []

    def noter(self, i, nature, detail=""):
        self.pannes[i] = self.pannes.get(i, 0) + 1; self.journal.append(dict(id=i, nature=nature, detail=str(detail)[:200]))
        if self.pannes[i] >= self.seuil: self.ouverts.add(i)


def jumeau(i):
    e = entree(i); return e.get("jumeau") if e else None


def executer_protege(i, t, nom, dj, pannes=None, opt=None):
    """Exécute le scriptone i sous contrat ; une panne (injectée ou réelle) ouvre son disjoncteur et ré-route vers son jumeau.
    Renvoie (sortie | None, id effectivement exécuté, nature de la panne | None)."""
    pannes = pannes or {}
    if i in dj.ouverts:
        j = jumeau(i)
        if j and j not in dj.ouverts:
            s, _, _ = executer_protege(j, t, nom, dj, pannes, opt); return s, j, "ouvert"
        return None, None, "ouvert"
    t0 = time.perf_counter(); nature = None
    try:
        m = module(i)
        if pannes.get(i) == "exception": raise RuntimeError("panne injectée")
        s = bus.executer(m, nom, html=t, options=opt or {}, ecrire=False)
        if pannes.get(i) == "contrat": s = dict(s); s.pop("doleances")
        if bus.valider(s): nature = "contrat"
        elif s.get("panne"): nature = "exception"
        elif pannes.get(i) == "lenteur" or 1000 * (time.perf_counter() - t0) > dj.budget_ms: nature = "lenteur"
    except SystemExit as e: nature, s = "alteration", None
    except Exception as e: nature, s = "exception", None
    if nature is None: return s, i, None
    dj.noter(i, nature)
    if nature == "lenteur": return s, i, "lenteur"          # le résultat reste valable ; les fichiers suivants passent par le jumeau
    j = jumeau(i)
    if j and j not in dj.ouverts:
        s2, _, _ = executer_protege(j, t, nom, dj, pannes, opt); return s2, j, nature
    return None, None, nature
