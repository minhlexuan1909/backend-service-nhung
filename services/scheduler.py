import functools
import schedule
from services.logging import LOGGER

def Loggable(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        LOGGER.info(f"[SCHEDULE_JOB]: Running job {func.__name__}...")
        try:
            func(*args, **kwargs)
            LOGGER.info(f"[SCHEDULE_JOB]: Job {func.__name__} finished")
        except Exception as exception:
            LOGGER.error(f"[SCHEDULE_JOB]: Job {func.__name__} failed | Reason", exception)

    return wrapper


class ScheduleJob:
    def __init__(self) -> None:
        self.__scheduler = schedule.Scheduler()
        self.__scheduler.run_all()
