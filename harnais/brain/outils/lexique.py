#!/usr/bin/env python3
"""Construit scriptones/verbes.json : formes verbales finies du français médical (lexique stdlib des synapses α·H).
Outil de construction (spaCy au moment de la construction seulement ; les scriptones restent en stdlib pure) :
  python3 harnais/brain/outils/lexique.py [DOSSIER_DE_COURS ...]   (défaut : LOT_Claude_Finaux de origin/main, via git archive)
Sources : (1) étiquetage spaCy fr_core_news_sm des cours réels (VERB/AUX à forme finie) ; (2) conjugaison régulière d'une liste
d'infinitifs fréquents (présent, imparfait, futur, conditionnel, 3e personnes) ; (3) formes irrégulières écrites à la main.
Le lexique est déterministe (trié) et figé par empreinte SHA-256 (SHA256SUMS)."""
import json, re, subprocess, sys, tempfile
from pathlib import Path
B = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(B / "scriptones"))
import bus

ER = """accompagner accélérer activer adapter affecter aggraver aider ajouter ajuster alerter aligner alimenter altérer améliorer amener analyser
annoncer anticiper apparaître appliquer apporter arrêter associer assurer atteindre augmenter autoriser baisser bloquer calculer causer centrer
changer chercher citer classer coexister commencer compenser compléter compliquer comporter compter concerner confirmer consister consulter contrôler
corriger coûter créer culminer débuter décider déclencher défier délivrer demander démontrer dépasser dépendre déplacer désigner détecter
déterminer développer devenir diagnostiquer diminuer documenter doser durer éclairer écarter éliminer empêcher employer encadrer engager
entraîner entrer envisager estimer évaluer éviter évoluer évoquer examiner exclure exiger expliquer exposer exprimer faciliter favoriser
fixer fonder former freiner gagner garder gérer guider hospitaliser identifier ignorer imposer indiquer influencer informer injecter inquiéter
installer interdire interpréter interroger inverser isoler justifier limiter localiser manipuler manquer marquer masquer mesurer modifier
montrer motiver multiplier nécessiter noter observer occuper orienter oublier passer peser placer porter poser préciser prédire préférer
prélever préparer prescrire présenter préserver presser prévenir procéder proposer protéger prouver provoquer quantifier rassurer réaliser
recommander rechercher récupérer réduire refléter régler relever remplacer renforcer repérer reposer représenter résister respecter rester
restaurer résulter retarder retirer révéler risquer séparer signaler signer simuler situer soigner souligner stabiliser suggérer supprimer
surveiller suspecter tarder témoigner tenter tester toucher traiter transférer transmettre trancher transporter trouver utiliser valider
varier vérifier viser""".split()
IRR = """est sont a ont était étaient sera seront serait seraient fut furent avait avaient aura auront aurait auraient peut peuvent pouvait
pourra pourrait doit doivent devait devra devrait faut fallait faudra faudrait fait font faisait fera feront ferait va vont allait ira iront
vient viennent venait tient tiennent maintient maintiennent obtient obtiennent contient contiennent devient deviennent survient surviennent
prévient préviennent intervient interviennent provient proviennent reste restent dit disent permet permettent met mettent admet admettent
transmet transmettent prend prennent comprend comprennent reprend reprennent apprend surprend voit voient prévoit prévoient revoit sait savent
suit suivent poursuit vit vivent produit produisent réduit réduisent conduit conduisent induit induisent traduit introduit construit détruit
reçoit reçoivent perçoit conçoit décrit décrivent prescrit prescrivent inscrit écrit écrivent lit lisent rejoint atteint atteignent
éteint craint peint dépend dépendent répond répondent rend rendent tend tendent étend étendent attend attendent entend entendent perd perdent
descend descendent vaut valent équivaut prévaut sort sortent part partent ressort dort sert servent offre offrent ouvre ouvrent couvre
couvrent découvre souffre souffrent meurt meurent naît naissent paraît paraissent apparaît apparaissent disparaît connaît connaissent
reconnaît croît croissent décroît accroît accroissent conclut concluent exclut excluent inclut incluent résout résolvent dissout absout
fuit acquiert acquièrent requiert requièrent conquiert court courent recourt parcourt secourt boit boivent cuit nuit plaît suffit suffisent
choisit choisissent finit finissent agit agissent réagit réagissent établit établissent rétablit grandit guérit guérissent noircit rougit
pâlit vieillit grossit maigrit fournit fournissent remplit saisit unit réunit définit définissent ralentit ralentissent affaiblit aboutit
aboutissent subit subissent avertit convertit investit garantit garantissent envahit trahit nourrit pourrit fleurit jaunit blanchit
s'agit s'accompagne s'explique s'installe s'observe s'aggrave s'améliore""".split()


