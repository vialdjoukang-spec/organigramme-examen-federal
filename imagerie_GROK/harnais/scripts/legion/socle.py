"""Chemins, état reprenable, journal. Le journal ne reçoit aucun identifiant patient."""
import hashlib, json, os, re, time

ICI = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.dirname(ICI)
ROOT = os.path.dirname(SCRIPTS)
LEGION = os.path.join(ROOT, "legion")
ETAT = os.path.join(LEGION, "etat")
RAPPORTS = os.path.join(LEGION, "rapports")
JOURNAL = os.path.join(LEGION, "journaux", "legion.jsonl")
TRAVAIL = os.path.join(LEGION, "travail")
ENTRANT = os.path.join(ROOT, "entrant")
CONFIG = os.path.join(ROOT, "config", "interface.json")
FILE = os.path.join(ROOT, "config", "file_a_interpreter.json")
MANIFEST = os.path.join(ROOT, "manifest")
DEMO = os.path.join(LEGION, "demo")
VERSION = "1"

for d in (ETAT, RAPPORTS, os.path.dirname(JOURNAL), TRAVAIL, ENTRANT, os.path.dirname(CONFIG), DEMO):
    os.makedirs(d, exist_ok=True)


def ecrire_json(path, obj):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.replace(tmp, path)


def lire_json(path, defaut=None):
    if not os.path.isfile(path):
        return defaut
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def cle(*parts):
    brut = json.dumps(parts, ensure_ascii=False, sort_keys=True, default=str)
    return hashlib.sha256(brut.encode()).hexdigest()[:16]


def _propre(cle_nom, valeur):
    if cle_nom in ("source_url", "license_url", "requete", "fichier", "id"):
        return valeur
    if isinstance(valeur, str) and re.search(r"\b\d{6,}\b", valeur):
        return re.sub(r"\b\d{6,}\b", "[effacé]", valeur)
    return valeur


def journal(evt, **champs):
    interdit = {"caption", "texte", "ocr", "legend", "extrait_brut"}
    ligne = {"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "evt": evt}
    for k, v in champs.items():
        if k in interdit:
            continue
        ligne[k] = _propre(k, v)
    with open(JOURNAL, "a", encoding="utf-8") as f:
        f.write(json.dumps(ligne, ensure_ascii=False) + "\n")


def chemin_etat(mid):
    return os.path.join(ETAT, mid + ".json")


def charger(mid):
    etat = lire_json(chemin_etat(mid), {})
    etat.setdefault("id", mid)
    etat.setdefault("refus", [])
    etat.setdefault("acceptes", [])
    return etat


def sauver(etat):
    ecrire_json(chemin_etat(etat["id"]), etat)


def manifeste(mid):
    p = os.path.join(MANIFEST, mid + ".json")
    if not os.path.isfile(p):
        return None, p
    return lire_json(p), p


def diagnostics():
    return {d["id"]: d for d in lire_json(os.path.join(ROOT, "diagnostics.json"), [])}


def introuvables():
    """Inventaire : manifestes au statut introuvable, ordre d'identifiant décroissant."""
    out = []
    for nom in os.listdir(MANIFEST):
        if not nom.endswith(".json") or nom == "SCHEMA.json" or nom.startswith("TEST-"):
            continue
        m = lire_json(os.path.join(MANIFEST, nom), {})
        if m.get("statut") == "introuvable" and m.get("id"):
            out.append(m)
    out.sort(key=lambda m: m["id"], reverse=True)
    return out


def choisir(n=10):
    """Introuvables qui ont déjà une requête Commons, Open-i ou Europe PMC."""
    pris = []
    for m in introuvables():
        blob = " ".join(m.get("queries") or []).lower()
        if any(k in blob for k in ("commons", "openi", "europe", "pmc")):
            pris.append(m["id"])
        if len(pris) >= n:
            break
    return pris


def ajouter_requete(mid, texte):
    m, p = manifeste(mid)
    if not m or not texte or texte in (m.get("queries") or []):
        return False
    m.setdefault("queries", []).append(texte)
    ecrire_json(p, m)
    return True
