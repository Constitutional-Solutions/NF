# Container Profiles (Legion Light / Heavy)

This document defines the two deployment profiles used by the kernel.

## Legion-Light
- Base: `python:3.11-slim`
- Purpose: edge nodes, minimal memory footprint
- Rust: not required

Dockerfile: `docker/Dockerfile.light`

## Legion-Heavy
- Base: `python:3.11`
- Purpose: server nodes with Rust toolchain and optional GPU stack
- Rust: included for `legion_core_rs` compilation

Dockerfile: `docker/Dockerfile.heavy`
