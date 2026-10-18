import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'audit'))
import prevalence as P


SOURCES = [{'id': 'R-1'}]
TODAY = '2026-10-18'


def section(order=None):
    out = {'cadre': 'adultes, consultation spécialisée', 'items': [
        {'i': 0, 'nom': 'A', 'prev_pct': None, 'statut': 'À vérifier', 'rang': 1},
        {'i': 1, 'nom': 'B', 'prev_pct': 8, 'type': 'consultation', 'rang': 2},
        {'i': 2, 'nom': 'C', 'prev_pct': None, 'statut': 'À vérifier', 'rang': 3},
    ]}
    if order is not None:
        out['classement'] = {'type': 'qualitatif_source', 'src': 'R-1', 'date_lu': '2026-10-17',
                             'loc': 'Tableau 2', 'ordre': order,
                             'cadre': 'adultes, consultation spécialisée'}
    return out


class ClassementTest(unittest.TestCase):
    def status(self, value, sources=SOURCES):
        return P.classification_status(value, sources, today=TODAY)

    def test_absent_classement_is_explicitly_indetermine(self):
        self.assertEqual(self.status(section())['etat'], 'indetermine')

    def test_valid_order_can_interleave_unknowns_without_turning_them_into_zero(self):
        value = section([0, 1, 2])
        status = self.status(value)
        self.assertEqual(status['etat'], 'valide', status['raisons'])
        result = P.prv({'X': value}, SOURCES, today=TODAY)['X']
        self.assertEqual(result, [[0, None], [1, 8], [2, None]])

    def test_future_date_is_rejected(self):
        value = section([0, 1, 2])
        value['classement']['date_lu'] = '2026-10-19'
        self.assertEqual(self.status(value)['etat'], 'invalide')

    def test_unregistered_source_is_rejected(self):
        value = section([0, 1, 2])
        value['classement']['src'] = 'R-absente'
        self.assertEqual(self.status(value)['etat'], 'invalide')

    def test_partial_order_is_rejected(self):
        self.assertEqual(self.status(section([0, 1]))['etat'], 'invalide')

    def test_order_cannot_contradict_comparable_numeric_values(self):
        value = section([1, 0, 2])
        value['items'][0]['prev_pct'] = 12
        self.assertEqual(self.status(value)['etat'], 'invalide')

    def test_legacy_order_is_preserved_without_claiming_classification(self):
        value = section()
        result = P.prv({'X': value}, SOURCES, today=TODAY)['X']
        self.assertEqual(result, [[1, 8], [0, None], [2, None]])
        self.assertEqual(P.detail({'X': value}, SOURCES, today=TODAY)['X']['classement']['etat'],
                         'indetermine')


if __name__ == '__main__':
    unittest.main()
