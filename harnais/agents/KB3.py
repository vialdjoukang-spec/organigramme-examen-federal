#!/usr/bin/env python3
"""Clone 3 du CONTRACTEUR DE TEXTE · CONSERVATEUR DE NOTIONS : dernier secteur de l'auditeur B3. Usage : python3 harnais/agents/KB3.py contracter|verifier|etat <fichier>"""
import sys
sys.path.insert(0, "/home/user/organigramme-examen-federal/harnais/contracteur"); sys.path.insert(0, "/home/user/organigramme-examen-federal/harnais/grille14")
import contracteur; sys.exit(contracteur.main("KB3", sys.argv[1], sys.argv[2:]))
