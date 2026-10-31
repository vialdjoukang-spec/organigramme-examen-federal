from format_lecon import table
DIAGNOSTICS=[
('Cervicalgie commune non spécifique','Usuelle ; retentissement fonctionnel variable.','Douleur axiale, lien avec mouvement, sans alarme ni déficit.','Diagnostic clinique réévalué ; activité adaptée.'),
('Radiculopathie cervicale dégénérative','Cause neurologique ; urgence si déficit moteur progressif.','Douleur du bras, paresthésies et signes radiculaires concordants.','Examen neurologique ; IRM selon déficit et évolution.'),
('Myélopathie cervicale dégénérative','🚩 Risque de handicap médullaire.','Mains maladroites, marche perturbée, signes pyramidaux.','IRM et avis rachidien rapide ; urgence si aggravation aiguë.'),
('Fracture du rachis cervical','🚩 Instabilité et lésion médullaire possibles.','Traumatisme, douleur médiane ; parfois choc mineur sur rachis fragile.','Protection du rachis et imagerie selon évaluation.'),
('Méningite bactérienne aiguë','🚩 Urgence vitale infectieuse.','Fièvre, céphalée, raideur, altération de conscience ; tableau incomplet possible.','Hospitalisation ; prélèvements et antibiothérapie sans retard dangereux.'),
('Hémorragie sous-arachnoïdienne','🚩 Urgence neurovasculaire.','Céphalée brutale, parfois raideur et vomissements.','Imagerie cérébrale urgente ; bilan complémentaire selon délai et suspicion.'),
('Dissection artérielle cervicale','🚩 Risque d’ischémie cérébrale.','Douleur inhabituelle, syndrome de Horner ou signes neurologiques.','Imagerie vasculaire et filière neurovasculaire.'),
('Spondylodiscite cervicale','🚩 Infection rachidienne ; abcès et compression possibles.','Douleur persistante, terrain infectieux ; fièvre inconstante.','IRM, hémocultures et prise en charge interdisciplinaire.'),
('Syndrome de la dent couronnée','Cause microcristalline, surtout chez la personne âgée.','Cervicalgie aiguë haute, rotation limitée, syndrome inflammatoire.','Scanner ciblé ; ne pas méconnaître infection ou autre urgence.'),
('Subluxation atlanto-axoïdienne rhumatoïde','🚩 Instabilité inflammatoire et menace médullaire.','Polyarthrite ancienne, douleur cervicale haute, signes neurologiques possibles.','Avis spécialisé ; éviter mobilisation forcée.')]
def comparison():
 return table(['Diagnostic','Contexte et gravité','Orientation','Décision'],[[f'<a href="LOT_032_Phase_B_V0_DX.{i}.html">DX.{i} — {d[0]}</a>',*d[1:]] for i,d in enumerate(DIAGNOSTICS,1)])
