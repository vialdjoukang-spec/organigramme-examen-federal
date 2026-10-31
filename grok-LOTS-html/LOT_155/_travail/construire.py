#!/usr/bin/env python3
"""Construit les 11 leçons de LOT_155 à partir des preuves lues le 31.10.2026."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from moteur import ecrire

SOURCES = [
    "PROFILES 2023, validé le 1er novembre 2023, situation F2.7.",
    "Spasovski G et al., Nephrology Dialysis Transplantation, 25 février 2014.",
    "Association britannique de néphrologie, octobre 2023, hyperkaliémie de l'adulte.",
    "Tagan G, Benmachiche M, Revue Médicale Suisse, 22 novembre 2023.",
    "Katerinis I, Fumeaux Z, Revue Médicale Suisse, 7 mars 2007.",
    "Minetto D, Serratrice J, Stirnemann J, Revue Médicale Suisse, 19 octobre 2016.",
    "Bex S, Mollard F, Stirnemann J, Revue Médicale Suisse, 16 octobre 2019.",
    "Walsh J, Gittoes N, Selby P, Society for Endocrinology, 2016, hypercalcémie.",
    "Society for Endocrinology, Endocrine Connections, 2016, hypocalcémie aiguë.",
    "Information professionnelle Samsca, Swissmedic 66962, lue le 31 octobre 2026.",
    "Information professionnelle Lokelma, Swissmedic 67851, lue le 31 octobre 2026.",
    "Information professionnelle Veltassa, Swissmedic 66411, lue le 31 octobre 2026.",
    "Information professionnelle Resonium A, Swissmedic 33379, lue le 31 octobre 2026.",
    "Information professionnelle Kaliumchlorid B. Braun, Swissmedic 29552, lue le 31 octobre 2026.",
    "Information professionnelle Zometa, Swissmedic 56257, lue le 31 octobre 2026.",
    "Information professionnelle Aclasta, Swissmedic 57363, lue le 31 octobre 2026.",
    "Information professionnelle Minirin injectable, Swissmedic 43585, lue le 31 octobre 2026.",
]

GLOSSAIRE = [
    "Référentiel suisse des objectifs de formation (PROFILES).",
    "Situation de départ de ce référentiel (SSP).",
    "Information professionnelle suisse (AIPS).",
    "Syndrome d'antidiurèse inappropriée (SIAD).",
    "Syndrome de sécrétion inappropriée d'hormone antidiurétique (SIADH).",
    "Électrocardiogramme (ECG).",
    "Association britannique de néphrologie dans son guide d'octobre 2023 (UKKA).",
    "Conseil européen de réanimation (ERC).",
    "Hormone parathyroïdienne (PTH).",
    "Intervalle de l'électrocardiogramme (QT).",
    "Inhibiteur de la pompe à protons (IPP).",
    "Système rénine-angiotensine-aldostérone (SRAA).",
    "Débit de filtration glomérulaire (DFG).",
    "Facteur de croissance des fibroblastes 23 (FGF23).",
]

TITRES = [
    "1. Définition",
    "2. Épidémiologie",
    "3. Physiopathologie",
    "4. Démarche diagnostique",
    "5. Anamnèse et drapeaux rouges",
    "6. Examen physique",
    "7. Approche syndromique",
    "8. Diagnostic positif",
    "9. Examens complémentaires",
    "10. Arbre décisionnel",
    "11. Prise en charge en Suisse",
    "12. Prévention",
    "13. Points clés",
    "14. Pièges d'examen",
]


def exp(items):
    out = []
    for e, c, p, k in items:
        out.append(f"{e}.")
        out.append(f"La conduite retenue est celle-ci : {c}.")
        out.append(f"Le piège à éviter est celui-ci : {p}.")
        out.append(f"Le contrôle utile ensuite est le suivant : {k}.")
    return out


def point(i, fiche, items, sous=None):
    d = {"titre": TITRES[i - 1], "fiche": fiche, "fenetre": exp(items)}
    if sous:
        d["sous"] = sous
    return d


def meta_base(**kw):
    kw.setdefault("glossaire", GLOSSAIRE)
    kw.setdefault("sources", SOURCES)
    return kw
