#!/usr/bin/env python3
"""File ALPHA → BETTA → GAMMA : propose du travail, ne rédige ni n'atteste un audit."""
import argparse
from collections import Counter
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import sys
import subprocess
from datetime import datetime, timezone
from functools import lru_cache
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools._app import span
from tools.tip_data import TAG as TIP_TAG, ASSET as TIP_ASSET, from_js as tip_from_js, load as load_tip, check_loading as check_tip_loading
from tools.cours.controler import bilan
from tools.mono_build import mid
from tools.predecesseurs_fusion import validate_config as valider_integration

ID = 'modifications_1_ck_2_cs'
LIVE = {'en_redaction', 'a_auditer', 'en_audit', 'a_corriger', 'a_integrer', 'a_publier'}
OCCUPE = {'en_redaction', 'en_audit'}


def empreinte(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                    separators=(',', ':')).encode()).hexdigest()


def lire(root, path):
    target = (root / path).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError('chemin de preuve hors dépôt')
    return json.loads(target.read_text())


def appliquer_priorite_integration(root, result, registry):
    """P0 conserve l'inventaire mais n'attribue ni ne reprend aucun lot clinique."""
    path = root / 'tools/mandat/integration.json'
    try:
        if not path.exists() and not path.is_symlink() and 'remastering' not in registry:
            return result  # Instantanés historiques, avant le mandat P0 → P4 uniquement.
        config = valider_integration(lire(root, 'tools/mandat/integration.json'))
    except (OSError, ValueError, TypeError) as exc:
        result['anomalies'].append('Configuration integration.json invalide : ' + str(exc))
        result.update(etape_suspendue=result.get('etape'), phase_suspendue=result.get('phase'),
                      etape='BLOQUE', phase='integration_invalide', complet=False,
                      prochains_lots=[], audit_phase_requis=False,
                      prochaine_action='Corriger la configuration technique integration.json ; aucun lot clinique autorisé.')
        return result
    result['priorite_active'] = config['priorite_active']
    if config['priorite_active'] == 'P0':
        result.update(etape_suspendue=result.get('etape'), phase_suspendue=result.get('phase'),
                      etape='P0', phase='stabilisation', complet=False,
                      prochains_lots=[], audit_phase_requis=False,
                      prochaine_action='Achever la stabilisation technique P0, son audit, sa CI, sa fusion et sa publication avant toute reprise clinique.')
    return result


def preuve(root, record):
    if not isinstance(record, dict) or not isinstance(record.get('rapport'), str):
        return None
    try:
        target = (root / record['rapport']).resolve()
        if not target.is_relative_to(root.resolve()):
            return None
        raw = target.read_bytes()
        if hashlib.sha256(raw).hexdigest() != record.get('rapport_sha256'):
            return None
        return json.loads(raw)
    except (OSError, ValueError, TypeError):
        return None


# Adresse canonique publiée dans README.md, ligne « Application en ligne ».
PAGES = 'https://vialdjoukang-spec.github.io/organigramme-examen-federal/'


def date_lue(value):
    try:
        return isinstance(value, str) and date.fromisoformat(value) <= date.today()
    except ValueError:
        return False


def date_audit(report):
    if 'audit_utc' not in report and 'fuseau_date_lecture' not in report:
        return date_lue(report.get('lu_le'))
    try:
        stamp = datetime.fromisoformat(report['audit_utc'].replace('Z', '+00:00'))
        zone = ZoneInfo(report['fuseau_date_lecture'])
        return (stamp.tzinfo is not None and stamp <= datetime.now(timezone.utc)
                and stamp.astimezone(zone).date() == date.fromisoformat(report['lu_le']))
    except (KeyError, TypeError, ValueError, ZoneInfoNotFoundError):
        return False


# Ordre de Vial du 20.10.2026 à 07:40 : « grok-bot » est un contre-auditeur accepté (signature réelle).
AUDITEURS = ('gpt-6-astra', 'grok-bot')


def astra(report):
    """Une attestation déclarative est vérifiable en cohérence, pas une identité signée."""
    if not isinstance(report, dict):
        return False
    reviewer = report.get('relecteur_independant')
    return bool(report.get('verdict') == 'favorable_documentaire'
                and isinstance(reviewer, str) and reviewer.strip()
                and reviewer != report.get('auteur')
                and report.get('modele') in AUDITEURS
                and date_audit(report))


