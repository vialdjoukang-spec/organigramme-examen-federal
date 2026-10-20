import importlib.util
from pathlib import Path
import unittest
spec=importlib.util.spec_from_file_location('gate',Path(__file__).resolve().parents[1]/'tools/predecesseurs_fusion.py')
gate=importlib.util.module_from_spec(spec);spec.loader.exec_module(gate)

class ChainOrder(unittest.TestCase):
    plan={'chaines':{'doses':[59,61,67,70],'other':[50,53,70]}}
    def test_open_predecessor_blocks(self):
        self.assertFalse(gate.ready(self.plan,61,lambda n:'OPEN'))
    def test_all_previous_must_finish(self):
        self.assertFalse(gate.ready(self.plan,70,lambda n:'OPEN' if n==53 else 'MERGED'))
    def test_closed_or_merged_allows(self):
        self.assertTrue(gate.ready(self.plan,67,lambda n:'CLOSED' if n==59 else 'MERGED'))
    def test_error_never_allows(self):
        def error(n):raise OSError('API inaccessible')
        self.assertFalse(gate.ready(self.plan,61,error))
    def test_first_or_unlisted_has_no_dependency(self):
        def unexpected(n):raise AssertionError('aucun appel nécessaire')
        self.assertTrue(gate.ready(self.plan,59,unexpected))
        self.assertTrue(gate.ready(self.plan,999,unexpected))


