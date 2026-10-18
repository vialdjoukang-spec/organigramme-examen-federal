"""The crisis mission revises existing G1 records and cannot dispatch broad searches."""
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.coordination.calculer import CONFIG, calculer, empreinte, page, relecture_prototype
from tools.coordination.relance import decision, main
from tools.mono_build import NEW_EXP, REQ


def prototype_fields():
    return {
        'prototype_version': 1,
        **{k: 'Examen précisé.' for k in NEW_EXP},
        'chronologie_version': 1,
        'bilan_ordre': [{'titre': 'À faire en premier', 'texte': 'Examen précisé.'}],
        'pec_ordre': [{'titre': 'Conduite initiale', 'mes': 'Mesure adaptée.', 'pha': 'Traitement indiqué.'}],
    }


class CrisisCoordinationTests(unittest.TestCase):
    def fixture(self, root):
        (root/'data/ck/mono').mkdir(parents=True)
        monos={}
        tasks=[]
        for i in range(4):
            name=f'Maladie {i}'
            monos[f'maladie-{i}']={**{k:'Phrase complète.' for k in REQ},'n':name,'src':'SRC','lu':'18.10.2026'}
            tasks.append(dict(key=f'G1#{i}',ssp='G1',title_ssp='Sudation',secteur='G',categorie='G',
                              i=i,diagnostic=name,fingerprint=f'fp{i}'))
        tasks.append(dict(key='G10#0',ssp='G10',title_ssp='Douleur',secteur='G',categorie='G',
                          i=0,diagnostic='Absente',fingerprint='fp10'))
        (root/'data/ck/mono/m.json').write_text(json.dumps(monos))
        (root/'data/ck/src.json').write_text(json.dumps([{'id':'SRC'}]))
        (root/'data/ck/prev.json').write_text('{}')
        (root/'audit.json').write_text('Contrelecture documentaire indépendante.')
        return monos,tasks

    def config(self):
        return dict(CONFIG,mission_exclusive='infobulles_prototype6',ssp_prioritaire='G1',taille_lot_monographies=3)

    def run_report(self,root,tasks,ledger=None,config=None):
        with patch('tools.coordination.calculer.catalog',return_value=([('G1','Sudation','G'),('G10','Douleur','G')],tasks)):
            return calculer(root,ledger=ledger,config=config or self.config())

    def proof(self,root,mono):
        return {'statut':'revue_documentaire','validation_clinique':False,'date_lu':'2026-01-01',
                'sha256':empreinte(mono),'sources':['SRC'],'rapport':'audit.json',
                'rapport_sha256':hashlib.sha256((root/'audit.json').read_bytes()).hexdigest()}

    def test_prototype_attestation_requires_chronology_flag_for_ssp_and_monography(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);monos,_=self.fixture(root)
            value={**monos['maladie-0'], **prototype_fields()}
            (root/'audit.json').write_text('Contrelecture documentaire indépendante.')
            proof=self.proof(root,value)
            self.assertFalse(relecture_prototype(proof,value,root,{'SRC':{'id':'SRC'}}))
            proof['chronologie_relue']=True
            self.assertTrue(relecture_prototype(proof,value,root,{'SRC':{'id':'SRC'}}))
            value['dia']='Fiche modifiée après la relecture.'
            self.assertFalse(relecture_prototype(proof,value,root,{'SRC':{'id':'SRC'}}))

    def test_existing_g1_comes_before_missing_g10_and_batch_is_bounded(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);_,tasks=self.fixture(root);report=self.run_report(root,tasks)
            self.assertEqual([x['diagnostic_id'] for x in report['plan']['prochain_lot9']],['maladie-0','maladie-1','maladie-2'])
            self.assertEqual(report['mesure']['monographies_structure'],4)
            self.assertEqual(report['mesure']['prototype_structure'],0)
            self.assertEqual(report['mesure']['prototype_relecture'],0)

    def test_mechanical_prototype_without_current_review_stays_in_queue(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);monos,tasks=self.fixture(root)
            old_proof=self.proof(root,monos['maladie-0'])
            monos['maladie-0'].update(prototype_fields())
            (root/'data/ck/mono/m.json').write_text(json.dumps(monos))
            report=self.run_report(root,tasks,{'monographies':{'maladie-0':old_proof}})
            self.assertEqual(report['mesure']['prototype_structure'],1)
            self.assertEqual(report['mesure']['prototype_relecture'],0)
            self.assertEqual(report['plan']['prochain_lot9'][0]['diagnostic_id'],'maladie-0')

    def test_current_review_advances_queue_only_with_chronology_flag_and_current_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);monos,tasks=self.fixture(root)
            for mono in monos.values():mono.update(prototype_fields())
            (root/'data/ck/mono/m.json').write_text(json.dumps(monos))
            ledger={'monographies':{key:self.proof(root,mono) for key,mono in monos.items()}}
            without_flag=self.run_report(root,tasks,ledger)
            self.assertEqual(without_flag['mesure']['prototype_relecture'],0)
            ledger={'monographies':{key:{**self.proof(root,mono), 'chronologie_relue': True}
                                    for key,mono in monos.items()}}
            report=self.run_report(root,tasks,ledger)
            self.assertEqual(report['mesure']['prototype_relecture'],4)
            self.assertEqual(report['plan']['prochain_lot9'][0]['ssp'],'G10')
            monos['maladie-0']['premier']='Un autre bilan initial.'
            (root/'data/ck/mono/m.json').write_text(json.dumps(monos))
            revised=self.run_report(root,tasks,ledger)
            self.assertEqual(revised['mesure']['prototype_relecture'],3)
            self.assertEqual(revised['plan']['prochain_lot9'][0]['ssp'],'G1')

    def test_legacy_config_keeps_missing_monograph_priority(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);_,tasks=self.fixture(root);legacy=self.config();legacy.pop('mission_exclusive')
            report=self.run_report(root,tasks,config=legacy)
            self.assertEqual(report['plan']['prochain_lot9'][0]['diagnostic_id'],'absente')

    def test_crisis_blocks_bootstrap_and_empty_history(self):
        plan={'mission_exclusive':'infobulles_prototype6','intervalle_recherche_minutes':240,'limite_recherche':3}
        for history in [None,{'workflow_runs':[]},{'workflow_runs':[{'status':'completed','created_at':'2020-01-01T00:00:00Z'}]}]:
            self.assertFalse(decision(history,plan,amorcer=True)['lancer'])

    def test_current_crisis_configuration_blocks_stale_plan_without_any_api(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'plan.json';path.write_text(json.dumps({'intervalle_recherche_minutes':240,'limite_recherche':3}))
            with patch('tools.coordination.relance.CONFIG',self.config()),patch('sys.argv',['relance.py','--plan',str(path),'--lancer','--amorcer']),patch('tools.coordination.relance.subprocess.run') as execute,patch('sys.stdout',new_callable=io.StringIO) as output:
                main();execute.assert_not_called()
                self.assertFalse(json.loads(output.getvalue())['lancer'])

    def test_page_distinguishes_prototype_review_and_suspended_research(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);_,tasks=self.fixture(root);report=self.run_report(root,tasks)
            output=page(report)
            self.assertIn('Prototypes avec relecture documentaire actuelle',output)
            self.assertIn('Recherches automatiques transversales suspendues',output)
            self.assertNotIn('Recherche régulée :',output)
            self.assertTrue(report['plan']['recherche_automatique_suspendue'])


if __name__=='__main__':unittest.main()
