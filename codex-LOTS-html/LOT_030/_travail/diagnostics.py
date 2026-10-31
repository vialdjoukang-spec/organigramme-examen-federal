from format_lecon import table
DIAGNOSTICS=[
('Rhinite virale aiguë','Fréquente, généralement spontanément résolutive.','Contexte respiratoire aigu, amélioration progressive.','Clinique ; rechercher complications si évolution atypique.'),
('Rhinite allergique','Fréquente, retentissement et asthme à rechercher.','Prurit, éternuements, rhinorrhée aqueuse et exposition concordante.','Histoire compatible ; tests ciblés si utiles.'),
('Rhinite non allergique','Hétérogène, souvent chronique.','Déclencheurs irritants, thermiques ou alimentaires ; médicaments.','Exclusion raisonnée des causes allergiques et structurelles.'),
('Rhinosinusite aiguë postvirale','Réévaluer selon évolution.','Persistance au-delà de dix jours ou aggravation après cinq jours.','Ne signifie pas automatiquement infection bactérienne.'),
('Rhinosinusite aiguë bactérienne','🚩 Complications orbitaires et intracrâniennes possibles.','Faisceau de sévérité, douleur, fièvre, évolution biphasique.','Antibiothérapie selon indication ; urgence si complication.'),
('Rhinosinusite chronique sans polypes','Chronique, retentissement à évaluer.','Symptômes au moins douze semaines, sans polypes visibles.','Confirmation objective par endoscopie ou imagerie selon bilan.'),
('Rhinosinusite chronique avec polypes','Asthme et intolérances associées possibles.','Obstruction, écoulement et perte d’odorat ; polypes bilatéraux.','Endoscopie ; masse unilatérale atypique à explorer.'),
('Corps étranger nasal','🚩 Pile bouton ou aimants : urgence.','Écoulement unilatéral fétide ou sanglant chez l’enfant.','Localiser et extraire par une équipe équipée.'),
('Fuite nasale de liquide cérébrospinal','🚩 Risque de méningite et contexte traumatique.','Écoulement aqueux souvent unilatéral, positionnel.','Biomarqueur du liquide et localisation spécialisée.'),
('Tumeur maligne nasosinusienne','🚩 Orientation spécialisée rapide.','Symptômes unilatéraux persistants, sang, douleur ou déficit.','Endoscopie, imagerie puis prélèvement organisé.')]
def comparison():
 return table(['Diagnostic','Contexte et gravité','Orientation','Décision'],[[f'<a href="LOT_030_Phase_B_V0_DX.{i}.html">DX.{i} — {d[0]}</a>',*d[1:]] for i,d in enumerate(DIAGNOSTICS,1)])
