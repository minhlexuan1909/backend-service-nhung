from dotenv import dotenv_values
from typing import Any
from errors import ConfigNotFound
import os

int_variables = ['PORT']

__config = {
    **dotenv_values("dev.env"),
    **os.environ
}

for key in int_variables:
    __config[key] = int(__config[key])

def get_config(key: str, default=Any) -> Any:
    return __config.get(key, default)

