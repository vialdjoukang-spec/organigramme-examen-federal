# Contrôles des stations CS (Chiron, 17.10.2026) : données valides et à jour (cs_build --check), cinq stations
# pilotes, fenêtre « Station CS » sur la fiche SSP (Notions CK), sections officielles (consigne, rôle, grille ASM,
# communication KK), répliques « seulement si demandé », infobulles g|… et hyp|… au clic, sources datées,
# état ouvert conservé après un nouveau rendu, fiche sans station inchangée, ordinateur et mobile sans débordement.
# Variables : APP_FILE, CHROME_PATH, SHOTS_DIR. Sortie JSON.
import asyncio, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.abspath(os.environ.get('APP_FILE', os.path.join(ROOT, 'app_v2.html')))
SHOTS = os.environ.get('SHOTS_DIR', os.path.join(ROOT, 'qa', 'shots'))
os.makedirs(SHOTS, exist_ok=True)
CHROME = os.environ.get('CHROME_PATH') or None
LAUNCH = dict(args=['--no-sandbox'], **({'executable_path': CHROME} if CHROME else {}))
from playwright.async_api import async_playwright
ST = json.load(open(os.path.join(ROOT, 'data', 'cs', 'stations.json'), encoding='utf-8'))
CLIP = """(()=>{const P=$('.st-pan');if(!P)return false;const p=P.getBoundingClientRect();return [...P.querySelectorAll('*')].every(e=>{const r=e.getBoundingClientRect();if(!r.width)return true;return r.right<=p.right+1&&r.left>=p.left-1})&&document.documentElement.scrollWidth<=innerWidth+1})()"""


async def fiche(pg, c):
    await pg.locator('.tab[data-v=not]').click(); await pg.wait_for_timeout(200)
    await pg.evaluate("c=>{NSEL=c;renderNot()}", c)


