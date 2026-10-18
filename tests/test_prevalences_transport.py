import io
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from tools.prevalences.moteur import Client, FetchError, Societes, source_editoriale, expected_protocol, search_task


class TransportTests(unittest.TestCase):
    def test_transient_http_retried_then_cached(self):
        with tempfile.TemporaryDirectory() as directory:
            client=Client(directory,interval=0)
            with patch('tools.prevalences.moteur.urlopen',side_effect=[HTTPError('https://example.org/data',503,'temp',{},None),io.BytesIO(b'{"ok":true}')]) as call,patch('tools.prevalences.moteur.time.sleep'):
                self.assertTrue(client.get_json('https://example.org/data')['ok'])
                self.assertEqual(call.call_count,2)
                self.assertTrue(client.get_json('https://example.org/data')['ok'])
                self.assertEqual(call.call_count,2)
    def test_forbidden_never_retried_or_bypassed(self):
        with tempfile.TemporaryDirectory() as directory:
            client=Client(directory,interval=0)
            with patch('tools.prevalences.moteur.urlopen',side_effect=HTTPError('https://example.org',403,'forbidden',{},None)) as call:
                with self.assertRaises(FetchError):client.fetch('https://example.org/a')
                with self.assertRaises(FetchError):client.fetch('https://example.org/b')
                self.assertEqual(call.call_count,1)
    def test_proxy_denial_is_visible_and_not_zero_results(self):
        with tempfile.TemporaryDirectory() as directory:
            client=Client(directory,interval=0)
            with patch('tools.prevalences.moteur.urlopen',side_effect=URLError('Tunnel connection failed:403 Forbidden')):
                with self.assertRaises(FetchError) as error:client.fetch('https://example.org/')
                self.assertEqual(error.exception.details['http_status'],403)
                self.assertFalse(error.exception.details['reessayable'])
    def test_html_shell_not_cached_as_json(self):
        with tempfile.TemporaryDirectory() as directory:
            client=Client(directory,interval=0)
            with patch('tools.prevalences.moteur.urlopen',return_value=io.BytesIO(b'<html>captcha</html>')):
                with self.assertRaises(ValueError):client.get_json('https://example.org/')
                self.assertEqual(list(Path(directory).iterdir()),[])
    def test_recognized_source_suffix_is_not_domain_spoof(self):
        self.assertEqual(source_editoriale('https://reco.sfdermato.org/x'),'SFD')
        self.assertIsNone(source_editoriale('https://sfdermato.org.evil.test/x'))
        self.assertIsNone(source_editoriale('https://ehaweb.org/x'))
    def test_protocol_includes_scientific_societies(self):
        protocol=expected_protocol();self.assertIn(('societes','Europe:societes'),protocol)
        self.assertEqual(len(protocol),10)
    def test_official_link_context_keeps_discovery_provenance(self):
        registry={'sources':[{'id':'SFD','verified':True,'domaines':['sfdermato.org'],'index_recherche':['https://sfdermato.org/index']} ]}
        class FakeClient:
            def fetch(self,url):
                if url.endswith('/index'):return b'<h2>Psoriasis</h2><a href="https://doi.org/10.1/guideline">Texte integral</a>'
                return b'Psoriasis prevalence 10% among selected patients.'
        task={'diagnostic':'Psoriasis','title_ssp':'Prurit'}
        with patch('tools.prevalences.moteur.load_registry',return_value=registry):
            _,docs=Societes(FakeClient()).search(task)
        self.assertEqual(len(docs),1)
        self.assertEqual(docs[0]['index_origine'],'https://sfdermato.org/index')
        self.assertEqual(docs[0]['source_editoriale_id'],'SFD')
        self.assertFalse(docs[0]['population_verifiee'])
        self.assertIsNone(source_editoriale(docs[0]['url']))
    def test_one_society_failure_keeps_query_partial_and_candidates(self):
        class FakeSocietes:
            def __init__(self,client):self.traces=[]
            def search(self,task):
                self.traces=[{'ok':True,'url':'https://sfdermato.org'}, {'ok':False,'url':'https://ersnet.org','erreur':'HTTP403'}]
                return 'https://example.org/index',[{'url':'https://sfdermato.org/page','text':'Psoriasis 10%','loc':'HTML'}]
        with patch('tools.prevalences.moteur.Societes',FakeSocietes):
            result=search_task({'diagnostic':'Psoriasis','title_ssp':'Prurit'},SimpleNamespace(deadline=float('inf')),None,['societes'])
        self.assertEqual(result['statut'],'erreur')
        self.assertFalse(result['queries'][0]['ok'])
        self.assertEqual(len(result['queries'][0]['trace_sources']),2)
        self.assertEqual(len(result['candidates']),1)


if __name__=='__main__':unittest.main()
