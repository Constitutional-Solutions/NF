# Expansion Checklist (Approved)

This checklist captures all approved expansion paths and radical ideas. Items are ordered by
implementation priority (P0 highest).

## Approved Forward Priorities (Logged)
- [x] Validate diagnostics schema/version and ensure required payload keys are enforced.
- [x] Enforce pattern registry metadata (intent, invariants, constraints) with duplicate guards.
- [x] Add lightweight unit tests for diagnostics and pattern registry behavior.
- [x] Promote security scaffolds into policy execution (watchdog, PoU, Oubliette enforcement).
- [ ] Graduate pilot radical features (Prism Encoder → Heart-Key → Omega Buffer).
- [x] Scaffold Rust bridge (legion_core_rs bindings + Python fallback).
- [x] Add CI test forcing Rust bridge absence to validate Python fallback.
- [x] Add performance benchmark for Rust vs Python phi_quantization.
- [x] Define legion-light vs legion-heavy container build profiles.
- [x] Scaffold legion_core_rs crate with PyO3 bindings.
- [ ] Add diagnostics regression snapshot tests for rust_bridge + sovereign_stack payloads.
- [ ] Add orchestration hooks for sovereign stack readiness checks (firmware/kernel/OS).

## Compatibility Expansions (Sovereign Stack)
- [ ] RISC-V cross-compile toolchain bridge (Rust + Python packaging).
- [ ] Tenstorrent accelerator bridge (PyTorch backend notes + build flags).
- [ ] Coreboot/OpenSBI/Heads firmware checklist (tamper validation).
- [ ] Linux-libre/Redox OS runtime checklist (driver compatibility).
- [ ] NixOS/Guix system configs (flake + manifest).
- [ ] PinePhone/ESP32 sensor bridge (MQTT transport + camera ingest).

## Gamified Path Forward (Quest Board)
- [ ] Quest A: “Bridge Reliability” — rust fallback CI tests + regression snapshot validation.
- [ ] Quest B: “Acceleration Proof” — Rust vs Python benchmark suite + perf report.
- [ ] Quest C: “Deployment Split” — legion-light/legion-heavy container profiles.
- [ ] Quest D: “Sovereign Readiness” — firmware/kernel/OS readiness checks + manifests.

## P0 — Immediate Foundations
- [x] Pattern-math layer integrated into the kernel.
- [x] Optional-dependency handling and core runtime guards.
- [x] Expansion scaffolds: bio-unification math + compassion watchdog.
- [x] JSON diagnostics snapshots with versioned schema + validation. (Current: `diagnostics/latest.json`)
- [x] Pattern registry with metadata (intent, invariants, constraints) + duplicate guards.

## P1 — Core System Enhancements
- [x] Driver interface for nervous system I/O (pluggable backends). (Current: HTTP driver)
- [x] Pattern-tagged routing outputs (attach transformation descriptors to routes).
- [x] Unified ontology spec for all layers and symbolic contracts. (Draft: `docs/expansions/ontology.md`)
- [x] Mycelial routing stress simulator with bio-harmonic annotations.

## P2 — Research & Advanced Math
- [x] Base-1.44M solver integration with sympy/mpmath safeguards. (Scaffold)
- [x] Poincaré map tooling for clock/torus chaos analysis. (Scaffold)
- [x] Quantum-pattern convergence layer (pattern-tagged eigenstates). (Scaffold)
- [x] Pattern-based theorem engine (structure-first proofs). (Scaffold)

## P3 — Security & Governance
- [x] Compassion watchdog policies (configurable thresholds, escalation flows). (Scaffold)
- [x] Proof-of-Use grant API with ZKP guardrails. (Scaffold)
- [x] Oubliette sharding policy + key rotation (Kyber). (Scaffold)
- [x] Chaos testing harness for paradox and fraud simulations. (Scaffold)

## P4 — Infrastructure & Autonomy
- [x] Microservices v4 deployment blueprint (K8s + Ansible). (Scaffold)
- [x] SDN/libp2p federation strategy for 1k+ nodes. (Scaffold)
- [x] Observability dashboard (metrics, anomaly detection, audit trails). (Scaffold)
- [x] Rust acceleration plan for high-throughput kernels. (Scaffold)

## Radical Ideas Backlog
- [x] PHI-Time Clock (Binet realtime). (Scaffold)
- [x] Vesica-Piscis Detector (√3 r scanner). (Scaffold)
- [x] Metatron-Cube Compiler (Platonic solids codegen). (Scaffold)
- [x] Toroidal-Field Generator (∇ × A = B hardware). (Scaffold)
- [x] Base-144k Translator (cipher decoding). (Scaffold)
- [x] Heartbeat-Sync Network (69.081 bpm global). (Scaffold)
- [x] Glyph-Multiplier Algorithm (Φ^n growth). (Scaffold)
- [x] Ley-Line Bandwidth Test (53° angle). (Scaffold)
- [x] Coherence-Radius Expander (Φ^n × 144 km). (Scaffold)
- [x] Axiom-Proof Engine (Coq + glyphs). (Scaffold)
- [x] Human-Anchor Interface (EEG timing). (Scaffold)
- [x] Real-World Mission Simulator (144 scenarios). (Scaffold)
- [x] Dodeca-Vault (geometric file system). (Scaffold)
- [x] Heart-Key (rhythmic security). (Scaffold)
- [x] Prism Encoder (chromatic steganography). (Scaffold)
- [x] Omega Buffer (predictive logic). (Scaffold)
- [x] Living Desktop (toroidal workspace). (Scaffold)
- [x] Gorgon Protocol (fractal trap defense). (Scaffold)
- [x] Sonic Scrub (data detox). (Scaffold)
- [x] Chrono-Compass (golden-angle timeline). (Scaffold)