async def main():
    out, errs = {}, []
    out['cs_build_a_jour'] = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'cs_build.py'), '--check'],
                                            capture_output=True).returncode == 0
    out['cinq_stations_formats_distincts'] = len(ST) >= 5 and len({s['format'] for s in ST}) >= 4 and len({s['ssp'] for s in ST}) == len(ST)
    async with async_playwright() as p:
        b = await p.chromium.launch(**LAUNCH)
        c = await b.new_context(viewport={'width': 1366, 'height': 900})
        pg = await c.new_page()
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.on('console', lambda m: m.type == 'error' and errs.append(m.text))
        await pg.goto('file://' + APP); await pg.wait_for_timeout(1000)
        await fiche(pg, 'G1'); await pg.wait_for_timeout(600)
        out['fiche_sans_station_inchangee'] = await pg.evaluate("!$('#n-main .st-cs')")
        await fiche(pg, 'S2.5')
        await pg.wait_for_selector('#n-main .st-cs [data-st]', timeout=8000)
        out['bouton_apres_premier_p_st'] = await pg.evaluate("$('#n-main p.st').nextElementSibling.classList.contains('st-cs')")
        await pg.locator('#n-main [data-st]').first.click()
        await pg.wait_for_function("$('.st-pan')&&!$('.st-pan').hidden&&$$('.st-pan details').length>=6", timeout=8000)
        out['sections_officielles'] = await pg.evaluate("(()=>{const t=$('.st-pan').textContent;return ['Consigne affichée sur la porte','Rôle du patient standardisé','Grille ASM (75 %','Communication KK (25 %','Être à l’écoute des sentiments et des besoins','Sources et format officiel'].every(x=>t.includes(x))})()")
        out['seulement_si_demande'] = await pg.evaluate("$$('.st-pan .vb.pend').some(e=>e.textContent==='seulement si demandé')")
        out['sources_datees'] = await pg.evaluate("/lu le 17\\.10\\.2026/.test($('.st-pan').textContent)&&!!$('.st-pan a[href*=\"bag.admin.ch\"]')")
        out['a_verifier_visible'] = await pg.evaluate("$$('.st-pan .vb.pend').some(e=>e.textContent==='À vérifier')")
        await pg.evaluate("$$('.st-pan details').forEach(d=>d.open=true)")
        g = pg.locator('.st-pan .ck-l[data-t^="g|"]').first
        await g.scroll_into_view_if_needed(); await g.click(); await pg.wait_for_timeout(400)
        out['geste_ouvre_infobulle'] = await pg.evaluate("!$('#tip').hidden")
        await pg.evaluate("hideTip(true)")
        h = pg.locator('.st-pan .ck-l[data-t^="hyp|"]').first
        await h.scroll_into_view_if_needed(); await h.click(); await pg.wait_for_timeout(700)
        out['chaine_ck_ouvre_infobulle'] = await pg.evaluate("!$('#tip').hidden&&/Syndrome coronarien|coronarien/i.test($('#tip').textContent)")
        await pg.evaluate("hideTip(true)")
        out['texte_justifie_sans_rouge'] = await pg.evaluate("(()=>{const s=getComputedStyle($('.st-pan li'));const red=$$('.st-pan *').some(e=>{const m=getComputedStyle(e).color.match(/\\d+/g);return m&&+m[0]>180&&+m[1]<80&&+m[2]<80});return s.textAlign==='justify'&&!red})()")
        out['ordinateur_sans_debordement'] = await pg.evaluate(CLIP)
        await pg.locator('#n-todo').check(); await pg.wait_for_timeout(500)
        out['etat_ouvert_conserve'] = await pg.evaluate("!!$('.st-pan')&&!$('.st-pan').hidden&&$('#n-main [data-st]').getAttribute('aria-expanded')==='true'")
        await pg.locator('#n-todo').uncheck(); await pg.wait_for_timeout(500)
        await pg.evaluate("$$('.st-pan details').forEach((d,i)=>d.open=i===0||/Grille ASM/.test(d.firstElementChild.textContent))")
        await pg.evaluate("$('.tab').parentElement.style.visibility='hidden'")
        await pg.locator('#n-main .st-cs').screenshot(path=os.path.join(SHOTS, 'cs-station-ordinateur.png'))
        await pg.evaluate("$('.tab').parentElement.style.visibility=''")
        ok = True
        for s in ST:
            await fiche(pg, s['ssp'])
            try:
                await pg.wait_for_selector(f'#n-main [data-st="{s["id"]}"]', timeout=6000)
                await pg.locator(f'#n-main [data-st="{s["id"]}"]').click()
                await pg.wait_for_function("$('.st-pan')&&$$('.st-pan details').length>=6", timeout=6000)
            except Exception:
                ok = False
        out['cinq_stations_affichees'] = ok
        m = await b.new_context(viewport={'width': 412, 'height': 915}, device_scale_factor=2, is_mobile=True, has_touch=True)
        mp = await m.new_page(); mp.on('pageerror', lambda e: errs.append(str(e)))
        await mp.goto('file://' + APP); await mp.wait_for_timeout(1000)
        await mp.evaluate("$$('.tab').find(t=>t.dataset.v==='not').click();NSEL='S2.5';renderNot()")
        await mp.wait_for_selector('#n-main [data-st]', timeout=8000)
        await mp.locator('#n-main [data-st]').first.tap()
        await mp.wait_for_function("$('.st-pan')&&$$('.st-pan details').length>=6", timeout=8000)
        await mp.evaluate("$$('.st-pan details').forEach((d,i)=>d.open=i<2);$('.tab').parentElement.style.visibility='hidden'")
        out['mobile_sans_debordement'] = await mp.evaluate(CLIP)
        await mp.locator('#n-main .st-cs').screenshot(path=os.path.join(SHOTS, 'cs-station-mobile.png'))
        await b.close()
    out['errors'] = errs
    print(json.dumps(out, ensure_ascii=False))


asyncio.run(main())
