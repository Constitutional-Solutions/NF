"""Oubliette sharding policy scaffolding."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class OubliettePolicy:
    """Define shard rotation and retention policy metadata."""

    rotation_hours: int = 24
    retention_days: int = 30
    cipher: str = "Kyber"

    def summary(self) -> Dict[str, str]:
        return {
            "rotation_hours": str(self.rotation_hours),
            "retention_days": str(self.retention_days),
            "cipher": self.cipher,
        }
