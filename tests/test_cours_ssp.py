"""La forme automatique n’atteste jamais une relecture ; les DD restent en attente."""
import json
import copy
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.cours.controler import bilan, empreinte
from tools.cours.appliquer import appliquer_au_cours
from tools.coordination.calculer import CONFIG, calculer, page
from tools.garde.permanence import complete, digest
from tools.porte import ordre


class CoursSSPTests(unittest.TestCase):
    def test_first_course_annotation_preserves_unreviewed_dd_and_replays(self):
        item = {'c': ['Ancien cours'] * 14, 'd': ['DD hérité'],
                'f': ['Fondamental'], 's': 'Source héritée'}
        original = copy.deepcopy(item)
        lot = {'parties': ['Cours relu'] * 14,
               'avant_sha256': [empreinte(x) for x in item['c']],
               'references_par_partie': [[1]] * 14,
               'sources_ajoutees': [{'id': 1, 't': 'Source lue'}]}
        appliquer_au_cours(item, lot)
        self.assertEqual({k: item[k] for k in ('d', 'f', 's')},
                         {k: original[k] for k in ('d', 'f', 's')})
        self.assertEqual(item['v']['d'], [None])
        applied = copy.deepcopy(item)
        appliquer_au_cours(item, lot)
        self.assertEqual(item, applied)
        item['c'][0] = 'Changement postérieur non relu'
        with self.assertRaises(AssertionError):
            appliquer_au_cours(item, lot)

    def fixture(self, root):
        (root / 'tools/cours').mkdir(parents=True)
        parts = ['<b>Partie :</b><ul><li>Contenu précis.</li></ul>'] * 14
        tip = {'G1': {'c': parts}, 'G2': {'c': parts}}
        (root / 'app_v2.html').write_text('\nconst TIP=' + json.dumps(tip) + ';\n')
        hashes = [empreinte(s) for s in parts]
        report = {'verdict': 'favorable_documentaire', 'parties_sha256': hashes,
                  'sources_lues': ['source lue'], 'relecteur_independant': 'auditeur'}
        raw = json.dumps(report)
        (root / 'audit.json').write_text(raw)
        registry = {'relectures': {'G1': {'parties_sha256': hashes, 'rapport': 'audit.json',
                     'rapport_sha256': empreinte(raw), 'lu_le': '2026-01-01'}}}
        (root / 'tools/cours/registre.json').write_text(json.dumps(registry))
        return tip, registry

    def test_numbering_or_unreviewed_parts_do_not_count_as_review(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); self.fixture(root)
            result = bilan(root)
            self.assertEqual((result['ssp_relus'],result['parties_relues']), (1,14))
            self.assertEqual(result['ssp_restant'], ['G2'])
            self.assertEqual(result['anomalies'], [])

    def test_changed_part_report_or_future_date_revokes_attestation(self):
        for changed in ('content','report','date'):
            with self.subTest(changed=changed), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp); tip, registry = self.fixture(root)
                if changed == 'content':
                    tip['G1']['c'][0] = 'Une information modifiée après audit.'
                    (root/'app_v2.html').write_text('\nconst TIP='+json.dumps(tip)+';\n')
                elif changed == 'report':
                    (root/'audit.json').write_text('{}')
                else:
                    registry['relectures']['G1']['lu_le'] = '2099-01-01'
                    (root/'tools/cours/registre.json').write_text(json.dumps(registry))
                result = bilan(root)
                self.assertEqual(result['parties_relues'], 0)
                self.assertTrue(result['anomalies'])

    def test_active_priority_dispatches_courses_and_never_dd_or_prevalence(self):
        result = calculer(ROOT,config=dict(CONFIG,priorite_cours_ssp=True,
                           prompt_cours_ssp='docs/PROMPT-DIRECTEUR-ACADEMIQUE.md'))
        plan = result['plan']
        self.assertTrue(plan['priorite_cours_ssp'])
        self.assertTrue(plan['diagnostics_differentiels_suspendus'])
        self.assertEqual(plan['priorites8'], [])
        self.assertTrue(plan['recherche_automatique_suspendue'])
        self.assertTrue(all(x['diagnostic'].startswith('Cours SSP') for x in plan['prochain_lot9']))
        self.assertIn('diagnostics différentiels en attente', page(result))
        self.assertFalse(complete(result))
        self.assertEqual(set(digest(result)), {'cours_ssp_relus','cours_parties_relues'})

    def test_local_sentinel_keeps_course_priority_even_with_legacy_step_title(self):
        text = ordre({'etape_courante':9,'mission_exclusive':{'priorite_courante':
                     {'id':'forme_fond_cours_ssp'}}})
        self.assertIn('uniquement les parties du cours SSP', text)
        self.assertIn('diagnostics différentiels restent suspendus', text)
        self.assertNotIn('continue avec l’étape suivante', text)


if __name__ == '__main__':
    unittest.main()
