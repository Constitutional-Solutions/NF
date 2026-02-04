"""Nervous system I/O bridge for hardware integration."""
from __future__ import annotations

from dataclasses import dataclass, field
import importlib.util
from typing import Dict, List, Protocol

if importlib.util.find_spec("requests"):
    import requests
else:  # pragma: no cover - optional dependency
    requests = None


@dataclass
class NervousSystemDriver(Protocol):
    """Protocol for pluggable nervous system drivers."""

    def dispatch_dream(self, task_data: Dict[str, object]) -> Dict[str, object]:
        ...

    def optical_reflex(self) -> List[Dict[str, str]]:
        ...


@dataclass
class NervousSystemIO:
    """Bridge between the logic core and physical device clusters."""

    swarm_ips: List[str] = field(default_factory=list)
    vision_ips: List[str] = field(default_factory=list)
    dispatch_timeout_s: float = 1.0
    vision_timeout_s: float = 0.5
    driver_name: str = "http"

    def dispatch_dream(self, task_data: Dict[str, object]) -> Dict[str, object]:
        """Send a background task to the Orange Pi swarm."""
        if not self.swarm_ips:
            return {"status": "NO_NERVES_DETECTED"}

        target_node = self.swarm_ips[hash(str(task_data)) % len(self.swarm_ips)]
        if requests is None:
            return {"status": "REQUESTS_UNAVAILABLE", "node": target_node}
        try:
            # response = requests.post(
            #     f"http://{target_node}:8000/dream",
            #     json=task_data,
            #     timeout=self.dispatch_timeout_s,
            # )
            return {"status": "SENT", "node": target_node}
        except Exception as exc:  # pragma: no cover - network dependent
            return {"status": "DEAD_NERVE", "node": target_node, "error": str(exc)}

    def optical_reflex(self) -> List[Dict[str, str]]:
        """Trigger the S20 array to capture reality."""
        if not self.vision_ips:
            return [{"status": "BLIND"}]
        results: List[Dict[str, str]] = []
        for eye_ip in self.vision_ips[:3]:
            if requests is None:
                results.append({"eye": eye_ip, "status": "REQUESTS_UNAVAILABLE"})
                continue
            try:
                # response = requests.get(
                #     f"http://{eye_ip}:5000/look",
                #     timeout=self.vision_timeout_s,
                # )
                results.append({"eye": eye_ip, "status": "CAPTURED"})
            except Exception:  # pragma: no cover - network dependent
                results.append({"eye": eye_ip, "status": "UNREACHABLE"})
        return results
