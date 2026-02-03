"""Pattern-based theorem engine scaffolding."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List

from ..pattern_math import StructuralProperty


@dataclass(frozen=True)
class TheoremEngine:
    """Skeleton for structure-first theorem reasoning."""

    def summarize(self, properties: List[StructuralProperty]) -> str:
        return ", ".join(prop.name for prop in properties) or "none"
