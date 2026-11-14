"""Éclaireur Open-i. L'API a souvent renvoyé du HTML en novembre 2026."""
import urllib.parse

from base import ecrire_cache, get, lire_cache, vide


def chercher(besoin):
    terme = f"{besoin.get('modalite') or ''} {besoin.get('dx') or ''}".strip()
    cache = lire_cache("openi", terme)
    if cache:
        return cache
    url = "https://openi.nlm.nih.gov/api/search?" + urllib.parse.urlencode({
        "query": terme, "it": "x", "lic": "by", "m": "1", "n": "3",
    })
    try:
        corps = get(url, timeout=12)
    except Exception as exc:
        res = vide("openi", f"source injoignable ({type(exc).__name__})")
        ecrire_cache("openi", terme, res)
        return res
    if corps.lstrip().startswith("<"):
        res = vide("openi", "réponse HTML, pas de JSON")
    else:
        res = vide("openi", "JSON reçu sans image retenue dans cette passe")
    ecrire_cache("openi", terme, res)
    return res
