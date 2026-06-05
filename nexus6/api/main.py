from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from nexus6.core.engine.kernel import IntelligenceEngine
import asyncio

app = FastAPI(title="NEXUS-6 Ω API", version="1.0.0")
engine = IntelligenceEngine()

class ProblemRequest(BaseModel):
    problem: str

@app.get("/")
def read_root():
    return {"status": "NEXUS-6 CORE ONLINE", "version": "1.0.0-omega"}

@app.post("/solve")
async def solve(request: ProblemRequest):
    try:
        result = await engine.solve_problem(request.problem)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return engine.immune_system.health_metrics
