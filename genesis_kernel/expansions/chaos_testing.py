"""Chaos testing harness scaffolding."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class ChaosTestHarness:
    """Define simple chaos test metadata for paradox/fraud scenarios."""

    name: str = "baseline"

    def scenario(self) -> Dict[str, str]:
        return {"scenario": self.name, "status": "PENDING"}
