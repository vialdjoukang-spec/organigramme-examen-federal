"""Tests automatiques du harnais (pytest). Aucun réseau requis ; Playwright requis pour test_captures."""
import json, os, re, shutil, subprocess, sys
from pathlib import Path
import pytest
RACINE = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(RACINE / "coeur"))
import harnais as H

def nouvelle_instance(tmp_path, ollama=False):
    d = tmp_path / "Test__Harnais_LOT999"; d.mkdir()
    (d / "config.json").write_text(json.dumps({"agent": "Test__Harnais_LOT999", "lot": "999", "ollama": ollama, "sonde_recherche": "smarter medicine",
                                               "seuils": {"rep4_max_1000": 10, "connecteurs_min_100": 1.0}}), encoding="utf-8")
    shutil.copy(sorted(RACINE.glob("instances/*/SKILL.md"))[0], d / "SKILL.md")
    return H.Instance(d)

def page(tmp_path, nom, corps):
    f = tmp_path / nom; f.write_text(f"<html lang='fr'><body><main><p>{corps}</p></main></body></html>", encoding="utf-8"); return f

def test_registre_suisse():
    r = json.loads((RACINE / "registre/SOURCES_SUISSES.json").read_text(encoding="utf-8"))
    assert r["meta"]["urls_uniques"] == len(r["sources"]) >= 223
    assert r["meta"]["specialites_couvertes"] == 45 and r["meta"]["paramedical"]["specialites"] == 45
    assert sum(r["meta"]["par_rang"].values()) == len(r["sources"])
    cas = {"https://www.swissmedicinfo.ch/": 1, "https://www.fedlex.admin.ch/eli/cc/2008/832/fr": 2, "https://www.bag.admin.ch/fr/x": 3,
           "https://ssai.ch/fr": 4, "https://www.hug.ch/x.pdf": 5, "https://www.escardio.org/g": 6, "https://doi.org/10.1/x": 7, "local:neo/x": 8}
    for u, k in cas.items(): assert H.rang_url(u) == k, u

def test_collecte_index_tri_filtre_doublons(tmp_path):
    I = nouvelle_instance(tmp_path)
    txt = "La BPCO se traite par bronchodilatateurs en cas d'exacerbation selon la stratégie locale. " * 3
    a = H.collecter(I, "https://www.hug.ch/bpco.html", "S1", "DX2", "HUG", "2026", page(tmp_path, "a.html", txt))
    b = H.collecter(I, "https://www.has-sante.fr/bpco.html", "S2", "DX2", "HAS", "2010", page(tmp_path, "b.html", "Exacerbation de BPCO : traitement par bronchodilatateurs et corticoïdes systémiques en France, recommandations nationales. " * 3))
    c = H.collecter(I, "https://www.hug.ch/copie.html", "S3", "DX2", "copie", "2026", page(tmp_path, "c.html", txt))
    assert a["sha256"] == c["sha256"] and a["rang"] == 5 and b["rang"] == 6
    assert H.indexer(I, a)["passages"] >= 1 and H.indexer(I, b)["passages"] >= 1
    assert H.indexer(I, c)["doublons_filtres"] >= 1                       # filtre doublons
    assert H.collecter(I, "https://www.hug.ch/bpco.html", "S1")["depuis_cache"]  # cache
    r = H.chercher(I, "exacerbation BPCO", "p11", "DX2")
    assert r and r[0]["rang"] == 5                                         # tri suisse d'abord
    assert all(x["rang"] <= 5 for x in H.chercher(I, "exacerbation", suisse=True))   # filtre suisse
    assert all(x["doc"] != "S2" for x in H.chercher(I, "exacerbation", max_age_ans=10))  # filtre périmé (2010)

def test_pec_refus_sans_source_suisse(tmp_path):
    I = nouvelle_instance(tmp_path)
    m = H.collecter(I, "https://www.has-sante.fr/x.html", "S1", "", "", "2024", page(tmp_path, "x.html", "Prise en charge de l'exacerbation : traitement en France selon recommandation. " * 3)); H.indexer(I, m)
    assert H.prise_en_charge(I, "exacerbation")["statut"] == "REFUS_AUCUNE_SOURCE_SUISSE"
    m = H.collecter(I, "https://www.swissmedicinfo.ch/x.html", "S2", "", "", "2026", page(tmp_path, "y.html", "Posologie lors d'exacerbation : traitement selon information professionnelle suisse. " * 3)); H.indexer(I, m)
    r = H.prise_en_charge(I, "exacerbation"); assert r["statut"] == "OK_SUISSE" and r["passages"][0]["rang"] == 1

