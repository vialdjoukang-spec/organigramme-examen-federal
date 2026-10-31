#!/usr/bin/env python3
"""DX.1 à DX.10 de LOT_166. Usage : python3 dx_tous.py 1  (ou 0 pour tous)."""
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
from gabarit import btn, fen, p, page

LOT = ICI.parent
A = '<abbr title="information professionnelle suisse">AIPS</abbr>'
EASL = '<abbr title="European Association for the Study of the Liver">EASL</abbr>'
BTS = '<abbr title="British Thoracic Society">BTS</abbr>'
ESC = '<abbr title="European Society of Cardiology">ESC</abbr>'
LDH = '<abbr title="lactate déshydrogénase">LDH</abbr>'
SAAG = '<abbr title="gradient d&#x27;albumine entre le sérum et l&#x27;ascite">SAAG</abbr>'
PNN = '<abbr title="polynucléaires neutrophiles">PNN</abbr>'
RAPID = '<abbr title="renal, age, purulence, infection source, dietary factors">RAPID</abbr>'
FAST = '<abbr title="focused assessment with sonography for trauma">FAST</abbr>'

NOMS = {
    1: "Ascite de l'hypertension portale",
    2: "Épanchements de l'insuffisance cardiaque",
    3: "Épanchement parapneumonique et empyème",
    4: "Péritonite bactérienne spontanée",
    5: "Hémopéritoine et hémothorax",
    6: "Épanchement pleural malin",
    7: "Ascite maligne",
    8: "Épanchement péricardique et tamponnade",
    9: "Pleurésie tuberculeuse",
    10: "Ascite par hypoalbuminémie",
}

# une phrase qui sépare, pour la fenêtre des écarts
CLE = {
    1: "gradient d'albumine d'au moins 11 g/l et foie malade, sans neutrophiles au-dessus de 250",
    2: "transsudat de Light, souvent des deux côtés, et cœur défaillant",
    3: "pneumonie avec pus, ou pH pleural ≤ 7,2, ou glucose inférieur à 3,3 mmol/l",
    4: "ascite et polynucléaires neutrophiles au-dessus de 250 par mm³, sans perforation",
    5: "trauma ou choc, liquide libre dans les fenêtres, hémoglobine qui chute",
    6: "exsudat pleural, souvent unilatéral, cytologie sur 25 à 50 ml",
    7: "ascite à gradient sous 11 g/l et cellules tumorales",
    8: "lame péricardique, et compression clinique pour parler de tamponnade",
    9: "exsudat lymphocytaire cloisonné, exposition, biopsie ou culture",
    10: "albumine sérique basse, protéinurie ou dénutrition, gradient souvent bas",
}


def ecarts(n):
    moi = NOMS[n]
    paras = []
    for i, nom in NOMS.items():
        if i == n:
            continue
        paras.append(p(
            f"{moi} ne se confond pas avec {nom}. Ici, on retient : {CLE[n]}. "
            f"Là, on retient : {CLE[i]}. Le geste du jour change : diurétique, antibiotique, drain, bloc ou drainage du péricarde. "
            f"On n'utilise pas le numéro DX comme ordre d'urgence.",
            "1" if n in (2, 3, 6, 9) else "2",
        ))
    return fen(f"w-ecarts-{n}", "Écarts avec les neuf autres", "".join(paras))


def sources():
    lignes = (LOT / "evidence/INDEX.md").read_text(encoding="utf-8").splitlines()
    items = [f"<li>{ligne.split('. ', 1)[1]}</li>" for ligne in lignes if ligne.strip()]
    return "<ol class=\"sources\">\n" + "\n".join(items) + "\n</ol>"


def assembler(n, essentiel, ilots):
    nom = NOMS[n]
    # fenêtre d'écarts sur le point 7 si elle n'y est pas
    ile, fens = ilots["p7"]
    fens.append(ecarts(n))
    html = page(
        f"LOT_166_Phase_B_V0_DX.{n}.html",
        nom,
        f"DX.{n} de F2.18. Le rang E n'est pas le numéro. Texte du 31 octobre 2026.",
        essentiel,
        ilots,
        sources(),
        h2_dx=f"DX.{n} — {nom}",
    )
    out = LOT / f"LOT_166_Phase_B_V0_DX.{n}.html"
    out.write_text(html, encoding="utf-8")
    print(out.name, len(html.encode()))


def ilot(base_paras, fenetres):
    return ("".join(base_paras), fenetres)


def W(n, wid, titre, paras):
    return fen(f"w-{n}-{wid}", titre, "".join(paras))
