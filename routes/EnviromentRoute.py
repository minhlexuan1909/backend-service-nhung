from fastapi import APIRouter, status, Depends
from fastapi.security.api_key import APIKeyHeader
from schemas.enviroment import CaptureEnviroment
from repositories import Enviroment
import routes.auth as Auth

router = APIRouter(prefix="/enviroment")


@router.post("/capture", status_code=status.HTTP_201_CREATED)
async def capture(body: CaptureEnviroment, api_key: APIKeyHeader = Depends(Auth.ApiKey)):
    captured_enviroment = Enviroment.create(body).to_dict()
    return captured_enviroment