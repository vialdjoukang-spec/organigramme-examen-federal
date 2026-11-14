"""NIH ChestX-ray14. Pas de fichier unitaire anonyme sans le store GCP."""
from base import vide


def chercher(besoin):
    if "thorax" not in (besoin.get("cliche") or "").lower() and besoin.get("modalite") != "RX":
        return vide("nih_cxr14", "hors radiographie thoracique")
    return vide("nih_cxr14", "pas d'API anonyme d'un seul cliché ; store GCP sur formulaire")
