#!/usr/bin/env python3
"""screenshot.py — captures Playwright (chromium headless) + test console sans erreurs.
CLI: python3 scripts/screenshot.py [--html app/Radio_Paires.html] [--ids IMG-134,IMG-025] [--tag lotX]
Sorties (chemins absolus affichés) : shots/<tag>_list.png, shots/<tag>_<id>.png, shots/<tag>_<id>_bulles.png,
  shots/<tag>_mobile_list.png, shots/<tag>_mobile_<id>.png ; code 1 si erreur console/page.
Par défaut : 2 premiers « complet », 1 « partiel », 1 « introuvable » trouvés dans l'app.
"""
import os, sys, json, time
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    a = sys.argv[1:]
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    html = os.path.abspath(opt("--html", os.path.join(ROOT, "app", "Radio_Paires.html")))
    tag = opt("--tag", time.strftime("%H%M"))
    ids = [x for x in (opt("--ids", "") or "").split(",") if x]
    shots = os.path.join(ROOT, "shots"); os.makedirs(shots, exist_ok=True)
    url = "file://" + html
    errors, made = [], []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
        pg.on("console", lambda m: errors.append(f"console.{m.type}: {m.text}") if m.type in ("error", "warning") else None)
        pg.on("pageerror", lambda e: errors.append(f"pageerror: {e}"))
        pg.goto(url); pg.wait_for_timeout(300)
        if not ids:
            rows = pg.evaluate("DATA.rows.map(r=>[r.id,r.st])")
            pick = lambda st, n: [i for i, s in rows if s == st][:n]
            ids = pick("complet", 2) + pick("partiel", 1) + pick("introuvable", 1)
        def snap(name):
            f = os.path.join(shots, f"{tag}_{name}.png"); pg.screenshot(path=f); made.append(f)
        snap("list")
        for i, mid in enumerate(ids):
            if pg.evaluate(f"RP.open('{mid}')") < 0:
                errors.append(f"id introuvable dans la vue: {mid}"); continue
            pg.wait_for_timeout(350)
            snap(mid)
            reveal = pg.locator("#bHide")
            if reveal.count() and reveal.is_enabled() and "Révéler" in reveal.inner_text():
                reveal.click()
                pg.wait_for_timeout(200)
            if pg.locator("#db .arw").count():
                # Le centre du groupe tombe souvent dans le vide du contour : on clique le numéro.
                num = pg.locator("#db .arw text")
                (num.first if num.count() else pg.locator("#db .les button").first).click(force=True)
                pg.wait_for_timeout(200)
                if pg.locator("#db .les .detail:not([hidden])").count() < 1:
                    pg.locator("#db .les button").first.click()
                    pg.wait_for_timeout(200)
                if not pg.locator("#db .bub:not(.compact)").count():
                    errors.append(f"{mid}: clic sur le numéro sans bulle")
                else:
                    fit = pg.evaluate("""() => {
                      const bub = document.querySelector('#db .bub.sheet');
                      const box = document.querySelector('#db .panel.p');
                      if (!bub || !box) return null;
                      const a = bub.getBoundingClientRect(), f = box.getBoundingClientRect();
                      const cut = bub.scrollWidth > bub.clientWidth + 2 || bub.scrollHeight > bub.clientHeight + 2;
                      const txt = bub.innerText || "";
                      return {ok: a.left >= f.left - 1 && a.right <= f.right + 1 && a.top >= f.top - 1 && a.bottom <= f.bottom + 1 && !cut && txt.includes("Confiance"),
                              L: Math.round(a.left - f.left), R: Math.round(f.right - a.right),
                              T: Math.round(a.top - f.top), B: Math.round(f.bottom - a.bottom), cut};
                    }""")
                    if not fit or not fit["ok"]:
                        errors.append(f"{mid}: bulle hors du panneau ou texte coupé {fit}")
                    txt = pg.locator("#db .bub:not(.compact)").first.inner_text()
                    if "Définition" not in txt:
                        errors.append(f"{mid}: bulle sans définition radiologique")
                if pg.locator("#db .panel.p svg polyline").count() < 1:
                    errors.append(f"{mid}: contour pointillé absent")
                det = pg.locator("#db .les .detail:not([hidden])")
                if det.count() < 1 or "Définition" not in det.first.inner_text():
                    errors.append(f"{mid}: le numéro n'ouvre ni le nom ni la définition")
                # Bande et définition ouvertes, avant le mode « tous les noms ».
                pg.locator("#db .bub.sheet").scroll_into_view_if_needed()
                pg.wait_for_timeout(100)
                snap(mid + "_bulles")
                if i == 0 and pg.locator("#bNames").is_enabled():
                    pg.click("#bNames"); pg.wait_for_timeout(150)
                    snap(mid + "_noms")
                if i == 0 and pg.locator("#bDefi").is_enabled():
                    pg.click("#bDefi")
                    pg.wait_for_timeout(200)
                    pt = pg.evaluate(
                        """(id) => {
                          const row = DATA.rows.find(r => r.id === id);
                          const a = row && row.m && row.m.patho && row.m.patho.arrows && row.m.patho.arrows[0];
                          const img = document.querySelector('#db .panel.p img');
                          if (!a || !img) return null;
                          const b = img.getBoundingClientRect();
                          return {x: b.left + a.tip[0] * b.width, y: b.top + a.tip[1] * b.height};
                        }""",
                        mid,
                    )
                    if not pt:
                        errors.append(f"{mid}: défi sans pointe cliquable")
                    else:
                        pg.mouse.click(pt["x"], pt["y"])
                        pg.wait_for_timeout(150)
                        pg.click("#bNote")
                        pg.wait_for_timeout(250)
                        sc = pg.locator("#score").inner_text() if pg.locator("#score").count() else ""
                        if "Score" not in sc:
                            errors.append(f"{mid}: mode défi sans score ({sc!r})")
                        elif sc.startswith("Score 0"):
                            errors.append(f"{mid}: clic sur la lésion non compté ({sc!r})")
                        snap(mid + "_defi")
                pg.mouse.click(5, 5)  # overlay click closes? -> no, it's header area of dlg/ov
            pg.keyboard.press("Escape"); pg.keyboard.press("Escape"); pg.wait_for_timeout(100)
            if pg.evaluate("document.querySelector('#ov').classList.contains('on')"):
                pg.keyboard.press("Escape")
        # keyboard/a11y sanity
        pg.focus("#tb button"); pg.keyboard.press("Enter"); pg.wait_for_timeout(200)
        if not pg.evaluate("document.querySelector('#ov').classList.contains('on')"):
            errors.append("Entrée sur une ligne n'ouvre pas la fenêtre")
        pg.keyboard.press("Escape")
        m = b.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=2, has_touch=True, is_mobile=True)
        m.on("pageerror", lambda e: errors.append(f"mobile pageerror: {e}"))
        m.on("console", lambda x: errors.append(f"mobile console.{x.type}: {x.text}") if x.type == "error" else None)
        m.goto(url); m.wait_for_timeout(300)
        f = os.path.join(shots, f"{tag}_mobile_list.png"); m.screenshot(path=f); made.append(f)
        if ids:
            m.evaluate(f"RP.open('{ids[0]}')"); m.wait_for_timeout(400)
            ow = m.evaluate("document.documentElement.scrollWidth")
            if ow > 392: errors.append(f"mobile: débordement horizontal {ow}px")
            mr = m.locator("#bHide")
            if mr.count() and mr.is_enabled() and "Révéler" in mr.inner_text():
                mr.tap()
                m.wait_for_timeout(200)
            if m.locator("#db .arw").count():
                m.locator("#db .arw").first.tap(force=True); m.wait_for_timeout(200)
                if m.locator("#db .les button").count() and m.locator("#db .bub:not(.compact)").count() < 1:
                    m.locator("#db .les button").first.tap()
                    m.wait_for_timeout(200)
                m.locator("#db .bub.sheet").scroll_into_view_if_needed()
                m.wait_for_timeout(150)
                fit = m.evaluate("""() => {
                  const bub = document.querySelector('#db .bub.sheet');
                  const box = document.querySelector('#db .panel.p');
                  if (!bub || !box) return null;
                  const a = bub.getBoundingClientRect(), f = box.getBoundingClientRect();
                  const cut = bub.scrollWidth > bub.clientWidth + 2 || bub.scrollHeight > bub.clientHeight + 2;
                  const txt = bub.innerText || "";
                  return {ok: a.left >= f.left - 1 && a.right <= f.right + 1 && a.width > 40 && !cut && txt.includes("Confiance"),
                          w: Math.round(a.width), cut};
                }""")
                if not fit or not fit["ok"]:
                    errors.append(f"mobile {ids[0]}: bulle hors du panneau ou texte coupé {fit}")
            f = os.path.join(shots, f"{tag}_mobile_{ids[0]}.png"); m.screenshot(path=f, full_page=False); made.append(f)
            m.evaluate("document.querySelector('#db').scrollTop=9999"); m.wait_for_timeout(100)
            f = os.path.join(shots, f"{tag}_mobile_{ids[0]}_bas.png"); m.screenshot(path=f); made.append(f)
        b.close()
    for f in made: print(f)
    print("CONSOLE:", "OK (0 erreur)" if not errors else "\n  " + "\n  ".join(errors))
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
