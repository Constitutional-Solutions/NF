"""Heartbeat sync network scaffold."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class HeartbeatSync:
    """Return target bpm for synchronization."""

    bpm: float = 69.081

    def status(self) -> Dict[str, float]:
        return {"bpm": self.bpm}
