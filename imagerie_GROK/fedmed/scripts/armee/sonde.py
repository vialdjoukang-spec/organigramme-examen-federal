"""Sonde commune : une source sans image unitaire libre s'arrête avant tout pixel."""
from base import ecrire_cache, get, lire_cache, vide


def sonder(source, url, raison_si_interdit, timeout=12):
    cache = lire_cache(source, url)
    if cache:
        return cache
    try:
        corps = get(url, timeout=timeout)[:4000].lower()
    except Exception as exc:
        res = vide(source, f"source injoignable ({type(exc).__name__})")
        ecrire_cache(source, url, res)
        return res
    if any(m in corps for m in ("by-nc", "non-commercial", "noncommercial", "data use agreement", "dua")):
        res = vide(source, raison_si_interdit)
    elif "creativecommons.org/licenses/by" in corps or "cc0" in corps or "public domain" in corps:
        res = vide(source, "licence peut-être ouverte, mais pas de fichier image unitaire anonyme")
    else:
        res = vide(source, raison_si_interdit)
    ecrire_cache(source, url, res)
    return res
