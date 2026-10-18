#!/usr/bin/env python3
"""Régressions de l'audit : découvertes sans perte de relecture, ni biais du plafond."""
import copy
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.prevalences.moteur import catalog, merge_candidates, snippets


def candidate(identity, provider='europepmc', query='CH:consultation'):
    return {'id': identity, 'url': 'https://example.org/' + identity, 'extrait': identity + ' 10% eczema',
            'provenance': provider, 'requete': query, 'date_recherche': '2026-01-01'}


class SearchAuditRegressions(unittest.TestCase):
    def test_refresh_preserves_structured_reading_and_correction_history(self):
        old = candidate('a')
        old.update(statistique={'numerateur': 1, 'denominateur': 10, 'pct': 10},
                   audit={'corrections': [{'avant': 15, 'apres': 10}], 'calcul_verifie': True},
                   relecture_agent={'verdict': 'À vérifier', 'source': old['url']})
        fresh = candidate('a', 'crossref', 'Europe:population')
        fresh['date_recherche'] = '2026-10-18'
        originals = copy.deepcopy((old, fresh))
        chosen, report = merge_candidates([old], [fresh], 12)
        self.assertEqual(chosen[0]['statistique'], old['statistique'])
        self.assertEqual(chosen[0]['audit'], old['audit'])
        self.assertEqual(chosen[0]['relecture_agent'], old['relecture_agent'])
        self.assertEqual(chosen[0]['date_recherche'], '2026-10-18')
        self.assertEqual(len(chosen[0]['decouvert_par']), 2)
        self.assertEqual((old, fresh), originals)
        self.assertEqual(report['candidats_omis'], 0)

    def test_changed_source_does_not_inherit_arithmetic_proof(self):
        old = candidate('a'); old['statistique'] = {'pct': 10}
        fresh = candidate('a'); fresh['extrait'] = 'A changed cohort 20%'
        chosen, _ = merge_candidates([old], [fresh], 12)
        self.assertNotIn('statistique', chosen[0])
        self.assertTrue(chosen[0]['source_modifiee'])

    def test_changed_document_fingerprint_requires_new_reading(self):
        old = candidate('a'); old.update(sha256='old', statistique={'pct': 10})
        fresh = candidate('a'); fresh['sha256'] = 'new'
        chosen, _ = merge_candidates([old], [fresh], 12)
        self.assertNotIn('statistique', chosen[0])
        self.assertTrue(chosen[0]['source_modifiee'])

    def test_round_robin_preserves_europe_hug_and_population(self):
        rows = [candidate('ch' + str(i)) for i in range(20)]
        rows += [candidate('eu' + str(i), query='Europe:population') for i in range(20)]
        rows += [candidate('hug' + str(i), provider='hug', query='CH:documents_hug') for i in range(20)]
        chosen, report = merge_candidates([], rows, 12)
        self.assertEqual(len(chosen), 12)
        self.assertEqual(sum(c['requete'] == 'Europe:population' for c in chosen), 4)
        self.assertEqual(sum(c['provenance'] == 'hug' for c in chosen), 4)
        self.assertEqual(report['candidats_total_avant_limite'], 60)
        self.assertEqual(report['candidats_omis'], 48)

    def test_curated_candidates_retained_before_unread_discoveries(self):
        old = candidate('old', 'hug'); old['relecture_agent'] = {'verdict': 'À vérifier'}
        chosen, _ = merge_candidates([old], [candidate(str(i)) for i in range(20)], 2)
        self.assertEqual(chosen[0]['id'], 'old')

    def test_automatic_audit_does_not_override_diversity(self):
        old = [candidate('a' + str(i)) for i in range(20)]
        for c in old:
            c['audit'] = {'calcul_verifie': False, 'corrections': []}
        chosen, _ = merge_candidates(old, [candidate('eu', query='Europe:population')], 2)
        self.assertEqual({c['requete'] for c in chosen}, {'CH:consultation', 'Europe:population'})

    def test_short_medical_tokens_match_whole_words(self):
        for diagnostic in ('VIH', 'SIDA', 'BPCO'):
            with self.subTest(diagnostic=diagnostic):
                doc = {'url': 'https://example.org/study', 'text': diagnostic + ' prevalence 10% among patients'}
                task = {'diagnostic': diagnostic}
                self.assertEqual(len(snippets(doc, task, 'CH:population')), 1)
                doc['text'] = 'prefix' + diagnostic + 'suffix prevalence 10% among patients'
                self.assertEqual(snippets(doc, task, 'CH:population'), [])

    def test_source_decimal_ranges_and_bounds_are_preserved_verbatim(self):
        for value in ('4, 69%', '10–35%', '≤40 %', '41 à 49%'):
            with self.subTest(value=value):
                doc = {'url': 'https://example.org/study', 'text': 'hypertension : ' + value}
                candidates = snippets(doc, {'diagnostic': 'hypertension'}, 'CH:population')
                self.assertEqual(len(candidates), 1)
                self.assertEqual(candidates[0]['valeur_reperee'], value)
                self.assertNotIn('statistique', candidates[0])

    def test_preposition_is_not_a_medical_short_token(self):
        doc = {'url': 'https://example.org/study', 'text': 'Le traitement par médicaments réduit le risque de 10%.'}
        task = {'diagnostic': 'Retard de croissance par insuffisance placentaire'}
        self.assertEqual(snippets(doc, task, 'CH:population'), [])

    def test_catalogue_proves_real_empty_ssps_without_historical_assumption(self):
        ssps, tasks = catalog()
        self.assertEqual(len(ssps), 248)
        # Source of truth: the current SSP/NOT arrays. No copied historical 22.
        empty = [code for code, _, _ in ssps if not any(t['ssp'] == code for t in tasks)]
        self.assertEqual(len(empty) + len({t['ssp'] for t in tasks}), len(ssps))
        self.assertEqual(len({t['key'] for t in tasks}), len(tasks))


if __name__ == '__main__':
    unittest.main()
