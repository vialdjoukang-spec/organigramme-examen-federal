#!/usr/bin/env python3
"""Collecte extractive pour la page de veille INTERNAT.

Aucun modèle de langage, aucune API payante. Pour chaque source : titre, date,
lien, et un résumé extractif de 2 ou 3 phrases repris de la page liée
(meta description ou og:description si elle est informative, sinon les premières
phrases utiles de la zone principale). Coupe vers 300 caractères sur une fin de phrase. Les échecs (HTTP ≠ 200, TLS,
écran anti-robot, robots.txt) sont signalés, jamais remplacés par une invention.

Usage :
  python3 veille/collecter_pages.py \\
      --sources veille/sources.yml \\
      --etat veille/pages/empreintes.json \\
      --sortie-html veille/pages/index.html \\
      --sortie-json veille/pages/donnees.json
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import re
import ssl
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from zoneinfo import ZoneInfo

# Réutilise le lecteur existant (empreintes, robots, parseur YAML).
sys.path.insert(0, str(Path(__file__).resolve().parent))
import veille as argos  # noqa: E402

TZ = ZoneInfo("Europe/Zurich")
UA = argos.UA
CTX = ssl.create_default_context()
MOIS_FR = {
    "janvier": 1, "février": 2, "fevrier": 2, "mars": 3, "avril": 4,
    "mai": 5, "juin": 6, "juillet": 7, "août": 8, "aout": 8,
    "septembre": 9, "octobre": 10, "novembre": 11, "décembre": 12, "decembre": 12,
}
ANTI_ROBOT = ("un instant, s'il vous plaît", "un instant, s'il vous plait",
              "just a moment", "access denied by security policy",
              "attention required", "enable javascript")


def maintenant():
    return dt.datetime.now(TZ)


def iso(d: dt.datetime) -> str:
    return d.strftime("%Y-%m-%dT%H:%M:%S%z")


def lisible(d: dt.datetime) -> str:
    return d.strftime("%d.%m.%Y %H:%M") + " (Europe/Zurich)"


def fetcher(url, timeout=45):
    """Retourne (code, url_finale, corps_bytes, ctype, erreur)."""
    if not argos.robots_ok(url):
        return 0, url, b"", "", "robots.txt interdit cette page ; la veille ne la lit pas."
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept-Language": "fr-CH,fr,de-CH,de,en",
            "Accept": "text/html,application/xhtml+xml,application/rss+xml,application/atom+xml,application/xml,text/xml,*/*",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            return r.status, r.geturl(), r.read(), r.headers.get("Content-Type", ""), ""
    except Exception as exc:
        # Repli curl pour les TLS instables (constaté sur smw.ch).
        alt = fetcher_curl(url, timeout=timeout)
        if alt[0] == 200 and alt[2]:
            return alt
        code = getattr(exc, "code", None) or getattr(exc, "status", None) or 0
        return int(code or 0), url, b"", "", f"{type(exc).__name__}: {exc}"


def fetcher_curl(url, timeout=45):
    """Repli si urllib échoue sur un TLS capricieux : curl, sans inventer le contenu."""
    import subprocess, tempfile, os
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.close()
    try:
        r = subprocess.run(
            ["curl", "-sS", "-L", "--max-time", str(timeout),
             "-A", UA, "-H", "Accept-Language: fr-CH,fr,de-CH",
             "-o", tmp.name, "-w", "%{http_code} %{url_effective} %{content_type}",
             url],
            capture_output=True, text=True, timeout=timeout + 5,
        )
        parts = (r.stdout or "").strip().rsplit(" ", 2)
        if r.returncode != 0 or len(parts) < 3:
            err = (r.stderr or r.stdout or f"curl exit {r.returncode}").strip()
            return 0, url, b"", "", f"curl: {err[:200]}"
        code_s, finale, ctype = parts[-3], parts[-2], parts[-1]
        try:
            code = int(code_s)
        except ValueError:
            return 0, url, b"", "", f"curl: sortie inattendue {r.stdout[:120]}"
        corps = Path(tmp.name).read_bytes()
        if code != 200:
            return code, finale, corps, ctype, f"HTTP {code}"
        return code, finale, corps, ctype, ""
    finally:
        try:
            os.unlink(tmp.name)
        except OSError:
            pass


def decoder(corps: bytes) -> str:
    for enc in ("utf-8", "iso-8859-1", "cp1252"):
        try:
            return corps.decode(enc)
        except UnicodeDecodeError:
            continue
    return corps.decode("utf-8", "replace")


def est_anti_robot(texte: str, titre: str = "") -> bool:
    blob = (titre + " " + texte[:2000]).lower()
    return any(m in blob for m in ANTI_ROBOT)


def titre_html(texte: str) -> str:
    m = re.search(r"<title[^>]*>(.*?)</title>", texte, re.I | re.S)
    if not m:
        return ""
    return " ".join(re.sub(r"<[^>]+>", "", html.unescape(m.group(1))).split())


def strip_tags(fragment: str) -> str:
    fragment = re.sub(r"(?is)<script[^>]*>.*?</script>", " ", fragment)
    fragment = re.sub(r"(?is)<style[^>]*>.*?</style>", " ", fragment)
    fragment = re.sub(r"(?is)<br\s*/?>", " ", fragment)
    texte = re.sub(r"<[^>]+>", " ", html.unescape(fragment))
    return " ".join(texte.split())


def extraire_phrases(texte: str, n=2, maxlen=420) -> str:
    texte = " ".join((texte or "").split())
    if not texte:
        return ""
    morceaux = re.split(r"(?<=[\.\!\?…])\s+", texte)
    phrases = [p.strip() for p in morceaux if p.strip()]
    out = " ".join(phrases[:n]) if phrases else texte
    if len(out) > maxlen:
        out = out[: maxlen - 1].rsplit(" ", 1)[0] + "…"
    return out


def parse_date(valeur):
    if not valeur:
        return None
    if isinstance(valeur, dt.datetime):
        return valeur if valeur.tzinfo else valeur.replace(tzinfo=TZ)
    s = " ".join(str(valeur).strip().split())
    # ISO
    try:
        if s.endswith("Z"):
            s = s[:-1] + "+00:00"
        d = dt.datetime.fromisoformat(s)
        return d if d.tzinfo else d.replace(tzinfo=TZ)
    except ValueError:
        pass
    # RFC 2822
    try:
        from email.utils import parsedate_to_datetime
        d = parsedate_to_datetime(s)
        if d:
            return d if d.tzinfo else d.replace(tzinfo=TZ)
    except Exception:
        pass
    # jj.mm.aaaa
    m = re.search(r"\b(\d{1,2})\.(\d{1,2})\.(\d{4})\b", s)
    if m:
        return dt.datetime(int(m.group(3)), int(m.group(2)), int(m.group(1)), tzinfo=TZ)
    # 17 novembre 2026
    m = re.search(
        r"\b(\d{1,2})\s+([A-Za-zéèêëàâùûüôçÉÈÀÙÛÔÇ]+)\s+(\d{4})\b", s
    )
    if m:
        mois = MOIS_FR.get(m.group(2).lower())
        if mois:
            return dt.datetime(int(m.group(3)), mois, int(m.group(1)), tzinfo=TZ)
    return None


def dans_7_jours(d, now):
    if not d:
        return False
    if d.tzinfo is None:
        d = d.replace(tzinfo=TZ)
    delta = now.date() - d.astimezone(TZ).date()
    return dt.timedelta(0) <= delta <= dt.timedelta(days=7)


def parse_rss(corps: bytes, base: str):
    items = []
    try:
        root = ET.fromstring(corps)
    except ET.ParseError:
        return items
    # RSS 2.0
    for it in root.findall(".//item"):
        def txt(tag):
            el = it.find(tag)
            return (el.text or "").strip() if el is not None else ""
        titre = txt("title")
        lien = txt("link") or txt("guid")
        date = parse_date(txt("pubDate") or txt("date") or txt("{http://purl.org/dc/elements/1.1/}date"))
        desc = strip_tags(txt("description") or txt("{http://purl.org/rss/1.0/modules/content/}encoded"))
        if titre:
            items.append({"titre": titre, "lien": urllib.parse.urljoin(base, lien),
                          "date": date, "extrait": extraire_phrases(desc)})
    # Atom
    ns = {"a": "http://www.w3.org/2005/Atom"}
    for it in root.findall(".//{http://www.w3.org/2005/Atom}entry"):
        titre = (it.findtext("{http://www.w3.org/2005/Atom}title") or "").strip()
        lien_el = it.find("{http://www.w3.org/2005/Atom}link[@rel='alternate']") or it.find("{http://www.w3.org/2005/Atom}link")
        lien = lien_el.get("href") if lien_el is not None else ""
        date = parse_date(it.findtext("{http://www.w3.org/2005/Atom}updated") or it.findtext("{http://www.w3.org/2005/Atom}published"))
        desc = strip_tags(it.findtext("{http://www.w3.org/2005/Atom}summary") or it.findtext("{http://www.w3.org/2005/Atom}content") or "")
        if titre:
            items.append({"titre": titre, "lien": urllib.parse.urljoin(base, lien),
                          "date": date, "extrait": extraire_phrases(desc)})
    return items


TITRES_A_ECARTER = {
    "articles du bulletin actuel", "table des matières", "table des matieres",
    "vol d'ordonnances", "vol d’ordonnances", "avis de publication",
    "documents", "liens", "contact", "navigation", "footer", "cookies",
    "pdf", "zip", "2024", "2022", "2021", "2020", "2020–2023", "2020-2023",
    "breadcrumb", "recherche", "search", "sitemap", "context sidebar",
    "homepage", "main navigation", "accueil", "home", "login", "menu",
    "actualité", "actualite", "news", "communications",
}

def _titre_a_ecarter(titre: str) -> bool:
    t = (titre or "").strip().lower()
    if not t or t in TITRES_A_ECARTER or len(t) < 8:
        return True
    return False


def _extrait_utile(texte: str) -> str:
    s = extraire_phrases(texte)
    if not s:
        return ""
    # Un extrait qui n'est qu'une date n'informe pas.
    if parse_date(s) and len(s) <= 20:
        return ""
    return s


def _attr_meta(attrs: str, nom: str) -> str:
    double = re.search(rf'(?:{nom})\s*=\s*"([^"]*)"', attrs or "", re.I)
    if double:
        return html.unescape(double.group(1)).strip()
    single = re.search(rf"(?:{nom})\s*=\s*'([^']*)'", attrs or "", re.I)
    if single:
        return html.unescape(single.group(1)).strip()
    bare = re.search(rf'(?:{nom})\s*=\s*([^\s>]+)', attrs or "", re.I)
    if bare:
        return html.unescape(bare.group(1)).strip()
    return ""


def meta_candidates(texte: str):
    """Retourne des couples (origine, texte) : og d'abord, puis meta description."""
    og, metas = [], []
    for m in re.finditer(r"<meta\b([^>]*)>", texte or "", re.I):
        attrs = m.group(1)
        name = (_attr_meta(attrs, "property") or _attr_meta(attrs, "name")).lower()
        content = " ".join(_attr_meta(attrs, "content").split())
        if not content:
            continue
        if name == "og:description":
            og.append(("og", content))
        elif name in {"description", "twitter:description"}:
            metas.append(("meta", content))
    vus, cands = set(), []
    for typ, s in og + metas:
        if s not in vus:
            vus.add(s)
            cands.append((typ, s))
    return cands


