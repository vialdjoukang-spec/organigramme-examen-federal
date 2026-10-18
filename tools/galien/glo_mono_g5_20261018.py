#!/usr/bin/env python3
"""Trois termes des monographies G5, sans source ni validation inventée."""
import json
from pathlib import Path
ROWS=[{'id': 'ppr', 'type': 'abreviation', 'label': 'PPR', 'alias': ['pseudopolyarthrite rhizomélique'], 'def': 'Cette maladie inflammatoire provoque surtout des douleurs et une raideur des épaules et des hanches.', 'statut': 'À vérifier', 'valide_par_vial': False}, {'id': 'hyperventiler', 'type': 'terme', 'label': 'Hyperventiler', 'def': 'Ce verbe signifie ventiler au-delà des besoins de l’organisme, ce qui tend à abaisser le dioxyde de carbone dans le sang.', 'statut': 'À vérifier', 'valide_par_vial': False}, {'id': 'triade-virchow', 'type': 'terme', 'label': 'Triade de Virchow', 'def': 'Ces trois mécanismes favorisent une thrombose : ralentissement du sang, lésion de la paroi d’un vaisseau et tendance accrue à coaguler.', 'statut': 'À vérifier', 'valide_par_vial': False}]
p=Path('data/ck/glo.json');g=json.loads(p.read_text());ids={x['id'] for x in g}
g.extend(x for x in ROWS if x['id'] not in ids)
p.write_text(json.dumps(g,ensure_ascii=False,indent=1)+'\n')
