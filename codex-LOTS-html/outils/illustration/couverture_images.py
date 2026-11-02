#!/usr/bin/env python3
"""Inventaire mécanique des points V8 (p9 par défaut), sans réseau ni validation médicale/des droits.

Usage: python3 -B couverture_images.py LOT --scope codex-LOTS-html --output rapport.json
Codes: 0 inventaire sans anomalie structurelle; 1 anomalie; 2 erreur d'exécution.
Une couverture nulle est un constat, pas une validation ni une erreur d'exécution.
"""
import argparse
import base64
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, unquote_to_bytes, urlsplit

from lxml import html


IMAGE_XPATH = './/*[local-name()="img" or local-name()="image"]'


def bounded(path, scope):
    path = path.resolve()
    if not path.is_relative_to(scope.resolve()):
        raise ValueError('Chemin hors périmètre autorisé')
    return path


def asset(reference, document, scope):
    result = {'reference': reference}
    if reference.startswith('data:'):
        result['reference'] = reference.split(',', 1)[0] + ',[contenu omis]'
        try:
            head, payload = reference.split(',', 1)
            if not head.lower().startswith('data:image/'):
                raise ValueError('MIME non image')
            raw = base64.b64decode(payload, validate=True) if head.endswith(';base64') else unquote_to_bytes(payload)
            if not raw:
                raise ValueError('Image vide')
            result.update(statut='embarquee', sha256=hashlib.sha256(raw).hexdigest(), octets=len(raw))
        except (ValueError, TypeError):
            result['statut'] = 'donnees_invalides'
        return result
    try:
        parts = urlsplit(reference)
        if parts.scheme or parts.netloc:
            result['statut'] = 'externe_non_verifiee' if parts.scheme in ('http', 'https', '') else 'schema_non_pris_en_charge'
            return result
        if not parts.path:
            result['statut'] = 'reference_vide'
            return result
        local = bounded(document.parent / unquote(parts.path), scope)
        result['chemin'] = str(local.relative_to(scope.resolve()))
        if not local.is_file():
            result['statut'] = 'absente'
        else:
            raw = local.read_bytes()
            result.update(statut='locale_presente' if raw else 'fichier_vide', sha256=hashlib.sha256(raw).hexdigest(), octets=len(raw))
    except (ValueError, OSError):
        result['statut'] = 'hors_perimetre_ou_illisible'
    return result


def nodes_within(root):
    # Images dans template/noscript ne prouvent pas un rendu actif.
    return [n for n in root.xpath(IMAGE_XPATH)
            if not any(a.tag in ('template', 'noscript') for a in n.iterancestors())]


def inspect_document(document, scope, points=(9,)):
    document = bounded(document, scope)
    raw = document.read_bytes()
    tree = html.fromstring(raw)
    ids = {}
    for node in tree.xpath('//*[@id]'):
        ids.setdefault(node.get('id'), []).append(node)
    result = {'fichier': str(document.relative_to(scope.resolve())),
              'sha256_html': hashlib.sha256(raw).hexdigest(), 'points_trouves': [],
              'fenetres': [], 'liens_brises': [], 'images': [], 'paires': [],
              'anomalies': []}
    selected = []
    for ident, nodes in ids.items():
        match = re.fullmatch(r'(?:a|dx\d+)-p(\d+)', ident)
        if match and int(match.group(1)) in points:
            result['points_trouves'].append(ident)
            for node in nodes:
                sections = node.xpath('ancestor-or-self::section[1]')
                selected.append(sections[0] if sections else node)
    for point in points:
        if not any(ident.endswith('-p' + str(point)) for ident in result['points_trouves']):
            result['anomalies'].append('point' + str(point) + '_absent')
    visited = set()
    index = 0
    while index < len(selected):
        root = selected[index]
        index += 1
        for node in root.xpath('.//*[@popovertarget or @href]'):
            target = node.get('popovertarget')
            if node.get('popovertargetaction') == 'hide':
                continue
            href = node.get('href', '')
            fragment = unquote(href[1:]) if href.startswith('#') else None
            ident = target or fragment
            if not ident:
                continue
            matches = ids.get(ident, [])
            if not matches:
                if ident not in result['liens_brises']:
                    result['liens_brises'].append(ident)
                continue
            if len(matches) > 1:
                result['anomalies'].append('identifiant_duplique:' + ident)
            dest = matches[0]
            if ident in visited:
                continue
            if target or 'popover' in dest.attrib or 'fenetre' in dest.get('class', '').split():
                visited.add(ident)
                result['fenetres'].append(ident)
                selected.append(dest)
    seen = set()
    image_nodes = {}
    figures = set()
    for root in selected:
        for node in nodes_within(root):
            if node in seen:
                continue
            seen.add(node)
            reference = node.get('src', '') if node.tag == 'img' else node.get('href', node.get('{http://www.w3.org/1999/xlink}href', node.get('xlink:href', '')))
            item = asset(reference, document, scope)
            item.update(balise=node.tag, ligne=node.sourceline, alt=node.get('alt'))
            # srcset is exposed, never silently treated as verified.
            if node.get('srcset') or node.xpath('parent::picture/source[@srcset]'):
                item['limite'] = 'srcset_non_resolu'
                result['anomalies'].append('srcset_non_resolu')
            ancestors = node.xpath('ancestor::figure[1]')
            if ancestors:
                figure = ancestors[0]
                figures.add(figure)
                captions = figure.xpath('./figcaption')
                item['credits_html'] = [' '.join(c.text_content().split()) for c in captions]
                item['liens_credits'] = figure.xpath('./figcaption//a/@href')
                item['illustration_id'] = figure.get('data-illustration')
            else:
                item['credits_html'] = []
                item['liens_credits'] = []
            image_nodes[node] = item
            result['images'].append(item)
        figures.update(root.xpath('.//figure[@data-illustration]'))
    for figure in sorted(figures, key=lambda f: f.sourceline or 0):
        pairs = figure.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," paire ")]')
        entry = {'illustration_id': figure.get('data-illustration'), 'ligne': figure.sourceline,
                 'statut': 'paire_non_detectee'}
        if pairs:
            views = list(pairs[0])
            left = nodes_within(views[0]) if len(views) > 0 else []
            right = nodes_within(views[1]) if len(views) > 1 else []
            entry['images_par_vue'] = [len(left), len(right)]
            a = image_nodes.get(left[0], {}) if len(left) == 1 else {}
            b = image_nodes.get(right[0], {}) if len(right) == 1 else {}
            local_states = ('locale_presente', 'embarquee')
            if a.get('statut') in local_states and b.get('statut') in local_states:
                entry['statut'] = 'deux_vues_presentes'
                entry['octets_identiques_sha256'] = a['sha256'] == b['sha256']
                entry['reperes_svg_detectes'] = bool(views[1].xpath('.//*[local-name()="polygon" or local-name()="path" or local-name()="circle"]'))
            else:
                entry['statut'] = 'paire_incomplete_ou_non_verifiable'
        result['paires'].append(entry)
    if result['liens_brises']:
        result['anomalies'].append('liens_internes_brises')
    for item in result['images']:
        if item['statut'] not in ('locale_presente', 'embarquee', 'externe_non_verifiee'):
            result['anomalies'].append('asset:' + item['statut'])
    if any(p['statut'] == 'paire_incomplete_ou_non_verifiable' for p in result['paires']):
        result['anomalies'].append('paire_incomplete_ou_non_verifiable')
    result['anomalies'] = sorted(set(result['anomalies']))
    return result


