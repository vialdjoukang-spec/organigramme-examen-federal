"""Checkpoint unique DX6 après contrôles ; publication confirmée séparément."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
D=Path(__file__).resolve().parent;B=D.parent
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
C=json.loads((D/'CONTROLE.json').read_text());Q=json.loads((D/'qa/CONTROLE_NAVIGATEUR.json').read_text());I=json.loads((B/'imagerie_20261101/INVENTAIRE.json').read_text())
for r in Q['rendus']:assert hashlib.sha256((B/r['fichier']).read_bytes()).hexdigest()==r['sha256']
s=json.loads((B/'ETAT_CONTINUITE.json').read_text());assert s['renforcement_medical']['fichiers_renforces_valides']==12
s['renforcement_medical_passe_precedente_dx5']=s['renforcement_medical'];r=dict(s['renforcement_medical'])
r.update(statut='DX6 contrôlés ; publication en préparation',preuve_base=D.name+'/BASELINE.json',fichiers_renforces_valides=14,parties_relues=196,questions_reponses_relues=196,preuves=D.name+'/',reste_lecons_a_renforcer=230,date=now,prochaines_lecons=['LOT_018/LOT_018_Phase_B_V0_DX.7.html','LOT_029/LOT_029_Phase_B_V0_DX.7.html'],contrelecture_distincte_portee='6 premières leçons seulement ;8 DX3 à DX6 relus en interne',commit=None,push_confirme=False,publication_verifiee_le=None,verrou_libere_le=None)
r['tranche_fichiers']=r['tranche_fichiers']+[x['fichier'] for x in C['lecons']]
r['qa']={'preuve':D.name+'/qa/CONTROLE_NAVIGATEUR.json','configurations':8,'ouvertures_fenetres_directes':112,'ouvertures_reponses':112,'ouvertures_definitions':8,'captures_inspectees':8}
r['cette_passe']={'lecons':2,'parties':28,'questions_reponses':28,'nouveaux_cliches_integres':0,'pixels_nouveaux_inspectes':0,'candidat_licence_verifiee_telechargement_refuse':1,'schema_preexistant_preserve':1,'contrelecture_independante':False,'v8':550,'navigateur':True,'captures_inspectees':8}
s['renforcement_medical']=r;s['verrou']='détenu pour publication';s['prochaine_action']='Poursuivre seul LOT018 DX7 puis LOT029 DX7 ; acquérir les clichés manquants, notamment DX6. Premier nouveau diagnostic LOT040 DX2 après le rattrapage prioritaire.'
s['verification_reprise_solo_dx6']={'date':now,'checkpoint_frais':C['base'],'branche':'codex/lots','plage_fraiche':[18,133],'registre_token':'4f3b52bb58','registre_signe':True,'pret_verifier':[18,29],'verrou_acquis':True,'sous_agents':0,'communs_intacts':9,'autres_lecons_intactes':242,'modele':'Famille GPT-6 exposée ; variante/effort actuels non exposés. Astra ultra historique, high recommandé, aucun réglage changé.'}
s['balayage_imagerie_ecg'].update(date=now,passages=I['totaux']['passages'],passages_tries=I['totaux']['passages'],lecons_modifiees=2,statut=f"244leçons recensées ;{I['totaux']['passages']}passages, tri actualisé pour les deux DX6.",preuves_campagne_actuelle=D.name+'/',portee_campagne='Deux DX6 renforcés et relus en interne ;242autres leçons inchangées.',publication='en préparation',push_confirme=False,commit=None,publication_verifiee_le=None,verrou_libere_le=None)
s['dernier_checkpoint_le']=now;s['dernier_commit_checkpoint']=C['base'];save(B/'ETAT_CONTINUITE.json',s)
measures=' ; '.join(x['fichier']+f" : HTML {x['octets_apres']/1000:.3f} Ko, base {x['texte_fiche_octets']/1000:.3f} Ko, fenêtres {x['texte_fenetres_octets']/1000:.3f} Ko" for x in C['lecons'])
intro=f'''# Reprise solo DX6 — {now}

Dernier ordre : seul, sans sous-agents ; aucun agent lancé. Dépôt frais013d1302, branche codex/lots ; borne18–133 relue, registre signé, pret/verifier018 et029 autorisés, verrou acquis. Écritures exclusivement codex-LOTS-html/.

Deux leçons renforcées : LOT018 DX6 occlusion veineuse rétinienne et LOT029 DX6 craniosténose.14parties et14réponses chacune ; relecture interne réelle, pas de contrelecture indépendante ni validation clinique humaine. Les12leçons précédentes restent identiques. Cumul14/244,230restantes. Aucun nouveau lot terminé :22lots018–039 rédigés,040 PhaseA/DX1. Ne pas refaire la production initiale018 au commit950a4cd1.

Sources CH HUG/Paediatrie2023/CHUV, puis UE COUF2025, RCOphth2022 et guide néerlandais2021, dans les sections consignées. AIPS Eylea62393002 local relu pour occlusion veineuse ; deux fenêtres thérapeutiques identiques, pas de dose nouvelle ni certification de fraîcheur distante. Lectures et limites : renforcement_solo_dx6_20261101/LECTURES.json.

Images : aucun nouveau cliché intégré. Notice Commons Branch_retinal_vein_occlusion.jpg lue, auteurs etCC BY2.0 identifiés. Acquisition directe refusée par tunnel403 ; aucun pixel vu, aucune annotation. Guide craniosténoseCC BY-NC-ND exclu pour ses figures. RevuesPMC8467503/PMC10887665 simples pistes à vérifier. Schéma rétinien conceptuel antérieur préservé ; contraste sombre corrigé. Rattrapage iconographique incomplet. Réponses web exactes en cache local ignoré, notes/liens publiés.

Contrôles :550conditionsV8 sur22fichiers,242autres leçons/9harnais intacts. Chromium8configurations,112fenêtres,112réponses,8définitions ;8captures partie9 inspectées. Répétition ajoutée corrigée, accent normalisé ; audit langue historique encore non conforme à certaines règles incompatibles avecV8. Inventaire244leçons/{I['totaux']['passages']}passages actualisé. Mesures : {measures}. Base DD sous9Ko ; HTML complet distinct du plafond.

Suite :018 DX7 puis029 DX7 ; clichés manquants DX6 et antérieurs.040 DX2 suspendu pendant le rattrapage. Veilles locales37511/48342 existantes, contrôle chaque60s pendant le runtime, sans rédaction ; aucune veille concurrente. Le contrôleur générique continue de signaler la pause des nouveaux diagnostics, sans masquer son alerte. Verrou détenu pour publication ; état final dans ETAT_CONTINUITE.json et JOURNAL_PASSES.jsonl.

Modèle : famille GPT-6 exposée ; variante et effort courants non exposés. Astra ultra historiquement confirmé, high recommandé ; aucun changement de réglage revendiqué.

## Historique daté conservé

'''
p=B/'REPRISE_CODEX.md';p.write_text(intro+p.read_text())
e={'date':now,'mode':'solo','sous_agents':0,'actions':['reprise fraîche, verrou et registre','lectures CH puis UE, AIPS local','rédaction deuxDX6','relecture28parties/28réponses, corrections','550conditionsV8, langue avant/après','Chromium8configurations/8captures inspectées','candidatBRVO sousCC BY2, acquisition403','tri578passages et checkpoint'],'publication':'en préparation'}
with (D/'JOURNAL_PASSES.jsonl').open('a') as f:f.write(json.dumps(e,ensure_ascii=False)+'\n')
with (B/'JOURNAL_CODEX.md').open('a') as f:f.write(f'\n{now} — Solo DX6 : occlusion veineuse018 et craniosténose029 renforcées.28parties/28réponses relues,550conditionsV8,8configurationsChromium,8captures inspectées. Cumul14/244 ; aucune nouvelle image ni lot clos. Publication en préparation.\n')
for n in (18,29):
 with (B/f'LOT_{n:03}/JOURNAL.md').open('a') as f:f.write(f'\n{now} — DX6 renforcé,14parties/14réponses relues en interne. Preuves ../{D.name}/. Dix autres leçons du lot inchangées ; pas de cliché nouveau ni de validation indépendante.\n')
 for poste in ('redacteur','relecture-interne','controle-v8','transversale-interne'):
  e={'horodatage':now,'lot':f'LOT_{n:03}','fichier':'DX.6@renforcement-solo-20261101','poste':poste,'modele':'GPT-6 — famille exposée ; variante non exposée','effort':'réglage courant non exposé ; high recommandé','independant':False,'raison':'Passe réellement effectuée sur DX6 ; preuves '+D.name+'/ ; Astra ultra historique, aucun changement.'}
  with (B/'ROUTAGE_CODEX.jsonl').open('a') as f:f.write(json.dumps(e,ensure_ascii=False)+'\n')
print('Checkpoint préparé, publication non revendiquée.')
