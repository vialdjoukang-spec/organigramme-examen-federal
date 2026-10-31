from format_lecon import table
DIAGNOSTICS=[
('Paralysie faciale idiopathique de Bell','Faiblesse unilatérale supérieure et inférieure rapidement progressive.','Diagnostic d’élimination après examen neurologique, oculaire et otologique.','Protéger la cornée ; une présentation atypique impose une autre recherche.'),
('Accident vasculaire cérébral avec déficit facial','Déficit soudain, souvent avec autre signe neurologique.','Imagerie cérébrale et vasculaire dans la filière urgente.','L’atteinte du front n’exclut pas une origine vasculaire.'),
('Paralysie faciale zostérienne','Otalgie, vésicules auriculaires, parfois signes auditifs ou vestibulaires.','Examen ORL et neurologique ; bilan adapté si forme sans éruption.','Chercher les vésicules, protéger l’œil et traiter précocement.'),
('Neuroborréliose de Lyme avec atteinte faciale','Exposition compatible, déficit parfois bilatéral, douleurs radiculaires ou méningées.','Clinique et examens sérologiques/liquidiens concordants.','Une sérologie positive isolée ne démontre pas une neuroborréliose active.'),
('Fracture mandibulaire','Traumatisme, douleur, malocclusion ou trouble de sensibilité du menton.','Examen dentaire et osseux, imagerie adaptée.','Rechercher lésions associées et menace respiratoire.'),
('Fracture zygomatico-orbitaire','Aplatissement de la pommette, diplopie ou hypoesthésie de la joue après choc.','Examen ophtalmologique et imagerie du massif facial.','Une baisse visuelle ou une incarcération modifie l’urgence.'),
('Cellulite cervico-faciale odontogène','Tuméfaction douloureuse liée à une dent, parfois trismus et fièvre.','Examen dentaire, recherche de collection et d’extension profonde.','Plancher buccal gonflé, dysphagie ou dyspnée signalent une menace.'),
('Tumeur parotidienne','Masse préauriculaire ou sous-auriculaire persistante.','Imagerie et prélèvement planifié par le spécialiste.','Une paralysie faciale associée est suspecte ; l’absence de douleur ne rassure pas.'),
('Angioœdème facial','Gonflement des lèvres ou du visage, parfois langue et pharynx.','Diagnostic clinique urgent puis bilan du mécanisme.','Protéger les voies aériennes et distinguer anaphylaxie et mécanisme bradykinique.'),
('Microsomie craniofaciale','Asymétrie développementale avec hypoplasie mandibulaire et anomalies auriculaires possibles.','Bilan clinique et fonctionnel multidisciplinaire.','Une anomalie ancienne peut compromettre audition, alimentation ou respiration.')]
def comparison():
 return '<h3>Dix diagnostics retenus</h3><p>Ordre pédagogique, sans classement de prévalence démontré pour ce symptôme composite.</p>'+table(['Diagnostic','Orientation','Confirmation','Priorité'],[[f'<a href="LOT_020_Phase_B_V0_DX.{i}.html">DX.{i} — {n}</a>',a,b,c] for i,(n,a,b,c) in enumerate(DIAGNOSTICS,1)])
