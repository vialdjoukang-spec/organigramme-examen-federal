import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'scripts'))
from recherche import conforme, nom_court

BASE = dict(valeur_txt='14,0', unite='%', population='population générale', age_sexe='adultes ; deux sexes', definition='DSM-IV',
            mesure='prévalence 12 mois', annee='2010', type_source='revue', source='x', url='https://x')

def test_complet_europe():
    assert conforme(dict(BASE, territoire='Europe (UE-27 + CH)'), 'eu') == []
    assert conforme(dict(BASE, territoire='France'), 'eu') == []

def test_contexte_incomplet_refuse():
    assert 'population' in conforme(dict(BASE, territoire='Europe', population=''), 'eu')

def test_hors_europe_refuse():
    assert conforme(dict(BASE, territoire='monde (195 pays)'), 'eu')
    assert conforme(dict(BASE, territoire='États-Unis'), 'eu')

def test_suisse():
    assert conforme(dict(BASE, territoire='Suisse'), 'ch') == []
    assert conforme(dict(BASE, territoire='France'), 'ch')

def test_nom_court():
    assert nom_court('Rhinite allergique (rhume des foins)') == 'Rhinite allergique'

if __name__ == '__main__':
    for k, f in list(globals().items()):
        if k.startswith('test_'): f()
    print('test_completude : OK')
