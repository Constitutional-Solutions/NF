"""Metatron cube compiler scaffold."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class MetatronCompiler:
    """Return platonic solid labels for codegen placeholders."""

    def solids(self) -> List[str]:
        return ["tetrahedron", "cube", "octahedron", "dodecahedron", "icosahedron"]
