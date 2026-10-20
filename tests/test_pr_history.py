"""Le vrai script de PR conserve les commits publiés et refuse leur écrasement."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'tools/arsenal/pr.sh'


class PublishedHistory(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.repo = self.root / 'author'
        self.remote = self.root / 'remote.git'
        self.env = {**os.environ, 'GIT_AUTHOR_NAME': 'Test', 'GIT_AUTHOR_EMAIL': 'test@example.invalid',
                    'GIT_COMMITTER_NAME': 'Test', 'GIT_COMMITTER_EMAIL': 'test@example.invalid'}
        self.git(self.root, 'init', '--bare', str(self.remote))
        self.git(self.root, 'clone', str(self.remote), str(self.repo))
        self.git(self.repo, 'checkout', '-b', 'main')
        (self.repo / 'assets').mkdir()
        (self.repo / 'data').mkdir()
        (self.repo / 'base').write_text('base')
        self.git(self.repo, 'add', '.')
        self.git(self.repo, 'commit', '-m', 'base')
        self.git(self.repo, 'push', '-u', 'origin', 'main')
        self.git(self.repo, 'checkout', '-b', 'feature')
        (self.repo / 'author').write_text('author')
        self.git(self.repo, 'add', '.')
        self.git(self.repo, 'commit', '-m', 'author')
        self.published = self.git(self.repo, 'rev-parse', 'HEAD').stdout.strip()
        self.git(self.repo, 'push', '-u', 'origin', 'feature')
        bin_path = self.root / 'bin'
        bin_path.mkdir()
        for name, body in [('python3', 'exit 0'), ('gh', 'echo https://example.invalid/pr/1')]:
            script = bin_path / name
            script.write_text('#!/bin/sh\n'+body+'\n')
            script.chmod(0o755)
        self.env['PATH'] = str(bin_path)+os.pathsep+os.environ['PATH']

    def git(self, cwd, *args, check=True):
        return subprocess.run(['git', *args], cwd=cwd, env=self.env,
                              text=True, capture_output=True, check=check)

    def run_script(self):
        return subprocess.run(['bash', str(SCRIPT), 'Technical test'], cwd=self.repo,
                              env=self.env, text=True, capture_output=True, timeout=20)

    def test_main_update_keeps_published_commit_as_ancestor(self):
        self.git(self.repo, 'checkout', 'main')
        (self.repo / 'main-update').write_text('new main')
        self.git(self.repo, 'add', '.')
        self.git(self.repo, 'commit', '-m', 'main update')
        main = self.git(self.repo, 'rev-parse', 'HEAD').stdout.strip()
        self.git(self.repo, 'push', 'origin', 'main')
        self.git(self.repo, 'checkout', 'feature')
        result = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        for sha in (main, self.published):
            self.assertEqual(self.git(self.repo, 'merge-base', '--is-ancestor', sha, 'HEAD').returncode, 0)
        self.assertEqual(len(self.git(self.repo, 'rev-list', '--parents', '-n', '1', 'HEAD').stdout.split()), 3)

    def test_concurrent_published_work_is_never_force_pushed(self):
        other = self.root / 'other'
        self.git(self.root, 'clone', '--branch', 'feature', str(self.remote), str(other))
        (other / 'independent').write_text('independent work')
        self.git(other, 'add', '.')
        self.git(other, 'commit', '-m', 'independent author')
        independent = self.git(other, 'rev-parse', 'HEAD').stdout.strip()
        self.git(other, 'push', 'origin', 'feature')
        # Même avec un remote-tracking à jour, le script ne doit pas écraser ce commit.
        self.git(self.repo, 'fetch', 'origin', 'feature')
        result = self.run_script()
        self.assertNotEqual(result.returncode, 0)
        remote_head = self.git(self.repo, 'ls-remote', 'origin', 'refs/heads/feature').stdout.split()[0]
        self.assertEqual(remote_head, independent)


if __name__ == '__main__':
    unittest.main()
