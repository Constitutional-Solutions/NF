"""Run acceleration proof benchmarks for the Genesis Kernel."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from genesis_kernel.aether import AetherProtocol
from genesis_kernel.benchmarks import run_benchmark
from genesis_kernel.bio import BioSystemEngine
from genesis_kernel.constants import UniversalConstants
from genesis_kernel.love_math import LoveMathematics
from genesis_kernel.nervous_system import NervousSystemIO
from genesis_kernel.quantum import QuantumHarmonicEngine
from genesis_kernel.rust_bridge import rust_status
from genesis_kernel.expansions import SovereignStackPlan


def main() -> int:
    parser = argparse.ArgumentParser(description="Run kernel benchmarks.")
    parser.add_argument("--iterations", type=int, default=10000)
    parser.add_argument("--warmup", type=int, default=100)
    parser.add_argument("--output", type=Path, default=Path("benchmarks.json"))
    args = parser.parse_args()

    def build_engines() -> tuple[QuantumHarmonicEngine, AetherProtocol]:
        constants = UniversalConstants()
        love = LoveMathematics(constants)
        bio = BioSystemEngine(constants)
        quantum = QuantumHarmonicEngine(constants, love)
        nerves = NervousSystemIO()
        aether = AetherProtocol(constants, quantum, bio, nerves)
        return quantum, aether

    def warmup(quantum: QuantumHarmonicEngine, aether: AetherProtocol) -> None:
        for _ in range(args.warmup):
            quantum.phi_quantization()
            aether.bicameral_synthesis("logic", "creative")

    def run_suite(label: str) -> dict:
        quantum, aether = build_engines()
        warmup(quantum, aether)
        results = []
        results.append(
            run_benchmark(
                "phi_quantization",
                lambda: quantum.phi_quantization(),
                args.iterations,
            )
        )
        results.append(
            run_benchmark(
                "bicameral_synthesis",
                lambda: aether.bicameral_synthesis("logic", "creative"),
                args.iterations,
            )
        )
        return {
            "label": label,
            "rust_bridge": rust_status(),
            "results": [result.as_dict() for result in results],
        }

    os.environ["LEGION_FORCE_PYTHON"] = "1"
    baseline = run_suite("python_baseline")
    os.environ.pop("LEGION_FORCE_PYTHON", None)
    accelerated = run_suite("rust_accelerated")

    def speedup(name: str) -> float:
        base = next(
            item for item in baseline["results"] if item["name"] == name
        )
        accel = next(
            item for item in accelerated["results"] if item["name"] == name
        )
        return base["avg_ms"] / accel["avg_ms"]

    payload = {
        "iterations": args.iterations,
        "warmup": args.warmup,
        "sovereign_stack": SovereignStackPlan().summary(),
        "baseline": baseline,
        "accelerated": accelerated,
        "speedup": {
            "phi_quantization": speedup("phi_quantization"),
            "bicameral_synthesis": speedup("bicameral_synthesis"),
        },
    }
    args.output.write_text(json.dumps(payload, indent=2))
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
