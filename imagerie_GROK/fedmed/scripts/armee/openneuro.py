"""OpenNeuro. Un jeu CC0 sans participants.tsv complet n'est pas téléchargé."""
from sonde import sonder


def chercher(besoin):
    if besoin.get("modalite") not in ("IRM", "EEG"):
        return {"source": "openneuro", "raison": "hors IRM ou EEG", "candidats": []}
    return sonder(
        "openneuro",
        "https://openneuro.org/datasets/ds006395/versions/1.0.8",
        "participants.tsv non apparié à ce besoin : pas de coupe extraite",
    )
