"""Toroidal field generator scaffold."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class ToroidalField:
    """Return placeholder coefficients for toroidal flow."""

    def coefficients(self) -> Dict[str, float]:
        return {"ax": -0.5, "ay": 0.5, "az": 0.0}
