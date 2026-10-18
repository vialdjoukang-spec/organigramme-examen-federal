#!/usr/bin/env python3
"""Sélection documentaire prudente entre estimations comparables.

Ordre : admissibilité, reconnaissance éditoriale attestée, qualité de l'étude,
puis dénominateur effectivement analysé. Ne publie aucune donnée clinique,
ne combine jamais des prévalences et ne déduit aucune comparabilité de N.
"""
from __future__ import annotations

from datetime import date
from decimal import Decimal, InvalidOperation
import math
import re
from urllib.parse import urlsplit

from tools.prevalences.auditeur import audit_candidate
from tools.prevalences.relance_agent import review_completed

QUALITY = {'faible': 0, 'modere': 1, 'modéré': 1, 'eleve': 2, 'élevé': 2}
META_FIELDS = ('population', 'definition_diagnostic', 'cadre', 'age', 'pays', 'periode',
               'type_echantillonnage', 'methodologie')
# Pays d'Europe ; une affiliation, une publication ou un domaine ne les prouve pas.
EUROPE = {'europe', 'ch', 'suisse', 'switzerland', 'fr', 'france', 'de', 'germany', 'allemagne',
          'it', 'italy', 'italie', 'es', 'spain', 'espagne', 'be', 'belgium', 'belgique',
          'nl', 'netherlands', 'pays-bas', 'at', 'austria', 'autriche', 'gb', 'uk',
          'united kingdom', 'royaume-uni', 'ie', 'ireland', 'irlande', 'pt', 'portugal',
          'dk', 'denmark', 'danemark', 'se', 'sweden', 'suede', 'suède', 'no', 'norway',
          'norvege', 'norvège', 'fi', 'finland', 'finlande', 'pl', 'poland', 'pologne',
          'gr', 'greece', 'grece', 'grèce', 'cz', 'czechia', 'tchequie', 'tchéquie',
          'ro', 'romania', 'roumanie', 'hu', 'hungary', 'hongrie', 'hr', 'croatia',
          'croatie', 'si', 'slovenia', 'slovénie', 'sk', 'slovakia', 'slovaquie',
          'ee', 'estonia', 'estonie', 'lv', 'latvia', 'lettonie', 'lt', 'lithuania',
          'lituanie', 'bg', 'bulgaria', 'bulgarie', 'lu', 'luxembourg', 'mt', 'malta',
          'malte', 'cy', 'cyprus', 'chypre', 'is', 'iceland', 'islande', 'li', 'liechtenstein'}


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float, str, Decimal)):
        return None
    try:
        token = str(value)
        if len(token) > 256:
            return None
        number = Decimal(token)
        if number.is_zero():
            return Decimal(0)
        return number if number.is_finite() and abs(number.adjusted()) <= 100 else None
    except (InvalidOperation, ValueError, OverflowError):
        return None


def _date(value):
    try:
        return isinstance(value, str) and date.fromisoformat(value) <= date.today()
    except ValueError:
        return False


def _host(url):
    try:
        parsed = urlsplit(url)
        if parsed.scheme not in ('https', 'http') or parsed.username or parsed.password:
            return None
        return parsed.hostname.lower().rstrip('.') if parsed.hostname else None
    except (ValueError, TypeError, AttributeError):
        return None


def _domain_matches(url, domains):
    host = _host(url)
    return bool(host and any(isinstance(d, str) and (host == d.lower().rstrip('.') or
                host.endswith('.' + d.lower().rstrip('.'))) for d in domains if d))



def _country_supported(country, proof):
    aliases = [
        {'ch', 'suisse', 'switzerland', 'swiss', 'schweiz', 'svizzera'},
        {'fr', 'france', 'french'}, {'de', 'germany', 'german', 'allemagne'},
        {'it', 'italy', 'italian', 'italie'}, {'es', 'spain', 'spanish', 'espagne'},
        {'gb', 'uk', 'united kingdom', 'british', 'england', 'royaume-uni'},
        {'nl', 'netherlands', 'dutch', 'pays-bas'}, {'be', 'belgium', 'belgian', 'belgique'},
        {'at', 'austria', 'austrian', 'autriche'}, {'ie', 'ireland', 'irish', 'irlande'},
        {'europe', 'european', 'europeenne', 'européenne'},
    ]
    country = str(country).casefold()
    words = next((group for group in aliases if country in group), {country})
    # The proof for the participants' geography, not affiliations elsewhere.
    return any(len(word) > 2 and re.search(r'(?<!\w)' + re.escape(word) + r'(?!\w)', proof.casefold()) for word in words)