class MandateIntegration(unittest.TestCase):
    sha = 'a' * 40

    def config(self, entries=None):
        return {'version': 1, 'actif': True, 'priorite_active': 'P0',
                'fusion_clinique': 'manuelle_centralisee',
                'autorisations_techniques': [] if entries is None else entries}

    def entry(self, **updates):
        return dict(number=123, head_sha=self.sha, priorite='P0', **updates)

    def test_empty_p0_blocks_unknown_alpha_beta_gamma_and_legacy(self):
        for number in (123, 161, 160, 150, 37):
            self.assertFalse(gate.authorize(self.config(), number, self.sha))

    def test_only_explicit_exact_head_is_authorized(self):
        config = self.config([self.entry()])
        self.assertTrue(gate.authorize(config, 123, self.sha))
        self.assertFalse(gate.authorize(config, 124, self.sha))
        self.assertFalse(gate.authorize(config, 123, 'b' * 40))

    def test_bad_inactive_missing_config_or_future_priority_refused(self):
        for config in ({}, None, self.config([dict(number=123, head_sha=self.sha, priorite='P1')]),
                       {**self.config(), 'actif': False},
                       self.config([self.entry(), self.entry()]),
                       self.config([dict(number=True, head_sha=self.sha, priorite='P0')])):
            with self.subTest(config=config), self.assertRaises(ValueError):
                gate.authorize(config, 123, self.sha)

    def test_clinical_or_unknown_paths_never_technical(self):
        for path in ('data/tip/S3.6.json', 'data/ck/mono/x.json', 'app_v2.html',
                     'assets/config/tip.js', 'assets/config/fonctions.js',
                     'data/cs/thorax.json', 'tools/cours/lots/S3.6.json',
                     'tools/patches/inject.py', '../tools/fake.py'):
            self.assertFalse(gate.technical_path(path), path)
        for path in ('tools/predecesseurs_fusion.py', 'tools/mandat/integration.json',
                     '.github/workflows/auto-fusion.yml', 'tests/test_file_fusion.py'):
            self.assertTrue(gate.technical_path(path), path)

    def checks(self):
        return [{'name': name, 'status': 'COMPLETED', 'conclusion': 'SUCCESS'}
                for name in gate.REQUIRED]

    def test_all_required_success_and_optional_skipped(self):
        self.assertTrue(gate.checks_green(self.checks() + [
            {'name': 'liens', 'status': 'COMPLETED', 'conclusion': 'SKIPPED'}]))
        self.assertTrue(gate.checks_green(self.checks() + [
            {'name': 'auto-fusion', 'status': 'IN_PROGRESS', 'conclusion': None}]))

    def test_required_skip_neutral_missing_or_any_optional_failure_blocks(self):
        for conclusion in ('SKIPPED', 'NEUTRAL', 'FAILURE', 'CANCELLED', ''):
            checks = self.checks()
            checks[0]['conclusion'] = conclusion
            self.assertFalse(gate.checks_green(checks), conclusion)
        self.assertFalse(gate.checks_green(self.checks()[1:]))
        self.assertFalse(gate.checks_green(self.checks() + [
            {'name': 'auto-fusion', 'status': 'COMPLETED', 'conclusion': 'FAILURE'}]))
        for status, conclusion in (('COMPLETED', 'FAILURE'), ('IN_PROGRESS', None),
                                   ('QUEUED', None), ('COMPLETED', 'TIMED_OUT')):
            self.assertFalse(gate.checks_green(self.checks() + [
                {'name': 'liens', 'status': status, 'conclusion': conclusion}]))

    def test_workflow_uses_main_guard_and_exact_head_without_update(self):
        workflow = (Path(__file__).resolve().parents[1]/'.github/workflows/auto-fusion.yml').read_text()
        self.assertIn('  pull_request_target:', workflow)
        self.assertNotIn('  pull_request:', workflow)
        self.assertIn('ref: main', workflow)
        self.assertNotIn('ref: ${{ github.event.pull_request.head.sha }}', workflow)
        self.assertIn('--match-head-commit "$HEAD_SHA"', workflow)
        self.assertNotIn('/update-branch', workflow)
        self.assertNotIn('--auto', workflow)
        self.assertIn('--merge --match-head-commit', workflow)

    def test_api_failure_fails_closed_cli(self):
        from unittest.mock import patch
        with patch.object(gate, 'canonical_config', side_effect=OSError('offline')):
            with patch('sys.argv', ['gate', '123', '--check']):
                self.assertEqual(gate.main(), 1)
            with patch('sys.argv', ['gate', '--list']):
                self.assertEqual(gate.main(), 1)

    def test_main_configuration_not_pr_configuration(self):
        import base64
        from unittest.mock import patch
        calls = []
        def fake(*args):
            calls.append(args)
            if args[1].endswith('/branches/main'):
                return __import__('json').dumps({'commit': {'sha': self.sha}})
            return __import__('json').dumps({'encoding': 'base64', 'content': base64.b64encode(
                __import__('json').dumps(self.config()).encode()).decode()})
        with patch.object(gate, 'gh', side_effect=fake):
            self.assertEqual(gate.canonical_config('owner/repo'), self.config())
        self.assertIn('ref=' + self.sha, calls[1][1])

    def integration_case(self, mutate):
        import copy
        import json
        from unittest.mock import patch
        config = self.config([self.entry()])
        pr = {'state': 'OPEN', 'isDraft': False, 'baseRefName': 'main',
              'mergeStateStatus': 'CLEAN', 'headRefOid': self.sha,
              'labels': [{'name': 'audit-ok'}], 'statusCheckRollup': self.checks(), 'changedFiles': 1}
        def files(*args):
            mutate(config, pr)  # Changement pendant la lecture des fichiers de la PR.
            return [{'filename': 'tools/gate.py'}]
        with patch.object(gate, 'canonical_config', side_effect=lambda *args: copy.deepcopy(config)), \
             patch.object(gate, 'changed_files', side_effect=files), \
             patch.object(gate, 'gh', side_effect=lambda *args: json.dumps(pr)):
            return gate.integration_ready('owner/repo', 123, self.sha)

    def test_stable_complete_final_snapshot_allows(self):
        self.assertTrue(self.integration_case(lambda config, pr: None))

    def test_changed_head_during_final_recheck_blocks(self):
        self.assertFalse(self.integration_case(lambda config, pr: pr.update(headRefOid='b' * 40)))

    def test_main_allowlist_revoked_during_file_read_blocks(self):
        self.assertFalse(self.integration_case(
            lambda config, pr: config.update(autorisations_techniques=[])))

    def test_priority_changed_during_file_read_blocks_even_if_reauthorized(self):
        def mutate(config, pr):
            config['priorite_active'] = 'P1'
            config['autorisations_techniques'][0]['priorite'] = 'P1'
        self.assertFalse(self.integration_case(mutate))

    def test_main_disabled_during_file_read_blocks(self):
        self.assertFalse(self.integration_case(lambda config, pr: config.update(actif=False)))

    def test_audit_label_removed_during_file_read_blocks(self):
        self.assertFalse(self.integration_case(lambda config, pr: pr.update(labels=[])))

    def test_attente_vial_added_during_file_read_blocks(self):
        self.assertFalse(self.integration_case(
            lambda config, pr: pr['labels'].append({'name': 'attente-vial'})))

    def test_ci_restarted_at_same_sha_during_file_read_blocks(self):
        self.assertFalse(self.integration_case(lambda config, pr:
            pr['statusCheckRollup'][0].update(status='IN_PROGRESS', conclusion=None)))

    def test_merge_state_changed_during_file_read_blocks(self):
        self.assertFalse(self.integration_case(lambda config, pr: pr.update(mergeStateStatus='BEHIND')))

if __name__ == '__main__':
    unittest.main()
