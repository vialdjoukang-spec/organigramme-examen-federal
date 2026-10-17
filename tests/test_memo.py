# Contrôles de l’onglet « Mémorisation » fondé sur les preuves (Mnémosyne, 17.10.2026) : douze méthodes, fenêtre m|id
# (survol, clic épinglé, toucher, clavier), DOI cliquables, réglages anciens intacts, options nouvelles, ordinateur et mobile,
# texte non coupé, aucun débordement, données à jour. Variables : APP_FILE, CHROME_PATH, SHOTS_DIR. Sortie JSON.
import asyncio, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.abspath(os.environ.get('APP_FILE', os.path.join(ROOT, 'app_v2.html')))
SHOTS = os.environ.get('SHOTS_DIR', os.path.join(ROOT, 'qa', 'shots'))
os.makedirs(SHOTS, exist_ok=True)
CHROME = os.environ.get('CHROME_PATH') or None
LAUNCH = dict(args=['--no-sandbox'], **({'executable_path': CHROME} if CHROME else {}))
from playwright.async_api import async_playwright
MEM = json.load(open(os.path.join(ROOT, 'data', 'MEM.json'), encoding='utf-8'))
IDS = [m['id'] for m in MEM['methodes']]
OLD = {'meth': 'sm2', 'int': '2,5,9', 'rappel': False, 'test': True, 'inter': False, 'feyn': True, 'ret': 85, 'max': 7, 'hor': 18}
CLIP = """(()=>{const L=$$('#v-memo .m-it, #v-memo .m-it *');return L.every(e=>{const r=e.getBoundingClientRect();if(!r.width)return true;
 const p=e.closest('.m-it').getBoundingClientRect();return r.right<=p.right+1&&r.left>=p.left-1&&e.scrollWidth<=e.clientWidth+1})})()"""


async def boot(pg):
    await pg.goto('file://' + APP); await pg.wait_for_timeout(1200)
    await pg.locator('.tab[data-v=memo]').click()
    await pg.wait_for_function("$$('#m-evl .m-it').length===12", timeout=8000)


