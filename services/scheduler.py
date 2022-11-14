import asyncio
from typing import Any, Dict, Union

from rocketry import Rocketry
from rocketry.conds import cron

from actions import Device
from services.logging import LOGGER

__Scheduler = Rocketry(config={
    "task_execution": "async",
    "instant_shutdown": True
})


def schedule_device(device_id: str, cron_exp: Union[str, None], duration: Union[int, None]):
    __register_task(f"{device_id}:schedule", cron_exp, __control_device, {
        "device_id": device_id,
        "duration": duration
    })


def __register_task(task_name: str, cron_exp: Union[str, None], func, params: Dict[str, Any]):
    LOGGER.info(f"[SCHEDULER]: Register task {task_name} | cron: {cron_exp} | params: {params}")
    task = cron(cron_exp)
    __Scheduler.task(task, name=task_name, func=func, parameters=params)


async def __control_device(device_id: str, duration: int):
    try:
        LOGGER.info(f"[SCHEDULER]: Turn on device {device_id}")
        Device.set_status(device_id, status="on", must_be_manual=False)
        await asyncio.sleep(duration)
        LOGGER.info(f"[SCHEDULER]: Turn off device {device_id}")
        Device.set_status(device_id, status="off", must_be_manual=False)
    except Exception as exception:
        LOGGER.error(f"[SCHEDULER]: Error when handling device {device_id} | Reason {exception.__str__()}")


def get_tasks():
    return __Scheduler.session.tasks


def get_task(task_name: str):
    try:
        return __Scheduler.session[task_name]
    except KeyError:
        LOGGER.error(f"[SCHEDULER]: Task {task_name} does not exist")
    return None


def delete(device_id: str):
    task = get_task(f"{device_id}:schedule")

    if task != None:
        LOGGER.info(f"[SCHEDULER]: Remove task {task.name}")
        task.delete()
        return True

    return False


def shutdown(force=True):
    return __Scheduler.session.shut_down(force)


def serve():
    return __Scheduler.serve()
