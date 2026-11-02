"""Rendu des monographies structurées ; aucune validation médicale implicite."""
import json
import re
import sys
from pathlib import Path
import format_lecon as fmt

D = Path(__file__).resolve().parent

def rendre(n):
    data = json.loads((D / f'DX{n}_CONTENU.json').read_text())
    canonical = json.loads((D.parent / 'LISTE_DX_CANONIQUE.json').read_text())
    assert data['titre'] == canonical['diagnostics'][n-1]['nom']
    assert [x['numero'] for x in data['sections']] == list(range(1,14))
    assert len(data['quiz']) == 14
    assert [x['id'] for x in data['sources']] == list(range(1,len(data['sources'])+1))
    refs = [[f"{s['titre']} ; version : {s['date_publication'] or 'non précisée'} ; passages lus : {s['passages_lus']}", s['url']] for s in data['sources']]
    fmt.S = refs
    (D.parent / f'evidence/SOURCES_DX{n}.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n')
    known={s['id'] for s in data['sources']}
    lesson=fmt.Lesson(data['titre'],n)
    for section in data['sections']:
        assert set(section['refs']) <= known
        assert len(re.findall(r'\{[^{}]+\}',section['main'])) == 1
        assert not re.search(r'<(?:script|iframe|img)\b',section['detail_html'],re.I)
        lesson.add(section['main'],section['detail_html'],section['refs'])
    qs=[]
    for q in data['quiz']:
        assert set(q['refs']) <= known
        qs.append((q['question'],q['reponse']+fmt.ref(q['refs'])))
    lesson.quiz(qs,tuple(sorted({x for q in data['quiz'] for x in q['refs']})))
    lesson.write()
    p=D.parent/f'LOT_132_Phase_B_V0_DX.{n}.html'
    s=p.read_text().replace('cours en rédaction ; liste différentielle provisoire, audit distinct avant gel. Illustration en préparation séparée.','monographie en relecture ; sélection canonique issue de la Phase A. Illustration en préparation séparée.')
    p.write_text(s)

if __name__ == '__main__':
    for n in map(int,sys.argv[1:]): rendre(n)
