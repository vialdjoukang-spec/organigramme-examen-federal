#!/usr/bin/env python3
"""BRAIN-HARNESS · bus de doléances et socle commun des scriptones (stdlib seule, zéro dépendance payante).

Contrat d'entrée (JSON, `--contrat -` sur stdin)   : {"fichier": str, "html"?: str, "appliquer"?: bool, "options"?: {}}
Contrat de sortie (JSON, `--json`)                 : {"contrat": "brain.scriptone/1", "scriptone", "version", "region",
   "sha256_script", "sha256_entree", "sha256_sortie", "dry_run", "modifie", "mesures": {}, "doleances": [Doléance], "encodage", "panne"?}
Doléance : {id, region, scriptone, code, fichier, ancre, severite, constat, correction_prescrite, executant, preuve}
   executant = "script" (le scriptone corrige seul avec --appliquer) | "agent" (le rédacteur applique la correction prescrite, sans réinterpréter).
Dry-run par défaut : rien n'est écrit sans --appliquer. Idempotence : corriger(corriger(x)) == corriger(x) (testée).
Robustesse : lecture tolérante (BOM, UTF-16, cp1252), écriture atomique sous verrou exclusif (un seul écrivain par fichier),
journal append-only sous flock ; une exception d'un scriptone devient une doléance Z0 « panne » (annoncée, jamais avalée), le contrat reste valide.
Empreintes : SHA256SUMS du dossier (sous-dossiers alpha/ et beta/ compris) ; un scriptone altéré refuse de tourner (code 3)."""
import contextlib, functools, hashlib, html as H, json, os, re, sys, time
from pathlib import Path

D = Path(__file__).resolve().parent
R = D.parents[2]
CONTRAT = "brain.scriptone/1"
SEVERITES = ("CRITIQUE", "GRAVE", "MOYEN", "DETAIL")
REGIONS = ("MEM", "ENT", "PRO", "AUM", "AUL", "AUF", "VIS", "SEC", "LIV", "ECO", "BUS", "ALP", "BET")
TYPES = ("medical", "langue", "forme", "memoire", "doleance", "jetons")      # types de signaux (couleurs du schéma 3D)
CHAMPS = ("id", "region", "scriptone", "code", "fichier", "ancre", "severite", "constat", "correction_prescrite", "executant", "preuve")
RX_CODE = re.compile(r"^[A-Z]{1,2}[0-9]$")
CPL = 110            # caractères par ligne affichée (Atkinson 16 px, colonne de 980 px) ; calibré par captures.js (mesure réelle)
DONNEES = ("budgets.json", "contrat.schema.json", "synapses.json", "verbes.json", "memoire_fautes.json", "evenements.schema.json")


def sha(t):
    return hashlib.sha256(t.encode("utf-8", "surrogatepass") if isinstance(t, str) else t).hexdigest()


def rel(p):
    """Chemin relatif au dossier des scriptones (séparateur /), sinon nom du fichier."""
    p = Path(p).resolve()
    try: return p.relative_to(D).as_posix()
    except ValueError: return p.name


# ───────────────────────── lecture et écriture robustes ─────────────────────────
def lire(f):
    """Lit un fichier quel que soit son encodage : (texte, encodage). BOM retiré ; UTF-16 reconnu ; sinon UTF-8 strict, puis cp1252."""
    b = Path(f).read_bytes()
    if b[:3] == b"\xef\xbb\xbf": b = b[3:]
    if b[:2] in (b"\xff\xfe", b"\xfe\xff"): return b.decode("utf-16", errors="replace"), "utf-16"
    if b"\x00" in b[:4000] and len(b) > 1 and b.count(b"\x00") > len(b) // 4:
        return b.decode("utf-16-le", errors="replace"), "utf-16-le"
    try: return b.decode("utf-8"), "utf-8"
    except UnicodeDecodeError: return b.decode("cp1252", errors="replace"), "cp1252"


class Occupe(Exception):
    """Un autre écrivain tient le fichier : refus (code 4), jamais d'écriture concurrente."""


@contextlib.contextmanager
def verrou(f, age_max=300):
    """Verrou exclusif d'écriture (O_EXCL) : un seul écrivain par fichier ; un verrou orphelin de plus de age_max s est repris."""
    v = Path(str(f) + ".brainlock")
    for _ in range(2):
        try:
            fd = os.open(v, os.O_CREAT | os.O_EXCL | os.O_WRONLY); os.write(fd, f"{os.getpid()} {time.time():.0f}".encode()); os.close(fd); break
        except FileExistsError:
            try: age = time.time() - v.stat().st_mtime
            except OSError: continue
            if age > age_max: v.unlink(missing_ok=True); continue
            raise Occupe(f"fichier tenu par un autre écrivain : {v.name}")
    else: raise Occupe(f"verrou impossible : {v.name}")
    try: yield
    finally: v.unlink(missing_ok=True)


