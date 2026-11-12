#!/usr/bin/env python3
"""RAPPORT — page HTML du harnais (zéro modèle) : état des lieux chiffré, modèle, harnais, outils historiques, reprise.
Usage : python3 Claude/_harnais/rapport.py  → Claude/_harnais/RAPPORT_HARNAIS.html"""
import json, collections, html, datetime

G = json.load(open('Claude/_harnais/donnees/gaspillon.json', encoding='utf-8'))
A = [json.loads(l) for l in open('Claude/_harnais/donnees/agents.jsonl', encoding='utf-8')]
M = json.load(open('Claude/_harnais/donnees/modele.json', encoding='utf-8'))
P = [a for a in A if a['type'] == 'principal'][0]
S = [a for a in A if a['type'] != 'principal']
tot_s = sum(a['cout'] for a in S) / 1e6; tot_p = P['cout'] / 1e6; tot = tot_s + tot_p
cr = sum(a['cache_read_input_tokens'] for a in S) * .1 / 1e6; cw = sum(a['cache_creation_input_tokens'] for a in S) * 1.25 / 1e6
ou = sum(a['output_tokens'] for a in S) * 5 / 1e6
morts = [a for a in S if not a.get('fini')]; cm = sum(a['cout'] for a in morts) / 1e6
par = collections.defaultdict(list)
for a in S: par[a['type']].append(a)
f = lambda x, d=1: f'{x:,.{d}f}'.replace(',', ' ')
st = M['stats']
LIB = {'redaction_2DX': 'Rédaction, 2 DX par agent', 'redaction_1DX': 'Rédaction, 1 DX par agent', 'redaction_PhaseA': 'Rédaction Phase A',
       'audit': 'Audit', 'contre_audit': 'Contre-audit', 'correction': 'Corrections', 'gel_P1': 'Porte P1 (liste)', 'recherche': 'Recherche de sources', 'autre': 'Autres tâches'}
lignes_type = ''.join(f'<tr><td>{LIB.get(t, t)}</td><td>{len(par[t])}</td><td>{f(sum(a["cout"] for a in par[t]) / 1e6, 0)}</td><td>{f(100 * sum(a["cout"] for a in par[t]) / 1e6 / tot_s, 0)} %</td>'
                      f'<td>{f(st[t]["cout"], 2)}</td><td>{f(st[t]["T"], 0)}</td><td>{f(st[t]["C0"] / 1e3, 0)} k</td><td>{f(st[t]["Cfin"] / 1e3, 0)} k</td><td>{f(st[t]["sortie"] / 1e3, 0)} k</td></tr>'
                      for t in sorted(par, key=lambda t: -sum(a['cout'] for a in par[t])) if t in st)
