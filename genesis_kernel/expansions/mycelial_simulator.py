"""Mycelial routing stress simulator expansion."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class MycelialStressSimulator:
    """Generate stress response metrics for mycelial routing."""

    base_redundancy: int = 1

    def simulate(self, stress_levels: List[float]) -> Dict[str, List[float]]:
        """Return normalized stress and redundancy multipliers."""
        normalized = [max(0.0, min(1.0, level)) for level in stress_levels]
        redundancy = [self.base_redundancy + (2 if level >= 0.5 else 0) for level in normalized]
        return {
            "stress": normalized,
            "redundancy": redundancy,
        }
