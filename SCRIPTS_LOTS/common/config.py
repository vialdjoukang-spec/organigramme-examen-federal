"""Chargement et validation de la configuration d'un agent (JSON, bibliothèque standard)."""
import json, os
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
TYPES = {"int": int, "str": str, "bool": bool, "dict": dict}

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
    cfg["_chemin"] = str(Path(chemin).resolve())
    return cfg

def lot_autorise(cfg, numero):
    return cfg["lot_min"] <= int(numero) <= cfg["lot_max"]
