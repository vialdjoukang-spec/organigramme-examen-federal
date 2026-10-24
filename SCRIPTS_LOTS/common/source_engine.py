#!/usr/bin/env python3
"""SCRIPT SOURCE — recherche rapide et classée dans les sites médicaux agréés (5 niveaux), sans aucune IA.

Commandes :
  domaines                        liste blanche validée (niveaux, statut)
  crawl   [--niveaux 1,2] [--domaines d1,d2] [--seed URL] [--max-pages 60] [--profondeur 2] [--budget 90]
  search  "requête" [--niveau-max 5] [--pec] [--limite 10] [--format json|md]
  extrait URL [--requete "..."] [--max-car 1200]
  pubmed  "requête" [--max 5]      MCP local 127.0.0.1:3010 s'il répond, sinon E-utilities NCBI
  check   FICHIER.html [--format json|md]   code 1 si une affirmation n'a pas de source (dépôt bloqué)
Principe : sources suisses d'abord ; priorité aux pages de prise en charge ; rien sans source (V7-Tunder §4)."""
import threading, argparse, heapq, json, os, re, sqlite3, subprocess, sys, time, unicodedata
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, urldefrag, quote
sys.path.insert(0, str(Path(__file__).resolve().parent))
import config as cfgmod
from netutil import Client, ErreurSource, ListeBlanche, maintenant_iso
from token_bucket import SeauPartage
import lot_readonly

NIVEAUX = {1: "Suisse officielle", 2: "Société savante ou institution suisse", 3: "Recommandation européenne",
           4: "International (jamais seule pour une conduite, V7-Tunder §4.2)", 5: "Littérature (PubMed)"}
MOTS_PEC = ["prise en charge", "traitement", "thérapie", "therapie", "posologie", "dosage", "recommandation",
            "recommandations", "directive", "guideline", "guidelines", "empfehlung", "empfehlungen", "behandlung",
            "management", "treatment", "terapia", "trattamento", "urgence", "notfall", "algorithme", "algorithmus",
            "grossesse", "schwangerschaft", "enfant", "kinder", "insuffisance rénale", "niereninsuffizienz", "sortie",
            "vaccination", "impfung", "impfplan", "antibiotique", "antibiotika"]
SAUT_EXT = re.compile(r"\.(jpg|jpeg|png|gif|svg|webp|zip|docx?|xlsx?|pptx?|mp4|mp3|ics|css|js)(\?|$)", re.I)

def score_pec(texte):
    t = texte.lower()
    return sum(t.count(m) for m in MOTS_PEC)

