"""Chargement et validation de la configuration d'un agent (JSON, bibliothèque standard).
v1.4 (organisation à 8 agents, 2 équipes) : champs facultatifs `equipe`, `chapitre`, `lots`, `parties_autorisees`,
`dossier_travail`. Une configuration sans ces champs se comporte exactement comme en v1.3 (rétrocompatible)."""
import json, os, re
from pathlib import Path

ICI = Path(__file__).resolve().parent
DEFAUTS = {
    "lots_root": None,
    "user_agent": "scripts_lots/1.3 (projet organigramme-examen-federal; lecture de sources publiques)",
    "enforce_os_readonly": False,
    "languagetool": {"url": "https://api.languagetool.org/v2/check", "language": "fr-CH", "enabled": True,
                     "budget_req_per_min": 10, "budget_bytes_per_min": 60000, "max_bytes_per_request": 18000,
                     "debounce_s": 60, "timeout_s": 20, "max_requests_per_pass": 4},
    "pubmed": {"mcp_url": "http://127.0.0.1:3010/mcp", "eutils_base": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils",
               "rate_per_s_without_key": 3, "rate_per_s_with_key": 10},
    "http": {"per_domain_per_s": 1.0, "timeout_s": 15, "max_workers": 8,
             "ttl_s": {"1": 604800, "2": 86400, "3": 86400, "4": 86400, "5": 604800}},
    "compteur": {},
}
TYPES = {"int": int, "str": str, "bool": bool, "dict": dict, "list": list}
PARTIES = ("A", "P1", "P2", "P3", "P4")
RE_PARTIE_A = re.compile(r"_Appel_A_", re.I)
RE_PARTIE_B = re.compile(r"_Appel_B_.*?Partie_([1-4])", re.I)
# Numéro de LOT avec ou sans zéros de tête (LOT_1 ≡ LOT_01 ≡ LOT_001) ; 1 à 3 chiffres significatifs, jamais un 4e chiffre.
RE_NUM = re.compile(r"LOT_0*(\d{1,3})(?!\d)")

class ConfigErreur(Exception):
    pass

def _verifier_type(nom, val, spec):
    ok = any((t == "null" and val is None) or (t in TYPES and isinstance(val, TYPES[t]) and not (t == "int" and isinstance(val, bool)))
             for t in spec.split("|"))
    if not ok:
        raise ConfigErreur(f"champ {nom} : type attendu {spec}")

def charger(chemin):
    schema = json.loads((ICI / "config_schema.json").read_text("utf-8"))
    brut = json.loads(Path(chemin).read_text("utf-8"))
    for nom, spec in schema["required"].items():
        if nom not in brut:
            raise ConfigErreur(f"champ obligatoire absent : {nom}")
        _verifier_type(nom, brut[nom], spec)
    for nom, val in brut.items():
        if nom.startswith("_"):
            continue
        spec = schema["required"].get(nom) or schema["optional"].get(nom)
        if spec is None:
            raise ConfigErreur(f"champ inconnu : {nom}")
        _verifier_type(nom, val, spec)
    cfg = json.loads(json.dumps(DEFAUTS))
    for k, v in brut.items():
        if isinstance(v, dict) and isinstance(cfg.get(k), dict):
            cfg[k].update(v)
        else:
            cfg[k] = v
    if not cfg["lot_min"] <= cfg["lot_max"]:
        raise ConfigErreur("lot_min > lot_max")
    for k in ("cache_dir", "output_dir", "shared_state_dir", "prompt_path", "lots_root"):
        if cfg.get(k):
            cfg[k] = str(Path(os.path.expanduser(os.path.expandvars(cfg[k]))).resolve())
    if len({cfg["cache_dir"], cfg["output_dir"], cfg["shared_state_dir"]}) != 3:
        raise ConfigErreur("cache_dir, output_dir et shared_state_dir doivent être distincts")
    if cfg.get("compteur", {}).get("csv"):
        cfg["compteur"]["csv"] = str(Path(os.path.expanduser(os.path.expandvars(cfg["compteur"]["csv"]))).resolve())
    _valider_perimetre(cfg)
    if "equipe" in cfg:
        _valider_independance(cfg)
    cfg["_chemin"] = str(Path(chemin).resolve())
    return cfg

def _valider_perimetre(cfg):
    if "lots" in cfg:
        if not cfg["lots"] or not all(isinstance(x, int) and not isinstance(x, bool) for x in cfg["lots"]):
            raise ConfigErreur("lots : liste non vide d'entiers attendue")
        if any(not cfg["lot_min"] <= x <= cfg["lot_max"] for x in cfg["lots"]):
            raise ConfigErreur("lots : chaque LOT doit être compris entre lot_min et lot_max")
    pa = cfg.get("parties_autorisees")
    if pa is None:
        return
    listes = [pa] if isinstance(pa, list) else list(pa.values())
    for l in listes:
        if not isinstance(l, list) or not l or any(x not in PARTIES for x in l):
            raise ConfigErreur(f"parties_autorisees : listes non vides de {', '.join(PARTIES)} attendues")
    if isinstance(pa, dict):
        for k in pa:
            if k != "*" and not re.fullmatch(r"(LOT_)?\d{1,3}", k):
                raise ConfigErreur(f"parties_autorisees : clé invalide {k!r} (attendu « 227 », « LOT_227 », « 1 », « 001 » ou « * »)")
    if "dossier_travail" in cfg:
        d = cfg["dossier_travail"]; d = [d] if isinstance(d, str) else d
        if not d or not all(isinstance(x, str) and x for x in d):
            raise ConfigErreur("dossier_travail : chemin ou liste de chemins attendu")

