#!/usr/bin/env python3
"""Exercise the real queue with a fake GitHub CLI, including failed publication retries."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'tools/file_fusion.sh'
FAKE_GH = '''#!/usr/bin/env python3
import json, os, pathlib, sys
a = sys.argv[1:]
root = pathlib.Path(os.environ['OEF_REPO'])
with (root/'calls.jsonl').open('a') as f: f.write(json.dumps(a)+'\\n')
if a[:2] == ['auth','status']: sys.exit(0)
if a[:1] == ['api'] and 'protection' in a[1]:
 print('{"message":"Resource not accessible by integration"}'); sys.exit(1)
if a[:2] == ['pr','view']:
 print((root/'pr.json').read_text()); sys.exit(0)
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
        gh = self.root/'bin/gh'
        gh.write_text(FAKE_GH)
        gh.chmod(0o755)
        self.env = {**os.environ, 'OEF_REPO': str(self.root),
                    'PATH': str(self.root/'bin')+os.pathsep+os.environ['PATH']}
        self.pr = {'state':'OPEN', 'labels':[{'name':'audit-ok'}], 'isDraft':False,
                   'mergeStateStatus':'CLEAN', 'headRefOid':'abc123',
                   'statusCheckRollup':[{'name':n, 'status':'COMPLETED', 'conclusion':'SUCCESS'}
                                        for n in ('garde','html','tests','visuel')]}

    def run_queue(self, *args):
        (self.root/'pr.json').write_text(json.dumps(self.pr))
        result = subprocess.run(['bash', str(SCRIPT), *args], env=self.env,
                                text=True, capture_output=True, timeout=20)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result

    def calls(self, prefix):
        return [a for a in map(json.loads, (self.root/'calls.jsonl').read_text().splitlines())
                if a[:len(prefix)] == prefix]

    def test_protection_error_uses_required_checks_and_merge_head(self):
        self.run_queue()
        self.assertEqual(self.calls(['pr','merge']),
                         [['pr','merge','123','--merge','--match-head-commit','abc123']])

    def test_missing_failed_or_pending_check_never_merges(self):
        for conclusion in ('FAILURE', ''):
            with self.subTest(conclusion=conclusion):
                self.pr['statusCheckRollup'][-1]['conclusion'] = conclusion
                self.run_queue()
                self.assertFalse(self.calls(['pr','merge']))
        self.pr['statusCheckRollup'].pop()
        self.run_queue()
        self.assertFalse(self.calls(['pr','merge']))

    def test_attente_vial_suspends_even_if_audited_and_green(self):
        self.pr['labels'].append({'name':'attente-vial'})
        self.run_queue()
        self.assertFalse(self.calls(['pr','merge']))

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
        self.assertFalse(self.calls(['pr','merge']))
        self.assertFalse(self.calls(['workflow','run']))


if __name__ == '__main__':
    unittest.main()
