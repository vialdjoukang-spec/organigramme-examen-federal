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


class InternationalDefinitionTests(unittest.TestCase):
    def fixture(self, root):
        import yaml
        source = {'id': 'R-IUPS', 'url': 'https://example.jp/definition.pdf',
                  'org': 'Éditeur japonais', 'pays': 'JP', 'type': 'glossaire'}
        policy = {'suisse': [], 'europe': [], 'anatomie': [], 'pays_admis': ['CH', 'GB'],
                  'definitions_internationales': [{**source, 'ssp': 'G6', 'source_cours': 17}]}
        (root / 'qa').mkdir()
        (root / 'qa/domaines.yml').write_text(yaml.safe_dump(policy))
        tip = {'G6': {'c': ['<b>Définition :</b> Reformulation attribuée.'] * 14,
                      'v': {'S': [{'id': 17, 'u': source['url'], 'n': 'JP', 'o': source['org']}],
                            'c': [['réorganisé', [17]]] + [['hérité', []]] * 13,
                            'd': [['hérité', []]]}}}
        data = {key: [] for key in ('src', 'glo', 'syn', 'hyp', 'nc', 'loc', 'doses_ch')}
        data['src'] = [source]
        return tip, data

    def flags(self, root, tip, data):
        from tools.audit.niveau1 import g3
        (root / 'app_v2.html').write_text('\nconst TIP=' + json.dumps(tip) + ';\n')
        flags = []
        g3(str(root), data, flags)
        return flags

    def test_world_definition_keeps_actual_country_and_precise_scope(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); tip, data = self.fixture(root)
            self.assertEqual(self.flags(root, tip, data), [])
            self.assertEqual(data['src'][0]['pays'], 'JP')

    def test_definition_list_wrapper_keeps_precise_scope(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); tip, data = self.fixture(root)
            tip['G6']['c'][0] = '<ul><li><b>Définition :</b> Reformulation attribuée.</li></ul>'
            self.assertEqual(self.flags(root, tip, data), [])
            tip['G6']['v']['c'][10] = ['ajouté', [17]]
            self.assertTrue(self.flags(root, tip, data))

    def test_unrelated_list_heading_does_not_authorize_definition_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); tip, data = self.fixture(root)
            tip['G6']['c'][0] = '<ul><li><b>Traitement :</b> Texte.</li></ul>'
            self.assertTrue(self.flags(root, tip, data))

    def test_definition_cannot_be_reused_in_care_or_dd(self):
        for field, index in (('c', 10), ('d', 0)):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp); tip, data = self.fixture(root)
                tip['G6']['v'][field][index] = ['ajouté', [17]]
                self.assertTrue(self.flags(root, tip, data))

    def test_definition_cannot_authorize_ck_treatment_or_dose(self):
        for field in ('hyp', 'doses_ch'):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp); tip, data = self.fixture(root)
                data[field] = [{'id': 'exemple', 'src': [{'id': 'R-IUPS'}]}]
                self.assertTrue(self.flags(root, tip, data))

    def test_unreferenced_reuse_in_other_course_or_fundamental_is_rejected(self):
        for target in ('care', 'fundamental', 'other_ssp'):
            with self.subTest(target=target), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp); tip, data = self.fixture(root)
                url = data['src'][0]['url']
                if target == 'care':
                    tip['G6']['c'][10] += url
                elif target == 'fundamental':
                    tip['G6']['f'] = [url]
                else:
                    tip['G7'] = {'c': [url]}
                self.assertTrue(self.flags(root, tip, data))

    def test_second_world_definition_keeps_its_own_ssp_and_rejects_care(self):
        import yaml
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); tip, data = self.fixture(root)
            source = {'id': 'R-IASP', 'url': 'https://example.us/definition.pdf',
                      'org': 'Association internationale, États-Unis', 'pays': 'US', 'type': 'glossaire'}
            policy = yaml.safe_load((root / 'qa/domaines.yml').read_text())
            policy['definitions_internationales'].append({**source, 'ssp': 'G10', 'source_cours': 20})
            (root / 'qa/domaines.yml').write_text(yaml.safe_dump(policy))
            data['src'].append(source)
            tip['G10'] = {'c': ['<ul><li><b>Définition :</b> Douleur attribuée.</li></ul>'] * 14,
                          'v': {'S': [{'id': 20, 'u': source['url'], 'n': 'US', 'o': source['org']}],
                                'c': [['réorganisé', [20]]] + [['hérité', []]] * 13}}
            self.assertEqual(self.flags(root, tip, data), [])
            tip['G10']['v']['c'][10] = ['ajouté', [20]]
            self.assertTrue(self.flags(root, tip, data))

    def test_no_global_authorization_of_country_or_host(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); tip, data = self.fixture(root)
            data['src'].append({'id': 'R-AUTRE', 'url': 'https://example.jp/autre.pdf',
                                'org': 'Autre éditeur', 'pays': 'JP', 'type': 'article'})
            self.assertTrue(self.flags(root, tip, data))


    def reused_wgo_fixture(self, root):
        """Identités réelles S1.7/S2.9 ; URL commune, deux visas explicites."""
        import yaml
        url = 'https://www.worldgastroenterology.org/guidelines/dysphagia'
        sources = [
            {'id': 'R-COURS-S17-01', 'url': url, 'org': 'World Gastroenterology Organisation',
             'pays': 'US', 'type': 'glossaire'},
            {'id': 'R-COURS-S2-9-7', 'url': url,
             'org': 'World Gastroenterology Organisation, fédération mondiale de sociétés ; secrétariat aux États-Unis',
             'pays': 'US', 'type': 'glossaire'}]
        records = [{**s, 'ssp': code, 'source_cours': number}
                   for s, code, number in zip(sources, ('S1.7', 'S2.9'), (1, 7))]
        policy = {'suisse': [], 'europe': [], 'anatomie': [], 'pays_admis': ['CH', 'GB'],
                  'definitions_internationales': records}
        (root / 'qa').mkdir()
        (root / 'qa/domaines.yml').write_text(yaml.safe_dump(policy))
        tip = {rec['ssp']: {'c': ['<b>Définition :</b> Reformulation attribuée.'] * 14,
                           'v': {'S': [{'id': rec['source_cours'], 'u': url,
                                        'n': rec['pays'], 'o': rec['org']}],
                                 'c': [['réorganisé', [rec['source_cours']]]] + [['hérité', []]] * 13,
                                 'd': [['hérité', []]], 'k': 1}}
               for rec in records}
        data = {key: [] for key in ('src', 'glo', 'syn', 'hyp', 'nc', 'loc', 'doses_ch')}
        data['src'] = sources
        return tip, data, policy

    def test_same_wgo_document_in_two_explicit_definitions_is_accepted(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); tip, data, _ = self.reused_wgo_fixture(root)
            self.assertEqual(self.flags(root, tip, data), [])
            # Références littérales acceptées seulement dans leurs définitions.
            for item, source in zip(tip.values(), data['src']):
                item['c'][0] += source['url'] + source['id']
            self.assertEqual(self.flags(root, tip, data), [])
            self.assertEqual({s['pays'] for s in data['src']}, {'US'})

    def test_shared_definition_requires_each_exact_exception_and_source(self):
        import yaml
        for change in ('no_exception', 'no_source', 'id', 'url', 'org', 'pays', 'type',
                       'ssp', 'source_cours', 'unapproved_source'):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp); tip, data, policy = self.reused_wgo_fixture(root)
                records = policy['definitions_internationales']
                if change == 'no_exception':
                    records.pop()
                elif change == 'no_source':
                    data['src'].pop()
                elif change == 'unapproved_source':
                    data['src'].append({**data['src'][1], 'id': 'R-NON-AUTORISE'})
                else:
                    records[1][change] = 8 if change == 'source_cours' else 'incorrect'
                (root / 'qa/domaines.yml').write_text(yaml.safe_dump(policy))
                self.assertEqual({f['element'] for f in self.flags(root, tip, data)},
                                 {'src|' + source['id'] for source in data['src']})

    def test_shared_definition_rejects_duplicates_and_ambiguous_visas(self):
        import copy
        import yaml
        for change in ('exception', 'source', 'visa', 'collision_id', 'reference',
                       'same_ssp', 'boolean_id', 'boolean_reference', 'bad_entry', 'bad_k'):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp); tip, data, policy = self.reused_wgo_fixture(root)
                visa = tip['S1.7']['v']
                if change == 'exception':
                    policy['definitions_internationales'].append(copy.deepcopy(policy['definitions_internationales'][0]))
                elif change == 'source':
                    data['src'].append(copy.deepcopy(data['src'][0]))
                elif change == 'visa':
                    visa['S'].append(copy.deepcopy(visa['S'][0]))
                elif change == 'collision_id':
                    visa['S'].append({**visa['S'][0], 'u': 'https://example.us/autre'})
                elif change == 'reference':
                    visa['c'][0][1].append(1)
                elif change == 'same_ssp':
                    policy['definitions_internationales'][1]['ssp'] = 'S1.7'
                elif change == 'boolean_id':
                    visa['S'][0]['id'] = True
                elif change == 'boolean_reference':
                    visa['c'][0][1] = [True]
                elif change == 'bad_entry':
                    visa['c'][0] = ['réorganisé', 1]
                else:
                    visa['k'] = data['src'][0]['url']
                (root / 'qa/domaines.yml').write_text(yaml.safe_dump(policy))
                self.assertEqual({f['element'] for f in self.flags(root, tip, data)},
                                 {'src|' + source['id'] for source in data['src']})

    def test_shared_definition_never_authorizes_care_dd_fundamental_or_third_ssp(self):
        import copy
        for change in ('c1', 'care', 'dd', 'fundamental_visa', 'fundamental_url',
                       'care_url', 'dd_id', 'wrong_definition_id', 'third_ssp', 'ck', 'dose'):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp); tip, data, _ = self.reused_wgo_fixture(root)
                item = tip['S2.9']; source = data['src'][1]
                if change in ('c1', 'care'):
                    item['v']['c'][1 if change == 'c1' else 10] = ['ajouté', [7]]
                elif change in ('dd', 'fundamental_visa'):
                    item['v']['d' if change == 'dd' else 'f'] = [['ajouté', [7]]]
                elif change == 'fundamental_url':
                    item['f'] = [source['url']]
                elif change == 'care_url':
                    item['c'][10] += source['url']
                elif change == 'dd_id':
                    item['d'] = [source['id']]
                elif change == 'wrong_definition_id':
                    tip['S1.7']['c'][0] += source['id']
                elif change == 'third_ssp':
                    tip['S3.1'] = copy.deepcopy(item)
                else:
                    data['hyp' if change == 'ck' else 'doses_ch'].append(
                        {'id': 'exemple', 'src': [{'id': source['id']}]})
                self.assertEqual({f['element'] for f in self.flags(root, tip, data)},
                                 {'src|' + source['id'] for source in data['src']})

    def test_shared_definition_requires_actual_definition_for_every_authorization(self):
        for change in ('unused', 'wrong_heading', 'missing_course'):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp); tip, data, _ = self.reused_wgo_fixture(root)
                if change == 'unused':
                    tip['S2.9']['v']['c'][0] = ['hérité', []]
                elif change == 'wrong_heading':
                    tip['S2.9']['c'][0] = '<b>Traitement :</b> Texte.'
                else:
                    del tip['S2.9']
                self.assertEqual({f['element'] for f in self.flags(root, tip, data)},
                                 {'src|' + source['id'] for source in data['src']})


if __name__ == '__main__':
    unittest.main()
