"""Kvasir. CC BY possible, âge par cliché non attesté : la porte d'aspect adulte ne s'ouvre pas sans mot « adulte »."""
from sonde import sonder


def chercher(besoin):
    if besoin.get("modalite") != "ENDO":
        return {"source": "kvasir", "raison": "hors endoscopie", "candidats": []}
    return sonder(
        "kvasir",
        "https://datasets.simula.no/kvasir/",
        "âge absent par cliché : ni nombre, ni mention adulte",
    )
