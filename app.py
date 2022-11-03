from fastapi import FastAPI, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from mongoengine import connect as connect_mongo, disconnect as diconnect_mongo

from configs import get_config
from routes import HeartbeatRoute, UserRoute, EnviromentRoute
from services.logging import Logger

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def connect_thirdparties():
    MONGODB_URI = get_config("MONGODB_URI")
    connect_mongo(host=MONGODB_URI)
    Logger.info(f"[THIRD_PARITES]: MongoDB is connected | URI = {MONGODB_URI}")


@app.on_event("shutdown")
async def disconnect_thirdparties():
    diconnect_mongo()
    Logger.info("[THIRD_PARITES]: MongoDB is disconnected")


@app.exception_handler(Exception)
async def handle_exception(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder({"errors": exc}),
    )


@app.exception_handler(HTTPException)
async def handle_http_exception(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(exc.detail),
    )


async def handle_validation_exception(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"errors": exc.errors()}),
    )

app.include_router(HeartbeatRoute.router)
app.include_router(UserRoute.router)
app.include_router(EnviromentRoute.router)
