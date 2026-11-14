"""Sleep-EDFx. ODC-By n'est pas dans la liste blanche stricte."""
from base import vide


def chercher(besoin):
    if besoin.get("modalite") != "PSG":
        return vide("sleep_edf", "hors polysomnographie")
    return vide("sleep_edf", "ODC-By 1.0 hors liste blanche CC0, domaine public, CC BY, CC BY-SA")