BOILER_PHRASE = re.compile(
    r"(cookie|consentement|datenschutz|privacy policy|tous droits r[ée]serv[ée]s|"
    r"all rights reserved|javascript doit|[ée]nable javascript|"
    r"accepter (les |nos )?cookies|manage cookies|we use cookies|"
    r"diese (website|seite) verwendet cookies|"
    r"cette page utilise des cookies|nous utilisons des cookies|"
    r"s['’]abonner [àa] (notre|la) newsletter|follow us|suivez-nous|"
    r"aller au contenu|skip to (content|main)|zum inhalt springen|"
    r"menu principal|hauptnavigation|toggle navigation|"
    r"un instant,\s*s['’]il vous pla[iî]t)",
    re.I,
)


def phrase_utile(s: str) -> bool:
    s = " ".join((s or "").split()).strip()
    if not s or len(s) < 40:
        return False
    if BOILER_PHRASE.search(s):
        return False
    if parse_date(s) and len(s) <= 24:
        return False
    if sum(c.isalpha() for c in s) < 30:
        return False
    return True


def couper_sur_fin_de_phrase(phrases, n=3, maxlen=300) -> str:
    """Assemble 2 ou 3 phrases utiles et coupe vers 300 caractères sur une fin de phrase."""
    out = []
    for p in phrases:
        p = " ".join((p or "").split()).strip()
        if not p:
            continue
        if len(out) >= n:
            break
        candidate = (" ".join(out + [p])).strip()
        if out and len(candidate) > maxlen:
            break
        if not out and len(p) > maxlen:
            window = p[: maxlen + 40]
            cut = None
            for i in range(min(len(window) - 1, maxlen + 20), 160, -1):
                if window[i] in ".!?…" and (i + 1 == len(window) or window[i + 1].isspace()):
                    cut = i + 1
                    break
            if cut:
                out.append(window[:cut].strip())
            else:
                out.append(p[:maxlen].rsplit(" ", 1)[0].rstrip(",;:") + "…")
            break
        out.append(p)
        if len(" ".join(out)) >= 220 and len(out) >= 2:
            break
    return " ".join(out)


def description_informative(s: str, titre: str = "") -> bool:
    s = " ".join((s or "").split())
    if len(s) < 40 or not phrase_utile(s) and len(s) < 80:
        # une meta un peu courte mais informative (sans boiler) reste admissible dès 40 caractères
        if len(s) < 40 or BOILER_PHRASE.search(s):
            return False
    if BOILER_PHRASE.search(s):
        return False
    t = (titre or "").strip().lower()
    a = s.lower().strip()
    if t and (a == t or a.startswith(t + " |") or a.startswith(t + " –") or a.startswith(t + " -")):
        if len(s) < len(titre) + 30:
            return False
    return True


def retirer_zones_parasites(fragment: str) -> str:
    t = fragment or ""
    t = re.sub(r"(?is)<!--.*?-->", " ", t)
    t = re.sub(r"(?is)<script\b[^>]*>.*?</script>", " ", t)
    t = re.sub(r"(?is)<style\b[^>]*>.*?</style>", " ", t)
    t = re.sub(r"(?is)<noscript\b[^>]*>.*?</noscript>", " ", t)
    for tag in ("nav", "footer", "aside", "form"):
        t = re.sub(rf"(?is)<{tag}\b[^>]*>.*?</{tag}>", " ", t)
    t = re.sub(r"(?is)<header\b[^>]*>.*?</header>", " ", t)
    t = re.sub(
        r'(?is)<(div|section|aside|p)\b[^>]*(id|class)=["\'][^"\']*(cookie|consent|banner-cc|onetrust|gdpr|datenschutz-banner)[^"\']*["\'][^>]*>.*?</\1>',
        " ",
        t,
    )
    return t


def _plus_long_bloc(texte: str, tag: str) -> str:
    blocs = re.findall(rf"(?is)<{tag}\b[^>]*>(.*?)</{tag}>", texte or "")
    if not blocs:
        return ""
    blocs.sort(key=lambda b: len(strip_tags(b)), reverse=True)
    return blocs[0]


def zone_principale(texte: str) -> str:
    t = texte or ""
    main = _plus_long_bloc(t, "main")
    article = _plus_long_bloc(t, "article")
    chosen = ""
    if len(strip_tags(main)) >= 80:
        chosen = main
    elif len(strip_tags(article)) >= 80:
        chosen = article
    else:
        m = re.search(r"(?is)<body[^>]*>(.*)</body>", t)
        chosen = m.group(1) if m else t
    return retirer_zones_parasites(chosen)


