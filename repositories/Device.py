from models.device import Device
from helpers import now
from errors import DeviceNotFound
from typing import Any, Dict, List


def find_by_id(id: str) -> Device:
    device = Device.objects(id=id).first()
    if device == None:
        raise DeviceNotFound()
    return device


def find_one_and_update(filter: Dict[str, Any], update_values: Dict[str, Any]) -> Device:
    device = find_one(filter)
    for [key, value] in update_values.items():
        device[key] = value
    device["updated_at"] = now()
    return device.save()


def find(filter: Dict[str, Any], limit=None, skip=None) -> List[Device]:
    return Device.objects(**filter).skip(skip).limit(limit)


def find_one(filter: Dict[str, Any]) -> Device:
    device = Device.objects(**filter).first()
    if device == None:
        raise DeviceNotFound()
    return device


def update(doc: Device, update_values: Dict[str, Any]) -> Device:
    for [key, value] in update_values.items():
        doc[key] = value
    doc["updated_at"] = now()
    return doc.save()


def create(doc: Dict[str, Any]) -> Device:
    return Device(**doc).save()
