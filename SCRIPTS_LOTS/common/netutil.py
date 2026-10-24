"""Accès réseau sobre et déterministe : liste blanche, robots.txt, débit partagé par domaine, cache SQLite.
Bibliothèque standard uniquement (urllib, sqlite3, zlib)."""
import gzip, json, sqlite3, time, urllib.request, urllib.error, urllib.robotparser, zlib, datetime, threading
from pathlib import Path
from urllib.parse import urlparse
from token_bucket import SeauPartage

ICI = Path(__file__).resolve().parent

class ErreurSource(Exception):
    def __init__(self, code, message, url=""):
        super().__init__(message); self.code, self.message, self.url = code, message, url

def maintenant_iso():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")

class ListeBlanche:
    def __init__(self, chemin=ICI / "allowlist.json"):
        doc = json.loads(Path(chemin).read_text("utf-8"))
        self.valide_le = doc.get("valide_le")
        self.domaines = {d["domaine"]: d for d in doc["domaines"]}
        for d in list(doc["domaines"]):           # les hôtes finaux des redirections héritent du niveau
            h = d.get("hote_final")
            if h and h not in self.domaines and d["statut"] != "rejete":
                self.domaines[h] = dict(d, domaine=h)

    def info(self, hote):
        hote = (hote or "").lower()
        if hote in self.domaines:
            return self.domaines[hote]
        for nom, d in self.domaines.items():       # sous-domaines d'un domaine agréé
            if hote.endswith("." + nom.removeprefix("www.")) or hote == nom.removeprefix("www."):
                return d
        return None

    def niveau(self, url):
        d = self.info(urlparse(url).hostname)
        return d["niveau"] if d else None

    def autoriser(self, url, local_ok=False):
        u = urlparse(url)
        if local_ok and u.hostname in ("127.0.0.1", "localhost"):
            return {"niveau": 5, "statut": "valide", "auto_fetch": True}
        if u.scheme != "https":
            raise ErreurSource("DOMAINE_INTERDIT", "seul HTTPS est autorisé", url)
        d = self.info(u.hostname)
        if not d or d["statut"] == "rejete":
            raise ErreurSource("DOMAINE_INTERDIT", f"domaine hors liste blanche : {u.hostname}", url)
        if not d.get("auto_fetch"):
            raise ErreurSource("BLOQUE_ROBOTS", f"{u.hostname} bloque l'accès automatisé : consultation manuelle seulement", url)
        return d

class Cache:
    def __init__(self, dossier):
        Path(dossier).mkdir(parents=True, exist_ok=True)
        self.chemin = str(Path(dossier) / "cache.sqlite"); self._local = threading.local()
        c = self._c()
        c.execute("create table if not exists http(url text primary key, t real, statut int, type text, etag text, lm text, corps blob, finale text)")
        c.execute("create table if not exists robots(hote text primary key, t real, contenu text)")
        c.commit()

    def _c(self):
        if not hasattr(self._local, "c"):
            self._local.c = sqlite3.connect(self.chemin, timeout=30); self._local.c.execute("pragma journal_mode=wal")
        return self._local.c

    def lire(self, url):
        r = self._c().execute("select t,statut,type,etag,lm,corps,finale from http where url=?", (url,)).fetchone()
        if not r:
            return None
        return {"t": r[0], "statut": r[1], "type": r[2], "etag": r[3], "lm": r[4], "corps": zlib.decompress(r[5]), "finale": r[6]}

    def ecrire(self, url, statut, typ, etag, lm, corps, finale):
        self._c().execute("insert or replace into http values(?,?,?,?,?,?,?,?)",
                          (url, time.time(), statut, typ, etag, lm, zlib.compress(corps, 6), finale)); self._c().commit()

    def toucher(self, url):
        self._c().execute("update http set t=? where url=?", (time.time(), url)); self._c().commit()

    def robots(self, hote):
        r = self._c().execute("select t, contenu from robots where hote=?", (hote,)).fetchone()
        return r if r and time.time() - r[0] < 86400 else None

    def robots_ecrire(self, hote, contenu):
        self._c().execute("insert or replace into robots values(?,?,?)", (hote, time.time(), contenu)); self._c().commit()

class _Redir(urllib.request.HTTPRedirectHandler):
    def __init__(self, lb, local_ok): super().__init__(); self.lb, self.local_ok = lb, local_ok
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        self.lb.autoriser(newurl, self.local_ok)   # une redirection hors liste blanche est refusée
        return super().redirect_request(req, fp, code, msg, headers, newurl)

