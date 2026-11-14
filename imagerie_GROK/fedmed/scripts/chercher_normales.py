#!/usr/bin/env python3
"""Cherche une normale libre, adulte, du même sexe si la région l'exige, même modalité."""
import argparse
import io
import os
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import commun as C
import age_documenter as AD

UA = AD.UA
WL = C.WL
SENSIBLES = ("bassin", "sein", "génit", "genit", "pelvis", "utér", "uter", "prostat", "ovari")


def get(url, binaire=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as rep:
        data = rep.read()
    return data if binaire else data.decode("utf-8", "replace")


def commons(requete, n=8):
    params = {
        "action": "query", "format": "json", "generator": "search", "gsrnamespace": "6",
        "gsrsearch": requete + " filetype:bitmap", "gsrlimit": str(n),
        "prop": "imageinfo", "iiprop": "url|extmetadata|size|mime", "iiurlwidth": "1024",
    }
    url = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params)
    try:
        data = json.loads(get(url))
    except Exception as exc:
        print("commons", type(exc).__name__, flush=True)
        return []
    pages = (data.get("query") or {}).get("pages") or {}
    out = []
    for page in pages.values():
        ii = (page.get("imageinfo") or [{}])[0]
        em = ii.get("extmetadata") or {}
        def val(k):
            return re.sub(r"<[^>]+>", " ", (em.get(k) or {}).get("value") or "")
        out.append({
            "titre": page.get("title") or "",
            "licence": val("LicenseShortName"),
            "auteur": val("Artist"),
            "description": val("ImageDescription"),
            "url": "https://commons.wikimedia.org/wiki/" + urllib.parse.quote((page.get("title") or "").replace(" ", "_")),
            "thumb": ii.get("thumburl") or ii.get("url") or "",
        })
    return out


def europepmc(requete):
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode({
        "query": requete + " OPEN_ACCESS:y", "format": "json", "resultType": "core", "pageSize": "5",
    })
    try:
        data = json.loads(get(url))
    except Exception as exc:
        print("europepmc", type(exc).__name__, flush=True)
        return []
    out = []
    for art in ((data.get("resultList") or {}).get("result") or []):
        if not art.get("isOpenAccess") or art.get("license") not in ("cc by", "cc by-sa", "cc0", "cc by-nc"):
            # la porte refusera NC ; on garde le texte pour ne pas télécharger
            pass
        licence = art.get("license") or ""
        texte = " ".join(str(art.get(k) or "") for k in ("title", "abstractText"))
        out.append({
            "titre": art.get("title") or "",
            "licence": licence,
            "auteur": art.get("authorString") or "",
            "description": texte,
            "url": "https://europepmc.org/article/" + (art.get("source") or "MED") + "/" + (art.get("id") or ""),
            "thumb": "",
        })
    return out


def incidence(texte):
    t = (texte or "").lower()
    for mot, canon in (
        ("longitud", "longitudinal"), ("coron", "coronal"), ("sagitt", "sagittal"),
        ("axial", "axial"), ("profil", "profil"), ("transvers", "axial"),
    ):
        if mot in t:
            return canon
    if re.search(r"\bde face\b|\bface view\b|\bpa view\b|\bap view\b", t):
        return "face"
    return ""


def modalite(texte):
    t = (texte or "").lower()
    if any(k in t for k in ("échog", "echog", "ultrasound", "ultrason")):
        return "us"
    if any(k in t for k in ("tep", "pet-ct", "pet/ct", "scintigraph")):
        return "mn"
    if any(k in t for k in ("irm", "mri")):
        return "irm"
    if any(k in t for k in ("tdm", "scanner", " ct ", "computed tomography")):
        return "tdm"
    if any(k in t for k in ("radio", "x-ray", "xray", "radiograph", "cliché", "cliche")):
        return "rx"
    return ""


ORGANES = (
    ("hépat", "liver"), ("hepat", "liver"), ("foie", "liver"),
    ("rein", "kidney"), ("rén", "kidney"), ("poumon", "lung"),
    ("thorax", "chest"), ("plevr", "chest"), ("céréb", "brain"),
    ("cereb", "brain"), ("encéph", "brain"), ("aorte", "aorta"),
    ("cœur", "heart"), ("coeur", "heart"), ("rachis", "spine"),
    ("sein", "breast"), ("pelv", "pelvis"), ("genou", "knee"),
)


def requete(fiche):
    im = fiche["enr"].get("images") or {}
    cherche = (im.get("a_chercher") or {}).get("normal") or ""
    tech = (im.get("patho") or {}).get("technique") or ""
    region = (fiche.get("contexte") or {}).get("region") or ""
    blob = f"{cherche} {tech} {region}".lower()
    mod = modalite(blob)
    mots = {
        "rx": "normal radiograph",
        "tdm": "normal CT",
        "irm": "normal MRI",
        "us": "normal ultrasound",
        "mn": "normal scintigraphy",
    }.get(mod, "normal")
    organe = next((en for fr, en in ORGANES if fr in blob), "")
    return f"{mots} {organe} normal anatomy".strip(), mod, tech