# homographes nom/verbe à la 3e personne du singulier : retirés (une phrase nominale « La mesure de la pression. » ne doit pas passer pour verbale)
HOMOGRAPHES = set("""mesure cause marque forme porte place note garde contrôle change pose dose signe risque aide manque compte demande fixe règle
poste base charge sonde ligne face file perte trace masque passe reste_n""".split())


def conj(inf):
    if not inf.endswith("er"): return []
    s = inf[:-2]; f = [s + "e", s + "ent", s + "ait", s + "aient", inf + "a", inf + "ont", inf + "ait", inf + "aient"]
    if s.endswith("g"): f += [s + "eait", s + "eaient"]
    if s.endswith("c"): f += [s[:-1] + "çait", s[:-1] + "çaient"]
    if re.search(r"é[a-z]+$", s):   # préférer → préfère, accélérer → accélère
        s2 = re.sub(r"é([a-z]+)$", r"è\1", s); f += [s2 + "e", s2 + "ent"]
    return f


def corpus(dossiers):
    if not dossiers:
        d = tempfile.mkdtemp(); subprocess.run(f"git -C {bus.R} archive origin/main LOT_Claude_Finaux | tar -x -C {d}", shell=True, check=True); dossiers = [d]
    for d in dossiers:
        for f in sorted(Path(d).rglob("*.html")):
            t = bus.lire(f)[0]; a, b = bus.bornes_cours(t)
            yield from bus.phrases(bus.texte(t[a:b]))


def main(dossiers):
    formes = set(IRR) | {x for i in ER for x in conj(i)}
    try:
        import spacy
        nlp = spacy.load("fr_core_news_sm", disable=["ner", "parser"]); n = 0; fin = {}; tot = {}
        for d in nlp.pipe(corpus(dossiers), batch_size=512):
            n += 1
            for x in d:
                w = x.text.lower(); tot[w] = tot.get(w, 0) + 1
                if x.pos_ in ("VERB", "AUX") and "VerbForm=Fin" in str(x.morph) and x.text.isalpha() and len(x.text) > 1: fin[w] = fin.get(w, 0) + 1
        # une forme n'entre que si spaCy la voit verbe fini au moins 2 fois ET dans au moins 60 % de ses occurrences (exclut traitement, agent, rhume…)
        gardees = {w for w, k in fin.items() if k >= 2 and k / tot[w] >= 0.6 and not re.search(r"(?:ment|tion|isme|ite|ose|ine|ide|ole|ate|ème)$", w)}
        formes |= gardees
        print(f"spaCy : {n} phrases lues, {len(fin)} formes candidates, {len(gardees)} retenues")
    except (ImportError, OSError) as e:
        print(f"spaCy indisponible ({e}) : lexique réduit aux conjugaisons et formes irrégulières")
    formes -= HOMOGRAPHES
    out = B / "scriptones/verbes.json"
    out.write_text(json.dumps({"_note": "Formes verbales finies (minuscules). Construit par harnais/brain/outils/lexique.py ; ne pas éditer à la main.",
                               "formes": sorted(formes)}, ensure_ascii=False, indent=0))
    print(f"{out.relative_to(bus.R)} : {len(formes)} formes")


if __name__ == "__main__":
    main(sys.argv[1:])
