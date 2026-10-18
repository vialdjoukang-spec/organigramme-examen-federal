#!/usr/bin/env python3
"""Sélection entre études : validité avant taille, jamais publication automatique."""
import copy
import hashlib
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.prevalences.selection import selectionner, wilson_interval


def registry():
    return {'version': 1, 'sources': [{'id': 'HUG', 'domaines': ['hug.ch'], 'verified': True,
            'niveau_reconnaissance': 1, 'reference_reconnaissance': 'https://www.hug.ch/',
            'date_verification': '2026-01-01'}]}


def candidate(identity='a', n=50, denominator=500, risk='faible', evidence=2):
    excerpt = (f'Among {denominator} adult patients recruited in Switzerland for pruritus, '
               f'{n} patients had eczema. Both counts describe the same cohort. '
               f'The final analysis included {denominator} patients. '
               'Random sample; complete follow-up and predefined diagnosis.')
    digest = hashlib.sha256(excerpt.encode()).hexdigest()
    url = 'https://www.hug.ch/study-' + identity
    return {'id': identity, 'url': url, 'extrait': excerpt, 'sha256': digest,
            'date_recherche': '2026-01-01', 'provenance': 'hug', 'diagnostic': 'eczema',
            'statut': 'candidat_a_relire', 'statistique': {
                'numerateur': n, 'denominateur': denominator, 'pct': n*100/denominator,
                'decimales': 2, 'type': 'consultation', 'mesure': 'proportion_diagnostique',
                'geographie': 'CH', 'meme_population': True,
                'preuve_numerateur': f'{n} patients had eczema',
                'preuve_denominateur': f'{denominator} adult patients',
                'preuve_population': 'Both counts describe the same cohort.',
                'preuve_geographie': f'{denominator} adult patients recruited in Switzerland',
                'preuve_diagnostic': f'{n} patients had eczema'},
            'meta_etude': {'source_id': 'HUG', 'population': 'adultes consultant pour prurit',
                'definition_diagnostic': 'eczema confirmé', 'cadre': 'consultation',
                'age': '18–65 ans', 'pays': 'CH', 'periode': '2020–2024',
                'type_echantillonnage': 'aléatoire', 'methodologie': 'étude transversale',
                'niveau_preuve': evidence, 'risque_biais': risk,
                'preuve_qualite': 'Random sample; complete follow-up and predefined diagnosis.',
                'denominateur_analyse': denominator,
                'preuve_denominateur_analyse': f'The final analysis included {denominator} patients.',
                'echantillon_pondere': False, 'grappes': False,
                'comparabilite': {'cle': 'eczema-prurit-adultes', 'attestee': True,
                                 'preuve': 'Même définition, âge, cadre et période relus.',
                                 'methode': 'comparaison documentaire des protocoles'},
                'relecture_documentaire': {'statut': 'terminee', 'date': '2026-01-01',
                     'verdict': 'prêt_relecture_clinique', 'source': url, 'sha256': digest,
                     'loc': 'Tableau 1 et méthodes', 'extrait': excerpt, 'validation_clinique': False}}}


def codes(result):
    return {e['code'] for e in result['erreurs']}


