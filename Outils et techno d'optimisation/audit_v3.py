from pathlib import Path
from bs4 import BeautifulSoup
import json,sys
from playwright.sync_api import sync_playwright
R=Path('/workspace/outils-puissants');html_path=R/'Outils_Puissants_AZ.html'
s=BeautifulSoup(html_path.read_text(),'html.parser');D=json.loads((R/'data.json').read_text())
checks=[]
def check(name,ok,detail=''):
 checks.append({'controle':name,'statut':'OK' if ok else 'KO','detail':detail})
check('Alphabet A–Z complet',list(D)==[chr(i) for i in range(65,91)],'26 lettres')
check('128 outils conservés',sum(map(len,D.values()))==128,f"{sum(map(len,D.values()))} outils")
names={t[0] for v in D.values() for t in v}
check('Corrections v2 présentes',{'LadybugDB','Query2doc / QueryGym','Quivr','Elysia'}<=names and 'AutoGen' in names and 'Kuzu' in names,'LadybugDB, QueryGym, Quivr, Elysia, AutoGen, Kuzu')
check('FastEmbed sans doublon',sum(t[0]=='FastEmbed' for v in D.values() for t in v)==1,'1 entrée')
check('Rouge usage intensif',sum(t[4] for v in D.values() for t in v)>=90 and s.find('script').string.count('priority-label')-1==sum(t[4] for v in D.values() for t in v),f"{sum(t[4] for v in D.values() for t in v)} outils signalés")
check('Vulgarisation chaque outil',all(len(t)==6 and t[5] for v in D.values() for t in v),'128 explications doubles')
check('Vulgarisation chaque technologie',len(s.select('.tech-plain-toggle'))==15,'11 technos + 4 modèles entreprise')
check('Guide en 6 étapes',len(s.select('#guide .usage-steps li'))==6,'6 étapes guide (+6 bac à sable)')
check('Objectifs vulgarisés',len(s.select('.outcome-grid article'))>=4,'gaspillage, coût, recherche, automatisation')
check('Atkinson WOFF2 embarquée',s.style.string.count('@font-face')==4 and 'data:font/woff2;base64' in s.style.string,'4 variantes inline')
check('Aucun CDN',not s.select('script[src],link[rel=stylesheet]'),'aucune dépendance externe')
techs=['reseaux','obsidian','harness','rag','web','ops','bracelet','mcp','skills','scripts','ultra']
for t in techs:
 w=s.select_one('#work-'+t)
 check('Deux schémas · '+t,w is not None and len(w.select('[data-network]'))==2 and len(w.select('.svg-node'))==14,'Medina + Organigramme, 7 nœuds chacun')
