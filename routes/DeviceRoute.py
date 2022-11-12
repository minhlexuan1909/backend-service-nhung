from fastapi import APIRouter, Depends, status
from fastapi.security.api_key import APIKeyHeader

from actions import Device
from middlewares import ApiKey
from schemas.device import CreateDevice, SetModePayload, SetStatusPayLoad

router = APIRouter(prefix="/devices")


@router.put("/{device_id}/status")
async def set_status(device_id: str, payload: SetStatusPayLoad, api_key: APIKeyHeader = Depends(ApiKey)):
    return Device.set_status(device_id, payload)


@router.put("/{device_id}/mode")
async def set_mode(device_id: str, payload: SetModePayload, api_key: APIKeyHeader = Depends(ApiKey)):
    return Device.set_mode(device_id, payload)


@router.get("")
async def get_all(api_key: APIKeyHeader = Depends(ApiKey)):
    return Device.find_all()


@router.get("/{device_id}")
async def get_one(device_id: str, api_key: APIKeyHeader = Depends(ApiKey)):
    return Device.find_by_id(device_id)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create(payload: CreateDevice, api_key: APIKeyHeader = Depends(ApiKey)):
    return Device.create(payload)
