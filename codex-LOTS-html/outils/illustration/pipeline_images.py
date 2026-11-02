#!/usr/bin/env python3
"""Chaîne iconographique : recherche documentaire, acquisition, fenêtre et insertion.
Le connecteur web alimente RESULTATS_WEB.json via rechercher_web.js. Aucune
validation visuelle ou clinique n'est attribuée automatiquement par ce script.
"""
import argparse
import hashlib
import io
import json
import re
import subprocess
import urllib.request
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from urllib.parse import urlparse
from lxml import etree, html
from PIL import Image
import illustrer
from acquerir_commons import politique_permet, SansRedirection, POLITIQUE

BASE = Path(__file__).resolve().parents[2]
MAX = 20 * 1024 * 1024


def now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def path(value, root=None):
    root = BASE if root is None else root
    p = (BASE / value).resolve()
    if not p.is_relative_to(BASE.resolve()) or not p.is_relative_to(root.resolve()):
        raise ValueError('Chemin hors périmètre : ' + str(value))
    return p


def save(p, obj):
    path(p).parent.mkdir(parents=True, exist_ok=True)
    path(p).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')


def guard(lot):
    if not re.fullmatch(r'LOT_\d{3}', lot):
        raise ValueError('Lot invalide')
    res = json.loads((BASE.parent / 'IA_RESERVATIONS.json').read_text())['codex']
    if not res['plage'][0] <= int(lot[4:]) <= res['plage'][1]:
        raise ValueError('Lot hors borne fraîche')
    branch = subprocess.check_output(['git', 'branch', '--show-current'], cwd=BASE, text=True).strip()
    if branch != 'codex/lots' or branch != res['branche']:
        raise ValueError('Branche non autorisée')
    if not (BASE / '_cache/production.lock').exists():
        raise ValueError('Verrou officiel requis')
    for cmd in [('pret', 'codex'), ('verifier', 'codex', lot)]:
        subprocess.run(['python3', '-B', str(BASE / 'registre_ia.py'), *cmd], check=True, stdout=subprocess.DEVNULL)


def get(url, limit=MAX):
    u = urlparse(url)
    if u.scheme != 'https' or u.username or u.password or u.port not in (None, 443):
        raise ValueError('URL HTTPS simple requise')
    if not politique_permet(url, json.loads(POLITIQUE.read_text())):
        raise PermissionError('Domaine exclu de la politique réseau : ' + str(u.hostname))
    req = urllib.request.Request(url, headers={'User-Agent': 'Codex-LOTS/1.0 (verification documentaire)'})
    with urllib.request.build_opener(SansRedirection()).open(req, timeout=25) as r:
        if r.status != 200:
            raise ValueError('HTTP non 200')
        raw = r.read(limit + 1)
        if not raw or len(raw) > limit:
            raise ValueError('Réponse vide ou trop volumineuse')
        return raw, r.headers.get_content_type()


def license_info(node):
    """N'accepte qu'une URL de licence explicite et non ambiguë."""
    attributes = node.xpath('.//license//@*[local-name()="href"]')
    urls = set(attributes)
    text = ' '.join(node.xpath('.//license//text()'))
    if re.search(r'non.?commercial|no.?derivatives|by-nc|by-nd', text + ' '.join(urls), re.I):
        return {'decision': 'exclu_NC_ND', 'preuve': text}
    # Certains JATS distinguent explicitement contenu CC BY et métadonnées CC0.
    # Exclusion étroite : uniquement le paragraphe autonome de cette déclaration.
    metadata = []
    ignored = set()
    for paragraph in node.xpath('.//license/license-p'):
        sentence = ' '.join(' '.join(paragraph.itertext()).split())
        links = paragraph.xpath('.//@*[local-name()="href"]')
        if (re.fullmatch(r'The Creative Commons Public Domain Dedication waiver https?://creativecommons\.org/publicdomain/zero/1\.0/ applies to the metadata files associated with this article\.', sentence)
                and len(links) == 1 and str(links[0]) in ('http://creativecommons.org/publicdomain/zero/1.0/', 'https://creativecommons.org/publicdomain/zero/1.0/')):
            ignored.add(links[0].getparent())
            metadata.append({'portee': 'métadonnées seules', 'licence': 'CC0 1.0', 'preuve': sentence})
    urls = {str(a) for a in attributes if a.getparent() not in ignored}
    valid = []
    for u in urls:
        parsed = urlparse(u)
        if parsed.hostname != 'creativecommons.org' or parsed.scheme not in ('http', 'https'):
            continue
        m = re.fullmatch(r'/licenses/(by|by-sa)/([1234]\.0|2\.5)/?', parsed.path)
        if m:
            valid.append(('CC ' + m[1].upper() + ' ' + m[2], 'https://creativecommons.org' + parsed.path.rstrip('/') + '/'))
        elif parsed.path.rstrip('/') == '/publicdomain/zero/1.0':
            valid.append(('CC0 1.0', 'https://creativecommons.org/publicdomain/zero/1.0/'))
        elif parsed.path.rstrip('/') == '/publicdomain/mark/1.0':
            valid.append(('Domaine public', 'https://creativecommons.org/publicdomain/mark/1.0/'))
    if len(set(valid)) != 1:
        return {'decision': 'reserve_licence', 'preuve': text, 'urls': sorted(urls)}
    lic, url = valid[0]
    result = {'decision': 'licence_admissible_a_relire', 'licence': lic, 'licence_url': url, 'preuve': text}
    if metadata:
        result['perimetres_exclus_du_contenu'] = metadata
    return result


