#!/usr/bin/env python3
"""Lit une leçon balisée et produit le HTML V8. Le texte est rédigé, pas généré par angles."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from habillage import abbr, bouton, cliche, ecrire, schema, sup, svg_boite  # noqa: E402

MARQUE = re.compile(r"\{\{([^}]+)\}\}")


def marques(s: str) -> str:
    def repl(m: re.Match) -> str:
        b = m.group(1)
        if b.startswith("sup:"):
            return sup(int(b.split(":")[1]))
        if b.startswith("abbr:"):
            _, sigle, titre = b.split(":", 2)
            return abbr(sigle, titre)
        if b.startswith("cliche:"):
            _, ancre, mot = b.split(":", 2)
            return cliche(ancre, mot)
        if b.startswith("btn:"):
            _, fid, mot = b.split(":", 2)
            return bouton(fid, mot)
        if b.startswith("auto:"):
            return m.group(0)
        raise SystemExit(f"marque inconnue : {b}")

    return MARQUE.sub(repl, s)


SCHEMAS_DX = {
    "[[TVP]]": ("tvp", [
        ("Veine souple", ("La lumière s'efface", ["Compression proximale", "Pas de caillot vu", "Question non close"], "#e8f7ef", "#1a7a50")),
        ("Veine dure", ("La lumière reste", ["Poplité, fémoral, iliaque", "Caillot proximal", "Anticoagulation lue"], "#f8e8e8", "#a1262f")),
        ("Délai", ("Quatre heures, 2020", ["Score probable de 2003", "Écho sinon D-dimères", "Image sous vingt-quatre heures"], "#e5f3fb", "#176fa0")),
    ]),
    "[[ANGIO]]": ("angio", [
        ("Voix", ("D'abord la gorge", ["Langue, lèvre, stridor", "Appeler avant le nom", "Ne pas renvoyer"], "#f8e8e8", "#a1262f")),
        ("Peau", ("Blanc et douloureux", ["Plus d'un jour", "Sans urticaire", "Pas l'allergie seule"], "#fff6df", "#8a5a00")),
        ("Crise", ("Deux produits lus", ["Inhibiteur par kilogramme", "Icatibant adulte", "51950 et 68263"], "#e5f3fb", "#176fa0")),
    ]),
    "[[OAP]]": ("oap", [
        ("Position", ("Assis, jambes pendantes", ["On n'allonge pas", "Oxygène", "Voix et sueurs"], "#f8e8e8", "#a1262f")),
        ("Poumons", ("Deux bases", ["Crépitants symétriques", "Pas un seul mollet", "Le godet vient après"], "#fff6df", "#8a5a00")),
        ("Injection", ("Lentement, 30630", ["Quarante milligrammes", "Puis réévaluation", "Quatre milligrammes par minute"], "#e5f3fb", "#176fa0")),
    ]),
    "[[NECROSE]]": ("necrose", [
        ("Douleur", ("Hors de proportion", ["Peau encore pauvre", "Effleurement intolérable", "On n'attend pas"], "#f8e8e8", "#a1262f")),
        ("Bulle", ("Signe possible", ["Bulle hémorragique", "Tache livide", "Le bloc ne se discute plus"], "#fff6df", "#8a5a00")),
        ("Appel", ("Chirurgie d'abord", ["À jeun", "Marquer le contour", "Pas de dose récitée"], "#e5f3fb", "#176fa0")),
    ]),
    "[[CAVE]]": ("cave", [
        ("Territoire", ("Pèlerine", ["Visage, cou, bras", "Pas les chevilles seules", "Collatérales du thorax"], "#f8e8e8", "#a1262f")),
        ("Image", ("Scanner, 2012", ["Lacout en fait la clé", "Obstacle et détours", "Résonance si elle tient"], "#e5f3fb", "#176fa0")),
        ("Geste", ("Lever l'obstacle", ["Asseoir si étouffement", "Pas le diurétique seul", "Cause souvent tumorale"], "#fff6df", "#8a5a00")),
    ]),
    "[[COEUR]]": ("coeur", [
        ("Cou", ("Jugulaires visibles", ["Tronc relevé", "Surcharge d'amont", "Les deux déclivités"], "#f8e8e8", "#a1262f")),
        ("Souffle", ("Oreillers et crépitants", ["Globale si les deux", "Droite si le poumon est clair", "Poids du matin"], "#fff6df", "#8a5a00")),
        ("Diurétique", ("Selon l'autorisation", ["Furosémide ou torasémide", "Pas à la place d'un caillot", "Potassium et poids"], "#e5f3fb", "#176fa0")),
    ]),
    "[[NEPHRO]]": ("nephro", [
        ("Définition", ("Deux critères, 2021", ["Plus de 3,5 grammes", "Albumine sous 30 g/l", "L'œdème n'est pas exigé"], "#e5f3fb", "#176fa0")),
        ("Visage", ("Paupières du matin", ["Urines mousseuses", "Godet blanc mou", "Pas un seul mollet"], "#fff6df", "#8a5a00")),
        ("Traitement", ("Sel, eau, puis diurétique", ["Spironolactone si échec", "Autorisation 27257", "Pas anti-inflammatoire"], "#e8f7ef", "#1a7a50")),
    ]),
    "[[FOIE]]": ("foie", [
        ("Ventre", ("Ascite", ["Matité et flot", "Angiomes stellaires", "Chevilles souvent avec"], "#fff6df", "#8a5a00")),
        ("Albumine", ("Le foie ne fabrique plus", ["Porte oncotique", "Et parfois l'amont", "Deux mécanismes"], "#e5f3fb", "#176fa0")),
        ("Diurétique", ("Plutôt à l'hôpital", ["Spironolactone selon Na/K", "Torasémide si choisi", "Foie sévère, lire l'interdit"], "#f8e8e8", "#a1262f")),
    ]),
    "[[VEINE]]": ("veine", [
        ("Classes", ("Zéro à six, 2020", ["Rien, puis télangiectasies", "Varices, y compris récidive", "La classe trois est l'œdème"], "#e8f7ef", "#1a7a50")),
        ("Peau", ("Pigment et ulcère", ["Pigment ou eczéma", "Sclérose, atrophie, couronne", "Ulcère guéri ou actif"], "#fff6df", "#8a5a00")),
        ("Preuve", ("Pas la classe seule", ["Écho-doppler", "Pouls avant le bas", "Caillot aigu d'abord"], "#f8e8e8", "#a1262f")),
    ]),
    "[[LYMPHE]]": ("lymphe", [
        ("Territoire", ("Dos du pied", ["Orteils compris", "Pli de Stemmer", "Écho pour écarter la veine"], "#e8f7ef", "#1a7a50")),
        ("Stades", ("Trois stades, 2002", ["Godet, régresse la nuit", "Permanent, plis marqués", "Peau épaisse"], "#fff6df", "#8a5a00")),
        ("Soin", ("Compression", ["Pierre angulaire lue", "Pas le diurétique seul", "Érysipèle à surveiller"], "#e5f3fb", "#176fa0")),
    ]),
}


def _onglets(spec):
    return [(lib, svg_boite(*args)) for lib, args in spec]


def injecter_schema(para: str) -> str:
    token = para.strip()
    if token == "[[PORTES]]":
        return schema(
            "portes",
            [
                ("Hydrostatique", svg_boite("Pression d'amont", ["Veine, cœur, obstacle", "Godet souvent mou"], "#f8e8e8", "#a1262f")),
                ("Oncotique", svg_boite("Albumine basse", ["Rein, foie, carence", "Œdème mou diffus"], "#e5f3fb", "#176fa0")),
                ("Inflammatoire", svg_boite("Fuite de paroi", ["Chaleur, douleur, bulles", "Ou bradykinine"], "#fff6df", "#8a5a00")),
                ("Lymphatique", svg_boite("Drainage arrêté", ["Dos du pied, orteils", "Stemmer, peau épaisse"], "#e8f7ef", "#1a7a50")),
            ],
        )
    if token == "[[ECHO]]":
        return schema(
            "echo",
            [
                ("Veine compressible", svg_boite("Sonde et compression", ["La lumière s'efface", "Pas de caillot proximal vu"], "#e8f7ef", "#1a7a50")),
                ("Veine incompressible", svg_boite("Caillot proximal", ["La lumière reste ouverte", "Anticoagulation et avis"], "#f8e8e8", "#a1262f")),
                ("Scanner cave", svg_boite("Coupes cervico-thoraciques", ["Obstacle et collatérales", "Lacout, 2012"], "#e5f3fb", "#176fa0")),
            ],
        )
    if token == "[[ARBRE]]":
        return schema(
            "arbre",
            [
                ("Voies aériennes", svg_boite("D'abord la voix", ["Langue, stridor, étouffement", "Traitement avant le nom"], "#f8e8e8", "#a1262f")),
                ("Un seul côté", svg_boite("Jambe aiguë", ["Thrombose ou nécrose", "Écho ou chirurgie"], "#fff6df", "#8a5a00")),
                ("Les deux côtés", svg_boite("Surcharge ou carence", ["Cœur, rein, foie", "Poids, albumine, souffle"], "#e5f3fb", "#176fa0")),
                ("Pied et orteils", svg_boite("Lymphe", ["Stemmer, dos du pied", "Compression, pas le diurétique seul"], "#e8f7ef", "#1a7a50")),
            ],
        )
    if token == "[[WELLS]]":
        return schema(
            "wells",
            [
                ("Items à un point", svg_boite("Neuf items, 2003", ["Cancer, plâtre, alitement", "Mollet, godet, antécédent"], "#e5f3fb", "#176fa0")),
                ("Moins deux", svg_boite("Autre diagnostic", ["Aussi probable", "On soustrait deux points"], "#fff6df", "#8a5a00")),
                ("Deux niveaux", svg_boite("Probable ou non", ["Deux points ou plus", "Un point ou moins"], "#f8e8e8", "#a1262f")),
            ],
        )
    if token == "[[CEAP]]":
        return schema(
            "ceap",
            [
                ("C0 à C2", svg_boite("Signes visibles", ["C0 rien", "C1 télangiectasies", "C2 varices"], "#e8f7ef", "#1a7a50")),
                ("C3 et C4", svg_boite("Œdème et peau", ["C3 œdème seulement", "C4a pigment, C4b sclérose", "C4c couronne"], "#fff6df", "#8a5a00")),
                ("C5 et C6", svg_boite("Ulcère", ["C5 guéri", "C6 actif", "C6r récidive"], "#f8e8e8", "#a1262f")),
            ],
        )
    if token in SCHEMAS_DX:
        nom, onglets = SCHEMAS_DX[token]
        return schema(nom, _onglets(onglets))
    return para


SOURCES = [
    "Depairon, angiologie, Centre hospitalier universitaire vaudois, Lausanne, 3 juin 2021.",
    "Bongard, Revue Médicale Suisse, 2002, lymphœdème.",
    "Stehlin et Ribi, Revue Médicale Suisse, 8 avril 2020, angiœdème héréditaire.",
    "Lacout et collaborateurs, Journal de radiologie diagnostique et interventionnelle, juillet-août 2012.",
    "Furosémide comprimés, autorisation 30629, corpus du 8 octobre 2026.",
    "Furosémide injectable, autorisation 30630, corpus du 8 octobre 2026.",
    "Spironolactone, autorisation 27257, corpus du 8 octobre 2026.",
    "Torasémide, autorisation 68924, corpus du 8 octobre 2026.",
    "Icatibant, autorisation 68263, corpus du 8 octobre 2026.",
    "Concentré d'inhibiteur de C1, autorisation 51950, corpus du 8 octobre 2026.",
    "Rivaroxaban, autorisation 68552, corpus du 8 octobre 2026.",
    "Énoxaparine, autorisation 49456, corpus du 8 octobre 2026.",
    "Guidance britannique numéro 158, 2012, amendée en 2020, score de Wells de 2003. Source du Royaume-Uni, non déguisée.",
    "Lurie et al., classification clinique, étiologique, anatomique et physiopathologique, 2020.",
    "Guide international des maladies glomérulaires, Kidney International, 2021.",
]


def lire(path: Path) -> dict:
    brut = path.read_text(encoding="utf-8")
    meta: dict[str, str] = {}
    lignes = brut.splitlines()
    i = 0
    while i < len(lignes) and lignes[i].startswith("@"):
        k, v = lignes[i][1:].split(":", 1)
        meta[k.strip()] = v.strip()
        i += 1
    corps = "\n".join(lignes[i:]).strip()
    blocs = re.split(r"\n(?=## )", corps)
    essentiel, urgence = [], ""
    points = []
    for bloc in blocs:
        bloc = bloc.strip()
        if not bloc:
            continue
        tete, _, reste = bloc.partition("\n")
        if tete.startswith("## essentiel"):
            essentiel = [marques(p.strip()) for p in reste.splitlines() if p.strip()]
            continue
        if tete.startswith("## urgence"):
            urgence = marques(" ".join(reste.split()))
            continue
        if not tete.startswith("## "):
            raise SystemExit(f"bloc sans titre : {tete[:80]}")
        parts = [x.strip() for x in tete[3:].split("|")]
        if len(parts) != 4:
            raise SystemExit(f"titre de point mal formé : {tete}")
        pid, classe, titre, sommaire = parts
        fiche = ""
        fenetres = []
        courant = None
        para: list[str] = []

        for ligne in reste.splitlines():
            if ligne.startswith("FICHE:"):
                fiche = marques(ligne[len("FICHE:") :].strip())
                continue
            if ligne.startswith("### "):
                courant = {"id": "", "titre": ligne[4:].strip(), "paragraphes": []}
                fenetres.append(courant)
                continue
            if not ligne.strip():
                continue
            if courant is None:
                raise SystemExit(f"texte hors fenêtre dans {pid} : {ligne[:80]}")
            courant["paragraphes"].append(marques(ligne.strip()))
        if not fiche:
            raise SystemExit(f"FICHE manquante : {pid}")
        for n, f in enumerate(fenetres, 1):
            f["id"] = f"{pid}f{n}"
            for i, para in enumerate(f["paragraphes"]):
                f["paragraphes"][i] = injecter_schema(para)
        if len(fenetres) > 1:
            liens = " ".join(bouton(f["id"], f["titre"]) for f in fenetres[1:])
            fenetres[0]["paragraphes"].insert(0, liens)
        fiche = re.sub(
            r"\{\{auto:([^}]+)\}\}",
            lambda m: bouton(fenetres[0]["id"], m.group(1)) if fenetres else m.group(1),
            fiche,
        )
        if fenetres and "popovertarget" not in fiche:
            fiche = fiche + " " + bouton(fenetres[0]["id"], "Développer")
        points.append(
            {
                "id": pid,
                "classe": classe,
                "titre": titre,
                "sommaire": sommaire,
                "fiche": fiche,
                "fenetres": fenetres,
            }
        )
    ids = [p["id"] for p in points]
    if ids != [f"p{n}" for n in range(1, 15)]:
        raise SystemExit(f"points attendus p1–p14, trouvé {ids}")
    return {
        "fichier": meta["fichier"],
        "title": meta["title"],
        "h1": meta["h1"],
        "sous": meta["sous"],
        "fin": meta["fin"],
        "essentiel": essentiel,
        "urgence": urgence,
        "points": points,
        "sources": SOURCES,
    }


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print("usage: parser_lecon.py <fichier.lecon>")
        return 2
    lecon = lire(Path(argv[0]))
    ecrire(lecon)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
