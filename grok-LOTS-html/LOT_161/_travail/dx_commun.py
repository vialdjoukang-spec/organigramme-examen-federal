#!/usr/bin/env python3
"""Assemble un DX du LOT_161 avec le moteur V8."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from moteur import GLOSSAIRE, SOURCES_LI, bouton, ecrire, fenetre, page
from phase_a import bloc, section


def rendre(n: int, nom: str, fiches: dict, details: dict, extras: dict | None = None) -> str:
    extras = extras or {}
    morceaux = []
    for i in range(1, 15):
        titre = {
            1: "Définition",
            2: "Épidémiologie",
            3: "Physiopathologie et rappels",
            4: "Démarche diagnostique",
            5: "Anamnèse et drapeaux rouges",
            6: "Examen physique",
            7: "Approche syndromique",
            8: "Diagnostic positif",
            9: "Examens complémentaires",
            10: "Arbre décisionnel",
            11: "Prise en charge en Suisse",
            12: "Prévention",
            13: "Points clés",
            14: "Pièges d'examen",
        }[i]
        morceaux.append(section(i, titre, fiches[i], details[i], extras.get(i, "")))
    essentiel = bloc(
        f"""
{nom} est le sujet de ce DX. Le rang du cours n'est pas une fréquence suisse.

Les cibles de LDL et les doses suisses restent celles déjà sourcées pour la leçon.|s1

Le détail de chaque point s'ouvre dans sa fenêtre.
"""
    )
    return page(
        nom,
        f"DX.{n}. {nom}. F2.13, lipides sériques anormaux. Texte du 31 octobre 2026.",
        essentiel,
        True,
        "\n".join(morceaux),
        SOURCES_LI,
        f"LOT_161_Phase_B_V0_DX.{n}.html",
        GLOSSAIRE,
    )


def ecrire_dx(n: int, nom: str, fiches: dict, details: dict, extras: dict | None = None) -> None:
    ecrire(f"LOT_161_Phase_B_V0_DX.{n}.html", rendre(n, nom, fiches, details, extras))
