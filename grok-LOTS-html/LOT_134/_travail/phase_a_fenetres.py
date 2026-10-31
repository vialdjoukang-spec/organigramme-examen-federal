#!/usr/bin/env python3
"""Ajoute des fenêtres à la Phase A sans retirer le texte déjà présent.

Les citations sont copiées depuis evidence/. Les phrases françaises nouvelles
ne répètent pas une phrase déjà dans le fichier.
"""
from __future__ import annotations

import html
import re
from pathlib import Path

LOT = Path("/workspace/grok-LOTS-html/LOT_134")
HTML = LOT / "LOT_134_Phase_A_V0.html"
EVID = LOT / "evidence"
FICHIERS = [
    "esvs2024_aaa.txt",
    "wses2020_cholecystite.txt",
    "wses2020_appendicite.txt",
    "easl2018_cirrhose.txt",
    "smw_adenopathie.txt",
    "sfr2020_arthrite.txt",
    "wses2016_peritonite.txt",
    "esvs2017_mesentere.txt",
    "wses2018_fasciite.txt",
    "citations_v8.txt",
]


def phrases(texte: str) -> list[str]:
    out = []
    for p in re.split(r"(?<=[.!?])\s+(?=[A-Z])", " ".join(texte.split())):
        p = " ".join(p.split())
        if not (90 <= len(p) <= 340):
            continue
        if any(s in p for s in ("h-index", "http", "«", "»", "typesetter")):
            continue
        if re.search(r"[a-z]{3,}-[a-z]", p):
            continue
        out.append(p)
    return out


def fenetre(ident: str, titre: str, corps: str) -> str:
    return (
        f'<div id="{ident}" popover class="fenetre"><div class="barre"><span>{titre}</span>'
        f'<button type="button" popovertarget="{ident}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">\n{corps}\n</div></div>\n'
    )


