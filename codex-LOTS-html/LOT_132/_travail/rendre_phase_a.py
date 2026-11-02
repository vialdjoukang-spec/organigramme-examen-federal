"""Rend le contenu médical relu séparément ; n’attribue aucun verdict clinique."""
import json
import re
from pathlib import Path
from html import escape

D = Path(__file__).resolve().parent
data = json.loads((D / 'PHASEA_CONTENU.json').read_text())
assert [s['numero'] for s in data['sections']] == list(range(1,14))
assert len(data['quiz']) == 14 and len(data['diagnostics']) == 10
assert [s['id'] for s in data['sources']] == list(range(1,len(data['sources'])+1))
sources = [[f"{s['titre']} ; version : {s['date_publication'] or 'non précisée'} ; passages lus : {s['passages_lus']}", s['url']] for s in data['sources']]
(D.parent / 'evidence/sources.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n')
from format_lecon import Lesson, table, ref, paras

lesson = Lesson(data['titre'])
known = {s['id'] for s in data['sources']}
for section in data['sections']:
    assert set(section['refs']) <= known
    assert len(re.findall(r'\{[^{}]+\}',section['main'])) == 1
    detail = section['detail_html']
    assert not re.search(r'<(?:script|iframe|img)\b',detail,re.I)
    if section['numero'] == 7:
        rows=[]
        for n,dx in enumerate(data['diagnostics'],1):
            assert set(dx['refs']) <= known
            rows.append([f"DX.{n} — {escape(dx['nom'])}"+ref(dx['refs']),escape(dx['niveau'].replace(' ; proposition provisoire','') if (D.parent/'LISTE_DX_CANONIQUE.json').exists() else dx['niveau']),escape(dx['signes']),escape(dx['confirmation']),escape(dx['urgence'])])
        detail+=table(['Hypothèse pédagogique','Niveau diagnostique','Signes et contexte','Confirmation','Priorité et limite'],rows)
        detail+=paras('Sélection adulte non exhaustive, sans classement de fréquence. Liste canonique fixée après audit distinct.' if (D.parent/'LISTE_DX_CANONIQUE.json').exists() else 'Sélection adulte non exhaustive, sans classement de fréquence. Liste provisoire jusqu’au contre-audit de cette Phase A.')
    lesson.add(section['main'],detail,section['refs'])
items=[]
for q in data['quiz']:
    assert set(q['refs']) <= known
    items.append((q['question'],q['reponse']+ref(q['refs'])))
lesson.quiz(items,tuple(sorted({n for q in data['quiz'] for n in q['refs']})))
lesson.write()

if (D.parent / "LISTE_DX_CANONIQUE.json").exists():
    p=D.parent / "LOT_132_Phase_A_V0.html"
    p.write_text(p.read_text().replace("cours en rédaction ; liste différentielle provisoire, audit distinct avant gel. Illustration en préparation séparée.", "Phase A relue et liste différentielle fixée après audit distinct. Illustration en préparation séparée."))
