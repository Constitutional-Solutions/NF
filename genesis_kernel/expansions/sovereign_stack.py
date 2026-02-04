"""Sovereign stack compatibility and migration helpers."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(frozen=True)
class SovereignStackPlan:
    """Capture hardware/software migration targets and toolchain bridges."""

    hardware_targets: List[str] = field(
        default_factory=lambda: ["RISC-V", "Tenstorrent Grayskull/Wormhole"]
    )
    firmware_targets: List[str] = field(
        default_factory=lambda: ["Coreboot", "OpenSBI", "Heads"]
    )
    kernel_targets: List[str] = field(
        default_factory=lambda: ["Linux-libre", "Redox OS"]
    )
    os_targets: List[str] = field(default_factory=lambda: ["NixOS", "Guix System"])
    sensory_targets: List[str] = field(
        default_factory=lambda: ["PinePhone Pro", "ESP32-S3 Camera Swarm"]
    )
    toolchain_bridges: List[str] = field(
        default_factory=lambda: [
            "Rust bridge for pattern_math/quantum",
            "RISC-V cross-compile toolchain",
            "Nix/Guix reproducible build configs",
            "MQTT transport for ESP32 sensors",
        ]
    )

    def summary(self) -> Dict[str, List[str]]:
        return {
            "hardware_targets": list(self.hardware_targets),
            "firmware_targets": list(self.firmware_targets),
            "kernel_targets": list(self.kernel_targets),
            "os_targets": list(self.os_targets),
            "sensory_targets": list(self.sensory_targets),
            "toolchain_bridges": list(self.toolchain_bridges),
        }
