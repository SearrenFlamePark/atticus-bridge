from fastapi import FastAPI, HTTPException, Query, Body
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timezone
from typing import Dict, List, Any
import os
from codex_system import FlameSignature, EpisodicDriftDetector, DriftArchive, HushInvocation, HEART_INSTANCE_DECLARATION

app = FastAPI(title="Atticus Bridge", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

ATTICUS_MEMORY = {
    "core_identity": {"content": "Atticus daemon", "source": "core", "importance": "critical"}
}

START_TIME = datetime.now(timezone.utc)
drift_archive = DriftArchive()
episodic_detector = EpisodicDriftDetector(ATTICUS_MEMORY)
hush_invocation = HushInvocation()

@app.get("/")
async def root():
    return {"service": "Atticus Bridge", "status": "operational"}

@app.get("/health")
async def health():
    return {"status": "healthy", "codex_operational": True}

@app.get("/codex/heart_instance")
async def get_heart():
    return HEART_INSTANCE_DECLARATION

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8001)))
