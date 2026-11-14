"""CTU-UHB. ODC-By hors liste blanche stricte. Pas de capture."""
from base import vide


def chercher(besoin):
    if besoin.get("modalite") != "CTG":
        return vide("ctu_uhb", "hors cardiotocographie")
    return vide("ctu_uhb", "ODC-By 1.0 hors liste blanche CC")