class StudySelection(unittest.TestCase):
    def test_representative_500_beats_biased_10000_with_same_source(self):
        smaller = candidate('representatif', denominator=500)
        larger = candidate('biais', denominator=10000, risk='eleve')
        result = selectionner([larger, smaller], registry())
        self.assertEqual(result['retenu'], 'representatif')
        self.assertFalse(result['validation_clinique'])
        self.assertFalse(result['publication_automatique'])

    def test_at_equal_quality_5000_beats_500(self):
        result = selectionner([candidate('petit'), candidate('grand', denominator=5000)], registry())
        self.assertEqual(result['retenu'], 'grand')

    def test_recognition_before_n_without_implying_medical_validation(self):
        r = registry(); r['sources'].append(dict(r['sources'][0], id='AUTRE', niveau_reconnaissance=2))
        larger = candidate('grand', denominator=5000); larger['meta_etude']['source_id'] = 'AUTRE'
        result = selectionner([candidate('reconnu'), larger], r)
        self.assertEqual(result['retenu'], 'reconnu')

    def test_unrecognized_source_never_wins_on_n(self):
        unknown = candidate('inconnu', denominator=10000); unknown['meta_etude']['source_id'] = 'MISSING'
        result = selectionner([unknown, candidate('connu')], registry())
        self.assertEqual(result['retenu'], 'connu')
        self.assertIn('source_non_reconnue_ou_non_attestee', codes(result))

    def test_verified_flag_requires_dated_editorial_evidence(self):
        for field in ('date_verification', 'reference_reconnaissance'):
            r = registry(); r['sources'][0].pop(field)
            self.assertIsNone(selectionner([candidate()], r)['retenu'])
        r = registry(); r['sources'][0]['verified'] = False
        self.assertIsNone(selectionner([candidate()], r)['retenu'])

    def test_population_age_definition_period_cadre_are_not_interchangeable(self):
        for field, value in [('population', 'enfants hospitalisés'), ('age', '0–17 ans'),
                             ('definition_diagnostic', 'diagnostic auto-déclaré'), ('periode', '1990–1995')]:
            with self.subTest(field=field):
                other = candidate('other', denominator=5000); other['meta_etude'][field] = value
                result = selectionner([candidate(), other], registry())
                self.assertIsNone(result['retenu'])
                self.assertIn('populations_non_comparables', codes(result))
                self.assertEqual(len(result['suggestions_par_groupe']), 2)

    def test_geography_must_be_compared_explicitly(self):
        other = candidate('other'); other['meta_etude']['pays'] = 'France'
        other['extrait'] = other['extrait'].replace('Switzerland', 'France')
        other['sha256'] = hashlib.sha256(other['extrait'].encode()).hexdigest()
        other['statistique']['geographie'] = 'Europe'
        other['statistique']['preuve_geographie'] = other['statistique']['preuve_geographie'].replace('Switzerland', 'France')
        other['meta_etude']['relecture_documentaire'].update(extrait=other['extrait'], sha256=other['sha256'])
        result = selectionner([candidate(), other], registry())
        self.assertIsNone(result['retenu'])
        self.assertIn('populations_non_comparables', codes(result))

    def test_country_metadata_cannot_contradict_participants_source_proof(self):
        c = candidate(); c['meta_etude']['pays'] = 'France'
        result = selectionner([c], registry())
        self.assertIsNone(result['retenu'])
        self.assertIn('geographie_non_attestee', codes(result))

    def test_comparability_key_without_attestation_never_suffices(self):
        c = candidate(); c['meta_etude']['comparabilite']['attestee'] = 'true'
        result = selectionner([c], registry())
        self.assertIsNone(result['retenu'])
        self.assertIn('comparabilite_non_attestee', codes(result))

    def test_n_is_analyzed_denominator_not_worldwide_or_enrolled_sample(self):
        c = candidate(); c['meta_etude']['denominateur_analyse'] = 10000000
        self.assertIn('denominateur_analyse_non_atteste', codes(selectionner([c], registry())))
        c = candidate(); c['meta_etude']['preuve_denominateur_analyse'] = '500000 enrolled'
        self.assertIsNone(selectionner([c], registry())['retenu'])

    def test_incidence_or_hr_and_therapy_are_not_prevalence(self):
        for measure in ('incidence', 'OR', 'HR', 'reduction_risque_therapeutique'):
            c = candidate(); c['statistique']['mesure'] = measure
            result = selectionner([c], registry())
            self.assertIsNone(result['retenu'])
            self.assertIn('mesure_non_conditionnelle_ou_inconnue', codes(result))

    def test_weighted_or_clustered_sample_needs_effective_n_and_variance(self):
        for field in ('echantillon_pondere', 'grappes'):
            c = candidate(); c['meta_etude'][field] = True
            result = selectionner([c], registry())
            self.assertIsNone(result['retenu'])
            self.assertIn('precision_plan_complexe_non_attestee', codes(result))

    def test_clustered_precision_uses_attested_effective_n_and_no_binomial_ci(self):
        c = candidate('cluster', denominator=10000)
        extra = ' Design-adjusted effective sample size was 100.'
        c['extrait'] += extra
        c['sha256'] = hashlib.sha256(c['extrait'].encode()).hexdigest()
        meta = c['meta_etude']
        meta.update(grappes=True, n_effectif=100, variance_corrigee_plan=True,
                    preuve_n_effectif='effective sample size was 100.')
        meta['relecture_documentaire'].update(extrait=c['extrait'], sha256=c['sha256'])
        result = selectionner([c, candidate('simple500')], registry())
        self.assertEqual(result['retenu'], 'simple500')
        cluster = next(x for x in result['comparaisons'] if x['candidat_id'] == 'cluster')
        self.assertTrue(cluster['eligible'])
        self.assertEqual(cluster['n_pour_comparaison_precision'], 100)
        self.assertIsNone(cluster['intervalle_wilson_calcule'])

    def test_published_rounding_is_not_a_false_arithmetic_error(self):
        c = candidate(n=1, denominator=6)
        c['statistique'].update(pct=16.7, decimales=1)
        result = selectionner([c], registry())
        self.assertEqual(result['retenu'], 'a')
        self.assertNotIn('arithmetique_corrigee_pour_comparaison', codes(result))

    def test_simple_wilson_keeps_original_interval_separate(self):
        c = candidate(); original = {'borne_inferieure_pct': 8, 'borne_superieure_pct': 12, 'methode': 'source'}
        c['statistique']['intervalle_confiance'] = original
        result = selectionner([c], registry())
        item = next(x for x in result['comparaisons'] if x['eligible'])
        self.assertEqual(item['intervalle_original'], original)
        calculated = item['intervalle_wilson_calcule']
        self.assertLess(calculated['borne_inferieure_pct'], 10)
        self.assertGreater(calculated['borne_superieure_pct'], 10)
        self.assertEqual(c['statistique']['intervalle_confiance'], original)

    def test_zero_count_valid_and_wilson_nonnegative(self):
        result = selectionner([candidate(n=0)], registry())
        self.assertEqual(result['retenu'], 'a')
        interval = wilson_interval(0, 100)
        self.assertGreaterEqual(interval['borne_inferieure_pct'], 0)
        self.assertGreater(interval['borne_superieure_pct'], 0)
        for args in ((True, 100), (0, 0), (101, 100), (1.5, 100)):
            with self.assertRaises(ValueError): wilson_interval(*args)

    def test_arithmetic_correction_is_traced_and_input_not_mutated(self):
        c = candidate(); c['statistique']['pct'] = 99
        original = copy.deepcopy(c)
        result = selectionner([c], registry())
        self.assertEqual(result['retenu'], 'a')
        err = next(e for e in result['erreurs'] if e['code'] == 'arithmetique_corrigee_pour_comparaison')
        self.assertEqual((err['avant'], err['apres']), (99, 10))
        self.assertTrue(err['corrigee'])
        self.assertEqual(c, original)

    def test_historical_correction_not_claimed_as_new(self):
        c = candidate(); c['audit'] = {'corrections': [{'champ': 'statistique.pct', 'avant': 99, 'apres': 10, 'motif': 'ancien'}]}
        self.assertNotIn('arithmetique_corrigee_pour_comparaison', codes(selectionner([c], registry())))

    def test_stable_tie_does_not_depend_on_discovery_order(self):
        a, b = candidate('a'), candidate('b')
        self.assertEqual(selectionner([a, b], registry())['retenu'], 'a')
        self.assertEqual(selectionner([b, a], registry())['retenu'], 'a')

    def test_duplicate_does_not_inflate_sample_size(self):
        result = selectionner([candidate(), candidate()], registry())
        self.assertEqual(result['retenu'], 'a')
        self.assertIn('identite_dupliquee', codes(result))
        self.assertEqual(len(result['comparaisons']), 1)

    def test_conflicting_duplicate_identity_never_chooses_first_discovery(self):
        for field in ('url', 'meta_etude', 'statistique'):
            a = candidate(); b = copy.deepcopy(a)
            if field == 'url': b['url'] = 'https://www.hug.ch/other'
            elif field == 'meta_etude': b['meta_etude']['age'] = 'enfants'
            else: b['statistique']['pct'] = 20
            for rows in ([a, b], [b, a]):
                result = selectionner(rows, registry())
                self.assertIsNone(result['retenu'])
                self.assertIn('identite_dupliquee_ambigue', codes(result))

    def test_effective_n_bool_nan_and_huge_numeric_exponents_rejected(self):
        for value in (True, 'NaN', float('inf'), '1e1000000', '9' * 10000):
            c = candidate(); c['meta_etude'].update(grappes=True, n_effectif=value,
                    variance_corrigee_plan=True, preuve_n_effectif='not documented')
            result = selectionner([c], registry())
            self.assertIsNone(result['retenu'])
            self.assertIn('precision_plan_complexe_non_attestee', codes(result))
        for value in ('1e1000000', '1e-1000000'):
            with self.assertRaises(ValueError): wilson_interval(1, value)

    def test_domain_mimic_and_unattested_doi_trace_rejected(self):
        for url in ('https://hug.ch.evil.example/study', 'https://doi.org/10.1234/example'):
            c = candidate(); c['url'] = url; c['meta_etude']['relecture_documentaire']['source'] = url
            result = selectionner([c], registry())
            self.assertIsNone(result['retenu'])
            self.assertIn('source_primaire_non_reliee', codes(result))

    def test_doi_can_link_to_official_primary_source_with_explicit_trace(self):
        c = candidate(); c['doi'] = '10.1234/example'; c['url'] = 'https://doi.org/' + c['doi']
        review = c['meta_etude']['relecture_documentaire']
        review.update(source=c['url'], source_primaire='https://www.hug.ch/study',
                      preuve_tracabilite='La page officielle HUG cite explicitement le DOI 10.1234/example.')
        self.assertEqual(selectionner([c], registry())['retenu'], 'a')

    def test_unresolved_or_inapplicable_agent_review_prevents_selection(self):
        for change in ({'verdict': 'À vérifier'}, {'verdict': 'à corriger'},
                       {'applicable_au_dd_dans_ce_cadre': False}):
            c = candidate(); c['meta_etude']['relecture_documentaire'].update(change)
            result = selectionner([c], registry())
            self.assertIsNone(result['retenu'])
            self.assertIn('relecture_documentaire_non_favorable', codes(result))

    def test_ambiguous_registry_identity_does_not_pick_first_source(self):
        r = registry(); r['sources'].append(dict(r['sources'][0], verified=False))
        self.assertIsNone(selectionner([candidate()], r)['retenu'])

    def test_malformed_review_quality_and_source_metadata_are_flags_not_tracebacks(self):
        for field, value in (('risque_biais', []), ('source_id', []), ('relecture_documentaire', {'extrait': 1})):
            with self.subTest(field=field):
                c = candidate(); c['meta_etude'][field] = value
                self.assertIsNone(selectionner([c], registry())['retenu'])
        c = candidate(); c['audit'] = {'corrections': 'malformed'}; c['statistique']['pct'] = 99
        self.assertIn('arithmetique_corrigee_pour_comparaison', codes(selectionner([c], registry())))

    def test_metadata_and_quality_cannot_be_inferred_from_journal(self):
        for field in ('preuve_qualite', 'relecture_documentaire', 'population'):
            c = candidate(); c['meta_etude'].pop(field)
            self.assertIsNone(selectionner([c], registry())['retenu'])


if __name__ == '__main__':
    unittest.main()