def phrases_depuis_zone(zone_html: str, n=3, maxlen=300) -> str:
    paras = []
    for m in re.finditer(r"(?is)<p\b[^>]*>(.*?)</p>", zone_html or ""):
        s = strip_tags(m.group(1))
        if s:
            paras.append(s)
    if not paras:
        paras = [strip_tags(zone_html or "")]
    phrases = []
    for p in paras:
        for morceau in re.split(r"(?<=[\.\!\?…])\s+", p):
            s = " ".join(morceau.split()).strip()
            if phrase_utile(s):
                phrases.append(s)
    # Pages d'actualité sans paragraphe utile : on reprend les titres de la zone principale.
    if not phrases:
        for m in re.finditer(r"(?is)<h([1-4])[^>]*>(.*?)</h\1>", zone_html or ""):
            s = " ".join(strip_tags(m.group(2)).split()).strip()
            if _titre_a_ecarter(s):
                continue
            if len(s) >= 40 and not BOILER_PHRASE.search(s):
                phrases.append(s)
    return couper_sur_fin_de_phrase(phrases, n=n, maxlen=maxlen)


def resume_extractif(texte: str, titre: str = ""):
    """Résumé extractif déterministe : meta/og si informatifs, sinon phrases de la zone principale.

    Retourne (resume, origine) avec origine dans {'og','meta','main',''}.
    """
    for typ, s in meta_candidates(texte):
        if description_informative(s, titre=titre):
            phrases = [p.strip() for p in re.split(r"(?<=[\.\!\?…])\s+", s) if p.strip()]
            resume = couper_sur_fin_de_phrase(phrases, n=3, maxlen=300) or s[:300]
            return resume, typ
    resume = phrases_depuis_zone(zone_principale(texte))
    return resume, ("main" if resume else "")


MOTIF_CLE = re.compile(
    r"(d[ée]lai|inscription|anmeldefrist|anmeldung|"
    r"jusqu['’]?au|bis zum|bis am|"
    r"frais|émolument|emolument|taxe d['’]examen|geb[üu]hr|"
    r"chf\s*[\d'’]+|"
    r"date (de l['’])?examen|examen a lieu|pr[üu]fungstermin|"
    r"session d['’]examen|examen [ée]crit|examen oral|"
    r"schriftliche pr[üu]fung|mündliche pr[üu]fung)",
    re.I,
)


def contenu_cle_examen(texte: str) -> str:
    """Extrait des phrases déjà présentes qui portent dates, délais ou frais. N'invente rien."""
    zone = zone_principale(texte)
    blocs = []
    for m in re.finditer(
        r"(?is)<p\b[^>]*>.*?</p>|<li\b[^>]*>.*?</li>|<h[1-4][^>]*>.*?</h[1-4]>",
        zone or texte or "",
    ):
        s = strip_tags(m.group(0))
        if s:
            blocs.append(s)
    if not blocs:
        blocs = [strip_tags(zone or texte or "")]
    retenus, vus = [], set()
    for bloc in blocs:
        for s in re.split(r"(?<=[\.\!\?…;:])\s+", bloc):
            s = " ".join(s.split()).strip(" •·-–")
            if len(s) < 24 or len(s) > 280:
                continue
            if not MOTIF_CLE.search(s):
                continue
            a_date = re.search(
                r"\b(\d{1,2}[./]\d{1,2}[./]\d{2,4}|\d{1,2}\s+(?:janvier|f[ée]vrier|mars|avril|mai|juin|juillet|ao[ûu]t|septembre|octobre|novembre|d[ée]cembre|januar|februar|märz|april|mai|juni|juli|august|september|oktober|november|dezember)\s+\d{4})\b",
                s,
                re.I,
            )
            a_frais = re.search(r"chf\s*[\d'’]+", s, re.I)
            a_delai = re.search(r"d[ée]lai|anmeldefrist|jusqu['’]?au|bis zum|bis am", s, re.I)
            a_fait = re.search(
                r"doit|fix[ée]|jusqu['’]?au|bis zum|bis am|s['’]inscrire|anmelden|betr[äa]gt|s['’][eé]l[eè]ve",
                s,
                re.I,
            )
            # Un intitulé court du type « Tableau des délais » n'est pas un fait.
            if not (a_date or a_frais) and not (a_delai and a_fait and len(s) >= 60):
                continue
            # Les intitulés de fichiers (PDF, poids) ne sont pas un fait de calendrier.
            if re.search(r"\bPDF\b|\bkB\b", s, re.I):
                continue
            key = s.lower()
            if key in vus:
                continue
            vus.add(key)
            retenus.append(s)
            if len(retenus) >= 3:
                break
        if len(retenus) >= 3:
            break
    return " ".join(retenus)


def libelle_ligne_argos(ligne: str) -> str:
    parts = (ligne or "").split(" | ")
    if not parts:
        return ""
    if parts[0] == "titre" and len(parts) > 1:
        return parts[-1].strip()
    if parts[0] == "lien" and len(parts) >= 2:
        return parts[1].strip()
    return ""


IGNORER_DIFF = re.compile(
    r"google\.(ch|com)/maps|indiquer l['’]emplacement|"
    r"^\+41|^(contact|login|menu|home|accueil|suche|search)$|"
    r"^tel:|^mailto:",
    re.I,
)


def diff_changement(lignes_avant, lignes_apres) -> str:
    """Compare les titres et intitulés de liens ; n'invente aucun mot."""
    def utiles(lignes):
        out, vus = [], set()
        for l in lignes or []:
            lab = libelle_ligne_argos(l)
            if not lab or len(lab) < 8 or IGNORER_DIFF.search(lab):
                continue
            key = lab.lower()
            if key in vus:
                continue
            vus.add(key)
            out.append(lab)
        return out

    avant, apres = utiles(lignes_avant), utiles(lignes_apres)
    sa, sb = set(avant), set(apres)
    ajouts = [x for x in apres if x not in sa]
    retraits = [x for x in avant if x not in sb]
    if not ajouts and not retraits:
        return ""
    morceaux = []
    if ajouts:
        suite = " ; ".join(f"« {x} »" for x in ajouts[:4])
        if len(ajouts) > 4:
            suite += "…"
        morceaux.append("ajouté : " + suite)
    if retraits:
        suite = " ; ".join(f"« {x} »" for x in retraits[:4])
        if len(retraits) > 4:
            suite += "…"
        morceaux.append("retiré : " + suite)
    texte = " ; ".join(morceaux)
    if texte and not texte.endswith("."):
        texte += "."
    return texte


def meme_page(a: str, b: str) -> bool:
    def norm(u):
        u = urllib.parse.urldefrag(u or "")[0]
        p = urllib.parse.urlparse(u)
        path = (p.path or "/").rstrip("/") or "/"
        return (p.scheme, (p.netloc or "").lower(), path, p.query)
    return bool(a and b and norm(a) == norm(b))


def resume_page_liee(url, cache, page_source_url, texte_source, titre_source="", timeout=15):
    """Résumé de la page pointée par le lien. Ne reprend pas le résumé d'accueil si le lien est le même."""
    if not url or url.lower().startswith(("mailto:", "tel:", "javascript:")):
        return "", "aucune"
    if re.search(r"\.pdf(\?|$)", url, re.I):
        return "", "pdf"
    # Même page que la source : on ne refetch pas ; l'appelant utilisera l'extrait local.
    if meme_page(url, page_source_url):
        return "", "meme-page"
    cle = urllib.parse.urldefrag(url)[0]
    if cle in cache:
        return cache[cle]
    code, finale, corps, ctype, err = fetcher(url, timeout=timeout)
    if err or code != 200 or not corps:
        cache[cle] = ("", "inaccessible")
        return cache[cle]
    ct = (ctype or "").lower()
    if "pdf" in ct or corps[:5] == b"%PDF-":
        cache[cle] = ("", "pdf")
        return cache[cle]
    texte = decoder(corps)
    titre = titre_html(texte)
    if est_anti_robot(texte, titre):
        cache[cle] = ("", "anti-robot")
        return cache[cle]
    r, o = resume_extractif(texte, titre=titre)
    cache[cle] = (r, o or "main")
    return cache[cle]