def ecrire_atomique(f, texte):
    """Écrit dans un fichier temporaire puis le renomme : un lecteur ne voit jamais un fichier à moitié écrit."""
    f = Path(f); tmp = f.with_name(f".{f.name}.{os.getpid()}.tmp")
    tmp.write_text(texte, encoding="utf-8"); os.replace(tmp, f)


def ajouter_ligne(f, ligne):
    """Ajout append-only sous flock (concurrence de 16 processus sans ligne entrelacée)."""
    f = Path(f); f.parent.mkdir(parents=True, exist_ok=True)
    with open(f, "a", encoding="utf-8") as fh:
        try:
            import fcntl; fcntl.flock(fh, fcntl.LOCK_EX)
        except (ImportError, OSError): pass
        fh.write(ligne.rstrip("\n") + "\n"); fh.flush()


# ───────────────────────── empreintes ─────────────────────────
def fichiers_empreintes():
    py = sorted(p.relative_to(D).as_posix() for p in D.rglob("*.py") if "__pycache__" not in p.parts and not p.name.startswith("test_"))
    return py + [n for n in DONNEES if (D / n).exists()]


def verifier_empreintes(nom=None):
    """Vérifie SHA256SUMS ; renvoie la liste des fichiers altérés (vide si tout est intact ou si la liste n'existe pas)."""
    f = D / "SHA256SUMS"
    if not f.exists(): return []
    alt = []
    for l in f.read_text(encoding="utf-8", errors="replace").splitlines():
        if not l.strip(): continue
        try: h, n = l.split(None, 1)
        except ValueError: alt.append(f"ligne illisible : {l[:40]}"); continue
        n = n.strip(); p = D / n
        if nom and n != nom: continue
        if not p.exists() or sha(p.read_bytes()) != h: alt.append(n)
    return alt


def ecrire_empreintes():
    noms = fichiers_empreintes()
    (D / "SHA256SUMS").write_text("".join(f"{sha((D / n).read_bytes())}  {n}\n" for n in noms))
    return noms


# ───────────────────────── doléances ─────────────────────────
def doleance(mod, code, fichier, ancre, severite, constat, correction, executant="agent", preuve=""):
    assert severite in SEVERITES and executant in ("script", "agent") and RX_CODE.match(code), (code, severite, executant)
    d = dict(region=mod.REGION, scriptone=mod.ID, code=code, fichier=fichier, ancre=ancre or "#haut", severite=severite,
             constat=constat, correction_prescrite=correction or "relire", executant=executant, preuve=(preuve or "")[:400])
    d["id"] = hashlib.sha1(f"{mod.ID}|{code}|{ancre}|{constat}".encode("utf-8", "surrogatepass")).hexdigest()[:12]
    return {k: d[k] for k in CHAMPS}


def valider(sortie):
    """Validation du contrat de sortie, sans jsonschema (zéro dépendance). Renvoie la liste des erreurs."""
    err = []
    if not isinstance(sortie, dict): return ["sortie non objet"]
    for k in ("contrat", "scriptone", "version", "region", "sha256_script", "sha256_entree", "sha256_sortie", "dry_run", "modifie", "mesures", "doleances"):
        if k not in sortie: err.append(f"champ absent : {k}")
    if sortie.get("contrat") != CONTRAT: err.append("contrat inconnu")
    if sortie.get("region") not in REGIONS: err.append(f"région inconnue : {sortie.get('region')}")
    for k in ("sha256_script", "sha256_entree", "sha256_sortie"):
        if not re.fullmatch(r"[0-9a-f]{64}", str(sortie.get(k, ""))): err.append(f"{k} invalide")
    if not isinstance(sortie.get("mesures"), dict): err.append("mesures non objet")
    if not isinstance(sortie.get("doleances"), list): return err + ["doleances non liste"]
    for i, d in enumerate(sortie.get("doleances", [])):
        if not isinstance(d, dict) or set(d) != set(CHAMPS): err.append(f"doléance {i} : champs {sorted(set(CHAMPS) ^ set(d or {}))}"); continue
        if d["severite"] not in SEVERITES or d["executant"] not in ("script", "agent") or not d["correction_prescrite"] or not d["ancre"] \
                or not RX_CODE.match(str(d["code"])) or d["region"] not in REGIONS or not re.fullmatch(r"[0-9a-f]{12}", str(d["id"])):
            err.append(f"doléance {i} : valeur invalide ({d.get('code')})")
    return err


