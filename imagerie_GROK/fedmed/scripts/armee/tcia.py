"""TCIA. On préfère le miroir IDC ; pas de ZIP de collection sans licence lue."""
from sonde import sonder


def chercher(besoin):
    return sonder(
        "tcia",
        "https://services.cancerimagingarchive.net/nbia-api/services/v1/getCollectionValues",
        "collection sans licence CC lue dans l'archive",
    )