def git(root, *args):
    return subprocess.run(['git', *args], cwd=root, capture_output=True,
                          check=True, timeout=15).stdout


@lru_cache(maxsize=16)
def commit_files(root, commit):
    return git(root, 'ls-tree', '-r', '--name-only', commit).decode().splitlines()


@lru_cache(maxsize=128)
def blob(root, commit, path):
    return git(root, 'show', commit + ':' + path)


def chemin(path):
    return (isinstance(path, str) and bool(path) and not Path(path).is_absolute()
            and '..' not in Path(path).parts and ':' not in path and '\\' not in path)


def gamma_scope(root):
    # Périmètre calculé, jamais choisi par le rédacteur de la preuve.
    paths = {Path('app_v2.html')}
    for pattern in ('assets/**/*.css', 'assets/config/**/*.js',
                    'assets/st/**/*.js', 'data/cs/**/*.json'):
        paths.update(p.relative_to(root) for p in root.glob(pattern) if p.is_file())
    return {str(p): hashlib.sha256((root / p).read_bytes()).hexdigest()
            for p in sorted(paths)}


def publie(root, record, key, digest):
    report = preuve(root, record)
    if not isinstance(report, dict) or report.get('statut') != 'publication_verifiee':
        return False
    if not isinstance(report.get('unites'), dict) or report['unites'].get(key) != digest:
        return False
    commit = report.get('commit', '')
    if not isinstance(commit, str) or not re.fullmatch(r'[a-f0-9]{40}', commit):
        return False
    try:
        observed = datetime.fromisoformat(report.get('verifie_le', '').replace('Z', '+00:00'))
        if observed.tzinfo is None or observed > datetime.now(timezone.utc):
            return False
        if not re.fullmatch(r'https://github\.com/vialdjoukang-spec/organigramme-examen-federal/actions/runs/[0-9]+', report.get('workflow_pages', '')):
            return False
        # Le commit doit réellement être intégré dans main, pas une branche de travail.
        git(root, 'merge-base', '--is-ancestor', commit, 'refs/remotes/origin/main')
        files = report.get('fichiers')
        if not isinstance(files, list) or not files:
            return False
        verified = set()
        for f in files:
            if not isinstance(f, dict) or not chemin(f.get('path')):
                return False
            path = f['path']; public_path = f.get('public_path', path)
            if (path in verified or not chemin(public_path) or f.get('http') != 200
                    or f.get('url') != PAGES + public_path
                    or public_path != path and (path, public_path) != ('app_v2.html', 'index.html')):
                return False
            expected = hashlib.sha256(blob(str(root), commit, path)).hexdigest()
            if f.get('sha256_attendu') != expected or f.get('sha256_public') != expected:
                return False
            verified.add(path)
        if key.startswith('ALPHA:'):
            code = key.split(':', 1)[1]
            app = blob(str(root), commit, 'app_v2.html').decode()
            if TIP_ASSET in app:
                if TIP_ASSET not in verified:
                    return False
                check_tip_loading(app)
                tip = tip_from_js(blob(str(root), commit, TIP_ASSET).decode())
                if json.loads(blob(str(root), commit, f'data/tip/{code}.json')) != tip[code]:
                    return False
            else:  # publications antérieures à la migration, dont PR148/149
                a, b = span(app, 'TIP')
                tip = json.loads(app[a:b])
            return 'app_v2.html' in verified and empreinte(tip[code]['c']) == digest
        if key.startswith('BETTA:'):
            diagnostic = key.split(':', 1)[1]
            matches = []
            for path in commit_files(str(root), commit):
                if path.startswith('data/ck/mono/') and path.endswith('.json'):
                    data = json.loads(blob(str(root), commit, path))
                    if diagnostic in data:
                        matches.append((path, data[diagnostic]))
            if len(matches) != 1 or empreinte(matches[0][1]) != digest:
                return False
            asset = 'assets/mono/mono-' + Path(matches[0][0]).stem + '.js'
            if asset not in verified:
                return False
            js = blob(str(root), commit, asset).decode()
            payload, _ = json.JSONDecoder().raw_decode(js[js.index('=') + 1:].lstrip())
            return isinstance(payload, dict) and payload.get(diagnostic) == matches[0][1]
        if key.startswith('GAMMA:'):
            scope = gamma_scope(root)
            return (empreinte(scope) == digest and all(
                hashlib.sha256(blob(str(root), commit, path)).hexdigest() == sha
                and (path.startswith('data/') or path in verified)
                for path, sha in scope.items()))
    except (OSError, ValueError, TypeError, KeyError, SystemExit, subprocess.SubprocessError):
        return False
    return False


def audit_phase(root, record, scope):
    report = preuve(root, record)
    return bool(scope and astra(report) and report.get('perimetre_sha256') == empreinte(scope))


def audit_cours(root, code, parts):
    try:
        record = lire(root, 'tools/cours/registre.json').get('relectures', {}).get(code)
        report = preuve(root, record)
        return bool(astra(report) and report.get('sources_lues')
                    and report.get('parties_sha256') == [hashlib.sha256(p.encode()).hexdigest() for p in parts])
    except (OSError, ValueError, TypeError):
        return False


def lotir(rows, size):
    return [rows[i:i + size] for i in range(0, len(rows), size)]


def valider_reservations(registry, stage, phase, units, limit):
    errors, active, seen, agents, branches = [], [], set(), set(), set()
    for reservation in registry.get('reservations', []):
        if not isinstance(reservation, dict) or reservation.get('statut') not in LIVE | {'publie', 'annule'}:
            errors.append('Statut de réservation inconnu')
            continue
        if reservation['statut'] not in LIVE:
            continue
        agent = reservation.get('agent')
        if (not isinstance(agent, str) or not agent.strip()
                or reservation['statut'] in OCCUPE and agent in agents):
            errors.append('Agent absent ou réservé plusieurs fois : ' + str(agent))
        if reservation['statut'] in OCCUPE:
            agents.add(str(agent))
        branch = reservation.get('branche')
        if (not isinstance(branch, str) or not branch.strip()
                or reservation['statut'] in OCCUPE and branch in branches):
            errors.append('Branche absente ou partagée par plusieurs réservations : ' + str(branch))
        if reservation['statut'] in OCCUPE:
            branches.add(str(branch))
        if reservation.get('modele') != 'gpt-6-sol' or reservation.get('raisonnement') != 'high':
            errors.append('Modèle/raisonnement de rédaction non conforme : ' + str(agent))
        selected = reservation.get('unites', [])
        if reservation.get('etape') != stage or reservation.get('phase') != phase:
            errors.append('Réservation active hors de la phase courante : ' + str(reservation.get('agent')))
        if not isinstance(selected, list) or not 1 <= len(selected) <= limit:
            errors.append('Taille du lot invalide : ' + str(reservation.get('agent')))
            continue
        if any(not isinstance(x, str) or x not in units or x in seen for x in selected) or len(set(map(str, selected))) != len(selected):
            errors.append('Unité inconnue ou réservée deux fois : ' + str(reservation.get('agent')))
        seen.update(str(x) for x in selected)
        active.append(reservation)
    return errors, active


