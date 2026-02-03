"""Rhythmic security scaffold (Heart-Key)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class HeartKey:
    """Validate cadence timing against a target bpm signature."""

    bpm: float = 69.081

    def validate(self, intervals_ms: List[float], tolerance_ms: float = 120.0) -> bool:
        if not intervals_ms:
            return False
        target_ms = 60000.0 / self.bpm
        return all(abs(interval - target_ms) <= tolerance_ms for interval in intervals_ms)
