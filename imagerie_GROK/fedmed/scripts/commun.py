#!/usr/bin/env python3
"""Décodage et réencodage octet-fidèle de PROGRESSION__FedMed.html."""
import base64
import hashlib
import html as htmlmod
import json
import re
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
DEPOT = RACINE.parents[1]
ORIGINAL = RACINE / "original" / "PROGRESSION__FedMed.html"
FENETRES = RACINE / "fenetres"
IMAGES = FENETRES / "images"
SQUELETTE = RACINE / "squelette" / "PROGRESSION__FedMed.html"
FUSION = RACINE / "fusion"
SORTIE = RACINE / "sortie" / "PROGRESSION__FedMed.html"
SIGNAUX = RACINE / "signaux"
CAPTURES = RACINE / "captures"
JOURNAL = RACINE / "JOURNAL.md"
SHA256_ATTENDU = "92efecc27ab16238b7a123e8b178e687704abbc3464c36dc16e477fc6f6362fc"
REF_INTERFACE = "origin/cursor/interface-didactique-ffbc"
PHRASE_NON_SOURCEE = "Interprétation de l'image (non sourcée)"

WL = re.compile(
    r"^(cc0( 1\.0)?|public domain|pd(-[\w-]+)?|cc[ -]by(-sa)?[ -]\d\.\d( [a-z]{2,})?|cc[ -]by(-sa)?)$",
    re.I,
)
RTS_RE = re.compile(r'(<script\b[^>]*data-emb="rts"[^>]*>)(.*?)(</script>)', re.S)
DON_RE = re.compile(r'(<script\b[^>]*id="donnees"[^>]*>)(.*?)(</script>)', re.S)
EMB_RE = re.compile(r'(<script\b[^>]*data-emb="(rts|sf|semio)"[^>]*>)(.*?)(</script>)', re.S)


def lire_original():
    data = ORIGINAL.read_text(encoding="utf-8")
    dig = hashlib.sha256(data.encode("utf-8")).hexdigest()
    if dig != SHA256_ATTENDU:
        raise SystemExit(f"sha256 inattendu : {dig}")
    return data


def dumps_donnees(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def dumps_html(page):
    return json.dumps(page, ensure_ascii=False).replace("<", "\\u003c")


def ouvrir_rts(data):
    m = RTS_RE.search(data)
    if not m:
        raise SystemExit("script data-emb=rts introuvable")
    page = json.loads(m.group(2))
    d = DON_RE.search(page)
    if not d:
        raise SystemExit("donnees du recensement introuvables")
    return m, page, d, json.loads(d.group(2))


def refermer(data, m, page, d, obj):
    page2 = page[: d.start(2)] + dumps_donnees(obj) + page[d.end(2) :]
    bloc = dumps_html(page2)
    return data[: m.start(2)] + bloc + data[m.end(2) :]


def est_fenetre(enr):
    im = (enr or {}).get("images") or {}
    patho = im.get("patho")
    fichier = patho.get("fichier") if isinstance(patho, dict) else ""
    return isinstance(fichier, str) and (
        fichier.startswith("data:image") or fichier.startswith("images/")
    )


def scinder_data_uri(uri):
    entete, b64 = uri.split(",", 1)
    mime = entete[5:].split(";")[0]
    brut = base64.b64decode(b64)
    if base64.b64encode(brut).decode("ascii") != b64:
        raise SystemExit("data URI non réversible")
    return mime, brut


def data_uri(mime, brut):
    return f"data:{mime};base64,{base64.b64encode(brut).decode('ascii')}"


def plain(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = htmlmod.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def ecrire_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def lire_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def licence_ok(licence):
    return bool(WL.match((licence or "").strip()))


def donnees_patient(blob):
    if not blob:
        return False
    marques = (
        b"PatientName",
        b"PatientID",
        b"PatientBirthDate",
        b"PatientSex",
        b"InstitutionName",
        b"ReferringPhysician",
    )
    return any(m in blob for m in marques)


def _sexe(jeton):
    t = (jeton or "").strip().lower()
    if t in {"f", "femme", "female", "woman", "girl", "fille", "féminin", "feminin"}:
        return "femme"
    if t in {"m", "h", "homme", "male", "man", "boy", "garçon", "garcon", "masculin"}:
        return "homme"
    return ""


def age_sexe_texte(texte):
    age = ""
    m = re.search(r"\b(\d{1,3})\s*(?:ans|an\b|years?[\s-]?old|year-old|\byo\b)", texte or "", re.I)
    if m and 0 < int(m.group(1)) < 120:
        age = f"{int(m.group(1))} ans"
    sex = ""
    m = re.search(
        r"\b(femme|woman|female|fille|féminin|feminin|homme|man|male|garçon|garcon|masculin|boy|girl)\b",
        texte or "",
        re.I,
    )
    if m:
        sex = _sexe(m.group(1))
    return age, sex


def age_sexe_manifeste(cote):
    if not isinstance(cote, dict):
        return "", ""
    age = ""
    brut = cote.get("age_ans")
    if isinstance(brut, (int, float)) and 0 < float(brut) < 120:
        age = f"{int(brut)} ans"
    elif isinstance(brut, str) and brut.strip():
        age, _ = age_sexe_texte(brut if "ans" in brut.lower() else brut + " ans")
        if not age:
            age = brut.strip()
    return age, _sexe(str(cote.get("sex") or cote.get("sexe") or ""))


def jpeg_taille(blob):
    if not blob or blob[:2] != b"\xff\xd8":
        return None
    i = 2
    n = len(blob)
    while i < n - 8:
        if blob[i] != 0xFF:
            i += 1
            continue
        marque = blob[i + 1]
        if marque in (0xC0, 0xC1, 0xC2):
            h = int.from_bytes(blob[i + 5 : i + 7], "big")
            w = int.from_bytes(blob[i + 7 : i + 9], "big")
            return w, h
        if marque in (0xD8, 0x01) or 0xD0 <= marque <= 0xD9:
            i += 2
            continue
        if i + 4 > n:
            break
        long = int.from_bytes(blob[i + 2 : i + 4], "big")
        if long < 2:
            break
        i += 2 + long
    return None


def maj_etat(lignes):
    texte = JOURNAL.read_text(encoding="utf-8")
    bloc = "<!-- ETAT:DEBUT -->\n" + "\n".join(lignes) + "\n<!-- ETAT:FIN -->"
    if "<!-- ETAT:DEBUT -->" in texte:
        texte = re.sub(r"<!-- ETAT:DEBUT -->.*?<!-- ETAT:FIN -->", bloc, texte, count=1, flags=re.S)
    else:
        texte = texte.replace("## État\n", "## État\n\n" + bloc + "\n", 1)
    JOURNAL.write_text(texte, encoding="utf-8")
