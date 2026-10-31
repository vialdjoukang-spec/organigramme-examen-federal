from format_lecon import table
DIAGNOSTICS=[
('Sténose œsophagienne peptique','Dysphagie surtout aux solides dans un contexte de reflux.','Ne pas présumer une cause bénigne sans bilan endoscopique.'),
('Dysphagie oropharyngée après accident vasculaire cérébral','Trouble d’initiation, toux ou fausses routes parfois silencieuses.','Déficit récent : filière AVC ; sécurité de déglutition avant toute prise orale.'),
('Cancer de l’œsophage','Dysphagie progressive, amaigrissement ou autres signes d’alarme.','Endoscopie avec prélèvements et bilan rapide.'),
('Œsophagite à éosinophiles','Dysphagie intermittente aux solides, impactions, contexte atopique possible.','Biopsies même si l’endoscopie paraît normale.'),
('Achalasie','Dysphagie aux solides et liquides, régurgitations.','Exclure obstacle et pseudo-achalasie ; manométrie spécialisée.'),
('Impaction alimentaire œsophagienne','Blocage brutal au cours d’un repas.','Salive impossible à avaler : obstruction complète, endoscopie en urgence.'),
('Diverticule de Zenker','Régurgitations et dysphagie cervicale, résidus et fausses routes.','Bilan anatomique spécialisé avant instrumentation adaptée.'),
('Dysphagie de la maladie de Parkinson','Déglutition lente ou inefficace, risque respiratoire et nutritionnel.','Ne pas se fier uniquement à la plainte ou à l’absence de toux.'),
('Myasthénie auto-immune','Faiblesse fatigable, symptômes bulbaires parfois oculaires associés.','Dyspnée ou difficulté de gestion des sécrétions : urgence.'),
('Obstruction aiguë des voies aériennes par corps étranger','Étouffement brutal avec toux inefficace ou impossibilité de parler.','Gestes de désobstruction et appel immédiat au 144.')]
def comparison():
 return table(['Diagnostic','Orientation','Vigilance'],[[f'<a href="LOT_023_Phase_B_V0_DX.{i}.html">DX.{i} — {x[0]}</a>',x[1],x[2]] for i,x in enumerate(DIAGNOSTICS,1)])
