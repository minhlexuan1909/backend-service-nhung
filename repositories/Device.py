from models.device import Device
from schemas.device import SetStatusPayLoad
from helpers import now
from errors import DeviceNotFound


def update_status(id: str, args: SetStatusPayLoad):
    device = Device.objects(id=id).first()
    if device == None:
        raise DeviceNotFound()
    device.status = args.status
    device.updated_at = now()
    return device.save()


def create_device():
    return Device(
        name='Pump',
        mode='manual',
        status='off'
    ).save()
