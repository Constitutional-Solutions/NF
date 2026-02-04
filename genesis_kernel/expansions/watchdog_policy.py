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
        action = "ALLOW" if status == "PASS" else self.escalation
        return {
            "status": status,
            "escalation": self.escalation,
            "action": action,
            "coherence": f"{coherence:.4f}",
            "threshold": f"{self.threshold:.4f}",
        }

    def enforce(self, coherence: float) -> Dict[str, str]:
        """Evaluate coherence and raise if enforcement is required."""
        result = self.evaluate(coherence)
        if result["status"] == "FAIL":
            raise ValueError(
                "Watchdog enforcement triggered: "
                f"coherence={result['coherence']}, threshold={result['threshold']}"
            )
        return result
