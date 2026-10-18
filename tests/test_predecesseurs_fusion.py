import importlib.util
from pathlib import Path
import unittest
spec=importlib.util.spec_from_file_location('gate',Path(__file__).resolve().parents[1]/'tools/predecesseurs_fusion.py')
gate=importlib.util.module_from_spec(spec);spec.loader.exec_module(gate)

class ChainOrder(unittest.TestCase):
    plan={'chaines':{'doses':[59,61,67,70],'other':[50,53,70]}}
    def test_open_predecessor_blocks(self):
        self.assertFalse(gate.ready(self.plan,61,lambda n:'OPEN'))
    def test_all_previous_must_finish(self):
        self.assertFalse(gate.ready(self.plan,70,lambda n:'OPEN' if n==53 else 'MERGED'))
    def test_closed_or_merged_allows(self):
        self.assertTrue(gate.ready(self.plan,67,lambda n:'CLOSED' if n==59 else 'MERGED'))
    def test_error_never_allows(self):
        def error(n):raise OSError('API inaccessible')
        self.assertFalse(gate.ready(self.plan,61,error))
    def test_first_or_unlisted_has_no_dependency(self):
        def unexpected(n):raise AssertionError('aucun appel nécessaire')
        self.assertTrue(gate.ready(self.plan,59,unexpected))
        self.assertTrue(gate.ready(self.plan,999,unexpected))

if __name__=='__main__':unittest.main()
