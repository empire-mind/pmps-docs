import sys
import tempfile
import unittest
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from pmps_control.ledger import Ledger
from pmps_control.runtime import intake, approve_record, cite_record, supersede_record, restore_record

class GoldenPathLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.source = self.root / "PMPS_SOP_001.md"
        self.source.write_text("# Controlled SOP Document\nStandard Operating Procedure v1.0", encoding="utf-8")
        self.config = yaml.safe_load((ROOT / "config/runtime.yaml").read_text())
        self.metadata = {
            "record_id": "PMPS-SOP-001-V1",
            "client_id": "_NA",
            "project_id": "PMPS-CORE",
            "record_class": "controlled_document",
            "authority_system": "google_drive",
            "sensitivity": "CONFIDENTIAL",
            "retention_rule": "life_plus_7_years",
            "owner": "Ashley Halvorson",
        }
        self.ledger = Ledger(self.root / "golden_ledger.sqlite3")

    def tearDown(self):
        self.ledger.close()
        self.tmp.cleanup()

    def test_full_document_golden_path_lifecycle(self):
        # 1. Source -> Quarantine & Intake Validation
        intake_res = intake(self.source, self.metadata, 0.98, self.config, self.ledger)
        self.assertEqual(intake_res["outcome"], "APPROVAL_REQUIRED")
        self.assertEqual(intake_res["record_id"], "PMPS-SOP-001-V1")

        # 2. Human Approval -> Canonical Vault Filing
        approve_res = approve_record("PMPS-SOP-001-V1", "Ashley Halvorson", self.config, self.ledger)
        self.assertEqual(approve_res["status"], "APPROVED")
        self.assertIn("PMPS-SOP-001-V1.md", approve_res["canonical_vault_path"])

        # 3. Agent Retrieval & Citation Receipt
        cite_res = cite_record("PMPS-SOP-001-V1", "hermes-agent-nova", self.ledger)
        self.assertEqual(cite_res["sha256"], intake_res["sha256"])
        self.assertTrue(len(cite_res["citation_hash"]) == 64)

        # 4. Supersession / Revocation by V2
        super_res = supersede_record("PMPS-SOP-001-V1", "PMPS-SOP-001-V2", "Scheduled annual policy update", self.ledger)
        self.assertEqual(super_res["status"], "SUPERSEDED")
        self.assertEqual(super_res["superseded_by"], "PMPS-SOP-001-V2")

        # 5. Checkpoint Verification & Verified Restore
        restore_res = restore_record("PMPS-SOP-001-V1", self.ledger)
        self.assertEqual(restore_res["status"], "RESTORED")
        self.assertEqual(restore_res["verified_sha256"], intake_res["sha256"])

        # 6. Replay Audit Chain
        all_events = self.ledger.replay("PMPS-SOP-001-V1")
        event_types = [e["event_type"] for e in all_events]
        expected_types = [
            "record.received",
            "route.proposed",
            "route.approved",
            "filed.canonical",
            "retrieved.cited",
            "record.superseded",
            "record.restored",
        ]
        self.assertEqual(event_types, expected_types)

if __name__ == "__main__":
    unittest.main()
