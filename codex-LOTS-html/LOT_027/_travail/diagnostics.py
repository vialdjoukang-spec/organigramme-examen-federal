from format_lecon import table
DIAGNOSTICS=[
('Pulpite dentaire','Douleur thermique ou spontanée, parfois mal localisée.','Soins dentaires causaux ; pas d’antibiotique pour une pulpite isolée.'),
('Abcès dentoalvéolaire','Dent causale, douleur à la percussion, tuméfaction ou pus.','🚩 Extension, plancher gonflé, trismus important ou dysphagie : urgence.'),
('Péricoronarite','Inflammation autour d’une dent partiellement sortie, souvent de sagesse.','Soins locaux ; rechercher extension et menace respiratoire.'),
('Trouble temporo-mandibulaire douloureux','Douleur reproduite par mouvement ou palpation musculaire et articulaire.','Ne pas attribuer une claudication avec signes visuels à l’articulation.'),
('Luxation mandibulaire','Bouche bloquée ouverte, fermeture impossible après grande ouverture ou traumatisme.','Réduction professionnelle ; rechercher fracture si traumatisme ou atypie.'),
('Fracture mandibulaire','Traumatisme, malocclusion, douleur, hématome ou hypoesthésie mentonnière.','🚩 Voies aériennes, traumatisme crânien et cervical d’abord.'),
('Névralgie du trijumeau','Décharges faciales brèves, déclenchées par un stimulus léger.','Bilan neurologique et IRM ; éviter des gestes dentaires sans lésion démontrée.'),
('Sinusite maxillaire aiguë','Douleur jugale ou dentaire supérieure avec symptômes nasaux.','🚩 Œil, méninges ou neurologie atteints : hospitalisation urgente.'),
('Abcès périamygdalien','Odynophagie souvent unilatérale, voix modifiée, bombement et parfois trismus.','🚩 Déglutition salivaire, hydratation et voies aériennes ; avis ORL urgent.'),
('Artérite à cellules géantes','Claudication de mâchoire après 50 ans, céphalée nouvelle ou signes visuels.','🚩 Traitement urgent si forte suspicion ; ne pas attendre la biopsie.')]
def comparison():
 return table(['Diagnostic','Orientation','Décision'],[[f'<a href="LOT_027_Phase_B_V0_DX.{i}.html">DX.{i} — {a}</a>',b,c] for i,(a,b,c) in enumerate(DIAGNOSTICS,1)])
