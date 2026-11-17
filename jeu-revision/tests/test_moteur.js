/**
 * Tests unitaires du moteur (Node, sans navigateur) : progression, Leitner, maîtrise,
 * calibration, angles morts, vitesse, grades, préparation PROFILES, export/import,
 * duel (pénalités, étoiles, chrono, confiance) et validateur (cas négatifs).
 * Usage : node tests/test_moteur.js
 */
const assert = require("assert");
const { charger } = require("../tools/charger");
const vm = require("vm"), fs = require("fs"), path = require("path");
const J = charger();
const ctx = J.__ctx;
let n = 0, ko = 0;
const eq = (a, b, m) => assert.strictEqual(JSON.stringify(a), JSON.stringify(b), m);
const t = (nom, f) => { n++; try { f(); console.log("PASS " + nom); } catch (e) { ko++; console.log("FAIL " + nom + " — " + e.message); } };

// Contexte : stockage mémoire + horloge réglable
const mem = {}; let maintenant = Date.parse("2026-11-17T09:00:00");
const G = J.__global;
G.localStorage = { getItem: k => (k in mem ? mem[k] : null), setItem: (k, v) => { mem[k] = String(v); }, removeItem: k => { delete mem[k]; } };
G.JEU.horloge = { now: () => maintenant };
const run = f => vm.runInContext(fs.readFileSync(path.join(__dirname, "..", f), "utf8"), J.__ctx, { filename: f });
run("js/engine/progression.js"); run("js/engine/duel.js");
const P = G.JEU.progression; P.charger(); P.reset();
const JOUR = 86400000;
const coup = (o) => P.enregistrer(Object.assign({ sp: "cardiologie", pa: "stemi", ech: 3, src: "duel", carte: "stemi", v: "bon", conf: "sur", ms: 5000, mode: "urgence" }, o));

