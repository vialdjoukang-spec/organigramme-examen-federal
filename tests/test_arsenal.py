"""Arsenal (tools/arsenal) : extrait, lot, audit_diff, budget --lignes sur données réelles."""
import json, os, subprocess, sys, unittest
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(R, 'tools/arsenal')
def run(*a):
    return subprocess.run([sys.executable, *a], cwd=A, capture_output=True, text=True)
class T(unittest.TestCase):
    def test_extrait_ssp(self):
        o = json.loads(run('extrait.py', 'ssp', 'G1', '--partie', '1').stdout); self.assertEqual(o['partie'], 1)
    def test_extrait_region(self):
        self.assertIn('peau', json.loads(run('extrait.py', 'liste', 'region').stdout))
    def test_extrait_mono(self):
        k = json.loads(run('extrait.py', 'liste', 'mono').stdout)[0]
        self.assertIn(k, json.loads(run('extrait.py', 'mono', k).stdout))
    def test_lot_une_ligne(self):
        p = run('lot.py', 'cours', 'G1'); self.assertEqual(p.returncode, 0); self.assertEqual(len(p.stdout.splitlines()), 1)
    def test_lot_echec(self):
        self.assertEqual(run('lot.py', 'cours', 'Z9').returncode, 1)
    def test_budget_lignes(self):
        p = subprocess.run([sys.executable, 'tools/budget.py', '--lignes', '50', 'app_v2.html'], cwd=R, capture_output=True, text=True)
        self.assertEqual(p.returncode, 1); self.assertIn('TROP LONGUE', p.stdout)
    def test_dose_hors_concentration(self):
        sys.path.insert(0, os.path.join(R, 'tools/arsenal')); from _c import DOSE
        self.assertEqual(DOSE.findall('ferritine < 30 µg/L ; 50 µg/j'), ['50 µg'])
if __name__ == '__main__': unittest.main()
