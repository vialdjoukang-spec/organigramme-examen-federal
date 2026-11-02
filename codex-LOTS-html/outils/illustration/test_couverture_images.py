"""Fixtures synthétiques uniquement; aucune attestation clinique."""
import base64
from pathlib import Path
import tempfile
import unittest

from couverture_images import inventory


class CoverageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=Path(__file__).parent)
        self.addCleanup(self.temp.cleanup)
        self.scope = Path(self.temp.name)
        self.lot = self.scope / 'LOT_TEST'
        self.lot.mkdir()

    def report(self, body):
        (self.lot / 'test.html').write_text('<html><body>' + body + '</body></html>', encoding='utf-8')
        return inventory(self.lot, self.scope)['documents'][0]

    def test_missing_image_and_broken_link(self):
        report = self.report('<section><h2 id="dx1-p9">9</h2><img src="absente.png"><button popovertarget="absente"></button></section>')
        self.assertEqual(report['images'][0]['statut'], 'absente')
        self.assertEqual(report['liens_brises'], ['absente'])
        self.assertIn('asset:absente', report['anomalies'])

    def test_nested_windows_cycle_and_decorations(self):
        (self.lot / 'fixture.png').write_bytes(b'synthetic fixture only')
        report = self.report('''<style>.example{background:url(fake.png)}</style>
          <section><h2 id="a-p9">9</h2><button popovertarget="first"></button><svg><path d="M0 0"/></svg></section>
          <div id="first" popover><button popovertarget="second"></button></div>
          <div id="second" popover><button popovertarget="first"></button><img src="fixture.png"></div>
          <div id="other" popover><img src="foreign.png"></div>''')
        self.assertEqual(report['fenetres'], ['first', 'second'])
        self.assertEqual(len(report['images']), 1)
        self.assertEqual(report['images'][0]['statut'], 'locale_presente')
        self.assertEqual(report['anomalies'], [])

    def test_real_pair_requires_both_assets(self):
        (self.lot / 'original.png').write_bytes(b'synthetic fixture only')
        report = self.report('''<section><h2 id="a-p9">9</h2>
          <figure data-illustration="test"><div class="paire">
          <div><img src="original.png"></div><div><svg><image href="absente.png"/><polygon points="0,0 1,1 1,0"/></svg></div></div>
          <figcaption>Auteur de test — licence déclarée <a href="https://example.test">Source</a></figcaption></figure></section>''')
        self.assertEqual(report['paires'][0]['statut'], 'paire_incomplete_ou_non_verifiable')
        self.assertEqual(len(report['images']), 2)
        self.assertTrue(report['images'][0]['credits_html'])
        self.assertNotIn('licence_validee', report['images'][0])

    def test_embedded_pair_and_svg_image(self):
        fixture = 'data:image/png;base64,' + base64.b64encode(b'synthetic fixture').decode()
        report = self.report(f'''<section><h2 id="a-p9">9</h2><figure><div class="paire"><div><img src="{fixture}"></div>
          <div><svg><image href="{fixture}"/><polygon points="0,0 1,1 1,0"/></svg></div></div></figure></section>''')
        self.assertEqual(report['paires'][0]['statut'], 'deux_vues_presentes')
        self.assertTrue(report['paires'][0]['octets_identiques_sha256'])
        self.assertTrue(report['paires'][0]['reperes_svg_detectes'])
        self.assertNotIn(base64.b64encode(b'synthetic fixture').decode(), str(report))

    def test_scope_escape_encoded_and_symlink(self):
        (self.lot / 'outside.png').symlink_to('/etc/passwd')
        report = self.report('<section><h2 id="a-p9">9</h2><img src="%2E%2E/%2E%2E/private.png"><img src="outside.png"></section>')
        self.assertEqual([i['statut'] for i in report['images']], ['hors_perimetre_ou_illisible'] * 2)
        self.assertTrue(all('sha256' not in i for i in report['images']))

    def test_points_8_and_9_deduplicate_shared_window(self):
        self.report('''<section><h2 id="dx10-p8">8</h2><button popovertarget="shared"></button></section>
          <section><h2 id="dx10-p9">9</h2><button popovertarget="shared"></button></section>
          <div id="shared" popover><img src="missing.png"></div>''')
        report = inventory(self.lot, self.scope, (8, 9))
        self.assertEqual(report['points_demandes'], [8, 9])
        self.assertEqual(len(report['documents'][0]['points_trouves']), 2)
        self.assertEqual(len(report['documents'][0]['images']), 1)
        self.assertEqual(report['documents'][0]['fenetres'], ['shared'])

    def test_no_p9_is_explicit_and_documentary_credit_is_not_coverage(self):
        (self.lot / 'SOURCES.json').write_text('{"images":[{"original":"https://example.test/candidate.png","licence":"déclarée"}]}')
        self.report('<section><h2 id="a-p8">8</h2><img src="p8.png"></section>')
        report = inventory(self.lot, self.scope)
        self.assertEqual(report['totaux']['images_referencees'], 0)
        self.assertEqual(report['documents'][0]['anomalies'], ['point9_absent'])
        self.assertEqual(report['credits_documentaires']['statut'], 'document_lu')


if __name__ == '__main__':
    unittest.main()
