/**
 * Moteur de duel : fait progresser un cas étape par étape.
 * Aucune dépendance au DOM ; l’interface écoute les résultats de play().
 */
window.JEU = window.JEU || {};
JEU.Duel = class Duel {
  constructor(service, cas) {
    this.service = service;
    this.cas = cas;
    this.reset();
  }

  reset() {
    this.indexEtape = 0;
    this.pv = this.cas.pvInitial;
    this.revele = new Set();
    this.jouees = [];               // [{ carte, verdict }] pour l’étape courante
    this.erreursPartie = 0;
    this.statut = "en-cours";       // "en-cours" | "victoire" | "defaite"
  }

  get etape() { return this.cas.etapes[this.indexEtape]; }
  get main() {
    const jouees = new Set(this.jouees.map(j => j.carte));
    return this.etape.main.filter(id => !jouees.has(id));
  }
  get objectifsRestants() {
    const ok = new Set(this.jouees.filter(j => j.compteObjectif).map(j => j.carte));
    return this.etape.objectifs.filter(id => !ok.has(id));
  }

  /** Joue une carte et retourne le verdict complet. */
  play(idCarte) {
    if (this.statut !== "en-cours") return null;
    if (!this.main.includes(idCarte)) return null;
    const e = this.etape;
    let r = Object.assign({ verdict: "neutre", msg: "Ce geste ne change rien à ce stade.", pv: 0 }, e.regles[idCarte] || {});

    // Variante si un prérequis manque (ex. imagerie avant l’ECG).
    if (r.avant && !r.avant.requiert.every(id => this.jouees.some(j => j.carte === id))) {
      r = Object.assign({}, r, { verdict: r.avant.verdict, msg: r.avant.msg });
    }
    const compteObjectif = e.objectifs.includes(idCarte) && r.verdict !== "erreur";

    if (r.verdict === "erreur") {
      this.pv = Math.max(0, this.pv - (r.pv || 0));
      this.erreursPartie++;
    }
    if (r.revele) this.revele.add(r.revele);
    this.jouees.push({ carte: idCarte, verdict: r.verdict, compteObjectif });

    const res = {
      carte: idCarte, verdict: r.verdict, msg: r.msg, perte: r.verdict === "erreur" ? (r.pv || 0) : 0,
      fiche: r.verdict === "erreur" ? (r.fiche || idCarte) : null,
      revele: r.revele || null, etape: e.id, etapeGagnee: false, statut: this.statut
    };

    if (this.pv <= 0) { this.statut = "defaite"; res.statut = "defaite"; return res; }
    if (this.objectifsRestants.length === 0) {
      res.etapeGagnee = true;
      if (this.indexEtape >= this.cas.etapes.length - 1) { this.statut = "victoire"; res.statut = "victoire"; }
    }
    return res;
  }

  /** Passe au duel suivant (appelé par l’interface après l’animation de victoire). */
  suivante() {
    if (this.indexEtape < this.cas.etapes.length - 1) { this.indexEtape++; this.jouees = []; return true; }
    return false;
  }
};
