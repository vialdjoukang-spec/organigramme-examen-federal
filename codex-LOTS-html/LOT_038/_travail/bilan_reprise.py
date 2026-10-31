"""Bilan vérifié de la production réellement présente, sans score médical."""
from pathlib import Path
from datetime import datetime, timezone
from html import escape
import hashlib, json, sys
from lxml import html

P=Path(__file__).resolve().parents[1]
vpath=P/'audits'/sys.argv[1]
v=json.loads(vpath.read_text())
rows=[];fichiers=[]
for f in v['fichiers']:
    p=P/f['fichier'];b=p.read_bytes()
    assert hashlib.sha256(b).hexdigest()==f['sha256']
    assert len(b)==f['octets']
    tree=html.fromstring(b)
    questions=len(tree.xpath('//details[contains(concat(" ",normalize-space(@class)," ")," quiz ")]'))
    assert questions==14
    c=sum(x['ok'] for x in f['controles'])
    limite=100000 if 'Phase_A' in p.name else 9000
    taille_v8=f['texte_fiche_octets']<=limite
    bande_v0=80000<=f['octets']<=150000
    fichiers.append({**{k:f[k] for k in ['fichier','sha256','octets','texte_fiche_octets','texte_fenetres_octets','citations_aips']},'texte_total_octets':f['texte_fiche_octets']+f['texte_fenetres_octets'],'taille_v8_conforme':taille_v8,'bande_v0_conforme':bande_v0,'questions':questions,'conditions_positives':c,'conditions_total':len(f['controles'])})
    vals=[f'{f["texte_fiche_octets"]/1000:.3f}',f'{f["texte_fenetres_octets"]/1000:.3f}',f'{(f["texte_fiche_octets"]+f["texte_fenetres_octets"])/1000:.3f}',f'{f["octets"]/1000:.3f}','Oui' if taille_v8 else 'Non','Oui' if bande_v0 else 'Non',str(questions),f'{c}/{len(f["controles"])}',str(f['citations_aips'])]
    rows.append('<tr><th scope="row"><a href="LOT_038/'+escape(p.name)+'">'+escape(p.name)+'</a></th>'+''.join('<td>'+x+'</td>' for x in vals)+'</tr>')
