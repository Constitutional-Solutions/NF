"""Core universal constants and derived ratios."""
from __future__ import annotations

from dataclasses import dataclass, field
import importlib.util
import math
from typing import List

if importlib.util.find_spec("numpy"):
    import numpy as np
else:  # pragma: no cover - optional dependency
    np = None


@dataclass(frozen=True)
class UniversalConstants:
    """Container for universal constants and derived bio-math values."""

    PHI: float = field(
        default_factory=lambda: (1 + (np.sqrt(5) if np else math.sqrt(5))) / 2
    )
    PI: float = field(default_factory=lambda: np.pi if np else math.pi)
    E: float = field(default_factory=lambda: np.e if np else math.e)
    C: float = 299792458
    PLANCK: float = 6.62607015e-34
    HBAR: float = field(
        default_factory=lambda: 6.62607015e-34
        / (2 * (np.pi if np else math.pi))
    )
    LOVE_FREQ: float = 528.0
    SCHUMANN: float = 7.83

    @property
    def FIBONACCI_ANGLE(self) -> float:  # noqa: N802 - preserve symbolic name
        return 137.507764

    @property
    def BIO_SCALE(self) -> float:  # noqa: N802 - preserve symbolic name
        return self.PHI ** 3

    def fibonacci(self, n: int) -> List[int]:
        """Generate Fibonacci sequence for quantum stepping."""
        if n <= 0:
            return []
        if n == 1:
            return [0]
        fib = [0, 1]
        for _ in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib
