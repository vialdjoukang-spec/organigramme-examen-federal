#!/usr/bin/env python3
"""Auditeur statistique déterministe des candidats, sans validation clinique.

Conserve les sources et inconnus. Ne publie jamais dans data/ck/prev.json.
Seule une erreur arithmétique de proportion explicitement documentée se corrige.
"""
from __future__ import annotations

import argparse
import copy
from datetime import date, datetime, timezone
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
import hashlib
import ipaddress
import json
import os
from pathlib import Path
import re
import tempfile
import unicodedata
from urllib.parse import urlsplit


def _normal(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', str(text)).lower()
                   if not unicodedata.combining(c))


def _safe_url(value):
    if not isinstance(value, str) or any(ord(c) < 33 for c in value):
        return False
    try:
        u = urlsplit(value)
        if u.scheme not in ('http', 'https') or not u.hostname or u.username or u.password:
            return False
        _ = u.port
        host = u.hostname.lower().rstrip('.')
        if host == 'localhost' or host.endswith(('.localhost', '.local', '.internal')):
            return False
        try:
            return ipaddress.ip_address(host).is_global
        except ValueError:
            return '.' in host
    except ValueError:
        return False


def _number(value):
    # bool is an int in Python; it is never a statistical count.
    if isinstance(value, bool) or not isinstance(value, (int, float, str, Decimal)):
        return None
    try:
        token = str(value)
        if len(token) > 256:
            return None
        n = Decimal(token)
        # Computational bounds only, far beyond any clinical cohort. Inspect
        # exponent before int()/format(), which could allocate millions of digits.
        if n.is_zero():
            return Decimal(0)
        return n if n.is_finite() and abs(n.adjusted()) <= 100 else None
    except (InvalidOperation, ValueError, OverflowError):
        return None


def _proof(stat, key, excerpt):
    p = stat.get(key)
    return p if isinstance(p, str) and p.strip() and p in excerpt else None


def _count_present(count, proof):
    # Avoid treating 12 as evidence for 112, or 1 as evidence for 1.5.
    token = str(int(count))
    return bool(re.search(r'(?<![\d.,])' + re.escape(token) + r'(?![\d.,])', proof))


def _geography_supported(geography, proof):
    text = _normal(proof)
    people = re.search(r'\b(patient\w*|participant\w*|population\w*|resident\w*|recruit\w*|recrut\w*|subjects?|cohort\w*|inhabitant\w*)\b', text)
    if not people:
        return False
    swiss = r'\b(switzerland|swiss|suisse|schweiz|svizzera|zurich|geneva|geneve|lausanne|bern|berne|basel|bale)\b'
    europe = r'\b(europ\w*|france|french|germany|german|allemagne|italy|italian|italie|spain|spanish|espagne|belgium|belgian|belgique|netherlands|dutch|pays.bas|austria|austrian|autriche|united kingdom|british|royaume.uni|england|sweden|swedish|suede|denmark|danish|danemark|norway|norwegian|norvege|finland|finnish|finlande|poland|polish|pologne|portugal|portuguese|greece|greek|grece|ireland|irish|irlande)\b'
    return bool(re.search(swiss if geography == 'CH' else europe, text))



def _structured_errors(candidate, flags, corrections):
    """Unknowns are points to verify; only observed corrections claim a fix."""
    errors = []
    for flag in flags:
        severity = 'majeure' if flag in {
            'effectifs_invalides', 'pourcentage_invalide', 'empreinte_extrait_incoherente',
            'url_non_sure_ou_absente', 'date_recherche_absente_invalide_ou_future',
            'mesure_non_prevalence_ou_ambigue'} else 'information'
        errors.append({'code': flag, 'gravite': severity,
                       'nature': 'point_a_verifier', 'motif': flag.replace('_', ' '),
                       'candidat_id': candidate.get('id'), 'source': candidate.get('url'),
                       'corrigee': False})
    for correction in corrections:
        if not isinstance(correction, dict):
            continue
        errors.append({'code': 'arithmetique_corrigee', 'gravite': 'majeure',
                       'nature': 'correction_constatee', 'motif': correction.get('motif'),
                       'candidat_id': candidate.get('id'), 'source': candidate.get('url'),
                       'avant': correction.get('avant'), 'apres': correction.get('apres'),
                       'corrigee': True})
    return errors


