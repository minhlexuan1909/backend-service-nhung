from schemas.enviroment import CaptureEnviroment
from repositories import Enviroment

def capture(body: CaptureEnviroment):
    return Enviroment.create(body).to_dict()
    