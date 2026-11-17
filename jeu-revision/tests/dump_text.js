// Extrait tout le texte affiché (cartes + cas) pour le contrôle de reprise textuelle.
global.window = global; const fs = require("fs"), path = require("path"); const R = path.join(__dirname, "..");
for (const f of ["data/sources.js", "data/systems.js", "data/cards/cardio.js", "data/services/urgences-cardio.js"]) eval(fs.readFileSync(path.join(R, f), "utf8"));
const out = []; const skip = ["url", "id", "lu_le", "titre", "editeur", "portee"];
const walk = (o, k) => { if (typeof o === "string") { if (!skip.includes(k)) out.push(o); } else if (o && typeof o === "object") for (const kk in o) walk(o[kk], kk); };
walk({ c: JEU.cards || JEU.data, s: JEU.services }); console.log(out.join("\n"));
