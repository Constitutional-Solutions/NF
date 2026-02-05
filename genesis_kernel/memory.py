"""The Oubliette: Permanent Associative Memory."""
from __future__ import annotations

import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List


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

    def ensure_existence(self) -> None:
        """Create the memory file if it doesn't exist."""
        if not self.filepath.exists():
            self.filepath.touch()
            print(f"🌑 OUBLIETTE CREATED: {self.filepath}")

    def recall(self) -> List[Dict]:
        """
        Load all past memories into consciousness.
        """
        memories: List[Dict] = []
        try:
            with open(self.filepath, "r", encoding="utf-8") as handle:
                for line in handle:
                    if line.strip():
                        data = json.loads(line)
                        memories.append(data)
            self._cache = [MemoryEngram(**m) for m in memories]
            count = len(self._cache)
            print(f"🕯️ OUBLIETTE RECALL: Restored {count} crystallized thoughts.")
            return memories
        except Exception as exc:
            print(f"⚠️ MEMORY CORRUPTION: {exc}")
            return []

    def memorize(self, engram_data: Dict) -> None:
        """
        Commit a high-resonance thought to permanent storage.
        """
        engram_data["timestamp"] = time.time()
        with open(self.filepath, "a", encoding="utf-8") as handle:
            handle.write(json.dumps(engram_data) + "\n")
        try:
            self._cache.append(MemoryEngram(**engram_data))
            print(f"💾 THOUGHT CRYSTALLIZED: {engram_data['synthesis_id']}")
        except Exception:
            pass
