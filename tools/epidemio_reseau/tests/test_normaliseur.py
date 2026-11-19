import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from normaliseur import parse, concorde, nombres
def v(s): return parse(s)
def test_virgule_decimale():
    assert v('0,4 %').bas == 0.4 and v('0.4%').bas == 0.4 and v('0,4').decimales == 1
def test_milliers():
    assert v('17 690').bas == 17690 and v('17\u202f690').bas == 17690 and v("1'240").bas == 1240 and v('17\u00a0690').bas == 17690
def test_fourchette():
    x = v('30 à 40 %'); assert (x.bas, x.haut, x.unite) == (30, 40, '%')
    x = v('3–10 / 100 000 hab./an'); assert (x.bas, x.haut, x.unite) == (3, 10, 'pour 100 000')
def test_qualif():
    assert v('~150 à 200 / 100 000').qualif == '~' and v('< 1 %').qualif == '<' and v('> 5 %').qualif == '>'
def test_unites():
    assert v('5 ‰').bas == 500 and v('5 ‰').unite == 'pour 100 000'
    assert v('2 pour 1 000').bas == 200 and v('3 / 10 000').bas == 30
def test_arrondi():
    assert concorde(v('6,2 %'), v('6.2%')) and concorde(v('6 %'), v('6,2 %')) and not concorde(v('5 %'), v('6,2 %'))
    assert concorde(v('113,6 / 100 000'), v('113.6 pour 100 000')) and not concorde(v('114,6 / 100 000'), v('113.6 pour 100 000'))
def test_unite_incompatible():
    assert concorde(v('5 %'), v('5 pour 100 000')) is False
def test_bug_zero_virgule():
    assert [n for n, _ in nombres('soit 0,4 % et 17 690 cas')] == [0.4, 17690]
if __name__ == '__main__':
    import inspect; [f() for n, f in dict(globals()).items() if n.startswith('test_')]; print('OK')