NORMALITE = re.compile(
    r"(normal anatomy|no injuries|unremarkable|no abnormality|without abnormality|"
    r"healthy volunteer|normal (ct|mri|ultrasound|radiograph|x-ray|chest|abdomen|brain|study|scan))",
    re.I,
)
CAS = re.compile(r"presents to|presenting with|was diagnosed|case report|emergency department", re.I)
PEDIATRIE = re.compile(
    r"\b(nouveau-né|nouveau né|nourrisson|enfant|pédiatri|pediatr|infant|neonat|child)\b",
    re.I,
)


def porte(candidat, tech_patho, region, sexe_patho, age_patho=""):
    raisons = []
    if PEDIATRIE.search(tech_patho or ""):
        raisons.append("pathologie pédiatrique, normale adulte non appariée")
    texte = ((candidat.get("description") or "") + " " + (candidat.get("titre") or ""))
    if not NORMALITE.search(texte) or (CAS.search(texte) and not re.search(r"normal anatomy|no injuries|unremarkable", texte, re.I)):
        raisons.append("normalité non attestée dans la légende")
    licence = candidat.get("licence") or ""
    if not C.licence_ok(licence):
        raisons.append("licence")
    if re.search(r"\bnc\b|noncommercial|non-commercial|by-nc", licence, re.I):
        raisons.append("licence non commerciale")
    age, sexe = AD.depuis_texte(candidat.get("description") or "")
    if not age or not sexe:
        raisons.append("âge ou sexe absent")
    elif int(re.search(r"\d+", age).group(0)) < 18:
        raisons.append("non adulte")
    elif age_patho:
        na = re.search(r"\d+", age_patho)
        if na and abs(int(na.group(0)) - int(re.search(r"\d+", age).group(0))) > 15:
            raisons.append("écart d'âge supérieur à 15 ans")
    if C.donnees_patient((candidat.get("description") or "").encode()):
        raisons.append("données patient")
    if any(m in (region or "").lower() for m in SENSIBLES):
        if not sexe_patho or (sexe and sexe != sexe_patho):
            raisons.append("sexe non concordant")
    mod_c = modalite((candidat.get("description") or "") + " " + (candidat.get("titre") or ""))
    mod_p = modalite(tech_patho)
    if not mod_c or (mod_p and mod_c != mod_p):
        raisons.append("modalité non attestée ou différente")
    if not candidat.get("thumb") and not candidat.get("octets"):
        raisons.append("pas de fichier image")
    inc_c = incidence((candidat.get("description") or "") + " " + (candidat.get("titre") or ""))
    inc_p = incidence(tech_patho)
    if inc_c and inc_p and inc_c != inc_p:
        raisons.append("incidence différente")
    if not (candidat.get("auteur") or "").strip():
        raisons.append("auteur absent")
    return raisons, age, sexe


def jpeg_sans_exif(blob):
    if C.donnees_patient(blob[:80000]):
        return None
    im = Image.open(io.BytesIO(blob)).convert("RGB")
    im.thumbnail((1024, 1024))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=85)
    return buf.getvalue()


def figures_europepmc(requete):
    """Une figure libre dont la légende porte déjà l'âge et le sexe."""
    import io as _io
    import zipfile
    api = "https://www.ebi.ac.uk/europepmc/webservices/rest/"
    url = api + "search?" + urllib.parse.urlencode({
        "query": requete + " OPEN_ACCESS:Y", "format": "json", "pageSize": "3", "resultType": "core",
    })
    try:
        data = json.loads(get(url))
    except Exception:
        return []
    rendus = []
    for art in ((data.get("resultList") or {}).get("result") or [])[:2]:
        pmcid = art.get("pmcid") or ""
        if not pmcid or not C.licence_ok(art.get("license") or ""):
            continue
        try:
            xml = get(api + pmcid + "/fullTextXML")
        except Exception:
            continue
        if "creativecommons.org/licenses/by" not in xml and "publicdomain/zero" not in xml:
            continue
        voulu = None
        for bloc in re.findall(r"<fig\b.*?</fig>", xml, flags=re.S)[:6]:
            cap = re.search(r"<caption[^>]*>(.*?)</caption>", bloc, flags=re.S)
            texte = re.sub(r"<[^>]+>", " ", cap.group(1) if cap else "")
            texte = re.sub(r"\s+", " ", texte)
            age, sexe = AD.depuis_texte(texte)
            if not (age and sexe and int(re.search(r"\d+", age).group(0)) >= 18 and NORMALITE.search(texte)):
                continue
            href = re.search(r'xlink:href="([^"]+)"', bloc)
            if not href:
                continue
            voulu = (os.path.basename(href.group(1)), texte)
            break
        if not voulu:
            continue
        try:
            blob = get(api + pmcid + "/supplementaryFiles?includeInlineImage=true", binaire=True)
            z = zipfile.ZipFile(_io.BytesIO(blob))
            octets = next(z.read(i) for i in z.infolist() if os.path.basename(i.filename) == voulu[0] and i.file_size < 8_000_000)
        except Exception:
            continue
        rendus.append({
            "titre": art.get("title") or pmcid,
            "licence": art.get("license") or "CC BY",
            "auteur": art.get("authorString") or "",
            "description": voulu[1][:500],
            "url": f"https://europepmc.org/articles/{pmcid}",
            "thumb": "",
            "octets": octets,
        })
        return rendus
    return rendus