def test_memoire_et_cp(tmp_path):
    I = nouvelle_instance(tmp_path)
    I.retenir("decision", "DX2-ordre", {"choix": "B"}); assert I.rappeler("decision")[0]["valeur"] == {"choix": "B"}
    H.cp_sauver(I, "test"); assert H.cp_verifier(I)[0]
    p = I.d / "cp/DERNIER.json"; j = json.loads(p.read_text()); j["note"] = "altéré"; p.write_text(json.dumps(j))
    assert not H.cp_verifier(I)[0]

def squelette(tmp_path):
    f = tmp_path / "LOT_999_Phase_B_V0_DX.2.html"; f.write_text(H.squelette("999", 2, "Test"), encoding="utf-8"); return f

def test_squelette_conforme_sauf_taille(tmp_path):
    f = squelette(tmp_path); t = f.read_text()
    assert len(re.findall(r'<h3 id="dx2-p\d+"', t)) == 14 and t.count('class="ilot"') == 14
    R = H.controler(None, f, francais=False)
    crit = [x["msg"] for c in ("syntaxe", "semantique_detecte", "langue", "sources", "securite") for x in R[c] if x["niveau"] == "critique"]
    assert crit == [f"taille {f.stat().st_size} o hors bande 80–150 Ko"], crit

def test_controles_detectent_les_defauts(tmp_path):
    f = squelette(tmp_path); t = f.read_text()
    t = t.replace("text-align:justify", "text-align:left").replace('<h2 id="dx2">', '<h2 id="dx2" title="x">')
    t = t.replace('<div class="p">', '<p>', 1).replace(" qui reste intacte.</div>", " qui reste intacte.</p>", 1)
    t = t.replace('<section class="ilot" id="dx2-i5">', '<section id="dx2-i5">').rsplit("<!-- FIN_FICHIER", 1)[0]
    f.write_text(t, encoding="utf-8"); R = H.controler(None, f, francais=False); M = json.dumps(R, ensure_ascii=False)
    assert "texte non justifié" in M and "title=" in M and "FIN_FICHIER absent" in M and "îlots : 13/14" in M
    assert "dans un <p>" in M and R["synthese"]["syntaxe"]["critique"] >= 2 and not R["conforme_mecanique"]

def test_controle_pec_suisse(tmp_path):
    f = squelette(tmp_path); t = f.read_text()
    bloc = '<p>Le traitement de fond associe deux bronchodilatateurs de longue durée selon la recommandation citée [S1].</p>'
    t2 = t.replace('<div class="u" id="dx2-urgence">', bloc + '\n<div class="u" id="dx2-urgence">')
    f.write_text(t2.replace("[S1] [titre, organisme, année. URL (consulté le JJ mois AAAA).]", "[S1] HAS. <a href=\"https://www.has-sante.fr/x\">x</a>"), encoding="utf-8")
    assert "sans source suisse" in json.dumps(H.controler(None, f, francais=False), ensure_ascii=False)
    f.write_text(t2.replace("[S1] [titre, organisme, année. URL (consulté le JJ mois AAAA).]", "[S1] HUG. <a href=\"https://www.hug.ch/x.pdf\">x</a>"), encoding="utf-8")
    assert "sans source suisse" not in json.dumps(H.controler(None, f, francais=False), ensure_ascii=False)

def test_rapport_html_colore(tmp_path):
    R = H.controler(None, squelette(tmp_path), francais=False); h = H.rapport_html(R)
    for k in ("Erreurs de syntaxe", "Sémantique", "Langue", "Sources", "Sécurité", "#c0392b"): assert k in h

def test_francais_metriques(tmp_path):
    f = squelette(tmp_path); R = H.controler(None, f, francais=True)
    assert "repetitions_4grammes_pour_1000_mots" in R["info"].get("francais", {}), R["langue"]