def parse_article(raw, metadata, pmcid):
    doc = etree.fromstring(raw, etree.XMLParser(resolve_entities=False, no_network=True))
    info = license_info(doc.find('front'))
    author_nodes = doc.xpath('./front/article-meta/contrib-group/contrib[@contrib-type="author" or (not(@contrib-type) and parent::contrib-group[@content-type="author"])]')
    authors = [' '.join(n.xpath('./name/given-names/text() | ./string-name/given-names/text()') + n.xpath('./name/surname/text() | ./string-name/surname/text()')) for n in author_nodes]
    authors = [name for name in authors if name.strip()]
    result = {'pmcid': pmcid, 'titre': ' '.join(doc.xpath('./front/article-meta/title-group/article-title//text()')),
              'auteur': ', '.join(authors), 'droits': info, 'figures': []}
    if info['decision'] != 'licence_admissible_a_relire':
        return result
    for fig in doc.xpath('.//body//fig'):
        hrefs = fig.xpath('.//graphic/@*[local-name()="href"]')
        files = [f for f in metadata.get('files', []) if f.get('type') == 'image' and f.get('mimeType') in ('image/jpeg', 'image/png') and any(Path(f['filename']).stem == Path(h).stem for h in hrefs)]
        for f in files:
            fid = re.sub('[^a-z0-9-]', '-', (pmcid + '-' + f['filename']).lower())
            caption = ' '.join(fig.xpath('./caption//text()'))
            nature = 'exclu_non_clinique' if re.search(r'flow.?chart|flow.?diagram|PRISMA|study selection', caption, re.I) else 'a_relire'
            result['figures'].append({'id': fid, 'figure': fig.get('id'), 'original_url': f['url'],
                'mime': f['mimeType'], 'md5': f.get('md5'), 'legende_source': caption, 'decision_figure': nature,
                'credits_figure': ' '.join(fig.xpath('./attrib//text() | ./permissions//text()')),
                'source_url': 'https://europepmc.org/article/PMC/' + pmcid[3:],
                'auteur': result['auteur'], 'licence': info['licence'], 'licence_url': info['licence_url'],
                'acces_le': now()[:10], 'revue_documentaire': False, 'acquis': False, 'integre': False})
    return result


