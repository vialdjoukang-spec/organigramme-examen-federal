"""Rédaction originale DX6 ; relecture interne et sources tracées séparément."""
from pathlib import Path
import json,re,subprocess
D=Path(__file__).resolve().parent;B=D.parent;R=B.parent
BASE=json.loads((D/'BASELINE.json').read_text())['commit']
def run(n,content,answers):
 name=f'codex-LOTS-html/LOT_{n:03}/LOT_{n:03}_Phase_B_V0_DX.6.html'
 text=subprocess.check_output(['git','show',BASE+':'+name],cwd=R).decode()
 if n==18:
  phrase='Une occlusion veineuse ne se traite pas comme une occlusion artérielle.'
  assert phrase in text
  text=text.replace(phrase,f'<button type="button" class="terme" popovertarget="dx6-detail13">{phrase}</button>',1)
  win='<div id="dx6-detail13" popover class="fenetre"><div class="barre"><span>Points clés raisonnés</span><button type="button" popovertarget="dx6-detail13" popovertargetaction="hide" aria-label="Fermer">✕</button></div><div class="corps"></div></div>'
  text=text.replace('<div id="dx6-quiz"',win+'\n<div id="dx6-quiz"',1)
  text=text.replace('</style>','\n.illustration h3,.illustration h4,.illustration figcaption,.illustration .definition{color:#142633}.illustration a{color:#075a84}.illustration .definition{margin:auto;inset:10vh auto auto 5vw}.illustration .scene{scroll-margin-top:80px}\n</style>',1)
 for k,body in content.items():
  i=text.index('<div class="corps">',text.index(f'<div id="dx6-detail{k}"'))+len('<div class="corps">')
  refs=([14,35,36] if k!=11 else [14,25,36]) if n==18 else [2,27,28]
  cite='<sup class="s">'+','.join(f'<a href="#s{x}">{x}</a>' for x in refs)+'</sup>'
  text=text[:i]+f'<!-- RENFORCEMENT_SOLO_DX6_20261101_P{k} -->'+body+cite+'\n'+text[i:]
 start=text.index('<div id="'+('dx6-quiz' if n==18 else 'dx6-detail14')+'"');end=text.index('<section class="ilot c sources">',start);it=iter(answers)
 sub,count=re.subn(r'(<details class="quiz">.*?<summary>.*?</summary>)(.*?)(</details>)',lambda m:m[1]+m[2]+'<p><strong>Raisonnement :</strong> '+next(it)+'</p>'+m[3],text[start:end],flags=re.S);assert count==14
 text=text[:start]+sub+text[end:]
 sources=[(35,'HUG — Occlusion veineuse rétinienne : traitements','https://www.hug.ch/ophtalmologie/occlusion-veineuse-retinienne-traitements'),(36,'Royal College of Ophthalmologists — Retinal vein occlusion guideline, résumé exécutif2022','https://www.rcophth.ac.uk/wp-content/uploads/2026/06/Retinal-vein-occlusion-guideline-exec-summary.pdf')] if n==18 else [(28,'CHUV — La craniosténose, page française','https://www.chuv.ch/fr/neurochirurgie/nch-home/patients-et-familles/maladies-traitees/la-craniostenose')]
 i=text.index('</ol></section>',text.index('<section class="ilot c sources">'));text=text[:i]+''.join(f'<li id="s{x}" value="{x}">{title}. <a href="{url}">Source</a>. Consulté le 01.11.2026.</li>\n' for x,title,url in sources)+text[i:]
 assert '\u00a0' not in text and '\u202f' not in text
 (R/name).write_text(text)
from contenu import G,H,GA,HA
if __name__=='__main__':run(18,G,GA);run(29,H,HA)
