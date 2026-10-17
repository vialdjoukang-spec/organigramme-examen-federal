#!/usr/bin/env python3
"""Veille Argos : compare une empreinte normalisée (titres, liens, dates) à l'état précédent.

Le script ne copie aucun texte protégé : il ne garde que des titres, des liens et des dates.
Il ouvre un ticket « Veille » seulement si l'empreinte change, et un ticket d'échec après
deux exécutions manquées consécutives ; un échec réseau ne produit jamais un faux changement.
Usage : veille.py --id ve1 --sources veille/sources.yml --etat veille/etat.json [--dry-run]
"""
import argparse, datetime as dt, hashlib, json, os, re, subprocess, sys, urllib.parse, urllib.request, urllib.robotparser
from html.parser import HTMLParser
from zoneinfo import ZoneInfo

UA = "argos-veille/1.0 (+https://github.com/vialdjoukang-spec/organigramme-examen-federal)"
TZ = ZoneInfo("Europe/Zurich")
DATE_RE = re.compile(r"\b\d{1,2}\.\s?\d{1,2}\.\s?\d{4}\b|\b\d{1,2}\s+(?:janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)\s+\d{4}\b", re.I)


def charger_sources(chemin):
    """Lit le YAML simple de veille/sources.yml sans dépendance externe."""
    import ast
    data, cur, liste = {}, None, None
    for brut in open(chemin, encoding="utf-8"):
        ligne = brut.split(" #")[0].rstrip() if not brut.lstrip().startswith("- ") else brut.rstrip()
        if not ligne.strip() or ligne.lstrip().startswith("#"):
            continue
        if not ligne.startswith(" "):
            cur = data.setdefault(ligne.rstrip(":"), {}); liste = None
        elif ligne.lstrip().startswith("- "):
            cur[liste].append(ligne.strip()[2:].strip())
        else:
            k, _, v = ligne.strip().partition(":"); v = v.strip()
            if not v:
                cur[k] = []; liste = k
            else:
                try: cur[k] = ast.literal_eval(v)
                except Exception: cur[k] = v.strip('"')
    return data


def robots_ok(url):
    p = urllib.parse.urlsplit(url)
    rp = urllib.robotparser.RobotFileParser()
    try:
        req = urllib.request.Request(f"{p.scheme}://{p.netloc}/robots.txt", headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=20) as r:
            txt = r.read().decode("utf-8", "replace")
    except Exception:
        return True  # robots.txt absent : aucune règle n'interdit l'accès
    if "<html" in txt[:500].lower():
        return True  # une application renvoie sa page au lieu d'un robots.txt
    rp.parse(txt.splitlines())
    return rp.can_fetch(UA, url)


class Main(HTMLParser):
    """Garde les titres h1–h4 et les liens de la zone <main> (ou du corps si <main> manque)."""
    def __init__(self, base):
        super().__init__(); self.base = base; self.in_main = 0; self.has_main = False
        self.tag = None; self.href = None; self.buf = []; self.items = []
    def handle_starttag(self, t, a):
        a = dict(a)
        if t == "main": self.in_main += 1; self.has_main = True
        if t in ("h1", "h2", "h3", "h4") or (t == "a" and a.get("href")):
            self.tag = t; self.buf = []; self.href = a.get("href"); self.zone = self.in_main > 0
    def handle_endtag(self, t):
        if t == "main": self.in_main -= 1
        if self.tag == t:
            txt = " ".join("".join(self.buf).split())
            if t == "a":
                href = urllib.parse.urljoin(self.base, self.href).split("#")[0]
                if not href.startswith(("mailto:", "javascript:")):
                    self.items.append((self.zone, f"lien | {txt} | {href}"))
            elif txt:
                self.items.append((self.zone, f"titre | {txt}"))
            self.tag = None
    def handle_data(self, d):
        if self.tag: self.buf.append(d)


def lire_html(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "fr-CH,fr"})
    with urllib.request.urlopen(req, timeout=60) as r:
        html = r.read().decode("utf-8", "replace")
    p = Main(url); p.feed(html)
    lignes = [s for z, s in p.items if z or not p.has_main]
    return sorted(set(lignes))


def lire_playwright(url):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(user_agent=UA, locale="fr-CH")
        pg.goto(url, wait_until="networkidle", timeout=90000)
        pg.wait_for_timeout(3000)
        texte = pg.inner_text("body")
        titres = pg.eval_on_selector_all("h1,h2,h3", "els => els.map(e => e.innerText.trim()).filter(Boolean)")
        b.close()
    dates = sorted(set(" ".join(d.split()) for d in DATE_RE.findall(texte)))
    if not dates and not titres:
        raise RuntimeError("Le rendu ne contient ni titre ni date : le sélecteur est probablement cassé.")
    return [f"date | {d}" for d in dates] + [f"titre | {t}" for t in sorted(set(titres))]


