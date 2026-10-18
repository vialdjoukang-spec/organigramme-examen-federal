#!/usr/bin/env python3
"""Contrat du relanceur : demande != exécution, acquittement lié à la source."""
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.prevalences import relance_agent as R


def candidate():
    return {'id': 'a', 'url': 'https://example.org/study', 'sha256': 'a' * 64,
            'statut': 'candidat_a_relire', 'audit': {'validation_clinique': False}}


def reviewed():
    c = candidate()
    c['relecture_agent'] = {'statut': 'terminee', 'date': '2026-01-01',
                            'verdict': 'À vérifier', 'source': c['url'], 'sha256': c['sha256'],
                            'loc': 'Tableau 1', 'extrait': '25 patients', 'validation_clinique': False}
    return c


class AgentFollowup(unittest.TestCase):
    def setUp(self):
        mock = patch.object(R, 'catalog', return_value=([], [{'categorie': 'G', 'key': 'G1#0', 'fingerprint': 'current', 'diagnostic': 'eczema'}]))
        mock.start()
        self.addCleanup(mock.stop)

    def state(self, directory, candidates=None):
        path = Path(directory) / 'G.json'
        path.write_text(json.dumps({'category': 'G', 'tasks': {'G1#0': {'diagnostic': 'eczema', 'fingerprint': 'current',
                        'candidates': candidates if candidates is not None else [candidate()]}}}))

    def test_automatic_audit_does_not_acknowledge_source_reading(self):
        self.assertFalse(R.review_completed(candidate()))
        self.assertTrue(R.review_completed(reviewed()))

    def test_review_needs_source_fingerprint_and_documentary_proof(self):
        for key in ('sha256', 'loc', 'extrait', 'date', 'source'):
            with self.subTest(key=key):
                c = reviewed(); c['relecture_agent'].pop(key)
                self.assertFalse(R.review_completed(c))
        c = reviewed(); c['sha256'] = 'b' * 64
        self.assertFalse(R.review_completed(c))
        c = reviewed(); c['relecture_agent']['validation_clinique'] = True
        self.assertFalse(R.review_completed(c))

    def test_retry_date_reopens_uncertain_source_after_deadline(self):
        c = reviewed(); c['relecture_agent']['reessayer_apres'] = '2026-06-01'
        self.assertTrue(R.review_completed(c, datetime(2026, 5, 1, tzinfo=timezone.utc)))
        self.assertFalse(R.review_completed(c, datetime(2026, 7, 1, tzinfo=timezone.utc)))

    def test_queue_distinct_counts_and_excludes_completed(self):
        with tempfile.TemporaryDirectory() as directory:
            done = reviewed(); done['id'] = 'done'
            self.state(directory, [candidate(), candidate(), done])
            self.assertEqual(len(R.build_queue(directory)), 1)

    def test_archived_tasks_and_obsolete_fingerprints_never_notified(self):
        with tempfile.TemporaryDirectory() as directory:
            self.state(directory)
            path = Path(directory) / 'G.json'
            state = json.loads(path.read_text())
            state['tasks']['G1#0']['fingerprint'] = 'obsolete'
            state['tasks']['retired#0'] = {'fingerprint': 'current', 'candidates': [candidate()]}
            path.write_text(json.dumps(state))
            self.assertEqual(R.build_queue(directory), [])

    def test_without_send_never_posts_or_creates_execution_ledger(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(R.subprocess, 'run') as run:
            self.state(directory)
            self.assertEqual(R.main(['--state-dir', directory]), 0)
            run.assert_not_called()
            self.assertEqual(json.loads((Path(directory) / 'agent-file.json').read_text())['a_controler'], 1)
            self.assertFalse((Path(directory) / 'agent-relances.json').exists())

    def test_send_records_request_only_and_same_queue_can_retry_after_cooldown(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(R.subprocess, 'run') as run:
            self.state(directory)
            run.return_value.stdout = json.dumps({'html_url': 'https://github.com/test/comment/1'})
            args = ['--state-dir', directory, '--envoyer']
            self.assertEqual(R.main(args), 0)
            ledger_path = Path(directory) / 'agent-relances.json'
            ledger = json.loads(ledger_path.read_text())
            self.assertEqual(ledger['statut'], 'relance_demandee_non_execution_prouvee')
            self.assertEqual(run.call_count, 1)
            self.assertEqual(R.main(args), 0)
            self.assertEqual(run.call_count, 1)
            ledger['date'] = (datetime.now(timezone.utc) - timedelta(hours=13)).isoformat()
            ledger_path.write_text(json.dumps(ledger))
            self.assertEqual(R.main(args), 0)
            self.assertEqual(run.call_count, 2)
            body = json.loads(run.call_args.kwargs['input'])['body']
            self.assertIn('ne constitue pas une preuve d’exécution', body)

    def test_post_failure_never_claims_request_or_execution(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(R.subprocess, 'run', side_effect=subprocess.CalledProcessError(1, 'gh')):
            self.state(directory)
            with self.assertRaises(subprocess.CalledProcessError):
                R.main(['--state-dir', directory, '--envoyer'])
            self.assertFalse((Path(directory) / 'agent-relances.json').exists())

    def test_empty_queue_does_not_post(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(R.subprocess, 'run') as run:
            R.main(['--state-dir', directory, '--envoyer'])
            run.assert_not_called()
            self.assertEqual(json.loads((Path(directory) / 'agent-file.json').read_text())['a_controler'], 0)


if __name__ == '__main__':
    unittest.main()