check('t287u · 22 schémas SVG',len(s.select('.pro-network'))==22 and len(s.select('.svg-node'))==154,'22 vues SVG, 154 cases')
check('t287u · courbes et cibles',len(s.select('.net-link[marker-end]'))>=132 and all(' C ' in x.get('d','') for x in s.select('.net-link')),'courbes cubiques C + flèches marker-end')
check('t287u · Obsidian dédié',all(x in s.select_one('#work-obsidian').get_text(' ',strip=True) for x in ['Vault','Notes','Liens','Graph','Plugins']),'Vault, notes, liens bidirectionnels, graph, plugins')
check('t287u · fond blanc et liens cliquables','.pro-network' in str(s) and len(s.select('.net-link[role=button]'))>=132,'fond blanc, nœuds et connexions accessibles')
check('t288u · Graph Obsidian circulaire',len(s.select('#work-obsidian .graph-vignette'))==2 and len(s.select('#work-obsidian .graph-dot'))==32 and all('Q ' in x.get('d','') for x in s.select('.graph-edge')),'2 panneaux Graph, 32 nœuds circulaires, courbes denses')
check('t288u · Canvas entreprise',len(s.select('.biz-svg .biz-note-title-bar'))==20 and all(' C ' in x.get('d','') for x in s.select('.biz-svg-link')),'20 cartes-notes, liens cubiques, contenu hors santé')
check('Onglet entreprise',len(s.select('.biz-card'))==4 and len(s.select('.biz-node'))==20,'4 modèles cliquables')
check('Conseil projet présent',s.select_one('#conseil') is not None and s.select_one('#project-description') is not None,'formulaire structuré et textarea')
check('Questions ciblées → recommandation','function buildQuestions' in str(s) and 'function scoreAdvisor' in str(s),'questions conditionnelles et scoring local')
check('Score honnête + alternatives','meilleure correspondance sur ce catalogue' in str(s).lower() and 'pas une probabilité de réussite' in str(s),'adéquation, pas promesse')
check('Export IA Markdown/JSON','copy-ai-prompt' in str(s) and 'download-ai-prompt' in str(s) and 'download-ai-json' in str(s),'copie + téléchargements')
check('Mise à jour lettre/section','export-letter' in str(s) and 'import-letter' in str(s) and 'namesCatalog[letter]=items' in str(s),'export + import fusionné par lettre')
check('Mission6 · 22 légendes chiffrées',len(s.select('.pro-network .diagram-metrics'))==22 and all('ESTIMATION' in x.get_text() and 'Coût évité' in x.get_text() and 'Performance' in x.get_text() and 'Mise en place' in x.get_text() for x in s.select('.diagram-metrics')),'22 × coût, performance, qualité, complexité + justification')
check('Mission6 · 11 fiches chef-d’œuvre',len(s.select('.masterpiece'))==11 and len(s.select('.master-flow'))==12,'11 architectures Atelier + circuit bac à sable')
check('Mission6 · coût honnête','taux de 99 % est une cible expérimentale' in str(s) and 'pas coût total ni qualité garantie' in str(s),'estimations, aucune promesse 99–100 %')
check('Mission6 · harnais bracelet audit local',all(x in str(s) for x in ['1–3 outils','Ollama','llama.cpp','Promptfoo','petit modèle local','Audit intégré']),'outils récents + escalade bornée')
check('Mission6 · onglet bac à sable',s.select_one('#tab-sandbox') is not None and len(s.select('#sandbox .sandbox-grid article'))==6,'🧪 + six options avec coût et limites')
check('Mission6 · vrai vault Obsidian',len(list((R/'Vault_BacASable').glob('*.md')))==6 and all('[[' in p.read_text() for p in (R/'Vault_BacASable').glob('*.md')),'six notes liées [[...]]')
canvas=json.loads((R/'Vault_BacASable/Circuit_Zero_Cout.canvas').read_text())
ids={n['id'] for n in canvas['nodes']}
check('Mission6 · JSON Canvas valide',len(canvas['nodes'])==6 and len(canvas['edges'])==6 and all(e['fromNode'] in ids and e['toNode'] in ids and e.get('toEnd')=='arrow' for e in canvas['edges']),'6 cartes-fichiers + 6 flèches conformes')
for doc in ['RECAP_TECHNOS_EXISTANTES.md','REFERENCES_OBSIDIAN.md','HARNAIS_BRACELET_V4.md']:
 check('Mission6 · document '+doc,(R/doc).exists() and len((R/doc).read_text())>1000,'texte sourcé inclus')
