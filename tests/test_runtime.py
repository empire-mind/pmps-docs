import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from pmps_control.ledger import Ledger
from pmps_control.runtime import intake, record_approval


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.source = self.root / "sample.txt"
        self.source.write_text("controlled bytes", encoding="utf-8")
        self.config = yaml.safe_load((ROOT / "config/runtime.yaml").read_text())
        self.metadata = {
            "record_id": "PMPS-REC-TEST-1",
            "client_id": "_NA",
            "project_id": "_NA",
            "record_class": "operations",
            "authority_system": "google_drive",
            "sensitivity": "INTERNAL",
            "retention_rule": "life_plus_3_years",
            "owner": "Document Controller",
        }
        self.ledger = Ledger(self.root / "ledger.sqlite3")

    def tearDown(self):
        self.ledger.close()
        self.tmp.cleanup()

    def test_low_risk_intake_and_replay(self):
        result = intake(self.source, self.metadata, 0.99, self.config, self.ledger)
        self.assertEqual(result["outcome"], "ROUTE_PROPOSED")
        self.assertFalse(result["duplicate"])
        events = self.ledger.replay("PMPS-REC-TEST-1")
        self.assertEqual(
            [e["event_type"] for e in events],
            ["record.received", "route.proposed"],
        )
        self.assertEqual(events[0]["sha256"], events[1]["sha256"])
        self.assertEqual(events[0]["source_name"], "sample.txt")
        self.assertNotIn("source_path", events[0])
        chain = self.ledger.verify_chain()
        self.assertTrue(chain["ok"])
        self.assertEqual(chain["checked"], 2)

    def test_controlled_document_requires_approval(self):
        self.metadata["record_class"] = "controlled_document"
        result = intake(self.source, self.metadata, 0.99, self.config, self.ledger)
        self.assertEqual(result["outcome"], "APPROVAL_REQUIRED")

    def test_low_confidence_holds_in_intake(self):
        result = intake(self.source, self.metadata, 0.20, self.config, self.ledger)
        self.assertEqual(result["outcome"], "EXCEPTION")
        self.assertEqual(result["route_key"], "intake")

    def test_disabled_restricted_route_is_exception(self):
        self.metadata["record_class"] = "payroll"
        result = intake(self.source, self.metadata, 0.99, self.config, self.ledger)
        self.assertEqual(result["outcome"], "EXCEPTION")
        self.assertIn("ROUTE_NOT_ENABLED", result["reason_codes"])

    def test_duplicate_intake_is_idempotent(self):
        first = intake(self.source, self.metadata, 0.99, self.config, self.ledger)
        second = intake(self.source, self.metadata, 0.99, self.config, self.ledger)
        self.assertFalse(first["duplicate"])
        self.assertTrue(second["duplicate"])
        self.assertEqual(first["record_id"], second["record_id"])
        self.assertEqual(first["sha256"], second["sha256"])
        events = self.ledger.replay(first["record_id"])
        self.assertEqual(len(events), 2)

    def test_approval_and_chain_verify(self):
        result = intake(self.source, self.metadata, 0.99, self.config, self.ledger)
        approval = record_approval(
            result["record_id"],
            decision="APPROVED",
            approver="Ashley Halvorson",
            content_hash=result["sha256"],
            version="1.0",
            config=self.config,
            ledger=self.ledger,
            document_id="PMPS-PRO-OPS-001",
        )
        self.assertEqual(approval["decision"], "APPROVED")
        events = self.ledger.replay(result["record_id"])
        self.assertEqual(
            [e["event_type"] for e in events],
            ["record.received", "route.proposed", "approval.recorded"],
        )
        chain = self.ledger.verify_chain()
        self.assertTrue(chain["ok"])
        self.assertEqual(chain["checked"], 3)

    def test_chain_detects_tamper(self):
        intake(self.source, self.metadata, 0.99, self.config, self.ledger)
        # Tamper with raw payload in DB
        self.ledger.db.execute(
            "UPDATE events SET payload=? WHERE sequence=1",
            (json.dumps({"tampered": True}),),
        )
        self.ledger.db.commit()
        chain = self.ledger.verify_chain()
        self.assertFalse(chain["ok"])


if __name__ == "__main__":
    unittest.main()
