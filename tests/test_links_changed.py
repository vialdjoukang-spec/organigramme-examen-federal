import unittest
from tools.links_changed import changed_urls


class ChangedLinksTests(unittest.TestCase):
    def test_complete_doi_with_parentheses_is_checked(self):
        url='https://doi.org/10.1016/S2213-2600(15)00043-0'
        self.assertEqual(changed_urls('+{"source":"'+url+'"}'),[url])

    def test_only_unbalanced_prose_parentheses_are_removed(self):
        self.assertEqual(changed_urls('+Voir (https://example.org/document).'),
                         ['https://example.org/document'])
        self.assertEqual(changed_urls('+Voir (https://example.org/document(1)).'),
                         ['https://example.org/document(1)'])

    def test_prose_change_on_minified_line_does_not_recheck_unchanged_sources(self):
        diff='-{"cours":"ancien", "source":"https://example.org/ancien.pdf"}\n+{"cours":"nouveau", "source":"https://example.org/ancien.pdf"}'
        self.assertEqual(changed_urls(diff),[])

    def test_new_and_replaced_urls_remain_checked_on_same_minified_line(self):
        diff='-"https://example.org/fixe", "https://example.org/version1"\n+"https://example.org/fixe", "https://example.org/version2", "https://example.org/nouveau"'
        self.assertEqual(changed_urls(diff),['https://example.org/nouveau','https://example.org/version2'])

    def test_new_reference_on_an_added_line_is_checked_without_global_whitelist(self):
        # Un lien déjà utilisé ailleurs, mais absent des lignes retirées, reste vérifié.
        self.assertEqual(changed_urls('+{"source":"https://example.org/existant"}'),['https://example.org/existant'])

    def test_removed_or_moved_links_do_not_become_new_links(self):
        self.assertEqual(changed_urls('-https://example.org/retire'),[])
        self.assertEqual(changed_urls('-https://example.org/deplace\n+https://example.org/deplace'),[])

    def test_headers_are_not_sources_and_new_file_urls_are_checked(self):
        self.assertEqual(changed_urls('+++ b/https://faux.test\n--- a/https://faux.test\n+https://example.org/valide.'),['https://example.org/valide'])


if __name__ == '__main__':
    unittest.main()