# ---------- extraction de texte (HTML et PDF) ----------
class _Extracteur(HTMLParser):
    IGNORE = {"script", "style", "nav", "footer", "header", "noscript", "svg", "form"}
    BLOCS = {"p", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6", "div", "section", "article", "br", "dd", "dt", "td", "th"}
    def __init__(self, base):
        super().__init__(convert_charrefs=True); self.base = base; self.ign = 0; self.parts = []; self.titre = ""; self.dans_titre = False; self.liens = []
    def handle_starttag(self, t, a):
        if t in self.IGNORE: self.ign += 1
        if t == "title": self.dans_titre = True
        if t == "a":
            href = dict(a).get("href")
            if href: self.liens.append(urldefrag(urljoin(self.base, href))[0])
        if t in self.BLOCS: self.parts.append("\n")
    def handle_endtag(self, t):
        if t in self.IGNORE and self.ign: self.ign -= 1
        if t == "title": self.dans_titre = False
        if t in self.BLOCS: self.parts.append("\n")
    def handle_data(self, d):
        if self.dans_titre: self.titre += d
        elif not self.ign: self.parts.append(d)

def extraire(reponse):
    typ = (reponse.get("type") or "").lower(); corps = reponse["corps"]; url = reponse.get("finale") or reponse["url"]
    if "pdf" in typ or url.lower().endswith(".pdf"):
        try:
            txt = subprocess.run(["pdftotext", "-layout", "-", "-"], input=corps, capture_output=True, timeout=60).stdout.decode("utf-8", "replace")
        except Exception:
            txt = ""
        return {"titre": Path(urlparse(url).path).name, "texte": _norm(txt), "liens": []}
    if "html" not in typ and not corps[:200].lstrip().lower().startswith((b"<!doctype", b"<html")):
        return {"titre": "", "texte": _norm(corps.decode("utf-8", "replace")), "liens": []}
    p = _Extracteur(url); p.feed(corps.decode("utf-8", "replace"))
    return {"titre": re.sub(r"\s+", " ", p.titre).strip(), "texte": _norm("".join(p.parts)), "liens": p.liens}

def _norm(t):
    t = re.sub(r"[ \t\u00a0]+", " ", t); t = re.sub(r"\n\s*\n+", "\n", t)
    return t.strip()

# ---------- index local FTS5 ----------
class Index:
    def __init__(self, cache_dir):
        Path(cache_dir).mkdir(parents=True, exist_ok=True)
        self.c = sqlite3.connect(str(Path(cache_dir) / "index.sqlite"), timeout=30, check_same_thread=False)
        self.verrou = threading.Lock(); self.c.execute("pragma journal_mode=wal")
        self.c.execute("create virtual table if not exists pages using fts5(url unindexed, domaine unindexed, niveau unindexed, titre, texte, pec unindexed, consulte_le unindexed, tokenize='unicode61 remove_diacritics 2')")
        self.c.execute("create table if not exists vues(url text primary key, t real)")
    def ajouter(self, url, domaine, niveau, titre, texte, consulte_le):
        with self.verrou:
            self.c.execute("delete from pages where url=?", (url,))
            self.c.execute("insert into pages values(?,?,?,?,?,?,?)", (url, domaine, niveau, titre, texte, score_pec(titre + " " + texte[:20000]), consulte_le))
            self.c.execute("insert or replace into vues values(?,?)", (url, time.time())); self.c.commit()
    def vu(self, url, ttl):
        with self.verrou:
            r = self.c.execute("select t from vues where url=?", (url,)).fetchone()
        return bool(r and time.time() - r[0] < ttl)
    def chercher(self, requete, niveau_max=5, pec=False, limite=10):
        termes = [t for t in re.findall(r"\w+", unicodedata.normalize("NFC", requete.lower())) if len(t) > 1]
        if not termes:
            return []
        res = []
        for op in (" AND ", " OR "):
            q = op.join(f'"{t}"' for t in termes)
            res = self.c.execute(
                "select url, domaine, niveau, titre, snippet(pages, 4, '«', '»', ' … ', 28), bm25(pages, 0, 0, 0, 3.0, 1.0), pec, consulte_le "
                "from pages where pages match ? and niveau <= ? order by bm25(pages, 0, 0, 0, 3.0, 1.0) limit 200", (q, niveau_max)).fetchall()
            if res:
                break
        lignes = []
        for url, dom, niv, titre, ext, bm, p, date in res:
            bonus = min(int(p), 10) ** 0.5            # priorité « prise en charge » : multiplicative ET additive (robuste aux petits corpus)
            pertinence = -bm * (1 + (0.5 if pec else 0.15) * bonus) + (1.0 if pec else 0.1) * bonus
            if pec and int(p) == 0:
                pertinence *= 0.5
            lignes.append({"niveau": int(niv), "categorie": NIVEAUX[int(niv)], "titre": titre, "url": url, "domaine": dom,
                           "extrait": ext, "consulte_le": date, "pec": int(p), "pertinence": round(pertinence, 3)})
        lignes.sort(key=lambda r: (r["niveau"], -r["pertinence"]))
        return lignes[:limite]

# ---------- moteur ----------
class Moteur:
    def __init__(self, cfg):
        self.cfg = cfg; self.lb = ListeBlanche(); self.client = Client(cfg, self.lb); self.index = Index(cfg["cache_dir"])

    def sitemap(self, hote, limite=400):
        urls, a_voir = [], [f"https://{hote}/sitemap.xml"]
        try:
            r = self.client.get(f"https://{hote}/robots.txt", ttl=86400, attente_max=10)
            a_voir = re.findall(r"(?im)^sitemap:\s*(\S+)", r["corps"].decode("utf-8", "replace")) or a_voir
        except ErreurSource:
            pass
        vus = 0
        while a_voir and vus < 4 and len(urls) < limite:
            sm = a_voir.pop(0); vus += 1
            try:
                corps = self.client.get(sm, ttl=86400, attente_max=10)["corps"]
            except ErreurSource:
                continue
            if sm.endswith(".gz") or corps[:2] == b"\x1f\x8b":
                import gzip; corps = gzip.decompress(corps)
            locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", corps.decode("utf-8", "replace"))
            if "<sitemapindex" in corps[:500].decode("utf-8", "replace"):
                a_voir.extend(sorted(locs, key=lambda u: -score_pec(u))[:3])
            else:
                urls.extend(locs)
        return urls[:limite]

    def crawl(self, domaines, seeds=(), max_pages=60, profondeur=2, budget=90, journal=None):
        t0 = time.monotonic(); file = []; compteur = 0; deja = set(); indexees = []
        def pousser(url, prof, bonus=0):
            url = urldefrag(url)[0]
            if url in deja or SAUT_EXT.search(url):
                return
            d = self.lb.info(urlparse(url).hostname)
            if not d or not d.get("auto_fetch") or d["domaine"] not in autorises:
                return
            deja.add(url); heapq.heappush(file, (d["niveau"], -(score_pec(url) + bonus), prof, url))
        autorises = set()
        for dom in domaines:
            d = self.lb.info(dom)
            if d and d.get("auto_fetch"):
                autorises.add(d["domaine"])
        for s in seeds:
            d = self.lb.info(urlparse(s).hostname)
            if d: autorises.add(d["domaine"]); pousser(s, 0, 5)
        for dom in sorted(autorises):
            pousser(f"https://{dom}/", 0)
            for u in self.sitemap(dom):
                pousser(u, 1)
        erreurs = []
        with ThreadPoolExecutor(self.cfg["http"]["max_workers"]) as ex:
            while file and compteur < max_pages and time.monotonic() - t0 < budget:
                # vague équitable : chaque hôte en attente reçoit sa part des travailleurs (le débit par domaine reste borné par le seau partagé)
                n_max = min(self.cfg["http"]["max_workers"], max_pages - compteur)
                en_attente = {urlparse(x[3]).hostname for x in file}
                part = max(1, n_max // max(1, len(en_attente)))
                lot, par_hote, reste = [], {}, []
                while file and len(lot) < n_max:
                    it = heapq.heappop(file); h = urlparse(it[3]).hostname
                    if par_hote.get(h, 0) >= part:
                        reste.append(it); continue
                    par_hote[h] = par_hote.get(h, 0) + 1; lot.append(it)
                for it in reste: heapq.heappush(file, it)
                futs = {ex.submit(self._traiter, it, max(1, int(budget - (time.monotonic() - t0)))): it for it in lot}
                for f in as_completed(futs):
                    niv, _, prof, url = futs[f]
                    try:
                        page = f.result()
                    except ErreurSource as e:
                        erreurs.append({"url": url, "code": e.code}); continue
                    compteur += 1; indexees.append(url)
                    if journal: journal(f"[{compteur}] N{niv} {url}")
                    if prof < profondeur:
                        for l in page["liens"]:
                            pousser(l, prof + 1)
        return {"pages_indexees": compteur, "duree_s": round(time.monotonic() - t0, 2), "erreurs": erreurs[:20], "file_restante": len(file), "urls": indexees}

    def _traiter(self, it, attente):
        niv, _, prof, url = it
        r = self.client.get(url, attente_max=min(attente, 30))
        if r["statut"] not in (200, 203):
            raise ErreurSource("NON_TROUVE", f"HTTP {r['statut']}", url)
        page = extraire(r)
        if page["texte"]:
            self.index.ajouter(url, urlparse(url).hostname, niv, page["titre"], page["texte"],
                               time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(r.get("t") or time.time())))
        return page

    def extrait(self, url, requete="", max_car=1200):
        r = self.client.get(url); page = extraire(r)
        phrases = re.split(r"(?<=[.!?:;])\s+|\n", page["texte"])
        termes = [t for t in re.findall(r"\w+", requete.lower()) if len(t) > 2]
        if termes:
            notes = [(sum(p.lower().count(t) for t in termes), i) for i, p in enumerate(phrases)]
            choisis = set()
            for n, i in sorted(notes, reverse=True):
                if n == 0: break
                for j in (i - 1, i, i + 1):
                    if 0 <= j < len(phrases): choisis.add(j)
                if sum(len(phrases[k]) for k in choisis) > max_car: break
            morceaux = [phrases[i] for i in sorted(choisis)] or phrases
        else:
            morceaux = phrases
        txt, tronque = "", False
        for m in morceaux:
            if len(txt) + len(m) + 1 > max_car:
                tronque = True; break
            txt += m + " "
        niv = r["niveau"]
        return {"statut": "ok" if txt.strip() else "non_trouve", "niveau": niv, "categorie": NIVEAUX[niv], "titre": page["titre"],
                "url": url, "consulte_le": maintenant_iso(), "extrait": txt.strip(), "tronque": tronque, "cache": r["cache"],
                "jetons_estimes": len(txt) // 4,
                "ligne_evidence": {"url": url, "document": page["titre"], "extrait": txt.strip()[:300], "lu_le": maintenant_iso()[:10]}}

    def pubmed(self, requete, maxi=5):
        try:
            return self._pubmed_mcp(requete, maxi)
        except Exception as e:
            raison = f"MCP local indisponible ({type(e).__name__}) : repli sur E-utilities"
        res = self._pubmed_eutils(requete, maxi); res["voie"] = "eutils"; res["note"] = raison
        return res

    def _pubmed_mcp(self, requete, maxi):
        url = self.cfg["pubmed"]["mcp_url"]
        corps = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                            "params": {"name": "pubmed_search_articles", "arguments": {"query": requete, "maxResults": maxi, "summaryCount": maxi}}}).encode()
        import urllib.request
        req = urllib.request.Request(url, data=corps, headers={"Content-Type": "application/json", "Accept": "application/json, text/event-stream"})
        with urllib.request.urlopen(req, timeout=5) as r:
            brut = r.read().decode("utf-8", "replace")
        if brut.lstrip().startswith("event:") or "data:" in brut[:50]:
            brut = "\n".join(l[5:] for l in brut.splitlines() if l.startswith("data:"))
        doc = json.loads(brut)
        if "error" in doc:
            raise RuntimeError(doc["error"])
        texte = "".join(c.get("text", "") for c in doc.get("result", {}).get("content", []))
        return {"statut": "ok", "voie": "mcp_local", "niveau": 5, "categorie": NIVEAUX[5], "consulte_le": maintenant_iso(),
                "resultats_bruts": texte[:6000], "jetons_estimes": min(len(texte), 6000) // 4}

    def _pubmed_eutils(self, requete, maxi):
        cle = os.environ.get("NCBI_API_KEY")
        debit = self.cfg["pubmed"]["rate_per_s_with_key" if cle else "rate_per_s_without_key"]
        seau = SeauPartage(Path(self.cfg["shared_state_dir"]) / "ncbi", "eutils", debit, debit)
        base = self.cfg["pubmed"]["eutils_base"]; sec = f"api_key={quote(cle)}" if cle else None
        def appel(u):
            if not seau.prendre(attente_max=20):
                raise ErreurSource("LIMITE_DEBIT", "budget NCBI épuisé", u)
            return json.loads(self.client.get(u, ttl=604800, params_secrets=sec, accept="application/json", api=True)["corps"])
        q = quote(requete) + "&tool=scripts_lots" + (f"&email={quote(os.environ['NCBI_ADMIN_EMAIL'])}" if os.environ.get("NCBI_ADMIN_EMAIL") else "")
        ids = appel(f"{base}/esearch.fcgi?db=pubmed&retmode=json&sort=relevance&retmax={maxi}&term={q}")["esearchresult"].get("idlist", [])
        res = []
        if ids:
            s = appel(f"{base}/esummary.fcgi?db=pubmed&retmode=json&id={','.join(ids)}")["result"]
            for i in ids:
                d = s.get(i, {})
                res.append({"pmid": i, "titre": d.get("title"), "revue": d.get("fulljournalname"), "date": d.get("pubdate"),
                            "url": f"https://pubmed.ncbi.nlm.nih.gov/{i}/"})
        return {"statut": "ok" if res else "non_trouve", "niveau": 5, "categorie": NIVEAUX[5], "consulte_le": maintenant_iso(),
                "debit_ncbi_req_s": debit, "resultats": res, "jetons_estimes": len(json.dumps(res, ensure_ascii=False)) // 4}

# ---------- check : rien sans source ----------
RE_REF = re.compile(r"\[S(\d+)(?:\s*[,–-]\s*S?(\d+))*\]")
RE_CHIFFRE = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)?\s?(?:%|‰|mg|µg|mcg|ng|g|kg|ml|mL|dl|dL|l|L|mmol|µmol|mol|mmHg|kPa|UI|U|mEq|h|heures?|j|jours?|semaines?|mois|ans|min|s|°C|/min|bpm|cm|mm|m²|kcal)(?![\w])"
                       r"|[<>≤≥]\s?\d|\b\d+\s?(?:fois|patients|cas)\b|\bart\.\s?\d+|\bRS\s?\d{3}", re.I)