V = M['validation']
val = ''.join(f'<tr><td>LOT_0{L}</td><td>{f(v["reel"])}</td><td>{f(v["mediane"])}</td><td>{f(v["ic95"][0])} – {f(v["ic95"][1])}</td><td>{"oui" if v["ic95"][0] <= v["reel"] <= v["ic95"][1] else "non"}</td></tr>' for L, v in V.items())
ac, hc = M['lot_actuel_calibre'], M['lot_harnais_calibre']
eco = 100 * (1 - hc['mediane'] / ac['mediane'])
OUTILS = [
 ('suivi.py', 'Compteur par agent : tours, contexte, sortie, coût, accès web, usage de la mémoire ; page de progression.', 'Après chaque agent, et toutes les 10 min (veille).'),
 ('modele.py', 'Modèle de consommation : identité mécanique, régression, Monte-Carlo, effet LOT, mesure réelle des économies.', 'Toutes les 10 min (veille).'),
 ('resumeur.py', 'Mémoire d’un LOT (MEMOIRE.md, ≈ 12 Ko au lieu de ≈ 950 Ko de cours) : liste gelée, états, verdicts, restants, sources déjà lues.', 'Avant chaque agent, après chaque commit (veille).'),
 ('memoire_agent.py', 'Carnet de chaque agent (une ligne par fait établi) : reprise sans relecture, transmission entre agents.', 'Lu au départ, écrit à chaque étape.'),
 ('sources_cache.py', 'Cache partagé des sources : une page n’est rapatriée qu’une fois ; citations ciblées par mots ; API SSI.', 'À la place de toute relecture web.'),
 ('aips_fiche.py', 'Fiche AIPS compacte (≈ 3 Ko au lieu de 40–120 Ko) et porte « grossesse, allaitement, date » avant audit.', 'Rédaction et avant audit.'),
 ('abreviations.py', 'Porte « sigles développés » (principe de Lyncée).', 'Avant audit.'),
 ('images_lot.py', 'Quête d’images en lot, licences libres, classement couleur (Blausen, OpenStax d’abord), planche unique.', 'Une fois par LOT.'),
 ('gaspillon.py', 'Le_Gaspillon : 9 détecteurs de gaspillage sur les journaux de chaque agent (refetch, domaine en échec relancé, lecture intégrale, relecture, sortie d’outil géante, contexte, tours, échec répété, accès au dépôt fermé), coût évitable estimé.', 'Toutes les 10 min (veille) ; page GASPILLON.html.'),
 ('extrait.py', 'Lecture d’un cours par point, par fenêtre ou par motif (≈ 3–20 Ko au lieu de 85–150 Ko).', 'À la place de toute lecture intégrale.'),
 ('cerveau.py', 'Second cerveau : recherche BM25 sur mémoires, carnets, consignes, audits et sources en cache ; 8 passages avec leur chemin.', 'Avant toute relecture ; index rafraîchi par la veille.'),
 ('bracelet.py', 'Sélecteur du Bracelet : une tâche → 1 à 3 outils locaux.', 'Au début de chaque tâche.'),
 ('verrou_medina.py', 'Crochet PreToolUse : refuse tout outil visant le dépôt MEDINA (agents compris).', 'Permanent ; vérifié par la veille.'),
 ('veille_harnais.sh', 'Boucle locale gratuite : MEMOIRE.md, progression, modèle, Gaspillon, index du cerveau toutes les 10 minutes ; consigne ses propres échecs.', 'Lancée au GO.'),
 ('BRIEF_HARNAIS.md', 'Brief de 2 Ko remplaçant ≈ 300 Ko de lectures (MISSION, CONSIGNES, prompt L1 par extraits).', 'Donné à chaque agent.')]
