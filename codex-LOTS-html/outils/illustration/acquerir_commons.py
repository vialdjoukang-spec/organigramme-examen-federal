#!/usr/bin/env python3
"""Acquérir des originaux Commons dont la notice a été réellement lue.

Par défaut : contrôle local, sans requête. --acquerir : téléchargement si permis.
Aucune annotation, légende définitive ou intégration n'est générée ici.
"""
import argparse
import hashlib
import io
import json
import re
import subprocess
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

from PIL import Image

BASE = Path(__file__).resolve().parents[2]
POLITIQUE = Path('/etc/codex/network-policy.json')
MAX_OCTETS = 20 * 1024 * 1024
FORMATS = {'JPEG': 'image/jpeg', 'PNG': 'image/png', 'WEBP': 'image/webp'}


def maintenant():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def chemin(p):
    p = Path(p).resolve()
    if not p.is_relative_to(BASE):
        raise ValueError('Chemin hors codex-LOTS-html')
    return p


def verifier_notice(s):
    for k in ('id', 'auteur', 'licence', 'licence_url', 'source_url',
              'revision_url', 'original_url', 'acces_le', 'passages_lus', 'destination'):
        if not s.get(k):
            raise ValueError('Notice incomplète : ' + k)
    if s.get('decision') != 'retenu_sous_reserve_visuelle':
        raise ValueError('Candidat non retenu')
    if not re.fullmatch(r'[a-z][a-z0-9-]*', s['id']):
        raise ValueError('Identifiant invalide')
    lic = s['licence']
    if not re.fullmatch(r'CC BY(?:-SA)? (?:[1234]\.0|2\.5)|CC0 1\.0|Domaine public', lic):
        raise ValueError('Licence refusée')
    path = {'Domaine public': '/publicdomain/mark/1.0/', 'CC0 1.0': '/publicdomain/zero/1.0/'}.get(lic)
    if path is None:
        kind, version = lic.rsplit(' ', 1)
        path = '/licenses/' + kind.replace('CC ', '').lower() + '/' + version + '/'
    if s['licence_url'].rstrip('/') != ('https://creativecommons.org' + path).rstrip('/'):
        raise ValueError('URL de licence incohérente')
    for key, host in [('source_url', 'commons.wikimedia.org'),
                      ('revision_url', 'commons.wikimedia.org'),
                      ('original_url', 'upload.wikimedia.org')]:
        u = urlparse(s[key])
        if u.scheme != 'https' or u.hostname != host or u.username or u.password or u.port not in (None, 443):
            raise ValueError('URL de provenance refusée : ' + key)
    if not urlparse(s['original_url']).path.startswith('/wikipedia/commons/'):
        raise ValueError('Original Commons requis')
    if date.fromisoformat(s['acces_le']) > date.today():
        raise ValueError('Date de lecture future')
    dims = s.get('dimensions_annoncees', [])
    if len(dims) != 2 or any(type(n) is not int or n <= 0 for n in dims):
        raise ValueError('Dimensions annoncées manquantes')
    if s.get('mime_annonce') not in FORMATS.values():
        raise ValueError('Format non pris en charge')
    return chemin(BASE / s['destination'])


def politique_permet(url, politique):
    p = politique.get('http_network_policy', {})
    if p.get('type') == 'unrestricted':
        return True
    if p.get('type') != 'restricted':
        return False
    # Correspondance exacte volontaire ; aucune approximation de domaine.
    return urlparse(url).hostname in {x.get('host') for x in p.get('egress_rules', [])}


