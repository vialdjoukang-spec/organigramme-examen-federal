"""ISIC. Pipeline A : l'API v2 peut rendre un JPEG sous CC0 ou CC BY."""
import urllib.parse

from base import candidat, ecrire_cache, get_json, lire_cache, vide


def chercher(besoin):
    if besoin.get("modalite") != "DERM":
        return vide("isic", "hors dermatoscopie")
    requete = "age_approx:[18 TO 120]"
    cache = lire_cache("isic", requete)
    if cache:
        return cache
    try:
        data = get_json("https://api.isic-archive.com/api/v2/images/search/?" + urllib.parse.urlencode({
            "query": requete, "limit": "3",
        }))
    except Exception as exc:
        res = vide("isic", f"source injoignable ({type(exc).__name__})")
        ecrire_cache("isic", requete, res)
        return res
    cands = []
    for item in (data.get("results") or [])[:3]:
        lic = ((item.get("license") or "") + " " + (item.get("attribution") or "")).strip()
        cands.append(candidat(
            source="isic", titre=item.get("isic_id") or "",
            url="https://api.isic-archive.com/api/v2/images/" + (item.get("isic_id") or ""),
            img_url=(item.get("files") or {}).get("full", {}).get("url") or "",
            license=lic, author=item.get("attribution") or "ISIC Archive",
            caption=f"dermatoscopie {item.get('isic_id') or ''}",
            age_ans=item.get("age_approx") if isinstance(item.get("age_approx"), int) else None,
            sex=(item.get("sex") or "")[:1].upper(),
            modalite="DERM", pipeline="A",
        ))
    res = {"source": "isic", "raison": "" if cands else "aucune image", "candidats": cands}
    ecrire_cache("isic", requete, res)
    return res
