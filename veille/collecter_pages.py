#!/usr/bin/env python3
"""Collecte extractive pour la page de veille INTERNAT.

Aucun modèle de langage, aucune API payante. Pour chaque source : titre, date,
lien, et 1 à 2 phrases reprises de la source. Les échecs (HTTP ≠ 200, TLS,
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
        entree["items"] = [serialiser_item(it) for it in items[:12]]
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

    def liste_items(items, vide):
        if not items:
            return f'<p class="vide">{esc(vide)}</p>'
        lis = []
        for it in items:
            date = f'<time datetime="{esc(it.get("date") or "")}">{esc(it.get("date_lisible") or "")}</time>' if it.get("date_lisible") or it.get("date") else ""
            extrait = f'<p class="extrait">{esc(it.get("extrait"))}</p>' if it.get("extrait") else ""
            titre = it.get("titre") or "(sans titre)"
            href = it.get("lien") or "#"
            lis.append(
                f'<li><a href="{esc(href)}">{esc(titre)}</a> {date}{extrait}</li>'
            )
        return "<ul class='items'>" + "".join(lis) + "</ul>"

    def bloc_source(src, avec_items=True):
        motif = f'<p class="motif">{esc(src.get("motif"))}</p>' if src.get("motif") and not src["accessible"] else ""
        det = ""
        if src.get("date_detection"):
            d = src["date_detection"]
            try:
                dt_obj = dt.datetime.fromisoformat(d)
                det = f'<p class="meta">Dernière détection : {esc(lisible(dt_obj))} · empreinte {esc((src.get("empreinte") or "")[:12]) or "—"}.</p>'
            except ValueError:
                det = f'<p class="meta">Dernière détection : {esc(d)}.</p>'
        items = liste_items(src.get("items") or [], "Aucun extrait daté n'a été repris sur cette page.") if avec_items else ""
        return f"""
        <article class="source {'ok' if src['accessible'] else 'ko'}" id="{esc(src['id'])}">
          <header>
            <h3>{esc(src['nom'])}</h3>
            {badge(src)}
          </header>
          <p class="url"><a href="{esc(src['url'])}">{esc(src['url'])}</a>
             {f'· HTTP {esc(src["http"])}' if src.get('http') else ''}</p>
          {motif}{det}{items}
        </article>"""

    # Santé : liste plate des 7 jours, dépliable
    items_sante = []
    for src in donnees.get("sante") or []:
        for it in src.get("items") or []:
            items_sante.append((src, it))
    # déjà filtrés sur 7 jours
    def key_date(pair):
        d = pair[1].get("date") or ""
        return d
    items_sante.sort(key=key_date, reverse=True)

    lis_sante = []
    for src, it in items_sante:
        date = it.get("date_lisible") or it.get("date") or ""
        extrait = f'<p class="extrait">{esc(it.get("extrait"))}</p>' if it.get("extrait") else ""
        lis_sante.append(
            f'<li><time>{esc(date)}</time> '
            f'<span class="src">{esc(src["nom"])}</span> '
            f'<a href="{esc(it.get("lien") or src["url"])}">{esc(it.get("titre"))}</a>'
            f'{extrait}</li>'
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
  padding:1rem; margin:0 0 1rem; box-shadow:0 1px 2px rgba(16,24,40,.05); }
.source header { display:flex; justify-content:space-between; gap:.6rem; align-items:start; }
.source h3 { margin:0; font-size:1.05rem; }
.source .url { font-size:.85rem; word-break:break-all; margin:.3rem 0; }
.source .url a, .items a, .defilable a { color:var(--calme); }
.badge { font-size:.75rem; font-weight:650; text-transform:uppercase; letter-spacing:.04em;
  padding:.15rem .5rem; border-radius:999px; white-space:nowrap; }
.badge-ok { background:var(--bon-fond); color:var(--bon); }
.badge-change { background:var(--attention-fond); color:var(--attention); }
.badge-off { background:var(--urgence-fond); color:var(--urgence); }
.motif { color:var(--urgence); }
.meta, .vide, .extrait { color:var(--encre-3); }
.extrait { margin:.25rem 0 0; font-size:.95rem; color:var(--encre-2); }
.items, .defilable { margin:.4rem 0 0; padding-left:1.15rem; }
.items li, .defilable li { margin:.45rem 0; }
.defilable-wrap { background:var(--papier); border:1px solid var(--trait); border-radius:14px; padding:1rem; }
.defilable { max-height:28rem; overflow:auto; padding-right:.5rem; }
.defilable.replie { max-height:0; overflow:hidden; margin:0; padding:0; }
.defilable time, .src { display:inline-block; margin-right:.4rem; color:var(--encre-3); font-size:.9rem; }
.btn-defile { font:inherit; font-weight:650; background:var(--calme); color:#fff; border:0;
  border-radius:10px; padding:.5rem .9rem; cursor:pointer; margin:0 0 .8rem; }
h2 { font-size:1.15rem; margin:1.4rem 0 .6rem; }
footer.pied { padding:0 1.25rem 2.5rem; color:var(--encre-3); font-size:.9rem; }
footer.pied a { color:var(--calme); }
@media (prefers-reduced-motion: reduce) { * { animation:none !important; transition:none !important; } }
"""
    js = """
(function(){
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
  const btn=document.getElementById('btn-defile');
  const liste=document.getElementById('liste-sante');
  if(btn && liste){
    btn.addEventListener('click',()=>{
      const replie=liste.classList.toggle('replie');
      btn.setAttribute('aria-expanded', String(!replie));
      btn.textContent=replie ? 'Déplier la liste des 7 derniers jours' : 'Replier la liste';
    });
  }
})();
"""
    return f"""<!doctype html>
<html lang="fr-CH">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Veille · Internat — examen fédéral, santé publique, sociétés savantes</title>
  <meta name="description" content="Veille gratuite, hébergée sur GitHub : pages officielles de l'examen fédéral, actualités de santé publique suisse des 7 derniers jours, et extraits par société savante.">
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
    <p class="accroche">Surveille les pages officielles de l'examen fédéral, parcours les actualités de santé publique suisse des sept derniers jours, et lis un extrait par société savante. Chaque ligne reprend un titre, une date, un lien et une ou deux phrases de la source. Rien n'est inventé, aucun abonnement n'est demandé.</p>
    <p class="meta-collecte">Collecte du {esc(donnees.get('collectee_lisible'))}. {n_act} source{'' if n_act==1 else 's'} active{'' if n_act==1 else 's'} sur {n_tot}. Fenêtre des actualités : du {esc(fen.get('debut'))} au {esc(fen.get('fin'))}.</p>
    <ul class="onglets" role="tablist">
      <li><button type="button" role="tab" data-cible="panneau-examen" aria-selected="true">0. Examen fédéral</button></li>
      <li><button type="button" role="tab" data-cible="panneau-sante" aria-selected="false">1. Santé publique suisse</button></li>
      <li><button type="button" role="tab" data-cible="panneau-societes" aria-selected="false">2. Sociétés savantes</button></li>
    </ul>
  </header>
  <main>
    <section class="panneau actif" id="panneau-examen" role="tabpanel">
      <h2>Pages officielles de l'examen</h2>
      <p>Ce panneau signale toute modification d'une page officielle (OFSP, MEBEKO, IML Berne, portail d'inscription). L'empreinte porte sur les titres et les liens de la zone principale, comme la veille Argos déjà en place.</p>
      {examen_html}
    </section>
    <section class="panneau" id="panneau-sante" role="tabpanel">
      <h2>Actualités des 7 derniers jours</h2>
      <p>La liste reprend les communications officiellement datées de l'OFSP (Bulletin) et de Swissmedic, dans la fenêtre indiquée ci-dessus. Clique le bouton pour la déplier ou la replier.</p>
      <div class="defilable-wrap">
        <button type="button" class="btn-defile" id="btn-defile" aria-expanded="true" aria-controls="liste-sante">Replier la liste</button>
        <p class="meta-collecte">{n_sante} actualité{'' if n_sante==1 else 's'} dans les 7 derniers jours.</p>
        {liste_sante}
      </div>
      <h2>Sources de ce panneau</h2>
      {sources_sante}
    </section>
    <section class="panneau" id="panneau-societes" role="tabpanel">
      <h2>Par société savante</h2>
      <p>Chaque bloc reprend des titres, dates et extraits lus le jour de la collecte. Une société dont le site refuse la lecture (protection, certificat, erreur HTTP) reste visible et porte la mention « source non accessible ».</p>
      {societes_html}
      <h2>Autres veilles utiles</h2>
      <p>Sommaires de la Revue Médicale Suisse et du Swiss Medical Weekly, et page d'actualité de Swissmedic, lorsque ces pages répondent.</p>
      {autres_html}
    </section>
  </main>
  <footer class="pied">
    <p>Cette veille ne coûte rien : un workflow GitHub Actions, public, tourne une fois par jour, sans API payante et sans modèle de langage. Les données s'écrivent sur la branche <code>veille-etat</code>, pas sur <code>main</code>.</p>
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
    etat = json.loads(etat_path.read_text(encoding="utf-8")) if etat_path.exists() else {"empreintes": {}, "dates": {}}
    now = maintenant()
    donnees, rapport = collecter(sources, etat, now)

    # Met à jour les empreintes (seulement les sources accessibles).
    etat.setdefault("empreintes", {})
    etat.setdefault("dates", {})
    for groupe in ("examen", "sante", "societes", "autres"):
        for src in donnees[groupe]:
            if src.get("empreinte") and src.get("url"):
                etat["empreintes"][src["url"]] = src["empreinte"]
                etat["empreintes"][src["id"]] = src["empreinte"]
                if src.get("date_detection"):
                    etat["dates"][src["url"]] = src["date_detection"]
                    etat["dates"][src["id"]] = src["date_detection"]
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
