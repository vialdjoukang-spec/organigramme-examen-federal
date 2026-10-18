import copy
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
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
