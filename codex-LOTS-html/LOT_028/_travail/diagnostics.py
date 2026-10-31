from format_lecon import table
DIAGNOSTICS=[
('Bouchon de cérumen','Obstruction visible du conduit, gêne ou hypoacousie.','Vérifier l’audition après retrait ; une surdité brusque ne doit pas être banalisée.'),
('Otite moyenne avec épanchement','Liquide de l’oreille moyenne sans tableau infectieux aigu.','Retentissement sur langage et apprentissages ; cause persistante ou unilatérale à explorer.'),
('Otospongiose','Hypoacousie progressive, souvent de transmission, avec tympan peu modifié.','Audiométrie et bilan spécialisé ; appareillage ou chirurgie selon situation.'),
('Presbyacousie','Baisse progressive, plutôt symétrique, difficulté de compréhension dans le bruit.','Ne pas attribuer au vieillissement une asymétrie ou une baisse soudaine.'),
('Surdité induite par le bruit','Exposition professionnelle ou de loisir, aiguë ou répétée.','🚩 Baisse récente après bruit intense : évaluation rapide ; prévention des lésions irréversibles.'),
('Surdité brusque neurosensorielle','Baisse soudaine, parfois impression d’oreille bouchée ou acouphène.','🚩 Avis urgent sans attendre un audiogramme programmé ; rechercher AVC si signes associés.'),
('Maladie de Ménière','Vertiges récurrents avec audition fluctuante, acouphènes et plénitude.','Confirmer par bilan audiovestibulaire ; ne pas attribuer tout vertige aigu à Ménière.'),
('Schwannome vestibulaire','Hypoacousie neurosensorielle asymétrique, parfois acouphène unilatéral.','IRM selon signes et bilan ; décision multidisciplinaire.'),
('Cholestéatome','Hypoacousie avec otorrhée persistante ou récidivante et lésion tympanique.','🚩 Vertige, paralysie faciale ou signes neurologiques : rechercher complication.'),
('Fistule artérioveineuse durale','Acouphène pulsatile, parfois céphalée ou déficit neurologique.','🚩 Cause vasculaire à explorer ; urgence immédiate si signes neurologiques ou hémorragiques.')]
def comparison():
 return table(['Diagnostic','Présentation utile','Vigilance'],[[f'<a href="LOT_028_Phase_B_V0_DX.{i}.html">DX.{i} — {a}</a>',b,c] for i,(a,b,c) in enumerate(DIAGNOSTICS,1)])
