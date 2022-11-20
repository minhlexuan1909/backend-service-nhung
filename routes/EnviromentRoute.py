from fastapi import APIRouter, Depends
from fastapi.security.api_key import APIKeyHeader

from actions import Eviroment
from middlewares import ApiKey
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


@router.get("/latest")
async def get_latest_enviroment(api_key: APIKeyHeader = Depends(ApiKey)):
    return Eviroment.get_latest_capture()
