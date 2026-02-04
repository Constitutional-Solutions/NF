# Microservices v4 Blueprint (Scaffold)

## Goal
Outline a service decomposition for the Genesis Kernel runtime.

## Candidate Services
- **kernel-orchestrator**: boot, diagnostics, snapshotting.
- **pattern-service**: pattern registry, transformations, properties.
- **bio-routing**: mycelial routing and stress simulations.
- **quantum-engine**: eigenvalue and quantization APIs.
- **aether-gateway**: synthesis and decision APIs.

## Deployment Notes
- Target Kubernetes namespaces per service.
- Provide Helm charts and baseline resource limits.