def test_sante_ok_puis_alerte_puis_resolution(tmp_path):
    I = nouvelle_instance(tmp_path); H.main(["--instance", str(I.d), "init"])
    st = H.sante(I); assert st["ok"], st["echecs"]
    (I.d / "SKILL.md").rename(I.d / "SKILL.bak"); st = H.sante(I)
    assert not st["ok"] and st["echecs"] == ["skills"] and (I.d / "sante/ALERTE.json").exists()
    (I.d / "SKILL.bak").rename(I.d / "SKILL.md"); assert H.sante(I)["ok"] and not (I.d / "sante/ALERTE.json").exists()

def test_cli_unique():
    r = subprocess.run([str(RACINE / "coeur/bin/harnais"), "--help"], capture_output=True, text=True)
    assert r.returncode == 0 and "sante" in r.stdout and "pec" in r.stdout

def test_captures_desktop_mobile_justifie(tmp_path):
    pytest.importorskip("playwright")
    r = H.captures(squelette(tmp_path), tmp_path / "cap", 2)
    imgs = [x for x in r if "fichier" in x]; assert len(imgs) == 8 and all(Path(x["fichier"]).stat().st_size > 1000 for x in imgs)
    assert all(x["p_total"] == x["p_justifies_rendu"] > 0 for x in imgs)
    assert all(x["debordement_horizontal"] is False for x in r if "debordement_horizontal" in x)

@pytest.mark.skipif(not Path("/workspace/outils-puissants/Leona__Production_4LOTs_Cloud_20261109/LOT_132/LOT_132_Phase_B_V0_DX.1.html").exists(), reason="box seulement")
def test_dx1_reel_lecture_seule():
    f = Path("/workspace/outils-puissants/Leona__Production_4LOTs_Cloud_20261109/LOT_132/LOT_132_Phase_B_V0_DX.1.html"); avant = f.read_bytes()
    R = H.controler(None, f, francais=False); M = json.dumps(R, ensure_ascii=False)
    assert "texte non justifié" in M and "îlots : 0/14" in M and f.read_bytes() == avant

