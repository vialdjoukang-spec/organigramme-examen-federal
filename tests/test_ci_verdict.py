import importlib.util, unittest, json, os, subprocess, tempfile
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

    def test_script_clone_sans_reference_distante_et_sha_different(self):
        # Un clone limité à main n'a pas origin/<branche>, même après le push.
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            env = {**os.environ, 'GIT_AUTHOR_NAME': 'Test', 'GIT_AUTHOR_EMAIL': 'test@example.invalid',
                   'GIT_COMMITTER_NAME': 'Test', 'GIT_COMMITTER_EMAIL': 'test@example.invalid'}
            def git(*args):
                return subprocess.run(['git', *args], cwd=root, env=env, check=True,
                                      capture_output=True, text=True).stdout.strip()
            git('init')
            git('checkout', '-b', 'feature')
            git('commit', '--allow-empty', '-m', 'base')
            sha = git('rev-parse', 'HEAD')
            (root/'gh').write_text('#!/bin/sh\ncat "$TEST_SNAPSHOT_PATH"\n')
            (root/'gh').chmod(0o755)
            env.update(PATH=str(root)+os.pathsep+env['PATH'], TEST_SNAPSHOT_PATH=str(root/'snapshot.json'))
            script = Path(__file__).resolve().parents[1]/'tools/arsenal/ci_attente.sh'
            for actual_sha, expected_code in ((sha, 0), ('0'*40, 1)):
                snapshot = self.snapshot(headRefOid=actual_sha)
                (root/'snapshot.json').write_text(json.dumps(snapshot))
                result = subprocess.run(['bash', str(script), 'feature'], cwd=root, env=env,
                                        capture_output=True, text=True, timeout=10)
                self.assertEqual(result.returncode, expected_code, result.stdout+result.stderr)
            # Une référence distante périmée ne doit pas certifier l'ancien SHA.
            git('update-ref', 'refs/remotes/origin/feature', sha)
            git('commit', '--allow-empty', '-m', 'final local commit')
            final_sha = git('rev-parse', 'HEAD')
            for actual_sha, expected_code in ((sha, 1), (final_sha, 0)):
                (root/'snapshot.json').write_text(json.dumps(self.snapshot(headRefOid=actual_sha)))
                result = subprocess.run(['bash', str(script), 'feature'], cwd=root, env=env,
                                        capture_output=True, text=True, timeout=10)
                self.assertEqual(result.returncode, expected_code, result.stdout+result.stderr)
            result = subprocess.run(['bash', str(script), 'unknown'], cwd=root, env=env,
                                    capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 1)
            self.assertIn('introuvable', result.stdout)
            git('checkout', '-b', 'other')
            git('commit', '--allow-empty', '-m', 'unrelated HEAD')
            (root/'snapshot.json').write_text(json.dumps(self.snapshot(headRefOid=final_sha)))
            result = subprocess.run(['bash', str(script), 'feature'], cwd=root, env=env,
                                    capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stdout+result.stderr)

if __name__ == '__main__': unittest.main()
