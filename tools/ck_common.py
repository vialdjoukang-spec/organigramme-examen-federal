"""Atlas et Janus · fonctions communes aux outils CK (compilateur, Lyncée, audit de niveau 1).

Chaque outil accepte --racine DIR (racine du dépôt, par défaut celle de ce script) pour
pouvoir tourner sur un jeu d'essai temporaire dans les tests.
"""
import datetime, json, os, re, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Fichiers de données CK, dans l'ordre de compilation. sig = entrées de glo de type « signe ».
FICHIERS = ('src', 'glo', 'syn', 'hyp', 'nc', 'loc', 'doses_ch')
# Champs qui portent des identifiants, des codes ou des métadonnées, jamais du texte affiché.
CHAMPS_NON_TEXTE = {'id', 'type', 'module', 'statut', 'lu_le', 'lu_par', 'url', 'src', 'rang', 'site',
                    'dose_ref', 'valide_par_vial', 'bloquant', 'vues', 'tour', 'composantes', 'voir',
                    'signes', 'orientation_hyp', 'syn', 'hyp', 'A', 'B', 'pays', 'licence', 'flexions_auto',
                    'aips_rubrique', 'org', 'loc',
                    # Pharmakon : extraits AIPS cités mot pour mot et métadonnées de la source, jamais rédigés par nous.
                    'aips_extrait', 'aips_version', 'aips_publie', 'url_texte', 'titulaire', 'methode'}
# Champs rédigés en phrases complètes : G6 exige une forme verbale conjuguée par phrase.
CHAMPS_PROSE = {'def', 'orientation', 'pourquoi', 'precautions', 'alternative', 'confirmation',
                'objectif', 'mesures_generales', 'texte', 'deficit', 'comment',
                'mecanisme', 'principe', 'pourquoi_ce_choix', 'limites'}


def today():
    """Date du jour à Zurich (le dépôt suit Europe/Zurich), au format ISO."""
    try:
        from zoneinfo import ZoneInfo
        return datetime.datetime.now(ZoneInfo('Europe/Zurich')).date().isoformat()
    except Exception:  # pragma: no cover
        return datetime.date.today().isoformat()


def norm(t):
    """Minuscules sans accents, espaces réduits (comparaison des termes)."""
    t = unicodedata.normalize('NFKD', t.replace('œ', 'oe').replace('Œ', 'OE').replace('’', "'"))
    t = ''.join(c for c in t if not unicodedata.combining(c)).lower()
    return re.sub(r'\s+', ' ', t).strip()


def data_dir(root):
    return os.path.join(root, 'data', 'ck')


def load(root, name):
    p = os.path.join(data_dir(root), name + '.json')
    if not os.path.exists(p):
        return []
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def load_all(root):
    return {n: load(root, n) for n in FICHIERS}


def strings(obj, path=''):
    """Parcourt un objet JSON et rend (chemin, champ, texte) pour chaque chaîne de texte affiché."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in CHAMPS_NON_TEXTE:
                continue
            yield from _strings_field(v, f'{path}.{k}' if path else k, k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from strings(v, f'{path}[{i}]')


def _strings_field(v, path, field):
    if isinstance(v, str):
        yield path, field, v
    elif isinstance(v, list):
        for i, x in enumerate(v):
            if isinstance(x, str):
                yield f'{path}[{i}]', field, x
            else:
                yield from strings(x, f'{path}[{i}]')
    elif isinstance(v, dict):
        yield from strings(v, path)


_LINES = {}


def line_of(root, name, ident):
    """Numéro de ligne de « "id": "<ident>" » dans data/ck/<name>.json (0 si introuvable)."""
    p = os.path.join(data_dir(root), name + '.json')
    if p not in _LINES:
        try:
            _LINES[p] = open(p, encoding='utf-8').read().split('\n')
        except OSError:
            _LINES[p] = []
    needle = json.dumps(ident, ensure_ascii=False)
    for i, l in enumerate(_LINES[p], 1):
        if '"id"' in l and needle in l:
            return i
    return 0


def strip_tags(t):
    return re.sub(r'<[^>]+>', ' ', t)
