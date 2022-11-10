from fastapi import APIRouter, status, Depends
from fastapi.security.api_key import APIKeyHeader
from schemas.enviroment import CaptureEnviroment
from repositories import Enviroment
from middlewares import ApiKey

router = APIRouter(prefix="/enviroment")


@router.post("/capture", status_code=status.HTTP_201_CREATED)
async def capture(body: CaptureEnviroment, api_key: APIKeyHeader = Depends(ApiKey)):
    captured_enviroment = Enviroment.create(body).to_dict()
    return captured_enviroment