import uvicorn

from app import app
from configs import get_config

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=get_config("HOST"),
        port=get_config("PORT"),
    )
    