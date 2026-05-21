from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from datetime import datetime
import os

app = FastAPI()

# Монтируем статику только если папка существует
static_dir = "static"
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir, html=True), name="static")

class UserRequest(BaseModel):
    user_id: int

@app.get("/")
async def root():
    return {"message": "TON Miner Farm API"}

@app.post("/state")
async def get_state(request: UserRequest):
    return {
        "balance": 0,
        "total_mined": 0,
        "miners": [],
        "available_to_claim": 0,
        "last_claim_at": datetime.utcnow().isoformat()
    }

@app.post("/claim")
async def claim(request: UserRequest):
    return {"success": True, "claimed": 0, "new_balance": 0}