# ───────────────────────── lecture du HTML (commun) ─────────────────────────
RX_STYLE = re.compile(r"(?is)<(script|style)\b[^>]*>.*?</\1>")
RX_FENETRE = re.compile(r'(?s)<span class="(?:df|dxc)">.*?</span></span>|<abbr[^>]*>|</abbr>')


def masque(t, rx):
    """Remplace les zones par des espaces de même longueur : les positions restent valables."""
    return rx.sub(lambda m: " " * len(m.group(0)), t)


@functools.lru_cache(maxsize=32)
def bornes_cours(t):
    """(début, fin) du corps du cours : de <main>/monographie aux sources ; l'onglet Rappel mémoire (#rm) est exclu."""
    m = re.search(r'<section class="monograph"|<main[ >]', t); a = m.start() if m else (t.find("<body") + 1 if "<body" in t else 0)
    f = re.search(r'(?is)<details class="refs"|<h2[^>]*>\s*Sources|<div id="rappel"|<section id="rm"|<div id="rm"', t[a:])
    return a, a + f.start() if f else len(t)


def texte(h):
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", h))).strip()


def texte_visible(h):
    """Texte affiché sans clic : fenêtres (.df, .dxc) et exposants de source retirés, sigles déshabillés."""
    h = re.sub(r'(?is)<sup class="r">.*?</sup>', "", h)
    h = re.sub(r'(?s)<span class="(?:df|dxc)">(?:(?!<span class="(?:df|dxc)">).)*?</span>', " ", h)
    h = re.sub(r'(?s)<span class="(?:df|dxc)">.*?</span></span>', " ", h)
    return texte(h)


def ligne(t, pos):
    return t.count("\n", 0, pos) + 1


def ancre(t, pos, extrait=""):
    """Ancre exploitable sans réinterprétation : id le plus proche avant la position + ligne + extrait."""
    ids = list(re.finditer(r'\sid="([^"]+)"', t[:pos]))
    i = next((x.group(1) for x in reversed(ids) if not re.fullmatch(r"dx\d+|sb-\d+|src-\d+|med-\w+", x.group(1))), "")
    e = re.sub(r"\s+", " ", extrait).strip()[:70]
    zone = "CSS " if t.rfind("<style", 0, pos) > t.rfind("</style>", 0, pos) else ""
    return f"{zone}#{i or 'haut'} · l.{ligne(t, pos)}" + (f" · « {e} »" if e else "")


def sections(t):
    """{n° de point: (début, fin)} d'après les titres <h3> « N. … » (copie : le cache n'est jamais modifié par l'appelant)."""
    return dict(_sections(t))


@functools.lru_cache(maxsize=32)
def _sections(t):
    a, f = bornes_cours(t)
    ms = [m for m in re.finditer(r"<h3[^>]*>\s*(?:<strong>)?\s*(\d{1,2})\.\s", t) if a <= m.start() < f]
    out = {}
    for i, m in enumerate(ms):
        n = int(m.group(1))
        if 1 <= n <= 14: out.setdefault(n, (m.start(), ms[i + 1].start() if i + 1 < len(ms) else f))
    return tuple(out.items())


@functools.lru_cache(maxsize=32)
def zones_fenetres(t):
    """Intervalles des fenêtres et bandes (.df, .dxc, div.mb, div.sb) : contenu caché, jamais lu comme texte du cours."""
    out = []; pile = []
    for m in re.finditer(r"(?is)<(/?)(span|div)\b([^>]*)>", t):
        if not m.group(1):
            ouvre = bool(re.search(r'class="(?:df|dxc|mb|sb)"', m.group(3)))
            pile.append((m.group(2).lower(), m.start() if ouvre else None))
        else:
            while pile:
                tag, debut = pile.pop()
                if tag == m.group(2).lower():
                    if debut is not None and not any(d is not None for _, d in pile): out.append((debut, m.end()))
                    break
    return tuple(out)


def dans_fenetre(t, pos):
    return any(a <= pos < b for a, b in zones_fenetres(t))


