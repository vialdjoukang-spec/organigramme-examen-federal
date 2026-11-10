from pathlib import Path
import json,html,re,sys,subprocess,hashlib,os,collections
B=Path(__file__).parent;ROOT=B.parents[3];os.environ['PYTHONDONTWRITEBYTECODE']='1'
def render(n):
 d=B/f'DX.{n}';a=json.loads((d/'contenu.json').read_text());pack=json.loads((d/'paquet.json').read_text());refs={p['id']:p for p in pack['passages']};mapping=a['references'];used={}
 def cite(c):
  ids=[mapping.get(x,x) for x in c.split('+')];assert all(i in refs for i in ids),ids;used.setdefault(str(k),[]).extend(ids);return ''.join('<sup class="r"><a href="#sb-'+i+'">'+str(list(refs).index(i)+1)+'</a></sup>' for i in ids)
 def para(item):
  c,t=item;return '<div class="p">'+html.escape(t)+cite(c)+'</div>\n'
 for k in range(1,15):
  s=a['points'][str(k)];out=[]
  for title,items in s.get('blocs',[]):
   if title:out.append('<h4>'+html.escape(title)+'</h4>')
   out.extend(para(x) for x in items)
  for title,heads,rows in s.get('tableaux',[]):
   out.append('<h4>'+html.escape(title)+'</h4><div class="t" style="overflow-x:auto"><table><thead><tr>'+''.join('<th>'+html.escape(x)+'</th>' for x in heads)+'</tr></thead><tbody>')
   for row in rows:out.append('<tr>'+''.join('<td>'+para(x)+'</td>' for x in row)+'</tr>')
   out.append('</tbody></table></div>')
  for j,(title,items) in enumerate(s.get('fenetres',[]),1):
   ident=f'dx{n}-p{k}-f{j}';out.append('<h4><button class="w" popovertarget="'+ident+'">'+html.escape(title)+'</button></h4><div class="fenetre" popover id="'+ident+'"><h4>'+html.escape(title)+'</h4>');out.extend(para(x) for x in items);out.append('</div>')
  (d/'fragments'/f'p{k:02}.html').write_text('\n'.join(out)+'\n')
 pack['points']={k:list(dict.fromkeys(v)) for k,v in used.items()};(d/'paquet.json').write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n');t=d/f'LOT_083_Phase_B_V0_DX.{n}.html'
 subprocess.run([sys.executable,str(ROOT.parent/'outils/assembler.py'),'--fragments',str(d/'fragments'),'--paquet',str(d/'paquet.json'),'--contrat',str(d/'contrat.json'),'--titre',f'DX.{n} — '+a['entite'],'--sortie',str(t)],check=True)
 s=t.read_text();q='Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ?';assert q not in s;i=s.rfind('</section>');s=s[:i]+'<p class="p">'+q+'</p>'+s[i:];s=re.sub(r'>\s+<','><',s);s=re.sub(r'(</(?:div|p|td|th|tr|table|thead|tbody|section|h[1-6]|li|ol|main)>|<(?:html|head|body|main)[^>]*>)',r'\1\n',s);s=s.replace("<!-- FIN_FICHIER", "\n<!-- FIN_FICHIER");t.write_text(s)
 r=subprocess.run([sys.executable,str(ROOT.parent/'outils/controle3.py'),str(t),'--paquet',str(d/'paquet.json'),'--ex','20'],capture_output=True,text=True);(d/'CONTROLE3.json').write_text(r.stdout)
 ids=re.findall(r'\bid="([^"]+)"',s);targets=re.findall(r'popovertarget="([^"]+)"',s);m={'fichier':str(t),'octets':t.stat().st_size,'sha256':hashlib.sha256(t.read_bytes()).hexdigest(),'max_ligne':max(map(len,s.splitlines())),'ids_dupliques':[i for i,c in collections.Counter(ids).items() if c>1],'cibles_absentes':[i for i in targets if i not in ids],'question_finale':s.count(q),'statut':'Rédaction privée ; audit indépendant requis'};(d/'MANIFESTE.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print(json.dumps(m,ensure_ascii=False));print(r.stdout)
if __name__=='__main__':render(int(sys.argv[1]))
