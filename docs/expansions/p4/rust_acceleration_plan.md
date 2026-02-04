# Rust Acceleration Plan (Scaffold)

## Goal
Identify hot paths for Rust migration.

## Candidates
- Bio routing and stress simulation
- Quantum harmonic computations
- Pattern registry serialization

## Approach
- Start with FFI bindings for compute-heavy functions.
- Validate against Python reference outputs.

## Phase 1: Legion Core Rust Bridge (Scaffolded)
- Create a `legion_core_rs` crate with PyO3 bindings to accelerate:
  - `genesis_kernel/quantum.py` (energy eigenvalue + phi quantization)
  - `genesis_kernel/pattern_math.py` (quadratic growth stream)
- Python side uses `importlib` detection to call Rust when available, with a
  safe Python fallback when not installed.

## Phase 2: Packaging & Cross-Compile
- Publish wheels for macOS/Linux/x86_64 and cross-compile for RISC-V.
- Include build flags and toolchain notes in the Sovereign Stack plan.
