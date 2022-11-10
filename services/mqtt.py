import paho.mqtt.client as mqtt

from configs import get_config
from services.logging import LOGGER
from constants import MQTT_CONNECTION_STATUS


def on_connect(client: mqtt.Client, userdata, flags, rc):
    if rc != MQTT_CONNECTION_STATUS['SUCCESSFUL']:
        LOGGER.error("[MQTT]: Connect to MQTT successfully")
        exit(1)

    LOGGER.info(f"[MQTT]: Connect to MQTT fail | status={mqtt.connack_string(rc)}")


def on_message(client: mqtt.Client, userdata, msg):
    LOGGER.info(f"[MQTT]: Recieved message on topic={msg.topic} | QoS={msg.qos}")


def on_publish(client: mqtt.Client, userdata, mid):
    LOGGER.info(f"[MQTT]: Publish message mid={mid}")


def on_subcribe(client: mqtt.Client, userdata, mid, granted_qos):
    LOGGER.info(f"[MQTT]: Subcribe message mid={mid}")


def on_disconnect(client: mqtt.Client, userdata, rc):
    if rc != MQTT_CONNECTION_STATUS['SUCCESSFUL']:
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
