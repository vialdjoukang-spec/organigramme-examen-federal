#!/usr/bin/env python3
"""Thémis · 17.10.2026 · écrit data/EXI.json et data/SESSION.json (source : research_exigences.md, pages lues le 17.10.2026).
Toute correction se fait ici, puis on relance le script et le patch 0004 (ou json_inject.py inject EXI|SESSION)."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S1="https://www.bag.admin.ch/fr/examen-federal-en-medecine-humaine"
S2="https://www.bag.admin.ch/fr/deposer-une-demande-de-reconnaissance-dun-diplome-de-profession-medicale-delivre-dans-un-etat-tiers-hors-de-lueaele"
S3="https://www.bag.admin.ch/fr/inscription-a-lexamen-federal"
S4="https://healthreg-online.admin.ch/examination-registration"
S5="https://www.bag.admin.ch/dam/fr/sd-web/fL9EvX0YPT2d/20260204_Exigences%20MED%202026_f.pdf"
S6="https://www.bag.admin.ch/dam/fr/sd-web/NGRcSCsXT8zF/20260204_Directives%20MED%202026_f.pdf"
S7="https://www.bag.admin.ch/dam/fr/sd-web/KdRYk-5ILb74/20260204_Infotext%20MED%202026_f.pdf"
S8="https://www.bag.admin.ch/dam/fr/sd-web/288COTC16Hkv/Tableau%20des%20d%C3%A9lais%202026%20pour%20les%20examens%20f%C3%A9d%C3%A9raux%20en%20m%C3%A9decine%20humaine.pdf"
S9="https://www.bag.admin.ch/dam/fr/sd-web/mytSOaIs-KIq/antragsformular-erwerb-des-eidgenoessischen-diploms.pdf"
S10="https://www.fedlex.admin.ch/eli/cc/2008/832/fr"
S11="https://www.bag.admin.ch/fr/revision-lpmed-enregistrement-des-diplomes-et-inscription-des-connaissances-linguistiques"
S12="https://www.iml.unibe.ch/fr/offres/assessment/organisation-examens/self-assessment"
N1="https://www.unige.ch/medecine/download_file/view/4895/1512"
C,V="confirme","a_verifier"
G={"A":"A · Décision MEBEKO et droit d’admission","B":"B · Pièces du dossier MEBEKO (à garder prêtes)","C":"C · Inscription en ligne 2027","D":"D · Taxes après l’émolument MEBEKO","E":"E · Dates","F":"F · Préparation, jour de l’examen et suite"}
L=[
("A1","Je relis ma décision MEBEKO, car elle fixe mes conditions d’admission et indique si je dois passer l’examen complet ou seulement certaines épreuves.",S10,"Ordonnance concernant les examens LPMéd (RS 811.113.3), art. 6",C,None,[],""),
("A2","Je repère dans ma décision la procédure d’inscription qui m’est communiquée, car le formulaire MEBEKO précise que la procédure et les dates sont transmises avec la décision d’admission.",S9,"Formulaire « Obtention du diplôme fédéral » (17.09.2018), § 4",C,None,[],""),
("A3","Je fais confirmer par la MEBEKO que ma décision vaut admission à l’examen fédéral, car le terme « reconnaissance partielle » ne figure dans aucun texte officiel consulté.",S2,"OFSP · Diplôme d’un État tiers ; RS 811.113.3, art. 6",V,None,[],""),
("A4","Je détermine la voie qui s’applique : avec au moins 36 mois d’activité clinique en Suisse à 100 %, je dois réussir l’examen complet ; avec au moins 60 mois, je dois réussir seulement la partie théorique.",S2,"OFSP · Diplôme d’un État tiers",V,None,[],"La règle est confirmée ; la voie qui me concerne reste à confirmer."),
("A5","Je retiens qu’une décision d’enregistrement au MedReg ne permet pas de s’inscrire à l’examen fédéral.",S2,"OFSP · Diplôme d’un État tiers",C,None,[],""),
("A6","Si je n’ai pas encore de décision formelle d’accès direct, je l’adresse au secrétariat de la MEBEKO 6 à 8 semaines avant le 31.03.2027, c’est-à-dire entre le 03.02 et le 17.02.2027 environ.",S2,"OFSP · Diplôme d’un État tiers (règle des 6 à 8 semaines ; dates calculées)",C,"2027-02-03",[],""),
("A7","Je conserve une copie de toutes les pièces envoyées, car la MEBEKO ne restitue aucun document.",S2,"OFSP · Diplôme d’un État tiers, FAQ ; formulaire MEBEKO, § 4",C,None,[],""),
("B1","Le formulaire de demande est daté, signé et envoyé uniquement par la poste à l’OFSP, MEBEKO, Schwarzenburgstrasse 157, 3003 Berne.",S9,"Formulaire MEBEKO, § 4 et § 5",C,None,["e5"],""),
("B2","Je tiens mon curriculum vitae à jour.",S9,"Formulaire MEBEKO, § 5",C,None,["e6"],""),
("B3","Je garde une photocopie de mon passeport comme preuve de nationalité.",S9,"Formulaire MEBEKO, § 5",C,None,["e7"],""),
("B4","Je garde une copie de mon diplôme et sa traduction officielle si l’original n’est ni en français, ni en allemand, ni en italien, ni en anglais.",S9,"Formulaire MEBEKO, § 5 ; OFSP, langues admises",C,None,["e8"],""),
("B5","Je garde la liste des examens réussis pendant mes études et sa traduction officielle.",S9,"Formulaire MEBEKO, § 5",C,None,["e9"],""),
("B6","Je garde, si elles existent, les preuves de mon expérience professionnelle à l’étranger et leur traduction officielle.",S9,"Formulaire MEBEKO, § 5",C,None,["e10"],""),
("B7","Je garde, si elles existent, les preuves de mon expérience en Suisse, avec le début, la fin, la fonction et le taux d’occupation.",S9,"Formulaire MEBEKO, § 5",C,None,["e11"],""),
("B8","J’indique une adresse de contact en Suisse si je suis domicilié à l’étranger.",S9,"Formulaire MEBEKO, § 4",C,None,["e12"],""),
("B9","Je fournis des copies certifiées conformes plutôt que des originaux, car la MEBEKO ne renvoie pas les originaux.",S2,"OFSP · Diplôme d’un État tiers, FAQ",C,None,[],""),
("B10","Je communique tout changement d’adresse ou de nom à la MEBEKO par courriel (mebeko@bag.admin.ch).",S2,"OFSP · Diplôme d’un État tiers, FAQ",C,None,[],""),
("C1","Je m’inscris en ligne pendant la période d’inscription 2027, qui va du 15.12.2026 au 31.03.2027.",S4,"Portail d’inscription de l’OFSP (healthreg), lu le 17.10.2026",C,"2027-03-31",["e4"],""),
("C2","Je respecte le 31.03.2027, car une inscription tardive n’est admise que pour de justes motifs, comme une maladie ou un accident, et elle reporte l’examen à l’année suivante.",S10,"RS 811.113.3, art. 13, al. 4 ; OFSP · Inscription",C,"2027-03-31",[],""),
("C3","Je lis les rubriques « i » du formulaire en ligne, car l’OFSP y indique les documents à joindre à l’inscription.",S3,"OFSP · Inscription à l’examen fédéral",C,None,[],""),
("C4","Je prépare les pièces à joindre à l’inscription 2027 dès que le formulaire les affiche, car leur liste exacte n’est pas publiée avant l’ouverture du 15.12.2026.",S3,"OFSP · Inscription ; portail healthreg",V,"2026-12-15",[],""),
("C5","Je vérifie que j’ai reçu le courriel automatique de confirmation, et je contrôle les courriels indésirables s’il n’arrive pas.",S3,"OFSP · Inscription à l’examen fédéral",C,None,[],""),
("C6","Je choisis la langue d’examen lors de l’inscription : en 2026, le CK se passait en allemand, en français ou en italien, et le CS en principe dans la langue du site.",S5,"Exigences MED 2026, § 4.5",V,None,["e3"],"La règle est confirmée pour 2026 ; elle reste à confirmer pour 2027."),
("C7","Je fais confirmer la langue d’examen qui m’est ouverte, car le formulaire MEBEKO de 2018 cite seulement le français et l’allemand, alors que les Exigences 2026 citent aussi l’italien pour le CK.",S9,"Formulaire MEBEKO, § 4 ; Exigences MED 2026, § 4.5",V,None,[],""),
("C8","Je retiens que je ne peux pas exiger une date ou un lieu précis, et que la MEBEKO transfère en priorité les titulaires d’un diplôme étranger non reconnu si un site manque de places.",S5,"Exigences MED 2026, § 4.4 b ; OFSP · Inscription",V,None,[],"La règle est confirmée ; le site qui me sera attribué reste à connaître."),
("C9","J’indique lors de l’inscription si je veux inscrire au MedReg la langue du site, une autre langue ou aucune langue après la réussite ; chaque inscription de langue coûte entre 50 et 100 francs.",S3,"OFSP · Inscription à l’examen fédéral",C,None,[],""),
("C10","Si j’ai besoin d’une compensation des inégalités liée à un handicap, j’envoie une demande écrite à la MEBEKO avant la date limite, avec un certificat médical de moins de six mois, une levée du secret professionnel et les mesures obtenues pendant mes études.",S6,"Directives MED 2026, § 1.1 à 1.3",V,None,[],"La date limite 2026 était le 31.03.2026 ; celle de 2027 reste à confirmer."),
("D1","L’émolument de traitement de la demande MEBEKO, que la MEBEKO fixe par décision entre 800 et 1000 francs, est payé.",S9,"Formulaire MEBEKO, § 4 ; OFSP, FAQ",C,None,["e13"],""),
("D2","Je fais confirmer qu’aucun solde de cet émolument ne reste dû.",S9,"Formulaire MEBEKO, § 4",V,None,[],""),
("D3","Je prévois la taxe d’inscription de 200 francs, qui reste due dans tous les cas et n’est pas remboursable.",S10,"RS 811.113.3, art. 27, al. 1 ; Informations MED 2026, § 8",C,None,[],""),
("D4","Je prévois la taxe d’examen de 1500 francs pour l’examen complet.",S10,"RS 811.113.3, art. 27, al. 2 ; Informations MED 2026, § 8",C,None,[],""),
("D5","Si je ne passe qu’une partie de l’examen, je fais confirmer le montant, car la taxe est alors calculée proportionnellement.",S10,"RS 811.113.3, art. 27, al. 3",V,None,[],"La règle est confirmée ; le montant reste à confirmer."),
("D6","Je prévois la taxe de 500 francs pour l’octroi du diplôme, qui n’est facturée qu’après la réussite.",S7,"Informations concernant l’examen fédéral MED 2026, § 8",C,None,[],""),
("D7","Je retiens que la taxe d’examen reste due si je retire mon inscription sans juste motif après la décision d’admission.",S10,"RS 811.113.3, art. 15 ; Exigences MED 2026, § 4.2",C,None,[],""),
("E1","Je sais que la session 2026 est terminée (CK les 04 et 06.08.2026, réserve QCM le 25.08.2026, CS du 31.08 au 02.09.2026).",S8,"Tableau des délais 2026 ; Exigences MED 2026, § 4.3",C,None,[],""),
("E2","Je note les dates 2027 que la faculté de Genève annonce sous réserve (CK les 10 et 12.08.2027, CS entre le 06 et le 10.09.2027), car l’OFSP ne les a pas encore publiées.",N1,"Faculté de médecine UNIGE, calendrier 2026-2027 (source facultaire, non OFSP)",V,None,[],"Ces dates restent à confirmer par l’OFSP."),
("E3","Je télécharge les Exigences, les Directives et le Tableau des délais 2027 dès leur publication, car l’OFSP les met à jour chaque année.",S1,"Informations MED 2026, § 1 ; OFSP · Examen fédéral",V,None,[],"La mise à jour annuelle est confirmée ; la date de publication 2027 reste inconnue."),
("E4","Je retiens que l’OFSP envoie les résultats officiels au plus tard à la fin du mois d’octobre.",S7,"Informations MED 2026, § 6 e",C,None,[],""),
("F1","Je fais le self-assessment QCM de l’IML pour connaître l’interface du CK.",S12,"IML Berne · Self-assessment ; Informations MED 2026, § 4 h",C,None,[],""),
("F2","J’apporte une pièce d’identité officielle avec photo, car l’identité est contrôlée à chaque épreuve.",S6,"Directives MED 2026",C,None,[],""),
("F3","Je n’apporte au CK qu’un dictionnaire de traduction standard d’une langue officielle suisse, sans annotation ni définition médicale, car tout autre moyen auxiliaire est interdit.",S6,"Directives MED 2026, § 6.1",C,None,[],""),
("F4","Si je dois renoncer ou interrompre après la décision d’admission, j’envoie sans tarder un courrier recommandé au responsable de site avec un certificat médical.",S10,"RS 811.113.3, art. 16 ; Tableau des délais 2026",C,None,[],""),
("F5","Je retiens qu’en cas d’échec je ne répète que l’épreuve non réussie, au maximum deux fois, et que trois échecs excluent définitivement de l’examen.",S10,"RS 811.113.3, art. 18 et 19 ; Exigences MED 2026",C,None,[],""),
("F6","Je prépare la preuve de mes connaissances linguistiques de niveau B2 au moins : un diplôme de langue de moins de six ans, une formation dans la langue ou trois ans d’expérience professionnelle dans les dix dernières années.",S11,"OFSP · Connaissances linguistiques (MedReg) ; OFSP, FAQ",C,None,["e14"],""),
("F7","Je retiens que l’autorisation d’exercer relève du canton et qu’elle se distingue de l’examen.",S2,"OFSP · Diplôme d’un État tiers",C,None,[],""),
("F8","Je contacte la MEBEKO par office@mebeko.admin.ch ou au +41 58 462 94 83 le vendredi de 8 h à 11 h, et je prévois jusqu’à six semaines de délai de réponse par courriel.",S1,"OFSP · Examen fédéral ; OFSP · Diplôme d’un État tiers",C,None,[],""),
]
assert len(L)==46 and len({x[0] for x in L})==46
EXI={"groupes":G,"lu":"2026-10-17","items":[dict(id=i,g=i[0],t=t,u=u,r=r,s=s,**({"e":e} if e else {}),**({"m":m} if m else {}),**({"n":n} if n else {})) for i,t,u,r,s,e,m,n in L]}
SESSION={"annee":2027,"inscription":{"debut":"2026-12-15","fin":"2027-03-31","url":S4,"source":"Portail d’inscription de l’OFSP, lu le 17.10.2026","statut":C},
 "ck":{"dates":["2027-08-10","2027-08-12"],"statut":V},"cs":{"debut":"2027-09-06","fin":"2027-09-10","statut":V},
 "dates_source":{"url":N1,"ref":"Faculté de médecine UNIGE, calendrier 2026-2027 (source facultaire, non publiée par l’OFSP)"},
 "precedente":{"annee":2026,"ck":["2026-08-04","2026-08-06"],"cs":["2026-08-31","2026-09-02"],"url":S8,"ref":"Tableau des délais 2026"}}
for n,v in (("EXI",EXI),("SESSION",SESSION)):
    json.dump(v,open(os.path.join(ROOT,"data",n+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); open(os.path.join(ROOT,"data",n+".json"),"a").write("\n")
print("EXI : 46 cases ;", sum(x[4]==V for x in L), "à vérifier.")
