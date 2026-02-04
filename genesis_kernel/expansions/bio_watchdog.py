"""Compassion watchdog expansion scaffold."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BioCompassionWatchdog:
    """Guardrail for minimum coherence during autonomous operations."""

    threshold: float = 0.7

    def check_coherence(self, coherence: float) -> bool:
        """Return True when coherence passes, raise on dissonance."""
        if coherence < self.threshold:
            raise ValueError("Bio-dissonance detected: halt for reflection.")
        return True
