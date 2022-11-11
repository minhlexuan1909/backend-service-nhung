from models.device import Device
from schemas.device import SetStatusPayLoad, SetModePayload
from helpers import now
from errors import DeviceNotFound


def find_by_id(id: str):
    device = Device.objects(id=id).first()
    if device == None:
        raise DeviceNotFound()
    return device


def update_status(id: str, args: SetStatusPayLoad):
    device = find_by_id(id)
    device.status = args.status
    device.updated_at = now()
    return device.save()


def update_mode(id: str, args: SetModePayload):
    device = find_by_id(id)
    device.mode = args.mode
    device.updated_at = now()
    return device.save()

