from format_lecon import table
DIAGNOSTICS=[
('Otite externe aiguë bactérienne','Douleur au tragus, conduit inflammatoire, parfois écoulement.','Évaluer tympan, extension et terrain.'),
('Otite moyenne aiguë','Otalgie récente, tympan bombé et épanchement inflammatoire.','Rechercher mastoïdite et altération générale ; antibiothérapie individualisée.'),
('Bouchon de cérumen','Obstruction visible avec gêne ou impossibilité d’examiner le tympan.','Ne pas expliquer toute douleur par le cérumen ; extraction adaptée au tympan.'),
('Barotraumatisme de l’oreille moyenne','Douleur liée à un vol, une plongée ou un changement de pression.','Surdité brusque et vertige imposent de rechercher une atteinte interne.'),
('Corps étranger du conduit auditif','Objet visible, douleur, hypoacousie ou écoulement unilatéral.','Pile bouton : retrait immédiat ; pas d’irrigation.'),
('Zona otique avec paralysie faciale','Otalgie, vésicules et paralysie faciale périphérique.','Les signes peuvent être décalés ; protéger la cornée et évaluer l’audition.'),
('Otite externe nécrosante','Douleur profonde persistante, souvent nocturne, avec inflammation du conduit.','Diabète, immunodépression, granulations ou atteinte des nerfs crâniens : avis urgent.'),
('Trouble temporo-mandibulaire douloureux','Douleur reproduite par mastication ou palpation articulaire et musculaire.','Écarter infection, luxation et symptômes d’artérite à cellules géantes.'),
('Abcès dentoalvéolaire','Dent causale, douleur à la mastication, tuméfaction ou drainage.','Traiter le foyer ; extension au plancher, dysphagie ou sepsis : urgence.'),
('Carcinome épidermoïde oropharyngé','Otalgie unilatérale persistante, parfois oreille normale et gêne pharyngée.','Masse cervicale, odynophagie, saignement ou amaigrissement : bilan rapide.')]
def comparison():
 return table(['Diagnostic','Orientation','Vigilance'],[[f'<a href="LOT_026_Phase_B_V0_DX.{i}.html">DX.{i} — {a}</a>',b,c] for i,(a,b,c) in enumerate(DIAGNOSTICS,1)])
