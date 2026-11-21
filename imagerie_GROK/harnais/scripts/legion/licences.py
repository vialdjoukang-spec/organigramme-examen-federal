"""Liste blanche : CC0, domaine public, CC BY, CC BY-SA. Auteur et URL exigés."""
import re
import validate as V

# NC / ND avant le motif de validate : « CC BY-NC » ne doit pas passer pour « CC BY ».
_INTERDIT = re.compile(r"(?:\bnc\b|\bnd\b|non[-\s]?commercial|no[-\s]?deriv)", re.I)
_AUTEUR_VIDE = re.compile(r"^(unknown|inconnu|anonyme|anonymous|\?|n/?a|none)$", re.I)


def normaliser(licence):
    s = re.sub(r"\s+", " ", (licence or "").strip())
    bas = s.lower().replace("_", " ")
    aliases = {
        "cc0": "CC0",
        "cc0 1.0": "CC0 1.0",
        "cc-zero": "CC0",
        "public domain": "Public domain",
        "pd": "PD",
        "cc by": "CC BY",
        "cc-by": "CC BY",
        "cc by-sa": "CC BY-SA",
        "cc-by-sa": "CC BY-SA",
    }
    if bas in aliases:
        return aliases[bas]
    m = re.fullmatch(r"(cc[ -]by(?:-sa)?)\s*(\d\.\d)?", s, re.I)
    if m:
        nom = "CC BY-SA" if "sa" in m.group(1).lower() else "CC BY"
        return (nom + " " + m.group(2)).strip()
    return s


def licence_ok(licence):
    s = normaliser(licence)
    if not s or _INTERDIT.search(s):
        return False
    return bool(V.WL.match(s))


def auteur_ok(auteur):
    s = re.sub(r"\s+", " ", (auteur or "").strip())
    if len(s) < 2 or _AUTEUR_VIDE.match(s):
        return False
    return True


def url_ok(url):
    return (url or "").startswith("http")


def raison_licence(licence, auteur, url):
    if not licence_ok(licence):
        return f"licence hors liste blanche ({normaliser(licence) or 'absente'})"
    if not auteur_ok(auteur):
        return "auteur absent"
    if not url_ok(url):
        return "URL de source absente"
    return ""
