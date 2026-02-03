"""Glyph multiplier algorithm scaffold."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class GlyphMultiplier:
    """Generate phi-scaled glyph counts."""

    phi: float = 1.618033988749895

    def sequence(self, base: float, n: int) -> List[float]:
        return [base * (self.phi**idx) for idx in range(n)]
