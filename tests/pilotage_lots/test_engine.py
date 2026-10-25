from copy import deepcopy
from datetime import datetime, timezone, timedelta
import json
from pathlib import Path
import unittest
from harnais.pilotage_lots.engine import (validate_state,number,expected_files,digest,evaluate_lot,acquire,advance,technical)

NOW=datetime(2026,10,25,18,30,tzinfo=timezone.utc)
ROOT=Path(__file__).resolve().parents[2]

def seed():
    state=json.loads((ROOT/'harnais/pilotage_lots/etat.json').read_text())
    state.update(status='active',stop_requested=False)
    return state

def document(key):
    dxs={'A':(), 'B1':(1,2),'B2':(3,4,5),'B3':(6,7),'B4':(8,9,10)}[key]
    text='<!DOCTYPE html>\n<html><body>\n'
    text+='\n'.join(f'<section id="dx{dx}-p{n}"><p>Le point est illustré.</p></section>' for dx in dxs for n in range(1,15))
    text+='\n'+'\n'.join('<p>'+('x'*1900)+'</p>' for _ in range(49))
    return (text+'\n</body></html>\n<!-- FIN_FICHIER LOT_226_TEST -->\n').encode()

class Fake:
    def __init__(self):self.files={};self.read_heads=[]
    def head(self,branch):return '1'*40
    def file(self,path,head):
        self.read_heads.append(head)
        if path not in self.files:raise FileNotFoundError(path)
        return self.files[path]

def complete_case():
    state=seed();job=state['jobs'][0];api=Fake();directory='lot en cours de production/'+job['lot'];pack={'schema_version':1,'files':{}}
    for key,name in expected_files(job['lot']).items():
        raw=document(key);api.files[directory+'/'+name]=raw;entry={}
        for role in ('medical','linguistique','visual','delivery'):
            path=directory+'/'+key+'_'+role+'.html';report=b'<html>Rapport de test.</html>';api.files[path]=report
            r={'file_sha256':digest(raw),'checked_at':(NOW-timedelta(seconds=30 if role=='delivery' else 60)).isoformat(),
               'report_path':path,'report_sha256':digest(report)}
            if role in {'medical','linguistique'}:r.update(role=role,auditor_id='independent',score=95,critical_count=0,full_read=True,critical_sources_read=True)
            elif role=='visual':r.update(width_px=390,performed=True,authorized_environment=True)
            else:r.update(destination='Drive Finaux',remote_file_id='actual-test-receipt',verified=True)
            entry[role]=r
        pack['files'][key]=entry
    return state,job,api,pack

def upload(api,job,pack):api.files['lot en cours de production/'+job['lot']+'/VALIDATION_V8.json']=json.dumps(pack).encode()

class Gates(unittest.TestCase):
    def setUp(self):self.state,self.job,self.api,self.pack=complete_case()
    def evaluate(self):upload(self.api,self.job,self.pack);return evaluate_lot(self.api,self.job,NOW)
    def test_complete_proofs_pass_and_pin_head(self):
        self.assertTrue(self.evaluate()['complete']);self.assertEqual(set(self.api.read_heads),{'1'*40})
    def test_drafts_without_audits_do_not_pass(self):
        self.pack['files']={};r=self.evaluate();self.assertFalse(r['complete']);self.assertEqual(r['next_action']['action'],'audit_or_correct')
    def test_self_review_rejected(self):
        self.pack['files']['A']['medical']['auditor_id']='root';self.assertFalse(self.evaluate()['complete'])
    def test_document_changed_invalidates_old_scores(self):
        name=expected_files('LOT_226')['B3'];self.api.files['lot en cours de production/LOT_226/'+name]+=b' '
        self.assertFalse(self.evaluate()['complete'])
    def test_report_changed_rejected(self):
        self.api.files[self.pack['files']['A']['medical']['report_path']]+=b'X';self.assertFalse(self.evaluate()['complete'])
    def test_critical_or_low_score_rejected(self):
        for field,value in [('score',89.99),('critical_count',1),('full_read',False),('critical_sources_read',False)]:
            with self.subTest(field=field):
                saved=deepcopy(self.pack);self.pack['files']['B4']['medical'][field]=value
                self.assertFalse(self.evaluate()['complete']);self.pack=saved
    def test_nonfinite_and_bool_scores_rejected(self):
        for value in [True,float('nan'),float('inf')]:
            self.pack['files']['A']['medical']['score']=value;self.assertFalse(self.evaluate()['complete'])
    def test_visual_not_inferred_from_static(self):
        self.pack['files']['B2']['visual']['performed']=False;r=self.evaluate()
        self.assertFalse(r['complete']);self.assertEqual(r['next_action']['action'],'await_authorized_visual_proof')
    def test_missing_audit_prioritized_over_other_file_visual_block(self):
        self.pack['files']['A']['visual']['performed']=False;self.pack['files']['B4'].pop('medical')
        r=self.evaluate();self.assertEqual((r['next_action']['file'],r['next_action']['action']),('B4','audit_or_correct'))
    def test_delivery_cannot_precede_validations(self):
        self.pack['files']['A']['delivery']['checked_at']=(NOW-timedelta(hours=2)).isoformat();self.assertFalse(self.evaluate()['complete'])
    def test_delivery_missing_rejected(self):
        self.pack['files']['B1'].pop('delivery');self.assertFalse(self.evaluate()['complete'])
    def test_cross_lot_report_rejected(self):
        self.pack['files']['A']['medical']['report_path']='lot en cours de production/LOT_225/audit.html';self.assertFalse(self.evaluate()['complete'])
    def test_future_and_naive_dates_rejected(self):
        for value in [(NOW+timedelta(days=1)).isoformat(),'2026-10-25T18:00:00']:
            self.pack['files']['A']['medical']['checked_at']=value;self.assertFalse(self.evaluate()['complete'])
    def test_missing_file_prevents_completion(self):
        del self.api.files['lot en cours de production/LOT_226/'+expected_files('LOT_226')['B4']]
        r=self.evaluate();self.assertFalse(r['complete']);self.assertEqual(r['next_action'],{'action':'write','file':'B4'})
    def test_html_cadence_and_script_rejected(self):
        data=document('B1').replace(b'</body>',b'<script></script><section id="dx3-p1"></section></body>')
        self.assertTrue(technical(data,'B1'))

