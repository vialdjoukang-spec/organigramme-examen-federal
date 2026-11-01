"""Checkpoint de préparation DX5, à exécuter une seule fois après les contrôles."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
D=Path(__file__).resolve().parent;B=D.parent
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
C=json.loads((D/'CONTROLE.json').read_text());Q=json.loads((D/'qa/CONTROLE_NAVIGATEUR.json').read_text());I=json.loads((B/'imagerie_20261101/INVENTAIRE.json').read_text())
for r in Q['rendus']:assert hashlib.sha256((B/r['fichier']).read_bytes()).hexdigest()==r['sha256']
s=json.loads((B/'ETAT_CONTINUITE.json').read_text());assert s['renforcement_medical']['fichiers_renforces_valides']==10
s['renforcement_medical_passe_precedente_dx4']=s['renforcement_medical'];r=dict(s['renforcement_medical'])
r.update(statut='DX5 contrôlés ; publication en préparation',preuve_base=D.name+'/BASELINE.json',fichiers_renforces_valides=12,parties_relues=168,questions_reponses_relues=168,preuves=D.name+'/',reste_lecons_a_renforcer=232,date=now,prochaines_lecons=['LOT_018/LOT_018_Phase_B_V0_DX.6.html','LOT_029/LOT_029_Phase_B_V0_DX.6.html'],contrelecture_distincte_portee='6 premières leçons seulement ;6 DX3/DX4/DX5 relus en interne',commit=None,push_confirme=False,publication_verifiee_le=None,verrou_libere_le=None)
r['tranche_fichiers']=r['tranche_fichiers']+[x['fichier'] for x in C['lecons']]
r['qa']={'preuve':D.name+'/qa/CONTROLE_NAVIGATEUR.json','configurations':8,'ouvertures_fenetres_directes':112,'ouvertures_reponses':112,'ouvertures_definitions':8,'captures_inspectees':8}
r['cette_passe']={'lecons':2,'parties':28,'questions_reponses':28,'nouveaux_cliches_integres':0,'apercus_tiers_acquis_inspectes_non_retenus':2,'schema_preexistant_preserve':1,'contrelecture_independante':False,'v8':550,'navigateur':True,'captures_inspectees':8}
s['renforcement_medical']=r;s['verrou']='détenu pour publication';s['prochaine_action']='Poursuivre seul LOT018 DX6 puis LOT029 DX6 ; acquérir les clichés manquants, notamment DX5. Premier nouveau diagnostic LOT040 DX2 après le rattrapage prioritaire.'
s['verification_reprise_solo_dx5']={'date':now,'checkpoint_frais':C['base'],'branche':'codex/lots','plage_fraiche':[18,133],'registre_token':'4f3b52bb58','registre_signe':True,'pret_verifier':[18,29],'verrou_acquis':True,'sous_agents':0,'communs_intacts':9,'autres_lecons_intactes':242,'modele':'Famille GPT-6 exposée ; variante/effort actuels non exposés. Astra ultra historique, high recommandé, aucun réglage changé.'}
s['balayage_imagerie_ecg'].update(date=now,passages=I['totaux']['passages'],passages_tries=I['totaux']['passages'],lecons_modifiees=2,statut='244 leçons recensées ;574 passages, tri actualisé pour les deux DX5.',preuves_campagne_actuelle=D.name+'/',portee_campagne='Deux DX5 renforcés et relus en interne ;242autres leçons inchangées.',publication='en préparation',push_confirme=False,commit=None)
s['dernier_checkpoint_le']=now;s['dernier_commit_checkpoint']=C['base'];save(B/'ETAT_CONTINUITE.json',s)
measures=' ; '.join(x['fichier']+f" : HTML {x['octets_apres']/1000:.3f} Ko, base {x['texte_fiche_octets']/1000:.3f} Ko, fenêtres {x['texte_fenetres_octets']/1000:.3f} Ko" for x in C['lecons'])
intro=f'''# Reprise solo DX5 — {now}

Dernier ordre : seul, sans sous-agents ; aucun agent lancé. Dépôt frais6c43b8b2, branche codex/lots ; borne18–133 relue, registre signé, pret/verifier018 et029 autorisés, verrou acquis. Écritures exclusivement codex-LOTS-html/.

Deux leçons renforcées : LOT018 DX5 rétinopathie diabétique et LOT029 DX5 tumeur intracrânienne pédiatrique.14parties et14réponses chacune ; relecture interne réelle, pas de contrelecture indépendante ni validation clinique humaine. Les dix leçons précédentes restent identiques. Cumul12/244,232restantes. Aucun nouveau lot terminé :22lots018–039 rédigés,040 PhaseA/DX1. Ne pas refaire la production initiale018 au commit950a4cd1.

Sources suisses HUG/Paediatrie2020, européennes COUF2025 et extraitsNICE ; résuméSIOPE seulement, complément international IRM2022 partiel. AIPS Eylea62393002 local relu ; deux fenêtres exactes préservées. Pas de nouvelle dose. Registre des lectures et limites dans renforcement_solo_dx5_20261101/LECTURES.json.

Images : aucun nouveau cliché intégré. IDRiD/RETA identifiés sousCC BY4 ; deux aperçus tiers acquis et inspectés, non retenus : composite déjà annoté, et original non identifié/résolution faible. MDPI429 ; EuropePMC403 pour la revue IRM, pixels non acquis. Schéma rétinien conceptuel conservé, contraste sombre corrigé. Ne pas déclarer le rattrapage iconographique terminé. Les réponses web et candidats exacts sont conservés localement dans _cache ignoré, notes et liens publiés.

Contrôles :550conditions V8 sur22fichiers,242autres leçons/9harnais intacts. Chromium8configurations,112fenêtres,112réponses,8définitions ;8captures partie9 inspectées. Audit langue historique toujours non conforme à certaines règles incompatibles avec V8 ; corrections de formulation documentées. Inventaire244leçons/574passages actualisé. Mesures : {measures}. Base DD sous9Ko ; poids HTML complet distinct du plafond.

Suite :018 DX6 puis029 DX6, acquisitions DX5 et lacunes antérieures.040 DX2 suspendu pendant le rattrapage. Les veilles locales37511/48342 contrôlent chaque60s pendant le runtime, sans rédiger ; aucune nouvelle veille concurrente. Le contrôleur générique signale la pause des nouveaux diagnostics ; cette alerte n’est pas masquée. Verrou détenu pour publication ; état final à consulter dans ETAT_CONTINUITE.json et JOURNAL_PASSES.jsonl.

Modèle : famille GPT-6 exposée ; variante et effort courants non exposés. Confirmation Astra ultra historique conservée, high recommandé ; aucun changement de réglage revendiqué.

## Historique daté conservé

'''
p=B/'REPRISE_CODEX.md';p.write_text(intro+p.read_text())
e={'date':now,'mode':'solo','sous_agents':0,'actions':['reprise fraîche, verrou et registre','lectures CH puis UE et complément international','rédaction des deuxDX5','relecture28parties/28réponses et corrections','V8 et langue avant/après','Chromium8configurations/8captures inspectées','deux aperçus tiers inspectés non retenus','tri574passages et checkpoint'],'publication':'en préparation'}
with (D/'JOURNAL_PASSES.jsonl').open('a') as f:f.write(json.dumps(e,ensure_ascii=False)+'\n')
with (B/'JOURNAL_CODEX.md').open('a') as f:f.write(f'\n{now} — Solo DX5 : rétinopathie018 et tumeur intracrânienne pédiatrique029 renforcées.28parties/28réponses relues,550conditionsV8,8configurationsChromium,8captures inspectées. Cumul12/244 ; aucune nouvelle image intégrée ni lot clos. Publication en préparation.\n')
for n in (18,29):
 with (B/f'LOT_{n:03}/JOURNAL.md').open('a') as f:f.write(f'\n{now} — DX5 renforcé,14parties/14réponses relues en interne. Preuves ../{D.name}/. Dix autres leçons inchangées ; aucun cliché nouveau intégré ni validation indépendante.\n')
 for poste in ('redacteur','relecture-interne','controle-v8','transversale-interne'):
  e={'horodatage':now,'lot':f'LOT_{n:03}','fichier':'DX.5@renforcement-solo-20261101','poste':poste,'modele':'GPT-6 — famille exposée ; variante non exposée','effort':'réglage courant non exposé ; high recommandé','independant':False,'raison':'Passe réellement effectuée sur DX5 ; preuves '+D.name+'/ ; Astra ultra historique, aucun changement.'}
  with (B/'ROUTAGE_CODEX.jsonl').open('a') as f:f.write(json.dumps(e,ensure_ascii=False)+'\n')
print('Checkpoint préparé, publication non revendiquée.')