def blocs(t, a=None, f=None, tags=("p", "li")):
    """Paragraphes et items de liste hors fenêtres et bandes : [(début, fin, html_interne)]."""
    a = bornes_cours(t)[0] if a is None else a; f = bornes_cours(t)[1] if f is None else f
    seg = masque(t[a:f], RX_STYLE); out = []; Z = zones_fenetres(t)
    rx = re.compile(r"(?is)<(%s)\b[^>]*>(.*?)</\1>" % "|".join(tags))
    for m in rx.finditer(seg):
        if any(za <= a + m.start() < zb for za, zb in Z): continue
        out.append((a + m.start(), a + m.end(), t[a + m.start(2):a + m.end(2)]))
    return out


ABREV = r"(?:p\. ex|env|cf|vs|etc|n°|cm|mm|mg|kg|min|max|éd|vol|art|al|Dr|Pr|St)\."
def phrases(txt):
    """Découpe en phrases (décimales, abréviations et sigles protégés)."""
    s = re.sub(ABREV, lambda m: m.group(0).replace(".", "․"), txt)
    ps = re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-ÖØ-Ý«(\d])", s)
    return [p.replace("․", ".").strip() for p in ps if len(p.split()) >= 2]


VIDES = set("le la les un une des de du d l à au aux en et ou où que qui quoi dont ce cet cette ces se sa son ses sur sous par pour dans avec sans "
            "est sont été être a ont avoir plus moins très ne pas n s y il elle ils elles on leur leurs lui nous vous je tu même aussi "
            "mais donc or ni car si comme entre vers chez tout tous toute toutes cas fait faire peut doit".split())
def jetons(p):
    """Jetons de contenu normalisés (racine de 6 lettres) : base des comparaisons de redite, sans spaCy."""
    return {w[:6] for w in re.findall(r"[a-zà-ÿ0-9]+(?:[,.]\d+)?", p.lower().replace("’", "'")) if w not in VIDES and (len(w) > 2 or w.isdigit())}


def estime_jetons(t):
    """Estimation des jetons (≈ 4 caractères par jeton pour le français en UTF-8 ; méthode constante pour les comparaisons avant/après)."""
    return round(len(t) / 4)


def pose_style(t, ident, bloc):
    """Pose <style id="ident"> : remplacé sur place s'il existe (ordre stable, idempotent), sinon inséré avant </head>."""
    rx = re.compile(r'(?is)<style id="%s">.*?</style>' % re.escape(ident))
    if rx.search(t): return rx.sub(lambda m: bloc, t, count=1)
    return t.replace("</head>", bloc + "</head>", 1) if "</head>" in t else bloc + t


# ───────────────────────── exécution commune (CLI et contrat) ─────────────────────────
def journal(ev):
    try: ajouter_ligne(R / ".cache/brain/journal.jsonl", json.dumps(ev, ensure_ascii=False))
    except OSError: pass


def evenement(ev, chemin=None):
    """Événement typé du journal de circulation (schéma evenements.schema.json ; lu par BRAIN_3D.html)."""
    ev = dict(v=1, ts=ev.get("ts") or time.strftime("%Y-%m-%dT%H:%M:%S"), **{k: v for k, v in ev.items() if k not in ("v", "ts")})
    if ev.get("type") not in TYPES: raise ValueError(f"type de signal inconnu : {ev.get('type')}")
    ajouter_ligne(chemin or R / ".cache/brain/evenements.jsonl", json.dumps(ev, ensure_ascii=False))
    return ev


def _deps(mod):
    return [rel(mod.__file__), "bus.py"] + list(getattr(mod, "DEPEND", []))


def panne(mod, nom, e):
    """Une exception devient une doléance Z0 : la panne est annoncée au bus et au disjoncteur, jamais avalée."""
    return doleance(mod, "Z0", nom, "#haut", "GRAVE", f"panne du scriptone {mod.ID} : {type(e).__name__} : {str(e)[:160]}",
                    "relire à la main la zone de ce scriptone ; le disjoncteur ré-route vers son jumeau et le gardien signale la panne", "agent", repr(e)[:300])


