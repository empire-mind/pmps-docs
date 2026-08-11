import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

class AugustFiveFilingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runtime = yaml.safe_load((ROOT / "config/runtime.yaml").read_text(encoding="utf-8"))
        cls.control = yaml.safe_load((ROOT / "config/control-room.yaml").read_text(encoding="utf-8"))

    def test_generation_and_single_intake_are_locked(self):
        self.assertEqual(self.runtime["filing_generation"], "2026-08-05")
        self.assertEqual(self.control["drive"]["filing_generation"], "2026-08-05")
        self.assertEqual(self.runtime["routing"]["only_intake_key"], "intake")
        self.assertEqual(self.runtime["routes"]["intake"]["display_path"], "00 Inbox")
        self.assertEqual(self.runtime["routes"]["intake"]["drive_folder_id"],
                         "1454WTIejGG2OD4xwC6I0dXkbLvJQoFHn")

    def test_route_ids_are_unique_and_present(self):
        ids = [route["drive_folder_id"] for route in self.runtime["routes"].values()]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(ids))

    def test_accounts_routes_use_august_five_children(self):
        self.assertEqual(self.runtime["class_routes"]["supplier_bill"], "bills_in")
        self.assertEqual(self.runtime["class_routes"]["sales_invoice"], "invoices_out")
        self.assertEqual(self.runtime["class_routes"]["receipt_expense"], "receipts_expenses")
        self.assertEqual(self.runtime["routes"]["bills_in"]["display_path"],
                         "04 Finance/Bills In")

    def test_private_vault_is_fail_closed(self):
        private = self.runtime["routes"]["private_vault"]
        self.assertFalse(private["enabled"])
        self.assertEqual(self.runtime["class_routes"]["payroll"], "private_vault")

    def test_legacy_scaffolds_are_not_routing_targets(self):
        paths = {route["display_path"] for route in self.runtime["routes"].values()}
        self.assertNotIn("99 INTAKE", paths)
        self.assertNotIn("98 ARCHIVE", paths)
        self.assertNotIn("90 RESTRICTED VAULT", paths)

if __name__ == "__main__":
    unittest.main()
