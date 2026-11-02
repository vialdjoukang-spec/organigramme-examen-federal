#!/usr/bin/env python3
"""Contrôles ponctuels : cache strict, extraits ciblés et activité documentée."""
from __future__ import annotations
import argparse
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import types

D = Path(__file__).resolve().parent
BASE = D.parent
VALIDATEUR = BASE.parent / 'harnais/controle_lot.py'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def serialiser(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':'))


def charger(validateur):
    # Compilation directe : aucune réutilisation de bytecode périmé, aucun .pyc écrit.
    module = types.ModuleType('controle_lot_cache_strict')
    module.__file__ = str(validateur)
    exec(compile(validateur.read_bytes(), str(validateur), 'exec'), module.__dict__)
    # Le cache historique ne tient pas compte de l'empreinte du code : le neutraliser.
    module.cache_lire = lambda key: None
    module.cache_ecrire = lambda key, value: None
    return module


def empreinte(lot, validateur, sans_nom=False, dependances=()):
    fichiers = set(lot.glob('*.html')) | {lot / 'LISTE_DX_CANONIQUE.md', validateur, Path(__file__)}
    # Tous les modules voisins sont inclus, même non importés ; les données externes
    # d'un futur validateur doivent être déclarées via --dependance.
    fichiers.update(validateur.parent.rglob('*.py'))
    fichiers.update(Path(p).resolve() for p in dependances)
    return {
        'schema': 1, 'lot': str(lot), 'sans_nom': sans_nom,
        'python': sys.version, 'executable': sha(Path(sys.executable).read_bytes()),
        'fichiers': {str(p.resolve()): sha(p.read_bytes()) if p.exists() else None
                     for p in sorted(fichiers)},
    }


def verifier(lot, cache=None, *, validateur=VALIDATEUR, sans_nom=False, dependances=()):
    lot, validateur = Path(lot).resolve(), Path(validateur).resolve()
    if not lot.is_dir():
        raise ValueError(f'Dossier LOT absent : {lot}')
    cache = Path(cache) if cache is not None else BASE / '.cache/harnais'
    initial = empreinte(lot, validateur, sans_nom, dependances)
    key = sha(serialiser(initial).encode())
    cible = cache / (key + '.json')
    try:
        stored = json.loads(cible.read_text(encoding='utf-8'))
        payload = stored['resultat']
        if (stored['empreinte'] == initial and
                stored['sha256_resultat'] == sha(serialiser(payload).encode()) and
                isinstance(payload['fichiers'], list) and
                isinstance(payload['critiques_lot'], list)):
            return {'cache': 'reutilise', 'cle': key, 'resultat': payload}
    except (OSError, ValueError, KeyError, TypeError):
        pass
    resultat = charger(validateur).verifier(lot, sans_nom)
    if empreinte(lot, validateur, sans_nom, dependances) != initial:
        raise RuntimeError('Entrées modifiées pendant le contrôle : relancer, aucun cache enregistré.')
    cache.mkdir(parents=True, exist_ok=True)
    record = {'empreinte': initial, 'resultat': resultat,
              'sha256_resultat': sha(serialiser(resultat).encode()),
              'date': datetime.now(timezone.utc).isoformat()}
    # Remplacement atomique : deux lecteurs ne voient jamais un JSON partiel.
    fd, tmp = tempfile.mkstemp(prefix='.controle-', dir=cache)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as stream:
            stream.write(serialiser(record) + '\n')
        os.replace(tmp, cible)
    finally:
        Path(tmp).unlink(missing_ok=True)
    return {'cache': 'calcule', 'cle': key, 'resultat': resultat}


