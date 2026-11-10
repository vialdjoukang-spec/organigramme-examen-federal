from pathlib import Path
import json,hashlib
B=Path('ChatGPT_Codex/LOT_083');D=B/'_travail/reprise/redaction_DX5_8/DX.8';F=D/'LOT_083_Phase_B_V0_DX.8.html';sha=hashlib.sha256(F.read_bytes()).hexdigest();assert sha=='0d9070dbfa585442f02f87e801295d4dbc50ae85c2e4a7a89c617a203012f091'
items=[
('Q1a',1,2,'Définition DGN nommée et principes EULAR2025 publiés2026 explicitement datés ; affection inflammatoire des ceintures.'),
('Q1b',1,2,'PPR/PMR, myalgie, myopathie et ACG distinguées ; classification et diagnostic séparés.'),
('Q2a',2,2,'Âge, sexe, gradient géographique, évolution, rechutes, autonomie et risques du traitement décrits ; association ACG correctement orientée.'),
('Q2b',2,1,'Estimations européennes territorialisées et revue2022 datée ; aucune incidence/prévalence nationale suisse établie, aucune extrapolation inventée.'),
('Q3a',3,2,'Recrutement leucocytaire, endothélium, immunité innée/adaptative et IL-6 reliés aux tissus périarticulaires puis à la clinique ; limites causales conservées.'),
('Q3b',3,2,'Tableau perturbation→exploration→thérapeutique ; pharmacologie nucléaire de prednisone/prednisolone, effets systémiques et maintien/rechute reliés.'),
('Q4a',4,2,'ACG conditionnelle menaçant la vision placée avant les imitateurs de PPR isolée.'),
('Q4b',4,2,'ACG, polyarthrite tardive, myosite et néoplasie ont leurs discriminants, pièges et conduites ; forte suspicion ACG traitée sans attendre la confirmation.'),
('Q5a',5,2,'Questions fonctionnelles, chronologie, traitements et terrain portent leur raison clinique ou physiopathologique.'),
('Q5b',5,2,'Trouble visuel, claudication, dysphagie et présentation réfractaire déclenchent des actions distinctes et explicites.'),
('Q6a',6,2,'Repère fonctionnel habituel sans douleur ni raideur invalidante avant anomalies ; comparaison actif/passif et limitations antérieures explicitées.'),
('Q6b',6,1,'Élévation active, mobilisation accompagnée, palpation et examen temporal sont décrits avec leur valeur ; technique de force contre résistance reste générique, sans méthode segmentaire reproductible.'),
('Q7',7,2,'Quatre syndromes numérotés, signes fonctionnels/physiques et fenêtres définissant raideur, claudication, symptômes visuels, synovite, bursite et ténosynovite.'),
('Q8a',8,2,'Critères EULAR/ACR2012 exacts : population d’entrée, points, durée>45min et seuils4/5 avec ou sans échographie.'),
('Q8b',8,2,'Classification explicitement distincte du diagnostic ; réponse aux glucocorticoïdes non utilisée comme essai diagnostique ; limites des marqueurs et CK expliquées.'),
('Q9a',9,2,'Absence de gold standard unique déclarée ; clinique et examens interprétés ensemble ; échographie des ceintures et stratégie vasculaire distinguées.'),
('Q9b',9,1,'Bilan initial, indication des examens et seconde intention interprétables ; normales chiffrées en unités SI et alternatives par terrain d’imagerie ne sont pas détaillées.'),
('Q10',10,2,'Branches urgence ACG, confirmation, induction, rechute et réfractarité aboutissent chacune à une décision ; rechute et sevrage distingués.'),
('Q11a',11,2,'Rémission sans glucocorticoïdes, repère10mg/j en1–2mois et objectif arrêt dans l’année explicitement individualisés et attribués EULAR.'),
('Q11b',11,2,'Confirmation puis induction orale, décroissance et éventuelle épargne spécialisée ; raison des restrictions et modalités de prise expliquée.'),
('Q11c',11,2,'Suspicion ACG→avis urgent, immédiat si menace visuelle→glucocorticoïdes sans attendre confirmation ; le schéma PPR ne remplace pas celui d’une ACG menaçante.'),
('Q11d',11,2,'15–25mg/j et décroissance sont exactement EULAR2026 ; AIPS prednisone générale distincte, voie orale et prise matinale avec repas conformes. Aucun schéma de PR transposé à la PPR pour sarilumab.'),
('Q11e',11,1,'Grossesse/allaitement, rein/foie, interactions, infections, surveillance et cinq conditions ambulatoires présents ; volet travail/assurances non développé au point11.'),
('Q12',12,2,'Primaire sans promesse étiologique, secondaire ACG et tertiaire complications ; mesures mediX suisses pour os, vaccins, contrôles et absence de prophylaxie cardiovasculaire automatique.'),
('Q13',13,2,'Six phrases verbales intactes et mémorisables couvrent diagnostic, ACG, traitement et suivi.'),
('Q14',14,2,'Questions avec réponse et raison sur classification, CK, urgence, doses, sevrage, statut suisse et marqueurs ; question finale littérale unique après correction technique.')]
assert len(items)==26;score=sum(x[2]for x in items);assert score==48
ctrl=json.loads((B/'audits/DX8_P3.controle.json').read_text())[0];ver=json.loads((B/'audits/DX8_P3.verifications.json').read_text())
limites=[
{'item':'Q2b','classe':'Moyen','emplacement':'dx8-p2','extrait_mot_pour_mot':'La valeur décrit les études suédoises reprises ; elle ne représente pas la population suisse','constat':'Les données nationales suisses ne sont pas produites ; le contexte européen est loyalement conservé.','correction_necessaire_au_franchissement':False,'source':'f8-1/f8-70 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC9796644/'},
{'item':'Q6b','classe':'Moyen','emplacement':'dx8-p6','extrait_mot_pour_mot':'Le mouvement et la résistance sont appréciés dans des conditions où la douleur est identifiée','constat':'Le geste de force est formulé de manière générale, sans position ni méthode segmentaire standardisée. La distinction douleur/déficit demeure correcte.','correction_necessaire_au_franchissement':False,'source':'f8-6/f8-11 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC9796644/'},
{'item':'Q9b','classe':'Moyen','emplacement':'dx8-p9','extrait_mot_pour_mot':'La CRP et la VS documentent une inflammation sans en établir l’étiologie','constat':'Interprétation correcte, mais pas de normales chiffrées SI ni de détail des alternatives d’imagerie par terrain. Ne pas inventer une plage ou une substitution universelle.','correction_necessaire_au_franchissement':False,'source':'f8-9/f8-18/f8-43/f8-44 ; https://ard.bmj.com/content/83/6/741'},
{'item':'Q11e','classe':'Moyen','emplacement':'dx8-p11','extrait_mot_pour_mot':'L’organisation ambulatoire suppose que l’urgence vasculaire a été évaluée, que la prescription est comprise et que le suivi est accessible','constat':'Les critères ambulatoires et le suivi sont explicites ; pas de volet spécifique capacité de travail/certification/assurances.','correction_necessaire_au_franchissement':False,'source':'f8-66/f8-21/f8-32 ; https://ard.eular.org/article/S0003-4967(26)00357-2/fulltext'}]
r={
 'type':'Première P3 indépendante','auditeur':'/root/sources_lot080','date':'2026-11-10','fichier':str(F),
 'version':{'octets':len(F.read_bytes()),'sha256':sha,'sha256_initial_lu':'5e395347106eef4c085cb47fe70fea57ea51fe37e2a280db2443b0308dd5efc4'},
 'reference':'037545b80fe03166dec9e05f70e24fb9f008821d : PROMPT_Casern/PROMPT_LOTS_Lo_9.11.26.claude.md Θ3',
 'methode':'A4 ciblé : fragments4/8/9/10/11 lus intégralement ; index et fragments dédiés pour les autres Q. Confrontation aux passages primaires réellement lus dans leurs caches EULAR2026, EULAR imagerie2023/24, EULAR/ACR2012, Lundberg2022, DGN2025, mediX2024 et AIPS françaises. Aucun HTML entier reçu à lire, aucun manuscrit modifié.',
 'independance':'Aucune rédaction ou correction de DX8 par cet auditeur. Le déplacement technique de citation a été réalisé par l’auteur ; sa réversibilité exacte a été vérifiée indépendamment.',
 'grille':[{'item':i,'point':p,'score':s,'maximum':2,'justification':j,'fragment':f'fragments/p{p:02d}.html'}for i,p,s,j in items],
 'somme':score,'maximum':52,'pourcentage':score/52*100,'seuil_pourcentage':90,'images_exclues':{'item':'Q9c','motif':'Images explicitement différées par Vial'},
 'point11':'Exactement cinq questions Q11a–Q11e ; situations spéciales, surveillance et sortie restent une seule question sur2.',
 'question_finale':'oui','porte_P3':'FRANCHIE','critiques':0,'graves':0,'corrections_obligatoires':[],'limites_grille_non_bloquantes':limites,
 'sources_cles_verifiees':[
  {'id':'f8-27','url':'https://ard.eular.org/article/S0003-4967(26)00357-2/fulltext','extrait':'In patients with a strong clinical suspicion of GCA, treatment with GC should be commenced without delay, while waiting for the results of confirmatory investigations.'},
  {'id':'f8-28','url':'https://ard.eular.org/article/S0003-4967(26)00357-2/fulltext','extrait':'at an initial dose of 15 to 25 mg/day, tapered to 10 mg/day within 1 to 2 months, with the aim of stopping GC within 1 year.'},
  {'id':'aips-f8-48','url':'https://www.swissmedicinfo-pro.ch/api/Medication/69640003/GetDokumentSectionItems','constat':'Notice Prednisone Galepharm : posologie générale5–60mg/j, dose minimale efficace, prise orale circadienne matinale avec ou après repas, arrêt progressif après exposition prolongée. Le cours attribue le protocole spécifique à EULAR.'},
  {'id':'aips-f8-47','constat':'Le libellé AIPS rhumatologique vise les poussées/exacerbations insuffisamment contrôlées par AINS, dont PPR. Ce libellé général n’est pas confondu avec le schéma spécifique EULAR ; aucune obligation nouvelle d’essai AINS n’est inventée dans cet audit.'},
  {'id':'aips-f8-49/50/51/52','constat':'Contre-indications et précautions infections/glaucome, CYP3A4, AINS, fluoroquinolones, sevrage, rein/foie et instruction suisse de ne pas allaiter conformes aux sections lues.'},
  {'id':'aips-f8-57','url':'https://www.swissmedicinfo-pro.ch/api/Medication/66424003/GetDokumentSectionItems','constat':'Kevzara : indication suisse PR dans la notice consultée ; aucune indication PPR ajoutée et aucune dose PR transférée.'},
  {'id':'f8-64','constat':'Tableau4 EULAR/ACR2012 relu : âge≥50ans, douleurs bilatérales épaules, CRP/VS anormale ; points2/1/2/1 et échographie1/1 ; seuils4/5.'},
  {'id':'f8-43/44/45','constat':'Échographie temporale+axillaire première imagerie sous expertise disponible ; imagerie sans retard au traitement et probabilité préalable interprétées ensemble.'}],
 'controle_independant':{'rapport':'DX8_P3.controle.json','verdict_brut':ctrl['verdict'],'defauts':{k:v['n']for k,v in ctrl['defauts'].items()},'aucun_A_C':not any(k.startswith(('A_','C_'))for k in ctrl['defauts']),'arbitrage':'Les49 alertes nominales regroupent des libellés de fenêtres et des verbes non reconnus ; une phrase longue37mots et la faible proportion de connecteurs restent du perfectionnement différé. Le rapport brut ORANGE est conservé ; aucun VERT revendiqué.'},
 'structure':ver,
 'correction_technique_verifiee':{'objet':'Citation f8-68 déplacée après le point d’interrogation de M1.3.','ancien_SHA_restitue_par_inverse':ver['ancien_SHA_restitue'],'identite_contenu_medical':ver['ancien_SHA_restitue']=='5e395347106eef4c085cb47fe70fea57ea51fe37e2a280db2443b0308dd5efc4','question_exacte_occurrences':ver['question_exacte']},
 'absence_mutation':'Aucun manuscrit, paquet, contrat ou fichier Git modifié par l’auditeur.'}
(B/'audits/DX8_P3.audit.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print('DX8 P3',score,'/52',r['pourcentage'],'finale',r['question_finale'],sha)
