"""Tests locaux de l'import : aucun réseau ni cliché clinique acquis par ces tests."""
import copy
import importlib.util
import io
import json
import tempfile
import unittest
from email.message import Message
from pathlib import Path
from unittest.mock import Mock

from PIL import Image

spec = importlib.util.spec_from_file_location('acquerir', Path(__file__).with_name('acquerir_commons.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class Reponse(io.BytesIO):
    status = 200

    def __init__(self, raw, mime):
        super().__init__(raw)
        self.headers = Message()
        self.headers['Content-Type'] = mime


class Importer(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='tests-acquisition-', dir=m.BASE / '_cache')
        self.addCleanup(self.tmp.cleanup)
        notices = json.loads((m.BASE / 'LOT_018/illustrations/acquisition/CANDIDATS.json').read_text())['candidats']
        self.s = copy.deepcopy(next(s for s in notices if s['decision'] == 'retenu_sous_reserve_visuelle'))
        self.s['destination'] = str((Path(self.tmp.name) / 'fixture.webp').relative_to(m.BASE))
        # Fixture anatomique déjà présente, explicitement sans prétention clinique.
        self.raw = (m.BASE / 'LOT_018/illustrations/cerveau-inferieur-commons.webp').read_bytes()
        with Image.open(io.BytesIO(self.raw)) as im:
            self.s['dimensions_annoncees'] = list(im.size)
        self.s['mime_annonce'] = 'image/webp'
        self.allowed = {'http_network_policy': {'type': 'restricted', 'egress_rules': [{'host': 'upload.wikimedia.org'}]}}
        self.blocked = {'http_network_policy': {'type': 'restricted', 'egress_rules': []}}

    def test_blocage_avant_toute_requete(self):
        ouvrir = Mock()
        result = m.traiter(self.s, self.blocked, True, ouvrir)
        self.assertEqual(result['statut'], 'bloque_politique_reseau')
        ouvrir.assert_not_called()
        self.assertFalse((m.BASE / self.s['destination']).exists())

    def test_controle_local_sans_telechargement(self):
        ouvrir = Mock()
        result = m.traiter(self.s, self.allowed, False, ouvrir)
        self.assertFalse(result['acquis'])
        ouvrir.assert_not_called()

    def test_candidat_suspendu_refuse_meme_si_reseau_autorise(self):
        notices = json.loads((m.BASE / 'LOT_018/illustrations/acquisition/CANDIDATS.json').read_text())['candidats']
        suspendu = next(s for s in notices if s['id'] == 'rd-fond-oeil')
        self.assertEqual(suspendu['decision'], 'suspendu_provenance')
        ouvrir = Mock()
        with self.assertRaisesRegex(ValueError, 'Candidat non retenu'):
            m.traiter(suspendu, self.allowed, True, ouvrir)
        ouvrir.assert_not_called()
        self.assertFalse((m.BASE / suspendu['destination']).exists())

    def test_licences_nc_nd_inconnues_refusees(self):
        for lic in ['CC BY-NC 4.0', 'CC BY-ND 4.0', 'CC BY-NC-ND 4.0', 'inconnue', 'CC BY 4.0 ou NC']:
            with self.subTest(lic=lic), self.assertRaises(ValueError):
                m.verifier_notice(dict(self.s, licence=lic))

    def test_notice_incomplete_et_licence_url_incoherente(self):
        for change in [{'auteur': ''}, {'passages_lus': ''}, {'acces_le': '2999-01-01'},
                       {'licence_url': 'https://creativecommons.org/licenses/by-nc/4.0/'},
                       {'decision': 'reserve_identification_visuelle'}]:
            with self.subTest(change=change), self.assertRaises(ValueError):
                m.verifier_notice(dict(self.s, **change))

    def test_pages_html_et_dimensions_differentes_refusees(self):
        for raw, mime, s in [(b'<html>Forbidden</html>', 'text/html', self.s),
                             (b'<html>Forbidden</html>', 'image/webp', self.s),
                             (self.raw, 'image/webp', dict(self.s, dimensions_annoncees=[10, 10]))]:
            with self.subTest(mime=mime), self.assertRaises((ValueError, OSError)):
                m.verifier_octets(raw, s, mime)

    def test_original_preserve_et_pas_de_fausse_revue(self):
        result = m.traiter(self.s, self.allowed, True, lambda *a, **k: Reponse(self.raw, 'image/webp'))
        dest = m.BASE / self.s['destination']
        self.assertEqual(dest.read_bytes(), self.raw)
        proof = json.loads(dest.with_name(dest.name + '.source.json').read_text())
        self.assertEqual(proof['sha256_original'], result['sha256_original'])
        self.assertFalse(proof['inspection_visuelle'])
        self.assertIsNone(proof['annotations'])
        self.assertFalse(result['integre'])

    def test_existant_jamais_ecrase(self):
        dest = m.BASE / self.s['destination']
        dest.write_bytes(b'original a conserver')
        ouvrir = Mock()
        with self.assertRaises(ValueError):
            m.traiter(self.s, self.allowed, True, ouvrir)
        ouvrir.assert_not_called()
        self.assertEqual(dest.read_bytes(), b'original a conserver')

    def test_domaines_trompeurs_et_sorties_hors_perimetre(self):
        for change in [{'original_url': 'https://upload.wikimedia.org.evil.test/a.png'},
                       {'original_url': 'https://user:password@upload.wikimedia.org/wikipedia/commons/a.png'},
                       {'destination': '../hors-perimetre.png'}]:
            with self.subTest(change=change), self.assertRaises(ValueError):
                m.verifier_notice(dict(self.s, **change))

    def test_redirection_refusee(self):
        with self.assertRaises(ValueError):
            m.SansRedirection().redirect_request(None, None, 302, '', {}, 'https://autre.test/image.png')


if __name__ == '__main__':
    unittest.main(verbosity=2)