outils = ''.join(f'<tr><td><code>{n}</code></td><td>{d}</td><td>{q}</td></tr>' for n, d, q in OUTILS)
HIST = [
 ('controle3.py', 'Conservé, porte obligatoire', 'Contrôle gratuit des 3 axes ; déjà au cœur du flux.'),
 ('verif_aips.py', 'Conservé et complété', 'Vérifie les doses ; aips_fiche ajoute grossesse, allaitement, contre-indications et dates.'),
 ('cliche.py', 'Conservé, intégré', 'Fournisseur de images_lot.py (recherche et prise) ; figures annotées.'),
 ('outils/images.py', 'Intégré comme fournisseur large', 'Commons + Europe PMC + catalogue de liens, budget journalier, refus NC/ND : à appeler avant images_lot pour le tri couleur.'),
 ('paquet.py', 'Conservé', 'Paquet de preuves par point ; complémentaire du cache des sources.'),
 ('geler.py', 'Conservé', 'Gel signé de la liste DX (porte P1).'),
 ('planche5.py, capture5.py', 'Conservés', 'Contrôle visuel en une planche par LOT.'),
 ('inventaire_images.py', 'Conservé', 'Compte rendu des images d’un LOT, utile à l’audit B.'),
 ('reprise_g.py, detecteur_lots.py, progression.py', 'Remplacés pour Claude par resumeur.py --global', 'Même but (état sans relecture) ; resumeur lit verdicts et restants.'),
 ('legion.py, mere.py, soldat.py', 'Principe repris', 'Lecture git sans checkout, sorties ≤ 3 Ko : repris dans la mémoire compacte.'),
 ('rediger.py', 'Principe repris', 'Une passe par point avec paquet : repris par la rédaction en un fichier de contenu (générateur).'),
 ('tools/lyncee.py', 'Principe repris dans abreviations.py', 'Lié au corpus app_v2 : non applicable tel quel aux cours LOT.'),
 ('tools/aletheia.py, tools/audit/*', 'Non retenus', 'Liés aux données data/ck d’app_v2, pas aux cours LOT.'),
 ('tools/garde/*, porte.py, checkpoint.py', 'Conservés (CI)', 'Garde-fous des PR ; indépendants du harnais de production.'),
 ('appliquer.py, appliquer_html.py', 'Conservés', 'Application mécanique des corrections avant/après des audits : moins de tours en correction.'),
 ('forme.py, migrer_l1.py, renfort_citations.py', 'Conservés', 'Passes mécaniques de forme, zéro modèle.'),
 ('Corpus AipsDownload (8.10.2026)', 'Intégré (sorti de MEDINA)', 'Copié dans le cache ; aips_fiche.py trouve donne n° d’autorisation, date et URL de l’AIPS (SmPC) sans recherche web. Il tranche déjà un restant du LOT_023 : Mestinon 19943 comprimés, 19945 dragées, 56387 retard.')]
BRA = [
 ('Crawl4AI, Firecrawl', 'Filtrage', 'Non installés', 'sources_cache.py nettoie déjà HTML et PDF en texte ; Firecrawl est un service payant.'),
 ('Chonkie, FlagEmbedding', 'Filtrage', 'Principe repris', 'cerveau.py découpe et classe les passages (BM25, sans modèle d’embeddings lourd).'),
 ('LLMLingua', 'Filtrage', 'Non applicable', 'Compresse les invites d’une API directe ; les agents Claude Code n’y passent pas. Équivalent : extrait.py.'),
 ('RTK', 'Filtrage', 'Principe repris', 'Sorties d’outils courtes : Gaspillon G5 (> 20 000 car.) et extrait.py. C’est la première fuite mesurée.'),
 ('Mem0, Graphiti', 'Mémoire', 'Remplacés', 'Mémoire en fichiers (MEMOIRE.md, carnets) + cerveau.py : lisible, versionnée, gratuite.'),
 ('GPTCache, Portkey', 'Cache', 'Non applicables', 'Caches de réponses d’API ; aucun appel API direct ici.'),
 ('requests-cache, Hishel', 'Cache', 'Déjà couverts', 'sources_cache.py et le cache AIPS.'),
 ('Prefect, APScheduler, Celery', 'Orchestration', 'Remplacés', 'veille_harnais.sh suffit (une boucle, zéro dépendance).'),
 ('PyBreaker', 'Protection', 'Principe repris', 'Disjoncteur par domaine dans sources_cache.py : 2 échecs en 24 h coupent le domaine.'),
 ('LiteLLM, RouteLLM, Semantic Router', 'Routage', 'Règle reprise', 'Tâche mécanique → script d’abord ; rédaction et audit médical gardent le modèle actuel (qualité d’abord).'),
 ('Phoenix', 'Observation', 'Remplacé', 'suivi.py, modele.py et Le_Gaspillon lisent les journaux locaux, sans serveur.')]
