# Liste blanche validée — 2026-10-24T02:57:25+02:00

Méthode : curl -L https://<domaine><sonde> ; 200 sans page de défi anti-robot = valide ; 401/403/412/415/429 = joignable mais bloque l'accès automatisé (usage manuel seulement)

Source lisible par les scripts : `allowlist.json`. Relancer la validation : `python3 validate_allowlist.py`.

| Rang | Domaine | Organisme | Statut au 2026-10-24 | Accès automatique |
|---|---|---|---|---|
| 1 | `compendium.ch` | Compendium suisse des médicaments (HCI Solutions) | valide (HTTP 200) | oui |
| 1 | `download.swissmedicinfo.ch` | Refdata — téléchargement officiel AIPS (XML, CGU à accepter) | valide (HTTP 200) | oui |
| 1 | `fedlex.data.admin.ch` | Fedlex — données ouvertes (SPARQL, ELI) | valide (HTTP 200) | oui |
| 1 | `sl.bag.admin.ch` | OFSP — liste des spécialités (LS) | valide (HTTP 200) | oui |
| 1 | `www.bag.admin.ch` | OFSP / BAG — santé publique, vaccination, déclaration | valide (HTTP 200) | oui |
| 1 | `www.bfs.admin.ch` | OFS / BFS — statistiques de santé | valide (HTTP 200) | oui |
| 1 | `www.bsv.admin.ch` | OFAS / BSV — assurances sociales (AI, AVS) | valide (HTTP 200) | oui |
| 1 | `www.fedlex.admin.ch` | Fedlex — recueil systématique du droit fédéral | valide (HTTP 200) | oui |
| 1 | `www.infovac.ch` | Infovac — information vaccinale (HUG, mandat OFSP) | valide (HTTP 200) | oui |
| 1 | `www.obsan.admin.ch` | Obsan — observatoire suisse de la santé | valide (HTTP 200) | oui |
| 1 | `www.samw.ch` | ASSM / SAMW — directives médico-éthiques | valide (HTTP 200) | oui |
| 1 | `www.swissmedic.ch` | Swissmedic — listes officielles, autorisations | valide (HTTP 200) | oui |
| 1 | `www.swissmedicinfo.ch` | Swissmedic / Refdata — AIPS (information professionnelle) | valide (HTTP 200) | oui |
| 1 | `www.toxinfo.ch` | Tox Info Suisse | valide (HTTP 200) | oui |
| 1 | `www.fmh.ch` | FMH — Fédération des médecins suisses | joignable, protégé contre les robots (403) | non — consultation manuelle |
| 2 | `pharmasuisse.org` | pharmaSuisse — pharmaciens | valide (HTTP 200) | oui |
| 2 | `sgc-ssc.ch` | SSC / SGC — chirurgie | valide (HTTP 200) | oui |
| 2 | `sggssg.ch` | SSG / SGG — gastro-entérologie et hépatologie | valide (HTTP 200) | oui |
| 2 | `sgnor.ch` | SSMUS / SGNOR — médecine d'urgence et de sauvetage | valide (HTTP 200) | oui |
| 2 | `sgr-ssr.ch` | SSR / SGR — radiologie | valide (HTTP 200) | oui |
| 2 | `sgtm.ch` | SSMT / SGTM — médecine tropicale et des voyages | valide (HTTP 200) | oui |
| 2 | `ssai.ch` | SSAI / SGAI — allergologie et immunologie (identité à confirmer) | valide (HTTP 200) | oui |
| 2 | `ssi.guidelines.ch` | SSI — recommandations thérapeutiques en ligne | valide (HTTP 200) | oui |
| 2 | `swissurology.ch` | SSU / SGU — urologie | valide (HTTP 200) | oui |
| 2 | `www.chuv.ch` | CHUV — hôpital universitaire | valide (HTTP 200) | oui |
| 2 | `www.derma.swiss` | SSDV / SGDV — dermatologie et vénéréologie | valide (HTTP 200) | oui |
| 2 | `www.diabetesschweiz.ch` | diabètesuisse | valide (HTTP 200) | oui |
| 2 | `www.hug.ch` | HUG — hôpitaux universitaires de Genève | valide (HTTP 200) | oui |
| 2 | `www.insel.ch` | Inselspital — hôpital universitaire | valide (HTTP 200) | oui |
| 2 | `www.orl-hno.ch` | SSORL — ORL et chirurgie cervico-faciale | valide (HTTP 200) | oui |
| 2 | `www.psychiatrie.ch` | SSPP / SGPP — psychiatrie et psychothérapie | valide (HTTP 200) | oui |
| 2 | `www.sfgg.ch` | SFGG / SPSG — gériatrie | valide (HTTP 200) | oui |
| 2 | `www.sgaim.ch` | SSMIG / SGAIM — médecine interne générale | valide (HTTP 200) | oui |
| 2 | `www.sgedssed.ch` | SSED / SGED — endocrinologie et diabétologie | valide (HTTP 200) | oui |
| 2 | `www.sggg.ch` | SSGO / SGGG — gynécologie et obstétrique | valide (HTTP 200) | oui |
| 2 | `www.sgh-ssh.ch` | SSH / SGH — hématologie | valide (HTTP 200) | oui |
| 2 | `www.sginf.ch` | SSI / SGInf — infectiologie | valide (HTTP 200) | oui |
| 2 | `www.sgkjpp.ch` | SSPPEA / SGKJPP — pédopsychiatrie | valide (HTTP 200) | oui |
| 2 | `www.sgmo.ch` | SSOM / SGMO — oncologie médicale | valide (HTTP 200) | oui |
| 2 | `www.sog-sso.ch` | SSO / SOG — ophtalmologie | valide (HTTP 200) | oui |
| 2 | `www.ssapm.ch` | SSAPM — anesthésiologie et médecine périopératoire | valide (HTTP 200) | oui |
| 2 | `www.swisscardio.ch` | SSC / SGK — cardiologie | valide (HTTP 200) | oui |
| 2 | `www.swissnephrology.ch` | SSN / SGN — néphrologie | valide (HTTP 200) | oui |
| 2 | `www.swissneuro.ch` | SSN / SNG — neurologie | valide (HTTP 200) | oui |
| 2 | `www.swissnoso.ch` | Swissnoso — infections associées aux soins | valide (HTTP 200) | oui |
| 2 | `www.swissorthopaedics.ch` | swiss orthopaedics — orthopédie | valide (HTTP 200) | oui |
| 2 | `www.swisstph.ch` | Swiss TPH — institut tropical et de santé publique | valide (HTTP 200) | oui |
| 2 | `www.swisstransplant.org` | Swisstransplant | valide (HTTP 200) | oui |
| 2 | `www.unisante.ch` | Unisanté — médecine générale et santé publique | valide (HTTP 200) | oui |
| 2 | `www.unispital-basel.ch` | USB — hôpital universitaire | valide (HTTP 200) | oui |
| 2 | `www.usz.ch` | USZ — hôpital universitaire | valide (HTTP 200) | oui |
| 2 | `sgg-ssg.ch` | REJET attendu : association de seniors, hors champ | REJETÉ (domaine hors sujet) (200) | non — consultation manuelle |
| 2 | `www.paediatrieschweiz.ch` | SSP / Pädiatrie Schweiz — pédiatrie | injoignable lors du test (000) | non — consultation manuelle |
| 2 | `www.pneumo.ch` | SSP / SGP — pneumologie | joignable, protégé contre les robots (200) | non — consultation manuelle |
| 2 | `www.rheuma-net.ch` | SSR / SGR — rhumatologie | joignable, protégé contre les robots (200) | non — consultation manuelle |
| 2 | `www.sgsmp.ch` | REJET attendu : physique médicale, hors champ | REJETÉ (domaine hors sujet) (200) | non — consultation manuelle |
| 2 | `www.ssai-sgai.ch` | REJET attendu : domaine non médical | REJETÉ (domaine hors sujet) (200) | non — consultation manuelle |
| 3 | `eaaci.org` | EAACI — allergologie | valide (HTTP 200) | oui |
| 3 | `eacs.sanfordguide.com` | EACS — recommandations en ligne | valide (HTTP 200) | oui |
| 3 | `easl.eu` | EASL — hépatologie | valide (HTTP 200) | oui |
| 3 | `esgar.org` | ESGAR — radiologie digestive | valide (HTTP 200) | oui |
| 3 | `esvs.org` | ESVS — chirurgie vasculaire | valide (HTTP 200) | oui |
| 3 | `ueg.eu` | UEG — gastro-entérologie | valide (HTTP 200) | oui |
| 3 | `uroweb.org` | EAU — urologie | valide (HTTP 200) | oui |
| 3 | `www.eacsociety.org` | EACS — VIH | valide (HTTP 200) | oui |
| 3 | `www.ean.org` | EAN — neurologie | valide (HTTP 200) | oui |
| 3 | `www.easd.org` | EASD — diabète | valide (HTTP 200) | oui |
| 3 | `www.ecdc.europa.eu` | ECDC | valide (HTTP 200) | oui |
| 3 | `www.ema.europa.eu` | EMA | valide (HTTP 200) | oui |
| 3 | `www.erc.edu` | ERC — réanimation | valide (HTTP 200) | oui |
| 3 | `www.ersnet.org` | ERS — pneumologie | valide (HTTP 200) | oui |
| 3 | `www.escardio.org` | ESC — cardiologie | valide (HTTP 200) | oui |
| 3 | `www.escmid.org` | ESCMID — infectiologie | valide (HTTP 200) | oui |
| 3 | `www.ese-hormones.org` | ESE — endocrinologie | valide (HTTP 200) | oui |
| 3 | `www.eshonline.org` | ESH — hypertension | valide (HTTP 200) | oui |
| 3 | `www.esmo.org` | ESMO — oncologie | valide (HTTP 200) | oui |
| 3 | `www.eular.org` | EULAR — rhumatologie | valide (HTTP 200) | oui |
| 4 | `ginasthma.org` | GINA | valide (HTTP 200) | oui |
| 4 | `goldcopd.org` | GOLD | valide (HTTP 200) | oui |
| 4 | `kdigo.org` | KDIGO | valide (HTTP 200) | oui |
| 4 | `www.acc.org` | ACC (jamais seule, V7-Tunder §4.2) | valide (HTTP 200) | oui |
| 4 | `www.idsociety.org` | IDSA (jamais seule, V7-Tunder §4.2) | valide (HTTP 200) | oui |
| 4 | `www.ilcor.org` | ILCOR | valide (HTTP 200) | oui |
| 4 | `www.nice.org.uk` | NICE | valide (HTTP 200) | oui |
| 4 | `www.who.int` | OMS | valide (HTTP 200) | oui |
| 4 | `www.ahajournals.org` | AHA (jamais seule, V7-Tunder §4.2) | joignable, protégé contre les robots (403) | non — consultation manuelle |
| 4 | `www.cdc.gov` | CDC (jamais seule, V7-Tunder §4.2) | joignable, protégé contre les robots (403) | non — consultation manuelle |
| 4 | `www.cochranelibrary.com` | Cochrane | joignable, protégé contre les robots (412) | non — consultation manuelle |
| 5 | `eutils.ncbi.nlm.nih.gov` | NCBI E-utilities (API) | valide (HTTP 200) | oui |
| 5 | `pubmed.ncbi.nlm.nih.gov` | PubMed | valide (HTTP 200) | oui |
| 5 | `www.ebi.ac.uk` | Europe PMC (API REST) | valide (HTTP 200) | oui |
| 5 | `europepmc.org` | Europe PMC (site) | joignable, protégé contre les robots (403) | non — consultation manuelle |
