from format_lecon import Lesson,paras,table,steps
from diagnostics import DIAGNOSTICS
from medicaments import window
def produire(n,parts,quiz,refs,med=None):
 assert len(parts)==13
 l=Lesson(DIAGNOSTICS[n-1][0],n)
 drug=window(l,med) if med else ''
 for i,(main,detail) in enumerate(parts,1):
  if i==11 and drug:detail+=paras(drug)
  l.add(main,detail,refs)
 l.quiz(quiz,refs);l.write()
