import json
import tempfile
import unittest
from pathlib import Path

from genesis_kernel.diagnostics import DiagnosticsSnapshot, SCHEMA_VERSION


class DiagnosticsSnapshotTests(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = {
            "energy": 1.0,
            "path_data": {"mode": "TEST"},
            "thought": {"decision": "TEST"},
            "glyph": {"phi_base": 1},
        }

    def test_write_includes_schema_version(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            snapshot = DiagnosticsSnapshot(output_dir=Path(tmpdir))
            path = snapshot.write(self.payload)
            data = json.loads(path.read_text())
            self.assertEqual(data["schema_version"], SCHEMA_VERSION)
            self.assertIn("timestamp", data)
            self.assertEqual(data["payload"], self.payload)

    def test_validate_payload_missing_keys(self) -> None:
        snapshot = DiagnosticsSnapshot()
        with self.assertRaises(ValueError):
            snapshot.validate_payload({"energy": 1.0})


if __name__ == "__main__":
    unittest.main()