bra = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in BRA)
LIBG = dict(G1='Source rapatriée deux fois ou déjà en cache', G2='Domaine en échec relancé', G3='Lecture intégrale d’un fichier > 50 Ko', G4='Même fichier lu ≥ 3 fois', G5='Sortie d’outil > 20 000 caractères', G6='Contexte > 250 k tokens', G7='Tours au-delà du budget', G8='Même commande en échec répétée', G9='Accès au dépôt MEDINA fermé')
gas = ''.join(f'<tr><td>{g}</td><td>{LIBG[g]}</td><td>{G["par_regle"][g]}</td><td>{f(G["cout_estime"].get(g, 0) / 1e6, 0) if G["cout_estime"].get(g) else "—"}</td></tr>' for g in sorted(G['par_regle']))
hist = ''.join(f'<tr><td><code>{n}</code></td><td>{d}</td><td>{m}</td></tr>' for n, d, m in HIST)
recent = sorted([a for a in S if (a.get('lot') or 0) >= 23], key=lambda a: a.get('fin') or '', reverse=True)[:30]
ag = ''.join(f'<tr><td>{html.escape(a["desc"][:48])}</td><td>{"en pause" if not a.get("fini") else "terminé"}</td><td>{a["tours"]}</td><td>{f(a["ctx_max"] / 1e3, 0)} k</td><td>{f(a["cout"] / 1e6, 2)}</td></tr>' for a in recent)
page = f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Harnais d'économie</title><style>
:root{{--fond:#f4faff;--carte:#fff;--trait:#d5e5f1;--titre:#0d3b66;--accent:#1b7f5a;--alerte:#b00020}}
body{{margin:0;background:var(--fond);color:#123;font:15px/1.5 system-ui,-apple-system,Segoe UI,sans-serif}}
main{{max-width:1100px;margin:0 auto;padding:16px}} h1{{color:var(--titre)}} h2{{color:var(--titre);border-bottom:2px solid var(--trait);padding-bottom:4px;margin-top:28px}}
.cartes{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px}} .c{{background:var(--carte);border:1px solid var(--trait);border-radius:12px;padding:12px}}
.c b{{display:block;font-size:24px;color:var(--titre)}} table{{border-collapse:collapse;width:100%;background:#fff}} td,th{{border:1px solid var(--trait);padding:5px 7px;text-align:left;vertical-align:top}}
th{{background:#eaf4fb}} .t{{overflow-x:auto}} .ok{{color:var(--accent);font-weight:600}} .rouge{{color:var(--alerte);font-weight:600}} nav a{{margin-right:10px}}
.barre{{height:22px;display:flex;border-radius:6px;overflow:hidden;border:1px solid var(--trait)}} .barre span{{display:block;color:#fff;font-size:12px;padding:2px 6px;white-space:nowrap}}
</style></head><body><main>
<h1>Harnais d’économie — état des lieux, modèle et reprise</h1>
<p>Relevé du {datetime.date.today():%d.%m.%Y}. Tous les agents sont <b class="rouge">en pause</b> ; leur travail est sauvegardé sur leurs branches. Rien ne reprend sans votre GO.</p>
<nav><a href="#resume">Résumé</a><a href="#lieux">État des lieux</a><a href="#fuites">Fuites</a><a href="#modele">Modèle</a><a href="#harnais">Harnais</a><a href="#memoire">Mémoire</a><a href="#gaspillon">Gaspillon</a><a href="#bracelet">Bracelet</a><a href="#historique">Outils historiques</a><a href="#agents">Agents</a><a href="#reprise">Reprise</a><a href="#decisions">Décisions</a></nav>
<h2 id="resume">Résumé</h2><div class="cartes">
<div class="c">Consommation mesurée depuis le 11.11<b>{f(tot, 0)} M</b>tokens équivalents coût (agents {f(tot_s, 0)} M · boucle principale {f(tot_p, 0)} M)</div>
<div class="c">Coût d’un LOT aujourd’hui<b>{f(ac["mediane"], 0)} M</b>IC 95 % {f(ac["ic95"][0], 0)} – {f(ac["ic95"][1], 0)} M (agents)</div>
<div class="c">Coût d’un LOT avec le harnais<b>{f(hc["mediane"], 0)} M</b>IC 95 % {f(hc["ic95"][0], 0)} – {f(hc["ic95"][1], 0)} M</div>
<div class="c">Économie prévue sur les agents<b class="ok">−{f(eco, 0)} %</b>à qualité identique : la sortie rédigée n’est pas réduite</div></div>
<p>Le gaspillage ne vient pas de ce que les agents écrivent : il vient de ce qu’ils <b>relisent à chaque tour</b>. Le harnais coupe ces relectures par des scripts gratuits et une mémoire persistante, et il mesure automatiquement l’économie réelle dès la reprise.</p>
<h2 id="lieux">État des lieux chiffré</h2>
<p>Unité : token équivalent coût (entrée ×1, cache écrit ×1,25, cache lu ×0,1, sortie ×5). Agents mesurés : {len(S)} ; agents terminés modélisés : {M["n_agents"]}.</p>
<div class="barre"><span style="width:{100 * cr / tot_s:.0f}%;background:#2d6a9f">relecture du contexte {100 * cr / tot_s:.0f} %</span><span style="width:{100 * cw / tot_s:.0f}%;background:#6a4c93">écriture du cache {100 * cw / tot_s:.0f} %</span><span style="width:{100 * ou / tot_s:.0f}%;background:#1b7f5a">texte produit {100 * ou / tot_s:.0f} %</span></div>
<div class="t"><table><tr><th>Tâche</th><th>Agents</th><th>Coût total (M)</th><th>Part</th><th>Coût médian par agent (M)</th><th>Tours</th><th>Contexte au départ</th><th>Contexte à la fin</th><th>Texte produit</th></tr>{lignes_type}</table></div>
<p>Boucle principale : {P["tours"]} tours, contexte moyen {f(P["cache_read_input_tokens"] / P["tours"] / 1e3, 0)} k tokens, maximum {f(P["ctx_max"] / 1e3, 0)} k. Agents arrêtés avant la fin (quota, pauses) : {len(morts)}, soit {f(cm, 0)} M perdus.</p>
<h2 id="fuites">Fuites identifiées, par ordre d’impact</h2><ol>
<li><b>Le nombre de tours pèse au carré.</b> Chaque tour relit tout le contexte, qui grossit d’environ {f(st["redaction_2DX"]["g"] / 1e3, 1)} k tokens par tour : le coût de relecture vaut T·C0 + g·T²/2. Un agent à 2 DX fait {f(st["redaction_2DX"]["T"], 0)} tours et finit à {f(st["redaction_2DX"]["Cfin"] / 1e3, 0)} k tokens.</li>
<li><b>Un socle de {f(st["redaction_2DX"]["C0"] / 1e3, 0)} k tokens relu à chaque tour par chaque agent</b> : outils, instructions, et le CLAUDE.md du dépôt MEDINA (28 Ko), sans rapport avec ces cours.</li>
<li><b>Relectures évitables</b> : AIPS entières (40–120 Ko), extraits du prompt L1 (142 Ko), cours entiers, sources déjà lues par un autre agent.</li>
<li><b>Fautes mécaniques laissées à l’audit</b> : les rubriques grossesse et allaitement adoucies et les dates d’AIPS fausses se détectent par script. Sur le LOT_024, aips_fiche.py a retrouvé sans modèle les défauts critiques et graves que l’audit avait relevés (14 défauts bloquants).</li>
<li><b>Boucle principale trop chargée</b> : contexte jusqu’à {f(P["ctx_max"] / 1e3, 0)} k tokens ; chaque notification relit tout.</li>
<li><b>Agents perdus</b> : {f(cm, 0)} M dépensés par des agents arrêtés sans rendre leur travail.</li></ol>
<h2 id="modele">Modèle mathématique multivarié</h2>
<p><b>1. Identité mécanique</b> (vérifiée agent par agent, R² = {M["r2_identite"]:.4f}) : coût = 0,1 · Σ<sub>tours</sub> contexte + 1,25 · cache écrit + 5 · sortie, avec Σ contexte ≈ T·C0 + g·T²/2.</p>
<p><b>2. Régression a priori</b> : log(coût) selon le type de tâche ; R² = {M["r2_regression"]:.2f}, écart-type résiduel {M["sigma_log"]:.2f} en log ; intervalles par bootstrap (2 000 tirages).</p>
<p><b>3. Monte-Carlo d’un LOT standard</b> (Phase A, porte P1, 5 agents × 2 DX, 4 audits, 2 corrections, 2 contre-audits, 2 recherches ; 20 000 tirages), avec un <b>effet LOT</b> calibré (difficulté commune : ×{f(2.718281828 ** M["effet_lot"]["mu"], 2)} en moyenne, écart-type log {M["effet_lot"]["sd"]:.2f}).</p>
<div class="t"><table><tr><th>LOT laissé de côté</th><th>Réel (M)</th><th>Prévu sans effet LOT (M)</th><th>IC 95 %</th><th>Dans l’intervalle</th></tr>{val}</table></div>
<p>Le LOT_024 mêle des agents de deux journées (des rédacteurs morts avant d’écrire, puis les binômes) : il sort de l’intervalle pour cette raison. L’effet LOT corrige le biais observé sur les LOT 021 et 023.</p>
<p><b>4. Leviers du harnais</b> (incertitude propagée, plages prudentes) : socle C0 −{int(M["leviers"]["C0"][0] * 100)} à −{int(M["leviers"]["C0"][1] * 100)} % ; tours T −{int(M["leviers"]["T"][0] * 100)} à −{int(M["leviers"]["T"][1] * 100)} % ; croissance g −{int(M["leviers"]["g"][0] * 100)} à −{int(M["leviers"]["g"][1] * 100)} %. La sortie (le texte des cours) n’est pas réduite : la qualité ne paie pas l’économie.</p>
<div class="t"><table><tr><th>Par LOT (agents)</th><th>Médiane</th><th>IC 80 %</th><th>IC 95 %</th></tr>
<tr><td>Aujourd’hui</td><td>{f(ac["mediane"], 0)} M</td><td>{f(ac["ic80"][0], 0)} – {f(ac["ic80"][1], 0)}</td><td>{f(ac["ic95"][0], 0)} – {f(ac["ic95"][1], 0)}</td></tr>
<tr><td>Avec le harnais</td><td class="ok">{f(hc["mediane"], 0)} M</td><td>{f(hc["ic80"][0], 0)} – {f(hc["ic80"][1], 0)}</td><td>{f(hc["ic95"][0], 0)} – {f(hc["ic95"][1], 0)}</td></tr></table></div>
<p>Pour les 223 LOT restants, l’économie médiane prévue vaut environ {f((ac["mediane"] - hc["mediane"]) * 223 / 1000, 1)} milliards de tokens équivalents. Chaque agent lancé sous harnais porte « [H] » dans sa description : modele.py compare alors automatiquement les coûts réels, avec un IC 95 %.</p>
<h2 id="harnais">Le harnais (réseau péri-agentique, tout gratuit)</h2>
<div class="t"><table><tr><th>Script</th><th>Rôle</th><th>Quand</th></tr>{outils}</table></div>
<p>Flux d’un agent : brief de 2 Ko → carnet + MEMOIRE.md + index des sources → rédaction en un fichier de contenu → portes gratuites (controle3, verif_aips, aips_fiche, abréviations) → note au carnet → commit → la veille met à jour mémoire, progression et modèle.</p>
<h2 id="memoire">Mémoire persistante : trois couches</h2><ol>
<li><b>MEMOIRE.md par LOT</b> (résumeur) : sur le LOT_023, 12 Ko au lieu de 950 Ko de cours, audits et sources.</li>
<li><b>Carnet de chaque agent</b> (memoire_agent.py) : une ligne par fait établi ; un agent qui reprend ou remplace un autre ne relit rien.</li>
<li><b>Caches partagés</b> : sources (texte brut hors dépôt, index dans le dépôt) et AIPS (rubriques compactes).</li></ol>
<p>Suivi de son fonctionnement : suivi.py compte, par agent, les appels à la mémoire et les accès web ; la page de progression les affiche. Un agent qui refetch une source déjà en cache est une fuite visible.</p>
<h2 id="gaspillon">Le_Gaspillon : détecteurs de gaspillage</h2>
<p>Relevé sur {len(G["agents"])} agents en alerte depuis le 11.11. Le coût évitable est une estimation haute : une sortie d’outil reste dans le contexte et se relit à chaque tour suivant (au plus 150 tours comptés).</p>
<div class="t"><table><tr><th>Règle</th><th>Détecteur</th><th>Alertes</th><th>Coût évitable (M)</th></tr>{gas}</table></div>
<p><b>Première fuite :</b> les lectures intégrales de cours (Read d’un HTML de 85–150 Ko), environ 150 M sur 173 M de sorties géantes. Correctif : extrait.py et Read toujours borné. Les accès à MEDINA servaient surtout au corpus AIPS, désormais sorti de MEDINA.</p>
<h2 id="bracelet">Bracelet : ce qui est repris</h2>
<p>Le Bracelet (19 bibliothèques, 5 catégories) reste un <b>sélecteur</b> : bracelet.py propose 1 à 3 outils locaux par tâche. Les bibliothèques ne sont pas installées : leurs principes sont repris là où ils ont un effet mesurable.</p>
<div class="t"><table><tr><th>Outil</th><th>Catégorie</th><th>Décision</th><th>Motif</th></tr>{bra}</table></div>
<h2 id="historique">Outils de vos anciens harnais, un par un</h2>
<div class="t"><table><tr><th>Outil</th><th>Décision</th><th>Motif</th></tr>{hist}</table></div>
<h2 id="agents">Agents en pause et derniers agents (LOT 023 à 025)</h2>
<div class="t"><table><tr><th>Agent</th><th>État</th><th>Tours</th><th>Contexte max</th><th>Coût (M)</th></tr>{ag}</table></div>
<p>Page détaillée et rafraîchie : <code>Claude/_harnais/progression_agents.html</code>.</p>
<h2 id="reprise">Plan de reprise au GO</h2><ol>
<li>Fusion du harnais (PR) puis lancement de la veille (10 min).</li>
<li>LOT_023 : 3 restants du contre-audit (numéros Mestinon tranchés par le corpus, allaitement Mestinon, CROSS/FLOT), corrigés par moi, puis PR.</li>
<li>LOT_024 : portes gratuites d’abord (aips_fiche, abréviations), puis corrections en une passe, contre-audit, PR.</li>
<li>LOT_025 : Phase A en contre-audit ; les 5 agents reprennent depuis leur WIP avec le brief harnais et leur carnet.</li>
<li>Mesure : premier LOT sous harnais comparé au modèle ; rapport régénéré automatiquement.</li></ol>
<h2 id="decisions">Décisions pour vous</h2><ol>
<li><b>MEDINA fermé</b> : verrou actif (tout accès refusé, agents compris), corpus AIPS sorti. Hors de ma portée : son CLAUDE.md (28 Ko, ≈ 9 k tokens) reste injecté par la plateforme tant que le dépôt est attaché à la session. Pour la prochaine session, ne sélectionnez que <code>organigramme-examen-federal</code>.</li>
<li><b>GO</b> pour lever la pause et appliquer le harnais à partir du LOT_023.</li></ol>
</main></body></html>'''
open('Claude/_harnais/RAPPORT_HARNAIS.html', 'w', encoding='utf-8').write(page)
print('Claude/_harnais/RAPPORT_HARNAIS.html', len(page.encode()))
