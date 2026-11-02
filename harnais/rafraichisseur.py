#!/usr/bin/env python3
"""RAFRAÎCHISSEUR DE MÉMOIRE : un seul appel qui emboîte dans l'agent tout le Harnais utile (prompt du projet, exigences du Prompt ULTIME,
leçons du rôle, skills, outils gratuits, règles de territoire). Coût de départ minimal, démarrage rapide.
  python3 harnais/rafraichisseur.py <redacteur|phase-a|opus> <LOT> [territoire 1|2|3]"""
import subprocess, sys
from pathlib import Path
R = Path(__file__).resolve().parent.parent; role, lot = sys.argv[1], sys.argv[2]; ter = sys.argv[3] if len(sys.argv) > 3 else ""
run = lambda *c: subprocess.run([sys.executable, *c], capture_output=True, text=True, cwd=R).stdout.strip()
print("# RAFRAÎCHISSEUR —", role, "LOT_" + lot, ("territoire B" + ter) if ter else "")
print("\n## 1. Projet\n" + run("harnais/prompt_projet.py"))
print("\n## 2. Exigences du Prompt ULTIME\n" + run("harnais/prompt_expert.py", "phase-a" if role == "phase-a" else "redacteur"))
lec = {"redacteur": "redacteur", "phase-a": "redacteur-phase-a", "opus": "auditeur-medical"}[role]
print("\n## 3. Leçons du rôle\n" + (R / f"harnais/LECONS/{lec}.md").read_text(encoding="utf-8"))
sk = ["harnais-lot", "sources-pubmed"] + (["controle-medical"] if role == "opus" else [])
for s in sk: print(f"\n## Skill {s}\n" + (R / f".claude/skills/{s}/SKILL.md").read_text(encoding="utf-8").split("---", 2)[2].strip())
print("\n## 3 bis. GABARIT DE FORME (obligatoire)\n" + (R / "harnais/GABARIT_FORME.md").read_text(encoding="utf-8"))
print("\n## 3 ter. GRILLE À 14 POINTS (Vial, valeur de vérité 1 de l'audit médical)\n" + (R / "harnais/GRILLE_14_POINTS.md").read_text(encoding="utf-8"))
print("\n## 4. Outils gratuits\n- AIPS : python3 harnais/aips_texte.py <n° Swissmedic> --section <mot> | --nom <marque>\n- PubMed : python3 harnais/pubmed.py chercher \"<q>\" 8 | verifier <PMID> ; MCP mcp__PubMed__* ; recherche web (WebSearch/WebFetch) ; sources : harnais/SOURCES_AUTORISEES.md\n- Contrôles : harnais/controle_medical.py <f> · controle_sources.py <f> · controle_langue.py <f> · checkpoint.py\n- Rappel mémoire G : onglet ajouté par le checkpoint (ne pas le coder à la main)")
if role == "opus":
    print(f"\n## 5. TERRITOIRE B{ter} (strict)\n- Tu travailles UNIQUEMENT dans .cache/travail/LOT_{lot}/B{ter}/ : fichiers de entree/ → corrigés en place → sortie/. Tu n'écris ni ne modifies aucun autre fichier du LOT, ni aucun autre territoire, ni le harnais.\n- Avant : territoire.py garde {lot} {ter} <fichier> ; après : territoire.py controle {lot} {ter} <fichier> doit afficher OK (sinon sortie refusée).\n- Ton rapport : .cache/travail/LOT_{lot}/audits/OPUS_<fichier>.md (seul fichier hors territoire autorisé).\n- Audit-correctif : lis le fichier point par point, vérifie chaque dose (AIPS), chaque chiffre [Sn] (source ouverte), chaque grave/🚩, la cohérence clinique, la langue ; corrige TOUT dans le fichier, sans perte d'information ; relance le checkpoint --sortie.")
