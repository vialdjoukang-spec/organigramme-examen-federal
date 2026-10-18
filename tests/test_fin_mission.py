"""La clôture doit échouer sans preuves fraîches, même après un ancien succès."""
import contextlib
import fcntl
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "tools/garde/fin.py"
spec = importlib.util.spec_from_file_location("fin_mission", SCRIPT)
fin = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fin)


class FinMission(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()

    def mission(self, *checks):
        return {"version": 1, "objectif": "Fin vérifiée", "taches": [
            {"id": "livrer", "titre": "Livrer le résultat", "controles": list(checks)}]}

    def save(self, name, data):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def command(self, code, **kwargs):
        return {"type": "commande", "argv": [sys.executable, "-c", code], **kwargs}

    def cli(self, *args):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return fin.main(["--racine", str(self.root), *args])

    def test_missing_proof_and_open_task_remain_open(self):
        code, report = fin.verifier(self.mission(
            {"type": "a_faire", "motif": "Audit à faire"},
            {"type": "sha256", "fichier": "absent", "empreinte": "a" * 64}), self.root)
        self.assertEqual(code, 1)
        self.assertFalse(report["cloture_autorisee"])
        self.assertEqual(len(report["taches"][0]["controles"]), 2)
        self.assertEqual(report["prochaine"], "livrer")

    def test_empty_or_unknown_or_fake_completion_rejected(self):
        cases = [self.mission(), {"version": 1, "objectif": "x", "taches": []},
                 self.mission({"type": "terminee", "valeur": True})]
        fake = self.mission({"type": "a_faire", "motif": "À faire"})
        fake["taches"][0]["terminee"] = True
        cases.append(fake)
        for mission in cases:
            with self.subTest(mission=mission), self.assertRaises(fin.Erreur):
                fin.verifier(mission, self.root)

    def test_all_schema_checked_before_executing_anything(self):
        marker = self.root / "ne-pas-creer"
        mission = self.mission(self.command(f"from pathlib import Path; Path({str(marker)!r}).touch()"), {"type": "inconnu"})
        with self.assertRaises(fin.Erreur):
            fin.verifier(mission, self.root)
        self.assertFalse(marker.exists())

    def test_duplicate_tasks_rejected(self):
        mission = self.mission({"type": "a_faire", "motif": "Audit"})
        mission["taches"] *= 2
        with self.assertRaises(fin.Erreur):
            fin.verifier(mission, self.root)

    def test_json_missing_and_strict_types(self):
        check = {"type": "json", "fichier": "preuve.json", "cles": ["audit", "valide"], "attendu": True}
        for data, expected in [({}, 1), ({"audit": {"valide": 1}}, 1), ({"audit": {"valide": True}}, 0)]:
            self.save("preuve.json", data)
            code, _ = fin.verifier(self.mission(check), self.root)
            self.assertEqual(code, expected)

    def test_invalid_json_duplicate_keys_and_nan_fail(self):
        check = {"type": "json", "fichier": "preuve.json", "cles": ["ok"], "attendu": True}
        for raw in ['{', '{"ok":true,"ok":false}', '{"ok":NaN}', '{"ok":1e999}']:
            (self.root / "preuve.json").write_text(raw)
            code, report = fin.verifier(self.mission(check), self.root)
            self.assertEqual(code, 2)
            self.assertFalse(report["cloture_autorisee"])

    def test_changed_file_invalidates_old_success(self):
        proof = self.root / "preuve.txt"
        proof.write_text("relu")
        check = {"type": "sha256", "fichier": "preuve.txt", "empreinte": hashlib.sha256(proof.read_bytes()).hexdigest()}
        self.save(".etat_local/mission.json", self.mission(check))
        self.assertEqual(self.cli(), 0)
        proof.write_text("modifié après relecture")
        self.assertEqual(self.cli(), 1)
        self.assertFalse(fin.lire_json(self.root / ".etat_local/fin-mission.json")["cloture_autorisee"])

    def test_paths_outside_repo_including_symlink_rejected(self):
        for name in ["../preuve", "/tmp/preuve"]:
            with self.assertRaises(fin.Erreur):
                fin.verifier(self.mission({"type": "sha256", "fichier": name, "empreinte": "a" * 64}), self.root)
        (self.root / "dehors").symlink_to(self.root.parent, target_is_directory=True)
        with self.assertRaises(fin.Erreur):
            fin.chemin(self.root, "dehors/preuve")

    def test_command_failure_does_not_skip_next_check(self):
        code, report = fin.verifier(self.mission(self.command("raise SystemExit(7)"), self.command("print('OK')")), self.root)
        self.assertEqual(code, 1)
        self.assertEqual([r["statut"] for r in report["taches"][0]["controles"]], ["reste_a_faire", "valide"])

    def test_command_timeout_and_invalid_timeout(self):
        code, report = fin.verifier(self.mission(self.command("import time; time.sleep(10)", delai=1)), self.root)
        self.assertEqual(code, 1)
        self.assertIn("Délai dépassé", report["taches"][0]["controles"][0]["detail"])
        for delay in [0, 61, True]:
            with self.assertRaises(fin.Erreur):
                fin.verifier(self.mission(self.command("pass", delai=delay)), self.root)

    def test_no_shell_interpretation(self):
        check = {"type": "commande", "argv": [sys.executable, "-c", "import sys; print(sys.argv[1])", "$(touch intrusion)"]}
        self.assertEqual(fin.verifier(self.mission(check), self.root)[0], 0)
        self.assertFalse((self.root / "intrusion").exists())

    def test_gauge_requires_exact_counts_not_rounded_100_percent(self):
        mission = self.mission({"type": "jauge", "nom": "prevalences"})
        for data, expected in [({"ok": 999, "total": 1000, "pct": 100}, 1),
                               ({"ok": 1000, "total": 1000, "pct": 100}, 0),
                               ({"ok": 0, "total": 0, "pct": 100}, 2),
                               ({"ok": True, "total": 1, "pct": 100}, 2)]:
            with patch.object(fin, "executer", return_value=(0, json.dumps({"prevalences": data}), False)):
                self.assertEqual(fin.verifier(mission, self.root)[0], expected)

    def test_chronology_gauges_are_supported_and_require_exact_counts(self):
        for name in ("chronologie_structures", "chronologie_relectures"):
            mission = self.mission({"type": "jauge", "nom": name})
            payload = {name: {"ok": 8, "total": 9, "pct": 100}}
            with patch.object(fin, "executer", return_value=(0, json.dumps(payload), False)):
                self.assertEqual(fin.verifier(mission, self.root)[0], 1)
            payload[name]["ok"] = 9
            with patch.object(fin, "executer", return_value=(0, json.dumps(payload), False)):
                self.assertEqual(fin.verifier(mission, self.root)[0], 0)

    def test_missing_state_uses_project_plan_not_success(self):
        self.save("tools/garde/mission-projet.json", self.mission({"type": "a_faire", "motif": "Audit"}))
        self.assertEqual(self.cli(), 1)
        self.assertEqual(self.cli("--mission", "absent.json"), 2)

    def test_initialisation_never_overwrites_mission(self):
        self.save("tools/garde/mission-projet.json", self.mission({"type": "a_faire", "motif": "Audit"}))
        self.assertEqual(self.cli("initialiser"), 0)
        path = self.root / ".etat_local/mission.json"
        original = path.read_bytes()
        self.assertEqual(self.cli("initialiser"), 2)
        self.assertEqual(path.read_bytes(), original)

    def test_error_clears_prior_success_report(self):
        self.save(".etat_local/fin-mission.json", {"cloture_autorisee": True})
        self.save(".etat_local/mission.json", {"mauvais": True})
        self.assertEqual(self.cli(), 2)
        self.assertFalse(fin.lire_json(self.root / ".etat_local/fin-mission.json")["cloture_autorisee"])

    def test_interruption_invalidates_previous_success(self):
        self.save(".etat_local/mission.json", self.mission(self.command("pass")))
        self.save(".etat_local/fin-mission.json", {"cloture_autorisee": True})
        with patch.object(fin, "verifier", side_effect=KeyboardInterrupt):
            self.assertEqual(self.cli(), 130)
        self.assertFalse(fin.lire_json(self.root / ".etat_local/fin-mission.json")["cloture_autorisee"])

    def test_changed_plan_during_checks_is_rejected(self):
        path = self.save(".etat_local/mission.json", self.mission(self.command("pass")))
        original = fin.verifier
        def mutate(mission, root):
            result = original(mission, root)
            path.write_text(path.read_text() + "\n")
            return result
        with patch.object(fin, "verifier", side_effect=mutate):
            self.assertEqual(self.cli(), 2)

    def test_concurrent_check_cannot_overwrite_report(self):
        self.save(".etat_local/mission.json", self.mission(self.command("pass")))
        report = self.save(".etat_local/fin-mission.json", {"cloture_autorisee": False, "statut": "controle_en_cours"})
        with (self.root / ".etat_local/fin-mission.lock").open("a+") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            original = report.read_bytes()
            self.assertEqual(self.cli(), 2)
            self.assertEqual(report.read_bytes(), original)

    def test_report_never_overwrites_evidence(self):
        self.save(".etat_local/mission.json", self.mission({"type": "json", "fichier": ".etat_local/fin-mission.json", "cles": ["ok"], "attendu": True}))
        report = self.save(".etat_local/fin-mission.json", {"ok": True})
        original = report.read_bytes()
        self.assertEqual(self.cli(), 2)
        self.assertEqual(report.read_bytes(), original)

    def test_protocol_fin_requires_successful_audit(self):
        self.save(".etat_local/mission.json", self.mission({"type": "a_faire", "motif": "Audit"}))
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(fin.main(["--racine", str(self.root)]), 1)
        self.assertIn("[EN COURS]", output.getvalue())
        self.assertIn("NON TERMINÉE", output.getvalue())
        self.assertNotIn("[FIN]", output.getvalue())
        self.save(".etat_local/mission.json", self.mission(self.command("pass")))
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(fin.main(["--racine", str(self.root)]), 0)
        self.assertIn("[FIN]", output.getvalue())
        self.assertIn("tous critères", output.getvalue())
        self.assertIn("→ OUI", output.getvalue())


if __name__ == "__main__":
    unittest.main()
