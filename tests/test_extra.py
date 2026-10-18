# Contrôles complémentaires (5) : touche i, absence d’ouverture au survol, défilement, appui long, toucher court.
# Variables : APP_FILE, CHROME_PATH, SHOTS_DIR. Les contrôles eux-mêmes sont inchangés.
import asyncio, json
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.abspath(os.environ.get('APP_FILE', os.path.join(ROOT, 'app_v2.html')))
SHOTS = os.environ.get('SHOTS_DIR', os.path.join(ROOT, 'qa', 'shots'))
os.makedirs(SHOTS, exist_ok=True)
CHROME = os.environ.get('CHROME_PATH') or None
LAUNCH = dict(args=['--no-sandbox'], **({'executable_path': CHROME} if CHROME else {}))
from playwright.async_api import async_playwright
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(**LAUNCH)
    out={}
    c=await b.new_context(viewport={'width':1366,'height':860}); pg=await c.new_page(); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    await pg.goto('file://'+APP); await pg.wait_for_timeout(2500)
    it=pg.locator('#list .it').first; await it.focus(); await pg.keyboard.press('i'); await pg.wait_for_timeout(300)
    out['i_key_on_ssp_list']=await pg.evaluate("!tip.hidden&&tipPin")
    await pg.keyboard.press('Escape')
    # Le survol ne doit ouvrir aucune infobulle ; un clic explicite l’ouvre.
    await pg.locator('.tab[data-v=not]').click(); await pg.locator('#n-list [data-n]').first.click(); await pg.wait_for_timeout(300)
    await pg.locator('#v-not .nr .tw').nth(2).hover(); await pg.wait_for_timeout(500)
    survol_ne_ouvre_pas=await pg.evaluate("tip.hidden")
    await pg.locator('#v-not .nr .tw').nth(2).click(); await pg.wait_for_timeout(250)
    out['survol_ne_ouvre_pas_clic_ouvre_epingle']=survol_ne_ouvre_pas and await pg.evaluate("!tip.hidden&&tipPin")
    out['tip_scrollable_css']=await pg.evaluate("getComputedStyle(tip).overflowY")
    await c.close()
    c=await b.new_context(**p.devices['Pixel 7']); pg=await c.new_page(); pg.on('pageerror',lambda e:errs.append(str(e)))
    await pg.goto('file://'+APP); await pg.wait_for_timeout(2500)
    await pg.locator('.tab[data-v=not]').tap(); await pg.wait_for_timeout(300)
    it=pg.locator('#n-list [data-n]').first; await it.scroll_into_view_if_needed(); bb=await it.bounding_box()
    cdp=await c.new_cdp_session(pg); x,y=bb['x']+bb['width']/2,bb['y']+bb['height']/2
    await cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':[{'x':x,'y':y}]}); await pg.wait_for_timeout(800)
    out['appui_long_ne_ouvre_pas']=await pg.evaluate("tip.hidden")
    await cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]}); await pg.wait_for_timeout(300)
    await pg.screenshot(path=SHOTS+'/after_mobile_longpress.png')
    await it.tap(); await pg.wait_for_timeout(300)
    out['short_tap_still_selects']=await pg.evaluate("!!document.querySelector('#n-list [data-n].sel')")
    out['errors']=errs
    print(json.dumps(out,indent=1)); await b.close()
asyncio.run(main())
