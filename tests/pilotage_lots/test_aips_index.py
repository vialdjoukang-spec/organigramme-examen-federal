from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from zipfile import ZipFile

from harnais.pilotage_lots.aips_index import inventory


def bundle(kind, language):
    return f'''<MedicinalDocumentsBundle><Type>{kind}</Type>
      <RegulatedAuthorization><Identifier>01234</Identifier></RegulatedAuthorization>
      <AttachedDocument><Language>{language}</Language><Description>Produit synthetique</Description>
      <Period><Start>2026-10-01T00:00:00Z</Start></Period>
      <DocumentReference><ContentType>text/html</ContentType><Url>https://files.refdata.ch/document-99999.html</Url></DocumentReference>
      </AttachedDocument></MedicinalDocumentsBundle>'''


class AipsIndexTests(TestCase):
    def make_archive(self, directory):
        path = Path(directory) / "fixture.zip"
        text = '<MedicinalDocumentsBundles xmlns="https://simisinfo.refdata.ch/MedicinalDocuments/1.0/" generatedOn="2026-10-08T00:30:27Z">'
        text += bundle("SmPC", "fr") + bundle("PIL", "fr") + bundle("SmPC", "de")
        text += '</MedicinalDocumentsBundles>'
        with ZipFile(path, "w") as z:
            z.writestr("index.xml", text)
        return path

    def test_professional_french_information_is_distinguished_from_pil(self):
        with TemporaryDirectory() as directory:
            result = inventory(self.make_archive(directory), "synthetique")
        self.assertEqual(len(result["matches"]), 1)
        self.assertEqual(result["matches"][0]["type"], "SmPC")
        self.assertEqual(result["matches"][0]["language"], "fr")

    def test_authorization_is_not_invented_from_url(self):
        with TemporaryDirectory() as directory:
            result = inventory(self.make_archive(directory), "synthetique")
        self.assertEqual(result["matches"][0]["authorization_identifiers_as_read"], ["01234"])
        self.assertIn("99999", result["matches"][0]["references"][0]["url"])

    def test_index_never_claims_that_monograph_or_dose_was_read(self):
        with TemporaryDirectory() as directory:
            result = inventory(self.make_archive(directory), "synthetique")
        self.assertFalse(result["clinical_validation"])
        self.assertFalse(result["embedded_monograph_text"])
        self.assertFalse(result["matches"][0]["professional_information_read"])
