#!/usr/bin/env python3
"""Quatre nouveaux termes des monographies main, sans admission en baseline."""
import json
from pathlib import Path
ROWS=[{'id': 'hypertrophie', 'type': 'terme', 'label': 'Hypertrophie', 'alias': ['hypertrophient'], 'def': 'Ce terme désigne une augmentation du volume d’un tissu ou d’un organe.', 'statut': 'sourcé', 'valide_par_vial': False, 'src': [{'id': 'R-LAR-HYPERTROPHIE', 'loc': 'Définition, première phrase', 'lu_le': '2026-10-18'}]}, {'id': 'serite', 'type': 'terme', 'label': 'Sérite', 'alias': ['sérites'], 'def': 'Ce terme désigne une inflammation d’une membrane qui tapisse une cavité du corps.', 'statut': 'À vérifier', 'valide_par_vial': False}, {'id': 'syndrome-lofgren', 'type': 'terme', 'label': 'Syndrome de Löfgren', 'alias': [], 'def': 'Ce syndrome est une forme aiguë de sarcoïdose qui associe typiquement des ganglions augmentés de volume des deux côtés du thorax, un érythème noueux et une inflammation articulaire de la cheville.', 'statut': 'sourcé', 'valide_par_vial': False, 'src': [{'id': 'R-FMS-LOFGREN-2024', 'loc': 'p. 160, PDF p. 42, Vintage Corner : triade typique', 'lu_le': '2026-10-18'}]}]
p=Path('data/ck/glo.json');g=json.loads(p.read_text())
for x in g:
 if x['id']=='hypoesthesie': x['alias']=list(dict.fromkeys(x.get('alias',[])+['hypo-esthésie']))
ids={x['id'] for x in g}
for x in ROWS:
 if x['id'] not in ids:g.append(x)
p.write_text(json.dumps(g,ensure_ascii=False,indent=1)+'\n')

REFS=[{'id': 'R-LAR-HYPERTROPHIE', 'titre': 'Hypertrophie — définition du Larousse Médical', 'org': 'Larousse', 'pays': 'FR', 'type': 'glossaire', 'url': 'https://www.larousse.fr/encyclopedie/medical/hypertrophie/13716'}, {'id': 'R-FMS-LOFGREN-2024', 'titre': 'Weekly Briefing — Syndrome de Löfgren : triade typique. Forum Médical Suisse 2024;24(12):160–161', 'org': 'Forum Médical Suisse / EMH', 'pays': 'CH', 'type': 'article', 'url': 'https://fmh.ch/files/pdf30/saez-bms-2024-12-fr.pdf', 'annee': 2024}]
p=Path('data/ck/src.json');s=json.loads(p.read_text());ids={x['id'] for x in s}
s.extend(x for x in REFS if x['id'] not in ids)
p.write_text(json.dumps(s,ensure_ascii=False,indent=1)+'\n')
