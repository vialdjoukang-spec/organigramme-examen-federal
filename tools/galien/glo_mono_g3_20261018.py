#!/usr/bin/env python3
"""Trois termes des nouvelles monographies, définitions provisoires explicites."""
import json
from pathlib import Path
ROWS=[{'id': 'hydroxybutyrate', 'type': 'terme', 'label': 'Hydroxybutyrate', 'alias': ['β-hydroxybutyrate', 'bêta-hydroxybutyrate'], 'def': 'Cette substance acide est produite par le foie à partir des graisses ; sa concentration peut augmenter quand l’insuline manque.', 'statut': 'À vérifier', 'valide_par_vial': False}, {'id': 'hyperproteique', 'type': 'terme', 'label': 'Hyperprotéique', 'def': 'Ce mot qualifie une alimentation ou un mélange riche en protéines.', 'statut': 'À vérifier', 'valide_par_vial': False}, {'id': 'kaliurie', 'type': 'terme', 'label': 'Kaliurie', 'def': 'Ce terme désigne la quantité de potassium éliminée dans les urines.', 'statut': 'À vérifier', 'valide_par_vial': False}]
p=Path('data/ck/glo.json');g=json.loads(p.read_text());ids={x['id'] for x in g}
g.extend(x for x in ROWS if x['id'] not in ids)
for x in g:
 if x['id']=='corps-cetoniques':
  x['def']=x['def'].replace('des acides que','des substances que');x['statut']='À vérifier'
p.write_text(json.dumps(g,ensure_ascii=False,indent=1)+'\n')
