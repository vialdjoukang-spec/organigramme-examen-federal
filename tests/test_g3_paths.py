"""G3 : une autorisation documentaire ne s'étend pas aux documents voisins."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from audit.niveau1 import _match


class DocumentScope(unittest.TestCase):
    def test_exact_document_without_prefix_collision(self):
        rule = ['onlinelibrary.wiley.com/doi/10.1111/ddg.14988']
        self.assertTrue(_match('https://onlinelibrary.wiley.com/doi/10.1111/ddg.14988', rule))
        for suffix in ('0', '-other', '/supplement'):
            self.assertIsNone(_match('https://onlinelibrary.wiley.com/doi/10.1111/ddg.14988'+suffix, rule))

    def test_subtree_requires_explicit_slash(self):
        url = 'https://www.resus.org.uk/library/2025/child'
        self.assertIsNone(_match(url, ['resus.org.uk/library/2025']))
        self.assertTrue(_match(url, ['resus.org.uk/library/2025/']))
        self.assertIsNone(_match('https://resus.org.uk/library/20250/child', ['resus.org.uk/library/2025/']))

    def test_hostname_boundaries_and_existing_domain_rules(self):
        self.assertTrue(_match('https://www.hug.ch/document', ['hug.ch']))
        self.assertIsNone(_match('https://hug.ch.example.invalid/document', ['hug.ch']))
        self.assertIsNone(_match('https://fakehug.ch/document', ['hug.ch']))

    def test_subtree_does_not_allow_path_escape(self):
        for path in ('allowed/../other', 'allowed/%2e%2e/other', 'allowed/./child'):
            self.assertIsNone(_match('https://example.org/'+path, ['example.org/allowed/']))
        self.assertIsNone(_match('ftp://example.org/allowed/doc', ['example.org/allowed/']))


if __name__ == '__main__':
    unittest.main()
