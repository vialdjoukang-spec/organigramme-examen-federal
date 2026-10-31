from format_lecon import table
DIAGNOSTICS=[
('Épistaxis antérieure essentielle','Point septal antérieur et contexte local, après recherche des causes.','Ne pas clore le bilan d’une récidive unilatérale.'),
('Fracture des os propres du nez','Traumatisme, déformation et obstruction.','Chercher hématome septal et lésions faciales associées.'),
('Corps étranger nasal','Rhinorrhée unilatérale fétide ou objet connu.','Pile bouton : extraction urgente.'),
('Épistaxis favorisée par un traitement antithrombotique','Anticoagulant ou antiagrégant et risque hémorragique accru.','Ne pas interrompre automatiquement un traitement nécessaire.'),
('Perforation de la cloison nasale','Croûtes, saignements et parfois sifflement.','Rechercher traumatisme, geste, exposition ou cause inflammatoire.'),
('Purpura thrombopénique immunologique','Saignements cutanéomuqueux et thrombopénie.','Une baisse des plaquettes n’établit pas seule la cause immune.'),
('Maladie de von Willebrand','Histoire personnelle ou familiale de saignements muqueux.','Bilan spécialisé du facteur, pas seul bilan standard.'),
('Maladie de Rendu-Osler','Épistaxis récurrentes, télangiectasies et contexte familial possible.','Rechercher anémie et atteintes viscérales.'),
('Angiofibrome nasopharyngien juvénile','Obstruction et épistaxis chez un adolescent, surtout masculin.','Masse vasculaire : pas de biopsie improvisée.'),
('Cancer des fosses nasales ou des sinus','Saignement récidivant unilatéral avec obstruction persistante.','Bilan endoscopique, imagerie et prélèvement planifié.')]
def comparison():
 return table(['Diagnostic','Orientation','Vigilance'],[[f'<a href="LOT_021_Phase_B_V0_DX.{i}.html">DX.{i} — {x[0]}</a>',x[1],x[2]] for i,x in enumerate(DIAGNOSTICS,1)])
