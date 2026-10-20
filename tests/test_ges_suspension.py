"""Parcours Gestes suspendu : statut, coche historique et infobulle au clic."""
import asyncio
import json
import os
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
APP = Path(os.environ.get('APP_FILE', ROOT / 'app_v2.html')).resolve()
CHROME = os.environ.get('CHROME_PATH')


async def main():
    out = {}
    errors = []
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(args=['--no-sandbox'], **({'executable_path': CHROME} if CHROME else {}))
        page = await browser.new_page()
        page.on('pageerror', lambda error: errors.append(str(error)))
        await page.goto(APP.as_uri())
        await page.evaluate("localStorage.setItem('orga-ges', JSON.stringify({peau_0:1}))")
        await page.reload()
        await page.click('.tab[data-v=ges]')
        row = page.locator('#g-list .gr[data-t="g|peau|0"]')
        box = row.locator('input[data-g="peau_0"]')
        out['suspension_annoncee'] = await page.locator('#v-ges .card').first.locator('p.st').first.evaluate("e=>e.textContent.includes('Contenu en reconstruction')")
        out['progression_conservee'] = await box.is_checked() and await page.evaluate("JSON.parse(localStorage.getItem('orga-ges')).peau_0===1")
        out['nouvelle_coche_suspendue'] = await box.is_disabled() and await row.locator('p.st').count() == 1
        await row.locator('.tw').click()
        out['infobulle_statut'] = await page.evaluate("!document.querySelector('#tip').hidden && document.querySelector('#tip').textContent.includes('contenu en reconstruction') && !document.querySelector('#tip').textContent.includes('À énoncer')")
        await browser.close()
    out['errors'] = errors
    print(json.dumps(out, ensure_ascii=False))


asyncio.run(main())