def gh(*args, inp=None):
    return subprocess.run(["gh", *args], input=inp, text=True, capture_output=True, check=True).stdout


def ouvrir_ticket(titre, corps, labels, dry):
    if dry:
        print(f"[dry-run] ticket : {titre}\n{corps}"); return
    gh("issue", "create", "--title", titre, "--body-file", "-", *sum((["--label", l] for l in labels), []), inp=corps)


def doit_tourner(src, maintenant, evenement):
    if evenement != "schedule":
        return True
    if maintenant.weekday() == int(src.get("hebdo_jour", 0)):
        return True
    q = src.get("quotidien")
    if q:
        md = maintenant.strftime("%m-%d"); debut, fin = q
        return md >= debut or md <= fin if debut > fin else debut <= md <= fin
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True); ap.add_argument("--sources", required=True)
    ap.add_argument("--etat", required=True); ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    src = charger_sources(a.sources)[a.id]
    now = dt.datetime.now(TZ); stamp = now.strftime("%d.%m.%Y %H:%M")
    if not doit_tourner(src, now, os.environ.get("GITHUB_EVENT_NAME", "manual")):
        print(f"{a.id} : aucune exécution prévue ce jour ({stamp}, Europe/Zurich)."); return 0
    etat = json.load(open(a.etat, encoding="utf-8")) if os.path.exists(a.etat) else {}
    e = etat.setdefault(a.id, {"empreintes": {}, "lignes": {}, "echecs": 0})
    lecteur = lire_playwright if src["methode"] == "playwright" else lire_html
    rapport, erreurs, changements = [], [], []
    for url in src["urls"]:
        try:
            if not robots_ok(url):
                raise PermissionError("robots.txt interdit cette page ; la veille ne la lit pas.")
            lignes = lecteur(url)
        except Exception as exc:
            erreurs.append(f"{url} : {type(exc).__name__} : {exc}"); continue
        emp = hashlib.sha256("\n".join(lignes).encode()).hexdigest()
        avant = e["lignes"].get(url)
        if avant is None:
            rapport.append(f"{url} : état initial enregistré ({len(lignes)} éléments, empreinte {emp[:12]}).")
        elif emp != e["empreintes"].get(url):
            ajout = [l for l in lignes if l not in set(avant)]; retrait = [l for l in avant if l not in set(lignes)]
            changements.append((url, ajout, retrait))
            rapport.append(f"{url} : changement détecté (+{len(ajout)} / −{len(retrait)}).")
        else:
            rapport.append(f"{url} : inchangé.")
        e["empreintes"][url] = emp; e["lignes"][url] = lignes
    e["derniere_execution"] = stamp
    if erreurs:
        e["echecs"] = e.get("echecs", 0) + 1
        rapport += [f"ÉCHEC {x}" for x in erreurs]
        if e["echecs"] == 2:
            ouvrir_ticket(f"[Veille] {src['nom']} : échec de lecture deux fois de suite",
                          "La veille a échoué lors de deux exécutions consécutives ; aucun changement n'est déduit d'un échec.\n\n"
                          + "\n".join(f"- {x}" for x in erreurs) + f"\n\nDate de détection : {stamp} (Europe/Zurich).",
                          ["agent:argos", src["categorie"], "prio:P0"], a.dry_run)
    else:
        e["echecs"] = 0
    for url, ajout, retrait in changements:
        pdf2027 = [l for l in ajout if ".pdf" in l.lower() and "2027" in l]
        extrait = "\n".join([f"+ {l}" for l in ajout[:15]] + [f"− {l}" for l in retrait[:15]])
        corps = (f"### Source\n{src['nom']} · {url}\n\n### Catégorie\n{src['categorie']}\n\n"
                 f"### Date de détection\n{stamp}\n\n### Extrait du changement\n```\n{extrait}\n```\n"
                 + (f"\nUn nouveau PDF portant « 2027 » est apparu ({len(pdf2027)}).\n" if pdf2027 else "")
                 + f"\n### Destinataire\n{src['destinataire']}\n")
        ouvrir_ticket(f"[Veille] {src['nom']} a changé" + (" · nouveau PDF 2027" if pdf2027 else ""),
                      corps, ["agent:argos", src["categorie"], "prio:P0"], a.dry_run)
    json.dump(etat, open(a.etat, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    print("\n".join(rapport))
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as s:
            s.write(f"## Veille {a.id} · {stamp} (Europe/Zurich)\n\n" + "\n".join(f"- {r}" for r in rapport) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