def extraire(fichier, points, brut_html=False, *, validateur=VALIDATEUR):
    if not points or any(n not in range(1, 15) for n in points):
        raise ValueError('Points attendus : entiers de 1 à 14.')
    # Le V8 place les développements dans des popovers hors des sections.
    from lxml import html as lh
    arbre = lh.document_fromstring(Path(fichier).read_bytes())
    sections = []
    for n in points:
        matches = arbre.xpath('//section[h2[@id="a-p'+str(n)+'" or substring(@id, string-length(@id)-'+str(len(str(n))+1)+')="-p'+str(n)+'"]]')
        sections.extend(matches)
    if sections:
        found = {int(x.xpath('./h2')[0].get('id').rsplit('-p', 1)[1]) for x in sections}
        if found != set(points):
            raise ValueError('Extraction V8 incomplète : parties absentes.')
        blocs = list(sections)
        vus = set()
        for bloc in blocs:
            for ident in bloc.xpath('.//button[@popovertargetaction!="hide" or not(@popovertargetaction)]/@popovertarget'):
                if ident in vus:
                    continue
                vus.add(ident)
                fenetres = arbre.xpath('//*[@id=$ident and @popover]', ident=ident)
                if len(fenetres) != 1:
                    raise ValueError('Fenêtre V8 absente ou ambiguë : '+ident)
                blocs.append(fenetres[0])
        if brut_html:
            return '\n'.join(lh.tostring(x, encoding='unicode') for x in blocs)
        return '\n\n'.join(' '.join(x.text_content().split()) for x in blocs)
    texte = charger(Path(validateur)).extraire(Path(fichier), points, brut_html)
    if not texte:
        raise ValueError('Aucun point demandé retrouvé ; extraction impossible.')
    return texte


def activite(sources=None):
    """Lecture seule ; un événement consigné ne prouve pas un agent en cours."""
    if sources is None:
        sources = sorted(set(D.glob('*.jsonl')) | set(BASE.glob('*.jsonl')))
    agents = defaultdict(list)
    erreurs, lus = [], []
    for source in sources:
        p = Path(source)
        try:
            texte = p.read_text(encoding='utf-8')
            lignes = texte.splitlines() if p.suffix == '.jsonl' else [texte]
        except OSError as exc:
            erreurs.append({'source': str(p), 'erreur': str(exc)})
            continue
        lus.append(str(p))
        for n, ligne in enumerate(lignes, 1):
            if not ligne.strip():
                continue
            try:
                objet = json.loads(ligne)
                rows = objet if isinstance(objet, list) else [objet]
                for row in rows:
                    if not isinstance(row, dict):
                        raise ValueError('Événement attendu sous forme objet JSON.')
                    agent = row.get('agent') or row.get('agent_id') or row.get('producteur') or 'non_attribue'
                    agents[str(agent)].append({'source': str(p), 'ligne': n,
                        **{k: row[k] for k in ('date', 'horodatage', 'tache', 'poste', 'modele',
                                             'lot', 'fichier', 'code_sortie', 'statut') if k in row}})
            except (ValueError, TypeError) as exc:
                erreurs.append({'source': str(p), 'ligne': n, 'erreur': str(exc)})
    return {'sources_lues': lus, 'agents': {k: {'evenements': len(v), 'preuves': v}
            for k, v in sorted(agents.items())}, 'erreurs': erreurs,
            'portee': 'Activité déclarée uniquement ; présence actuelle, jetons, coûts et validation médicale non déduits.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='commande', required=True)
    v = sub.add_parser('verifier')
    v.add_argument('lot')
    v.add_argument('--sans-nom', action='store_true')
    v.add_argument('--dependance', action='append', default=[])
    e = sub.add_parser('extraire')
    e.add_argument('fichier')
    e.add_argument('--points', required=True)
    e.add_argument('--html', action='store_true')
    a = sub.add_parser('activite')
    a.add_argument('--source', action='append')
    args = parser.parse_args()
    try:
        if args.commande == 'extraire':
            print(extraire(args.fichier, [int(x) for x in args.points.split(',')], args.html))
            return 0
        if args.commande == 'activite':
            rapport = activite(args.source)
            code = int(bool(rapport['erreurs']))
        else:
            rapport = verifier(args.lot, sans_nom=args.sans_nom, dependances=args.dependance)
            r = rapport['resultat']
            code = int(bool(r['critiques_lot'] or any(f['critiques'] for f in r['fichiers'])))
        print(json.dumps(rapport, ensure_ascii=False, indent=2))
        return code
    except (OSError, ValueError, RuntimeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
