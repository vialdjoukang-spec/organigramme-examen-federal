#!/usr/bin/env python3
"""Harnais d'agent LOT (zéro jeton) — Leona, 9 nov. 2026.
Automatise UNIQUEMENT le mécanique : collecte, extraction, index BM25, recherche/tri/filtre, mémoire, CP,
squelette HTML V0, contrôles, rapport, captures, santé. Ne rédige rien, ne juge rien cliniquement.
Usage : harnais [--instance DOSSIER] <commande> ... (ou variable HARNAIS_INSTANCE). Inclut `illustrer` (délégation + fragment data:URI)."""
from __future__ import annotations
import argparse, csv, datetime as dt, hashlib, html, json, os, re, shutil, sqlite3, subprocess, sys, time
import urllib.parse, urllib.request, urllib.robotparser
from pathlib import Path

COEUR = Path(__file__).resolve().parent
RACINE = COEUR.parent
REGISTRE = RACINE / "registre"
ILLUSTRATION = COEUR / "illustration"
ILLUSTRER_PY = ILLUSTRATION / "illustrer.py"
MAX_IMG_DATA_O = 25_000  # plafond data:URI WebP/JPEG (octets binaires)
UA = "Leona-Harnais/1.0 (+collecte polie, usage pedagogique non commercial)"
DELAI_DOMAINE_S = 2.0
TITRES = {1: "Définition et sémantique", 2: "Épidémiologie (Suisse, puis Europe)", 3: "Physiopathologie",
          4: "Démarche diagnostique", 5: "Anamnèse ciblée et drapeaux rouges", 6: "Examen physique ciblé, région par région",
          7: "Approche syndromique", 8: "Diagnostic positif et critères", 9: "Examens complémentaires",
          10: "Arbre décisionnel", 11: "Prise en charge selon les recommandations suisses", 12: "Prévention",
          13: "Points clés", 14: "Pièges et questions fréquentes à l'examen fédéral suisse"}
RUBRIQUES = {  # extension de requête par rubrique (FR + EN pour sources anglophones) ; mécanique, pas de jugement
    "p1": "définition defined definition terminologie", "p2": "prévalence incidence mortalité épidémiologie suisse prevalence incidence",
    "p3": "physiopathologie mécanisme inflammation pathogenèse pathophysiology mechanism",
    "p4": "diagnostic démarche suspicion", "p5": "anamnèse symptômes drapeaux alarme history symptoms",
    "p6": "examen clinique auscultation signes examination", "p7": "syndrome différentiel differential",
    "p8": "critères diagnostic criteria", "p9": "spirométrie radiographie laboratoire examen imagerie test spirometry",
    "p10": "algorithme arbre décision algorithm", "p11": "traitement prise charge posologie dose recommandation thérapie treatment management therapy",
    "p12": "prévention vaccination dépistage tabac prevention vaccination screening", "p13": "essentiel retenir",
    "p14": "piège erreur attention pitfall"}
RANGS = {1: "AIPS/Swissmedic", 2: "Fedlex", 3: "OFSP/Confédération", 4: "Sociétés et organismes nationaux suisses",
         5: "HUG-CHUV-RMS-Unisanté-mediX-hôpitaux/universités suisses", 6: "Européen", 7: "International/autre",
         8: "Index NEO local (secondaire : oriente vers les sources, jamais preuve)"}
D5 = ("hug.ch", "chuv.ch", "revmed.ch", "unisante.ch", "medix.ch", "medix-romandie.ch", "urgences-ge.ch", "medskills.ch",
      "pepra.ch", "unige.ch", "unil.ch", "unibas.ch", "uzh.ch", "unibe.ch", "usz.ch", "insel.ch", "usb.ch", "ksa.ch",
      "kssg.ch", "luks.ch", "firstline.org", "hopitalvs.ch", "h-fr.ch", "hne.ch", "ehc-vd.ch", "rhne.ch", "eviprev.ch", "hcuge.ch", "unifr.ch", "ethz.ch")
D6 = (".eu", ".fr", ".de", ".at", ".it", ".be", ".nl", ".es", ".uk", "escardio.org", "ersnet.org", "erc.edu", "easl.eu",
      "esmo.org", "eular.org", "eaaci.org", "kdigo.org", "ecdc.europa.eu", "who.int/europe", "esicm.org", "ese-hormones.org", "escmid.org", "eacsociety.org")

# ---------------------------------------------------------------- utilitaires
def maintenant(): return dt.datetime.now().astimezone().isoformat(timespec="seconds")
def sha256b(b: bytes) -> str: return hashlib.sha256(b).hexdigest()
def norm(t: str) -> str: return re.sub(r"\s+", " ", t.replace("\u00ad", "")).strip()
def domaine(url: str) -> str:
    try: return (urllib.parse.urlsplit(url).hostname or "").lower().removeprefix("www.")
    except ValueError: return ""
def rang_url(url: str) -> int:
    d = domaine(url); u = url.lower()
    if u.startswith("local:neo"): return 8
    if any(d == x or d.endswith("." + x) for x in ("swissmedicinfo.ch", "refdata.ch", "swissmedic.ch")): return 1
    if d.endswith("fedlex.admin.ch"): return 2
    if d.endswith(".admin.ch") or d == "admin.ch": return 3
    if any(d == x or d.endswith("." + x) for x in D5): return 5
    if d.endswith(".ch") or d.endswith(".swiss"): return 4
    if any(d.endswith(x) or x in u for x in D6): return 6
    return 7
def type_url(url: str) -> str:
    u = url.lower(); d = domaine(url)
    if rang_url(url) == 1: return "AIPS/information professionnelle"
    if "fedlex" in d: return "loi/ordonnance"
    if "smartermedicine" in d: return "liste Top 5 smarter medicine"
    if d == "doi.org": return "article (DOI)"
    if u.split("?")[0].endswith(".pdf"): return "document PDF"
    if "guideline" in u or "recommand" in u or "strateg" in u or "protocol" in u: return "recommandation/stratégie"
    return "page web"
def charger_json(p: Path, defaut=None):
    try: return json.loads(Path(p).read_text(encoding="utf-8"))
    except (OSError, ValueError): return defaut

# ---------------------------------------------------------------- registre des sources suisses (NEO 8 nov.)
def construire_registre(md: Path, liens_json: Path, paramedical: Path | None) -> dict:
    t = md.read_text(encoding="utf-8")
    cibles = dict(re.findall(r"^\[(R\d{3})\]:\s*<([^>]+)>", t, re.M))
    entrees: dict[str, dict] = {}
    def ajout(url, specialite, organisme, origine):
        e = entrees.setdefault(url, {"url": url, "domaine": domaine(url), "specialites": [], "organismes": [], "origines": [],
                                     "type": type_url(url), "rang": rang_url(url)})
        e["rang_libelle"] = RANGS[e["rang"]]
        for k, v in (("specialites", specialite), ("organismes", organisme), ("origines", origine)):
            if v and v not in e[k]: e[k].append(v)
    section = ""
    for ligne in t.splitlines():
        if ligne.startswith("## ") or ligne.startswith("### "): section = ligne.lstrip("# ").strip()
        m = re.match(r"^\|\s*(\d{1,2})\s*\|\s*([^|]+?)\s*\|(.*)$", ligne)
        if m and section.startswith("1."):
            spec = re.sub(r"\s*\(.*$", "", m.group(2)).strip()
            for cell in m.group(3).split("|"):
                for lab, ref in re.findall(r"\[([^\]]*)\]\[(R\d{3})\]", cell):
                    org = re.findall(r"•\s*([^:•]{2,80}?)\s*:\s*[^•]*" + re.escape(f"[{ref}]"), cell)
                    ajout(cibles.get(ref, ""), f"{int(m.group(1)):02d}. {spec}", norm(org[-1]) if org else "", f"NEO v3 §1 [{ref}]")
            continue
        for ref in re.findall(r"\]\[(R\d{3})\]", ligne):
            ajout(cibles.get(ref, ""), "", "", f"NEO v3 §{section[:40]} [{ref}]")
    lj = charger_json(liens_json, {})
    for l in lj.get("links", []): ajout(l["uri"], "", "", "NEO v3 annotation PDF")
    for c in lj.get("citations", []): ajout(c["url"], "", norm(c.get("title", ""))[:120], f"NEO v3 citation {c['n']}")
    entrees.pop("", None)
    liste = sorted(entrees.values(), key=lambda e: (e["rang"], e["domaine"], e["url"]))
    compte = {f"{r} {RANGS[r]}": sum(1 for e in liste if e["rang"] == r) for r in RANGS}
    spec_n = len({s for e in liste for s in e["specialites"]})
    meta = {"schema": "registre-sources-suisses-v1", "genere": maintenant(),
            "source_md": str(md), "source_md_sha256": sha256b(md.read_bytes()),
            "source_liens_sha256": sha256b(liens_json.read_bytes()), "urls_uniques": len(liste), "par_rang": compte,
            "specialites_couvertes": spec_n,
            "note": "Rang attribué mécaniquement par domaine (heuristique documentée dans harnais.py:rang_url), à confirmer ; aucune URL visitée pour ce registre.",
            "paramedical": None}
    if paramedical and paramedical.exists():
        p = paramedical.read_text(encoding="utf-8")
        meta["paramedical"] = {"fichier": str(paramedical), "sha256": sha256b(paramedical.read_bytes()),
                               "specialites": len(re.findall(r"^### \d{2}\. ", p, re.M)),
                               "urls": len(re.findall(r"https?://", p)),
                               "note": "0 URL dans la source paramédicale v5 (domaine textuel siwf.ch seulement) : indexée comme document local, pas de lien ajouté."}
    return {"meta": meta, "sources": liste}

