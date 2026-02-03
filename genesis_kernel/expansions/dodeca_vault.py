"""Geometric file system scaffold (Dodeca-Vault)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class DodecaVault:
    """Assign categories to geometric anchors."""

    def classify(self, label: str) -> Dict[str, str]:
        mapping = {
            "work": "cube",
            "creative": "icosahedron",
            "archive": "dodecahedron",
        }
        return {"label": label, "anchor": mapping.get(label, "sphere")}
