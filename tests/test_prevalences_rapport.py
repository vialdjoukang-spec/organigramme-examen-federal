import copy
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from tools.prevalences.rapport import centraliser, ecrire_pdf
from tools.prevalences.jauges import measure, page


class ReportingTests(unittest.TestCase):
    def state(self):
        return {'G':{'tasks':{'G1#0':{'queries':[{'provider':'europepmc','id':'CH:population','ok':False,'erreur':'HTTP503'}],'candidates':[{'id':'x','url':'https://example.org/source','audit':{'flags':['denominateur_non_atteste'],'corrections':[]}}]}}}}
    def test_unresolved_flag_and_network_failure_are_not_corrections(self):
        report=centraliser(self.state())
        self.assertEqual(report['synthese']['point_a_verifier'],1)
        self.assertEqual(report['synthese']['acces_recherche'],1)
        self.assertTrue(all(not e['corrigee'] for e in report['evenements']))
    def test_repeat_observation_does_not_inflate_error_count(self):
        first=centraliser(self.state());second=centraliser(self.state(),previous=first)
        self.assertEqual(first,second)
    def test_absence_of_problem_is_not_proof_of_correction(self):
        first=centraliser(self.state());second=centraliser({},previous=first)
        self.assertTrue(all(not e['corrigee'] and e['non_reobserve_dans_instantane'] for e in second['evenements']))
    def test_legacy_event_ids_are_migrated_without_double_counting(self):
        original=centraliser(self.state());legacy=copy.deepcopy(original)
        for event in legacy['evenements']:
            event['id']='legacy-'+event['id'];event.pop('empreinte_source',None)
        updated=centraliser(self.state(),previous=legacy)
        self.assertEqual(updated['synthese'],original['synthese'])
        self.assertEqual(len(updated['evenements']),len(original['evenements']))
        self.assertEqual(updated['synthese_archives'],{})
    def test_outdated_agent_review_is_archived_not_counted_as_current_reading(self):
        state=self.state();candidate=state['G']['tasks']['G1#0']['candidates'][0]
        candidate['sha256']='a'*64
        candidate['relecture_agent']={'statut':'terminee','date':'2026-01-01',
            'verdict':'À vérifier','source':candidate['url'],'loc':'Tableau 1',
            'extrait':'Source effectivement relue','sha256':candidate['sha256'],
            'validation_clinique':False}
        first=centraliser(state)
        self.assertEqual(first['synthese']['relecture_documentaire'],1)
        candidate['sha256']='b'*64
        updated=centraliser(state,previous=first)
        self.assertEqual(updated['synthese'].get('relecture_documentaire',0),0)
        self.assertEqual(updated['synthese_archives']['relecture_documentaire'],1)
        reviews=[e for e in updated['evenements'] if e['nature']=='relecture_documentaire']
        self.assertTrue(all(e['non_reobserve_dans_instantane'] for e in reviews))

    def inaccessible_agent_state(self):
        return {'O': {'tasks': {'O1.1#1': {'queries': [], 'candidates': [
            {'id': identity, 'url': 'https://doi.org/10.1234/test', 'sha256': fingerprint * 64,
             'audit': {'flags': [], 'corrections': []},
             'relecture_agent': {'statut': 'source_inaccessible', 'date': '2026-01-01T12:30:00+00:00',
                 'source': 'https://doi.org/10.1234/test', 'motifs': ['CONNECT 403 : source non relue.'],
                 'validation_clinique': False}}
            for identity, fingerprint in [('premier-extrait', 'a'), ('second-extrait', 'b')]]}}}}

    def test_inaccessible_agent_sources_are_not_completed_reviews(self):
        report=centraliser(self.inaccessible_agent_state())
        self.assertEqual(report['synthese'].get('acces_relecture'),2)
        self.assertEqual(report['synthese'].get('relecture_documentaire',0),0)
        self.assertEqual(report['synthese'].get('acces_recherche',0),0)
        for event in report['evenements']:
            self.assertEqual(event['source'],'https://doi.org/10.1234/test')
            self.assertEqual(event['date'],'2026-01-01T12:30:00+00:00')
            self.assertEqual(len(event['empreinte_source']),64)
            self.assertIn('CONNECT 403',event['motif'])
            self.assertFalse(event['corrigee'])

    def test_null_or_scalar_review_motifs_are_normalized_without_type_error(self):
        for completed in (False,True):
            for value in (None,17,'Note externe'):
                with self.subTest(completed=completed,motifs=value):
                    state=self.inaccessible_agent_state()
                    state['O']['tasks']['O1.1#1']['candidates']=state['O']['tasks']['O1.1#1']['candidates'][:1]
                    candidate=state['O']['tasks']['O1.1#1']['candidates'][0]
                    review=candidate['relecture_agent'];review['motifs']=value
                    if completed:
                        review.update(statut='terminee',verdict='À vérifier',sha256=candidate['sha256'],
                                      loc='Résumé',extrait='Source effectivement relue')
                    result=centraliser(state)
                    event=result['evenements'][0]
                    self.assertIsInstance(event['motif'],str)
                    self.assertTrue(event['motif'])
                    if value is not None:self.assertEqual(event['motif'],str(value))

    def test_same_agent_refusal_is_deduplicated_after_new_attempt_date(self):
        state=self.inaccessible_agent_state();first=centraliser(state)
        repeated=centraliser(state,previous=first)
        self.assertEqual(first,repeated)
        for candidate in state['O']['tasks']['O1.1#1']['candidates']:
            candidate['relecture_agent']['date']='2026-01-02T12:30:00+00:00'
        latest=centraliser(state,previous=repeated)
        self.assertEqual(latest['synthese']['acces_relecture'],2)
        self.assertEqual(len(latest['evenements']),2)
        self.assertTrue(all(e['date']=='2026-01-02T12:30:00+00:00' for e in latest['evenements']))

    def test_missing_agent_refusal_becomes_archive_without_assumed_fix(self):
        first=centraliser(self.inaccessible_agent_state())
        archived=centraliser({},previous=first)
        self.assertEqual(archived['synthese'].get('acces_relecture',0),0)
        self.assertEqual(archived['synthese_archives']['acces_relecture'],2)
        self.assertTrue(all(e['non_reobserve_dans_instantane'] and not e['corrigee'] for e in archived['evenements']))

    def test_changed_candidate_fingerprint_keeps_previous_refusal_as_archive(self):
        state=self.inaccessible_agent_state();first=centraliser(state)
        state['O']['tasks']['O1.1#1']['candidates'][0]['sha256']='c'*64
        updated=centraliser(state,previous=first)
        self.assertEqual(updated['synthese']['acces_relecture'],2)
        self.assertEqual(updated['synthese_archives']['acces_relecture'],1)
        self.assertEqual(updated['synthese'].get('relecture_documentaire',0),0)

    def test_agent_access_refusals_are_in_pdf_outside_limited_network_examples(self):
        from reportlab.platypus import Paragraph
        state=self.inaccessible_agent_state()
        state['O']['tasks']['O1.1#1']['queries']=[
            {'provider':'europepmc','id':str(i),'ok':False,'erreur':'HTTP503'} for i in range(40)]
        errors=centraliser(state);gauge=measure()
        with tempfile.TemporaryDirectory() as directory, patch('reportlab.platypus.Paragraph', wraps=Paragraph) as paragraphs:
            target=Path(directory)/'erreurs.pdf';ecrire_pdf(target,gauge,errors)
            self.assertTrue(target.read_bytes().startswith(b'%PDF-'))
            texts=[call.args[0] for call in paragraphs.call_args_list]
        self.assertIn('Réserves d’accès de l’agent par candidat : 2',texts)
        self.assertIn('Sources inaccessibles pendant la relecture de l’agent',texts)
        self.assertTrue(any('premier-extrait' in t for t in texts))
        self.assertTrue(any('second-extrait' in t for t in texts))
        self.assertEqual(texts.count('https://doi.org/10.1234/test'),2)
        self.assertEqual(texts.count('CONNECT 403 : source non relue.'),2)
        self.assertEqual(texts.count('01.01.2026 à 13:30 · Europe/Zurich'),2)
        self.assertEqual(errors['synthese']['relecture_documentaire'] if 'relecture_documentaire' in errors['synthese'] else 0,0)

    def test_actual_candidate_correction_preserves_before_after(self):
        state=self.state();state['G']['tasks']['G1#0']['candidates'][0]['audit']['corrections']=[{'champ':'pct','avant':12,'apres':10,'motif':'100×1/10'}]
        report=centraliser(state)
        corrections=[e for e in report['evenements'] if e['corrigee']]
        self.assertEqual(len(corrections),1);self.assertEqual(corrections[0]['avant'],12);self.assertEqual(corrections[0]['apres'],10)
    def test_corrupt_state_does_not_become_silent_success(self):
        result=measure(states={'G':['bad']});self.assertTrue(result['erreurs_chargement'])
        errors=centraliser({'G':['bad']});self.assertEqual(errors['synthese']['etat_invalide'],1)
    def test_pdf_is_written_and_report_does_not_change_published_counts(self):
        gauge=measure();errors=centraliser(self.state())
        with tempfile.TemporaryDirectory() as directory:
            target=Path(directory)/'erreurs.pdf';ecrire_pdf(target,gauge,errors);raw=target.read_bytes()
            self.assertTrue(raw.startswith(b'%PDF-'));self.assertTrue(raw.rstrip().endswith(b'%%EOF'))
            self.assertGreater(len(re.findall(rb'/Type\s*/Page\b',raw)),0)
        self.assertEqual(gauge['total']['chiffres_sources'],measure()['total']['chiffres_sources'])
        self.assertIn('prevalences-erreurs.pdf',page(gauge))


if __name__=='__main__':unittest.main()
