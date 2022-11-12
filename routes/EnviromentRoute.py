from fastapi import APIRouter

from actions import Eviroment
from services.logging import LOGGER
from services.mqtt import MQTT, Client, MQTTMessage

router = APIRouter(prefix="/enviroment")


@MQTT.topic_callback("enviroment/capture")
def capture_enviroment(client: Client, userdata, msg: MQTTMessage):
    topic = msg.topic
    qos = msg.qos
    raw_payload = msg.payload.decode("utf-8")

    LOGGER.info(f"[MQTT]: Recieved message | topic: {topic} | QoS: {qos} | Payload: {raw_payload}")
    return Eviroment.capture(raw_payload)
