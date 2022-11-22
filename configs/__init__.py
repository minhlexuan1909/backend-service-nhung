import os
from typing import Any

from dotenv import dotenv_values

int_variables = ["PORT", "MQTT_PORT", "MQTT_KEEPALIVE"]
bool_variables = []

__config = {
    **dotenv_values(".env"),
    **os.environ
}

for key in int_variables:
    __config[key] = int(__config[key])

for key in bool_variables:
    __config[key] = bool(__config[key])


def get_config(key: str, default=None) -> Any:
    return __config.get(key, default)
