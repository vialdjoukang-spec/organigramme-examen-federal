"""Noyau : SQLite WAL, cache disque (SHA-256 + date), limitation de débit polie par hôte, journal."""
import os, sqlite3, hashlib, json, time, threading, urllib.parse, datetime
import requests
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SORTIE = os.environ.get('EPI_SORTIE') or RACINE   # dossier propre à chaque IA (NomIA__Completude_Epidemio)
CACHE = os.path.join(SORTIE, 'cache'); DB = os.path.join(SORTIE, 'out', 'reseau.sqlite')
UA = 'FedMed-Epidemio-CH/1.0 (recherche pedagogique; respect robots; contact via GitHub vialdjoukang-spec)'
_verrous, _dernier, _g = {}, {}, threading.Lock()
DELAI = 1.0  # s entre deux requêtes au même hôte
DELAI_HOTE = {'www.ebi.ac.uk': 0.25, 'www.wikidata.org': 0.5}   # API publiques prévues pour l'usage programmatique

def db():
    os.makedirs(os.path.dirname(DB), exist_ok=True)
    c = sqlite3.connect(DB, timeout=60, check_same_thread=False)
    c.execute('PRAGMA journal_mode=WAL'); c.execute('PRAGMA synchronous=NORMAL')
    c.executescript('''
    CREATE TABLE IF NOT EXISTS pages(url TEXT PRIMARY KEY, sha256 TEXT, date TEXT, statut INT, fichier TEXT, octets INT);
    CREATE TABLE IF NOT EXISTS indicateurs(cle TEXT PRIMARY KEY, source TEXT, libelle TEXT, valeur REAL, valeur_txt TEXT,
      unite TEXT, population TEXT, age_sexe TEXT, definition TEXT, mesure TEXT, annee TEXT, territoire TEXT,
      type_source TEXT, url TEXT, preuve TEXT, sha256 TEXT, phrase TEXT, hors_ch INT DEFAULT 0);
    CREATE TABLE IF NOT EXISTS resultats(lot INT, dx INT, diagnostic TEXT, json TEXT, date TEXT, PRIMARY KEY(lot,dx));
    CREATE TABLE IF NOT EXISTS checkpoint(etape TEXT PRIMARY KEY, fait TEXT, date TEXT);
    ''')
    return c

def maintenant(): return datetime.datetime.now().astimezone().isoformat(timespec='seconds')

def journal(msg):
    with open(os.path.join(SORTIE, 'JOURNAL.md'), 'a') as f: f.write(f'- {maintenant()} — {msg}\n')

def fetch(url, binaire=False, force=False):
    """GET poli avec cache disque. Retourne (contenu, sha256, date, fichier). Aucun contournement : un 403/429 est enregistré tel quel."""
    os.makedirs(CACHE, exist_ok=True)
    h = hashlib.sha1(url.encode()).hexdigest(); f = os.path.join(CACHE, h); meta = f + '.meta'
    if os.path.exists(meta) and not force:
        m = json.load(open(meta))
        if m['statut'] == 200:
            data = open(f, 'rb').read(); return (data if binaire else data.decode('utf-8', 'ignore')), m['sha256'], m['date'], f
    hote = urllib.parse.urlparse(url).netloc
    with _g: v = _verrous.setdefault(hote, threading.Lock())
    with v:
        attente = DELAI_HOTE.get(hote, DELAI) - (time.time() - _dernier.get(hote, 0))
        if attente > 0: time.sleep(attente)
        try:
            r = requests.get(url, headers={'User-Agent': UA}, timeout=60); st, data = r.status_code, r.content
        except Exception as e:
            st, data = -1, str(e).encode()
        _dernier[hote] = time.time()
    sha = hashlib.sha256(data).hexdigest(); d = maintenant()
    open(f, 'wb').write(data); json.dump({'url': url, 'statut': st, 'sha256': sha, 'date': d, 'octets': len(data)}, open(meta, 'w'))
    c = db(); c.execute('INSERT OR REPLACE INTO pages VALUES(?,?,?,?,?,?)', (url, sha, d, st, f, len(data))); c.commit(); c.close()
    if st != 200: return None, sha, d, f
    return (data if binaire else data.decode('utf-8', 'ignore')), sha, d, f
