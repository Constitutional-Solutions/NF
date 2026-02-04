"""PHI-time clock scaffold (Binet realtime)."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PhiTimeClock:
    """Compute phi-scaled timestamps."""

    phi: float = 1.618033988749895

    def scale(self, seconds: float) -> float:
        return seconds * self.phi
