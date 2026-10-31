from format_lecon import Lesson,paras,table,steps
from diagnostics import DIAGNOSTICS
def produire(n,parts,quiz,refs,medicaments=None):
 assert len(parts)==13
 l=Lesson(DIAGNOSTICS[n-1][0],n)
 if medicaments:
  liens=medicaments(l)
  parts=[(a,b.replace('@@MEDICAMENTS@@',liens)) for a,b in parts]
 for main,detail in parts:l.add(main,detail,refs)
 l.quiz(quiz,refs);l.write()
