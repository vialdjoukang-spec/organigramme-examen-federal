import importlib.util, unittest, json
from pathlib import Path
s = importlib.util.spec_from_file_location('v', Path(__file__).resolve().parents[1] / 'tools/arsenal/ci_verdict.py')
v = importlib.util.module_from_spec(s); s.loader.exec_module(v)
class Verdict(unittest.TestCase):
    def test_rouge_si_un_echec(self):
        self.assertEqual(v.verdict('[{"name":"garde","bucket":"fail"},{"name":"t","bucket":"pass"}]')[1], 1)
    def test_rouge_echec_meme_si_attente(self):
        self.assertEqual(v.verdict('[{"name":"garde","bucket":"fail"},{"name":"t","bucket":"pending"}]')[1], 1)
    def test_jamais_vert_sans_controle_ou_sortie_vide(self):
        self.assertNotEqual(v.verdict('')[1], 0); self.assertNotEqual(v.verdict('[]')[1], 0)
        self.assertEqual(v.verdict('oops')[1], 1)
    def test_attente_puis_vert(self):
        self.assertEqual(v.verdict('[{"name":"t","bucket":"pending"}]')[1], 2)
        self.assertEqual(v.verdict('[{"name":"t","bucket":"pass"},{"name":"s","bucket":"skipping"}]')[1], 0)
    def test_schema_inconnu_refuse(self):
        for value in ('{}', 'null', '[1]', '[{"name":"t","bucket":"unknown"}]'):
            self.assertEqual(v.verdict(value)[1], 1)

    def snapshot(self, **updates):
        result = {'headRefOid': 'sha-final', 'statusCheckRollup': [
            {'name': name, 'status': 'COMPLETED', 'conclusion': 'SUCCESS'}
            for name in v.REQUIS]}
        result.update(updates)
        return result

    def test_sha_final_et_tous_requis(self):
        snapshot = self.snapshot()
        self.assertEqual(v.snapshot_verdict(json.dumps(snapshot), 'sha-final')[1], 0)
        self.assertEqual(v.snapshot_verdict(json.dumps(snapshot), 'ancien-sha')[1], 1)
        snapshot['statusCheckRollup'].pop()
        self.assertEqual(v.snapshot_verdict(json.dumps(snapshot), 'sha-final')[1], 2)

    def test_requis_ignore_et_ancien_echec_non_masques(self):
        for state in ('SKIPPED', 'NEUTRAL', 'FAILURE', 'CANCELLED', 'TIMED_OUT'):
            snapshot = self.snapshot()
            snapshot['statusCheckRollup'][0]['conclusion'] = state
            self.assertEqual(v.snapshot_verdict(json.dumps(snapshot), 'sha-final')[1], 1)
        snapshot = self.snapshot()
        snapshot['statusCheckRollup'].append({'name': 'garde', 'status': 'COMPLETED', 'conclusion': 'FAILURE'})
        self.assertEqual(v.snapshot_verdict(json.dumps(snapshot), 'sha-final')[1], 1)

    def test_optionnel_en_attente_bloque_et_ignore_admis(self):
        snapshot = self.snapshot()
        snapshot['statusCheckRollup'].append({'name': 'liens', 'status': 'IN_PROGRESS'})
        self.assertEqual(v.snapshot_verdict(json.dumps(snapshot), 'sha-final')[1], 2)
        snapshot['statusCheckRollup'][-1].update(status='COMPLETED', conclusion='SKIPPED')
        self.assertEqual(v.snapshot_verdict(json.dumps(snapshot), 'sha-final')[1], 0)

if __name__ == '__main__': unittest.main()
