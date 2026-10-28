#!/usr/bin/env python3
"""Construit le jeu doré : source.html → arbre rendu (S5) → conversion forme_interactive → tous les écrivains jusqu'au point fixe → cours_dore.html ;
puis les gabarits d'entrée des scriptones qui ne lisent pas un cours : journal_dore.jsonl (journal réel d'un passage de l'orchestre sur le doré)
et brief_dore.md (brief compilé). Le jeu doré doit produire ZÉRO doléance (spécificité) sur les 160 scriptones ; chaque mutant la sienne."""
import sys
from pathlib import Path
D = Path(__file__).resolve().parent
sys.path.insert(0, str(D.parent))
import cerveau, orchestre, reseau

if __name__ == "__main__":
    t = cerveau.corriger((D / "source.html").read_text(encoding="utf-8"), convertir=True)
    (D / "cours_dore.html").write_text(t, encoding="utf-8")
    j = D / "journal_dore.jsonl"; j.unlink(missing_ok=True)
    orchestre.passer(html=t, nom="cours_dore.html", journal=j, historique=[])
    (D / "brief_dore.md").write_text(reseau.module("s17_brief").compiler(t, "cours_dore.html", []), encoding="utf-8")
    Dl, _ = cerveau.analyser(t, "cours_dore.html", ecrire=False)
    print(f"cours_dore.html : {len(t.encode()) // 1000} Ko · {len(Dl)} doléance(s) · journal {sum(1 for _ in j.open())} événements")
    for d in Dl: print(f"- {d['severite']} {d['code']} {d['scriptone']} {d['ancre']} : {d['constat']}")
    sys.exit(1 if Dl else 0)
