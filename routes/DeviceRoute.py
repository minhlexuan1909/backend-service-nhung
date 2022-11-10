import json

from fastapi import APIRouter, Depends, status
from fastapi.security.api_key import APIKeyHeader

from middlewares import ApiKey
from repositories import Device
from schemas.device import SetModePayload, SetStatusPayLoad
from services.mqtt import MQTT

router = APIRouter(prefix="/devices")


@router.put("/{device_id}/status")
async def set_status(device_id: str, payload: SetStatusPayLoad, api_key: APIKeyHeader = Depends(ApiKey)):
    device = Device.update_status(device_id, payload)
    MQTT.publish("device/update-status", payload=json.dumps({
        "device_id": device_id,
        "status": payload.status
    }))
    return device.to_dict()


@router.put("/{device_id}/mode")
async def set_mode(payload: SetModePayload, api_key: APIKeyHeader = Depends(ApiKey)):
    pass


@router.post("/")
async def create():
    return Device.create_device().to_dict()
