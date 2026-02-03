"""Quantum-pattern convergence scaffolding."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from ..pattern_math import PatternTransformation


@dataclass(frozen=True)
class QuantumPatternTagger:
    """Tag quantum states with pattern descriptors."""

    def tag(self, state_id: int) -> Dict[str, str]:
        pattern = PatternTransformation(
            name="quantum-eigenstate",
            steps=["prepare", "quantize", f"state-{state_id}"],
        )
        return {"state": str(state_id), "pattern": pattern.describe()}
