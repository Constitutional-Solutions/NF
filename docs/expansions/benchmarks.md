# Acceleration Proof Benchmarks

This document captures the benchmark harness used to compare Python vs Rust
paths in the Genesis Kernel.

## Script
Run:

```bash
PYTHONPATH=. python scripts/run_benchmarks.py --iterations 10000 --warmup 100 --output benchmarks.json
```

The output JSON includes:
- `baseline` (forced Python)
- `accelerated` (Rust when available)
- `speedup` summary
- `sovereign_stack` target summary
- per-task timings (`phi_quantization`, `bicameral_synthesis`)

## Notes
- The warmup loop reduces first-iteration jitter.
- When Rust bindings are present, `phi_quantization` uses the Rust engine.
- The bicameral synthesis benchmark exercises the end-to-end decision loop.
