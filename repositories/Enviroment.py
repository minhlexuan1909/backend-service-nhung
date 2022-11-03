from models.enviroment import Enviroment
from schemas.enviroment import CaptureEnviroment


def create(doc: CaptureEnviroment):
    return Enviroment(
        humidity=doc.humidity, 
        temperature=doc.temperature, 
        light=doc.light
    ).save(force_insert=True)
