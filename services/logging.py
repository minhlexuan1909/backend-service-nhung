import logging
from rich.logging import RichHandler

FORMAT = "%(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(
    format=FORMAT,
    datefmt=DATE_FORMAT,
    handlers=[RichHandler()]
)

LOGGER = logging.getLogger('main')
LOGGER.setLevel(logging.DEBUG)