check('Mission6 · sources web ouvertes',all(x in (R/'REFERENCES_OBSIDIAN.md').read_text() for x in ['help.obsidian.md/plugins/canvas','help.obsidian.md/plugins/graph','jsoncanvas.org/spec/1.0','github.com/ollama/ollama','x.com/swarogan']),'Obsidian + GitHub + X')
with sync_playwright() as p:
 b=p.chromium.launch(headless=True);page=b.new_page(viewport={'width':1440,'height':1100})
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto(html_path.as_uri()+'#guide');page.wait_for_timeout(300)
 check('Onglet guide fonctionnel',page.locator('#guide').is_visible() and not page.locator('#alphabet').is_visible())
 page.click('#start-alpha');page.locator('#tools .plain-toggle').first.click();check('Bouton outil révèle la vulgarisation',page.locator('#tools .plain-copy').first.is_visible())
 page.click('#tab-atelier');page.click('[data-work="mcp"]')
 check('Deux schémas MCP visibles',page.locator('#work-mcp [data-network]').count()==2)
 for course in ['medina','ssp']:
  page.locator(f'#work-mcp .svg-node[data-course="{course}"]').first.click()
  panel=page.locator(f'#explain-mcp-{course}')
  check('Explication nœud MCP '+course,'Pourquoi cela économise' in panel.inner_text() and len(panel.inner_text())>140)
 page.click('#tab-entreprise');page.locator('.biz-node').first.click()
 check('Schéma entreprise cliquable','Valeur créée' in page.locator('#biz-agents').inner_text())
 page.click('#tab-conseil');page.fill('#project-description','Projet de monographies et lots SSP avec preuves.');page.fill('#project-goal','Production hebdomadaire fiable');page.click('#generate-questions');check('Questions projet générées',page.locator('[data-answer]').count()>=3)
 page.click('#generate-recommendation');check('Recommandation et alternatives affichées','meilleure correspondance sur ce catalogue' in page.locator('#recommendation-result').inner_text() and len(page.locator('#ai-prompt').input_value())>1000)
 with page.expect_download() as dl:page.click('#download-ai-json')
 dl.value.save_as(R/'test-conseil-audit.json');check('Export IA JSON téléchargé',json.loads((R/'test-conseil-audit.json').read_text())['methode'].startswith('score local'));(R/'test-conseil-audit.json').unlink()
 check('Aucune erreur JavaScript',not errors,'; '.join(errors))
 page.click('#tab-sandbox');check('Onglet bac à sable fonctionnel',page.locator('#sandbox').is_visible() and not page.locator('#atelier').is_visible());page.screenshot(path=str(R/'captures/13_Bac_a_sable_Desktop.png'),full_page=False)
 page.click('#tab-atelier');page.click('[data-work="obsidian"]');page.screenshot(path=str(R/'captures/14_Obsidian_Legendes_Desktop.png'),full_page=False)
 page.click('[data-work="harness"]');page.locator('#work-harness .svg-node[data-course="medina"]').nth(2).click();page.screenshot(path=str(R/'captures/15_Harnais_Desktop.png'),full_page=False)
 # Capture demonstrating interactions, not merely placeholders
 page.click('#tab-atelier');page.click('[data-work="mcp"]');page.locator('#work-mcp .svg-node[data-course="medina"]').nth(2).click();page.locator('#work-mcp .svg-node[data-course="ssp"]').nth(2).click()
 page.screenshot(path=str(R/'captures/03_Reseaux_Interactifs.png'),full_page=False)
 page.set_viewport_size({'width':390,'height':844});page.click('#tab-sandbox');page.screenshot(path=str(R/'captures/16_Bac_a_sable_Mobile.png'),full_page=False)
 check('Mobile sans débordement',page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'))
 page.click('#tab-entreprise');page.locator('.biz-node').first.click(timeout=5000);check('Mobile entreprise cliquable','Valeur créée' in page.locator('#biz-agents').inner_text())
 b.close()
report={'version':'3','date':'2026-11-06','resultat':'OK' if all(c['statut']=='OK' for c in checks) else 'KO','controles':checks}
(R/'AUDIT_V3.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
lines=['# Auto-audit v3 — Atlas des outils puissants','',f"Résultat global : **{report['resultat']}** — 6 novembre 2026 (Europe/Zurich).",'']
lines += [f"- [{'x' if c['statut']=='OK' else ' '}] **{c['statut']} · {c['controle']}** — {c['detail']}" for c in checks]
(R/'AUDIT_V3.md').write_text('\n'.join(lines)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
if report['resultat']!='OK':sys.exit(1)
