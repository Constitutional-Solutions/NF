"""Compassion watchdog policy scaffolding."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class WatchdogPolicy:
    """Define threshold and escalation responses for watchdog checks."""

    threshold: float = 0.7
    escalation: str = "HALT"

    def evaluate(self, coherence: float) -> Dict[str, str]:
        status = "PASS" if coherence >= self.threshold else "FAIL"
        return {"status": status, "escalation": self.escalation}
