import json

from fastapi import APIRouter, Depends
from fastapi.security.api_key import APIKeyHeader

from middlewares import ApiKey
from schemas.device import SetModePayload, SetStatusPayLoad
from actions import Device

router = APIRouter(prefix="/devices")


@router.put("/{device_id}/status")
async def set_status(device_id: str, payload: SetStatusPayLoad, api_key: APIKeyHeader = Depends(ApiKey)):
    return Device.set_status(device_id, payload)


@router.put("/{device_id}/mode")
async def set_mode(device_id: str, payload: SetModePayload, api_key: APIKeyHeader = Depends(ApiKey)):
    return Device.set_mode(device_id, payload)
