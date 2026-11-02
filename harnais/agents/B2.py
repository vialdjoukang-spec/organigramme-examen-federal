#!/usr/bin/env python3
"""Agent B2 : script « Grille des 14 points », lecture seule. Usage : python3 harnais/agents/B2.py memoire|controle <fichier>|fin <fichier>|lecon "<texte>"|etat"""
import sys; sys.argv.insert(1, "B2")
sys.path.insert(0, "/home/user/organigramme-examen-federal/harnais/grille14")
import grille_agent; sys.exit(grille_agent.main())
