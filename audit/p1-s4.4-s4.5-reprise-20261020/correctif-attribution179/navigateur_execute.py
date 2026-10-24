import asyncio,pathlib,json,http.server,threading
from playwright.async_api import async_playwright
R=pathlib.Path('/workspace/organigramme-examen-federal/work/p1/s4.4-s4.5');T=pathlib.Path('/tmp/p1-179-projection-attribution');O=R/'audit/p1-s4.4-s4.5-reprise-20261020/correctif-attribution179'
class H(http.server.SimpleHTTPRequestHandler):
 def __init__(self,*a,**k):super().__init__(*a,directory=str(T),**k)
 def log_message(self,*a):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',8887),H);threading.Thread(target=server.serve_forever,daemon=True).start()
async def main():
 out={'date':'2026-10-20','projection':'b56030c + correctif ciblé après db8084ee','url':'http://127.0.0.1:8887/app_v2.html','limite':'Parcours au clic via span data-t injecté, Chromium local ; requêtes externes des liens sources interceptées et servies localement pour vérifier destination/ouverture, sans prétendre lire le serveur médical par ce test.','errors':[],'sources_cliquees':{},'requêtes_externes_interceptees':[]};data=json.load(open(T/'data/tip/S4.5.json'));sources={s['id']:s for s in data['v']['S']}
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);ctx=await browser.new_context(viewport={'width':1360,'height':980})
  async def handler(route):
   u=route.request.url
   if u.startswith('http://127.0.0.1:8887/'):await route.continue_()
   else:out['requêtes_externes_interceptees'].append(u);await route.fulfill(status=200,content_type='text/html',body='<p>Vérification locale du lien de source.</p>')
  await ctx.route('**/*',handler);pg=await ctx.new_page();pg.on('pageerror',lambda e:out['errors'].append(str(e)));await pg.goto(out['url']);await pg.wait_for_timeout(1200)
  await pg.evaluate("()=>{const e=document.createElement('span');e.id='probe';e.textContent='Ouvrir';e.style.cssText='position:fixed;top:4px;left:4px;z-index:100';document.body.append(e)}")
  async def open_part(i):
   await pg.evaluate("i=>{hideTip(true);document.querySelector('#probe').dataset.t='n|S4.5|c'+i}",i);await pg.locator('#probe').click();await pg.wait_for_function('!TIPEL.hidden');await pg.wait_for_timeout(150)
  await open_part(5);out['partie6_texte_corrige']=await pg.evaluate("TIPEL.innerText.includes('hymen bombé, parfois bleuté, avec douleurs cycliques sans règles')")
  out['partie6_references_13_14_15']=all([await pg.locator('#tip .s a').filter(has_text=sources[n]['t']).count()==1 for n in [13,14,15]])
  for n in [13,14,15]:
   link=pg.locator('#tip .s a').filter(has_text=sources[n]['t']);target=await link.get_attribute('href')
   async with pg.expect_popup() as pending:await link.click()
   popup=await pending.value;await popup.wait_for_load_state('domcontentloaded');out['sources_cliquees'][str(n)]={'href':target,'url_ouverte':popup.url,'reussi':target==sources[n]['u'] and popup.url==target};await popup.close()
  link=pg.locator('#tip [data-t="glo|hematocolpos"]').first;out['hematocolpos_cliquable_depuis_partie6']=await link.count()>0
  await link.click();await pg.wait_for_function("!TIPEL.hidden&&TIPEL.innerText.includes('accumulation de sang menstruel dans le vagin')");out['glo_definition_et_signe']=await pg.evaluate("TIPEL.innerText.includes('hymen bombé')")
  glolinks=await pg.locator('#tip .ck-src a').evaluate_all('(a)=>a.map(e=>e.href)');out['glo_sources_exactes']=set(glolinks)=={sources[13]['u'],sources[14]['u']};out['glo_ne_cite_plus_SFE']=all('sfendocrino' not in u for u in glolinks)
  await open_part(6);out['partie7_synthese_prudente']=await pg.evaluate("TIPEL.innerText.includes('évoquer un hématocolpos sur hymen imperforé')");out['partie7_references_13_14']=all([await pg.locator('#tip .s a').filter(has_text=sources[n]['t']).count()==1 for n in [13,14]])
  await ctx.close();await browser.close()
 checks=['partie6_texte_corrige','partie6_references_13_14_15','hematocolpos_cliquable_depuis_partie6','glo_definition_et_signe','glo_sources_exactes','glo_ne_cite_plus_SFE','partie7_synthese_prudente','partie7_references_13_14'];out['reussi']=all(out[k] for k in checks) and all(x['reussi'] for x in out['sources_cliquees'].values()) and not out['errors'];(O/'navigateur.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False,indent=2));assert out['reussi']
try:asyncio.run(main())
finally:server.shutdown()