def extrait_suffisant(s: str) -> bool:
    """Un extrait trop court, ou qui n'est qu'une date, n'aide pas à décider si l'on clique."""
    s = " ".join((s or "").split()).strip()
    if len(s) < 60:
        return False
    if parse_date(s) and len(s) <= 40:
        return False
    return True


def enrichir_items(items, page_url, texte_source, cache):
    """Place un résumé extractif de la page liée sous chaque item ; garde l'extrait local en repli."""
    out = []
    for it in items:
        lien = it.get("lien") or ""
        local = (it.get("extrait") or "").strip()
        resume, origine = resume_page_liee(lien, cache, page_url, texte_source)
        if origine == "meme-page":
            if not extrait_suffisant(local):
                # Même page que le bloc source, déjà résumé en tête : on n'ajoute pas un sous-lien vide.
                continue
            resume, origine = local, "liste"
        elif resume:
            pass
        elif extrait_suffisant(local):
            resume, origine = local, "liste"
        else:
            resume, origine = "", origine or "vide"
        it = dict(it)
        it["extrait"] = resume
        it["origine_resume"] = origine
        out.append(it)
    return out


def semer_lignes_argos(etat: dict, chemin="veille/etat.json"):
    """Reprend les titres déjà vus par la veille Argos, uniquement s'ils manquent encore."""
    etat.setdefault("lignes", {})
    path = Path(chemin)
    if not path.exists():
        return etat
    try:
        ae = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return etat
    for groupe in ae.values() if isinstance(ae, dict) else []:
        if not isinstance(groupe, dict):
            continue
        for u, lg in (groupe.get("lignes") or {}).items():
            if u not in etat["lignes"] and lg:
                etat["lignes"][u] = lg
    return etat


def parse_ofsp_cards(texte: str, base: str):
    """Cartes datées du design fédéral (Bulletin OFSP, portail News)."""
    items = []
    # Chaque carte : date dans meta-info, titre h2, éventuellement un paragraphe, un lien.
    for m in re.finditer(
        r'<span class="meta-info__item">([^<]+)</span>[\s\S]{0,800}?<h2[^>]*>(.*?)</h2>([\s\S]{0,2000}?)(?:</li>|</article>|</div></div></div>)',
        texte,
        re.I,
    ):
        date = parse_date(strip_tags(m.group(1)))
        titre = strip_tags(m.group(2))
        suite = m.group(3)
        if _titre_a_ecarter(titre):
            continue
        href = ""
        lm = re.search(r'href="([^"]+)"', suite)
        if lm:
            href = urllib.parse.urljoin(base, html.unescape(lm.group(1)))
        # premier paragraphe
        pm = re.search(r"<p[^>]*>(.*?)</p>", suite, re.S | re.I)
        extrait = _extrait_utile(strip_tags(pm.group(1))) if pm else ""
        if titre:
            items.append({"titre": titre, "lien": href or base, "date": date, "extrait": extrait})
    return items


def parse_swissmedic_teasers(texte: str, base: str):
    items = []
    for m in re.finditer(
        r'teaserDate">([^<]+)</p>\s*<h3>\s*<a href="([^"]+)"[^>]*>(.*?)</a>',
        texte,
        re.S | re.I,
    ):
        date = parse_date(strip_tags(m.group(1)))
        lien = urllib.parse.urljoin(base, html.unescape(m.group(2)))
        titre = strip_tags(m.group(3))
        # paragraphe éventuellement juste après
        after = texte[m.end(): m.end() + 800]
        pm = re.search(r"<p[^>]*>(.*?)</p>", after, re.S | re.I)
        extrait = _extrait_utile(strip_tags(pm.group(1))) if pm else ""
        if titre:
            items.append({"titre": titre, "lien": lien, "date": date, "extrait": extrait})
    return items


def parse_titres_generiques(texte: str, base: str, limite=8):
    """Reprend des titres h2/h3 et, s'il y en a, une date et un paragraphe voisins."""
    items = []
    # Coupe nav/footer grossièrement : zone main si possible
    main = texte
    mm = re.search(r"(?is)<main[^>]*>(.*)</main>", texte)
    if mm:
        main = mm.group(1)
    for m in re.finditer(r"<h([23])[^>]*>(.*?)</h\1>", main, re.S | re.I):
        titre = strip_tags(m.group(2))
        if _titre_a_ecarter(titre) or len(titre) > 220:
            continue
        if titre.lower() in {"menu", "navigation", "footer", "cookie", "contact", "login",
                             "suche", "search", "home", "accueil", "news"}:
            continue
        fenetre = main[max(0, m.start() - 400): m.end() + 700]
        date = parse_date(fenetre)
        href = ""
        # lien dans le titre ou juste après
        lm = re.search(r'href="([^"]+)"', m.group(2)) or re.search(r'href="([^"]+)"', main[m.end(): m.end() + 300])
        if lm:
            href = urllib.parse.urljoin(base, html.unescape(lm.group(1)))
        pm = re.search(r"<p[^>]*>(.*?)</p>", main[m.end(): m.end() + 800], re.S | re.I)
        extrait = _extrait_utile(strip_tags(pm.group(1))) if pm else ""
        items.append({"titre": titre, "lien": href or base, "date": date, "extrait": extrait})
        if len(items) >= limite:
            break
    return items


def serialiser_item(it):
    d = it.get("date")
    return {
        "titre": it.get("titre") or "",
        "date": d.strftime("%Y-%m-%d") if isinstance(d, dt.datetime) else (d or None),
        "date_lisible": d.strftime("%d.%m.%Y") if isinstance(d, dt.datetime) else None,
        "lien": it.get("lien") or "",
        "extrait": it.get("extrait") or "",
        "origine_resume": it.get("origine_resume") or "",
    }


