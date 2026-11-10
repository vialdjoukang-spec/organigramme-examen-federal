import json,html,subprocess,sys,hashlib
from pathlib import Path
B=Path(__file__).parent
OUTILS=B.parents[3]/'_outils'
def main():
 data=json.loads((B/'contenu.json').read_text());packet=json.loads((B/'paquet.json').read_text());refs={x['id']for x in packet['passages']};aliases=data['references']
 def cite(code):
  ids=[aliases.get(x,x)for x in code.split('+')];assert all(x in refs for x in ids),ids
  return ''.join('<sup class="r"><a href="#sb-'+x+'">'+x+'</a></sup>'for x in ids)
 for n in range(1,15):
  x=data['points'][str(n)];parts=[];counter=0
  def fact(item):
   nonlocal counter
   counter+=1
   return '<div class="p" id="dx1-p'+str(n)+'-fait'+str(counter)+'">'+html.escape(item[1])+cite(item[0])+'</div>\n'
  for title,items in x.get('blocs',[]):
   if title:parts.append('<h4><em>'+html.escape(title)+'</em></h4>\n')
   parts.extend(fact(v)for v in items)
  for title,cols,rows in x.get('tableaux',[]):
   parts.append('<h4><em>'+html.escape(title)+'</em></h4>\n<div class="t" style="overflow-x:auto"><table><thead><tr>'+''.join('<th>'+html.escape(c)+'</th>'for c in cols)+'</tr></thead><tbody>\n')
   for row in rows:parts.append('<tr>'+''.join('<td>'+html.escape(v[1])+cite(v[0])+'</td>'for v in row)+'</tr>\n')
   parts.append('</tbody></table></div>\n')
  for j,(title,items)in enumerate(x.get('fenetres',[]),1):
   ident=f'dx1-p{n}-fen{j}';parts.append('<h4><button class="w" popovertarget="'+ident+'">'+html.escape(title)+'</button></h4>\n<div id="'+ident+'" popover class="fenetre"><h4>'+html.escape(title)+'</h4>\n');parts.extend(fact(v)for v in items);parts.append('</div>\n')
  if n==14:parts.append('<h4>Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ?'+cite('prompt-question-finale')+'</h4>\n')
  (B/'fragments'/f'p{n:02d}.html').write_text(''.join(parts))
 target=B/'LOT_081_Phase_B_V0_DX.1.html'
 subprocess.run([sys.executable,str(OUTILS/'assembler.py'),'--fragments',str(B/'fragments'),'--paquet',str(B/'paquet.json'),'--contrat',str(B/'contrat.json'),'--titre','DX.1 — Lombalgie commune non spécifique','--sortie',str(target)],check=True)
 target.write_text(target.read_text().replace('</li>','</li>\n'));raw=target.read_bytes();(B/'MANIFESTE.json').write_text(json.dumps({target.name:{'octets':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}},indent=2)+'\n')
 r=subprocess.run([sys.executable,str(OUTILS/'controle3.py'),str(target),'--paquet',str(B/'paquet.json'),'--ex','12'],capture_output=True,text=True);(B/'controle.json').write_text(r.stdout);print(r.stdout)
if __name__=='__main__':main()
