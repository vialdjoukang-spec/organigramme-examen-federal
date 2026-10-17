# Journal · urgences CK (Podalire)

## 17.10.2026, Europe/Zurich · lot 1

- Décision : le contenu didactique CK passe avant les nerfs crâniens (demande de Vial). Le lot 1 couvre dix urgences vitales déjà présentes dans les notions : syndrome coronarien aigu, embolie pulmonaire, dissection aortique, pneumothorax sous tension, sepsis, anaphylaxie, méningite bactérienne, état de mal épileptique, acidocétose diabétique, hyperkaliémie.
- Motif du choix : chaque urgence menace la vie, couvre plusieurs diagnostics des notions et dispose d’une recommandation européenne lisible ce jour (ESC, ESICM, EAACI, JBDS, DGN, ESCMID, ERC).
- Écartés du lot 1 : asthme aigu et exacerbation de BPCO, car GINA et GOLD sont internationales et aucune source suisse ou européenne n’a été lue ; hémorragie digestive, prévue au lot 2 avec l’ESGE.
- Décision : aucune posologie n’est écrite. Chaque moyen porte dose_ref nul et la phrase « La posologie reste À vérifier dans l’information professionnelle suisse », jusqu’à la lecture manuelle de l’AIPS par Galien.
- Décision : l’étape « Geste (A) » de la chaîne passe par le champ syn.gestes, qui cite les clés k du catalogue GES ; ck_build refuse une clé inconnue, et la fenêtre Syndrome affiche ces gestes comme liens.
- Décision : la synthèse locale (loc.json) devient l’entrée des urgences depuis l’onglet Gestes, pour quatre régions.
- Corrections faites en relisant les sources : définition du choc septique alignée sur l’ERC ; démarrage périphérique bref de la noradrénaline admis (SSC, recommandations 43 et 44) ; rythme de surveillance de l’acidocétose (60 minutes, 2 heures, puis toutes les 2 heures) ; justification de la dexaméthasone non sourcée retirée ; équipe pluridisciplinaire de l’EP écrite « peut organiser ».

## 17.10.2026, Europe/Zurich · lot 2

- Demande de Vial (20:25) : lot 2 avec les mêmes règles, environ 10 hypothèses, sources européennes ou suisses, GINA et GOLD seulement en contexte.
- Couverture : hémorragie digestive haute (ESGE 2021), asthme aigu grave (NVL Asthma 5.0, chapitre 7), exacerbation de BPCO (ERS/ATS 2017, ligne directrice européenne, et Guide de poche BPCO de la Ligue pulmonaire suisse 2023), insuffisance cardiaque aiguë et choc cardiogénique (ESC 2021), hypoglycémie sévère (JBDS 01, 2023), hyponatrémie (guideline européenne 2014), insuffisance rénale aiguë (position ERBP 2012 sur KDIGO), corps étranger inhalé (ERC 2021 BLS), polytraumatisme (S3 AWMF 187-023 et guideline européenne du saignement traumatique 2023).
- Décision : l’AVC est relié et non dupliqué. Le syndrome urg-deficit-neuro-brutal (module neuro-moteur) renvoie aux hypothèses avc-ischemique et avc-hemorragique du VII, et à l’hypoglycémie sévère, qui imite un AVC.
- Décision : GINA et GOLD ne sont pas cités comme sources. Le guide suisse s’appuie sur GOLD 2023 ; cette dépendance figure dans la note de la source.
- Décision : la NVL Asthma et le guide suisse citent des doses (consensus d’experts) ; elles ne sont pas reprises, et chaque moyen porte la phrase « À vérifier dans l’information professionnelle suisse ».
- Décision : l’hémorragie variqueuse reste hors champ, car l’ESGE 2021 ne couvre que l’hémorragie non variqueuse et Baveno VII n’a pas été lu.
- Domaines ajoutés à qa/domaines.yml, avec motif : liguepulmonaire.ch (Suisse) et abcd.care (hôte des JBDS) ; ils attendent l’accord de Vial et d’Argos.
- Non obtenus : chapitre BPCO de la NVL (le registre AWMF ne rend que du HTML), Baveno VII, mise à jour ciblée ESC 2023, partie 2 de l’ERBP.
- Corrections faites en relisant les sources : numéros de section de l’ESC (§ 11.3.10 pour l’assistance circulatoire), restriction hydrique rattachée au § 3.4.3 de l’hyponatrémie, justifications non lues retirées ou adoucies (aérosol doseur contre nébulisation, bénéfices des corticoïdes, risques des inotropes, compressions thoraciques).