def inventory(lot, scope, points=(9,)):
    if not points or any(not isinstance(p, int) or p < 1 for p in points):
        raise ValueError('Points : entiers positifs requis')
    points = tuple(sorted(set(points)))
    scope = scope.resolve()
    lot = bounded(lot, scope)
    paths = sorted(lot.glob('*.html'))
    if not paths:
        raise ValueError('Aucun HTML directement dans le LOT')
    documents = [inspect_document(path, scope, points) for path in paths]
    sources = bounded(lot / 'SOURCES.json', scope)
    credits = {'fichier': str(sources.relative_to(scope)), 'statut': 'absent'}
    if sources.is_file():
        data = json.loads(sources.read_text(encoding='utf-8'))
        credits.update(statut='document_lu', sha256=hashlib.sha256(sources.read_bytes()).hexdigest(),
                       rubriques={key: data[key] for key in ('images', 'images_et_schemas') if key in data})
    return {'version': 1, 'portee': 'HTML directs du LOT : points V8 sélectionnés et fenêtres liées récursivement',
            'points_demandes': list(points),
            'limites': ['Inventaire mécanique sans validation clinique, visuelle ou des droits.',
                        'Existence et empreinte ne prouvent pas que le fichier est décodable.',
                        'SVG décoratifs, CSS et scripts exclus; img et SVG image inclus.',
                        'Crédits documentaires du LOT sans attribution automatique aux images.',
                        'Paire détectée selon figure/.paire du renderer; autres structures non reconnues.',
                        'Aucune résolution réseau, JavaScript, base href ou srcset; source HTML statique.'],
            'lot': str(lot.relative_to(scope)), 'documents': documents, 'credits_documentaires': credits,
            'totaux': {'html': len(documents), 'images_referencees': sum(len(d['images']) for d in documents),
                       'html_avec_images': sum(bool(d['images']) for d in documents),
                       'html_avec_anomalies': sum(bool(d['anomalies']) for d in documents)}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('lot', type=Path)
    parser.add_argument('--scope', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--output', type=Path)
    parser.add_argument('--points', default='9', help='Numéros séparés par des virgules, défaut 9')
    args = parser.parse_args()
    try:
        report = inventory(args.lot, args.scope, tuple(int(p.strip()) for p in args.points.split(',')))
        encoded = json.dumps(report, ensure_ascii=False, indent=2) + '\n'
        if args.output:
            output = bounded(args.output, args.scope)
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(encoded, encoding='utf-8')
        else:
            print(encoded, end='')
        return 1 if report['totaux']['html_avec_anomalies'] else 0
    except (OSError, ValueError) as exc:
        parser.exit(2, str(exc) + '\n')


if __name__ == '__main__':
    raise SystemExit(main())
