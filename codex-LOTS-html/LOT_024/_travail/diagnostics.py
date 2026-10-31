from format_lecon import table
DIAGNOSTICS=[
('Otite externe aiguë bactérienne','Douleur au tragus, conduit inflammatoire après humidité ou traumatisme local.','Évaluer le tympan avant toute préparation locale.'),
('Otite moyenne aiguë perforée','Otalgie aiguë puis écoulement purulent, parfois soulagement de la douleur.','Rechercher mastoïdite, altération générale et contexte pédiatrique.'),
('Otite moyenne chronique suppurée sans cholestéatome','Écoulements récidivants avec perforation ancienne et hypoacousie.','Bilan ORL et auditif ; exclure un cholestéatome.'),
('Cholestéatome de l’oreille moyenne','Otorrhée persistante parfois fétide, débris kératiniques ou poche de rétraction.','Potentiel destructeur ; prise en charge ORL, souvent chirurgicale.'),
('Otomycose','Prurit, plénitude et débris évocateurs, parfois après antibiotiques locaux.','Nettoyage sous contrôle et choix local adapté au tympan.'),
('Dermatite eczémateuse du conduit auditif','Prurit, desquamation et suintement associés à une irritation ou allergie.','Rechercher surinfection et sensibilisation aux gouttes ou dispositifs.'),
('Corps étranger du conduit auditif','Écoulement unilatéral, corps visible ou insertion parfois non rapportée.','E : pile bouton, retrait immédiat sans irrigation.'),
('Perforation tympanique traumatique','Douleur ou saignement après instrument, pression ou choc.','Vertige ou surdité importante imposent une évaluation urgente.'),
('Otite externe nécrosante','Douleur profonde persistante, souvent nocturne, terrain diabétique ou immunodéprimé.','E : suspicion d’infection invasive de la base du crâne ; avis urgent.'),
('Fuite otologique de liquide cérébrospinal','Écoulement clair après traumatisme ou chirurgie, parfois sans déclencheur évident.','E : risque intracrânien et infectieux ; bilan urgent spécialisé.')]
def comparison():
 return table(['Diagnostic','Orientation','Vigilance'],[[f'<a href="LOT_024_Phase_B_V0_DX.{i}.html">DX.{i} — {x[0]}</a>',x[1],x[2]] for i,x in enumerate(DIAGNOSTICS,1)])
