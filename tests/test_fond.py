# Contrôles du sélecteur « Thème de fond d’écran » (Apollon avec Janus, 17.10.2026) : visible sur chaque onglet,
# ordinateur et mobile, choix appliqué et mémorisé, clavier, contraste AA du texte sur chaque fond.
# Variables : APP_FILE, CHROME_PATH. Sortie : JSON {contrôle: booléen, …, "errors": [...]}.
import asyncio, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.abspath(os.environ.get('APP_FILE', os.path.join(ROOT, 'app_v2.html')))
CHROME = os.environ.get('CHROME_PATH') or None
LAUNCH = dict(args=['--no-sandbox'], **({'executable_path': CHROME} if CHROME else {}))
from playwright.async_api import async_playwright
TABS = ['att', 'cal', 'not', 'vit', 'memo', 'cs', 'ges', 'calc', 'exi']
VISIBLE = """()=>{const b=document.getElementById('fond-btn'),r=b.getBoundingClientRect(),e=document.elementFromPoint(r.left+r.width/2,r.top+r.height/2);
return getComputedStyle(b).position==='fixed'&&r.width>=44&&r.height>=44&&r.bottom<=innerHeight&&r.right<=innerWidth&&(e===b||b.contains(e))}"""
CONTRAST = """()=>{const cv=document.createElement('canvas').getContext('2d',{willReadFrequently:true});
const rgb=c=>{cv.clearRect(0,0,1,1);cv.fillStyle='#000';cv.fillStyle=c;cv.fillRect(0,0,1,1);return [...cv.getImageData(0,0,1,1).data].slice(0,3)};
const lum=a=>{const f=v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)};return .2126*f(a[0])+.7152*f(a[1])+.0722*f(a[2])};
const cr=(a,b)=>{const x=lum(a),y=lum(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05)};const s=getComputedStyle(document.documentElement);
const v=n=>rgb(s.getPropertyValue(n).trim());return Math.min(cr(v('--ink'),v('--paper')),cr(v('--ink'),v('--bg')),cr(v('--mut'),v('--paper')),cr(v('--mut'),v('--bg')))}"""


async def main():
    out, errs = {}, []
    async with async_playwright() as p:
        b = await p.chromium.launch(**LAUNCH)
        for prof, ctx in (('ordinateur', {'viewport': {'width': 1366, 'height': 860}}), ('mobile', dict(p.devices['Pixel 7']))):
            c = await b.new_context(**ctx); pg = await c.new_page(); pg.on('pageerror', lambda e: errs.append(str(e)))
            await pg.goto('file://' + APP); await pg.wait_for_timeout(1500)
            act = (lambda l: l.tap()) if ctx.get('has_touch') else (lambda l: l.click())
            ok = True
            for t in TABS:
                await act(pg.locator(f'.tab[data-v={t}]')); await pg.wait_for_timeout(150)
                await pg.evaluate('window.scrollTo(0,document.body.scrollHeight/2)'); await pg.wait_for_timeout(100)
                ok = ok and await pg.evaluate(VISIBLE)
            out[f'{prof}_bouton_visible_sur_9_onglets'] = ok
            await act(pg.locator('#fond-btn')); await pg.wait_for_timeout(200)
            out[f'{prof}_panneau_ouvert_dix_themes'] = await pg.evaluate("!document.getElementById('fond-pan').hidden&&document.querySelectorAll('#fond-pan input[name=fond]').length===11&&document.getElementById('fond-btn').getAttribute('aria-expanded')==='true'")
            await act(pg.locator('#fond-pan input[value="sauge-pale"]')); await pg.wait_for_timeout(150)
            await pg.reload(); await pg.wait_for_timeout(1200)
            out[f'{prof}_choix_memorise_apres_rechargement'] = await pg.evaluate("document.documentElement.dataset.fond==='sauge-pale'&&localStorage.getItem('orga-fond')==='sauge-pale'&&document.documentElement.dataset.theme==='light'")
            await c.close()
        # Clavier et contraste de chaque fond (ordinateur).
        c = await b.new_context(viewport={'width': 1366, 'height': 860}); pg = await c.new_page(); pg.on('pageerror', lambda e: errs.append(str(e)))
        await pg.goto('file://' + APP); await pg.wait_for_timeout(1500)
        await pg.locator('#fond-btn').focus(); await pg.keyboard.press('Enter'); await pg.wait_for_timeout(150)
        foc = await pg.evaluate("document.activeElement&&document.activeElement.name==='fond'")
        await pg.keyboard.press('Escape'); await pg.wait_for_timeout(150)
        out['clavier_ouvre_echap_ferme_focus_rendu'] = foc and await pg.evaluate("document.getElementById('fond-pan').hidden&&document.activeElement.id==='fond-btn'")
        vals = await pg.evaluate("[...document.querySelectorAll('#fond-pan input[name=fond]')].map(i=>i.value).filter(Boolean)")
        mins = []
        for v in vals:
            await pg.evaluate("v=>{localStorage.setItem('orga-fond',v)}", v); await pg.reload(); await pg.wait_for_timeout(600)
            mins.append(await pg.evaluate(CONTRAST))
        out['contraste_aaa_texte_sur_dix_fonds'] = len(mins) == 10 and min(mins) >= 7
        await pg.evaluate("localStorage.removeItem('orga-fond')"); await pg.reload(); await pg.wait_for_timeout(600)
        out['par_defaut_sans_attribut'] = await pg.evaluate("!document.documentElement.hasAttribute('data-fond')")
        await b.close()
    out['errors'] = errs
    print(json.dumps(out, ensure_ascii=False))


asyncio.run(main())
