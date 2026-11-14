"""Quatre portes de l'armée : licence, âge selon Vial, modalité, OCR."""
import io
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw

from base import PROVENANCE

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "harnais" / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "harnais" / "scripts" / "legion"))
import attestations as A
import licences as L
import validate as V

_ENFANT = re.compile(
    r"\b(nouveau-n[ée]s?|nourrissons?|n[ée]onat\w*|infants?|neonat\w*|enfants?|"
    r"child(?:ren)?|p[ée]diatr\w*|boys?|girls?|gar[çc]ons?|filles?)\b",
    re.I,
)
_DATE = re.compile(r"\d{1,2}[./:-]\d{1,2}[./:-]\d{2,4}|\d{1,2}:\d{2}:\d{2}")
_ID = re.compile(r"\b\d{5,}\b")
_MOTS = re.compile(r"\b(patient|nom|name|dob|mrn|accession|hopital|hôpital|hospital|clinique)\b", re.I)
_PLANS = (
    ("axial", "axial"), ("coron", "coronal"), ("sagitt", "sagittal"),
    ("doppler", "doppler"), ("face", "face"), ("profil", "profil"),
)


def plan_de(texte):
    t = (texte or "").lower()
    for mot, canon in _PLANS:
        if mot in t:
            return canon
    return ""


def modalite_de(texte):
    t = (texte or "").lower()
    regles = (
        ("ECG", ("ecg", "électrocard", "electrocardi")),
        ("EEG", ("eeg", "électroenc", "electroenc")),
        ("CTG", ("cardiotoco", "ctg", "rythme cardiaque fœtal")),
        ("PSG", ("polysomno", "hypnogramme")),
        ("DERM", ("dermato", "dermatoscop")),
        ("FO", ("fond d'œil", "fond d'oeil", "rétino", "retino")),
        ("ENDO", ("endoscop", "gastroscop", "coloscop")),
        ("MN", ("scintigraph", " tep", "pet-ct", "médecine nucléaire")),
        ("US", ("échog", "echog", "ultrasound", "doppler")),
        ("IRM", ("irm", "mri")),
        ("TDM", ("tdm", "scanner", "computed tomography")),
        ("RX", ("radio", "radiograph", "x-ray", "cliché", "cliche")),
    )
    for nom, mots in regles:
        if any(m in t for m in mots):
            return nom
    return ""


def porte_licence(c):
    lic = c.get("license") or ""
    if not L.licence_ok(lic):
        return False, f"licence hors liste blanche ({lic or 'absente'})"
    if not L.auteur_ok(c.get("author")):
        return False, "auteur absent"
    if not (c.get("url") or "").startswith("http"):
        return False, "URL de source absente"
    bas = (c.get("url") or "").lower() + " " + (c.get("titre") or "").lower()
    for mot in ("eurorad", "radiopaedia", "padchest", "chexpert", "camus", "echonet"):
        if mot in bas:
            return False, f"source exclue ({mot})"
    return True, L.normaliser(lic)


def porte_age(c, besoin):
    age = c.get("age_ans")
    if age is None:
        age = A.age_ans(c.get("caption") or "")
        c["age_ans"] = age
    if c.get("sex") not in ("M", "F"):
        c["sex"] = A.sexe(c.get("caption") or "")
    if isinstance(age, int) and age < 18:
        return False, f"non adulte avéré ({age} ans)"
    if age is None and _ENFANT.search(c.get("caption") or ""):
        return False, "non adulte avéré dans la légende"
    blob = f"{besoin.get('dx') or ''} {besoin.get('cliche') or ''} {besoin.get('region') or ''}"
    if V.sexe_requis({"dx": blob, "cliche": besoin.get("cliche") or ""}, {"region": besoin.get("region") or ""}):
        if c.get("sex") not in ("M", "F"):
            return False, "bassin, sein ou organes génitaux : sexe non attesté"
    if isinstance(age, int) and age >= 18:
        return True, f"adulte {age} ans"
    return True, "âge non documenté (adulte d'aspect)"


def porte_modalite(c, besoin):
    attendu = besoin.get("modalite") or ""
    trouve = c.get("modalite") or modalite_de(f"{c.get('caption') or ''} {c.get('titre') or ''}")
    if attendu and trouve and attendu != trouve:
        return False, f"modalité {trouve} au lieu de {attendu}"
    plan_a = besoin.get("plan") or ""
    plan_t = c.get("plan") or plan_de(f"{c.get('caption') or ''} {c.get('titre') or ''}")
    if plan_a and plan_t and plan_a != plan_t:
        return False, f"plan {plan_t} au lieu de {plan_a}"
    c["modalite"] = trouve or attendu
    c["plan"] = plan_t or plan_a
    return True, "modalité et plan compatibles"


def _aplat(im, boite):
    x, y, w, h = boite
    x0, y0 = max(0, x - 2), max(0, y - 2)
    x1, y1 = min(im.width, x + w + 2), min(im.height, y + h + 2)
    anneau = []
    for yy in range(max(0, y0 - 6), min(im.height, y1 + 6)):
        for xx in (max(0, x0 - 6), min(im.width - 1, x1 + 5)):
            anneau.append(im.getpixel((xx, yy)))
    if not anneau:
        couleur = (0, 0, 0)
    else:
        couleur = tuple(sorted(p[i] for p in anneau)[len(anneau) // 2] for i in range(3))
    ImageDraw.Draw(im).rectangle([x0, y0, x1, y1], fill=couleur)


def masquer_ocr(im):
    """Aplat sur le texte identifiant. Un rognage ne remplace pas ce masque."""
    try:
        import pytesseract
    except ImportError:
        return im, 0, "pytesseract absent"
    data = pytesseract.image_to_data(im, lang="eng", output_type=pytesseract.Output.DICT)
    n = 0
    for i, mot in enumerate(data["text"]):
        mot = (mot or "").strip()
        if not mot:
            continue
        if _DATE.search(mot) or _ID.search(mot) or _MOTS.search(mot):
            _aplat(im, (data["left"][i], data["top"][i], data["width"][i], data["height"][i]))
            n += 1
    return im, n, "OCR exécuté"


def evaluer(c, besoin, octets):
    ok, raison = porte_licence(c)
    if not ok:
        return False, raison, None
    ok, raison = porte_age(c, besoin)
    if not ok:
        return False, raison, None
    ok, raison_m = porte_modalite(c, besoin)
    if not ok:
        return False, raison_m, None
    im = Image.open(io.BytesIO(octets)).convert("RGB")
    im, masques, ocr = masquer_ocr(im)
    im.thumbnail((1200, 1200))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=85)
    c["masques_ocr"] = masques
    c["ocr"] = ocr
    c["porte_age"] = raison
    return True, raison, buf.getvalue()


def ecrire_provenance(ident, cote, c, raison):
    PROVENANCE.mkdir(parents=True, exist_ok=True)
    doc = {
        "id": ident, "cote": cote, "source": c.get("source"), "url_directe": c.get("img_url") or "",
        "url": c.get("url") or "", "auteur": c.get("author") or "", "licence": L.normaliser(c.get("license") or ""),
        "age": c.get("age_ans"), "sexe": c.get("sex") or "", "mention": raison,
        "modalite": c.get("modalite") or "", "plan": c.get("plan") or "",
        "methode_rendu": c.get("pipeline") or "A", "masques_ocr": c.get("masques_ocr") or 0,
    }
    path = PROVENANCE / f"{ident}_{cote}.json"
    path.write_text(__import__("json").dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    return path
