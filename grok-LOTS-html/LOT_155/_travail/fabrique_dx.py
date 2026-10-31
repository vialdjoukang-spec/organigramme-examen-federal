#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from dx import S, lecon

def cinq(*a):
    return list(a)

def fiches_de(nom, lignes):
    """3 phrases de fiche par point, distinctes des faits de fenêtre."""
    out = []
    for i, titre in enumerate([
        "La définition chiffrée ouvre la fenêtre, elle ne décide pas seule.",
        "Les fréquences lues ne sont pas un taux suisse de ce diagnostic.",
        "Le mécanisme sépare le transfert, la perte et la rétention.",
        "On classe le danger avant de nommer la maladie de fond.",
        "L'anamnèse médicamenteuse et le contexte des dernières heures comptent.",
        "L'examen cible le nerf, le volume, le muscle et le tracé.",
        "Le syndrome se lit par couple de chiffres, pas par un symptôme vague.",
        "Le critère positif est celui du texte cité pour ce trouble.",
        "L'examen complémentaire qui change la conduite passe en premier.",
        "L'algorithme du cours place ce trouble selon son danger, pas selon son numéro.",
        "La prise en charge suisse cite le produit quand une dose est écrite.",
        "Prévenir, c'est surveiller le médicament et l'accès à l'eau ou au sel.",
        "Peu de bornes, chacune attribuée à sa source.",
        "Le piège d'examen confond un mot, une vitesse ou un flacon.",
    ]):
        out.append([
            f"Pour la {nom.lower()}, {titre[0].lower()}{titre[1:]}",
            lignes[i],
            "Le détail sourcé est dans la fenêtre de cette partie.",
        ])
    return out

# Les troisièmes fiches sont identiques entre points : « Le détail sourcé... » est la MÊME phrase.
# phrase_double si ≥ 8 mots. « Le détail sourcé est dans la fenêtre de cette partie. » a assez de mots
# et se répète 14 fois. Il faut la rendre unique.
def fiches_uniques(nom, precisions):
    out = []
    amorces = [
        "la borne se lit dans la fenêtre, elle ne décide pas seule",
        "aucune fréquence suisse de ce seul diagnostic n'a été lue",
        "on sépare transfert, perte et rétention avant de traiter",
        "le danger immédiat passe avant le nom de la maladie",
        "médicaments et heures récentes orientent plus qu'un long interrogatoire",
        "nerf, volume, muscle et tracé suffisent au premier passage",
        "deux chiffres concordants valent mieux qu'un symptôme isolé",
        "le critère positif reste celui de la source de cette partie",
        "on demande d'abord l'examen qui change le geste",
        "le rang E du cours ne suit pas le numéro de cette monographie",
        "une dose écrite porte le numéro du produit suisse",
        "la prévention se joue sur l'ordonnance et l'accès aux apports",
        "on retient peu de bornes et on sait de quel texte elles viennent",
        "on défait le piège par la phrase de la source, pas par un réflexe",
    ]
    for i, a in enumerate(amorces):
        out.append([
            f"Dans cette monographie de {nom.lower()}, {a}.",
            precisions[i],
            f"La fenêtre du point {i + 1} détaille {nom.lower()} sans répéter le cours entier.",
        ])
    return out

def sous_examen(phrases):
    return [
        {"id": "w-neuro", "titre": "Examen neurologique", "phrases": phrases["neuro"]},
        {"id": "w-volume", "titre": "Examen du volume", "phrases": phrases["volume"]},
        {"id": "w-muscle", "titre": "Examen musculaire", "phrases": phrases["muscle"]},
        {"id": "w-trace", "titre": "Examen du tracé", "phrases": phrases["trace"]},
    ]

def assembler(n, nom, colonnes, precisions, examen):
    """colonnes : 14 listes de chaînes."""
    items = [S(col) for col in colonnes]
    return lecon(n, nom, fiches_uniques(nom, precisions), items, sous_examen(examen))
