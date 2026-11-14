"""ODIR-5K. Figshare annonce CC BY 4.0 ; le paquet entier n'est pas une image unitaire."""
from sonde import sonder


def chercher(besoin):
    if besoin.get("modalite") != "FO":
        return {"source": "odir", "raison": "hors fond d'œil", "candidats": []}
    return sonder(
        "odir",
        "https://figshare.com/articles/dataset/ODIR-5K_dataset/32157930",
        "paquet Figshare sans image unitaire extraite dans cette passe",
    )
