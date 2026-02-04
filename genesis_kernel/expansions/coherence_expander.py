"""Coherence radius expander scaffold."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class CoherenceExpander:
    """Compute phi-powered radius expansion values."""

    phi: float = 1.618033988749895

    def expand(self, base_km: float, n: int) -> List[float]:
        return [base_km * (self.phi**idx) for idx in range(n)]
