"""Fixtures synthétiques en mémoire ; aucun cours ni audit réel n'est généré."""
from copy import deepcopy
from datetime import datetime, timedelta, timezone
import json
import unittest

from harnais.pilotage_lots.engine import (
    advance, attestation, digest, evaluate_lot, layout, technical, validate_state,
)
from harnais.pilotage_lots.cli import collect


NOW = datetime(2026, 10, 25, 20, tzinfo=timezone.utc)
ROOT = "lot en cours de production/LOT_226/"


def encoded(value):
    return (json.dumps(value, ensure_ascii=False) + "\n").encode()


class Memory:
    def __init__(self):
        self.files, self.reads = {}, []

    def head(self, branch):
        return "a" * 40

    def file(self, path, head):
        if head != "a" * 40:
            raise AssertionError("Lecture hors instantané fixe")
        self.reads.append(path)
        if path not in self.files:
            raise FileNotFoundError(path)
        return self.files[path]


def html(entities, names, a=False, small=False):
    parts = ["<!DOCTYPE html>\n<html><head><meta charset='utf-8'></head><body>"]
    if a:
        parts.extend(f'<strong data-dx="DX.{i}" data-name="{name}">DX.{i} — {name}</strong>\n' for i, name in enumerate(names, 1))
    for entity in entities:
        prefix, code = entity["id"], entity["code"]
        summary = "SSP de test" if code == "SSP" else code + " — " + names[int(code[3:]) - 1]
        parts.append(f'<details open id="{prefix}"><summary>{summary}</summary>')
        for point in range(1, 15):
            parts.append(f'<section id="{prefix}-p{point}"><h3>{point}. Le point est synthetique.</h3><p>')
            for i in range(1 if small else 112):
                parts.append(f"Le controle synthetique {prefix} de la section {point:02d}, ligne {i:04d}, teste un fichier sans contenu medical.")
            parts.append("</p></section>")
        parts.append("</details>")
    parts.append("</body></html>\n<!-- FIN_FICHIER LOT_226_TEST -->\n")
    return "\n".join(parts).encode()


