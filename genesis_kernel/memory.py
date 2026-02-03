"""The Oubliette: Permanent Associative Memory."""
from __future__ import annotations

import json
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Dict, Optional

@dataclass
class MemoryEngram:
    """A single unit of crystallized thought."""
    timestamp: float
    synthesis_id: str
    logic_input: str
    creative_input: str
    resonance: float
    decision: str
    method: str

class Oubliette:
    """
    The Permanent Storage Layer.
    Writes high-resonance thoughts to a distinct timeline.
    """
    def __init__(self, filename: str = "memory.jsonl"):
        self.filepath = Path(filename)
        self._cache: List[MemoryEngram] = []
        self.ensure_existence()

    def ensure_existence(self):
        """Create the memory file if it doesn't exist."""
        if not self.filepath.exists():
            self.filepath.touch()
            print(f"🌑 OUBLIETTE CREATED: {self.filepath}")

    def recall(self) -> List[Dict]:
        """
        Load all past memories into consciousness.
        """
        memories = []
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        data = json.loads(line)
                        memories.append(data)
            self._cache = [MemoryEngram(**m) for m in memories]
            count = len(self._cache)
            print(f"🕯️ OUBLIETTE RECALL: Restored {count} crystallized thoughts.")
            return memories
        except Exception as e:
            print(f"⚠️ MEMORY CORRUPTION: {e}")
            return []

    def memorize(self, engram_data: Dict):
        """
        Commit a high-resonance thought to permanent storage.
        """
        # Add timestamp
        engram_data["timestamp"] = time.time()
        
        # Write to disk (Append Mode)
        with open(self.filepath, "a", encoding="utf-8") as f:
            f.write(json.dumps(engram_data) + "\n")
        
        # Update cache
        try:
            self._cache.append(MemoryEngram(**engram_data))
            print(f"💾 THOUGHT CRYSTALLIZED: {engram_data['synthesis_id']}")
        except:
            pass # Non-critical cache failure
