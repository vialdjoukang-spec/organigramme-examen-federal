"""Bilan de la nuit du 14.11.2026 (régénérable). Images intégrées en base64, réduites."""
import base64, io, json, html
from PIL import Image
E = html.escape
def img(p, w=900):
    im = Image.open(p).convert('RGB'); r = w / im.width
    if r < 1: im = im.resize((w, int(im.height * r)))
    b = io.BytesIO(); im.save(b, 'JPEG', quality=72)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
CAP = [('Imagerie : vrai cliché, repères numérotés', 'recensement/captures_v2/reel_IMG-003_patho.png'),
       ('Explorations : fenêtre ECG avec QTc calculé', 'recensement/captures_v2/B_fenetre_ECG_QTc.png'),
       ('Sémiologie : fiche syndrome', 'donnees/semiologie/captures/DSF2_syndrome_SY17.png'),
       ('Sémiologie : version CS en 13 minutes', 'donnees/semiologie/captures/DSF2_version_CS.png'),
       ('Physiopathologie : grille système × VITE DIT CAFé', 'donnees/fondamentales_v2/captures/DSF2_grille_physiopathologie.png'),
       ('Physiologie : formule et exemple résolu', 'donnees/fondamentales_v2/captures/DSF2_formule_exemple.png')]
LIGNES = [  # bloc, fiches, état, détail
 ('Imagerie : textes (examen de référence, autres, syndrome, traitement)', '344', 'audit-ok', '5 lots, 2 tours chacun'),
 ('Imagerie : clichés réels repérés', '314 pathologiques, dont 194 paires', 'audit-ok', '30 introuvables en libre, déclarés'),
 ('Explorations fonctionnelles : textes (lecture, valeurs normales, calculs)', '153', 'audit-ok', 'tracés réels : 82 posés (70 paires), audit-ok ; 28 introuvables en libre, déclarés'),
 ('Sémiologie : Status (examen par temps, manœuvres, version CS)', '35', 'audit-ok', '56 images réelles ; gestes manquants à photographier'),
 ('Sémiologie : Syndromes cliniques', '81', 'audit-ok', 'doses AIPS mot pour mot'),
 ('Sémiologie : Anamnèse (trame, spéciales, 60 motifs)', '68', 'audit-ok', 'axes ASSM, drapeaux rouges, ICE'),
 ('Sémiologie : Management et Communication', '35', 'audit-ok', '4 dimensions KK citées mot pour mot'),
 ('Sciences fondamentales : Physiopathologie', '108 (≈ 500 affections)', 'audit-ok', 'grille système × VITE DIT CAFé'),
 ('Sciences fondamentales : Physiologie', '88', 'audit-ok', 'formules avec exemples résolus'),
]
T = json.load(open('bilans/tokens_nuit.json'))
lig = ''.join(f'<tr><td>{E(a)}</td><td>{E(b)}</td><td class=ok>{E(c)}</td><td>{E(d)}</td></tr>' for a, b, c, d in LIGNES)
caps = ''.join(f'<figure><img src="{img(p)}" alt="{E(t)}"><figcaption>{E(t)}</figcaption></figure>' for t, p in CAP)
eco = T['sans_harnais'] - T['avec_harnais']
page = f"""<!doctype html><html lang=fr><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>Bilan de nuit</title>
<style>:root{{--n1:#bcd0f7;--n2:#f9dcae;--n3:#cfeedd}}body{{background:#fff;color:#000;font:16px/1.5 system-ui,sans-serif;margin:16px auto;max-width:1100px;padding:0 16px}}
h1{{background:var(--n1);padding:8px 12px;border-radius:6px}}h2{{background:var(--n2);padding:6px 12px;border-radius:6px;margin-top:28px}}
.w{{overflow-x:auto}}table{{border-collapse:collapse;width:100%}}th,td{{border-bottom:1px solid #ddd;padding:6px 8px;text-align:left;vertical-align:top}}th{{border-bottom:2px solid #000}}
td.ok{{background:var(--n3);font-weight:700}}.k{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px}}.k div{{border:1px solid #999;border-radius:8px;padding:10px}}.k b{{font-size:1.6em;display:block}}
figure{{margin:14px 0}}figure img{{max-width:100%;border:1px solid #999}}figcaption{{font-weight:700}}</style>
<h1>Bilan de la nuit — 14.11.2026, 02h00 → 08h00</h1>
<p>Toutes les fiches ci-dessous ont été rédigées, puis auditées par un agent médical indépendant, puis corrigées jusqu'au verdict « audit-ok » (2 à 3 tours). Les doses viennent de l'AIPS suisse lue mot pour mot ; toute source non suisse porte son étiquette.</p>
<h2>Ce qui est fait</h2><div class=w><table><tr><th>Bloc</th><th>Fiches</th><th>État</th><th>Détail</th></tr>{lig}</table></div>
<p><b>{T['audits']}</b> rapports d'audit écrits ; <b>{T['commits']}</b> commits poussés. Pages à ouvrir : <code>recensement/RECENSEMENT_TOPOSYSTEMIQUE.html</code>, <code>donnees/semiologie/SEMIOLOGIE.html</code>, <code>donnees/fondamentales_v2/SCIENCES_FONDAMENTALES.html</code>.</p>
<h2>Tokens économisés grâce au harnais</h2>
<div class=k><div><b>{T['avec_harnais']:.0f} M</b>coût réel des {T['agents']} agents lancés cette nuit (équivalent tokens d'entrée)</div>
<div><b>{T['sans_harnais']:.0f} M</b>coût du même travail sans réutilisation du cache</div>
<div><b>{eco:.0f} M</b>économisés, soit <b>{100*eco/T['sans_harnais']:.0f} %</b></div></div>
<p>Pourquoi : la plateforme facture le cache lu à 10 % ; le harnais en tire parti en relançant le même agent pour corriger ce qu'il a écrit (son contexte reste en cache) au lieu d'en créer un neuf ; les briefs sont partagés par fichier ; les tâches répétitives tournent en scripts gratuits (recherche d'images et de tracés, génération des pages, contrôle des phrases verbales, listes de besoins), sans modèle. Méthode : compteur gratuit <code>Claude/_harnais/suivi.py</code> (entrée ×1, cache écrit ×1,25, cache lu ×0,1, sortie ×5) ; le coût « sans harnais » compte chaque token de cache comme une entrée pleine. La boucle principale n'est pas incluse.</p>
<div class=w><table><tr><th>Type de travail</th><th>Agents</th><th>Coût (M éq.)</th></tr>{''.join(f'<tr><td>{E(k)}</td><td>{v[0]}</td><td>{v[1]}</td></tr>' for k, v in T['par_type'].items())}</table></div>
<h2>Décisions qui t'attendent</h2><ul>
<li><b>IMG-242</b> : le nom d'un patient (issu d'un article CC BY public) reste lisible dans l'historique git ; le fichier actuel est masqué. Purger l'historique demande ton accord.</li>
<li><b>Images intimes</b> (S-11 seins, S-14, S-16, lividités) : masquées par une fenêtre occultante ; à garder ou remplacer par une figurante habillée ?</li>
<li><b>Gestes à photographier</b> : 13 gestes neurologiques et une vingtaine de manœuvres n'existent pas en image libre (liste dans <code>recensement/BESOINS_IMAGES.html</code> et dans chaque fiche Status).</li>
<li><b>Anatomie</b> : seul sous-onglet non commencé (riche en images) ; je propose de l'ouvrir après ton feu vert.</li></ul>
<h2>Ce qui tourne encore</h2><ul><li>Recherche Commons complémentaire (script gratuit, lent).</li><li>Recherche Commons complémentaire (script gratuit, lent).</li></ul>
<h2>Captures</h2>{caps}"""
open('bilans/BILAN_NUIT_14_11.html', 'w', encoding='utf-8').write(page)
print('ok')
