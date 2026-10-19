import json
from pathlib import Path
import tempfile
import subprocess
import unittest
from unittest.mock import patch
from tools.garde.permanence import Store
from tools.garde.relance_bail import occupe,reserver,liberer,renouveler,executer,STATUS,FINISHED


class ReservationTests(unittest.TestCase):
    def test_unknown_or_malformed_lease_cannot_authorize_launch(self):
        for state in ([],{'agent':{}},{'agent':{'owner':'a','expires':'bad'}},
                      {'agent':{'owner':'a','expires':float('nan')}},
                      {'demande':{'owner':'x','expires':200,'statut':'unknown'}}):
            with self.subTest(state=state),self.assertRaises(ValueError):occupe(state,100)

    def test_notification_is_not_executor_but_active_reservation_is(self):
        state={'demande':{'owner':'notice','expires':200,'statut':'demande_non_execution_prouvee'}}
        self.assertFalse(occupe(state,100))
        state['demande']['statut']=STATUS
        self.assertTrue(occupe(state,100));self.assertFalse(occupe(state,201))

    def test_second_checkout_is_blocked_and_only_owner_can_release(self):
        with tempfile.TemporaryDirectory() as tmp,patch('tools.garde.relance_bail.busy_now',return_value=False):
            a=Store(tmp);state=a.read();state['worker']={'owner':'veille','expires':200};a.write(state)
            owner=reserver(a,100);self.assertTrue(owner)
            self.assertIsNone(reserver(Store(tmp),101))
            liberer(Store(tmp),'autre',101);self.assertIsNone(reserver(Store(tmp),102))
            liberer(Store(tmp),owner,101);self.assertIsNone(reserver(Store(tmp),103))
            self.assertTrue(reserver(Store(tmp),221))
            self.assertEqual(Store(tmp).read()['worker']['owner'],'veille')

    def test_competing_agent_cas_cannot_be_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp,patch('tools.garde.relance_bail.busy_now',return_value=False):
            a=Store(tmp)
            write=a.write
            def competing_write(value):
                b=Store(tmp);current=b.read();current['agent']={'owner':'nouvel-agent','expires':300};b.write(current)
                write(value)
            with patch.object(a,'write',side_effect=competing_write),self.assertRaises(RuntimeError):reserver(a,100)
            state=Store(tmp).read()
            self.assertEqual(state['agent']['owner'],'nouvel-agent')
            self.assertNotIn('demande',state)

    def test_process_renewal_blocks_another_machine_after_initial_120s(self):
        with tempfile.TemporaryDirectory() as tmp,patch('tools.garde.relance_bail.busy_now',return_value=False):
            store=Store(tmp);owner=reserver(store,100);now=[100];seen=[]
            class Process:
                pid=123;returncode=None
                def wait(self,timeout):
                    if not seen:
                        seen.append('en_cours');now[0]=279
                        raise subprocess.TimeoutExpired('codex',timeout)
                    seen.append(reserver(Store(tmp),281))
                    self.returncode=0;return 0
                def poll(self):return self.returncode
            with patch('tools.garde.relance_bail.time.time',side_effect=lambda:now[0]),patch('tools.garde.relance_bail.subprocess.Popen',return_value=Process()):
                self.assertEqual(executer(store,owner,['simulation-codex']),0)
            self.assertEqual(seen,['en_cours',None])
            self.assertNotIn('agent',Store(tmp).read())

    def test_lost_reservation_terminates_process_group(self):
        with tempfile.TemporaryDirectory() as tmp,patch('tools.garde.relance_bail.busy_now',return_value=False):
            store=Store(tmp);owner=reserver(store,100)
            class Process:
                pid=123;returncode=None
                def wait(self,timeout):
                    if self.returncode is not None:return self.returncode
                    b=Store(tmp);s=b.read();s['demande']['owner']='autre';b.write(s)
                    raise subprocess.TimeoutExpired('codex',timeout)
                def poll(self):return self.returncode
            process=Process()
            def stop(*_):process.returncode=-15
            with patch('tools.garde.relance_bail.subprocess.Popen',return_value=process),patch('tools.garde.relance_bail.os.killpg',side_effect=stop) as kill:
                with self.assertRaises(RuntimeError):executer(store,owner,['simulation-codex'])
                kill.assert_called_once()

    def test_slow_store_retains_margin_before_next_renewal(self):
        with tempfile.TemporaryDirectory() as tmp,patch('tools.garde.relance_bail.busy_now',return_value=False):
            store=Store(tmp);owner=reserver(store,100);clock=[100]
            read,write=store.read,store.write
            def slow_read():clock[0]+=30;return read()
            def slow_write(value):clock[0]+=35;write(value)
            with patch.object(store,'read',side_effect=slow_read),patch.object(store,'write',side_effect=slow_write),patch('tools.garde.relance_bail.time.time',side_effect=lambda:clock[0]):
                for _ in range(4):
                    previous=read()['demande']['expires']
                    renouveler(store,owner)
                    self.assertLess(clock[0]+5,previous)
                    clock[0]+=30


if __name__=='__main__':unittest.main()
