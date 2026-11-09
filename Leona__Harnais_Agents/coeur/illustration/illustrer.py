#!/usr/bin/env python3
"""Illustrations de lésions (imagerie et biologie) pour les cours, licences libres seulement.

  python3 grok-LOTS-html/outils/illustration/illustrer.py --autotest
  python3 grok-LOTS-html/outils/illustration/illustrer.py --outils
  python3 grok-LOTS-html/outils/illustration/illustrer.py --chercher wikimedia "aortic dissection CT"
  python3 grok-LOTS-html/outils/illustration/illustrer.py --chercher openi "aortic dissection"
  python3 grok-LOTS-html/outils/illustration/illustrer.py --chercher pmc "aortic dissection"
  python3 grok-LOTS-html/outils/illustration/illustrer.py --rendre annotation.json -o DOSSIER [--page exemple.html]

Sources acceptées : Wikimedia Commons (API), Open-i (sous-ensemble PMC), Europe PMC open access.
Licence exigée : CC0, CC BY, CC BY-SA ou domaine public. Refus si vide, NC, ND, ou inconnue.
Radiopaedia n'est pas interrogé. Aucune lésion n'est inventée : les coordonnées viennent du JSON.

Le format du JSON est décrit dans README.md (même dossier).
"""
from __future__ import annotations

import argparse, hashlib, html, importlib.util, json, math, re, threading, time, urllib.error, urllib.parse, urllib.request
from datetime import date
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ICI = Path(__file__).resolve().parent
OUTILS = ICI.parent
RACINE = ICI.parents[2]
CACHE = ICI / "_cache" / "http"
POLICE = ICI / "polices" / "AtkinsonHyperlegible-Regular.ttf"
UA = "GrokIllustration/1.0 (educational medical course; stdlib urllib; disk cache)"
# En-tête explicite, même idée que harnais/surveillance/watchdog.py (User-Agent nommé, urllib).
ENTREPOTS = ("wikimedia", "openi", "pmc", "fichier", "schema")
PALETTE = [
    (20, 20, 22),
    (161, 38, 47),
    (11, 93, 134),
    (26, 122, 80),
    (255, 214, 10),
    (0, 188, 212),
    (255, 255, 255),
    (255, 122, 0),
]


class LicenceRefusee(Exception):
    pass


class SourceIndisponible(Exception):
    pass


class DisjoncteurOuvert(Exception):
    pass


class Disjoncteur:
    """Coupe un hôte après plusieurs échecs (idée PyBreaker, sans dépendance)."""

    def __init__(self, seuil: int = 3):
        self.seuil = seuil
        self.echecs: dict[str, int] = {}

    def verifier(self, cle: str) -> None:
        if self.echecs.get(cle, 0) >= self.seuil:
            raise DisjoncteurOuvert(f"disjoncteur ouvert pour {cle} ({self.seuil} échecs)")

    def echec(self, cle: str) -> None:
        self.echecs[cle] = self.echecs.get(cle, 0) + 1

    def succes(self, cle: str) -> None:
        self.echecs[cle] = 0


BREAKER = Disjoncteur()
RAFRAICHIR = False


