/**
 * Plateau de duel v2 (écran 1) : dossier, adversaire, coups joués, main, confiance, chrono, étoiles.
 * Choisir une carte n’est pas jouer : le coup part seulement après le choix de confiance.
 */
window.JEU = window.JEU || {};
JEU.ui = JEU.ui || {};
JEU.ui.board = (function () {
  const { h, $, pulse, reducedMotion, mmss } = JEU.dom;
  let duel = null, dealer = true, nouveauRevele = null, dernier = null, choisie = null, tTour = 0, minuteur = null;
  let examen = null, dernierPct = null;   // { file: [ids], index, resultats: [] } en mode examen blanc
  const MODE_LIB = { urgence: "Urgence", consultation: "Consultation", final: "Cas final", entrainement: "Entraînement", examen: "Examen blanc" };

  function renderAccueil(root) {
    root.replaceChildren(h("section", { class: "accueil", "aria-labelledby": "accueil-titre" },
      h("p", { class: "sur-titre" }, "Internat · Plateau"),
      h("h1", { id: "accueil-titre" }, "Choisis un cas dans le parcours."),
      h("p", { class: "accueil-texte" }, "Chaque cas se joue en duels : trier, explorer, différencier, diagnostiquer, traiter. Avant chaque coup, tu déclares ta confiance."),
      h("div", { class: "debrief-actions" },
        h("button", { type: "button", class: "btn btn-primaire", id: "btn-commencer", onclick: () => demarrer("douleur-thoracique-74") }, "Prendre la garde : urgence cardio"),
        h("button", { type: "button", class: "btn", onclick: () => JEU.app.montrer("parcours") }, "Ouvrir le parcours")),
      h("p", { class: "aide" }, "Clavier : touches 1 à 9 pour choisir une carte, puis S (sûr), H (hésitant) ou A (au hasard). Échap annule.")));
  }

  /** Démarre un cas. opts.mode force un mode (entrainement, examen). */
  function demarrer(idCas, opts = {}) {
    const cas = JEU.registry.cas(idCas);
    if (!cas) return;
    if (!opts.examen) examen = null;
    duel = new JEU.Duel(cas, { mode: opts.mode || (JEU.ui.parcours && JEU.ui.parcours.entrainement() ? "entrainement" : cas.mode) });
    dealer = true; dernier = null; nouveauRevele = null; choisie = null; dernierPct = null;
    JEU.app.montrer("plateau", true);
    render(); demarrerMinuteur();
    const p = $(".main .carte-action"); if (p) p.focus();
  }
  function demarrerExamen(ids) {
    examen = { file: ids, index: 0, resultats: [] };
    demarrer(ids[0], { mode: "examen", examen: true });
  }

  function demarrerMinuteur() {
    clearInterval(minuteur);
    if (!duel || !duel.chronoActif) return;
    minuteur = setInterval(() => {
      const el = $("#chrono"); if (!el || !duel || duel.statut !== "en-cours") return clearInterval(minuteur);
      const r = duel.tempsRestantS();
      el.textContent = r >= 0 ? mmss(r) : `+${mmss(-r)}`;
      el.classList.toggle("chrono--depasse", r < 0);
    }, 1000);
  }

  function render() {
    const root = $("#vue-plateau");
    if (!duel) return renderAccueil(root);
    root.replaceChildren(h("div", { class: "plateau" }, barreCas(), h("div", { class: "plateau-grille" }, dossier(), arene()), main()));
    dealer = false; nouveauRevele = null;
    // Barre de PV animée : part de l’ancienne valeur, glisse vers la nouvelle.
    const pctPv = Math.round(duel.pv / duel.cas.pvInitial * 100), bar = $(".pv-barre span");
    if (bar && dernierPct !== null && dernierPct !== pctPv && !reducedMotion()) {
      bar.style.width = dernierPct + "%"; void bar.offsetWidth; requestAnimationFrame(() => { bar.style.width = pctPv + "%"; });
    }
    dernierPct = pctPv;
    if (!choisie) tTour = JEU.horloge.now();
  }

  function barreCas() {
    const cas = duel.cas, pv = duel.pv, pct = Math.round(pv / cas.pvInitial * 100);
    const sp = JEU.registry.specialite(cas.specialite);
    const r = duel.tempsRestantS();
    return h("div", { class: "barre-cas" },
      h("div", {},
        h("p", { class: "sur-titre" }, h("span", { class: `tag-mode tag-mode--${duel.mode}` }, MODE_LIB[duel.mode]), ` ${sp.nom} · ${cas.titre}`,
          examen ? ` · cas ${examen.index + 1}/${examen.file.length}` : ""),
        h("ol", { class: "etapes", "aria-label": "Progression des duels" }, cas.etapes.map((et, i) =>
          h("li", { class: i < duel.indexEtape || duel.statut === "victoire" ? "fait" : i === duel.indexEtape ? "courant" : "", "aria-current": i === duel.indexEtape ? "step" : null },
            h("span", {}, et.titre.replace(/^Duel \d · /, "")))))),
      h("div", { class: "barre-droite" },
        duel.chronoActif ? h("div", { class: "chrono-bloc" }, h("span", { class: "pv-label" }, "Chrono"),
          h("span", { id: "chrono", class: `chrono ${r < 0 ? "chrono--depasse" : ""}`, role: "timer", "aria-label": "Temps restant" }, r >= 0 ? mmss(r) : `+${mmss(-r)}`)) : h("span", { class: "pv-label" }, "Sans chrono"),
        h("div", { class: "pv" },
          h("span", { class: "pv-label", id: "pv-label" }, "État du patient"),
          h("div", { class: `pv-barre ${pct <= 40 ? "pv-bas" : ""}`, role: "progressbar", "aria-labelledby": "pv-label", "aria-valuemin": "0", "aria-valuemax": String(cas.pvInitial), "aria-valuenow": String(pv) },
            h("span", { style: `width:${pct}%` })),
          h("span", { class: "pv-valeur", "data-testid": "pv" }, `${pv} PV`))));
  }

  function dossier() {
    const cas = duel.cas, p = cas.patient;
    return h("aside", { class: "dossier", "aria-labelledby": "dossier-titre" },
      h("h2", { id: "dossier-titre", class: "bloc-titre" }, "Dossier"),
      h("p", { class: "dossier-id" }, p.identite), h("p", { class: "dossier-motif" }, p.motif),
      h("p", { class: "dossier-atcd" }, h("span", {}, "ATCD "), p.atcd),
      h("dl", { class: "constantes" }, p.constantes.map(k => h("div", { class: `constante ${k.alerte ? "alerte" : ""}` }, h("dt", {}, k.label), h("dd", {}, k.valeur)))),
      h("ul", { class: "signes" }, p.signes.map(s => h("li", { class: s.alerte ? "alerte" : "" }, s.t))),
      h("div", { class: "examens" }, Object.entries(cas.dossier).map(([id, d]) => {
        const vu = duel.revele.has(id);
        return h("div", { class: `examen ${vu ? "revele" : ""} ${id === nouveauRevele && !reducedMotion() ? "flip" : ""}`, "data-examen": id },
          h("div", { class: "examen-face examen-attente", "aria-hidden": vu ? "true" : "false" }, h("strong", {}, d.titre), h("span", {}, d.attente)),
          h("div", { class: "examen-face examen-resultat", "aria-hidden": vu ? "false" : "true" }, h("strong", {}, d.titre), h("span", {}, d.texte)));
      })));
  }

  function arene() {
    const e = duel.etape, adv = JEU.registry.card(e.adversaire), fin = duel.statut !== "en-cours";
    const ech = JEU.progression.ECHELONS[duel.echelon - 1];
    return h("section", { class: "arene", "aria-labelledby": "duel-titre" },
      h("div", { class: "arene-tete" },
        h("h2", { id: "duel-titre" }, e.titre),
        h("p", { class: "phase" }, h("span", { class: "tag-phase" }, e.phase), ech ? ` Échelon ${ech[0]} · ${ech[1]}` : ""),
        h("p", { class: "consigne" }, e.consigne)),
      h("div", { class: "arene-face" },
        h("div", { class: "adversaire" }, h("p", { class: "zone-label" }, "Situation"), JEU.ui.renderCard(adv, { mode: "lecture", extraClass: "carte--adversaire" })),
        h("div", { class: "vs", "aria-hidden": "true" }, "vs"),
        h("div", { class: "jouees" },
          h("p", { class: "zone-label" }, `Tes coups · objectifs restants : ${duel.objectifsRestants.length}`),
          h("div", { class: "jouees-liste" }, duel.jouees.length ? duel.jouees.map((j, i) =>
            JEU.ui.renderCard(JEU.registry.card(j.carte), { mode: "lecture", extraClass: `mini verdict--${j.verdict} ${i === duel.jouees.length - 1 && dernier ? "anim-joue" : ""}` })) : h("p", { class: "vide" }, "Choisis une carte, puis ta confiance.")))),
      feedback(), fin ? debrief() : null);
  }

  function feedback() {
    const box = h("div", { id: "feedback", class: `feedback ${dernier ? "feedback--" + dernier.verdict : ""}`, role: "status", "aria-live": "polite" });
    if (!dernier) { box.append("Lis le dossier. Choisis ta carte."); return box; }
    const label = { bon: "Bon réflexe", erreur: dernier.gravite === "dangereuse" ? "Erreur dangereuse" : "Erreur mineure", neutre: "Info", inutile: "Examen inutile" }[dernier.verdict];
    box.append(h("span", { class: "feedback-tag" }, label), h("span", {}, dernier.msg.replace(/^(Bon réflexe|Erreur|Examen inutile[^.]*)\.\s*/, "")));
    if (dernier.perte) box.append(h("span", { class: "feedback-pv" }, `−${dernier.perte} PV`));
    if (dernier.verdict === "inutile") box.append(h("span", { class: "feedback-pv" }, "+1 min"));
    if (dernier.fiche) box.append(h("button", { type: "button", class: "btn btn-lien", onclick: () => JEU.ui.fiche.open(dernier.fiche, dernier.msg) }, "Revoir la fiche"));
    if (dernier.etapeGagnee && duel.statut === "en-cours") box.append(h("button", { type: "button", class: "btn btn-primaire", id: "btn-suivant", onclick: suivant }, "Duel suivant"));
    return box;
  }

  function etoiles(n) {
    return h("div", { class: "etoiles", role: "img", "aria-label": `${n} étoile${n > 1 ? "s" : ""} sur 3`, "data-etoiles": String(n) },
      [1, 2, 3].map(i => h("span", { class: `etoile ${i <= n ? "on" : ""}`, style: `--i:${i}`, "aria-hidden": "true" }, "★")));
  }
  function debrief() {
    const ok = duel.statut === "victoire", n = duel.etoiles();
    const suiteExamen = examen && examen.index < examen.file.length - 1;
    return h("div", { class: `debrief ${ok ? "debrief--ok" : "debrief--ko"}`, "aria-labelledby": "debrief-titre" },
      h("h3", { id: "debrief-titre" }, ok ? "Cas résolu." : "Le patient se dégrade."),
      etoiles(n),
      ok ? h("ul", {}, duel.cas.debrief.map(t => h("li", {}, t))) : h("p", {}, "Les PV sont tombés à zéro. Relis les fiches ouvertes, puis rejoue."),
      h("p", {}, `PV restants : ${duel.pv}. Erreurs : ${duel.erreursPartie}. Examens inutiles : ${duel.inutiles}. Temps patient : ${mmss(duel.tempsS())}${duel.chronoActif ? ` / ${mmss(duel.cas.chrono)}` : ""}.`),
      examen && !suiteExamen ? resultatExamen() : null,
      h("div", { class: "debrief-actions" },
        suiteExamen ? h("button", { type: "button", class: "btn btn-primaire", id: "btn-examen-suivant", onclick: () => { examen.index++; demarrer(examen.file[examen.index], { mode: "examen", examen: true }); } }, "Cas suivant de l’examen")
          : h("button", { type: "button", class: "btn btn-primaire", id: "btn-rejouer", onclick: () => demarrer(duel.cas.id) }, "Rejouer le cas"),
        h("button", { type: "button", class: "btn", onclick: () => JEU.app.montrer("tableau") }, "Voir le tableau de bord"),
        h("button", { type: "button", class: "btn", onclick: () => JEU.app.montrer("parcours") }, "Retour au parcours")));
  }
  function resultatExamen() {
    const R = examen.resultats, note = R.length ? Math.round(R.reduce((a, x) => a + x.pv / x.pvInitial, 0) / R.length * 100) : 0;
    return h("div", { class: "examen-resultat-bloc", id: "examen-resultat" },
      h("h4", {}, "Examen blanc PROFILES · structure de démonstration"),
      h("p", {}, `Score moyen : ${note} %. Cas joués : ${R.length}. Étoiles : ${R.map(x => x.etoiles).join(" · ")}.`),
      h("p", {}, "Seuil de réussite de l’examen fédéral : ", h("span", { class: "badge-verif" }, "À vérifier")));
  }

  function main() {
    const ids = duel.main;
    const fin = duel.statut !== "en-cours" || (dernier && dernier.etapeGagnee);
    const c = choisie && JEU.registry.card(choisie);
    return h("section", { class: `main ${fin ? "main--inactive" : ""}`, "aria-labelledby": "main-titre" },
      h("h2", { id: "main-titre", class: "bloc-titre" }, "Ta main"),
      h("div", { class: "main-cartes" }, ids.map((id, i) => {
        const el = JEU.ui.renderCard(JEU.registry.card(id), { mode: fin ? "lecture" : "main", onPlay: choisir, choisie: id === choisie,
          delay: dealer ? i * 60 : undefined, extraClass: `${dealer ? "anim-deal" : ""} ${id === choisie ? "carte--choisie" : ""}` });
        el.prepend(h("span", { class: "raccourci", "aria-hidden": "true" }, String(i + 1)));
        return el;
      })),
      c && !fin ? JEU.ui.confiance.panneau(`Jouer : ${c.court}`, valider, annuler) : null);
  }

  /* ---------- Actions ---------- */
  function choisir(id) {
    if (!duel || duel.statut !== "en-cours" || (dernier && dernier.etapeGagnee)) return;
    choisie = id; JEU.son.jouer("bip"); render();
    const p = $("#confiance"); if (p) p.focus();
  }
  function annuler() { const id = choisie; choisie = null; render(); const el = id && $(`.main .carte[data-id="${id}"] .carte-action`); if (el) el.focus(); }
  function valider(conf) {
    if (!choisie) return;
    const id = choisie, ms = JEU.horloge.now() - tTour;
    const res = duel.play(id, conf);
    choisie = null;
    if (!res) return render();
    dernier = res;
    if (res.revele) nouveauRevele = res.revele;
    const cas = duel.cas;
    JEU.progression.enregistrer({ sp: cas.specialite, pa: res.pathologie, ech: res.echelon, src: duel.mode === "examen" ? "examen" : "duel", cas: cas.id, et: res.etape,
      carte: id, rep: id, v: res.verdict, g: res.gravite, conf, ms, mode: duel.mode, fiche: res.fiche, mortel: res.mortel || undefined });
    if (res.statut !== "en-cours") {
      clearInterval(minuteur);
      JEU.progression.enregistrerPartie({ cas: cas.id, sp: cas.specialite, mode: duel.mode, pv: duel.pv, pvInitial: cas.pvInitial, resultat: res.statut, etoiles: res.etoiles, erreurs: duel.erreursPartie, inutiles: duel.inutiles, tempsS: duel.tempsS() });
      if (examen) examen.resultats.push({ pv: duel.pv, pvInitial: cas.pvInitial, etoiles: res.etoiles });
    }
    render();
    if (res.verdict === "erreur" || res.verdict === "inutile") {
      JEU.son.jouer("alerte");
      pulse($(".plateau"), "anim-alerte");
      setTimeout(() => JEU.ui.fiche.open(res.fiche, res.msg), reducedMotion() ? 0 : 450);
    } else {
      JEU.son.jouer(res.statut === "victoire" ? "victoire" : "valide");
      if (res.statut === "victoire") for (let i = 0; i < res.etoiles; i++) setTimeout(() => JEU.son.jouer("etoile"), 500 + i * 180);
      const next = $("#btn-suivant") || $("#btn-examen-suivant") || $("#btn-rejouer") || $(".main .carte-action");
      if (next) next.focus();
    }
  }
  function suivant() { if (duel.suivante()) { dealer = true; dernier = null; choisie = null; render(); const p = $(".main .carte-action"); if (p) p.focus(); } }

  function onKey(ev) {
    if (!duel || $("#fiche").open || $("#confirm").open || document.body.dataset.vue !== "plateau") return;
    if (ev.target.matches("input, textarea, select")) return;
    if (ev.key === "Escape" && choisie) { ev.preventDefault(); return annuler(); }
    const conf = JEU.ui.confiance.touche(ev);
    if (conf && choisie) { ev.preventDefault(); return valider(conf); }
    const n = parseInt(ev.key, 10);
    if (n >= 1 && n <= 9) { const id = duel.main[n - 1]; if (id) choisir(id); }
  }
  function init() { document.addEventListener("keydown", onKey); render(); }
  const etat = () => ({ duel, choisie, examen });
  return { init, render, demarrer, demarrerExamen, etat };
})();
