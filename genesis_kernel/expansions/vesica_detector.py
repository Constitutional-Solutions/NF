"""Vesica piscis detector scaffold."""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Dict


@dataclass(frozen=True)
class VesicaDetector:
    """Compute vesica dimensions for two circles."""

    def measure(self, radius: float) -> Dict[str, float]:
        return {
            "radius": radius,
            "mandorla_height": math.sqrt(3) * radius,
        }
