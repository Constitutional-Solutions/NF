"""Diagnostics snapshot utilities."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import json
from pathlib import Path
from typing import Any, Dict, Iterable


SCHEMA_VERSION = "1.1"
REQUIRED_PAYLOAD_KEYS = ("energy", "path_data", "thought", "glyph")


@dataclass(frozen=True)
class DiagnosticsSnapshot:
    """Persist diagnostic payloads for regression tracking."""

    output_dir: Path = Path("diagnostics")
    filename: str = "latest.json"

    def validate_payload(self, payload: Dict[str, Any]) -> None:
        """Validate the diagnostics payload before writing."""
        if not isinstance(payload, dict):
            raise TypeError("Diagnostics payload must be a dictionary.")
        missing = [key for key in REQUIRED_PAYLOAD_KEYS if key not in payload]
        if missing:
            missing_str = ", ".join(missing)
            raise ValueError(f"Diagnostics payload missing keys: {missing_str}")

    def required_keys(self) -> Iterable[str]:
        """Return required payload keys for diagnostics validation."""
        return REQUIRED_PAYLOAD_KEYS

    def write(self, payload: Dict[str, Any]) -> Path:
        """Write a diagnostics snapshot to disk and return the path."""
        self.validate_payload(payload)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        enriched = {
            "schema_version": SCHEMA_VERSION,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "payload": payload,
        }
        path = self.output_dir / self.filename
        path.write_text(json.dumps(enriched, indent=2, sort_keys=True))
        return path
