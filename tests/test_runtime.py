import sys
import tempfile
import unittest
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from pmps_control.ledger import Ledger
from pmps_control.runtime import intake

class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.source = self.root / "sample.txt"
        self.source.write_text("controlled bytes", encoding="utf-8")
        self.config = yaml.safe_load((ROOT / "config/runtime.yaml").read_text())
        self.metadata = {
            "record_id": "PMPS-REC-TEST-1", "client_id": "_NA",
            "project_id": "_NA", "record_class": "operations",
            "authority_system": "google_drive", "sensitivity": "INTERNAL",
            "retention_rule": "life_plus_3_years", "owner": "Document Controller",
        }
        self.ledger = Ledger(self.root / "ledger.sqlite3")

    def tearDown(self):
        self.ledger.close()
        self.tmp.cleanup()

    def test_low_risk_intake_and_replay(self):
        result = intake(self.source, self.metadata, .99, self.config, self.ledger)
        self.assertEqual(result["outcome"], "ROUTE_PROPOSED")
        events = self.ledger.replay("PMPS-REC-TEST-1")
        self.assertEqual([e["event_type"] for e in events],
                         ["record.received", "route.proposed"])
        self.assertEqual(events[0]["sha256"], events[1]["sha256"])

    def test_controlled_document_requires_approval(self):
        self.metadata["record_class"] = "controlled_document"
        result = intake(self.source, self.metadata, .99, self.config, self.ledger)
        self.assertEqual(result["outcome"], "APPROVAL_REQUIRED")

    def test_low_confidence_holds_in_intake(self):
        result = intake(self.source, self.metadata, .20, self.config, self.ledger)
        self.assertEqual(result["outcome"], "EXCEPTION")
        self.assertEqual(result["route_key"], "intake")

    def test_disabled_restricted_route_is_exception(self):
        self.metadata["record_class"] = "payroll"
        result = intake(self.source, self.metadata, .99, self.config, self.ledger)
        self.assertEqual(result["outcome"], "EXCEPTION")
        self.assertIn("ROUTE_NOT_ENABLED", result["reason_codes"])

if __name__ == "__main__":
    unittest.main()
