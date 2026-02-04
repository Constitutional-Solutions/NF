"""Chromatic steganography scaffold (Prism Encoder)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class PrismEncoder:
    """Encode payload metadata into a chromatic envelope."""

    channel: str = "rgb"

    def encode(self, payload: str) -> Dict[str, str]:
        return {"channel": self.channel, "payload": payload}

    def decode(self, envelope: Dict[str, str]) -> str:
        return envelope.get("payload", "")