def rechercher(plan, folder):
    exports = json.loads(path(plan['resultats_web']).read_text())
    ids = sorted(set(x for r in exports['resultats'] for x in re.findall(r'PMC\d+', r['url'])))
    # Limite explicite de la passe ; la recherche ne vaut pas lecture clinique.
    ids = [x for x in ids if x in plan.get('pmcids', ids)][:plan.get('max_articles', 5)]
    out = {'date': now(), 'lot': plan['lot'], 'requetes': exports['requetes'], 'articles': [], 'erreurs': []}
    for pmcid in ids:
        try:
            url = 'https://europepmc.org/api/fulltextXmlRepo?ft_id=' + pmcid
            raw, _ = get(url, 4 * 1024 * 1024)
            doc = etree.fromstring(raw, etree.XMLParser(resolve_entities=False, no_network=True))
            lic = license_info(doc.find('front'))
            # Ne pas republier un article NC/ND ou aux droits inconnus.
            access = {'date': now(), 'url': url, 'sha256': sha(raw), 'octets': len(raw), 'droits': lic}
            if lic['decision'] != 'licence_admissible_a_relire':
                out['articles'].append({'pmcid': pmcid, 'droits': lic, 'figures': []})
                save(folder / (pmcid + '-acces.json'), access)
                continue
            meta_url = 'https://europepmc.org/api/fulltextRepo?pmcId=' + pmcid + '&type=METADATA'
            meta_raw, _ = get(meta_url, 2 * 1024 * 1024)
            article = parse_article(raw, json.loads(meta_raw), pmcid)
            folder.mkdir(parents=True, exist_ok=True)
            for name, data in [(pmcid + '.xml', raw), (pmcid + '-metadata.json', meta_raw)]:
                p = folder / name
                if p.exists() and p.read_bytes() != data:
                    raise ValueError('Preuve déjà présente et différente : ' + name)
                p.write_bytes(data)
            access['metadata_url'] = meta_url
            access['metadata_sha256'] = sha(meta_raw)
            save(folder / (pmcid + '-acces.json'), access)
            out['articles'].append(article)
        except Exception as exc:
            out['erreurs'].append({'pmcid': pmcid, 'erreur': str(exc)})
    save(folder / 'RECHERCHE.json', out)
    return {'articles': len(out['articles']), 'figures': sum(len(a['figures']) for a in out['articles']), 'erreurs': out['erreurs']}


def verify_image(raw, candidate, mime):
    if mime != candidate['mime'] or not raw or len(raw) > MAX:
        raise ValueError('Format HTTP ou poids incorrect')
    if candidate.get('md5') and hashlib.md5(raw).hexdigest() != candidate['md5']:
        raise ValueError('Empreinte différente des métadonnées primaires')
    with Image.open(io.BytesIO(raw)) as im:
        if im.format not in ('JPEG', 'PNG') or Image.MIME[im.format] != mime or im.width * im.height > 50_000_000 or getattr(im, 'n_frames', 1) != 1:
            raise ValueError('Image non admissible')
        dims = list(im.size)
        im.verify()
    return dims


def acquerir(plan, folder):
    selected = json.loads(path(plan['selection']).read_text())
    out = []
    for c in selected['candidats']:
        r = {'id': c['id'], 'acquis': False, 'integre': False, 'inspection_visuelle': False}
        try:
            if c.get('revue_documentaire') is not True or not c.get('preuve_droits_figure'):
                raise ValueError('Lecture de la légende et des droits propres à la figure requise')
            if not re.fullmatch('[a-z][a-z0-9-]*', c['id']):
                raise ValueError('Identifiant invalide')
            # Réutilise la validation stricte de l'outil du dépôt.
            illustrer.validate(dict(c, titre='Contrôle documentaire', nature='image clinique', legende=c['legende_source'], pieges='Inspection à réaliser', annotations=[{}]))
            if urlparse(c['original_url']).hostname != 'cdn.ncbi.nlm.nih.gov' or not urlparse(c['original_url']).path.startswith('/pmc/blobs/'):
                raise ValueError('Provenance image Europe PMC non reconnue')
            ext = {'image/jpeg': '.jpg', 'image/png': '.png'}[c['mime']]
            target = path(folder / (c['id'] + ext), folder)
            if target.exists():
                raise ValueError('Original déjà présent : ne pas écraser')
            raw, mime = get(c['original_url'])
            dims = verify_image(raw, c, mime)
            folder.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
            r.update(acquis=True, fichier=str(target.relative_to(BASE)), sha256_original=sha(raw), dimensions=dims, date=now(), notice=c)
            save(target.with_suffix(target.suffix + '.source.json'), r)
        except Exception as exc:
            r['erreur'] = str(exc)
        out.append(r)
    save(folder / 'ACQUISITIONS.json', {'date': now(), 'resultats': out})
    return out


def reachable(root):
    parts = root.xpath('//h2[contains(@id,"-p9")]/parent::section')
    if len(parts) != 1:
        raise ValueError('Section 9 non unique')
    seen, nodes = set(), parts[:]
    for n in nodes:
        if n.get('id'):
            seen.add(n.get('id'))
        for target in n.xpath('.//*[@popovertarget]/@popovertarget'):
            if target not in seen:
                found = root.xpath('//*[@id=$x]', x=target)
                if len(found) == 1:
                    seen.add(target)
                    nodes.append(found[0])
    return parts[0], nodes