def ecrire_registre(reg: dict, dossier: Path):
    dossier.mkdir(parents=True, exist_ok=True)
    (dossier / "SOURCES_SUISSES.json").write_text(json.dumps(reg, ensure_ascii=False, indent=1), encoding="utf-8")
    with open(dossier / "SOURCES_SUISSES.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["rang", "rang_libelle", "specialites", "organismes", "url", "domaine", "type", "origines"])
        for e in reg["sources"]:
            w.writerow([e["rang"], e["rang_libelle"], " ; ".join(e["specialites"]), " ; ".join(e["organismes"]), e["url"], e["domaine"], e["type"], " ; ".join(e["origines"])])
    (dossier / "COMPTES_PAR_RANG.json").write_text(json.dumps(reg["meta"], ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- instance
class Instance:
    def __init__(self, chemin: Path):
        self.d = Path(chemin).resolve()
        self.cfg = charger_json(self.d / "config.json", {}) or {}
        for s in ("cache", "logs", "sante", "cp", "rapports", "captures", "texte"): (self.d / s).mkdir(parents=True, exist_ok=True)
    def log(self, msg):
        with open(self.d / "logs" / "harnais.log", "a", encoding="utf-8") as f: f.write(f"{maintenant()} {msg}\n")
    # --- mémoire
    def mem(self):
        c = sqlite3.connect(self.d / "memoire.sqlite"); c.execute("PRAGMA journal_mode=WAL")
        c.execute("CREATE TABLE IF NOT EXISTS memoire(id INTEGER PRIMARY KEY, ts TEXT, type TEXT, cle TEXT, valeur TEXT)")
        return c
    def retenir(self, type_, cle, valeur):
        with self.mem() as c:
            c.execute("INSERT INTO memoire(ts,type,cle,valeur) VALUES(?,?,?,?)", (maintenant(), type_, cle, json.dumps(valeur, ensure_ascii=False)))
    def rappeler(self, type_=None, motif=None, n=50):
        q, a = "SELECT ts,type,cle,valeur FROM memoire WHERE 1=1", []
        if type_: q += " AND type=?"; a.append(type_)
        if motif: q += " AND (cle LIKE ? OR valeur LIKE ?)"; a += [f"%{motif}%"] * 2
        with self.mem() as c: return [dict(ts=r[0], type=r[1], cle=r[2], valeur=json.loads(r[3])) for r in c.execute(q + " ORDER BY id DESC LIMIT ?", a + [n])]
    # --- index
    def idx(self):
        c = sqlite3.connect(self.d / "index.sqlite")
        c.executescript("""CREATE TABLE IF NOT EXISTS docs(doc_id TEXT PRIMARY KEY, url TEXT, titre TEXT, rang INT, annee TEXT, dx TEXT, sha256 TEXT, fichier TEXT, indexe TEXT);
        CREATE VIRTUAL TABLE IF NOT EXISTS passages USING fts5(pid UNINDEXED, doc_id UNINDEXED, texte, tokenize='unicode61 remove_diacritics 2');
        CREATE TABLE IF NOT EXISTS empreintes(h TEXT PRIMARY KEY, pid TEXT);""")
        return c

# ---------------------------------------------------------------- collecte (cache + hash + robots + débit poli)
_dernier_appel: dict[str, float] = {}
def robots_ok(url: str) -> bool:
    p = urllib.parse.urlsplit(url); rp = urllib.robotparser.RobotFileParser()
    try:
        req = urllib.request.Request(f"{p.scheme}://{p.netloc}/robots.txt", headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=15) as r: rp.parse(r.read().decode("utf-8", "ignore").splitlines())
    except Exception: return True  # robots absent/injoignable : autorisé par convention
    return rp.can_fetch(UA, url)
def collecter(inst: Instance, url: str, ident: str | None = None, dx: str = "", titre: str = "", annee: str = "",
              fichier_local: Path | None = None, rafraichir=False) -> dict:
    cle = sha256b(url.encode())[:20]; meta_p = inst.d / "cache" / f"{cle}.json"
    meta = charger_json(meta_p)
    if meta and not rafraichir and (inst.d / "cache" / meta["fichier"]).exists():
        meta["depuis_cache"] = True; return meta
    if fichier_local:
        b = Path(fichier_local).read_bytes(); ctype = "application/pdf" if str(fichier_local).endswith(".pdf") else "text/html"; statut = "local"
    else:
        if not robots_ok(url): raise PermissionError(f"robots.txt interdit : {url}")
        dom = domaine(url); attente = DELAI_DOMAINE_S - (time.time() - _dernier_appel.get(dom, 0))
        if attente > 0: time.sleep(attente)
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "fr-CH,fr;q=0.9,de;q=0.6,en;q=0.5"})
        with urllib.request.urlopen(req, timeout=60) as r: b = r.read(); ctype = r.headers.get("Content-Type", ""); statut = r.status
        _dernier_appel[dom] = time.time()
    ext = ".pdf" if (b[:5] == b"%PDF-" or "pdf" in ctype) else (".txt" if fichier_local and Path(fichier_local).suffix in (".md", ".txt") else ".html")
    nom = f"{cle}{ext}"; (inst.d / "cache" / nom).write_bytes(b)
    meta = {"id": ident or cle, "url": url, "fichier": nom, "sha256": sha256b(b), "octets": len(b), "content_type": ctype,
            "statut": statut, "collecte": maintenant(), "rang": rang_url(url), "dx": dx, "titre": titre, "annee": annee}
    meta_p.write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
    inst.log(f"collecte {url} {len(b)} o sha={meta['sha256'][:12]}")
    return meta

# ---------------------------------------------------------------- extraction texte
def extraire(inst: Instance, meta: dict) -> str:
    src = inst.d / "cache" / meta["fichier"]; out = inst.d / "texte" / (Path(meta["fichier"]).stem + ".txt")
    if out.exists() and out.stat().st_mtime >= src.stat().st_mtime: return out.read_text(encoding="utf-8")
    if src.suffix == ".txt": t = src.read_text(encoding="utf-8", errors="ignore")
    elif src.suffix == ".pdf":
        t = subprocess.run(["pdftotext", "-enc", "UTF-8", str(src), "-"], capture_output=True, text=True, timeout=300).stdout
    else:
        brut = src.read_text(encoding="utf-8", errors="ignore"); t = None
        try:
            import trafilatura
            t = trafilatura.extract(brut, include_tables=True, include_comments=False, favor_recall=True)
        except Exception: t = None
        if not t or len(t) < 200:  # repli regex
            b2 = re.sub(r"(?is)<(script|style|nav|header|footer)[^>]*>.*?</\1>", " ", brut)
            b2 = re.sub(r"(?i)<br\s*/?>|</p>|</li>|</h\d>|</tr>", "\n", b2)
            t = html.unescape(re.sub(r"<[^>]+>", " ", b2))
    out.write_text(t, encoding="utf-8"); return t
def decouper(t: str, n_max=650) -> list[str]:
    t = norm(t); ph = re.split(r"(?<=[.;!?])\s+(?=[A-ZÀ-ÖØ-Þ«(0-9•▪-])", t); out, cur = [], ""
    for s in ph:
        if len(cur) + len(s) + 1 > n_max and cur: out.append(cur); cur = s
        else: cur = (cur + " " + s).strip()
    if cur: out.append(cur)
    res = []
    for p in out:  # coupe dure des blocs sans ponctuation (tableaux PDF)
        while len(p) > 2 * n_max:
            c = p.rfind(" ", 0, n_max); c = c if c > 0 else n_max; res.append(p[:c]); p = p[c:].strip()
        res.append(p)
    return [p for p in res if len(p) > 60]

# ---------------------------------------------------------------- index BM25 (SQLite FTS5) + filtre doublons
def indexer(inst: Instance, meta: dict) -> dict:
    t = extraire(inst, meta); c = inst.idx(); doc = meta["id"]
    with c:
        old = c.execute("SELECT sha256 FROM docs WHERE doc_id=?", (doc,)).fetchone()
        if old and old[0] == meta["sha256"]: return {"doc": doc, "passages": 0, "deja_indexe": True}
        c.execute("DELETE FROM passages WHERE doc_id=?", (doc,)); c.execute("DELETE FROM empreintes WHERE pid LIKE ?", (doc + "-%",))
        n = dbl = 0
        for i, p in enumerate(decouper(t), 1):
            h = sha256b(re.sub(r"\W+", "", p.lower()).encode()); pid = f"{doc}-{i:03d}"
            if c.execute("SELECT 1 FROM empreintes WHERE h=?", (h,)).fetchone(): dbl += 1; continue
            c.execute("INSERT INTO empreintes VALUES(?,?)", (h, pid)); c.execute("INSERT INTO passages VALUES(?,?,?)", (pid, doc, p)); n += 1
        c.execute("INSERT OR REPLACE INTO docs VALUES(?,?,?,?,?,?,?,?,?)", (doc, meta["url"], meta.get("titre", ""), meta["rang"],
                  str(meta.get("annee", "")), meta.get("dx", ""), meta["sha256"], meta["fichier"], maintenant()))
    inst.log(f"index {doc} {n} passages, {dbl} doublons filtrés"); return {"doc": doc, "passages": n, "doublons_filtres": dbl}

def requete_fts(q: str) -> str:
    mots = [m for m in re.findall(r"\w[\w'-]*", q.lower()) if len(m) > 2]
    return " OR ".join('"' + m.replace('"', '') + '"' for m in dict.fromkeys(mots)) or '""'
def chercher(inst: Instance, q: str, rubrique: str = "", dx: str = "", suisse=False, rang_max=8, max_age_ans=None, n=10, tri="suisse") -> list[dict]:
    if rubrique: q = f"{q} {RUBRIQUES.get(rubrique, '')}"
    if suisse: rang_max = min(rang_max, 5)
    c = inst.idx(); sql = ("SELECT p.pid, p.doc_id, p.texte, bm25(passages) s, d.url, d.rang, d.annee, d.titre, d.dx FROM passages p "
                           "JOIN docs d ON d.doc_id=p.doc_id WHERE passages MATCH ? AND d.rang<=?")
    a = [requete_fts(q), rang_max]
    if dx: sql += " AND (d.dx=? OR d.dx='')"; a.append(dx)
    rows = c.execute(sql + " ORDER BY s LIMIT 200", a).fetchall()
    an = dt.date.today().year; out = []
    for pid, doc, t, s, url, rang, annee, titre, d in rows:
        y = int(m.group()) if (m := re.search(r"(19|20)\d{2}", annee or "")) else None
        if max_age_ans is not None and y is not None and an - y > max_age_ans: continue
        out.append({"pid": pid, "doc": doc, "rang": rang, "annee": annee, "bm25": round(s, 3), "url": url, "titre": titre, "texte": t, "perime": bool(y and an - y > 10)})
    if tri == "suisse":  # défaut : 25 meilleurs BM25, puis bloc suisse (1–5) avant non suisse (6–7) avant index NEO (8), pertinence dans chaque bloc
        out = sorted(out, key=lambda r: r["bm25"])[:25]; out.sort(key=lambda r: (0 if r["rang"] <= 5 else 1 if r["rang"] <= 7 else 2, r["bm25"]))
    elif tri == "rang": out.sort(key=lambda r: (r["rang"], r["bm25"]))
    elif tri == "date": out.sort(key=lambda r: (-(int(re.search(r"\d{4}", r["annee"]).group()) if re.search(r"\d{4}", r["annee"] or "") else 0), r["bm25"]))
    # tri "pertinence" = ordre bm25 natif
    return out[:n]

def prise_en_charge(inst: Instance, q: str, dx="", n=8) -> dict:
    """Prise en charge : sources suisses (rangs 1–5) en priorité absolue ; refus explicite si aucune."""
    ch = chercher(inst, q, "p11", dx, suisse=True, n=n)
    if ch: return {"statut": "OK_SUISSE", "passages": ch}
    hors = chercher(inst, q, "p11", dx, n=3)
    return {"statut": "REFUS_AUCUNE_SOURCE_SUISSE", "message": "Aucune source suisse indexée : affirmation de prise en charge REFUSÉE. "
            "Toute utilisation d'une source non suisse doit être marquée <span class=\"exception-non-suisse\"> et justifiée.", "non_suisses_pour_info": hors}

# ---------------------------------------------------------------- CP (point de contrôle)
def cp_sauver(inst: Instance, note=""):
    prod = Path(inst.cfg.get("dossier_production", "")) if inst.cfg.get("dossier_production") else None
    fichiers = {}
    if prod and prod.exists():
        for f in sorted(prod.glob("*.html")): fichiers[f.name] = {"octets": f.stat().st_size, "sha256": sha256b(f.read_bytes())}
    c = inst.idx(); nd = c.execute("SELECT count(*) FROM docs").fetchone()[0]; npass = c.execute("SELECT count(*) FROM passages").fetchone()[0]
    with inst.mem() as m: nm = m.execute("SELECT count(*) FROM memoire").fetchone()[0]
    etat = inst.rappeler("etat", n=1)
    corps = {"ts": maintenant(), "agent": inst.cfg.get("agent"), "note": note, "etat": etat[0] if etat else None,
             "index_docs": nd, "index_passages": npass, "memoire_entrees": nm, "fichiers_production": fichiers}
    b = json.dumps(corps, ensure_ascii=False, sort_keys=True).encode(); corps["sha256_corps"] = sha256b(b)
    nom = f"CP_{dt.datetime.now().strftime('%Y%m%dT%H%M%S')}.json"
    for n_ in (nom, "DERNIER.json"): (inst.d / "cp" / n_).write_text(json.dumps(corps, ensure_ascii=False, indent=1), encoding="utf-8")
    return corps
def cp_verifier(inst: Instance) -> tuple[bool, str]:
    c = charger_json(inst.d / "cp" / "DERNIER.json")
    if not c: return False, "aucun CP"
    s = c.pop("sha256_corps", ""); ok = sha256b(json.dumps(c, ensure_ascii=False, sort_keys=True).encode()) == s
    return ok, f"CP {c['ts']} {'intègre' if ok else 'ALTÉRÉ'}"

# ---------------------------------------------------------------- squelette HTML V0 (forme seulement)
CSS_V0 = """:root{--b:#0b3d62;--a:#c0392b;--g:#5b6770;--f:#f4f7fa}
*{box-sizing:border-box}body{margin:0;font:17px/1.6 Georgia,'Times New Roman',serif;color:#1d232a;background:#fff}
main{max-width:46rem;margin:auto;padding:0 1rem 3rem}
p,div.p,li,dd,[popover] p,details div{text-align:justify;hyphens:auto;-webkit-hyphens:auto;overflow-wrap:break-word}
section.ilot{border:1px solid #dde3e8;border-left:4px solid var(--b);border-radius:.6rem;background:#fff;padding:.2rem 1rem .8rem;margin:1.2rem 0;box-shadow:0 1px 3px rgba(0,0,0,.06)}
h2{font:700 1.5rem/1.25 system-ui,sans-serif;color:var(--b)}h3{font:700 1.12rem/1.3 system-ui,sans-serif;color:var(--b);margin:.8rem 0 .5rem}
.tw{overflow-x:auto}table{border-collapse:collapse;width:100%;font:.86rem/1.4 system-ui,sans-serif}th{background:var(--b);color:#fff;text-align:left;padding:.4rem}td{border-bottom:1px solid #dde3e8;padding:.4rem;vertical-align:top}
button.fen{font:inherit;color:var(--b);background:none;border:0;border-bottom:1px dotted var(--b);padding:0;cursor:pointer}
[popover].fenetre{width:min(96vw,60rem);max-height:88vh;overflow:auto;padding:1rem;border:1px solid #888;border-radius:.5rem}
[popover]::backdrop{background:rgb(0 0 0 / .35)}
details.fc{display:inline}details.fc:not([open])::details-content{display:none}details.fc>summary{display:inline;cursor:pointer;color:var(--b);border-bottom:1px dotted var(--b);list-style:none}
details.fc[open]>div{display:block;margin:.4rem 0;padding:.5rem .8rem;border-left:3px solid var(--b);background:var(--f)}
div.u{border:2px solid var(--a);border-radius:.6rem;background:#fff5f4;padding:.2rem .8rem .6rem;margin:1rem 0}
.exception-non-suisse{background:#fff3cd}.nv{font-style:italic;color:var(--g)}"""
def squelette(lot: str, n: int, titre: str, lot_titre: str = "") -> str:
    blocs = []
    for k in range(1, 15):
        # NB : <details> est un élément de bloc ; dans un <p> le navigateur ferme le <p> et coupe la phrase.
        # Une phrase qui porte une fenêtre <details> inline vit donc dans <div class="p">, jamais dans <p>.
        fen = "" if k == 13 else (f"\n<p>⟦À RÉDIGER⟧ 1 à 4 phrases ; terme technique → <button type=\"button\" class=\"fen\" popovertarget=\"dx{n}-p{k}-f1\">terme</button> (grande fenêtre).</p>\n"
              f"<div id=\"dx{n}-p{k}-f1\" popover class=\"fenetre\"><button type=\"button\" popovertarget=\"dx{n}-p{k}-f1\" popovertargetaction=\"hide\">Fermer ✕</button>\n<p>⟦À RÉDIGER⟧ mécanisme, exemple chiffré, piège, source [Sn].</p></div>\n"
              f"<div class=\"p\">⟦À RÉDIGER⟧ phrase avec fenêtre courte <details class=\"fc\" style=\"display:inline;\"><summary>terme</summary><div>⟦À RÉDIGER⟧ définition courte, source [Sn].</div></details> qui reste intacte.</div>")
        if k == 9: fen = (f"\n<h4 id=\"dx{n}-p9a\"><em>9.a Gold standard</em></h4>\n<p>⟦À RÉDIGER⟧ gold standard (ou « pas de gold standard » écrit).</p>"
                          f"\n<h4 id=\"dx{n}-p9b\"><em>9.b 1<sup>re</sup> intention</em></h4>" + fen)
        if k == 13: fen = "\n<p>⟦À RÉDIGER⟧ 3 à 6 phrases courtes, verbales, intactes ; aucune fenêtre ne coupe une phrase porteuse.</p>"
        urg = (f"\n<div class=\"u\" id=\"dx{n}-urgence\"><h4>Fenêtre « Urgence — conduite chronologique »</h4><p>⟦À RÉDIGER⟧ conduite minute par minute ; sources suisses uniquement.</p></div>" if k == 11 else "")
        blocs.append(f"<section class=\"ilot\" id=\"dx{n}-i{k}\">\n<h3 id=\"dx{n}-p{k}\"><strong>{k}. {TITRES[k]}</strong></h3>{fen}{urg}\n</section>")
    nom = f"LOT_{lot}_Phase_B_V0_DX.{n}.html"
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>LOT {lot} — Phase B — DX.{n} {html.escape(titre)}</title>
<style>
{CSS_V0}
</style>
</head>
<body>
<main>
<header class="lot">LOT {lot} {html.escape(lot_titre)} · Phase B · V0</header>
<h2 id="dx{n}">DX.{n} — {html.escape(titre)}</h2>
<section class="monograph" id="dx{n}-mono">
""" + "\n".join(blocs) + f"""
</section>
<section id="sources">
<h3>Sources</h3>
<ol>
<li id="sb-1">[S1] [titre, organisme, année. URL (consulté le JJ mois AAAA).]</li>
</ol>
<p class="nv">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</section>
</main>
</body>
</html>
<!-- FIN_FICHIER {nom} -->
"""


# ---------------------------------------------------------------- illustration (délégation + data:URI)
LICENCES_IMG_OK = re.compile(r"(?i)\b(CC\s*0|CC0|CC\s*BY(?:\s*[- ]?\s*SA)?|domaine\s+public|public\s+domain)\b")
LICENCES_IMG_INTERDITES = re.compile(r"(?i)(?:\bNC\b|\bND\b|non[\s-]?commercial|no[\s-]?derivativ)")

def image_vers_data_uri(chemin: Path, plafond: int = MAX_IMG_DATA_O) -> tuple[str, str, int]:
    """Convertit une image rendue en data:URI WebP (sinon JPEG) ≤ plafond octets binaires."""
    from PIL import Image
    import base64, io
    im = Image.open(chemin).convert("RGB")
    essais = [
        ("WEBP", "image/webp", [{"quality": q, "method": 4} for q in (80, 70, 60, 50, 40, 30, 20)]),
        ("JPEG", "image/jpeg", [{"quality": q, "optimize": True} for q in (85, 75, 65, 55, 45, 35, 25)]),
    ]
    candidats = [im]
    w, h = im.size
    for scale in (0.75, 0.5, 0.35, 0.25):
        candidats.append(im.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.Resampling.LANCZOS))
    for img in candidats:
        for fmt, mime, kws in essais:
            for kw in kws:
                buf = io.BytesIO(); img.save(buf, fmt, **kw); raw = buf.getvalue()
                if len(raw) <= plafond:
                    return f"data:{mime};base64,{base64.b64encode(raw).decode('ascii')}", mime, len(raw)
    raise RuntimeError(f"impossible de compresser {chemin} sous {plafond} o")

def fragment_figure_data(data_uri: str, *, alt: str, titre: str, source: str, auteur: str, licence: str, anomalies: list[str]) -> str:
    """Fragment HTML <figure> autonome : img data:, légende source/auteur/licence, liste numérotée des anomalies."""
    items = "".join(f"<li>{html.escape(a)}</li>" for a in anomalies)
    mention = f"Source : {source}. Auteur : {auteur}. Licence : {licence}."
    return (
        '<figure class="schema illustration">\n'
        f'<img src="{data_uri}" alt="{html.escape(alt or titre or "illustration")}">\n'
        "<figcaption>\n"
        f"<strong>{html.escape(titre or 'Illustration')}</strong>\n"
        f'<p class="mention">{html.escape(mention)}</p>\n'
        f'<ol start="1">{items}</ol>\n'
        "</figcaption>\n</figure>\n"
    )

def illustrer_deleguer(argv: list[str]) -> int:
    """Délègue à coeur/illustration/illustrer.py (copie octet-identique, non modifiée)."""
    if not ILLUSTRER_PY.exists():
        raise FileNotFoundError(f"illustrer.py absent : {ILLUSTRER_PY}")
    py = str(COEUR / ".venv/bin/python") if (COEUR / ".venv/bin/python").exists() else sys.executable
    r = subprocess.run([py, str(ILLUSTRER_PY), *argv], capture_output=True, text=True)
    if r.stdout: print(r.stdout, end="" if r.stdout.endswith("\n") else "\n")
    if r.stderr: print(r.stderr, end="" if r.stderr.endswith("\n") else "\n", file=sys.stderr)
    return r.returncode

def illustrer_apres_rendre(annotations: list[Path], sortie: Path) -> list[dict]:
    """Après --rendre : convertit chaque PNG en data:URI ≤25 Ko et réécrit le fragment HTML."""
    res = []
    for ap in annotations:
        ann = json.loads(Path(ap).read_text(encoding="utf-8"))
        ident = ann.get("id") or Path(ap).stem
        png = sortie / f"{ident}.png"
        if not png.exists():
            # biologie peut produire SVG ; chercher aussi .webp/.jpg
            cands = list(sortie.glob(f"{ident}.*"))
            pngs = [c for c in cands if c.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")]
            if not pngs: raise FileNotFoundError(f"image rendue introuvable pour {ident} dans {sortie}")
            png = pngs[0]
        uri, mime, nbytes = image_vers_data_uri(png)
        src = ann.get("source") or {}
        licence = src.get("licence") or ""
        if isinstance(src.get("references"), list) and src["references"]:
            licence = licence or src["references"][0].get("licence_figure") or "schéma pédagogique (références citées)"
            auteur = ", ".join(r.get("titre", "") for r in src["references"] if r.get("titre")) or "schéma"
            source = "schéma biologique (références de l'annotation)"
        else:
            auteur = src.get("auteur") or "—"
            source = src.get("url_page") or src.get("identifiant") or src.get("entrepot") or "—"
        anomalies = [str(L.get("legende") or L.get("texte") or "").strip() for L in (ann.get("lesions") or ann.get("elements") or [])]
        anomalies = [a for a in anomalies if a]
        frag = fragment_figure_data(uri, alt=ann.get("alt") or ann.get("titre") or ident,
                                   titre=ann.get("titre") or ident, source=str(source),
                                   auteur=str(auteur), licence=str(licence), anomalies=anomalies)
        fp = sortie / f"{ident}.fragment.html"
        fp.write_text(frag, encoding="utf-8")
        res.append({"id": ident, "fragment": str(fp), "mime": mime, "octets_binaires": nbytes, "licence": licence})
    return res

# Rév. prompt 9.11.2026 (§11 point 9, §24) : sous-titre gold standard / 1re intention + termes vagues
RE_SOUS_TITRE_P9 = {
    "gold_standard": re.compile(r"(?is)<(h4|h5|strong|em|summary|th)\b[^>]*>(?:(?!</\1>).)*?(gold[\s\u00a0-]*standard|examen\s+de\s+r[ée]f[ée]rence)"),
    "premiere_intention": re.compile(r"(?is)<(h4|h5|strong|em|summary|th)\b[^>]*>(?:(?!</\1>).)*?(1\s*(?:<sup>\s*)?(?:re|ère|er)\b|premi[eè]re)(?:\s*</sup>)?[\s\u00a0]*intention"),
}
RE_TERMES_VAGUES = re.compile(r"(?i)\b(anomalies?|taches?|trucs?|machins?|quelque\s+chose|images?\s+(?:bizarres?|suspectes?|anormales?)|aspects?\s+anormal(?:e|aux|es)?|truc)\b")
RE_TERMES_DEDIES = re.compile(r"(?i)(opacit|clart|bronchogramme|silhouette|épanchement|epanchement|hydro-?a[ée]rique|hypodens|hyperdens|isodens|prise\s+de\s+contraste|rehaussement|verre\s+dépoli|hypersignal|hyposignal|isosignal|échogène|echogene|cône\s+d.ombre|renforcement\s+postérieur|décalage|onde\s+q|trouble\s+ventilatoire|réversibilit|cytolyse|cholestase|émie|urie|hyperfix|hypofix|de\s+signal)")
def controler_point9_contenu(seg9: str, E) -> dict:
    """p9 : sous-titre gold standard et/ou 1re intention (critique si les deux manquent) ; termes vagues (avertissement)."""
    st = {k: bool(r.search(seg9)) for k, r in RE_SOUS_TITRE_P9.items()}
    if not any(st.values()):
        E("semantique_detecte", "critique", "p9 : aucun sous-titre « gold standard » ni « 1re intention » (prompt rév. 9.11.2026 §11 point 9 : au minimum l'un des deux)")
    # texte principal + listes sous images (figcaption) ; on retire seulement les mentions source/licence
    s = re.sub(r"(?is)<p[^>]*class=[\"']mention[\"'][^>]*>.*?</p>", " ", seg9)
    s = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<h[1-6].*?</h[1-6]>", " ", s)))
    vagues = []
    for m in RE_TERMES_VAGUES.finditer(s):
        voisin = s[m.end(): m.end() + 60]
        if m.group(1).lower().startswith("anomalie") and RE_TERMES_DEDIES.search(voisin): continue  # « anomalie de signal : hypersignal T2 » admis
        vagues.append(norm(s[max(0, m.start() - 30): m.end() + 30]))
    if vagues:
        E("semantique_detecte", "avert", f"p9 : {len(vagues)} terme(s) vague(s) (heuristique ; employer le terme dédié de la modalité, prompt §24) ex. « {vagues[0][:80]} »")
    return {"sous_titres": st, "termes_vagues": vagues[:20]}

def controler_images_point9(seg9: str, E) -> dict:
    """Contrôle « images point 9 » : data:URI, licence libre, source, liste numérotée ; absence = avertissement."""
    info = {"nb_img": 0, "ok": 0}
    imgs = list(re.finditer(r"(?is)<img\b([^>]*)>", seg9))
    info["nb_img"] = len(imgs)
    if not imgs:
        E("semantique_detecte", "avert", "p9 examens complémentaires : aucune image (absence peut être justifiée si aucune figure libre fiable)")
        return info
    # découper le point en figures ou fenêtres autour de chaque img
    for i, m in enumerate(imgs, 1):
        attrs = m.group(1)
        src_m = re.search(r"""src\s*=\s*["']([^"']+)["']""", attrs, re.I)
        src = src_m.group(1) if src_m else ""
        # contexte : figure englobante si possible, sinon voisinage
        avant = seg9.rfind("<figure", 0, m.start())
        apres_fig = seg9.find("</figure>", m.end())
        if avant >= 0 and apres_fig > m.start():
            ctx = seg9[avant:apres_fig + len("</figure>")]
        else:
            ctx = seg9[max(0, m.start() - 200): m.end() + 1200]
        if not src:
            E("securite", "critique", f"p9 image #{i} : attribut src absent")
            continue
        if re.match(r"(?i)https?://", src) or (not src.startswith("data:") and "://" in src):
            E("securite", "critique", f"p9 image #{i} : src externe interdit (exiger data:URI embarquée)")
            continue
        if not src.startswith("data:"):
            E("securite", "critique", f"p9 image #{i} : src non data: (fichier relatif/externe refusé pour autonomie du DX)")
            continue
        # légende / licence / source
        # Le data URI (base64) peut contenir les lettres NC ou ND entre deux symboles :
        # on juge la licence sur la légende, pas sur les octets de l'image.
        ctx_txt = re.sub(r"(?is)\bsrc\s*=\s*[\"'][^\"']*[\"']", " ", ctx)
        if LICENCES_IMG_INTERDITES.search(ctx_txt):
            E("sources", "critique", f"p9 image #{i} : licence NC/ND ou non libre")
            continue
        if not LICENCES_IMG_OK.search(ctx_txt):
            E("sources", "critique", f"p9 image #{i} : licence absente ou non reconnue (exiger CC0 / CC BY / CC BY-SA / domaine public)")
            continue
        if not re.search(r"(?i)\b(source|wikimedia|commons|open-?i|europe\s*pmc|pmc|auteur)\b", ctx_txt):
            E("sources", "critique", f"p9 image #{i} : source/auteur absent de la légende")
            continue
        # liste numérotée juste après l'image (dans la figure / figcaption)
        apres_img = ctx[ctx.find("<img"):] if "<img" in ctx else ctx[m.start() - (avant if avant >= 0 else 0):]
        if not re.search(r"(?is)<img\b[^>]*>.*?<ol\b", apres_img):
            E("semantique_detecte", "critique", f"p9 image #{i} : liste numérotée <ol> absente juste après l'image (anomalies / contours)")
            continue
        info["ok"] += 1
    return info

# ---------------------------------------------------------------- contrôles scriptables
STOP_TERMES = set("""limite suite visite site vite ensuite petite conduite faite dite chose dose propose suppose repose impose expose
réussite gratuite écrite décrite prescrite inscrite produite réduite introduite construite poursuite fuite élite cite cité
rose prose pose cause clause pause dispose compose oppose""".split())
ACRONYMES_OK = {"DX", "LOT", "HUG", "CHUV", "OFSP", "AIPS", "FMH", "ISFM", "SMPR", "CH", "UE", "EU", "SI", "URL", "HTML", "OK", "PDF", "RUG", "IUMFE", "CEP", "SPLF", "SGP", "OMS", "FIN", "V0"}
RE_TECH = re.compile(r"\b([A-Z][A-Z0-9]{1,6}|[a-zà-ÿ]{4,}(?:ite|ose|émie|urie|pathie|plégie|algie|ectomie|tomie|scopie|graphie|métrie|mab|nib|olol|pril|sartan|azole|cilline|mycine|asone|olone|térol|tropium|thérapie))\b")
def sections_points(t: str, n: int) -> dict[int, str]:
    pos = [(int(m.group(1)), m.start()) for m in re.finditer(rf"<h3[^>]*\bid=[\"']dx{n}-p(\d{{1,2}})[\"']", t)]
    fin = t.find('<section id="sources">'); fin = fin if fin > 0 else len(t)
    return {k: t[s:(pos[i + 1][1] if i + 1 < len(pos) else fin)] for i, (k, s) in enumerate(pos)}
def texte_principal(seg: str) -> str:
    s = re.sub(r"(?is)<div[^>]*\bpopover\b[^>]*>.*?</div>", " ", seg)
    s = re.sub(r"(?is)<details.*?</details>|<button.*?</button>|<abbr.*?</abbr>|<sup.*?</sup>|<h3.*?</h3>|<h4.*?</h4>", " ", s)
    return html.unescape(re.sub(r"<[^>]+>", " ", s))
def declencheurs(t: str) -> str:
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", x)) for x in re.findall(r"(?is)<button[^>]*popovertarget[^>]*>(.*?)</button>|<summary[^>]*>(.*?)</summary>|<abbr[^>]*>(.*?)</abbr>", t) for x in x if x).lower()
def controler(inst: Instance | None, f: Path, liens=False, francais=True) -> dict:
    sys.path.insert(0, str(COEUR)); import controle_lot_v0 as V0
    t = f.read_text(encoding="utf-8", errors="replace"); o = f.stat().st_size
    m = re.search(r"Phase_B_V0_DX\.(\d{1,2})", f.name) or re.search(r"<h2[^>]*id=[\"']dx(\d{1,2})[\"']", t)
    n = int(m.group(1)) if m else 1
    R = {"fichier": str(f), "octets": o, "sha256": sha256b(f.read_bytes()), "dx": n, "syntaxe": [], "semantique_detecte": [], "langue": [], "sources": [], "securite": [], "info": {}}
    def E(cat, niv, msg): R[cat].append({"niveau": niv, "msg": msg})
    a = V0.analyse_fichier(f)
    for c in a.get("critiques", []): E("syntaxe", "critique", f"V0 controle_lot 1.1 : {c}")
    for c in a.get("avertissements", []): E("syntaxe", "avert", f"V0 controle_lot 1.1 : {c}")
    if not 80_000 <= o <= 150_000: E("syntaxe", "critique", f"taille {o} o hors bande 80–150 Ko")
    if not re.search(r"<!--\s*FIN_FICHIER\s+[^>]*-->\s*$", t): E("syntaxe", "critique", "FIN_FICHIER absent en fin de fichier")
    if not re.search(r"<html[^>]*\blang=[\"']fr", t, re.I): E("langue", "critique", "<html lang=\"fr\"> absent (césure française impossible)")
    longues = sum(1 for l in t.splitlines() if len(l) > 3000)
    if longues: E("syntaxe", "avert", f"{longues} ligne(s) > 3000 caractères")
    seg = sections_points(t, n); manq = [k for k in range(1, 15) if k not in seg]
    if manq: E("semantique_detecte", "critique", f"ids dx{n}-p… manquants : {manq}")
    style = " ".join(re.findall(r"(?is)<style[^>]*>(.*?)</style>", t))
    if not re.search(r"text-align\s*:\s*justify", style): E("langue", "critique", "texte non justifié (aucun text-align:justify dans le CSS)")
    if not re.search(r"hyphens\s*:\s*auto", style): E("langue", "avert", "hyphens:auto absent (justification sans césure → lézardes)")
    ilots = [k for k in range(1, 15) if re.search(rf"<(section|div)[^>]*class=[\"'][^\"']*\bilot\b[^\"']*[\"'][^>]*>\s*<h3[^>]*id=[\"']dx{n}-p{k}[\"']", t)]
    if len(ilots) < 14: E("semantique_detecte", "critique", f"îlots : {len(ilots)}/14 points enveloppés dans <section class=\"ilot\">")
    trig = declencheurs(t); fen_par_point = {}; sans = {}
    for k, s in seg.items():
        nb = len(re.findall(r"(?i)<div[^>]*\bpopover\b", s)) + len(re.findall(r"(?i)<details", s)); fen_par_point[f"p{k}"] = nb
        if nb == 0 and k != 13: E("semantique_detecte", "critique", f"p{k} « {TITRES[k]} » : 0 fenêtre")
        for terme in set(RE_TECH.findall(texte_principal(s))):
            if terme.lower() in STOP_TERMES or terme in ACRONYMES_OK or re.fullmatch(r"S\d+|P\d+|DX\d*|\d+", terme): continue
            if terme.lower() not in trig: sans.setdefault(terme, []).append(f"p{k}")
    R["info"]["fenetres_par_point"] = fen_par_point
    def rep4(txt):
        w = re.findall(r"[a-zà-ÿœæ]+", txt.lower()); g = {}
        for i in range(len(w) - 3): g[tuple(w[i:i + 4])] = g.get(tuple(w[i:i + 4]), 0) + 1
        return round(1000 * sum(c - 1 for c in g.values() if c > 1) / max(len(w), 1), 1), len(w)
    fens = " ".join(html.unescape(re.sub(r"<[^>]+>", " ", x)) for x in re.findall(r"(?is)<div[^>]*\bpopover\b[^>]*>(.*?)</div>|<details.*?</details>", t))
    R["info"]["rep4_par_zone_1000mots"] = {"texte_principal": rep4(" ".join(texte_principal(x) for x in seg.values())), "fenetres": rep4(fens),
                                            "note": "[valeur, mots] ; découpage simple sans spaCy, pour localiser les répétitions"}
    R["info"]["termes_techniques_sans_fenetre"] = dict(sorted(sans.items())[:60])
    if sans: E("semantique_detecte", "avert", f"{len(sans)} terme(s) technique(s) sans fenêtre (heuristique, à confirmer) ex. {', '.join(sorted(sans)[:8])}")
    dp = len(re.findall(r"(?is)<p\b[^>]*>(?:(?!</p>).)*?<details", t))
    if dp: E("semantique_detecte", "critique", f"{dp} fenêtre(s) <details> dans un <p> : le navigateur ferme le <p> et coupe la phrase → utiliser <div class=\"p\">")
    if 11 in seg and "Urgence" not in seg[11]: E("semantique_detecte", "critique", "p11 : fenêtre « Urgence — conduite chronologique » absente")
    # sources + prise en charge suisse
    srcs = {}
    sec = t[t.find('<section id="sources">'):] if '<section id="sources">' in t else ""
    for li in re.findall(r"(?is)<li[^>]*>(.*?)</li>", sec):
        ms = re.search(r"\[S(\d+)\]", li); mu = re.search(r"href=[\"'](https?://[^\"']+)", li) or re.search(r"(https?://\S+?)[\s<)]", li)
        if ms: srcs[ms.group(1)] = mu.group(1) if mu else ""
    R["info"]["sources"] = {k: {"url": u, "rang": rang_url(u) if u else None} for k, u in srcs.items()}
    if not srcs: E("sources", "critique", "section Sources [Sn] absente ou vide")
    if "non validé cliniquement" not in t: E("securite", "critique", "mention « non validé cliniquement » absente")
    if 11 in seg:
        nb_ns = 0
        for b in re.findall(r"(?is)<(?:p|li|tr|div class=\"p\")\b[^>]*>(.*?)</(?:p|li|tr|div)>", re.sub(r"(?is)<div[^>]*\bpopover\b[^>]*>.*?</div>", " ", seg[11])):
            txt = norm(html.unescape(re.sub(r"<[^>]+>", " ", b)))
            if len(txt.split()) < 8 or "⟦À RÉDIGER⟧" in txt: continue
            cites = set(re.findall(r"\bS(\d+)\b", b)) | set(re.findall(r"#sb-(\d+)", b))
            if "exception-non-suisse" in b: continue
            if not any((srcs.get(c) and rang_url(srcs[c]) <= 5) for c in cites): nb_ns += 1
        if nb_ns: E("sources", "critique", f"p11 prise en charge : {nb_ns} bloc(s) sans source suisse citée (rangs 1–5) ni marque exception-non-suisse")
    nonch = [k for k, u in srcs.items() if u and rang_url(u) > 5]
    if nonch: E("sources", "info", f"sources non suisses citées : {', '.join('S' + k for k in nonch)} (autorisées hors p11 si le rang suisse manque)")
    # sécurité / interdits
    if re.search(r"\stitle\s*=", re.sub(r"(?is)<head>.*?</head>", "", t)): E("securite", "critique", "attribut title= (infobulle interdite)")
    if re.search(r"(?i)<script\b", t): E("securite", "critique", "<script> présent (fichier sans JavaScript)")
    if re.search(r"(?i)<[a-z][^>]*\son[a-z]+\s*=", t): E("securite", "critique", "attribut on…= présent")
    if re.search(r"(?i)<(img|link|iframe)[^>]*(src|href)=[\"']https?://", t): E("securite", "critique", "ressource externe chargée (img/link/iframe)")
    # images point 9 (examens complémentaires)
    if 9 in seg:
        R["info"]["images_p9"] = controler_images_point9(seg[9], E)
        R["info"]["contenu_p9"] = controler_point9_contenu(seg[9], E)
    else:
        E("semantique_detecte", "avert", "p9 absent : contrôle images point 9 non applicable")
    # html-validate (syntaxe)
    hv = COEUR / "node" / "node_modules" / ".bin" / "html-validate"
    if hv.exists():
        cfg = COEUR / "htmlvalidate.json"
        r = subprocess.run([str(hv), "-c", str(cfg), "-f", "json", str(f)], capture_output=True, text=True, timeout=120)
        try:
            msgs = [m_ for x in json.loads(r.stdout or "[]") for m_ in x.get("messages", [])]
            par = {}
            for m_ in msgs: par.setdefault(m_["ruleId"], []).append(m_)
            for rid, l in sorted(par.items(), key=lambda x: -len(x[1])):
                E("syntaxe", "critique" if l[0]["severity"] == 2 else "avert", f"html-validate {rid} ×{len(l)} (l.{l[0]['line']} : {l[0]['message'][:90]})")
        except ValueError: E("syntaxe", "info", "html-validate : sortie illisible")
    else: E("syntaxe", "info", "html-validate non installé (coeur/installer.sh)")
    if liens:
        ly = COEUR / "outils_bin" / "lychee"
        if ly.exists():
            r = subprocess.run([str(ly), "--format", "json", "--no-progress", "--max-concurrency", "4", "--timeout", "20", "--max-retries", "1",
                                "--user-agent", UA, str(f)], capture_output=True, text=True, timeout=600)
            try:
                j = json.loads(r.stdout); morts = [e.get("url") for v in (j.get("error_map") or j.get("fail_map") or {}).values() for e in v]
                R["info"]["liens"] = {k: j.get(k) for k in ("total", "successful", "errors", "excludes", "timeouts", "redirects")}
                if morts: E("sources", "critique", f"{len(morts)} lien(s) mort(s) (lychee) ex. {morts[0]}")
            except ValueError: E("sources", "info", "lychee : sortie illisible")
    if francais:
        py = COEUR / ".venv" / "bin" / "python"; py = py if py.exists() else Path(sys.executable)
        r = subprocess.run([str(py), str(COEUR / "metriques_francais.py"), str(f), "--json"], capture_output=True, text=True, timeout=900)
        try:
            fr = json.loads(r.stdout)["prose"]; R["info"]["francais"] = fr; seuils = (inst.cfg if inst else {}).get("seuils", {})
            if fr["repetitions_4grammes_pour_1000_mots"] > seuils.get("rep4_max_1000", 10): E("langue", "critique", f"répétitions 4-grammes {fr['repetitions_4grammes_pour_1000_mots']}/1000 mots > {seuils.get('rep4_max_1000', 10)}")
            if fr["connecteurs_pour_100_mots"] < seuils.get("connecteurs_min_100", 1.0): E("langue", "avert", f"connecteurs {fr['connecteurs_pour_100_mots']}/100 mots < {seuils.get('connecteurs_min_100', 1.0)} (seuil configurable)")
            if fr["phrases_sans_verbe_%"] > 0: E("langue", "avert", f"phrases sans verbe conjugué détectées : {fr['phrases_sans_verbe_%']} % (spaCy, approx.) ex. « {(fr['exemples_sans_verbe'] or [''])[0][:70]} »")
        except (ValueError, KeyError): E("langue", "info", f"métriques français indisponibles : {r.stderr[-200:]}")
    R["synthese"] = {c: {"critique": sum(1 for x in R[c] if x["niveau"] == "critique"), "avert": sum(1 for x in R[c] if x["niveau"] == "avert")}
                     for c in ("syntaxe", "semantique_detecte", "langue", "sources", "securite")}
    R["conforme_mecanique"] = all(v["critique"] == 0 for v in R["synthese"].values())
    if inst:
        (inst.d / "rapports" / (f.stem + ".controle.json")).write_text(json.dumps(R, ensure_ascii=False, indent=1), encoding="utf-8")
        inst.retenir("controle", f.name, {"conforme": R["conforme_mecanique"], "synthese": R["synthese"], "sha256": R["sha256"]})
    return R

def rapport_html(R: dict) -> str:
    lib = {"syntaxe": "Erreurs de syntaxe", "semantique_detecte": "Sémantique (détecté mécaniquement)", "langue": "Langue", "sources": "Sources", "securite": "Sécurité"}
    col = {"critique": "#c0392b", "avert": "#d68910", "info": "#5b6770"}
    lignes = []
    for c, l in lib.items():
        s = R["synthese"][c]; fond = "#fdecea" if s["critique"] else ("#fff4e0" if s["avert"] else "#e8f6ec")
        items = "".join(f"<li style='color:{col[x['niveau']]}'><b>{x['niveau']}</b> — {html.escape(x['msg'])}</li>" for x in R[c]) or "<li style='color:#1e8449'>aucune anomalie</li>"
        lignes.append(f"<section style='background:{fond};border-radius:.5rem;padding:.4rem .9rem;margin:.6rem 0'><h3 style='margin:.3rem 0'>{lib[c]} · {s['critique']} critique(s) · {s['avert']} avert.</h3><ul>{items}</ul></section>")
    fr = R["info"].get("francais", {}); verdict = "CONFORME (mécanique)" if R["conforme_mecanique"] else "NON CONFORME (mécanique)"
    return f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<style>body{{font:15px/1.45 system-ui,sans-serif;max-width:52rem;margin:auto;padding:1rem;color:#1d232a}}li{{margin:.2rem 0}}</style></head><body>
<h2>Rapport harnais — {html.escape(Path(R['fichier']).name)}</h2>
<p><b style="color:{'#1e8449' if R['conforme_mecanique'] else '#c0392b'}">{verdict}</b> · {R['octets']} o · SHA-256 <code>{R['sha256'][:16]}…</code> · fenêtres/point : {html.escape(json.dumps(R['info'].get('fenetres_par_point', {})))}
· rép. 4-grammes {fr.get('repetitions_4grammes_pour_1000_mots', '—')}/1000 · connecteurs {fr.get('connecteurs_pour_100_mots', '—')}/100</p>
{''.join(lignes)}
<p style="color:#5b6770">Contrôles mécaniques uniquement ; le fond clinique reste à l'auditeur. Contenu non validé cliniquement.</p></body></html>"""

# ---------------------------------------------------------------- captures Playwright (desktop + mobile)
def captures(f: Path, sortie: Path, n: int) -> list[dict]:
    from playwright.sync_api import sync_playwright
    sortie.mkdir(parents=True, exist_ok=True); res = []
    cibles = [("a_prise_en_charge", f"#dx{n}-p11"), ("b_fenetre_urgence", f"#dx{n}-urgence"), ("c_physiopathologie", f"#dx{n}-p3"), ("d_epidemiologie", f"#dx{n}-p2")]
    with sync_playwright() as p:
        b = p.chromium.launch()
        for vue, (w, h, sc) in {"mobile": (390, 844, 2), "desktop": (1280, 900, 1)}.items():
            pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=sc); pg.goto(f.resolve().as_uri()); pg.wait_for_timeout(200)
            for nom, sel in cibles:
                if pg.locator(sel).count() == 0: res.append({"capture": nom, "vue": vue, "erreur": f"{sel} absent"}); continue
                bb = pg.eval_on_selector(sel, """e=>{let s=e.closest('section.ilot,div.u');let top,h,ps;
                   if(s){const r=s.getBoundingClientRect();top=r.top+scrollY;h=r.height;ps=[...s.querySelectorAll('p,div.p')];}
                   else{const hs=[...document.querySelectorAll('h3')];const nx=hs[hs.indexOf(e)+1];const r=e.getBoundingClientRect();top=r.top+scrollY;
                     h=(nx?nx.getBoundingClientRect().top+scrollY:document.body.scrollHeight)-top;ps=[];let x=e.nextElementSibling;
                     while(x&&x!==nx&&x.tagName!=='H3'){if(x.matches('p,div.p'))ps.push(x);x=x.nextElementSibling;}}
                   ps=ps.filter(x=>!x.closest('[popover]'));const al=ps.map(x=>getComputedStyle(x).textAlign);
                   return [top,h,al.length,al.filter(a=>a==='justify').length]}""")
                hh = min(bb[1] + 16, 3000); out = sortie / f"DX{n}_{nom}_{vue}.png"
                pg.screenshot(path=str(out), full_page=True, clip={"x": 0, "y": max(bb[0] - 8, 0), "width": w, "height": hh})
                res.append({"capture": nom, "vue": vue, "fichier": str(out), "hauteur_css": round(hh), "p_total": bb[2], "p_justifies_rendu": bb[3]})
            debord = pg.evaluate("document.documentElement.scrollWidth>innerWidth+1"); res.append({"vue": vue, "debordement_horizontal": debord}); pg.close()
        b.close()
    return res