RE_NORME = re.compile(r"\b(recommand\w*|indiqu\w*|contre-indiqu\w*|posologie|dose\w*|seuil\w*|première intention|gold standard|"
                      r"critères? diagnostiques?|incidence|prévalence|mortalité|sensibilité|spécificité)\b", re.I)

class _Blocs(HTMLParser):
    BLOC = {"p", "li", "tr", "dd", "blockquote", "figcaption", "caption"}
    def __init__(self):
        super().__init__(convert_charrefs=True); self.pile = []; self.blocs = []; self.sources = False; self.point = None
        self.titre_h = None; self.strong = None; self.table_refs = []; self.ligne = 0
    def handle_starttag(self, t, a):
        if t in self.BLOC: self.pile.append({"tag": t, "texte": "", "ligne": self.getpos()[0], "point": self.point, "sources": self.sources})
        if t in ("h1", "h2", "h3", "h4", "summary"): self.titre_h = ""
        if t == "strong": self.strong = ""
        if t == "table": self.table_refs.append({"ref": False, "lignes": []})
    def handle_endtag(self, t):
        if t in ("h1", "h2", "h3", "h4", "summary") and self.titre_h is not None:
            if re.search(r"\bSources\b", self.titre_h): self.sources = True
            self.titre_h = None
        if t == "strong" and self.strong is not None:
            m = re.match(r"\s*(\d{1,2})\s*[.)]", self.strong)
            if m: self.point = int(m.group(1))
            self.strong = None
        if t in self.BLOC and self.pile and self.pile[-1]["tag"] == t:
            b = self.pile.pop()
            if self.table_refs and t in ("tr", "caption"):
                if RE_REF.search(b["texte"]) and (t == "caption" or not self.table_refs[-1]["lignes"]): self.table_refs[-1]["ref"] = True
                if t == "tr": self.table_refs[-1]["lignes"].append(b)
                else: self.blocs.append(b)
            else:
                self.blocs.append(b)
        if t == "table" and self.table_refs:
            tb = self.table_refs.pop()
            for b in tb["lignes"]:
                b["table_ref"] = tb["ref"]; self.blocs.append(b)
    def handle_data(self, d):
        if self.pile and self.pile[-1]["tag"] == "tr": d = " " + d
        if self.titre_h is not None: self.titre_h += d
        if self.strong is not None: self.strong += d
        if self.pile: self.pile[-1]["texte"] += d