class Fixture:
    def __init__(self, ranges=((1, 2), (3, 5), (6, 7), (8, 10))):
        self.reader = Memory()
        self.names = [f"Scenario synthetique {i}" for i in range(1, 11)]
        self.job = {"lot": "LOT_226", "worker": "auteur", "writers": ["auteur"], "branch": "prod/lot-226-test",
                    "decision_path": ROOT + "DECISION_SEANCE.md", "session_path": ROOT + "DECISION_SEANCE.json",
                    "runtime_path": ROOT + "PREUVE_RUNTIME.json"}
        self.session = {"schema_version": 1, "prompt": "V0", "lot": "LOT_226", "worker": "auteur", "writers": ["auteur"],
                        "branch": self.job["branch"], "authority": {"mode": "delegated", "decided_by": "fixture", "instruction": "Mandat synthetique de test"},
                        "phase_a": {"name": "LOT_226_Phase_A_V0_SSP_et_10DD.html", "entities": [{"code": "SSP", "id": "ssp"}]}, "phase_b": []}
        for k, (a, b) in enumerate(ranges, 1):
            self.session["phase_b"].append({"name": f"LOT_226_Phase_B_V0_Partie_{k}_DX.{a}_a_DX.{b}.html", "start": a, "end": b,
                                             "entities": [{"code": f"DX.{i}", "id": f"dx{i}"} for i in range(a, b + 1)]})
        self.reader.files[self.job["decision_path"]] = b"Decision exclusivement synthetique.\n"
        self.sync_session()
        proof = {"agent": "auteur", "complete": True, "tested_at": (NOW - timedelta(minutes=5)).isoformat(),
                 "medical_source_compressed": False, "tests": {x: {"ok": True} for x in ("chonkie", "gptcache", "llmlingua")}}
        self.set_runtime(proof)
        self.package = {"schema_version": 1, "files": {}}
        for key, spec in layout(self.session):
            raw = html(spec["entities"], self.names, a=key == "A")
            self.reader.files[ROOT + spec["name"]] = raw
            entry = {"production_started_at": (NOW - timedelta(minutes=28)).isoformat()}
            for role in ("medical", "linguistique", "visual", "delivery"):
                report = ROOT + f"audits/{key}-{role}.json"
                self.reader.files[report] = encoded({"fixture": True, "file": key, "role": role})
                entry[role] = {"file_sha256": digest(raw), "role": role, "auditor_id": "auditeur-independant", "score": 97,
                               "critical_count": 0, "full_read": True, "final_question": "oui", "critical_sources_read": True,
                               "v0_line_by_line_complete": True, "condensation_preserves_clinical_data": True,
                               "entities": {e["code"]: {"score": 97, "critical_count": 0, "final_question": "oui"} for e in spec["entities"]},
                               "checked_at": (NOW - timedelta(minutes=30 if key == "A" else 20)).isoformat(),
                               "report_path": report, "report_sha256": digest(self.reader.files[report]),
                               "performed": True, "authorized_environment": True, "width_px": 390,
                               "verified": True, "destination": "Drive Finaux", "remote_file_id": "fixture", "mime_type": "text/html",
                               "remote_sha256": digest(raw), "remote_bytes": len(raw)}
                if role == "delivery":
                    entry[role]["checked_at"] = (NOW - timedelta(minutes=10)).isoformat()
            self.package["files"][key] = entry
        a_sha = digest(self.reader.files[ROOT + self.session["phase_a"]["name"]])
        corrections = b"Corrections exclusivement synthetiques.\n"
        self.reader.files[ROOT + "CORRECTIONS_AUDIT.md"] = corrections
        self.canonical = {"phase_a_sha256": a_sha, "frozen_at": (NOW - timedelta(minutes=29)).isoformat(),
                          "corrections_sha256": digest(corrections),
                          "diagnoses": [{"code": f"DX.{i}", "name": name} for i, name in enumerate(self.names, 1)]}
        self.sync_canonical()
        self.sync_package()

    def sync_session(self):
        self.session["decision_sha256"] = digest(self.reader.files[self.job["decision_path"]])
        raw = encoded(self.session)
        self.reader.files[self.job["session_path"]] = raw
        self.job.update(decision_sha256=self.session["decision_sha256"], session_sha256=digest(raw))

    def sync_canonical(self):
        self.reader.files[ROOT + "LISTE_DX_CANONIQUE.md"] = b"# Fixture\n```json\n" + encoded(self.canonical).rstrip() + b"\n```\n"

    def sync_package(self):
        self.reader.files[ROOT + "VALIDATION_V0.json"] = encoded(self.package)

    def set_runtime(self, proof):
        raw = encoded(proof)
        self.reader.files[self.job["runtime_path"]] = raw
        self.job["runtime_sha256"] = digest(raw)

    def run(self):
        self.sync_package()
        return evaluate_lot(self.reader, self.job, NOW)

    def state(self):
        return {"schema_version": 2, "prompt": "V0", "status": "paused", "stop_requested": True,
                "deployment_enabled": False, "automatic_assignment": False, "jobs": [self.job]}


