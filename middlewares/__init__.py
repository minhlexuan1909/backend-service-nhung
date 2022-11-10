from fastapi.security.api_key import APIKeyHeader
from fastapi import Security
from errors import UnauthorizedException
from configs import get_config

x_api_key = APIKeyHeader(name="x-api-key", auto_error=False)

async def ApiKey(x_api_key: str = Security(x_api_key)):
    if x_api_key == get_config("API_KEY"):
        return x_api_key   
    else:
        raise UnauthorizedException()
