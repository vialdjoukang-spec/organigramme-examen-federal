"""NCI IDC. Pipeline B seulement si une visionneuse est ouverte ; pas de série entière."""
from base import vide


def chercher(besoin):
    return vide("idc", "idc-index absent : pas de série CC BY isolée ni de visionneuse ouverte dans cette passe")