def _registry_source(registry, identity):
    if not _text(identity) or not isinstance(registry, dict) or registry.get('version') != 1:
        return None
    sources = registry.get('sources', [])
    if isinstance(sources, dict):
        return sources.get(identity)
    if not isinstance(sources, list):
        return None
    matches = [source for source in sources if isinstance(source, dict) and source.get('id') == identity]
    return matches[0] if matches and all(source == matches[0] for source in matches) else None


def _editorial_proof(source):
    proof = source.get('preuve_reconnaissance')
    reference = source.get('reference_reconnaissance')
    checked = source.get('date_verification')
    if isinstance(proof, dict):
        reference = reference or proof.get('url')
        checked = checked or proof.get('date') or proof.get('date_lu')
    elif isinstance(proof, str):
        reference = reference or proof
    return bool(_host(reference) and _date(checked))


def _proof_number(number, proof, excerpt):
    if not _text(proof) or not isinstance(excerpt, str) or proof not in excerpt:
        return False
    # Only exact numeric tokens, not 500 in 5000 or an unquoted assertion.
    tokens = re.findall(r'(?<![\w.,])\d+(?:[.,]\d+)?(?!\w|[.,]\d)', proof)
    return any(_number(token.replace(',', '.')) == number for token in tokens)


def wilson_interval(numerator, denominator):
    """Mechanical 95% binomial interval for simple unweighted counts only."""
    if isinstance(numerator, bool) or isinstance(denominator, bool):
        raise ValueError('Effectifs entiers attendus')
    n, d = _number(numerator), _number(denominator)
    if n is None or d is None or n != int(n) or d != int(d) or not 0 <= n <= d or d <= 0:
        raise ValueError('Effectifs invalides')
    z = 1.959963984540054
    p = float(n / d); sample = float(d)
    divisor = 1 + z*z/sample
    centre = (p + z*z/(2*sample)) / divisor
    radius = z * math.sqrt(p*(1-p)/sample + z*z/(4*sample*sample)) / divisor
    return {'niveau': 0.95, 'methode': 'Wilson binomial non pondéré',
            'borne_inferieure_pct': max(0, 100*(centre-radius)),
            'borne_superieure_pct': min(100, 100*(centre+radius)),
            'validation_clinique': False}