def collecter(sources, etat, now):
    examen, sante, societes, autres = [], [], [], []
    rapport = []

    for ident, src in sources.items():
        if not isinstance(src, dict) or not src.get("onglet"):
            continue  # ve1 / ve2 et clés sans onglet : laissées aux workflows existants
        onglet = src["onglet"]
        nom = src.get("nom") or ident
        urls = src.get("urls") or []
        methode = src.get("methode") or "html"
        entree = {
            "id": ident,
            "nom": nom,
            "onglet": onglet,
            "url": urls[0] if urls else "",
            "statut": "à lire",
            "http": None,
            "accessible": False,
            "motif": "",
            "titre_page": "",
            "empreinte": None,
            "changee": False,
            "date_detection": None,
            "items": [],
            "resume": "",
            "origine_resume": "",
            "contenu_cle": "",
            "ce_qui_a_change": "",
        }
        if not urls:
            entree["statut"] = "source non accessible"
            entree["motif"] = "Aucune URL n'est enregistrée."
            _ranger(onglet, entree, examen, sante, societes, autres)
            continue

        # On lit la première URL (une entrée = une page officielle).
        url = urls[0]
        code, finale, corps, ctype, err = fetcher(url)
        entree["http"] = code
        entree["url"] = finale or url
        if err or code != 200 or not corps:
            entree["statut"] = "source non accessible"
            entree["motif"] = err or f"HTTP {code or '—'}."
            rapport.append(f"{ident} : non accessible ({entree['motif']})")
            _ranger(onglet, entree, examen, sante, societes, autres)
            continue

        texte = decoder(corps)
        titre = titre_html(texte)
        entree["titre_page"] = titre
        if est_anti_robot(texte, titre):
            entree["statut"] = "source non accessible"
            entree["motif"] = "La page ne livre qu'un écran d'attente ou une protection anti-robot."
            rapport.append(f"{ident} : anti-robot ({url})")
            _ranger(onglet, entree, examen, sante, societes, autres)
            continue

        entree["accessible"] = True
        entree["statut"] = "active"

        # Empreinte à la manière d'Argos (titres et liens de <main>),
        # calculée sur le corps déjà téléchargé : on évite une seconde requête.
        lignes = []
        try:
            parser = argos.Main(finale or url)
            parser.feed(texte)
            lignes = [s for z, s in parser.items if z or not parser.has_main]
            lignes = sorted(set(lignes))
        except Exception:
            lignes = []
        if not lignes:
            lignes = [f"titre | {titre}"] if titre else []
        emp = hashlib.sha256("\n".join(lignes).encode()).hexdigest()
        entree["empreinte"] = emp
        avant = (etat.get("empreintes") or {}).get(url) or (etat.get("empreintes") or {}).get(ident)
        if avant is None:
            entree["changee"] = False
            entree["date_detection"] = iso(now)
            entree["motif"] = "État initial enregistré."
        elif avant != emp:
            entree["changee"] = True
            entree["date_detection"] = iso(now)
        else:
            # conserve la date de dernière modification connue
            ancienne = (etat.get("dates") or {}).get(url) or (etat.get("dates") or {}).get(ident)
            entree["date_detection"] = ancienne
            entree["changee"] = False

        resume, origine = resume_extractif(texte, titre=titre)
        entree["resume"] = resume
        entree["origine_resume"] = origine
        if onglet == "examen":
            entree["contenu_cle"] = contenu_cle_examen(texte)
        avant_lignes = (etat.get("lignes") or {}).get(url) or (etat.get("lignes") or {}).get(ident) or []
        if entree["changee"]:
            detail = diff_changement(avant_lignes, lignes)
            if detail:
                entree["ce_qui_a_change"] = detail
            elif avant_lignes:
                entree["ce_qui_a_change"] = (
                    "L'empreinte a changé, mais aucun titre ou phrase distincte n'a pu être isolé."
                )
            else:
                entree["ce_qui_a_change"] = (
                    "L'empreinte a changé ; les titres précédents n'étaient pas encore enregistrés, "
                    "le détail des phrases ajoutées ou retirées n'est donc pas disponible."
                )
        entree["_lignes"] = lignes

        items = []
        if "xml" in (ctype or "").lower() or corps.lstrip()[:20].lower().startswith(b"<?xml") or b"<rss" in corps[:400].lower() or b"<feed" in corps[:400].lower():
            items = parse_rss(corps, finale or url)
        if not items and ("ofsp" in ident or "bulletin" in ident):
            items = parse_ofsp_cards(texte, finale or url)
        if not items and "swissmedic" in ident:
            items = parse_swissmedic_teasers(texte, finale or url)
            if not items:
                items = parse_ofsp_cards(texte, finale or url)
        if not items:
            items = parse_titres_generiques(texte, finale or url)

        if onglet == "sante":
            items = [it for it in items if dans_7_jours(it.get("date"), now)]
        cache_pages = etat.setdefault("_cache_resumes", {})
        a_lire = items[:12]
        if a_lire:
            print(f"  {ident} : résumé de {len(a_lire)} page(s) liée(s)…", flush=True)
        items = enrichir_items(a_lire, finale or url, texte, cache_pages)
        entree["items"] = [serialiser_item(it) for it in items]
        rapport.append(
            f"{ident} : HTTP {code}, {len(entree['items'])} extrait(s), "
            f"empreinte {emp[:12]}{' · changée' if entree['changee'] else ''}."
        )
        _ranger(onglet, entree, examen, sante, societes, autres)

    return {
        "collectee_le": iso(now),
        "collectee_lisible": lisible(now),
        "fenetre_sante": {
            "debut": (now.date() - dt.timedelta(days=7)).isoformat(),
            "fin": now.date().isoformat(),
        },
        "examen": examen,
        "sante": sante,
        "societes": societes,
        "autres": autres,
        "rapport": rapport,
    }, rapport


def _ranger(onglet, entree, examen, sante, societes, autres):
    if onglet == "examen":
        examen.append(entree)
    elif onglet == "sante":
        sante.append(entree)
    elif onglet == "societes":
        societes.append(entree)
    else:
        autres.append(entree)


