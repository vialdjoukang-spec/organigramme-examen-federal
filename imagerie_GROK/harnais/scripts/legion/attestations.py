"""Âge et sexe lus dans une légende. Priorité aux adultes. Sexe : validate.sexe_requis."""
import re
import validate as V

_AGE = re.compile(
    r"\b(\d{1,3})\s*(?:ans|[- ]?year[- ]?olds?|[- ]?yo\b|y/o|y\.o\.|[- ]?yrs?\b)",
    re.I,
)
_SEXE_M = re.compile(r"\b(males?|hommes?|garçons?|garcons?|boys?|masculins?)\b", re.I)
_SEXE_F = re.compile(r"\b(females?|femmes?|filles?|girls?|wom[ae]n|féminins?|feminins?)\b", re.I)
_MAN = re.compile(r"\byear[- ]old man\b|\bman aged\b", re.I)
_WOMAN = re.compile(r"\byear[- ]old woman\b|\bwoman aged\b", re.I)


def age_ans(texte):
    m = _AGE.search(texte or "")
    if not m:
        return None
    n = int(m.group(1))
    if not 0 < n < 120:
        return None
    return n


def phrase_age(texte):
    m = _AGE.search(texte or "")
    return m.group(0).strip() if m else ""


def sexe(texte):
    """M, F, ou vide. « man » seul est ignoré (faux ami). Les deux sexes : vide."""
    t = texte or ""
    m = bool(_SEXE_M.search(t) or _MAN.search(t))
    f = bool(_SEXE_F.search(t) or _WOMAN.search(t))
    if m and f:
        return ""
    if m:
        return "M"
    if f:
        return "F"
    return ""


def adulte_de(age):
    if age is None:
        return ""
    return "oui" if age >= 18 else "non"


def tranche(age):
    if age is None:
        return ""
    if age < 18:
        return "enfant"
    if age < 40:
        return "jeune-adulte"
    if age < 65:
        return "adulte"
    return "age"


def rediger(texte, limite=180):
    """Retire courriels, dates et longs numéros. Conserve la formule d'âge."""
    t = texte or ""
    gardes = []

    def garder(m):
        gardes.append(m.group(0))
        return f"[[A{len(gardes) - 1}]]"

    t = _AGE.sub(garder, t)
    t = re.sub(r"[\w.+-]+@[\w.-]+", "[courriel effacé]", t)
    t = re.sub(r"\b\d{1,2}[./-]\d{1,2}[./-]\d{2,4}\b", "[date effacée]", t)
    t = re.sub(r"\b\d{6,}\b", "[nombre effacé]", t)
    for i, g in enumerate(gardes):
        t = t.replace(f"[[A{i}]]", g)
    t = re.sub(r"\s+", " ", t).strip()
    return t[:limite]


def sexe_region(manifeste, dx):
    return V.sexe_requis(manifeste or {}, dx)


def ecart_max(cfg=None):
    try:
        return int(((cfg or {}).get("age") or {}).get("ecart_max_ans") or 15)
    except (TypeError, ValueError):
        return 15


def ages_comparables(a, b, cfg=None):
    if a is None or b is None:
        return False
    if (a >= 18) != (b >= 18):
        return False
    return abs(a - b) <= ecart_max(cfg)


def priorite(candidat):
    """Plus petit = mieux. Les adultes attestés passent devant."""
    age = candidat.get("age_ans")
    adulte = 0 if isinstance(age, int) and age >= 18 else 1
    sexe_manque = 0 if candidat.get("sex") in ("M", "F") else 1
    age_manque = 0 if isinstance(age, int) else 1
    return (age_manque, sexe_manque, adulte, abs((age or 40) - 40))