async def main():
    out, errs = {}, []
    out['mem_js_a_jour'] = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'build_mem.py'), '--js', '--check'],
                                          capture_output=True).returncode == 0
    out['douze_methodes_sourcees'] = len(IDS) == 12 and all(m['references'] and m['examen'] and m['principe'] for m in MEM['methodes'])
    async with async_playwright() as p:
        b = await p.chromium.launch(**LAUNCH)
        c = await b.new_context(viewport={'width': 1366, 'height': 860})
        pg = await c.new_page()
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.on('console', lambda m: m.type == 'error' and errs.append(m.text))
        await pg.goto('file://' + APP); await pg.wait_for_timeout(800)
        await pg.evaluate("o=>{S.params.memo=o;put('reglages','params',S.params)}", OLD); await pg.wait_for_timeout(400)
        await boot(pg)
        out['douze_cartes_ordre'] = await pg.evaluate("ids=>$$('#m-evl h3[data-t]').map(h=>h.dataset.t.slice(2)).join()===ids.join()", IDS)
        out['chaque_carte_doi_et_examen'] = await pg.evaluate("$$('#m-evl .m-it').every(a=>a.querySelector('a[href^=\"https://doi.org/10.\"][target=_blank]')&&/Pour l’examen fédéral/.test(a.textContent)&&/lu le 17\\.10\\.2026/.test(a.textContent))")
        # Survol (ordinateur) : la fenêtre s'ouvre sur la méthode 3, avec ses preuves en médecine et un DOI.
        await pg.hover('#m-it-pratique-espacee h3 .tw'); await pg.wait_for_timeout(500)
        out['survol_ouvre_fenetre'] = await pg.evaluate("!$('#tip').hidden&&/Pratique espacée/.test($('#tip').textContent)&&/Preuves en médecine/.test($('#tip').textContent)&&!!$('#tip a[href^=\"https://doi.org/\"]')")
        # Clic : chaque méthode s'épingle, avec principe, usage, preuves en médecine et au moins un DOI.
        ok = True
        for i in IDS:
            await pg.locator(f'#m-it-{i} h3 .tw').click(); await pg.wait_for_timeout(120)
            r = await pg.evaluate("i=>{const t=$('#tip');return !t.hidden&&t.getAttribute('role')==='dialog'&&/Pour l’examen fédéral/.test(t.textContent)&&/Preuves en médecine/.test(t.textContent)&&t.querySelectorAll('a[href^=\"https://doi.org/10.\"]').length>0}", i)
            ok = ok and r
            await pg.locator('#tip .h button[aria-label=Fermer]').click(); await pg.wait_for_timeout(80)
        out['clic_epingle_douze_fenetres'] = ok
        await pg.locator('#m-it-enseigner h3 .tw').focus(); await pg.keyboard.press('Enter'); await pg.wait_for_timeout(200)
        out['clavier_ouvre_fenetre'] = await pg.evaluate("!$('#tip').hidden&&/Enseigner|enseigner/.test($('#tip').textContent)")
        await pg.evaluate("hideTip(true)")
        out['options_i_sur_strategies'] = await pg.evaluate("['m-rappel','m-test','m-inter','m-feyn','m-retro','m-reap'].every(i=>$('#'+i).nextElementSibling.querySelector('.ti[data-t^=\"m|\"]'))&&!!$('#v-memo legend .ti[data-t=\"m|pratique-espacee\"]')")
        await pg.locator('#m-reap + span .ti').click(); await pg.wait_for_timeout(150)
        out['bouton_i_ouvre_sans_cocher'] = await pg.evaluate("!$('#tip').hidden&&/Réapprentissage/.test($('#tip').textContent)&&$('#m-reap').checked")
        await pg.locator('#tip .h button[aria-label=Fermer]').click()
        out['reglages_anciens_intacts'] = await pg.evaluate("o=>{const m=M();return Object.keys(o).every(k=>m[k]===o[k])&&$('input[name=m-meth][value=sm2]').checked&&$('#m-int').value==='2,5,9'&&!$('#m-rappel').checked&&$('#m-feyn').checked&&$('#m-ret').value==='85'}", OLD)
        out['options_nouvelles_par_defaut'] = await pg.evaluate("$('#m-retro').checked&&$('#m-reap').checked&&/rétroaction|correction/.test($('#m-cons').textContent)")
        await pg.locator('#m-retro').uncheck(); await pg.locator('#m-save').click(); await pg.wait_for_timeout(200)
        await boot(pg)
        out['options_nouvelles_persistent'] = await pg.evaluate("!$('#m-retro').checked&&$('#m-reap').checked&&!/même juste/.test($('#m-cons').textContent)&&M().max===7")
        out['ordinateur_sans_debordement'] = await pg.evaluate(CLIP)
        out['texte_justifie_titres_noirs'] = await pg.evaluate("getComputedStyle($('#m-evl .m-it p')).textAlign==='justify'&&getComputedStyle($('#m-evl h3')).color==='rgb(0, 0, 0)'&&+getComputedStyle($('#m-evl h3')).fontWeight>=700")
        await pg.evaluate("$('.tab').parentElement.style.visibility='hidden'")
        await pg.locator('#m-ev').screenshot(path=os.path.join(SHOTS, 'memo-ordinateur.png'))
        await pg.evaluate("$('.tab').parentElement.style.visibility=''")
        await pg.locator('#m-it-recuperation h3 .tw').click(); await pg.wait_for_timeout(300)
        await pg.screenshot(path=os.path.join(SHOTS, 'memo-ordinateur-fenetre.png'))
        await pg.evaluate("hideTip(true)")
        # Mobile : toucher.
        m = await b.new_context(viewport={'width': 412, 'height': 915}, device_scale_factor=2, is_mobile=True, has_touch=True)
        mp = await m.new_page(); mp.on('pageerror', lambda e: errs.append(str(e)))
        await boot(mp)
        await mp.locator('#m-it-recuperation h3 .tw').scroll_into_view_if_needed()
        await mp.locator('#m-it-recuperation h3 .tw').tap(); await mp.wait_for_timeout(300)
        out['mobile_toucher_ouvre'] = await mp.evaluate("!$('#tip').hidden&&/Rowland/.test($('#tip').textContent)")
        out['mobile_fenetre_dans_ecran'] = await mp.evaluate("(()=>{const r=$('#tip').getBoundingClientRect();return r.left>=0&&r.right<=innerWidth+1})()")
        await mp.locator('#tip .h button[aria-label=Fermer]').tap(); await mp.wait_for_timeout(100)
        out['mobile_sans_debordement'] = await mp.evaluate(CLIP + "&&document.documentElement.scrollWidth<=innerWidth+1")
        await mp.evaluate("$('.tab').parentElement.style.visibility='hidden'")
        await mp.evaluate("scrollTo({top:$('#m-ev').getBoundingClientRect().top+scrollY-8,behavior:'instant'})")
        await mp.screenshot(path=os.path.join(SHOTS, 'memo-mobile.png'))
        await mp.evaluate("$('.tab').parentElement.style.visibility=''")
        await mp.locator('#m-it-pratique-espacee h3 .tw').tap(); await mp.wait_for_timeout(300)
        await mp.screenshot(path=os.path.join(SHOTS, 'memo-mobile-fenetre.png'))
        await b.close()
    out['errors'] = errs
    print(json.dumps(out, ensure_ascii=False))


asyncio.run(main())