# ---------------------------------------------------------------- santé (outils, CP, skills)
def sante(inst: Instance) -> dict:
    verrou = inst.d / "sante" / ".verrou"
    try: fd = os.open(verrou, os.O_CREAT | os.O_EXCL | os.O_WRONLY); os.write(fd, str(os.getpid()).encode()); os.close(fd)
    except FileExistsError:
        if time.time() - verrou.stat().st_mtime < 240: return {"ok": None, "message": "passage précédent en cours"}
        verrou.unlink(missing_ok=True); return sante(inst)
    T = []
    def test(nom, fn):
        t0 = time.time()
        try: d = fn(); T.append({"test": nom, "ok": True, "ms": round(1000 * (time.time() - t0)), "detail": d})
        except Exception as e: T.append({"test": nom, "ok": False, "ms": round(1000 * (time.time() - t0)), "detail": f"{type(e).__name__}: {e}"[:300]})
    def bin_v(cmd):
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if r.returncode: raise RuntimeError(r.stderr[-200:] or r.stdout[-200:])
        return (r.stdout or r.stderr).strip().splitlines()[0][:80]
    try:
        test("config", lambda: (inst.cfg["agent"], inst.cfg["lot"])[0])
        test("ripgrep", lambda: bin_v(["rg", "--version"]))
        test("pdftotext", lambda: bin_v(["pdftotext", "-v"]))
        test("sqlite_fts5", lambda: sqlite3.connect(":memory:").execute("CREATE VIRTUAL TABLE t USING fts5(x)") and sqlite3.sqlite_version)
        test("html-validate", lambda: bin_v([str(COEUR / "node/node_modules/.bin/html-validate"), "--version"]))
        test("lychee", lambda: bin_v([str(COEUR / "outils_bin/lychee"), "--version"]))
        py = str(COEUR / ".venv/bin/python") if (COEUR / ".venv/bin/python").exists() else sys.executable
        test("trafilatura+spacy_fr", lambda: bin_v([py, "-c", "import trafilatura,spacy,fr_core_news_sm;print('ok',trafilatura.__version__,spacy.__version__)"]))
        test("playwright_chromium", lambda: bin_v([py, "-c", "from playwright.sync_api import sync_playwright as s\nwith s() as p:\n b=p.chromium.launch();print('chromium',b.version);b.close()"]))
        def t_mem():
            k = f"sante-{time.time_ns()}"; inst.retenir("sante", k, {"ok": 1})
            assert inst.rappeler("sante", k, 1), "relecture impossible"
            with inst.mem() as c: c.execute("DELETE FROM memoire WHERE type='sante' AND id NOT IN (SELECT id FROM memoire WHERE type='sante' ORDER BY id DESC LIMIT 20)")
            return "écriture+relecture SQLite"
        test("memoire", t_mem)
        def t_idx():
            c = inst.idx(); nd = c.execute("SELECT count(*) FROM docs").fetchone()[0]
            if nd == 0: raise RuntimeError("index vide")
            sonde = inst.cfg.get("sonde_recherche", "")
            if sonde:
                r = chercher(inst, sonde, n=1)
                if not r: raise RuntimeError(f"mini-recherche « {sonde} » : 0 résultat")
                return f"{nd} docs ; sonde « {sonde} » → {r[0]['pid']}"
            return f"{nd} docs"
        test("index_recherche", t_idx)
        test("cp", lambda: (lambda ok, m: m if ok else (_ for _ in ()).throw(RuntimeError(m)))(*cp_verifier(inst)))
        def t_skills():
            sk = inst.d / "SKILL.md"; bh = COEUR / "bin" / "harnais"
            if not sk.exists() or sk.stat().st_size < 200: raise RuntimeError("SKILL.md absent/vide")
            if not os.access(bh, os.X_OK): raise RuntimeError("bin/harnais non exécutable")
            if not (REGISTRE / "SOURCES_SUISSES.json").exists(): raise RuntimeError("registre suisse absent")
            return "SKILL.md + bin/harnais + registre"
        test("skills", t_skills)
        if inst.cfg.get("ollama"):
            def t_ollama():
                with urllib.request.urlopen("http://127.0.0.1:11434/api/tags", timeout=10) as r: tags = [m["name"] for m in json.load(r)["models"]]
                with urllib.request.urlopen("http://127.0.0.1:11434/api/ps", timeout=10) as r: charges = [m["name"] for m in json.load(r).get("models", [])]
                manq = [m for m in inst.cfg.get("modeles_ollama", []) if m not in tags]
                if manq: raise RuntimeError(f"modèles absents : {manq}")
                return f"joignable ; installés {len(tags)} ; chargés {charges}"
            test("ollama", t_ollama)
        ok = all(x["ok"] for x in T)
        st = {"agent": inst.cfg.get("agent"), "ts": maintenant(), "ok": ok, "echecs": [x["test"] for x in T if not x["ok"]], "tests": T}
        (inst.d / "sante" / "statut.json").write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")
        with open(inst.d / "sante" / "historique.jsonl", "a", encoding="utf-8") as h: h.write(json.dumps({"ts": st["ts"], "ok": ok, "echecs": st["echecs"]}, ensure_ascii=False) + "\n")
        al = inst.d / "sante" / "ALERTE.json"
        if not ok: al.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")
        elif al.exists(): (inst.d / "sante" / "alertes_resolues").mkdir(exist_ok=True); al.rename(inst.d / "sante" / "alertes_resolues" / f"ALERTE_{int(time.time())}.json")
        return st
    finally: verrou.unlink(missing_ok=True)

