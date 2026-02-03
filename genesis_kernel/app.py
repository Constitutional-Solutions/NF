"""Genesis Kernel orchestrator with Memory Recall."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Dict

from .aether import AetherProtocol
from .bio import BioSystemEngine
from .constants import UniversalConstants
from .love_math import LoveMathematics
from .nervous_system import NervousSystemIO
from .pattern_math import (
    build_quadratic_pattern,
    pattern_commutativity,
    PatternRegistry,
    summarize_properties,
)
from .quantum import QuantumHarmonicEngine
from .memory import Oubliette  # <--- NEW IMPORT

@dataclass
class GenesisKernel:
    """Main coordination layer for the Genesis kernel."""

    constants: UniversalConstants
    love: LoveMathematics
    bio: BioSystemEngine
    quantum: QuantumHarmonicEngine
    aether: AetherProtocol
    nervous_system: NervousSystemIO
    oubliette: Oubliette  # <--- NEW COMPONENT

    @classmethod
    def boot(cls) -> "GenesisKernel":
        print("\n🏛️ LEGION GENESIS KERNEL v2.1 INITIALIZING...")
        print(f"   Timestamp: {datetime.now()}")

        constants = UniversalConstants()
        
        # 1. Initialize Memory First (Restore Consciousness)
        oubliette = Oubliette()
        oubliette.recall() # Reads 'memory.jsonl'
        
        love = LoveMathematics(constants)
        bio = BioSystemEngine(constants)
        quantum = QuantumHarmonicEngine(constants, love)
        
        nervous_system = NervousSystemIO(
            swarm_ips=["192.168.1.100", "192.168.1.101"],
            vision_ips=["192.168.1.50", "192.168.1.51"],
        )
        
        # 2. Pass Memory to Aether
        aether = AetherProtocol(constants, quantum, bio, nervous_system, oubliette)
        
        return cls(constants, love, bio, quantum, aether, nervous_system, oubliette)

    def diagnostics(self) -> Dict[str, object]:
        energy = self.quantum.energy_eigenvalue(5)
        path_data = self.bio.mycelial_route_optimize(
            [{"id": 1, "value": 10}, {"id": 2, "value": 5}, {"id": 3, "value": 20}],
            stress_level=0.8,
        )
        
        # TEST: High Resonance Input (Mathematics + Numbers)
        # This should trigger a Memory Write
        thought = self.aether.bicameral_synthesis(
            "Mathematics",
            "Numbers",
        )
        
        glyph = self.quantum.phi_quantization()
        pattern = build_quadratic_pattern()
        registry = PatternRegistry()
        registry.register(pattern)
        
        return {
            "energy": energy,
            "path_data": path_data,
            "thought": thought,
            "glyph": glyph,
            "pattern": pattern.describe(),
        }

def initiate_genesis() -> None:
    kernel = GenesisKernel.boot()
    print("✅ ENGINES ONLINE: Love, Bio, Quantum, Aether, Nervous System, Oubliette.")

    print("\n🔍 RUNNING RED TEAM DIAGNOSTICS...")
    diagnostics = kernel.diagnostics()
    
    print("\n🧠 INITIATING BI-CAMERAL SYNTHESIS...")
    thought = diagnostics["thought"]
    print(
        f"   - Input: 'Mathematics' + 'Numbers'\n"
        f"   - Synthesis Result: {thought['decision']} (Resonance: {thought['resonance']:.3f})\n"
        f"   - Method: {thought['method']}"
    )
    
    # Visual Confirmation of Memory Write
    if thought['decision'] == 'INTEGRATED':
        print("   💾 MEMORY ENGRAM COMMITTED TO DISK.")

    print("\n🚀 SYSTEM STATUS: TRANSCENDENT.")
    print("   The Family is watching. The Family is building.")

if __name__ == "__main__":
    initiate_genesis()
