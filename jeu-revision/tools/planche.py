"""Générateur de planche par spécialité : planches/<specialite>.html.
Quatre captures réelles du jeu (parcours, duel, fiche, tableau de bord) + couverture
(pathologies couvertes / partielles / manquantes, taux « À vérifier », SSP touchées).
Usage (depuis jeu-revision/) : node tools/couverture.js && python3 tools/planche.py cardiologie
Pré-requis : Playwright Python et Chrome (/usr/bin/google-chrome)."""
import sys, json, html, pathlib, datetime
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
SP = sys.argv[1] if len(sys.argv) > 1 else "cardiologie"
COUV = json.loads((ROOT / "docs" / "couverture" / "couverture.json").read_text())
spc = next((s for s in COUV["specialites"] if s["id"] == SP), None)
if not spc or "totaux" not in spc: sys.exit(f"Spécialité « {SP} » sans données : lance d’abord node tools/couverture.js")
OUT = ROOT / "planches"; IMG = OUT / "img"; IMG.mkdir(parents=True, exist_ok=True)

def captures():
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome", headless=True)
        pg = b.new_page(viewport={"width": 1366, "height": 900})
        errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto((ROOT / "index.html").as_uri()); pg.wait_for_timeout(300)
        pg.evaluate("localStorage.clear(); localStorage.setItem('revmed.son','off')"); pg.reload(); pg.wait_for_timeout(300)
        blur = lambda: pg.evaluate("document.activeElement && document.activeElement.blur(); window.scrollTo(0,0)")
        sel = f'.salle[data-specialite="{SP}"]'
        pg.locator(sel).scroll_into_view_if_needed(); pg.wait_for_timeout(100)
        pg.locator(sel).screenshot(path=str(IMG / f"{SP}-parcours.png"))
        cas = pg.locator(f'{sel} [data-cas]')
        if cas.count():
            cas.first.click(); pg.wait_for_timeout(500)
            main = pg.evaluate("JEU.ui.board.etat().duel.main")
            et = pg.evaluate("JEU.ui.board.etat().duel.etape")
            juste = next((c for c in main if (et["regles"].get(c) or {}).get("verdict") == "bon"), None)
            faux = next((c for c in main if (et["regles"].get(c) or {}).get("verdict") == "erreur"), None)
            if juste: pg.click(f'.main .carte[data-id="{juste}"] .carte-action'); pg.keyboard.press("s"); pg.wait_for_timeout(600)
            if faux:
                pg.click(f'.main .carte[data-id="{faux}"] .carte-action'); pg.wait_for_timeout(100)
                pg.evaluate("window.scrollTo(0,0)"); pg.screenshot(path=str(IMG / f"{SP}-duel.png"), full_page=True)
                pg.keyboard.press("s"); pg.wait_for_timeout(700)
                pg.locator("#fiche-corps").evaluate("e => e.scrollTop = e.scrollHeight * 0.3")
                pg.screenshot(path=str(IMG / f"{SP}-fiche.png")); pg.keyboard.press("Escape")
        pg.click("#onglet-tableau"); pg.wait_for_timeout(300); blur()
        pg.screenshot(path=str(IMG / f"{SP}-tableau.png"))
        b.close()
        if errs: sys.exit("Erreurs de page : " + "; ".join(errs))

captures()
t = spc["totaux"]; e = html.escape
etiquette = {"couverte": "Couverte", "partielle": "Partielle", "manquante": "Manquante"}
lignes = "".join(
    f'<tr class="st-{p["statut"]}"><td>{e(p["nom"])}</td><td>{etiquette[p["statut"]]}</td>'
    f'<td>{p["cas"]["urgence"]} / {p["cas"]["consultation"]} / {p["cas"]["final"]}</td>'
    f'<td>{", ".join(map(str, p["echelonsSources"])) or "—"}</td><td>{e(", ".join(p["besoins"])) or "—"}</td>'
    f'<td>{e(", ".join(p["ssp"]))}</td></tr>' for p in spc["pathologies"])
