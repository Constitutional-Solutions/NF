# Legion Genesis Kernel

## Overview
A Bio-Quantum AI Kernel with Rust Acceleration. This project implements a hybrid Python/Rust computation engine featuring quantum harmonics, bio-math calculations, and pattern-based transformations.

## Project Architecture

### Core Modules (genesis_kernel/)
- **app.py** - Main orchestrator, GenesisKernel class
- **quantum.py** - Quantum harmonic engine with Rust FFI
- **bio.py** - Bio-math and mycelial routing
- **love_math.py** - Harmonic resonance calculations
- **aether.py** - Bicameral synthesis protocol
- **nervous_system.py** - Hardware I/O bridge
- **constants.py** - Universal constants (PHI, HBAR, etc.)
- **pattern_math.py** - Pattern-first mathematical representations
- **diagnostics.py** - Snapshot utilities

### Expansions (genesis_kernel/expansions/)
Additional modules for specialized computations including base-144k solving, bio-unification math, chaos testing, and more.

### Rust Acceleration (src/lib.rs)
High-performance Rust components via PyO3:
- QuantumEngineRS - Fast energy eigenvalue calculations
- PatternEngineRS - Quadratic growth stream computations

## Tech Stack
- **Python 3.11** - Primary runtime
- **Rust (stable)** - Native acceleration via PyO3/maturin
- **NumPy/SciPy** - Numerical computations
- **NetworkX** - Graph-based routing algorithms

## Running the Project
```bash
python -m genesis_kernel
```

## Building Rust Extension
```bash
maturin build --release
pip install target/wheels/*.whl
```

## Recent Changes
- 2026-02-03: Initial Replit setup, fixed syntax errors in multiple Python files, configured Rust build pipeline