def executer(mod, fichier, html=None, appliquer=False, options=None, ecrire=True):
    """Exécute un scriptone selon le contrat ; renvoie la sortie (dict validé). N'écrit le fichier que si appliquer=True (verrou + écriture atomique)."""
    options = options or {}
    src = Path(mod.__file__).read_bytes()
    alt = [x for n in _deps(mod) for x in verifier_empreintes(n)]
    if alt: raise SystemExit(f"ALTÉRATION DÉTECTÉE : {', '.join(alt)} ne correspond plus à SHA256SUMS. STOP.")
    enc = "texte"
    if html is not None: t = html
    else: t, enc = lire(fichier)
    nom = Path(fichier).name if fichier else "<entrée>"
    t0 = time.perf_counter(); err = None
    try:
        neuf = mod.corriger(t, options) if hasattr(mod, "corriger") else t
        D_, M_ = mod.analyser(t, nom, options)
        if appliquer and neuf != t:     # après correction : seules restent les doléances que le script ne sait pas résoudre
            D_, M_2 = mod.analyser(neuf, nom, options); M_ = dict(M_, apres=M_2)
    except (KeyboardInterrupt, SystemExit): raise
    except BaseException as e:      # MemoryError, RecursionError, erreurs de logique : panne annoncée
        err = e; neuf = t; D_ = [panne(mod, nom, e)]; M_ = {}
    M_ = dict(M_, duree_ms=round(1000 * (time.perf_counter() - t0), 1))
    s = dict(contrat=CONTRAT, scriptone=mod.ID, version=mod.VERSION, region=mod.REGION, sha256_script=sha(src),
             sha256_entree=sha(t), sha256_sortie=sha(neuf if appliquer else t), dry_run=not appliquer,
             modifie=bool(appliquer and neuf != t), corrigeable=neuf != t, mesures=M_, doleances=D_, encodage=enc)
    if err is not None: s["panne"] = dict(type=type(err).__name__, message=str(err)[:300])
    if appliquer and neuf != t and fichier and ecrire:
        with verrou(fichier):
            if sha(lire(fichier)[0]) != s["sha256_entree"]: raise Occupe("fichier modifié pendant l'analyse : relancer")
            ecrire_atomique(fichier, neuf)
    if ecrire:
        journal(dict(ts=time.strftime("%Y-%m-%dT%H:%M:%S"), scriptone=mod.ID, fichier=nom, entree=s["sha256_entree"][:16],
                     sortie=s["sha256_sortie"][:16], doleances=len(D_), modifie=s["modifie"], panne=bool(err)))
    return s


def resume(s, n=12):
    """Sortie compacte (économie de jetons) : une ligne par doléance, les plus graves d'abord."""
    o = {k: i for i, k in enumerate(SEVERITES)}
    L = sorted(s["doleances"], key=lambda d: (o[d["severite"]], d["code"]))
    tete = f"[{s['scriptone']}] {len(L)} doléance(s){' · corrigeable par script (--appliquer)' if s.get('corrigeable') else ''}{' · MODIFIÉ' if s['modifie'] else ''}{' · PANNE' if s.get('panne') else ''}"
    lignes = [f"- {d['severite']} {d['code']} {d['ancre']} : {d['constat']} → {d['correction_prescrite']}" for d in L[:n]]
    if len(L) > n: lignes.append(f"- … {len(L) - n} de plus (--json pour tout)")
    return "\n".join([tete] + lignes)


def cli(mod):
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print((mod.__doc__ or "") + "\nUsage : <scriptone>.py <fichier> [--appliquer] [--json] | --contrat - (JSON sur stdin)"); return 0
    try:
        if a[0] == "--contrat":
            c = json.load(sys.stdin if len(a) < 2 or a[1] == "-" else open(a[1], encoding="utf-8"))
            if not isinstance(c, dict) or not (c.get("fichier") or "html" in c): raise ValueError("contrat d'entrée : 'fichier' ou 'html' requis")
            s = executer(mod, c.get("fichier", ""), c.get("html"), bool(c.get("appliquer")), c.get("options") if isinstance(c.get("options"), dict) else {},
                         ecrire=bool(c.get("fichier")) and "html" not in c)
            print(json.dumps(s, ensure_ascii=False, indent=1)); return 0
        s = executer(mod, a[0], appliquer="--appliquer" in a)
    except SystemExit as e:
        print(e); return 3
    except Occupe as e:
        print(f"OCCUPÉ : {e}"); return 4
    except (OSError, ValueError, KeyError, IndexError, json.JSONDecodeError) as e:
        print(f"ERREUR D'ENTRÉE : {type(e).__name__} : {str(e)[:200]}"); return 2
    print(json.dumps(s, ensure_ascii=False, indent=1) if "--json" in a else resume(s))
    return 1 if any(d["severite"] in ("CRITIQUE", "GRAVE") for d in s["doleances"]) else 0
