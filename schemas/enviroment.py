from typing import Optional
from pydantic import BaseModel


class CaptureEnviroment(BaseModel):
    humidity: float
    temperature: float
    light: float
