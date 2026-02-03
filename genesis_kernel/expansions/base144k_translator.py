"""Base-144k translator scaffold."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Base144kTranslator:
    """Translate a string into base-144k codepoints."""

    def encode(self, text: str) -> List[int]:
        return [ord(char) for char in text]
