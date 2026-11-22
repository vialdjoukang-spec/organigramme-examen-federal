"""OCR du texte brûlé, puis masquage. L'âge et le sexe restent. Le reste patient est détruit."""
import os, re, shutil

_ETIQUETTE = {
    "patient", "patients", "nom", "name", "dob", "mrn", "id", "identifiant",
    "hopital", "hôpital", "hospital", "clinique", "clinic", "chu", "accession",
    "dossier", "née", "nee", "birth",
}
_AGE_VOISIN = re.compile(r"\b(ans|yo|y/o|year|years|yrs?)\b", re.I)
_SEXE = re.compile(
    r"^(males?|females?|hommes?|femmes?|wom[ae]n|girls?|boys?|féminin|feminin|masculin)$",
    re.I,
)
_DATE = re.compile(r"\d{1,2}[./-]\d{1,2}[./-]\d{2,4}")


def tesseract_disponible():
    return shutil.which("tesseract") is not None


def _mot(token):
    return token.strip(" ,;:()[]{}").lower()


def mots_a_masquer(mots):
    """Indices à noircir. Ne renvoie pas les chaînes : l'appelant détruit les pixels."""
    bas = [_mot(m) for m in mots]
    conserve = set()
    for i, b in enumerate(bas):
        if re.fullmatch(r"\d{1,3}", b):
            voisins = " ".join(bas[max(0, i - 2):i + 3])
            if _AGE_VOISIN.search(voisins):
                conserve.add(i)
        if _SEXE.match(b):
            conserve.add(i)
        if b in ("r", "l"):
            conserve.add(i)
    for i, b in enumerate(bas):
        if b in ("f", "m", "h"):
            conserve.add(i)
    etiquette = any(b in _ETIQUETTE for b in bas)
    date = bool(_DATE.search(" ".join(mots)))
    masquer = set()
    for i, b in enumerate(bas):
        if i in conserve or not b:
            continue
        ident = b in _ETIQUETTE or bool(re.fullmatch(r"\d{5,}", b)) or bool(_DATE.fullmatch(b))
        if ident or etiquette or date:
            masquer.add(i)
    return masquer


def masquer_image(im, boites):
    from PIL import ImageDraw
    d = ImageDraw.Draw(im)
    for b in boites:
        x, y, w, h = b["l"], b["t"], b["w"], b["h"]
        d.rectangle([x - 2, y - 2, x + w + 2, y + h + 2], fill=(0, 0, 0))
    return im


def _lignes(data):
    groupes = {}
    n = len(data.get("text") or [])
    for i in range(n):
        txt = (data["text"][i] or "").strip()
        if not txt:
            continue
        try:
            if int(float(data["conf"][i])) < 0:
                continue
        except (TypeError, ValueError):
            continue
        cle = (data["block_num"][i], data["par_num"][i], data["line_num"][i])
        groupes.setdefault(cle, []).append({
            "text": txt,
            "l": int(data["left"][i]), "t": int(data["top"][i]),
            "w": int(data["width"][i]), "h": int(data["height"][i]),
        })
    lignes = []
    for mots in groupes.values():
        lignes.append(mots)
    return lignes


def ocr(path):
    if not tesseract_disponible():
        return None
    import pytesseract
    from PIL import Image
    im = Image.open(path).convert("RGB")
    lang = "eng+fra"
    try:
        data = pytesseract.image_to_data(im, lang=lang, output_type=pytesseract.Output.DICT)
    except Exception:
        data = pytesseract.image_to_data(im, lang="eng", output_type=pytesseract.Output.DICT)
    return im, _lignes(data)


def anonymiser(path, dest):
    """Masque les identifiants. Échoue fermé si tesseract est absent."""
    if not tesseract_disponible():
        return {"ok": False, "raison": "tesseract absent : anonymisation non vérifiée", "masques": 0}
    lu = ocr(path)
    if lu is None:
        return {"ok": False, "raison": "tesseract absent : anonymisation non vérifiée", "masques": 0}
    im, lignes = lu
    boites = []
    for mots in lignes:
        idx = mots_a_masquer([m["text"] for m in mots])
        for i in idx:
            boites.append(mots[i])
    if boites:
        masquer_image(im, boites)
    # fraction noircie : refuse un masque qui mangerait le cliché
    larg, haut = im.size
    if larg * haut and boites:
        aire = sum(max(0, b["w"]) * max(0, b["h"]) for b in boites)
        if aire / float(larg * haut) > 0.40:
            return {"ok": False, "raison": "masque trop étendu, image inutilisable", "masques": len(boites)}
    os.makedirs(os.path.dirname(os.path.abspath(dest)), exist_ok=True)
    tmp = dest + ".png"
    im.save(tmp)
    from normalize import normalize
    normalize(tmp, dest)
    os.remove(tmp)
    return {"ok": True, "raison": "OCR exécuté", "masques": len(boites)}
