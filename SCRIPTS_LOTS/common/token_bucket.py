"""Seau à jetons entre processus d'UN MÊME agent, par verrou de fichier fcntl.
v1.4 : chaque agent a son propre dossier d'état (~/.scripts_lots/agent_N/etat) ; aucun seau n'est commun à deux agents.
Sert au budget LanguageTool de l'agent et à ses limites NCBI ou par domaine."""
import fcntl, json, os, time
from pathlib import Path

class SeauPartage:
    def __init__(self, dossier, nom, debit_par_s, capacite, debit_octets_par_s=None, capacite_octets=None):
        self.dossier = Path(dossier); self.dossier.mkdir(parents=True, exist_ok=True)
        sur = "".join(c if c.isalnum() or c in "-_." else "_" for c in nom)
        self.etat = self.dossier / f"seau_{sur}.json"; self.verrou = self.dossier / f"seau_{sur}.lock"
        self.debit, self.capacite = float(debit_par_s), float(capacite)
        self.debit_o, self.capacite_o = debit_octets_par_s, capacite_octets

    def _lire(self, now):
        try:
            e = json.loads(self.etat.read_text())
        except Exception:
            e = {"jetons": self.capacite, "octets": self.capacite_o or 0, "t": now, "bloque_jusqua": 0, "echecs": 0}
        dt = max(0.0, now - e["t"])
        e["jetons"] = min(self.capacite, e["jetons"] + dt * self.debit)
        if self.debit_o:
            e["octets"] = min(self.capacite_o, e["octets"] + dt * self.debit_o)
        e["t"] = now
        return e

    def _ecrire(self, e):
        tmp = self.etat.with_suffix(".tmp"); tmp.write_text(json.dumps(e)); os.replace(tmp, self.etat)

    def prendre(self, octets=0, attente_max=0.0):
        """Retourne True si un jeton (et `octets`) est obtenu avant attente_max secondes, sinon False."""
        fin = time.monotonic() + attente_max
        while True:
            with open(self.verrou, "a+") as fv:
                fcntl.flock(fv, fcntl.LOCK_EX)
                now = time.time(); e = self._lire(now)
                attente = 0.0
                if e.get("bloque_jusqua", 0) > now:
                    attente = e["bloque_jusqua"] - now
                elif e["jetons"] < 1:
                    attente = (1 - e["jetons"]) / self.debit
                elif self.debit_o and e["octets"] < octets:
                    attente = (octets - e["octets"]) / self.debit_o
                else:
                    e["jetons"] -= 1
                    if self.debit_o:
                        e["octets"] -= octets
                    self._ecrire(e); return True
                self._ecrire(e)
            if time.monotonic() + attente > fin:
                return False
            time.sleep(min(attente, 1.0))

    def reculer(self, secondes=None):
        """Recul partagé après 429/5xx : Retry-After si fourni, sinon 30 → 60 → 120 → 240 s, puis 900 s."""
        with open(self.verrou, "a+") as fv:
            fcntl.flock(fv, fcntl.LOCK_EX)
            now = time.time(); e = self._lire(now)
            e["echecs"] = e.get("echecs", 0) + 1
            pas = [30, 60, 120, 240]
            d = secondes if secondes is not None else (pas[e["echecs"] - 1] if e["echecs"] <= 4 else 900)
            e["bloque_jusqua"] = now + d; self._ecrire(e); return d

    def succes(self):
        with open(self.verrou, "a+") as fv:
            fcntl.flock(fv, fcntl.LOCK_EX)
            e = self._lire(time.time()); e["echecs"] = 0; self._ecrire(e)

    def bloque(self):
        try:
            return json.loads(self.etat.read_text()).get("bloque_jusqua", 0) > time.time()
        except Exception:
            return False
