"""Oubliette sharding policy scaffolding."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
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

    def next_rotation(self, created_at: datetime) -> datetime:
        return created_at + timedelta(hours=self.rotation_hours)

    def expires_at(self, created_at: datetime) -> datetime:
        return created_at + timedelta(days=self.retention_days)

    def is_expired(self, created_at: datetime, now: datetime | None = None) -> bool:
        comparison = now or datetime.utcnow()
        return comparison >= self.expires_at(created_at)

    def enforce_retention(self, created_at: datetime) -> Dict[str, str]:
        expired = self.is_expired(created_at)
        return {
            "expired": str(expired),
            "expires_at": self.expires_at(created_at).isoformat() + "Z",
            "cipher": self.cipher,
        }