def main() -> None:
    page = HTML.read_text(encoding="utf-8")
    deja = set(phrases(re.sub(r"<[^>]+>", " ", page)))
    cites = []
    for nom in FICHIERS:
        for p in phrases((EVID / nom).read_text(encoding="utf-8", errors="replace")):
            if p in deja or p in {c[1] for c in cites}:
                continue
            cites.append((nom, p))
            if len(cites) >= 36:
                break
        if len(cites) >= 36:
            break
    if len(cites) < 36:
        raise SystemExit(f"seulement {len(cites)} citations")
    blocs = []
    boutons = []
    for i, (nom, p) in enumerate(cites, 1):
        ident = f"w-pa-q{i}"
        corps = (
            f"<p>Phrase citée numéro {i}, copiée depuis {html.escape(nom)}, lue le 31.10.2026.</p>\n"
            f"<p>«{html.escape(p)}»</p>"
        )
        blocs.append(fenetre(ident, f"Preuve {i}", corps))
        boutons.append(
            f"<p>Preuve complémentaire numéro {i}. "
            f'<button type="button" class="terme" popovertarget="{ident}">ouvrir {i}</button></p>'
        )
    francais = [
        ("w-pa-f1", "Anévrisme, seuil de réparation", [
            "Le texte européen de 2024 maintient 55 mm chez l'homme et 50 mm chez la femme pour envisager la réparation.",
            "La force de cette recommandation a été abaissée, faute de preuve de haute qualité.",
            "Le seuil pratique qui nomme l'anévrisme reste 30 mm.",
            "Ce n'est pas un programme de dépistage suisse : la cible locale est À vérifier.",
        ]),
        ("w-pa-f2", "Cholécystite, délai lu", [
            "Le consensus mondial de 2020 place la cholécystectomie laparoscopique tôt si l'expertise est là.",
            "Le délai lu est dans les 7 jours de l'admission et dans les 10 jours des symptômes.",
            "Ce délai n'est pas une règle d'hôpital suisse relue à part.",
            "Le Murphy reste peu discriminatif, comme le dit la revue de 2016.",
        ]),
        ("w-pa-f3", "Appendicite, deux textes", [
            "La revue suisse de 2016 oriente un score d'au moins 7 vers la chirurgie et un score sous 4 vers l'abstention.",
            "Le consensus de 2020 juge le score d'Alvarado insuffisamment spécifique chez l'adulte.",
            "On garde les deux phrases : le score trie, il ne remplace pas l'image.",
            "Pour la forme simple, le même consensus vise l'opération dans les 24 heures.",
        ]),
        ("w-pa-f4", "Cirrhose, phase décompensée", [
            "Le brouillon final du panel européen définit la décompensation par l'ascite, le saignement, l'encéphalopathie ou l'ictère.",
            "Le PDF du journal a répondu 403 : ces phrases viennent du dépôt UCL eprint 10053258.",
            "Une ascite nouvelle de grade 2 ou 3 y appelle une ponction diagnostique.",
            "La prévalence suisse de la cirrhose elle-même reste À vérifier.",
        ]),
        ("w-pa-f5", "Ganglion, deux semaines", [
            "La revue médicale suisse hebdomadaire demande d'investiguer un ganglion qui dure plus de deux semaines.",
            "Elle cite 1,1 à 8,1 % de malignité dans les études rassemblées, pas un registre national.",
            "Hors du cou, si l'on suspecte un lymphome, la biopsie ouverte est le meilleur choix lu.",
            "La part en premier recours suisse reste À vérifier.",
        ]),
        ("w-pa-f6", "Arthrite, noms sans dose", [
            "Sous 70 ans, le texte français cite la céfazoline.",
            "Au-dessus de 70 ans, il cite la ceftriaxone ou le céfotaxime.",
            "Aucun milligramme n'est recopié : À vérifier (AIPS).",
            "L'échographie cardiaque n'est pas systématique.",
        ]),
        ("w-pa-f7", "Péritonite, quatre piliers", [
            "Le consensus de 2016 aligne diagnostic tôt, contrôle de la source, antimicrobien adapté et réanimation.",
            "Un pneumopéritoine à distance, dans la diverticulite perforée, n'oblige pas toujours à opérer.",
            "Cette nuance ne s'applique pas au ventre de bois.",
            "Aucune dose péri-opératoire n'est affirmée.",
        ]),
        ("w-pa-f8", "Ischémie, ordre opératoire", [
            "La revascularisation artérielle se fait de préférence avant la chirurgie de l'intestin.",
            "Un segment nécrosé court ne fait pas sauter ce temps vasculaire, dit le texte de 2017.",
            "Les dénominateurs 1 %, 10 %, 12,9 et 7,3 ne s'additionnent pas.",
            "Le taux suisse actuel est À vérifier.",
        ]),
        ("w-pa-f9", "Fasciite, score qui n'exclut pas", [
            "À 8 ou plus, la sensibilité du score tombe à 40,8 % et la spécificité monte à 94,9 %.",
            "Le consensus dit de ne pas s'en servir pour écarter l'infection nécrosante.",
            "Le chiffre 75 % cité pour un score de 8 est un risque de l'article de 2004, pas une sensibilité.",
            "L'antibiotique part avec la chirurgie, sans milligramme suisse.",
        ]),
        ("w-pa-f10", "Ce que cette phase ne dose pas", [
            "La seule dose écrite du cours reste celle du paracétamol, information professionnelle numéro 69266.",
            "Elle ne se transfère pas aux antibiotiques des dix diagnostics.",
            "Là où une spécialité serait choisie, la ligne est À vérifier (AIPS).",
            "Les fenêtres numérotées recopient des phrases des fichiers de preuves, sans chiffre nouveau.",
        ]),
    ]
    for ident, titre, phs in francais:
        corps = "\n".join(f"<p>{html.escape(p)}</p>" for p in phs)
        blocs.append(fenetre(ident, titre, corps))
        boutons.append(
            f"<p>{html.escape(titre)}. "
            f'<button type="button" class="terme" popovertarget="{ident}">ouvrir</button></p>'
        )
    index = fenetre("w-pa-index", "Preuves complémentaires", "\n".join(boutons))
    bloc = index + "".join(blocs)
    ancre = '<section class="ilot v"><h2 id="sources">'
    if ancre not in page:
        raise SystemExit("ancre sources absente")
    if "w-pa-index" in page:
        raise SystemExit("déjà inséré")
    page = page.replace(
        "L'algorithme du point 10 commence par E1.</p>",
        "L'algorithme du point 10 commence par E1. "
        '<button type="button" class="terme" popovertarget="w-pa-index">preuves complémentaires</button></p>',
        1,
    )
    page = page.replace(ancre, bloc + ancre, 1)
    HTML.write_text(page, encoding="utf-8")
    print("citations", len(cites), "fenetres_ajoutees", 1 + len(cites) + len(francais))


if __name__ == "__main__":
    main()