def selectionner(candidates, registry):
    """Return a reviewable documentary selection, without mutating candidates.

    ``meta_etude.comparabilite`` requires cle/attestee/preuve/methode. Its
    geographie field may name an explicitly assessed geographic equivalence;
    otherwise countries remain separate. Population, diagnostic definition,
    setting, age and period must also match. A key alone never overrides them.
    """
    errors, comparisons, eligible = [], [], []
    result = {'retenu': None, 'raison': '', 'comparaisons': comparisons, 'erreurs': errors,
              'validation_clinique': False, 'publication_automatique': False}
    if not isinstance(candidates, list):
        result['raison'] = 'Liste de candidats attendue.'
        errors.append({'code': 'candidats_invalides', 'gravite': 'majeure', 'motif': result['raison'],
                       'candidat_id': None, 'source': None, 'corrigee': False})
        return result
    # Identical rediscoveries count once. Conflicting identities are excluded
    # entirely, so discovery order cannot choose their source or population.
    identity_groups = {}
    for candidate in candidates:
        if isinstance(candidate, dict) and _text(candidate.get('id')):
            identity_groups.setdefault(candidate['id'], []).append(candidate)
    semantic_fields = ('url', 'sha256', 'extrait', 'diagnostic', 'statistique', 'meta_etude')
    ambiguous_ids = {cid for cid, rows in identity_groups.items() if any(
        any(row.get(field) != rows[0].get(field) for field in semantic_fields) for row in rows[1:])}
    ids = set()
    for candidate in candidates:
        cid = candidate.get('id') if isinstance(candidate, dict) else None
        url = candidate.get('url') if isinstance(candidate, dict) else None
        issues = []
        def error(code, reason, severity='majeure', **extra):
            entry = {'code': code, 'gravite': severity, 'motif': reason, 'candidat_id': cid,
                     'source': url, 'corrigee': False, **extra}
            issues.append(entry); errors.append(entry)
        if not isinstance(candidate, dict) or not _text(cid):
            error('identite_absente', 'Le candidat ne porte pas une identité documentaire stable.')
            continue
        if cid in ambiguous_ids:
            error('identite_dupliquee_ambigue', 'Le même identifiant désigne des sources, valeurs ou populations différentes ; tous ses exemplaires restent à vérifier.')
            continue
        if cid in ids:
            error('identite_dupliquee', 'Une identité dupliquée ne reçoit pas deux voix dans la sélection.', severity='information')
            continue
        ids.add(cid)
        audited = audit_candidate(candidate)
        audit = audited['audit']
        if not audit['calcul_verifie']:
            error('chiffre_non_atteste', 'Numérateur, dénominateur, population, diagnostic et mesure doivent être attestés.', flags=audit['flags'])
        original_stat = candidate.get('statistique')
        stat = audited.get('statistique')
        if not isinstance(stat, dict):
            continue
        for correction in audit['corrections']:
            # Historical corrections are not presented as newly made here.
            previous = candidate.get('audit', {}).get('corrections', []) if isinstance(candidate.get('audit'), dict) else []
            if not isinstance(previous, list):
                previous = []
            if correction not in previous:
                errors.append({'code': 'arithmetique_corrigee_pour_comparaison', 'gravite': 'majeure',
                               'motif': correction['motif'], 'candidat_id': cid, 'source': url,
                               'avant': correction.get('avant'), 'apres': correction.get('apres'), 'corrigee': True})
        if stat.get('mesure') not in ('prevalence', 'proportion_diagnostique'):
            error('mesure_non_conditionnelle_ou_inconnue', 'Seule une prévalence ou proportion diagnostique explicitement identifiée est comparable.')
        meta = candidate.get('meta_etude')
        if not isinstance(meta, dict):
            error('metadonnees_etude_absentes', 'Le N le plus élevé ne suffit pas sans description de l’étude.')
            continue
        missing = [key for key in META_FIELDS if not _text(meta.get(key))]
        if missing:
            error('metadonnees_etude_incompletes', 'Champs d’étude manquants : ' + ', '.join(missing))
        if meta.get('cadre') != stat.get('type'):
            error('cadre_incoherent', 'Le cadre de l’étude diffère de celui du pourcentage.')
        if str(meta.get('pays', '')).lower() not in EUROPE or not _country_supported(meta.get('pays'), str(stat.get('preuve_geographie', ''))):
            error('geographie_non_attestee', 'Le pays étudié CH/Europe doit être explicite ; le pays de l’éditeur ne le remplace pas.')
        review = meta.get('relecture_documentaire') or candidate.get('relecture_agent')
        documentary_candidate = dict(candidate, relecture_agent=review)
        if not review_completed(documentary_candidate):
            error('relecture_documentaire_absente', 'Une relecture complète, datée et liée à l’empreinte de la source est requise.')
        if isinstance(review, dict) and (review.get('verdict') != 'prêt_relecture_clinique' or review.get('applicable_au_dd_dans_ce_cadre') is False):
            error('relecture_documentaire_non_favorable', 'Une réserve documentaire explicite doit être levée avant la sélection, même si N est élevé.')
        source = _registry_source(registry, meta.get('source_id'))
        recognition = source.get('niveau_reconnaissance') if isinstance(source, dict) else None
        if not isinstance(source, dict) or source.get('verified') is not True or not _editorial_proof(source) or type(recognition) is not int or not 1 <= recognition <= 3:
            error('source_non_reconnue_ou_non_attestee', 'La reconnaissance scientifique doit être vérifiée dans le registre, avec sa preuve éditoriale datée.')
        else:
            domains = source.get('domaines', [source['domain']] if source.get('domain') else [])
            if isinstance(domains, str):
                domains = [domains]
            if not isinstance(domains, (list, tuple)):
                domains = []
            primary = review.get('source_primaire') if isinstance(review, dict) else None
            if not _domain_matches(url, domains):
                trace = review.get('preuve_tracabilite') if isinstance(review, dict) else None
                doi = candidate.get('doi')
                if not (_domain_matches(primary, domains) and _text(doi) and _text(trace) and doi.lower() in trace.lower()):
                    error('source_primaire_non_reliee', 'Un DOI ou un miroir exige une source primaire reconnue et une trace documentaire du DOI vers cette source.')
        n = _number(meta.get('denominateur_analyse'))
        d = _number(stat.get('denominateur'))
        review_excerpt = review.get('extrait', '') if isinstance(review, dict) else ''
        if not isinstance(review_excerpt, str):
            review_excerpt = ''
        if n is None or n <= 0 or n != n.to_integral_value() or n != d or not _proof_number(n, meta.get('preuve_denominateur_analyse'), review_excerpt):
            error('denominateur_analyse_non_atteste', 'N doit être le dénominateur effectivement analysé de cette proportion, attesté dans la source, pas le nombre recruté ou mondial.')
        if type(meta.get('echantillon_pondere')) is not bool or type(meta.get('grappes')) is not bool:
            error('plan_echantillonnage_inconnu', 'Préciser si la proportion est pondérée ou issue d’un plan en grappes.')
        complex_design = meta.get('echantillon_pondere') is True or meta.get('grappes') is True
        effective_n = n
        if complex_design:
            effective_n = _number(meta.get('n_effectif'))
            if effective_n is None or n is None or not 0 < effective_n <= n or meta.get('variance_corrigee_plan') is not True or not _proof_number(effective_n, meta.get('preuve_n_effectif'), review_excerpt):
                error('precision_plan_complexe_non_attestee', 'Une étude pondérée/en grappes exige N effectif et correction de variance attestés ; N brut ne prouve pas sa précision.')
        evidence = meta.get('niveau_preuve')
        bias = meta.get('risque_biais')
        if type(evidence) is not int or not 1 <= evidence <= 5 or not isinstance(bias, str) or bias not in QUALITY:
            error('qualite_etude_non_attestee', 'Niveau de preuve (1–5) et risque de biais (faible/modéré/élevé) doivent être explicitement relus.')
        if not _text(meta.get('preuve_qualite')) or meta['preuve_qualite'] not in review_excerpt:
            error('preuve_qualite_absente', 'Le jugement de qualité doit citer les méthodes réellement relues, pas seulement le nom d’un éditeur.')
        comparable = meta.get('comparabilite')
        if not isinstance(comparable, dict) or comparable.get('attestee') is not True or any(not _text(comparable.get(k)) for k in ('cle', 'preuve', 'methode')) or ('geographie' in comparable and not _text(comparable['geographie'])):
            error('comparabilite_non_attestee', 'Une clé de comparabilité accompagnée de son attestation et de sa méthode est requise.')
        if issues:
            comparisons.append({'candidat_id': cid, 'eligible': False, 'motifs': [e['code'] for e in issues]})
            continue
        # A manually attested geographic equivalence is explicit; no inferred
        # equivalence from a European author, domain or large sample.
        geography = comparable.get('geographie') or meta['pays']
        signature = tuple(str(v).strip().casefold() for v in (comparable['cle'], meta['population'],
                          meta['definition_diagnostic'], meta['cadre'], meta['age'], meta['periode'], geography, stat['mesure']))
        quality = (recognition, QUALITY[bias], evidence)
        item = {'candidat_id': cid, 'eligible': True, 'groupe': list(signature),
                'qualite': {'niveau_reconnaissance_source': recognition, 'risque_biais': bias,
                            'niveau_preuve': evidence, 'methodologie': meta['methodologie']},
                'n_analyse': int(n), 'n_pour_comparaison_precision': float(effective_n),
                'pourcentage_publie': original_stat.get('pct'), 'pourcentage_recalcule': stat['pct'],
                'provenance': {'url': url, 'source_id': meta['source_id'], 'sha256': candidate['sha256'],
                               'loc': review['loc'], 'date_relecture': review['date']},
                'intervalle_original': original_stat.get('intervalle_confiance'),
                'intervalle_wilson_calcule': None if complex_design else wilson_interval(stat['numerateur'], stat['denominateur'])}
        comparisons.append(item)
        eligible.append((signature, quality, effective_n, cid, item))
    groups = {}
    for entry in eligible:
        groups.setdefault(entry[0], []).append(entry)
    suggestions = []
    for signature, entries in groups.items():
        ranked = sorted(entries, key=lambda e: (e[1], -e[2], e[3]))
        suggestions.append({'groupe': list(signature), 'suggestion': ranked[0][3],
                            'classement': [e[3] for e in ranked]})
    result['suggestions_par_groupe'] = suggestions
    if not groups:
        result['raison'] = 'Aucune estimation admissible et documentée ; À vérifier.'
    elif len(groups) > 1:
        result['raison'] = 'Populations ou définitions non comparables ; aucune valeur globale retenue.'
        errors.append({'code': 'populations_non_comparables', 'gravite': 'majeure', 'motif': result['raison'],
                       'candidat_id': None, 'source': None, 'corrigee': False})
    else:
        result['retenu'] = suggestions[0]['suggestion']
        result['raison'] = 'Candidat documentaire retenu : source reconnue, qualité scientifique, puis N analysé/précision ; relecture clinique toujours requise.'
    return result
