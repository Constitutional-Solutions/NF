# Rust Bridge (Legion Core)

This document records the Rust bridge implementation for accelerating hot paths in
`genesis_kernel`.

## Targets
- `QuantumHarmonicEngine.energy_eigenvalue`
- `QuantumHarmonicEngine.phi_quantization`
- `pattern_math.quadratic_growth_stream`

## Python Fallback Strategy
- The Python runtime detects the `legion_core_rs` module via `importlib`.
- When the module is absent, Python implementations remain active.

## Next Deliverables
- `legion_core_rs` crate with PyO3 bindings.
- Build instructions for macOS/Linux and RISC-V.
- CI job to publish wheels and verify output parity with Python.