class Gates(unittest.TestCase):
    def test_complete_fixture_has_all_files_without_clinical_certification(self):
        result = Fixture().run()
        self.assertTrue(result["validated"])
        self.assertTrue(result["delivered"])
        self.assertFalse(result["clinical_validation"])

    def test_five_parts_and_ten_singletons_are_supported(self):
        for ranges in ([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)], [(i, i) for i in range(1, 11)]):
            with self.subTest(ranges=ranges):
                self.assertTrue(Fixture(ranges).run()["validated"])

    def test_large_multi_entity_file_is_allowed(self):
        f = Fixture()
        result = f.run()
        self.assertGreater(result["files"]["B1"]["bytes"], 200_000)
        self.assertTrue(result["delivered"])

    def test_each_entity_must_reach_minimum(self):
        f = Fixture()
        spec = f.session["phase_b"][0]
        errors, sizes, _ = technical(html(spec["entities"], f.names, small=True), spec)
        self.assertTrue(all(x < 150_000 for x in sizes.values()))
        self.assertTrue(errors)

    def test_dense_draft_over_200ko_calls_for_lossless_condensation(self):
        f = Fixture()
        path = ROOT + f.session["phase_a"]["name"]
        f.reader.files[path] = f.reader.files[path].replace(b"teste un fichier", b"teste un fichier exhaustif dont tous les faits doivent etre preserves lors de la reformulation")
        self.assertEqual(f.run()["next_action"]["action"], "condense_preserving_data")

    def test_unchecked_condensation_blocks_high_scoring_audit(self):
        f = Fixture()
        f.package["files"]["A"]["medical"]["condensation_preserves_clinical_data"] = False
        self.assertFalse(f.run()["validated"])

    def test_comment_padding_cannot_make_entity_large_enough(self):
        f = Fixture()
        spec = f.session["phase_a"]
        raw = html(spec["entities"], f.names, a=True, small=True).replace(b"</details>", (b"<!--" + b"x" * 1000 + b"-->\n") * 180 + b"</details>")
        errors, sizes, _ = technical(raw, spec)
        self.assertGreater(len(raw), 150_000)
        self.assertLess(sizes["SSP"], 150_000)
        self.assertTrue(any("contenu propre" in x for x in errors))

    def test_gaps_and_overlaps_are_rejected(self):
        for ranges in ([(1, 3), (3, 10)], [(1, 3), (5, 10)]):
            with self.assertRaises(ValueError):
                Fixture(ranges)

    def test_missing_decision_prevents_any_html_read(self):
        f = Fixture()
        del f.reader.files[f.job["decision_path"]]
        self.assertEqual(f.run()["next_action"]["action"], "repair_session_decision")
        self.assertFalse(any(p.endswith(".html") for p in f.reader.reads))

    def test_modified_decision_is_not_silently_accepted(self):
        f = Fixture()
        f.reader.files[f.job["decision_path"]] += b"Autre attribution."
        self.assertEqual(f.run()["next_action"]["action"], "repair_session_decision")

    def test_job_cannot_change_its_assigned_branch(self):
        f = Fixture()
        f.job["branch"] = "prod/lot-225-other"
        self.assertEqual(f.run()["next_action"]["action"], "repair_session_decision")

    def test_no_automatic_next_lot(self):
        with self.assertRaisesRegex(ValueError, "Aucune attribution automatique"):
            advance()

    def test_v8_state_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_state({"schema_version": 1, "campaign": "inverse-226-001-v8"})

    def test_one_worker_cannot_have_two_lots(self):
        f = Fixture()
        state = f.state()
        other = deepcopy(f.job)
        other["lot"] = "LOT_225"
        state["jobs"].append(other)
        with self.assertRaises(ValueError):
            validate_state(state)

    def test_failed_harness_prevents_production(self):
        f = Fixture()
        f.set_runtime({"agent": "auteur", "complete": False, "error": "403"})
        self.assertEqual(f.run()["next_action"]["action"], "restore_individual_harness")
        self.assertFalse(any(p.endswith(".html") for p in f.reader.reads))

    def test_stale_runtime_is_rejected(self):
        f = Fixture()
        proof = json.loads(f.reader.files[f.job["runtime_path"]])
        proof["tested_at"] = (NOW - timedelta(hours=2)).isoformat()
        f.set_runtime(proof)
        self.assertEqual(f.run()["next_action"]["action"], "restore_individual_harness")

    def test_phase_a_failure_does_not_open_phase_b(self):
        f = Fixture()
        f.package["files"]["A"]["medical"]["score"] = 89
        self.assertEqual(f.run()["next_action"]["file"], "A")
        self.assertFalse(any("Phase_B" in p for p in f.reader.reads))

    def test_final_no_blocks_despite_99_percent(self):
        f = Fixture()
        record = f.package["files"]["A"]["medical"]
        record.update(score=99, final_question="non")
        result = f.run()
        self.assertFalse(result["validated"])
        self.assertIn("Question finale", result["next_action"]["reason"])

    def test_both_independent_roles_are_required(self):
        f = Fixture()
        del f.package["files"]["A"]["linguistique"]
        self.assertIn("linguistique", f.run()["next_action"]["reason"])

    def test_author_cannot_audit_their_own_file(self):
        f = Fixture()
        f.package["files"]["A"]["medical"]["auditor_id"] = "auteur"
        self.assertIn("indépendant", f.run()["next_action"]["reason"])

    def test_critical_error_blocks_despite_high_score(self):
        f = Fixture()
        f.package["files"]["A"]["medical"]["critical_count"] = 1
        self.assertFalse(f.run()["validated"])

    def test_one_low_monograph_cannot_hide_in_file_average(self):
        f = Fixture()
        f.package["files"]["B1"]["medical"]["entities"]["DX.2"]["score"] = 89
        self.assertIn("moyenne", f.run()["next_action"]["reason"])

    def test_changed_html_does_not_inherit_old_audit(self):
        f = Fixture()
        path = ROOT + f.session["phase_a"]["name"]
        f.reader.files[path] = f.reader.files[path].replace(b"Le controle", b"Le nouveau controle", 1)
        self.assertIn("autre version", f.run()["next_action"]["reason"])

    def test_changed_report_is_rejected(self):
        f = Fixture()
        record = f.package["files"]["A"]["medical"]
        f.reader.files[record["report_path"]] += b"different"
        self.assertIn("rapport", f.run()["next_action"]["reason"])

    def test_report_cannot_escape_lot(self):
        f = Fixture()
        f.package["files"]["A"]["medical"]["report_path"] = "lot en cours de production/LOT_225/audits/test.json"
        self.assertIn("hors du lot", f.run()["next_action"]["reason"])

    def test_missing_canonical_stops_before_phase_b(self):
        f = Fixture()
        del f.reader.files[ROOT + "LISTE_DX_CANONIQUE.md"]
        self.assertEqual(f.run()["next_action"]["action"], "freeze_or_reaudit_phase_a")
        self.assertFalse(any("Phase_B" in p for p in f.reader.reads))

    def test_changed_audit_corrections_require_realigning(self):
        f = Fixture()
        f.reader.files[ROOT + "CORRECTIONS_AUDIT.md"] += b"correction"
        self.assertEqual(f.run()["next_action"]["action"], "freeze_or_reaudit_phase_a")

    def test_canonical_must_match_displayed_phase_a(self):
        f = Fixture()
        f.canonical["diagnoses"][0]["name"] = "Autre scenario"
        f.sync_canonical()
        self.assertEqual(f.run()["next_action"]["action"], "freeze_or_reaudit_phase_a")

    def test_b_name_must_match_canonical_exactly(self):
        f = Fixture()
        path = ROOT + f.session["phase_b"][0]["name"]
        f.reader.files[path] = f.reader.files[path].replace(b"DX.1 \xe2\x80\x94 Scenario synthetique 1", b"DX.1 \xe2\x80\x94 Autre nom", 1)
        self.assertEqual(f.run()["next_action"]["action"], "realign_phase_b")

    def test_historical_b_cannot_claim_to_follow_new_a(self):
        f = Fixture()
        f.package["files"]["B1"]["production_started_at"] = (NOW - timedelta(hours=1)).isoformat()
        self.assertEqual(f.run()["next_action"]["action"], "realign_phase_b")

    def test_visual_refusal_is_not_a_success(self):
        f = Fixture()
        f.package["files"]["A"]["visual"]["authorized_environment"] = False
        self.assertEqual(f.run()["next_action"]["action"], "await_authorized_visual_proof")

    def test_delivery_before_complete_validation_is_rejected(self):
        f = Fixture()
        f.package["files"]["A"]["delivery"]["checked_at"] = (NOW - timedelta(hours=1)).isoformat()
        result = f.run()
        self.assertTrue(result["validated"])
        self.assertFalse(result["delivered"])

    def test_remote_byte_difference_is_rejected(self):
        f = Fixture()
        f.package["files"]["B1"]["delivery"]["remote_bytes"] -= 1
        self.assertFalse(f.run()["delivered"])

    def test_paused_registry_never_grants_execution(self):
        f = Fixture()
        result = collect(f.reader, f.state(), NOW)
        self.assertFalse(result["may_execute"])
        self.assertFalse(result["automatic_assignment"])

    def test_non_finite_score_and_boolean_score_are_rejected(self):
        f = Fixture()
        record = deepcopy(f.package["files"]["A"]["medical"])
        for bad in (float("nan"), float("inf"), True):
            record["score"] = bad
            with self.assertRaises(ValueError):
                attestation(f.reader, "a" * 40, f.job, record, record["file_sha256"], "medical", NOW)


if __name__ == "__main__":
    unittest.main()
