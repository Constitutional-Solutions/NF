"""Human-anchor interface scaffold."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class HumanAnchorInterface:
    """Placeholder for EEG timing integration."""

    sample_hz: int = 100

    def status(self) -> Dict[str, int]:
        return {"sample_hz": self.sample_hz}
