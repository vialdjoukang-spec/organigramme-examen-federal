"""PTB-XL. Pipeline D seulement si la fiche PhysioNet est CC BY. Sinon refus."""
from sonde import sonder


def chercher(besoin):
    if besoin.get("modalite") != "ECG":
        return {"source": "ptbxl", "raison": "hors ECG", "candidats": []}
    return sonder(
        "ptbxl",
        "https://physionet.org/content/ptb-xl/1.0.3/",
        "licence PhysioNet non confirmée dans la liste CC (CC BY annoncé par un tiers seulement)",
    )
