"""Tests techniques locaux ; les attestations simulées ne sont jamais des revues cliniques."""
import copy
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from lxml import etree, html
from PIL import Image
import pipeline_images as p

REAL = p.BASE

def fixture():
    sections=[]
    for i in range(1,15):
        content='<div id="examens"><p>Reconnaître les voies optiques.</p></div>' if i==9 else '<p>Texte conservé.</p>'
        sections.append(f'<section><h2 id="dx-p{i}">{i}. Exemple technique</h2>{content}</section>')
    return '<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Essai technique — anatomie normale</title></head><body><main><h1>Essai technique du clic — aucune lésion clinique</h1>'+''.join(sections)+('<details class="quiz"><summary>Question technique</summary><p>Réponse</p></details>'*14)+'</main></body></html>'

class Pipeline(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(dir=REAL/'_cache',prefix='test-pipeline-')
        self.root=Path(self.tmp.name)
        self.patches=[patch.object(p,'BASE',self.root),patch.object(p.illustrer,'BASE',self.root)]
        for m in self.patches:m.start()
        self.folder=self.root/'LOT_018/illustrations/pipeline'
        self.folder.mkdir(parents=True)
        self.spec=json.loads((REAL/'LOT_018/illustrations/optique.json').read_text())
        target=self.root/self.spec['image'];target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(REAL/self.spec['image'],target)
        self.spec['revue_original']={'sha256':self.spec['sha256_original'],'inspecte':True,'observations':'ATTESTATION SIMULÉE POUR TEST LOCAL UNIQUEMENT'}
        self.sp=self.folder/'spec.json';p.save(self.sp,self.spec)
        self.lesson=self.root/'LOT_018/test.html';self.lesson.write_text(fixture())
        self.job={'id':self.spec['id'],'lecon':'LOT_018/test.html','sha256_lecon':p.sha(self.lesson.read_bytes()),'specification':str(self.sp.relative_to(self.root)),'ancre':'examens','expression':'voies optiques'}
        self.jp=self.folder/'job.json';p.save(self.jp,self.job)
        self.plan={'lot':'LOT_018','integration':str(self.jp.relative_to(self.root)),'revue_rendu':'LOT_018/illustrations/pipeline/revue.json'}
    def tearDown(self):
        for m in reversed(self.patches):m.stop()
        self.tmp.cleanup()
    def test_refus_licences(self):
        for url in ['https://creativecommons.org/licenses/by-nc/4.0/','https://creativecommons.org/licenses/by-nd/4.0/']:
            node=etree.fromstring(f'<front><license href="{url}">Licence</license></front>')
            self.assertEqual(p.license_info(node)['decision'],'exclu_NC_ND')
    def test_version_inconnue(self):
        node=etree.fromstring('<front><license>Creative Commons Attribution</license></front>')
        self.assertEqual(p.license_info(node)['decision'],'reserve_licence')
    def test_cc0_metadonnees_ne_remplace_pas_licence_article(self):
        node=etree.fromstring('<front><license><license-p>Article <ext-link href="https://creativecommons.org/licenses/by/4.0/">CC BY4</ext-link>.</license-p><license-p>The Creative Commons Public Domain Dedication waiver <ext-link href="https://creativecommons.org/publicdomain/zero/1.0/">http://creativecommons.org/publicdomain/zero/1.0/</ext-link> applies to the metadata files associated with this article.</license-p></license></front>')
        result=p.license_info(node)
        self.assertEqual(result['licence'],'CC BY 4.0')
        self.assertEqual(result['perimetres_exclus_du_contenu'][0]['portee'],'métadonnées seules')
    def test_double_licence_sans_portee_reste_en_reserve(self):
        node=etree.fromstring('<front><license><ext-link href="https://creativecommons.org/licenses/by/4.0/"/><ext-link href="https://creativecommons.org/publicdomain/zero/1.0/"/></license></front>')
        self.assertEqual(p.license_info(node)['decision'],'reserve_licence')
    def test_metadonnees_seules_ne_licencient_pas_article(self):
        node=etree.fromstring('<front><license><license-p>The Creative Commons Public Domain Dedication waiver <ext-link href="https://creativecommons.org/publicdomain/zero/1.0/">http://creativecommons.org/publicdomain/zero/1.0/</ext-link> applies to the metadata files associated with this article.</license-p></license></front>')
        self.assertEqual(p.license_info(node)['decision'],'reserve_licence')
    def test_portee_figures_non_assimilee_aux_metadonnees(self):
        node=etree.fromstring('<front><license><ext-link href="https://creativecommons.org/licenses/by/4.0/"/><license-p>The Creative Commons Public Domain Dedication waiver <ext-link href="https://creativecommons.org/publicdomain/zero/1.0/">http://creativecommons.org/publicdomain/zero/1.0/</ext-link> applies to the figures associated with this article.</license-p></license></front>')
        self.assertEqual(p.license_info(node)['decision'],'reserve_licence')
    def test_auteurs_type_porte_par_groupe(self):
        xml=b'<article><front><article-meta><contrib-group content-type="author"><contrib><name><given-names>Lena</given-names><surname>Folkestad</surname></name></contrib></contrib-group></article-meta></front><body/></article>'
        self.assertEqual(p.parse_article(xml,{},'PMC1')['auteur'],'Lena Folkestad')
    def test_editeur_non_attribue_comme_auteur(self):
        xml=b'<article><front><article-meta><contrib-group content-type="author"><contrib contrib-type="editor"><name><given-names>Un</given-names><surname>Editeur</surname></name></contrib><contrib contrib-type="author"><string-name><given-names>Une</given-names><surname>Autrice</surname></string-name></contrib></contrib-group></article-meta></front><body/></article>'
        self.assertEqual(p.parse_article(xml,{},'PMC1')['auteur'],'Une Autrice')
    def test_chemin_hors_perimetre(self):
        with self.assertRaises(ValueError):p.path('../ailleurs')
    def test_lien_symbolique_hors_perimetre(self):
        (self.root/'echappement').symlink_to(self.root.parent,target_is_directory=True)
        with self.assertRaises(ValueError):p.path(self.root/'echappement/fichier',self.root/'echappement')
    def test_empreinte_image_incorrecte(self):
        b=io.BytesIO();Image.new('RGB',(3,3)).save(b,format='PNG')
        with self.assertRaises(ValueError):p.verify_image(b.getvalue(),{'mime':'image/png','md5':'0'*32},'image/png')
    def test_html_pas_image(self):
        with self.assertRaises(ValueError):p.verify_image(b'<html></html>',{'mime':'image/png'},'text/html')
    def test_meme_image_gauche_droite(self):
        self.spec['comparaison']=True;r=html.fromstring(p.illustrer.render(self.spec))
        left=r.xpath('.//div[@class="paire"]//img/@src')[0]
        right=r.xpath('.//*[local-name()="image"]/@href')[0]
        self.assertEqual(left,right)
        self.assertEqual(len(r.xpath('.//div[@class="paire"]//img')),1)
        self.assertTrue(r.xpath('.//*[local-name()="polygon"][@stroke="#dc001f"]'))
    def test_insertion_dans_fenetre_examen(self):
        out=p.injection(fixture(),self.job,'<figure>Échantillon technique</figure>');r=html.fromstring(out)
        self.assertEqual(len(r.xpath('//*[@id="examens"]//button[@popovertarget="image-i018-optique"]')),1)
        self.assertEqual(len(r.xpath('//h2')),14);self.assertEqual(len(r.xpath('//details')),14)
        self.assertEqual(len(r.xpath('//*[@popover="manual"]//figure')),1)
    def test_ancre_hors_examen_refusee(self):
        with self.assertRaises(ValueError):p.injection(fixture(),dict(self.job,ancre='dx-p1'),'<figure/>')
    def test_terme_ambigu_refuse(self):
        with self.assertRaises(ValueError):p.injection(fixture().replace('les voies optiques','les voies optiques et voies optiques'),self.job,'<figure/>')
    def test_inspection_original_requise(self):
        self.spec.pop('revue_original');p.save(self.sp,self.spec)
        with self.assertRaises(ValueError):p.preparer(self.plan,self.folder)
    def prepare_review(self):
        p.preparer(self.plan,self.folder)
        proof=json.loads((self.folder/'i018-optique-preparation.json').read_text())
        cap=self.folder/'capture-test.txt';cap.write_text('Fixture technique de contrôle, pas une vraie capture clinique.')
        review={'sha256_apercu':proof['sha256_apercu'],'inspecte':True,'observations':'SIMULATION POUR TEST','captures':[{'fichier':str(cap.relative_to(self.root)),'sha256':p.sha(cap.read_bytes())}]}
        p.save(self.root/self.plan['revue_rendu'],review)
    def test_integration_preserve_credits_et_structure(self):
        source=self.root/'LOT_018/SOURCES.json';p.save(source,{'images_et_schemas':[{'id':'ancien'}]})
        self.prepare_review();p.integrer(self.plan,self.folder)
        self.assertEqual(len(json.loads(source.read_text())['images_et_schemas']),2)
        self.assertIn('image-i018-optique',self.lesson.read_text())
        with self.assertRaises(ValueError):p.integrer(self.plan,self.folder)
    def test_lecon_modifiee_refusee(self):
        self.prepare_review();self.lesson.write_text(self.lesson.read_text()+'\n')
        with self.assertRaises(ValueError):p.integrer(self.plan,self.folder)
    def test_rendu_modifie_refuse(self):
        self.prepare_review();preview=self.folder/'i018-optique-apercu.html';preview.write_text(preview.read_text()+'\n')
        with self.assertRaises(ValueError):p.integrer(self.plan,self.folder)
    def test_revue_absente_refusee(self):
        p.preparer(self.plan,self.folder)
        with self.assertRaises(FileNotFoundError):p.integrer(self.plan,self.folder)

if __name__=='__main__':unittest.main()
