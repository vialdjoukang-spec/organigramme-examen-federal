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

    def test_new_exploration_fields_precede_legacy_fields_at_head_of_section_five(self):
        value = entry()
        value.update(prototype_version=1, exp_ref='Référence clinique', exp_premier='Bilan initial',
                     exp_bio='Analyse → résultat', exp_morph='Imagerie → signe', exp_fonc='Test → anomalie')
        rendered = M.html(value)
        self.assertLess(rendered.index('Examen de référence diagnostique'), rendered.index('À faire en premier'))
        self.assertLess(rendered.index('À faire en premier'), rendered.index('Biologie'))
        self.assertLess(rendered.index('Explorations fonctionnelles'), rendered.index('Explorations :'))
        self.assertLess(rendered.index('Explorations :'), rendered.index('Critères diagnostiques :'))
        self.assertTrue(M.prototype_ready(value))

    def test_old_record_without_flag_is_not_marked_reviewed(self):
        value = entry()
        self.assertFalse(M.prototype_ready(value))
        self.assertEqual(M.errors({'diagnostic-exemple': ('d', value)}, {'diagnostic-exemple'}), [])

    def test_opt_in_requires_all_five_new_nonempty_string_fields(self):
        value = entry()
        value.update(prototype_version=1, exp_ref='Référence', exp_premier='Bilan', exp_bio='Biologie',
                     exp_morph='Morphologie', exp_fonc='Fonctionnel')
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
        value = entry()
        value.update(n='Sudation anormale', prototype_version=1, exp_ref='Référence', exp_premier='Bilan',
                     exp_bio='Biologie', exp_morph='Morphologie', exp_fonc='Explorations fonctionnelles')
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
