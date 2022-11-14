from constants import MQTT as MQTT_CONSTANTS
from errors import (BadRequest, ConflictException, InvervalServerError,
                    QueueFullException)
from helpers import generate_mqtt_payload, is_valid_cron
from models.device import DeviceMode
from repositories import Device
from schemas.device import CreateDevice, SetModePayload
from services.logging import LOGGER
from services.mqtt import MQTT
from services import scheduler

TIMEOUT = MQTT_CONSTANTS["TIMEOUT"]


def set_status(device_id: str, status: str, must_be_manual=True):
    try:
        device = Device.find_by_id(device_id)

        if must_be_manual and device["mode"] != DeviceMode.MANUAL:
            raise ConflictException("Cannot set status of device not in manual mode")
        if device["status"] == status:
            raise ConflictException(f"Device's status has been already {status}")

        mqtt_payload = generate_mqtt_payload({
            "device_id": device_id,
            "status": status
        })

        LOGGER.info(f"[MQTT]: Publish message | topic: device/update-status | payload: {mqtt_payload}")

        publish = MQTT.publish("device/update-status", payload=mqtt_payload)
        publish.wait_for_publish(TIMEOUT)

        device = Device.update(device, {"status": status})
        return device.to_dict()
    except ValueError as error:
        LOGGER.error("[MQTT]: Queue is full", error)
        raise QueueFullException()

    except RuntimeError as error:
        LOGGER.error("[MQTT]: Cannot publish | Reason =", error)
        raise InvervalServerError(error.__str__())


def set_mode(device_id: str, payload: SetModePayload):
    device = Device.find_by_id(device_id)

    is_schedule = payload.mode == DeviceMode.SCHEDULE
    valid_cron = is_valid_cron(payload.cron)

    if is_schedule:
        if not valid_cron or payload.duration == None:
            raise BadRequest("Cron is not valid")
        scheduler.delete(device_id)
        scheduler.schedule_device(device_id, payload.cron, payload.duration)
    else:
        scheduler.delete(device_id)

    device = Device.update(device, payload.dict())
    return device.to_dict()


def find_by_id(device_id: str):
    return Device.find_one({"id": device_id}).to_dict()


def find_all():
    devices = Device.find({})
    return [device.to_dict() for device in devices]


def create(doc: CreateDevice):
    return Device.create(doc.dict()).to_dict()
