import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

class UserRequest(BaseModel):
    user_id: int

@app.get("/")
async def root():
    return {"message": "TON Miner Farm работает!"}

@app.post("/state")
async def get_state(request: UserRequest):
    return {"balance": 0, "total_mined": 0, "miners": [], "available_to_claim": 0, "last_claim_at": datetime.utcnow().isoformat()}

@app.post("/claim")
async def claim(request: UserRequest):
    return {"success": True, "claimed": 0, "new_balance": 0}
