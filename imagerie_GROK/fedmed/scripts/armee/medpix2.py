"""MedPix 2.0. Le catalogue ODC-ODbL n'est pas dans la liste blanche sans fiche CC par cas."""
from sonde import sonder


def chercher(besoin):
    return sonder(
        "medpix2",
        "https://zenodo.org/records/12624810",
        "licence ODC-ODbL du catalogue, non vérifiée CC par cas",
    )
