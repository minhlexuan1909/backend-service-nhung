import paho.mqtt.client as mqtt

from actions import Eviroment
from configs import get_config
from constants import MQTT
from schemas.enviroment import CaptureEnviroment
from services.logging import LOGGER
from helpers import parse_enviroment_capture

CONNETION_STATUS = MQTT["CONNETION_STATUS"]
TOPIC = MQTT["TOPIC"]

def on_connect(client: mqtt.Client, userdata, flags, rc):
    if rc != CONNETION_STATUS["SUCCESSFUL"]:
        LOGGER.error(f"[MQTT]: Connect to MQTT fail | status={mqtt.connack_string(rc)}")
        exit(1)

    LOGGER.info(f"[MQTT]: Connect to MQTT successfully | status={mqtt.connack_string(rc)}")
    client.subscribe("enviroment/capture")


def on_message(client: mqtt.Client, userdata, msg):
    topic = msg.topic
    qos = msg.qos
    payload = msg.payload.decode("utf-8")

    LOGGER.info(f"[MQTT]: Recieved message | topic: {topic} | QoS: {qos} | Payload: {payload}")

    if topic == TOPIC["CAPTURE_ENVIROMENT"]:
        enviroment = parse_enviroment_capture(payload)

        return Eviroment.capture(CaptureEnviroment(
            humidity=enviroment['humidity'],
            temperature=enviroment['temperature'],
            light=enviroment['light']
        ))


def on_publish(client: mqtt.Client, userdata, mid):
    LOGGER.info(f"[MQTT]: Publish message mid={mid}")


def on_subcribe(client: mqtt.Client, userdata, mid, granted_qos):
    LOGGER.info(f"[MQTT]: Subcribe message mid={mid}")


def on_disconnect(client: mqtt.Client, userdata, rc):
    if rc != CONNETION_STATUS["SUCCESSFUL"]:
        LOGGER.error(f"[MQTT]: Disconect fail status={mqtt.connack_string(rc)}")
        exit(1)

    LOGGER.info("[MQTT]: Disconnected successfully")


MQTT = mqtt.Client()

MQTT.on_connect = on_connect
MQTT.on_message = on_message
MQTT.on_disconnect = on_disconnect
MQTT.on_publish = on_publish
MQTT.on_subscribe = on_subcribe

MQTT.disable_logger()
MQTT.username_pw_set(
    username=get_config("MQTT_USERNAME"),
    password=get_config("MQTT_PASSWORD")
)
