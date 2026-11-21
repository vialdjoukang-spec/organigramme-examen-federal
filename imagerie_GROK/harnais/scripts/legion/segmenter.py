"""Contour scikit-image via segment.py. Rien n'est inventé sans graine, rien n'est promu."""
import os
import socle


def executer(mid, force=False):
    etat = socle.charger(mid)
    graine = etat.get("graine")
    path = etat.get("fichier_segment") or ""
    cle = socle.cle("segment", socle.VERSION, graine, path)
    if not force and etat.get("cle_segment") == cle and etat.get("segment"):
        socle.journal("segment_reprise", id=mid)
        return etat
    if not (isinstance(graine, (list, tuple)) and len(graine) == 2 and path and os.path.isfile(path)):
        etat["segment"] = {"ok": False, "raison": "pas de graine : contour non inventé", "inscrit_manifeste": False}
        etat["cle_segment"] = cle
        socle.sauver(etat)
        socle.journal("segment", id=mid, ok=False)
        return etat
    try:
        import numpy as np
        from PIL import Image
        import segment as seg
    except Exception as e:
        etat["segment"] = {"ok": False, "raison": f"segment.py indisponible ({type(e).__name__})",
                           "inscrit_manifeste": False}
        etat["cle_segment"] = cle
        socle.sauver(etat)
        return etat
    im = np.array(Image.open(path).convert("L"))
    h, w = im.shape
    x, y = float(graine[0]), float(graine[1])
    sx = min(max(int(round(x * (w - 1))), 1), w - 2)
    sy = min(max(int(round(y * (h - 1))), 1), h - 2)
    try:
        poly, how = seg.polygon(im, sx, sy)
    except Exception as e:
        etat["segment"] = {"ok": False, "raison": f"échec ({type(e).__name__})", "inscrit_manifeste": False}
        etat["cle_segment"] = cle
        socle.sauver(etat)
        return etat
    if poly:
        dest = os.path.join(socle.DEMO, "segment", mid + ".png")
        seg.draw(path, poly, sx, sy, dest)
        etat["segment"] = {
            "ok": True, "methode": how, "points": len(poly),
            "fichier": os.path.relpath(dest, socle.ROOT),
            "inscrit_manifeste": False,
            "raison": "contour automatique, non inscrit dans le manifeste",
        }
    else:
        etat["segment"] = {"ok": False, "raison": how or "échec", "inscrit_manifeste": False}
    etat["cle_segment"] = cle
    socle.sauver(etat)
    socle.journal("segment", id=mid, ok=bool(poly), methode=how or "")
    return etat
