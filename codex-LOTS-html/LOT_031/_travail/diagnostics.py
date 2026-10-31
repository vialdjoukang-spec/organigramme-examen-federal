from format_lecon import table
DIAGNOSTICS=[
('Rhinite allergique','Fréquente ; asthme et retentissement à rechercher.','Obstruction fluctuante, prurit, éternuements et exposition.','Histoire concordante ; sensibilisation seule insuffisante.'),
('Rhinite virale aiguë','Fréquente ; tolérance selon âge et terrain.','Contexte respiratoire aigu, écoulement, amélioration progressive.','Clinique ; réévaluer aggravation et signes focaux.'),
('Rhinite médicamenteuse','Cause iatrogène à rechercher.','Usage prolongé de vasoconstricteur et congestion rebond.','Reconstituer spécialité, dose et durée ; organiser arrêt.'),
('Déviation de la cloison nasale','Anomalie fréquente, pas toujours symptomatique.','Gêne fixe ou asymétrique, histoire de croissance ou traumatisme.','Concordance anatomie–symptômes ; décision opératoire individualisée.'),
('Rhinosinusite chronique avec polypes','Chronicité ; asthme et perte d’odorat associés.','Symptômes au moins douze semaines, polypes bilatéraux.','Endoscopie ; ne pas banaliser une masse unilatérale.'),
('Hypertrophie adénoïdienne','Surtout enfant ; sommeil et audition.','Respiration buccale, ronflement, gêne nasale et parfois otites.','Rhinopharynx, oreilles et retentissement à évaluer.'),
('Corps étranger nasal','🚩 Pile bouton ou aimants dangereux.','Obstruction ou écoulement unilatéral, parfois fétide ou sanglant.','Localisation et extraction adaptée ; urgence si objet dangereux.'),
('Hématome de la cloison nasale','🚩 Urgence ORL après traumatisme ou chirurgie.','Obstruction avec tuméfaction septale molle, souvent bilatérale.','Examen intranasal et drainage urgent spécialisé.'),
('Atrésie des choanes','🚩 Forme bilatérale néonatale : urgence respiratoire.','Obstruction congénitale ; forme unilatérale parfois tardive.','Sécuriser ventilation avant bilan endoscopique et imagerie.'),
('Tumeur maligne nasosinusienne','🚩 Exploration rapide des signes suspects.','Obstruction unilatérale persistante, sang, douleur ou déficit.','Endoscopie, imagerie et biopsie organisée.')]
def comparison():
 return table(['Diagnostic','Contexte et gravité','Orientation','Décision'],[[f'<a href="LOT_031_Phase_B_V0_DX.{i}.html">DX.{i} — {d[0]}</a>',*d[1:]] for i,d in enumerate(DIAGNOSTICS,1)])