def injection(original, job, figure):
    if not re.fullmatch('[a-z][a-z0-9-]*', job['id']):
        raise ValueError('Identifiant de fenêtre invalide')
    root = html.fromstring(original)
    section, nodes = reachable(root)
    anchor = root.xpath('//*[@id=$x]', x=job['ancre'])
    if len(anchor) != 1 or not any(n is anchor[0] or n in anchor[0].iterancestors() for n in nodes):
        raise ValueError('Ancre hors des examens complémentaires et fenêtres liées')
    term = job['expression']
    if not term or '<' in term or '>' in term:
        raise ValueError('Expression invalide')
    # Le bloc exact est conservé ; pas de resérialisation de toute la leçon.
    start = re.search(r'<(?:div|section)\b[^>]*\bid=["\']' + re.escape(job['ancre']) + r'["\'][^>]*>', original)
    if not start:
        raise ValueError('Bloc source exact introuvable')
    # Repérage dans les nœuds textuels seulement, sans toucher attributs ni autres fenêtres.
    node = anchor[0]
    texts = node.xpath('.//text()[not(ancestor::button) and not(ancestor::script) and not(ancestor::style)]')
    matching = [str(t) for t in texts if term in str(t)]
    if len(matching) != 1 or matching[0].count(term) != 1:
        raise ValueError('Expression absente ou ambiguë dans le bloc ciblé')
    encoded = escape(matching[0], quote=False)
    pos = original.find(encoded, start.end())
    # Refuse les sérialisations à entités différentes plutôt que de deviner.
    if pos < 0:
        raise ValueError('Texte exact encodé introuvable')
    pid = 'image-' + job['id']
    if root.xpath('//*[@id=$x]', x=pid):
        raise ValueError('Fenêtre déjà présente')
    label = escape(term, quote=False)
    button = f'<button type="button" class="terme" popovertarget="{pid}">{label}</button>'
    replacement = encoded.replace(label, button, 1)
    result = original[:pos] + replacement + original[pos + len(encoded):]
    window = f'<div id="{pid}" class="fenetre" popover="manual"><div class="barre"><span>{escape(term)}</span><button type="button" popovertarget="{pid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div><div class="corps">{figure}</div></div>'
    if result.count('</main>') != 1:
        raise ValueError('Fin du document ambiguë')
    result = result.replace('</main>', window + '\n</main>')
    check = html.fromstring(result)
    inserted = check.xpath('//*[@id=$a]//button[@popovertarget=$p]', a=job['ancre'], p=pid)
    if len(inserted) != 1:
        raise ValueError('Insertion hors de l’ancre exacte')
    if len(check.xpath('//h2[contains(@id,"-p")]')) != len(root.xpath('//h2[contains(@id,"-p")]')) or len(check.xpath('//details[contains(@class,"quiz")]')) != len(root.xpath('//details[contains(@class,"quiz")]')):
        raise ValueError('Structure de la leçon modifiée')
    return result


def preparer(plan, folder):
    job = json.loads(path(plan['integration']).read_text())
    spec = json.loads(path(job['specification']).read_text())
    if spec['id'] != job['id']:
        raise ValueError('Identifiants du travail et de la figure différents')
    original = path(spec['image'], BASE / plan['lot'])
    if spec.get('revue_original', {}).get('sha256') != sha(original.read_bytes()) or spec.get('revue_original', {}).get('inspecte') is not True:
        raise ValueError('Inspection réelle de l’original requise et liée à son empreinte')
    spec['comparaison'] = True
    figure = illustrer.render(spec)
    lesson = path(job['lecon'], BASE / plan['lot'])
    raw = lesson.read_bytes()
    if sha(raw) != job['sha256_lecon']:
        raise ValueError('Leçon modifiée depuis préparation du travail')
    output = injection(raw.decode(), job, figure)
    folder.mkdir(parents=True, exist_ok=True)
    preview = path(folder / (job['id'] + '-apercu.html'), folder)
    preview.write_text(output)
    save(folder / (job['id'] + '-preparation.json'), {'date': now(), 'job': job, 'sha256_specification': sha(path(job['specification']).read_bytes()), 'sha256_apercu': sha(preview.read_bytes()), 'apercu': str(preview.relative_to(BASE)), 'inspection_rendu': False})
    return {'apercu': str(preview.relative_to(BASE)), 'integre': False}


