from pathlib import Path
import json,re,html,hashlib,subprocess,sys,os
B=Path(__file__).resolve().parent
D=B/'DX.10'
OUTILS=B.parents[3]/'_outils'
FINAL='Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ?'
class Cours:
 def __init__(self):
  self.packet=json.loads((D/'paquet.json').read_text());self.refs={q['id']:q for q in self.packet['passages']};self.alias={q['id'].removeprefix('dx10-'):q['id']for q in self.packet['passages']};self.parts={i:[]for i in range(1,15)};self.n={i:0 for i in self.parts};self.w={i:0 for i in self.parts};self.t={i:0 for i in self.parts}
  for k,name in [('sp','spiricort'),('im','imurek'),('oc','octagam')]:
   for label,sec in [('ind',3),('dose',4),('ci',5),('warn',6),('inter',7),('gross',8),('drive',9),('meca',12),('pk',13),('num',16),('date',19)]:self.alias[k+'-'+label]=f'aips-dx10-{name}-{sec}'
 def cite(self,refs):
  ids=[self.alias.get(x,x)for x in refs.split('+')];assert all(x in self.refs for x in ids),ids;return ''.join('<sup class="r"><a href="#sb-'+q+'">'+q+'</a></sup>'for q in ids)
 def p(self,n,text,refs):
  self.n[n]+=1;self.parts[n].append('<div class="p" id="dx10-p'+str(n)+'-f'+str(self.n[n])+'">'+html.escape(text)+self.cite(refs)+'</div>\n')
 def block(self,n,title,rows):
  self.parts[n].append('<h4><em>'+html.escape(title)+'</em></h4>\n')
  for t,r in rows:self.p(n,t,r)
 def fen(self,n,title,rows):
  self.w[n]+=1;i=f'dx10-p{n}-w{self.w[n]}';self.parts[n].append('<h4><button class="w" popovertarget="'+i+'">'+html.escape(title)+'</button></h4>\n<div class="fenetre" id="'+i+'" popover><h4>'+html.escape(title)+'</h4>\n')
  for t,r in rows:self.p(n,t,r)
  self.parts[n].append('</div>\n')
 def tab(self,n,title,heads,rows):
  self.t[n]+=1;i=self.t[n];self.parts[n].append('<h4><em>'+html.escape(title)+'</em></h4>\n<div class="t" style="overflow-x:auto"><table><thead><tr>'+''.join('<th>'+html.escape(t)+'</th>'for t in heads)+'</tr></thead><tbody>\n')
  for ri,row in enumerate(rows,1):self.parts[n].append('<tr>'+''.join('<td id="dx10-p'+str(n)+'-t'+str(i)+'-r'+str(ri)+'-c'+str(ci)+'">'+html.escape(t)+self.cite(r)+'</td>'for ci,(t,r)in enumerate(row,1))+'</tr>\n')
  self.parts[n].append('</tbody></table></div>\n')
 def save(self):
  (D/'fragments').mkdir(exist_ok=True)
  for n,parts in self.parts.items():
   s=''.join(parts)
   if n==14:s+='<h4 id="dx10-p14-question-finale">'+FINAL+self.cite('prompt-question-finale')+'</h4>\n'
   (D/'fragments'/f'p{n:02d}.html').write_text(s)
   self.packet['points'][str(n)]={'citations_effectives':list(dict.fromkeys(re.findall(r'href="#sb-([^\"]+)"',s))),'fenetres':self.w[n],'tableaux':self.t[n]}
  (D/'paquet.json').write_text(json.dumps(self.packet,ensure_ascii=False,indent=2)+'\n')
 def assembler(self):
  self.save();f=D/'LOT_083_Phase_B_V0_DX.10.html';env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
  subprocess.run([sys.executable,str(OUTILS/'assembler.py'),'--fragments',str(D/'fragments'),'--paquet',str(D/'paquet.json'),'--contrat',str(D/'contrat.json'),'--titre','DX.10 — Dermatomyosite','--sortie',str(f)],check=True,env=env)
  h=f.read_text();h=re.sub(r'(?<=>)(?=</?(?:section|div|p|table|thead|tbody|tr|td|th|li|ol|h[2-4])\b)','\n',h);f.write_text(h);raw=f.read_bytes();sha=hashlib.sha256(raw).hexdigest()
  (D/'MANIFESTE.json').write_text(json.dumps({f.name:{'octets':len(raw),'sha256':sha}},ensure_ascii=False,indent=2)+'\n')
  r=subprocess.run([sys.executable,str(OUTILS/'controle3.py'),str(f),'--paquet',str(D/'paquet.json'),'--ex','12'],capture_output=True,text=True,env=env);(D/'controle.json').write_text(r.stdout);print(r.stdout,r.stderr);print('SHA',sha,'OCTETS',len(raw))
