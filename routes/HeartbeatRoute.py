from fastapi import APIRouter

router = APIRouter(prefix="/heartbeat")


@router.get("/ping")
async def ping():
    return {"message": "PONG"}