t("Confiance obligatoire et validée", () => { assert.throws(() => P.enregistrer({ conf: "peut-être" })); });
t("Leitner : juste + sûr fait monter de boîte", () => { P.reset(); coup({}); coup({}); assert.strictEqual(P.items()["stemi|3"].boite, 3); });
t("Leitner : juste au hasard = boîte 1 (non maîtrisé)", () => { P.reset(); coup({}); coup({ conf: "hasard" }); assert.strictEqual(P.items()["stemi|3"].boite, 1); });
t("Leitner : faux + sûr = angle mort, prioritaire", () => {
  P.reset(); coup({ pa: "ep", ech: 5 }); coup({ pa: "ep", ech: 5 }); coup({ v: "erreur", conf: "sur" });
  const d = P.dues(maintenant + 1); assert.strictEqual(d[0].cle, "stemi|3"); assert.ok(d[0].angleMort);
});
t("Leitner : 5 boîtes, intervalles 0/1/7/14/30 j", () => { eq(P.LEITNER, [0, 1, 7, 14, 30]); P.reset(); for (let i = 0; i < 8; i++) coup({}); assert.strictEqual(P.items()["stemi|3"].boite, 5); });
t("Maîtrise : sûr à J0, J+1 et J+7", () => {
  P.reset(); const t0 = maintenant;
  coup({}); assert.ok(!P.items()["stemi|3"].maitrise);
  maintenant = t0 + JOUR; coup({}); assert.ok(!P.items()["stemi|3"].maitrise);
  maintenant = t0 + 7 * JOUR; coup({}); assert.ok(P.items()["stemi|3"].maitrise);
  coup({ v: "erreur", conf: "hesitant" }); assert.ok(!P.items()["stemi|3"].maitrise, "une erreur récente retire la maîtrise");
  maintenant = t0;
});
t("Maîtrise : hésitant ne compte pas", () => { P.reset(); const t0 = maintenant; coup({ conf: "hesitant" }); maintenant += JOUR; coup({ conf: "hesitant" }); maintenant += 6 * JOUR; coup({ conf: "hesitant" }); assert.ok(!P.items()["stemi|3"].maitrise); maintenant = t0; });
t("Pathologie maîtrisée = 7 échelons, grade et préparation", () => {
  P.reset(); const t0 = maintenant;
  [0, 1, 7].forEach(j => { maintenant = t0 + j * JOUR; for (let e = 1; e <= 7; e++) coup({ ech: e }); });
  const patho = G.JEU.specialites[0].pathologies;
  const m = P.maitrise(patho); assert.ok(m.stemi.maitrisee); assert.ok(!m.ep.maitrisee);
  const g = P.grade(patho); assert.strictEqual(g.n, 1); assert.strictEqual(g.grade, "Externe");
  const prep = P.preparation(patho, G.JEU.profiles); assert.strictEqual(prep.S2.maitrisees, 1); assert.ok(prep.S2.total >= 6);
  maintenant = t0 + 40 * JOUR; assert.ok(P.items()["stemi|1"].rappel, "rappel à J+30");
  maintenant = t0;
});
t("Grades : seuils 25/50/75/90 %", () => { eq(P.GRADES.map(g => g[0]), [0, 0.25, 0.5, 0.75, 0.9]); eq(P.GRADES.slice(0, 4).map(g => g[1]), ["Externe", "Interne", "Chef de clinique", "Médecin cadre"]); });
t("Calibration et excès de confiance", () => {
  P.reset(); for (let i = 0; i < 5; i++) coup({ v: i < 2 ? "bon" : "erreur", conf: "sur" }); for (let i = 0; i < 5; i++) coup({ v: "bon", conf: "hesitant" });
  const c = P.calibration(); assert.strictEqual(c.sur.n, 5); assert.strictEqual(Math.round(c.sur.precision * 100), 40); assert.ok(c.exces);
});
t("Angles morts : sûr, drapeau rouge, différentiel mortel ; récents d’abord", () => {
  P.reset();
  coup({ v: "erreur", conf: "sur", carte: "aspirine", cas: "x" });
  maintenant += 1000; coup({ v: "erreur", conf: "hesitant", ech: 3, g: "dangereuse", carte: "nitres", cas: "x" });
  maintenant += 1000; coup({ v: "erreur", conf: "hasard", ech: 4, mortel: true, carte: "pericardite", cas: "x" });
  coup({ v: "erreur", conf: "hesitant", ech: 5, g: "mineure", carte: "oxygene", cas: "x" });
  const a = P.anglesMorts(); assert.strictEqual(a.length, 3); assert.strictEqual(a[0].carte, "pericardite");
  eq(a.map(x => x.types[0]), ["differentiel-mortel", "drapeau-rouge", "sur"]);
});
t("Vitesse : médiane par échelon, objectif urgence 20 s", () => {
  P.reset(); [4000, 30000, 25000].forEach(ms => coup({ ms })); const v = P.vitesse(); assert.strictEqual(v[3].median, 25000); assert.strictEqual(v.urgence.atteint, false);
});
t("Carte de chaleur spécialité × échelon", () => { P.reset(); coup({ ech: 5 }); coup({ ech: 5, v: "erreur" }); const c = P.chaleur()["cardiologie|5"]; assert.strictEqual(c.n, 2); assert.strictEqual(c.precision, 0.5); });
t("Export puis import : fusion sans perte, sans doublon", () => {
  P.reset(); coup({}); coup({ ech: 4 }); const ex = P.exporter();
  P.reset(); coup({ ech: 6 });
  const r = P.importer(ex); assert.ok(r.ok); assert.strictEqual(r.ajoutes, 2); assert.strictEqual(P.get().coups.length, 3);
  const r2 = P.importer(ex); assert.strictEqual(r2.ajoutes, 0); assert.strictEqual(P.get().coups.length, 3);
});
t("Import : refuse schéma, version et coups invalides", () => {
  assert.ok(!P.importer("pas du json").ok);
  assert.ok(!P.importer({ schema: "autre", version: 2, coups: [], parties: [], rondes: [] }).ok);
  assert.ok(!P.importer({ schema: P.SCHEMA, version: 99, coups: [], parties: [], rondes: [] }).ok);
  assert.ok(!P.importer({ schema: P.SCHEMA, version: 2, coups: [{ id: "a", ts: 1, ech: 9 }], parties: [], rondes: [] }).ok);
});
t("Migration du journal v1", () => {
  for (const k in mem) delete mem[k];
  mem["revmed.journal.v1"] = JSON.stringify({ version: 1, erreurs: [{ ts: "2026-11-16T10:00:00Z", cas: "c", etape: "e", carte: "aspirine", fiche: "dissection" }] });
  P.charger(); assert.strictEqual(P.get().coups.length, 1); assert.strictEqual(P.get().coups[0].carte, "aspirine");
  P.charger(); assert.strictEqual(P.get().coups.length, 1, "pas de double migration");
});

