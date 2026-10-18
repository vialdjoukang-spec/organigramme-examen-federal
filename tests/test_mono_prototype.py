import os
import re
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import mono_build as M


def entry():
    return {
        'n': 'Diagnostic exemple', 'def': 'Définition conservée.', 'epi': 'Épidémiologie conservée.',
        'phy': 'Mécanisme A.\nMécanisme B.', 'cli': 'Signe A.\nSigne B.',
        'exp': 'Exploration legacy conservée.', 'dia': 'Diagnostic legacy conservé.',
        'but': 'Objectif conservé.', 'mes': 'Mesure générale conservée.',
        'pha': 'Pharmacologie conservée.', 'aut': 'Autre moyen conservé.',
        'src': 'Source lue', 'lu': '18.10.2026',
    }


def ordered_entry():
    value = entry()
    value.update(
        prototype_version=1,
        exp_ref='Biopsie orientée par l’examen clinique',
        exp_premier='NFS avec formule → recherche de cytopénies et cellules anormales.',
        exp_bio='NFS avec formule → recherche de cytopénies et cellules anormales.',
        exp_morph='Myélogramme → morphologie médullaire.',
        exp_fonc='Cytométrie de flux → immunophénotype.',
        chronologie_version=1,
        bilan_ordre=[
            {'titre': 'À faire en premier', 'texte': 'NFS avec formule → recherche de cytopénies et cellules anormales.'},
            {'titre': 'Confirmation', 'texte': 'Myélogramme → morphologie médullaire et prélèvements pour analyses complémentaires.'},
        ],
        pec_ordre=[
            {'titre': 'Stabilisation initiale, moyens en parallèle', 'mes': 'Évaluer et traiter les complications urgentes.',
             'pha': 'Traitement spécifique selon sous-type et avis spécialisé.'},
            {'titre': 'Suite', 'aut': 'Organiser le suivi spécialisé.'},
        ],
    )
    return value


