"""Fonctions communes : localisation d'une constante JS de premier niveau par str.find.

Les expressions régulières sur des lignes de plusieurs millions de caractères
expirent ; tous les outils passent donc par str.find.
"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.join(ROOT, 'app_v2.html')


def read(path=APP):
    with open(path, encoding='utf-8') as f:
        return f.read()


def write(text, path=APP):
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(text)


def span(s, name):
    """Renvoie (début, fin) de la valeur de « const NAME=… ; » ; la fin exclut le « ; » final."""
    hits = [k for k in ('\nconst ' + name + '=', '\nlet ' + name + '=') if s.count(k)]
    if len(hits) != 1 or s.count(hits[0]) != 1:
        raise SystemExit(f'Constante {name} introuvable ou ambiguë.')
    start = s.find(hits[0]) + len(hits[0])
    end = -1
    if s[start:start + 1] in '[{':
        try:  # une valeur JSON stricte se délimite exactement
            end = json.JSONDecoder().raw_decode(s, start)[1]
        except json.JSONDecodeError:
            end = -1
    if end < 0:
        end = s.find(';\n', start)
    if end < 0:
        raise SystemExit(f'Fin de la constante {name} introuvable.')
    return start, end
