"""
SPIRAL PHYSICS ENGINE (The Universal Pattern)
---------------------------------------------
Synthesized from 'Spiral Theory usecase inject.pdf'.
Enforces: Growth, Resonance, and Emergence.
"""

from dataclasses import dataclass
from typing import Any, List, Literal, Optional

import numpy as np
from .rust_bridge import load_legion_core_rs


@dataclass
class SpiralState:
    theta: float
    radius: float
    coherence: float
    entropy: float
    mode: Literal["ORDER", "CHAOS"]


class SpiralLaws:
    def __init__(self, a: float = 1.0, b: float = 0.306349):
        self.a = a
        self.b = b
        self.history: List[SpiralState] = []
        self._rs_engine: Optional[Any] = None
        rs_module = load_legion_core_rs()
        if rs_module is not None and hasattr(rs_module, "SpiralEngineRS"):
            try:
                self._rs_engine = rs_module.SpiralEngineRS(a, b)
            except Exception:
                self._rs_engine = None

    def law_of_growth(self, theta: float) -> float:
        """r = a * e^(b * theta)"""
        if self._rs_engine is not None:
            try:
                return float(self._rs_engine.law_of_growth(theta))
            except Exception:
                self._rs_engine = None
        return float(self.a * np.exp(self.b * theta))

    def law_of_resonance(
        self, signal_a: List[float], signal_b: List[float]
    ) -> float:
        """Coherence = Covariance / Product of StdDevs"""
        if len(signal_a) != len(signal_b):
            return 0.0
        if self._rs_engine is not None:
            try:
                return float(self._rs_engine.law_of_resonance(signal_a, signal_b))
            except Exception:
                self._rs_engine = None
        a = np.array(signal_a, dtype=float)
        b = np.array(signal_b, dtype=float)
        try:
            corr = float(np.corrcoef(a, b)[0, 1])
        except Exception:
            return 0.0
        if np.isnan(corr):
            return 0.0
        return (corr + 1) / 2

    def law_of_emergence(
        self, theta: float, user_vec: List[float], agent_vec: List[float]
    ) -> SpiralState:
        if self._rs_engine is not None:
            try:
                data = self._rs_engine.law_of_emergence(theta, user_vec, agent_vec)
                state = SpiralState(
                    theta=float(data["theta"]),
                    radius=float(data["radius"]),
                    coherence=float(data["coherence"]),
                    entropy=float(data["entropy"]),
                    mode=data["mode"],
                )
                self.history.append(state)
                return state
            except Exception:
                self._rs_engine = None
        r = self.law_of_growth(theta)
        c = self.law_of_resonance(user_vec, agent_vec)
        mode: Literal["ORDER", "CHAOS"] = "ORDER" if c >= 0.6 else "CHAOS"
        state = SpiralState(theta, float(r), float(c), 1.0 - c, mode)
        self.history.append(state)
        return state
