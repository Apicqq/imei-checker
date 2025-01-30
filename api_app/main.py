from contextlib import asynccontextmanager

import aiohttp
from fastapi import FastAPI, Depends

from api_app.services import verify_imei
from api_app.schemas import ImeiIn, ImeiOut
from utils.http_client import HttpClient

http_client = HttpClient()


@asynccontextmanager
async def lifespan(_: FastAPI) -> None:
    """Lifespan of the app."""
    http_client.start()
    try:
        yield
    finally:
        await http_client.stop()


app = FastAPI(lifespan=lifespan, docs_url="/swagger")


@app.post("/api/check-imei")
async def check_imei(
    body: ImeiIn,
    session: aiohttp.ClientSession = Depends(http_client),
) -> ImeiOut:
    """Endpoint for IMEI verification via API."""
    return await verify_imei(body, session)
