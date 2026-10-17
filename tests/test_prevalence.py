# Contrôles des fréquences des diagnostics différentiels (Asclépios, 17.10.2026) : règles P1 à P7 du contrôleur
# (tools/audit/prevalence.py) sur des cas d'essai, données réelles à jour, puis affichage sur ordinateur et mobile :
# ordre décroissant, % en rouge à côté du diagnostic, « % à vérifier » en dernier, fenêtre du % (cadre, source, date),
# légende, clé de progression inchangée. Variables : APP_FILE, CHROME_PATH, SHOTS_DIR. Sortie JSON.
import asyncio, copy, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools')); sys.path.insert(0, os.path.join(ROOT, 'tools', 'audit'))
import prevalence as P
APP = os.path.abspath(os.environ.get('APP_FILE', os.path.join(ROOT, 'app_v2.html')))
SHOTS = os.environ.get('SHOTS_DIR', os.path.join(ROOT, 'qa', 'shots'))
os.makedirs(SHOTS, exist_ok=True)
CHROME = os.environ.get('CHROME_PATH') or None
LAUNCH = dict(args=['--no-sandbox'], **({'executable_path': CHROME} if CHROME else {}))
from playwright.async_api import async_playwright

NOT = {'X1': [['A', 'B', 'C'], []]}
SRC = json.load(open(os.path.join(ROOT, 'data', 'ck', 'src.json'), encoding='utf-8'))[0]['id']
OK = {'X1': {'cadre': 'Essai', 'items': [
    {'i': 0, 'nom': 'A', 'prev_pct': 5, 'src': SRC, 'loc': 'Tableau 1', 'date_lu': '2026-10-17', 'rang': 2},
    {'i': 1, 'nom': 'B', 'prev_pct': 20, 'src': SRC, 'loc': 'Tableau 1', 'date_lu': '2026-10-17', 'rang': 1},
    {'i': 2, 'nom': 'C', 'prev_pct': None, 'statut': 'À vérifier', 'rang': 3}]}}


def regles(mut):
    D = copy.deepcopy(OK); mut(D['X1']['items']); return {e[2] for e in P.controler(ROOT, D, NOT)}


async def ecran(b, out, nom, vp, mobile):
    c = await b.new_context(viewport=vp, is_mobile=mobile, has_touch=mobile)
    pg = await c.new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    await pg.goto('file://' + APP); await pg.wait_for_timeout(1200)
    await pg.wait_for_function('!!window.CK_PREV&&!!window.CK_SRC', timeout=8000)
    c0 = await pg.evaluate("(()=>{const c=PRV['S2.5']?'S2.5':Object.keys(PRV)[0];return c||null})()")
    if not c0:  # aucune donnée encore : jeu d'essai en mémoire, jamais écrit dans le dépôt
        c0 = 'S2.5'
        await pg.evaluate("c=>{const n=NOT[c][0].length;PRV[c]=[[0,40.5],[3,12],[1,1,'<'],...[...Array(n).keys()].filter(i=>i>3||i===2).map(i=>[i,null])];"
                          "window.CK_PREV=window.CK_PREV||{};window.CK_PREV[c]={0:{cadre:'Essai',type:'consultation',date_lu:'2026-10-17'}}}", c0)
    await pg.evaluate("c=>{NSEL=c;$$('.tab').find(t=>t.dataset.v==='not').click();renderNot()}", c0)
    await pg.wait_for_timeout(500)
    r = await pg.evaluate("""c=>{const R=$$('#v-not .nr[data-k^="d"]');const k=R.map(r=>+r.dataset.k.slice(1));const p=PRV[c].map(x=>x[0]);
      const v=R.map(r=>r.querySelector('.pv'));const col=v[0]&&getComputedStyle(v[0]).color;
      const nums=PRV[c].filter(x=>x[1]!=null).map(x=>x[1]);
      return {ordre:k.join()===p.join(),pv:v.every(Boolean),rouge:/rgb\\((1[5-9]\\d|2\\d\\d), ?\\d{1,2}\\d?, ?\\d{1,2}\\d?\\)/.test(col)&&getComputedStyle(v[0]).fontWeight>=600,
       dec:nums.every((x,i)=>!i||x<=nums[i-1]),av:v.slice(nums.length).every(e=>/à vérifier/.test(e.textContent)),
       leg:!!$('#v-not .pvleg')&&/fréquence/.test($('#v-not .pvleg').textContent),
       cote:v[0]&&R[0].querySelector('.tw').getBoundingClientRect().top<=v[0].getBoundingClientRect().bottom}}""", c0)
    for k, v in r.items():
        out[f'{nom}_{k}'] = v
    first = pg.locator('#v-not .nr[data-k^="d"] .pv').first
    await first.scroll_into_view_if_needed()
    if mobile: await first.tap()
    else: await first.hover()
    await pg.wait_for_timeout(700)
    out[f'{nom}_fenetre_pct'] = await pg.evaluate("!$('#tip').hidden&&/Fréquence du diagnostic/.test($('#tip').textContent)&&/Cadre|à vérifier/.test($('#tip').textContent)")
    await pg.evaluate("hideTip(true)")
    tw = pg.locator('#v-not .nr[data-k^="d"] .tw').first
    if mobile: await tw.tap()
    else: await tw.click()
    await pg.wait_for_timeout(600)
    out[f'{nom}_fenetre_dd_pct_rouge'] = await pg.evaluate("!$('#tip').hidden&&!!$('#tip .pvl .pv')")
    await pg.screenshot(path=os.path.join(SHOTS, f'prevalence-{nom}.png'))
    out[f'{nom}_sans_erreur'] = not errs
    await c.close()


async def main():
    out = {}
    out['P2_chiffre_sup_100'] = 'P2' in regles(lambda L: L[0].update(prev_pct=120))
    out['P3_chiffre_sans_source'] = 'P3' in regles(lambda L: L[0].pop('src'))
    out['P3_chiffre_sans_date'] = 'P3' in regles(lambda L: L[0].pop('date_lu'))
    out['P3_date_future'] = 'P3' in regles(lambda L: L[0].update(date_lu='2999-01-01'))
    out['P4_vide_sans_statut'] = 'P4' in regles(lambda L: L[2].pop('statut'))
    out['P1_nom_change'] = 'P1' in regles(lambda L: L[1].update(nom='Bx'))
    out['P1_index_manquant'] = 'P1' in regles(lambda L: L.pop())
    out['cas_valide'] = not P.controler(ROOT, copy.deepcopy(OK), NOT)
    out['ordre_decroissant_puis_rang'] = [r[0] for r in P.prv(OK)['X1']] == [1, 0, 2]
    out['donnees_reelles_valides'] = not P.controler()
    out['prv_et_prev_js_a_jour'] = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'prev_build.py'), '--check'],
                                                  capture_output=True).returncode == 0
    async with async_playwright() as p:
        b = await p.chromium.launch(**LAUNCH)
        await ecran(b, out, 'ordinateur', {'width': 1366, 'height': 860}, False)
        await ecran(b, out, 'mobile', {'width': 390, 'height': 844}, True)
        await b.close()
    print(json.dumps(out, ensure_ascii=False))
    return 0 if all(out.values()) else 1

if __name__ == '__main__':
    sys.exit(asyncio.run(main()))
