from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException, Depends
from starlette.status import HTTP_401_UNAUTHORIZED
from configs import get_config

x_api_key = APIKeyHeader(name="x-api-key", auto_error=False)

async def ApiKey(x_api_key: str = Security(x_api_key)):
    if x_api_key == get_config("REQUEST_API_KEY"):
        return x_api_key   
    else:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED, 
            detail={
                "message": "Incorrect API Key"
            }
        )
