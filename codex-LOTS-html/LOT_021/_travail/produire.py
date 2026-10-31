from format_lecon import Lesson,paras,table,steps
from diagnostics import DIAGNOSTICS
def produire(n,parts,quiz,refs):
 assert len(parts)==13
 l=Lesson(DIAGNOSTICS[n-1][0],n)
 for main,detail in parts:l.add(main,detail,refs)
 l.quiz(quiz,refs);l.write()
