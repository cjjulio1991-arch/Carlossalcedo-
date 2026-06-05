import asyncio
import sys
import os

# Add root to path
sys.path.append(os.getcwd())

from nexus6.core.engine.kernel import IntelligenceEngine

async def test_nexus_solve():
    print("Testing NEXUS-6 Ω reasoning cycle...")
    engine = IntelligenceEngine()

    problem = "How to build a sustainable colony on Mars using local resources?"
    result = await engine.solve_problem(problem)

    assert result["status"] == "SUCCESS"
    assert "result" in result
    assert "solution" in result["result"]
    print(f"Test PASSED. Status: {result['status']}")
    print(f"Solution: {result['result']['solution']}")

if __name__ == "__main__":
    asyncio.run(test_nexus_solve())
