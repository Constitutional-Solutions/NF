"""Bio-math and mycelial routing engine."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List

from .constants import UniversalConstants

try:
    import networkx as nx
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    nx = None


@dataclass
class BioSystemEngine:
    """Implements mycelial routing, bio-torus concepts, and glyph encoding."""

    constants: UniversalConstants
    base_bio: int = 1_440_000

    def mycelial_route_optimize(
        self,
        nodes: Iterable[Dict[str, float]],
        stress_level: float,
        max_nodes: int = 5,
    ) -> Dict[str, object]:
        """
        Optimize network paths like slime mold.
        High stress = redundant paths. Low stress = efficient paths.
        """
        redundancy = 1 if stress_level < 0.5 else 3
        node_list = list(nodes)
        if nx is not None:
            graph = nx.Graph()
            for node in node_list:
                graph.add_node(node["id"], value=node["value"])
        sorted_nodes = sorted(node_list, key=lambda x: x["value"], reverse=True)
        selected: List[int] = [
            int(node["id"]) for node in sorted_nodes[: max_nodes * redundancy]
        ]
        return {
            "optimized_path": selected,
            "redundancy_factor": redundancy,
            "mode": "SURVIVAL" if redundancy > 1 else "GROWTH",
        }

    def bio_base_convert(self, number: int) -> str:
        """Convert decimal to Base-1.44M Bio-Glyphs."""
        return f"BIO-{number % self.base_bio:07d}"
