"""Diagnostics snapshot utilities."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import json
from pathlib import Path
from typing import Any, Dict


@dataclass(frozen=True)
class DiagnosticsSnapshot:
    """Persist diagnostic payloads for regression tracking."""

    output_dir: Path = Path("diagnostics")
    filename: str = "latest.json"

    def write(self, payload: Dict[str, Any]) -> Path:
        """Write a diagnostics snapshot to disk and return the path."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        enriched = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "payload": payload,
        }
        path = self.output_dir / self.filename
        path.write_text(json.dumps(enriched, indent=2, sort_keys=True))
        return path
