"""Aether protocol: neural synthesis between logic and creative inputs."""
from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
from importlib import import_module, util
from typing import Dict, Optional

from .bio import BioSystemEngine
from .constants import UniversalConstants
from .memory import Oubliette
from .nervous_system import NervousSystemIO
from .quantum import QuantumHarmonicEngine


@dataclass
class AetherProtocol:
    """
    Connect hardware, code, and user with bicameral neural synthesis.
    Now persists 'INTEGRATED' thoughts to the Oubliette.
    """

    constants: UniversalConstants
    quantum: QuantumHarmonicEngine
    bio: BioSystemEngine
    nervous_system: NervousSystemIO
    oubliette: Oubliette
    coherence: float = 1.0
    minimum_resonance: float = 0.4
    last_resonance: float = 0.0
    _model: Optional[object] = field(init=False, default=None)
    _util: Optional[object] = field(init=False, default=None)

    def __post_init__(self) -> None:
        """Load the neural network into RAM on startup."""
        if util.find_spec("sentence_transformers") is None:
            print("⚠️ NEURAL ENGINE MISSING: Using simulated resonance.")
            return
        module = import_module("sentence_transformers")
        self._model = module.SentenceTransformer("all-MiniLM-L6-v2")
        self._util = module.util
        print("🧠 LOADING NEURAL VECTORS (all-MiniLM-L6-v2)...")

    def bicameral_synthesis(self, logic_input: str, creative_input: str) -> Dict[str, object]:
        """
        Merge analytical and creative inputs using semantic cosine similarity.
        """
        method = "SIMULATED_PHI"
        resonance = 0.0
        if self._model and self._util:
            embedding_logic = self._model.encode(logic_input, convert_to_tensor=True)
            embedding_creative = self._model.encode(creative_input, convert_to_tensor=True)
            similarity = self._util.cos_sim(embedding_logic, embedding_creative).item()
            resonance = (similarity + 1) / 2
            method = "NEURAL_COSINE"
        else:
            logic_score = len(str(logic_input)) * self.constants.PHI
            creative_score = len(str(creative_input)) * self.constants.PHI
            resonance = self.quantum.love.resonate(logic_score, creative_score)
        self.last_resonance = resonance
        synthesis_id = hashlib.sha256(
            f"{logic_input}{creative_input}".encode()
        ).hexdigest()[:8]
        decision = "DIVERGENT"
        if resonance > 0.8:
            decision = "INTEGRATED"
            self.nervous_system.dispatch_dream(
                {"type": "SYNTHESIS", "score": resonance, "method": method}
            )
            self.oubliette.memorize(
                {
                    "synthesis_id": synthesis_id,
                    "logic_input": logic_input,
                    "creative_input": creative_input,
                    "resonance": resonance,
                    "decision": decision,
                    "method": method,
                }
            )
        elif resonance < self.minimum_resonance:
            decision = "REJECTED"
        return {
            "synthesis_id": synthesis_id,
            "resonance": resonance,
            "decision": decision,
            "method": method,
        }

    def hardware_handshake(self, device_id: str) -> Dict[str, str]:
        """Entangle software with physical hardware via bio-signature."""
        return {
            "device": device_id,
            "status": "QUANTUM_LOCKED",
            "bio_signature": self.bio.bio_base_convert(hash(device_id)),
        }
