"""Éclaireur PMC Open Access. Le seau S3 n'est ouvert qu'avec un PMCID de figure."""
from base import vide


def chercher(besoin):
    return vide("pmc_oa", "secours S3 : pas de PMCID de figure isolé dans cette passe")
