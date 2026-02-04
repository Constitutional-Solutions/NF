"""Quantum harmonic engine."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .constants import UniversalConstants
from .love_math import LoveMathematics
from .rust_bridge import load_legion_core_rs


@dataclass
class QuantumHarmonicEngine:
    """Integrates quantum mechanics with harmonic series."""

    constants: UniversalConstants
    love: LoveMathematics
    fibonacci: List[int] = field(init=False)
    _rs_engine: Optional[object] = field(init=False, default=None)

    def __post_init__(self) -> None:
        self.fibonacci = self.constants.fibonacci(20)
        module = load_legion_core_rs()
        if module is not None:
            self._rs_engine = module.QuantumEngineRS()

    def energy_eigenvalue(self, n: int, omega: float = 1.0) -> float:
        """
        E_n = h_bar * omega * (n + 1/2)
        Calculates energy of a quantum thought state.
        """
        if n < 0:
            raise ValueError("Quantum level must be non-negative.")
        if omega <= 0:
            raise ValueError("Omega must be positive.")
        if self._rs_engine is not None:
            try:
                return float(self._rs_engine.energy_eigenvalue(n, omega))
            except Exception:
                self._rs_engine = None
        return self.constants.HBAR * omega * (n + 0.5)

    def phi_quantization(self) -> Dict[str, int]:
        """Quantize the Golden Ratio into a base state."""
        if self._rs_engine is not None:
            try:
                base_144k, nearest_fib = self._rs_engine.phi_quantization()
                quantum_state = int(self.constants.PHI * 100)
            except Exception:
                self._rs_engine = None
                base_144k = int(self.constants.PHI * 144_000)
                quantum_state = int(self.constants.PHI * 100)
                nearest_fib = min(
                    self.fibonacci, key=lambda x: abs(x - quantum_state)
                )
        else:
            base_144k = int(self.constants.PHI * 144_000)
            quantum_state = int(self.constants.PHI * 100)
            nearest_fib = min(
                self.fibonacci, key=lambda x: abs(x - quantum_state)
            )
        return {
            "phi_base": base_144k,
            "quantum_n": quantum_state,
            "nearest_fib": nearest_fib,
        }
