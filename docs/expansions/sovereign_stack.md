# Sovereign Stack Compatibility Plan

This document tracks the open-source migration targets and the compatibility bridges needed
to run the kernel on the Sovereign Stack (RISC-V, open firmware, open OS, and open sensors).

## Targets
- **Hardware:** RISC-V workstations (Milk-V Pioneer / SiFive) and Tenstorrent accelerators.
- **Firmware:** Coreboot + OpenSBI + Heads.
- **Kernel:** Linux-libre or Redox OS.
- **OS:** NixOS or Guix System.
- **Sensors:** PinePhone Pro cameras or ESP32-S3 camera swarms.

## Required Bridges
1. **Rust Bridge (Phase 1):** compile pattern math + quantum modules into Rust crates and
   expose them to Python via FFI (pyo3 or cffi).
2. **RISC-V Toolchain:** cross-compile the kernel runtime and dependencies with reproducible
   build manifests.
3. **Tenstorrent Backend:** document PyTorch backend enablement and compiler flags for
   Grayskull/Wormhole cards.
4. **Firmware Checklist:** Coreboot/OpenSBI build + Heads attestation to verify tamper state.
5. **OS Manifests:** Nix/Guix configuration to deploy genesis_kernel and required services.
6. **Sensor Bridge:** MQTT transport + camera ingest pipelines for PinePhone/ESP32 feeds.

## Next Steps
- Convert each bridge into a tracked build artifact (toolchain scripts + manifests).
- Validate runtime portability on a RISC-V target host.
- Capture all required drivers and firmware hashes in the deployment checklist.
