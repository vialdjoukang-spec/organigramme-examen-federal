#!/usr/bin/env python3
"""Garde local de clôture : 0 = preuves réunies, 1 = reste à faire, 2 = erreur.

Ce contrôle ne peut pas retenir une session ChatGPT ouverte. Il ne lance aucune
boucle, n'ignore aucun arrêt demandé et ne réutilise jamais un ancien verdict.
Les commandes d'une mission locale doivent être des contrôles de confiance.
"""
import argparse
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import tempfile
from datetime import datetime, timezone


class Erreur(ValueError):
    pass


def lire_json(path):
    def interdit(value):
        raise Erreur(f"Nombre JSON interdit : {value}")

    def decimal(value):
        number = float(value)
        if not math.isfinite(number):
            interdit(value)
        return number

    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise Erreur(f"Clé JSON dupliquée : {key}")
            result[key] = value
        return result
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique,
                      parse_constant=interdit, parse_float=decimal)


def chemin(racine, value):
    if not isinstance(value, str) or not value.strip() or Path(value).is_absolute():
        raise Erreur("Un chemin relatif au dépôt est requis.")
    path = (racine / value).resolve()
    if not path.is_relative_to(racine):
        raise Erreur("Chemin hors du dépôt, y compris par lien symbolique.")
    return path


