from format_lecon import table
DIAGNOSTICS=[
('Pharyngite aiguë','Douleur pharyngée, signes respiratoires ou exsudat amygdalien.','Exclure obstruction, abcès et risque particulier avant le score de Centor.'),
('Stomatite aphteuse récidivante','Ulcères douloureux récidivants avec intervalles de guérison.','Une lésion persistante unique ou des signes systémiques changent le bilan.'),
('Candidose buccale','Plaques détachables ou muqueuse érythémateuse sur terrain favorisant.','Dysphagie, odynophagie et immunodépression nécessitent une évaluation élargie.'),
('Gingivostomatite herpétique','Fièvre, gingivite diffuse et lésions vésiculo-ulcéreuses.','Vérifier hydratation, œil, terrain et signes neurologiques.'),
('Ulcération buccale traumatique','Lésion au contact d’une dent, d’une prothèse ou après morsure.','La disparition après correction doit être vérifiée ; une cause apparente ne suffit pas.'),
('Xérostomie médicamenteuse','Sécheresse apparue ou aggravée avec une exposition médicamenteuse.','Ne pas interrompre seul un traitement essentiel ; rechercher les autres causes.'),
('Maladie de Sjögren','Sécheresse buccale et oculaire, avec possibles manifestations systémiques.','Une tuméfaction glandulaire nouvelle ou des adénopathies imposent un bilan.'),
('Sialolithiase sous-mandibulaire','Douleur et gonflement sous-mandibulaires rythmés par les repas.','Fièvre, pus, tuméfaction du plancher ou gêne respiratoire suggèrent une complication.'),
('Abcès périamygdalien','Odynophagie unilatérale, trismus, voix étouffée et bombement du voile.','Avis ORL urgent ; les voies aériennes priment sur l’imagerie.'),
('Carcinome épidermoïde buccal ou oropharyngé','Ulcère, masse ou gêne persistante, parfois adénopathie cervicale.','Induration, saignement, otalgie référée ou amaigrissement accélèrent le bilan.')]
def comparison():
 return table(['Diagnostic','Orientation','Vigilance'],[[f'<a href="LOT_025_Phase_B_V0_DX.{i}.html">DX.{i} — {a}</a>',b,c] for i,(a,b,c) in enumerate(DIAGNOSTICS,1)])
