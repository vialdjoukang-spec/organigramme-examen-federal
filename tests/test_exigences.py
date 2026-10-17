# Contrôles de l’onglet « Exigences » 2027 (Thémis avec Janus, 17.10.2026) : cases, statuts, sources, migration, persistance, bandeau, mobile.
# Variables : APP_FILE, CHROME_PATH, SHOTS_DIR. Sortie : JSON {contrôle: booléen, …, "errors": [...]}.
import asyncio, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.abspath(os.environ.get('APP_FILE', os.path.join(ROOT, 'app_v2.html')))
SHOTS = os.environ.get('SHOTS_DIR', os.path.join(ROOT, 'qa', 'shots'))
os.makedirs(SHOTS, exist_ok=True)
CHROME = os.environ.get('CHROME_PATH') or None
LAUNCH = dict(args=['--no-sandbox'], **({'executable_path': CHROME} if CHROME else {}))
from playwright.async_api import async_playwright
EXI = json.load(open(os.path.join(ROOT, 'data', 'EXI.json'), encoding='utf-8'))
VERIF = sorted(i['id'] for i in EXI['items'] if i['s'] == 'a_verifier')
# Ancien état : clés indexées e0…e15 de la version 2026 (e4 = inscription, e8 = diplôme, e13 = émolument, e0 = format CK sans équivalent).
OLD = {'e0': True, 'e4': True, 'e8': True, 'e13': True, 'e14': False, 'a0_0': True}


async def boot(pg, tab=True):
    await pg.goto('file://' + APP); await pg.wait_for_timeout(1500)
    if tab:
        await pg.locator('.tab[data-v=exi]').click(); await pg.wait_for_timeout(200)


async def main():
    out, errs = {}, []
    async with async_playwright() as p:
        b = await p.chromium.launch(**LAUNCH)
        c = await b.new_context(viewport={'width': 1366, 'height': 860})
        await c.clock.set_fixed_time('2026-11-16T10:00:00+01:00')
        pg = await c.new_page(); pg.on('pageerror', lambda e: errs.append(str(e)))
        await boot(pg, False)
        await pg.evaluate("o=>{const v=JSON.parse(localStorage.getItem('orga-ef')||'{}');v.exi=o;localStorage.setItem('orga-ef',JSON.stringify(v))}", OLD)
        await boot(pg)
        out['quarante_six_cases_ids_stables'] = await pg.evaluate("(()=>{const b=$$('#exi input[data-x]');return b.length===46&&new Set(b.map(x=>x.id)).size===46&&b.every(x=>x.id==='exi-'+x.dataset.x)})()")
        out['six_groupes'] = await pg.evaluate("$$('#exi fieldset').length===6")
        out['source_officielle_par_case'] = await pg.evaluate("$$('#exi label.chk').every(l=>{const a=l.querySelector('small a');return a&&/^https:\\/\\/(www\\.bag\\.admin\\.ch|healthreg-online\\.admin\\.ch|www\\.fedlex\\.admin\\.ch|www\\.iml\\.unibe\\.ch|www\\.unige\\.ch)\\//.test(a.href)&&a.target==='_blank'})")
        out['badges_a_verifier_exacts'] = await pg.evaluate("$$('#exi label.chk').filter(l=>l.querySelector('.exi-vb')).map(l=>l.querySelector('input').dataset.x).sort().join()") == ','.join(VERIF)
        out['migration_coches_reportees'] = await pg.evaluate("['C1','B4','D1'].every(k=>$('#exi-'+k).checked)&&!$('#exi-F6').checked&&$$('#exi input:checked').length===3")
        out['migration_conserve_autres_cles'] = await pg.evaluate("(()=>{const v=JSON.parse(localStorage.getItem('orga-ef')).exi;return v.e0===true&&v.a0_0===true&&v._m27===1})()")
        # Persistance : on décoche une case migrée, on en coche une autre, puis on recharge.
        await pg.locator('#exi-C1').uncheck(); await pg.locator('#exi-A3').check(); await pg.wait_for_timeout(200)
        await boot(pg)
        out['coches_persistent_apres_rechargement'] = await pg.evaluate("$('#exi-A3').checked&&!$('#exi-C1').checked&&$('#exi-B4').checked")
        out['migration_ne_rejoue_pas'] = await pg.evaluate("!$('#exi-C1').checked")
        out['compteur_juste'] = await pg.evaluate("/^3 points sur 46 sont cochés ; " + str(len(VERIF)) + " points/.test($('#exi-c').textContent)")
        out['bandeau_2027'] = await pg.evaluate("(()=>{const t=$('#exi-bn').textContent;return /session 2026 est terminée/.test(t)&&/15\\.12\\.2026/.test(t)&&/31\\.03\\.2027/.test(t)&&/à confirmer/.test(t)&&/10\\.08\\.2027/.test(t)&&/06\\.09\\.2027/.test(t)})()")
        out['compte_a_rebours'] = await pg.evaluate("/ouvre dans 29 jours/.test($('#exi-cd').textContent)")
        out['aucune_date_2026_a_venir'] = await pg.evaluate("!/délai 2026|Dates 2026 de référence/.test($('#v-exi').textContent+$('#v-calc').textContent)")
        await pg.screenshot(path=os.path.join(SHOTS, 'exigences_ordinateur.png'), full_page=False)
        m = await b.new_context(**p.devices['Pixel 7'])
        pm = await m.new_page(); pm.on('pageerror', lambda e: errs.append(str(e)))
        await boot(pm)
        await pm.locator('#exi-E2').tap(); await pm.wait_for_timeout(200)
        out['mobile_case_cochable_sans_debordement'] = await pm.evaluate("$('#exi-E2').checked&&document.documentElement.scrollWidth<=innerWidth+1")
        await pm.screenshot(path=os.path.join(SHOTS, 'exigences_mobile.png'))
        await b.close()
    out['errors'] = errs
    print(json.dumps(out, ensure_ascii=False))

asyncio.run(main())
