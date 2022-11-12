from schemas.enviroment import CaptureEnviroment
from repositories import Enviroment
from helpers import parse_enviroment_capture


def capture(raw_payload: str):
    enviroment = parse_enviroment_capture(raw_payload)

    return Enviroment.create(CaptureEnviroment(
        humidity=enviroment['humidity'],
        temperature=enviroment['temperature'],
        light=enviroment['light']
    ))
