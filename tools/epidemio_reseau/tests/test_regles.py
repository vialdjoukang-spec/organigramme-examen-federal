import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from regles import apparier
def cles(n): return [k for k, _ in apparier(n)]
def test_faux_positifs():
    assert not any(k.startswith('idd:TBE') for k in cles('Acidocétose diabétique'))
    assert not any(k.startswith('idd:TBE') for k in cles('Problèmes musculo-squelettiques'))
    assert 'ms:116' not in cles('Polydipsie primaire (potomanie)')
    assert not any(k.startswith('can:C70') for k in cles('Métastases cérébrales'))
def test_exacts():
    assert ('idd:TUBERCULOSIS_oblig:inc', 'exact') in apparier('Tuberculose')
    assert ('can:C50:inc_f', 'exact') in apparier('Carcinome mammaire infiltrant')
    assert ('obs:diabete', 'exact') in apparier('Diabète sucré')
    assert ('ms:169', 'groupe') in apparier('Pneumonie communautaire')
if __name__ == '__main__':
    [f() for n, f in dict(globals()).items() if n.startswith('test_')]; print('OK')
