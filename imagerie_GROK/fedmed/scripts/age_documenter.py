#!/usr/bin/env python3
"""Affiche l'âge et le sexe quand un texte les atteste. Ne les invente pas."""
import argparse
import hashlib
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import commun as C

CACHE = Path("/tmp/fedmed-http")
UA = "FedMedBot/1.0 (atlas pedagogique; pas de donnee patient) python-urllib"
AGE = re.compile(
    r"\b(\d{1,3})\s*(?:ans|an\b|years?[-\s]?old|year-old|\byo\b|-year-old|year old)\b",
    re.I,
)
SEXE = re.compile(
    r"\b(femme|woman|female|fille|girl|féminin|feminin|homme|man|male|boy|garçon|garcon|masculin)\b",
    re.I,
)


def lire(url):
    CACHE.mkdir(parents=True, exist_ok=True)
    cle = CACHE / hashlib.sha1(url.encode()).hexdigest()
    if cle.is_file() and cle.stat().st_size:
        return cle.read_text(encoding="utf-8", errors="replace")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=25) as rep:
        data = rep.read().decode("utf-8", "replace")
    cle.write_text(data, encoding="utf-8")
    return data


def depuis_texte(texte):
    age = sexe = ""
    m = AGE.search(texte or "")
    if m and 0 < int(m.group(1)) < 120:
        age = f"{int(m.group(1))} ans"
    m = SEXE.search(texte or "")
    if m:
        sexe = C._sexe(m.group(1))
    return age, sexe


def europepmc(texte):
    doi = re.search(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", texte or "", re.I)
    pmc = re.search(r"PMC\d{3,}", texte or "")
    if doi:
        query = "DOI:" + doi.group(0).rstrip(").")
    elif pmc:
        query = "PMCID:" + pmc.group(0)
    else:
        return ""
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode({
        "query": query, "format": "json", "resultType": "core", "pageSize": "1",
    })
    try:
        data = json.loads(lire(url))
    except Exception:
        return ""
    res = ((data.get("resultList") or {}).get("result") or [])
    if not res:
        return ""
    art = res[0]
    return " ".join(str(art.get(k) or "") for k in ("title", "abstractText"))


def commons(url):
    if "commons.wikimedia.org" not in (url or "") and "File:" not in (url or ""):
        return ""
    titre = urllib.parse.unquote(url.split("/wiki/")[-1]) if "/wiki/" in url else ""
    if not titre.startswith("File:"):
        return ""
    api = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({
        "action": "query", "titles": titre, "prop": "imageinfo",
        "iiprop": "extmetadata", "format": "json",
    })
    try:
        data = json.loads(lire(api))
    except Exception:
        return ""
    pages = ((data.get("query") or {}).get("pages") or {}).values()
    for page in pages:
        em = ((page.get("imageinfo") or [{}])[0].get("extmetadata") or {})
        return " ".join(
            re.sub(r"<[^>]+>", " ", (em.get(k) or {}).get("value") or "")
            for k in ("ImageDescription", "Artist", "Credit")
        )
    return ""


def completer(cote, textes, reseau):
    age, sexe = depuis_texte(" ".join(textes))
    preuve = "légende ou crédit" if age or sexe else ""
    if reseau and (not age or not sexe):
        extra = europepmc(" ".join(textes))
        if not extra:
            extra = commons((cote.get("source") or {}).get("url") or "")
        a2, s2 = depuis_texte(extra)
        if a2 and not age:
            age, preuve = a2, "Europe PMC ou Commons"
        if s2 and not sexe:
            sexe = s2
            preuve = preuve or "Europe PMC ou Commons"
    return age, sexe, preuve


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limite", type=int, default=0)
    ap.add_argument("--reseau", action="store_true")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    index = C.lire_json(C.FENETRES / "index.json")
    n = 0
    for ident in index["ids"]:
        dest = C.FUSION / f"{ident}.json"
        fusion = C.lire_json(dest)
        if fusion.get("age_sexe") and not args.force:
            continue
        fiche = C.lire_json(C.FENETRES / f"{ident}.json")
        im = fiche["enr"].get("images") or {}
        g = fusion["gabarit"]
        for cote in ("normal", "patho"):
            bloc = im.get(cote) if isinstance(im.get(cote), dict) else {}
            info = g.get(cote) or {}
            textes = [
                (bloc or {}).get("credit") or "",
                (bloc or {}).get("technique") or "",
                (info.get("source") or {}).get("credit") or "",
                (info.get("source") or {}).get("auteur") or "",
                (info.get("source") or {}).get("url") or "",
            ]
            if cote == "normal" and fusion.get("normal_ajoute"):
                textes.append(fusion["normal_ajoute"].get("credit") or "")
                textes.append(fusion["normal_ajoute"].get("technique") or "")
            age, sexe, preuve = completer(info, textes, args.reseau)
            if age:
                info["age"] = age
            if sexe:
                info["sexe"] = sexe
            if preuve:
                info["age_preuve"] = preuve
            g[cote] = info
        fusion["gabarit"] = g
        fusion["age_sexe"] = True
        C.ecrire_json(dest, fusion)
        n += 1
        if args.limite and n >= args.limite:
            break
        if n % 20 == 0:
            print(n, flush=True)
    print("documentés", n)


if __name__ == "__main__":
    main()