def audit_candidate(candidate):
    """Return an audited copy; never infer a percentage from free text or an OR.

    Proof fields are exact quotations in ``extrait``. For arithmetic corrections,
    require preuve_{numerateur,denominateur,population,geographie,diagnostic}.
    This is a mechanical gate, not an assessment of clinical applicability.
    """
    if not isinstance(candidate, dict):
        return {'valeur_originale': copy.deepcopy(candidate), 'statut': 'candidat_a_relire',
                'audit': {'statut': 'À vérifier', 'flags': ['candidat_non_objet'],
                          'corrections': [], 'calcul_verifie': False, 'validation_clinique': False,
                          'erreurs': _structured_errors({}, ['candidat_non_objet'], [])}}
    out = copy.deepcopy(candidate)
    flags = []
    corrections = copy.deepcopy(out.get('audit', {}).get('corrections', [])) if isinstance(out.get('audit'), dict) else []
    if not isinstance(corrections, list):
        corrections = []
    def flag(name):
        if name not in flags:
            flags.append(name)
    if not _safe_url(out.get('url')):
        flag('url_non_sure_ou_absente')
    try:
        value = out.get('date_recherche')
        if not isinstance(value, str):
            raise ValueError
        day = date.fromisoformat(value[:10])
        if len(value) > 10:
            datetime.fromisoformat(value.replace('Z', '+00:00'))
        if day > datetime.now(timezone.utc).date():
            raise ValueError
    except (ValueError, TypeError):
        flag('date_recherche_absente_invalide_ou_future')
    excerpt = out.get('extrait')
    if not isinstance(excerpt, str) or not excerpt.strip():
        excerpt = ''
        flag('extrait_absent')
    if not out.get('provenance'):
        flag('provenance_absente')
    if not isinstance(out.get('sha256'), str) or not re.fullmatch(r'[a-fA-F0-9]{64}', out['sha256']):
        flag('empreinte_source_absente_ou_invalide')
    if out.get('sha256_extrait') and out['sha256_extrait'] != hashlib.sha256(excerpt.encode()).hexdigest():
        flag('empreinte_extrait_incoherente')
    # A numerical-looking abstract may report an association or incidence only.
    # Retain it as a lead while making that risk explicit, even without counts.
    if re.search(r'\b(incidence|odds|hazard|risk.ratio|relative risk)\b|\b(?:or|hr|rr)\s*[=:]?\s*\d', _normal(excerpt)):
        flag('extrait_contient_mesure_potentiellement_non_prevalence')
    stat = out.get('statistique')
    verified = False
    if stat is None:
        flag('statistique_non_structuree')
    elif not isinstance(stat, dict):
        flag('statistique_non_objet')
    else:
        study = out.get('meta_etude') if isinstance(out.get('meta_etude'), dict) else {}
        weighted_fields = [(stat, 'ponderee'), (stat, 'ponderation'), (study, 'echantillon_pondere')]
        if any(field in data and type(data[field]) is not bool for data, field in weighted_fields):
            flag('ponderation_non_explicitement_booleenne')
        if (any(data.get(field) is True for data, field in weighted_fields)
                or re.search(r'\b(?:weighted|pondere\w*)\b', _normal(excerpt))):
            flag('proportion_ponderee_non_recalculable_par_effectifs_bruts')
        n, d, pct = (_number(stat.get(k)) for k in ('numerateur', 'denominateur', 'pct'))
        if n is None or d is None or n != n.to_integral_value() or d != d.to_integral_value() or n < 0 or d <= 0 or n > d:
            flag('effectifs_invalides')
        if 'pct' in stat and (pct is None or pct < 0 or pct > 100):
            flag('pourcentage_invalide')
        decimals = stat.get('decimales', 2)
        if isinstance(decimals, bool) or not isinstance(decimals, int) or not 0 <= decimals <= 6:
            flag('precision_invalide')
        proofs = {}
        for name in ('numerateur', 'denominateur', 'population', 'geographie', 'diagnostic'):
            proofs[name] = _proof(stat, 'preuve_' + name, excerpt)
            if not proofs[name]:
                flag('preuve_' + name + '_absente_ou_non_verbatim')
        if n is not None and n >= 0 and n == n.to_integral_value() and proofs['numerateur'] and not _count_present(n, proofs['numerateur']):
            flag('numerateur_non_atteste')
        if d is not None and d >= 0 and d == d.to_integral_value() and proofs['denominateur'] and not _count_present(d, proofs['denominateur']):
            flag('denominateur_non_atteste')
        if stat.get('meme_population') is not True:
            flag('meme_population_non_attestee')
        if stat.get('type') not in ('consultation', 'population'):
            flag('cadre_statistique_a_verifier')
        if stat.get('geographie') not in ('CH', 'Europe'):
            flag('population_hors_CH_Europe_ou_inconnue')
        elif proofs['geographie'] and not _geography_supported(stat['geographie'], proofs['geographie']):
            flag('geographie_population_non_attestee_affiliation_insuffisante')
        if stat.get('origine_geographie') in ('affiliation', 'auteurs', 'editeur'):
            flag('geographie_issue_des_auteurs_pas_de_population')
        # Never turn incidence, odds, risk/hazard ratios, sensitivity or CI into prevalence.
        measure = _normal(stat.get('mesure', ''))
        risk = _normal(' '.join(str(proofs.get(k) or '') for k in proofs))
        bad = r'\b(incidence|incident cases|odds|odds.ratio|hazard|risk.ratio|relative risk|sensitiv\w*|specific\w*)\b|\b(?:or|hr|rr)\s*[=:]?\s*\d|\b(?:95\s*%?\s*(?:ci|ic)|(?:ci|ic)\s*95)\b'
        if re.search(bad, risk) or (measure and measure not in ('prevalence', 'proportion', 'proportion_diagnostique')):
            flag('mesure_non_prevalence_ou_ambigue')
        diagnostic = out.get('diagnostic')
        if diagnostic and proofs['diagnostic'] and _normal(diagnostic) not in _normal(proofs['diagnostic']):
            flag('diagnostic_non_atteste')
        # A bad current pct can be fixed only when all count/source gates pass.
        blocking = [f for f in flags if f != 'pourcentage_invalide']
        if not blocking:
            computed = (n * 100 / d).quantize(Decimal(1).scaleb(-decimals), rounding=ROUND_HALF_UP)
            verified = True
            if pct != computed:
                corrections.append({'champ': 'statistique.pct', 'avant': stat.get('pct'),
                                    'apres': float(computed), 'motif': '100 × numerateur / denominateur ; arrondi decimal HALF_UP'})
                stat['pct'] = float(computed)
                flags = [f for f in flags if f != 'pourcentage_invalide']
    # Even perfect arithmetic leaves clinical/geographic transfer for explicit review.
    out['statut'] = 'candidat_a_relire'
    out['audit'] = {'statut': 'À vérifier', 'flags': flags, 'corrections': corrections,
                    'calcul_verifie': verified, 'validation_clinique': False,
                    'erreurs': _structured_errors(out, flags, corrections)}
    return out


