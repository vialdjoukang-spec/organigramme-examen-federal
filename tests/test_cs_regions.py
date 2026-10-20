# GAMMA · contrôles de la ligne des régions CS (une ligne, symétrie, défilement, couleurs, nom accessible, état non chromatique).
import asyncio, json, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP=os.path.abspath(os.environ.get('APP_FILE',os.path.join(ROOT,'app_v2.html')))
CHROME=os.environ.get('CHROME_PATH') or None
from playwright.async_api import async_playwright
JS="""(()=>{const g=document.getElementById('g-reg'),bs=[...g.querySelectorAll('button[data-r]')],R=b=>b.getBoundingClientRect(),s=f=>new Set(bs.map(f)).size;
const on=bs.filter(b=>b.getAttribute('aria-pressed')==='true');
return {une_ligne:s(b=>Math.round(R(b).top))===1,largeur_egale:s(b=>Math.round(R(b).width))===1,hauteur_egale:s(b=>Math.round(R(b).height))===1,
sans_debordement:document.documentElement.scrollWidth<=innerWidth&&getComputedStyle(g).overflowX==='auto'&&g.tabIndex===0&&!!g.getAttribute('aria-label'),
couleurs_distinctes:s(b=>getComputedStyle(b).borderTopColor)===bs.length,
nom_accessible:bs.every(b=>!b.hasAttribute('aria-label')&&b.textContent.trim().length>2),
selection_non_chromatique:on.length===1&&on[0].dataset.r==='abdomen'&&getComputedStyle(on[0].querySelector('.cs-l'),'::before').content.includes('✓')}})()"""
async def main():
  out={};errs=[]
  async with async_playwright() as p:
    b=await p.chromium.launch(args=['--no-sandbox'],**({'executable_path':CHROME} if CHROME else {}))
    for n,vp in (('ordi',{'width':1280,'height':900}),('mobile',{'width':390,'height':844})):
      pg=await (await b.new_context(viewport=vp)).new_page();pg.on('pageerror',lambda e:errs.append(str(e)))
      await pg.goto('file://'+APP);await pg.wait_for_timeout(1200)
      await pg.click('.tab[data-v=ges]');await pg.wait_for_timeout(300)
      await pg.click('#g-reg [data-r=abdomen]');await pg.wait_for_timeout(300)
      r=await pg.evaluate(JS)
      if n=='ordi': out.update(r)
      else: out['mobile_ligne_symetrique']=r['une_ligne'] and r['largeur_egale'] and r['hauteur_egale'] and r['sans_debordement']
    await b.close()
  out['errors']=errs
  print(json.dumps(out,ensure_ascii=False))
asyncio.run(main())
