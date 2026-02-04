"""Benchmark utilities for acceleration proof runs."""
from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter
from typing import Callable, Dict


@dataclass(frozen=True)
class BenchmarkResult:
    name: str
    iterations: int
    total_s: float

    @property
    def avg_ms(self) -> float:
        return (self.total_s / self.iterations) * 1000.0

    def as_dict(self) -> Dict[str, float | int | str]:
        return {
            "name": self.name,
            "iterations": self.iterations,
            "total_s": self.total_s,
            "avg_ms": self.avg_ms,
        }


def run_benchmark(name: str, func: Callable[[], None], iterations: int) -> BenchmarkResult:
    start = perf_counter()
    for _ in range(iterations):
        func()
    total = perf_counter() - start
    return BenchmarkResult(name=name, iterations=iterations, total_s=total)