def une(ident):
    fiche = C.lire_json(C.FENETRES / f"{ident}.json")
    fusion = C.lire_json(C.FUSION / f"{ident}.json")
    deja = fusion.get("recherche_normale") or {}
    if fusion.get("normal_ajoute") or (deja.get("ajoutee") or deja.get("refus")):
        return "déjà"
    q, mod, tech = requete(fiche)
    region = (fiche.get("contexte") or {}).get("region") or ""
    sexe_patho = (fusion["gabarit"].get("patho") or {}).get("sexe") or ""
    age_patho = (fusion["gabarit"].get("patho") or {}).get("age") or ""
    if PEDIATRIE.search(tech):
        fusion["recherche_normale"] = {"ajoutee": False, "requete": q, "refus": ["pathologie pédiatrique"]}
        C.ecrire_json(C.FUSION / f"{ident}.json", fusion)
        return "pédiatrique, non cherchée"
    candidats = commons(q) or commons(q.split()[0] + " " + q.split()[1] if len(q.split()) > 1 else q) 
    refus = []
    retenus = []
    for cand in candidats:
        raisons, age, sexe = porte(cand, tech, region, sexe_patho, age_patho)
        if cand.get("url") in DEJA:
            raisons.append("image déjà utilisée")
        if raisons:
            refus.append(cand.get("titre", "")[:40] + " : " + ", ".join(raisons))
            continue
        retenus.append((cand, age, sexe, "légende Commons"))
    if not retenus:
        for cand in figures_europepmc(q):
            raisons, age, sexe = porte(cand, tech, region, sexe_patho, age_patho)
            if raisons:
                refus.append("PMC " + (cand.get("titre") or "")[:24] + " : " + ", ".join(raisons))
                continue
            retenus.append((cand, age, sexe, "légende Europe PMC"))
            break
    for cand, age, sexe, preuve in retenus[:1]:
        try:
            brut = cand.get("octets") or get(cand["thumb"], binaire=True)
        except Exception:
            continue
        jpeg = jpeg_sans_exif(brut)
        if not jpeg:
            refus.append("exif patient")
            continue
        nom = f"{ident}_normal.jpg"
        (C.IMAGES / nom).write_bytes(jpeg)
        fusion["normal_ajoute"] = {
            "fichier": f"images/{nom}",
            "mime": "image/jpeg",
            "technique": tech,
            "credit": re.sub(r"\s+", " ", cand.get("auteur") or "")[:180],
            "licence": cand.get("licence") or "",
            "url": cand.get("url") or "",
        }
        info = fusion["gabarit"].setdefault("normal", {})
        info["age"] = age
        info["sexe"] = sexe
        info["refus"] = ""
        info["source"] = {
            "auteur": fusion["normal_ajoute"]["credit"],
            "licence": cand.get("licence") or "",
            "url": cand.get("url") or "",
            "credit": (cand.get("description") or "")[:240],
        }
        info["age_preuve"] = preuve
        fusion["recherche_normale"] = {"ajoutee": True, "requete": q}
        DEJA.add(cand.get("url") or "")
        fusion["signaux"] = [s for s in (fusion.get("signaux") or []) if "Normale" not in s]
        fusion["signaux"].append("Normale ajoutée après recherche.")
        C.ecrire_json(C.FUSION / f"{ident}.json", fusion)
        return "ajoutée " + (cand.get("titre") or "")[:60]
    fusion["recherche_normale"] = {"ajoutee": False, "requete": q, "refus": refus[:6]}
    C.ecrire_json(C.FUSION / f"{ident}.json", fusion)
    return "aucune (" + str(len(refus)) + " refus)"


DEJA = set()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limite", type=int, default=10)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    index = C.lire_json(C.FENETRES / "index.json")
    for ident in index["ids"]:
        doc = C.lire_json(C.FUSION / f"{ident}.json")
        url = (doc.get("normal_ajoute") or {}).get("url")
        if url:
            DEJA.add(url)
    sans = []
    for ident in index["sans_normale"]:
        fusion = C.lire_json(C.FUSION / f"{ident}.json")
        if fusion.get("normal_ajoute"):
            continue
        deja = fusion.get("recherche_normale") or {}
        if deja and not args.force and (deja.get("ajoutee") or deja.get("refus")):
            continue
        sans.append(ident)
        if len(sans) >= args.limite:
            break
    for ident in sans:
        print(ident, une(ident), flush=True)


if __name__ == "__main__":
    main()