def integrer(plan, folder):
    job = json.loads(path(plan['integration']).read_text())
    proof = json.loads((folder / (job['id'] + '-preparation.json')).read_text())
    review = json.loads(path(plan['revue_rendu']).read_text())
    preview = path(proof['apercu'], folder)
    raw = preview.read_bytes()
    if sha(raw) != proof['sha256_apercu'] or review.get('sha256_apercu') != sha(raw) or review.get('inspecte') is not True or not review.get('observations'):
        raise ValueError('Revue réelle du rendu absente ou périmée')
    for capture in review.get('captures', []):
        if sha(path(capture['fichier']).read_bytes()) != capture['sha256']:
            raise ValueError('Capture modifiée')
    if not review.get('captures'):
        raise ValueError('Capture de contrôle requise')
    specpath = path(job['specification'])
    if proof['job'] != job or sha(specpath.read_bytes()) != proof['sha256_specification']:
        raise ValueError('Travail ou annotations modifiés depuis rendu')
    spec = json.loads(specpath.read_text())
    if sha(path(spec['image'], BASE / plan['lot']).read_bytes()) != spec['sha256_original']:
        raise ValueError('Original modifié')
    lesson = path(job['lecon'], BASE / plan['lot'])
    before = lesson.read_bytes()
    if sha(before) != job['sha256_lecon']:
        raise ValueError('Leçon source modifiée')
    sources_path = path(BASE / plan['lot'] / 'SOURCES.json', BASE / plan['lot'])
    prior = sources_path.read_bytes() if sources_path.exists() else None
    sources = json.loads(prior) if prior else {'portee': 'Illustrations seulement ; sources médicales des leçons préservées.', 'images_et_schemas': []}
    # Les lots documentaires (dont LOT_133) n'ont pas encore cette collection.
    # Ajouter seulement la collection iconographique, sans remplacer leurs sources.
    images = sources.setdefault('images_et_schemas', [])
    if not isinstance(images, list) or any(not isinstance(s, dict) for s in images):
        raise ValueError('Collection images_et_schemas invalide')
    if any(s.get('id') == job['id'] for s in images):
        raise ValueError('Crédit déjà présent')
    images.append({**{k: spec[k] for k in ('auteur','licence','licence_url','source_url','acces_le','sha256_original')}, 'id': job['id'], 'fichier_original': spec['image'], 'lecon': job['lecon'], 'sha256_lecon': sha(raw), 'preuve': plan['revue_rendu'], 'validation_humaine': False, 'revue_visuelle_interne': True, 'modifications': 'Comparaison du même cliché, contours rouges pointillés et repères numérotés dans une fenêtre de la section 9.'})
    backup = path(folder / (job['id'] + '-avant.html'), folder)
    if backup.exists():
        raise ValueError('Sauvegarde existante ; examiner la précédente intégration')
    backup.write_bytes(before)
    try:
        save(sources_path, sources)
        lesson.write_bytes(raw)
    except Exception:
        lesson.write_bytes(before)
        if prior is None:
            sources_path.unlink(missing_ok=True)
        else:
            sources_path.write_bytes(prior)
        raise
    save(folder / (job['id'] + '-integration.json'), {'date': now(), 'lecon': job['lecon'], 'sha256_avant': sha(before), 'sha256_apres': sha(raw), 'validation_clinique': False})
    return {'lecon': job['lecon'], 'integre': True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['rechercher','acquerir','preparer','integrer'])
    parser.add_argument('plan')
    args = parser.parse_args()
    plan = json.loads(path(Path(args.plan).resolve()).read_text())
    guard(plan['lot'])
    folder = path(plan['dossier'], BASE / plan['lot'] / 'illustrations')
    result = globals()[args.action](plan, folder)
    print(json.dumps(result, ensure_ascii=False))
    if args.action == 'acquerir' and (not result or any(not r['acquis'] for r in result)):
        raise SystemExit(2)
    if args.action == 'rechercher' and result['erreurs']:
        raise SystemExit(2)

if __name__ == '__main__':
    main()
