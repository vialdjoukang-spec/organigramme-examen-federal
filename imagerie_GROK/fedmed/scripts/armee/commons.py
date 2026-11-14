"""Éclaireur Wikimedia Commons. Pipeline A : l'API donne le fichier."""
import urllib.parse

from base import candidat, ecrire_cache, get_json, lire_cache, vide

EPINGLES = {
    ("IMG-226", "patho"): "File:RA stenoz doppler.jpg",
    ("IMG-293", "normal"): "File:Graf Hip Ultrasound Type Ia.jpg",
    ("EXP-027", "patho"): "File:Audiograma representando perda auditiva sensórioneural.png",
    ("EXP-090", "normal"): "File:GastricEmptying.jpg",
}
NOUVEAU_NE = "File:Ultrasound - normal newborn left hip (Graf type Ia).jpg"


def _meta(page):
    ii = (page.get("imageinfo") or [{}])[0]
    em = ii.get("extmetadata") or {}

    def val(k):
        import re
        return re.sub(r"<[^>]+>", " ", (em.get(k) or {}).get("value") or "")

    return candidat(
        source="commons",
        titre=page.get("title") or "",
        url="https://commons.wikimedia.org/wiki/" + urllib.parse.quote((page.get("title") or "").replace(" ", "_")),
        img_url=ii.get("url") or "",
        license=val("LicenseShortName"),
        author=val("Artist")[:180],
        caption=val("ImageDescription")[:800],
        pipeline="A",
    )


def _pages(titles):
    data = get_json("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({
        "action": "query", "format": "json", "prop": "imageinfo",
        "iiprop": "url|extmetadata|mime", "titles": "|".join(titles),
    }))
    return list((data.get("query") or {}).get("pages", {}).values())


def chercher(besoin):
    epingle = EPINGLES.get((besoin["id"], besoin["cote"]))
    if epingle:
        cache = lire_cache("commons", epingle)
        if cache:
            return cache
        pages = _pages([epingle])
        page = pages[0] if pages else {}
        if page.get("missing") is not None or page.get("imagerepository") is None and not page.get("imageinfo"):
            if besoin["id"] == "IMG-293":
                res = vide("commons", f"{epingle} absent. Le seul Graf Ia trouvé est un nouveau-né, refusé.")
            else:
                res = vide("commons", f"{epingle} absent de Commons")
        else:
            res = {"source": "commons", "raison": "", "candidats": [_meta(page)]}
        ecrire_cache("commons", epingle, res)
        return res
    requete = f"{besoin.get('modalite') or ''} {besoin.get('dx') or ''} normal".strip()
    cache = lire_cache("commons", requete)
    if cache:
        return cache
    try:
        data = get_json("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({
            "action": "query", "format": "json", "generator": "search", "gsrnamespace": "6",
            "gsrsearch": requete, "gsrlimit": "4",
            "prop": "imageinfo", "iiprop": "url|extmetadata|mime",
        }))
    except Exception as exc:
        res = vide("commons", f"source injoignable ({type(exc).__name__})")
        ecrire_cache("commons", requete, res)
        return res
    pages = (data.get("query") or {}).get("pages") or {}
    cands = [_meta(p) for p in pages.values() if p.get("imageinfo")]
    cands = [c for c in cands if NOUVEAU_NE not in c["titre"]]
    res = {"source": "commons", "raison": "" if cands else "aucun fichier", "candidats": cands}
    ecrire_cache("commons", requete, res)
    return res