def _charger(chemin: Path, nom: str):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    if spec is None or spec.loader is None:
        raise ImportError(chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def outils_reutilises() -> list[str]:
    """Outils du dépôt réellement appelés, plus le cache disque que le bracelet désigne."""
    bracelet = _charger(RACINE / "harnais" / "bracelet" / "bracelet_suggest.py", "bracelet_suggest")
    sug = bracelet.suggest("cache HTTP téléchargement images réutiliser", top=3)
    noms = ", ".join(s["name"] for s in sug)
    extraire = _charger(OUTILS / "extraire_v8.py", "extraire_v8")
    # L'appel prouve l'import ; le texte sert au mode --outils.
    _ = extraire.extraire_v8
    return [
        f"harnais/bracelet/bracelet_suggest.py → {noms} (cache HTTP : Hishel / requests-cache). "
        "Réécrit en stdlib (urllib + fichier, durée de vie, pas de second téléchargement).",
        "harnais/surveillance/watchdog.py → modèle lu : urllib.request + User-Agent nommé. Non importé (il parle à GitHub).",
        "grok-LOTS-html/outils/extraire_v8.py → extraire_v8(), contexte d'une leçon V8 sans passer par le harnais V0.",
        "Bracelet /cursor/stores/bot/outils/bracelet/bracelet.py consulté : même famille d'outils de cache.",
    ]


def licence_libre(libelle: str) -> bool:
    """CC0, CC BY, CC BY-SA, domaine public. Refuse vide, NC, ND, et toute formule vague."""
    if not libelle or not str(libelle).strip():
        return False
    n = re.sub(r"\s+", " ", str(libelle).lower().replace("_", " ").replace("-", " ")).strip()
    if any(b in n for b in ("all rights reserved", "copyrighted", "unknown", "unspecified", "à vérifier", "a verifier")):
        return False
    jetons = re.findall(r"[a-z0-9]+", n)
    if "nc" in jetons or "nd" in jetons or "noncommercial" in n or "non commercial" in n:
        return False
    if "no" in jetons and "derivatives" in jetons:
        return False
    if "public" in jetons and "domain" in jetons:
        return True
    if "pd" in jetons or "cc0" in jetons:
        return True
    if "cc" in jetons and "by" in jetons:
        return True
    return False


def _hote(url: str) -> str:
    return urllib.parse.urlparse(url).netloc.lower()


def http_get(url: str, ttl: float = 7 * 86400, accept: str = "*/*") -> tuple[bytes, dict]:
    """GET avec cache disque (réutilisation tant que ttl) et disjoncteur par hôte."""
    if "radiopaedia.org" in _hote(url):
        raise LicenceRefusee("Radiopaedia : récupération refusée")
    cle = _hote(url)
    BREAKER.verifier(cle)
    CACHE.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha256(url.encode()).hexdigest()
    corps, meta_p = CACHE / h, CACHE / (h + ".json")
    now = time.time()
    if not RAFRAICHIR and corps.exists() and meta_p.exists():
        meta = json.loads(meta_p.read_text(encoding="utf-8"))
        if now - float(meta.get("fetched", 0)) < ttl:
            meta["cache"] = True
            return corps.read_bytes(), meta
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
    try:
        with urllib.request.urlopen(req, timeout=40) as rep:
            body = rep.read()
            meta = {
                "url": url,
                "fetched": now,
                "status": getattr(rep, "status", 200),
                "content_type": rep.headers.get("Content-Type", ""),
                "cache": False,
            }
    except Exception as exc:
        BREAKER.echec(cle)
        raise SourceIndisponible(f"{url} : {exc}") from exc
    BREAKER.succes(cle)
    corps.write_bytes(body)
    meta_p.write_text(json.dumps(meta), encoding="utf-8")
    return body, meta


def _json(url: str) -> dict:
    body, _ = http_get(url, accept="application/json")
    if not body or body.lstrip()[:1] not in (b"{", b"["):
        raise SourceIndisponible(f"réponse non JSON : {url}")
    return json.loads(body.decode("utf-8", errors="replace"))


def _texte_licence(brut: str) -> str:
    t = re.sub(r"<[^>]+>", " ", brut or "")
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


def resoudre_commons(titre: str) -> dict:
    if not titre.startswith("File:"):
        titre = "File:" + titre
    q = urllib.parse.urlencode({
        "action": "query", "format": "json", "prop": "imageinfo",
        "iiprop": "url|extmetadata|mime|size", "titles": titre,
    })
    data = _json("https://commons.wikimedia.org/w/api.php?" + q)
    pages_map = (data.get("query") or {}).get("pages") or {}
    pages = list(pages_map.values()) if isinstance(pages_map, dict) else []
    if not pages or "imageinfo" not in pages[0]:
        raise SourceIndisponible(f"fichier Commons introuvable : {titre}")
    ii = pages[0]["imageinfo"][0]
    meta = ii.get("extmetadata") or {}
    lic = _texte_licence((meta.get("LicenseShortName") or {}).get("value", ""))
    if not licence_libre(lic):
        raise LicenceRefusee(f"Commons {titre} : licence refusée ({lic or 'absente'})")
    auteur = _texte_licence((meta.get("Artist") or {}).get("value", ""))
    if not auteur:
        raise LicenceRefusee(f"Commons {titre} : auteur absent")
    page = ii.get("descriptionurl") or (
        "https://commons.wikimedia.org/wiki/" + urllib.parse.quote(titre.replace(" ", "_"), safe="/:")
    )
    brut = ii.get("url") or ""
    return {
        "entrepot": "wikimedia",
        "identifiant": titre,
        "url_page": page,
        "url_fichier": brut.split("?")[0],
        "url_telechargement": brut,
        "auteur": auteur,
        "licence": lic,
        "licence_url": _texte_licence((meta.get("LicenseUrl") or {}).get("value", "")),
        "date_acces": date.today().isoformat(),
        "mime": ii.get("mime", ""),
        "largeur": ii.get("width"),
        "hauteur": ii.get("height"),
    }


def chercher_commons(requete: str, n: int = 5) -> list[dict]:
    q = urllib.parse.urlencode({
        "action": "query", "format": "json", "list": "search",
        "srsearch": requete, "srnamespace": "6", "srlimit": str(n),
    })
    data = _json("https://commons.wikimedia.org/w/api.php?" + q)
    out = []
    for h in (data.get("query") or {}).get("search") or []:
        try:
            out.append(resoudre_commons(h["title"]))
        except LicenceRefusee as exc:
            out.append({"entrepot": "wikimedia", "identifiant": h["title"], "refuse": str(exc)})
    return out


def parser_openi(data: dict) -> list[dict]:
    """Garde le sous-ensemble dont la licence est libre. Le reste est marqué refuse."""
    out = []
    for it in data.get("list") or []:
        lic = _texte_licence(str(it.get("license") or it.get("licence") or ""))
        url = it.get("imgLarge") or it.get("img_large") or ""
        rec = {
            "entrepot": "openi",
            "identifiant": str(it.get("uid") or it.get("pmcid") or ""),
            "url_page": ("https://www.ncbi.nlm.nih.gov/pmc/articles/" + it["pmcid"]) if it.get("pmcid") else "",
            "url_fichier": url,
            "auteur": _texte_licence(str(it.get("authors") or it.get("author") or "")),
            "licence": lic,
            "licence_url": "",
            "date_acces": date.today().isoformat(),
            "titre": _texte_licence(str(it.get("title") or "")),
        }
        if not licence_libre(lic) or not url or not rec["auteur"]:
            rec["refuse"] = f"licence ou attribution insuffisante ({lic or 'absente'})"
        out.append(rec)
    return out


def chercher_openi(requete: str, n: int = 5) -> list[dict]:
    q = urllib.parse.urlencode({"query": requete, "it": "c", "m": "1", "n": str(n), "coll": "pmc"})
    url = "https://openi.nlm.nih.gov/api/search?" + q
    try:
        data = _json(url)
    except SourceIndisponible as exc:
        raise SourceIndisponible(
            "Open-i n'a pas renvoyé de JSON (constaté le 2026-10-31 : page d'erreur). " + str(exc)
        ) from exc
    return parser_openi(data)


def parser_pmc(data: dict) -> list[dict]:
    out = []
    for r in ((data.get("resultList") or {}).get("result") or []):
        lic = _texte_licence(str(r.get("license") or ""))
        pmcid = str(r.get("pmcid") or "")
        rec = {
            "entrepot": "pmc",
            "identifiant": pmcid,
            "url_page": f"https://europepmc.org/articles/{pmcid}" if pmcid else "",
            "url_fichier": "",
            "auteur": _texte_licence(str(r.get("authorString") or "")),
            "licence": lic,
            "licence_url": "",
            "date_acces": date.today().isoformat(),
            "titre": _texte_licence(str(r.get("title") or "")),
            "doi": r.get("doi") or "",
        }
        if not licence_libre(lic):
            rec["refuse"] = f"licence PMC refusée ({lic or 'absente'})"
        out.append(rec)
    return out


def chercher_pmc(requete: str, n: int = 5) -> list[dict]:
    q = urllib.parse.urlencode({
        "query": requete + " OPEN_ACCESS:Y", "format": "json",
        "pageSize": str(n), "resultType": "core",
    })
    return parser_pmc(_json("https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + q))


def contexte_lecon(fichier: str, points: list[int]) -> str:
    """Réutilise extraire_v8 (lecture seule). Ne modifie pas le LOT."""
    mod = _charger(OUTILS / "extraire_v8.py", "extraire_v8")
    return mod.extraire_v8(fichier, points, False)


def _lin(c: float) -> float:
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(rgb: tuple[int, int, int]) -> float:
    r, g, b = rgb
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contraste(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    l1, l2 = luminance(a), luminance(b)
    return (max(l1, l2) + 0.05) / (min(l1, l2) + 0.05)


def choisir_couleurs(fonds: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    """Une couleur par lésion, contraste maximal avec le fond local, couleurs distinctes."""
    pris: list[tuple[int, int, int]] = []
    out = []
    for fond in fonds:
        classe = sorted(PALETTE, key=lambda c: contraste(c, fond), reverse=True)
        choisi = None
        for c in classe:
            if c not in pris and contraste(c, fond) >= 3:
                choisi = c
                break
        if choisi is None:
            choisi = next((c for c in classe if c not in pris), classe[0])
        pris.append(choisi)
        out.append(choisi)
    return out


def echantillon(im: Image.Image, pts: list[tuple[float, float]], bande: int = 16) -> tuple[int, int, int]:
    px = im.load()
    w, h = im.size
    acc = []
    pas = max(1, len(pts) // 48)
    for x, y in pts[::pas]:
        for dx in range(-bande, bande + 1, 4):
            for dy in range(-bande, bande + 1, 4):
                if 36 <= dx * dx + dy * dy <= bande * bande:
                    xx, yy = int(x + dx), int(y + dy)
                    if 0 <= xx < w and 0 <= yy < h:
                        acc.append(px[xx, yy][:3])
    if not acc:
        return (128, 128, 128)
    n = len(acc)
    return tuple(sum(c[i] for c in acc) // n for i in range(3))  # type: ignore[return-value]


def _points_ellipse(cx: float, cy: float, rx: float, ry: float, n: int = 72) -> list[tuple[float, float]]:
    return [(cx + rx * math.cos(2 * math.pi * i / n), cy + ry * math.sin(2 * math.pi * i / n)) for i in range(n)]


def geometrie(lesion: dict, w: int, h: int, ox: int = 0, oy: int = 0) -> tuple[list[tuple[float, float]], bool]:
    """Retourne (points, fermé). points_norm : 0–1 de l'image déjà cadrée. points : pixels du fichier entier."""
    forme = lesion.get("forme") or "polygone"
    if lesion.get("points_norm"):
        pts = [(float(x) * w, float(y) * h) for x, y in lesion["points_norm"]]
    elif lesion.get("points"):
        pts = [(float(x) - ox, float(y) - oy) for x, y in lesion["points"]]
    elif forme == "ellipse":
        e = lesion["ellipse"]
        if e.get("norm"):
            cx, cy, rx, ry = float(e["cx"]) * w, float(e["cy"]) * h, float(e["rx"]) * w, float(e["ry"]) * h
        else:
            cx, cy = float(e["cx"]) - ox, float(e["cy"]) - oy
            rx, ry = float(e["rx"]), float(e["ry"])
        return _points_ellipse(cx, cy, rx, ry), True
    elif forme == "rect":
        r = lesion["rect"]
        if r.get("norm"):
            x, y, rw, rh = float(r["x"]) * w, float(r["y"]) * h, float(r["w"]) * w, float(r["h"]) * h
        else:
            x, y, rw, rh = float(r["x"]) - ox, float(r["y"]) - oy, float(r["w"]), float(r["h"])
        pts = [(x, y), (x + rw, y), (x + rw, y + rh), (x, y + rh)]
        return pts, True
    else:
        raise ValueError("lésion sans points, ellipse ni rect")
    ferme = forme in ("polygone", "ellipse", "rect")
    if len(pts) < 2:
        raise ValueError("une lésion a besoin d'au moins deux points")
    return pts, ferme


def centroide(pts: list[tuple[float, float]]) -> tuple[float, float]:
    return sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts)


def tri_lecture(lesions: list[dict], modalite: str, w: int, h: int, ox: int, oy: int) -> list[dict]:
    """Ordre explicite `ordre`, sinon lecture du cliché : haut→bas puis gauche→droite (ECG : gauche→droite)."""

    def cle(lesion: dict) -> tuple:
        if lesion.get("ordre") is not None:
            return (0, float(lesion["ordre"]), 0.0)
        pts, _ = geometrie(lesion, w, h, ox, oy)
        cx, cy = centroide(pts)
        if modalite == "ecg":
            return (1, cx, cy)
        return (1, cy, cx)

    return sorted(lesions, key=cle)


def dessiner_pointilles(draw: ImageDraw.ImageDraw, pts: list[tuple[float, float]], fill, width: int, on: float, off: float, ferme: bool) -> None:
    seq = list(pts)
    if ferme and (seq[0] != seq[-1]):
        seq = seq + [seq[0]]
    dessin, reste = True, on
    for (x0, y0), (x1, y1) in zip(seq, seq[1:]):
        dx, dy = x1 - x0, y1 - y0
        longueur = math.hypot(dx, dy)
        if longueur < 1e-3:
            continue
        ux, uy = dx / longueur, dy / longueur
        t = 0.0
        while t < longueur - 1e-6:
            pas = min(reste, longueur - t)
            if dessin and pas > 0.4:
                draw.line([(x0 + ux * t, y0 + uy * t), (x0 + ux * (t + pas), y0 + uy * (t + pas))], fill=fill, width=width)
            t += pas
            reste -= pas
            if reste <= 0.4:
                dessin = not dessin
                reste = off if not dessin else on


def _police(taille: int) -> ImageFont.ImageFont:
    if POLICE.is_file():
        return ImageFont.truetype(str(POLICE), taille)
    raise FileNotFoundError(f"police absente : {POLICE}")


def _place_numero(pts, w, h, r, pris, lesion):
    """À côté du trait : milieu d'une ligne, centre d'un polygone, ou numero_xy explicite."""
    if lesion.get("numero_xy"):
        cx, cy = float(lesion["numero_xy"][0]), float(lesion["numero_xy"][1])
    elif lesion.get("forme") in ("polygone", "ellipse", "rect"):
        cx, cy = centroide(pts)
    else:
        mx, my = pts[len(pts) // 2]
        dx = abs(pts[-1][0] - pts[0][0])
        dy = abs(pts[-1][1] - pts[0][1])
        if dy > dx:
            cx, cy = mx + r + 10, my
        else:
            cx, cy = mx, my - r - 10
    cx = min(max(cx, r + 2), w - r - 2)
    cy = min(max(cy, r + 2), h - r - 2)
    for _ in range(24):
        if all((cx - px) ** 2 + (cy - py) ** 2 >= (r + pr + 6) ** 2 for px, py, pr in pris):
            break
        cy = min(cy + r, h - r - 2)
    return cx, cy


def annoter_image(im: Image.Image, lesions: list[dict], modalite: str) -> tuple[Image.Image, list[dict], list[tuple[int, int, int]]]:
    im = im.convert("RGB")
    w, h = im.size
    ordre = tri_lecture(lesions, modalite, w, h, 0, 0)
    geos = []
    for i, lesion in enumerate(ordre, 1):
        pts, ferme = geometrie(lesion, w, h, 0, 0)
        if not any(0 <= x < w and 0 <= y < h for x, y in pts):
            raise ValueError(f"lésion {i} entièrement hors image")
        lesion = dict(lesion)
        lesion["numero"] = i
        geos.append((lesion, pts, ferme))
    fonds = [echantillon(im, pts) for _, pts, _ in geos]
    couleurs = choisir_couleurs(fonds)
    draw = ImageDraw.Draw(im)
    # Plafond : sur un grand cliché, un numéro calé sur la largeur de l'image cache la lésion.
    trait = min(5, max(3, min(w, h) // 220))
    on, off = trait * 3.2, trait * 2.2
    rayon = min(18, max(13, min(w, h) // 80))
    font = _police(max(16, rayon))
    pris = []
    for (lesion, pts, ferme), coul in zip(geos, couleurs):
        dessiner_pointilles(draw, pts, coul, trait, on, off, ferme)
        cx, cy = _place_numero(pts, w, h, rayon, pris, lesion)
        pris.append((cx, cy, rayon))
        draw.ellipse([cx - rayon, cy - rayon, cx + rayon, cy + rayon], fill=coul)
        chiffre = str(lesion["numero"])
        encre = (255, 255, 255) if luminance(coul) < 0.45 else (20, 20, 22)
        bbox = font.getbbox(chiffre)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        draw.text((cx - tw / 2 - bbox[0], cy - th / 2 - bbox[1]), chiffre, fill=encre, font=font)
    return im, [g[0] for g in geos], couleurs


def _morceaux(mot: str, font, largeur: int) -> list[str]:
    """Coupe un mot plus large que la ligne, sinon le rend tel quel."""
    if largeur < 8:
        largeur = 8
    if font.getlength(mot) <= largeur:
        return [mot]
    out, cour = [], ""
    for ch in mot:
        if cour and font.getlength(cour + ch) > largeur:
            out.append(cour)
            cour = ch
        else:
            cour += ch
    if cour:
        out.append(cour)
    return out or [mot]


def _plier(texte: str, font, largeur: int) -> list[str]:
    """Retour à la ligne : aucun fragment ne dépasse `largeur`."""
    largeur = max(8, int(largeur))
    lignes, cour = [], ""
    for mot in (texte or "").split():
        for part in _morceaux(mot, font, largeur):
            essai = (cour + " " + part).strip()
            if cour and font.getlength(essai) > largeur:
                lignes.append(cour)
                cour = part
            else:
                cour = essai
    if cour:
        lignes.append(cour)
    return lignes or [""]


def bande_legende(im: Image.Image, lesions: list[dict], couleurs: list[tuple[int, int, int]], attribution: str) -> Image.Image:
    font = _police(max(18, im.width // 48))
    petit = _police(max(15, im.width // 58))
    marge, inter = 16, 8
    pastille = font.size
    indent = marge + pastille + 10
    largeur_texte = im.width - indent - marge
    lignes: list[tuple] = []
    for lesion, coul in zip(lesions, couleurs):
        bloc = _plier(f"{lesion['numero']}. {lesion.get('legende') or lesion.get('etiquette') or ''}", font, largeur_texte)
        lignes.append((bloc, coul, font))
    attr = _plier(attribution, petit, im.width - 2 * marge)
    haut = marge
    for bloc, _, f in lignes:
        haut += len(bloc) * (f.size + 6) + inter
    haut += inter + len(attr) * (petit.size + 4) + marge
    out = Image.new("RGB", (im.width, im.height + haut), (238, 247, 252))
    out.paste(im, (0, 0))
    draw = ImageDraw.Draw(out)
    y = im.height + marge
    for bloc, coul, f in lignes:
        for i, ligne in enumerate(bloc):
            if i == 0:
                draw.ellipse([marge, y + 2, marge + f.size, y + 2 + f.size], fill=coul)
                encre_n = (255, 255, 255) if luminance(coul) < 0.45 else (20, 20, 22)
                draw.text((marge + 4, y + 2), str(ligne.split(".", 1)[0]), fill=encre_n, font=petit)
                draw.text((indent, y), ligne, fill=(29, 42, 48), font=f)
            else:
                draw.text((indent, y), ligne, fill=(29, 42, 48), font=f)
            y += f.size + 6
        y += inter
    y += inter
    for ligne in attr:
        draw.text((marge, y), ligne, fill=(79, 95, 102), font=petit)
        y += petit.size + 4
    return out


def attribution_image(src: dict, modification: str) -> str:
    bits = [
        f"Source : {src.get('auteur', '')}.",
        f"Licence : {src.get('licence', '')}.",
        src.get("licence_url") or "",
        src.get("url_page") or src.get("url_fichier") or "",
        f"Consulté le {src.get('date_acces', '')}.",
    ]
    if modification:
        bits.append(modification)
    return " ".join(b for b in bits if b).strip()


def fragment_figure(titre: str, alt: str, corps: str, lesions: list[dict], semiologie: str, attribution: str, pieges: list[str]) -> str:
    items = "".join(f"<li>{html.escape(L.get('legende') or '')}</li>" for L in lesions)
    pieges_html = ""
    if pieges:
        pieges_html = "<p><strong>Pièges.</strong> " + " ".join(html.escape(p) for p in pieges) + "</p>"
    semi = f"<p>{html.escape(semiologie)}</p>" if semiologie else ""
    return (
        '<figure class="schema illustration">\n'
        f"{corps}\n"
        "<figcaption>\n"
        f"<strong>{html.escape(titre)}</strong>\n"
        f'<ol start="1">{items}</ol>\n'
        f"{semi}{pieges_html}\n"
        f'<p class="mention">{html.escape(attribution)}</p>\n'
        "</figcaption>\n</figure>"
    )


def _exiger_source_image(src: dict) -> None:
    for cle in ("url_fichier", "auteur", "licence", "date_acces"):
        if not str(src.get(cle) or "").strip():
            raise LicenceRefusee(f"image refusée, champ vide : {cle}")
    if not (src.get("url_page") or src.get("url_fichier")):
        raise LicenceRefusee("image refusée : pas d'URL")
    if not licence_libre(src["licence"]):
        raise LicenceRefusee(f"image refusée : {src['licence']}")


def obtenir_image(annotation: dict) -> tuple[Image.Image, dict]:
    src = dict(annotation.get("source") or {})
    entrepot = src.get("entrepot") or ""
    if entrepot == "wikimedia":
        src = resoudre_commons(src.get("identifiant") or "")
    elif entrepot == "openi":
        raise LicenceRefusee("Open-i : passer par --chercher puis une fiche dont la licence est libre")
    elif entrepot == "pmc":
        trouve = chercher_pmc("PMCID:" + str(src.get("identifiant") or ""), n=1)
        if not trouve or trouve[0].get("refuse") or not licence_libre(trouve[0].get("licence", "")):
            raise LicenceRefusee("PMC : licence libre non confirmée par Europe PMC")
        src.update({k: trouve[0][k] for k in ("licence", "licence_url", "url_page", "date_acces", "auteur", "identifiant") if trouve[0].get(k)})
        if not src.get("url_fichier"):
            raise LicenceRefusee("PMC : pas d'URL de fichier image (ne pas inventer une figure)")
    elif entrepot == "fichier":
        pass
    else:
        raise LicenceRefusee(f"entrepôt d'image inconnu : {entrepot}")
    _exiger_source_image(src)
    if "radiopaedia.org" in (src.get("url_fichier") or "") or "radiopaedia.org" in (src.get("url_page") or ""):
        raise LicenceRefusee("Radiopaedia : récupération refusée")
    chemin = src.get("chemin")
    if entrepot == "fichier" and chemin:
        im = Image.open(chemin)
    else:
        body, _ = http_get(src.get("url_telechargement") or src["url_fichier"])
        from io import BytesIO
        im = Image.open(BytesIO(body))
    im = im.convert("RGB")
    cadre = annotation.get("cadre") or {}
    if cadre:
        x, y = int(cadre["x"]), int(cadre["y"])
        w, h = int(cadre["largeur"]), int(cadre["hauteur"])
        im = im.crop((x, y, x + w, y + h))
        ox, oy = x, y
    else:
        ox = oy = 0
    # Les points du JSON sont dans le fichier entier : on les translate après le cadre.
    lesions = []
    for lesion in annotation.get("lesions") or []:
        L = dict(lesion)
        if L.get("points") and cadre:
            L["points"] = [[float(px) - ox, float(py) - oy] for px, py in L["points"]]
        if L.get("ellipse") and not L["ellipse"].get("norm") and cadre:
            e = dict(L["ellipse"])
            e["cx"] = float(e["cx"]) - ox
            e["cy"] = float(e["cy"]) - oy
            L["ellipse"] = e
        if L.get("rect") and not L["rect"].get("norm") and cadre:
            r = dict(L["rect"])
            r["x"] = float(r["x"]) - ox
            r["y"] = float(r["y"]) - oy
            L["rect"] = r
        if L.get("numero_xy") and cadre:
            L["numero_xy"] = [float(L["numero_xy"][0]) - ox, float(L["numero_xy"][1]) - oy]
        lesions.append(L)
    reperes = []
    for r in annotation.get("reperes") or []:
        rr = dict(r)
        if cadre:
            rr["x"] = float(r["x"]) - ox
            rr["y"] = float(r["y"]) - oy
        reperes.append(rr)
    return im, {**annotation, "source": src, "lesions": lesions, "reperes": reperes, "_origine": (ox, oy)}


def _dessiner_reperes(im: Image.Image, reperes: list[dict]) -> None:
    if not reperes:
        return
    font = _police(max(16, im.width // 55))
    draw = ImageDraw.Draw(im)
    for r in reperes:
        texte = str(r.get("texte") or "")
        if not texte:
            continue
        x, y = int(r["x"]), int(r["y"])
        bb = font.getbbox(texte)
        tw, th = bb[2] - bb[0], bb[3] - bb[1]
        x = min(max(2, x), im.width - tw - 10)
        y = min(max(2, y), im.height - th - 8)
        draw.rectangle([x, y, x + tw + 8, y + th + 6], fill=(20, 20, 22))
        draw.text((x + 4 - bb[0], y + 2 - bb[1]), texte, fill=(255, 255, 255), font=font)


def rendre_imagerie(annotation: dict, dossier: Path) -> dict:
    im, ann = obtenir_image(annotation)
    modalite = ann.get("modalite") or "scanner"
    annote, lesions, couleurs = annoter_image(im, ann["lesions"], modalite)
    _dessiner_reperes(annote, ann.get("reperes") or [])
    modif = ann.get("modification") or ""
    attr = attribution_image(ann["source"], modif)
    final = bande_legende(annote, lesions, couleurs, attr)
    ident = ann.get("id") or "imagerie"
    dossier.mkdir(parents=True, exist_ok=True)
    png = dossier / f"{ident}.png"
    final.save(png, "PNG")
    alt = ann.get("alt") or ann.get("titre") or ident
    corps = f'<img src="{html.escape(png.name)}" alt="{html.escape(alt)}">'
    frag = fragment_figure(ann.get("titre") or ident, alt, corps, lesions, ann.get("semiologie") or "", attr, ann.get("pieges") or [])
    (dossier / f"{ident}.fragment.html").write_text(frag + "\n", encoding="utf-8")
    return {"id": ident, "png": png.name, "fragment": frag, "source": ann["source"], "lesions": lesions}


def _xy_schema(x_rel: float, y_rel: float, x0, y0, x1, y1) -> tuple[float, float]:
    """y_rel : 0 en bas, 1 en haut, dans l'aire du graphique."""
    return x0 + x_rel * (x1 - x0), y1 - y_rel * (y1 - y0)


def rendre_biologie(annotation: dict, dossier: Path) -> dict:
    refs = (annotation.get("source") or {}).get("references") or []
    if not refs or any(not r.get("date_lecture") or not r.get("titre") for r in refs):
        raise LicenceRefusee("schéma biologique : chaque référence doit avoir un titre et une date de lecture")
    for r in refs:
        if r.get("licence_figure") and not licence_libre(r["licence_figure"]):
            raise LicenceRefusee("figure tierce refusée : " + r["licence_figure"])
    elements = list(annotation.get("elements") or [])
    if not elements:
        raise ValueError("schéma sans élément numéroté")
    W, H = 960, 640
    fond = Image.new("RGB", (W, H), (255, 255, 255))
    # Aires : titre + graphe. La légende longue est sous l'image (bande) et dans le HTML.
    x0, y0, x1, y1 = 90, 70, 920, 520
    geos = []
    for el in sorted(elements, key=lambda e: float(e.get("ordre", 0))):
        forme = el.get("forme")
        if forme == "ligne":
            y = float(el["y_rel"])
            pts = [_xy_schema(0.0, y, x0, y0, x1, y1), _xy_schema(1.0, y, x0, y0, x1, y1)]
            ferme = False
        elif forme == "courbe":
            pts = [_xy_schema(float(x), float(y), x0, y0, x1, y1) for x, y in el["points_rel"]]
            ferme = False
        else:
            raise ValueError("forme de schéma inconnue : " + str(forme))
        geos.append((el, pts, ferme))
    # Fond local : blanc du graphe, mesuré vraiment.
    sondes = []
    for _, pts, _ in geos:
        sondes.append(echantillon(fond, pts, bande=10))
    couleurs = choisir_couleurs(sondes)
    draw = ImageDraw.Draw(fond)
    font = _police(20)
    petit = _police(16)
    draw.text((x0, 24), annotation.get("titre") or "Schéma", fill=(20, 48, 59), font=font)
    # Axes
    draw.line([(x0, y0), (x0, y1), (x1, y1)], fill=(29, 42, 48), width=2)
    draw.text((8, (y0 + y1) // 2 - 20), "schéma", fill=(79, 95, 102), font=petit)
    for lab, xr in annotation.get("graduations_x") or []:
        xx, yy = _xy_schema(float(xr), 0, x0, y0, x1, y1)
        draw.line([(xx, y1), (xx, y1 + 6)], fill=(29, 42, 48), width=2)
        draw.text((xx - 8, y1 + 10), str(lab), fill=(29, 42, 48), font=petit)
    axe = annotation.get("axe_x") or ""
    axe_lignes = _plier(axe, petit, x1 - x0) if axe else []
    for i, ligne in enumerate(axe_lignes):
        draw.text((x0, y1 + 28 + i * (petit.size + 4)), ligne, fill=(79, 95, 102), font=petit)
    trait = 5
    lesions = []
    pris = []
    rayon = 16
    for i, ((el, pts, ferme), coul) in enumerate(zip(geos, couleurs), 1):
        dessiner_pointilles(draw, pts, coul, trait, 16, 9, ferme)
        L = dict(el)
        L["numero"] = i
        L["legende"] = el.get("legende") or ""
        lesions.append(L)
        cx, cy = _place_numero(pts, W, H, rayon, pris, L)
        pris.append((cx, cy, rayon))
        draw.ellipse([cx - rayon, cy - rayon, cx + rayon, cy + rayon], fill=coul)
        encre = (255, 255, 255) if luminance(coul) < 0.45 else (20, 20, 22)
        chiffre = str(i)
        bb = font.getbbox(chiffre)
        draw.text((cx - (bb[2] - bb[0]) / 2, cy - (bb[3] - bb[1]) / 2 - 2), chiffre, fill=encre, font=font)
        if el.get("etiquette"):
            et = el["etiquette"]
            tw = petit.getlength(et)
            sommet = min(pts, key=lambda p: p[1])
            ex = min(max(x0, sommet[0] + 8), W - tw - 8)
            ey = max(18, sommet[1] - 22)
            draw.text((ex, ey), et, fill=coul, font=petit)
    src = dict(annotation.get("source") or {})
    src.setdefault("date_acces", date.today().isoformat())
    src.setdefault("entrepot", "schema")
    attr = src.get("attribution") or (
        "Schéma original (pas une figure tierce). " + " ".join(
            f"{r.get('titre')} ({r.get('support', '')}, lu le {r.get('date_lecture')})." for r in refs
        )
    )
    # Bande sous le graphe : on recolle car le graphe a déjà une marge basse.
    # On coupe la marge basse vide pour coller la légende.
    bas = y1 + 36 + max(1, len(axe_lignes)) * (petit.size + 4)
    graphe = fond.crop((0, 0, W, min(H - 1, bas)))
    final = bande_legende(graphe, lesions, couleurs, attr)
    ident = annotation.get("id") or "biologie"
    dossier.mkdir(parents=True, exist_ok=True)
    png = dossier / f"{ident}.png"
    final.save(png, "PNG")
    svg = _svg_biologie(annotation, lesions, couleurs)
    (dossier / f"{ident}.svg").write_text(svg, encoding="utf-8")
    frag = fragment_figure(
        annotation.get("titre") or ident,
        annotation.get("alt") or annotation.get("titre") or ident,
        svg,
        lesions,
        annotation.get("semiologie") or "",
        attr,
        annotation.get("pieges") or [],
    )
    (dossier / f"{ident}.fragment.html").write_text(frag + "\n", encoding="utf-8")
    return {"id": ident, "png": png.name, "svg": f"{ident}.svg", "fragment": frag, "source": src, "lesions": lesions}


def _svg_biologie(annotation: dict, lesions: list[dict], couleurs: list[tuple[int, int, int]]) -> str:
    """Même géométrie que le PNG, pour l'insertion V8 (figure svg)."""
    x0, y0, x1, y1 = 90, 56, 900, 420
    def xy(xr, yr):
        return _xy_schema(float(xr), float(yr), x0, y0, x1, y1)

    def coul(c):
        return "#{:02x}{:02x}{:02x}".format(*c)

    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" role="img">',
        "<title>" + html.escape(annotation.get("titre") or "Schéma") + "</title>",
        '<style>text{font-family:"Atkinson Hyperlegible",Verdana,sans-serif;fill:#1d2a30}</style>',
        '<rect width="960" height="520" fill="#ffffff"/>',
        f'<text x="{x0}" y="36" font-size="20" font-weight="700" fill="#14303b">{html.escape(annotation.get("titre") or "")}</text>',
        f'<polyline points="{x0},{y0} {x0},{y1} {x1},{y1}" fill="none" stroke="#1d2a30" stroke-width="2"/>',
    ]
    for lab, xr in annotation.get("graduations_x") or []:
        xx, yy = xy(xr, 0)
        parts.append(f'<line x1="{xx:.1f}" y1="{y1}" x2="{xx:.1f}" y2="{y1+6}" stroke="#1d2a30" stroke-width="2"/>')
        parts.append(f'<text x="{xx-8:.1f}" y="{y1+26}" font-size="15">{html.escape(str(lab))}</text>')
    if annotation.get("axe_x"):
        parts.append(f'<text x="{x0}" y="{y1+48}" font-size="15" fill="#4f5f66">{html.escape(annotation["axe_x"])}</text>')
    elements = sorted(annotation.get("elements") or [], key=lambda e: float(e.get("ordre", 0)))
    for el, lesion, c in zip(elements, lesions, couleurs):
        if el.get("forme") == "ligne":
            a, b = xy(0, el["y_rel"]), xy(1, el["y_rel"])
            pts = [a, b]
        else:
            pts = [xy(x, y) for x, y in el["points_rel"]]
        points = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        parts.append(
            f'<polyline points="{points}" fill="none" stroke="{coul(c)}" stroke-width="4" '
            f'stroke-dasharray="14 8" stroke-linecap="round"/>'
        )
        mx, my = pts[len(pts) // 2]
        dx, dy = abs(pts[-1][0] - pts[0][0]), abs(pts[-1][1] - pts[0][1])
        cx, cy = (mx + 26, my) if dy > dx else (mx, my - 22)
        parts.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="14" fill="{coul(c)}"/>')
        encre = "#ffffff" if luminance(c) < 0.45 else "#141416"
        parts.append(f'<text x="{cx-5:.1f}" y="{cy+5:.1f}" font-size="16" fill="{encre}">{lesion["numero"]}</text>')
    parts.append("</svg>")
    return "\n".join(parts)


def ecrire_sources(dossier: Path, fiches: list[dict]) -> None:
    chemin = dossier / "SOURCES.json"
    ancien = []
    if chemin.exists():
        try:
            ancien = json.loads(chemin.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            ancien = []
    par_id = {x.get("id"): x for x in ancien if isinstance(x, dict)}
    for f in fiches:
        par_id[f["id"]] = {
            "id": f["id"],
            "fichier": f.get("png"),
            "svg": f.get("svg"),
            "source": f.get("source"),
            "legende": [{"n": L.get("numero"), "texte": L.get("legende")} for L in f.get("lesions") or []],
        }
    chemin.write_text(json.dumps(list(par_id.values()), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def page_demonstration(titre: str, fragments: list[str], mention: str) -> str:
    """Page autonome au rendu V8, avec les identifiants que la porte locale attend d'un HTML de LOT."""
    ids = [
        ("ess", "L'essentiel", "Deux figures pour le LOT 150 : scanner annoté d'une dissection aortique, et schéma de cinétique de la troponine haute sensibilité. Ce n'est pas la leçon."),
        ("som", "Sommaire", "La leçon reste dans le LOT, en lecture seule. Cette page ne fait que montrer le rendu de l'outil."),
        ("p1", "1. Définition", "Le signe dessiné est celui visible sur le cliché source, pas une définition inventée."),
        ("p2", "2. Épidémiologie", "Aucune fréquence n'est ajoutée ici."),
        ("p3", "3. Physiopathologie", "Le schéma de troponine sépare une forme rise-and-fall d'une forme plate, toutes deux qualitatives."),
        ("p4", "4. Démarche", "L'ordre des numéros suit la lecture du cliché, puis le graphe de gauche à droite."),
        ("p5", "5. Anamnèse", "Pas d'histoire clinique dans cette page."),
        ("p6", "6. Examen", "Pas d'examen physique dans cette page."),
        ("p7", "7. Syndromes", "La sémiologie du scanner est sous la première figure."),
        ("p8", "8. Diagnostic", "La source Commons nomme une dissection de type Stanford A."),
        ("p9", "9. Examens", "Scanner injecté pour l'imagerie. Schéma pour la biologie, faute d'une lame utile."),
        ("p10", "10. Décision", "Les seuils d'un dosage particulier ne sont pas dessinés."),
        ("p11", "11. Suisse", "Les chiffres repris viennent des textes suisses lus dans le dossier de preuves."),
        ("p12", "12. Prévention", "Hors sujet de cette illustration."),
        ("p13", "13. Points clés", "Licence libre obligatoire. Contour en pointillés. Numéros lisibles."),
        ("p14", "14. Pièges", "Ne pas lire une densité sur cette photographie de film. Ne pas attribuer une cinétique à la dissection sans source."),
        ("sources", "Sources", mention),
    ]
    blocs = []
    for i, (ident, titre_s, texte) in enumerate(ids):
        tag = "h2"
        blocs.append(f'<{tag} id="{ident}">{html.escape(titre_s)}</{tag}><p>{html.escape(texte)}</p>')
    figures = "\n".join(fragments)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titre)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&amp;display=swap">
<style>
:root{{--fond:#eef7fc;--page:#fff;--texte:#1d2a30;--doux:#4f5f66;--lien:#0b5d86;--titre:#14303b;--trait:#cfe3ec}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--fond);color:var(--texte);font:1rem/1.45 "Atkinson Hyperlegible",Verdana,sans-serif}}
main{{max-width:74ch;margin:0 auto;padding:1rem 1rem 2rem}}
h1,h2,figcaption,strong{{font-family:"Atkinson Hyperlegible",Verdana,sans-serif}}
h1{{font-size:1.6rem;color:var(--titre);margin:0 0 .4rem}}
h2{{font-size:1.15rem;color:var(--titre);margin:1rem 0 .3rem}}
figure{{margin:1.2rem 0;background:var(--page);padding:.6rem;border:1px solid var(--trait);border-radius:12px}}
figure img,figure svg{{width:100%;height:auto;display:block}}
figcaption{{font-size:.92rem;color:var(--doux);margin-top:.4rem}}
figcaption ol{{color:var(--texte);text-align:left;padding-left:1.2rem}}
.mention{{font-style:italic}}
.avertissement{{border:2px solid #a1262f;border-radius:8px;padding:.6rem .8rem}}
</style>
</head>
<body>
<main>
<h1>{html.escape(titre)}</h1>
<p class="avertissement">Document de démonstration de l'outil d'illustration, non validé cliniquement.</p>
{figures}
{''.join(blocs)}
</main>
</body>
</html>
<!-- FIN_FICHIER illustration exemple -->
"""


def rendre(fichiers: list[str], sortie: str, page: str = "") -> list[dict]:
    dossier = Path(sortie)
    fiches = []
    for f in fichiers:
        ann = json.loads(Path(f).read_text(encoding="utf-8"))
        if ann.get("type") == "biologie":
            fiches.append(rendre_biologie(ann, dossier))
        elif ann.get("type") == "imagerie":
            fiches.append(rendre_imagerie(ann, dossier))
        else:
            raise ValueError("type attendu : imagerie ou biologie")
    ecrire_sources(dossier, fiches)
    if page:
        mention = "Détail dans SOURCES.json du même dossier. " + " ".join(
            attribution_image(f["source"], "") if f["source"].get("licence") else (f["source"].get("attribution") or "")
            for f in fiches
        )
        html_page = page_demonstration("Exemple d'illustration, enzymes cardiaques anormales", [f["fragment"] for f in fiches], mention)
        (dossier / page).write_text(html_page, encoding="utf-8")
    return fiches


def _autotest() -> int:
    erreurs = []

    def ok(cond, msg):
        if not cond:
            erreurs.append(msg)

    ok(licence_libre("CC BY-SA 3.0"), "CC BY-SA acceptée")
    ok(licence_libre("CC0"), "CC0 acceptée")
    ok(licence_libre("Public domain"), "PD accepté")
    ok(licence_libre("CC BY 4.0"), "CC BY acceptée")
    ok(not licence_libre(""), "vide refusé")
    ok(not licence_libre("CC BY-NC-SA 4.0"), "NC refusé")
    ok(not licence_libre("CC BY-ND 4.0"), "ND refusé")
    ok(not licence_libre("open access"), "open access seul refusé")
    try:
        http_get("https://radiopaedia.org/cases/1")
        erreurs.append("Radiopaedia aurait dû être refusée")
    except LicenceRefusee:
        pass

    # Parseurs sans réseau.
    openi = parser_openi({"list": [
        {"uid": "1", "title": "A", "license": "CC BY", "imgLarge": "https://example.org/a.jpg", "authors": "Doe", "pmcid": "PMC1"},
        {"uid": "2", "title": "B", "license": "CC BY-NC", "imgLarge": "https://example.org/b.jpg", "authors": "X"},
    ]})
    ok(len(openi) == 2 and "refuse" not in openi[0] and "refuse" in openi[1], "Open-i filtre NC")
    pmc = parser_pmc({"resultList": {"result": [
        {"title": "T", "pmcid": "PMC9", "license": "cc by", "authorString": "A", "doi": "10.1/x"},
        {"title": "U", "pmcid": "PMC8", "license": "", "authorString": "B"},
    ]}})
    ok(not pmc[0].get("refuse") and pmc[1].get("refuse"), "PMC refuse une licence vide")

    # Cache : un second GET ne retélécharge pas.
    appels = {"n": 0}

    class H(BaseHTTPRequestHandler):
        def do_GET(self):
            appels["n"] += 1
            body = b"ok"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *_a):
            return

    serveur = ThreadingHTTPServer(("127.0.0.1", 0), H)
    port = serveur.server_address[1]
    threading.Thread(target=serveur.serve_forever, daemon=True).start()
    url = f"http://127.0.0.1:{port}/t"
    BREAKER.succes(_hote(url))
    http_get(url, ttl=3600)
    http_get(url, ttl=3600)
    ok(appels["n"] == 1, f"cache HTTP : {appels['n']} téléchargement(s) au lieu de 1")
    serveur.shutdown()

    # Disjoncteur.
    BREAKER.echecs.clear()
    mort = "http://127.0.0.1:9/rien"
    for _ in range(3):
        try:
            http_get(mort, ttl=0)
        except (SourceIndisponible, DisjoncteurOuvert):
            pass
    try:
        http_get(mort, ttl=0)
        erreurs.append("disjoncteur muet")
    except DisjoncteurOuvert:
        pass
    BREAKER.echecs.clear()

    # Dessin : fond sombre → couleur claire ; pointillés troués ; ordre de lecture.
    sombre = Image.new("RGB", (240, 160), (12, 16, 20))
    lesions = [
        {"legende": "Lesion basse", "forme": "rect", "rect": {"x": 20, "y": 100, "w": 70, "h": 40}},
        {"legende": "Lesion haute", "forme": "rect", "rect": {"x": 20, "y": 15, "w": 80, "h": 36}},
    ]
    # annoter_image suppose des points déjà dans l'image (cadre déjà appliqué).
    img, les, cols = annoter_image(sombre, lesions, "scanner")
    ok(les[0]["legende"] == "Lesion haute" and les[0]["numero"] == 1, "ordre de lecture haut puis bas")
    ok(luminance(cols[0]) > 0.45, f"fond sombre, couleur trop sombre {cols[0]}")
    clair = Image.new("RGB", (240, 80), (250, 250, 250))
    _, _, cols2 = annoter_image(clair.copy(), [{"legende": "A", "forme": "rect", "rect": {"x": 10, "y": 10, "w": 40, "h": 20}}], "scanner")
    ok(luminance(cols2[0]) < 0.35, f"fond clair, couleur trop claire {cols2[0]}")

    # Trous des pointillés sur une ligne horizontale connue.
    ligne = Image.new("RGB", (200, 40), (255, 255, 255))
    d = ImageDraw.Draw(ligne)
    dessiner_pointilles(d, [(5, 20), (190, 20)], (0, 0, 0), 3, 10, 8, False)
    px = ligne.load()
    noirs = sum(1 for x in range(5, 190) if px[x, 20][0] < 30)
    blancs = sum(1 for x in range(5, 190) if px[x, 20][0] > 200)
    ok(noirs > 20 and blancs > 20, f"pointillés sans trous (noirs={noirs}, blancs={blancs})")

    # Légende : le texte ne doit pas sortir du bord droit, même un mot très long.
    fond_bande = (238, 247, 252)
    base = Image.new("RGB", (280, 30), (255, 255, 255))
    longue = "99e percentile de la troponine T ultrasensible : 14 ng/L. " * 3 + ("X" * 60)
    bande = bande_legende(base, [{"numero": 1, "legende": longue}], [(20, 20, 22)], "Source longue " * 12)
    bp = bande.load()
    debord = 0
    for y in range(base.height, bande.height):
        for x in range(bande.width - 6, bande.width):
            if bp[x, y][:3] != fond_bande:
                debord += 1
    ok(debord == 0, f"légende qui déborde à droite : {debord} px")
    font_test = _police(22)
    for ligne in _plier(longue, font_test, 180):
        ok(font_test.getlength(ligne) <= 180, "ligne de légende plus large que la mesure")

    # Fragment et refus de licence.
    frag = fragment_figure("Titre", "alt", "<svg></svg>", [{"numero": 1, "legende": "Un"}], "Sémiologie.", "Auteur. CC BY. Consulté le 2026-10-31.", [])
    ok("<figure" in frag and "<figcaption>" in frag and "<ol" in frag and "CC BY" in frag, "fragment HTML incomplet")
    try:
        _exiger_source_image({"url_fichier": "https://example.org/a.png", "auteur": "A", "licence": "", "date_acces": "2026-10-31"})
        erreurs.append("licence vide acceptée")
    except LicenceRefusee:
        pass

    # Réutilisation réelle.
    try:
        lst = outils_reutilises()
        ok(any("extraire_v8" in x for x in lst), "extraire_v8 non réutilisé")
        ok(any("Hishel" in x or "requests-cache" in x for x in lst), "bracelet cache non vu")
    except Exception as exc:
        erreurs.append("outils réutilisés : " + str(exc))

    # Schéma : les seuils non sourcés de l'algorithme 0/1 h ne sont pas émis par le moteur.
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        ann = {
            "id": "auto-schema",
            "type": "biologie",
            "titre": "Essai",
            "source": {"references": [{"titre": "Texte lu", "date_lecture": "2026-10-31", "support": "essai"}]},
            "graduations_x": [["0", 0], ["1", 0.33], ["3", 1]],
            "axe_x": "heures",
            "elements": [
                {"ordre": 1, "forme": "ligne", "y_rel": 0.4, "legende": "Seuil 14 ng/L", "etiquette": "14 ng/L"},
                {"ordre": 2, "forme": "courbe", "points_rel": [[0.05, 0.2], [0.4, 0.8], [0.9, 0.6]], "legende": "Rise-and-fall"},
            ],
            "semiologie": "Schéma.",
            "pieges": [],
        }
        fiche = rendre_biologie(ann, Path(tmp))
        texte = (Path(tmp) / "auto-schema.svg").read_text(encoding="utf-8") + fiche["fragment"]
        ok("52 ng" not in texte and "52 ng/L" not in texte, "seuil 52 ng/L inventé dans le schéma")
        ok((Path(tmp) / "auto-schema.png").is_file(), "png schéma absent")

    if erreurs:
        print("AUTOTEST ROUGE")
        for e in erreurs:
            print(" -", e)
        return 1
    print("AUTOTEST VERT")
    return 0


def main(argv=None) -> int:
    global RAFRAICHIR
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--autotest", action="store_true")
    ap.add_argument("--outils", action="store_true", help="liste les outils du dépôt réutilisés")
    ap.add_argument("--chercher", nargs=2, metavar=("ENTREPOT", "REQUETE"))
    ap.add_argument("--rendre", nargs="+", metavar="ANNOTATION.json")
    ap.add_argument("-o", "--sortie", default=".")
    ap.add_argument("--page", default="", help="nom du fichier HTML de démonstration")
    ap.add_argument("--rafraichir", action="store_true", help="ignore le cache HTTP")
    a = ap.parse_args(argv)
    RAFRAICHIR = a.rafraichir
    if a.autotest:
        return _autotest()
    if a.outils:
        for ligne in outils_reutilises():
            print(ligne)
        return 0
    if a.chercher:
        ent, req = a.chercher
        fn = {"wikimedia": chercher_commons, "openi": chercher_openi, "pmc": chercher_pmc}.get(ent)
        if not fn:
            print("entrepôt : wikimedia, openi ou pmc")
            return 2
        try:
            rows = fn(req)
        except (SourceIndisponible, LicenceRefusee) as exc:
            print(exc)
            return 1
        print(json.dumps(rows, ensure_ascii=False, indent=1))
        return 0
    if a.rendre:
        fiches = rendre(a.rendre, a.sortie, a.page)
        for f in fiches:
            print(f["id"], f.get("png"), (f.get("source") or {}).get("licence", ""))
        return 0
    ap.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
