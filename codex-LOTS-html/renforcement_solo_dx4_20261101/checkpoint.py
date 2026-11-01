from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
D=Path(__file__).resolve().parent;B=D.parent;now=datetime.now(timezone.utc).isoformat(timespec='seconds')
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
C=json.loads((D/'CONTROLE.json').read_text());Q=json.loads((D/'qa/CONTROLE_NAVIGATEUR.json').read_text())
for r in Q['rendus']:assert hashlib.sha256((B/r['fichier']).read_bytes()).hexdigest()==r['sha256']
s=json.loads((B/'ETAT_CONTINUITE.json').read_text());s['renforcement_medical_passe_precedente_dx3']=s['renforcement_medical'];r=dict(s['renforcement_medical'])
r.update(statut='DX4 contrôlés ; publication en préparation',preuve_base=f'{D.name}/BASELINE.json',fichiers_renforces_valides=10,parties_relues=140,questions_reponses_relues=140,preuves=D.name+'/',reste_lecons_a_renforcer=234,date=now,prochaines_lecons=['LOT_018/LOT_018_Phase_B_V0_DX.5.html','LOT_029/LOT_029_Phase_B_V0_DX.5.html'],contrelecture_distincte_portee='6 leçons précédentes seulement ;4 DX3/DX4 relus en interne',commit=None,push_confirme=False,publication_verifiee_le=None,verrou_libere_le=None)
r['tranche_fichiers']=r['tranche_fichiers']+[x['fichier'] for x in C['lecons']]
r['qa']={'preuve':f'{D.name}/qa/CONTROLE_NAVIGATEUR.json','configurations':len(Q['rendus']),'ouvertures_fenetres_directes':sum(x['fenetres_directes'] for x in Q['rendus']),'ouvertures_reponses':sum(x['reponses_ouvertes'] for x in Q['rendus']),'ouvertures_definitions':sum(x['definitions_ouvertes'] for x in Q['rendus']),'captures_inspectees':8}
r['cette_passe']={'lecons':2,'parties':28,'questions_reponses':28,'nouvelles_images_acquises':0,'images_reutilisees':0,'schema_preexistant_preserve':1,'contrelecture_independante':False,'v8':550,'navigateur':True,'captures_inspectees':8}
s['renforcement_medical']=r;s['verrou']='détenu pour publication';s['prochaine_action']='Poursuivre seul LOT018 DX5 puis LOT029 DX5 ; clichés lésionnels manquants. Premier nouveau diagnostic LOT040 DX2 après rattrapage.'
s['verification_reprise_solo_dx4']={'date':now,'checkpoint_frais':C['base'],'branche':'codex/lots','plage_fraiche':[18,133],'registre_token':'4f3b52bb58','registre_signe':True,'pret_verifier':[18,29],'verrou_acquis':True,'sous_agents':0,'communs_intacts':9,'autres_lecons_intactes':242,'modele':'Famille GPT-6 exposée ; variante/effort actuels non exposés ; Astra ultra historique, high recommandé, aucun réglage changé.'}
s['balayage_imagerie_ecg'].update(date=now,passages=569,passages_tries=569,lecons_modifiees=2,statut='244 leçons recensées ;569 passages, tri actualisé pour les deux DX4.',preuves_campagne_actuelle=D.name+'/',portee_campagne='Deux DX4 renforcés et relus en interne ;242 autres leçons inchangées.',publication='en préparation',push_confirme=False,commit=None)
s['dernier_checkpoint_le']=now;s['dernier_commit_checkpoint']=C['base'];save(B/'ETAT_CONTINUITE.json',s)
measures=' ; '.join(x['fichier']+f" : HTML{x['octets_apres']/1000:.3f}Ko, base{x['texte_fiche_octets']/1000:.3f}Ko, fenêtres{x['texte_fenetres_octets']/1000:.3f}Ko" for x in C['lecons'])
intro=f'''# Reprise solo DX4 — {now}

Dernier ordre : seul, sans sous-agents ; aucun agent lancé. Dépôt frais fdd11b10, branche codex/lots, borne18–133 relue, registre signé, pret/verifier018 et029 autorisés, verrou acquis. Écritures exclusivement codex-LOTS-html/.

Deux leçons renforcées : LOT018 DX4 glaucome et LOT029 DX4 hématome sous-dural.14parties et14réponses chacune ; relecture interne explicite, pas de contrelecture indépendante ni validation clinique humaine. Les huit leçons déjà renforcées demeurent identiques ; cumul10/244,234 restantes. Aucun nouveau lot terminé.22lots018–039 rédigés ;040 PhaseA/DX1. Ne pas refaire la production initiale018 au commit950a4cd1.

Sources CH puis UE lues : HUG, Paediatrie Suisse, EGS6 conservé et passage officiel sur la cible, Raissaki XML, paragraphe pédiatrique NICE indexé. AIPS Xalatan53675 local relu, fenêtres exactes préservées. Nouvelle fenêtre partie13 glaucome ; schéma inchangé, contraste sombre corrigé. Aucune image nouvelle : miroirs DNB/WhiteRose refusés403 ; licence article PAPILA non transposée au dataset. Clichés glaucomateux et sous-duraux toujours manquants.

Contrôles :550 conditions V8 sur22fichiers ;242autres leçons/9harnais intacts. Chromium8configurations,112fenêtres,112réponses,12définitions ;8captures partie9 inspectées, autres captures conservées sans allégation d’inspection. Audit langue historique non conforme à ses règles anciennes ; une phrase scindée. Inventaire244leçons/569passages actualisé. Mesures : {measures}. Base DD sous9Ko ; fichier complet distinct de ce plafond.

Preuves : renforcement_solo_dx4_20261101/ ; contrôleur courant dans ce dossier et imagerie_20261101/verifier.py. Anciennes preuves conservées, leurs baselines ne décrivent pas les nouveaux DX4. Bilan BILAN_RENFORCEMENT_MEDICAL.html. Suite :018 DX5 puis029 DX5, acquisitions et lacunes antérieures.040DX2 suspendu pendant le rattrapage. Veilles37511/48342 chaque60s, contrôle seul pendant le runtime. Verrou détenu pour publication ; état final dans ETAT_CONTINUITE.json et JOURNAL_PASSES.jsonl.

Modèle : famille GPT-6 exposée ; variante/effort courants non exposés. Astra ultra historique, high recommandé. Aucun réglage modifié. Incident : déconnexion ponctuelle exec, reprise réussie sans perte de fichiers ni arrêt des veilles.

## Historique daté conservé

'''
p=B/'REPRISE_CODEX.md';p.write_text(intro+p.read_text())
e={'date':now,'mode':'solo','sous_agents':0,'actions':['verrou et registre','lectures CH puis UE','deux accès images403','rédaction enrichir.py','relecture28parties/28réponses','correction langue et contraste','V8 et langue avant/après','Chromium8configurations,8captures inspectées','tri569passages et checkpoint'],'publication':'en préparation'}
with (D/'JOURNAL_PASSES.jsonl').open('a') as f:f.write(json.dumps(e,ensure_ascii=False)+'\n')
with (B/'JOURNAL_CODEX.md').open('a') as f:f.write(f'\n{now} — Solo DX4 : glaucome018 et hématome sous-dural029 renforcés,28parties/28réponses relues.550conditionsV8 ;8configurations/8captures inspectées. Cumul10/244. Deux accès images403, aucun cliché nouveau ni lot clos. Publication en préparation.\n')
for n in (18,29):
 with (B/f'LOT_{n:03}/JOURNAL.md').open('a') as f:f.write(f'\n{now} — DX4 renforcé,14parties/14réponses relues en interne. Preuves ../{D.name}/. Autres dix leçons inchangées ; aucune image nouvelle ni validation indépendante.\n')
 for poste in ['redacteur','relecture-interne','controle-v8','transversale-interne']:
  e={'horodatage':now,'lot':f'LOT_{n:03}','fichier':'DX.4@renforcement-solo-20261101','poste':poste,'modele':'GPT-6 — famille exposée ; variante non exposée','effort':'réglage courant non exposé ; high recommandé','independant':False,'raison':'Passe réellement effectuée sur DX4 ; preuves '+D.name+'/ ; Astra ultra historique, aucun changement.'}
  with (B/'ROUTAGE_CODEX.jsonl').open('a') as f:f.write(json.dumps(e,ensure_ascii=False)+'\n')
print('Checkpoint préparé ; publication non revendiquée.')
