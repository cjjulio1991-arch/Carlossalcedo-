# Deployment Guide: NEXUS-6 Ω

## Docker Deployment

### 1. Build Image
```bash
docker build -t nexus6-core .
```

### 2. Docker Compose
```yaml
version: '3.8'
services:
  nexus6-api:
    image: nexus6-core
    command: uvicorn nexus6.api.main:app --host 0.0.0.0 --port 8000
    ports:
      - "8000:8000"
    volumes:
      - ./nexus_data:/app/data

  nexus6-dashboard:
    image: nexus6-core
    command: streamlit run nexus6/dashboard/interface.py --server.port 3000
    ports:
      - "3000:3000"
    depends_on:
      - nexus6-api
```

## Kubernetes (Conceptual)
Deployments should be scaled based on `Cognitive Noise` metrics reported by the Immune System.
- Core Engine: StatefulSet (due to local vector store indices, or use external Vector DB).
- Agents: Horizontal Pod Autoscaler.
