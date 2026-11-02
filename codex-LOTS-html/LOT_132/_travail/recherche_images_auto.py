#!/usr/bin/env python3
"""Recherche documentaire gratuite ; aucune acquisition ou insertion d'image.

Exécution : python3 -B codex-LOTS-html/LOT_132/_travail/recherche_images_auto.py
Chaque passe conserve son rapport horodaté dans recherche/automatique/.
Une licence d'article admissible ne valide jamais les droits d'une figure.
"""
import argparse
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode

LOT = Path(__file__).resolve().parents[1]
API = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search'
REQUETES = {
    'condensation': '"pneumonia" AND "air bronchogram" AND "case report" AND OPEN_ACCESS:Y',
    'pneumothorax': '"pneumothorax" AND "chest radiograph" AND "adult" AND OPEN_ACCESS:Y',
    'oedeme': '"pulmonary edema" AND "chest radiograph" AND "heart failure" AND OPEN_ACCESS:Y',
    'pleural': '"pleural effusion" AND "ultrasound" AND "adult" AND OPEN_ACCESS:Y',
}
MOTS = {
    'condensation': r'condensation|consolidation|bronchogram',
    'pneumothorax': r'pneumothorax',
    'oedeme': r'pulmonary edema|pulmonary oedema|œdème|oedème|oedeme',
    'pleural': r'pleural|épanchement',
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def droits(value):
    value = re.sub(r'\s+', ' ', (value or '').lower().replace('-', ' ')).strip()
    if re.search(r'\bnc\b|\bnd\b|non.?commercial|no.?derivatives', value):
        return 'refuse_NC_ND'
    if re.fullmatch(r'(?:cc by(?: sa)?(?: [1-4]\.[05])?|cc0(?: 1\.0)?|public domain|domaine public)', value):
        return 'licence_article_admissible_droits_figure_a_relire'
    return 'refuse_licence_inconnue_ou_ambigue'


def consulter(query):
    url = API + '?' + urlencode({'query': query, 'format': 'json', 'resultType': 'core', 'pageSize': 5})
    try:
        run = subprocess.run(['curl', '--proto', '=https', '--max-time', '15', '--max-filesize', '4194304',
                              '--silent', '--show-error', '--write-out', '\n%{http_code}', url],
                             capture_output=True, timeout=18)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {'url': url, 'statut': 'echec_client', 'erreur': str(exc)}, []
    body, _, code = run.stdout.rpartition(b'\n')
    access = {'url': url, 'curl_code': run.returncode, 'http': code.decode(errors='replace'),
              'sha256_reponse': sha(body), 'octets_reponse': len(body),
              'erreur_client': run.stderr.decode(errors='replace')[:500]}
    if run.returncode or code != b'200':
        access['statut'] = 'acces_refuse_ou_echoue'
        return access, []
    try:
        data = json.loads(body)
        results = data['resultList']['result']
        if not isinstance(results, list):
            raise ValueError('Liste attendue')
    except (ValueError, KeyError, TypeError) as exc:
        access.update(statut='reponse_non_exploitable', erreur=str(exc))
        return access, []
    access.update(statut='recherche_web_effectuee', nombre_resultats=len(results), total=data.get('hitCount'))
    candidates = []
    for item in results:
        license_value = item.get('license') or ''
        pmcid = item.get('pmcid') or ''
        candidates.append({'origine': 'api_web_europepmc', 'pmcid': pmcid,
                           'titre': item.get('title'), 'auteurs': item.get('authorString'),
                           'doi': item.get('doi'), 'date_publication': item.get('firstPublicationDate'),
                           'licence_declaree_api': license_value, 'decision_droits': droits(license_value),
                           'source_url': 'https://europepmc.org/articles/' + pmcid if re.fullmatch(r'PMC\d+', pmcid) else None,
                           'preuve_metadata': {'sha256': sha(json.dumps(item, sort_keys=True).encode()), 'metadata': item},
                           'figure_choisie': False, 'pixels_inspectes_par_cette_passe': False,
                           'droits_figure_verifies_par_cette_passe': False, 'acquisition_image': False})
    return access, candidates


def locaux():
    """Relit des preuves acquises ; ne transforme pas ce repli en recherche web."""
    found = []
    for manifest in sorted((LOT / 'recherche/images').glob('CANDIDAT*.json')):
        item = {'origine': 'manifeste_local_acquis', 'manifeste': str(manifest.relative_to(LOT)),
                'sha256_manifeste': sha(manifest.read_bytes()), 'acquisition_image': False,
                'pixels_inspectes_par_cette_passe': False, 'droits_figure_verifies_par_cette_passe': False}
        try:
            doc = json.loads(manifest.read_text())
            filename = doc['fichier_original']
            original = (manifest.parent / filename).resolve()
            if not original.is_relative_to((LOT / 'recherche/images').resolve()):
                raise ValueError('Original hors dossier')
            if sha(original.read_bytes()) != doc['sha256_original']:
                raise ValueError('Empreinte original différente')
            acquisition_path = manifest.parent / 'ACQUISITION.json'
            acquisition = json.loads(acquisition_path.read_text())
            for proof in acquisition['fichiers']:
                file = (manifest.parent / proof['nom']).resolve()
                if not file.is_relative_to(manifest.parent.resolve()) or sha(file.read_bytes()) != proof['sha256']:
                    raise ValueError('Preuve acquisition modifiée ou hors dossier')
            item.update(titre=doc['titre'], auteurs=doc['auteurs'], source_url=doc['source_url'],
                        licence=doc.get('licence'), licence_url=doc.get('licence_url'),
                        decision_droits=droits(doc.get('licence')),
                        fichier_original=str(original.relative_to(LOT)), sha256_original=doc['sha256_original'],
                        preuve_licence_preexistante=doc.get('preuve_licence'),
                        inspection_preexistante=doc.get('inspection_pixels'),
                        preuves_acquisition_sha_verifiees=True,
                        sha256_acquisition=sha(acquisition_path.read_bytes()),
                        legende=doc.get('legende_originale'), contexte=doc.get('contexte_adulte'),
                        texte_indexe=' '.join(str(doc.get(k, '')) for k in ('titre', 'legende_originale', 'constats_pixels')))
        except (OSError, ValueError, KeyError, TypeError) as exc:
            item.update(decision_droits='refuse_preuve_locale_incomplete_ou_modifiee', erreur=str(exc))
        found.append(item)
    return found


def licence_pdf(text):
    # Uniquement la déclaration d'ouverture, pas une licence citée en bibliographie.
    opening = re.sub(r'\s+', ' ', text[:9000])
    match = re.search(r'(?:This (?:is an |article is an )open.access article|Open Access This article).*?(?:source are credited\.|licenses/[^\s]+|licen[cs]e\s*\([^)]*\))', opening, re.I)
    if not match:
        return {'decision': 'refuse_licence_inconnue_ou_ambigue', 'preuve': ''}
    paragraph = match.group(0)
    if re.search(r'non.?commercial|no.?derivatives|\bNC\b|\bND\b|/by-nc|/by-nd', paragraph, re.I):
        return {'decision': 'refuse_NC_ND', 'preuve': paragraph}
    if re.search(r'CC[ -]BY\s*4\.0|creativecommons\.org/licenses/by/4\.0', paragraph, re.I):
        return {'decision': 'licence_article_admissible_droits_figure_a_relire',
                'licence': 'CC BY 4.0', 'licence_url': 'https://creativecommons.org/licenses/by/4.0/', 'preuve': paragraph}
    return {'decision': 'refuse_licence_inconnue_ou_ambigue', 'preuve': paragraph}


def acquerir_pdf(pmcid, folder, provenance):
    url = 'https://europepmc.org/api/getPdf?' + urlencode({'pmcid': pmcid})
    target = folder / pmcid
    target.mkdir()
    pdf = target / (pmcid + '.pdf')
    txt = target / 'article.txt'
    row = {'pmcid': pmcid, 'origine_decouverte': provenance, 'origine_acquisition': 'web_curl_europepmc_pdf',
           'url': url, 'date_utc': datetime.now(timezone.utc).isoformat(), 'statut': 'acquisition_en_cours',
           'inspection_pixels': False, 'figure_choisie': False, 'integration': False}
    try:
        run = subprocess.run(['curl', '--proto', '=https', '--max-time', '35', '--max-filesize', '33554432',
                              '--silent', '--show-error', '--output', str(pdf), '--write-out', '%{http_code}', url],
                             capture_output=True, timeout=40)
        row.update(curl_code=run.returncode, http=run.stdout.decode(errors='replace'), erreur_client=run.stderr.decode(errors='replace')[:500])
        if run.returncode or run.stdout != b'200':
            raise ValueError('Acquisition HTTP refusée ou échouée')
        raw = pdf.read_bytes()
        row.update(sha256_pdf=sha(raw), octets_pdf=len(raw))
        if not raw.startswith(b'%PDF-'):
            raise ValueError('Réponse non PDF')
        subprocess.run(['pdftotext', '-layout', str(pdf), str(txt)], check=True, capture_output=True, timeout=20)
        text = txt.read_text()
        row['droits'] = licence_pdf(text)
        if not row['droits']['decision'].startswith('licence_article_admissible'):
            row['statut'] = row['droits']['decision']
            # Conserver l'empreinte et l'extrait de droits, pas republier le PDF refusé.
            pdf.unlink(); txt.unlink()
        else:
            row.update(statut='pdf_acquis_licence_article_detectee_figure_a_relire',
                       sha256_texte=sha(txt.read_bytes()), pdf=str(pdf.relative_to(LOT)), texte=str(txt.relative_to(LOT)),
                       doi=re.findall(r'10\.\d{4,9}/[A-Za-z0-9.\-/]+', text[:9000]),
                       extraction_licence='Déclaration explicite en ouverture ; détection mécanique, relecture de la figure requise',
                       limitations='Aucune image extraite ou réutilisée automatiquement ; contrôle adulte/clinique, crédits propres aux figures et pixels restent humains/agents distincts.')
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        row.update(statut='echec_acquisition_ou_extraction', erreur=str(exc))
        pdf.unlink(missing_ok=True); txt.unlink(missing_ok=True)
    (target / 'ACQUISITION.json').write_text(json.dumps(row, ensure_ascii=False, indent=2) + '\n')
    return row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pmcid', '--pmcids', nargs='+', help='PMCID repérés via outil web ou fournis explicitement ; ne relance pas API search bloquée')
    parser.add_argument('--provenance', type=Path, help='JSON de découverte ; fichier existant sous recherche/automatique/')
    args = parser.parse_args()
    if args.pmcid and (any(not re.fullmatch(r'PMC\d+', x) for x in args.pmcid) or len(args.pmcid) > 5):
        parser.error('Un à cinq PMCID valides requis')
    if args.pmcid and not args.provenance:
        parser.error('--provenance requis avec --pmcid')
    now = datetime.now(timezone.utc)
    folder = LOT / 'recherche/automatique' / now.strftime('%Y%m%dT%H%M%S%fZ')
    folder.mkdir(parents=True, exist_ok=False)
    if args.pmcid:
        source = args.provenance.resolve()
        if not source.is_relative_to((LOT / 'recherche/automatique').resolve()):
            parser.error('Provenance hors recherche/automatique')
        discovery = json.loads(source.read_text())
        known = {r['pmcid'] for r in discovery['resultats']}
        if any(x not in known for x in args.pmcid):
            parser.error('PMCID absent de la provenance fournie')
        provenance = {'fichier': str(source.relative_to(LOT)), 'sha256': sha(source.read_bytes()),
                      'canal': discovery['canal'], 'recherche_effectuee_par_cli': False}
        rows = []
        for pmcid in dict.fromkeys(args.pmcid):
            row = acquerir_pdf(pmcid, folder, provenance)
            rows.append(row)
            with (folder / 'JOURNAL.jsonl').open('a') as stream:
                stream.write(json.dumps(row, ensure_ascii=False) + '\n')
            print(pmcid + ': ' + row['statut'], flush=True)
        (folder / 'ACQUISITIONS.json').write_text(json.dumps({'date': now.isoformat(), 'mode': 'pmcid_decouvert_separement', 'resultats': rows}, ensure_ascii=False, indent=2) + '\n')
        print(folder / 'ACQUISITIONS.json')
        return
    local = locaux()
    report = {'date_utc': now.isoformat(), 'lot': 'LOT_132', 'outil': 'curl + API officielle EuropePMC + repli local SHA',
              'cout_api_payante': False, 'appel_modele': False, 'insertion_html': False,
              'limite': 'Recherche documentaire seulement ; âge adulte, pertinence clinique et droits propres à chaque figure restent à vérifier. Les échecs web ne prouvent aucune absence de candidat.',
              'requetes': [], 'manifestes_locaux': [{k:v for k,v in x.items() if k != 'texte_indexe'} for x in local]}
    for theme, query in REQUETES.items():
        access, candidates = consulter(query)
        matches = [{k:v for k,v in x.items() if k != 'texte_indexe'} for x in local
                   if re.search(MOTS[theme], x.get('texte_indexe', ''), re.I)]
        row = {'theme': theme, 'requete': query, 'acces_web': access, 'candidats_web': candidates,
               'correspondances_locales': matches,
               'statut': 'web_effectue' if access['statut'] == 'recherche_web_effectuee' else 'web_indisponible_repli_local' if matches else 'web_indisponible_aucun_local_correspondant',
               'reutilisation_automatique': False}
        report['requetes'].append(row)
        with (folder / 'JOURNAL.jsonl').open('a') as stream:
            stream.write(json.dumps({'date': datetime.now(timezone.utc).isoformat(), **row}, ensure_ascii=False) + '\n')
        print(theme + ': ' + row['statut'], flush=True)
    (folder / 'RECHERCHE.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(folder / 'RECHERCHE.json')


if __name__ == '__main__':
    main()