def construire(root=ROOT, coordination=None, contract=None, registry=None):
    root = Path(root)
    contract = contract if contract is not None else lire(root, 'tools/mandat/contrat.json')
    registry = registry if registry is not None else lire(root, 'tools/mandat/registre.json')
    if contract.get('actif') is not True:
        return None
    if (contract.get('id') != ID or contract.get('version') != 1
            or contract.get('ordre_categories') != ['G', 'S', 'F', 'O']
            or contract.get('alpha_categories') != ['S', 'F', 'O']
            or contract.get('cours_parties') != 14 or contract.get('dd_rubriques') != 6
            or contract.get('redaction', {}).get('ssp_max_par_agent') != 2
            or contract.get('redaction', {}).get('dd_max_par_agent') != 3
            or contract.get('redaction', {}).get('modele') != 'gpt-6-sol'
            or contract.get('audit', {}).get('modele') != 'gpt-6-astra'
            or not set(contract.get('audit', {}).get('modeles_acceptes', ['gpt-6-astra'])) <= set(AUDITEURS)
            or contract.get('audit', {}).get('independant') is not True
            or contract.get('redaction', {}).get('raisonnement') != 'high'
            or type(contract.get('agents_redacteurs_simultanes_max')) is not int
            or not 1 <= contract['agents_redacteurs_simultanes_max'] <= 3
            or contract.get('gamma_phases') != ['organisation', 'couleurs', 'fond_forme']):
        raise ValueError('Contrat ALPHA/BETTA/GAMMA invalide')
    if (registry.get('version') != 1 or not isinstance(registry.get('reservations'), list)
            or any(not isinstance(registry.get(k, {}), dict) for k in ('publications', 'audits_phases', 'gamma', 'applicabilite', 'audits_dd'))):
        raise ValueError('Registre du mandat invalide')
    app = (root / 'app_v2.html').read_text()
    a, b = span(app, 'SSP'); ssps = json.loads(app[a:b])
    tip = load_tip(root, app)
    categories = list(dict.fromkeys(row[0][0] for row in ssps))
    if (categories != contract['ordre_categories'] or len(ssps) != len(tip)
            or set(tip) != {row[0] for row in ssps}):
        raise ValueError('Catalogue SSP différent : inventaire à revoir')
    courses = bilan(root)
    read = {c for c in set(tip) - set(courses['ssp_restant'])
            if audit_cours(root, c, tip[c]['c'])}
    pubs, phase_audits = registry.get('publications', {}), registry.get('audits_phases', {})
    result = {'id': ID, 'version': 1, 'ordre': ['ALPHA', 'BETTA', 'GAMMA'],
              'catalogue': {'categories': dict(Counter(row[0][0] for row in ssps)),
                            'dernier_ssp': ssps[-1][0], 'total': len(ssps)},
              'modeles': {'redaction': contract['redaction'], 'audit': contract['audit']},
              'anomalies': list(courses['anomalies']), 'complet': False,
              'mesure': {'alpha_publies': 0, 'beta_publies': 0, 'gamma_publies': 0},
              'phases': [], 'prochains_lots': [], 'reservations_actives': []}
    current = None
    for category in contract['alpha_categories']:
        rows, scope = [], {}
        for code, title, _ in ssps:
            if code[0] != category:
                continue
            key = 'ALPHA:' + code; digest = empreinte(tip[code]['c']); scope[key] = digest
            published = code in read and publie(root, pubs.get(key), key, digest)
            result['mesure']['alpha_publies'] += int(published)
            if not published:
                rows.append({'unite': code, 'ssp': code, 'diagnostic': title,
                             'action': 'publier_et_verifier' if code in read else 'rediger_puis_auditer'})
        audited = not rows and audit_phase(root, phase_audits.get('ALPHA:' + category), scope)
        result['phases'].append({'etape': 'ALPHA', 'phase': category, 'total': len(scope),
                                 'publies': len(scope) - len(rows), 'audit_phase_valide': audited})
        if current is None and not audited:
            current = ('ALPHA', category, rows, scope, 2)
    # La liste des différentiels n'est jamais inventée à partir des cours.
    if coordination is None:
        from tools.coordination.calculer import calculer
        config = lire(root, 'tools/coordination/config.json'); config.pop('mandat', None)
        ledger = lire(root, 'tools/coordination/relectures.json')
        coordination = calculer(root, ledger=ledger, config=config)
    occurrences = coordination['occurrences']
    a, b = span(app, 'NOT'); notions = json.loads(app[a:b])
    expected_dd = [(code, mid(d), d) for code, _, _ in ssps
                   for d in notions.get(code, [[]])[0]]
    actual_dd = [(x['ssp'], x['diagnostic_id'], x['diagnostic']) for x in occurrences]
    if actual_dd != expected_dd:
        raise ValueError('Inventaire des différentiels différent du NOT courant')
    result['catalogue']['occurrences_dd'] = len(occurrences)
    result['catalogue']['diagnostics_uniques'] = len({x['diagnostic_id'] for x in occurrences})
    monos, duplicate_monos = {}, set()
    for path in sorted((root / 'data/ck/mono').glob('*.json')):
        data = json.loads(path.read_text())
        duplicate_monos.update(set(monos) & set(data))
        monos.update(data)
    if duplicate_monos:
        result['anomalies'].append('Monographies dupliquées : ' + ', '.join(sorted(duplicate_monos)))
    accounted = set()
    for code, title, _ in ssps:
        rows = []
        scope = {'CONTEXTE:' + code: empreinte({'ssp': code, 'titre': title,
                    'differentiels': notions.get(code, [[]])[0]})}
        context = [x for x in occurrences if x['ssp'] == code]
        if not context:
            key = 'BETTA:' + code + ':applicabilite'
            digest = empreinte({'ssp': code, 'titre': title, 'dd': []}); scope[key] = digest
            report = preuve(root, registry.get('applicabilite', {}).get(code))
            accepted = bool(isinstance(report, dict) and report.get('perimetre_sha256') == digest
                            and astra(report) and report.get('motif')
                            and report.get('decision') == 'sans_differentiel_applicable')
            if not accepted:
                rows.append({'unite': code + ':applicabilite', 'ssp': code, 'diagnostic': title,
                             'action': 'examiner_applicabilite_sans_inventer_un_diagnostic'})
        for item in context:
            diagnostic = item['diagnostic_id']; key = 'BETTA:' + diagnostic
            digest = empreinte(monos.get(diagnostic, {})); scope[key] = digest
            published = (item['prototype_relecture'] and diagnostic in monos
                         and audit_phase(root, registry.get('audits_dd', {}).get(diagnostic), {key: digest})
                         and publie(root, pubs.get(key), key, digest))
            if diagnostic not in accounted:
                result['mesure']['beta_publies'] += int(published); accounted.add(diagnostic)
            if not published and not any(x['unite'] == diagnostic for x in rows):
                rows.append({'unite': diagnostic, 'ssp': code, 'diagnostic': item['diagnostic'],
                             'action': 'adapter_six_rubriques_puis_auditer'})
        audited = not rows and audit_phase(root, phase_audits.get('BETTA:' + code), scope)
        result['phases'].append({'etape': 'BETTA', 'phase': code, 'total': len(scope),
                                 'a_traiter': len(rows), 'audit_phase_valide': audited})
        if current is None and not audited:
            current = ('BETTA', code, rows, scope, 3)
    for phase in contract['gamma_phases']:
        entry = registry.get('gamma', {}).get(phase, {})
        scope = gamma_scope(root)
        key = 'GAMMA:' + phase; digest = empreinte(scope)
        published = bool(scope) and publie(root, pubs.get(key), key, digest)
        audited = published and audit_phase(root, phase_audits.get(key), scope)
        result['mesure']['gamma_publies'] += int(published)
        result['phases'].append({'etape': 'GAMMA', 'phase': phase, 'audit_phase_valide': bool(audited)})
        if current is None and not audited:
            current = ('GAMMA', phase, [{'unite': phase, 'ssp': 'CS', 'diagnostic': phase,
                                        'action': 'implementer_puis_auditer'}], scope, 1)
    if current is None:
        errors, active = valider_reservations(registry, 'TERMINE', None, set(), 0)
        result['anomalies'].extend(errors)
        result.update(etape='TERMINE', phase=None, complet=not result['anomalies'])
        return appliquer_priorite_integration(root, result, registry)
    stage, phase, rows, scope, limit = current
    result.update(etape=stage, phase=phase, perimetre_sha256=empreinte(scope),
                  audit_phase_requis=not rows, restant_phase=len(rows))
    units = ({phase} if stage == 'GAMMA'
             else set(scope_key.split(':', 1)[1] for scope_key in scope
                      if not scope_key.startswith('CONTEXTE:')))
    errors, active = valider_reservations(registry, stage, phase, units, limit)
    result['anomalies'].extend(errors)
    if sum(x['statut'] in OCCUPE for x in active) > contract['agents_redacteurs_simultanes_max']:
        result['anomalies'].append('Trop de réservations actives pour les capacités de cette équipe')
    result['reservations_actives'] = active
    if result['anomalies']:
        return appliquer_priorite_integration(root, result, registry)
    if active:
        result['prochains_lots'] = [{'agent': x['agent'], 'branche': x.get('branche'),
            'action': 'reprendre_lot_reserve', 'statut': x['statut'],
            'travail_attendu': {'en_redaction': 'poursuivre_redaction', 'a_auditer': 'attribuer_audit_independant',
                'en_audit': 'poursuivre_audit', 'a_corriger': 'attribuer_corrections',
                'a_integrer': 'integrer_apres_audit', 'a_publier': 'publier_et_verifier_sans_nouvelle_redaction'}[x['statut']],
            'unites': x['unites']} for x in active]
    else:
        result['prochains_lots'] = [{'action': 'attribuer', 'unites': [r['unite'] for r in chunk],
                                    'elements': chunk}
                                   for chunk in lotir(rows, limit)[:contract['agents_redacteurs_simultanes_max']]]
    return appliquer_priorite_integration(root, result, registry)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--coordination', type=Path)
    args = parser.parse_args()
    coordination = json.loads(args.coordination.read_text()) if args.coordination else None
    result = construire(args.root, coordination=coordination)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return int(bool(result and result['anomalies']))


if __name__ == '__main__':
    sys.exit(main())