// Duel
const cas = G.JEU.specialites[0].cas[0];
t("Duel : la confiance est exigée", () => { const d = new G.JEU.Duel(cas); assert.throws(() => d.play("ecg")); });
t("Duel : erreur dangereuse −30, mineure −10, inutile −5 et +60 s", () => {
  const d = new G.JEU.Duel(cas);
  assert.strictEqual(d.play("aspirine", "sur").perte, 30);
  assert.strictEqual(d.play("oxygene", "hasard").perte, 10);
  d.play("ecg", "sur"); d.play("angio-ct", "sur"); d.suivante(); d.play("stemi", "sur"); d.suivante();
  const r = d.play("troponine", "hesitant"); assert.strictEqual(r.verdict, "inutile"); assert.strictEqual(r.perte, 5); assert.strictEqual(d.penaliteS, 60);
});
t("Duel : 3 étoiles sans faute, chrono respecté ; échelon par phase", () => {
  const d = new G.JEU.Duel(cas); const t0 = maintenant;
  assert.strictEqual(d.echelon, 3);
  d.play("ecg", "sur"); d.play("angio-ct", "sur"); d.suivante(); assert.strictEqual(d.echelon, 4);
  d.play("stemi", "sur"); d.suivante(); d.play("derivations-droites", "sur"); d.suivante();
  ["aspirine", "hnf"].forEach(c => d.play(c, "sur")); const r = d.play("icp", "sur");
  assert.strictEqual(r.statut, "victoire"); assert.strictEqual(r.etoiles, 3); maintenant = t0;
});
t("Duel : chrono dépassé et PV < 80 coûtent des étoiles", () => {
  const d = new G.JEU.Duel(cas); const t0 = maintenant;
  d.play("aspirine", "sur"); d.play("ecg", "sur"); d.play("angio-ct", "sur"); d.suivante(); d.play("stemi", "sur"); d.suivante(); d.play("derivations-droites", "sur"); d.suivante();
  maintenant = t0 + (cas.chrono + 5) * 1000;
  ["aspirine", "hnf"].forEach(c => d.play(c, "sur")); const r = d.play("icp", "sur");
  assert.strictEqual(r.etoiles, 1); maintenant = t0;
});
t("Duel : mode Entraînement sans chrono", () => { const d = new G.JEU.Duel(cas, { mode: "entrainement" }); assert.strictEqual(d.chronoActif, false); assert.strictEqual(d.tempsRestantS(), null); });

t("Duel : Consultation sans chrono, examen inutile pénalisé", () => {
  const c = JSON.parse(JSON.stringify(cas)); c.mode = "consultation"; delete c.chrono;
  const d = new G.JEU.Duel(c); assert.strictEqual(d.chronoActif, false);
  d.play("ecg", "sur"); d.play("angio-ct", "sur"); d.suivante(); d.play("stemi", "sur"); d.suivante();
  assert.strictEqual(d.play("troponine", "sur").perte, 5);
});

// Validateur : cas négatifs
const clone = o => JSON.parse(JSON.stringify(o));
const V = sp => G.JEU.schema.valider([sp], G.JEU.sources, { profiles: G.JEU.profiles, parcours: G.JEU.parcours }).erreurs;
t("Validateur : les données livrées passent", () => eq(V(clone(G.JEU.specialites[0])), []));
t("Validateur : affirmation sans source ni « À vérifier »", () => { const s = clone(G.JEU.specialites[0]); s.cartes[0].rubriques.demarche.push({ t: "Phrase.", s: [] }); assert.ok(V(s).some(e => /sans source ni/.test(e))); });
t("Validateur : clinique appuyée sur la seule pharmacologie", () => { const s = clone(G.JEU.specialites[0]); s.cartes[0].rubriques.diagnostic.push({ t: "Critère.", s: ["os-nitres"] }); assert.ok(V(s).some(e => /sans source suisse/.test(e))); });
t("Validateur : dose sans extrait swissmedicinfo", () => { const s = clone(G.JEU.specialites[0]); s.cartes[0].rubriques.priseEnCharge.push({ t: "Donne 250 mg.", s: ["hug-smur-sca"] }); assert.ok(V(s).some(e => /dose/.test(e))); });
t("Validateur : rubrique manquante, différentiels hors ordre, phase hors ordre, 3–5 duels", () => {
  const s = clone(G.JEU.specialites[0]);
  delete s.cartes[0].rubriques.suivi;
  s.cartes[0].rubriques.differentiels = [{ dx: "A", tue: false, t: "x. À vérifier.", s: [] }, { dx: "B", tue: true, t: "y. À vérifier.", s: [] }];
  s.cas[0].etapes[1].phase = "trier"; s.cas[0].etapes[0].phase = "traiter";
  s.cas[0].etapes = s.cas[0].etapes.slice(0, 2);
  const e = V(s).join("\n");
  ["rubrique « suivi » manquante", "qui tuent passent en premier", "hors ordre clinique", "3 à 5 duels"].forEach(m => assert.ok(e.includes(m), m));
});
t("Validateur : SSP inconnue, gravité manquante, cas final sans piège", () => {
  const s = clone(G.JEU.specialites[0]);
  s.pathologies[0].ssp = ["Z9.9"]; delete s.cas[0].etapes[0].regles.aspirine.gravite;
  const f = clone(s.cas[0]); f.id = "final"; f.mode = "final"; s.cas.push(f);
  const e = V(s).join("\n");
  ["SSP inconnue", "gravité dangereuse ou mineure", "un cas final combine"].forEach(m => assert.ok(e.includes(m), m));
});
t("Validateur : question rédigée mal formée", () => { const s = clone(G.JEU.specialites[0]); s.questions = [{ id: "q1", pathologie: "stemi", echelon: 9, enonce: "?", choix: [{ t: "a", juste: true }, { t: "b", juste: true }] }]; const e = V(s).join("\n"); assert.ok(e.includes("échelon hors 1–7") && e.includes("un seul juste")); });

console.log(`\n${n - ko}/${n} tests moteur réussis`);
process.exit(ko ? 1 : 0);
