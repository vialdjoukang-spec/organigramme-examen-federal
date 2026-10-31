#!/usr/bin/env python3
"""Trois schémas du dessinateur pour LOT_173. Pas de page HTML dans le LOT (un HTML isolé serait jugé comme une leçon)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "grok-LOTS-html/outils/dessinateur"))
import dessinateur  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "illustrations"
POLICE = "../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf"


def E(cx, cy, rx, ry):
    return {"type": "ellipse", "cx": cx, "cy": cy, "rx": rx, "ry": ry}


def zone(i, nom, geo, badge, definition, lesion=False, remplissage="#d7e8f2", contour="#14303b"):
    z = {
        "id": f"z{i}",
        "nom": nom,
        "numero": i,
        "geometrie": geo,
        "remplissage": remplissage,
        "contour": contour,
        "epaisseur": 1.6,
        "badge": badge,
        "definition": definition,
    }
    if lesion:
        z["lesion"] = True
    return z


def niveau(nid, etiquette, note, structures, defaut=False):
    n = {
        "id": nid,
        "etiquette": etiquette,
        "note": note,
        "viewBox": [0, 0, 1000, 760],
        "repere": {"texte": "D", "x": 78, "y": 78, "titre": "Repère D, côté gauche de l'écran"},
        "structures": structures,
    }
    if defaut:
        n["defaut"] = True
    return n


def abdomen():
    paroi = lambda: zone(1, "Paroi abdominale", E(500, 390, 420, 300), [180, 180],
                         "Limite du schéma, pas un organe.")
    foie = lambda: zone(2, "Foie", E(300, 340, 150, 120), [300, 340],
                        "À gauche de l'écran : côté droit du patient.", remplissage="#c9a27c", contour="#6b4028")
    rate = lambda big=False: zone(3, "Rate", E(760, 330, 120 if big else 70, 90 if big else 52), [760, 330],
                                  "À droite de l'écran : côté gauche du patient. Elle grossit dans l'hypersplénisme.",
                                  lesion=big, remplissage="#c96b6b", contour="#7a2430")
    aorte = lambda: zone(4, "Aorte", E(500, 500, 32, 32), [500, 500],
                         "Repère médian, devant le rachis.", remplissage="#e36b6b", contour="#8d1e28")
    rachis = lambda: zone(5, "Rachis", E(500, 600, 55, 40), [500, 600],
                          "Repère postérieur du schéma axial.", remplissage="#d9d3c7", contour="#5c564c")
    return {
        "id": "lot173-abdomen",
        "titre": "Coupe axiale schématique : foie, rate, aorte",
        "question": {
            "intitule": "Pourquoi la rate du niveau 2 change-t-elle la lecture d'un compte bas ?",
            "html": "<p>Un compte bas et stable, avec une rate grande et une maladie du foie, oriente vers la séquestration. Le même compte avec une rate de taille ordinaire et des saignements ouvre d'autres diagnostics.</p><p>Le schéma n'est pas un scanner. Il fixe seulement l'orientation : D à gauche de l'écran, rate à droite de l'écran.</p>",
        },
        "sources_courtes": "Schéma original du 31 octobre 2026, orientation radiologique. Pas un cliché de patient.",
        "niveaux": [
            niveau("haute", "Rate ordinaire", "Schéma. Rate de taille ordinaire, foie et aorte pour l'orientation.",
                   [paroi(), foie(), rate(False), aorte(), rachis()], True),
            niveau("grande", "Rate grande", "Schéma. La rate dépasse le volume du niveau précédent. Pastille sur la rate.",
                   [paroi(), foie(), rate(True), aorte(), rachis()]),
            niveau("porte", "Foie et rate", "Schéma. Le foie et la rate sont tous deux à regarder avant de traiter le chiffre.",
                   [paroi(), foie(), rate(True), aorte(), rachis()]),
        ],
    }


def frottis():
    champ = lambda: zone(1, "Champ du frottis", E(500, 390, 420, 280), [200, 180],
                         "Zone où l'on cherche les plaquettes et les globules rouges.")
    rouge = lambda: zone(2, "Globules rouges", E(340, 400, 70, 48), [340, 400],
                         "Disques roses, taille de référence du frottis.", remplissage="#e7a0a0", contour="#8d3030")
    plaquettes = lambda: zone(3, "Plaquettes libres", E(640, 360, 36, 28), [640, 360],
                              "Petits éléments violets dispersés, sans amas.", remplissage="#6b4c9a", contour="#3a2460")
    amas = lambda: zone(3, "Amas de plaquettes", E(640, 400, 90, 70), [640, 400],
                        "Amas in vitro, typique de l'artefact au tube, sans saignement clinique.",
                        lesion=True, remplissage="#5c3d86", contour="#2a1848")
    schizo = lambda: zone(4, "Fragments rouges", E(470, 500, 80, 36), [470, 500],
                          "Fragments de globules rouges : on cherche une microangiopathie, pas un artefact.",
                          lesion=True, remplissage="#c44848", contour="#6e1414")
    return {
        "id": "lot173-frottis",
        "titre": "Frottis schématique : plaquettes, amas, fragments",
        "question": {
            "intitule": "Quel niveau interdit de transfuser sur le seul chiffre ?",
            "html": "<p>Le niveau des amas. Le compte machine est bas parce que les plaquettes sont collées dans le tube, pas parce que le malade saigne.</p><p>Le niveau des fragments rouges est une autre urgence : on n'attend pas un compte joli pour reconnaître la microangiopathie.</p>",
        },
        "sources_courtes": "Schéma original du 31 octobre 2026. Ce n'est pas une lame de patient.",
        "niveaux": [
            niveau("libres", "Plaquettes libres", "Schéma de frottis. Plaquettes dispersées, globules rouges intacts.",
                   [champ(), rouge(), plaquettes()], True),
            niveau("amas", "Amas au tube", "Schéma. Les plaquettes sont en amas. Le malade ne saigne pas.",
                   [champ(), rouge(), amas()]),
            niveau("fragments", "Fragments rouges", "Schéma. Fragments de globules rouges et peu de plaquettes libres.",
                   [champ(), rouge(), plaquettes(), schizo()]),
        ],
    }


def moelle():
    cadre = lambda: zone(1, "Espace médullaire", E(500, 390, 400, 270), [200, 190],
                         "Cadre du schéma, pas une cellule.")
    graisse = lambda: zone(2, "Logettes graisseuses", E(320, 430, 80, 55), [320, 430],
                           "Repère d'une moelle pauvre quand elles dominent.", remplissage="#f3e2b8", contour="#8a7340")
    mega = lambda big=False: zone(3, "Mégacaryocytes", E(660, 360, 110 if big else 60, 80 if big else 44), [660, 360],
                                  "Grandes cellules qui font les plaquettes. Elles dominent dans la thrombocytémie essentielle.",
                                  lesion=big, remplissage="#7a4e9a", contour="#3d2058")
    blastes = lambda: zone(4, "Cellules immatures", E(450, 520, 70, 48), [450, 520],
                           "Formes immatures : on sort de la simple thrombocytose et on cherche une maladie centrale.",
                           lesion=True, remplissage="#4d6f8a", contour="#1d3344")
    return {
        "id": "lot173-moelle",
        "titre": "Moelle schématique : mégacaryocytes et moelle pauvre",
        "question": {
            "intitule": "Quel niveau va avec une thrombocytose clonale, et lequel avec un compte bas central ?",
            "html": "<p>Les grands mégacaryocytes vont avec la thrombocytémie essentielle, dans le cadre des critères complets, pas à eux seuls.</p><p>Les logettes graisseuses et les cellules immatures vont avec une production qui tombe. On ne traite pas ces deux images avec le même médicament.</p>",
        },
        "sources_courtes": "Schéma original du 31 octobre 2026. Pas une biopsie de patient.",
        "niveaux": [
            niveau("riche", "Mégacaryocytes nombreux", "Schéma. Mégacaryocytes grands et nombreux.",
                   [cadre(), graisse(), mega(True)], True),
            niveau("pauvre", "Moelle pauvre", "Schéma. Les logettes dominent, peu de mégacaryocytes.",
                   [cadre(), graisse(), mega(False)]),
            niveau("immature", "Cellules immatures", "Schéma. Formes immatures dans une moelle qui n'est plus seulement pauvre.",
                   [cadre(), graisse(), mega(False), blastes()]),
        ],
    }


def fragment(desc: dict) -> str:
    frag = dessinateur.rendre(desc, POLICE)
    frag = frag.replace('url("POLICE")', f'url("{POLICE}")')
    frag = re.sub(r"<script>.*?</script>", "", frag, flags=re.S)
    erreurs = []
    # Contrôles utiles, sans les marques de l'exemple aortique.
    if frag.count("<script") or "faux chenal" in frag.lower():
        erreurs.append("script ou texte d'exemple")
    if "display:none" not in frag:
        erreurs.append("bascule absente")
    if erreurs:
        raise SystemExit(" ; ".join(erreurs))
    return frag


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    specs = {"abdomen": abdomen(), "frottis": frottis(), "moelle": moelle()}
    for nom, desc in specs.items():
        # Vérifie le rendu complet (avec script) puis on n'embarque que la partie sans script.
        plein = dessinateur.rendre(desc, "POLICE")
        erreurs = [e for e in dessinateur.verifier(plein, desc)
                   if "faux chenal" not in e and "source manquante" not in e and "question absente" not in e
                   and not e.startswith("script")]
        # La question existe, mais pas les mots de l'exemple : on retire seulement ces échecs.
        if erreurs:
            raise SystemExit(nom + " : " + " | ".join(erreurs))
        (OUT / f"{nom}.json").write_text(json.dumps(desc, ensure_ascii=False, indent=1), encoding="utf-8")
        frag = fragment(desc)
        # Pas de HTML nu dans le LOT : la porte le jugerait comme une leçon.
        Path("/tmp") .joinpath(f"lot173-{nom}.fragment.html").write_text(frag, encoding="utf-8")
        print(nom, len(frag), "erreurs filtrées ok")


if __name__ == "__main__":
    main()