def empreinte(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def schema(obj, requis, facultatifs=()):
    if not isinstance(obj, dict) or not set(requis) <= obj.keys() or obj.keys() - set(requis) - set(facultatifs):
        raise Erreur(f"Champs requis : {', '.join(requis)} ; champs inconnus interdits.")


def texte(value):
    if not isinstance(value, str) or not value.strip():
        raise Erreur("Un texte non vide est requis.")


def valider(mission, racine):
    schema(mission, ("version", "objectif", "taches"), ("numero",))
    if type(mission["version"]) is not int or mission["version"] != 1:
        raise Erreur("Version de mission inconnue.")
    texte(mission["objectif"])
    if type(mission.get("numero", 1)) is not int or mission.get("numero", 1) < 0:
        raise Erreur("Le numéro de mission doit être un entier positif ou nul.")
    if not isinstance(mission["taches"], list) or not mission["taches"]:
        raise Erreur("Une mission vide ne peut pas être terminée.")
    ids = set()
    for task in mission["taches"]:
        schema(task, ("id", "titre", "controles"))
        texte(task["id"])
        texte(task["titre"])
        if task["id"] in ids:
            raise Erreur("Identifiants de tâche dupliqués.")
        ids.add(task["id"])
        if not isinstance(task["controles"], list) or not task["controles"]:
            raise Erreur("Toute tâche doit avoir au moins un contrôle.")
        for check in task["controles"]:
            if not isinstance(check, dict):
                raise Erreur("Contrôle invalide.")
            kind = check.get("type")
            if kind == "a_faire":
                schema(check, ("type", "motif"))
                texte(check["motif"])
            elif kind == "commande":
                schema(check, ("type", "argv"), ("delai",))
                if not isinstance(check["argv"], list) or not check["argv"]:
                    raise Erreur("La commande exige un tableau argv non vide.")
                for arg in check["argv"]:
                    texte(arg)
                delay = check.get("delai", 30)
                if type(delay) is not int or not 1 <= delay <= 60:
                    raise Erreur("Délai de contrôle : entier entre 1 et 60 secondes.")
            elif kind == "jauge":
                schema(check, ("type", "nom"))
                if check["nom"] not in ("prevalences", "monographies", "chronologie_structures", "chronologie_relectures"):
                    raise Erreur("Jauge inconnue.")
            elif kind == "json":
                schema(check, ("type", "fichier", "cles", "attendu"))
                chemin(racine, check["fichier"])
                if not isinstance(check["cles"], list) or not check["cles"] or any(not isinstance(k, str) or not k for k in check["cles"]):
                    raise Erreur("Une liste non vide de clés JSON est requise.")
                if check["attendu"] is not None and type(check["attendu"]) not in (str, bool, int, float):
                    raise Erreur("La valeur JSON attendue doit être un scalaire.")
                if type(check["attendu"]) is float and not math.isfinite(check["attendu"]):
                    raise Erreur("Une valeur numérique finie est requise.")
            elif kind == "sha256":
                schema(check, ("type", "fichier", "empreinte"))
                chemin(racine, check["fichier"])
                if not isinstance(check["empreinte"], str) or not re.fullmatch(r"[a-f0-9]{64}", check["empreinte"]):
                    raise Erreur("Empreinte SHA-256 invalide.")
            else:
                raise Erreur(f"Type de contrôle inconnu : {kind}")


def executer(argv, racine, delai):
    env = os.environ.copy()
    env["OEF_REPO"] = str(racine)
    with tempfile.TemporaryFile() as out:
        process = subprocess.Popen(argv, cwd=racine, env=env, shell=False,
                                   stdout=out, stderr=subprocess.STDOUT, start_new_session=True)
        try:
            code = process.wait(timeout=delai)
        except (subprocess.TimeoutExpired, KeyboardInterrupt):
            # Finir aussi les descendants du contrôle, sans réessai automatique.
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            process.wait()
            raise
        out.seek(0, os.SEEK_END)
        size = out.tell()
        out.seek(max(0, size - 4096))
        return code, out.read().decode("utf-8", errors="replace"), size > 4096


def evaluer(check, racine):
    kind = check["type"]
    if kind == "a_faire":
        return False, check["motif"]
    if kind == "commande":
        code, output, truncated = executer(check["argv"], racine, check.get("delai", 30))
        return code == 0, f"Code {code}. " + ("[sortie tronquée] " if truncated else "") + output.strip()
    if kind == "jauge":
        code, output, truncated = executer([sys.executable, "tools/jauge/binomes.py", "--json"], racine, 60)
        if code != 0 or truncated:
            raise Erreur("Lecture de la jauge impossible ou sortie tronquée.")
        data = json.loads(output)[check["nom"]]
        done, total = data["ok"], data["total"]
        if type(done) is not int or type(total) is not int or not 0 <= done <= total or total <= 0:
            raise Erreur("Effectifs de jauge invalides.")
        # Un affichage arrondi à 100 % ne suffit jamais.
        return done == total, f"{done}/{total} dans origin/main (référence locale ; faire git fetch origin avant une clôture)."
    path = chemin(racine, check["fichier"])
    if not path.is_file():
        return False, f"Preuve absente : {check['fichier']}"
    if kind == "sha256":
        ok = empreinte(path) == check["empreinte"]
        return ok, f"Empreinte {'conforme' if ok else 'différente'} : {check['fichier']}"
    data = lire_json(path)
    for key in check["cles"]:
        if not isinstance(data, dict) or key not in data:
            return False, f"Clé absente dans {check['fichier']} : {key}"
        data = data[key]
    ok = type(data) is type(check["attendu"]) and data == check["attendu"]
    return ok, f"Valeur JSON {'conforme' if ok else 'différente'} : {check['fichier']} / {'/'.join(check['cles'])}"


def verifier(mission, racine):
    valider(mission, racine)  # Valider tout le plan avant de lancer un contrôle.
    tasks = []
    for task in mission["taches"]:
        results = []
        for check in task["controles"]:
            try:
                ok, detail = evaluer(check, racine)
                status = "valide" if ok else "reste_a_faire"
            except subprocess.TimeoutExpired:
                status, detail = "reste_a_faire", "Délai dépassé ; contrôle arrêté, aucune preuve de réussite."
            except (OSError, ValueError, KeyError, TypeError) as exc:
                status, detail = "erreur", str(exc)
            results.append({"type": check["type"], "statut": status, "detail": detail})
        tasks.append({"id": task["id"], "titre": task["titre"],
                      "validee": all(r["statut"] == "valide" for r in results), "controles": results})
    done = sum(t["validee"] for t in tasks)
    code = 2 if any(r["statut"] == "erreur" for t in tasks for r in t["controles"]) else (0 if done == len(tasks) else 1)
    return code, {"date_utc": datetime.now(timezone.utc).isoformat(), "objectif": mission["objectif"],
                  "numero": mission.get("numero", 1), "etat": "[FIN]" if code == 0 else "[EN COURS]",
                  "cloture_autorisee": code == 0, "validees": done, "total": len(tasks),
                  "prochaine": next((t["id"] for t in tasks if not t["validee"]), None), "taches": tasks}


def enregistrer(path, rapport):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=".fin-")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(rapport, stream, ensure_ascii=False, indent=2, allow_nan=False)
            stream.write("\n")
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("initialiser", "verifier"), nargs="?", default="verifier")
    parser.add_argument("--racine", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--mission", default=".etat_local/mission.json")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    racine = args.racine.resolve()
    lock = None
    destination = None
    number = 1
    try:
        path = chemin(racine, args.mission)
        modele = racine / "tools/garde/mission-projet.json"
        if args.action == "initialiser":
            mission = lire_json(modele)
            valider(mission, racine)
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("x", encoding="utf-8") as stream:
                json.dump(mission, stream, ensure_ascii=False, indent=2)
                stream.write("\n")
            print(f"TÂCHE #{mission.get('numero', 1)} — ÉTAT : [DÉBUT]")
            print(f"Mission créée : {path} (aucune mission existante écrasée).")
            return 0
        # Un état local absent ne désactive pas le garde du projet.
        source = modele if args.mission == ".etat_local/mission.json" and not path.exists() else path
        destination = chemin(racine, ".etat_local/fin-mission.json")
        verrou = chemin(racine, ".etat_local/fin-mission.lock")
        if source in (destination, verrou):
            destination = None
            raise Erreur("La mission ne peut pas remplacer le rapport ou le verrou.")
        verrou.parent.mkdir(parents=True, exist_ok=True)
        lock = verrou.open("a+")
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            destination = None  # Ne pas écraser le rapport d'un contrôle concurrent.
            raise Erreur("Un contrôle est déjà en cours ; aucune clôture nouvelle validée.")
        source_hash = empreinte(source)
        mission = lire_json(source)
        valider(mission, racine)
        number = mission.get("numero", 1)
        protected = {source} | {chemin(racine, c["fichier"]) for t in mission["taches"] for c in t["controles"] if "fichier" in c}
        if destination in protected or verrou in protected:
            destination = None
            raise Erreur("Le rapport ne doit pas écraser une preuve ou la mission.")
        # Invalider l'ancien succès AVANT les contrôles, même en cas d'arrêt brutal.
        enregistrer(destination, {"date_utc": datetime.now(timezone.utc).isoformat(),
                                 "cloture_autorisee": False, "statut": "controle_en_cours"})
        code, report = verifier(mission, racine)
        report["mission_sha256"] = source_hash
        report["source"] = str(source.relative_to(racine))
        # Refuser aussi un plan modifié pendant la vérification.
        if empreinte(source) != source_hash:
            raise Erreur("Mission modifiée pendant les contrôles ; relancer le garde.")
        enregistrer(destination, report)
        if args.json:
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            number = report["numero"]
            print(f"TÂCHE #{number} — ÉTAT : [EN COURS]")
            print(f"Objectif : {report['objectif']}")
            print(f"Auto-audit : {report['validees']}/{report['total']} obligations validées.")
            for task in report["taches"]:
                print(f"- {task['id']} : {task['titre']} → {'OUI' if task['validee'] else 'NON'}")
                for result in task["controles"]:
                    if result["statut"] != "valide":
                        print(f"  {result['statut']} : {result['detail']}")
            if code:
                print(f"⛔ BLOCAGE — TÂCHE #{number} NON TERMINÉE")
                print("Manquant(s) : " + ", ".join(t["id"] for t in report["taches"] if not t["validee"]))
                print(f"Reprise immédiate : {report['prochaine']}")
            else:
                print("╔══════════════════════════════════════╗")
                print(f"║ TÂCHE #{number} — ÉTAT : [FIN]")
                print("║ Audit : tous critères ✅")
                print("╚══════════════════════════════════════╝")
            print("Rapport : .etat_local/fin-mission.json")
        return code
    except (OSError, ValueError, TypeError) as exc:
        if destination is not None:
            try:
                enregistrer(destination, {"date_utc": datetime.now(timezone.utc).isoformat(),
                                         "cloture_autorisee": False, "statut": "erreur", "detail": str(exc)})
            except OSError:
                pass  # L'erreur d'écriture ne peut jamais produire un code 0.
        print(f"⛔ BLOCAGE — TÂCHE #{number} NON TERMINÉE\nManquant(s) : contrôle valide — {exc}\nReprise immédiate : corriger le contrôle.", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("Contrôle interrompu ; aucune clôture validée.", file=sys.stderr)
        return 130
    finally:
        if lock is not None:
            lock.close()


if __name__ == "__main__":
    sys.exit(main())
