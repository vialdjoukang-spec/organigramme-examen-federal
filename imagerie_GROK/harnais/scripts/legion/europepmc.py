"""Europe PMC : la licence de l'article est lue avant toute figure."""
import io, os, re, zipfile, urllib.parse
import xml.etree.ElementTree as ET

import licences as L
from _common import get, get_json

API = "https://www.ebi.ac.uk/europepmc/webservices/rest/"
XLINK = "{http://www.w3.org/1999/xlink}href"
_ORDRE = {"webp": 0, "png": 1, "jpg": 2, "jpeg": 2, "gif": 3}


def _search_url(requete, n):
    q = requete.strip()
    if "OPEN_ACCESS" not in q.upper():
        q = q + " OPEN_ACCESS:Y"
    return API + "search?" + urllib.parse.urlencode({
        "query": q, "format": "json", "pageSize": str(n),
        "resultType": "core", "cursorMark": "*",
    })


def licence_xml(texte):
    m = re.search(r"https?://creativecommons\.org/(licenses|publicdomain)/([a-z0-9./-]+)", texte or "", re.I)
    if not m:
        if re.search(r"public domain", texte or "", re.I):
            return "Public domain", ""
        return "", ""
    url = m.group(0).rstrip("/")
    kind = m.group(2).strip("/")
    if kind.startswith("zero") or "publicdomain/zero" in url:
        return "CC0 1.0", "https://creativecommons.org/publicdomain/zero/1.0/"
    code, _, version = kind.partition("/")
    noms = {
        "by": "CC BY", "by-sa": "CC BY-SA", "by-nc": "CC BY-NC", "by-nd": "CC BY-ND",
        "by-nc-sa": "CC BY-NC-SA", "by-nc-nd": "CC BY-NC-ND",
    }
    nom = noms.get(code.lower(), code)
    if version:
        nom = nom + " " + version.split("/")[0]
    return nom, url


def _choisir_href(graphics):
    """Préfère le cliché (content-type image) au timbre, puis le format le plus net."""
    if not graphics:
        return ""
    def rang(g):
        href = g[1].lower()
        ext = href.rsplit(".", 1)[-1]
        type_rang = 0 if g[0] == "image" else 1
        return (type_rang, _ORDRE.get(ext, 9))
    return sorted(graphics, key=rang)[0][1]


def figures_xml(texte, max_fig=2):
    try:
        root = ET.fromstring(texte)
    except ET.ParseError:
        return []
    figs = []
    for fig in root.iter("fig"):
        cap = fig.find("caption")
        caption = "".join(cap.itertext()) if cap is not None else ""
        graphics = []
        for g in fig.iter("graphic"):
            href = g.get(XLINK) or ""
            if href:
                graphics.append((g.get("content-type") or "", os.path.basename(href)))
        href = _choisir_href(graphics)
        if href:
            figs.append({"href": href, "caption": re.sub(r"\s+", " ", caption).strip()})
        if len(figs) >= max_fig:
            break
    return figs


def _extraire(blob, noms):
    voulu = set(noms)
    out = {}
    try:
        z = zipfile.ZipFile(io.BytesIO(blob))
    except zipfile.BadZipFile:
        return out
    for info in z.infolist():
        base = os.path.basename(info.filename)
        if base not in voulu or info.file_size > 15_000_000:
            continue
        if info.filename.startswith("/") or ".." in info.filename.split("/"):
            continue
        out[base] = z.read(info)
    return out


class Reseau:
    def search(self, requete, n):
        d = get_json(_search_url(requete, n))
        return ((d.get("resultList") or {}).get("result") or [])

    def xml(self, pmcid):
        return get(API + pmcid + "/fullTextXML")

    def zip(self, pmcid):
        return get(API + pmcid + "/supplementaryFiles?includeInlineImage=true", binary=True)


def articles(requete, n=2, max_figures=2, client=None):
    """Filtre la licence sur la notice, puis la confirme dans le XML, puis seulement télécharge."""
    client = client or Reseau()
    brut = client.search(requete, n)
    rendus = []
    for art in brut:
        pmcid = art.get("pmcid") or ""
        courte = L.normaliser(art.get("license") or "")
        base = {
            "pmcid": pmcid,
            "author": art.get("authorString") or "",
            "title": art.get("title") or "",
            "source_url": f"https://europepmc.org/articles/{pmcid}" if pmcid else "",
            "license_notice": courte,
        }
        if not L.licence_ok(courte):
            base.update({"accepte_licence": False, "license": courte,
                         "raison": f"licence d'article hors liste ({courte or 'absente'})"})
            rendus.append(base)
            continue
        if not pmcid:
            base.update({"accepte_licence": False, "license": courte, "raison": "PMCID absent"})
            rendus.append(base)
            continue
        xml = client.xml(pmcid)
        lic, url = licence_xml(xml if isinstance(xml, str) else xml.decode("utf-8", "replace"))
        if not L.licence_ok(lic):
            base.update({"accepte_licence": False, "license": lic or courte,
                         "raison": f"licence XML hors liste ({lic or 'absente'})"})
            rendus.append(base)
            continue
        texte = xml if isinstance(xml, str) else xml.decode("utf-8", "replace")
        figs = figures_xml(texte, max_figures)
        base.update({"accepte_licence": True, "license": lic, "license_url": url,
                     "figures": figs,
                     "raison": "" if figs else "article libre sans figure"})
        rendus.append(base)
    return rendus


def charger_figures(art, client=None):
    """Archive des figures, seulement après le filtre de licence."""
    if not art.get("accepte_licence") or not art.get("figures"):
        return art
    client = client or Reseau()
    blob = client.zip(art["pmcid"])
    fichiers = _extraire(blob, [f["href"] for f in art["figures"]])
    for fig in art["figures"]:
        fig["octets"] = fichiers.get(fig["href"])
    return art
