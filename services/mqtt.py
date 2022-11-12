from paho.mqtt.client import Client, MQTTMessage, connack_string, MQTTv5

from configs import get_config
from constants import MQTT as MQTT_CONSTANTS
from services.logging import LOGGER

CONNETION_STATUS = MQTT_CONSTANTS["CONNETION_STATUS"]
MQTT_USERNAME = get_config("MQTT_USERNAME")
MQTT_PASSWORD = get_config("MQTT_PASSWORD")
MQTT_TSL = get_config("MQTT_TSL")

MQTT = Client(protocol=MQTTv5)

MQTT.disable_logger()
MQTT.username_pw_set(
    username=get_config("MQTT_USERNAME"),
    password=get_config("MQTT_PASSWORD")
)
if MQTT_TSL:
    MQTT.tls_set_context()


@MQTT.connect_callback()
def on_connect(client: Client, userdata, flags_dict, reason, properties):
    if reason != CONNETION_STATUS["SUCCESSFUL"]:
        LOGGER.error(f"[MQTT]: Connect to MQTT fail | status={connack_string(reason)}")
        exit(1)

    LOGGER.info(f"[MQTT]: Connect to MQTT successfully | status={connack_string(reason)}")

    # Register subcribe topic
    client.subscribe("enviroment/capture")


@MQTT.disconnect_callback()
def on_disconnect(client: Client, userdata, rc, properties):
    if rc != CONNETION_STATUS["SUCCESSFUL"]:
        LOGGER.error(f"[MQTT]: Disconect fail status={connack_string(rc)}")
        exit(1)

    LOGGER.info("[MQTT]: Disconnected successfully")
