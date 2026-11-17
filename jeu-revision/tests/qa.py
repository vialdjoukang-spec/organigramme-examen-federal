"""QA navigateur (Playwright + Chrome, file://) du moteur v2 : parcours, confiance, règles, chrono,
étoiles, fiche en 8 rubriques, Ronde, Fondamentaux, tableau de bord, export/import, déblocage,
examen blanc, son, accessibilité clavier, mouvement réduit, absence d’erreur console.
Usage : python3 tests/qa.py   (depuis jeu-revision/)"""
import pathlib, sys, json, re
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
URL = (ROOT / "index.html").as_uri()
SHOTS = ROOT / "docs" / "screenshots"; SHOTS.mkdir(parents=True, exist_ok=True)
CHROME = "/usr/bin/google-chrome"
checks = []
def ok(name, cond, extra=""):
    checks.append((name, bool(cond), extra)); print(("PASS " if cond else "FAIL ") + name, extra)

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME, headless=True)
    ctx = b.new_context(viewport={"width": 1440, "height": 1000}, accept_downloads=True)
    pg = ctx.new_page()
    errors = []
    pg.on("console", lambda m: errors.append(m.text) if m.type in ("error", "warning") else None)
    pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.goto(URL); pg.wait_for_load_state("load"); pg.wait_for_timeout(300)
    top = lambda: pg.evaluate("window.scrollTo(0,0); document.activeElement && document.activeElement.blur()")
    fiche_titre = lambda: pg.locator("#fiche-titre").inner_text() if pg.locator("#fiche").evaluate("d => d.open") else None
    def choisir(cid): pg.click(f'.main .carte[data-id="{cid}"] .carte-action'); pg.wait_for_timeout(80)
    def jouer(cid, conf="s"): choisir(cid); pg.keyboard.press(conf); pg.wait_for_timeout(650)
    def fermer():
        if pg.locator("#fiche").evaluate("d => d.open"): pg.keyboard.press("Escape"); pg.wait_for_timeout(150)

    # 1. Parcours
    ok("Parcours affiché par défaut", pg.locator("#vue-parcours").is_visible() and "Fais le tour" in pg.locator("#parcours-titre").inner_text())
    ok("Grade initial : Externe", pg.locator("#grade").inner_text() == "Externe")
    ok("Salle cardiologie ouverte", pg.locator('.salle[data-specialite="cardiologie"]').get_attribute("class").find("salle--ouverte") >= 0)
    ok("Cycle en 4 étapes visible", pg.locator('.salle[data-specialite="cardiologie"] .pas').count() == 4)
    ok("41 salles du plan, 40 en préparation", pg.locator(".salle").count() == 41 and pg.locator(".salle--preparation").count() == 40)
    ok("Examen blanc PROFILES présent", pg.locator("#btn-examen-blanc").is_visible())
    top(); pg.screenshot(path=str(SHOTS / "06-parcours.png"), full_page=True)

    # 2. Règles et son
    pg.click("#onglet-regles"); pg.wait_for_timeout(150)
    txt = pg.locator("#vue-regles").inner_text()
    ok("Règles : pénalités 30 / 10 / 5 PV + 1 min", all(x in txt for x in ["30 PV", "10 PV", "5 PV et 1 minute"]))
    ok("Règles : Leitner 5 boîtes, grades, maîtrise J+1/J+7", "boîte 5 = J+30" in txt and "Médecin cadre" in txt and "J+7" in txt)
    pg.screenshot(path=str(SHOTS / "10-regles.png"), full_page=True)
    avant = pg.evaluate("JEU.son.actif()")
    pg.click("#btn-son"); pg.wait_for_timeout(50)
    ok("Bouton muet : bascule et mémorise", pg.evaluate("JEU.son.actif()") != avant and pg.evaluate("localStorage.getItem('revmed.son')") in ("on", "off"))
    if not pg.evaluate("JEU.son.actif()"): pg.click("#btn-son")
    ok("Son activé : sons synthétisés (Web Audio, aucun fichier)", pg.evaluate("JEU.son.SONS.join(',')") == "bip,valide,alerte,victoire,etoile" and pg.locator("audio").count() == 0)

    # 3. Urgence : duel 1
    pg.click("#onglet-parcours"); pg.wait_for_timeout(150)
    pg.click('.salle[data-specialite="cardiologie"] .pas[data-pas="urgence"] [data-cas]'); pg.wait_for_timeout(700)
    ok("Plateau : mode Urgence et chrono", "Urgence" in pg.locator(".tag-mode").text_content() and re.match(r"\d\d:\d\d", pg.locator("#chrono").inner_text()))
    ok("Duel 1 = dissection, phase « trier », échelon 3", "dissection" in pg.locator(".arene-tete h2").inner_text().lower() and "Échelon 3" in pg.locator("#vue-plateau .phase").text_content())
    choisir("aspirine")
    conf_ok = pg.locator("#confiance").is_visible()
    ok("Choisir une carte ouvre la confiance sans jouer", conf_ok and pg.locator(".jouees .carte").count() == 0 and pg.locator('[data-testid="pv"]').inner_text().startswith("100"))
    ok("Aucune confiance présélectionnée (focus sur le groupe)", pg.evaluate("document.activeElement.id") == "confiance" and pg.locator(".btn-conf[aria-pressed='true']").count() == 0)
    pg.keyboard.press("Escape"); pg.wait_for_timeout(80)
    ok("Échap annule la sélection", pg.locator("#confiance").count() == 0)
    jouer("aspirine", "s")
    ok("Erreur ouvre la fiche Dissection", fiche_titre() == "Dissection aortique aiguë", str(fiche_titre()))
    ok("Fiche : 8 rubriques dans l’ordre", pg.locator("#fiche [data-rubrique]").evaluate_all("e => e.map(x => x.dataset.rubrique).join(',')") == "fondamentaux,demarche,differentiels,exploration,diagnostic,priseEnCharge,suivi,explication")
    corps = pg.locator("#fiche-corps").inner_text()
    ok("Fiche : différentiel qui tue marqué", pg.locator("#fiche .tag-tue").count() >= 1)
    ok("Fiche : explications de coups tirées du cas", pg.locator("#fiche .fiche-coups li").count() >= 3)
    ok("Fiche : hypotension/bradycardie → pas de baisse de TA", "tu ne baisses pas la TA" in corps and "tamponnade" in corps)
    ok("Fiche : KSSG = hôpital cantonal, complémentaire", "hôpital cantonal · complémentaire" in corps)
    ok("Fiche : badge À vérifier et source suisse", pg.locator("#fiche .badge-verif").count() >= 1 and pg.locator("#fiche .tag-suisse").count() >= 1)
    pg.screenshot(path=str(SHOTS / "02-fiche.png"))
    pg.locator("#fiche-corps").evaluate("e => e.scrollTop = e.scrollHeight * 0.45"); pg.wait_for_timeout(100)
    pg.screenshot(path=str(SHOTS / "08-fiche-8-rubriques.png"))
    fermer()
    ok("Fiche fermée par Échap", not pg.locator("#fiche").evaluate("d => d.open"))
    anim = pg.locator(".jouees .carte").last.evaluate("e => [e.className, getComputedStyle(e).animationName]")
    ok("Carte jouée : retournement + flash rouge", "anim-joue" in anim[0] and "verdict--erreur" in anim[0] and "joue-flip" in anim[1], str(anim))
    ok("Erreur dangereuse : −30 PV (70)", pg.locator('[data-testid="pv"]').inner_text().startswith("70"))
    idx = pg.evaluate("JEU.ui.board.etat().duel.main.indexOf('ecg')") + 1
    pg.keyboard.press(str(idx)); pg.wait_for_timeout(80); pg.keyboard.press("h"); pg.wait_for_timeout(650)
    ok("Clavier : chiffre puis H joue l’ECG", "Sus-décalage" in pg.locator('[data-examen="ecg"]').inner_text())
    top(); pg.screenshot(path=str(SHOTS / "01-plateau.png"), full_page=True)
    choisir("angio-ct"); pg.click(".btn-conf--hasard"); pg.wait_for_timeout(650)
    ok("Bouton « Au hasard » valide le coup", pg.locator("#btn-suivant").is_visible())
    ok("Dossier : angio-CT négatif avant le duel 2", "Négatif : pas de dissection" in pg.locator('[data-examen="ct"]').inner_text())
    pg.click("#btn-suivant"); pg.wait_for_timeout(500)
    ok("Duel 2 : rappel coronaire droite / STEMI inférieur", "coronaire droite" in pg.locator("#vue-plateau").inner_text())
    idx = pg.evaluate("JEU.ui.board.etat().duel.main.indexOf('stemi')") + 1
    pg.keyboard.press(str(idx)); pg.keyboard.press("s"); pg.wait_for_timeout(650)
    ok("Duel 2 gagné au clavier", pg.locator("#btn-suivant").is_visible())
    pg.click("#btn-suivant"); pg.wait_for_timeout(500)
    # Duel 3 : examen inutile, puis erreur nitrés
    jouer("troponine", "h")
    ok("Examen inutile : −5 PV et +1 min", pg.locator('[data-testid="pv"]').inner_text().startswith("65") and "+1 min" in pg.locator("#feedback").inner_text())
    fermer(); top(); pg.screenshot(path=str(SHOTS / "07-duel-urgence.png"), full_page=True)
    jouer("nitres", "s")
    ok("Erreur nitrés ouvre la fiche Nitrés", fiche_titre() == "Dérivés nitrés", str(fiche_titre()))
    pg.click("#fiche-fermer"); pg.wait_for_timeout(150)
    jouer("derivations-droites", "s")
    ok("V4R révélé", "V4R" in pg.locator('[data-examen="v4r"]').inner_text())
    pg.click("#btn-suivant"); pg.wait_for_timeout(500)
    for cid in ["aspirine", "hnf", "icp"]: jouer(cid, "s")
    ok("Cas résolu, étoiles affichées", pg.locator(".debrief--ok").is_visible() and pg.locator(".etoiles").get_attribute("data-etoiles") == "1")
    ok("Sons joués : alerte, valide, victoire", all(x in pg.evaluate("JEU.son.trace.map(t => t.nom).join(',')") for x in ["alerte", "valide", "victoire"]))
    top(); pg.screenshot(path=str(SHOTS / "01b-plateau-fin.png"), full_page=True)
    coups = pg.evaluate("JEU.progression.get().coups")
    ok("Chaque coup enregistré avec échelon, confiance, temps, gravité", len(coups) == 10 and all(c.get("ech") and c.get("conf") and c.get("ms", 0) > 0 for c in coups) and any(c.get("g") == "dangereuse" for c in coups), str(len(coups)))

    # 4. Tableau de bord
    pg.click("#onglet-tableau"); pg.wait_for_timeout(300)
    ok("Carte de chaleur : ligne cardiologie × 7 échelons", pg.locator('#tb-chaleur tr[data-specialite="cardiologie"] td').count() == 7)
    ok("Calibration : 3 niveaux", pg.locator("#tb-calibration tr[data-conf]").count() == 3 and pg.locator('#tb-calibration tr[data-conf="sur"] td').first.inner_text() == "7")
    am = pg.locator("#tb-angles li").count()
    ok("Angles morts : erreurs « sûr » listées (aspirine, nitrés)", am >= 2 and pg.locator('#tb-angles li[data-carte="nitres"]').count() == 1, str(am))
    ok("Vitesse et objectif Urgence 20 s", "objectif < 20 s" in pg.locator("#vitesse-urgence").inner_text())
    ok("Leitner : 5 boîtes", pg.locator("#tb-leitner li").count() == 5)
    ok("Préparation par domaine PROFILES", pg.locator("#tb-preparation tr[data-domaine]").count() == 19)
    pg.locator("#tb-angles .btn-lien").first.click(); pg.wait_for_timeout(250)
    ok("Angle mort : lien vers la fiche", fiche_titre() is not None, str(fiche_titre()))
    fermer()
    top(); pg.screenshot(path=str(SHOTS / "03-tableau.png"), full_page=True)
    pg.reload(); pg.wait_for_load_state("load"); pg.wait_for_timeout(300)
    ok("Progression persistante après rechargement", pg.evaluate("JEU.progression.get().coups.length") == 10)

    # 5. Export / import
    pg.click("#onglet-tableau"); pg.wait_for_timeout(200)
    with pg.expect_download() as dl: pg.click("#btn-export")
    data = json.loads(pathlib.Path(dl.value.path()).read_text())
    ok("Export JSON : schéma et version", data["schema"] == "revmed.progression" and data["version"] == 2 and len(data["coups"]) == 10)
    export_path = str(dl.value.path())
    pg.click("#btn-reset"); pg.click("#confirm-oui"); pg.wait_for_timeout(200)
    ok("Tout effacer vide la progression", pg.evaluate("JEU.progression.get().coups.length") == 0)
    pg.set_input_files("#fichier-import", export_path); pg.wait_for_timeout(400)
    ok("Import : restaure sans perte", pg.evaluate("JEU.progression.get().coups.length") == 10 and "Import réussi" in pg.locator("#tb-message").inner_text())
    pg.set_input_files("#fichier-import", export_path); pg.wait_for_timeout(400)
    ok("Import répété : aucun doublon", pg.evaluate("JEU.progression.get().coups.length") == 10 and "0 élément" in pg.locator("#tb-message").inner_text())
    bad = ROOT / "docs" / "_bad.json"; bad.write_text('{"schema":"x"}')
    pg.set_input_files("#fichier-import", str(bad)); pg.wait_for_timeout(300); bad.unlink()
    ok("Import invalide refusé avec message", "Import refusé" in pg.locator("#tb-message").inner_text())

    # 6. Ronde (angles morts d’abord)
    pg.click("#btn-ronde"); pg.wait_for_timeout(300)
    ok("Ronde : 20 min, angle mort en premier", pg.locator("#ronde-chrono").inner_text() in ("20:00", "19:59") and "Angle mort" in pg.locator("#vue-quiz .tag-raison").first.text_content())
    pg.locator(".quiz-choix .choix").first.click(); pg.wait_for_timeout(80)
    ok("Ronde : réponse en attente de confiance", pg.locator("#confiance").is_visible() and pg.locator("#feedback").count() == 0)
    pg.keyboard.press("h"); pg.wait_for_timeout(200)
    ok("Ronde : retour et lien fiche", pg.locator("#feedback").is_visible() and pg.locator("#btn-q-suivante").is_visible())
    pg.screenshot(path=str(SHOTS / "09-ronde.png"), full_page=True)
    last = pg.evaluate("JEU.progression.get().coups.slice(-1)[0]")
    ok("Ronde : coup enregistré (src ronde, échelon, confiance)", last["src"] == "ronde" and last["conf"] == "hesitant" and 1 <= last["ech"] <= 7)

    # 7. Fondamentaux
    pg.click("#onglet-parcours"); pg.click("#btn-fond-cardiologie"); pg.wait_for_timeout(250)
    ok("Fondamentaux : échelons 1–2 seulement", re.search(r"Échelon [12]", pg.locator("#vue-quiz .tag-phase").text_content()) and pg.evaluate("JEU.ui.quiz.etat().file.every(q => q.ech <= 2)"))
    pg.keyboard.press("1"); pg.keyboard.press("s"); pg.wait_for_timeout(150)
    ok("Fondamentaux : clavier 1 puis S", pg.locator("#feedback").is_visible())

    # 8. Entraînement et déblocage
    pg.click("#onglet-parcours"); pg.wait_for_timeout(100)
    pg.evaluate("""() => { const c = JSON.parse(JSON.stringify(JEU.specialites[0])); c.id = 'angiologie'; c.nom = 'Angiologie';
      c.cartes.forEach(x => x.id = 'ang-' + x.id); c.pathologies.forEach(x => { x.id = 'ang-' + x.id; x.carte = 'ang-' + x.carte; });
      c.cas.forEach(k => { k.id = 'ang-' + k.id; k.pathologies = k.pathologies.map(x => 'ang-' + x); k.etapes.forEach(e => { e.pathologie = 'ang-' + e.pathologie; e.adversaire = 'ang-' + e.adversaire; e.main = e.main.map(x => 'ang-' + x); e.objectifs = e.objectifs.map(x => 'ang-' + x);
        e.regles = Object.fromEntries(Object.entries(e.regles).map(([k2, r]) => [ 'ang-' + k2, Object.assign(r, r.fiche ? { fiche: 'ang-' + r.fiche } : {}) ])); if (e.regles['ang-angio-ct'] && e.regles['ang-angio-ct'].avant) e.regles['ang-angio-ct'].avant.requiert = ['ang-ecg']; }); });
      JEU.specialites.push(c); JEU.registry.init(); JEU.quiz.reset(); JEU.progression.reset(); JEU.ui.parcours.render(); }""")
    ok("Déblocage : salle suivante verrouillée sous 2 étoiles", "salle--verrouillee" in pg.locator('.salle[data-specialite="angiologie"]').get_attribute("class"))
    pg.evaluate("JEU.progression.enregistrerPartie({cas:'douleur-thoracique-74', sp:'cardiologie', mode:'urgence', etoiles:2, pv:80, pvInitial:100, resultat:'victoire'}); JEU.ui.parcours.render()")
    ok("Déblocage : ouverte après 2 étoiles de moyenne", "salle--ouverte" in pg.locator('.salle[data-specialite="angiologie"]').get_attribute("class"))
    pg.evaluate("JEU.progression.reset(); JEU.ui.parcours.render()")
    pg.check("#chk-entrainement"); pg.wait_for_timeout(100)
    ok("Entraînement : toutes les salles avec contenu ouvertes", "salle--ouverte" in pg.locator('.salle[data-specialite="angiologie"]').get_attribute("class"))
    pg.click('.salle[data-specialite="cardiologie"] .pas[data-pas="urgence"] [data-cas]'); pg.wait_for_timeout(500)
    ok("Entraînement : sans chronomètre", "Entraînement" in pg.locator(".tag-mode").text_content() and pg.locator("#chrono").count() == 0)
    pg.click("#onglet-parcours"); pg.uncheck("#chk-entrainement")
    pg.reload(); pg.wait_for_load_state("load"); pg.wait_for_timeout(300)

    # 9. Examen blanc (structure)
    pg.click("#btn-examen-blanc"); pg.wait_for_timeout(500)
    ok("Examen blanc : plateau en mode examen", "Examen blanc" in pg.locator(".tag-mode").text_content())
    for seq in [["ecg", "angio-ct"], ["stemi"], ["derivations-droites"], ["aspirine", "hnf", "icp"]]:
        for cid in seq:
            i = pg.evaluate(f"JEU.ui.board.etat().duel.main.indexOf('{cid}')") + 1
            pg.keyboard.press(str(i)); pg.keyboard.press("s"); pg.wait_for_timeout(120)
        if pg.locator("#btn-suivant").count(): pg.click("#btn-suivant"); pg.wait_for_timeout(150)
    ok("Examen blanc : note et seuil « À vérifier »", "Score moyen : 100 %" in pg.locator("#examen-resultat").inner_text() and "À vérifier" in pg.locator("#examen-resultat").inner_text())

    # 10. Collection et données
    pg.click("#onglet-collection"); pg.wait_for_timeout(200)
    ok("Collection : ≥ 10 cartes", pg.locator("#vue-collection .carte").count() >= 10, str([pg.locator("#vue-collection .carte").count(), pg.evaluate("document.body.dataset.vue"), pg.locator("#vue-collection").inner_text()[:200]]))
    pg.screenshot(path=str(SHOTS / "04-collection.png"), full_page=True)
    info = pg.evaluate("""() => ({ probs: JEU.registry.validate(), noSwiss: JEU.registry.cards().filter(c => c.type === 'pathologie' && !JEU.registry.hasSwissSource(c)).map(c => c.id),
      doses: JEU.registry.cards().filter(c => c.posologie).map(c => c.id), q: JEU.quiz.toutes().length })""")
    ok("Validateur : 0 erreur sur les données chargées", not info["probs"], json.dumps(info["probs"])[:300])
    ok("Chaque pathologie cite une source suisse", not info["noSwiss"])
    ok("Aucune posologie", not info["doses"])
    ok("Questions sur l’échelle à 7 échelons générées", info["q"] >= 20, str(info["q"]))

    # 11. Tablette, mouvement réduit
    tab = b.new_page(viewport={"width": 820, "height": 1180}); tab.goto(URL); tab.wait_for_timeout(300)
    no_scroll = [tab.evaluate("document.documentElement.scrollWidth <= window.innerWidth")]
    tab.click("#onglet-plateau"); tab.click("#btn-commencer"); tab.wait_for_timeout(600); tab.evaluate("document.activeElement.blur(); window.scrollTo(0,0)")
    tab.screenshot(path=str(SHOTS / "05-tablette.png"), full_page=True)
    no_scroll.append(tab.evaluate("document.documentElement.scrollWidth <= window.innerWidth"))
    tab.click("#onglet-tableau"); tab.wait_for_timeout(200); no_scroll.append(tab.evaluate("document.documentElement.scrollWidth <= window.innerWidth"))
    ok("Tablette : pas de défilement horizontal (parcours, plateau, tableau)", all(no_scroll), str(no_scroll))
    rm = b.new_context(reduced_motion="reduce").new_page(); rm.goto(URL); rm.wait_for_timeout(200)
    ok("Mouvement réduit : son coupé par défaut", rm.evaluate("JEU.son.actif()") is False)
    rm.click("#onglet-plateau"); rm.click("#btn-commencer"); rm.wait_for_timeout(300)
    rm.click('.main .carte[data-id="ecg"] .carte-action'); rm.keyboard.press("s"); rm.wait_for_timeout(300)
    an = rm.locator(".jouees .carte").last.evaluate("e => [e.className, getComputedStyle(e).animationName]")
    ok("Mouvement réduit : carte jouée sans retournement", an[1] == "none" and "verdict--bon" in an[0], str(an))

    ok("Aucune erreur/avertissement console", not errors, json.dumps(errors)[:400])
    b.close()

failed = [c for c in checks if not c[1]]
print(f"\n{len(checks) - len(failed)}/{len(checks)} contrôles navigateur réussis")
sys.exit(1 if failed else 0)