def verifier_sources(html, liste=None):
    """Retourne (problèmes, statistiques). Chaque problème cite la section V7-Tunder concernée."""
    lb = liste or ListeBlanche(); p = _Blocs(); p.feed(html)
    corps = [b for b in p.blocs if not b["sources"]]; src = [b for b in p.blocs if b["sources"]]
    defs = {}
    for b in src:
        for m in re.finditer(r"\[S(\d+)\]", b["texte"]):
            defs[int(m.group(1))] = b
    problemes = []; affirmations = 0; cites = set()
    for b in corps:
        t = re.sub(r"\s+", " ", b["texte"]).strip()
        refs = {int(x) for m in RE_REF.finditer(t) for x in re.findall(r"\d+", m.group(0))}
        cites |= refs
        if not (RE_CHIFFRE.search(t) or RE_NORME.search(t)):
            continue
        if re.fullmatch(r"\s*\d{1,2}\s*[.)]\s*[^.!?]{0,120}", t) or b["tag"] == "caption" and not RE_CHIFFRE.search(t):
            continue          # intitulé de point (« 11. Prise en charge … ») : pas une affirmation
        affirmations += 1
        if not refs and not b.get("table_ref"):
            problemes.append({"gravite": "P1", "section": "§4.1", "ligne": b["ligne"], "point": b["point"],
                              "message": "affirmation chiffrée ou normative sans référence [Sn]", "extrait": t[:120]})
        elif b["point"] == 11 and refs:
            niveaux = [lb.niveau(_url(defs.get(r, {}).get("texte", ""))) for r in refs]
            if all((n is None or n >= 4) for n in niveaux):
                problemes.append({"gravite": "P1", "section": "§4.2", "ligne": b["ligne"], "point": 11,
                                  "message": "prise en charge appuyée seulement sur des sources de niveau 4–5 ou hors liste", "extrait": t[:120]})
    for r in sorted(cites - set(defs)):
        problemes.append({"gravite": "P1", "section": "§4.10", "ligne": None, "point": None, "message": f"[S{r}] cité mais absent de la section Sources", "extrait": ""})
    for n, b in sorted(defs.items()):
        t = b["texte"]
        if not re.search(r"https?://", t):
            problemes.append({"gravite": "P1", "section": "§4.10", "ligne": b["ligne"], "point": None, "message": f"[S{n}] sans URL", "extrait": t[:120]})
        if not re.search(r"\d{4}-\d{2}-\d{2}|\d{1,2}\.\d{1,2}\.\d{4}|consult", t, re.I):
            problemes.append({"gravite": "P1", "section": "§4.10", "ligne": b["ligne"], "point": None, "message": f"[S{n}] sans date de consultation", "extrait": t[:120]})
        u = _url(t)
        if u and lb.niveau(u) is None:
            problemes.append({"gravite": "P2", "section": "§4.2", "ligne": b["ligne"], "point": None, "message": f"[S{n}] hors liste blanche : {urlparse(u).hostname}", "extrait": ""})
    stats = {"affirmations_detectees": affirmations, "sources_definies": len(defs), "references_citees": len(cites),
             "bloquants": sum(1 for x in problemes if x["gravite"] == "P1")}
    return problemes, stats

