from format_lecon import table
DIAGNOSTICS=[
('Blépharospasme essentiel','Fermetures bilatérales synchrones et stéréotypées.','Rechercher une cause secondaire et un geste antagoniste.'),
('Myokymie palpébrale','Frémissement localisé, souvent favorisé par fatigue ou stimulants.','Réévaluer si persistance, extension ou autre symptôme.'),
('Sécheresse oculaire','Brûlure, grain de sable et gêne de surface.','Peut coexister avec une dystonie.'),
('Blépharite','Bords palpébraux inflammatoires et croûtes.','Rechercher atteinte de surface et dysfonction meibomienne.'),
('Spasme hémifacial','Contractions d’un côté avec atteinte du bas du visage.','Ne pas l’appeler blépharospasme bilatéral asymétrique sans examen.'),
('Tic moteur palpébral','Mouvements brefs, parfois précédés d’une envie et temporairement retenus.','Rechercher autres tics et contexte évolutif.'),
('Dystonie palpébrale médicamenteuse','Lien temporel possible avec un médicament, autres mouvements associés.','Distinguer forme aiguë et tardive, sans arrêt autonome du traitement.'),
('Apraxie de l’ouverture des paupières','Difficulté à initier la réouverture sans spasme évident.','Peut accompagner dystonie ou maladie neurologique.'),
('Corps étranger cornéen ou abrasion cornéenne','Douleur et larmoiement après exposition ou traumatisme.','Exclure une plaie pénétrante avant les manipulations.'),
('Kératite aiguë','Œil rouge douloureux, photophobie et possible baisse visuelle.','Avis ophtalmologique urgent, surtout avec lentilles ou infiltrat.')]
def comparison():
 return table(['Diagnostic','Orientation','Vigilance'],[[f'<a href="LOT_022_Phase_B_V0_DX.{i}.html">DX.{i} — {x[0]}</a>',x[1],x[2]] for i,x in enumerate(DIAGNOSTICS,1)])
