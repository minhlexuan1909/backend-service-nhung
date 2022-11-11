from constants import MQTT as MQTT_CONSTANT
from errors import InvervalServerError, QueueFullException
from helpers import generate_mqtt_payload
from repositories import Device
from schemas.device import SetModePayload, SetStatusPayLoad
from services.logging import LOGGER
from services.mqtt import MQTT

TIMEOUT = MQTT_CONSTANT["TIMEOUT"]

def set_status(device_id: str, payload: SetStatusPayLoad):
    try:
        mqtt_payload = generate_mqtt_payload({
            "device_id": device_id,
            "status": payload.status
        })
        LOGGER.info(f"[MQTT]: Publish message | topic: device/update-status | payload: {mqtt_payload}")
        publish = MQTT.publish("device/update-status", payload=mqtt_payload)
        publish.wait_for_publish(TIMEOUT)
    except ValueError:
        LOGGER.error("[MQTT]: Queue is full")
        raise QueueFullException()
    except RuntimeError as error:
        LOGGER.error("[MQTT]: Cannot publish | Reason =", error)
        raise InvervalServerError(error.__str__())

    device = Device.update_status(device_id, payload)
    return device.to_dict()


def set_mode(device_id: str, payload: SetModePayload):
    pass