class SansRedirection(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError('Redirection refusée ; relire la source et la politique avant acquisition')


def verifier_octets(raw, s, mime):
    if not raw or len(raw) > MAX_OCTETS:
        raise ValueError('Original vide ou supérieur à 20 Mio')
    if mime != s['mime_annonce']:
        raise ValueError('Type HTTP inattendu ; aucune page HTML acceptée comme image')
    with Image.open(io.BytesIO(raw)) as im:
        if FORMATS.get(im.format) != mime or list(im.size) != s['dimensions_annoncees']:
            raise ValueError('Format ou dimensions différents de la notice lue')
        if im.width * im.height > 50_000_000 or getattr(im, 'n_frames', 1) != 1:
            raise ValueError('Image trop grande ou animée : traitement distinct requis')
        im.verify()
    return hashlib.sha256(raw).hexdigest()


def traiter(s, politique, acquerir=False, ouvrir=None):
    dest = verifier_notice(s)
    r = {'id': s['id'], 'notice_conforme': True, 'acquis': False,
         'inspection_visuelle': False, 'integre': False}
    if not politique_permet(s['original_url'], politique):
        return dict(r, statut='bloque_politique_reseau', requete_envoyee=False)
    if not acquerir:
        return dict(r, statut='controle_local_seulement', requete_envoyee=False)
    preuve = dest.with_name(dest.name + '.source.json')
    if dest.exists() or preuve.exists():
        raise ValueError('Destination déjà présente ; préserver et examiner les fichiers existants')
    if ouvrir is None:
        ouvrir = urllib.request.build_opener(SansRedirection()).open
    req = urllib.request.Request(s['original_url'], headers={'User-Agent': 'Vial-LOTS-Illustrations/1.0'})
    # Proxy et CA hérités conservés ; aucune connexion hors politique ni miroir.
    with ouvrir(req, timeout=25) as response:
        if response.status != 200:
            raise ValueError('Réponse HTTP non 200')
        mime = response.headers.get_content_type()
        raw = response.read(MAX_OCTETS + 1)
    sha = verifier_octets(raw, s, mime)
    provenance = {'acquis_le': maintenant(), 'notice': s,
                  'sha256_original': sha, 'octets': len(raw),
                  'inspection_visuelle': False, 'annotations': None,
                  'statut': 'original acquis ; inspection et annotation obligatoires'}
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open('xb') as f:
        f.write(raw)
    try:
        with preuve.open('x', encoding='utf-8') as f:
            f.write(json.dumps(provenance, ensure_ascii=False, indent=2) + '\n')
    except Exception:
        dest.unlink()  # uniquement le fichier créé par cette invocation
        raise
    return dict(r, acquis=True, statut='acquis_non_inspecte', requete_envoyee=True,
                sha256_original=sha, octets=len(raw), destination=str(dest.relative_to(BASE)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('registre')
    parser.add_argument('--acquerir', action='store_true')
    args = parser.parse_args()
    registre = chemin(args.registre)
    if not (BASE / '_cache/production.lock').exists():
        raise SystemExit('Acquérir le verrou officiel avant de produire le rapport')
    branch = subprocess.check_output(['git', 'branch', '--show-current'], cwd=BASE, text=True).strip()
    if branch != 'codex/lots':
        raise SystemExit('Branche non autorisée')
    doc = json.loads(registre.read_text())
    lot = doc['lot']
    res = json.loads((BASE.parent / 'IA_RESERVATIONS.json').read_text())['codex']
    if not res['plage'][0] <= int(lot.removeprefix('LOT_')) <= res['plage'][1]:
        raise SystemExit('Lot hors réservation fraîche')
    if branch != res['branche']:
        raise SystemExit('Branche différente de la réservation fraîche')
    for cmd in [('pret', 'codex'), ('verifier', 'codex', lot)]:
        subprocess.run(['python3', '-B', str(BASE / 'registre_ia.py'), *cmd], check=True)
    politique = json.loads(POLITIQUE.read_text())
    retenus = [s for s in doc['candidats'] if s['decision'] == 'retenu_sous_reserve_visuelle']
    if not retenus or len({s['id'] for s in retenus}) != len(retenus):
        raise SystemExit('Sélection vide ou identifiants dupliqués')
    results = []
    for s in doc['candidats']:
        if s['decision'] != 'retenu_sous_reserve_visuelle':
            continue
        try:
            dest = verifier_notice(s)
            if not dest.is_relative_to(BASE / lot / 'illustrations'):
                raise ValueError('Destination hors illustrations du lot contrôlé')
            results.append(traiter(s, politique, args.acquerir))
        except Exception as exc:
            results.append({'id': s.get('id'), 'statut': 'echec', 'erreur': str(exc), 'acquis': False})
    rapport = {'date': maintenant(), 'lot': lot, 'mode': 'acquisition' if args.acquerir else 'controle_local',
               'resultats': results, 'portee': 'Aucune inspection visuelle ni validation médicale automatique.'}
    chemin(registre.parent / 'CONTROLE_ACQUISITION.json').write_text(json.dumps(rapport, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(rapport, ensure_ascii=False))
    return int(any(r['statut'] in ('echec', 'bloque_politique_reseau') for r in results))


if __name__ == '__main__':
    raise SystemExit(main())