def _url(t):
    m = re.search(r"https?://[^\s<>\"')]+", t or "")
    return m.group(0).rstrip(".,;") if m else ""

def check(cfg, fichier, fmt="md"):
    n = lot_readonly.numero_lot(fichier)
    if n is None or not cfgmod.lot_autorise(cfg, n):
        print(f"REFUS : {fichier} n'appartient pas à la série LOT_{cfg['lot_min']}–{cfg['lot_max']} de l'agent {cfg['agent']}.", file=sys.stderr)
        return 2
    html = lot_readonly.lire_octets(fichier).decode("utf-8", "replace")
    pb, st = verifier_sources(html)
    if fmt == "json":
        print(json.dumps({"fichier": str(fichier), "stats": st, "problemes": pb}, ensure_ascii=False, indent=1))
    else:
        print(f"# Contrôle des sources — {Path(fichier).name}\n\n{st['affirmations_detectees']} affirmations détectées · {st['sources_definies']} sources définies · **{st['bloquants']} bloquant(s)**\n")
        for x in pb[:40]:
            loc = f"ligne {x['ligne']}" if x["ligne"] else ""
            print(f"- {x['gravite']} [{x['section']}] {loc} {('point ' + str(x['point'])) if x['point'] else ''} : {x['message']}" + (f" — « {x['extrait']} »" if x["extrait"] else ""))
        if len(pb) > 40: print(f"- … {len(pb) - 40} autres (voir --format json)")
        print("\nDÉPÔT BLOQUÉ" if st["bloquants"] else "\nDépôt autorisé du point de vue des sources")
    return 1 if st["bloquants"] else 0

