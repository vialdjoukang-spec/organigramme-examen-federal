#!/usr/bin/env python3
"""Régression de l'erreur d'unité x1000 produite par la police Symbol."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'tools'))
from aips_verbatim import decode, missing_lines


class AipsTest(unittest.TestCase):
    def test_symbol_mu_preserves_microgram_and_does_not_change_milligram(self):
        html = '<style>.s11{font-family:Symbol;}</style><p>2 à 4 <span class="s11">m</span>g/minute ; 1 mg</p>'
        text = decode(html)
        self.assertIn('2 à 4 µg/minute ; 1 mg', text)
        self.assertTrue(missing_lines({'aips_extrait':[{'texte':'2 à 4 mg/minute'}]}, text))
        self.assertFalse(missing_lines({'aips_extrait':[{'texte':'2 à 4 µg/minute'}]}, text))

    def test_threshold_and_table_unit_survive_nested_markup(self):
        text = decode('<p><font face="Symbol"><b>³</b></font>50 ml/minute</p><table><tr><td>Posologie (µg/jour)</td></tr></table>')
        self.assertIn('≥50 ml/minute', text)
        self.assertIn('Posologie (µg/jour)', text)

    def test_only_whitespace_is_normalized(self):
        row = {'aips_extrait':[{'texte':'10 mg\nune fois par jour'}]}
        self.assertFalse(missing_lines(row, '10\u00a0mg une fois par jour'))
        self.assertTrue(missing_lines(row, '100 mg une fois par jour'))
        self.assertTrue(missing_lines(row, '10 µg une fois par jour'))


if __name__ == '__main__':
    unittest.main()
