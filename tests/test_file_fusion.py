#!/usr/bin/env python3
"""Exercise both authorization and real queue mutations with a fake GitHub CLI."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'tools/file_fusion.sh'
SHA = 'a' * 40
FAKE_GH = r'''#!/usr/bin/env python3
import base64, json, os, pathlib, sys
a = sys.argv[1:]
root = pathlib.Path(os.environ['OEF_REPO'])
with (root/'calls.jsonl').open('a') as f: f.write(json.dumps(a)+'\n')
if a[:2] == ['auth','status']: sys.exit(0)
if a[:1] == ['api']:
 endpoint = a[1]
 if 'protection' in endpoint:
  print('{"message":"Resource not accessible by integration"}'); sys.exit(1)
 if endpoint.endswith('/branches/main'):
  print(json.dumps({'commit': {'sha': 'd'*40}})); sys.exit(0)
 if '/contents/tools/mandat/integration.json?' in endpoint:
  if not (root/'canonical.json').exists(): sys.exit(1)
  print(json.dumps({'encoding':'base64', 'content':base64.b64encode((root/'canonical.json').read_bytes()).decode()})); sys.exit(0)
 if '/files?' in endpoint:
  print((root/'files.json').read_text()); sys.exit(0)
if a[:2] == ['pr','view']:
 pr = json.loads((root/'pr.json').read_text())
 if '--jq' in a: print(pr['headRefOid'])
 else: print(json.dumps(pr))
 sys.exit(0)
if a[:2] == ['run','list']: sys.exit(0)
if a[:2] == ['pr','merge']: sys.exit(0)
if a[:3] == ['workflow','run','pages.yml']:
 sys.exit(1 if (root/'fail_pages').exists() else 0)
print('Unexpected mock call: '+repr(a), file=sys.stderr); sys.exit(2)
'''


class QueueTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root/'tools').mkdir()
        (self.root/'journal').mkdir()
        (self.root/'bin').mkdir()
        (self.root/'tools/etapes.json').write_text(json.dumps({'chaines': {'test': [123]}}))
        shutil.copy(ROOT/'tools/predecesseurs_fusion.py', self.root/'tools/predecesseurs_fusion.py')
        self.config = {'version':1, 'actif':True, 'priorite_active':'P0',
                       'fusion_clinique':'manuelle_centralisee',
                       'autorisations_techniques':[{'number':123, 'head_sha':SHA, 'priorite':'P0'}]}
        (self.root/'canonical.json').write_text(json.dumps(self.config))
        (self.root/'files.json').write_text(json.dumps([{'filename':'tools/predecesseurs_fusion.py'}]))
        gh = self.root/'bin/gh'
        gh.write_text(FAKE_GH)
        gh.chmod(0o755)
        self.env = {**os.environ, 'OEF_REPO':str(self.root),
                    'PATH':str(self.root/'bin')+os.pathsep+os.environ['PATH']}
        self.pr = {'state':'OPEN', 'labels':[{'name':'audit-ok'}], 'isDraft':False,
                   'mergeStateStatus':'CLEAN', 'headRefOid':SHA, 'baseRefName':'main', 'changedFiles':1,
                   'statusCheckRollup':[{'name':n, 'status':'COMPLETED', 'conclusion':'SUCCESS'}
                                        for n in ('garde','html','tests','visuel','checkpoint','schemas')]}

    def run_queue(self, *args):
        (self.root/'pr.json').write_text(json.dumps(self.pr))
        result = subprocess.run(['bash', str(SCRIPT), *args], env=self.env,
                                text=True, capture_output=True, timeout=20)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result

    def calls(self, prefix):
        return [a for a in map(json.loads, (self.root/'calls.jsonl').read_text().splitlines())
                if a[:len(prefix)] == prefix]

    def assert_no_pr_mutation(self):
        self.assertFalse(self.calls(['pr','merge']))
        self.assertFalse([a for a in self.calls(['api']) if '-X' in a])
        self.assertFalse(self.calls(['run','rerun']))

    def test_protection_error_uses_required_checks_and_merge_head(self):
        self.run_queue()
        self.assertEqual(self.calls(['pr','merge']),
                         [['pr','merge','123','--merge','--match-head-commit',SHA]])

    def test_missing_failed_pending_neutral_or_skipped_required_never_merges(self):
        for conclusion in ('FAILURE', '', 'NEUTRAL', 'SKIPPED'):
            with self.subTest(conclusion=conclusion):
                self.pr['statusCheckRollup'][-1]['conclusion'] = conclusion
                self.run_queue()
                self.assert_no_pr_mutation()
        self.pr['statusCheckRollup'].pop()
        self.run_queue()
        self.assert_no_pr_mutation()

    def test_optional_failed_pending_blocks_but_skipped_allowed(self):
        optional = {'name':'liens','status':'COMPLETED','conclusion':'FAILURE'}
        self.pr['statusCheckRollup'].append(optional)
        self.run_queue()
        self.assert_no_pr_mutation()
        optional.update(status='IN_PROGRESS', conclusion=None)
        self.run_queue()
        self.assert_no_pr_mutation()
        optional.update(status='COMPLETED', conclusion='SKIPPED')
        self.run_queue()
        self.assertEqual(len(self.calls(['pr','merge'])),1)

    def test_attente_vial_suspends_even_if_audited_and_green(self):
        self.pr['labels'].append({'name':'attente-vial'})
        self.run_queue()
        self.assert_no_pr_mutation()

    def test_empty_canonical_p0_blocks_legacy_chain_despite_audit_green(self):
        self.config['autorisations_techniques'] = []
        (self.root/'canonical.json').write_text(json.dumps(self.config))
        self.run_queue()
        self.assert_no_pr_mutation()

    def test_local_allowlist_cannot_replace_missing_main_configuration(self):
        (self.root/'tools/mandat').mkdir()
        (self.root/'tools/mandat/integration.json').write_text(json.dumps(self.config))
        (self.root/'canonical.json').unlink()
        self.run_queue()
        self.assert_no_pr_mutation()

    def test_future_priority_or_changed_sha_never_mutates(self):
        self.config['autorisations_techniques'][0]['priorite'] = 'P3'
        (self.root/'canonical.json').write_text(json.dumps(self.config))
        self.run_queue()
        self.assert_no_pr_mutation()
        self.config['autorisations_techniques'][0]['priorite'] = 'P0'
        (self.root/'canonical.json').write_text(json.dumps(self.config))
        self.pr['headRefOid'] = 'b' * 40
        self.run_queue()
        self.assert_no_pr_mutation()

    def test_clinical_diff_denied_even_if_number_sha_explicit(self):
        for path in ('data/tip/S3.6.json','data/ck/mono/g3.json','assets/config/tip.js',
                     'data/cs/thorax.json','app_v2.html'):
            (self.root/'files.json').write_text(json.dumps([{'filename':path}]))
            self.run_queue()
            self.assert_no_pr_mutation()

    def test_incomplete_file_inventory_blocks(self):
        self.pr['changedFiles'] = 3001
        self.run_queue()
        self.assert_no_pr_mutation()

    def test_behind_branch_not_updated_before_new_exact_authorization(self):
        self.pr['mergeStateStatus'] = 'BEHIND'
        self.run_queue()
        self.assert_no_pr_mutation()

    def test_pages_failure_is_retried_without_another_merge(self):
        (self.root/'fail_pages').touch()
        self.run_queue()
        marker = self.root/'.etat_local/pages_a_relancer'
        self.assertTrue(marker.exists())
        self.pr['state'] = 'MERGED'
        (self.root/'fail_pages').unlink()
        self.run_queue()
        self.assertEqual(len(self.calls(['workflow','run','pages.yml'])), 2)
        self.assertEqual(len(self.calls(['pr','merge'])), 1)
        self.assertFalse(marker.exists())

    def test_dry_run_neither_merges_nor_dispatches_pages(self):
        self.run_queue('--dry-run')
        self.assert_no_pr_mutation()
        self.assertFalse(self.calls(['workflow','run']))

    def test_legacy_chain_selection_cannot_mutate(self):
        self.run_queue('--chaine','test')
        self.assert_no_pr_mutation()


if __name__ == '__main__':
    unittest.main()
