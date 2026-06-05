# NEXUS-6 Ω: Production-Ready Cognitive Swarm

NEXUS-6 Ω is a modular, scalable multi-agent AI platform designed for solving complex global challenges.

## 💠 Improved Architecture

### 1. Unified Engine & Providers
- **LLM Agnostic**: Supports OpenAI, Anthropic, and Local models via a standardized `Provider` interface.
- **Hierarchical Reasoning**: Orchestrates Analyst, Engineer, Scientist, and Auditor agents in a collaborative cycle.

### 2. Specialized Agents
- **Analyst**: Generates hypotheses using pattern recognition.
- **Engineer**: Designs optimized technical architectures.
- **Scientist**: Validates theoretical foundations via simulation.
- **Auditor**: Conducts safety scans and logical consistency checks.

### 3. Tiered Memory System
- **Vector-Native**: Powered by **ChromaDB** for semantic retrieval.
- **Experience Layer**: Implements recursive learning from previous interaction results.

### 4. Advanced Security (Cognitive Immune System)
- **Static Analysis**: Scans agent outputs for hazardous patterns (e.g., code injection).
- **Consensus Validation**: Only authorizes actions meeting confidence thresholds.

## 🚀 Deployment & Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL (Docker-ready)
- **Cache/PubSub**: Redis (Docker-ready)
- **Frontend**: Streamlit (Observability Console)
- **Infra**: Docker & Docker Compose

### Fast Start
```bash
docker-compose up --build
```

### Manual Run
```bash
pip install -r requirements.txt
export PYTHONPATH=$PYTHONPATH:.
streamlit run nexus6/dashboard/interface.py
```

## 🛠 Project Structure
```
nexus6/
├── api/             # FastAPI Endpoints
├── dashboard/       # Streamlit Console
└── core/
    ├── agents/      # Specialized Swarm Logic
    ├── engine/      # Kernel & LLM Providers
    ├── memory/      # Tiered Vector Storage
    ├── reasoning/   # First Principles & Divergent Engines
    └── security/    # Cognitive Immune System
```
