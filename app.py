from fastapi import FastAPI, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from mongoengine import connect as connect_mongo
from mongoengine import disconnect as diconnect_mongo

from configs import get_config
from routes import DeviceRoute, EnviromentRoute, HeartbeatRoute, UserRoute
from services.logging import LOGGER
from services.mqtt import MQTT
from services.model import init_knn_model

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
    MQTT_HOST = get_config("MQTT_HOST")
    MQTT_PORT = get_config("MQTT_PORT")
    MQTT_KEEPALIVE = get_config("MQTT_KEEPALIVE")
    TIME_ZONE = get_config("TZ")

    LOGGER.info(f"[TIME_ZONE]: Current time zone is {TIME_ZONE}")
    LOGGER.info(f"[KNN]: Init model")
    init_knn_model()

    LOGGER.info(f"[MongoDB]: Connecting to {MONGODB_URI}")
    connect_mongo(host=MONGODB_URI)

    LOGGER.info(f"[MQTT]: Connecting to {MQTT_HOST} on port {MQTT_PORT}")
    MQTT.connect_async(
        host=MQTT_HOST,
        port=MQTT_PORT,
        keepalive=MQTT_KEEPALIVE,
    )
    MQTT.loop_start()


@app.on_event("shutdown")
async def disconnect_thirdparties():
    diconnect_mongo()
    LOGGER.info("[MongoDB]: Disconnected")
    MQTT.disconnect()


@app.exception_handler(HTTPException)
async def handle_http_exception(request: Request, exception: HTTPException):
    return JSONResponse(
        status_code=exception.status_code,
        content=jsonable_encoder(exception.detail),
    )


@app.exception_handler(RequestValidationError)
async def handle_validation_exception(request: Request, error: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"errors": error.errors()}),
    )


@app.exception_handler(Exception)
async def handle_exception(request: Request, exception: Exception):
    LOGGER.error(f"[EXCEPTION]: Error when handling request | Reason: {exception.__str__()}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder({"message": exception.__str__()}),
    )


app.include_router(HeartbeatRoute.router)
app.include_router(UserRoute.router)
app.include_router(EnviromentRoute.router)
app.include_router(DeviceRoute.router)
