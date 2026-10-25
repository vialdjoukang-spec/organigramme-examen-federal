import copy
from datetime import datetime, timezone, timedelta
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('watchdog',ROOT/'harnais/surveillance/watchdog.py')
w=importlib.util.module_from_spec(spec);spec.loader.exec_module(w)
NOW=datetime(2026,10,25,18,0,tzinfo=timezone.utc)
CONFIG={'activity_max_age_seconds':900,'runtime_max_age_seconds':3600,'clock_skew_seconds':120}
AGENT={'id':'LOT_226','branch':'cursor/test','directory':'lot en cours de production/LOT_226'}
DIR=AGENT['directory']
def encoded(data):return json.dumps(data).encode()
class API:
    def __init__(self,files):self.files=files;self.refs=[]
    def head(self,branch):return 'a'*40
    def file(self,path,ref):self.refs.append(ref);return self.files[path]
class MonitorTests(unittest.TestCase):
    def fixture(self):
        runtime={'schema_version':1,'agent':'LOT_226','run_id':'test-real-run','versions':dict(w.EXPECTED_VERSIONS),'medical_source_compressed':False,'complete':True,
          'tested_at':NOW.isoformat(),'tests':{'chonkie':{'ok':True,'chunks':7,'exact_reconstruction':True},
          'gptcache':{'ok':True,'mode':'exact-match','write_read':True,'distinct_key_miss':True},
          'llmlingua':{'ok':True,'model':w.MODEL,'revision':w.REVISION,'origin_tokens':97,'compressed_tokens':54}}}
        files={DIR+'/PREUVE_RUNTIME_HARNAIS.json':encoded(runtime),DIR+'/real.html':b'actual artifact'}
        harness={n:b'actual trusted file '+n.encode() for n in ('harnais/bracelet/bracelet_suggest.py','harnais/bracelet/catalog.json','harnais/ARSENAL.md')}
        files.update(harness)
        proof={'schema_version':1,'agent':'LOT_226','state':'working','recorded_at':NOW.isoformat(),
          'runtime_proof':DIR+'/PREUVE_RUNTIME_HARNAIS.json','runtime_sha256':w.sha(encoded(runtime)),
          'harness_sha256':{n:w.sha(v) for n,v in harness.items()},'artifacts':[{'path':DIR+'/real.html','sha256':w.sha(b'actual artifact')}]}
        return files,proof,runtime
    def run_case(self,change_proof=None,change_runtime=None,change_files=None,missing=False):
        files,proof,runtime=self.fixture()
        if change_runtime:change_runtime(runtime)
        files[DIR+'/PREUVE_RUNTIME_HARNAIS.json']=encoded(runtime)
        proof['runtime_sha256']=w.sha(encoded(runtime))
        if change_proof:change_proof(proof)
        if change_files:change_files(files)
        if not missing:files[DIR+'/HARNAIS_ACTIVITE.json']=encoded(proof)
        api=API(files);result=w.assess_agent(CONFIG,AGENT,api,NOW)
        self.assertTrue(all(ref=='a'*40 for ref in api.refs))
        return result
    def test_real_recent_proof_is_accepted(self):self.assertTrue(self.run_case()['ok'])
    def test_missing_proof_fails(self):self.assertFalse(self.run_case(missing=True)['ok'])
    def test_stale_activity_fails_without_refresh(self):
        r=self.run_case(lambda p:p.update(recorded_at=(NOW-timedelta(minutes=16)).isoformat()))
        self.assertFalse(r['ok']);self.assertEqual(r['activity'],'stale')
    def test_declared_pause_is_not_claimed_active(self):
        r=self.run_case(lambda p:p.update(state='paused',recorded_at=(NOW-timedelta(days=1)).isoformat()))
        self.assertTrue(r['ok']);self.assertEqual(r['activity'],'paused')
    def test_future_activity_fails(self):self.assertFalse(self.run_case(lambda p:p.update(recorded_at=(NOW+timedelta(minutes=3)).isoformat()))['ok'])
    def test_future_runtime_fails(self):self.assertFalse(self.run_case(change_runtime=lambda r:r.update(tested_at=(NOW+timedelta(minutes=3)).isoformat()))['ok'])
    def test_old_runtime_fails_for_working_agent(self):self.assertFalse(self.run_case(change_runtime=lambda r:r.update(tested_at=(NOW-timedelta(hours=2)).isoformat()))['ok'])
    def test_suggestion_without_execution_fails(self):self.assertFalse(self.run_case(change_runtime=lambda r:r.update(tests={}))['ok'])
    def test_wrong_agent_fails(self):self.assertFalse(self.run_case(lambda p:p.update(agent='LOT_225'))['ok'])
    def test_modified_harness_fails(self):self.assertFalse(self.run_case(change_files=lambda f:f.update({'harnais/ARSENAL.md':b'changed'}))['ok'])
    def test_modified_artifact_fails(self):self.assertFalse(self.run_case(change_files=lambda f:f.update({DIR+'/real.html':b'changed'}))['ok'])
    def test_forged_runtime_hash_fails(self):self.assertFalse(self.run_case(lambda p:p.update(runtime_sha256='0'*64))['ok'])
    def test_cross_lot_artifact_fails(self):self.assertFalse(self.run_case(lambda p:p.update(artifacts=[{'path':'lot en cours de production/LOT_225/file','sha256':'0'*64}]))['ok'])
    def test_path_traversal_fails(self):self.assertFalse(self.run_case(lambda p:p.update(artifacts=[{'path':DIR+'/../LOT_225/file','sha256':'0'*64}]))['ok'])
    def test_fake_compression_fails(self):
        self.assertFalse(self.run_case(change_runtime=lambda r:r['tests']['llmlingua'].update(compressed_tokens=97))['ok'])
    def test_boolean_token_counts_fail(self):
        self.assertFalse(self.run_case(change_runtime=lambda r:r['tests']['llmlingua'].update(compressed_tokens=True))['ok'])
    def test_no_timezone_fails(self):self.assertFalse(self.run_case(lambda p:p.update(recorded_at='2026-10-25T18:00:00'))['ok'])
    def test_failed_cache_test_fails(self):self.assertFalse(self.run_case(change_runtime=lambda r:r['tests']['gptcache'].update(write_read=False))['ok'])
    def test_unrelated_versions_fail(self):self.assertFalse(self.run_case(change_runtime=lambda r:r.update(versions={'unrelated':'1'}))['ok'])
    def test_wrong_model_fails(self):self.assertFalse(self.run_case(change_runtime=lambda r:r['tests']['llmlingua'].update(model='wrong'))['ok'])
    def test_wrong_revision_fails(self):self.assertFalse(self.run_case(change_runtime=lambda r:r['tests']['llmlingua'].update(revision='wrong'))['ok'])
    def test_single_chunk_fails(self):self.assertFalse(self.run_case(change_runtime=lambda r:r['tests']['chonkie'].update(chunks=1))['ok'])
    def test_null_tests_fail_without_crash(self):self.assertFalse(self.run_case(change_runtime=lambda r:r.update(tests=None))['ok'])
    def test_list_test_fails_without_crash(self):self.assertFalse(self.run_case(change_runtime=lambda r:r['tests'].update(llmlingua=[]))['ok'])
    def test_medical_compression_fails(self):self.assertFalse(self.run_case(change_runtime=lambda r:r.update(medical_source_compressed=True))['ok'])
    def test_null_hashes_fail_without_crash(self):self.assertFalse(self.run_case(lambda p:p.update(harness_sha256=None))['ok'])
    def test_branch_cannot_redefine_trusted_harness(self):
        files,proof,runtime=self.fixture()
        trusted=dict(proof['harness_sha256'])
        files['harnais/ARSENAL.md']=b'modified'
        proof['harness_sha256']['harnais/ARSENAL.md']=w.sha(b'modified')
        files[DIR+'/HARNAIS_ACTIVITE.json']=encoded(proof)
        self.assertFalse(w.assess_agent(CONFIG,AGENT,API(files),NOW,trusted_hashes=trusted)['ok'])
if __name__=='__main__':unittest.main()
