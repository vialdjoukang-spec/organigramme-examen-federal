# HELP_DX4 — LOT_013 — DX.4 Accident de la circulation routière

Questions ouvertes le 30.10.2026 par le rédacteur de DX.4. Toute réponse se vérifie sur sa source primaire avant réinjection.

| ID | Fichier / point | Contexte (ce que dit le cours) | Question précise | Déjà cherché (URL, date) | Emplacement cible |
|---|---|---|---|---|---|
| H13-DX4-01 | DX.4, point 2 | OFS 221 décès routiers (CIM-10 V01–V79, V85–V87, V89) contre OFROU 250 tués (30 jours, police) en 2024 | Quelle note méthodologique de l'OFS décrit le champ de la statistique des causes de décès (résidents, décès à l'étranger, délai) et explique l'écart avec l'OFROU ? Extrait daté | bfs.admin.ch pages « mortalité, causes de décès » et « ecod » (30.10.2026) : aucune note trouvée | Fenêtre `dx4-p2-ofs` |
| H13-DX4-02 | DX.4, point 2 | Seul taux cantonal lu : Vaud 1986–1989 (Halinen 1994) | Répartition cantonale récente des tués de la route (OFROU, tableau de bord) avec taux par habitant | astra.admin.ch, news.admin.ch (30.10.2026) | Fenêtre `dx4-p2-usagers` |
| H13-DX4-03 | DX.4, point 11 | ERC 2025 lu via le résumé RCUK : priorité aux causes réversibles dans l'arrêt traumatique | Place de l'adrénaline et critères d'abstention/arrêt dans l'arrêt cardiaque traumatique selon l'ERC 2025 (texte intégral) et selon une recommandation suisse (ASSM « Décisions de réanimation » 2021, SGNOR) | resus.org.uk nodes 36442/36444 ; cprguidelines.eu (redirection) ; sams.ch article PHC (30.10.2026) | Fenêtre `dx4-p11-adre`, point 10 |
| H13-DX4-04 | DX.4, point 11 | Aucune indication « traumatisme » dans 7 informations AIPS de l'acide tranexamique (33741, 69385, 69390, 70581, 65978, 69007, 69880) | Une spécialité suisse autorisée porte-t-elle l'indication « hémorragie traumatique » ? Sinon, quelle recommandation suisse ou européenne (texte, année) encadre l'usage hors AIPS ? | Corpus AIPS local 08.10.2026 (grep « trauma », « polytrau », « CRASH ») | Fenêtre `dx4-p11-atx` |
| H13-DX4-05 | DX.4, points 5 et 11 | Donnée non trouvée | Conduite médico-légale suisse quand une femme enceinte meurt dans un accident de la route (fœtus, annonce, autopsie) | Sources du LOT (30.10.2026) | Fenêtre `dx4-p11-spec` |
| H13-DX4-06 | DX.4, point 11 | Reprend H13-07 | Accord du MP avant un prélèvement d'organes chez une victime de la route en mort cérébrale : texte suisse applicable | LTx art. 9 ; ASSM 2017 §2.9 (30.10.2026) | Fenêtre `dx4-p11-spec` |
| H13-DX4-07 | DX.4, points 3 et 9 | Skriptum Berne/Lucerne 2013 utilisé pour l'alcoolémie post mortem et la biomécanique | Directive SGRM/SSML (section médecine du trafic) plus récente sur le prélèvement post mortem, le rétrocalcul et les formulaires OFROU (annexes 2 et 3 OOCCR-OFROU) | sgrm.ch (30.10.2026) | Fenêtres `dx4-p3-alcool`, `dx4-p9-vivant` |
| H13-DX4-08 | DX.4, point 1 | Reprend H13-05 | Article du Code de déontologie FMH sur les certificats | FMH en 403 le 30.10.2026 | Fenêtre `dx4-p1-deonto` |

## État après audit médical (30.10.2026, auditeur-medical, opus, xhigh)

| ID | État | Ce que l'audit a trouvé et réinjecté |
|---|---|---|
| H13-DX4-01 | Ouverte | Aucune note méthodologique OFS trouvée ; l'écart de 29 décès (250 − 221) reste non décomposé |
| H13-DX4-02 | Partielle | Tableau OFS « Accidents avec victimes et victimes de la circulation routière, par canton, 1975–2025 » (je-f-11.06.01.01.01, https://www.bfs.admin.ch/bfs/fr/home/statistiques/mobilite-transports.assetdetail.36499574.html) : tués 2025 BE 35, VD 32, ZH 30, LU 14, TI 14, SG 13, FR 12 ; total 214. Réinjecté [S39]. Taux par habitant non calculés (population cantonale non lue) |
| H13-DX4-03 | Partielle | Manuscrit intégral ERC 2025 Special Circumstances (Minerva, https://minerva.usc.gal/bitstreams/dd824d63-af81-45de-897a-ab3fa325b107/download) : rôle des vasopresseurs « unclear », pont temporaire, causes réversibles d'abord ; abstention si aucun signe de vie depuis 15 min ou traumatisme massif ; arrêt suggéré 20 min après correction des causes réversibles. Réinjecté [S40]. Recommandation suisse (ASSM, SGNOR) : non trouvée |
| H13-DX4-04 | Partielle | Huit SmPC françaises relues (70009 ajoutée) : aucune indication traumatisme. ERC 2025 : acide tranexamique cité pendant le transfert d'une hémorragie non compressible, sans dose traumatisme. Aucune dose réinjectée (AIPS seule) |
| H13-DX4-05 | Partielle | Conduite médico-légale du fœtus : non trouvée. ERC 2025 (femme enceinte vivante en arrêt) : déplacement utérin manuel vers la gauche, hystérotomie de réanimation au-delà de 20 semaines, dose d'adrénaline inchangée. Réinjecté [S40] |
| H13-DX4-06, -07, -08 | Ouvertes | Aucune donnée nouvelle |