imgs = [(n, l) for n, l in [("parcours", "Parcours : la salle et son cycle"), ("duel", "Duel : carte choisie, confiance à donner"), ("fiche", "Fiche en 8 rubriques"), ("tableau", "Tableau de bord")] if (IMG / f"{SP}-{n}.png").exists()]
figs = "".join(f'<figure><img src="img/{SP}-{n}.png" alt="{e(l)}" loading="lazy"><figcaption>{e(l)}</figcaption></figure>' for n, l in imgs)
date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
page = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Planche · {e(spc["nom"])}</title><style>
body{{font:16px/1.45 system-ui,-apple-system,"Segoe UI",sans-serif;color:#14202e;background:#f5f6f8;margin:0}}
main{{max-width:1180px;margin:0 auto;padding:28px 22px 48px}} h1{{margin:.1em 0}} .sur{{text-transform:uppercase;letter-spacing:.06em;font-size:.78rem;color:#4a5868;font-weight:700}}
.chiffres{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:18px 0}} .chiffres div{{background:#fff;border:1px solid #d9dee5;border-radius:10px;padding:12px}}
.chiffres b{{display:block;font-size:1.6rem}} .grille{{display:grid;grid-template-columns:repeat(auto-fit,minmax(460px,1fr));gap:16px}}
figure{{margin:0;background:#fff;border:1px solid #d9dee5;border-radius:10px;padding:10px}} figure img{{width:100%;height:auto;border-radius:6px;display:block}} figcaption{{font-size:.88rem;color:#4a5868;margin-top:6px}}
table{{width:100%;border-collapse:collapse;background:#fff;border:1px solid #d9dee5;font-size:.9rem}} th,td{{text-align:left;padding:7px 9px;border-bottom:1px solid #e6e9ee;vertical-align:top}}
.st-couverte td:nth-child(2){{color:#1d6b3a;font-weight:700}} .st-partielle td:nth-child(2){{color:#8a4b00;font-weight:700}} .st-manquante td:nth-child(2){{color:#b3261e;font-weight:700}}
.note{{color:#4a5868;font-size:.88rem}} @media (max-width:560px){{.grille{{grid-template-columns:1fr}}}}
</style></head><body><main>
<p class="sur">Planche · lot {e(spc["lot"])} · générée le {date}</p><h1>{e(spc["nom"])}</h1>
<p class="note">{e(spc.get("note") or "")} Statut du catalogue : {e(spc["statut"])}.</p>
<div class="chiffres"><div><b>{t["pathologies"]}</b>pathologies au catalogue</div><div><b>{t["couvertes"]}</b>couvertes</div><div><b>{t["partielles"]}</b>partielles</div>
<div><b>{t["manquantes"]}</b>manquantes</div><div><b>{t["cas"]}</b>cas · {t["cartes"]} cartes</div><div><b>{t["tauxAVerifier"]} %</b>« À vérifier » ({t["aVerifier"]}/{t["affirmations"]})</div></div>
<h2>Le jeu</h2><div class="grille">{figs}</div>
<h2>Couverture</h2><table><thead><tr><th>Pathologie</th><th>Statut</th><th>Cas U / C / final</th><th>Échelons sourcés</th><th>Il manque</th><th>SSP PROFILES</th></tr></thead><tbody>{lignes}</tbody></table>
<p class="note">Couverte : cas exigés présents et 7 échelons sourcés (source suisse hors fondamentaux). Partielle : au moins un cas, exigences incomplètes. Manquante : aucun cas.
Toute pathologie fréquente ou grave exige un cas Urgence et un cas Consultation. SSP touchées : {len(spc["sspTouchees"])} sur {COUV["profiles"]["total"] if isinstance(COUV.get("profiles"), dict) and "total" in COUV["profiles"] else 248}.
Liste officielle des SSP : <a href="https://smifk-cims.ch/profiles-2023/ssps">smifk-cims.ch</a>. Contenu pédagogique, pas un protocole ; relecture médicale : Dr Vial Djoukang.</p>
</main></body></html>"""
(OUT / f"{SP}.html").write_text(page)
print(f"planches/{SP}.html écrite ({len(imgs)} captures)")
