"""Click opens G1 and its definitions; moving across words must open nothing."""
import asyncio
import os
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]

async def check(page, touch=False):
    await page.goto((ROOT / 'app_v2.html').as_uri())
    await page.evaluate("""() => {
      const f=document.createElement('div');f.id='prototype-test';
      f.style.cssText='position:fixed;top:10px;left:10px;z-index:99999;background:white';
      f.innerHTML='<button class="tw" data-t="s|G1">SSP G1</button><button class="tw" data-t="n|G1|d0">Hyperhidrose</button><button class="tw" data-t="n|G1|c0">Cours G1</button><button class="tw" data-t="n|G1|c5">Examen G1</button>';
      document.body.appendChild(f);
    }""")
    async def six():
        await page.wait_for_function("""() => !TIPEL.hidden &&
          [...TIPEL.querySelectorAll('.ck-b b')].filter(x=>/^[1-6]\\./.test(x.textContent)).length===6""")
        text = await page.locator('#tip .ck-b').inner_text()
        assert text.index('Examen de référence diagnostique') < text.index('À faire en premier')
        assert text.index('A- But') < text.index('B- Moyens') < text.index('Mesures générales')
        return text

    dd=page.locator('#prototype-test [data-t="n|G1|d0"]')
    if not touch:
        await dd.hover()
        await page.wait_for_timeout(650)
        assert await page.locator('#tip').is_hidden(), 'Hover must not open a monography'
        await page.mouse.move(1,1)
    await dd.tap() if touch else await dd.click()
    clicked=await six()
    await page.wait_for_function("document.querySelector('#tip .ck-b .glo')")
    term=page.locator('#tip .ck-b .glo').first
    if not touch:
        await term.hover()
        await page.wait_for_timeout(650)
        assert await page.evaluate('tipStk.length===0'), 'Hover must not open a nested definition'
        assert await term.get_attribute('title') is None, 'No native hover definition'
    await term.tap() if touch else await term.click()
    await page.wait_for_function('tipStk.length===1 && !TIPEL.hidden')
    await page.wait_for_function("!document.querySelector('#tip .ck-b').textContent.includes('Chargement…')")
    assert (await page.locator('#tip .ck-b').inner_text()).strip()
    back=page.locator('#tip .bk')
    await back.tap() if touch else await back.click()
    await six()
    if not touch:
        await page.locator('#tip .pvl .pv[role="button"]').focus()
        await page.keyboard.press('Enter')
        await page.wait_for_function("tipK==='pv|G1|0' && tipStk.length===1")
        await page.locator('#tip .bk').click()
        await six()
    await page.keyboard.press('Escape')
    ssp=page.locator('#prototype-test [data-t="s|G1"]')
    await ssp.tap() if touch else await ssp.click()
    await six()
    assert await page.locator('#tip .t').inner_text() == 'Sudation anormale'
    if not touch:
        await page.keyboard.press('Escape')
        await ssp.focus()
        await page.keyboard.press('Enter')
        await six()
    await page.keyboard.press('Escape')
    course=page.locator('#prototype-test [data-t="n|G1|c0"]')
    await course.tap() if touch else await course.click()
    await six()
    assert await page.locator('#tip .t').inner_text() == 'Sudation anormale'

    await page.keyboard.press('Escape')
    examination=page.locator('#prototype-test [data-t="n|G1|c5"]')
    await examination.tap() if touch else await examination.click()
    await six()
    assert await page.locator('#tip .ex-region .ex-region__h').count() >= 2
    assert await page.locator('#tip .ex-chip').count() >= 1
    text=await page.locator('#tip .ck-b').inner_text()
    assert text.index('Examen physique par région') < text.index('5. Sémiologie aux explorations')

async def main():
    async with async_playwright() as p:
        kwargs={'args':['--no-sandbox']}
        if os.environ.get('CHROME_PATH'):kwargs['executable_path']=os.environ['CHROME_PATH']
        browser=await p.chromium.launch(**kwargs)
        for touch in (False,True):
            context=await browser.new_context(**(p.devices['Pixel 7'] if touch else {'viewport':{'width':1366,'height':860}}))
            page=await context.new_page()
            errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
            await check(page,touch)
            assert not errors, errors
            await context.close()
        await browser.close()
    print('Infobulles G1 : aucun survol, clic/toucher, clavier, six rubriques, définition imbriquée et retour : OK')

if __name__=='__main__':asyncio.run(main())
