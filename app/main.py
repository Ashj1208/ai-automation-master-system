import os
from fastapi import FastAPI

app = FastAPI(title="AI Automation Master System", version="1.0-staging")

@app.get("/health")
def health():
    return {"status": "ok", "environment": os.getenv("APP_ENV", "staging"), "service": "ai-automation-master-system"}

@app.get("/ready")
def ready():
    return {"status": "ready"}
