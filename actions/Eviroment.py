from actions import Device as DeviceAction
from helpers import parse_enviroment_capture
from models.device import DeviceMode, DeviceStatus
from repositories import Device, Enviroment
from services.model import can_turn_on_light, can_turn_on_pump


def capture(raw_payload: str):
    enviroment = parse_enviroment_capture(raw_payload)

    pump = Device.find_one({"name": "Pump"})
    light = Device.find_one({"name": "Light"})

    if pump["mode"] == DeviceMode.AUTO:
        humidity, temp = enviroment["humidity"], enviroment["temperature"]
        status = DeviceStatus.ON if can_turn_on_pump(humidity, temp) else DeviceStatus.OFF
        if pump["status"] != status:
            DeviceAction.set_status(pump, status, must_be_manual=False)

    if light["mode"] == DeviceMode.AUTO:
        status = DeviceStatus.ON if can_turn_on_light(enviroment["light"]) else DeviceStatus.OFF
        if light["status"] != status:
            DeviceAction.set_status(light, status, must_be_manual=False)

    return Enviroment.create(enviroment)
