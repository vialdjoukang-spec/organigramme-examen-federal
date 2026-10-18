import unittest
import json
from unittest.mock import patch

from tools.jauge.binomes import (check, chronology_fingerprint, chronologie_ok, chronology_review_ids)
from tools.garde import checkpoint
from tools.garde.checkpoint import nested_texts


def fiche():
    return {
        'prototype_version': 1,
        'chronologie_version': 1,
        'exp_ref': 'Référence diagnostique.',
        'exp_premier': 'Bilan initial → résultat recherché.',
        'exp_bio': 'Biologie → résultat recherché.',
        'exp_morph': 'Morphologie → résultat recherché.',
        'exp_fonc': 'Fonctionnel → anomalie recherchée.',
        'bilan_ordre': [
            {'titre': 'À faire en premier', 'texte': 'Bilan initial → résultat recherché.'},
            {'titre': 'Confirmation', 'texte': 'Examen ultérieur → confirmation.'},
        ],
        'pec_ordre': [
            {'titre': 'Initiale', 'mes': 'Évaluer les risques.', 'pha': 'Traitement indiqué.'},
            {'titre': 'Suivi', 'aut': 'Organiser le suivi.'},
        ],
    }


class ChronologieJaugesTest(unittest.TestCase):
    def test_counts_only_complete_ordered_prototypes(self):
        value = fiche()
        self.assertTrue(chronologie_ok(value))
        for field, bad in (
            ('prototype_version', 2),
            ('chronologie_version', True),
            ('exp_premier', 'Different.'),
            ('bilan_ordre', []),
            ('pec_ordre', [{'titre': 'Initiale', 'mes': 'Seule mesure.'}]),
        ):
            with self.subTest(field=field):
                self.assertFalse(chronologie_ok(dict(value, **{field: bad})))

    def test_legacy_records_are_not_fabricated_as_chronologies(self):
        self.assertFalse(chronologie_ok({'def': 'Ancienne fiche complète.'}))

    def test_review_requires_current_central_attestation_and_verified_report(self):
        current = fiche()
        report = 'Contrelecture documentaire indépendante.'
        import hashlib
        proof = {'statut': 'revue_documentaire', 'validation_clinique': False,
                 'sha256': chronology_fingerprint(current), 'chronologie_relue': True,
                 'date_lu': '2026-10-18', 'sources': ['SRC'], 'rapport': 'audit/rapport.md',
                 'rapport_sha256': hashlib.sha256(report.encode()).hexdigest()}
        raw = json.dumps({'version': 1, 'monographies': {'diagnostic-exemple': proof}})
        loader = lambda path: report if path == 'audit/rapport.md' else ''
        args = ({'diagnostic-exemple': current}, {'diagnostic-exemple'}, {'SRC'}, loader)
        self.assertEqual(chronology_review_ids(raw, *args), {'diagnostic-exemple'})
        stale = dict(current, **{'def': 'Une fiche modifiée.'})
        self.assertEqual(chronology_review_ids(raw, {'diagnostic-exemple': stale},
                                               {'diagnostic-exemple'}, {'SRC'}, loader), set())
        self.assertEqual(chronology_review_ids(raw, {'diagnostic-exemple': current},
                                               {'diagnostic-exemple'}, {'SRC'}, lambda _: 'rapport modifié'), set())
        invalid_source = json.loads(raw)
        invalid_source['monographies']['diagnostic-exemple']['sources'] = ['INCONNUE']
        self.assertEqual(chronology_review_ids(json.dumps(invalid_source), {'diagnostic-exemple': current},
                                               {'diagnostic-exemple'}, {'SRC'}, loader), set())
        unmarked = json.loads(raw)
        unmarked['monographies']['diagnostic-exemple']['chronologie_relue'] = False
        self.assertEqual(chronology_review_ids(json.dumps(unmarked), {'diagnostic-exemple': current},
                                               {'diagnostic-exemple'}, {'SRC'}, loader), set())
        self.assertEqual(chronology_review_ids('## (diagnostic-exemple) · chronologie relue', *args), set())

    def test_manual_gauge_check_uses_central_attestations_for_all_ids(self):
        import hashlib
        from tools.jauge import binomes
        entries = {}
        ledger_items = {}
        report = 'Independent chronology review.'
        for index in range(4):
            key = f'diagnostic-{index}'
            entry = {key_name: 'Texte documenté.' for key_name in
                     ('def', 'epi', 'phy', 'cli', 'exp', 'dia', 'but', 'mes', 'pha')}
            entry.update(fiche())
            entries[key] = entry
            ledger_items[key] = {
                'statut': 'revue_documentaire', 'validation_clinique': False,
                'sha256': chronology_fingerprint(entry), 'chronologie_relue': True,
                'date_lu': '2026-10-18', 'sources': ['SRC'], 'rapport': 'audit/review.md',
                'rapport_sha256': hashlib.sha256(report.encode()).hexdigest(),
            }
        raw_ledger = json.dumps({'version': 1, 'monographies': ledger_items})
        responses = {
            'app_v2.html': '\nconst NOT={}',
            'tools/coordination/relectures.json': raw_ledger,
            'data/ck/src.json': '[{"id":"SRC"}]',
            'audit/review.md': report,
        }
        result = {
            'ref': 'test-ref', 'prevalences': {'ok': 0, 'total': 0, 'pct': 0},
            'monographies': {'ok': 4, 'total': 4, 'pct': 100},
            'chronologie_structures': {'ok': 4, 'total': 4, 'pct': 100},
            'chronologie_relectures': {'ok': 4, 'total': 4, 'pct': 100},
            '_detail_prev': {}, '_ids': set(entries), '_mono': entries,
        }
        with patch.object(binomes, 'show', side_effect=lambda _ref, path: responses.get(path, '')):
            with patch.object(binomes, 'load_prev', return_value={}):
                self.assertEqual(check(result, ssp=()), [])

    def test_checkpoint_can_inspect_nested_pec_prose(self):
        value = {'pec_ordre': [{'titre': 'Phase', 'pha': 'Traitement 10 mg.'}]}
        self.assertIn(('pec_ordre[0].pha', 'Traitement 10 mg.'), list(nested_texts(value)))

    def test_checkpoint_dose_guard_flags_new_phase_pharmacology_dose(self):
        old = {'exemple': {'n': 'Exemple', 'pha': 'Pharmacologie habituelle.'}}
        new = {'exemple': {**old['exemple'], 'pec_ordre': [{'titre': 'Phase', 'pha': 'Traitement 10 mg.'}]}}
        def lookup(ref, path):
            if path == 'data/ck/doses_ch.json':
                return []
            if path == 'data/ck/mono/a.json':
                return new if ref == 'HEAD' else old
            return None
        failures = []
        with patch.object(checkpoint, 'json_at', side_effect=lookup):
            checkpoint.ctrl_doses('BASE', ['data/ck/mono/a.json'], failures)
        self.assertTrue(any('10mg' in message for message in failures))


if __name__ == '__main__':
    unittest.main()