class MonographiePrototypeTest(unittest.TestCase):
    def test_renders_exactly_six_rubrics_and_keeps_diagnostic_under_five(self):
        rendered = M.html(entry())
        headings = re.findall(r'<b>(\d+)\.', rendered)
        self.assertEqual(headings, ['1', '2', '3', '4', '5', '6'])
        self.assertIn('<b>Critères diagnostiques :</b> Diagnostic legacy conservé.', rendered)
        self.assertIn('<b>Explorations :</b> Exploration legacy conservée.', rendered)
        self.assertLess(rendered.index('Diagnostic legacy conservé.'), rendered.index('<b>6.'))
        self.assertNotIn('<b>7.', rendered)

    def test_pec_is_nested_as_goal_then_means(self):
        rendered = M.html(entry())
        self.assertLess(rendered.index('<b>A- But :</b>'), rendered.index('<b>B- Moyens</b>'))
        self.assertLess(rendered.index('<b>B- Moyens</b>'), rendered.index('<b>Mesures générales :</b>'))
        self.assertLess(rendered.index('<b>Mesures générales :</b>'), rendered.index('<b>Pharmacologie :</b>'))
        self.assertLess(rendered.index('<b>Pharmacologie :</b>'), rendered.index('<b>Autres :</b>'))

    def test_timeline_suppresses_redundant_exploration_fields_and_keeps_criteria_once(self):
        value = ordered_entry()
        value.update(exp_bio='Analyse → résultat', exp_morph='Imagerie → signe', exp_fonc='Test → anomalie')
        rendered = M.html(value)
        self.assertLess(rendered.index('Examen de référence diagnostique'), rendered.index('Bilan ordonné'))
        self.assertLess(rendered.index('Bilan ordonné'), rendered.index('À faire en premier'))
        self.assertNotIn('Analyse → résultat', rendered)
        self.assertNotIn('Imagerie → signe', rendered)
        self.assertNotIn('Test → anomalie', rendered)
        self.assertNotIn('<b>Explorations :</b>', rendered)
        self.assertEqual(rendered.count('Diagnostic legacy conservé.'), 1)
        self.assertLess(rendered.index('2 — Confirmation'), rendered.index('Critères diagnostiques'))
        self.assertTrue(M.prototype_ready(value))

    def test_ordered_timelines_render_in_order_without_repeating_first_bilan(self):
        value = ordered_entry()
        self.assertTrue(M.chronologie_ready(value))
        self.assertTrue(M.prototype_ready(value))
        rendered = M.html(value)
        first = rendered.index('<b>1 — À faire en premier :</b>')
        second = rendered.index('<b>2 — Confirmation :</b>')
        pec = rendered.index('<b>6. Prise en charge</b>')
        phase1 = rendered.index('<b>Phase 1 — Stabilisation initiale, moyens en parallèle</b>')
        phase2 = rendered.index('<b>Phase 2 — Suite</b>')
        self.assertLess(first, second)
        self.assertLess(second, pec)
        self.assertLess(pec, phase1)
        self.assertLess(phase1, phase2)
        self.assertEqual(rendered.count(value['exp_premier']), 1)
        self.assertIn('moyens en parallèle', rendered)

    def test_invalid_chronology_does_not_break_legacy_but_rejects_prototype(self):
        legacy = entry()
        self.assertEqual(M.errors({'diagnostic-exemple': ('d', legacy)}, {'diagnostic-exemple'}), [])
        partial = dict(legacy, chronologie_version=1)
        self.assertTrue(any('bilan_ordre' in error for error in
                            M.errors({'diagnostic-exemple': ('d', partial)}, {'diagnostic-exemple'})))
        bad = ordered_entry()
        bad['bilan_ordre'][0]['texte'] = 'Autre texte.'
        self.assertFalse(M.chronologie_ready(bad))
        self.assertFalse(M.prototype_ready(bad))
        self.assertTrue(any('exp_premier' in error for error in
                            M.errors({'diagnostic-exemple': ('d', bad)}, {'diagnostic-exemple'})))

    def test_timeline_requires_both_general_measures_and_pharmacology(self):
        bad = ordered_entry()
        bad['pec_ordre'] = [{'titre': 'Phase', 'mes': 'Mesure.'}]
        self.assertFalse(M.chronologie_ready(bad))
        self.assertTrue(any('couvrir mesures générales' in error for error in
                            M.errors({'diagnostic-exemple': ('d', bad)}, {'diagnostic-exemple'})))

    def test_nested_prototype_body_rejects_bold_markup(self):
        for path, value in (
            ('bilan_ordre', [{'titre': 'À faire en premier', 'texte': 'Examiner.'},
                             {'titre': '<strong>Confirmation</strong>', 'texte': 'Résultat.'}]),
            ('pec_ordre', [{'titre': 'Phase', 'mes': '<STRONG>Mesure.</STRONG>', 'pha': '<b>10 mg</b>'}]),
        ):
            with self.subTest(path=path):
                bad = ordered_entry()
                bad[path] = value
                errors = M.errors({'diagnostic-exemple': ('d', bad)}, {'diagnostic-exemple'})
                self.assertTrue(any(f'.{path}[' in error and 'gras réservé aux titres' in error for error in errors))

    def test_phase_pharmacology_dose_keeps_aips_guard(self):
        bad = ordered_entry()
        bad['pec_ordre'][0]['pha'] = 'Donner 10 mg de traitement.'
        errors = M.errors({'diagnostic-exemple': ('d', bad)}, {'diagnostic-exemple'})
        self.assertTrue(any('pec_ordre[0].pha' in error and 'dose sans AIPS' in error for error in errors))

    def test_old_record_without_flag_is_not_marked_reviewed(self):
        value = entry()
        self.assertFalse(M.prototype_ready(value))
        self.assertEqual(M.errors({'diagnostic-exemple': ('d', value)}, {'diagnostic-exemple'}), [])

    def test_opt_in_requires_all_five_new_nonempty_string_fields(self):
        value = ordered_entry()
        self.assertTrue(M.prototype_ready(value))
        self.assertEqual(M.errors({'diagnostic-exemple': ('d', value)}, {'diagnostic-exemple'}), [])
        for field, invalid in [('exp_ref', ''), ('exp_premier', None), ('exp_bio', 12),
                               ('exp_morph', '  '), ('exp_fonc', [])]:
            with self.subTest(field=field):
                bad = dict(value, **{field: invalid})
                self.assertFalse(M.prototype_ready(bad))
                self.assertTrue(any(field in error for error in
                                    M.errors({'diagnostic-exemple': ('d', bad)}, {'diagnostic-exemple'})))

    def test_prototype_version_is_numeric_one(self):
        value = entry()
        value['prototype_version'] = True
        self.assertFalse(M.prototype_ready(value))
        self.assertTrue(any('prototype_version' in error for error in
                            M.errors({'diagnostic-exemple': ('d', value)}, {'diagnostic-exemple'})))

    def test_ssp_file_uses_catalogue_code_and_exact_catalogue_label(self):
        value = ordered_entry()
        value.update(n='Sudation anormale')
        catalogue = {'G1': 'Sudation anormale'}
        self.assertEqual(M.errors_ssp({'G1': value}, catalogue), [])
        self.assertTrue(M.prototype_ready(value))
        self.assertTrue(any('code SSP absent' in e for e in M.errors_ssp({'G99': value}, catalogue)))
        self.assertTrue(any('libellé SSP' in e for e in
                            M.errors_ssp({'G1': dict(value, n='Autre')}, catalogue)))

    def test_ssp_entry_without_prototype_flag_is_rejected(self):
        value = entry()
        value['n'] = 'Sudation anormale'
        self.assertTrue(any('doivent déclarer prototype_version: 1' in e
                            for e in M.errors_ssp({'G1': value}, {'G1': 'Sudation anormale'})))

    def test_ssp_asset_uses_dedicated_window_mapping(self):
        value = entry()
        value['n'] = 'Sudation anormale'
        built = M.build_ssp({'G1': value})
        self.assertTrue(built.startswith('/* Généré'))
        self.assertIn('window.CK_MONO_SSP=', built)
        self.assertIn('"G1":{"h":', built)


if __name__ == '__main__':
    unittest.main()