def cloud_etat(inst: Instance) -> dict:
    """Surveillance gratuite depuis la box : dernier run Actions de la branche de l'agent (API publique, lecture seule)."""
    repo, br = inst.cfg["depot"], inst.cfg["branche"]
    url = f"https://api.github.com/repos/{repo}/actions/runs?branch={urllib.parse.quote(br, safe='')}&per_page=5"
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=20) as r: runs = json.load(r).get("workflow_runs", [])
    hs = [x for x in runs if "sante" in (x.get("path", "") + x.get("name", "")).lower()]
    der = (hs or runs or [None])[0]
    st = {"ts": maintenant(), "branche": br, "runs_vus": len(runs), "workflow_sante_present": bool(hs),
          "dernier": {k: der.get(k) for k in ("name", "status", "conclusion", "created_at", "html_url", "head_sha")} if der else None}
    st["alerte"] = bool(hs) and der.get("conclusion") not in (None, "success")
    (inst.d / "sante" / "cloud_runs.json").write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")
    return st

# ---------------------------------------------------------------- CLI
def main(argv=None):
    ap = argparse.ArgumentParser(prog="harnais", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--instance", default=os.environ.get("HARNAIS_INSTANCE", ""))
    sp = ap.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("registre", help="(re)construit le registre des sources suisses (NEO v3 + paramédical v5)")
    s.add_argument("--md", required=True); s.add_argument("--liens", required=True); s.add_argument("--paramedical", default="")
    s = sp.add_parser("collecter", help="télécharge (ou importe) une source : cache + SHA-256 + robots + débit poli, puis indexe")
    s.add_argument("--url"); s.add_argument("--id", default=None); s.add_argument("--dx", default=""); s.add_argument("--titre", default="")
    s.add_argument("--annee", default=""); s.add_argument("--fichier", default=None); s.add_argument("--depuis", help="JSON {Sn:{url,titre,annee,fichier?}}")
    s.add_argument("--dossier-local", default=None, help="avec --depuis : importer les fichiers déjà présents (aucun réseau)"); s.add_argument("--rafraichir", action="store_true")
    s = sp.add_parser("chercher", help="recherche BM25 triée par rang suisse, filtres")
    s.add_argument("requete"); s.add_argument("--rubrique", default=""); s.add_argument("--dx", default=""); s.add_argument("--suisse", action="store_true")
    s.add_argument("--rang-max", type=int, default=8); s.add_argument("--max-age-ans", type=int); s.add_argument("--n", type=int, default=10)
    s.add_argument("--tri", choices=["suisse", "rang", "pertinence", "date"], default="suisse"); s.add_argument("--json", action="store_true"); s.add_argument("--retenir", action="store_true")
    s = sp.add_parser("pec", help="prise en charge : sources suisses uniquement, refus explicite sinon"); s.add_argument("requete"); s.add_argument("--dx", default=""); s.add_argument("--n", type=int, default=8)
    s = sp.add_parser("memoire", help="mémoire de l'agent"); s.add_argument("action", choices=["ajouter", "lister", "exporter"])
    s.add_argument("--type", default=None); s.add_argument("--cle", default=""); s.add_argument("--valeur", default=""); s.add_argument("--motif", default=None)
    s = sp.add_parser("cp", help="point de contrôle"); s.add_argument("action", choices=["sauver", "verifier"]); s.add_argument("--note", default="")
    s = sp.add_parser("squelette", help="gabarit HTML V0 (forme seule)"); s.add_argument("--lot", required=True); s.add_argument("--dx", type=int, required=True)
    s.add_argument("--titre", required=True); s.add_argument("--lot-titre", default=""); s.add_argument("--sortie", required=True)
    s = sp.add_parser("controler", help="contrôles scriptables + rapport HTML coloré"); s.add_argument("fichier"); s.add_argument("--liens", action="store_true"); s.add_argument("--sans-francais", action="store_true")
    s = sp.add_parser("captures", help="4 captures × (mobile 390 px, desktop 1280 px)"); s.add_argument("fichier"); s.add_argument("--dx", type=int, default=0)
    s = sp.add_parser("illustrer", help="délègue à coeur/illustration/illustrer.py (--chercher/--rendre) ; --data-uri → fragment HTML autonome ≤25 Ko")
    s.add_argument("--chercher", nargs=2, metavar=("ENTREPOT", "REQUETE"), help="wikimedia|openi|pmc + requête")
    s.add_argument("--rendre", nargs="+", metavar="ANNOTATION.json")
    s.add_argument("-o", "--sortie", default=".")
    s.add_argument("--page", default="")
    s.add_argument("--rafraichir", action="store_true")
    s.add_argument("--data-uri", action="store_true", help="après --rendre : WebP/JPEG data:URI ≤25 Ko + fragment <figure>")
    s.add_argument("--image", default=None, help="image déjà rendue → fragment data:URI (sans appeler illustrer.py)")
    s.add_argument("--titre", default=""); s.add_argument("--alt", default="")
    s.add_argument("--source", default=""); s.add_argument("--auteur", default=""); s.add_argument("--licence", default="")
    s.add_argument("--anomalies", default="", help="anomalies séparées par | (ordre = contours)")
    s.add_argument("--fragment-sortie", default="", help="chemin du .fragment.html à écrire")
    sp.add_parser("init", help="prépare l'instance : index NEO local (orientation) + CP initial")
    sp.add_parser("sante", help="teste outils, CP, skills ; statut.json ; ALERTE.json si échec")
    sp.add_parser("cloud-etat", help="dernier run Actions de la branche (API publique)")
    a = ap.parse_args(argv)
    if a.cmd == "registre":
        reg = construire_registre(Path(a.md), Path(a.liens), Path(a.paramedical) if a.paramedical else None); ecrire_registre(reg, REGISTRE)
        print(json.dumps(reg["meta"], ensure_ascii=False, indent=1)); return 0
    if a.cmd == "illustrer":
        if a.image:
            uri, mime, nbytes = image_vers_data_uri(Path(a.image))
            anom = [x.strip() for x in a.anomalies.split("|") if x.strip()]
            frag = fragment_figure_data(uri, alt=a.alt, titre=a.titre, source=a.source or "—",
                                       auteur=a.auteur or "—", licence=a.licence or "—", anomalies=anom)
            out = Path(a.fragment_sortie) if a.fragment_sortie else Path(a.sortie) / (Path(a.image).stem + ".fragment.html")
            out.parent.mkdir(parents=True, exist_ok=True); out.write_text(frag, encoding="utf-8")
            print(json.dumps({"fragment": str(out), "mime": mime, "octets_binaires": nbytes, "plafond": MAX_IMG_DATA_O}, ensure_ascii=False, indent=1))
            return 0
        if a.chercher:
            ent, req = a.chercher
            if ent not in ("wikimedia", "openi", "pmc"):
                print("entrepôt : wikimedia, openi ou pmc", file=sys.stderr); return 2
            argv_d = ["--chercher", ent, req] + (["--rafraichir"] if a.rafraichir else [])
            return illustrer_deleguer(argv_d)
        if a.rendre:
            argv_d = ["--rendre", *a.rendre, "-o", a.sortie] + (["--page", a.page] if a.page else []) + (["--rafraichir"] if a.rafraichir else [])
            rc = illustrer_deleguer(argv_d)
            if rc: return rc
            if a.data_uri:
                infos = illustrer_apres_rendre([Path(x) for x in a.rendre], Path(a.sortie))
                print(json.dumps({"data_uri": infos, "plafond": MAX_IMG_DATA_O}, ensure_ascii=False, indent=1))
            return 0
        ap.parse_args(["illustrer", "--help"]); return 2
    if not a.instance: ap.error("--instance ou HARNAIS_INSTANCE requis")
    inst = Instance(Path(a.instance)); P = lambda o: print(json.dumps(o, ensure_ascii=False, indent=1))
    if a.cmd == "collecter":
        t0 = time.time(); res = []
        items = []
        if a.depuis:
            for sid, m in json.loads(Path(a.depuis).read_text(encoding="utf-8")).items():
                loc = Path(a.dossier_local) / m["fichier"] if a.dossier_local and m.get("fichier") else None
                items.append(dict(url=m["url"], ident=f"{a.dx or 'X'}-{sid}", titre=m.get("titre", ""), annee=str(m.get("annee", "")), fichier_local=loc if loc and loc.exists() else None))
        else: items.append(dict(url=a.url, ident=a.id, titre=a.titre, annee=a.annee, fichier_local=Path(a.fichier) if a.fichier else None))
        for it in items:
            try:
                m = collecter(inst, it["url"], it["ident"], a.dx, it["titre"], it["annee"], it["fichier_local"], a.rafraichir)
                res.append({"id": m["id"], "rang": m["rang"], "octets": m["octets"], "sha256": m["sha256"][:16], "cache": m.get("depuis_cache", False), **indexer(inst, m)})
            except Exception as e: res.append({"url": it["url"], "erreur": f"{type(e).__name__}: {e}"})
        P({"secondes": round(time.time() - t0, 2), "resultats": res}); return 0 if all("erreur" not in r for r in res) else 1
    if a.cmd == "chercher":
        r = chercher(inst, a.requete, a.rubrique, a.dx, a.suisse, a.rang_max, a.max_age_ans, a.n, a.tri)
        if a.retenir:
            for x in r: inst.retenir("preuve", x["pid"], {k: x[k] for k in ("doc", "url", "rang", "annee", "texte")} | {"requete": a.requete, "rubrique": a.rubrique})
        if a.json: P(r)
        else:
            for x in r: print(f"[{x['pid']}] rang {x['rang']} {x['annee']} bm25 {x['bm25']}{' PÉRIMÉ>10a' if x['perime'] else ''}\n  {x['texte'][:300]}\n  {x['url']}")
        return 0
    if a.cmd == "pec":
        r = prise_en_charge(inst, a.requete, a.dx, a.n); P(r); return 0 if r["statut"] == "OK_SUISSE" else 3
    if a.cmd == "memoire":
        if a.action == "ajouter": inst.retenir(a.type or "note", a.cle, a.valeur); print("ok"); return 0
        rows = inst.rappeler(a.type, a.motif, 10_000 if a.action == "exporter" else 50)
        if a.action == "exporter":
            p = inst.d / "memoire_export.jsonl"; p.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in reversed(rows)), encoding="utf-8"); print(p); return 0
        P(rows); return 0
    if a.cmd == "cp":
        if a.action == "sauver": P(cp_sauver(inst, a.note)); return 0
        ok, m = cp_verifier(inst); print(m); return 0 if ok else 1
    if a.cmd == "squelette":
        Path(a.sortie).write_text(squelette(a.lot, a.dx, a.titre, a.lot_titre), encoding="utf-8"); print(a.sortie); return 0
    if a.cmd == "controler":
        R = controler(inst, Path(a.fichier), a.liens, not a.sans_francais)
        rp = inst.d / "rapports" / (Path(a.fichier).stem + ".rapport.html"); rp.write_text(rapport_html(R), encoding="utf-8")
        P({"conforme_mecanique": R["conforme_mecanique"], "synthese": R["synthese"], "rapport": str(rp)}); return 0 if R["conforme_mecanique"] else 2
    if a.cmd == "captures":
        f = Path(a.fichier); m_ = re.search(r"DX\.(\d+)", f.name); n = a.dx or (int(m_.group(1)) if m_ else 1)
        r = captures(f, inst.d / "captures", n); P(r); return 0 if all("erreur" not in x for x in r) else 1
    if a.cmd == "init":
        r = []
        for nom, url in (("NEO_REFERENTIEL_SUISSE_2026.md", "local:neo/referentiel-v3"), ("NEO_DISCIPLINES_ALLIEES_SUISSE.md", "local:neo/paramedical-v5")):
            m = collecter(inst, url, "NEO-" + nom.split("_")[1], "", nom, "2026", REGISTRE / nom); r.append(indexer(inst, m))
        inst.retenir("etat", "init", {"agent": inst.cfg.get("agent"), "lot": inst.cfg.get("lot")}); P({"index": r, "cp": cp_sauver(inst, "init")["ts"]}); return 0
    if a.cmd == "sante":
        st = sante(inst); print(json.dumps({k: st.get(k) for k in ("agent", "ts", "ok", "echecs", "message")}, ensure_ascii=False)); return 0 if st.get("ok") is not False else 1
    if a.cmd == "cloud-etat": P(cloud_etat(inst)); return 0
if __name__ == "__main__":
    sys.exit(main())
