"""QA automatisée (Playwright + Chromium) : chargement sans erreur console, partie complète,
ouverture automatique de la fiche sur erreur, journal persistant, captures des trois écrans.
Usage : python3 tests/qa.py   (depuis la racine du projet)"""
import pathlib, sys, json
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
URL = (ROOT / "index.html").as_uri()          # file:// : vérifie que le jeu tourne sans serveur
SHOTS = ROOT / "docs" / "screenshots"; SHOTS.mkdir(parents=True, exist_ok=True)
CHROME = "/usr/bin/google-chrome"
checks = []
def ok(name, cond, extra=""):
    checks.append((name, bool(cond), extra)); print(("PASS " if cond else "FAIL ") + name, extra)

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME, headless=True)
    ctx = b.new_context(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
    pg = ctx.new_page()
    errors = []
    pg.on("console", lambda m: errors.append(m.text) if m.type in ("error", "warning") else None)
    pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.goto(URL); pg.wait_for_load_state("load")
    ok("Accueil affiché", pg.locator("#btn-commencer").is_visible())
    pg.click("#btn-commencer")
    hand = lambda: pg.locator(".main .carte").evaluate_all("els => els.map(e => e.dataset.id)")
    def play(cid):
        pg.click(f'.main .carte[data-id="{cid}"] .carte-action'); pg.wait_for_timeout(650)
    def fiche_title(): return pg.locator("#fiche-titre").inner_text() if pg.locator("#fiche").evaluate("d => d.open") else None

    # Duel 1 – erreur volontaire : aspirine avant exclusion de la dissection
    ok("Duel 1 = dissection", "dissection" in pg.locator(".arene-tete h2").inner_text().lower())
    ok("ECG en attente au départ", "ECG en attente" in pg.locator('[data-examen="ecg"]').inner_text())
    play("aspirine")
    ok("Erreur ouvre la fiche Dissection", fiche_title() == "Dissection aortique aiguë", str(fiche_title()))
    ok("Fiche montre le contexte d’erreur", pg.locator(".fiche-erreur").count() == 1)
    ok("Fiche cite une source suisse", pg.locator(".fiche-sources .tag-suisse").count() >= 1)
    ok("Badge À vérifier visible dans la fiche", pg.locator("#fiche .badge-verif").count() >= 1)
    corps = pg.locator("#fiche-corps").inner_text()
    ok("Fiche dissection : pas de baisse de TA si hypotension/bradycardie", "tu ne baisses pas la TA" in corps and "tamponnade" in corps)
    ok("Fiche : KSSG étiqueté hôpital cantonal", "hôpital cantonal" in corps)
    pg.screenshot(path=str(SHOTS / "02-fiche.png"))
    pg.keyboard.press("Escape"); pg.wait_for_timeout(200)
    ok("Fiche fermée par Échap", not pg.locator("#fiche").evaluate("d => d.open"))
    anim = pg.locator(".jouees .carte").last.evaluate("e => [e.className, getComputedStyle(e).animationName]")
    ok("Carte jouée : retournement + flash rouge", "anim-joue" in anim[0] and "verdict--erreur" in anim[0] and "joue-flip" in anim[1], str(anim))
    ok("PV diminués (70)", pg.locator('[data-testid="pv"]').inner_text().startswith("70"))
    play("ecg")
    ok("ECG révélé", "Sus-décalage" in pg.locator('[data-examen="ecg"]').inner_text())
    pg.evaluate("window.scrollTo(0, 0)"); pg.wait_for_timeout(100)
    pg.screenshot(path=str(SHOTS / "01-plateau.png"), full_page=True)
    play("angio-ct")
    ok("Duel 1 gagné", pg.locator("#btn-suivant").is_visible())
    ok("Dossier : angio-CT négatif avant le duel 2", "Négatif : pas de dissection" in pg.locator('[data-examen="ct"]').inner_text())
    pg.click("#btn-suivant"); pg.wait_for_timeout(500)
    ok("Duel 2 : rappel coronaire droite / STEMI inférieur", "coronaire droite" in pg.locator("#vue-plateau").inner_text())
    # Duel 2 – diagnostic, au clavier (touche du raccourci)
    idx = hand().index("stemi") + 1
    pg.keyboard.press(str(idx)); pg.wait_for_timeout(600)
    ok("Duel 2 gagné au clavier", pg.locator("#btn-suivant").is_visible())
    pg.click("#btn-suivant"); pg.wait_for_timeout(500)
    # Duel 3 – nitrés = erreur, puis dérivations droites
    play("nitres")
    ok("Erreur nitrés ouvre la fiche Nitrés", fiche_title() == "Dérivés nitrés", str(fiche_title()))
    pg.click("#fiche-fermer"); pg.wait_for_timeout(200)
    play("derivations-droites")
    ok("V4R révélé", "V4R" in pg.locator('[data-examen="v4r"]').inner_text())
    pg.click("#btn-suivant"); pg.wait_for_timeout(500)
    # Duel 4 – reperfusion
    for cid in ["aspirine", "hnf", "icp"]: play(cid)
    ok("Cas résolu", pg.locator(".debrief--ok").is_visible())
    pg.evaluate("window.scrollTo(0, 0)")
    pg.screenshot(path=str(SHOTS / "01b-plateau-fin.png"), full_page=True)

    # Journal
    pg.click("#onglet-journal"); pg.wait_for_timeout(300)
    n_err = pg.locator(".erreurs li").count()
    ok("Journal : 2 erreurs listées", n_err == 2, str(n_err))
    pct = pg.locator('[data-systeme="cardio"] .systeme-pct').inner_text()
    ok("Journal : précision cardio calculée", pct.endswith("%"), pct)
    pg.locator(".erreurs .btn-lien").first.click(); pg.wait_for_timeout(300)
    ok("Lien du journal ouvre une fiche", fiche_title() is not None, str(fiche_title()))
    pg.keyboard.press("Escape")
    pg.reload(); pg.wait_for_load_state("load"); pg.wait_for_timeout(300)
    ok("Journal persistant après rechargement", pg.locator(".erreurs li").count() == 2)
    pg.screenshot(path=str(SHOTS / "03-journal.png"), full_page=True)

    # Collection
    pg.click("#onglet-collection"); pg.wait_for_timeout(300)
    n_cards = pg.locator("#vue-collection .carte").count()
    ok("Collection : ≥ 10 cartes", n_cards >= 10, str(n_cards))
    pg.screenshot(path=str(SHOTS / "04-collection.png"), full_page=True)

    # Drapeau « système faible » : 1 bon, 3 erreurs => faible
    weak = pg.evaluate("""() => { const J = JEU.journal; J.reset();
      J.enregistrerCoup({systeme:'cardio',verdict:'bon'}); for (let i=0;i<3;i++) J.enregistrerCoup({systeme:'cardio',verdict:'erreur',fiche:'nitres',carte:'nitres',etape:'e3-ventricule-droit',msg:'test'});
      const st = J.stats('cardio'); return st.faible; }""")
    pg.click("#onglet-collection"); pg.click("#onglet-journal"); pg.wait_for_timeout(200)
    ok("Système faible signalé (< 70 %)", weak and pg.locator('[data-systeme="cardio"] .tag-faible').count() == 1)

    # Réinitialisation
    pg.click("#onglet-journal"); pg.click("#btn-reset"); pg.click("#confirm-oui"); pg.wait_for_timeout(200)
    ok("Reset efface le journal", pg.locator(".erreurs li").count() == 0)

    # Données : aucune posologie, chaque carte avec une source suisse ?
    info = pg.evaluate("""() => ({
      probs: JEU.registry.validate(),
      noSwiss: JEU.registry.cards().filter(c => !JEU.registry.hasSwissSource(c)).map(c => c.id),
      doses: JEU.registry.cards().filter(c => c.posologie).map(c => c.id) })""")
    ok("Données cohérentes", not info["probs"], json.dumps(info["probs"]))
    ok("Chaque fiche cite une source suisse", not info["noSwiss"], json.dumps(info["noSwiss"]))
    ok("Aucune posologie affichée", not info["doses"])

    # Tablette
    tab = b.new_page(viewport={"width": 820, "height": 1180}); tab.goto(URL); tab.click("#btn-commencer"); tab.wait_for_timeout(700); tab.evaluate("document.activeElement.blur(); window.scrollTo(0,0)"); tab.wait_for_timeout(100)
    tab.screenshot(path=str(SHOTS / "05-tablette.png"), full_page=True)
    ok("Pas de défilement horizontal en tablette", tab.evaluate("document.documentElement.scrollWidth <= window.innerWidth"))

    # Mouvement réduit
    rm = b.new_context(reduced_motion="reduce").new_page(); rm.goto(URL); rm.click("#btn-commencer")
    d = rm.locator(".main .carte").first.evaluate("e => getComputedStyle(e).animationDuration")
    ok("prefers-reduced-motion respecté", d in ("1e-06s", "0.001s", "0s", "1ms") or rm.locator(".main .carte").first.evaluate("e => getComputedStyle(e).animationName") == "none", d)
    rm.click('.main .carte[data-id="ecg"] .carte-action'); rm.wait_for_timeout(300)
    an = rm.locator(".jouees .carte").last.evaluate("e => [e.className, getComputedStyle(e).animationName]")
    ok("Mouvement réduit : carte jouée sans retournement, couleur statique", an[1] == "none" and "verdict--bon" in an[0], str(an))

    ok("Aucune erreur/avertissement console", not errors, json.dumps(errors))
    b.close()

failed = [c for c in checks if not c[1]]
print(f"\n{len(checks) - len(failed)}/{len(checks)} contrôles réussis")
sys.exit(1 if failed else 0)