def chemins_inscriptibles(cfg):
    """Tous les chemins où les scripts de cet agent écrivent (état, cache, sorties, compteur)."""
    ch = {"cache_dir": cfg["cache_dir"], "output_dir": cfg["output_dir"], "shared_state_dir": cfg["shared_state_dir"]}
    if cfg.get("compteur", {}).get("csv"):
        ch["compteur.csv"] = cfg["compteur"]["csv"]
    return ch

def _valider_independance(cfg):
    """Loi d'indépendance absolue : aucun chemin inscriptible commun, aucun dossier « partage »."""
    marque = f"agent_{cfg['agent']}"
    for nom, ch in chemins_inscriptibles(cfg).items():
        parts = Path(ch).parts
        if marque not in parts:
            raise ConfigErreur(f"indépendance : {nom} ({ch}) doit être sous un dossier {marque}/ propre à l'agent")
        if "partage" in parts:
            raise ConfigErreur(f"indépendance : {nom} ({ch}) ne doit pas utiliser un dossier partagé")

def lots_autorises(cfg):
    return list(cfg["lots"]) if cfg.get("lots") else list(range(cfg["lot_min"], cfg["lot_max"] + 1))

def plages(lots):
    """« LOT_218–110, LOT_227–229 » : plages contiguës (pas de ±1) dans l'ordre de la liste."""
    res, i = [], 0
    while i < len(lots):
        j = i
        pas = lots[i + 1] - lots[i] if i + 1 < len(lots) and abs(lots[i + 1] - lots[i]) == 1 else 0
        while pas and j + 1 < len(lots) and lots[j + 1] - lots[j] == pas:
            j += 1
        res.append(f"LOT_{lots[i]}" if i == j else f"LOT_{lots[i]}–{lots[j]}"); i = j + 1
    return ", ".join(res)

def lot_autorise(cfg, numero):
    n = int(numero)
    if not cfg["lot_min"] <= n <= cfg["lot_max"]:
        return False
    return n in cfg["lots"] if cfg.get("lots") else True

def partie_de(chemin):
    """« A » (Appel A), « P1 »…« P4 » (Appel B, Partie N) ou None si le nom n'est pas reconnu."""
    nom = Path(chemin).name
    if RE_PARTIE_A.search(nom):
        return "A"
    m = RE_PARTIE_B.search(nom)
    return f"P{m.group(1)}" if m else None

def parties_pour(cfg, numero):
    pa = cfg.get("parties_autorisees")
    if pa is None:
        return list(PARTIES)
    if isinstance(pa, list):
        return list(pa)
    n = int(numero)
    for k in (str(n), f"{n:03d}", f"LOT_{n}", f"LOT_{n:03d}"):
        if k in pa:
            return list(pa[k])
    return list(pa.get("*", []))

def _dans(chemin, dossier):
    a, b = os.path.realpath(chemin), os.path.realpath(os.path.expanduser(dossier))
    return os.path.commonpath([a, b]) == b

def fichier_autorise(cfg, chemin, numero=None):
    """(True, "") si le fichier est dans le périmètre de l'agent (LOT, Partie, dossier de travail), sinon (False, raison)."""
    if numero is None:
        m = RE_NUM.search(Path(chemin).name) or RE_NUM.search(str(Path(chemin).parent))
        numero = int(m.group(1)) if m else None
    qui = f"l'agent {cfg['agent']}" + (f" (équipe {cfg['equipe']}, {cfg['chapitre']})" if cfg.get("equipe") and cfg.get("chapitre") else "")
    if numero is None or not lot_autorise(cfg, numero):
        lots = lots_autorises(cfg)
        return False, f"{Path(chemin).name} : LOT hors de la série de {qui} ({plages(lots)})"
    if cfg.get("parties_autorisees") is not None:
        p = partie_de(chemin); ok = parties_pour(cfg, numero)
        if p is None:
            return False, f"{Path(chemin).name} : nom de fichier non reconnu (Appel A ou Appel B Partie 1–4 attendu) pour {qui}"
        if p not in ok:
            return False, f"{Path(chemin).name} : {p} de LOT_{numero} hors du chapitre de {qui} (autorisé : {', '.join(ok) or 'aucun'})"
    if cfg.get("dossier_travail"):
        d = cfg["dossier_travail"]; d = [d] if isinstance(d, str) else d
        if not any(_dans(chemin, x) for x in d):
            return False, f"{Path(chemin).name} : hors du dossier de travail de {qui} ({', '.join(d)})"
    return True, ""