n=len(fichiers);qs=sum(x['questions'] for x in fichiers);cond=sum(x['conditions_positives'] for x in fichiers);cit=sum(x['citations_aips'] for x in fichiers)
nextdx=next((i for i in range(1,11) if not (P/f'LOT_038_Phase_B_V0_DX.{i}.html').exists()),None)
statut='Production des onze HTML terminée ; conformité globale non certifiée.' if nextdx is None else f'Lot incomplet ; prochain diagnostic DX{nextdx}.'
report={'date':datetime.now(timezone.utc).isoformat(),'lot':38,'source_controles':str(vpath),'html':n,'questions':qs,'conditions_v8_positives':cond,'citations_aips':cit,'prochain_diagnostic':nextdx,'statut':statut,'audit_independant':False,'validation_clinique_humaine':False,'navigateur':False,'fichiers':fichiers}
(P/'audits/BILAN_REPRISE.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
page='''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>LOT038 — bilan de production</title><style>body{font:17px/1.6 system-ui,sans-serif;color:#173044;background:#f4f6f7;margin:0}main{max-width:1250px;margin:auto;padding:2rem}article{background:white;padding:1.5rem;border-radius:12px;margin:1rem 0}h1,h2{line-height:1.2}table{border-collapse:collapse;width:100%;font-size:.82rem}th,td{border-bottom:1px solid #ccd7dc;padding:.65rem;text-align:right}th:first-child{text-align:left}thead{background:#e5eff2}a{color:#075e8a}.table{overflow:auto}.limites{border-left:6px solid #be8418}</style></head><body><main>'''
page+=f'<h1>LOT038 : {n} leçons produites sur onze</h1><p>Checkpoint du 31 octobre 2026 · {escape(statut)}</p><article><h2>Production mesurée</h2><p>{qs} questions, {cond} conditions statiques V8 satisfaites, {cit} paragraphes AIPS retrouvés dans les archives officielles. Relectures et corrections internes tracées. LOT038 comprend désormais ses onze leçons ; la relecture transversale interne est conservée dans ses audits.</p></article>'
page+='<article><h2>Tailles et contrôles exacts</h2><p>1 Ko = 1000 octets. x mesure le texte de la fiche sans fenêtres ; y mesure les fenêtres et dépliants ; x+y donne le texte total. Le HTML contient aussi balisage, styles et polices. La limite V8 de x est de 9 Ko pour un diagnostic et de 100 Ko pour le cours du symptôme (PROMPT_PRODUCTION_V2.md, §12 ; PROMPT_CODEX.md, §8). La bande initiale V0 est de 80 à 150 Ko pour le fichier HTML complet, bornes comprises (PROMPT_ULTIME_PRODUCTION_LOTS_V0.md, §14). Les deux comparaisons sont affichées séparément.</p><p>Ouvrir ou fermer une fenêtre ne change pas la taille du fichier : son contenu est déjà embarqué. Les colonnes x et x+y comparent les volumes de texte, sans créer une version HTML privée de ses fenêtres. « Oui » dans une colonne de taille ne signifie pas conformité médicale, linguistique ou globale au prompt.</p><div class="table"><table><thead><tr><th>Leçon</th><th>Sans fenêtres x Ko</th><th>Fenêtres y Ko</th><th>Avec fenêtres x+y Ko</th><th>HTML Ko</th><th>Taille V8 conforme</th><th>Bande V0 conforme</th><th>Questions</th><th>Conditions V8</th><th>Citations AIPS</th></tr></thead><tbody>'+''.join(rows)+'</tbody></table></div></article>'
page+='<article class="limites"><h2>Limites qui restent ouvertes</h2><ul><li>Les relectures sont internes. Aucun audit indépendant, score médical ou validation clinique humaine.</li><li>Les rapports historiques du harnais et de langue restent négatifs et conservés. Les incompatibilités title/h3 avec V8 sont expliquées sans modifier les contrôles.</li><li>Les citations exactes ne certifient ni le choix du traitement ni son exhaustivité. Les protocoles spécialisés et les accès partiels restent indiqués dans HELP et les relectures.</li><li>Aucun essai navigateur ou contrôle visuel revendiqué. Aucun classement de fréquence suisse démontré.</li><li>La présence des parties et le succès des contrôles V8 ne valent pas conformité globale au prompt.</li></ul><p><a href="LOT_038/audits/'+escape(vpath.name)+'">Contrôles détaillés</a> · <a href="LOT_038/audits/BILAN_REPRISE.json">Bilan et empreintes</a> · <a href="LOT_038/HELP.md">Points ouverts</a> · <a href="LOT_038/evidence/INDEX.md">Sources lues</a></p></article><p>Les veilles contrôlent le contrat pendant la disponibilité du runtime ; elles ne rédigent pas les leçons.</p></main></body></html>'
dest=P.parent/'BILAN_CHECKPOINT_LOT_038.html';dest.write_text(page)
tree=html.fromstring(dest.read_bytes())
assert len(tree.xpath('//tbody/tr'))==n
for link in tree.xpath('//a[@href]/@href'):
    assert (P.parent/link).exists(),link
(P/'audits/verification_bilan_reprise.json').write_text(json.dumps({'date':report['date'],'lignes':n,'questions':qs,'empreintes_sources_verifiees':True,'liens_locaux_resolus':True,'sha256_rapport':hashlib.sha256(dest.read_bytes()).hexdigest()},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['html','questions','conditions_v8_positives','citations_aips','prochain_diagnostic']},ensure_ascii=False))
