"""Golden-angle timeline scaffold (Chrono-Compass)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class ChronoCompass:
    """Project timeline slots along a golden-angle spiral."""

    golden_angle_deg: float = 137.50776405

    def project(self, steps: int) -> List[float]:
        return [self.golden_angle_deg * idx for idx in range(steps)]
