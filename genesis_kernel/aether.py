"""Aether protocol: Neural synthesis with Oubliette persistence."""
from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
from typing import Dict, Optional

# 🧠 NEURAL IMPORTS
try:
    from sentence_transformers import SentenceTransformer, util
    NEURAL_AVAILABLE = True
except ImportError:
    NEURAL_AVAILABLE = False

from .bio import BioSystemEngine
from .constants import UniversalConstants
from .nervous_system import NervousSystemIO
from .quantum import QuantumHarmonicEngine
from .memory import Oubliette  # <--- NEW IMPORT

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
    oubliette: Oubliette  # <--- NEW COMPONENT
    
    coherence: float = 1.0
    minimum_resonance: float = 0.4
    last_resonance: float = 0.0
    
    _model: Optional[object] = field(init=False, default=None)

    def __post_init__(self):
        """Load the Neural Network into RAM on startup."""
        if NEURAL_AVAILABLE:
            print("🧠 LOADING NEURAL VECTORS (all-MiniLM-L6-v2)...")
            self._model = SentenceTransformer('all-MiniLM-L6-v2')
        else:
            print("⚠️ NEURAL ENGINE MISSING: Using simulated resonance.")

    def bicameral_synthesis(self, logic_input: str, creative_input: str) -> Dict[str, object]:
        """
        Merge inputs. If resonance is high, commit to memory.
        """
        method = "SIMULATED_PHI"
        resonance = 0.0

        if NEURAL_AVAILABLE and self._model:
            # Neural Cosine Similarity
            emb_logic = self._model.encode(logic_input, convert_to_tensor=True)
            emb_creative = self._model.encode(creative_input, convert_to_tensor=True)
            similarity = util.cos_sim(emb_logic, emb_creative).item()
            resonance = (similarity + 1) / 2
            method = "NEURAL_COSINE"
        else:
            # Simulated Fallback
            l_score = len(str(logic_input)) * self.constants.PHI
            c_score = len(str(creative_input)) * self.constants.PHI
            resonance = self.quantum.love.resonate(l_score, c_score)

        self.last_resonance = resonance
        
        synthesis_id = hashlib.sha256(
            f"{logic_input}{creative_input}".encode()
        ).hexdigest()[:8]

        decision = "DIVERGENT"
        if resonance > 0.8:
            decision = "INTEGRATED"
        elif resonance < self.minimum_resonance:
            decision = "REJECTED"

        # 💾 THE OUBLIETTE COMMIT
        if decision == "INTEGRATED":
            # 1. Dispatch Dream (Action)
            self.nervous_system.dispatch_dream({
                "type": "SYNTHESIS", 
                "score": resonance, 
                "method": method
            })
            # 2. Crystallize Memory (Storage)
            self.oubliette.memorize({
                "synthesis_id": synthesis_id,
                "logic_input": logic_input,
                "creative_input": creative_input,
                "resonance": resonance,
                "decision": decision,
                "method": method
            })

        return {
            "synthesis_id": synthesis_id,
            "resonance": resonance,
            "decision": decision,
            "method": method
        }
    
    def hardware_handshake(self, device_id: str) -> Dict[str, str]:
        return {
            "device": device_id,
            "status": "QUANTUM_LOCKED",
            "bio_signature": self.bio.bio_base_convert(hash(device_id)),
        }