def test_illustrer_data_uri_fragment(tmp_path):
    """Convertit une image rendue en data:URI ≤25 Ko et produit un <figure> avec licence + <ol>."""
    from PIL import Image
    png = tmp_path / "lesion.png"
    Image.new("RGB", (320, 240), (30, 90, 140)).save(png, "PNG")
    uri, mime, nbytes = H.image_vers_data_uri(png)
    assert uri.startswith("data:image/") and ";base64," in uri and nbytes <= H.MAX_IMG_DATA_O
    frag = H.fragment_figure_data(uri, alt="Scanner thorax", titre="BPCO — emphysème",
                                  source="Wikimedia Commons", auteur="Exemple", licence="CC BY-SA 4.0",
                                  anomalies=["Bulle d'emphysème au sommet droit", "Aplatissement diaphragmatique"])
    assert "<figure" in frag and 'src="data:image/' in frag
    assert "CC BY-SA 4.0" in frag and "Wikimedia Commons" in frag
    assert "<ol" in frag and ("Bulle d&#x27;emphysème" in frag or "Bulle d'emphysème" in frag)
    out = tmp_path / "x.fragment.html"; out.write_text(frag, encoding="utf-8")
    # voie CLI --image
    r = subprocess.run([str(RACINE / "coeur/bin/harnais"), "illustrer", "--image", str(png),
                        "--titre", "T", "--source", "Wikimedia Commons", "--auteur", "A", "--licence", "CC0",
                        "--anomalies", "Anomalie 1|Anomalie 2", "--fragment-sortie", str(tmp_path / "cli.fragment.html")],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    j = json.loads(r.stdout); assert j["octets_binaires"] <= 25_000 and Path(j["fragment"]).exists()

def test_controle_images_point9(tmp_path):
    """Contrôle p9 : data:+licence OK ; externe/NC critiques ; absence = avertissement."""
    f = squelette(tmp_path); t = f.read_text(encoding="utf-8")
    # 1) absence → avert
    R0 = H.controler(None, f, francais=False)
    assert any("aucune image" in x["msg"] for x in R0["semantique_detecte"] if x["niveau"] == "avert")
    # 2) figure conforme
    from PIL import Image
    png = tmp_path / "ok.png"; Image.new("RGB", (64, 48), (10, 10, 10)).save(png)
    uri, _, _ = H.image_vers_data_uri(png)
    fig = H.fragment_figure_data(uri, alt="x", titre="Radio", source="Wikimedia Commons File:X.jpg",
                                 auteur="N. N.", licence="CC BY 4.0", anomalies=["Opacité basale droite"])
    t2 = t.replace('<h3 id="dx2-p9"><strong>9. Examens complémentaires</strong></h3>',
                   '<h3 id="dx2-p9"><strong>9. Examens complémentaires</strong></h3>\n' + fig, 1)
    f.write_text(t2, encoding="utf-8")
    R1 = H.controler(None, f, francais=False)
    assert R1["info"].get("images_p9", {}).get("ok") == 1
    assert not any("p9 image" in x["msg"] and x["niveau"] == "critique"
                   for c in ("securite", "sources", "semantique_detecte") for x in R1[c])
    # 3) image externe → critique
    fig_ext = fig.replace(uri, "https://upload.wikimedia.org/exemple.jpg")
    f.write_text(t.replace('<h3 id="dx2-p9"><strong>9. Examens complémentaires</strong></h3>',
                           '<h3 id="dx2-p9"><strong>9. Examens complémentaires</strong></h3>\n' + fig_ext, 1), encoding="utf-8")
    R2 = H.controler(None, f, francais=False); M2 = json.dumps(R2, ensure_ascii=False)
    assert "src externe" in M2 or "ressource externe" in M2
    # 4) licence NC → critique
    fig_nc = fig.replace("CC BY 4.0", "CC BY-NC 4.0")
    f.write_text(t.replace('<h3 id="dx2-p9"><strong>9. Examens complémentaires</strong></h3>',
                           '<h3 id="dx2-p9"><strong>9. Examens complémentaires</strong></h3>\n' + fig_nc, 1), encoding="utf-8")
    R3 = H.controler(None, f, francais=False)
    assert any("NC/ND" in x["msg"] or "non libre" in x["msg"] for x in R3["sources"])

def test_illustrer_copie_et_cli():
    """illustrer.py est présent (copie), CLI expose la sous-commande, délégation --help via script."""
    assert H.ILLUSTRER_PY.is_file() and (H.ILLUSTRATION / "README.md").is_file()
    assert (H.ILLUSTRATION / "polices" / "AtkinsonHyperlegible-Regular.ttf").is_file()
    r = subprocess.run([str(RACINE / "coeur/bin/harnais"), "--help"], capture_output=True, text=True)
    assert r.returncode == 0 and "illustrer" in r.stdout
    r2 = subprocess.run([str(RACINE / "coeur/bin/harnais"), "illustrer", "--help"], capture_output=True, text=True)
    assert r2.returncode == 0 and "--chercher" in r2.stdout and "--data-uri" in r2.stdout

def test_p9_gold_standard_et_termes_vagues(tmp_path):
    """Rév. prompt 9.11.2026 : p9 sans sous-titre gold standard ni 1re intention = critique ; terme vague = avertissement."""
    f = squelette(tmp_path); t = f.read_text(encoding="utf-8")
    R0 = H.controler(None, f, francais=False)
    assert R0["info"]["contenu_p9"]["sous_titres"] == {"gold_standard": True, "premiere_intention": True}
    t2 = re.sub(r'<h4 id="dx2-p9[ab]">.*?</h4>', "", t)
    t2 = t2.replace("(ou « pas de gold standard » écrit)", "").replace("⟦À RÉDIGER⟧ gold standard", "⟦À RÉDIGER⟧ On voit une tache au poumon droit")
    f.write_text(t2, encoding="utf-8"); R1 = H.controler(None, f, francais=False)
    assert any("aucun sous-titre « gold standard »" in x["msg"] and x["niveau"] == "critique" for x in R1["semantique_detecte"])
    assert any("terme(s) vague(s)" in x["msg"] and x["niveau"] == "avert" for x in R1["semantique_detecte"])
