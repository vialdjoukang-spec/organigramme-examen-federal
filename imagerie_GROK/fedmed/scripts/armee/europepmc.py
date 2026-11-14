"""Éclaireur Europe PMC. Pipeline A si la figure est dans l'archive."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "harnais" / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "harnais" / "scripts" / "legion"))
import europepmc as E

from base import candidat, ecrire_cache, lire_cache, vide


def chercher(besoin):
    terme = f"{besoin.get('modalite') or ''} {besoin.get('dx') or ''}".strip()
    cache = lire_cache("europepmc", terme)
    if cache:
        return cache
    try:
        arts = E.articles(terme, n=2, max_figures=1)
    except Exception as exc:
        res = vide("europepmc", f"source injoignable ({type(exc).__name__})")
        ecrire_cache("europepmc", terme, res)
        return res
    cands = []
    for art in arts:
        if not art.get("accepte_licence"):
            continue
        try:
            E.charger_figures(art)
        except Exception:
            continue
        for fig in art.get("figures") or []:
            if not fig.get("octets"):
                continue
            cands.append(candidat(
                source="europepmc", titre=fig.get("href") or "",
                url=art.get("source_url") or "", img_url="",
                license=art.get("license") or "", license_url=art.get("license_url") or "",
                author=(art.get("author") or "")[:180], caption=(fig.get("caption") or "")[:800],
                pipeline="A", octets=fig.get("octets"),
            ))
            fig["octets"] = None
    res = {"source": "europepmc", "raison": "" if cands else "aucune figure libre", "candidats": cands[:2]}
    # ne pas mettre les octets dans le cache disque
    leger = {"source": "europepmc", "raison": res["raison"], "candidats": [
        {k: v for k, v in c.items() if k != "octets"} for c in cands[:2]
    ]}
    ecrire_cache("europepmc", terme, leger)
    return res
