from typing import Any, Dict

from models.enviroment import Enviroment


def create(doc: Dict[str, Any]) -> Enviroment:
    return Enviroment(**doc).save(force_insert=True)
