"""Zenodo et Figshare. On refuse NC, les fantômes et les paquets sans image clinique unitaire."""
from base import vide


def chercher(besoin):
    return vide("zenodo_figshare", "pas de notice CC BY avec âge ou mention adulte pour ce besoin")