def audit_state(state):
    """Audit a category snapshot without mutating the caller, return (copy, report)."""
    result = copy.deepcopy(state)
    report = {'categorie': result.get('category'), 'candidats': 0, 'calculs_verifies': 0,
              'candidats_a_verifier': 0, 'corrections_nouvelles': 0, 'flags': {},
              'validation_clinique': False, 'erreurs_etat': []}
    tasks = result.get('tasks', {})
    if not isinstance(tasks, dict):
        report['erreurs_etat'].append('tasks_non_objet')
        return result, report
    for key, task in tasks.items():
        if not isinstance(task, dict) or not isinstance(task.get('candidates', []), list):
            report['erreurs_etat'].append(str(key) + ':candidats_invalides')
            continue
        audited = []
        for candidate in task.get('candidates', []):
            prior = candidate.get('audit', {}).get('corrections', []) if isinstance(candidate, dict) and isinstance(candidate.get('audit'), dict) else []
            old_count = len(prior) if isinstance(prior, list) else 0
            original = copy.deepcopy(candidate)
            if isinstance(original, dict) and 'diagnostic' not in original and task.get('diagnostic'):
                original['diagnostic'] = task['diagnostic']
            checked = audit_candidate(original)
            audited.append(checked)
            audit = checked['audit']
            report['candidats'] += 1
            report['calculs_verifies'] += int(audit['calcul_verifie'])
            report['candidats_a_verifier'] += 1
            report['corrections_nouvelles'] += max(0, len(audit['corrections']) - old_count)
            for flag in audit['flags']:
                report['flags'][flag] = report['flags'].get(flag, 0) + 1
        task['candidates'] = audited
    return result, report


def _atomic_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix='.' + path.name, suffix='.tmp', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as out:
            json.dump(data, out, ensure_ascii=False, indent=2, allow_nan=False)
            out.write('\n')
            out.flush()
            os.fsync(out.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--state-dir', type=Path, required=True)
    parser.add_argument('--check', action='store_true', help='lecture seule ; code 1 si audit à appliquer')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args(argv)
    summaries, changed = [], False
    if not args.state_dir.is_dir():
        parser.error('state-dir doit être un répertoire existant')
    # Reject a report pointing at an existing state before writing any category.
    if args.report and args.report.exists():
        try:
            report_target = json.loads(args.report.read_text(encoding='utf-8'))
        except (OSError, ValueError):
            report_target = None
        if isinstance(report_target, dict) and 'tasks' in report_target:
            parser.error('report doit être distinct des fichiers état')
    paths = sorted(args.state_dir.glob('*.json'))
    for path in paths:
        try:
            state = json.loads(path.read_text(encoding='utf-8'))
            if not isinstance(state, dict) or 'tasks' not in state:
                continue
            if args.report and path.resolve() == args.report.resolve():
                parser.error('report doit être distinct des fichiers état')
            updated, report = audit_state(state)
            report['fichier'] = path.name
            summaries.append(report)
            if updated != state:
                changed = True
                if not args.check:
                    _atomic_json(path, updated)
        except (OSError, ValueError, TypeError) as exc:
            summaries.append({'fichier': path.name, 'erreur': str(exc)})
    payload = {'role': 'Auditeur statistique', 'validation_clinique': False,
               'categories': summaries, 'changements_necessaires': changed}
    if args.report and not args.check:
        _atomic_json(args.report, payload)
    print(json.dumps(payload, ensure_ascii=False, allow_nan=False))
    return 1 if any('erreur' in x or x.get('erreurs_etat') for x in summaries) or (args.check and changed) else 0


if __name__ == '__main__':
    raise SystemExit(main())