class Client:
    def __init__(self, cfg, liste=None):
        self.cfg = cfg; self.lb = liste or ListeBlanche(); self.cache = Cache(cfg["cache_dir"])
        self.ua = cfg["user_agent"]; self.h = cfg["http"]; self.seaux = {}; self.verrou = threading.Lock()

    def _seau(self, hote):
        with self.verrou:
            if hote not in self.seaux:
                d = float(self.h["per_domain_per_s"])
                self.seaux[hote] = SeauPartage(Path(self.cfg["shared_state_dir"]) / "domaines", hote, d, max(1, d))
            return self.seaux[hote]

    def _ouvrir(self, req, local_ok=False):
        op = urllib.request.build_opener(_Redir(self.lb, local_ok))
        return op.open(req, timeout=self.h["timeout_s"])

    def robots_ok(self, url):
        u = urlparse(url); hote = u.hostname
        r = self.cache.robots(hote)
        if r is None:
            contenu = ""
            try:
                if self._seau(hote).prendre(attente_max=30):
                    req = urllib.request.Request(f"https://{hote}/robots.txt", headers={"User-Agent": self.ua})
                    with self._ouvrir(req) as rep:
                        if rep.status == 200:
                            contenu = rep.read(500_000).decode("utf-8", "replace")
            except Exception:
                contenu = ""          # robots.txt absent ou illisible : accès permis (RFC 9309)
            self.cache.robots_ecrire(hote, contenu); r = (time.time(), contenu)
        rp = urllib.robotparser.RobotFileParser(); rp.parse(r[1].splitlines())
        return rp.can_fetch(self.ua, url)

    def get(self, url, ttl=None, attente_max=30, accept="text/html,application/xhtml+xml,application/pdf,application/json;q=0.9,*/*;q=0.5", local_ok=False, data=None, en_tetes=None, cle=None, params_secrets=None, api=False):
        """api=True : point d'accès programmatique documenté (E-utilities…) régi par sa propre politique d'usage ; robots.txt (qui vise les robots d'exploration) n'est pas consulté, mais le débit reste borné."""
        d = self.lb.autoriser(url, local_ok)
        niveau = d["niveau"]
        if ttl is None:
            ttl = self.h["ttl_s"].get(str(niveau), 86400)
        cle = cle or (url if data is None else url + "#" + str(zlib.crc32(data)))
        c = self.cache.lire(cle)
        if c and time.time() - c["t"] < ttl:
            return dict(c, cache="hit", niveau=niveau, url=url)
        if not local_ok and not api and not self.robots_ok(url):
            raise ErreurSource("BLOQUE_ROBOTS", "robots.txt interdit cette URL", url)
        hote = urlparse(url).hostname
        if not local_ok and not self._seau(hote).prendre(attente_max=attente_max):
            if c:
                return dict(c, cache="perime", niveau=niveau, url=url)
            raise ErreurSource("LIMITE_DEBIT", "débit du domaine épuisé", url)
        h = {"User-Agent": self.ua, "Accept": accept, "Accept-Encoding": "gzip"}
        h.update(en_tetes or {})
        if c and c.get("etag"): h["If-None-Match"] = c["etag"]
        if c and c.get("lm"): h["If-Modified-Since"] = c["lm"]
        url_req = url + ("&" if "?" in url else "?") + params_secrets if params_secrets else url
        req = urllib.request.Request(url_req, headers=h, data=data)
        try:
            with self._ouvrir(req, local_ok) as rep:
                corps = rep.read(15_000_000)
                if rep.headers.get("Content-Encoding") == "gzip":
                    corps = gzip.decompress(corps)
                typ = rep.headers.get("Content-Type", ""); finale = rep.geturl()
                self.cache.ecrire(cle, rep.status, typ, rep.headers.get("ETag"), rep.headers.get("Last-Modified"), corps, finale)
                return {"statut": rep.status, "type": typ, "corps": corps, "finale": finale, "cache": "miss", "niveau": niveau, "url": url, "t": time.time()}
        except urllib.error.HTTPError as e:
            if e.code == 304 and c:
                self.cache.toucher(cle); return dict(c, cache="revalide", niveau=niveau, url=url)
            if e.code in (429, 503):
                self._seau(hote).reculer(_retry_after(e.headers.get("Retry-After")))
                raise ErreurSource("LIMITE_DEBIT", f"HTTP {e.code} : recul appliqué", url)
            if e.code == 404:
                raise ErreurSource("NON_TROUVE", "HTTP 404", url)
            if e.code in (401, 403):
                raise ErreurSource("BLOQUE_ROBOTS", f"HTTP {e.code} : accès automatisé refusé", url)
            raise ErreurSource("SOURCE_INDISPONIBLE", f"HTTP {e.code}", url)
        except ErreurSource:
            raise
        except Exception as e:
            if c:
                return dict(c, cache="perime", niveau=niveau, url=url)
            raise ErreurSource("SOURCE_INDISPONIBLE", f"{type(e).__name__}: {e}", url)

def _retry_after(v):
    try:
        return max(1, int(v))
    except Exception:
        return None
