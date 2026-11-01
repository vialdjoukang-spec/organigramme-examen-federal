#!/usr/bin/env python3
"""Schémas interactifs LOT_180. Les pages HTML restent hors dépôt (script)."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RACINE / "grok-LOTS-html" / "outils"))
from dessinateur.dessinateur import page, rendre, verifier  # noqa: E402

DEST = RACINE / "grok-LOTS-html" / "LOT_180" / "illustrations"
POLICE = RACINE / "grok-LOTS-html" / "outils" / "dessinateur" / "polices" / "AtkinsonHyperlegible-Regular.ttf"
HORS = RACINE / ".."  # jamais utilisé
TMP = Path("/tmp/lot180-dessins")
IGNORER = (
    "question absente",
    "source manquante dans la question : 2014",
    "source manquante dans la question : 2020",
    "source manquante dans la question : 2022",
    "source manquante dans la question : Radiopaedia",
)
VB = [0, 0, 1000, 760]
REP = {"texte": "D", "x": 48, "y": 56, "titre": "Droite de la patiente, à gauche de l'écran"}


def E(cx, cy, rx, ry):
    return {"type": "ellipse", "cx": cx, "cy": cy, "rx": rx, "ry": ry}


def S(sid, nom, numero, forme, badge, definition, remplissage, contour):
    return {
        "id": sid,
        "nom": nom,
        "numero": numero,
        "geometrie": forme,
        "remplissage": remplissage,
        "contour": contour,
        "epaisseur": 2,
        "badge": badge,
        "definition": definition,
    }


def N(nid, etiquette, note, structures, defaut=False):
    bloc = {
        "id": nid,
        "etiquette": etiquette,
        "note": note,
        "viewBox": VB,
        "repere": REP,
        "structures": structures,
    }
    if defaut:
        bloc["defaut"] = True
    return bloc


def Q(intitule, html):
    return {"intitule": intitule, "html": html}


UTERUS = {
    "id": "lot180-uterus",
    "titre": "Utérus gravide selon le trimestre",
    "sources_courtes": "Schéma pédagogique. Hauteur après 24 semaines et rendez-vous avant 10 semaines : suivi prénatal du 19 août 2021. Pression : hypertension de la grossesse, 25 juin 2019.",
    "question": Q(
        "Que vérifie-t-on quand l'utérus grandit ?",
        "<p>La datation se fait une fois. Après 24 semaines et 0 jour, la hauteur utérine se mesure à chaque visite d'une grossesse unique. Une pression de 140 ou de 90 n'est pas physiologique.</p>",
    ),
    "niveaux": [
        N("debut", "Premier trimestre", "L'utérus est encore dans le bassin. On date une fois.", [
            S("bassin", "Bassin", 1, E(500, 500, 280, 150), [230, 400],
              "Le fond utérin n'est pas encore un repère abdominal.", "#e7d5c4", "#5c564c"),
            S("uterus", "Utérus pelvien", 2, E(500, 500, 78, 56), [500, 480],
              "Petit. La datation échographique se fait une fois.", "#f3cfc3", "#a1262f"),
            S("ovaire", "Ovaire", 3, E(340, 470, 32, 22), [300, 450],
              "Repère latéral. La grossesse extra-utérine s'y cherche si ça saigne.", "#f7e2b5", "#8a5a00"),
            S("col", "Col", 4, E(500, 600, 26, 34), [560, 620],
              "Fermé dans une évolution qui se passe bien.", "#d5e8f5", "#1d4e89"),
        ], defaut=True),
        N("milieu", "Deuxième trimestre", "L'utérus quitte le bassin. La morphologie a sa fenêtre.", [
            S("uterus", "Utérus", 1, E(500, 400, 210, 160), [230, 230],
              "Le fond monte. La morphologie est détaillée dans le lot du dépistage.", "#f3cfc3", "#a1262f"),
            S("placenta", "Placenta", 2, E(640, 330, 70, 46), [700, 320],
              "On note son siège. Un saignement plus tard interdit le toucher avant de le savoir.", "#c9b6d6", "#5b3a73"),
            S("foetus", "Fœtus", 3, E(470, 430, 80, 100), [400, 450],
              "Les mouvements deviennent un sujet après 24 semaines et 0 jour.", "#b7e3d8", "#0f6e62"),
            S("col", "Col", 4, E(500, 610, 30, 36), [560, 640],
              "On ne le tâte pas pour rien.", "#d5e8f5", "#1d4e89"),
        ]),
        N("fin", "Troisième trimestre", "Après 24 semaines : hauteur, mouvements, présentation.", [
            S("uterus", "Utérus haut", 1, E(500, 360, 240, 200), [180, 160],
              "La hauteur se compare à la visite d'avant, pas à une norme inventée.", "#f3cfc3", "#a1262f"),
            S("placenta", "Placenta", 2, E(660, 280, 64, 42), [840, 220],
              "Son siège doit être connu avant un toucher tardif.", "#c9b6d6", "#5b3a73"),
            S("foetus", "Fœtus", 3, E(480, 390, 90, 130), [300, 500],
              "Une baisse des mouvements appelle le jour même.", "#b7e3d8", "#0f6e62"),
            S("tete", "Pôle céphalique", 4, E(500, 530, 52, 46), [700, 560],
              "La présentation s'ajoute au troisième trimestre.", "#f7e2b5", "#8a5a00"),
        ]),
    ],
}

PLACENTA = {
    "id": "lot180-placenta",
    "titre": "Interface placentaire et prééclampsie",
    "sources_courtes": "Schéma pédagogique. Seuils de pression et de protéinurie : 25 juin 2019. Prévention du soir : avis du 10.2.2019. Comprimé de 100 mg : information 51795.",
    "question": Q(
        "Quel chiffre n'attend pas le lendemain ?",
        "<p>Une pression au-dessus de 160 de systolique ou de 110 de diastolique. On mesure aussi la protéinurie, les plaquettes, la créatinine et le foie. La prévention du soir ne remplace pas cette urgence.</p>",
    ),
    "niveaux": [
        N("large", "Artère large", "Remodelage présent. La pression de la visite reste à mesurer.", [
            S("uterus", "Paroi utérine", 1, E(500, 400, 260, 180), [300, 280],
              "Le muscle entoure la chambre. On palpe le tonus plus tard, au travail.", "#f3cfc3", "#a1262f"),
            S("chambre", "Chambre intervilleuse", 2, E(500, 400, 150, 90), [620, 420],
              "Là où les échanges se font quand l'artère est ouverte.", "#f7e2b5", "#8a5a00"),
            S("artere", "Artère spiralée large", 3, E(500, 560, 36, 70), [560, 600],
              "Large : le débit placentaire est libre dans ce schéma.", "#d5e8f5", "#1d4e89"),
            S("foetus", "Côté fœtal", 4, E(500, 300, 70, 40), [500, 290],
              "La croissance se surveille par la hauteur, puis l'échographie si elle inquiète.", "#b7e3d8", "#0f6e62"),
        ], defaut=True),
        N("etroite", "Artère étroite", "Remodelage pauvre. Le risque précoce se discute avant 16 semaines.", [
            S("uterus", "Paroi utérine", 1, E(500, 400, 260, 180), [280, 260],
              "Même cadre. L'artère ne s'est pas ouverte.", "#f3cfc3", "#a1262f"),
            S("chambre", "Chambre moins perfusée", 2, E(500, 400, 130, 70), [600, 400],
              "Le débit est moindre. C'est le rationnel du dépistage du premier trimestre.", "#f8e0c0", "#8a5a12"),
            S("artere", "Artère étroite", 3, E(500, 570, 16, 60), [560, 590],
              "Étroite. La prophylaxie du soir vise ce risque, pas toutes les grossesses.", "#a1262f", "#5c1020"),
            S("mere", "Pression maternelle", 4, E(760, 480, 70, 40), [800, 470],
              "140 ou 90, confirmée, définit l'hypertension.", "#f6b7b7", "#a1262f"),
        ]),
        N("severe", "Signes sévères", "160 ou 110 : on ne renvoie pas au lendemain.", [
            S("uterus", "Paroi utérine", 1, E(500, 400, 260, 180), [200, 200],
              "Le cadre ne change pas. La gravité se lit sur la mère et le fœtus.", "#f3cfc3", "#a1262f"),
            S("artere", "Artère étroite", 2, E(500, 560, 16, 55), [280, 640],
              "Toujours étroite. La prévention ne traite pas la crise.", "#a1262f", "#5c1020"),
            S("foetus", "Fœtus petit", 3, E(470, 360, 50, 60), [360, 280],
              "Un retard de croissance peut être le critère de prééclampsie, sans protéinurie.", "#b7e3d8", "#0f6e62"),
            S("mere", "Atteinte maternelle", 4, E(760, 460, 80, 48), [840, 360],
              "Céphalée, phosphènes, barre épigastrique, plaquettes, foie ou rein.", "#5c1020", "#2a0810"),
        ]),
    ],
}

RHD = {
    "id": "lot180-rhd",
    "titre": "Passage d'hématies et prophylaxie anti-D",
    "sources_courtes": "Schéma pédagogique. Dose, dates et passage au-dessus de 4 ml : information 53609, lue le 1er novembre 2026.",
    "question": Q(
        "Quand injecte-t-on si la femme n'est pas immunisée ?",
        "<p>300 µg entre 28 et 30 semaines. Puis 300 µg dans les 72 heures si l'enfant est RhD positif, ou après un saignement et un geste. Au-delà de 72 heures, on injecte quand même.</p>",
    ),
    "niveaux": [
        N("passage", "Passage", "Des hématies fœtales peuvent entrer dans le sang maternel.", [
            S("mere", "Circulation maternelle", 1, E(280, 380, 140, 110), [220, 340],
              "Si la femme est RhD négative et non immunisée, ce passage peut la sensibiliser.", "#f6d0d2", "#a1262f"),
            S("placenta", "Placenta", 2, E(520, 400, 90, 70), [520, 360],
              "La barrière n'est pas étanche lors d'un saignement ou d'un geste.", "#c9b6d6", "#5b3a73"),
            S("hematie", "Hématie fœtale", 3, E(400, 390, 28, 20), [360, 400],
              "RhD positif possible. Le test de Kleihauer mesure un gros passage.", "#f7e2b5", "#8a5a00"),
            S("foetus", "Côté fœtal", 4, E(740, 400, 120, 100), [740, 340],
              "Le groupe de l'enfant se connaît à la naissance, pas des semaines après.", "#b7e3d8", "#0f6e62"),
        ], defaut=True),
        N("semaine", "28 à 30 semaines", "300 µg, dans la veine ou dans le muscle.", [
            S("mere", "Femme RhD négative", 1, E(300, 400, 150, 120), [180, 220],
              "Non immunisée. Une femme déjà immunisée se suit par le titre.", "#f6d0d2", "#a1262f"),
            S("anticorps", "Anti-D injecté", 2, E(520, 400, 70, 50), [520, 250],
              "300 µg, soit 1500 UI, entre la 28e et la 30e semaine.", "#d5e8f5", "#1d4e89"),
            S("placenta", "Placenta", 3, E(680, 420, 80, 56), [760, 300],
              "On répète toutes les 12 semaines après un geste, jusqu'à l'accouchement.", "#c9b6d6", "#5b3a73"),
            S("foetus", "Fœtus", 4, E(820, 500, 70, 60), [820, 620],
              "La prophylaxie prénatale s'ajoute à celle d'après la naissance.", "#b7e3d8", "#0f6e62"),
        ]),
        N("naissance", "Dans les 72 heures", "Puis tout de suite si le délai est passé. Dose en plus si le passage est gros.", [
            S("mere", "Mère", 1, E(280, 380, 140, 110), [170, 220],
              "300 µg au plus tard dans les 72 heures si l'enfant est RhD positif.", "#f6d0d2", "#a1262f"),
            S("cordon", "Sang du cordon", 2, E(520, 360, 70, 46), [520, 240],
              "Le groupe de l'enfant décide de l'injection postnatale.", "#f7e2b5", "#8a5a00"),
            S("passage", "Passage au-dessus de 4 ml", 3, E(680, 460, 80, 50), [780, 360],
              "Au-dessus de 4 ml d'érythrocytes fœtaux, une dose supplémentaire se calcule.", "#a1262f", "#5c1020"),
            S("dose", "Dose ajoutée", 4, E(820, 580, 60, 36), [820, 660],
              "10 µg pour 0,5 ml d'érythrocytes fœtaux, de préférence dans la veine.", "#d5e8f5", "#1d4e89"),
        ]),
    ],
}

DESSINS = {
    "uterus": UTERUS,
    "placenta": PLACENTA,
    "rhd": RHD,
}


def ecrire(desc: dict) -> Path:
    frag = rendre(desc, POLICE.as_uri())
    erreurs = [e for e in verifier(frag, desc) if e not in IGNORER and not e.startswith("source manquante")]
    if erreurs:
        raise SystemExit(desc["id"] + " : " + " | ".join(erreurs))
    TMP.mkdir(parents=True, exist_ok=True)
    dest = TMP / f"{desc['id']}.html"
    dest.write_text(page(frag, desc["titre"], POLICE.as_uri()), encoding="utf-8")
    return dest


def chrome() -> str:
    for c in ("/usr/bin/google-chrome-stable", "/usr/local/bin/google-chrome", "/usr/bin/google-chrome"):
        if Path(c).is_file():
            return c
    raise SystemExit("chrome absent")


def capturer(html: Path, png: Path, largeur: int, hauteur: int) -> None:
    png.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            chrome(), "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
            f"--window-size={largeur},{hauteur}", f"--screenshot={png}", html.as_uri(),
        ],
        check=True, capture_output=True, text=True,
    )


def niveau_deux(src: Path) -> Path:
    brut = src.read_text(encoding="utf-8")
    brut = brut.replace(' checked="checked"', "", 1)
    brut, n = re.subn(
        r'(<input class="sr" type="radio"[^>]*?)(/>)',
        lambda m: m.group(1) + ' checked="checked"' + m.group(2),
        brut,
        count=2,
    )
    # la première substitution a remis le niveau 1 ; on retire celle-là et on garde la deuxième
    # Plus simple : retirer toutes, puis cocher la deuxième radio.
    brut = src.read_text(encoding="utf-8").replace(' checked="checked"', "")
    vus = {"n": 0}

    def repl(m: re.Match) -> str:
        vus["n"] += 1
        extra = ' checked="checked"' if vus["n"] == 2 else ""
        return m.group(1) + extra + m.group(2)

    brut, n = re.subn(r'(<input class="sr" type="radio"[^>]*?)(/>)', repl, brut)
    if n < 2:
        raise SystemExit(f"radios introuvables dans {src.name}")
    dest = src.with_name(src.stem + "-niveau2.html")
    dest.write_text(brut, encoding="utf-8")
    return dest


def apercus_schemas() -> None:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import construire

    captures = DEST / "captures"
    TMP.mkdir(parents=True, exist_ok=True)
    for cle in ["Phase_A", *[f"DX.{i}" for i in range(1, 11)]]:
        corps = construire.schema(cle)
        html = TMP / f"schema-{cle}.html"
        html.write_text(
            "<!doctype html><html lang=\"fr\"><head><meta charset=\"utf-8\">"
            "<style>body{margin:12px;background:#fff;font-family:Verdana,sans-serif}"
            "svg{width:700px;height:180px}.etq{font-size:16px;fill:#1d2a30}"
            "figcaption{font-size:14px}</style></head><body>"
            f"{corps}</body></html>",
            encoding="utf-8",
        )
        capturer(html, captures / f"schema-{cle}.png", 780, 280)


def main() -> None:
    DEST.mkdir(parents=True, exist_ok=True)
    captures = DEST / "captures"
    for cle, desc in DESSINS.items():
        html = ecrire(desc)
        (DEST / f"{cle}.json").write_text(
            __import__("json").dumps(desc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        capturer(html, captures / f"{cle}.png", 1400, 1100)
        capturer(niveau_deux(html), captures / f"{cle}-niveau2.png", 1400, 1100)
        print(cle, "ok", html)
    apercus_schemas()
    print("schemas ok")


if __name__ == "__main__":
    main()
