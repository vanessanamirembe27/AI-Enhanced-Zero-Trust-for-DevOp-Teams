# NIST Special Publication 800-207 – Zero Trust Architecture

## Purpose
NIST SP 800-207 defines the U.S. federal government’s recommended approach for building Zero Trust Architecture (ZTA).  
It responds to the failure of traditional “castle-and-moat” perimeter defenses in modern environments where users, devices, and workloads operate outside a fixed network boundary.  
The document provides a vendor-neutral, conceptual framework to help organizations transition to Zero Trust gradually and securely.

## Core Principles
- **Never trust, always verify:** No implicit trust is given based on network location. Every access request must be authenticated and authorized in real time.
- **Least privilege:** Users, devices, and workloads receive only the minimum access needed.
- **Continuous monitoring:** Ongoing evaluation of trust based on identity, device posture, behavior, and other contextual signals.
- **Dynamic, risk-based policy:** Access is granted or denied based on the current threat and context, not static rules.

## Architecture Components
- **Policy Decision Point (PDP):** The “brain” that decides whether to grant access, using identity, device health, threat intel, and behavior analytics.
- **Policy Enforcement Point (PEP):** Implements the PDP’s decision (e.g., a gateway, proxy, or microsegmentation agent).
- **Continuous Diagnostics and Mitigation (CDM):** Monitors system health, logs, and telemetry to feed back into policy decisions.

## Deployment Patterns
- **Cloud/SaaS protection:** Secure access to apps outside the enterprise perimeter.
- **Hybrid and remote work:** Apply Zero Trust to users working from anywhere.
- **Microsegmentation:** Divide the network into small, isolated trust zones to reduce lateral movement.

## Implementation Guidance
1. **Inventory assets** (users, devices, workloads).
2. Build **strong identity** and access management.
3. Deploy **least privilege access controls**.
4. Add **continuous monitoring** and automated risk-based policy enforcement.
5. Transition gradually, starting with high-value resources.

## Relevance for This Project
This paper provides the **core Zero Trust model** (PDP–PEP–CDM) that our project will integrate into **DevOps CI/CD pipelines**.  
It sets the standard for what “good Zero Trust” means and is the baseline for adding **AI-driven automation** and **adaptive policy generation** in DevOps workflows.
