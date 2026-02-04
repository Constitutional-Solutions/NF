"""Poincaré map scaffolding for chaos analysis."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, List


@dataclass(frozen=True)
class PoincareMap:
    """Generate Poincaré section samples from a trajectory."""

    def sample(self, trajectory: List[float], predicate: Callable[[float], bool]) -> List[float]:
        """Filter trajectory values where predicate holds."""
        return [value for value in trajectory if predicate(value)]