def rendre_html(donnees: dict) -> str:
    def esc(s):
        return html.escape(str(s or ""), quote=True)

    def badge(src):
        if src["accessible"] and src.get("changee"):
            return '<span class="badge badge-change">page modifiée</span>'
        if src["accessible"]:
            return '<span class="badge badge-ok">source active</span>'
        return '<span class="badge badge-off">source non accessible</span>'

    def bloc_resume(texte, vide=False):
        if texte:
            return f'<p class="resume">{esc(texte)}</p>'
        if vide:
            return '<p class="resume vide-resume">Aucun résumé extractif n\'a pu être repris sur cette page.</p>'
        return ""

    def bloc_lien_date(href, libelle, date=""):
        date_html = f'<time>{esc(date)}</time>' if date else ""
        return (
            f'<p class="lien-date"><a href="{esc(href)}">{esc(libelle)}</a>'
            f'{(" · " + date_html) if date_html else ""}</p>'
        )

    def details_techniques(src):
        morceaux = []
        if src.get("http"):
            morceaux.append(f'HTTP {esc(src["http"])}')
        if src.get("empreinte"):
            morceaux.append(f'empreinte {esc(src["empreinte"])}')
        if src.get("date_detection"):
            d = src["date_detection"]
            try:
                d = dt.datetime.fromisoformat(d).astimezone(TZ).strftime("%d.%m.%Y %H:%M") + " (Europe/Zurich)"
            except ValueError:
                pass
            morceaux.append(f'dernière détection {esc(d)}')
        if not morceaux:
            return ""
        return (
            '<details class="technique"><summary>Détails techniques</summary>'
            f'<p>{esc(" · ".join(html.unescape(m) for m in morceaux))}</p></details>'
        )

    def liste_items(items, vide):
        if not items:
            return f'<p class="vide">{esc(vide)}</p>'
        lis = []
        for it in items:
            date = it.get("date_lisible") or it.get("date") or ""
            titre = it.get("titre") or "(sans titre)"
            href = it.get("lien") or "#"
            resume = bloc_resume(it.get("extrait"))
            if not resume:
                resume = '<p class="resume vide-resume">Aucun résumé extractif n\'a pu être repris sur la page liée.</p>'
            lis.append(
                f'<li>{resume}{bloc_lien_date(href, titre, date)}</li>'
            )
        return "<ul class='items'>" + "".join(lis) + "</ul>"

    def bloc_source(src, avec_items=True):
        motif = f'<p class="motif">{esc(src.get("motif"))}</p>' if src.get("motif") and not src["accessible"] else ""
        resume = bloc_resume(src.get("resume"), vide=bool(src.get("accessible")))
        cle = ""
        if src.get("contenu_cle"):
            cle = f'<p class="contenu-cle"><span class="libelle">Contenu clé.</span> {esc(src["contenu_cle"])}</p>'
        chg = ""
        if src.get("ce_qui_a_change"):
            chg = f'<p class="changement"><span class="libelle">Ce qui a changé.</span> {esc(src["ce_qui_a_change"])}</p>'
        date = ""
        if src.get("date_detection"):
            d = src["date_detection"]
            try:
                date = dt.datetime.fromisoformat(d).astimezone(TZ).strftime("%d.%m.%Y")
            except ValueError:
                date = d
        lien = bloc_lien_date(src.get("url") or "#", src.get("url") or "", date)
        items = liste_items(src.get("items") or [], "Aucun extrait daté n'a été repris sur cette page.") if avec_items else ""
        return f"""
        <article class="source {'ok' if src['accessible'] else 'ko'}" id="{esc(src['id'])}">
          <header>
            <h3>{esc(src['nom'])}</h3>
            {badge(src)}
          </header>
          {resume}{cle}{chg}{lien}
          {details_techniques(src)}
          {motif}{items}
        </article>"""

    # Santé : liste plate des 7 jours, dépliable
    items_sante = []
    for src in donnees.get("sante") or []:
        for it in src.get("items") or []:
            items_sante.append((src, it))
    def key_date(pair):
        return pair[1].get("date") or ""
    items_sante.sort(key=key_date, reverse=True)

    lis_sante = []
    for src, it in items_sante:
        date = it.get("date_lisible") or it.get("date") or ""
        titre = it.get("titre") or "(sans titre)"
        href = it.get("lien") or src["url"]
        resume = bloc_resume(it.get("extrait"))
        if not resume:
            resume = '<p class="resume vide-resume">Aucun résumé extractif n\'a pu être repris sur la page liée.</p>'
        lis_sante.append(
            f'<li>{resume}'
            f'<p class="lien-date"><a href="{esc(href)}">{esc(titre)}</a>'
            f'{(" · <time>" + esc(date) + "</time>") if date else ""}'
            f' · <span class="src">{esc(src["nom"])}</span></p></li>'
        )
    n_sante = len(lis_sante)
    liste_sante = (
        f'<ul class="defilable" id="liste-sante">{"".join(lis_sante)}</ul>'
        if lis_sante
        else '<p class="vide">Aucune actualité datée des 7 derniers jours n\'a été reprise sur les sources accessibles.</p>'
    )

    sources_sante = "".join(bloc_source(s, avec_items=False) for s in donnees.get("sante") or [])
    examen_html = "".join(bloc_source(s, avec_items=False) for s in donnees.get("examen") or [])
    societes_html = "".join(bloc_source(s, avec_items=True) for s in donnees.get("societes") or [])
    autres_html = "".join(bloc_source(s, avec_items=True) for s in donnees.get("autres") or [])

    n_act = sum(1 for s in (donnees.get("examen") + donnees.get("sante") + donnees.get("societes") + donnees.get("autres")) if s["accessible"])
    n_tot = len(donnees.get("examen") + donnees.get("sante") + donnees.get("societes") + donnees.get("autres"))
    fen = donnees.get("fenetre_sante") or {}

    css = """
:root { --fond:#f5f6f8; --papier:#fff; --encre:#101828; --encre-2:#344054; --encre-3:#5d6b82;
  --trait:#d9dee7; --calme:#1d4e89; --calme-fond:#eef4fb; --bon:#0e7a3b; --bon-fond:#ecfaf1;
  --attention:#a14a06; --attention-fond:#fff6ea; --urgence:#b42318; --urgence-fond:#fef3f2;
  --police:"Inter",system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif; }
* { box-sizing:border-box; }
html { font-size:18px; }
body { margin:0; font-family:var(--police); color:var(--encre); background:
  radial-gradient(1000px 480px at 0% -10%, #e8eef8, transparent 60%),
  radial-gradient(800px 400px at 100% 0%, #eef6ef, transparent 50%), var(--fond);
  line-height:1.5; }
header.haut, main, footer.pied { max-width:1080px; margin:0 auto; padding:0 1.25rem; }
header.haut { padding-top:2rem; }
.marque { display:flex; gap:.6rem; align-items:baseline; flex-wrap:wrap; }
.marque-logo { display:inline-grid; place-items:center; width:2rem; height:2rem; border-radius:8px;
  background:var(--calme); color:#fff; font-weight:700; }
.marque-nom { font-weight:700; font-size:1.35rem; }
.marque a { color:var(--calme); }
h1 { font-size:clamp(1.7rem,3vw,2.3rem); letter-spacing:-.03em; margin:1rem 0 .4rem; }
.accroche { color:var(--encre-2); max-width:46rem; }
.meta-collecte { color:var(--encre-3); font-size:.92rem; }
.onglets { display:flex; gap:.4rem; flex-wrap:wrap; margin:1.4rem 0 0; padding:0; list-style:none; }
.onglets button { font:inherit; font-weight:650; border:1px solid var(--trait); background:var(--papier);
  border-radius:999px; padding:.4rem .9rem; cursor:pointer; color:var(--encre-2); }
.onglets button[aria-selected="true"] { background:var(--calme); color:#fff; border-color:var(--calme); }
.panneau { display:none; padding:1.2rem 0 2.5rem; }
.panneau.actif { display:block; }
.source { background:var(--papier); border:1px solid var(--trait); border-radius:14px;
  padding:1rem 1.1rem 1.05rem; margin:0 0 1rem; box-shadow:0 1px 2px rgba(16,24,40,.05); }
.source header { display:flex; justify-content:space-between; gap:.6rem; align-items:start; }
.source h3 { margin:0; font-size:1.05rem; }
.resume { font-size:1.02rem; color:var(--encre); margin:.7rem 0 .35rem; line-height:1.45; }
.vide-resume { color:var(--encre-3); font-style:italic; font-size:.95rem; }
.lien-date { font-size:.85rem; color:var(--encre-3); margin:.15rem 0 .35rem; word-break:break-all; }
.lien-date a, .items a, .defilable a { color:var(--calme); }
.lien-date time, .src { color:var(--encre-3); }
.contenu-cle, .changement { font-size:.95rem; color:var(--encre-2); margin:.35rem 0; line-height:1.45; }
.contenu-cle .libelle, .changement .libelle { font-weight:650; color:var(--encre); }
details.technique { font-size:.85rem; color:var(--encre-3); margin:.15rem 0 .4rem; }
details.technique summary { cursor:pointer; color:var(--encre-2); }
details.technique p { margin:.35rem 0 0; word-break:break-all; }
.badge { font-size:.75rem; font-weight:650; text-transform:uppercase; letter-spacing:.04em;
  padding:.15rem .5rem; border-radius:999px; white-space:nowrap; }
.badge-ok { background:var(--bon-fond); color:var(--bon); }
.badge-change { background:var(--attention-fond); color:var(--attention); }
.badge-off { background:var(--urgence-fond); color:var(--urgence); }
.motif { color:var(--urgence); }
.meta, .vide, .extrait { color:var(--encre-3); }
.items, .defilable { margin:.5rem 0 0; padding:0; list-style:none; }
.items li, .defilable li { margin:0; padding:.75rem 0; border-top:1px solid var(--trait); }
.items .resume, .defilable .resume { margin:.1rem 0 .3rem; }
.defilable-wrap { background:var(--papier); border:1px solid var(--trait); border-radius:14px; padding:1rem; }
.defilable { max-height:36rem; overflow:auto; padding-right:.5rem; }
.defilable.replie { max-height:0; overflow:hidden; margin:0; padding:0; }
.btn-defile { font:inherit; font-weight:650; background:var(--calme); color:#fff; border:0;
  border-radius:10px; padding:.5rem .9rem; cursor:pointer; margin:0 0 .8rem; }
h2 { font-size:1.15rem; margin:1.4rem 0 .6rem; }
footer.pied { padding:0 1.25rem 2.5rem; color:var(--encre-3); font-size:.9rem; }
footer.pied a { color:var(--calme); }
.veille-statut { font-size:.95rem; margin:.55rem 0 0; }
.veille-statut.alerte { color:var(--attention); background:var(--attention-fond);
  border-radius:8px; padding:.45rem .7rem; display:inline-block; }
.veille-statut.ok { color:var(--encre-3); }
@media (prefers-reduced-motion: reduce) { * { animation:none !important; transition:none !important; } }
"""
    js = """
(function(){
  const DONNEES_URL="https://raw.githubusercontent.com/vialdjoukang-spec/organigramme-examen-federal/veille-etat/veille/pages/donnees.json";
  const onglets=[...document.querySelectorAll('.onglets button')];
  const panneaux=[...document.querySelectorAll('.panneau')];
  function activer(id){
    onglets.forEach(b=>b.setAttribute('aria-selected', String(b.dataset.cible===id)));
    panneaux.forEach(p=>p.classList.toggle('actif', p.id===id));
    history.replaceState(null,'','#'+id.replace('panneau-','') );
  }
  onglets.forEach(b=>b.addEventListener('click',()=>activer(b.dataset.cible)));
  const hash=(location.hash||'#examen').replace('#','');
  const map={examen:'panneau-examen', sante:'panneau-sante', societes:'panneau-societes'};
  activer(map[hash]||'panneau-examen');
  function brancherListe(){
    const btn=document.getElementById('btn-defile');
    const liste=document.getElementById('liste-sante');
    if(btn && liste && !btn.dataset.lie){
      btn.dataset.lie="1";
      btn.addEventListener('click',()=>{
        const replie=liste.classList.toggle('replie');
        btn.setAttribute('aria-expanded', String(!replie));
        btn.textContent=replie ? 'Déplier la liste des 7 derniers jours' : 'Replier la liste';
      });
    }
  }
  brancherListe();

  function esc(s){
    return String(s==null?"":s).replace(/[&<>"']/g,function(c){
      if(c==="&") return "&amp;";
      if(c==="<") return "&lt;";
      if(c===">") return "&gt;";
      if(c==='"') return "&quot;";
      return "&#39;";
    });
  }
  function dateCourte(iso){
    if(!iso) return "";
    var m=String(iso).match(/^([0-9]{4})-([0-9]{2})-([0-9]{2})/);
    if(m) return m[3]+"."+m[2]+"."+m[1];
    try{
      var d=new Date(iso);
      if(!isNaN(d)){
        var dd=String(d.getDate()).padStart(2,"0");
        var mm=String(d.getMonth()+1).padStart(2,"0");
        return dd+"."+mm+"."+d.getFullYear();
      }
    }catch(e){}
    return String(iso);
  }
  function dateLongue(iso){
    if(!iso) return "";
    var s=String(iso);
    var m=s.match(/^([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2})/);
    if(m) return m[3]+"."+m[2]+"."+m[1]+" "+m[4]+":"+m[5]+" (Europe/Zurich)";
    return s;
  }
  function badge(src){
    if(src.accessible && src.changee) return '<span class="badge badge-change">page modifiée</span>';
    if(src.accessible) return '<span class="badge badge-ok">source active</span>';
    return '<span class="badge badge-off">source non accessible</span>';
  }
  function blocResume(texte, vide){
    if(texte) return '<p class="resume">'+esc(texte)+'</p>';
    if(vide) return '<p class="resume vide-resume">Aucun résumé extractif n\\'a pu être repris sur cette page.</p>';
    return "";
  }
  function blocLienDate(href, libelle, date){
    var d=date ? ' · <time>'+esc(date)+'</time>' : "";
    return '<p class="lien-date"><a href="'+esc(href)+'">'+esc(libelle)+'</a>'+d+'</p>';
  }
  function detailsTechniques(src){
    var morceaux=[];
    if(src.http) morceaux.push("HTTP "+src.http);
    if(src.empreinte) morceaux.push("empreinte "+src.empreinte);
    if(src.date_detection) morceaux.push("dernière détection "+dateLongue(src.date_detection));
    if(!morceaux.length) return "";
    return '<details class="technique"><summary>Détails techniques</summary><p>'+esc(morceaux.join(" · "))+'</p></details>';
  }
  function listeItems(items, vide){
    if(!items || !items.length) return '<p class="vide">'+esc(vide)+'</p>';
    return "<ul class='items'>"+items.map(function(it){
      var date=it.date_lisible||it.date||"";
      var titre=it.titre||"(sans titre)";
      var href=it.lien||"#";
      var resume=blocResume(it.extrait);
      if(!resume) resume='<p class="resume vide-resume">Aucun résumé extractif n\\'a pu être repris sur la page liée.</p>';
      return '<li>'+resume+blocLienDate(href,titre,date)+'</li>';
    }).join("")+"</ul>";
  }
  function blocSource(src, avecItems){
    var motif=(src.motif && !src.accessible) ? '<p class="motif">'+esc(src.motif)+'</p>' : "";
    var resume=blocResume(src.resume, !!src.accessible);
    var cle=src.contenu_cle ? '<p class="contenu-cle"><span class="libelle">Contenu clé.</span> '+esc(src.contenu_cle)+'</p>' : "";
    var chg=src.ce_qui_a_change ? '<p class="changement"><span class="libelle">Ce qui a changé.</span> '+esc(src.ce_qui_a_change)+'</p>' : "";
    var date="";
    if(src.date_detection) date=dateCourte(src.date_detection);
    var items=avecItems ? listeItems(src.items||[], "Aucun extrait daté n'a été repris sur cette page.") : "";
    return '<article class="source '+(src.accessible?'ok':'ko')+'" id="'+esc(src.id)+'">'
      +'<header><h3>'+esc(src.nom)+'</h3>'+badge(src)+'</header>'
      +resume+cle+chg+blocLienDate(src.url||"#", src.url||"", date)
      +detailsTechniques(src)+motif+items+'</article>';
  }
  function listeSante(donnees){
    var items=[];
    (donnees.sante||[]).forEach(function(src){
      (src.items||[]).forEach(function(it){ items.push({src:src,it:it}); });
    });
    items.sort(function(a,b){ return String(b.it.date||"").localeCompare(String(a.it.date||"")); });
    if(!items.length){
      return {n:0, html:'<p class="vide">Aucune actualité datée des 7 derniers jours n\\'a été reprise sur les sources accessibles.</p>'};
    }
    var html='<ul class="defilable" id="liste-sante">'+items.map(function(pair){
      var it=pair.it, src=pair.src;
      var date=it.date_lisible||it.date||"";
      var titre=it.titre||"(sans titre)";
      var href=it.lien||src.url;
      var resume=blocResume(it.extrait);
      if(!resume) resume='<p class="resume vide-resume">Aucun résumé extractif n\\'a pu être repris sur la page liée.</p>';
      return '<li>'+resume+'<p class="lien-date"><a href="'+esc(href)+'">'+esc(titre)+'</a>'
        +(date?' · <time>'+esc(date)+'</time>':'')
        +' · <span class="src">'+esc(src.nom)+'</span></p></li>';
    }).join("")+"</ul>";
    return {n:items.length, html:html};
  }
  function compteSources(donnees){
    var tous=[].concat(donnees.examen||[], donnees.sante||[], donnees.societes||[], donnees.autres||[]);
    var nAct=tous.filter(function(s){ return s.accessible; }).length;
    return {nAct:nAct, nTot:tous.length};
  }
  function appliquer(donnees){
    var fen=donnees.fenetre_sante||{};
    var c=compteSources(donnees);
    var dateEl=document.getElementById("veille-date-collecte");
    if(dateEl){
      dateEl.textContent="Collecte du "+(donnees.collectee_lisible||"")+". "
        +c.nAct+" source"+(c.nAct===1?"":"s")+" active"+(c.nAct===1?"":"s")+" sur "+c.nTot
        +". Fenêtre des actualités : du "+(fen.debut||"")+" au "+(fen.fin||"")+".";
    }
    var ex=document.getElementById("examen-sources");
    if(ex) ex.innerHTML=(donnees.examen||[]).map(function(s){ return blocSource(s,false); }).join("");
    var sante=listeSante(donnees);
    var compte=document.getElementById("sante-compte");
    if(compte) compte.textContent=sante.n+" actualité"+(sante.n===1?"":"s")+" dans les 7 derniers jours.";
    var wrap=document.querySelector(".defilable-wrap");
    if(wrap){
      var ancienne=document.getElementById("liste-sante");
      var vide=wrap.querySelector("p.vide");
      var cible=ancienne||vide;
      if(cible) cible.outerHTML=sante.html;
      else wrap.insertAdjacentHTML("beforeend", sante.html);
      var btn=document.getElementById("btn-defile");
      if(btn){ btn.dataset.lie=""; btn.setAttribute("aria-expanded","true"); btn.textContent="Replier la liste"; }
      brancherListe();
    }
    var ss=document.getElementById("sante-sources");
    if(ss) ss.innerHTML=(donnees.sante||[]).map(function(s){ return blocSource(s,false); }).join("");
    var soc=document.getElementById("societes-sources");
    if(soc) soc.innerHTML=(donnees.societes||[]).map(function(s){ return blocSource(s,true); }).join("");
    var au=document.getElementById("autres-sources");
    if(au) au.innerHTML=(donnees.autres||[]).map(function(s){ return blocSource(s,true); }).join("");
  }
  function signaler(ok, message){
    var el=document.getElementById("veille-statut");
    if(!el) return;
    el.hidden=!message;
    el.className="veille-statut"+(ok?" ok":" alerte");
    el.textContent=message||"";
  }
  fetch(DONNEES_URL+"?t="+Date.now(), {cache:"no-store"})
    .then(function(r){
      if(!r.ok) throw new Error("HTTP "+r.status);
      return r.json();
    })
    .then(function(d){
      if(!d || !d.collectee_lisible || !Array.isArray(d.examen)) throw new Error("format");
      appliquer(d);
      signaler(true, "");
    })
    .catch(function(){
      signaler(false, "Le chargement de la dernière collecte a échoué ; voici la dernière version embarquée.");
    });
})();
"""
    return f"""<!doctype html>
<html lang="fr-CH">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Veille · Internat — examen fédéral, santé publique, sociétés savantes</title>
  <meta name="description" content="Veille gratuite, hébergée sur GitHub : sous chaque lien, un résumé extractif de deux ou trois phrases repris de la page, pour décider d'un coup d'œil si tu cliques.">
  <style>{css}</style>
</head>
<body>
  <header class="haut">
    <p class="marque">
      <span class="marque-logo" aria-hidden="true">+</span>
      <span class="marque-nom">Internat · Veille</span>
      <a href="https://vialdjoukang-spec.github.io/organigramme-examen-federal/jeu-revision/">Le jeu</a>
      ·
      <a href="https://vialdjoukang-spec.github.io/organigramme-examen-federal/jeu-revision/catalogue.html">Le catalogue</a>
    </p>
    <h1>La veille du médecin interne</h1>
    <p class="accroche">Sous chaque lien, tu lis d'abord un résumé de deux ou trois phrases repris de la page liée : tu décides d'un coup d'œil si tu cliques. Rien n'est inventé, aucun modèle de langage n'intervient, aucun abonnement n'est demandé.</p>
    <p class="meta-collecte" id="veille-date-collecte">Collecte du {esc(donnees.get('collectee_lisible'))}. {n_act} source{'' if n_act==1 else 's'} active{'' if n_act==1 else 's'} sur {n_tot}. Fenêtre des actualités : du {esc(fen.get('debut'))} au {esc(fen.get('fin'))}.</p>
    <p class="veille-statut" id="veille-statut" hidden></p>
    <ul class="onglets" role="tablist">
      <li><button type="button" role="tab" data-cible="panneau-examen" aria-selected="true">0. Examen fédéral</button></li>
      <li><button type="button" role="tab" data-cible="panneau-sante" aria-selected="false">1. Santé publique suisse</button></li>
      <li><button type="button" role="tab" data-cible="panneau-societes" aria-selected="false">2. Sociétés savantes</button></li>
    </ul>
  </header>
  <main>
    <section class="panneau actif" id="panneau-examen" role="tabpanel">
      <h2>Pages officielles de l'examen</h2>
      <p>Sous chaque page officielle (OFSP, MEBEKO, IML Berne, portail d'inscription), tu lis d'abord le résumé extractif, puis le lien et la date. Les dates, délais et frais détectés apparaissent sous « Contenu clé ». Si l'empreinte change, une ligne « Ce qui a changé » reprend les titres ou phrases ajoutés et retirés. L'empreinte et le code HTTP restent dans un détail repliable.</p>
      <div id="examen-sources">{examen_html}</div>
    </section>
    <section class="panneau" id="panneau-sante" role="tabpanel">
      <h2>Actualités des 7 derniers jours</h2>
      <p>La liste reprend les communications officiellement datées de l'OFSP (Bulletin) et de Swissmedic, dans la fenêtre indiquée ci-dessus. Sous chaque lien, le résumé extractif de la page liée précède le titre. Clique le bouton pour déplier ou replier la liste.</p>
      <div class="defilable-wrap">
        <button type="button" class="btn-defile" id="btn-defile" aria-expanded="true" aria-controls="liste-sante">Replier la liste</button>
        <p class="meta-collecte" id="sante-compte">{n_sante} actualité{'' if n_sante==1 else 's'} dans les 7 derniers jours.</p>
        {liste_sante}
      </div>
      <h2>Sources de ce panneau</h2>
      <div id="sante-sources">{sources_sante}</div>
    </section>
    <section class="panneau" id="panneau-societes" role="tabpanel">
      <h2>Par société savante</h2>
      <p>Chaque bloc commence par le résumé de la page d'accueil de la société. Sous chaque lien, le résumé de la page liée te permet de décider si tu cliques. Une société dont le site refuse la lecture (protection, certificat, erreur HTTP) reste visible et porte la mention « source non accessible ».</p>
      <div id="societes-sources">{societes_html}</div>
      <h2>Autres veilles utiles</h2>
      <p>Sommaires de la Revue Médicale Suisse et du Swiss Medical Weekly, et page d'actualité de Swissmedic, lorsque ces pages répondent. Le résumé de chaque article lié précède le lien.</p>
      <div id="autres-sources">{autres_html}</div>
    </section>
  </main>
  <footer class="pied">
    <p>Cette veille ne coûte rien : un workflow GitHub Actions, public, tourne une fois par jour, sans API payante et sans modèle de langage. Il n'écrit que sur la branche <code>veille-etat</code>, jamais sur <code>main</code>. À chaque ouverture, la page recharge ces données (avec un cache-buster) ; si le chargement échoue, elle affiche la dernière version embarquée et le signale.</p>
    <p>Elle prolonge la veille Argos déjà présente (<code>veille/veille.py</code>, <code>veille/sources.yml</code>, workflows ve1 et ve2) au lieu de la remplacer.</p>
  </footer>
  <script>{js}</script>
</body>
</html>
"""


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sources", default="veille/sources.yml")
    ap.add_argument("--etat", default="veille/pages/empreintes.json")
    ap.add_argument("--sortie-html", default="veille/pages/index.html")
    ap.add_argument("--sortie-json", default="veille/pages/donnees.json")
    args = ap.parse_args(argv)

    sources = argos.charger_sources(args.sources)
    etat_path = Path(args.etat)
    etat = json.loads(etat_path.read_text(encoding="utf-8")) if etat_path.exists() else {"empreintes": {}, "dates": {}, "lignes": {}}
    etat.setdefault("empreintes", {})
    etat.setdefault("dates", {})
    etat.setdefault("lignes", {})
    semer_lignes_argos(etat)
    now = maintenant()
    donnees, rapport = collecter(sources, etat, now)

    # Met à jour les empreintes et les titres (seulement les sources accessibles).
    for groupe in ("examen", "sante", "societes", "autres"):
        for src in donnees[groupe]:
            if src.get("empreinte") and src.get("url"):
                etat["empreintes"][src["url"]] = src["empreinte"]
                etat["empreintes"][src["id"]] = src["empreinte"]
                if src.get("date_detection"):
                    etat["dates"][src["url"]] = src["date_detection"]
                    etat["dates"][src["id"]] = src["date_detection"]
            lignes_src = src.pop("_lignes", None)
            if lignes_src and src.get("url"):
                etat["lignes"][src["url"]] = lignes_src
                etat["lignes"][src["id"]] = lignes_src
    etat.pop("_cache_resumes", None)
    etat["derniere_execution"] = donnees["collectee_lisible"]

    html_path = Path(args.sortie_html)
    json_path = Path(args.sortie_json)
    html_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    etat_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(donnees, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    html_path.write_text(rendre_html(donnees), encoding="utf-8")
    etat_path.write_text(json.dumps(etat, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("\n".join(rapport))
    print(f"Écrit : {html_path}")
    print(f"Écrit : {json_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
