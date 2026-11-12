#!/usr/bin/env python3
"""VERROU_MEDINA — crochet PreToolUse (ordre de Vial du 12.11.2026 : « ce projet ne nous sert pas »).
Refuse tout appel d'outil (agent principal et sous-agents) dont l'entrée vise /home/user/Medina.
Le seul actif utile de MEDINA, le corpus AIPS refdata, est copié dans ~/.cache/medina_aips (aips_fiche.py trouve).
Installation : ~/.claude/settings.json → hooks.PreToolUse, commande « python3 <ce fichier> ». Code 2 = refus motivé.
"""
import sys, json, re
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
s = json.dumps(d.get('tool_input', {}), ensure_ascii=False)
if re.search(r'/home/user/Medina(?![A-Za-z0-9_-])|(?<![\w/-])~?/?Medina/', s):
    print('VERROU MEDINA : projet fermé par Vial (12.11.2026). Corpus AIPS : python3 Claude/_harnais/aips_fiche.py trouve <nom|n°>.', file=sys.stderr)
    sys.exit(2)
sys.exit(0)
