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
    def test_pr_sh_sans_outil_modifie(self):
        l = next(x for x in open(os.path.join(R, 'tools/arsenal/pr.sh'), encoding='utf-8') if x.startswith('auto=$(git diff'))
        sh = 'set -euo pipefail\ngit() { echo data/tip/S1.1.json; }\n' + l + 'echo FIN'
        p = subprocess.run(['bash', '-c', sh], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0); self.assertIn('FIN', p.stdout)
    def test_dose_hors_concentration(self):
        sys.path.insert(0, A)
        from _c import DOSE
        self.assertEqual(DOSE.findall('ferritine < 30 µg/L ; 50 µg/j'), ['50 µg'])
        for text in ('5 mg/dL', '30 mcg / mL', '5 mg/kg/L'):
            self.assertFalse(DOSE.search(text), text)

    def test_vraies_doses_journalieres_toujours_detectees(self):
        sys.path.insert(0, A)
        from _c import DOSE
        for text in ('50 µg/24 h', '1 g/24h', '5 mg/kg/j', '5 mg/kg/24 h',
                     '5 mg/kg/h', '50 UI/j', '50 µg / 24 h',
                     '5 mg / kg / j', '5 mg/ kg/24 h'):
            self.assertTrue(DOSE.search(text), text)
if __name__ == '__main__': unittest.main()
