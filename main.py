import asyncio

import uvicorn

from app import app
from configs import get_config
from services import scheduler as Scheduler


class Server(uvicorn.Server):
    def handle_exit(self, sig: int, frame) -> None:
        Scheduler.shutdown()
        return super().handle_exit(sig, frame)


async def main():
    server = Server(
        config=uvicorn.Config(
            app=app,
            host=get_config("HOST"),
            port=get_config("PORT"),
            workers=2,
            loop="asyncio"
        )
    )

    api = asyncio.create_task(server.serve())
    scheduler = asyncio.create_task(Scheduler.serve())

    await asyncio.wait([scheduler, api])

if __name__ == "__main__":
    asyncio.run(main())
