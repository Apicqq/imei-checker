from contextlib import asynccontextmanager

import aiohttp
from fastapi import FastAPI, Depends

from api_app.services import verify_imei
from api_app.schemas import ImeiIn
from utils.http_client import HttpClient

http_client = HttpClient()

@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    http_client.start()
    try:
        yield
    finally:
        await http_client.stop()


app = FastAPI(lifespan=lifespan, docs_url="/swagger")



@app.post("/api/check-imei")
async def check_imei(
        body: ImeiIn,
        session: aiohttp.ClientSession = Depends(http_client)
) -> dict:
    return await verify_imei(body, session)
