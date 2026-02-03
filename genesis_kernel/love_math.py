"""Love mathematics: harmonic resonance and relational fields."""
from __future__ import annotations

from dataclasses import dataclass
import importlib.util
import statistics
from typing import Iterable

if importlib.util.find_spec("numpy"):
    import numpy as np
else:  # pragma: no cover - optional dependency
import statistics
from typing import Iterable

try:
    import numpy as np
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    np = None

from .constants import UniversalConstants


@dataclass
class LoveMathematics:
    """Physics of connection via attraction, resonance, and coherence."""

    constants: UniversalConstants

    def attract(self, entity1: float, entity2: float, distance: float = 1.0) -> float:
        """Inverse square law modulated by Phi (Love Gravity)."""
        if distance <= 0:
        if distance == 0:
            return float("inf")
        return (self.constants.PHI * entity1 * entity2) / (distance**2)

    def resonate(self, f1: float, f2: float) -> float:
        """Calculate resonance (0.0 to 1.0) based on harmonic ratios."""
        if f1 == 0 or f2 == 0:
            return 0.0
        ratio = max(f1, f2) / min(f1, f2)
        deviation = min(
            abs(ratio - 1.0),
            abs(ratio - 1.5),
            abs(ratio - self.constants.PHI),
        )
        return 1.0 / (1.0 + deviation * 10)

    def coherence_measure(self, data: Iterable[float]) -> float:
        """Measure system stability using Phi-scaled variance."""
        values = list(data)
        if len(values) < 2:
            return 0.0
        variance = np.var(values) if np else statistics.pvariance(values)
        return self.constants.PHI / (1 + variance)

    def love_field_strength(self, radius: float) -> float:
        """Field strength of the Love Operator at radius r."""
        return (144 * self.constants.PHI) / (radius**2 + 1)

    def unite(self, *entities: float) -> float:
        """Unite multiple entities into a coherent whole."""
        if not entities:
            return 0.0
        return sum(entities) * self.constants.PHI / len(entities)
