from format_lecon import table
DIAGNOSTICS=[
('Laryngite aiguë','Début récent, contexte infectieux, raucité.','Inflammation laryngée ; absence de signe de gravité.','Stridor, dysphagie majeure ou évolution inhabituelle imposent de revoir le diagnostic.'),
('Dysphonie fonctionnelle','Fatigue, effort, variabilité avec la tâche.','Évaluation du geste vocal après examen laryngé.','Une profession vocale ne prouve pas une origine fonctionnelle.'),
('Nodules vocaux','Forçage répété, fatigue et voix rauque.','Petites lésions généralement bilatérales en regard.','Différencier une lésion unilatérale et sa réaction de contact.'),
('Polype vocal','Dysphonie persistante, parfois après effort intense.','Lésion généralement unilatérale perturbant vibration ou fermeture.','Un aspect atypique nécessite une caractérisation et parfois une histologie.'),
('Laryngite chronique avec œdème de Reinke','Voix grave et rauque, exposition au tabac.','Œdème des plis vocaux dans un contexte d’irritation chronique.','Ne pas attribuer une lésion suspecte au seul tabagisme.'),
('Kyste vocal','Gêne persistante liée à une lésion sous-muqueuse.','Examen laryngé et étude de la vibration.','Un kyste peut être confondu avec un nodule ou un polype.'),
('Paralysie laryngée','Voix soufflée, fausses routes ou gêne inspiratoire.','Immobilité dynamique, puis distinction avec une fixation.','La forme bilatérale peut menacer la respiration malgré une voix conservée.'),
('Dystonie laryngée','Interruptions spasmodiques liées aux tâches vocales.','Bilan phoniatrique et neurologique ciblé.','À distinguer d’une dysphonie fonctionnelle et d’un tremblement.'),
('Papillomatose laryngée','Dysphonie persistante ou récidivante, parfois gêne respiratoire.','Lésions papillaires et confirmation histologique.','Le caractère bénin n’exclut ni obstruction ni récidives.'),
('Cancer du larynx','Dysphonie persistante ou progressive, surtout avec exposition au tabac.','Biopsie d’une lésion suspecte, puis bilan d’extension.','Une tumeur glottique précoce peut se manifester par la voix seule.')]
def comparison():
 return '<h3>Dix diagnostics retenus</h3><p>Repères pédagogiques sans ordre de prévalence démontré ; le tri de gravité garde la priorité.</p>'+table(['Diagnostic','Orientation','Confirmation','Piège'],[[f'<a href="LOT_019_Phase_B_V0_DX.{i}.html">DX.{i} — {n}</a>',a,b,c] for i,(n,a,b,c) in enumerate(DIAGNOSTICS,1)])
