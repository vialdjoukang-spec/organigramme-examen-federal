import sys, pathlib
try:
    import pytest
except ImportError:
    pytest = None
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'scripts'))
from applicabilite import classer

CAS = [
    ('', 'N'), ('0', 'N'), (')', 'N'), ('et DX.7', 'N'), ('à DX.2', 'N'), ('(V7-Tunder)', 'N'),
    ('Épuisement du proche aidant donnée non trouvée dans les sources consultées', 'A'),
    ('Bilan lipidique', 'C'), ('IRM du genou antérieur', 'C'), ('Dosage de vitamine D sans facteur de risque', 'C'),
    ('Mammographie et surdiagnostic', 'C'), ('Réadaptation cardiaque', 'C'), ('Signe d’alarme', 'C'), ('Papule', 'C'),
    ('Crampes', 'C'), ('Prurit anal', 'C'), ('Fièvre', 'C'), ('Xérostomie médicamenteuse', 'C'),
    ('Suicide assisté', 'A'), ('Risque suicidaire élevé', 'A'), ('Conduites autodommageables', 'A'),
    ('Tuberculose', 'A'), ('Cancer du sein', 'A'), ('Insomnie (primaire ou comorbide)', 'A'), ('Abus d’antalgiques', 'A'),
    ('Aphasie après accident vasculaire', 'A'),
    ('Syndrome de Duane', 'B'), ('Microcéphalie primitive génétique', 'B'), ('Tremblement essentiel', 'B'),
    ('Céphalée de tension', 'B'), ('Diabète insipide (central ou néphrogénique)', 'B'),
    ('Immunodépression et asplénie', 'B'), ('Perte de connaissance initiale', 'B'),
]

def test_classe():
    for nom, attendu in CAS:
        assert classer(nom)[0] == attendu, (nom, classer(nom))

def test_hypoglycemie_pas_C():
    assert classer('Hypoglycémie')[0] != 'C'

def test_verifie_prime():
    assert classer('Maladie inconnue quelconque', '≥1 vérifié', True)[:1] == ('A',)

def test_confiance_bornee():
    for n, _ in CAS:
        assert 0 < classer(n)[2] <= 1

if __name__ == '__main__':
    test_classe(); test_hypoglycemie_pas_C(); test_verifie_prime(); test_confiance_bornee(); print('test_applicabilite : OK', len(CAS))
