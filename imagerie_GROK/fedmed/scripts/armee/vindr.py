"""VinDr-CXR. Article CC BY, DICOM PhysioNet à confirmer avant tout pixel."""
from sonde import sonder


def chercher(besoin):
    if besoin.get("modalite") not in ("RX", "AUTRE"):
        return {"source": "vindr", "raison": "hors radiographie thoracique", "candidats": []}
    return sonder(
        "vindr",
        "https://physionet.org/content/vindr-cxr/",
        "licence DICOM PhysioNet non confirmée CC BY",
    )
