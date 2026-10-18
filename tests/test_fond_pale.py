# Fond pâle par défaut (patch 0016) : #fbfbf8 sans teinte jaune, gilt à 0, contraste AA du texte.
# Sortie : JSON de contrôles booléens + 'errors'. Variables : APP_FILE, CHROME_PATH.
import asyncio, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.abspath(os.environ.get('APP_FILE', os.path.join(ROOT, 'app_v2.html')))
CHROME = os.environ.get('CHROME_PATH') or None
from playwright.async_api import async_playwright

CHECK = """() => {
  const cs = getComputedStyle(document.body);
  const bg = cs.backgroundColor, ink = cs.color;
  const parse = s => s.match(/\\d+/g).map(Number).slice(0, 3);
  const [br, bg_g, bb] = parse(bg), [ir, ig, ib] = parse(ink);
  const lin = c => { c /= 255; return c <= 0.04045 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); };
  const L = (r, g, b) => 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b);
  const ratio = (L1, L2) => { const a = Math.max(L1, L2), b = Math.min(L1, L2); return (a + 0.05) / (b + 0.05); };
  const gilt = getComputedStyle(document.documentElement).getPropertyValue('--gilt').trim();
  const near = (a, b, t = 6) => Math.abs(a - b) <= t;
  // #fbfbf8 → rgb(251,251,248) ; #1a1a1a → rgb(26,26,26)
  return {
    bg_pale: near(br, 251) && near(bg_g, 251) && near(bb, 248),
    bg_sans_jaune: (br - bb) <= 8 && (bg_g - bb) <= 8,  // écart R/G vs B ≤ 8 (pas de dominante jaune)
    gilt_zero: parseFloat(gilt) === 0,
    contraste_aa: ratio(L(br, bg_g, bb), L(ir, ig, ib)) >= 4.5,
    contraste_mut: (() => {
      const m = getComputedStyle(document.documentElement).getPropertyValue('--mut').trim();
      let r, g, b;
      if (m.startsWith('#')) {
        const h = m.slice(1);
        r = parseInt(h.slice(0, 2), 16); g = parseInt(h.slice(2, 4), 16); b = parseInt(h.slice(4, 6), 16);
      } else {
        [r, g, b] = parse(m);
      }
      return ratio(L(br, bg_g, bb), L(r, g, b)) >= 4.5;
    })(),
    pas_de_selecteur_themes: !document.getElementById('fond-btn')
  };
}"""


async def main():
    out, errs = {}, []
    src = open(APP, encoding='utf-8').read()
    out['jetons_fbfbf8_dans_fichier'] = src.count('#fbfbf8') >= 2 and '#f6f1e4' not in src
    out['gilt_defaut_zero_dans_js'] = 'disp:{gilt:0,fs:100}' in src and "(d.gilt??0)" in src
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--no-sandbox'], **({'executable_path': CHROME} if CHROME else {}))
        ctx = await b.new_context(viewport={'width': 1280, 'height': 900}, color_scheme='light')
        pg = await ctx.new_page()
        pg.on('pageerror', lambda e: errs.append(str(e)))
        await pg.goto('file://' + APP)
        await pg.wait_for_timeout(800)
        mes = await pg.evaluate(CHECK)
        out.update(mes)
        await b.close()
    out['errors'] = errs
    print(json.dumps(out, ensure_ascii=False))


asyncio.run(main())
