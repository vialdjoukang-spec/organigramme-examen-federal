"""Preuve complémentaire de conservation du HTML et des renvois, sans éditer les tests."""
import asyncio, functools, http.server, json, os, pathlib, threading
from playwright.async_api import async_playwright
ROOT=pathlib.Path(os.environ['PHASES_PROJECTION'])
OUT=pathlib.Path(__file__).parent
class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(ROOT)))
threading.Thread(target=server.serve_forever,daemon=True).start()
async def main():
    async with async_playwright() as p:
        browser=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        page=await browser.new_page()
        await page.goto('http://127.0.0.1:'+str(server.server_port)+'/app_v2.html')
        await page.wait_for_function('typeof TIP!=="undefined" && typeof exFmt==="function"')
        result=await page.evaluate('''before=>{
          const html=exFmt(TIP['S4.3'].c[5]), el=document.createElement('div'); el.innerHTML=html;
          const genital=el.querySelector('[data-reg="tr-genital"]');
          const autres=el.querySelector('[data-reg="autres"]');
          return {html_strictement_identique_avant:exFmt(before)===html,
            phases:[...el.querySelectorAll('.ex-phase')].map(e=>e.dataset.ordre),
            renvois:[...el.querySelectorAll('.ex-chip')].map(e=>e.dataset.gx),
            preparation_avant_inspection:genital.children[1].tagName==='UL'
              &&genital.children[1].textContent.includes('consentement')
              &&genital.children[2].classList.contains('ex-phase')
              &&genital.children[2].dataset.ordre==='1',
            interpretation_hors_phase:autres.querySelectorAll('.ex-phase').length===0
              &&autres.querySelector('b').textContent==='Interprétation clinique'};
        }''',(OUT/'avant-partie6.txt').read_text().rstrip('\n'))
        assert result['html_strictement_identique_avant']
        assert result['preparation_avant_inspection'] and result['interpretation_hors_phase']
        assert result['phases']==['M','1','2','1','3','2','1','2']
        assert len(result['renvois'])==19 and all(result['renvois'])
        (OUT/'conservation-ui.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps(result,ensure_ascii=False))
        await browser.close()
asyncio.run(main())
server.shutdown()
