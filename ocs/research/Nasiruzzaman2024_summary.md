# The Evolution of Zero Trust Architecture (ZTA) — Nasiruzzaman et al., 2024

## Purpose
This paper reviews how Zero Trust Architecture has evolved from early network perimeter controls to modern, cloud-native, identity-driven security.  
It also identifies current operational challenges and forecasts the next generation of Zero Trust with automation and quantum-safe cryptography.

## Evolution of Zero Trust
- **Early Stage:** Mainly user authentication and device compliance; relied on static network rules.  
- **Shift to Cloud-Native:** Service meshes (e.g., Istio) and microsegmentation for east–west traffic inside dynamic clusters.  
- **Identity-Centric Security:** Access decisions based on user/workload identity rather than network location.

## Current Challenges
- Policy sprawl and complexity when scaling across multi-cloud environments.  
- Difficulty integrating legacy systems that lack modern identity.  
- Manual monitoring and tuning create heavy operational overhead.

## Emerging Trends
1. **AI & Machine Learning** — Automating policy generation, anomaly detection, and continuous verification.  
2. **Quantum-Safe Cryptography** — Preparing long-lifecycle systems for quantum threats by adopting post-quantum algorithms.  
3. **Edge & IoT Expansion** — Extending ZTA principles to tactical edge and IoT devices where resources are limited.

## Relevance for This Project
Shows that Zero Trust is **mature but not fully automated**.  
Highlights AI and quantum-safe security as the natural next steps — a gap this project can target by embedding AI-driven Zero Trust into DevOps CI/CD pipelines.

Rename folder ocs to docs
