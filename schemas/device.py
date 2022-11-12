from pydantic import BaseModel
from typing import Union, List
import datetime as dt


class SetStatusPayLoad(BaseModel):
    status: str


class SetModePayload(BaseModel):
    mode: str


class UpdateArgs(BaseModel):
    name: Union[str, None] = None
    mode: Union[str, None] = None
    status: Union[str, None] = None
    updated_at: Union[dt.datetime, None] = None


class CreateDevice(BaseModel):
    name: str
