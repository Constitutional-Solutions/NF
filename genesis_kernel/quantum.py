"""Quantum harmonic engine with Rust Acceleration."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .constants import UniversalConstants
from .love_math import LoveMathematics

# ⚡ RUST ACCELERATION BRIDGE
# Attempts to load the compiled Rust kernel (legion_core_rs).
# If missing, falls back to pure Python execution (Scavenger Mode).
try:
    import legion_core_rs
    RUST_AVAILABLE = True
    print("⚡ RUST ENGINE DETECTED: Quantum Harmonics Accelerating...")
except ImportError:
    RUST_AVAILABLE = False
    print("🐢 RUST NOT FOUND: Fallback to Python Mode.")


@dataclass
class QuantumHarmonicEngine:
    """
    Integrates quantum mechanics with harmonic series.
    Now supports hybrid execution via Rust FFI.
    """

    constants: UniversalConstants
    love: LoveMathematics
    fibonacci: List[int] = field(init=False)
    _rs_engine: Optional[object] = field(init=False, default=None)

    def __post_init__(self) -> None:
        """Initialize the engine, selecting Rust or Python backend."""
        if RUST_AVAILABLE:
            # Initialize the High-Performance Rust Engine
            self._rs_engine = legion_core_rs.QuantumEngineRS()
            # We still keep a small Python cache for fallback/debug
            self.fibonacci = self.constants.fibonacci(20)
        else:
            # Pure Python Initialization
            self.fibonacci = self.constants.fibonacci(20)

    def energy_eigenvalue(self, n: int, omega: float = 1.0) -> float:
        """
        E_n = h_bar * omega * (n + 1/2)
        Calculates energy of a quantum thought state.
        """
        if n < 0:
            raise ValueError("Quantum level must be non-negative.")
        if omega <= 0:
            raise ValueError("Omega must be positive.")

        if RUST_AVAILABLE and self._rs_engine:
            # 🚀 RUST PATH (Nanosecond Latency)
            return self._rs_engine.energy_eigenvalue(n, omega)
        else:
            # 🐢 PYTHON PATH (Microsecond Latency)
            return self.constants.HBAR * omega * (n + 0.5)

    def phi_quantization(self) -> Dict[str, int]:
        """
        Quantize the Golden Ratio into a base state.
        """
        if RUST_AVAILABLE and self._rs_engine:
            # 🚀 RUST PATH
            # Rust returns a tuple (base_144k, nearest_fib)
            base_144k, nearest_fib = self._rs_engine.phi_quantization()
            quantum_state = int(self.constants.PHI * 100) # Quick calc in Python
            
            return {
                "phi_base": base_144k,
                "quantum_n": quantum_state,
                "nearest_fib": nearest_fib,
            }
        else:
            # 🐢 PYTHON PATH
            base_144k = int(self.constants.PHI * 144_000)
            quantum_state = int(self.constants.PHI * 100)
            nearest_fib = min(self.fibonacci, key=lambda x: abs(x - quantum_state))
            
            return {
                "phi_base": base_144k,
                "quantum_n": quantum_state,
                "nearest_fib": nearest_fib,
            }
