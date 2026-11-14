"""Cache, requête HTTP et forme d'un candidat d'éclaireur."""
import hashlib
import json
import urllib.request
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
CACHE = RACINE / "sources" / "cache"
ETAT = RACINE / "sources" / "armee"
PROVENANCE = RACINE / "sources" / "provenance"
UA = "FedMedBot/1.0 (atlas pedagogique; pas de donnee patient) python-urllib"
EXCLUS = ("eurorad", "radiopaedia", "padchest", "chexpert", "camus", "echonet")


def cle(source, requete):
    brut = f"{source}\n{requete}".encode()
    return hashlib.sha256(brut).hexdigest()[:20]


def lire_cache(source, requete):
    path = CACHE / source / f"{cle(source, requete)}.json"
    if not path.is_file():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def ecrire_cache(source, requete, obj):
    path = CACHE / source / f"{cle(source, requete)}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=1), encoding="utf-8")


def get(url, binaire=False, timeout=18):
    import time
    import urllib.error
    dernier = None
    for essai in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as rep:
                data = rep.read()
            return data if binaire else data.decode("utf-8", "replace")
        except urllib.error.HTTPError as exc:
            dernier = exc
            if exc.code != 429:
                raise
            time.sleep(3 * (essai + 1))
    raise dernier


def get_json(url, timeout=18):
    return json.loads(get(url, timeout=timeout))


def vide(source, raison):
    return {"source": source, "raison": raison, "candidats": []}


def candidat(**champs):
    base = {
        "source": "", "titre": "", "url": "", "img_url": "", "license": "",
        "license_url": "", "author": "", "caption": "", "age_ans": None,
        "sex": "", "modalite": "", "plan": "", "pipeline": "A", "viewer_url": "",
    }
    base.update(champs)
    return base
