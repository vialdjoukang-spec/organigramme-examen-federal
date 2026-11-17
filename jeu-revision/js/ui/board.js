/**
 * Plateau de duel (écran 1).
 * Affiche le dossier patient, l’adversaire, les cartes jouées, la main et le retour immédiat.
 */
window.JEU = window.JEU || {};
JEU.ui = JEU.ui || {};
JEU.ui.board = (function () {
  const { h, $, pulse, reducedMotion } = JEU.dom;
  let duel = null;
  let dealer = true;          // anime la distribution au début de chaque duel
  let nouveauRevele = null;   // élément de dossier à retourner
  let dernier = null;         // dernier résultat (feedback)

  /* ---------- Écran d’accueil : carte des services (squelette narratif) ---------- */
  function renderAccueil(root) {
    const services = [
      { id: "urgences-cardio", nom: "Urgences cardio", etat: "Ouvert", actif: true },
      { id: "neuro", nom: "Neurologie", etat: "Bientôt", actif: false },
      { id: "infectio", nom: "Infectiologie", etat: "Bientôt", actif: false },
      { id: "pneumo", nom: "Pneumologie", etat: "Bientôt", actif: false }
    ];
    root.replaceChildren(h("section", { class: "accueil", "aria-labelledby": "accueil-titre" },
      h("p", { class: "sur-titre" }, "Internat · Tour des services"),
      h("h1", { id: "accueil-titre" }, "Ta garde commence."),
      h("p", { class: "accueil-texte" }, "Tu joues l’interne. Chaque cas se gagne en duels de cartes. Associe le bon geste à la bonne situation. Chaque erreur ouvre sa fiche."),
      h("ol", { class: "carte-services", "aria-label": "Services" }, services.map((s, i) =>
        h("li", { class: `service ${s.actif ? "service--actif" : ""}` },
          h("span", { class: "service-num" }, String(i + 1).padStart(2, "0")),
          h("span", { class: "service-nom" }, s.nom),
          h("span", { class: "service-etat" }, s.etat)))),
      h("button", { type: "button", class: "btn btn-primaire", id: "btn-commencer", onclick: demarrer }, "Prendre la garde"),
      h("p", { class: "aide" }, "Raccourcis : touches 1 à 9 pour jouer une carte de ta main.")
    ));
    $("#btn-commencer").focus();
  }

  function demarrer() {
    const sv = JEU.registry.service("urgences-cardio");
    duel = new JEU.Duel(sv, sv.cas[0]);
    dealer = true; dernier = null; nouveauRevele = null;
    render();
    const premier = $(".main .carte-action");
    if (premier) premier.focus();
  }

  /* ---------- Plateau ---------- */
  function render() {
    const root = $("#vue-plateau");
    if (!duel) return renderAccueil(root);
    const cas = duel.cas, e = duel.etape;
    root.replaceChildren(
      h("div", { class: "plateau" },
        barreCas(cas),
        h("div", { class: "plateau-grille" },
          dossier(cas),
          arene(e)),
        main(e)));
    dealer = false; nouveauRevele = null;
  }

  function barreCas(cas) {
    const pv = duel.pv, pct = Math.round(pv / cas.pvInitial * 100);
    return h("div", { class: "barre-cas" },
      h("div", {},
        h("p", { class: "sur-titre" }, `Urgences cardio · ${cas.titre}`),
        h("ol", { class: "etapes", "aria-label": "Progression des duels" }, cas.etapes.map((et, i) =>
          h("li", { class: i < duel.indexEtape || duel.statut === "victoire" ? "fait" : i === duel.indexEtape ? "courant" : "",
            "aria-current": i === duel.indexEtape ? "step" : null }, h("span", {}, et.titre.replace(/^Duel \d · /, "")))))),
      h("div", { class: "pv" },
        h("span", { class: "pv-label", id: "pv-label" }, "État du patient"),
        h("div", { class: `pv-barre ${pct <= 40 ? "pv-bas" : ""}`, role: "progressbar", "aria-labelledby": "pv-label",
          "aria-valuemin": "0", "aria-valuemax": String(cas.pvInitial), "aria-valuenow": String(pv) },
          h("span", { style: `width:${pct}%` })),
        h("span", { class: "pv-valeur", "data-testid": "pv" }, `${pv} PV`)));
  }

  function dossier(cas) {
    const p = cas.patient;
    return h("aside", { class: "dossier", "aria-labelledby": "dossier-titre" },
      h("h2", { id: "dossier-titre", class: "bloc-titre" }, "Dossier"),
      h("p", { class: "dossier-id" }, p.identite),
      h("p", { class: "dossier-motif" }, p.motif),
      h("p", { class: "dossier-atcd" }, h("span", {}, "ATCD "), p.atcd),
      h("dl", { class: "constantes" }, p.constantes.map(k =>
        h("div", { class: `constante ${k.alerte ? "alerte" : ""}` }, h("dt", {}, k.label), h("dd", {}, k.valeur)))),
      h("ul", { class: "signes" }, p.signes.map(s => h("li", { class: s.alerte ? "alerte" : "" }, s.t))),
      h("div", { class: "examens" }, Object.entries(cas.dossier).map(([id, d]) => {
        const vu = duel.revele.has(id);
        return h("div", { class: `examen ${vu ? "revele" : ""} ${id === nouveauRevele && !reducedMotion() ? "flip" : ""}`, "data-examen": id },
          h("div", { class: "examen-face examen-attente", "aria-hidden": vu ? "true" : "false" }, h("strong", {}, d.titre), h("span", {}, d.attente)),
          h("div", { class: "examen-face examen-resultat", "aria-hidden": vu ? "false" : "true" }, h("strong", {}, d.titre), h("span", {}, d.texte)));
      })));
  }

  function arene(e) {
    const adv = JEU.registry.card(e.adversaire);
    const fin = duel.statut !== "en-cours";
    return h("section", { class: "arene", "aria-labelledby": "duel-titre" },
      h("div", { class: "arene-tete" },
        h("h2", { id: "duel-titre" }, e.titre),
        h("p", { class: "consigne" }, e.consigne)),
      h("div", { class: "arene-face" },
        h("div", { class: "adversaire" },
          h("p", { class: "zone-label" }, "Situation"),
          JEU.ui.renderCard(adv, { mode: "lecture", extraClass: "carte--adversaire" })),
        h("div", { class: "vs", "aria-hidden": "true" }, "vs"),
        h("div", { class: "jouees" },
          h("p", { class: "zone-label" }, `Tes coups · objectifs restants : ${duel.objectifsRestants.length}`),
          h("div", { class: "jouees-liste" }, duel.jouees.length ? duel.jouees.map((j, i) =>
            JEU.ui.renderCard(JEU.registry.card(j.carte), {
              mode: "lecture",
              extraClass: `mini verdict--${j.verdict} ${i === duel.jouees.length - 1 && dernier ? "anim-joue" : ""}`
            })) : h("p", { class: "vide" }, "Joue une carte de ta main.")))),
      feedback(),
      fin ? debrief() : null);
  }

  function feedback() {
    const box = h("div", { id: "feedback", class: `feedback ${dernier ? "feedback--" + dernier.verdict : ""}`, role: "status", "aria-live": "polite" });
    if (!dernier) { box.append("Choisis ta carte. Lis le dossier d’abord."); return box; }
    const label = { bon: "Bon réflexe", erreur: "Erreur", neutre: "Info" }[dernier.verdict];
    box.append(h("span", { class: "feedback-tag" }, label), h("span", {}, dernier.msg.replace(/^(Bon réflexe|Erreur)\.\s*/, "")));
    if (dernier.perte) box.append(h("span", { class: "feedback-pv" }, `−${dernier.perte} PV`));
    if (dernier.fiche) box.append(h("button", { type: "button", class: "btn btn-lien", onclick: () => JEU.ui.fiche.open(dernier.fiche, dernier.msg) }, "Revoir la fiche"));
    if (dernier.etapeGagnee && duel.statut === "en-cours") {
      box.append(h("button", { type: "button", class: "btn btn-primaire", id: "btn-suivant", onclick: suivant }, "Duel suivant"));
    }
    return box;
  }

  function debrief() {
    const ok = duel.statut === "victoire";
    return h("div", { class: `debrief ${ok ? "debrief--ok" : "debrief--ko"}`, "aria-labelledby": "debrief-titre" },
      h("h3", { id: "debrief-titre" }, ok ? "Cas résolu." : "Le patient se dégrade."),
      ok ? h("ul", {}, duel.cas.debrief.map(t => h("li", {}, t))) : h("p", {}, "Les PV sont tombés à zéro. Relis les fiches ouvertes, puis rejoue."),
      h("p", {}, `PV restants : ${duel.pv}. Erreurs : ${duel.erreursPartie}.`),
      h("div", { class: "debrief-actions" },
        h("button", { type: "button", class: "btn btn-primaire", id: "btn-rejouer", onclick: demarrer }, "Rejouer le cas"),
        h("button", { type: "button", class: "btn", onclick: () => JEU.app.montrer("journal") }, "Voir le journal")));
  }

  function main(e) {
    const ids = duel.main;
    const fin = duel.statut !== "en-cours" || (dernier && dernier.etapeGagnee);
    return h("section", { class: `main ${fin ? "main--inactive" : ""}`, "aria-labelledby": "main-titre" },
      h("h2", { id: "main-titre", class: "bloc-titre" }, "Ta main"),
      h("div", { class: "main-cartes" }, ids.map((id, i) => {
        const el = JEU.ui.renderCard(JEU.registry.card(id), { mode: fin ? "lecture" : "main", onPlay: jouer, delay: dealer ? i * 60 : undefined, extraClass: dealer ? "anim-deal" : "" });
        el.prepend(h("span", { class: "raccourci", "aria-hidden": "true" }, String(i + 1)));
        return el;
      })));
  }

  /* ---------- Actions ---------- */
  function jouer(id) {
    if (!duel || duel.statut !== "en-cours" || (dernier && dernier.etapeGagnee)) return;
    const res = duel.play(id);
    if (!res) return;
    dernier = res;
    if (res.revele) nouveauRevele = res.revele;
    JEU.journal.enregistrerCoup({ systeme: duel.service.systeme, service: duel.service.id, cas: duel.cas.id, etape: res.etape, carte: id, verdict: res.verdict, fiche: res.fiche, msg: res.msg });
    if (res.statut !== "en-cours") JEU.journal.enregistrerPartie({ cas: duel.cas.id, pv: duel.pv, resultat: res.statut, erreurs: duel.erreursPartie });
    render();
    if (res.verdict === "erreur") {
      pulse($(".plateau"), "anim-alerte");
      // L’erreur ouvre automatiquement la fiche correspondante.
      setTimeout(() => JEU.ui.fiche.open(res.fiche, res.msg), reducedMotion() ? 0 : 450);
    } else {
      const next = $("#btn-suivant") || $("#btn-rejouer") || $(".main .carte-action");
      if (next) next.focus();
    }
  }

  function suivant() {
    if (duel.suivante()) { dealer = true; dernier = null; render(); const p = $(".main .carte-action"); if (p) p.focus(); }
  }

  /** Raccourcis clavier 1–9 : jouer la n-ième carte de la main. */
  function onKey(ev) {
    if (!duel || $("#fiche").open || $("#confirm").open || document.body.dataset.vue !== "plateau") return;
    if (ev.target.matches("input, textarea")) return;
    const n = parseInt(ev.key, 10);
    if (n >= 1 && n <= 9) { const id = duel.main[n - 1]; if (id) jouer(id); }
  }

  function init() { document.addEventListener("keydown", onKey); render(); }
  return { init, render, demarrer };
})();