# ---------- sortie ----------
def afficher(obj, fmt):
    if fmt == "json":
        print(json.dumps(obj, ensure_ascii=False, indent=1)); return
    if isinstance(obj, list):
        for r in obj:
            print(f"- **N{r['niveau']}** [{r['titre'] or r['url']}]({r['url']}) — {r['extrait']} _(consulté le {r['consulte_le'][:10]}{', PEC' if r['pec'] else ''})_")
        if not obj: print("donnée non trouvée dans les sources consultées")
    else:
        print(json.dumps(obj, ensure_ascii=False, indent=1))

def main(config_path, argv=None):
    cfg = cfgmod.charger(config_path)
    ap = argparse.ArgumentParser(prog=f"script_source (agent {cfg['agent']})", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("domaines")
    c = sp.add_parser("crawl"); c.add_argument("--niveaux", default="1,2"); c.add_argument("--domaines", default="")
    c.add_argument("--seed", action="append", default=[]); c.add_argument("--max-pages", type=int, default=60)
    c.add_argument("--profondeur", type=int, default=2); c.add_argument("--budget", type=float, default=90)
    s = sp.add_parser("search"); s.add_argument("requete"); s.add_argument("--niveau-max", type=int, default=5)
    s.add_argument("--pec", action="store_true"); s.add_argument("--limite", type=int, default=10); s.add_argument("--format", default="md")
    e = sp.add_parser("extrait"); e.add_argument("url"); e.add_argument("--requete", default=""); e.add_argument("--max-car", type=int, default=1200)
    p = sp.add_parser("pubmed"); p.add_argument("requete"); p.add_argument("--max", type=int, default=5)
    k = sp.add_parser("check"); k.add_argument("fichier"); k.add_argument("--format", default="md")
    a = ap.parse_args(argv)
    m = None if a.cmd in ("check", "domaines") else Moteur(cfg)
    try:
        if a.cmd == "domaines":
            lb = ListeBlanche()
            for d in sorted({id(v): v for v in lb.domaines.values()}.values(), key=lambda d: (d["niveau"], d["domaine"])):
                print(f"N{d['niveau']} {d['statut']:<24} {d['domaine']:<28} {d['organisme']}")
            return 0
        if a.cmd == "crawl":
            niv = {int(x) for x in a.niveaux.split(",") if x}
            doms = [x for x in a.domaines.split(",") if x] or [d["domaine"] for d in json.loads((Path(__file__).parent / "allowlist.json").read_text())["domaines"] if d["niveau"] in niv]
            r = m.crawl(doms, a.seed, a.max_pages, a.profondeur, a.budget, journal=lambda x: print(x, file=sys.stderr))
            r.pop("urls"); print(json.dumps(r, ensure_ascii=False, indent=1)); return 0
        if a.cmd == "search":
            t0 = time.perf_counter(); r = m.index.chercher(a.requete, a.niveau_max, a.pec, a.limite)
            afficher(r, a.format); print(f"\n_{len(r)} résultat(s) en {1000*(time.perf_counter()-t0):.1f} ms (index local)_", file=sys.stderr); return 0 if r else 3
        if a.cmd == "extrait":
            afficher(m.extrait(a.url, a.requete, a.max_car), "json"); return 0
        if a.cmd == "pubmed":
            afficher(m.pubmed(a.requete, a.max), "json"); return 0
        if a.cmd == "check":
            return check(cfg, a.fichier, a.format)
    except ErreurSource as e:
        print(json.dumps({"statut": "erreur", "code_erreur": e.code, "message": e.message, "url": e.url}, ensure_ascii=False)); return 4

if __name__ == "__main__":
    print("Utilisez agent_N/script_source.py", file=sys.stderr); sys.exit(2)