class Coordination(unittest.TestCase):
    def setUp(self):
        self.state=seed();self.owner='session-real';self.token='real-session-token-1234'
        self.eval={'LOT_226':{'lot':'LOT_226','branch':self.state['jobs'][0]['branch'],'complete':True,'head':'1'*40}}
        self.reserved={'complete':True,'checked_at':NOW.isoformat(),'lots':[]}
    def advance(self):return advance(self.state,self.owner,self.token,'root',self.eval,self.reserved,NOW)
    def test_archived_configuration_is_stopped(self):
        state=json.loads((ROOT/'harnais/pilotage_lots/etat.json').read_text())
        self.assertEqual(state['status'],'paused');self.assertTrue(state['stop_requested'])
        with self.assertRaises(ValueError):acquire(state,self.owner,self.token,NOW)
    def test_initial_state_and_number_range(self):
        validate_state(self.state)
        for value in ['LOT_000','LOT_249','LOT_1',True]:
            with self.assertRaises(ValueError):number(value)
    def test_next_free_lot_is_224_and_does_not_touch_partner(self):
        result=self.advance();self.assertEqual(result['jobs'][-1]['lot'],'LOT_224')
        self.assertEqual(result['jobs'][1],self.state['jobs'][1]);self.assertEqual(self.state['jobs'][0]['state'],'review')
    def test_incomplete_lot_does_not_advance(self):
        self.eval['LOT_226']['complete']=False
        with self.assertRaises(ValueError):self.advance()
    def test_wrong_evaluation_not_accepted(self):
        self.eval['LOT_226']['lot']='LOT_225'
        with self.assertRaises(ValueError):self.advance()
    def test_active_foreign_lease_denies_second_worker(self):
        self.state=acquire(self.state,'other-owner','another-real-token',NOW)
        with self.assertRaises(ValueError):self.advance()
    def test_own_lease_can_renew_and_expired_lease_can_transfer(self):
        state=acquire(self.state,self.owner,self.token,NOW)
        self.assertEqual(acquire(state,self.owner,self.token,NOW)['lease']['owner'],self.owner)
        self.assertEqual(acquire(state,'next-owner','another-real-token',NOW+timedelta(minutes=21))['lease']['owner'],'next-owner')
    def test_stop_quota_pause_block_mutations(self):
        for mode in ['stop','quota_exhausted','paused']:
            self.state=seed()
            if mode=='stop':self.state['stop_requested']=True
            else:self.state['status']=mode
            with self.assertRaises(ValueError):self.advance()
    def test_reservation_inventory_must_be_fresh_and_complete(self):
        for value in [{'complete':False,'lots':[]},{'complete':True,'lots':[],'checked_at':(NOW-timedelta(minutes=6)).isoformat()}]:
            self.reserved=value
            with self.assertRaises(ValueError):self.advance()
    def test_other_branch_claim_is_skipped_not_stolen(self):
        self.reserved['lots']=['LOT_224'];self.assertEqual(self.advance()['jobs'][-1]['lot'],'LOT_223')
    def test_duplicate_worker_and_protected_lot_rejected(self):
        for change in ['worker','protected']:
            state=seed()
            if change=='worker':state['jobs'][1]['worker']='root';state['jobs'][1]['writers']=['root']
            else:state['protected_lots'].append('LOT_226')
            with self.assertRaises(ValueError):validate_state(state)

if __name__=='__main__':unittest.main()
