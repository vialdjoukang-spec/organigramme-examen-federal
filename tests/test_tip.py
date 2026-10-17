# Contrôles d’interaction de la fenêtre d’information (19 par profil : ordinateur et mobile).
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
TAG = sys.argv[1] if len(sys.argv) > 1 else 'ci'
URL = 'file://' + APP
R = {}
async def run(p, name, ctxargs):
    b = await p.chromium.launch(**LAUNCH)
    c = await b.new_context(**ctxargs)
    pg = await c.new_page()
    errs = []
    pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
    pg.on('pageerror', lambda e: errs.append('PAGEERROR ' + str(e)))
    await pg.goto(URL); await pg.wait_for_timeout(2500)
    res = {}
    vis = lambda: pg.evaluate("!document.getElementById('tip').hidden")
    tap = (lambda loc: loc.tap()) if ctxargs.get('has_touch') else (lambda loc: loc.click())
    # Notions CK
    await tap(pg.locator('.tab[data-v=not]')); await pg.wait_for_timeout(300)
    await tap(pg.locator('#n-list [data-n]').first); await pg.wait_for_timeout(400)
    row = pg.locator('#v-not .nr').first
    word = row.locator('.tw') if await row.locator('.tw').count() else row.locator('span').first
    cb = row.locator('input[type=checkbox]')
    before_cb = await cb.is_checked()
    await pg.mouse.move(1, 1); await pg.wait_for_timeout(400)
    await tap(word); await pg.wait_for_timeout(400)
    res['not_click_word_opens'] = await vis()
    res['not_pinned'] = await pg.evaluate("typeof tipPin!=='undefined'?tipPin:null")
    res['not_checkbox_unchanged'] = (await cb.is_checked()) == before_cb
    await pg.screenshot(path=f'{SHOTS}/{TAG}_{name}_notions.png')
    await tap(word); await pg.wait_for_timeout(300)
    res['not_same_word_closes'] = not await vis()
    await tap(word); await pg.wait_for_timeout(300)
    await pg.keyboard.press('Escape'); await pg.wait_for_timeout(200)
    res['not_escape_closes'] = not await vis()
    await tap(word); await pg.wait_for_timeout(300)
    if await vis():
        await tap(pg.locator('#tip .h button')); await pg.wait_for_timeout(200)
    res['not_closebtn_closes'] = not await vis()
    # checkbox still toggles
    await tap(cb); await pg.wait_for_timeout(300)
    row = pg.locator('#v-not .nr').first
    res['not_checkbox_still_toggles'] = (await row.locator('input[type=checkbox]').is_checked()) != before_cb
    await tap(row.locator('input[type=checkbox]')); await pg.wait_for_timeout(300)  # restore
    # keyboard
    tw = pg.locator('#v-not .nr .tw').first
    if await tw.count():
        await tw.focus(); await pg.keyboard.press('Enter'); await pg.wait_for_timeout(300)
        res['kbd_enter_opens'] = await vis()
        await pg.keyboard.press('Escape'); await pg.wait_for_timeout(200)
        res['kbd_focus_returns'] = await pg.evaluate("document.activeElement.classList.contains('tw')")
        await tw.focus(); await pg.keyboard.press(' '); await pg.wait_for_timeout(300)
        res['kbd_space_opens'] = await vis()
        res['aria_expanded_true'] = await tw.get_attribute('aria-expanded')
        await pg.keyboard.press('Escape')
    # Gestes
    await tap(pg.locator('.tab[data-v=ges]')); await pg.wait_for_timeout(800)
    gr = pg.locator('#v-ges .gr').first
    gcb = gr.locator('input[type=checkbox]'); g0 = await gcb.is_checked()
    await tap(gr.locator('b').first); await pg.wait_for_timeout(400)
    res['ges_click_word_opens'] = await vis()
    res['ges_checkbox_unchanged'] = (await gcb.is_checked()) == g0
    box = await pg.evaluate("(()=>{const r=document.getElementById('tip').getBoundingClientRect();return [r.left,r.top,r.width,r.height,innerWidth,innerHeight]})()")
    res['tip_rect'] = box
    res['tip_inside_viewport'] = box[0] >= 0 and box[0]+box[2] <= box[4] and box[1] >= 0 and box[1]+box[3] <= box[5]
    await pg.screenshot(path=f'{SHOTS}/{TAG}_{name}_gestes.png')
    # click outside closes
    await tap(pg.locator('h1, header').first); await pg.wait_for_timeout(300)
    res['ges_outside_closes'] = not await vis()
    await tap(gcb); await pg.wait_for_timeout(300)
    res['ges_checkbox_still_toggles'] = (await pg.locator('#v-ges .gr').first.locator('input[type=checkbox]').is_checked()) != g0
    await tap(pg.locator('#v-ges .gr').first.locator('input[type=checkbox]'))
    # SSP list selection still works (calendar)
    await tap(pg.locator('.tab[data-v=cal]')); await pg.wait_for_timeout(300)
    it = pg.locator('#list .it').first; c = await it.get_attribute('data-c')
    await tap(it); await pg.wait_for_timeout(300)
    res['cal_list_select_works'] = await pg.evaluate(f"!!document.querySelector('#list .it.sel[data-c=\"{c}\"]')")
    res['console_errors'] = errs
    R[name] = res
    await b.close()
async def main():
    async with async_playwright() as p:
        await run(p, 'desktop', dict(viewport={'width':1366,'height':860}))
        await run(p, 'mobile', dict(**p.devices['Pixel 7']))
    print(json.dumps(R, indent=1, ensure_ascii=False))
asyncio.run(main())
