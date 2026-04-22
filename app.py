from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from client import aio
from Adafruit_IO.errors import RequestError

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/feeds/nhiet-do")
async def get_nhiet_do():
    try:
        data = aio.receive("nhiet-do")
        return {"feed": "nhiet-do", "value": data.value, "created_at": data.created_at}
    except RequestError as e:
        raise HTTPException(status_code=502, detail=str(e))


@app.get("/feeds/do-am")
async def get_do_am():
    try:
        data = aio.receive("do-am")
        return {"feed": "do-am", "value": data.value, "created_at": data.created_at}
    except RequestError as e:
        raise HTTPException(status_code=502, detail=str(e))


@app.get("/feeds/quat")
async def get_quat():
    try:
        data = aio.receive("quat")
        return {"feed": "quat", "value": data.value, "created_at": data.created_at}
    except RequestError as e:
        raise HTTPException(status_code=502, detail=str(e))


class FeedValue(BaseModel):
    value: str


@app.post("/feeds/quat")
async def set_quat(body: FeedValue):
    try:
        aio.send_data("quat", body.value)
        return {"feed": "quat", "value": body.value}
    except RequestError as e:
        raise HTTPException(status_code=502, detail=str(e))


@app.get("/feeds/den")
async def get_den():
    try:
        data = aio.receive("den")
        return {"feed": "den", "value": data.value, "created_at": data.created_at}
    except RequestError as e:
        raise HTTPException(status_code=502, detail=str(e))