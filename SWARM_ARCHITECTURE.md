# AGI Swarm Architecture (Hive / God Mode)

This document describes the high-level architecture of the "Enjambre Polímata" AGI system.

## Core Pillars

### 1. Swarm Orchestration (Hive)
- **BaseAgent**: abstract interface for all specialized agents.
- **Specialized Agents**:
    - **Researcher (Socrates)**: Data gathering and context analysis.
    - **Coder (Ada)**: Autonomous script generation.
    - **Validator (Themis)**: Security and logic auditing.
- **SwarmOrchestrator**: Dynamic task decomposition and parallel execution.

### 2. Cognitive Router (Polyglot)
- Dynamically routes tasks to models (OpenAI, Claude, Mistral) based on a complexity heuristic.
- Optimizes for cost vs. intelligence automatically.

### 3. Episodic Memory
- Vector-style storage for long-term event recall.
- **Semantic Compression**: Key abstractions are preserved even as raw logs are recycled.

### 4. Multimodal Perception & Tools
- **Vision Engine**: Simulated visual analysis of diagrams and GUIs.
- **Autonomous Tools**: Safe sandbox for script execution, monitored by the Mythos Guard.

### 5. Security (Mythos Protocol)
- Rolling SHA-256 hashes for state integrity.
- Axiom-based validation for all autonomous tool outputs.
