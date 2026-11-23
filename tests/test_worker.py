import csv
import tempfile
import unittest
from pathlib import Path

from worker import generate_report


class GenerateReportTests(unittest.TestCase):
    def test_generates_csv_atomically(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = generate_report("report-001", "sales", directory)
            self.assertEqual(path.name, "report-001.csv")
            with path.open(newline="", encoding="utf-8") as handle:
                self.assertEqual(
                    list(csv.reader(handle)),
                    [["report", "total"], ["sales", "42"]],
                )
            self.assertFalse(Path(directory, "report-001.csv.tmp").exists())

    def test_rejects_unsafe_report_id(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                generate_report("../escape", "sales", directory)

    def test_rejects_empty_report_name(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                generate_report("report-001", "", directory)


if __name__ == "__main__":
    unittest.main()
