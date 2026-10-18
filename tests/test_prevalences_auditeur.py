#!/usr/bin/env python3
"""Cas limites statistiques et contrat de non-publication de l'auditeur."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'tools/prevalences/auditeur.py'
spec = importlib.util.spec_from_file_location('auditeur_prevalences', SCRIPT)
A = importlib.util.module_from_spec(spec)
spec.loader.exec_module(A)


def candidate():
    excerpt = ('Among 200 patients recruited in Switzerland for pruritus, '
               '25 patients had eczema. Both counts describe the same cohort.')
    return {'id': 'test', 'url': 'https://example.org/study', 'title': 'Étude',
            'extrait': excerpt, 'sha256': hashlib.sha256(excerpt.encode()).hexdigest(),
            'sha256_extrait': hashlib.sha256(excerpt.encode()).hexdigest(),
            'date_recherche': '2026-01-01', 'provenance': 'source_lue',
            'diagnostic': 'eczema', 'statut': 'candidat_a_relire',
            'statistique': {'numerateur': 25, 'denominateur': 200, 'pct': 99,
                           'decimales': 2, 'meme_population': True,
                           'geographie': 'CH', 'type': 'consultation',
                           'preuve_numerateur': '25 patients had eczema',
                           'preuve_denominateur': '200 patients',
                           'preuve_population': 'Both counts describe the same cohort.',
                           'preuve_geographie': '200 patients recruited in Switzerland',
                           'preuve_diagnostic': '25 patients had eczema'}}


class StatisticalAuditor(unittest.TestCase):
    def test_arithmetic_corrected_with_history_but_not_validated(self):
        original = candidate()
        checked = A.audit_candidate(original)
        self.assertEqual(checked['statistique']['pct'], 12.5)
        self.assertEqual(original['statistique']['pct'], 99)
        self.assertTrue(checked['audit']['calcul_verifie'])
        self.assertFalse(checked['audit']['validation_clinique'])
        self.assertEqual(checked['statut'], 'candidat_a_relire')
        self.assertEqual(checked['audit']['statut'], 'À vérifier')
        self.assertEqual(checked['audit']['corrections'][0]['avant'], 99)

    def test_repeated_audit_is_idempotent_and_preserves_source(self):
        checked = A.audit_candidate(candidate())
        self.assertEqual(A.audit_candidate(checked), checked)
        self.assertEqual(checked['url'], candidate()['url'])
        self.assertEqual(checked['extrait'], candidate()['extrait'])

    def test_zero_denominator_boolean_negative_excess_and_fractional_counts(self):
        for field, value in [('denominateur', 0), ('denominateur', True),
                             ('numerateur', True), ('numerateur', -1),
                             ('numerateur', 201), ('numerateur', 1.5),
                             ('numerateur', 'NaN'), ('denominateur', 'Infinity')]:
            with self.subTest(field=field, value=value):
                c = candidate(); c['statistique'][field] = value
                checked = A.audit_candidate(c)
                self.assertFalse(checked['audit']['calcul_verifie'])
                self.assertIn('effectifs_invalides', checked['audit']['flags'])
                self.assertEqual(checked['statistique']['pct'], 99)

    def test_invalid_pct_correctable_only_from_full_proof(self):
        c = candidate(); c['statistique']['pct'] = 120
        self.assertEqual(A.audit_candidate(c)['statistique']['pct'], 12.5)
        c['statistique'].pop('preuve_population')
        checked = A.audit_candidate(c)
        self.assertEqual(checked['statistique']['pct'], 120)
        self.assertIn('pourcentage_invalide', checked['audit']['flags'])

    def test_missing_population_not_filled_from_assertion(self):
        c = candidate(); c['statistique'].pop('preuve_population')
        self.assertFalse(A.audit_candidate(c)['audit']['calcul_verifie'])
        c = candidate(); c['statistique']['meme_population'] = 'true'
        self.assertFalse(A.audit_candidate(c)['audit']['calcul_verifie'])

    def test_affiliation_is_not_population(self):
        c = candidate(); c['extrait'] += ' University of Zurich, Switzerland.'
        c.pop('sha256_extrait')
        c['statistique']['preuve_geographie'] = 'University of Zurich, Switzerland.'
        checked = A.audit_candidate(c)
        self.assertFalse(checked['audit']['calcul_verifie'])
        self.assertIn('geographie_population_non_attestee_affiliation_insuffisante', checked['audit']['flags'])

    def test_non_european_cohort_never_inferred_from_journal(self):
        c = candidate(); c['statistique']['geographie'] = 'US'
        checked = A.audit_candidate(c)
        self.assertFalse(checked['audit']['calcul_verifie'])
        self.assertIn('population_hors_CH_Europe_ou_inconnue', checked['audit']['flags'])

    def test_incidence_odds_sensitivity_and_ci_are_not_prevalence(self):
        for term in ('incidence', 'odds ratio', 'OR 2.5', 'HR=1.8', 'relative risk', 'sensitivity', '95% CI'):
            with self.subTest(term=term):
                c = candidate()
                c['extrait'] += ' ' + term
                c.pop('sha256_extrait')
                c['statistique']['preuve_population'] += ' ' + term
                checked = A.audit_candidate(c)
                self.assertFalse(checked['audit']['calcul_verifie'])
                self.assertIn('mesure_non_prevalence_ou_ambigue', checked['audit']['flags'])

    def test_unstructured_or_and_ambiguous_fraction_never_extracted(self):
        for text in ('OR 2.5, 95% CI 1.1–5.0', 'The proportions were 5/8 and 8/20.'):
            c = candidate(); c.pop('statistique'); c['extrait'] = text
            c.pop('sha256_extrait')
            checked = A.audit_candidate(c)
            self.assertNotIn('statistique', checked)
            self.assertFalse(checked['audit']['calcul_verifie'])
        self.assertIn('extrait_contient_mesure_potentiellement_non_prevalence',
                      A.audit_candidate({'extrait': 'OR 2.5'})['audit']['flags'])

    def test_proof_must_contain_exact_count_not_a_substring(self):
        c = candidate(); c['statistique']['numerateur'] = 5
        checked = A.audit_candidate(c)
        self.assertFalse(checked['audit']['calcul_verifie'])
        self.assertIn('numerateur_non_atteste', checked['audit']['flags'])

    def test_diagnostic_mismatch(self):
        c = candidate(); c['diagnostic'] = 'urticaria'
        checked = A.audit_candidate(c)
        self.assertIn('diagnostic_non_atteste', checked['audit']['flags'])
        self.assertEqual(checked['statistique']['pct'], 99)

    def test_missing_or_non_verbatim_proofs(self):
        c = candidate(); c['statistique']['preuve_numerateur'] = '26 patients had eczema'
        self.assertFalse(A.audit_candidate(c)['audit']['calcul_verifie'])

    def test_unsafe_urls_and_future_dates(self):
        for url in ('file:///tmp/study', 'https://localhost/study', 'http://127.0.0.1/',
                    'https://user:secret@example.org/', 'javascript:alert(1)', 'https://10.0.0.1/'):
            c = candidate(); c['url'] = url
            self.assertIn('url_non_sure_ou_absente', A.audit_candidate(c)['audit']['flags'])
        c = candidate(); c['date_recherche'] = '2999-01-01'
        self.assertFalse(A.audit_candidate(c)['audit']['calcul_verifie'])

    def test_zero_percent_supported_by_explicit_zero_count(self):
        c = candidate()
        c['extrait'] = c['extrait'].replace('25 patients', '0 patients')
        c.pop('sha256_extrait')
        s = c['statistique']; s['numerateur'] = 0
        s['preuve_numerateur'] = s['preuve_diagnostic'] = '0 patients had eczema'
        checked = A.audit_candidate(c)
        self.assertTrue(checked['audit']['calcul_verifie'])
        self.assertEqual(checked['statistique']['pct'], 0)

    def test_precision_not_bool_and_decimal_rounding(self):
        c = candidate(); c['statistique']['decimales'] = True
        self.assertFalse(A.audit_candidate(c)['audit']['calcul_verifie'])
        c = candidate(); c['statistique']['decimales'] = 0
        self.assertEqual(A.audit_candidate(c)['statistique']['pct'], 13)

    def test_weighted_prevalence_not_overwritten_with_unweighted_ratio(self):
        c = candidate(); c['statistique'].update(pct=15, ponderee=True)
        checked = A.audit_candidate(c)
        self.assertEqual(checked['statistique']['pct'], 15)
        self.assertFalse(checked['audit']['calcul_verifie'])
        self.assertIn('proportion_ponderee_non_recalculable_par_effectifs_bruts', checked['audit']['flags'])
        c = candidate(); c['meta_etude'] = {'echantillon_pondere': True}
        self.assertEqual(A.audit_candidate(c)['statistique']['pct'], 99)
        c = candidate(); c['meta_etude'] = {'echantillon_pondere': 'true'}
        self.assertEqual(A.audit_candidate(c)['statistique']['pct'], 99)
        c = candidate(); c['extrait'] += ' Weighted prevalence estimate.'
        c.pop('sha256_extrait')
        self.assertEqual(A.audit_candidate(c)['statistique']['pct'], 99)

    def test_errors_distinguish_unknowns_and_observed_arithmetic_correction(self):
        checked = A.audit_candidate(candidate())
        correction = next(e for e in checked['audit']['erreurs'] if e['corrigee'])
        self.assertEqual(correction['source'], candidate()['url'])
        self.assertEqual((correction['avant'], correction['apres']), (99, 12.5))
        unknown = A.audit_candidate({'id': 'unknown', 'extrait': 'unstructured'})
        for entry in unknown['audit']['erreurs']:
            self.assertFalse(entry['corrigee'])
            self.assertNotIn('avant', entry)
            self.assertNotIn('apres', entry)

    def test_source_fingerprint(self):
        c = candidate(); c['extrait'] += ' CHANGED'
        checked = A.audit_candidate(c)
        self.assertIn('empreinte_extrait_incoherente', checked['audit']['flags'])
        self.assertEqual(checked['statistique']['pct'], 99)

    def test_state_diagnostic_injected_without_mutation(self):
        c = candidate(); c.pop('diagnostic')
        state = {'version': 1, 'category': 'G', 'tasks': {'G1#0': {'diagnostic': 'eczema', 'candidates': [c]}}}
        original = copy.deepcopy(state)
        result, report = A.audit_state(state)
        self.assertEqual(state, original)
        self.assertEqual(report['corrections_nouvelles'], 1)
        self.assertEqual(report['candidats_a_verifier'], 1)
        self.assertEqual(result['tasks']['G1#0']['candidates'][0]['diagnostic'], 'eczema')
        self.assertEqual(A.audit_state(result)[1]['corrections_nouvelles'], 0)

    def test_malformed_candidates_preserved_with_flag(self):
        state = {'category': 'G', 'tasks': {'G1#0': {'candidates': [None]}}}
        result, report = A.audit_state(state)
        self.assertEqual(report['candidats'], 1)
        self.assertIn('valeur_originale', result['tasks']['G1#0']['candidates'][0])

    def test_huge_exponents_and_numeric_strings_are_rejected_before_allocation(self):
        for value in ('1e1000000', '1e-1000000', '9' * 10000):
            with self.subTest(value=value[:20]):
                c = candidate(); c['statistique']['denominateur'] = value
                checked = A.audit_candidate(c)
                self.assertIn('effectifs_invalides', checked['audit']['flags'])
                self.assertFalse(checked['audit']['calcul_verifie'])

    def test_report_cannot_overwrite_state_or_modify_other_categories(self):
        with tempfile.TemporaryDirectory() as directory:
            data = json.dumps({'version': 1, 'category': 'G', 'tasks': {'G1#0': {'candidates': [candidate()]}}})
            g = Path(directory) / 'G.json'; g.write_text(data)
            s = Path(directory) / 'S.json'; s.write_text(data)
            result = subprocess.run([sys.executable, str(SCRIPT), '--state-dir', directory,
                                     '--report', str(s)], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(g.read_text(), data)
            self.assertEqual(s.read_text(), data)

    def test_cli_check_read_only_apply_then_check_and_separate_report(self):
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / 'G.json'
            report = Path(directory) / 'audit.json'
            state.write_text(json.dumps({'version': 1, 'category': 'G', 'tasks': {'G1#0': {'candidates': [candidate()]}}}))
            original = state.read_bytes()
            command = [sys.executable, str(SCRIPT), '--state-dir', directory, '--report', str(report)]
            dry = subprocess.run(command + ['--check'], capture_output=True, text=True)
            self.assertEqual(dry.returncode, 1, dry.stderr)
            self.assertEqual(state.read_bytes(), original)
            self.assertFalse(report.exists())
            applied = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(applied.returncode, 0, applied.stderr)
            self.assertEqual(json.loads(state.read_text())['tasks']['G1#0']['candidates'][0]['statistique']['pct'], 12.5)
            self.assertTrue(report.exists())
            again = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(again.returncode, 0, again.stderr)
            self.assertEqual(subprocess.run(command + ['--check'], capture_output=True).returncode, 0)
            self.assertEqual(set(Path(directory).iterdir()), {state, report})


if __name__ == '__main__':
    unittest.main()
