"""Choix de dix fonds pâles : zones de lecture, persistance et blocs du haut préservés."""
import asyncio,base64
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
async def check(browser,mobile=False,dark=False):
    context=await browser.new_context(viewport={'width':390 if mobile else 1440,'height':844 if mobile else 900},has_touch=mobile,is_mobile=mobile,color_scheme='dark' if dark else 'light')
    page=await context.new_page()
    errors=[];page.on('pageerror',lambda error:errors.append(str(error)))
    await page.goto((ROOT/'app_v2.html').as_uri())
    await page.wait_for_selector('#fond-theme>button')
    await page.evaluate('document.fonts.ready')
    snapshot="""() => [...document.querySelectorAll('header.top,header.top *,#bak,#bak *')].map(el=>{const c=getComputedStyle(el);return [el.tagName,el.id,el.className,c.backgroundColor,c.color,c.font,c.borderColor]})"""
    before=await page.evaluate(snapshot)
    trigger=page.get_by_role('button',name='Thème de fond',exact=True)
    await trigger.click();await page.wait_for_selector('#fond-palette:not([hidden])')
    if not dark:
        out=ROOT/'qa/shots'/('fond-mobile.png' if mobile else 'fond-ordinateur.png');out.parent.mkdir(parents=True,exist_ok=True)
        picture=await page.locator('#fond-palette').screenshot(path=str(out))
        print('FOND_APERCU '+('mobile' if mobile else 'ordinateur')+' '+base64.b64encode(picture).decode(),flush=True)
    buttons=page.locator('.fond-choice');assert await buttons.count()==10
    names=await buttons.all_text_contents();assert len(set(names))==10
    choices=await buttons.evaluate_all("xs=>xs.map(x=>({id:x.dataset.fond,color:x.style.getPropertyValue('--swatch')}))")
    assert len({x['color'] for x in choices})==10
    for choice in choices:
        await page.locator('[data-fond="'+choice['id']+'"]').click()
        await page.wait_for_function('id=>document.documentElement.dataset.readingTheme===id',arg=choice['id'])
        got=await page.evaluate("""() => {const el=document.querySelector('#v-cal .card');return [getComputedStyle(el).backgroundColor,getComputedStyle(el).color]}""")
        h=choice['color'].lstrip('#');rgb='rgb('+', '.join(str(int(h[i:i+2],16)) for i in [0,2,4])+')'
        assert got==[rgb,'rgb(26, 26, 26)'],(choice,got)
        assert await page.evaluate(snapshot)==before,'En-tête ou sauvegarde modifiés'
        assert await page.locator('[data-fond="'+choice['id']+'"]').get_attribute('aria-pressed')=='true'
    last=choices[-1]
    await page.reload();await page.wait_for_selector('#fond-theme>button')
    await page.evaluate('document.fonts.ready')
    assert await page.evaluate('document.documentElement.dataset.readingTheme')==last['id']
    after=await page.evaluate(snapshot)
    assert after==before,{'profil':(mobile,dark),'avant':before,'apres':after}
    await page.get_by_role('button',name='Thème de fond',exact=True).click()
    await page.keyboard.press('Home');assert await page.locator('.fond-choice').first.evaluate('(el)=>el===document.activeElement')
    await page.keyboard.press('ArrowRight');assert await page.locator('.fond-choice').nth(1).evaluate('(el)=>el===document.activeElement')
    await page.keyboard.press('Escape');assert await page.locator('#fond-palette').is_hidden()
    assert await page.get_by_role('button',name='Thème de fond',exact=True).evaluate('(el)=>el===document.activeElement')
    assert await page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'),'Débordement horizontal'
    await page.evaluate("localStorage.setItem('orga-theme-fond','valeur-invalide')")
    await page.reload();await page.wait_for_selector('#fond-theme>button')
    await page.evaluate('document.fonts.ready')
    assert await page.evaluate('!document.documentElement.hasAttribute("data-reading-theme")')
    assert not errors,errors
    await context.close()
async def main():
    async with async_playwright() as p:
        browser=await p.chromium.launch(args=['--no-sandbox'])
        for mobile,dark in [(False,False),(True,False),(False,True)]:await check(browser,mobile,dark)
        await browser.close()
    print('Fonds : dix teintes, lecture, blocs préservés, persistance, clavier et mobile conformes.')
if __name__=='__main__':asyncio.run(main())
