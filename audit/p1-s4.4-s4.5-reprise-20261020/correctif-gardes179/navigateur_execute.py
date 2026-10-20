import asyncio,pathlib,json,http.server,threading,functools
from playwright.async_api import async_playwright
T=pathlib.Path('/tmp/p1-179-projection-gardes');R=pathlib.Path('/workspace/organigramme-examen-federal/work/p1/s4.4-s4.5');O=R/'audit/p1-s4.4-s4.5-reprise-20261020/correctif-gardes179'
class H(http.server.SimpleHTTPRequestHandler):
 def __init__(self,*a,**k):super().__init__(*a,directory=str(T),**k)
 def log_message(self,*a):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',8886),H);threading.Thread(target=server.serve_forever,daemon=True).start()
async def main():
 out={'date':'2026-10-20','projection':'2a3d2dc + TIP/lots/deltas corrigés après9fc53c9','url':'http://127.0.0.1:8886/app_v2.html','errors':[],'definitions':{}}
 entries={e['id']:e for e in json.load(open(T/'data/ck/glo.json'))}
 ids=['oat','sopk','iop','hsg','iiu','fiv','pma','menorragies','spm','tdpm','acanthosis','hyperprolactinemie','galactorrhee','infertilite','aos','asrm','cngof','dggg','oeggg','sggg','eshre','icmart','ims','figo','ng88','ng126','hypogonadotrophique','intrauterin','orchite','dysphorique']
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);pg=await b.new_page(viewport={'width':1360,'height':980});pg.on('pageerror',lambda e:out['errors'].append(str(e)));await pg.goto(out['url']);await pg.wait_for_timeout(1600)
  await pg.evaluate("()=>{const e=document.createElement('span');e.id='probe';e.textContent='Définition';e.style.cssText='position:fixed;top:4px;left:4px;z-index:100';document.body.append(e)}")
  for id in ids:
   await pg.evaluate("id=>{hideTip(true);document.querySelector('#probe').dataset.t='glo|'+id}",id);await pg.locator('#probe').click()
   expected=entries[id]['def'][:36]
   try:await pg.wait_for_function("t=>!TIPEL.hidden&&TIPEL.innerText.includes(t)",arg=expected,timeout=3000);out['definitions'][id]=True
   except Exception:out['definitions'][id]=False
  await pg.evaluate("()=>{hideTip(true);document.querySelector('#probe').dataset.t='n|S4.4|c0';showTip(document.querySelector('#probe'),true)}");await pg.wait_for_timeout(300)
  link=pg.locator('#tip [data-t="glo|eshre"]').first;out['sigle_dans_cours_cliquable']=await link.count()>0
  if await link.count():
   await link.click();await pg.wait_for_timeout(200);out['clic_sigle_ouvre_definition']=await pg.evaluate("!TIPEL.hidden&&TIPEL.innerText.includes('société européenne de reproduction humaine')")
  else:out['clic_sigle_ouvre_definition']=False
  await pg.evaluate('hideTip(true)');await pg.hover('#probe');await pg.wait_for_timeout(600);out['absence_ouverture_survol']=await pg.evaluate('TIPEL.hidden')
  await pg.set_viewport_size({'width':390,'height':844});await pg.evaluate("()=>{document.querySelector('#probe').dataset.t='glo|tdpm';showTip(document.querySelector('#probe'),true)}");await pg.wait_for_timeout(150);out['definition_mobile']=await pg.evaluate("!TIPEL.hidden&&TIPEL.innerText.includes('forme sévère de symptômes prémenstruels')")
  await b.close()
 out['reussi']=all(out['definitions'].values()) and all(out[k] for k in ['sigle_dans_cours_cliquable','clic_sigle_ouvre_definition','absence_ouverture_survol','definition_mobile']) and not out['errors'];(O/'navigateur.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False,indent=2))
try:asyncio.run(main())
finally:server.shutdown()
