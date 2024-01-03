from typing import Any
from fastapi import APIRouter, HTTPException
from app.api.deps import SessionDep
from app.models.hello import Hello, HelloOut

router = APIRouter()

@router.get("/api/hello/backend")
async def hello():
    return {"message": "backend"}

@router.get("/api/hello_db/backend", response_model=HelloOut)
async def hello_db(session: SessionDep, id:int = 1) -> Any:
    hello = session.get(Hello, id)
    if not hello:
        raise HTTPException(status_code=404, detail="Hello not found")
    return hello